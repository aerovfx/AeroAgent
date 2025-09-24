#!/usr/bin/env python3
# coding: utf-8
"""
Async scraper CBRE Vietnam properties (multi-page, parallel)
- Dùng Playwright async để crawl nhiều page nhanh
- Parse HTML listings
- Xuất JSONL
- Push lên Hugging Face
"""

import os
import json
import datetime
import asyncio
import random
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from playwright.async_api import async_playwright
from huggingface_hub import HfApi, create_repo

# ---------------- Environment ----------------
load_dotenv()
ROOT_URL = "https://www.cbrevietnam.com/properties"
AGENCY = "CBRE Vietnam"
HF_DATASET_ID = os.getenv("HF_DATASET_ID", "your-username/properties-vietnam")
HF_TOKEN = os.getenv("HF_TOKEN")
MERGE_STRATEGY = os.getenv("MERGE_STRATEGY", "smart_merge")

if not HF_TOKEN:
    raise RuntimeError("Please set HF_TOKEN env variable with your Hugging Face token.")

# ---------------- Async crawl ----------------
async def crawl_page(page_num):
    url = f"{ROOT_URL}?page={page_num}"
    print(f"[crawl] fetching: {url}")
    properties = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            screen={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            locale='en-US',
            timezone_id='Asia/Bangkok'
        )
        page = await context.new_page()
        try:
            await page.goto(url, timeout=90000, wait_until="domcontentloaded")
            await page.wait_for_selector(".property-list .property-item", timeout=60000)
            try:
                await page.wait_for_load_state("networkidle", timeout=30000)
            except:
                print("[crawl] Network idle timeout, proceeding anyway")
            await asyncio.sleep(random.uniform(2, 5))
            html = await page.content()
        except Exception as e:
            print(f"[crawl] Error page {page_num}: {e}")
            await browser.close()
            return []
        finally:
            await browser.close()

    soup = BeautifulSoup(html, "html.parser")
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    for idx, item in enumerate(soup.select(".property-list .property-item"), 1):
        title = item.select_one(".property-title")
        location = item.select_one(".property-location")
        price = item.select_one(".property-price")
        properties.append({
            "PropertyID": f"VN-CBRE-{page_num}-{idx}",
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
    print(f"[crawl] page {page_num}: found {len(properties)} properties")
    return properties

# ---------------- Main async ----------------
async def main():
    MAX_PAGES = 10  # số trang muốn crawl
    tasks = [crawl_page(i) for i in range(1, MAX_PAGES + 1)]
    results = await asyncio.gather(*tasks)

    all_properties = [item for sublist in results for item in sublist]

    # Export JSONL
    out_file = "properties.jsonl"
    with open(out_file, "w", encoding="utf-8") as f:
        for item in all_properties:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
    print(f"[main] saved {len(all_properties)} items to {out_file}")

    # Optional: push to Hugging Face
    if HF_DATASET_ID:
        api = HfApi()
        create_repo(HF_TOKEN, HF_DATASET_ID, exist_ok=True)
        api.upload_file(
            path_or_fileobj=out_file,
            path_in_repo="properties.jsonl",
            repo_id=HF_DATASET_ID,
            token=HF_TOKEN,
            repo_type="dataset"
        )
        print(f"[HF] Uploaded to Hugging Face dataset: {HF_DATASET_ID}")

if __name__ == "__main__":
    asyncio.run(main())