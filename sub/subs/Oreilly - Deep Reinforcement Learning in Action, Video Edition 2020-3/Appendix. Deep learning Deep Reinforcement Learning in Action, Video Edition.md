# Phụ lục. Học sâu Học tăng cường sâu trong thực tế, Phiên bản video

---

8.3 Học sâu

Mạng lưới thần kinh sâu đơn giản là sự kết hợp của nhiều lớp chức năng đơn giản hơn được gọi là

các lớp.

Mỗi hàm lớp bao gồm một phép nhân ma trận, theo sau là hàm kích hoạt phi tuyến.

Hàm kích hoạt phổ biến nhất là f(x) = max(0,x), trả về 0 nếu x âm

hoặc trả về x nếu không.

Một mạng lưới thần kinh đơn giản có thể

Xem hình này

Đọc sơ đồ này từ trái sang phải, như thể dữ liệu chảy từ bên trái vào hàm L1,

sau đó là hàm L2 và trở thành đầu ra ở bên phải.

Các ký hiệu k, m và n đề cập đến số chiều của vectơ.

Một vectơ có độ dài k là đầu vào của hàm L1, hàm này tạo ra một vectơ có độ dài m sau đó

được chuyển đến L2, cuối cùng tạo ra một vectơ n chiều.

Bây giờ chúng ta hãy xem từng hàm L này đang làm gì.

Xem hình này

Một lớp mạng nơ-ron nói chung bao gồm hai phần, phép nhân ma trận và

một chức năng kích hoạt.

Một vectơ có độ dài n xuất hiện từ bên trái và được nhân với một ma trận, thường được gọi là

một tham số hoặc ma trận trọng số, có thể thay đổi chiều của kết quả đầu ra

vectơ.

Vectơ đầu ra, bây giờ có độ dài m, được truyền qua hàm kích hoạt phi tuyến,

không làm thay đổi số chiều của vectơ.

Mạng lưới thần kinh sâu chỉ xếp chồng các lớp này lại với nhau và chúng tôi huấn luyện nó bằng cách áp dụng độ dốc

đi xuống các ma trận trọng số, là các tham số của mạng nơ-ron.

Đây là mạng thần kinh hai lớp đơn giản trong NumPy.

Liệt kê 8.2, một mạng nơ-ron đơn giản

Trong phần tiếp theo, bạn sẽ học cách sử dụng thư viện PyTorch để tự động tính toán

gradient để dễ dàng huấn luyện mạng lưới thần kinh.