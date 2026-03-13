## Nội dung

### 00:00:00.000 - 00:00:06.000
Trong video này, chúng ta sẽ xem thuật toán thứ hai học hỏi từ những khác biệt về thời gian được gọi là

### 00:00:06.000 - 00:00:07.000
q-học tập.

### 00:00:08.000 - 00:00:12.000
Phương pháp này tuân theo một chiến lược học tập ngoài chính sách.

### 00:00:12.000 - 00:00:15.000
Điều này có nghĩa là chúng tôi sẽ có hai chính sách riêng biệt.

### 00:00:16.000 - 00:00:23.000
Một trong số họ tham gia vào quá trình tối ưu hóa và người còn lại để khám phá môi trường.

### 00:00:24.000 - 00:00:31.000
Chính sách tham gia vào quá trình tối ưu hóa được gọi là Pi và nó sẽ là chính sách tham lam,

### 00:00:31.000 - 00:00:37.000
điều đó có nghĩa là nó sẽ luôn chọn hành động có giá trị Q ước tính cao nhất.

### 00:00:38.000 - 00:00:45.000
Mặt khác, chính sách khám phá sẽ được gọi là B và chúng tôi sẽ sử dụng nó để đối mặt với môi trường

### 00:00:45.000 - 00:00:46.000
và thu thập các mẫu kinh nghiệm.

### 00:00:47.000 - 00:00:49.000
Đây là quy tắc cập nhật.

### 00:00:50.000 - 00:00:55.000
Như bạn có thể thấy, nó khá giống với SAS, ngoại trừ việc hiện tại chúng tôi có hai chính sách.

### 00:00:55.000 - 00:00:59.000
Chúng tôi sẽ chọn hành động tiếp theo dựa trên chính sách mục tiêu.

### 00:00:59.000 - 00:01:05.000
Vì chính sách khám phá chỉ có vai trò thu thập kinh nghiệm và tương tác với

### 00:01:05.000 - 00:01:11.000
môi trường và như bạn biết, chính sách mục tiêu chọn hành động một cách tham lam.

### 00:01:11.000 - 00:01:15.000
Nó chọn hành động có giá trị Q ước tính cao nhất.

### 00:01:16.000 - 00:01:20.000
Phần còn lại của thuật toán gần như giống với saastr.

### 00:01:20.000 - 00:01:21.000
Đây rồi.

### 00:01:21.000 - 00:01:24.000
Như tôi đã nói, chúng tôi đã khởi tạo hai chính sách riêng biệt.

### 00:01:24.000 - 00:01:32.000
Chính sách mục tiêu là chính sách tham lam và chính sách thăm dò cũng như bảng giá trị Q.

### 00:01:33.000 - 00:01:39.000
Và sau đó chúng ta sẽ vào vòng lặp chính, vòng lặp sẽ lặp lại trong một số tập.

### 00:01:39.000 - 00:01:44.000
Trong mỗi tập, chúng ta sẽ khởi động lại nhiệm vụ và quan sát trạng thái ban đầu.

### 00:01:45.000 - 00:01:51.000
Sau đó, chúng tôi đi vào một vòng lặp bên trong sẽ thực thi theo từng thời điểm cho đến khi kết thúc tập.

### 00:01:52.000 - 00:01:57.000
Tại mỗi thời điểm, chúng tôi sẽ chọn một hành động bằng chính sách khám phá.

### 00:01:58.000 - 00:02:04.000
Chúng tôi sẽ thực hiện hành động đó trong môi trường và chúng tôi sẽ quan sát trạng thái tiếp theo cũng như phần thưởng nhận được,

### 00:02:05.000 - 00:02:11.000
và sau đó chúng tôi sẽ cập nhật ước tính giá trị Q theo quy tắc cập nhật mà chúng tôi đã thấy trước đó.

### 00:02:12.000 - 00:02:13.000
Và thế là xong.

### 00:02:13.000 - 00:02:20.000
Khi thuật toán kết thúc, chúng ta sẽ có chính sách tối ưu và ước tính giá trị Q tối ưu.

