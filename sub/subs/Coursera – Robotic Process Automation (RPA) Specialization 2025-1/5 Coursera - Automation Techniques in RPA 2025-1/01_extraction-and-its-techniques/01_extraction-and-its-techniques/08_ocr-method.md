# 08 phương pháp ocr

---

[ÂM THANH].

Trong video trước,

bạn đã hiểu phương pháp Bản địa,

trong video này bạn sẽ hiểu OCR

hoặc phương pháp nhận dạng ký tự quang học.

Mặc dù cả văn bản đầy đủ và bản gốc đều có

kết quả tuyệt vời về độ chính xác và

tốc độ, có trường hợp cụ thể

trong đó cả hai đều không thể sử dụng được.

Ví dụ: phương thức đầu ra OCR,

nên được sử dụng nếu bạn cần giải nén

thông tin từ môi trường ảo hoặc

,đọc, văn bản từ hình ảnh.

Nó dựa trên công nghệ OCR được sử dụng

trong việc nhận dạng tài liệu được quét.

Nó cố gắng nhận ra từng chữ cái của

văn bản được đưa ra trên một hình ảnh trong mục tiêu

tài liệu.

Nó chậm khi so sánh với cái khác

phương pháp có độ chính xác thấp hơn và

không thể trích xuất văn bản ẩn và

không thể làm việc ở chế độ nền.

Phương pháp OCR có ba công cụ mặc định,

đó là Tesseract OCR,

Microsoft OCR và UiPath Màn hình OCR.

Việc sử dụng các động cơ này phụ thuộc vào

loại thông tin được trích xuất,

nói chung tốt hơn là nên chuyển đổi

giữa các phương pháp để xem cái nào

động cơ mang lại kết quả tốt hơn cho

từng tình huống.

Nếu bạn đã tải xuống và cài đặt

các gói của công cụ OCR khác,

họ cũng sẽ có sẵn

trong khi chọn công cụ OCR.

Chúng ta hãy hiểu từng

chi tiết về các động cơ này.

Động cơ đầu tiên là Tesseract OCR.

Công cụ này mang lại kết quả tốt hơn cho

nhận dạng ký tự ở kích thước nhỏ hơn

khu vực và hỗ trợ đảo ngược màu sắc.

Nó cung cấp nhiều tùy chọn tùy chỉnh

thông qua các bộ lọc có thể được sử dụng để chọn

chỉ các loại ký tự cụ thể.

Phương pháp này cung cấp năm lựa chọn,

tùy chọn đầu tiên là ngôn ngữ,

đây là tiếng Anh theo mặc định.

Tùy chọn thứ hai là ký tự,

nó cho phép bạn chọn loại

các ký tự sẽ được trích xuất.

Các tùy chọn sau đây có sẵn,

bất kỳ ký tự nào, chỉ số, chữ cái,

chữ hoa, chữ thường, số điện thoại,

tiền tệ, ngày tháng và tùy chỉnh.

Khi được chọn tùy chỉnh, hai

các trường Được phép và Từ chối được hiển thị,

cho phép bạn tạo các quy tắc tùy chỉnh trên

loại ký tự nào cần cạo và

điều cần tránh.

Tùy chọn thứ ba là chia tỷ lệ, chia tỷ lệ

hệ số của thành phần UI đã chọn hoặc

hình ảnh, số càng cao

hình ảnh càng phóng to.

Điều này có thể cung cấp tỷ lệ OCR tốt hơn và

được khuyến nghị cho hình ảnh nhỏ.

Tùy chọn thứ tư là đảo ngược,

khi hộp kiểm này được chọn,

màu sắc của các thành phần UI

được đảo ngược trước khi cạo,

điều này rất hữu ích khi nền

đậm hơn màu văn bản.

Tùy chọn thứ năm là Nhận thông tin từ,

Nó giúp hiển thị trên màn hình

vị trí của từng tác phẩm được cạo.

Công cụ thứ hai là Microsoft OCR,

động cơ này được sử dụng để làm việc

với phông chữ của Microsoft và

trên hình ảnh kích thước lớn hơn,

nó hỗ trợ nhiều ngôn ngữ.

Động cơ này cung cấp ba tùy chọn,

tùy chọn đầu tiên là ngôn ngữ, nó cho phép

bạn thay đổi ngôn ngữ của phần bị loại bỏ

văn bản, theo mặc định tiếng Anh được chọn.

Tùy chọn thứ hai là chia tỷ lệ, chia tỷ lệ

hệ số của thành phần UI đã chọn hoặc

hình ảnh, số càng cao

hình ảnh càng phóng to.

Điều này có thể cung cấp khả năng đọc và ghi OCR tốt hơn

được khuyến nghị cho hình ảnh nhỏ.

Tùy chọn thứ ba là Nhận thông tin từ,

nó có được vị trí trên màn hình

của mỗi từ được cạo.

Công cụ thứ ba là UiPath Screen OCR,

động cơ này có thể được sử dụng

trong bất kỳ kịch bản tự động hóa giao diện người dùng nào trong

cần có động cơ OCR.

Động cơ này cung cấp ba tùy chọn,

tùy chọn đầu tiên là Điểm cuối,

đây là điểm cuối của

Màn hình UiPath OCR được nhập.

Tùy chọn thứ hai là Khóa API,

Khóa API được sử dụng để cung cấp cho bạn quyền truy cập

vào màn hình UiPath OCR,

nó không bắt buộc trong thời gian xem trước.

Tùy chọn thứ ba là Nhận thông tin từ,

nó có được vị trí trên màn hình

của mỗi từ được cạo.

Video tiếp theo sẽ hiển thị một cuộc biểu tình

văn bản đã được lấy từ đâu

một bài đăng blog UiPath sử dụng

trình hướng dẫn cạo màn hình và

được lưu trữ trong một tập tin notepad.

Tôi sẽ khuyến khích bạn đi

thông qua việc trình diễn và

cố gắng tự mình lặp lại nó.

Vậy là xong video này,

cảm ơn bạn đã xem.