## Nội dung

### 00:00:00.000 - 00:00:05.000
Trong phần này, chúng ta sẽ tìm hiểu cách giải các tác vụ điều khiển có không gian trạng thái liên tục.

### 00:00:06.000 - 00:00:12.000
Cho đến nay, chúng ta đã học được các thuật toán học tăng cường cơ bản bằng cách sử dụng một tác vụ điều khiển duy nhất.

### 00:00:12.000 - 00:00:14.000
Mê cung năm x năm.

### 00:00:14.000 - 00:00:20.000
Trong nhiệm vụ này, trạng thái là vị trí của tác nhân được xác định bởi chỉ mục hàng và cột.

### 00:00:21.000 - 00:00:27.000
Vì có năm giá trị có thể có cho hàng và năm giá trị có thể có cho cột, nên tổng cộng,

### 00:00:27.000 - 00:00:32.000
có 25 cách kết hợp hàng và cột.

### 00:00:32.000 - 00:00:35.000
Đó là 25 trạng thái có thể.

### 00:00:37.000 - 00:00:39.000
Bây giờ hãy nhìn vào nhiệm vụ kiểm soát này.

### 00:00:39.000 - 00:00:45.000
Người đại diện là người chơi gôn phải dùng gậy đánh bóng vào lỗ.

### 00:00:45.000 - 00:00:49.000
Bóng càng ném xa thì cú sút sẽ càng không chính xác.

### 00:00:51.000 - 00:00:59.000
Tác vụ này có hàm giá trị trạng thái sau đây, hàm giá trị trạng thái tối ưu trên trục x.

### 00:01:00.000 - 00:01:03.000
Bạn có thể thấy các giá trị khác nhau mà trạng thái có thể nhận.

### 00:01:03.000 - 00:01:07.000
Trạng thái là vị trí của quả bóng trên này.

### 00:01:08.000 - 00:01:15.000
Đường thẳng và các giá trị hợp lệ nằm trong khoảng âm mười và dương mười.

### 00:01:15.000 - 00:01:22.000
Trên trục y, bạn có thể thấy giá trị tối ưu có thể có cho từng trạng thái.

### 00:01:23.000 - 00:01:28.000
Như bạn có thể thấy, trạng thái càng gần lỗ trống thì giá trị của nó càng cao.

### 00:01:30.000 - 00:01:35.000
Đó là vì người đại diện được thưởng khi đưa bóng vào lỗ.

### 00:01:36.000 - 00:01:41.000
Nhưng bây giờ chúng tôi gặp một vấn đề vì chúng tôi không thể giải quyết nhiệm vụ này bằng các phương pháp mà chúng tôi đã thấy cho đến nay.

### 00:01:42.000 - 00:01:49.000
Bởi vì các phương thức này sử dụng bảng giá trị trong đó chúng lưu trữ giá trị của các trạng thái hoặc các giá trị.

### 00:01:50.000 - 00:01:56.000
Vấn đề là các nhiệm vụ điều khiển với không gian trạng thái liên tục có vô số trạng thái có thể xảy ra.

### 00:01:57.000 - 00:02:03.000
Nếu chúng ta lưu trữ một mục trong bảng cho mỗi trạng thái có thể, chúng ta sẽ cần một bảng có vô hạn

### 00:02:03.000 - 00:02:04.000
ký ức.

### 00:02:06.000 - 00:02:08.000
Vậy chúng ta có những lựa chọn nào?

### 00:02:09.000 - 00:02:13.000
Vâng, nói chung, chúng tôi có hai giải pháp khả thi.

### 00:02:14.000 - 00:02:19.000
Việc đầu tiên là chuyển trạng thái thành một định dạng mà chúng ta có thể làm việc.

### 00:02:19.000 - 00:02:22.000
Đây là giải pháp mà chúng ta sẽ khám phá trong phần này.

### 00:02:23.000 - 00:02:27.000
Trong các phần sau, chúng ta sẽ khám phá tùy chọn thứ hai trong số các tùy chọn này.

### 00:02:28.000 - 00:02:33.000
Bao gồm việc sử dụng các thuật toán có khả năng xử lý các không gian trạng thái liên tục.

### 00:02:36.000 - 00:02:37.000
Tùy chọn đầu tiên.

### 00:02:37.000 - 00:02:44.000
Sửa đổi các trạng thái để làm cho chúng có thể sử dụng được bằng các thuật toán cổ điển của chúng tôi có nghĩa là chuyển đổi một phạm vi liên tục

### 00:02:44.000 - 00:02:48.000
các giá trị thành một tập hữu hạn các trạng thái.

### 00:02:49.000 - 00:02:53.000
Để đạt được điều này trong phần này, chúng ta sẽ phát triển hai kỹ thuật.

### 00:02:54.000 - 00:02:57.000
Tập hợp trạng thái và mã hóa khối.

### 00:02:58.000 - 00:03:01.000
Trong video tiếp theo, chúng ta sẽ bắt đầu với việc tổng hợp trạng thái.

