## Nội dung

### 00:00:00.000 - 00:00:05.000
Trong video này, chúng ta sẽ tạo mạng lưới thần kinh sẽ sử dụng để ước tính các giá trị Q.

### 00:00:06.000 - 00:00:13.000
Mạng nơ-ron này sẽ lấy trạng thái đầu vào và nó sẽ có hai lớp ẩn.

### 00:00:15.000 - 00:00:22.000
Trong lớp đầu ra, nó sẽ tạo ra ước tính giá trị Q của từng hành động khả dụng.

### 00:00:25.000 - 00:00:26.000
Để tạo ra mạng lưới thần kinh này.

### 00:00:26.000 - 00:00:31.000
Chúng ta sẽ sử dụng một lớp từ thư viện PyTorch có tên là Sequential.

### 00:00:33.000 - 00:00:40.000
Lớp này lấy đầu vào là danh sách các thao tác sẽ được áp dụng tuần tự cho trạng thái mà chúng ta

### 00:00:40.000 - 00:00:41.000
chuyển làm đầu vào.

### 00:00:41.000 - 00:00:48.000
Và bằng cách áp dụng các thao tác tuần tự đó, chúng ta sẽ tạo ra ước tính về giá trị Q.

### 00:00:49.000 - 00:00:54.000
Các hoạt động sẽ chuyển dưới dạng đối số là các lớp tuyến tính.

### 00:00:58.000 - 00:01:00.000
Điều đó sẽ nhân đầu vào.

### 00:01:03.000 - 00:01:06.000
Bằng ma trận tham số.

### 00:01:13.000 - 00:01:20.000
Và ngay sau phép nhân đó, họ sẽ áp dụng phép toán phi tuyến tính vào kết quả.

### 00:01:21.000 - 00:01:29.000
Hoạt động đó sẽ lấy giá trị tối đa giữa 0 và giá trị được tạo bởi phép nhân ma trận.

### 00:01:30.000 - 00:01:36.000
Phép toán đầu tiên mà chúng ta chuyển sang lớp này là phép toán tuyến tính.

### 00:01:39.000 - 00:01:45.000
Its input will have size two because we know that the state has two values.

### 00:01:50.000 - 00:01:54.000
Vì vậy, chúng tôi sẽ cung cấp cho nó trạng thái giá trị mờ, mà như chúng tôi biết là hai.

### 00:01:55.000 - 00:02:01.000
Và đầu ra của lớp này sẽ là một vectơ có 128 mục.

### 00:02:01.000 - 00:02:08.000
Giá trị này chúng ta chọn tùy ý và nó sẽ xác định kích thước của lớp ẩn đầu tiên.

### 00:02:11.000 - 00:02:14.000
Sau đó, chúng ta sẽ áp dụng một thao tác cho kết quả.

### 00:02:14.000 - 00:02:19.000
Một thao tác có tên Relu sẽ phá vỡ tính tuyến tính của thao tác trước đó.

### 00:02:21.000 - 00:02:22.000
Hãy cho nó một dấu phẩy ở đây.

### 00:02:23.000 - 00:02:24.000
Được rồi.

### 00:02:27.000 - 00:02:32.000
Và sau khi áp dụng hai thao tác này, chúng ta sẽ nhận được kết quả đầu ra của lớp ẩn đầu tiên.

### 00:02:34.000 - 00:02:41.000
Bây giờ chúng ta sẽ lặp lại hai thao tác này một lần nữa để tạo đầu ra của ẩn thứ hai

### 00:02:41.000 - 00:02:48.000
lớp, sau đó phép toán tuyến tính sẽ áp dụng nó một lần nữa để tạo ra các ước tính của các giá trị Q.

### 00:02:48.000 - 00:02:51.000
Vì vậy chúng ta sẽ sao chép hai dòng này.

### 00:02:53.000 - 00:02:56.000
Hãy xóa bình luận và thì đấy.

### 00:02:59.000 - 00:03:05.000
Và bây giờ điều duy nhất chúng ta sẽ làm là thay đổi kích thước của đầu vào và đầu ra.

### 00:03:05.000 - 00:03:12.000
Hai thao tác này sẽ chuyển đổi đầu ra của lớp ẩn thứ nhất thành đầu ra của lớp thứ hai

### 00:03:12.000 - 00:03:13.000
một.

### 00:03:13.000 - 00:03:19.000
Hoạt động tuyến tính thứ hai sẽ lấy đầu vào là đầu ra của lớp ẩn thứ nhất nên nó sẽ có

### 00:03:19.000 - 00:03:21.000
kích thước đầu vào là 128.

### 00:03:21.000 - 00:03:28.000
Bây giờ chúng ta sẽ quyết định rằng lớp ẩn thứ hai sẽ có 64 đầu ra.

### 00:03:28.000 - 00:03:32.000
Với hai thao tác này, chúng ta đã tạo ra kết quả đầu ra của lớp ẩn thứ hai.

### 00:03:33.000 - 00:03:35.000
Và cuối cùng, chúng ta sẽ lặp lại.

### 00:03:36.000 - 00:03:38.000
Hoạt động tuyến tính.

### 00:03:39.000 - 00:03:43.000
Điều đó sẽ lấy 64 phần tử làm đầu vào từ lớp ẩn thứ hai.

### 00:03:44.000 - 00:03:51.000
Và nó sẽ tạo ra ba giá trị mà như chúng ta biết, sẽ là ước tính của các giá trị Q.

### 00:03:59.000 - 00:04:01.000
Hãy chạy ô này và thì đấy.

### 00:04:02.000 - 00:04:06.000
Bây giờ chúng ta có mạng lưới thần kinh để ước tính các giá trị Q.

