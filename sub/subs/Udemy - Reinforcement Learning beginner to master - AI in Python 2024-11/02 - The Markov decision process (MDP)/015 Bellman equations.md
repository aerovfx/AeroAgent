# Phương Trình Bellman

## Nội dung

### 00:00:00 - 00:00:05
Trong video này, chúng ta sẽ khám phá các phương trình Bellman, sẽ có tầm quan trọng sống còn khi

### 00:00:05 - 00:00:09
Tìm kiếm chính sách tối ưu để giải quyết các nhiệm vụ điều khiển.

### 00:00:12 - 00:00:17
Đây là phương trình Bellman cho giá trị của một trạng thái.

### 00:00:19 - 00:00:26
Bắt đầu từ định nghĩa giá trị của một trạng thái mà chúng ta biết là lợi nhuận kỳ vọng theo sau

### 00:00:26 - 00:00:35
Chính sách pi từ trạng thái này, chúng ta có thể mở rộng định nghĩa của lợi nhuận để đến biểu thức thứ hai.

### 00:00:37 - 00:00:45
Nếu bạn để ý, biểu thức này, bắt đầu từ số hạng thứ hai bằng với lợi nhuận bắt đầu từ

### 00:00:45 - 00:00:48
Thời điểm tiếp theo, chiết khấu bởi gamma.

### 00:00:50 - 00:00:58
Và do đó chúng ta đến công thức thứ ba. Cuối cùng để đến biểu thức thứ tư, hãy nhớ rằng

### 00:58:00 - 00:01:01
Giá trị của một trạng thái là lợi nhuận kỳ vọng.

### 01:01:00 - 00:01:08
Kỳ vọng toán học này có thể được viết là xác suất thực hiện mỗi hành động theo

### 01:08:00 - 00:01:15
Chính sách đó nhân với lợi nhuận mà chúng ta kỳ vọng nhận được từ việc thực hiện hành động đó.

### 01:16:00 - 00:01:19
Và lợi nhuận đó có thể được biểu diễn là xác suất.

### 01:21:00 - 00:01:28
Của việc đạt được mỗi trạng thái kế thừa có thể nhân với phần thưởng thu được khi đạt được trạng thái đó,

### 01:28:00 - 00:01:31
Cộng với giá trị chiết khấu của trạng thái kế thừa đó.

### 01:34:00 - 00:01:42
Lưu ý rằng chúng ta đã khám phá một mối quan hệ đệ quy giữa giá trị của một trạng thái và các giá trị

### 01:42:00 - 00:01:43
Của các trạng thái khác.

### 01:44:00 - 00:01:50
Điều này sẽ rất hữu ích trong phần tiếp theo để phát triển các thuật toán có khả năng giải quyết các nhiệm vụ điều khiển.

### 01:52:00 - 00:02:00
Quá trình tương tự có thể được thực hiện cho các giá trị q, bắt đầu từ định nghĩa của nó, tức là lợi nhuận kỳ vọng

### 02:00:00 - 00:02:04
Từ việc thực hiện hành động a và sau đó theo chính sách pi.

### 02:05:00 - 00:02:10
Chúng ta có thể mở rộng định nghĩa của lợi nhuận để đến công thức thứ hai.

### 02:11:00 - 00:02:19
Sau đó chúng ta có thể chuyển đổi tất cả các số hạng này thành lợi nhuận chiết khấu bắt đầu từ thời điểm tiếp theo,

### 02:20:00 - 00:02:25
Như chúng ta đã làm cho giá trị của các trạng thái, và chúng ta có thể đến biểu thức này.

### 02:28:00 - 00:02:35
Cuối cùng, chúng ta có thể viết lại lợi nhuận kỳ vọng là xác suất đạt được mỗi trạng thái kế thừa

### 02:36:00 - 00:02:38
Biết rằng chúng ta đã chọn hành động a

### 02:40:00 - 00:02:47
Nhân với phần thưởng đầu tiên thu được khi đạt được trạng thái kế thừa đó, cộng với tổng chiết khấu

### 02:47:00 - 00:02:55
Các giá trị q của mỗi hành động trong trạng thái kế thừa, được tính trọng số bởi xác suất chọn

### 02:55:00 - 00:02:57
Hành động đó bởi chính sách.

### 03:00:00 - 00:03:07
Bằng cách này, chúng ta đã biểu diễn một giá trị q bằng các giá trị q khác.

### 03:09:00 - 00:03:15
Các mối quan hệ đệ quy này sẽ được sử dụng để phát triển các phương pháp sẽ giải quyết các nhiệm vụ điều khiển.
