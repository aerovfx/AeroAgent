## Nội dung

### 00:00:01.000 - 00:00:08.000
Trong video này, chúng ta sẽ tìm hiểu thuật toán học khác biệt theo thời gian thứ hai được gọi là q-learning.

### 00:00:09.000 - 00:00:13.000
Thuật toán này sử dụng chiến lược khám phá chính sách không chính sách.

### 00:00:15.000 - 00:00:22.000
Điều này có nghĩa là chúng ta sẽ có hai chính sách riêng biệt, chính sách thăm dò được gọi là B và

### 00:00:22.000 - 00:00:25.000
một chính sách mục tiêu được gọi là Pi.

### 00:00:26.000 - 00:00:32.000
Tác nhân sẽ chọn các hành động mà nó sẽ thực thi trong môi trường bằng chính sách thăm dò.

### 00:00:33.000 - 00:00:37.000
Và chính sách mục tiêu là chính sách sẽ tối ưu hóa thông qua quá trình học tập.

### 00:00:42.000 - 00:00:46.000
Điều đầu tiên chúng ta cần làm là nhập các thư viện phần mềm mà chúng ta sẽ sử dụng trong phần này

### 00:00:46.000 - 00:00:47.000
thuật toán.

### 00:00:48.000 - 00:00:51.000
Chúng giống như những thư viện mà chúng tôi sử dụng cho saastr.

### 00:00:52.000 - 00:00:54.000
Hãy thực thi ô này.

### 00:00:55.000 - 00:00:56.000
Và bây giờ họ đã sẵn sàng.

### 00:00:57.000 - 00:01:01.000
Như mọi khi, điều tiếp theo chúng ta cần làm là khởi tạo môi trường.

### 00:01:01.000 - 00:01:07.000
Chúng ta sẽ tạo một thể hiện của lớp Mage và lưu trữ nó trong biến.

### 00:01:14.000 - 00:01:17.000
Bây giờ là lúc tạo bảng giá trị.

### 00:01:19.000 - 00:01:22.000
Chúng ta sẽ tạo một biến gọi là giá trị hành động.

### 00:01:27.000 - 00:01:33.000
Và chúng ta sẽ khởi tạo bảng bằng cách sử dụng hàm zeros từ numpy như chúng ta đã làm trước đây.

### 00:01:34.000 - 00:01:45.000
Một lần nữa, chúng ta sẽ tạo cho nó hình dạng 5 x 5 x 4, vì mỗi mục là sự kết hợp của một hàng

### 00:01:45.000 - 00:01:48.000
giá trị, giá trị cột và hành động.

### 00:01:50.000 - 00:01:53.000
Điều tiếp theo chúng ta sẽ làm là tạo chính sách mục tiêu.

### 00:01:56.000 - 00:01:58.000
Như bạn đã biết, chính sách là chức năng.

### 00:01:59.000 - 00:02:04.000
Điều đó trả về một hành động hoặc xác suất liên quan đến từng hành động.

### 00:02:05.000 - 00:02:06.000
Bây giờ đến phần thú vị.

### 00:02:06.000 - 00:02:13.000
Thay vì tạo một chính sách như chúng tôi đã làm ở Saastr, chúng tôi sẽ tạo hai chính sách riêng biệt.

### 00:02:13.000 - 00:02:17.000
Đầu tiên sẽ là chính sách mục tiêu được thể hiện dưới dạng chiếc bánh.

### 00:02:18.000 - 00:02:21.000
Đây là chính sách sẽ tham gia vào quá trình học tập.

### 00:02:21.000 - 00:02:27.000
Hãy khai báo nó như một hàm gọi là chính sách đích lấy trạng thái đầu vào làm đầu vào.

### 00:02:32.000 - 00:02:37.000
Sau đó, chính sách sẽ tra cứu các giá trị cho trạng thái đó.

### 00:02:40.000 - 00:02:43.000
Và chúng ta sẽ lưu trữ chúng trong một biến có tên AV.

### 00:02:47.000 - 00:02:49.000
Sau đó, trong số các giá trị Q này.

### 00:02:51.000 - 00:02:56.000
Chính sách sẽ chọn hành động có giá trị Q cao nhất.

### 00:02:58.000 - 00:03:02.000
Và nếu hòa thì ta sẽ bẻ ngẫu nhiên như trong thuật toán.

### 00:03:03.000 - 00:03:06.000
Để làm được điều đó, chúng tôi sử dụng cùng một dòng mã mà chúng tôi đã sử dụng trong Saastr.

### 00:03:09.000 - 00:03:17.000
Chúng tôi chọn ngẫu nhiên một trong các phần tử được xuất ra bằng phẳng trên 0, đây là những phần tử có giá trị cao nhất

### 00:03:17.000 - 00:03:19.000
giá trị giữa vectơ giá trị q.

### 00:03:27.000 - 00:03:32.000
Hãy thực thi ô này và chính sách mục tiêu của chúng tôi đã sẵn sàng.

### 00:03:33.000 - 00:03:37.000
Bây giờ là lúc chúng ta tuyên bố chính sách thăm dò.

### 00:03:38.000 - 00:03:45.000
Chính sách mục tiêu tham lam đối với các giá trị Q, có nghĩa là nó luôn chọn hành động

### 00:03:45.000 - 00:03:46.000
có giá trị Q cao nhất.

### 00:03:47.000 - 00:03:54.000
Bây giờ chính sách khám phá của chúng ta sẽ là ngẫu nhiên, có nghĩa là mọi hành động sẽ có một xác suất nhất định

### 00:03:54.000 - 00:03:55.000
của việc được chọn.

### 00:03:58.000 - 00:04:00.000
Bây giờ hãy xác định chính sách khám phá.

### 00:04:01.000 - 00:04:07.000
Chúng tôi thực hiện việc đó bằng cách tạo một hàm có chính sách khám phá cùng tên lấy trạng thái đầu vào.

### 00:04:08.000 - 00:04:14.000
Nhưng nó sẽ không làm được gì với trạng thái đó bởi vì loại chính sách khám phá mà chúng ta sắp thực hiện

### 00:04:14.000 - 00:04:14.000
tạo nên.

### 00:04:15.000 - 00:04:17.000
Là một hàm ngẫu nhiên.

### 00:04:18.000 - 00:04:23.000
Điều đó có nghĩa là mỗi khi chính sách thăm dò phải thực hiện một hành động trong môi trường,

### 00:04:23.000 - 00:04:25.000
nó sẽ chọn nó một cách ngẫu nhiên.

### 00:04:26.000 - 00:04:32.000
Và để làm được điều đó, chúng ta sử dụng hàm randint để chọn một số nguyên ngẫu nhiên từ 0 đến 4.

### 00:04:33.000 - 00:04:35.000
Hãy thực thi ô này.

### 00:04:37.000 - 00:04:39.000
Và bây giờ chúng tôi có sẵn cả hai chính sách của mình.

### 00:04:40.000 - 00:04:45.000
Điều tiếp theo chúng ta sẽ làm là hiển thị bảng giá trị Q, như bạn biết, tại thời điểm này

### 00:04:45.000 - 00:04:49.000
có cùng ước tính cho mọi hành động Zero.

### 00:04:49.000 - 00:04:55.000
Và chúng tôi cũng sẽ trình bày chính sách mục tiêu, tại thời điểm này sẽ chọn cùng một hành động trong mọi

### 00:04:55.000 - 00:04:58.000
trạng thái vì tất cả các giá trị Q đều giống nhau.

### 00:04:59.000 - 00:05:00.000
Đó là số không.

### 00:05:02.000 - 00:05:06.000
Tôi sẽ gặp bạn trong video tiếp theo nơi chúng ta sẽ bắt đầu triển khai thuật toán Q-learning.

