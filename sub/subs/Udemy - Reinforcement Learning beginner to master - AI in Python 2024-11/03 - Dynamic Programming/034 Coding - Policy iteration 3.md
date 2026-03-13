# Lập Trình - Lặp Chính Sách 3

## Nội dung

### 00:00:00 - 00:00:06
Trong video này, chúng ta sẽ triển khai phần thứ hai của thuật toán lặp chính sách được gọi là

### 00:00:06 - 00:00:08
Cải thiện chính sách.

### 00:00:12 - 00:00:18
Điều đầu tiên chúng ta sẽ làm là định nghĩa hàm sẽ chứa phần này của thuật toán và chúng ta sẽ

### 00:00:18 - 00:00:26
Định nghĩa nó là cải thiện chính sách, và hàm này sẽ lấy ba đối số.

### 00:00:27 - 00:00:30
Đầu tiên sẽ là bảng xác suất hành động.

### 00:00:33 - 00:00:37
Thứ hai sẽ là bảng giá trị trạng thái.

### 00:00:37 - 00:00:44
Và cuối cùng sẽ là gamma, mà như bạn biết, là hệ số chiết khấu để tính lợi nhuận.

### 00:00:49 - 00:00:50
Hãy tạo một chút không gian.

### 00:56:00 - 00:01:05
Và điều tiếp theo chúng ta sẽ làm là khởi tạo biến này ở đây gọi là policy_stable và chúng ta sẽ khởi tạo

### 01:05:00 - 00:01:05
Nó.

### 01:05:00 - 00:01:06
Là true.

### 01:08:00 - 00:01:17
Chúng ta viết policy_stable=True, sau đó chúng ta sẽ vào vòng lặp này sẽ lặp lại cho mỗi trạng thái hợp lệ

### 01:17:00 - 00:01:17
