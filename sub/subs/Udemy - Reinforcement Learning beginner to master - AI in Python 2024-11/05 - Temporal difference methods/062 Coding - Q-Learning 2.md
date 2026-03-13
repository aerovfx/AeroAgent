## Nội dung

### 00:00:00.000 - 00:00:04.000
Trong video này, chúng ta sẽ triển khai thuật toán Q-learning.

### 00:00:04.000 - 00:00:06.000
Điều đầu tiên chúng ta sẽ làm.

### 00:00:08.000 - 00:00:13.000
Tạo chức năng mà tất nhiên sẽ gọi là q-learning.

### 00:00:13.000 - 00:00:16.000
Và chức năng này sẽ có một số đầu vào.

### 00:00:16.000 - 00:00:19.000
Đầu tiên là bảng giá trị Q.

### 00:00:21.000 - 00:00:24.000
Sau đó, chúng tôi sẽ thông qua chính sách thăm dò.

### 00:00:27.000 - 00:00:28.000
Và chính sách mục tiêu.

### 00:00:34.000 - 00:00:35.000
Và sau đó chúng ta sẽ vượt qua nó.

### 00:00:35.000 - 00:00:38.000
Các giá trị mà chúng tôi đã sử dụng trong thuật toán RSA.

### 00:00:39.000 - 00:00:45.000
Đầu tiên là số tập, cho chúng ta biết chúng ta sẽ thực hiện bao nhiêu lần

### 00:00:45.000 - 00:00:46.000
vòng lặp chính.

### 00:00:48.000 - 00:00:56.000
Đối số tiếp theo là alpha, đo tốc độ chúng ta cập nhật bảng giá trị Q dựa trên

### 00:00:56.000 - 00:00:57.000
ước tính mới.

### 00:00:59.000 - 00:01:06.000
Và đối số cuối cùng là Gamma, như bạn đã biết, là hệ số chiết khấu để điều chỉnh phần thưởng trong tương lai.

### 00:01:08.000 - 00:01:09.000
Và với tất cả điều này.

### 00:01:12.000 - 00:01:15.000
Chúng ta sẽ bắt đầu viết thuật toán.

### 00:01:16.000 - 00:01:22.000
Như bạn thấy, điều đầu tiên chúng ta phải làm là khởi tạo các chính sách và bảng giá trị q, sau đó

### 00:01:22.000 - 00:01:23.000
chúng tôi đã làm điều đó rồi.

### 00:01:23.000 - 00:01:28.000
Vì vậy, chúng ta có thể chuyển sang vòng lặp chính sẽ lặp lại cho mỗi tập.

### 00:01:39.000 - 00:01:41.000
Bên trong vòng lặp.

### 00:01:41.000 - 00:01:44.000
Điều đầu tiên chúng ta sẽ làm là khởi tạo tác vụ.

### 00:01:46.000 - 00:01:52.000
Chúng tôi sẽ thiết lập lại môi trường và điều đó sẽ tạo ra quan sát trạng thái ban đầu.

### 00:01:54.000 - 00:01:57.000
Sau đó chúng ta sẽ khai báo biến done.

### 00:01:57.000 - 00:02:00.000
Điều đó sẽ cho chúng ta biết liệu tập phim đã kết thúc hay chưa.

### 00:02:02.000 - 00:02:08.000
Sau đó, chúng ta đi vào vòng lặp bên trong, vòng lặp này sẽ lặp lại từng thời điểm cho đến khi kết thúc

### 00:02:08.000 - 00:02:09.000
tập.

### 00:02:09.000 - 00:02:10.000
Hãy viết.

### 00:02:10.000 - 00:02:18.000
Mặc dù chưa hoàn thành và những gì chúng ta sẽ làm trong vòng lặp này, trước hết, hãy chọn một hành động cho

### 00:02:18.000 - 00:02:19.000
trạng thái hiện tại.

### 00:02:20.000 - 00:02:26.000
Chúng tôi sẽ thực hiện điều đó bằng cách sử dụng chính sách khám phá và chuyển trạng thái đó làm đối số.

### 00:02:30.000 - 00:02:37.000
Điều tiếp theo chúng ta sẽ làm là thực hiện hành động và quan sát trạng thái tiếp theo, phần thưởng mà chúng ta nhận được,

### 00:02:37.000 - 00:02:43.000
giá trị mới cho biến Dom và từ điển thông tin trống.

### 00:02:47.000 - 00:02:52.000
Đó là những gì chúng ta thu được khi gọi phương thức bước, chuyển hành động được chính sách chọn.

### 00:02:54.000 - 00:02:59.000
Sau đó, chúng tôi sẽ chọn những hành động này để sử dụng trong quy tắc cập nhật.

### 00:03:03.000 - 00:03:08.000
Và chúng ta sẽ làm điều đó bằng cách sử dụng chính sách đích và chuyển nó làm đối số.

### 00:03:08.000 - 00:03:09.000
Trạng thái tiếp theo.

### 00:03:16.000 - 00:03:19.000
Và bây giờ chúng ta có hành động đó.

### 00:03:20.000 - 00:03:27.000
Điều tiếp theo chúng ta sẽ làm là lưu trữ ước tính giá trị hiện tại vào một biến riêng biệt.

### 00:03:27.000 - 00:03:36.000
Chúng ta sẽ gọi nó là Q s A và nó sẽ là giá trị được lưu trong bảng Q cho trạng thái hiện tại

### 00:03:36.000 - 00:03:37.000
và hành động.

### 00:03:38.000 - 00:03:45.000
Chúng ta cũng sẽ lưu trữ trong một biến riêng biệt ước tính giá trị Q của trạng thái tiếp theo đạt được bởi

### 00:03:45.000 - 00:03:49.000
tác nhân và hành động tiếp theo mà chúng ta vừa chọn.

### 00:04:00.000 - 00:04:04.000
Và bây giờ chúng tôi đã sẵn sàng để thực hiện cập nhật giá trị của mình.

### 00:04:05.000 - 00:04:07.000
Chúng ta sẽ làm gì.

### 00:04:08.000 - 00:04:10.000
Là chỉ mục bảng giá trị Q của chúng tôi.

### 00:04:10.000 - 00:04:14.000
To find the value of the present state and action.

### 00:04:19.000 - 00:04:23.000
Và chúng tôi sẽ cập nhật giá trị này theo công thức mà chúng tôi có ở trên.

### 00:04:25.000 - 00:04:35.000
Là ước tính giá trị hiện tại cộng với alpha nhân với phần thưởng thu được cộng với gamma nhân với ước tính giá trị Q

### 00:04:35.000 - 00:04:36.000
của thời điểm tiếp theo trong thời gian.

### 00:04:39.000 - 00:04:41.000
Trừ đi giá trị hiện tại của ước tính.

### 00:04:46.000 - 00:04:48.000
Và cuối cùng là chúng ta sẽ làm gì.

### 00:04:49.000 - 00:04:52.000
Là cập nhật giá trị của biến trạng thái.

### 00:04:54.000 - 00:04:57.000
Vì vậy, trong lần lặp tiếp theo của vòng lặp, chúng tôi sẽ cập nhật.

### 00:04:58.000 - 00:05:00.000
Trạng thái tiếp theo mà tác nhân đạt được.

### 00:05:05.000 - 00:05:07.000
Hãy chú ý đến một vài chi tiết.

### 00:05:07.000 - 00:05:13.000
Đầu tiên trong số đó là hành động đã được chọn bằng chính sách mục tiêu.

### 00:05:13.000 - 00:05:18.000
Và vì lý do đó, nó không nhất thiết phải là hành động tiếp theo mà chúng tôi sắp cập nhật

### 00:05:18.000 - 00:05:23.000
bởi vì hành động tiếp theo sẽ được chọn theo chính sách khám phá.

### 00:05:24.000 - 00:05:31.000
Chính sách thăm dò quyết định tác nhân đi đâu, khi nào nó tương tác với môi trường.

### 00:05:31.000 - 00:05:36.000
Và chính sách đích xác định cách cập nhật giá trị Q.

### 00:05:37.000 - 00:05:41.000
Trong thuật toán Sarsa, sử dụng chiến lược học chính sách.

### 00:05:41.000 - 00:05:45.000
Cả hai nhiệm vụ này đều được thực hiện bởi cùng một chính sách.

### 00:05:50.000 - 00:05:57.000
Được rồi, bây giờ chúng ta đã triển khai xong thuật toán, hãy chạy ô này và chúng ta sẽ có nó.

### 00:05:57.000 - 00:05:59.000
Hãy cuộn một chút.

### 00:05:59.000 - 00:06:01.000
Và bây giờ hãy gọi thuật toán.

### 00:06:05.000 - 00:06:12.000
Truyền dưới dạng đối số, bảng giá trị Q, chính sách khám phá và chính sách đích.

### 00:06:20.000 - 00:06:23.000
Và cuối cùng, chúng tôi sẽ cho nó một nghìn tập.

### 00:06:23.000 - 00:06:25.000
Hãy thực hiện thuật toán.

### 00:06:32.000 - 00:06:34.000
Và ở đây chúng tôi có nó.

### 00:06:34.000 - 00:06:37.000
Hãy xem kết quả mà chúng ta đã thu được.

### 00:06:38.000 - 00:06:38.000
Rất tiếc.

### 00:06:39.000 - 00:06:41.000
Đây là một lỗi nhỏ.

### 00:06:41.000 - 00:06:43.000
Đây là một bảng giá trị.

### 00:06:43.000 - 00:06:44.000
Được rồi?

### 00:06:45.000 - 00:06:50.000
Bây giờ chúng ta hãy quan sát kết quả mà chúng ta đã thu được.

### 00:06:53.000 - 00:06:55.000
Và thì đấy, nó đây rồi.

### 00:06:55.000 - 00:07:01.000
Như bạn có thể thấy trong đường dẫn chính, các hành động có giá trị Q cao nhất là những hành động đưa chúng ta đến

### 00:07:01.000 - 00:07:02.000
mục tiêu.

### 00:07:08.000 - 00:07:11.000
Bây giờ hãy xem chính sách mà chúng tôi đã thu được.

### 00:07:14.000 - 00:07:21.000
Hãy chú ý đến thực tế là các hành động được thực hiện theo chính sách trên con đường chính sẽ đưa chúng ta đến mục tiêu.

### 00:07:24.000 - 00:07:31.000
Nhưng ở các bang còn lại, chẳng hạn, họ cũng ở bang này, chính sách quy định

### 00:07:31.000 - 00:07:34.000
di chuyển sang trái, trên thực tế đó là hành động tối ưu.

### 00:07:35.000 - 00:07:36.000
Tại sao bạn nghĩ điều này xảy ra?

### 00:07:38.000 - 00:07:44.000
Chà, điều đó xảy ra vì chính sách thăm dò đã đến thăm khá thường xuyên, tất cả các bang.

### 00:07:49.000 - 00:07:53.000
Mặc dù chính sách mục tiêu đã học được những hành động tốt nhất.

### 00:07:53.000 - 00:08:01.000
Chính sách khám phá là một chính sách ngẫu nhiên xuyên suốt toàn bộ quá trình học tập, và điều đó đã

### 00:08:01.000 - 00:08:08.000
cho tác nhân cơ hội khám phá tất cả các trạng thái này và hiểu rõ về các giá trị Q thực

### 00:08:08.000 - 00:08:11.000
và hành động tối ưu trong tất cả chúng.

### 00:08:11.000 - 00:08:18.000
Đó là một trong những lợi thế của việc sử dụng thuật toán học tập ngoài chính sách, bởi vì chúng ta có thể tách việc học

### 00:08:18.000 - 00:08:20.000
quá trình từ cuộc thăm dò.

### 00:08:20.000 - 00:08:27.000
Chúng ta có thể sử dụng chính sách chọn hành động tối ưu trong hầu hết thời gian và chỉ một lần trong

### 00:08:27.000 - 00:08:28.000
khám phá một lúc.

### 00:08:28.000 - 00:08:35.000
Hoặc chúng ta có thể chọn một chính sách tích cực hơn nhiều trong việc khám phá nó, đó là những gì chúng tôi đã làm

### 00:08:35.000 - 00:08:36.000
trong trường hợp này.

### 00:08:37.000 - 00:08:43.000
Điều cuối cùng chúng ta sẽ làm là kiểm tra tác nhân tạo thành trong môi trường.

### 00:08:43.000 - 00:08:46.000
Đối với điều đó, chúng tôi sẽ sử dụng chính sách mục tiêu.

### 00:08:49.000 - 00:08:51.000
Hãy thực thi ô này.

### 00:08:51.000 - 00:08:53.000
Và như chúng tôi mong đợi.

### 00:08:55.000 - 00:08:59.000
Chính sách mục tiêu có khả năng tìm ra lối thoát.

