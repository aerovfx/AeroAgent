# Phụ lục. Học sâu Học tăng cường sâu trong thực tế, Phiên bản video.vi

---

8.3 Học sâu Một mạng lưới thần kinh sâu

chỉ đơn giản là sự kết hợp của nhiều lớp

chức năng đơn giản hơn được gọi là các lớp.

Mỗi lớp chức năng bao gồm các nhân ma trận,

sau đó là một tính năng kích hoạt phi tuyến.

Hàm kích hoạt phổ biến nhất là f(x) = max(0,x),

hàm này trả về 0 nếu x âm hoặc trả về x nếu không.

Một mạng lưới thần kinh đơn giản có thể là Hãy xem

this screen Đọc sơ đồ này từ trái sang phải, như thể

`cuting data from left left to L1 function, after

đó là chức năng L2 và trở thành thành viên ở bên phải.

Các ký hiệu k, m và nđề

access to the size.

Một độ dài k được đưa vào chức năng L1, điều này tạo ra một

Sau đó, chiều dài được truyền đến L2, cuối cùng được tạo ra một chiều.

Bây giờ hãy xem xét những điều này

Mỗi hàm L này đang làm gì.

Mời bạn xem hình này Theo nghĩa chung, một

lớp mạng lưới thần kinh bao gồm hai

phần, ma trận nhân và một chức năng kích hoạt.

One length n đi vào từ bên trái và

được nhân với một ma trận, thường được gọi là

một tham số hoặc ma trận, có thể thay đổi chiều của đầu ra vectơ

quả.

Vector đầu ra, thời gian có độ dài m, được truyền qua một hàm

kích hoạt tính năng tuyến tính, không thay đổi chiều của vectơ.

Một mạng nơ-ron sâu chỉ chồng các lớp này lại với nhau và chúng ta đào tạo nó bằng cách

cách áp dụng độ dốc trên các số ma trận, chính là các tham số của mạng nơron.

Đây là một mạng lưới

hai lớp đơn giản trong NumPy.

Niêm yết 8.2, một mạng nơ-ron đơn giản Trong phần

tiếp theo, bạn sẽ học cách sử dụng thư viện PyTorch

để tính toán tự động độ dốc để dễ dàng đào tạo mạng nơ-ron.