#!/usr/bin/env python3
# coding: utf-8
"""
Scraper CBRE Vietnam properties (multi-page, Playwright)
- Render trang với Playwright để vượt Cloudflare
- Parse HTML listings
- Chuẩn hóa schema (RESO-like)
- Xuất ra properties.jsonl
- Tùy chọn push lên Hugging Face
"""

import os
import json
import datetime
import random
import time
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
from huggingface_hub import HfApi, HfFolder, create_repo
from huggingface_hub.utils import RepositoryNotFoundError

# ---------------- Environment ----------------
load_dotenv()
ROOT_URL = "https://www.cbrevietnam.com/properties"
AGENCY = "CBRE Vietnam"
HF_DATASET_ID = os.getenv("HF_DATASET_ID", "your-username/properties-vietnam")
HF_TOKEN = os.getenv("HF_TOKEN")
MERGE_STRATEGY = os.getenv("MERGE_STRATEGY", "smart_merge")

if not HF_TOKEN:
    raise RuntimeError("Please set HF_TOKEN env variable with your Hugging Face token.")

# ---------------- Crawl function ----------------
def crawl_cbre(url):
    print(f"[crawl] fetching: {url}")
    properties = []

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=[
                '--no-sandbox',
                '--disable-setuid-sandbox',
                '--disable-infobars',
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

# ---------------- Main ----------------
def main():
    all_properties = []
    MAX_PAGES = 5  # điều chỉnh số trang muốn crawl

    for page_num in range(1, MAX_PAGES + 1):
        url = f"{ROOT_URL}?page={page_num}"
        props = crawl_cbre(url)
        all_properties.extend(props)
        time.sleep(random.uniform(1, 3))

    # Export JSONL
    out_file = "properties.jsonl"
    with open(out_file, "w", encoding="utf-8") as f:
        for item in all_properties:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
    print(f"[main] saved {len(all_properties)} items to {out_file}")

    # Optional: push to Hugging Face
    if HF_DATASET_ID:
        api = HfApi()
        try:
            create_repo(HF_TOKEN, HF_DATASET_ID, exist_ok=True)
        except RepositoryNotFoundError:
            print(f"[HF] Repository {HF_DATASET_ID} not found, creating new repo.")
        api.upload_file(
            path_or_fileobj=out_file,
            path_in_repo="properties.jsonl",
            repo_id=HF_DATASET_ID,
            token=HF_TOKEN,
            repo_type="dataset"
        )
        print(f"[HF] Uploaded to Hugging Face dataset: {HF_DATASET_ID}")

if __name__ == "__main__":
    main()