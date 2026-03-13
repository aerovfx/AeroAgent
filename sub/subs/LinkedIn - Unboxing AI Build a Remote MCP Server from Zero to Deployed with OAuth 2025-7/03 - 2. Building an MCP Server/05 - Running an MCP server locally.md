# 05 - Chạy máy chủ MCP cục bộ

---

- [Người hướng dẫn] Hướng dẫn nói bắt đầu bằng

đi vào thư mục được đề cập.

Vì vậy, tôi sẽ mở trong terminal,

thì tôi sẽ, tôi đoán là tôi sẽ tạo một thiết bị đầu cuối mới cho chính mình.

Tôi sẽ vào terminal và sau đó điều hướng đến thư mục bên phải.

Vì vậy tôi sẽ đi tới cd ngày thứ 2

và sau đó ở đây tôi muốn hoàn thành máy chủ thời tiết.

Sau đó tôi chạy đồng bộ hóa uv.

Điều này giống như cài đặt pip.

Vì vậy, nó đồng bộ hóa dự án uv

bằng cách thu thập tất cả thông tin

từ tệp .toml dự án cao.

Và điều này cài đặt tất cả các phụ thuộc

và khởi động mọi thứ.

Nếu bạn chỉ đang chạy dự án,

bạn thực sự không cần phải làm điều này.

Điều này chỉ dành cho mục đích phát triển.

Nhưng tôi muốn trải qua quá trình này

vì vậy bạn thấy mọi thứ có liên quan.

Khi bạn đã cài đặt tất cả các phần phụ thuộc này,

bây giờ bạn có thể khởi động môi trường ảo

bằng cách gọi vào nguồn .venv/bin/activate

Vì vậy tôi sẽ đặt nó xuống đây.

Bạn sẽ nhận thấy trong terminal

bây giờ nó ghi mcp open meteo ở phía trước,

nghĩa là tôi hiện đang làm việc trong môi trường ảo

thay vì làm việc trong môi trường chung

của máy tính.

Và môi trường ảo này hiện đã cài đặt Python 3.10

và tất cả các phụ thuộc.

Vì vậy, mọi thứ đều có sẵn ở đây.

Và điều đó có nghĩa là nếu tôi vào thư mục con

và tôi mở ra, ví dụ: server.py,

Tôi có quyền truy cập vào tất cả các phần cần thiết

và tôi có thể khiến mọi thứ thành công,

ngoại trừ việc tôi không thể vì có màu vàng này

gạch chân nguệch ngoạc.

Điều đang xảy ra ở đây là VS Code không tôn trọng

những gì đang xảy ra trong thiết bị đầu cuối.

Chúng là hai thứ hoàn toàn riêng biệt.

Vì vậy, thiết bị đầu cuối hiện ở bên trong venv,

môi trường ảo, nhưng VS Code vẫn nằm ngoài nó.

Điều đó có thể dễ dàng được sửa chữa.

Chúng tôi đi đến mẫu lệnh

hoặc bảng lệnh, đó cũng là Shift Control hoặc Command P.

Sau đó, bạn nhập môi trường dự án Python set.

Thế đấy, mcp mở meteo.

Vì vậy, đây chính là môi trường mà chúng tôi đang tìm kiếm.

Và bây giờ bạn thấy rằng môi trường đó đang ngồi

bên trong VS Code, bây giờ tôi có quyền truy cập vào tất cả các gói

và mọi thứ ở đó.