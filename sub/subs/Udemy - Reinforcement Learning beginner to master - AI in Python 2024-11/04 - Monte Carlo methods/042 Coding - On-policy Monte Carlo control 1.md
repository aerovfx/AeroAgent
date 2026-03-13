# Lập Trình - Điều Khiển Monte Carlo On-Policy 1

## Nội dung

### 00:00:00 - 00:00:05
Trong video này, chúng ta sẽ triển khai thuật toán đầu tiên có khả năng học từ kinh nghiệm.

### 00:00:06 - 00:00:13
Đó là phương pháp Monte Carlo sẽ đối mặt với môi trường trong một episode hoàn chỉnh, tạo ra các mẫu

### 00:00:13 - 00:00:18
của lợi nhuận mà sau đó chúng ta sẽ sử dụng để cập nhật ước tính của các giá trị Q.

### 00:00:21 - 00:00:26
Để làm điều đó, chúng ta sẽ sử dụng một chiến lược học gọi là on-policy.

### 00:00:27 - 00:00:34
Theo chiến lược này, chúng ta sẽ có một chính sách duy nhất sẽ chịu trách nhiệm cả việc khám phá

### 00:00:34 - 00:00:37
môi trường và tham gia vào quá trình học.

### 00:00:39 - 00:00:43
Thông qua quá trình học này, chúng ta sẽ cố gắng tìm chính sách tối ưu.

### 00:00:44 - 00:00:50
Điều đầu tiên mà chúng ta sẽ làm, như thường lệ, là nhập các thư viện mã mà chúng ta sẽ

### 00:00:50 - 00:00:56
cần trong trường hợp này, chúng sẽ giống như trong phần trước, ngoại trừ giá trị

### 00:00:56 - 00:01:02
hành động (action values) sẽ thay thế hàm giá trị (blood values) mà chúng ta đã sử dụng trong phần trước

### 00:01:03 - 00:01:07
và sẽ cho phép chúng ta nhìn thấy trực quan các giá trị quan trọng của mỗi hành động trong mỗi trạng thái.

### 00:01:09 - 00:01:10
Hãy chạy Lizelle.

### 00:01:14 - 00:01:16
Và bây giờ chúng ta có các công cụ phần mềm cần thiết.

### 00:01:19 - 00:01:25
Tiếp theo, chúng ta phải làm là tạo môi trường, chúng ta sẽ sử dụng lớp mace mà

### 00:01:25 - 00:01:28
sẽ cho phép chúng ta tạo một phiên bản của Maize 5x5.

### 00:01:32 - 00:01:38
Và sau đó, chúng ta sẽ thấy một hình ảnh của môi trường mà chúng ta sẽ đối mặt.

### 00:01:42 - 00:01:44
Hãy chạy ô này và đây là nó.

### 00:01:46 - 00:01:53
Đó là môi trường tương tự mà chúng ta đã giải quyết trong phần trước, một mê cung 5x5 nơi tác

### 00:01:53 - 00:01:59
bắt đầu ở góc trên bên trái và phải tìm đường thoát, nằm ở góc dưới bên phải

### 00:01:59 - 00:01:59
của.

### 00:02:02 - 00:02:08
Trong giờ này, chúng ta sẽ thấy số lượng hành động có sẵn, như chúng ta biết, là bốn và

### 00:02:08 - 00:02:15
mỗi trạng thái được tạo thành bởi sự kết hợp của hai giá trị trong phạm vi từ không đến năm, năm không bao gồm.

### 00:02:19 - 00:02:24
Giá trị đầu tiên là hàng nơi tác đang ở và thứ hai là cột.

### 00:02:27 - 00:02:32
Tiếp theo, chúng ta sẽ làm là tạo bảng Q, đó là bảng giá trị, nơi

### 00:02:32 - 00:02:39
chúng ta lưu trữ ước tính của mình về lợi nhuận kỳ vọng sau khi thực hiện mỗi hành động trong mỗi trạng thái, hãy tạo

### 00:02:39 - 00:02:47
một biến mới gọi là Action Values và sẽ khởi tạo nó bằng hàm Zardoz từ lambi.

### 00:02:48 - 00:02:57
Chúng ta sẽ tạo một bảng 5x5x4 chứa các số không, 5x5, vì

### 00:02:57 - 00:03:04
nhiệm vụ có 25 trạng thái có thể, mỗi sự kết hợp của hàng và cột, và bốn, vì trong mỗi trạng thái

### 00:03:04 - 00:03:06
chúng ta có bốn hành động có sẵn.

### 00:03:06 - 00:03:09
Hãy chạy ô này và bây giờ chúng ta có bảng của mình.

### 00:03:10 - 00:03:15
Tiếp theo, chúng ta cần làm là hiển thị trực quan bảng mà chúng ta vừa tạo.

### 00:03:15 - 00:03:20
Để làm điều đó, chúng ta sử dụng phương thức production values mà chúng ta đã bao gồm trong các file cục bộ.

### 00:03:23 - 00:03:27
Và chúng ta sẽ đưa cho nó đối số này, tất nhiên, là bảng Q.

### 00:03:30 - 00:03:31
Hãy chạy ô này.

### 00:03:32 - 00:03:39
Và đây chúng ta có nó, mỗi hình vuông bên trong bảng này đại diện cho một trạng thái của nhiệm vụ và mỗi

### 00:03:39 - 00:03:45
hình tam giác bên trong hình vuông đó đại diện cho giá trị ước tính của hành động tương ứng.

### 00:03:46 - 00:03:53
Ví dụ, trong trạng thái này, hình tam giác ở đây đại diện cho giá trị của việc thực hiện hành động di chuyển lên

### 00:03:54 - 00:03:55
trong trạng thái.

### 00:03:55 - 00:03:56
Không không.

### 00:03:56 - 00:04:04
Hình tam giác này ở đây đại diện cho giá trị của việc di chuyển xuống và cứ tiếp tục như vậy cho mỗi hành động trong mỗi

### 00:04:04 - 00:04:04
trạng thái.

### 00:04:07 - 00:04:13
Như bạn thấy, ước tính ban đầu của mỗi giá trị là không vì đó là cách chúng ta quyết định tạo bảng,

### 00:04:13 - 00:04:19
nhưng chúng ta có thể bắt đầu với bất kỳ ước tính ban đầu nào thông qua quá trình học sẽ sửa đổi bảng này

### 00:04:19 - 00:04:21
để phản ánh các giá trị tối ưu.

### 00:04:22 - 00:04:25
Tiếp theo, chúng ta phải làm là tạo chính sách.

### 00:04:25 - 00:04:32
Chính sách sẽ luôn là một hàm và chúng ta có thể thiết kế nó để trả về xác suất

### 00:04:32 - 00:04:33
chọn mỗi hành động.

### 00:04:35 - 00:04:41
Hoặc chúng ta có thể làm cho nó đơn giản là chọn một hành động từ các hành động có sẵn, trong trường hợp của chúng ta, chúng ta sẽ thiết kế

### 00:04:41 - 00:04:47
nó sao cho nó chọn hành động vì nó sẽ thuận tiện hơn để làm việc với thuật toán này.

### 00:04:48 - 00:04:51
Vậy hãy định nghĩa hàm này là policy.

### 00:04:52 - 00:04:58
Và chính sách này sẽ nhận một trạng thái làm đầu vào, giống như trong phần trước.

### 00:04:59 - 00:05:05
Nhưng hãy nhớ rằng chính sách này cũng chịu trách nhiệm khám phá môi trường, làm thế nào chúng ta có thể buộc nó

### 00:05:05 - 00:05:06
làm điều đó?

### 00:05:06 - 00:05:12
Chà, điều chúng ta có thể làm là cho nó một xác suất nhất định của việc chọn một hành động ngẫu nhiên.

### 00:05:13 - 00:05:14
Điều này có nghĩa là gì?

### 00:05:16 - 00:05:22
Điều này có nghĩa là chúng ta có thể cho nó 20 phần trăm cơ hội chọn một hành động ngẫu nhiên và 80 phần trăm còn lại

### 00:05:22 - 00:05:28
thời gian chúng ta có thể cho phép nó chọn hành động có giá trị ước tính cao nhất.

### 00:05:28 - 00:05:34
Và để làm điều đó, tất cả những gì chúng ta phải làm là nhìn vào các giá trị Q trong bảng.

### 00:05:35 - 00:05:42
Và chúng ta sẽ làm điều đó để cố gắng tìm xem liệu một số hành động mà chính sách thường không chọn

### 00:05:43 - 00:05:48
có tốt hơn những gì chúng ta cho là tốt trước đó hay không.

### 00:05:48 - 00:05:55
Và bằng cách này, bảng Q sẽ thay đổi để phản ánh hiệu suất của hành động của nó.

### 00:05:56 - 00:06:01
Điều chúng ta sẽ làm là cho bạn giá trị epsilon sẽ xác định xác suất của việc chọn một

### 00:06:01 - 00:06:02
hành động ngẫu nhiên.

### 00:06:03 - 00:06:11
Ví dụ, chúng ta sẽ khởi tạo Epsilon là 0.2, đó là 20 phần trăm và bên trong

### 00:06:11 - 00:06:11
chính sách.

### 00:06:13 - 00:06:21
Điều chúng ta sẽ làm đầu tiên là chọn một số ngẫu nhiên giữa không và một, và chúng ta sẽ làm điều đó bằng cách

### 00:06:21 - 00:06:26
sử dụng hàm random từ module random từ numpy.

### 00:06:27 - 00:06:35
Và nếu số đó nhỏ hơn Epsilon, thì chúng ta sẽ chọn một số nguyên ngẫu nhiên giữa không và bốn.

### 00:06:38 - 00:06:40
Đó là các hành động có sẵn?

### 00:06:45 - 00:06:48
Và 80 phần trăm thời gian còn lại, chúng ta sẽ làm gì?

### 00:06:50 - 00:06:53
Bảng giá trị cho trạng thái cụ thể này.

### 00:06:56 - 00:07:02
AVY sẽ là một vectơ với bốn giá trị, một giá trị cho mỗi hành động trong trạng thái này, và những gì nó sẽ trả về

### 00:07:03 - 00:07:05
là hành động có giá trị Q cao nhất.

### 00:07:08 - 00:07:11
Và nếu có sự hòa giải giữa các hành động có giá trị cao nhất.

### 00:07:13 - 00:07:15
Chúng ta sẽ phá vỡ sự hòa giải đó ngẫu nhiên.

### 00:07:18 - 00:07:20
Nhưng làm thế nào chúng ta có thể làm điều đó?

### 00:07:22 - 00:07:24
Chà, với dòng mã này.

### 00:07:41 - 00:07:45
OK, hãy xem, từng bước một dòng này có nghĩa gì.

### 00:07:47 - 00:07:55
HIV bằng avy marks, những gì nó làm là chỉ ra các hành động có giá trị cao nhất, sau đó

### 00:07:55 - 00:08:02
hàm nonzero sẽ chọn các phần tử thực sự có giá trị cao nhất.

### 00:08:04 - 00:08:07
Và sau đó Choice sẽ chọn một trong số chúng ngẫu nhiên.

### 00:08:09 - 00:08:15
Vậy với dòng mã này, những gì chúng ta trả về là một trong các hành động có giá trị cao nhất.

### 00:08:21 - 00:08:29
Hãy thực thi ô và chúng ta có sẵn chính sách của mình, tiếp theo, như thường lệ, là kiểm tra nếu

### 08:29:00 - 00:08:30
chính sách hoạt động.

### 00:08:30 - 00:08:36
Vậy điều chúng ta sẽ làm là chọn một hành động bằng cách đưa cho chính sách trạng thái không không.

### 00:08:40 - 00:08:44
Và giá trị cho Epsilon, ví dụ, 0.5.

### 00:08:48 - 00:08:51
Và sau đó sẽ hiển thị hành động mà chính sách đã chọn.

### 00:09:08 - 00:09:09
Hãy xem.

### 00:09:10 - 00:09:13
Được rồi, như mong đợi, chính sách của chúng ta hoạt động.

### 00:09:15 - 00:09:24
Tiếp theo, chúng ta muốn làm là nhìn thấy chính sách một cách trực quan, cho việc đó chúng ta sẽ sử dụng hàm policy và

### 00:09:24 - 00:09:26
chúng ta sẽ đưa cho nó bảng Q.

### 00:09:28 - 00:09:35
Trong phần trước, chúng ta đã đưa cho hàm này bảng xác suất, và nó cho chúng ta thấy hành động

### 00:09:35 - 00:09:36
có xác suất cao nhất.

### 00:09:37 - 00:09:42
Ở đây chúng ta sẽ truyền bảng giá trị Q và nó sẽ cho chúng ta biết hành động với

### 00:09:42 - 00:09:43
giá trị Q cao nhất.

### 00:09:43 - 00:09:46
Bạn sẽ cung cấp cho nó cũng một hình ảnh của môi trường.

### 00:09:46 - 00:09:48
Và bây giờ chúng ta sẵn sàng để chạy ô này.

### 00:09:52 - 00:09:59
Khi chúng ta thực thi thuật toán, chính sách sẽ thay đổi cho đến khi nó trở thành chính sách tối ưu

### 00:09:59 - 00:10:02
trong video tiếp theo, chúng ta sẽ bắt đầu thiết kế thuật toán.

### 00:10:02 - 00:10:03
Tôi sẽ gặp bạn ở đó.
