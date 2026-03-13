## Nội dung

### 00:00:00.000 - 00:00:06.000
Trong video này, chúng ta sẽ bắt đầu triển khai thuật toán RSA, như bạn biết, thuật toán này là một thuật toán tạm thời.

### 00:00:06.000 - 00:00:12.000
phương pháp học tập khác biệt sử dụng chiến lược khám phá phi chính sách.

### 00:00:14.000 - 00:00:21.000
Điều này có nghĩa là chúng ta sẽ sử dụng chính sách tương tự để khám phá môi trường và tham gia

### 00:00:21.000 - 00:00:22.000
trong quá trình học tập.

### 00:00:24.000 - 00:00:28.000
Điều đầu tiên chúng ta cần làm là nhập các thư viện phần mềm mà chúng ta sẽ sử dụng.

### 00:00:30.000 - 00:00:34.000
Trong trường hợp này, chúng ta sẽ cần các thư viện tương tự như chúng ta đã sử dụng trong phần trước.

### 00:00:34.000 - 00:00:36.000
Hãy nhấn shift và nhập.

### 00:00:37.000 - 00:00:39.000
Và bây giờ chúng tôi có sẵn chúng.

### 00:00:41.000 - 00:00:47.000
Bây giờ chúng ta sẽ tạo môi trường và lưu trữ nó trong biến Env.

### 00:00:47.000 - 00:00:51.000
Trong trường hợp này, chúng ta cũng sẽ sử dụng mê cung 5 x 5.

### 00:01:01.000 - 00:01:08.000
Hãy thực thi ô và môi trường đã có sẵn trong biến này.

### 00:01:10.000 - 00:01:14.000
Việc tiếp theo chúng ta cần làm là tạo bảng giá trị.

### 00:01:14.000 - 00:01:22.000
Trong trường hợp này, nó sẽ là bảng giá trị Q, là bảng chứa các giá trị của mọi hành động ở mọi trạng thái.

### 00:01:23.000 - 00:01:29.000
Hãy tạo các giá trị hành động thay đổi và chúng ta sẽ khởi tạo nó bằng hàm số 0 từ hàm numpy

### 00:01:29.000 - 00:01:29.000
thư viện.

### 00:01:30.000 - 00:01:37.000
Như bạn đã biết, hàm này điền vào một mảng các kích thước mà chúng ta chỉ định bằng các số 0 và các kích thước

### 00:01:37.000 - 00:01:45.000
mảng của chúng ta sẽ là 5 x 5 x 4, bởi vì chúng ta có năm hàng, năm cột và có thể có bốn

### 00:01:45.000 - 00:01:45.000
hành động.

### 00:01:47.000 - 00:01:48.000
Hãy thực thi ô.

### 00:01:49.000 - 00:01:51.000
Và bây giờ chúng ta có bảng giá trị Q.

### 00:01:53.000 - 00:01:59.000
Điều cuối cùng chúng ta phải làm trước khi bắt đầu triển khai thuật toán là tạo chính sách.

### 00:01:59.000 - 00:02:02.000
Như bạn đã biết, chúng ta sẽ sử dụng chính sách tham lam epsilon.

### 00:02:02.000 - 00:02:09.000
Điều này có nghĩa là chính sách có xác suất Epsilon sẽ chọn một hành động ngẫu nhiên và có xác suất

### 00:02:09.000 - 00:02:15.000
trừ một epsilon, nó sẽ chọn hành động có giá trị Q ước tính cao nhất.

### 00:02:21.000 - 00:02:28.000
Để xác định chính sách này, chúng ta sẽ tạo một hàm có tên là chính sách và hàm này sẽ lấy

### 00:02:28.000 - 00:02:29.000
một trạng thái làm đầu vào.

### 00:02:31.000 - 00:02:38.000
Và còn có một tham số gọi là epsilon mà chúng ta sẽ đặt mặc định là 0,2.

### 00:02:38.000 - 00:02:44.000
Epsilon là giá trị xác định xác suất chọn một hành động ngẫu nhiên bên trong hàm.

### 00:02:44.000 - 00:02:46.000
Chúng ta sẽ tạo ra một số ngẫu nhiên.

### 00:02:50.000 - 00:02:56.000
Và nếu số ngẫu nhiên đó nhỏ hơn epsilon thì chúng ta sẽ chọn một hành động ngẫu nhiên.

### 00:02:59.000 - 00:03:05.000
Và chúng ta sẽ thực hiện điều đó bằng cách gọi hàm Randint từ mô-đun ngẫu nhiên của thư viện NumPy.

### 00:03:06.000 - 00:03:10.000
Hàm này sẽ chọn một số thấp hơn bốn.

### 00:03:11.000 - 00:03:18.000
Nó có thể chọn 0, 1, 2 hoặc 3, là những con số đại diện cho các hành động có sẵn.

### 00:03:20.000 - 00:03:29.000
Nếu số ngẫu nhiên không nhỏ hơn Epsilon thì chính sách sẽ tra cứu các giá trị của trạng thái

### 00:03:29.000 - 00:03:31.000
nơi nó phải thực hiện hành động.

### 00:03:35.000 - 00:03:40.000
Và chính sách sẽ chọn hành động liên quan đến giá trị cao nhất.

### 00:03:41.000 - 00:03:44.000
Nếu có sự ràng buộc giữa hai hoặc nhiều hành động.

### 00:03:44.000 - 00:03:51.000
Chúng ta sẽ phá vỡ mối ràng buộc này một cách ngẫu nhiên bằng cách sử dụng dòng mã mà chúng ta đã thấy ở phần trước.

### 00:04:02.000 - 00:04:05.000
Chúng ta hãy nhanh chóng nhớ lại biểu thức này có nghĩa là gì.

### 00:04:06.000 - 00:04:08.000
AV bằng AV.

### 00:04:08.000 - 00:04:15.000
Max trả về một vectơ cho biết mỗi hành động có giá trị cao nhất hay không.

### 00:04:17.000 - 00:04:24.000
Sau đó, Flood zero sẽ chọn các phần tử từ vectơ này có giá trị lớn nhất và lựa chọn

### 00:04:24.000 - 00:04:27.000
sẽ chọn ngẫu nhiên một trong các phần tử đó.

### 00:04:30.000 - 00:04:32.000
Và bây giờ chính sách của chúng tôi đã sẵn sàng.

### 00:04:33.000 - 00:04:38.000
Điều tiếp theo chúng ta sẽ làm là hiển thị bảng giá trị một cách trực quan.

### 00:04:40.000 - 00:04:42.000
Trước khi bắt đầu quá trình học tập.

### 00:04:42.000 - 00:04:43.000
Tất cả các giá trị đều bằng không.

### 00:04:45.000 - 00:04:48.000
Điều đó sẽ thay đổi khi chúng tôi thực hiện thuật toán của mình.

### 00:04:50.000 - 00:04:56.000
Và điều cuối cùng chúng ta sẽ làm trước khi bắt đầu triển khai thuật toán là trực quan hóa chính sách.

### 00:05:02.000 - 00:05:07.000
Vì tất cả các hành động đều có cùng giá trị nên chính sách sẽ cung cấp cho chúng ta hành động giống nhau cho mọi trạng thái.

### 00:05:08.000 - 00:05:10.000
Hành động có chỉ số thấp nhất.

### 00:05:13.000 - 00:05:16.000
Trong video tiếp theo, chúng ta sẽ bắt đầu triển khai thuật toán.

### 00:05:16.000 - 00:05:17.000
Tôi sẽ gặp bạn ở đó.

