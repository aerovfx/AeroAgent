import os
import time
import json
import sqlite3
from datetime import datetime
from typing import Dict, Any

import pandas as pd
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from huggingface_hub import HfApi, hf_hub_download

# ==========================
# Load ENV
# ==========================
load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")
HF_DATASET = os.getenv("HF_DATASET")

if not HF_TOKEN or not HF_DATASET:
    raise ValueError("⚠️ Thiếu cấu hình trong .env. Hãy set HF_TOKEN và HF_DATASET.")

# ==========================
# Helpers
# ==========================
def now_iso():
    return datetime.utcnow().replace(microsecond=0).isoformat()

def parse_price(text: str) -> float:
    if not text:
        return None
    text = text.replace(".", "").replace(",", "").replace(" ", "").replace("₫", "")
    try:
        return float(text)
    except:
        return None

def create_driver(headless=True):
    options = Options()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# ==========================
# Adapters
# ==========================
def adapter_phuquy(driver) -> Dict[str, Any]:
    url = "https://phuquygroup.vn/giavang"
    driver.get(url)
    time.sleep(3)
    rows = driver.find_elements(By.CSS_SELECTOR, "table tr")
    buy = sell = None
    raw = []
    for tr in rows:
        cols = [c.text.strip() for c in tr.find_elements(By.TAG_NAME, "td")]
        if not cols or len(cols) < 3: 
            continue
        raw.append(cols)
        if "SJC" in cols[0] or "Vàng miếng" in cols[0]:
            buy = parse_price(cols[1]); sell = parse_price(cols[2]); break
    return {"source": "PhuQuy", "url": url, "buy": buy, "sell": sell, "unit": "VND", "timestamp": now_iso(), "raw": raw}

def adapter_sjc(driver) -> Dict[str, Any]:
    url = "https://sjc.com.vn/giavang"
    driver.get(url)
    time.sleep(3)
    rows = driver.find_elements(By.CSS_SELECTOR, "table tr")
    buy = sell = None
    raw = []
    for tr in rows:
        cols = [c.text.strip() for c in tr.find_elements(By.TAG_NAME, "td")]
        if not cols or len(cols) < 3: 
            continue
        raw.append(cols)
        if "SJC" in cols[0]:
            buy = parse_price(cols[1]); sell = parse_price(cols[2]); break
    return {"source": "SJC", "url": url, "buy": buy, "sell": sell, "unit": "VND", "timestamp": now_iso(), "raw": raw}

def adapter_btmc(driver) -> Dict[str, Any]:
    url = "https://btmc.vn/giavang"
    driver.get(url)
    time.sleep(3)
    rows = driver.find_elements(By.CSS_SELECTOR, "table tr")
    buy = sell = None
    raw = []
    for tr in rows:
        cols = [c.text.strip() for c in tr.find_elements(By.TAG_NAME, "td")]
        if not cols or len(cols) < 3: 
            continue
        raw.append(cols)
        if "SJC" in cols[0] or "Vàng Rồng" in cols[0]:
            buy = parse_price(cols[1]); sell = parse_price(cols[2]); break
    return {"source": "BTMC", "url": url, "buy": buy, "sell": sell, "unit": "VND", "timestamp": now_iso(), "raw": raw}

def adapter_doji(driver) -> Dict[str, Any]:
    url = "https://doji.vn/giavang"
    driver.get(url)
    time.sleep(3)
    rows = driver.find_elements(By.CSS_SELECTOR, "table tr")
    buy = sell = None
    raw = []
    for tr in rows:
        cols = [c.text.strip() for c in tr.find_elements(By.TAG_NAME, "td")]
        if not cols or len(cols) < 3: 
            continue
        raw.append(cols)
        if "SJC" in cols[0]:
            buy = parse_price(cols[1]); sell = parse_price(cols[2]); break
    return {"source": "DOJI", "url": url, "buy": buy, "sell": sell, "unit": "VND", "timestamp": now_iso(), "raw": raw}

def adapter_pnj(driver) -> Dict[str, Any]:
    url = "https://www.pnj.com.vn/giavang"
    driver.get(url)
    time.sleep(3)
    rows = driver.find_elements(By.CSS_SELECTOR, "table tr")
    buy = sell = None
    raw = []
    for tr in rows:
        cols = [c.text.strip() for c in tr.find_elements(By.TAG_NAME, "td")]
        if not cols or len(cols) < 3: 
            continue
        raw.append(cols)
        if "SJC" in cols[0]:
            buy = parse_price(cols[1]); sell = parse_price(cols[2]); break
    return {"source": "PNJ", "url": url, "buy": buy, "sell": sell, "unit": "VND", "timestamp": now_iso(), "raw": raw}

# ==========================
# Save to SQLite
# ==========================
def save_to_sqlite(data: Dict[str, Any], db_path="gold_data.db"):
    conn = sqlite3.connect(db_path)
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
    c.execute("""
        INSERT INTO gold_prices (source, url, buy, sell, unit, timestamp, raw)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        data["source"], data["url"], data["buy"], data["sell"], data["unit"], data["timestamp"],
        json.dumps(data["raw"], ensure_ascii=False),
    ))
    conn.commit(); conn.close()

# ==========================
# Push to HuggingFace (smart merge)
# ==========================
def push_to_huggingface(db_file="gold_data.db"):
    repo_id = HF_DATASET
    hf_token = HF_TOKEN
    api = HfApi()

    # Tạo repo nếu chưa có
    try:
        api.create_repo(repo_id=repo_id, repo_type="dataset", token=hf_token, exist_ok=True)
        print(f"✅ Repo sẵn sàng: {repo_id}")
    except Exception as e:
        print(f"⚠️ Không tạo được repo {repo_id}: {e}")

    # Load local data
    conn = sqlite3.connect(db_file)
    df_local = pd.read_sql("SELECT * FROM gold_prices", conn)
    conn.close()
    if df_local.empty:
        print("⚠️ Không có dữ liệu mới.")
        return

    # Try to download existing remote CSV
    try:
        remote_csv = hf_hub_download(
            repo_id=repo_id,
            filename="gold_prices.csv",
            repo_type="dataset",
            token=hf_token
        )
        df_remote = pd.read_csv(remote_csv)
    except Exception:
        df_remote = pd.DataFrame()

    # Merge + drop duplicates
    df_all = pd.concat([df_remote, df_local], ignore_index=True)
    df_all.drop_duplicates(subset=["source", "timestamp"], keep="last", inplace=True)

    # Save outputs
    out_csv = "gold_prices.csv"
    out_parquet = "gold_prices.parquet"
    df_all.to_csv(out_csv, index=False)
    df_all.to_parquet(out_parquet, index=False)

    # Upload files
    api.upload_file(
        path_or_fileobj=out_csv,
        path_in_repo="gold_prices.csv",
        repo_id=repo_id,
        repo_type="dataset",
        token=hf_token
    )
    api.upload_file(
        path_or_fileobj=out_parquet,
        path_in_repo="gold_prices.parquet",
        repo_id=repo_id,
        repo_type="dataset",
        token=hf_token
    )

    print(f"✅ Smart merged {len(df_local)} new rows -> {len(df_all)} total rows trên {repo_id}")
# ==========================
# Main
# ==========================
if __name__ == "__main__":
    driver = create_driver(headless=True)
    adapters = [adapter_phuquy, adapter_sjc, adapter_btmc, adapter_doji, adapter_pnj]

    for adapter in adapters:
        try:
            data = adapter(driver)
            print(json.dumps(data, ensure_ascii=False, indent=2))
            save_to_sqlite(data)
        except Exception as e:
            print(f"❌ Error in {adapter.__name__}: {e}")

    driver.quit()

    # Push lên HF
    push_to_huggingface("gold_data.db")