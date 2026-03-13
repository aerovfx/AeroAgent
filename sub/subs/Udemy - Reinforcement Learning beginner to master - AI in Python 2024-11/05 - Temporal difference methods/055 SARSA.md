## Nội dung

### 00:00:00.000 - 00:00:04.000
Trong video này, chúng tôi sẽ giới thiệu phương pháp sai phân tạm thời đầu tiên mà chúng tôi sắp triển khai

### 00:00:04.000 - 00:00:06.000
gọi là Sahsa.

### 00:00:07.000 - 00:00:10.000
Nó tuân theo một chiến lược thăm dò chính sách.

### 00:00:10.000 - 00:00:17.000
Điều này có nghĩa là chúng tôi sẽ giữ một chính sách duy nhất chịu trách nhiệm cho cả việc khám phá môi trường

### 00:00:17.000 - 00:00:20.000
và tham gia vào quá trình tối ưu hóa.

### 00:00:20.000 - 00:00:25.000
Hãy nhớ rằng để tìm ra những hành động tối ưu, chúng ta cần tiếp tục khám phá tác dụng của tất cả các hành động.

### 00:00:25.000 - 00:00:26.000
hành động.

### 00:00:26.000 - 00:00:31.000
Thuật toán này đôi khi sẽ thực hiện việc khám phá bằng cách chọn một hành động ngẫu nhiên.

### 00:00:31.000 - 00:00:36.000
Bất cứ khi nào đến lúc phải chọn một hành động, chúng ta sẽ tung đồng xu có xác suất.

### 00:00:36.000 - 00:00:45.000
Epsilon sẽ chọn một hành động ngẫu nhiên và với xác suất, Epsilon trừ một sẽ chọn hành động có

### 00:00:45.000 - 00:00:47.000
giá trị Q ước tính cao nhất.

### 00:00:48.000 - 00:00:53.000
Cái tên Sahsa xuất phát từ năm yếu tố liên quan đến quy tắc cập nhật.

### 00:00:53.000 - 00:00:57.000
Trạng thái tại thời điểm thực hiện hành động ở trạng thái đó.

### 00:00:57.000 - 00:01:07.000
Phần thưởng nhận được ngay sau khi thực hiện hành động đó, trạng thái tiếp theo đạt được sau khi thực hiện hành động đó

### 00:01:07.000 - 00:01:13.000
và cả hành động mà chính sách sẽ lựa chọn cho trạng thái kế tiếp đó.

### 00:01:13.000 - 00:01:17.000
Năm yếu tố này tạo thành từ viết tắt Sahsa.

### 00:01:19.000 - 00:01:24.000
Dựa trên năm yếu tố này, sai số chênh lệch tạm thời được tính toán.

### 00:01:25.000 - 00:01:30.000
Và được sử dụng để tinh chỉnh ước tính giá trị Q trong bảng của chúng tôi.

### 00:01:31.000 - 00:01:39.000
Chúng tôi sẽ thực hiện điều đó bằng cách di chuyển ước tính của chúng tôi về giá trị Q theo hướng ước tính mới được thu thập bằng cách sử dụng

### 00:01:39.000 - 00:01:44.000
kinh nghiệm từ môi trường trong một phần trăm alpha nhất định.

### 00:01:45.000 - 00:01:51.000
Một lần nữa lưu ý rằng chính sách khám phá môi trường cũng chính là chính sách chọn hành động tiếp theo

### 00:01:51.000 - 00:01:52.000
trong quy tắc cập nhật.

### 00:01:54.000 - 00:01:58.000
Điều này sẽ tách biệt khỏi thuật toán tiếp theo mà chúng ta sẽ tìm hiểu.

### 00:01:59.000 - 00:02:01.000
Đây là thuật toán.

### 00:02:01.000 - 00:02:08.000
Đầu tiên, chúng ta sẽ khởi tạo chính sách của mình, đây sẽ là chính sách epsilon tham lam, như chúng tôi đã đề cập trước đó.

### 00:02:08.000 - 00:02:15.000
Và chúng ta cũng sẽ khởi tạo bảng giá trị q với các ước tính về giá trị q cho mỗi hành động trong mỗi hành động.

### 00:02:15.000 - 00:02:16.000
tình trạng.

### 00:02:16.000 - 00:02:21.000
Sau đó, chúng ta sẽ vào vòng lặp chính sẽ lặp lại trong một số tập.

### 00:02:22.000 - 00:02:29.000
Trong mỗi tập, chúng ta sẽ khởi tạo tác vụ và quan sát trạng thái ban đầu mà chúng ta gọi là S0.

### 00:02:30.000 - 00:02:38.000
Tiếp theo, chúng tôi sẽ chọn một hành động cho trạng thái đó theo chính sách, chính sách mà chúng tôi đã khởi tạo ở đây,

### 00:02:38.000 - 00:02:47.000
rồi chúng ta sẽ vào một vòng lặp bên trong sẽ thực thi từng thời điểm cho đến khi tập phim kết thúc.

### 00:02:48.000 - 00:02:55.000
Và tại mỗi thời điểm, chúng tôi sẽ thực hiện hành động mà chúng tôi đã chọn cho trạng thái hiện tại và chúng tôi sẽ

### 00:02:55.000 - 00:03:00.000
quan sát trạng thái tiếp theo đạt được và phần thưởng thu được.

### 00:03:01.000 - 00:03:06.000
Sau đó, đối với trạng thái tiếp theo đạt được, chúng tôi sẽ chọn một hành động theo chính sách.

### 00:03:08.000 - 00:03:16.000
Và ngay sau đó chúng tôi sẽ cập nhật ước tính giá trị Q của trạng thái ban đầu và hành động được thực hiện.

### 00:03:16.000 - 00:03:21.000
Hành động này ở đây sử dụng quy tắc cập nhật mà chúng ta đã thấy trước đây.

### 00:03:22.000 - 00:03:29.000
Ước tính mới sẽ là ước tính cũ cộng với alpha lần lỗi chênh lệch thời gian.

### 00:03:30.000 - 00:03:31.000
Và đó là tất cả.

### 00:03:31.000 - 00:03:41.000
Khi thuật toán kết thúc, chúng ta sẽ có chính sách gần tối ưu và bảng ước tính giá trị Q gần tối ưu.

### 00:03:41.000 - 00:03:44.000
Bởi vì chính sách của chúng tôi đôi khi chọn một hành động ngẫu nhiên.

### 00:03:45.000 - 00:03:51.000
Vì vậy, chính sách của chúng tôi sẽ không bao giờ trở thành chính sách tối ưu, nhưng nó có thể gần đúng với chính sách đó.

