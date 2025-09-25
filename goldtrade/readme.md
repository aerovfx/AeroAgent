
# Gold Price Analysis App

Ứng dụng này được xây dựng để **thu thập, lưu trữ và phân tích dữ liệu giá vàng tại Việt Nam**.  
App hỗ trợ cả việc trực quan hóa qua dashboard, phân tích chuỗi thời gian, và lưu trữ dữ liệu dạng CSV, Parquet, hoặc SQLite.

---

## Table of Contents

- [Giới thiệu](#giới-thiệu)
- [Cài đặt](#cài-đặt)
- [Cấu hình môi trường](#cấu-hình-môi-trường)
- [Dataset](#dataset)
- [Các script](#các-script)
- [Chạy app và dashboard](#chạy-app-và-dashboard)
- [Cấu trúc thư mục](#cấu-trúc-thư-mục)
- [Liên hệ](#liên-hệ)

---

## Giới thiệu

Gold Price Analysis App giúp bạn:

- Scrape dữ liệu giá vàng từ website (ví dụ PhuQuy Group).  
- Lưu dữ liệu dưới nhiều định dạng: CSV, Parquet, SQLite.  
- Phân tích chuỗi thời gian, thống kê giá vàng theo ngày, tuần, tháng.  
- Trực quan hóa dữ liệu bằng `dashboard.py`.

---

## Cài đặt

### Yêu cầu

- Python >= 3.10  
- Các thư viện Python:
```bash
pip install -r requirements.txt

Clone repository

git clone https://github.com/username/gold-price-analysis.git
cd gold-price-analysis


⸻

Cấu hình môi trường

Tạo file .env với thông tin cấu hình (ví dụ goldtrade source):

GOLD_SOURCE=https://phuquygroup.vn/giavang
DB_PATH=data/gold_data.db

	•	GOLD_SOURCE: URL nguồn dữ liệu vàng.
	•	DB_PATH: Đường dẫn lưu database SQLite.

⸻

Dataset

Dữ liệu được lưu ở các định dạng khác nhau:

1. CSV
	•	gold_prices.csv – dữ liệu giá vàng chi tiết hàng ngày.
	•	gold_price_summary.csv – dữ liệu tổng hợp (mua/bán trung bình, min/max).
	•	gold_timeseries.csv – dữ liệu dạng chuỗi thời gian.

2. Parquet
	•	gold_prices.parquet – phiên bản Parquet của gold_prices.csv.
	•	gold_timeseries.parquet – phiên bản Parquet của chuỗi thời gian.

3. SQLite
	•	gold_data.db – chứa bảng gold_prices và gold_summary.
	•	gold_timeseries.db – chứa bảng dữ liệu chuỗi thời gian.

⸻

Các script

Script	Mục đích
gold_scraper.py	Thu thập dữ liệu từ website và lưu vào CSV/Parquet/DB
data_learning.py	Phân tích dữ liệu, tính toán thống kê, tạo datasets cho học máy
dashboard.py	Chạy dashboard trực quan hóa dữ liệu giá vàng (plot, chart)

Ví dụ sử dụng

Scrape dữ liệu và lưu CSV/DB:

python gold_scraper.py

Chạy dashboard trực quan hóa:

python dashboard.py

Phân tích dữ liệu cho học máy / học sâu:

python data_learning.py


⸻

Chạy app và dashboard
	1.	Cài đặt dependencies:

pip install -r requirements.txt

	2.	Cấu hình .env.
	3.	Thu thập dữ liệu:

python gold_scraper.py

	4.	Chạy dashboard:

python dashboard.py

	5.	(Tuỳ chọn) Phân tích dữ liệu học máy:

python data_learning.py


⸻

Cấu trúc thư mục

gold-price-analysis/
│
├─ .env                         # Cấu hình nguồn dữ liệu và DB
├─ gold_scraper.py               # Script crawl dữ liệu giá vàng
├─ dashboard.py                  # Dashboard trực quan hóa
├─ data_learning.py              # Script phân tích dữ liệu
├─ requirements.txt              # Các package Python cần thiết
│
├─ /data/
│   ├─ gold_prices.csv
│   ├─ gold_price_summary.csv
│   ├─ gold_prices.parquet
│   ├─ gold_timeseries.csv
│   ├─ gold_timeseries.db
│   └─ gold_timeseries.parquet
│
└─ README.md


⸻

Liên hệ
	•	Tác giả: Viet Chung
	•	GitHub: https://github.com/aerovfx

