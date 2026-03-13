## Nội dung

### 00:00:00.000 - 00:00:07.000
Trong phần này, chúng ta sẽ mở rộng phương pháp sai phân tạm thời để ước tính giá trị Q bằng cách sử dụng

### 00:00:07.000 - 00:00:09.000
một mạng lưới thần kinh.

### 00:00:09.000 - 00:00:13.000
Thuật toán kết quả sẽ được gọi là deep saastr.

### 00:00:13.000 - 00:00:20.000
Phương pháp này là sự kết hợp giữa thuật toán sarsa với mạng lưới thần kinh và các kỹ thuật được sử dụng để

### 00:00:20.000 - 00:00:24.000
đào tạo họ cái được gọi là học sâu.

### 00:00:24.000 - 00:00:31.000
Trong phiên bản thuật toán này, các ước tính của giá trị Q sẽ không được lưu trữ trong bảng mà

### 00:00:31.000 - 00:00:37.000
chúng sẽ được tạo ra bằng cách cung cấp trạng thái làm đầu vào cho mạng lưới thần kinh.

### 00:00:38.000 - 00:00:46.000
Và đầu ra của mạng nơ-ron đó sẽ là một vectơ trong đó mỗi phần tử là giá trị Q, ước tính

### 00:00:46.000 - 00:00:50.000
Giá trị Q của một hành động cụ thể cho trạng thái đó.

### 00:00:50.000 - 00:00:53.000
Thuật toán kết quả sẽ trông như thế này.

### 00:00:53.000 - 00:00:57.000
Chúng ta hãy xem nhanh nó và sau đó chúng tôi sẽ giải thích chi tiết sự khác biệt.

### 00:00:58.000 - 00:01:03.000
Như chúng tôi đã nói, chúng tôi sẽ sử dụng mạng thần kinh để ước tính các giá trị Q.

### 00:01:03.000 - 00:01:11.000
Vì vậy, thay vì khởi tạo một bảng giá trị Q như trước, chúng ta sẽ khởi tạo các tham số của nơron đó

### 00:01:11.000 - 00:01:12.000
mạng.

### 00:01:13.000 - 00:01:13.000
Như trong.

### 00:01:13.000 - 00:01:19.000
Chính sách mà chúng tôi sắp sử dụng sẽ là chính sách tham lam của epsilon.

### 00:01:19.000 - 00:01:26.000
Tức là chính sách sẽ chọn các hành động ngẫu nhiên với xác suất nhất định được xác định bởi giá trị của epsilon

### 00:01:26.000 - 00:01:29.000
và với xác suất bằng một trừ epsilon.

### 00:01:29.000 - 00:01:34.000
Chính sách sẽ chọn hành động có giá trị Q ước tính cao nhất.

### 00:01:34.000 - 00:01:40.000
Thuật toán học hỏi từ kinh nghiệm được thu thập bởi tác nhân tương tác với môi trường.

### 00:01:40.000 - 00:01:43.000
Giống như thuật toán sarsa ban đầu.

### 00:01:43.000 - 00:01:50.000
Vì vậy, phần chính của thuật toán là thực hiện vòng lặp này, vòng lặp này sẽ được lặp lại cho một số

### 00:01:50.000 - 00:01:51.000
của các tập phim.

### 00:01:51.000 - 00:01:54.000
Vòng lặp này bao gồm hai phần.

### 00:01:54.000 - 00:02:00.000
Phần đầu tiên là phần mà tác nhân tương tác với môi trường để thu thập kinh nghiệm, phần này

### 00:02:00.000 - 00:02:05.000
sau đó nó sẽ sử dụng để tinh chỉnh các ước tính mạng thần kinh nhằm cải thiện chính sách.

### 00:02:06.000 - 00:02:10.000
Phần thứ hai của thuật toán là nơi chúng ta cập nhật các tham số của mạng nơ-ron.

### 00:02:10.000 - 00:02:17.000
Chúng tôi sẽ làm điều đó dựa trên kinh nghiệm mà đại lý đã thu thập trước đó và chúng tôi sẽ cập nhật các thông số

### 00:02:17.000 - 00:02:23.000
của mạng nơ-ron sao cho các ước tính về giá trị Q mà nó tạo ra chính xác hơn mỗi lần

### 00:02:23.000 - 00:02:25.000
thời gian chúng tôi cập nhật nó.

### 00:02:25.000 - 00:02:30.000
Bản cập nhật này được tạo ra bởi thuật toán Giảm dần độ dốc ngẫu nhiên.

### 00:02:30.000 - 00:02:36.000
Trong các video sau, chúng ta sẽ thấy chi tiết những khác biệt đã nói ở trên, sarsa sâu ngoài

### 00:02:36.000 - 00:02:38.000
phiên bản cổ điển của thuật toán.

