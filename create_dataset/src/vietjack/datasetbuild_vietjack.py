import requests
from bs4 import BeautifulSoup
import random
import time
import cloudscraper
import threading
from urllib.parse import urljoin

print_lock = threading.Lock()

# --- Tải HTML với retry và cloudscraper ---
def fetch_html(url, retry=3):
    headers = {
        "User-Agent": random.choice([
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
        ]),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "vi-VN,vi;q=0.9,en;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
    }

    for attempt in range(retry):
        try:
            session = requests.Session()
            resp = session.get(url, headers=headers, timeout=20)
            if resp.status_code == 200 and len(resp.text) > 500:
                return resp.text
            else:
                with print_lock:
                    print(f"⚠️ Attempt {attempt+1}: Status {resp.status_code}, trying cloudscraper...")
                scraper = cloudscraper.create_scraper()
                resp = scraper.get(url, headers=headers, timeout=20)
                if resp.status_code == 200:
                    return resp.text
        except Exception as e:
            with print_lock:
                print(f"❌ Attempt {attempt+1} failed: {e}")
            if attempt < retry - 1:
                time.sleep(2 ** attempt)
    return None

# --- Crawl nhiều môn ---
def crawl_vietjack_multi(base_urls):
    all_urls = set()
    for base_url in base_urls:
        html = fetch_html(base_url)
        if not html:
            print(f"❌ Không tải được trang {base_url}")
            continue

        soup = BeautifulSoup(html, "html.parser")

        for a in soup.find_all("a", href=True):
            href = a['href']
            # Lọc các link bài tập các môn phổ biến
            if href.endswith(".jsp") and any(m in href for m in ["toan", "vat-li", "hoa-hoc", "sinh-hoc", "anh-van"]):
                full_url = urljoin(base_url, href)  # fix relative URL
                all_urls.add(full_url)

    return sorted(all_urls)

# --- Ví dụ sử dụng ---
if __name__ == "__main__":
    base_urls = [
        "https://vietjack.com/bai-tap-trac-nghiem-toan-lop-6.php",
        "https://vietjack.com/bai-tap-trac-nghiem-toan-lop-7.php",
        "https://vietjack.com/bai-tap-trac-nghiem-toan-lop-8.php",
        "https://vietjack.com/bai-tap-trac-nghiem-toan-lop-9.php",
        "https://vietjack.com/bai-tap-trac-nghiem-toan-lop-10.php",
        "https://vietjack.com/bai-tap-trac-nghiem-toan-lop-11.php",
        "https://vietjack.com/bai-tap-trac-nghiem-toan-lop-12.php",
        "https://vietjack.com/vat-li-12-kn/",
        "https://vietjack.com/hoa-hoc-12-kn/",
        "https://vietjack.com/sinh-hoc-12-kn/",
        "https://vietjack.com/anh-van-12-kn/"
    ]

    urls = crawl_vietjack_multi(base_urls)
    print(f"✅ Tổng số URL bài tập tìm được: {len(urls)}")
    for u in urls:
        print(u)