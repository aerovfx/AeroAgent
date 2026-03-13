## Nội dung

### 00:00:00.000 - 00:00:04.000
Trong video này, chúng ta sẽ triển khai thuật toán RSA.

### 00:00:05.000 - 00:00:08.000
Việc đầu tiên chúng ta sẽ làm là khai báo hàm.

### 00:00:09.000 - 00:00:14.000
Chúng ta sẽ gọi hàm này là sahsa và cung cấp cho nó một vài tham số.

### 00:00:14.000 - 00:00:17.000
Đầu tiên là bảng giá trị.

### 00:00:19.000 - 00:00:26.000
Chúng tôi cũng sẽ cung cấp cho nó chính sách mà tác nhân sẽ tuân theo trong quá trình học tập, cũng như

### 00:00:26.000 - 00:00:31.000
số tập, số lần chúng ta muốn thực hiện vòng lặp chính.

### 00:00:32.000 - 00:00:34.000
Giá trị đầu tiên là alpha.

### 00:00:36.000 - 00:00:43.000
Alpha đo lường mức độ chúng ta đẩy ước tính hiện tại của giá trị Q theo hướng mới

### 00:00:43.000 - 00:00:44.000
ước lượng.

### 00:00:50.000 - 00:00:56.000
Tham số tiếp theo sẽ là gamma có giá trị khởi tạo là 0,99.

### 00:00:57.000 - 00:01:04.000
Như bạn đã biết, gamma là hệ số chiết khấu mà chúng tôi sử dụng để điều chỉnh giá trị của phần thưởng trong tương lai và tương lai.

### 00:01:04.000 - 00:01:06.000
ước tính giá trị.

### 00:01:06.000 - 00:01:12.000
Và tham số cuối cùng là epsilon, là xác suất để tác nhân chọn một hành động ngẫu nhiên trong khi

### 00:01:12.000 - 00:01:15.000
theo chính sách tham lam của epsilon.

### 00:01:17.000 - 00:01:19.000
Trong những dòng đầu tiên của thuật toán.

### 00:01:19.000 - 00:01:26.000
Chúng ta cần khởi tạo chính sách này dưới dạng chính sách tham lam epsilon đối với các giá trị Q.

### 00:01:26.000 - 00:01:31.000
Và chúng ta cũng cần khởi tạo bảng giá trị Q, nhưng chúng ta đã làm xong việc đó rồi.

### 00:01:31.000 - 00:01:34.000
Vì vậy, bây giờ chúng ta đã sẵn sàng để chuyển sang vòng lặp chính.

### 00:01:35.000 - 00:01:40.000
Chúng tôi sẽ lặp lại vòng lặp chính cho một số tập cụ thể.

### 00:01:40.000 - 00:01:47.000
Vì vậy, chúng tôi viết cho mỗi tập trong phạm vi từ một tập cho đến các tập cộng một.

### 00:01:51.000 - 00:01:55.000
Và mỗi khi chúng tôi bắt đầu một tập phim, chúng tôi sẽ làm một số việc.

### 00:01:56.000 - 00:01:59.000
Điều đầu tiên chúng ta sẽ làm là thiết lập lại môi trường.

### 00:02:02.000 - 00:02:08.000
Sẽ làm điều đó bằng cách gọi phương thức reset trên đối tượng môi trường.

### 00:02:08.000 - 00:02:13.000
Và kết quả là môi trường sẽ cho chúng ta những quan sát ban đầu về trạng thái.

### 00:02:14.000 - 00:02:19.000
Sau đó, chúng tôi sẽ chọn một hành động dựa trên chính sách tham lam epsilon của chúng tôi.

### 00:02:19.000 - 00:02:26.000
Và để làm được điều đó, chúng ta sẽ viết hành động bằng kết quả của việc gọi hàm chính sách và đặt trạng thái cho nó

### 00:02:26.000 - 00:02:27.000
như đầu vào.

### 00:02:27.000 - 00:02:33.000
Và giá trị của chúng tôi đối với epsilon, xác suất chọn một hành động ngẫu nhiên.

### 00:02:33.000 - 00:02:39.000
Chúng ta cũng cần khởi tạo biến vòm, biến này sẽ cho chúng ta biết tập phim đã kết thúc hay chưa.

### 00:02:39.000 - 00:02:42.000
Rõ ràng lúc đầu chúng ta khởi tạo nó là sai.

### 00:02:44.000 - 00:02:52.000
Và sau đó chúng ta bước vào một vòng lặp bên trong sẽ lặp lại ở mọi thời điểm cho đến khi tập phim kết thúc.

### 00:02:54.000 - 00:02:55.000
Hãy đi thôi.

### 00:02:55.000 - 00:03:04.000
Mặc dù chưa được thực hiện và tại mọi thời điểm, chúng ta cần hành động trong môi trường và quan sát

### 00:03:05.000 - 00:03:07.000
kết quả của hành động đó.

### 00:03:07.000 - 00:03:14.000
Kết quả của việc thực hiện một hành động là chúng ta sẽ nhận được quan sát tiếp theo về trạng thái của nhiệm vụ và

### 00:03:14.000 - 00:03:21.000
phần thưởng mà môi trường mang lại cho tác nhân do kết quả của hành động đó và cả giá trị mới

### 00:03:21.000 - 00:03:22.000
đã xong.

### 00:03:24.000 - 00:03:31.000
Chúng tôi nhận được tất cả những gì gọi phương thức bước trên môi trường và thực hiện hành động mà tác nhân có

### 00:03:31.000 - 00:03:31.000
được chọn.

### 00:03:34.000 - 00:03:40.000
Bây giờ, theo thuật toán, chúng ta phải chọn hành động mà chính sách sẽ thực thi trong lần tiếp theo.

### 00:03:40.000 - 00:03:41.000
tình trạng.

### 00:03:44.000 - 00:03:45.000
Và vì điều đó chúng tôi.

### 00:03:45.000 - 00:03:45.000
Phải.

### 00:03:45.000 - 00:03:52.000
Hành động tiếp theo bằng kết quả của việc gọi chính sách.

### 00:03:52.000 - 00:03:53.000
Ở trạng thái tiếp theo.

### 00:03:57.000 - 00:03:59.000
Với giá trị của chúng tôi dành cho Epsilon.

### 00:04:02.000 - 00:04:06.000
Điều tiếp theo chúng ta sẽ làm là lưu trữ vào một biến có tên là qsa.

### 00:04:07.000 - 00:04:14.000
Ước tính hiện tại của giá trị Q cho trạng thái chúng ta đang ở và hành động mà tác nhân đã chọn.

### 00:04:15.000 - 00:04:20.000
Chúng ta sẽ truy cập giá trị đó bằng cách lập chỉ mục bảng giá trị hành động.

### 00:04:22.000 - 00:04:24.000
Với trạng thái và hành động thích hợp.

### 00:04:31.000 - 00:04:33.000
Và chúng tôi cũng sẽ lưu trữ trong một biến.

### 00:04:33.000 - 00:04:42.000
Giá trị Q cho trạng thái đạt được sau khi thực hiện hành động và hành động mà tác nhân chọn cho

### 00:04:42.000 - 00:04:43.000
trạng thái mới đó.

### 00:04:46.000 - 00:04:53.000
Bây giờ chúng tôi lập chỉ mục cho bảng bằng cách sử dụng trạng thái tiếp theo và hành động mà tác nhân chọn ở trạng thái tiếp theo đó.

### 00:04:57.000 - 00:05:00.000
Và bây giờ chúng tôi đã sẵn sàng cập nhật ước tính giá trị Q.

### 00:05:00.000 - 00:05:07.000
Chúng tôi lập chỉ mục lại bảng giá trị hành động bằng cách sử dụng trạng thái và hành động.

### 00:05:12.000 - 00:05:17.000
Và chúng tôi sẽ đặt ước tính đó làm giá trị mà nó hiện có.

### 00:05:17.000 - 00:05:24.000
Cộng alpha nhân với phần thưởng nhận được sau khi thực hiện hành động.

### 00:05:28.000 - 00:05:38.000
Cộng với thời gian gamma, giá trị Q của trạng thái tiếp theo mà chúng ta có ở dòng bên phải phía trên trừ đi hiện tại

### 00:05:38.000 - 00:05:41.000
giá trị ước tính đó.

### 00:05:43.000 - 00:05:48.000
Đó là quy tắc cập nhật mà bạn thấy trong mã giả của thuật toán.

### 00:05:48.000 - 00:05:55.000
Bây giờ tất cả những gì còn lại là đặt trạng thái là trạng thái mới và hành động là hành động mới.

### 00:05:59.000 - 00:06:06.000
Vì vậy, lần tiếp theo khi lặp qua vòng lặp bên trong, chúng tôi sẽ cập nhật trạng thái tiếp theo.

### 00:06:06.000 - 00:06:07.000
Và hành động.

### 00:06:09.000 - 00:06:11.000
Bây giờ hãy thực hiện thuật toán.

### 00:06:12.000 - 00:06:15.000
Chúng tôi sẽ cung cấp nó làm đầu vào cho bảng giá trị hành động.

### 00:06:18.000 - 00:06:22.000
Chính sách và một số tập phim.

### 00:06:23.000 - 00:06:25.000
Hãy cho nó 10.000.

### 00:06:28.000 - 00:06:32.000
Hãy cuộn một chút và thực hiện ô này.

### 00:06:35.000 - 00:06:36.000
Sẵn sàng.

### 00:06:37.000 - 00:06:42.000
Bây giờ, hãy kiểm tra xem kết quả mà chúng tôi thu được có đúng như mong đợi hay không.

### 00:06:43.000 - 00:06:47.000
Điều đầu tiên chúng ta sẽ thấy là bảng giá trị Q.

### 00:06:47.000 - 00:06:50.000
Có vẻ như Bây giờ chúng ta hãy thực thi ô này.

### 00:06:50.000 - 00:06:52.000
Và nó đây.

### 00:06:55.000 - 00:07:00.000
Như bạn có thể thấy, những hành động có giá trị cao nhất là những hành động đưa chúng ta đến thẳng mục tiêu.

### 00:07:01.000 - 00:07:08.000
Nhưng vì tác nhân đôi khi chọn một hành động ngẫu nhiên nên nó cũng đã khám phá các trạng thái và hành động

### 00:07:08.000 - 00:07:09.000
không đi theo con đường tối ưu.

### 00:07:11.000 - 00:07:15.000
Điều tiếp theo chúng ta sẽ thấy là chính sách mà chúng ta đã đạt được.

### 00:07:16.000 - 00:07:17.000
Hãy thực thi ô này.

### 00:07:18.000 - 00:07:20.000
Và nó đây.

### 00:07:20.000 - 00:07:25.000
Như bạn có thể thấy, chính sách là tối ưu ở các trạng thái dẫn đến mục tiêu.

### 00:07:27.000 - 00:07:31.000
Và còn ở một số trạng thái khác xung quanh trạng thái ban đầu.

### 00:07:34.000 - 00:07:39.000
Ở các tiểu bang khác, mặc dù chúng tôi đã khám phá chúng, nhưng thuật toán đã đầu tư đủ nỗ lực để

### 00:07:39.000 - 00:07:41.000
tìm các giá trị tối ưu.

### 00:07:41.000 - 00:07:45.000
Nếu thay vì 10.000 tập, chúng tôi thực hiện nhiều tập hơn nữa.

### 00:07:46.000 - 00:07:52.000
Cuối cùng, chính sách sẽ tìm thấy những giá trị tối ưu đó vì đôi khi chính sách chọn một giá trị ngẫu nhiên

### 00:07:52.000 - 00:07:55.000
hành động và điều đó dẫn tác nhân đến các trạng thái khác nhau.

### 00:07:56.000 - 00:08:03.000
Đó là một trong những ưu điểm của phương pháp sai biệt thời gian là họ tập trung nỗ lực vào các trạng thái

### 00:08:03.000 - 00:08:06.000
và những hành động có vẻ hứa hẹn hơn.

### 00:08:07.000 - 00:08:12.000
Điều cuối cùng chúng ta sẽ làm là kiểm tra chính sách kết quả đối với môi trường.

### 00:08:14.000 - 00:08:18.000
Hãy nhấn shift và enter để chạy ô này và.

### 00:08:20.000 - 00:08:23.000
Quả thực, chúng tôi đã tìm được chính sách tối ưu.

### 00:08:23.000 - 00:08:27.000
Như bạn có thể thấy, nó đạt được mục tiêu thông qua con đường ngắn nhất.

