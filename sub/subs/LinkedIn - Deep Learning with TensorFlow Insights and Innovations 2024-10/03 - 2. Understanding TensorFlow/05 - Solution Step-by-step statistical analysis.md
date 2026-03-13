# 05 - Giải pháp Phân tích thống kê từng bước

---

(nhạc cụ sôi động)

- [Người hướng dẫn] Bây giờ chúng ta hãy cùng nhau tìm hiểu cách giải

và xem chúng ta có thể giải quyết thách thức này như thế nào.

Đầu tiên, chúng ta sẽ tiếp tục với mã thử thách của mình,

và mã kết thúc sẽ được lưu trữ trong 02_05_solution.py.

Vì vậy, nếu chúng ta muốn mở nó ra từ đầu

nó sẽ trông giống như thế này.

Và nếu bạn chỉ mở cái này ra

thiết bị đầu cuối cũng có thể sạch sẽ.

Vì vậy, bây giờ chúng ta hãy tìm hiểu cách giải quyết thách thức này.

Trước tiên chúng ta sẽ bắt đầu lại từ mã thử thách của mình.

Tìm thư mục src từ khung bên trái

và nhấp vào tệp Python 02_04_challenge.

Trước hết chúng ta sẽ tìm hiểu giải pháp ở đây,

và mã hoàn thành sẽ có sẵn

trong tệp Python 02_05_solution.

Vì vậy, trước tiên chúng ta cần đảm bảo rằng tensor là

ở định dạng dấu phẩy động trước khi chúng tôi cố gắng chuẩn hóa nó.

Điều này rất quan trọng vì việc chia số nguyên

có thể không mang lại giá trị chuẩn hóa chính xác,

và đây là cách chúng ta có thể làm điều đó.

Vì vậy, chúng ta sẽ tiếp tục và tiếp tục sau khi tạo

một tenxơ TensorFlow có hình dạng bốn x bốn,

chúng ta sẽ bắt đầu bằng cách nói truyền tensor

nổi trước khi bình thường hóa.

Và sau đó chúng ta hãy tiếp tục và làm điều đó,

vì vậy chúng ta sẽ nói tensor bằng, chúng ta sẽ sử dụng tf.cast,

và sau đó chúng ta sẽ có dấu phẩy tensor tf.float32.

Vì vậy, điều này sẽ đảm nhiệm việc tạo

một float trước khi bình thường hóa.

Tiếp theo, chúng ta sẽ tiếp tục chuẩn hóa tensor

để có các giá trị từ 0 đến một.

Vì vậy, để làm được điều đó, chúng ta có thể loại bỏ nhiệm vụ và gợi ý

khỏi thử thách và bắt đầu bình thường hóa nó.

Vì vậy, normalized_tensor trong trường hợp này sẽ là

bằng tensor chia cho 9,0.

Vì vậy, để chuẩn hóa tensor chúng ta chia tất cả các phần tử

bằng giá trị tối đa trong phạm vi ban đầu của chúng tôi, là 9,0.

Vì vậy, sau khi giải quyết xong vấn đề đó, bây giờ chúng ta có thể tính giá trị trung bình

và độ lệch chuẩn

như họ đã được chúng tôi yêu cầu trong thử thách.

Vì vậy, hãy tiếp tục và chăm sóc những điều đó

bằng cách sử dụng các hàm tích hợp TensorFlow.

Vì vậy, chúng ta sẽ tiếp tục và bắt đầu với ý nghĩa.

Vì vậy, chúng ta sẽ loại bỏ nhiệm vụ ở đây và tính giá trị trung bình

và độ lệch chuẩn của tensor chuẩn hóa.

Vì vậy, để làm điều đó chúng ta sẽ sử dụng một hàm tích hợp

được gọi là tf.reduce_mean,

và sau đó chúng ta sẽ cung cấp tensor chuẩn hóa làm đầu vào.

Và thế là xong, chúng ta đã tính toán giá trị trung bình.

Bây giờ, tiếp theo chúng ta sẽ tiếp tục

và tính độ lệch chuẩn.

Vì vậy, đây là giá trị trung bình của tensor chuẩn hóa,

và đây là phép tính độ lệch chuẩn

của tensor chuẩn hóa tiếp theo.

Vì vậy, chúng ta hãy tiếp tục và làm điều đó.

Và một lần nữa, chúng ta sẽ sử dụng một hàm tích hợp cho việc đó,

vì vậy độ lệch chuẩn sẽ bằng tf.math.reduce_std.

Vì vậy, điều này sẽ cho chúng ta độ lệch chuẩn,

và chúng ta sẽ nhập tensor chuẩn hóa vào đây.

Vậy là xong, nó sẽ giải quyết giải pháp của chúng ta.

Vì vậy, bạn có thể tiếp tục và chạy cái này ở đây,

hoặc bạn có thể chọn đi tới tệp giải pháp,

đó sẽ là giải pháp tương tự

giống như chúng ta đã vượt qua mã thử thách,

và bạn có thể tiếp tục và chạy nó.

Hãy tiếp tục và phóng to màn hình terminal ở đây.

Và sau đây, hãy cùng tìm hiểu xem giải pháp này làm được gì.

Trước hết, chúng ta bắt đầu bằng việc đúc tensor.

Chúng tôi bắt đầu bằng cách sử dụng tensor số nguyên của chúng tôi

tới tensor dấu chấm động.

Bước này rất quan trọng vì nó cho phép chúng ta thực hiện

sự phân chia cần thiết để bình thường hóa

mà không làm mất đi độ chính xác.

Vì vậy, chúng ta đã thực hiện phép đúc này ở đây, tensor bằng

tới tf.cast tensor dấu phẩy tf.float32.

Bước này rất quan trọng vì nó cho phép chúng ta thực hiện

sự phân chia cần thiết để bình thường hóa

mà không làm mất đi độ chính xác.

Tiếp theo, chúng tôi thực hiện việc chuẩn hóa,

vì vậy chúng ta chuẩn hóa tensor bằng cách chia mỗi phần tử cho 9,0.

Điều này chia tỷ lệ tất cả các giá trị nằm trong khoảng từ 0 đến 1,

đó là những gì chúng tôi muốn

Tiếp theo, chúng tôi tiến hành tính giá trị trung bình

và độ lệch chuẩn.

Khi tính giá trị trung bình và độ lệch chuẩn

sử dụng các hàm less_mean và less_std của TensorFlow

nó trở nên thực sự đơn giản

bởi vì chúng tôi đã tận dụng được các chức năng tích hợp sẵn.

Các hàm này tính toán hiệu quả số liệu thống kê cần thiết

trên toàn bộ tensor.

Và bạn có nó.

Giải pháp đáp ứng hiệu quả yêu cầu thách thức

và thể hiện các hoạt động TensorFlow quan trọng.

Vì vậy, chúng ta có thể tiếp tục và xem xét

các bản in trong thiết bị đầu cuối.

Đầu tiên, chúng ta in tensor ban đầu mà chúng ta đã tạo.

Sau đó, chúng tôi tiếp tục và in tensor chuẩn hóa,

có giá trị từ 0 đến 9,0.

Sau đó chúng tôi tiến hành in giá trị trung bình được tính toán,

theo sau là độ lệch chuẩn

mà chúng ta có thể thấy trong thiết bị đầu cuối.

Vì vậy, trong bài tập này chúng ta đã học cách chuẩn hóa tensor

và tính toán các số liệu thống kê cơ bản như giá trị trung bình

và độ lệch chuẩn.

Chúng tôi đã thực hiện tất cả những điều đó bằng TensorFlow.

Vì vậy, những thử thách thực hành kiểu này rất tuyệt vời

để củng cố các khái niệm chúng tôi đã đề cập

và mang lại cho bạn trải nghiệm viết mã thực tế.

Hãy nhớ rằng, việc thành thạo TensorFlow chủ yếu là thực hành.

Bạn càng chơi nhiều với các tensor và hàm này

bạn sẽ càng trở nên thoải mái hơn.

Hãy tiếp tục thử nghiệm và tôi sẽ gặp bạn trong buổi tiếp theo

nơi chúng ta sẽ khám phá những chủ đề nâng cao hơn nữa.