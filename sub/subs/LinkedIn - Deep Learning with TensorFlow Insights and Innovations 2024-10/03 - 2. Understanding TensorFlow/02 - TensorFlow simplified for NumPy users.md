# 02 - TensorFlow được đơn giản hóa cho người dùng NumPy

---

- [Giảng viên] Trong buổi học này,

chúng ta sẽ khám phá cách sử dụng TensorFlow như NumPy.

API của TensorFlow xoay quanh các tensor,

về cơ bản là mảng đa chiều

tương tự như ndarray của NumPy.

Những tensor này rất quan trọng

để tạo các hàm chi phí tùy chỉnh,

số liệu, lớp tùy chỉnh và hơn thế nữa.

Bạn có thể tạo một tensor bằng tf.constant.

Ví dụ: tf.constant,

và sau đó bạn chèn các phần tử của tensor.

Điều này tạo ra một ma trận float 2x3.

Vô hướng cũng có thể được tạo như tf.constant

và bạn nhập vào bộ chia tỷ lệ,

như 42 trong trường hợp của chúng tôi.

Tensor có các thuộc tính như hình dạng và kiểu dữ liệu,

mà bạn có thể truy cập bằng t.shape và t.dtype.

Các tensor lập chỉ mục hoạt động giống như NumPy.

Bạn có thể sử dụng cắt, ví dụ,

t dấu ngoặc đơn mở, dấu ngoặc vuông,

dấu hai chấm chấm một, hai dấu hai chấm.

Vì vậy, điều này xác định phần nào của tensor

bạn muốn truy cập bằng cách sử dụng chức năng lập chỉ mục.

Hoạt động của tensor cũng rất đơn giản,

chẳng hạn như cộng 10 vào tensor, t cộng 10.

Điều này tương đương với việc sử dụng tf.n t dấu phẩy 10.

Các hoạt động khác như tf.square và tf.transpose

cũng có sẵn.

TensorFlow cung cấp tất cả các phép toán cơ bản mà bạn cần,

chẳng hạn như tf.add, tf.multiply,

và tf.square.

Chúng tương đương với các hàm NumPy

như np.add

và np.sum.

Vì vậy có một số khác biệt chính

chúng ta nên chỉ ra ở đây.

Ví dụ, hoán vị một tensor

yêu cầu tf.transpose thay vì t.T trong NumPy.

Ngoài ra, TensorFlows còn giảm bớt các hoạt động

như tf.reduce_sum và tf.reduce_max

có thể có sự khác biệt nhỏ về độ chính xác so với NumPy.

Keras cũng có API cấp thấp được đặt

trong keras.backend.

Các chức năng như hình vuông, exp và sqrt đều có sẵn.

Các hàm này thường gọi

các hoạt động TensorFlow tương ứng.

Nếu bạn muốn mã của bạn có thể di chuyển được

trong quá trình triển khai Keras,

sử dụng các chức năng này.

Ví dụ: sử dụng phần phụ trợ của Keras,

bạn có thể viết k.square

(K.transpose(t)) + 10.

Tensors hoạt động tốt với Numpy.

Bạn có thể tạo Tensor từ mảng NumPy

sử dụng dấu ngoặc đơn mở tf.constant np.array,

và bạn chèn mảng.

Chuyển đổi Tensors trở lại mảng Numpy rất đơn giản

với t.numpy

hoặc np.array(t).

Bạn cũng có thể áp dụng các thao tác TensorFlow

trực tiếp trên mảng NumPy,

chẳng hạn như tf.square, dấu ngoặc đơn mở np.array,

và bạn chèn mảng.

Chuyển đổi loại có thể ảnh hưởng đáng kể đến hiệu suất.

TensorFlow không thực hiện chuyển đổi loại tự động.

Sử dụng tf.cast khi cần thiết.

Ví dụ: tf.constant(40.,dtype=tf.float64)

có thể được truyền bằng tf.cast(t2, tf.float32).

Các biến trong TensorFlow giống như các Tensor hằng số,

nhưng chúng có thể được sửa đổi.

Sử dụng tf.variable

cho các giá trị thay đổi trong quá trình đào tạo.

Các biến có thể được cập nhật bằng các phương thức

như gán, gán_add và hơn thế nữa.

Ví dụ: bạn có thể nhân đôi giá trị của biến V

sử dụng v.sign(2*v).

TensorFlow hỗ trợ một số cấu trúc dữ liệu khác.

Ví dụ: Các tensor thưa thớt,

mà chúng ta có thể truy cập bằng cách gõ tf.SparseTensor

biểu diễn Tensors với nhiều số 0 một cách hiệu quả.

Tiếp theo, mảng Tensor.

tf.TensorArray.

Đây là danh sách các Tensors.

Tiếp theo là tensor Ragged.

Chúng tôi truy cập nó bằng cách gõ tf.RaggedTensor.

Chúng đại diện cho danh sách các tensor có độ dài khác nhau.

Tiếp theo là String Tensors, tf.string.

Họ xử lý các chuỗi byte và chuỗi Unicode.

Bộ và hàng đợi cũng được hỗ trợ

cho các hoạt động dữ liệu nâng cao hơn.

Với những thao tác này, các biến

và cấu trúc dữ liệu theo ý của bạn,

bây giờ bạn đã sẵn sàng để tùy chỉnh mô hình của mình

và huấn luyện thuật toán sử dụng TensorFlow

theo những cách mà bạn cảm thấy quen thuộc

nếu bạn đến từ nền NumPy.