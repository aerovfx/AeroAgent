import json
import time
import random
from collections import defaultdict
from urllib.parse import urljoin
import requests
import cloudscraper
from bs4 import BeautifulSoup

# --- Tải HTML ---
def fetch_html(url, retry=3):
    headers = {
        "User-Agent": random.choice([
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/121.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"
        ])
    }
    for attempt in range(retry):
        try:
            resp = requests.get(url, headers=headers, timeout=20)
            if resp.status_code == 200 and len(resp.text) > 500:
                return resp.text
            # fallback cloudscraper
            scraper = cloudscraper.create_scraper()
            resp = scraper.get(url, headers=headers, timeout=20)
            if resp.status_code == 200:
                return resp.text
        except Exception as e:
            print(f"❌ Lỗi {attempt+1}: {e}")
            time.sleep(2 ** attempt)
    return None

# --- Lấy links ---
def get_quiz_links(url):
    html = fetch_html(url)
    if not html:
        return []
    soup = BeautifulSoup(html, "html.parser")
    seen_urls = set()
    quiz_links = []

    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        if not href:
            continue
        full_url = urljoin(url, href)
        if not full_url.startswith("https://tech12h.com"):
            continue
        if full_url in seen_urls:
            continue
        seen_urls.add(full_url)

        if any(k in full_url.lower() for k in ['trac-nghiem', 'quiz', 'test']):
            quiz_links.append(full_url)

    return quiz_links

# --- Crawl đệ quy ---
def crawl_all_quiz_links(start_url, visited=None, max_depth=2, current_depth=0):
    if visited is None:
        visited = set()
    if current_depth > max_depth or start_url in visited:
        return []
    visited.add(start_url)

    links = get_quiz_links(start_url)
    all_links = links.copy()

    # Lấy thêm các trang khác để crawl tiếp (other links)
    html = fetch_html(start_url)
    if html:
        soup = BeautifulSoup(html, "html.parser")
        other_links = []
        for a in soup.find_all("a", href=True):
            full_url = urljoin(start_url, a["href"].strip())
            if full_url.startswith("https://tech12h.com") and full_url not in visited:
                other_links.append(full_url)
        for link in other_links[:5]:  # giới hạn 5 link để tránh loop
            all_links.extend(crawl_all_quiz_links(link, visited, max_depth, current_depth+1))

    return list(set(all_links))  # loại bỏ duplicate

# --- Lưu JSON ---
def save_json(urls, filename="quiz_urls.json"):
    data = {"urls": urls}
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ Đã lưu {len(urls)} URLs vào {filename}")

# --- Main ---
def main():
    start_url = input("Nhập URL (mặc định https://tech12h.com): ").strip() or "https://tech12h.com"
    max_depth = input("Độ sâu crawl (mặc định 2): ").strip()
    max_depth = int(max_depth) if max_depth.isdigit() else 2

    all_links = crawl_all_quiz_links(start_url, max_depth=max_depth)
    print(f"🔗 Tìm thấy {len(all_links)} quiz links")
    save_json(all_links, "quiz_urls.json")

if __name__ == "__main__":
    main()