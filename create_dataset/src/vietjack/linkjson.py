import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin, urlparse
import os

def crawl_sub_links(base_url: str, output_file: str):
    res = requests.get(base_url)
    res.encoding = "utf-8"
    soup = BeautifulSoup(res.text, "html.parser")

    # domain gốc (vd: vietjack.com)
    domain = "{uri.scheme}://{uri.netloc}".format(uri=urlparse(base_url))

    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()

        # Chuẩn hóa thành absolute link
        full_url = urljoin(base_url, href)

        # Điều kiện lọc: cùng domain + nằm trong cùng chuyên mục gốc
        if full_url.startswith(domain) and "vat-li-12-kn" in full_url and full_url.endswith(".jsp"):
            if full_url not in links:
                links.append(full_url)

    print(f"🔗 Found {len(links)} sub-links")

    # Lưu ra file JSON
    data = {"links": links}
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ Saved {len(links)} links into {output_file}")



if __name__ == "__main__":
    url = input("📥 Nhập URL gốc (ví dụ https://vietjack.com/vat-li-12-kn/trac-nghiem-vat-li-lop-12.jsp): ").strip()
    if not url:
        print("⚠️ Bạn chưa nhập URL!")
    else:
        # Lấy thư mục chứa file .py hiện tại
        current_dir = os.path.dirname(os.path.abspath(__file__))
        output_file = os.path.join(current_dir, "urls.json")

        crawl_sub_links(url, output_file)