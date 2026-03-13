# Giải Quyết Quá Trình Quyết Định Markov

## Nội dung

### 00:00:00 - 00:00:05
Trong video này, chúng ta sẽ xem một cách tổng quát việc tìm giải pháp cho Quá trình quyết định Markov có nghĩa là gì.

### 00:00:05 - 00:00:06
Quá trình.

### 00:00:08 - 00:00:14
Hãy nhớ rằng, giải quyết một nhiệm vụ điều khiển bao gồm việc tối đa hóa lợi nhuận kỳ vọng.

### 00:00:16 - 00:00:25
Giá trị của một trạng thái chính xác là lợi nhuận kỳ vọng đó, vì vậy giải quyết một nhiệm vụ bao gồm việc tối đa hóa giá trị

### 00:00:25 - 00:00:27
Của mọi trạng thái.

### 00:00:28 - 00:00:35
Hoặc tối đa hóa mọi giá trị q. Để tối đa hóa các lợi nhuận đó.

### 00:00:35 - 00:00:42
Chúng ta phải tìm chính sách tối ưu, là chính sách thực hiện các hành động tối ưu trong tất cả các trạng thái.

### 00:00:43 - 00:00:51
Mặt khác, chính sách tối ưu được định nghĩa chính xác là chính sách trong mỗi trạng thái chọn

### 00:00:51 - 00:00:55
Hành động dẫn đến lợi nhuận kỳ vọng cao nhất.

### 00:00:58 - 00:01:05
Sử dụng giá trị của các trạng thái sẽ tính đến các trạng thái mà hành động dẫn đến và lợi nhuận

### 01:05:00 - 00:01:13
Mà chúng ta kỳ vọng nhận được trong trạng thái kế thừa đó. Sử dụng các giá trị q, chúng ta sẽ đơn giản chọn hành động

### 01:14:00 - 00:01:16
Có giá trị q cao nhất.

### 01:19:00 - 00:01:25
Nhưng chúng ta dường như có một vấn đề: để tìm chính sách tối ưu, chúng ta phải biết các giá trị tối ưu và để

### 01:25:00 - 00:01:28
Tìm các giá trị tối ưu, chúng ta phải biết chính sách tối ưu.

### 01:29:00 - 00:01:32
Có vẻ như chúng ta đã gặp phải bài toán gà và trứng.

### 01:34:00 - 00:01:42
Làm thế nào để tìm hai yếu tố này nếu một yếu tố phụ thuộc vào yếu tố kia? Để làm điều đó, hãy xem lại các phương trình Bellman

### 01:42:00 - 00:01:49
Mà chúng ta đã thấy trong video trước và xem điều kiện nào phải giữ khi chính sách và

### 01:49:00 - 00:01:51
Các hàm giá trị là tối ưu.

### 01:52:00 - 00:01:57
Hãy bắt đầu với phương trình tối ưu Bellman cho giá trị của các trạng thái.

### 01:58:00 - 00:02:03
Giá trị tối ưu của một trạng thái là lợi nhuận kỳ vọng theo sau chính sách tối ưu.

### 02:05:00 - 00:02:09
Chính sách tối ưu sẽ luôn chọn hành động tối đa hóa

### 02:10:00 - 00:02:17
Lợi nhuận kỳ vọng và lợi nhuận kỳ vọng là biểu thức này ở đây:

### 02:19:00 - 00:02:24
Xác suất đạt được mỗi trạng thái kế thừa bằng cách thực hiện hành động tối ưu

### 02:26:00 - 00:02:34
Nhân với phần thưởng đạt được bằng cách đạt được trạng thái đó, cộng với giá trị tối ưu chiết khấu của trạng thái đó.

### 02:34:00 - 00:02:34
Trạng thái.

### 02:37:00 - 00:02:45
Đến lượt nó, giá trị q tối ưu cho một hành động trong một trạng thái là tổng có trọng số của các lợi nhuận thu được khi

### 02:45:00 - 00:02:48
Đạt được mỗi trạng thái kế thừa có thể.

### 02:50:00 - 00:02:54
Được tính trọng số bởi xác suất đạt được trạng thái kế thừa đó.

### 02:56:00 - 00:02:58
Lợi nhuận là biểu thức bạn thấy ở đây.

### 03:00:00 - 00:03:08
Được định nghĩa là phần thưởng đạt được khi đạt được trạng thái kế thừa cộng với giá trị q cao nhất trong số các hành động

### 03:08:00 - 00:03:09
Cho trạng thái tiếp theo đó.

### 03:11:00 - 00:03:17
Trong phần tiếp theo, thông qua hai công thức này, chúng ta sẽ phát triển các phương pháp có khả năng tìm chính sách tối ưu

### 03:17:00 - 00:03:19
Và các giá trị một cách lặp đi lặp lại.
