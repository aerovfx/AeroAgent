# 05 người học

---

Những chức năng này

sẽ được học bởi

mô hình được gọi là người học cơ bản,

và chúng ta có thể chọn những gì

chúng tôi muốn họ như vậy.

Bạn đã tìm hiểu về

cây quyết định trước và

làm thế nào họ có thể nắm bắt được phi tuyến tính

các mối quan hệ trong dữ liệu.

Người học cơ bản cũng có thể

là một mô hình tuyến tính hoặc chúng ta có thể

có hai mô hình khác nhau cho

hai người học khác nhau.

Mỗi mô hình này

có thể học cách sử dụng

các phần khác nhau của

dữ liệu thử nghiệm kiểm soát ngẫu nhiên.

Mu_1 được học từ

bệnh nhân được chỉ định

đến cánh tay điều trị,

đó là W_i của một người đang sử dụng

tuổi tác và huyết áp

đầu vào và Y là

đầu ra mong muốn.

Tương tự, Mu_0 được học

từ những bệnh nhân đang

được giao cho cánh tay điều khiển.

Sử dụng tuổi và huyết áp làm

đầu vào một lần nữa,

và y là đầu ra.

Để huấn luyện một trong những mô hình này,

chúng ta có thể chia tập dữ liệu thành

một tập huấn luyện và

một bộ xác nhận.

Chú ý rằng những

Mẫu mũ mu là

các mô hình tiên lượng thực sự như

bạn đã học ở khóa 2,

trong đó Mu_1 là

mô hình tiên lượng

mang đến cho chúng ta nguy cơ xảy ra điều bất lợi

sự kiện khi điều trị

bằng một trong khi Mu

mũ số 0 sẽ là

mô hình tiên lượng

mang đến cho chúng ta nguy cơ

biến cố bất lợi khi nào

điều trị bằng không.

Nếu bạn chọn một quyết định

cây dành cho người học cơ bản,

sau đó bạn có thể học các mô hình

trông giống như sau.

Lưu ý rằng cả hai mô hình đều đang sử dụng

huyết áp và tuổi tác

để đưa ra một điểm rủi ro.

Chúng ta có thể thấy làm thế nào chúng ta có thể

sử dụng những mô hình này để

bây giờ ước tính việc điều trị

hiệu quả đối với bệnh nhân mới.

Đối với bệnh nhân 56 tuổi

tuổi và có máu

áp suất 130,

chúng ta có thể nhận được rủi ro dự kiến của họ

đang dùng Mu hat đang điều trị.

Vì vậy, chúng ta thấy rằng máu

áp suất nhỏ hơn 140,

và chúng ta thấy rằng độ tuổi

nhỏ hơn 60,

vì vậy chúng ta có điểm rủi ro là 0,21.

Ở phía bên phải,

chúng tôi thấy cho bệnh nhân này

tuổi nhỏ hơn

60 và huyết áp

nhỏ hơn 160,

vì vậy chúng tôi tạo ra rủi ro

điểm 0,45.

Chúng ta có thể trừ

hai người đưa cho chúng tôi

trung bình có điều kiện

tác dụng điều trị cho

bệnh nhân này đã cho

tính năng của họ.

Đây sẽ là

0,21 trừ 0,45,

đó là âm 0,24.

Phương pháp sử dụng

hai mô hình này,

Mu hat một và Mu hat zero,

và lấy sự khác biệt giữa

hai ước tính này để ước tính

trung bình có điều kiện

tác dụng điều trị là

gọi là Hai Cây

phương pháp T-learner.