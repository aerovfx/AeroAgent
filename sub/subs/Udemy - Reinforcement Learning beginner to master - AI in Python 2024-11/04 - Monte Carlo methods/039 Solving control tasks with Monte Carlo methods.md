# Giải Quyết Nhiệm Vụ Điều Khiển Với Phương Pháp Monte Carlo

## Nội dung

### 00:00:00 - 00:00:06
Trong video này, chúng ta sẽ xem cách giải quyết một nhiệm vụ điều khiển sử dụng phương pháp Monte Carlo. Để làm điều đó,

### 00:00:06 - 00:00:12
Chúng ta sẽ sử dụng mẫu mà chúng ta đã thấy trong phần trước gọi là Lặp Chính Sách Tổng Quát.

### 00:00:13 - 00:00:21
Hãy nhớ rằng theo sau mẫu này, hai quá trình luân phiên để đánh giá và cải thiện chính sách,

### 00:00:21 - 00:00:24
Cuối cùng dẫn đến chính sách tối ưu.

### 00:00:26 - 00:00:28
Chúng ta sẽ bắt đầu với bất kỳ chính sách tùy ý nào.

### 00:00:29 - 00:00:37
Tác tử sẽ đối mặt với môi trường sử dụng chính sách ban đầu cho một đợt hoàn chỉnh từ đầu đến cuối.

### 00:00:38 - 00:00:47
Điều này sẽ tạo ra một quỹ đạo từ trạng thái ban đầu cho đến phần thưởng cuối cùng với các phần thưởng mà

### 00:47:00 - 00:00:56
Chúng ta thu được trong quỹ đạo sẽ tính lợi nhuận tại mỗi thời điểm, như bạn thấy trong các công thức này.

### 00:57:00 - 00:01:05
Lợi nhuận tại một thời điểm sẽ là tổng chiết khấu của các phần thưởng bắt đầu tại thời điểm đó.

### 01:08:00 - 00:01:13
Chà, chiến lược của chúng ta là sử dụng các lợi nhuận đó để đánh giá chính sách.

### 01:14:00 - 00:01:18
Và dựa trên hàm giá trị ước lượng, cải thiện chính sách.

### 01:21:00 - 00:01:27
Tuy nhiên, chúng ta có một vấn đề: với lập trình động, chúng ta sẽ cập nhật chính sách sử dụng quy tắc dưới đây.

### 01:29:00 - 00:01:31
