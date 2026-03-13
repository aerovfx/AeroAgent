# Lập Trình - Lặp Chính Sách 4

## Nội dung

### 00:00:00 - 00:00:07
Trong video này, chúng ta sẽ tích hợp hai phần của thuật toán lặp chính sách thành một hàm duy nhất.

### 00:00:11 - 00:00:24
Hãy định nghĩa hàm đó gọi là policy_iteration(), và chúng ta sẽ cung cấp cho nó bốn đối số, đầu tiên

### 00:00:24 - 00:00:26
Là bảng xác suất của chính sách.

### 00:00:27 - 00:00:29
Thứ hai là bảng giá trị.

### 00:00:34 - 00:00:38
Thứ ba là theta: tham số dung sai.

### 00:00:43 - 00:00:47
Và thứ tư là gamma, hệ số chiết khấu để tính lợi nhuận.

### 00:00:52 - 00:00:53
Và bây giờ chúng ta sẽ tích hợp.

### 00:56:00 - 00:01:03
Hai phần của thuật toán. Điều đầu tiên chúng ta sẽ làm là khai báo biến policy_stable là false.

### 01:08:00 - 00:01:17
Và sau đó chúng ta sẽ vào một vòng lặp mà chúng ta sẽ thực hiện miễn là chính sách ổn định.

### 01:21:00 - 00:01:26
Và bên trong vòng lặp, chúng ta sẽ thực hiện phần đánh giá chính sách

### 01:30:00 - 00:01:38
Truyền cho nó đối số là bảng xác suất của chính sách, bảng giá trị trạng thái,

### 01:40:00 - 00:01:41
theta,

### 01:42:00 - 00:01:50
