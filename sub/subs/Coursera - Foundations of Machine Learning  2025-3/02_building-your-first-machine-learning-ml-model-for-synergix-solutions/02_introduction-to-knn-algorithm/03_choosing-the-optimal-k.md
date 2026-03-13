# 03 lựa chọn-tối ưu-k

---

Giá trị mặc định của k trong

k hàng xóm gần nhất là 5.

Nhưng giá trị này cần được điều chỉnh cho phù hợp

từng phát biểu vấn đề riêng biệt.

Các thông số mà chúng tôi thay đổi trong

một thuật toán học máy được gọi là

siêu tham số và

quá trình tìm giá trị đúng của

những siêu tham số này là

được gọi là điều chỉnh siêu tham số.

Vì vậy, trong thuật toán KNN, số lượng

hàng xóm là một siêu tham số, và

quá trình tìm kiếm quyền

giá trị của hàng xóm đối với

tuyên bố vấn đề hiệp lực

sẽ là điều chỉnh siêu tham số.

Chúng ta hãy xem xét một cách tiếp cận thô thiển

để tìm giá trị đúng của k.

Đầu tiên chúng ta sẽ chọn

một khoảng giá trị k.

Bây giờ, hãy lưu ý rằng mức tối thiểu

giá trị của k có thể là 1 và

tối đa có thể là số lượng dữ liệu

các điểm có trong tập dữ liệu.

Thứ hai, chúng tôi sẽ

triển khai mô hình KNN cho

mọi giá trị của k trong phạm vi

mà chúng ta vừa chọn.

Sau đó, chúng tôi tính toán đánh giá

số liệu mà mô hình đạt được trong bài kiểm tra

đặt cho mọi giá trị của k và chọn

k có số liệu đánh giá tốt nhất.

Cốt truyện sẽ trông giống như thế này.

Ở đây chúng ta có phạm vi giá trị k trên

trục x và sai số trên trục y.

Vậy nhìn vào biểu đồ này,

chúng ta có thể chọn giá trị của k cho

mà sai số là nhỏ nhất.

Chúng ta sẽ trải qua quá trình này

khi chúng tôi xây dựng mô hình KNN cho

tuyên bố vấn đề hiệp lực.

Bây giờ, bạn đã hiểu rõ

về hoạt động bên trong của KNN,

nhưng còn một cái nữa

câu hỏi chúng ta cần trả lời.

Chúng ta tính toán như thế nào

khoảng cách giữa hai điểm trong KNN?

Chúng ta hãy thảo luận về những cách khác nhau để

tính khoảng cách trong video tiếp theo.