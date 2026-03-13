# Phương Pháp Monte Carlo

## Nội dung

### 00:00:00 - 00:00:05
Trong video này, chúng ta sẽ xem họ thuật toán đầu tiên sẽ học dựa trên kinh nghiệm

### 00:00:05 - 00:00:07
Được gọi là phương pháp Monte Carlo.

### 00:00:08 - 00:00:15
Đây là họ các phương pháp học giá trị trạng thái tối ưu hoặc giá trị q dựa trên các mẫu kinh nghiệm

### 00:00:16 - 00:00:20
Thu thập bởi tác tử trong khi tương tác với môi trường.

### 00:00:21 - 00:00:26
Ở đầu quá trình học tập, tác tử sẽ theo một chính sách tùy ý.

### 00:00:27 - 00:00:34
Sau đó, tác tử sẽ cố gắng thực hiện nhiệm vụ sử dụng chính sách đó cho đến khi kết thúc đợt, tạo ra

### 00:00:34 - 00:00:36
Dấu vết kinh nghiệm này.

### 00:00:37 - 00:00:40
Dấu vết chứa các trạng thái được thăm.

### 00:00:43 - 00:00:50
Các hành động được thực hiện trong các trạng thái đó và các phần thưởng thu được như một hậu quả.

### 00:00:52 - 00:00:57
Ở cuối đợt, chúng ta sẽ tính lợi nhuận từ mỗi trạng thái được thăm.

### 00:00:58 - 00:01:04
Mà, như bạn biết, là tổng các phần thưởng chiết khấu từ thời điểm chúng ta thăm trạng thái đó cho đến

### 01:04:00 - 00:01:11
Kết thúc đợt. Giá trị của một trạng thái là lợi nhuận kỳ vọng theo sau chính sách hiện tại.

### 01:12:00 - 00:01:19
Vì vậy, mỗi khi chúng ta quan sát một lợi nhuận mới cho một trạng thái cụ thể, chúng ta sẽ cập nhật giá trị ước lượng cho

### 01:19:00 - 00:01:27
Trạng thái đó như trung bình của tất cả các lợi nhuận mà tác tử đã thu thập và bắt đầu trong trạng thái đó.

### 01:29:00 - 01:36:00
Quá trình tương tự có thể được thực hiện sử dụng các giá trị q, ngoại trừ bây giờ chúng ta phải lấy trung bình các lợi nhuận được tạo ra sau
