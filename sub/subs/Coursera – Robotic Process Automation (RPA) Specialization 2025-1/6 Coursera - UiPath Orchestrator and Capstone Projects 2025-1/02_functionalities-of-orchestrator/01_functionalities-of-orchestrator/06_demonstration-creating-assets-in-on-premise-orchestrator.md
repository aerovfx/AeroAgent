# 06 người dàn nhạc trình diễn-tạo-tài sản tại chỗ

---

Xin chào và chào mừng đến với điều này

trình diễn về việc tạo

tài sản tại chỗ

Người soạn nhạc

và sử dụng nó trong một dự án.

Vì vậy hãy bắt đầu bằng cách

hiểu, tài sản là gì?

Tài sản là biến được chia sẻ

hoặc thông tin xác thực được lưu trữ trong

Orchestrator và được sử dụng bởi

các robot ở những nơi khác nhau

các dự án tự động hóa.

Họ có thể lưu trữ cụ thể

thông tin và hành động như

một kho lưu trữ dữ liệu

robot có thể truy cập

khi chạy các tiến trình.

Ở đây bạn có thể thấy một

dự án trong UiPath Studio.

Dự án này bước vào một

thông tin đăng nhập của người dùng trên

trang đăng nhập của UiPath

trang web khi thực hiện.

Thay vì lưu trữ

thông tin đăng nhập

trong các hoạt động của dự án,

bạn có thể lưu trữ những thứ này trong

Tài sản của người soạn nhạc.

Dữ liệu được lưu trữ

sẽ được lấy bởi

quy trình khi ký kết

vào trang web.

Để thực hiện việc này, hãy truy cập

trang Tài sản trong

thư mục Không gian làm việc của tôi

và tạo một tài sản thông tin xác thực

để lưu trữ chi tiết đăng nhập.

Sau khi hoàn tất, hãy kéo và thả

Nhận thông tin xác thực

hoạt động trong dự án.

Đổi tên hoạt động này và

nhập tên tài sản vào

thuộc tính AssetName của nó.

Tạo một biến chuỗi mới

được gọi là Mật khẩu trong đó

Thuộc tính mật khẩu,

và một biến chuỗi mới gọi là

Tên người dùng trong đó

Thuộc tính tên người dùng.

Khi thực hiện,

thông tin đăng nhập

từ người soạn nhạc

sẽ được lưu trữ trong

hai biến này và

sẽ được sử dụng theo yêu cầu.

Bây giờ thay thế các giá trị

từ cả hai Loại

Tham gia các hoạt động cùng họ

các biến tương ứng.

Thay thế Type Into

hoạt động của Mật khẩu với

hoạt động Loại văn bản bảo mật

để làm theo những thực hành tốt nhất.

Cho biết trường mật khẩu

và nhập biến mật khẩu

trong thuộc tính SecureText của nó.

Sau khi hoàn thành, dự án này có thể

bị xử tử để thấy điều đó

thông tin đăng nhập

được nhập vào

trang đăng nhập của

trang web UiPath.

Điều này kết thúc video của chúng tôi về

tạo nội dung trong Orchestrator.

Cảm ơn bạn đã xem.