## Nội dung

### 00:00:00.000 - 00:00:07.000
Trong video này, chúng ta sẽ giải quyết nhiệm vụ xe leo núi bằng thuật toán RSA và các trạng thái tổng hợp.

### 00:00:08.000 - 00:00:15.000
Điều đầu tiên chúng ta sẽ làm là so sánh không gian trạng thái trong môi trường đã sửa đổi và

### 00:00:15.000 - 00:00:16.000
bản gốc.

### 00:00:16.000 - 00:00:18.000
Hãy thực thi hai ô này.

### 00:00:21.000 - 00:00:24.000
Và ở đây bạn có thể thấy chúng cạnh nhau.

### 00:00:24.000 - 00:00:30.000
Tác vụ ban đầu có một không gian trạng thái bao gồm các giá trị dấu phẩy động.

### 00:00:32.000 - 00:00:38.000
Đầu tiên trong số đó là vị trí của xe theo trục ngang và thứ hai là vận tốc của nó.

### 00:00:39.000 - 00:00:47.000
Không gian trạng thái mới có thể nhận 20 giá trị có thể có cho vị trí của ô tô và 20 giá trị cho tốc độ của nó.

### 00:00:48.000 - 00:00:53.000
Và trạng thái bao gồm sự kết hợp của hai giá trị nguyên.

### 00:00:54.000 - 00:01:02.000
Cái đầu tiên là chỉ số về vị trí giỏ hàng trong 20 trạng thái tổng hợp này và cái thứ hai là

### 00:01:02.000 - 00:01:06.000
chỉ số tốc độ ở 20 trạng thái tổng hợp đó.

### 00:01:07.000 - 00:01:11.000
Điều tiếp theo chúng ta sẽ làm là tạo bảng giá trị Q.

### 00:01:11.000 - 00:01:19.000
Như chúng ta biết, trạng thái tổng hợp chứa 20 khả năng cho mỗi giá trị và chúng ta có sẵn ba khả năng

### 00:01:19.000 - 00:01:20.000
hành động.

### 00:01:20.000 - 00:01:25.000
Quay lại, không di chuyển chút nào hoặc tiến về phía trước.

### 00:01:25.000 - 00:01:30.000
Vì vậy, với các thứ nguyên này, chúng ta sẽ tạo bảng giá trị Q của mình.

### 00:01:32.000 - 00:01:35.000
Điều tiếp theo chúng ta sẽ làm là tạo chính sách.

### 00:01:35.000 - 00:01:42.000
Và bởi vì chúng tôi sẽ sử dụng thuật toán tìm kiếm nên nhân viên sẽ thực hiện khám phá chính sách

### 00:01:42.000 - 00:01:42.000
chiến lược.

### 00:01:42.000 - 00:01:49.000
Vì vậy, chúng tôi biết rằng chính sách mà chúng tôi tạo ra phải có khả năng khám phá và tham gia vào quá trình học tập

### 00:01:49.000 - 00:01:49.000
quá trình.

### 00:01:49.000 - 00:01:56.000
Vì lý do đó, chúng ta sẽ sử dụng chính sách tham lam epsilon giống như chính sách chúng ta đã sử dụng ở phần trước.

### 00:01:56.000 - 00:01:56.000
phần.

### 00:01:56.000 - 00:01:58.000
Hãy chạy tế bào này.

### 00:02:01.000 - 00:02:05.000
Bây giờ hãy chuyển sang thuật toán và chạy nó.

### 00:02:06.000 - 00:02:11.000
Nó sẽ giống hệt với cách triển khai mà chúng ta đã thực hiện trong phần về sự khác biệt về thời gian

### 00:02:11.000 - 00:02:12.000
phương pháp.

### 00:02:14.000 - 00:02:17.000
Chúng tôi chỉ thực hiện một vài thay đổi.

### 00:02:17.000 - 00:02:23.000
Chúng tôi đã tạo một từ điển có tên Thống kê, nơi chúng tôi sẽ lưu giữ kết quả chạy thuật toán.

### 00:02:23.000 - 00:02:26.000
Đó là, tập phim trở lại.

### 00:02:28.000 - 00:02:37.000
Và trong vòng lặp chính, chúng tôi đã sử dụng hàm tqdm để bao bọc phần khai báo của vòng lặp và sẽ hiển thị

### 00:02:37.000 - 00:02:43.000
thanh tiến trình sẽ cho chúng ta biết thuật toán đã hoàn thành bao nhiêu lần lặp và bao nhiêu lần lặp

### 00:02:43.000 - 00:02:44.000
bên trái.

### 00:02:47.000 - 00:02:49.000
Hãy thực hiện thuật toán này.

### 00:02:49.000 - 00:02:52.000
Và như bạn có thể thấy, việc này sẽ mất vài phút.

### 00:02:56.000 - 00:02:57.000
Tôi sẽ gặp bạn khi nó xong việc.

