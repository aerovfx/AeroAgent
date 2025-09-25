#!/usr/bin/env python3
# coding: utf-8
"""
gold_scraper.py
Full, runnable scraper for Vietnamese gold price pages (template + real adapters).
- Adapters included: PhuQuy (banggia.phuquygroup.vn), DOJI (webgia.com/gia-vang/doji),
  SJC Cần Thơ (sjccantho.vn/gia-vang) as example.
- Saves to SQLite 'gold_data.db' table 'gold_prices'.
- Usage:
    python3 gold_scraper.py             # run all adapters
    python3 gold_scraper.py --adapter PhuQuy
    python3 gold_scraper.py --init-sample  # insert sample rows for testing
Requirements:
    pip install requests beautifulsoup4 lxml pandas
"""

import requests
from bs4 import BeautifulSoup
import sqlite3
import json
import time
import re
import argparse
from datetime import datetime
from typing import Optional, Dict, Any, List
from requests.adapters import HTTPAdapter, Retry

DB_FILE = "gold_data.db"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

# ----------------------
# Utilities
# ----------------------
def create_session(retries: int = 3, backoff_factor: float = 0.3) -> requests.Session:
    s = requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=frozenset(["GET", "POST"])
    )
    s.mount("https://", HTTPAdapter(max_retries=retry))
    s.mount("http://", HTTPAdapter(max_retries=retry))
    s.headers.update(HEADERS)
    return s

def now_iso() -> str:
    return datetime.now().isoformat()

def parse_price(text: Optional[str]) -> Optional[float]:
    """
    Normalize Vietnamese price strings into float VND.
    Handles formats like:
      - "65.200.000 đ", "65,200,000", "65.2 triệu", "65.2tr"
      - returns float in VND (not per chỉ conversion)
    """
    if text is None:
        return None
    t = str(text).strip().lower()
    if t == "":
        return None
    # replace non-breaking spaces
    t = t.replace('\xa0', ' ')
    # handle "triệu" or "tr" -> millions
    m_mil = re.search(r'([0-9]+[\.,]?[0-9]*)\s*(triệu|triệu|tr|tr\.)\b', t)
    if m_mil:
        # m_mil.group(1) could be "65.2" => 65.2 triệu
        base = m_mil.group(1).replace(',', '.')
        try:
            return float(base) * 1_000_000.0
        except:
            pass
    # extract first large digit group
    m = re.search(r'([0-9][0-9\.,\s]+[0-9])', t)
    if not m:
        # maybe a plain number like "74200000"
        m2 = re.search(r'([0-9]{6,})', t)
        if m2:
            try:
                return float(m2.group(1))
            except:
                return None
        return None
    s = m.group(1)
    # remove spaces and thousands separators
    s_clean = s.replace(' ', '').replace(',', '').replace('.', '')
    try:
        return float(s_clean)
    except:
        return None

def safe_get_text(el) -> Optional[str]:
    if el is None:
        return None
    try:
        return el.get_text(" ", strip=True)
    except:
        return str(el)

# ----------------------
# Adapters (realistic)
# ----------------------
# NOTE: selectors may require adjustments over time. Use DevTools to update.
def adapter_phuquy(session: requests.Session) -> Dict[str, Any]:
    """
    Parse banggia.phuquygroup.vn (Phú Quý group price board).
    """
    url = "https://banggia.phuquygroup.vn/"
    resp = session.get(url, timeout=15)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "lxml")

    buy = sell = None
    raw = {}

    # Try: find table headers to locate columns
    table = soup.select_one("table")
    if table:
        # get header names
        headers = [th.get_text(" ", strip=True).lower() for th in table.select("thead th")]
        body_rows = table.select("tbody tr")
        buy_idx = sell_idx = None
        for i, h in enumerate(headers):
            if "mua" in h:
                buy_idx = i
            if "bán" in h or "ban" in h:
                sell_idx = i
        # find row containing 'sjc'
        for tr in body_rows:
            cols = [td.get_text(" ", strip=True) for td in tr.select("td")]
            if not cols:
                continue
            typ = cols[0].lower()
            if "sjc" in typ:
                raw["cols"] = cols
                if buy_idx is not None and buy_idx < len(cols):
                    buy = parse_price(cols[buy_idx])
                if sell_idx is not None and sell_idx < len(cols):
                    sell = parse_price(cols[sell_idx])
                break

    # fallback: search for text occurrences mentioning "SJC"
    if buy is None and sell is None:
        for el in soup.find_all(string=re.compile(r'sjc', re.I)):
            parent = el.find_parent("tr")
            if parent:
                cols = [td.get_text(" ", strip=True) for td in parent.select("td")]
                raw["fallback"] = cols
                if len(cols) >= 3:
                    buy = parse_price(cols[1])
                    sell = parse_price(cols[2])
                break

    return {
        "source": "PhuQuy",
        "url": url,
        "buy": buy,
        "sell": sell,
        "unit": "VND",
        "timestamp": now_iso(),
        "raw": raw
    }

def adapter_doji_webgia(session: requests.Session) -> Dict[str, Any]:
    """
    Parse DOJI prices from webgia.com/gia-vang/doji/
    (webgia often aggregates many brands - we look for SJC row)
    """
    url = "https://webgia.com/gia-vang/doji/"
    resp = session.get(url, timeout=15)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "lxml")

    buy = sell = None
    raw = {}

    # Try to locate table rows; look for "SJC" or "SJC Lẻ"
    for tr in soup.select("table tr"):
        text = tr.get_text(" ", strip=True).lower()
        if "sjc lẻ" in text or text.startswith("sjc") or "sjc" in text.split():
            cols = [td.get_text(" ", strip=True) for td in tr.select("td")]
            raw["cols"] = cols
            if len(cols) >= 3:
                # many aggregated tables: assume col1 type, col2 buy, col3 sell
                buy = parse_price(cols[1])
                sell = parse_price(cols[2])
            break

    # fallback: try rows containing 'mua' and 'bán'
    if buy is None and sell is None:
        for tr in soup.select("tr"):
            txt = tr.get_text(" ", strip=True).lower()
            if "mua" in txt and "bán" in txt and "sjc" in txt:
                cols = [td.get_text(" ", strip=True) for td in tr.select("td")]
                raw["fallback2"] = cols
                if len(cols) >= 3:
                    buy = parse_price(cols[1])
                    sell = parse_price(cols[2])
                break

    return {
        "source": "DOJI-webgia",
        "url": url,
        "buy": buy,
        "sell": sell,
        "unit": "VND",
        "timestamp": now_iso(),
        "raw": raw
    }

def adapter_sjc_cantho(session: requests.Session) -> Dict[str, Any]:
    """
    Example adapter for SJC Cần Thơ branch (sjccantho.vn/gia-vang).
    Many SJC branches have similar table layout; update URL if needed.
    """
    url = "https://sjccantho.vn/gia-vang"
    resp = session.get(url, timeout=15)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "lxml")

    buy = sell = None
    raw = {}

    # Look for rows that likely contain 'SJC' or 'SJCCT' names
    for tr in soup.select("table tr"):
        text = tr.get_text(" ", strip=True).lower()
        if any(k in text for k in ("sjc", "sjcct", "sjc ct")):
            cols = [td.get_text(" ", strip=True) for td in tr.select("td")]
            raw["cols"] = cols
            # assume cols like: [name, buy, sell, ...]
            if len(cols) >= 3:
                buy = parse_price(cols[1])
                sell = parse_price(cols[2])
            break

    # If still nothing, search for "mua" and "bán" occurrences
    if buy is None and sell is None:
        for el in soup.find_all(string=re.compile(r'mua', re.I)):
            tr = el.find_parent("tr")
            if tr:
                cols = [td.get_text(" ", strip=True) for td in tr.select("td")]
                raw["mua_row"] = cols
                if len(cols) >= 3:
                    buy = parse_price(cols[1])
                    sell = parse_price(cols[2])
                break

    return {
        "source": "SJC-CanTho",
        "url": url,
        "buy": buy,
        "sell": sell,
        "unit": "VND",
        "timestamp": now_iso(),
        "raw": raw
    }

ADAPTER_MAP = {
    "PhuQuy": adapter_phuquy,
    "DOJI-webgia": adapter_doji_webgia,
    "SJC-CanTho": adapter_sjc_cantho,
}

# ----------------------
# Database helpers
# ----------------------
def init_db(db_file: str = DB_FILE):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS gold_prices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source TEXT,
        url TEXT,
        buy REAL,
        sell REAL,
        unit TEXT,
        timestamp TEXT,
        raw TEXT
    )
    """)
    conn.commit()
    conn.close()

def save_to_db(rows: List[Dict[str, Any]], db_file: str = DB_FILE):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    for r in rows:
        # ensure buy/sell are numeric or None
        buy = float(r["buy"]) if r.get("buy") is not None else None
        sell = float(r["sell"]) if r.get("sell") is not None else None
        c.execute("""
        INSERT INTO gold_prices (source, url, buy, sell, unit, timestamp, raw)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            r.get("source"),
            r.get("url"),
            buy,
            sell,
            r.get("unit"),
            r.get("timestamp"),
            json.dumps(r.get("raw", {}), ensure_ascii=False)
        ))
    conn.commit()
    conn.close()

# ----------------------
# Runner
# ----------------------
def run_adapters(names: Optional[List[str]] = None) -> List[Dict[str, Any]]:
    session = create_session()
    results = []
    target = names if names else list(ADAPTER_MAP.keys())
    for name in target:
        adapter = ADAPTER_MAP.get(name)
        if adapter is None:
            print(f"[WARN] Unknown adapter: {name}")
            continue
        print(f"[INFO] Running adapter: {name}")
        try:
            r = adapter(session)
            # Log raw parse for debugging
            print(f"  -> {name} parsed buy={r.get('buy')} sell={r.get('sell')} timestamp={r.get('timestamp')}")
            if r.get("raw"):
                # print small raw sample (truncate)
                try:
                    raw_s = json.dumps(r["raw"], ensure_ascii=False)
                    print("     raw:", raw_s[:400])
                except:
                    print("     raw: (unserializable)")
            results.append(r)
            time.sleep(1.0)
        except Exception as e:
            print(f"[ERROR] Adapter {name} failed: {e}")
            results.append({
                "source": name,
                "url": None,
                "buy": None,
                "sell": None,
                "unit": "VND",
                "timestamp": now_iso(),
                "raw": {"error": str(e)}
            })
    return results

# ----------------------
# Test / sample data helper
# ----------------------
def insert_sample_data(db_file: str = DB_FILE, n: int = 20):
    """
    Insert synthetic sample time-series for testing (SJC).
    """
    import random, datetime
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    for i in range(n):
        ts = (datetime.datetime.now() - datetime.timedelta(hours=i)).isoformat()
        base = 74000000 + random.randint(-800000, 800000)
        buy = base
        sell = base + random.randint(100000, 400000)
        raw = {"sample": True}
        c.execute("""
        INSERT INTO gold_prices (source, url, buy, sell, unit, timestamp, raw)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, ("SJC-sample", "local", buy, sell, "VND", ts, json.dumps(raw, ensure_ascii=False)))
    conn.commit()
    conn.close()
    print(f"[INFO] Inserted {n} sample rows into {db_file}")

# ----------------------
# CLI
# ----------------------
def main():
    parser = argparse.ArgumentParser(description="Gold price scraper (Vietnam) - run adapters and save to SQLite")
    parser.add_argument("--adapter", "-a", help="Run single adapter by name (PhuQuy, DOJI-webgia, SJC-CanTho)", default=None)
    parser.add_argument("--init-db", action="store_true", help="Create DB and table if not exists")
    parser.add_argument("--init-sample", action="store_true", help="Insert sample rows for testing")
    args = parser.parse_args()

    if args.init_db:
        init_db()
        print("[INFO] DB initialized.")

    if args.init_sample:
        init_db()
        insert_sample_data()

    if args.adapter:
        if args.adapter not in ADAPTER_MAP:
            print(f"[ERROR] Unknown adapter name: {args.adapter}. Known: {list(ADAPTER_MAP.keys())}")
            return
        init_db()
        session_results = run_adapters([args.adapter])
        save_to_db(session_results)
        print(f"[INFO] Saved {len(session_results)} rows to {DB_FILE}")
    else:
        # run all adapters
        init_db()
        session_results = run_adapters()
        save_to_db(session_results)
        print(f"[INFO] Saved {len(session_results)} rows to {DB_FILE}")

if __name__ == "__main__":
    main()