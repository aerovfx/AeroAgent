#!/usr/bin/env python3
# coding: utf-8
"""
Scraper CBRE Vietnam properties (sync version, no stealth)
- Render trang với Playwright
- Parse HTML listings
- Chuẩn hóa schema (RESO-like)
- Xuất ra properties_vietnam.json
- Push lên Hugging Face
"""

import os
import json
import datetime
import random
import time
from bs4 import BeautifulSoup
from huggingface_hub import HfApi, HfFolder, create_repo
from huggingface_hub.errors import RepositoryNotFoundError
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

# ---------------- Environment ----------------
load_dotenv()
ROOT_URL = "https://batdongsan.com.vn"
AGENCY = "CBRE Vietnam"
HF_DATASET_ID = os.getenv("HF_DATASET_ID", "your-username/properties-vietnam")
HF_TOKEN = os.getenv("HF_TOKEN")
MERGE_STRATEGY = os.getenv("MERGE_STRATEGY", "smart_merge")

if not HF_TOKEN:
    raise RuntimeError("Please set HF_TOKEN env variable with your Hugging Face token.")

# ---------------- STEP 1: Crawl CBRE ----------------
def crawl_cbre(url=ROOT_URL):
    print(f"[crawl] fetching from: {url}")
    properties = []

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,  # Nếu site yêu cầu CAPTCHA, thử headless=False
            args=[
                '--no-sandbox',
                '--disable-setuid-sandbox',
                '--disable-infobars',
                '--window-position=0,0',
                '--ignore-certificate-errors',
            ]
        )
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            screen={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            locale='en-US',
            timezone_id='Asia/Bangkok'
        )
        page = context.new_page()
        try:
            page.goto(url, timeout=90000, wait_until="domcontentloaded")
            page.wait_for_selector(".property-list .property-item", timeout=60000)
            try:
                page.wait_for_load_state("networkidle", timeout=30000)
            except:
                print("[crawl] Network idle timeout, proceeding anyway")
            
            time.sleep(random.uniform(2, 5))
            html = page.content()
        except Exception as e:
            print(f"[crawl] Error during page load: {e}")
            browser.close()
            return []
        finally:
            browser.close()

    soup = BeautifulSoup(html, "html.parser")
    for idx, item in enumerate(soup.select(".property-list .property-item"), 1):
        title = item.select_one(".property-title")
        location = item.select_one(".property-location")
        price = item.select_one(".property-price")
        now = datetime.datetime.utcnow().strftime("%Y-%m-%d")
        properties.append({
            "PropertyID": f"VN-CBRE-{idx}",
            "Title": title.get_text(strip=True) if title else "N/A",
            "PropertyType": "Unknown",
            "TransactionType": "For Sale",
            "Price": {
                "Value": price.get_text(strip=True) if price else "Contact",
                "Currency": "USD",
                "Unit": None
            },
            "LotSize": None,
            "Location": {
                "Country": "Vietnam",
                "Province": location.get_text(strip=True) if location else "N/A",
            },
            "Source": {
                "ListingURL": url,
                "Agency": AGENCY,
                "LastUpdated": now
            }
        })
    print(f"[crawl] discovered {len(properties)} properties")
    return properties

# ---------------- STEP 2: Merge strategy ----------------
def merge_datasets(api, dataset_id, new_props, token, strategy="append"):
    try:
        files = api.list_repo_files(dataset_id, repo_type="dataset", token=token)
        if "data/properties_vietnam.json" in files:
            existing = api.hf_hub_download(
                repo_id=dataset_id,
                repo_type="dataset",
                filename="data/properties_vietnam.json",
                token=token
            )
            with open(existing, "r", encoding="utf-8") as f:
                old_data = json.load(f)
        else:
            old_data = {"properties": []}
    except RepositoryNotFoundError:
        print(f"[merge] dataset {dataset_id} not found → creating new.")
        create_repo(dataset_id, repo_type="dataset", private=False, exist_ok=True, token=token)
        old_data = {"properties": []}

    if strategy == "replace":
        merged = {"properties": new_props}
    elif strategy == "append":
        merged = {"properties": old_data["properties"] + new_props}
    elif strategy == "smart_merge":
        old_map = {p["PropertyID"]: p for p in old_data["properties"]}
        for p in new_props:
            old_map[p["PropertyID"]] = p
        merged = {"properties": list(old_map.values())}
    else:
        raise ValueError("Invalid merge strategy")
    return merged

# ---------------- STEP 3: Main ----------------
def main():
    properties = crawl_cbre()
    api = HfApi()
    merged = merge_datasets(api, HF_DATASET_ID, properties, HF_TOKEN, strategy=MERGE_STRATEGY)

    with open("properties_vietnam.json", "w", encoding="utf-8") as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)
    print("[main] saved properties_vietnam.json")

    print(f"[main] pushing to Hugging Face: {HF_DATASET_ID}")
    HfFolder.save_token(HF_TOKEN)
    api.upload_file(
        path_or_fileobj="properties_vietnam.json",
        path_in_repo="data/properties_vietnam.json",
        repo_id=HF_DATASET_ID,
        repo_type="dataset",
        token=HF_TOKEN,
    )
    print("[main] upload complete.")

if __name__ == "__main__":
    main()