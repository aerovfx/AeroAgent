## Nội dung

### 00:00:00.000 - 00:00:06.000
Trong video này, chúng ta sẽ kiểm tra kết quả của thuật toán, điều đầu tiên chúng ta sẽ làm

### 00:00:06.000 - 00:00:08.000
để hiển thị là bảng giá trị q.

### 00:00:11.000 - 00:00:18.000
Để làm được điều đó, hãy gọi hàm story_action_values() và đặt nó làm đối số cho bảng giá trị của chúng ta.

### 00:00:20.000 - 00:00:23.000
Hãy chạy nó, và nó đây.

### 00:00:27.000 - 00:00:32.000
Như bạn có thể thấy, những hành động tối ưu là những hành động đưa chúng ta thẳng đến mục tiêu.

### 00:00:37.000 - 00:00:44.000
Trong mỗi ô, bạn có thể thấy giá trị q của hành động đó. Ở mỗi trạng thái, những hành động có hiệu quả cao nhất

### 00:00:44.000 - 00:00:48.000
giá trị q là những giá trị đưa chúng ta ngày càng đến gần mục tiêu hơn.

### 00:00:50.000 - 00:00:52.000
Bây giờ, hãy xem chính sách mà chúng tôi đã có được.

### 00:00:54.000 - 00:00:54.000
Đây rồi.

### 00:01:02.000 - 00:01:05.000
Như bạn có thể thấy, bắt đầu từ trạng thái ban đầu

### 00:01:09.000 - 00:01:13.000
chính sách sẽ khuyên đại lý chuyển xuống,

### 00:01:16.000 - 00:01:21.000
sau đó di chuyển theo hướng này cho đến khi đạt được mục tiêu.

### 00:01:25.000 - 00:01:27.000
Bây giờ, hãy nhìn xem điều gì xảy ra ở phía bên này của mê cung.

### 00:01:31.000 - 00:01:36.000
Ở những trạng thái này, vì chúng không nằm trong con đường tối ưu dẫn chúng ta đến mục tiêu, đó là trạng thái này

### 00:01:36.000 - 00:01:43.000
ở đây, một chính sách không thực hiện bất kỳ hoạt động thăm dò nào, sẽ không đi qua bất kỳ trạng thái nào trong số này bởi vì

### 00:01:43.000 - 00:01:44.000
họ chỉ đến lối ra.

### 00:01:46.000 - 00:01:52.000
Tuy nhiên, vì chính sách của chúng tôi thỉnh thoảng chọn các hành động ngẫu nhiên nên chúng tôi cũng đã khám phá một số hành động trong số này

### 00:01:52.000 - 00:01:58.000
tiểu bang. Nhờ đó ở một số trạng thái này, chúng ta biết hành động nào tốt hơn hành động khác.

### 00:02:00.000 - 00:02:07.000
Như bạn có thể thấy ở ba trạng thái này ở đây, hành động được chính sách đề xuất sẽ di chuyển sang trái, điều này

### 00:02:07.000 - 00:02:12.000
thực chất là hành động tối ưu vì nó dẫn chúng ta đến mục tiêu bằng con đường ngắn nhất.

### 00:02:13.000 - 00:02:18.000
Cuối cùng, hãy xem liệu một tác nhân tuân theo chính sách mà chúng tôi đã thu được có khả năng tìm thấy

### 00:02:18.000 - 00:02:19.000
lối ra.

### 00:02:20.000 - 00:02:22.000
Để làm được điều đó, hãy thực thi ô này.

### 00:02:24.000 - 00:02:28.000
Và như bạn thấy, nó có khả năng tìm lối ra một cách tối ưu.

### 00:02:37.000 - 00:02:42.000
Xin chúc mừng, bạn đã triển khai thuật toán học hỏi kinh nghiệm đầu tiên của mình.

### 00:02:42.000 - 00:02:49.000
Bây giờ chúng ta hãy xem một phương pháp Montecarlo khác sử dụng chiến lược thăm dò khác gọi là phi chính sách.

### 00:02:49.000 - 00:02:51.000
Tôi sẽ gặp bạn trong video tiếp theo.

