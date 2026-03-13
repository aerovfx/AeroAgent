## Nội dung

### 00:00:00.000 - 00:00:06.000
Trong video này, chúng ta sẽ xem các phương pháp Montecarlo và các phương pháp khác nhau theo thời gian được kết nối như thế nào

### 00:00:06.000 - 00:00:09.000
với dòng phương pháp n-bước mới này.

### 00:00:11.000 - 00:00:12.000
Hãy quay lại SARSA một lát.

### 00:00:13.000 - 00:00:14.000
Đây là quy tắc cập nhật.

### 00:00:15.000 - 00:00:22.000
Mục tiêu là phần thưởng đầu tiên cộng với ước tính đã chiết khấu về giá trị q của hành động tiếp theo được thực hiện trong

### 00:00:22.000 - 00:00:23.000
trạng thái tiếp theo.

### 00:00:25.000 - 00:00:33.000
Nhưng đây thực sự là số lần quay lại tập được ước tính trong một bước. Đó là giá trị mà chúng tôi hướng tới

### 00:00:34.000 - 00:00:44.000
ước tính của chúng tôi về giá trị q. Vì vậy, trên thực tế, SARSA chỉ là một trường hợp đặc biệt của họ thuật toán n bước

### 00:00:45.000 - 00:00:52.000
nói chung, các phương pháp sai phân thời gian là một trường hợp đặc biệt của phương pháp sai phân thời gian n bước

### 00:00:53.000 - 00:00:56.000
trong đó 'n' bằng một.

### 00:00:58.000 - 00:01:02.000
Nhưng thuật toán SARSA cũng có thể sử dụng bất kỳ mục tiêu nào trong số này.

### 00:01:04.000 - 00:01:10.000
Lợi nhuận được ước tính theo hai bước trong ba hoặc theo 'n'.

### 00:01:12.000 - 00:01:16.000
Nếu chúng tôi làm điều đó, thuật toán kết quả sẽ được gọi là SARSA n bước.

### 00:01:18.000 - 00:01:18.000
Nhưng có một nhược điểm.

### 00:01:21.000 - 00:01:30.000
Nếu 'n' của chúng tôi, đó là số phần thưởng thực sự mà chúng tôi muốn đưa vào ước tính của mình lớn hơn

### 00:01:30.000 - 00:01:38.000
hơn thời lượng thực tế của tập phim thì chúng tôi sẽ có số tiền chiết khấu của mỗi phần thưởng nhận được

### 00:01:39.000 - 00:01:44.000
trong thời gian diễn ra sự kiện, đây là lợi nhuận thực tế chứ không phải ước tính.

### 00:01:45.000 - 00:01:46.000
Điều này nghe có quen không?

### 00:01:47.000 - 00:01:50.000
Chà, điều tương tự cũng xảy ra với phương pháp Montecarlo.

### 00:01:51.000 - 00:01:58.000
Các phương pháp Montecarlo là một thái cực khác của họ này, trong đó chữ 'n' lớn đến mức nó lớn hơn

### 00:01:58.000 - 00:02:01.000
số bước trong tập phim.

### 00:02:02.000 - 00:02:10.000
Điều này có nghĩa là chúng tôi sẽ đưa mọi phần thưởng vào tính toán lợi nhuận của mình và trên thực tế,

### 00:02:10.000 - 00:02:16.000
quy tắc cập nhật này ở đây chỉ đơn giản là quy tắc cập nhật của phương pháp Montecarlo alpha không đổi.

### 00:02:18.000 - 00:02:20.000
Bây giờ chúng ta có thể thấy phương pháp n bước phù hợp ở đâu.

### 00:02:21.000 - 00:02:28.000
Chúng là một nhóm các phương pháp mở rộng và bao gồm các phương pháp Montecarlo và các phương pháp khác nhau theo thời gian.

### 00:02:30.000 - 00:02:38.000
Phương pháp Montecarlo là trường hợp đặc biệt trong đó 'n' lớn hơn thời lượng của tập phim và thời gian

### 00:02:38.000 - 00:02:42.000
các phương pháp khác biệt là một thái cực khác trong đó 'n' bằng một.

### 00:02:44.000 - 00:02:52.000
Bằng cách điều chỉnh giá trị của 'n', chúng ta có thể đẩy phương thức của mình sang họ này hay họ khác.

