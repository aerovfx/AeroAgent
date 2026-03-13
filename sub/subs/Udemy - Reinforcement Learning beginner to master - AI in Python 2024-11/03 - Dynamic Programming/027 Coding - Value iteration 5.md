# Lập Trình - Lặp Giá Trị 5

## Nội dung

### 00:00:00 - 00:00:06
Trong video này, chúng ta sẽ xem kết quả của việc thực thi thuật toán lặp giá trị trong bảng giá trị

### 00:00:06 - 00:00:08
Và chính sách mà chúng ta nhận được.

### 00:00:10 - 00:00:14
Trước tiên, hãy xem các giá trị tối ưu cho mỗi trạng thái.

### 00:00:17 - 00:00:24
Để làm điều đó, hãy gọi hàm plot_values(), truyền cho nó đối số là bảng giá trị trạng thái và

### 00:00:24 - 00:00:27
Khung mà chúng ta đã tạo ở đầu notebook.

### 00:00:31 - 00:00:32
Đây nó là.

### 00:00:34 - 00:00:41
Như bạn biết, trong môi trường này, mọi phần thưởng đều là -1 cho đến khi tác tử tìm thấy lối ra. Vì

### 00:00:41 - 00:00:41
Lý do đó

### 00:00:42 - 00:00:47
Càng gần mục tiêu, giá trị của trạng thái càng cao.

### 00:00:50 - 00:00:57
Và, tất nhiên, giá trị của trạng thái nơi mục tiêu nằm là 0 vì ở trạng thái đó chúng ta

### 00:00:57 - 00:00:59
Không mong đợi nhận thêm bất kỳ phần thưởng nào.

### 01:03:00 - 00:01:10
Mặt khác, chúng ta càng di chuyển xa khỏi mục tiêu, giá trị của các trạng thái càng thấp, cho đến khi

### 01:10:00 - 00:01:14
