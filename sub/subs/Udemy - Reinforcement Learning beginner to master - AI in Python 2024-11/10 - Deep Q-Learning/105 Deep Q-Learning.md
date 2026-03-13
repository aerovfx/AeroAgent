## Nội dung

### 00:00:00.000 - 00:00:04.000
Trong phần này, chúng ta sẽ làm quen với thuật toán Deep Q-Learning.

### 00:00:06.000 - 00:00:13.000
Nó là sự kết hợp giữa thuật toán khác biệt tạm thời Q-Learning với mạng lưới thần kinh.

### 00:00:15.000 - 00:00:21.000
Tương tự như thuật toán Deep SARSA, chúng ta sẽ có một mạng lưới thần kinh ước tính các giá trị q

### 00:00:21.000 - 00:00:28.000
của mỗi hành động, lấy trạng thái làm đầu vào. Vì đây là phần mở rộng của thuật toán Q-learning

### 00:00:28.000 - 00:00:31.000
chúng tôi sẽ tuân theo chiến lược học tập ngoài chính sách.

### 00:00:32.000 - 00:00:40.000
Điều đó có nghĩa là chúng ta sẽ khám phá môi trường bằng cách sử dụng chính sách khám phá mang tính tham lam của epsilon

### 00:00:40.000 - 00:00:43.000
đối với các giá trị q ước tính.

### 00:00:45.000 - 00:00:53.000
Và để cập nhật mạng lưới thần kinh, chúng tôi sẽ sử dụng một chính sách riêng biệt sẽ được tôn trọng

### 00:00:53.000 - 00:00:55.000
tới các giá trị q ước tính.

### 00:00:57.000 - 00:01:03.000
Do đó, chúng tôi sẽ không tính toán mục tiêu của hàm chi phí dựa trên hành động tiếp theo được khám phá,

### 00:01:04.000 - 00:01:10.000
nhưng dựa trên chính sách được chọn bởi chính sách mục tiêu, đó là chính sách được tối ưu hóa.

### 00:01:12.000 - 00:01:19.000
Đây là điểm khác biệt lớn với phương pháp SARSA sâu, vốn tuân theo chiến lược thăm dò chính sách

### 00:01:21.000 - 00:01:29.000
và do đó, cập nhật mạng lưới thần kinh bằng cách sử dụng hành động được chọn bởi chính sách tương tự để khám phá

### 00:01:29.000 - 00:01:30.000
môi trường.

### 00:01:32.000 - 00:01:36.000
Bây giờ chúng ta sẽ thực hiện một thay đổi nhỏ đối với thuật toán để đơn giản hóa nó.

### 00:01:38.000 - 00:01:46.000
Thay vì khai báo chính sách đích một cách rõ ràng dưới dạng một hàm, sẽ chỉ khai báo thăm dò

### 00:01:46.000 - 00:01:54.000
chính sách và sau đó là trong hàm chi phí, khi chúng ta phải chọn giá trị q của hành động tiếp theo được thực hiện,

### 00:01:55.000 - 00:01:59.000
chúng tôi sẽ sử dụng giá trị q của hành động mà chính sách mục tiêu sẽ chọn.

### 00:02:00.000 - 00:02:03.000
Tức là hành động có giá trị q tối đa.

### 00:02:05.000 - 00:02:12.000
Đây chỉ là một sự đơn giản hóa nhỏ mà chúng ta sẽ có thể thực hiện được với chức năng tối đa của PyTorch

### 00:02:12.000 - 00:02:19.000
thư viện, nhưng kết quả sẽ giống với những gì chúng ta nhận được nếu chúng ta tạo chính sách đích riêng biệt

### 00:02:19.000 - 00:02:21.000
và chúng tôi sử dụng nó trong hàm chi phí.

### 00:02:23.000 - 00:02:30.000
Mặt khác, trong thuật toán này, chúng tôi cũng sẽ sử dụng bộ nhớ phát lại để lưu trữ

### 00:02:30.000 - 00:02:33.000
kinh nghiệm mà tác nhân quan sát được.

### 00:02:34.000 - 00:02:41.000
Và dựa trên các đợt trải nghiệm đó được chọn ngẫu nhiên, chúng tôi sẽ cập nhật mạng lưới thần kinh.

### 00:02:42.000 - 00:02:49.000
Cuối cùng, chúng tôi cũng phải nhấn mạnh rằng chúng tôi sẽ sử dụng mạng mục tiêu, như chúng tôi đã làm với

### 00:02:49.000 - 00:02:55.000
Thuật toán sâu SARSA. Mạng này sẽ mang lại sự ổn định cho các cập nhật tham số và sẽ cho phép

### 00:02:55.000 - 00:03:00.000
chúng tôi để có được ước tính chính xác về những giá trị q đó sớm hơn nhiều.

