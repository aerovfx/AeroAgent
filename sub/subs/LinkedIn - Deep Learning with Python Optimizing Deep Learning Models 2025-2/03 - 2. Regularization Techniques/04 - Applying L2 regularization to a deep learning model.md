# 04 - Áp dụng chuẩn hóa L2 vào mô hình deep learning

---

- [Người hướng dẫn] Trong video này,

bạn sẽ học cách áp dụng Chính quy L2,

còn được gọi là Chính quy hóa sườn núi,

sang mô hình học sâu để giảm hiện tượng trang bị quá mức,

Tôi sẽ viết mã trong tệp 02_04e.

Bạn có thể làm theo bằng cách hoàn thành các ô mã trống

trong tệp 02_04b.

Đảm bảo chạy mã đã viết trước đó

để nhập và xử lý trước dữ liệu

cũng như xây dựng và huấn luyện mô hình cơ sở.

Tôi đã làm như vậy rồi.

Nhìn vào kết quả của mô hình cơ sở,

chúng ta có thể thấy rằng có một dấu hiệu rõ ràng về việc trang bị quá mức.

Chúng ta thấy sự khác biệt

trong các chỉ số tổn thất về đào tạo và xác thực,

có thể nhìn thấy trong các đường cong mất huấn luyện và xác nhận

mà chúng ta thấy ở đây

Để giúp giảm thiểu việc trang bị quá mức trong mô hình cơ sở này,

hãy áp dụng Chính quy L2.

Chính quy L2 thêm một hình phạt

tỉ lệ thuận với bình phương của các trọng số.

Điều này không khuyến khích trọng lượng lớn,

giúp mô hình khái quát hóa tốt hơn.

Để áp dụng Chính quy L2 cho mô hình cơ sở,

chúng tôi đặt đối số kernel_regularizer

trong mỗi lớp ẩn của mạng.

Vì vậy, trong ví dụ này,

chúng tôi đặt tham số chính quy thành 0,001.

Trước khi chúng ta bắt đầu,

chúng tôi nhập L2 từ tensorflow.keras.regularizers.

Sau đó, chúng tôi xác định mô hình của chúng tôi.

Trong mỗi lớp dày đặc,

chúng tôi chỉ định kernel_regularizer là L2

và cung cấp cho nó một giá trị tham số.

Vì vậy, hãy tiếp tục và chạy mã của chúng tôi.

Sau khi chúng ta xác định xong mô hình của mình,

bây giờ chúng ta cần biên dịch nó,

đó là những gì chúng ta làm trong bước tiếp theo

bằng cách gọi phương thức biên dịch của mô hình của chúng tôi.

Sau đó, bây giờ chúng tôi áp dụng mô hình cho dữ liệu đào tạo của mình.

Vì vậy, chúng tôi gọi phương pháp phù hợp để làm như vậy.

Chúng tôi chỉ định số kỷ nguyên là 15,

vì vậy nó sẽ phải trải qua 15 lần huấn luyện lặp lại.

Chúng tôi chỉ định batch_size là 128

và validation_split là 0,1.

Điều này có nghĩa là mô hình mỗi lần

sẽ sử dụng 90% dữ liệu đào tạo để đào tạo

và 10% để xác nhận.

Vì vậy, hãy dành chút thời gian để hoàn thành tất cả 15 lần lặp

của 15 kỷ nguyên.

Và sau đó chúng ta sẽ tiếp tục và lên kế hoạch

các chỉ số mất mát về đào tạo và xác thực để xem tác động

của Chính quy hóa L2 đã có trên mô hình của chúng tôi.

Được rồi, bây giờ chúng ta có thể tiếp tục và lên kế hoạch

các số liệu xác nhận và tổn thất đào tạo.

Và lần này chúng ta thấy

rằng các chỉ số mất đi trong quá trình đào tạo và xác thực của mô hình

có xu hướng giảm với tốc độ tương tự

trong suốt quá trình đào tạo.

Đây là một dấu hiệu mạnh mẽ

rằng L2 Regularization đang giảm thiểu việc trang bị quá mức một cách hiệu quả

bằng cách ngăn cản mô hình dựa quá nhiều vào

trên các giá trị trọng lượng lớn.

Công việc tuyệt vời.

Bây giờ bạn đã biết cách sử dụng Chính quy L2

để giảm tình trạng trang bị quá mức trong mô hình học sâu bằng Python.