# 01 - Deep learning Dự đoán giá trị trọn đời của khách hàng

---

- [Người hướng dẫn] Xin nhắc lại, mục tiêu của ca sử dụng của chúng ta

là dự đoán giá trị lâu dài tiềm năng của khách hàng,

giúp công ty ưu tiên những khách hàng có giá trị cao

và tối ưu hóa các chiến lược tiếp thị.

Chúng tôi tìm thấy trong quá trình phân tích dữ liệu thăm dò

đó là một biểu đồ phân tán

chỉ ra mối tương quan tích cực mạnh mẽ

giữa quyền sử dụng và tổng doanh thu,

đó là cách chúng ta có thể xác định giá trị trọn đời của khách hàng.

Nhưng mặc dù chúng tôi tìm thấy mối tương quan chặt chẽ đó,

tạo mô hình Keras để dự đoán giá trị trọn đời của khách hàng

vẫn có lợi ích lớn.

Vì vậy khi nói đến việc dự đoán

giá trị trọn đời của khách hàng, hay CLV,

Keras có thể tận dụng nhiều loại dữ liệu khách hàng,

bao gồm nhân khẩu học, hành vi mua hàng,

mô hình sử dụng dịch vụ, v.v.

Nó cũng có thể khám phá và tìm hiểu các mẫu trong dữ liệu.

Và mặc dù trường hợp sử dụng của chúng tôi được coi là không phải dữ liệu lớn,

Keras được thiết kế để xử lý các tập dữ liệu lớn

bởi vì nó tận dụng các khuôn khổ cơ bản,

như TensorFlow hay Theano,

được tối ưu hóa để có hiệu suất cao và khả năng mở rộng.

Nhưng quan trọng hơn,

bạn sẽ xây dựng và huấn luyện mô hình tuần tự Keras

chỉ với sáu dòng mã

để có được cơ sở dự đoán của bạn.

Vậy tại sao kiến ​​trúc đơn giản này lại giúp ích cho CLV?

Vâng, đầu tiên, có sự tích hợp của các tính năng đa dạng.

Bằng cách kết hợp nhân khẩu học của khách hàng,

hành vi mua hàng, mô hình sử dụng dịch vụ, v.v.

mô hình đạt được một cái nhìn toàn diện

các yếu tố ảnh hưởng đến CLV

Ngoài ra các tính năng được thiết kế,

ví dụ: tổng số dịch vụ được sử dụng, mức sử dụng trung bình hàng tháng,

cung cấp đầu vào có ý nghĩa nhằm nâng cao khả năng của mô hình

để dự đoán CLV một cách chính xác.

Đây là mã.

Lưu ý rằng chúng ta phải chia dữ liệu

trước khi chúng tôi đưa nó vào mô hình.

Bạn sẽ thấy điều này trong phòng thí nghiệm.

Bây giờ chúng ta hãy thực hiện từng dòng hướng dẫn.

mô hình = Tuần tự.

Vâng, điều này khởi tạo một mô hình tuần tự

cho phép bạn thêm một lớp mỗi lần.

Model.add Dense 64 có nghĩa là chúng tôi đang thêm

một lớp dày đặc, được kết nối đầy đủ với 64 nơ-ron.

input_dim=X_train.shape có nghĩa là chúng tôi đang chỉ định

số lượng tính năng đầu vào

hoặc kích thước mà mô hình mong đợi.

X_train.shape cung cấp số cột trong X_train,

đại diện cho số lượng tính năng đầu vào.

Kích hoạt='relu' lại sử dụng

hàm kích hoạt relu cho tính phi tuyến.

Dense 1 thêm một lớp đầu ra với một nơ-ron duy nhất,

đó là điển hình cho một nhiệm vụ hồi quy

trong đó đầu ra là một giá trị liên tục đơn giản.

Activation='tuyến tính' sử dụng hàm kích hoạt tuyến tính,

phù hợp cho các nhiệm vụ hồi quy

vì nó hiển thị đầu ra để nhận bất kỳ số giá trị thực nào.

Vì vậy, sau đó chúng tôi biên dịch mô hình.

Optimizer=adam là nơi chúng tôi sử dụng trình tối ưu hóa adam,

đó là một thuật toán tối ưu hóa tốc độ học tập thích ứng

nó được thiết kế đặc biệt

để huấn luyện mạng lưới thần kinh sâu.

Loss='mean_squared_error' sử dụng lỗi bình phương trung bình

là hàm mất mát,

thường được sử dụng cho các nhiệm vụ hồi quy.

Nó đo sự khác biệt bình phương trung bình

giữa giá trị dự đoán và giá trị thực tế.

Và sau khi biên dịch mô hình, chúng ta cần huấn luyện mô hình,

và model.fit X_train, y_train

huấn luyện mô hình trên dữ liệu huấn luyện.

epoch=100 chỉ định số lần

thuật toán học tập

sẽ làm việc trong toàn bộ tập huấn luyện,

và ở đây, nó sẽ lặp lại 100 lần.

batch_size=32 chỉ định số lượng mẫu

sẽ được truyền bá qua mạng cùng một lúc,

nói cách khác, được đưa qua mạng theo một đợt,

và sau mỗi đợt, các thông số của mô hình sẽ được cập nhật.

Và xác thực_split=0,2

dành 20% dữ liệu đào tạo để xác nhận.

Điều này giúp đánh giá hiệu quả của mô hình

trên dữ liệu nó chưa từng thấy trong quá trình huấn luyện,

ngăn chặn việc trang bị quá mức và giúp điều chỉnh mô hình.

Và khi mô hình được đào tạo, bạn sẽ thấy kết quả này.

Chúng tôi vẽ một hình dung

để hình dung mô hình đang hoạt động tốt như thế nào.