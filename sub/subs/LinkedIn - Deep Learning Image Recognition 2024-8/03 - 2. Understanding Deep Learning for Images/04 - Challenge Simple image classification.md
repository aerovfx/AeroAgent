# 04 - Thử thách Phân loại hình ảnh đơn giản

---

(nhạc sôi động tươi sáng)

- Tuyệt vời.

Chúng tôi đã và đang tạo ra các mô hình.

Đơn giản, nâng cao và nâng cao.

Bây giờ đến lượt bạn.

Bạn sẽ tiếp tục và thực hiện thử thách,

và trong thử thách này, chúng tôi sẽ sử dụng mô hình CNN nâng cao

từ bài học trước,

và thêm một lớp chập khác

để làm sâu sắc thêm kiến trúc mạng.

Vì vậy, bài tập này nhằm mục đích giúp bạn hiểu

cách tăng độ sâu của mạng

có thể ảnh hưởng đến hiệu suất và tính tổng quát của mô hình.

Vì vậy, bạn sẽ tiếp tục và sửa đổi

mô hình CNN nâng cao hiện có

bằng cách thêm một lớp chập bổ sung vào nó.

Sau đó bạn sẽ huấn luyện mô hình đã sửa đổi

trên tập dữ liệu CIFAR-10.

Tiếp theo, bạn sẽ đánh giá hiệu suất của mô hình

và quan sát mọi cải tiến.

Hãy tóm tắt các bước

mà bạn sẽ hoàn thành cho thử thách này.

Số 1, bạn hãy chắc chắn

rằng bạn nhập các thư viện cần thiết.

Số 2, tải và xử lý trước dữ liệu.

3, sửa đổi mô hình.

4, biên dịch và huấn luyện mô hình.

Và 5, đánh giá mô hình,

và cuối cùng, hãy tiếp tục và lưu mô hình.

Đảm bảo thêm lớp chuẩn hóa hàng loạt

sau lớp chập mới

để ổn định quá trình học tập.

Sử dụng lớp bỏ học sau lớp chập mới

để tránh trang bị quá mức.

Vâng, tôi đã cung cấp cho bạn một đoạn mã khung

rằng bạn sẽ tiến bộ hơn trong thử thách này.

Bạn chỉ cần thêm lớp chập mới

trong hàm create_enhanced_plus_cnn_model

như được mô tả trong mục tiêu.

Để thuận tiện, bạn có thể bắt đầu từ mã bộ xương,

được cung cấp trong tệp Python 02_04_challenge.

Chà, bạn có thể tìm thấy thẻ TODO

để xem bạn sẽ sửa đổi mã ở đâu.

Vì vậy, hãy xem lại mã.

Và đây là tệp thử thách 02_04_challenge.python của chúng tôi.

Và bạn hãy tiếp tục và tìm thấy

chức năng nâng cao_plus_cnn_model,

which is defining an enhanced CNN model

với một lớp chập bổ sung,

và bạn có thể cuộn xuống và bạn sẽ thấy

Thêm lớp chập mới vào đây

nhận xét rằng tôi đã để lại.

Và bạn có thẻ TODO ở đây,

đang thêm một lớp Conv2D bổ sung

với 256 bộ lọc.

Ví dụ: Conv2D, dấu ngoặc đơn mở, 256,

hai x hai, và kích hoạt là relu.

Bây giờ chúng ta sẽ dừng video và tự mình xử lý nó,

và sau đó bạn có thể so sánh kết quả của mình với giải pháp.