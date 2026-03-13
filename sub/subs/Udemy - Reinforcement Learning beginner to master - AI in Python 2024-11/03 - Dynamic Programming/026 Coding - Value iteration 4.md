# Lập Trình - Lặp Giá Trị 4

## Nội dung

### 00:00:00 - 00:00:06
Trong video này, cuối cùng chúng ta sẽ triển khai thuật toán lặp giá trị. Điều đầu tiên chúng ta sẽ

### 00:00:06 - 00:00:13
Làm là định nghĩa hàm mà chúng ta sẽ gọi là lặp giá trị và chúng ta sẽ cung cấp cho nó bốn tham số:

### 00:00:14 - 00:00:16
Thứ nhất là bảng xác suất của chính sách.

### 00:00:18 - 00:00:21
Thứ hai là bảng sẽ chứa các ước lượng giá trị trạng thái.

### 00:00:22 - 00:00:28
Thứ ba là theta, tham số dung sai sẽ cho chúng ta biết khi nào dừng thực thi thuật toán.

### 00:00:30 - 00:00:35
Và thứ tư sẽ là gamma, hệ số chiết khấu để tính lợi nhuận. Theo mặc định, chúng ta sẽ đặt nó

### 00:00:35 - 00:00:36
Là 0,99.

### 00:00:44 - 00:00:50
Và điều tiếp theo chúng ta làm là khởi tạo delta là một giá trị rất cao để đảm bảo rằng chúng ta vào vòng lặp chính.

### 00:50:00 - 00:00:51
Vòng lặp.

### 00:53:00 - 00:01:01
Chúng ta sẽ thực thi vòng lặp miễn là delta lớn hơn theta và bên trong vòng lặp chúng ta sẽ duyệt qua

### 01:01:00 - 00:01:06
Toàn bộ không gian trạng thái, sửa đổi các giá trị ước lượng của chúng.

### 01:08:00 - 00:01:15
Trong các lần lặp đầu tiên, những thay đổi đó sẽ lớn và khi thuật toán tiếp tục lặp lại,

### 01:15:00 - 00:01:20
