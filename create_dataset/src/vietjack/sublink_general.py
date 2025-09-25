import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin, urlparse
import os

def crawl_sub_links(base_url: str, output_file: str):
    res = requests.get(base_url)
    res.encoding = "utf-8"
    soup = BeautifulSoup(res.text, "html.parser")

    # Domain gốc
    domain = "{uri.scheme}://{uri.netloc}".format(uri=urlparse(base_url))
    netloc = urlparse(base_url).netloc

    # Xác định pattern theo domain
    if "vietjack.com" in netloc:
        pattern = "vat-li-12-kn"
        condition = lambda url: url.startswith(domain) and pattern in url and url.endswith(".jsp")

    elif "tech12h.com" in netloc:
        pattern = "/trac-nghiem-vat-li-12-"
        condition = lambda url: url.startswith(domain) and pattern in url

    else:
        print("⚠️ Chưa hỗ trợ domain này:", netloc)
        return

    urls = []
    for a in soup.find_all("a", href=True):
        full_url = urljoin(base_url, a["href"].strip())
        if condition(full_url) and full_url not in urls:
            urls.append(full_url)

    print(f"🔗 Found {len(urls)} sub-links")

    # Lưu JSON với key "urls"
    data = {"urls": urls}
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ Saved {len(urls)} urls into {output_file}")


if __name__ == "__main__":
    url = input("📥 Nhập URL gốc: ").strip()
    if not url:
        print("⚠️ Bạn chưa nhập URL!")
    else:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        output_file = os.path.join(current_dir, "urls.json")
        crawl_sub_links(url, output_file)