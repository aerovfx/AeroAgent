# 01 phiên dịch-cnn-model

---

Bây giờ bạn đã tìm hiểu về các phương pháp

để giải thích các mô hình học máy bằng cách

tầm quan trọng của tính năng tính toán,

chúng ta sẽ chuyển sang phần giải thích

của các mô hình học sâu.

Trong bài học này, bạn sẽ tìm hiểu về

một phương pháp để giải thích tích chập

mạng lưới thần kinh mà bạn xây dựng cho

phân loại x-quang ngực trong khóa học một.

Đặc biệt, bạn sẽ học được cách bạn có thể

tạo bản đồ nhiệt để xác định vị trí

trong chụp X-quang ngực góp phần

nhất đối với việc phân loại mạng.

Trong phim chụp X-quang ngực này, bệnh nhân có

tim to còn được gọi là bệnh tim to.

Thuật toán của chúng tôi nhận ra

đó là bệnh tim to

với đầu ra có xác suất 80%.

Chúng ta sẽ xem xét làm thế nào chúng ta có thể có được

thuật toán xuất bản đồ nhiệt trên hình ảnh

hiển thị các phần của hình ảnh

biểu hiện rõ nhất của bệnh tim to.

Ở đây chúng ta có thể thấy rằng mô hình đang tìm kiếm

ở vùng tim để đưa ra quyết định.

Vậy là trái tim của nó đã ở đúng chỗ.

Chúng ta sẽ xem xét Grad-CAM

phương pháp để thực hiện đầu ra này.

Khi một hình ảnh được truyền qua

một mạng lưới thần kinh tích chập,

nó được truyền qua một loạt các lớp.

Ở đây cho

ví dụ là kiến trúc ResNet-34

trong đó hình ảnh được truyền qua

qua tất cả các lớp này.

Người ta thường tin rằng

các lớp đầu tiên trong CNN

nắm bắt các tính năng cấp thấp

trong khi các lớp sau

nắm bắt thông tin hình ảnh cấp cao hơn

điều đó có liên quan đến nhiệm vụ.

Cuối cùng, đầu ra của lượt chuyển đổi cuối cùng

lớp ở đây được làm phẳng và

sau đó được chuyển đến một hoặc

nhiều lớp được kết nối đầy đủ hơn với

đưa ra đầu ra ở đây của

bệnh tim to với xác suất 80%.

Một khi các tính năng được làm phẳng,

thông tin không gian bị mất.

Vì vậy, nếu chúng ta muốn hình dung các tính năng

mô hình đã được chọn trong hình ảnh của chúng tôi,

chúng tôi muốn hình dung các tính năng

trước khi quá trình làm phẳng xảy ra.