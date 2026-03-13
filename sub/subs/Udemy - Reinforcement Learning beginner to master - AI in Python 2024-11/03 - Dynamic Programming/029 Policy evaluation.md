# Đánh Giá Chính Sách

## Nội dung

### 00:00:00 - 00:00:05
Trong video này, chúng ta sẽ xem chi tiết hơn phần đầu tiên của thuật toán lặp chính sách trong

### 00:00:05 - 00:00:12
Đó là nơi chúng ta đánh giá chính sách. Nếu bạn nhớ, trong phần trước của khóa học, chúng ta đã giải thích rằng

### 00:00:12 - 00:00:20
Giá trị của một trạng thái theo một chính sách nhất định là lợi nhuận mà chúng ta kỳ vọng nhận được bằng cách bắt đầu từ

### 00:00:20 - 00:00:24
Trạng thái đó và thực hiện các hành động theo chính sách đó.

### 00:26:00 - 00:00:33
Điều này có thể được biểu diễn bằng công thức đầu tiên mà bạn thấy ở đây, đó là xác suất thực hiện mỗi

### 00:33:00 - 00:00:41
Hành động theo chính sách nhân với xác suất của hành động đó, đưa chúng ta đến một trạng thái kế thừa cụ thể.

### 00:42:00 - 00:00:49
Nhân với phần thưởng thu được sau khi đạt được trạng thái tiếp theo, cộng với giá trị chiết khấu của ngày tiếp theo đó.

### 00:51:00 - 00:00:56
Do đó, đó là tổng có trọng số của các kết quả có thể sử dụng chính sách đó.

### 00:57:00 - 00:01:00
Công thức này được gọi là phương trình Bellman.

### 01:01:00 - 00:01:08
Chà, đánh giá chính sách bao gồm việc tìm các giá trị này cho chính sách mà chúng ta có tại một thời điểm nhất định.

### 01:10:00 - 00:01:17
Để làm điều này, chúng ta sẽ theo một quá trình tương tự như thuật toán lặp giá trị mà chúng ta đã thấy.

### 01:18:00 - 00:01:25
Chúng ta sẽ duyệt qua không gian trạng thái, cập nhật ước lượng của mỗi giá trị với quy tắc cập nhật mà bạn thấy dưới đây.

### 01:28:00 - 00:01:34
