# môi trường Python (pip)
pip install requests beautifulsoup4 cloudscraper tqdm playwright
# sau khi cài playwright, cần cài browser binaries
python -m playwright install

.	Requests + realistic headers
	•	Nhiều site chặn python-requests vì UA. Thay UA + thêm Referer, Accept-Language có thể xuyên qua một số checks. Tuy nhiên site có WAF (Cloudflare/Akamai) thường vẫn trả 403.
	2.	Cloudscraper
	•	Thư viện này cố gắng giải các challenge  JS / Cloudflare ở mức độ nhẹ. (Đôi khi bị block nếu challenge quá mới). Nếu dùng cloudscraper, thư viện đã xử lý 1 vài bước challenge.
	3.	Playwright
	•	Đây là biện pháp mạnh nhất, vì script mở trình duyệt thật (Chromium) — server thấy request như từ người dùng thật. Đồng thời ta bắt được các request XHR / Fetch mà trang thực sự gọi (các API ngầm).
	•	Khi phát hiện endpoint JSON, script sẽ lấy cookie từ phiên Playwright và gắn vào requests.Session để gọi endpoint nhanh, tiết kiệm tài nguyên.
	4.	Tính đạo đức & kỹ thuật
	•	Luôn đặt delays (page.wait_for_timeout, time.sleep) và không spam.
	•	Nếu bạn làm production scraping: dùng proxy pool, respect robots.txt, lưu log, implement retry/backoff.

Câu hỏi này hay 👍 mình sẽ phân tích sâu để bạn nắm rõ cơ chế bảo vệ trước scraping và cách mà các website như CBRE hay các cổng bất động sản lớn (hoặc các sàn TMĐT, báo chí,…) thường dùng:

⸻

🔐 Các cơ chế bảo vệ chống scraping phổ biến

1. User-Agent & Header Filtering
	•	Bot thường dùng requests hoặc curl với User-Agent mặc định (python-requests, curl/7.81.0).
	•	Server sẽ block nếu phát hiện UA không giống trình duyệt thật (Chrome, Edge…).
	•	Ngoài ra còn check các header bắt buộc (Accept-Language, Accept-Encoding, Referer, Cookie…).

👉 Ví dụ CBRE: trả về 403 Forbidden khi bạn dùng requests mà không giả lập header.

⸻

2. Rate Limiting / Throttling
	•	Nếu 1 IP gửi quá nhiều request trong thời gian ngắn → block hoặc trả về CAPTCHA.
	•	Thường kèm theo 429 Too Many Requests.

⸻

3. JavaScript Rendering (Dynamic Content)
	•	Nhiều site chỉ load khung HTML ban đầu, còn nội dung (danh sách BĐS, giá, ảnh) là do JavaScript fetch từ API sau khi DOM load.
	•	Nếu bạn chỉ dùng requests lấy HTML → không thấy dữ liệu.
	•	Cần Playwright / Puppeteer / Selenium để render.

⸻

4. Session & Cookie Validation
	•	Một số trang yêu cầu session hợp lệ (cookie chứa JWT / CSRF token).
	•	Nếu bot không gửi kèm cookie hợp lệ → redirect về login hoặc trả về 403.

⸻

5. CAPTCHA / reCAPTCHA / hCaptcha
	•	CAPTCHA hình ảnh hoặc invisible reCAPTCHA (score-based).
	•	Thường kích hoạt khi nghi ngờ bot: request bất thường, IP datacenter, không load JS,…

⸻

6. Fingerprinting (Advanced)

Các hệ thống như Cloudflare, Akamai, PerimeterX, Datadome sẽ:
	•	Kiểm tra browser fingerprint (Canvas, WebGL, Fonts, Screen size…).
	•	Kiểm tra JS challenge (bắt client chạy JS tính toán hash).
	•	Dò bot bằng behavior analysis (chuột, scroll, timing request).

👉 Đây là lý do khi dùng requests bị block, còn dùng Playwright (headless Chromium) thì qua được.

⸻

7. Honeypot Links / Traps
	•	Cài link ẩn (dùng display:none hoặc vị trí ngoài màn hình).
	•	Người dùng thật không click, nhưng bot crawler thì follow → bị flag và block.

⸻

🛡️ Cách phòng chống scraping (cho người xây web)
	1.	Thêm CAPTCHA khi detect bot
→ Google reCAPTCHA v3, Cloudflare Turnstile.
	2.	Dùng dịch vụ bảo vệ (Cloudflare/Akamai/Datadome)
→ Có challenge JS, fingerprint, rate limiting.
	3.	Randomized API endpoints / GraphQL with auth
→ Tránh public endpoint dễ crawl.
	4.	Obfuscation / Delay load
→ Dữ liệu chỉ trả về khi người dùng tương tác (scroll, click).
	5.	Honeypot & monitoring
→ Phát hiện hành vi bất thường (truy cập 1000 trang/phút).
	6.	Legal protection
→ Điều khoản sử dụng, cấm scrape. Nếu phát hiện IP bot → block hoặc gửi DMCA.

⸻

✅ Tóm lại:
	•	Cơ chế phổ biến: Cloudflare/Akamai (header check + JS challenge + bot fingerprint).
	•	Lý do bạn bị 403: server phát hiện request không phải từ browser thật (headers, cookie, JS).
	•	Phòng chống scrape: CAPTCHA, rate limit, fingerprinting, honeypot, session validation.

