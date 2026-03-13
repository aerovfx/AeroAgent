# Cải Thiện Chính Sách

## Nội dung

### 00:00:00 - 00:00:05
Trong video này, chúng ta sẽ xem phần thứ hai của thuật toán lặp chính sách, nơi chúng ta sẽ cải thiện

### 00:00:05 - 00:00:10
Chính sách hiện tại sử dụng hàm giá trị trạng thái mà chúng ta vừa nhận được trong bước trước.

### 00:00:13 - 00:00:19
Để cải thiện chính sách, chúng ta sẽ tự hỏi câu hỏi sau: liệu chính sách có cải thiện không nếu chúng ta

### 00:00:19 - 00:00:22
Thay đổi hành động được chọn trong trạng thái hiện tại?

### 00:00:23 - 00:00:30
Nói cách khác, cái nào tốt hơn là theo chính sách như hiện tại, hay thay đổi hành động mà chúng ta

### 00:00:30 - 00:00:34
Thực hiện trong trạng thái này và sau đó theo chính sách như hiện tại?

### 00:00:36 - 00:00:43
Để trả lời câu hỏi này, chúng ta sẽ sử dụng hàm giá trị q, đánh giá lợi nhuận kỳ vọng nếu trong

### 00:00:43 - 00:00:48
Trạng thái hiện tại, chúng ta thực hiện một hành động nhất định và sau đó chúng ta theo chính sách.

### 00:00:48 - 00:00:55
Như bạn thấy trong công thức, đó là tổng các xác suất đến một trạng thái tiếp theo cụ thể sau

### 00:55:00 - 00:01:03
Thực hiện hành động đó nhân với phần thưởng thu được khi chúng ta đến trạng thái kế thừa đó, cộng với giá trị chiết khấu

### 01:03:00 - 00:01:05
Của trạng thái đó.

### 01:08:00 - 00:01:15
Mỗi phần sẽ có một giá trị q khác nhau trong trạng thái này. Sau đó, chúng ta sẽ so sánh các giá trị q đó với

### 01:15:00 - 00:01:16
