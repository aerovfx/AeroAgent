# Điều Khiển Monte Carlo On-Policy

## Nội dung

### 00:00:00 - 00:00:04
Trong video này, chúng ta sẽ trình bày phương pháp Monte Carlo đầu tiên mà chúng ta sẽ triển khai,

### 00:00:05 - 00:00:14
phương pháp này theo chiến lược on-policy để duy trì việc khám phá môi trường. Theo chiến lược này,

### 00:00:14 - 00:00:19
chúng ta sẽ định nghĩa một chính sách đôi khi thực hiện một hành động ngẫu nhiên.

### 00:00:19 - 00:00:23
Chính sách này được gọi là epsilon-greedy.

### 00:00:23 - 00:00:29
Trong chính sách này, mỗi hành động sẽ có xác suất được chọn lớn hơn 0.

### 00:00:30 - 00:00:34
Khi đến lúc chọn hành động, chúng ta sẽ tung đồng xu. Với xác suất

### 00:00:34 - 00:00:43
epsilon, chúng ta sẽ chọn hành động ngẫu nhiên và với xác suất 1 trừ epsilon, chúng ta sẽ chọn hành động

### 00:00:43 - 00:00:46
có giá trị Q ước tính cao nhất.

### 00:00:47 - 00:00:53
Do đó, xác suất chọn một hành động mà chúng ta cho là dưới tối ưu dựa trên ước tính

### 00:00:53 - 00:00:59
về giá trị của nó, sẽ là epsilon chia cho số hành động có sẵn.

### 00:01:01 - 00:01:08
Và xác suất chọn hành động mà chúng ta ước tính là tối ưu sẽ là một trừ epsilon

### 00:01:10 - 00:01:13
cộng với xác suất được chọn ngẫu nhiên.

### 00:01:15 - 00:01:21
Với chính sách này, tất cả các hành động sẽ được chọn время от времени, và chúng sẽ có cơ hội chứng minh rằng

### 00:01:21 - 00:01:23
chúng tốt hơn những gì chúng ta mong đợi.

### 00:01:24 - 00:01:32
Hãy xem ví dụ này. Giả sử epsilon bằng 0.2 và có bốn hành động.

### 00:01:33 - 00:01:40
Khi đó một trừ epsilon là 0.8, đây là xác suất chọn hành động có

### 00:01:40 - 00:01:42
giá trị ước tính cao nhất.

### 00:01:43 - 00:01:49
Khi chúng ta chọn một hành động ngẫu nhiên, mỗi hành động có cùng xác suất được chọn.

### 00:01:49 - 00:01:51
0.05.

### 00:01:52 - 00:01:59
Do đó, xác suất chọn hành động tối ưu là 0.85 và xác suất chọn

### 00:01:59 - 00:02:03
mỗi hành động khác là 0.05.

### 00:02:06 - 00:02:07
Đây là thuật toán đầy đủ.

### 00:02:08 - 00:02:16
Nó nhận đầu vào là giá trị của epsilon, xác suất thực hiện hành động ngẫu nhiên và cho gamma,

### 00:02:16 - 00:02:18
hệ số chiết khấu để tính toán lợi nhuận.

### 00:02:19 - 00:02:25
Chính sách sẽ là epsilon-greedy mọi lúc. Mỗi khi chúng ta kết thúc một chu kỳ đánh giá chính sách,

### 00:02:25 - 00:02:30
xác suất chọn mỗi hành động sẽ được cập nhật tương ứng.

### 00:02:32 - 00:02:39
Chúng ta cũng sẽ duy trì một bảng với một mục cho mỗi kết hợp trạng thái và hành động. Trong mỗi mục của bảng này,

### 00:02:39 - 00:02:45
chúng ta sẽ giữ một danh sách với các lợi nhuận mà tác tổng hợp từ kinh nghiệm mà nó thu thập được. Để cập nhật

### 00:02:45 - 00:02:49
các giá trị Q, chúng ta sẽ lấy trung bình các lợi nhuận này.

### 00:02:51 - 00:02:56
Khi tất cả được thiết lập, chúng ta sẽ vào vòng lặp chính của thuật toán,

### 00:02:57 - 00:02:59
mà chúng ta sẽ lặp lại trong một số episode.

### 00:03:00 - 00:03:07
Chúng ta sẽ làm cho tác tương tác với môi trường theo chính sách hiện tại cho đến khi kết thúc

### 00:03:07 - 00:03:14
episode. Khi episode kết thúc, chúng ta sẽ khởi tạo giá trị của lợi nhuận là 0.

### 00:03:16 - 00:03:20
Sau đó, cho mỗi trạng thái được ghé thăm, chúng ta sẽ tính lợi nhuận của nó.

### 00:03:20 - 00:03:27
Đó là tổng các phần thưởng chiết khấu có được sau khi ghé thăm trạng thái đó, và chúng ta sẽ thêm lợi nhuận đó

### 00:03:27 - 00:03:36
vào danh sách tương ứng với trạng thái tham chiếu và hành động được thực hiện. Sau đó, sẽ cập nhật giá trị Q của

### 00:03:36 - 00:03:44
trạng thái và hành động đó như là trung bình của các lợi nhuận đó. Để tính toán lợi nhuận hiệu quả,

### 00:03:45 - 00:03:53
chúng ta sẽ cập nhật các giá trị Q ngược từ lần ghé thăm trạng thái cuối cùng đến lần đầu tiên.

### 00:03:54 - 00:04:01
Bằng cách này, chúng ta có thể cập nhật lợi nhuận tại mỗi thời điểm với quy tắc cập nhật này là phần thưởng có được

### 00:04:01 - 00:04:07
tại thời điểm đó, cộng với lợi nhuận tích lũy đã chiết khấu.

### 00:04:08 - 00:04:10
Đây là một cách hiệu quả để tính

### 00:04:10 - 00:04:16
lợi nhuận cho mỗi trạng thái mà không cần cộng tất cả các phần thưởng cho mỗi trạng thái, nhưng kết quả là

### 00:04:16 - 00:04:17
giống nhau.

### 00:04:18 - 00:04:25
Khi quá trình kết thúc, chúng ta sẽ có một chính sách và các giá trị Q gần với các giá trị tối ưu. Không chính xác là tối ưu

### 00:04:25 - 00:04:29
vì chính sách đôi khi thực hiện một hành động ngẫu nhiên.

### 00:04:31 - 00:04:32
Hãy làm điều đó trong code.
