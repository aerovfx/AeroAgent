# 03 - Áp dụng chính quy L1 vào mô hình deep learning

---

- [Người hướng dẫn] Trong video này, bạn sẽ học cách

để áp dụng Chính quy L1, còn được gọi là

như chính quy hóa Lasso, đến mô hình học sâu

để giảm việc trang bị quá mức,

Tôi sẽ chạy mã trong tệp 02_03e.

Bạn có thể làm theo bằng cách hoàn thành các ô mã trống

trong tệp 02_03b.

Đảm bảo chạy mã đã viết trước đó để nhập

và xử lý trước dữ liệu cũng như xây dựng

và huấn luyện mô hình cơ sở.

Tôi đã làm như vậy rồi.

Vì vậy, chúng ta có thể thấy kết quả từ mô hình trước đó.

Một dấu hiệu rõ ràng của việc trang bị quá mức là sự phân kỳ

trong các chỉ số tổn thất về đào tạo và xác thực,

có thể nhìn thấy trong các đường cong đào tạo ở trên.

Chính quy hóa L1 thêm một hình phạt theo tỷ lệ

đến giá trị tuyệt đối của trọng lượng trong quá trình tập luyện.

Điều này khuyến khích sự thưa thớt, có nghĩa là mô hình học

chỉ dựa vào những tính năng quan trọng nhất.

Để áp dụng chính quy L1

với mô hình cơ sở mà chúng tôi đã tạo ở trên,

chúng tôi đặt đối số kernel_regularizer

trong mỗi lớp ẩn của mạng tới L1.

Trong ngoặc đơn, chúng tôi chuyển vào 0,001.

Điều này có nghĩa là tham số chính quy

được đặt thành 0,001.

Vì vậy, để làm điều này, chúng ta bắt đầu

bằng cách nhập l1 từ tensorflow.keras.regularizers.

Sau đó, chúng tôi xác định mô hình của chúng tôi.

Vì vậy, trong mô hình của chúng tôi, trong mỗi

của các lớp dày đặc, các lớp ẩn,

chúng tôi chỉ định đối số kernel_regularizer

và chúng tôi chỉ định tham số chính quy.

Vì vậy, hãy tiếp tục và chạy mã của chúng tôi.

Tiếp theo chúng tôi biên dịch mô hình chính quy.

Và sau đó chúng tôi đào tạo mô hình chính quy

chống lại dữ liệu đào tạo của chúng tôi.

Vì vậy, chúng tôi sẽ để mô hình ở đây huấn luyện trong 15 kỷ nguyên

chống lại dữ liệu huấn luyện.

Chúng tôi đặt batch_size là 128

và validation_split ở mức 0,1.

Hãy thoải mái sửa đổi các biến này

và những giá trị này trong môi trường của riêng bạn

để xem ảnh hưởng thế nào.

Sau khi quá trình đào tạo hoàn tất, bây giờ chúng ta có thể lập kế hoạch đào tạo

và số liệu mất xác nhận.

Vì vậy chúng ta hãy nhìn vào đó.

Lần này chúng ta thấy rằng hai số liệu giảm giá trị

với tốc độ tương tự khi quá trình đào tạo tiếp tục,

điều này hoàn toàn khác với những gì chúng ta đã thấy trước đây.

Điều này chỉ ra rằng Chính quy hóa L1 có hiệu quả

giúp mô hình khái quát hóa tốt hơn

bằng cách khuyến khích sự thưa thớt trong các trọng số đã học.

Bằng cách xử phạt các giá trị tuyệt đối của trọng số,

Chính quy hóa L1 đẩy nhiều trọng số về 0,

đơn giản hóa mô hình một cách hiệu quả

và giảm nguy cơ trang bị quá mức cho dữ liệu đào tạo lại.

Làm tốt lắm.

Bây giờ bạn đã biết cách sử dụng Chính quy L1

để giảm tình trạng trang bị quá mức trong mô hình học sâu bằng Python.