## Nội dung

### 00:00:00.000 - 00:00:04.000
Trong video này, chúng ta sẽ tìm hiểu cách cập nhật mạng lưới thần kinh của mình.

### 00:00:04.000 - 00:00:07.000
Chúng ta sẽ bắt đầu với Mạng Giá trị.

### 00:00:07.000 - 00:00:15.000
Người phê bình trong thuật toán này và chúng tôi sẽ cập nhật nó bằng cách tính toán mục tiêu tại một thời điểm cụ thể.

### 00:00:16.000 - 00:00:18.000
Với phần thưởng đầu tiên.

### 00:00:19.000 - 00:00:22.000
Và giá trị chiết khấu của trạng thái tiếp theo.

### 00:00:23.000 - 00:00:30.000
Và với mục tiêu đó, chúng ta sẽ trừ đi giá trị của trạng thái hiện tại, điều này làm cho biểu thức này trở thành

### 00:00:30.000 - 00:00:31.000
lỗi chênh lệch thời gian.

### 00:00:32.000 - 00:00:40.000
Sai số này sẽ bình phương nó và chúng tôi sẽ tính giá trị trung bình của các sai số bình phương trong tất cả các môi trường.

### 00:00:40.000 - 00:00:46.000
Đó sẽ là hàm chi phí của chúng tôi vì chúng tôi đang thực hiện giảm độ dốc ngẫu nhiên.

### 00:00:46.000 - 00:00:49.000
Chúng tôi muốn giảm thiểu chức năng này.

### 00:00:49.000 - 00:00:54.000
Để làm điều đó, chúng tôi sẽ tạo ước tính giá trị của trạng thái hiện tại.

### 00:00:57.000 - 00:01:02.000
Trong mỗi môi trường và sau đó chúng tôi sẽ tạo ra giá trị mục tiêu.

### 00:01:06.000 - 00:01:14.000
Giá trị mà chúng tôi muốn hướng tới ước tính của mình và chúng tôi sẽ nhận được giá trị đó bằng phần thưởng.

### 00:01:16.000 - 00:01:17.000
Không xong.

### 00:01:19.000 - 00:01:24.000
Hãy nhớ rằng chúng tôi làm điều này để loại bỏ các ước tính khi tập phim kết thúc.

### 00:01:26.000 - 00:01:27.000
Thời gian, Gamma.

### 00:01:29.000 - 00:01:32.000
Nhân với giá trị ước tính của trạng thái tiếp theo.

### 00:01:36.000 - 00:01:39.000
Và trên tensor này chúng ta sẽ gọi phương thức tách.

### 00:01:42.000 - 00:01:48.000
Bởi vì trong hàm chi phí, chúng ta muốn tính độ dốc theo các ước tính hiện tại.

### 00:01:50.000 - 00:01:53.000
Mục tiêu không tham gia vào quá trình cập nhật.

### 00:01:54.000 - 00:02:02.000
Hãy khai báo biến mất phê bình và nó sẽ là kết quả của việc gọi sai số bình phương trung bình

### 00:02:02.000 - 00:02:05.000
chức năng, truyền các giá trị và mục tiêu.

### 00:02:08.000 - 00:02:11.000
Chức năng mất MSE này.

### 00:02:11.000 - 00:02:15.000
Là lỗi bình phương trung bình mà bạn thấy ở đây.

### 00:02:19.000 - 00:02:26.000
Sau đó, chúng ta sẽ xóa các gradient được lưu trữ trong mạng giá trị bằng cách gọi hàm zerograd.

### 00:02:29.000 - 00:02:32.000
Sau đó chúng tôi viết Critic Los.

### 00:02:35.000 - 00:02:41.000
Ngược lại, đây là phương pháp kích hoạt lan truyền ngược để tính toán độ dốc.

### 00:02:44.000 - 00:02:51.000
Và cuối cùng chúng ta sẽ viết giá trị Optim, là đối tượng chịu trách nhiệm áp dụng quy tắc cập nhật để cập nhật

### 00:02:51.000 - 00:02:52.000
mạng giá trị.

### 00:02:52.000 - 00:02:57.000
Và chúng ta sẽ gọi phương thức step để thực hiện cập nhật theo hướng của mục tiêu.

### 00:02:58.000 - 00:03:02.000
Và thế là chúng ta đã hoàn tất việc cập nhật mạng giá trị.

### 00:03:05.000 - 00:03:08.000
Tiếp theo, chúng tôi sẽ cập nhật chính sách.

### 00:03:09.000 - 00:03:15.000
Và chúng ta sẽ thực hiện điều đó theo cách tương tự như trong phần trước, chúng ta sẽ thực hiện ngẫu nhiên

### 00:03:15.000 - 00:03:21.000
độ dốc tăng dần, khác với độ dốc giảm dần trong ước tính hiệu suất chính sách.

### 00:03:22.000 - 00:03:23.000
Vì điều đó.

### 00:03:23.000 - 00:03:28.000
Chúng tôi viết lợi thế bằng mục tiêu trừ đi giá trị.

### 00:03:28.000 - 00:03:31.000
Và trên tensor này, chúng ta gọi phương thức tách.

### 00:03:35.000 - 00:03:42.000
Và hãy nhớ rằng hàm lợi thế đo lường sự khác biệt giữa giá trị Q của một hành động cụ thể

### 00:03:42.000 - 00:03:44.000
và giá trị của một trạng thái.

### 00:03:44.000 - 00:03:47.000
Và ở đây chúng tôi đang ước tính cả hai.

### 00:03:47.000 - 00:03:51.000
Vì vậy, những gì chúng ta có là ước tính của hàm lợi thế.

### 00:03:51.000 - 00:03:57.000
Tiếp theo, chúng ta cần thực hiện tương tự như trong thuật toán củng cố và tính xác suất

### 00:03:57.000 - 00:04:01.000
bằng cách kêu gọi chính sách của các bang.

### 00:04:01.000 - 00:04:06.000
Và ngay sau đó, chúng ta sẽ lấy logarit của những xác suất đó.

### 00:04:10.000 - 00:04:14.000
Hãy viết nhật ký ngọn đuốc và chúng tôi chuyển cho nó các xác suất.

### 00:04:14.000 - 00:04:17.000
Nhưng hãy nhớ rằng logarit của số 0 không tồn tại.

### 00:04:17.000 - 00:04:24.000
Vì vậy để giữ sự ổn định của thao tác này, chúng ta phải thêm một hằng số rất nhỏ để tránh số

### 00:04:24.000 - 00:04:25.000
lỗi.

### 00:04:26.000 - 00:04:33.000
Tiếp theo, chúng ta sẽ chỉ chọn xác suất nhật ký của hành động từ vectơ xác suất nhật ký.

### 00:04:34.000 - 00:04:36.000
Đó là chúng tôi đã chọn.

### 00:04:36.000 - 00:04:42.000
Và chúng tôi thực hiện điều đó bằng cách gọi phương thức thu thập ở chiều thứ nhất với chỉ mục của hành động

### 00:04:42.000 - 00:04:48.000
chúng tôi đã thực hiện để thao tác thu thập được áp dụng cho từng vectơ xác suất một cách độc lập.

### 00:04:49.000 - 00:04:54.000
Việc tiếp theo chúng ta sẽ làm là tính entropy của phân bố xác suất.

### 00:04:57.000 - 00:05:05.000
Chúng tôi sẽ sử dụng entropy này làm cơ chế chính quy hóa để đảm bảo rằng chính sách tiếp tục bùng nổ.

### 00:05:06.000 - 00:05:13.000
Entropy sẽ là số âm của tổng từng xác suất nhân với logarit của nó.

### 00:05:13.000 - 00:05:21.000
Chúng ta sẽ áp dụng tổng này trên trục cuối cùng để đảm bảo rằng chúng ta sẽ áp dụng nó trên từng vectơ xác suất

### 00:05:21.000 - 00:05:22.000
một cách độc lập.

### 00:05:23.000 - 00:05:27.000
Và nhân tiện, chúng tôi muốn giữ nguyên kích thước của tensor đầu vào.

### 00:05:30.000 - 00:05:34.000
Bây giờ chúng ta sẽ tính hàm chi phí của chính sách.

### 00:05:34.000 - 00:05:36.000
Hãy gọi đó là mất diễn viên.

### 00:05:38.000 - 00:05:42.000
Và nó sẽ là số âm của biến I.

### 00:05:43.000 - 00:05:46.000
Nhân với xác suất nhật ký hành động.

### 00:05:47.000 - 00:05:49.000
Lần lợi thế.

### 00:05:53.000 - 00:05:58.000
Và với số tiền này, chúng ta sẽ trừ đi entropy nhân với một hệ số nhỏ.

### 00:06:02.000 - 00:06:06.000
Như bạn có thể thấy, con mắt tượng trưng cho yếu tố này.

### 00:06:08.000 - 00:06:12.000
Và ở đây chúng tôi cũng có lợi thế và nhật ký hành động thăm dò.

### 00:06:15.000 - 00:06:19.000
Điều đó thể hiện xác suất nhật ký của việc chọn một hành động.

### 00:06:24.000 - 00:06:30.000
Sau đó, chúng tôi sẽ tính giá trị chi phí trung bình trên tất cả các môi trường.

### 00:06:36.000 - 00:06:41.000
Và bây giờ chúng ta sẽ xóa bỏ các gradient của chính sách.

### 00:06:42.000 - 00:06:45.000
Sau đó, chúng tôi gọi phương pháp lùi.

### 00:06:50.000 - 00:06:55.000
Và cuối cùng, chúng ta sẽ thực hiện bước tăng dần độ dốc.

### 00:07:01.000 - 00:07:07.000
Nhưng chúng ta thay đổi dấu của biểu thức vì đối tượng này chỉ có thể thực hiện giảm độ dốc.

### 00:07:07.000 - 00:07:12.000
Đi xuống phía âm của một giá trị cũng giống như đi lên.

### 00:07:12.000 - 00:07:13.000
Được rồi.

### 00:07:13.000 - 00:07:17.000
Tất cả những gì còn lại bây giờ là cập nhật các biến.

### 00:07:17.000 - 00:07:21.000
Đến vectơ lưu trữ kết quả trả về của tập phim.

### 00:07:21.000 - 00:07:23.000
Sẽ thêm phần thưởng thu được.

### 00:07:25.000 - 00:07:32.000
Tại thời điểm này, cũng có vectơ lưu trữ các cờ cho chúng ta biết liệu môi trường có

### 00:07:32.000 - 00:07:33.000
đã kết thúc tập phim.

### 00:07:33.000 - 00:07:39.000
Chúng ta sẽ thêm các giá trị từ biến Don mà chúng ta thu được từ môi trường.

### 00:07:43.000 - 00:07:46.000
Sau đó, như mọi khi, chúng ta sẽ chuyển sang trạng thái tiếp theo.

### 00:07:52.000 - 00:07:54.000
Và biến I.

### 00:07:56.000 - 00:07:57.000
Chúng ta sẽ nhân nó với Gamma.

### 00:07:58.000 - 00:08:05.000
Bằng cách đó, khi tiến sâu hơn vào tập này, chúng tôi sẽ tính toán giá trị chính xác cho cụm từ này.

### 00:08:05.000 - 00:08:10.000
Bây giờ, tất cả những gì còn lại là lưu trữ số liệu thống kê và hoàn thành thuật toán.

### 00:08:12.000 - 00:08:13.000
Hãy viết số liệu thống kê.

### 00:08:16.000 - 00:08:16.000
Diễn viên Los.

### 00:08:20.000 - 00:08:22.000
Và chúng tôi sẽ thêm giá trị mới nhất.

### 00:08:24.000 - 00:08:26.000
Của hàm chi phí.

### 00:08:27.000 - 00:08:28.000
Của chính sách.

### 00:08:37.000 - 00:08:40.000
Và chúng tôi sẽ làm tương tự cho mạng Giá trị.

### 00:08:49.000 - 00:08:51.000
Và cũng với lợi nhuận.

### 00:09:02.000 - 00:09:06.000
Và khi thuật toán kết thúc, chúng tôi sẽ trả về số liệu thống kê này.

### 00:09:13.000 - 00:09:14.000
Và thì đấy.

### 00:09:14.000 - 00:09:16.000
Hãy chạy ô này và gọi thuật toán.

### 00:09:21.000 - 00:09:27.000
Với tư cách là nhà phê bình diễn viên và chúng tôi chuyển cho nó chính sách và mạng lưới giá trị làm đầu vào.

### 00:09:29.000 - 00:09:32.000
Cũng như 200 tập.

### 00:09:35.000 - 00:09:36.000
Hãy chạy tế bào này.

### 00:09:40.000 - 00:09:42.000
Và chúng tôi sẽ quay lại sau vài phút nữa khi nó kết thúc.

### 00:09:46.000 - 00:09:48.000
Được rồi, cuộc hành quyết đã kết thúc.

### 00:09:49.000 - 00:09:52.000
Mất khoảng một phút rưỡi trên máy tính của tôi.

### 00:09:52.000 - 00:09:55.000
Tiếp theo, chúng tôi sẽ hiển thị số liệu thống kê thực hiện.

### 00:09:57.000 - 00:09:59.000
Hãy chạy tế bào này.

### 00:10:00.000 - 00:10:01.000
Và ở đây chúng tôi có anh ấy.

### 00:10:04.000 - 00:10:10.000
Như bạn có thể thấy, hàm chi phí của mạng giá trị đã giảm đều đặn trong giai đoạn đầu tiên.

### 00:10:10.000 - 00:10:18.000
Sở dĩ như vậy là vì trong những tập phim này, nó đã học cách ước tính chính xác các giá trị tiếp cận mục tiêu của chúng.

### 00:10:18.000 - 00:10:18.000
các giá trị.

### 00:10:19.000 - 00:10:25.000
Mặt khác, chính sách này cũng đã đạt được sự gia tăng đáng kể về hiệu quả của nó.

### 00:10:28.000 - 00:10:36.000
Trong tập đầu tiên này, khi người đại diện áp dụng các hành động đúng đắn, lợi nhuận đã tăng từ mức tối thiểu,

### 00:10:36.000 - 00:10:41.000
tức là -300 đến khoảng -120.

### 00:10:42.000 - 00:10:50.000
Nghĩa là, nó có khả năng tìm ra giải pháp trong khoảng 120 bước trong khi ở đây nó thậm chí còn không thể

### 00:10:50.000 - 00:10:52.000
tìm giải pháp.

### 00:10:52.000 - 00:10:56.000
Điều cuối cùng chúng ta sẽ làm là kiểm tra chính sách mà chúng ta đã học.

### 00:10:57.000 - 00:10:59.000
Bây giờ hãy chạy ô này.

### 00:11:01.000 - 00:11:02.000
Và ở đây bạn có nó.

### 00:11:14.000 - 00:11:15.000
Hãy chạy nó một lần nữa.

### 00:11:20.000 - 00:11:24.000
Và như bạn thấy, tác nhân có khả năng chạm vào thanh ngang.

