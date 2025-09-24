#!/usr/bin/env python3
# coding: utf-8
"""
Scraper CBRE Vietnam properties
- Render trang với Playwright (bypass bot)
- Parse HTML listings
- Chuẩn hóa schema (RESO-like)
- Xuất ra properties_vietnam.json
- Push lên Hugging Face (create or merge dataset)

Optimized to bypass anti-scraping:
- Use playwright-stealth to avoid bot detection (fingerprinting, headers, etc.)
- Set realistic user-agent, viewport, screen size
- Add random delays to mimic human behavior
- Use headless=True with stealth to pass JS challenges (Cloudflare/Akamai)
- Increase timeouts and wait for network idle if possible
- Handle potential CAPTCHA by using real browser simulation (note: if manual CAPTCHA appears, headless=False may be needed for testing)
- Rate limiting: sleep between requests if paginating
- Avoid honeypots by not clicking hidden elements
"""

import os
import json
import datetime
import random
import time
import asyncio
from bs4 import BeautifulSoup
from huggingface_hub import HfApi, HfFolder, create_repo
from huggingface_hub.errors import RepositoryNotFoundError
from playwright.async_api import async_playwright
from playwright_stealth import stealth_async  # Requires pip install playwright-stealth
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

ROOT_URL = "https://www.cbrevietnam.com/properties"
AGENCY = "CBRE Vietnam"
HF_DATASET_ID = os.getenv("HF_DATASET_ID", "your-username/properties-vietnam")
HF_TOKEN = os.getenv("HF_TOKEN")
MERGE_STRATEGY = os.getenv("MERGE_STRATEGY", "smart_merge")

if not HF_TOKEN:
    raise RuntimeError("Please set HF_TOKEN env variable with your Hugging Face token.")

# ---------------- STEP 1: Crawl với Playwright (optimized for anti-bot, async mode) ----------------
async def crawl_cbre(url=ROOT_URL):
    print(f"[crawl] fetching from: {url}")
    properties = []

    async with async_playwright() as p:
        # Launch browser with configurations to mimic real user
        browser = await p.chromium.launch(
            headless=True,  # Can set to False for debugging
            args=[
                '--no-sandbox',
                '--disable-setuid-sandbox',
                '--disable-infobars',
                '--window-position=0,0',
                '--ignore-certificate-errors',
                '--ignore-certificate-errors-spki-list',
            ]
        )
        context = await browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            screen={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            java_script_enabled=True,
            bypass_csp=True,
            locale='en-US',
            timezone_id='Asia/Bangkok',  # Vietnam timezone
        )
        page = await context.new_page()
        
        # Apply stealth to avoid detection
        await stealth_async(page)
        
        try:
            # Goto with longer timeout
            await page.goto(url, timeout=90000, wait_until="domcontentloaded")
            
            # Wait for key selector, with longer timeout
            await page.wait_for_selector(".property-list .property-item", timeout=60000)
            
            # Optional: wait for network to be idle (helps with lazy loading)
            try:
                await page.wait_for_load_state('networkidle', timeout=30000)
            except:
                print("[crawl] Network idle timeout, proceeding anyway")
            
            # Add random human-like delay
            await asyncio.sleep(random.uniform(2, 5))
            
            # Optional: simulate scroll to load more if dynamic
            # await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            # await asyncio.sleep(random.uniform(1, 3))
            
            html = await page.content()
        except Exception as e:
            print(f"[crawl] Error during page load: {e}")
            await browser.close()
            return []
        finally:
            await browser.close()

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
    """Merge dataset theo chiến lược"""
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
    # Crawl
    properties = asyncio.run(crawl_cbre())

    # Merge
    api = HfApi()
    merged = merge_datasets(api, HF_DATASET_ID, properties, HF_TOKEN, strategy=MERGE_STRATEGY)

    # Save local
    with open("properties_vietnam.json", "w", encoding="utf-8") as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)
    print("[main] saved properties_vietnam.json")

    # Upload
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