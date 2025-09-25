import os
import time
import json
import sqlite3
import requests
from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional
import re

import pandas as pd
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

def parse_date(date_str: str, format_hint: str = None) -> Optional[str]:
    """Parse date string to ISO format"""
    if not date_str:
        return None
    
    formats = [
        "%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y", "%d-%m-%Y",
        "%Y/%m/%d", "%d.%m.%Y", "%Y.%m.%d", "%b %d, %Y",
        "%d %b %Y", "%Y-%m-%d %H:%M:%S"
    ]
    
    if format_hint:
        formats.insert(0, format_hint)
    
    for fmt in formats:
        try:
            return datetime.strptime(date_str.strip(), fmt).strftime("%Y-%m-%d")
        except:
            continue
    return None

def parse_price(text: str) -> Optional[float]:
    if not text:
        return None
    
    # Remove currency symbols and separators
    text = re.sub(r'[₫$,.\s]', '', text)
    text = re.sub(r'[^\d]', '', text)
    
    try:
        return float(text) if text else None
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
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# ==========================
# Time-Series Adapters
# ==========================

class TimeSeriesAdapter:
    def __init__(self, source_name: str):
        self.source_name = source_name
    
    def get_historical_data(self, start_date: str, end_date: str) -> List[Dict[str, Any]]:
        """Override this method in subclasses"""
        raise NotImplementedError

def adapter_kitco_historical(start_date: str, end_date: str) -> List[Dict[str, Any]]:
    """Kitco gold price API - International source"""
    results = []
    try:
        # Kitco API endpoint (may need API key for full access)
        base_url = "https://www.kitco.com/gold-price-history"
        
        # For demo, using a mock structure - replace with actual API calls
        current_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_dt = datetime.strptime(end_date, "%Y-%m-%d")
        
        while current_date <= end_dt:
            # Mock data - replace with actual API call
            data = {
                "date": current_date.strftime("%Y-%m-%d"),
                "source": "Kitco",
                "buy": None,  # Kitco mainly shows spot prices
                "sell": None,
                "spot_price": 2000.0 + (current_date.day * 10),  # Mock data
                "unit": "USD",
                "timestamp": now_iso(),
                "raw": {"mock": True}
            }
            results.append(data)
            current_date += timedelta(days=1)
            
    except Exception as e:
        print(f"❌ Error in Kitco adapter: {e}")
    
    return results

def adapter_cafef_historical(driver, start_date: str, end_date: str) -> List[Dict[str, Any]]:
    """CafeF historical gold prices"""
    results = []
    try:
        url = "https://cafef.vn/gia-vang.chn"
        driver.get(url)
        time.sleep(3)
        
        # Look for historical data section
        wait = WebDriverWait(driver, 10)
        
        # Try to find historical data table or chart data
        tables = driver.find_elements(By.CSS_SELECTOR, "table.CafeF_TableFormList")
        
        for table in tables:
            rows = table.find_elements(By.TAG_NAME, "tr")
            for row in rows[1:]:  # Skip header
                cells = row.find_elements(By.TAG_NAME, "td")
                if len(cells) >= 4:
                    date_text = cells[0].text.strip()
                    parsed_date = parse_date(date_text)
                    
                    if parsed_date and start_date <= parsed_date <= end_date:
                        buy_price = parse_price(cells[1].text)
                        sell_price = parse_price(cells[2].text)
                        
                        data = {
                            "date": parsed_date,
                            "source": "CafeF",
                            "buy": buy_price,
                            "sell": sell_price,
                            "unit": "VND",
                            "timestamp": now_iso(),
                            "raw": [cell.text for cell in cells]
                        }
                        results.append(data)
                        
    except Exception as e:
        print(f"❌ Error in CafeF adapter: {e}")
    
    return results

def adapter_vietstock_historical(driver, start_date: str, end_date: str) -> List[Dict[str, Any]]:
    """Vietstock historical gold prices"""
    results = []
    try:
        url = "https://vietstock.vn/gia-vang"
        driver.get(url)
        time.sleep(3)
        
        # Find historical data section
        historical_section = driver.find_elements(By.CSS_SELECTOR, ".price-history, .historical-data")
        
        if historical_section:
            tables = historical_section[0].find_elements(By.TAG_NAME, "table")
            for table in tables:
                rows = table.find_elements(By.TAG_NAME, "tr")
                for row in rows[1:]:  # Skip header
                    cells = row.find_elements(By.TAG_NAME, "td")
                    if len(cells) >= 3:
                        date_text = cells[0].text.strip()
                        parsed_date = parse_date(date_text)
                        
                        if parsed_date and start_date <= parsed_date <= end_date:
                            buy_price = parse_price(cells[1].text)
                            sell_price = parse_price(cells[2].text)
                            
                            data = {
                                "date": parsed_date,
                                "source": "Vietstock",
                                "buy": buy_price,
                                "sell": sell_price,
                                "unit": "VND",
                                "timestamp": now_iso(),
                                "raw": [cell.text for cell in cells]
                            }
                            results.append(data)
                            
    except Exception as e:
        print(f"❌ Error in Vietstock adapter: {e}")
    
    return results

def adapter_tradingview_api(symbol: str = "GOLD", start_date: str = None, end_date: str = None) -> List[Dict[str, Any]]:
    """TradingView API adapter (requires authentication for full access)"""
    results = []
    try:
        # TradingView API endpoint (simplified - actual implementation needs authentication)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json'
        }
        
        # For demo purposes - replace with actual TradingView API calls
        # url = f"https://api.tradingview.com/v1/symbols/{symbol}/history"
        
        # Mock implementation - replace with real API
        current_date = datetime.strptime(start_date or "2023-01-01", "%Y-%m-%d")
        end_dt = datetime.strptime(end_date or datetime.now().strftime("%Y-%m-%d"), "%Y-%m-%d")
        
        while current_date <= end_dt:
            data = {
                "date": current_date.strftime("%Y-%m-%d"),
                "source": "TradingView",
                "buy": None,
                "sell": None,
                "open": 1950.0 + (current_date.day * 5),
                "high": 1970.0 + (current_date.day * 5),
                "low": 1930.0 + (current_date.day * 5),
                "close": 1960.0 + (current_date.day * 5),
                "unit": "USD",
                "timestamp": now_iso(),
                "raw": {"mock": True}
            }
            results.append(data)
            current_date += timedelta(days=1)
            
    except Exception as e:
        print(f"❌ Error in TradingView adapter: {e}")
    
    return results

def adapter_vietcombank_historical(driver, start_date: str, end_date: str) -> List[Dict[str, Any]]:
    """Vietcombank historical exchange rates (for reference)"""
    results = []
    try:
        url = "https://portal.vietcombank.com.vn/Personal/TG/TyGia/Pages/default.aspx"
        driver.get(url)
        time.sleep(5)
        
        # Look for historical data or downloadable files
        # VCB might have CSV export functionality
        download_links = driver.find_elements(By.PARTIAL_LINK_TEXT, "Tải về")
        
        for link in download_links:
            href = link.get_attribute("href")
            if "csv" in href.lower() or "excel" in href.lower():
                # Download and process the file
                print(f"Found downloadable file: {href}")
                # Implementation would download and parse CSV/Excel
                
    except Exception as e:
        print(f"❌ Error in Vietcombank adapter: {e}")
    
    return results

# ==========================
# Enhanced Database Schema
# ==========================
def init_timeseries_db(db_path="gold_timeseries.db"):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    
    c.execute("""
        CREATE TABLE IF NOT EXISTS gold_timeseries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            source TEXT NOT NULL,
            buy REAL,
            sell REAL,
            open REAL,
            high REAL,
            low REAL,
            close REAL,
            spot_price REAL,
            unit TEXT,
            timestamp TEXT,
            raw TEXT,
            UNIQUE(date, source)
        )
    """)
    
    # Create indexes for better performance
    c.execute("CREATE INDEX IF NOT EXISTS idx_date ON gold_timeseries(date)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_source ON gold_timeseries(source)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_date_source ON gold_timeseries(date, source)")
    
    conn.commit()
    conn.close()

def save_timeseries_data(data_list: List[Dict[str, Any]], db_path="gold_timeseries.db"):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    
    for data in data_list:
        try:
            c.execute("""
                INSERT OR REPLACE INTO gold_timeseries 
                (date, source, buy, sell, open, high, low, close, spot_price, unit, timestamp, raw)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                data.get("date"),
                data.get("source"),
                data.get("buy"),
                data.get("sell"),
                data.get("open"),
                data.get("high"),
                data.get("low"),
                data.get("close"),
                data.get("spot_price"),
                data.get("unit"),
                data.get("timestamp"),
                json.dumps(data.get("raw", {}), ensure_ascii=False)
            ))
        except Exception as e:
            print(f"❌ Error saving data: {e}")
    
    conn.commit()
    conn.close()

# ==========================
# Data Export Functions
# ==========================
def export_to_formats(db_path="gold_timeseries.db"):
    """Export data to CSV and Parquet formats"""
    conn = sqlite3.connect(db_path)
    df = pd.read_sql("SELECT * FROM gold_timeseries ORDER BY date, source", conn)
    conn.close()
    
    if not df.empty:
        # Export to different formats
        df.to_csv("gold_timeseries.csv", index=False)
        df.to_parquet("gold_timeseries.parquet", index=False)
        
        # Create summary statistics
        summary = df.groupby(['source', df['date'].str[:7]]).agg({
            'buy': ['mean', 'min', 'max'],
            'sell': ['mean', 'min', 'max'],
            'spot_price': ['mean', 'min', 'max']
        }).round(2)
        
        summary.to_csv("gold_price_summary.csv")
        
        print(f"✅ Exported {len(df)} records to CSV/Parquet")
        return df
    else:
        print("⚠️ No data to export")
        return pd.DataFrame()

# ==========================
# Enhanced HuggingFace Push
# ==========================
def push_timeseries_to_huggingface(db_file="gold_timeseries.db"):
    repo_id = HF_DATASET
    hf_token = HF_TOKEN
    api = HfApi()

    # Create repo if not exists
    try:
        api.create_repo(repo_id=repo_id, repo_type="dataset", token=hf_token, exist_ok=True)
        print(f"✅ Repo ready: {repo_id}")
    except Exception as e:
        print(f"⚠️ Could not create repo {repo_id}: {e}")

    # Export current data
    df_local = export_to_formats(db_file)
    if df_local.empty:
        return

    # Try to download existing remote data
    try:
        remote_csv = hf_hub_download(
            repo_id=repo_id,
            filename="gold_timeseries.csv",
            repo_type="dataset",
            token=hf_token
        )
        df_remote = pd.read_csv(remote_csv)
    except Exception:
        df_remote = pd.DataFrame()

    # Smart merge
    df_all = pd.concat([df_remote, df_local], ignore_index=True)
    df_all.drop_duplicates(subset=["date", "source"], keep="last", inplace=True)
    df_all = df_all.sort_values(['date', 'source'])

    # Save final outputs
    files_to_upload = [
        "gold_timeseries.csv",
        "gold_timeseries.parquet", 
        "gold_price_summary.csv"
    ]
    
    # Re-export with merged data
    df_all.to_csv("gold_timeseries.csv", index=False)
    df_all.to_parquet("gold_timeseries.parquet", index=False)

    # Upload all files
    for filename in files_to_upload:
        if os.path.exists(filename):
            api.upload_file(
                path_or_fileobj=filename,
                path_in_repo=filename,
                repo_id=repo_id,
                repo_type="dataset",
                token=hf_token
            )

    print(f"✅ Uploaded {len(df_all)} total records to {repo_id}")

# ==========================
# Main Orchestration
# ==========================
def collect_historical_data(start_date: str, end_date: str, sources: List[str] = None):
    """Main function to collect historical data from multiple sources"""
    
    if sources is None:
        sources = ["kitco", "cafef", "vietstock", "tradingview"]
    
    # Initialize database
    init_timeseries_db()
    
    # Create driver for web scraping
    driver = None
    if any(src in sources for src in ["cafef", "vietstock", "vietcombank"]):
        driver = create_driver(headless=True)
    
    try:
        all_data = []
        
        # Collect from different sources
        if "kitco" in sources:
            print("📊 Collecting from Kitco...")
            kitco_data = adapter_kitco_historical(start_date, end_date)
            all_data.extend(kitco_data)
            
        if "cafef" in sources and driver:
            print("📊 Collecting from CafeF...")
            cafef_data = adapter_cafef_historical(driver, start_date, end_date)
            all_data.extend(cafef_data)
            
        if "vietstock" in sources and driver:
            print("📊 Collecting from Vietstock...")
            vietstock_data = adapter_vietstock_historical(driver, start_date, end_date)
            all_data.extend(vietstock_data)
            
        if "tradingview" in sources:
            print("📊 Collecting from TradingView...")
            tv_data = adapter_tradingview_api("GOLD", start_date, end_date)
            all_data.extend(tv_data)
            
        if "vietcombank" in sources and driver:
            print("📊 Collecting from Vietcombank...")
            vcb_data = adapter_vietcombank_historical(driver, start_date, end_date)
            all_data.extend(vcb_data)
        
        # Save all collected data
        if all_data:
            save_timeseries_data(all_data)
            print(f"✅ Collected {len(all_data)} historical records")
            
            # Export and push to HuggingFace
            push_timeseries_to_huggingface()
        else:
            print("⚠️ No historical data collected")
            
    finally:
        if driver:
            driver.quit()

# ==========================
# CLI Interface
# ==========================
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Gold Price Time-Series Collector")
    parser.add_argument("--start-date", default="2023-01-01", help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end-date", default=datetime.now().strftime("%Y-%m-%d"), help="End date (YYYY-MM-DD)")
    parser.add_argument("--sources", nargs="+", default=["kitco", "tradingview"], 
                       help="Sources to collect from", 
                       choices=["kitco", "cafef", "vietstock", "tradingview", "vietcombank"])
    parser.add_argument("--export-only", action="store_true", help="Only export existing data")
    
    args = parser.parse_args()
    
    if args.export_only:
        push_timeseries_to_huggingface()
    else:
        collect_historical_data(args.start_date, args.end_date, args.sources)