## Nội dung

### 00:00:00.000 - 00:00:07.280
Được rồi, chúng ta vẫn lưu bảng hàng đợi đã được huấn luyện một phần từ bài giảng trước.

### 00:00:07.280 - 00:00:13.400
Và bây giờ chúng ta thực sự cũng có thể lưu bảng hàng đợi, đó là một mảng cục bộ trên thiết bị

### 00:00:13.400 - 00:00:18.640
của chúng ta với np.save và chúng ta phải chỉ định một tên tệp.

### 00:00:18.640 - 00:00:25.359
Vì vậy, ví dụ: bảng xếp hàng dot n p y và chúng ta phải chuyển đối tượng vào đây.

### 00:00:25.359 - 00:00:32.759
Vì vậy, bảng xếp hàng, vì vậy chúng ta sẽ không làm điều này bây giờ vì bảng xếp hàng không đủ tốt

### 00:00:32.759 - 00:00:34.159
ở đây.

### 00:00:34.159 - 00:00:41.679
Và để có được một tác nhân được đào tạo khá tốt, bạn có thể chạy mã đào tạo ba lần với

### 00:00:41.679 - 00:00:46.120
trong tổng số 150.000 tập.

### 00:00:46.120 - 00:00:53.519
Và sau lần chạy đầu tiên, bạn không nên quên bỏ qua phần khởi tạo của bảng xếp hàng ngẫu nhiên

### 00:00:53.519 - 00:00:54.519
.

### 00:00:54.600 - 00:00:59.520
Vì vậy, nếu bạn chạy mã này ba lần, thì bạn sẽ có được một tác nhân khá tốt.

### 00:00:59.880 - 00:01:06.000
Nhưng nếu bạn không có khả năng tính toán hoặc thời gian để đào tạo cái này, thì bạn có thể

### 00:01:06.000 - 00:01:11.120
thực sự tải xuống tác nhân được đào tạo ở đây từ chi phí liệu.

### 00:01:11.520 - 00:01:17.800
Và tôi cung cấp mảng phức tạp kèm theo bài giảng này.

### 00:01:17.800 - 00:01:20.320
Vì vậy, tiết kiệm việc tải và kiểm tra một tác nhân đã được đào tạo.

### 00:01:20.599 - 00:01:26.119
Vì vậy, trong một tệp zip, nhưng hãy đảm bảo rằng bạn có đủ bộ nhớ.

### 00:01:26.439 - 00:01:31.879
Vì vậy, tệp zip và mảng numpy bên dưới khá lớn.

### 00:01:31.879 - 00:01:34.519
Vì vậy, khoảng 600 megabyte.

### 00:01:35.159 - 00:01:39.159
Vì vậy, trong trường hợp bạn không có bộ nhớ, vui lòng không tải xuống.

### 00:01:39.519 - 00:01:44.639
Và nếu không, bạn có thể nhấp vào đây trên tệp zip và tải xuống tệp.

### 00:01:45.040 - 00:01:51.519
Và sau đó nếu bạn đã tải xuống tệp zip, trước tiên bạn phải giải nén tệp bằng lệnh giải nén

### 00:01:51.519 - 00:01:52.519
all.

### 00:01:52.519 - 00:01:55.879
Và sau đó bạn sẽ nhận được tệp Npy đã giải nén.

### 00:01:55.879 - 00:01:59.760
Và bạn phải di chuyển tệp ở đây vào thư mục vật liệu chi phí.

### 00:01:59.879 - 00:02:01.200
Vì vậy, điều này rất quan trọng.

### 00:02:01.200 - 00:02:05.000
Hãy giải nén nó vào thư mục vật liệu chi phí.

### 00:02:05.280 - 00:02:07.560
Và sau đó bạn có thể chỉ cần sử dụng nó.

### 00:02:08.680 - 00:02:10.319
Vì vậy, hãy để tôi chứng minh điều này.

### 00:02:10.319 - 00:02:16.759
Và tôi đã có dấu chấm qtable NPWIFI trong thư mục vật liệu chi phí của mình.

### 00:02:17.159 - 00:02:23.799
Và nếu đúng như vậy, bạn chỉ cần tải nó ở đây vào Python với tải dấu chấm NP.

### 00:02:27.799 - 00:02:33.120
Vì vậy, hãy khởi động lại kernel, chỉ để chứng minh rằng chúng ta có thể làm điều này từ đầu.

### 00:02:33.439 - 00:02:35.079
Vì vậy, không có gì an toàn ở đây.

### 00:02:35.560 - 00:02:37.879
Và đầu tiên chúng ta cần amnazium và numpy.

### 00:02:38.280 - 00:02:41.519
Và sau đó chúng ta có thể tải qtable đã huấn luyện với NP dotload.

### 00:02:42.680 - 00:02:48.199
Và ở đây chúng ta có qtable, qtable đã huấn luyện với hình dạng sau.

### 00:02:48.879 - 00:02:55.960
Và sau đó để chạy thử nghiệm, chúng ta phải đảm bảo rằng chúng ta có kiến trúc tương ứng của qtable.

### 00:02:56.519 - 00:03:00.840
Vì vậy, chúng ta phải làm như vậy chỉ định số thùng cơ bản và cả không gian quan sát.

### 00:03:01.199 - 00:03:04.280
Và chúng ta phải xác định trạng thái rời rạc của hàm.

### 00:03:04.680 - 00:03:10.759
Vì vậy, trong mã kiểm tra, trạng thái rời rạc là một phần của mã.

### 00:03:12.159 - 00:03:20.719
Vì vậy, ở đây và trạng thái rời rạc thực sự sử dụng không gian quan sát và cả số lượng thùng.

### 00:03:20.719 - 00:03:21.960
Vì vậy, chúng ta cần điều này ở đây.

### 00:03:22.360 - 00:03:28.439
Vì vậy, bất cứ khi nào chúng ta tải ở đây, qtable, chúng ta cần biết kiến trúc cơ bản.

### 00:03:29.439 - 00:03:31.439
Vì vậy, hãy lưu nó ở đây.

### 00:03:31.439 - 00:03:39.439
Và bây giờ chúng tôi có thể chạy chẳng hạn, 2000 tập thử nghiệm các tập mà không cần sự hiển thị của con người.

### 00:03:42.039 - 00:03:46.240
Và chúng tôi cũng có thể đặt ở đây một vị trí ngẫu nhiên để tái tạo.

### 00:03:47.240 - 00:03:49.240
Vì vậy, hãy xem những gì chúng ta nhận được ở đây.

### 00:03:49.439 - 00:03:54.240
Vậy đặc vụ này được đào tạo với 150.000 tập.

### 00:03:55.240 - 00:04:00.240
Và như bạn có thể thấy, hiệu suất thử nghiệm khá tốt.

### 00:04:00.240 - 00:04:03.240
Vì vậy, tỷ lệ thành công là 62,5%.

### 00:04:03.240 - 00:04:07.240
Và tổng phần thưởng trung bình là 172.

### 00:04:07.240 - 00:04:13.240
Vì vậy, hãy nhớ lại rằng một tập có phần thưởng 200 được coi là thành công.

### 00:04:13.240 - 00:04:18.240
Và chúng ta cũng có thể hình dung phần thưởng thử nghiệm.

### 00:04:18.240 - 00:04:21.240
Vậy 2000 phần thưởng thử nghiệm trong biểu đồ.

### 00:04:22.240 - 00:04:24.240
Vậy đây là 200.

### 00:04:24.240 - 00:04:28.240
Và hầu hết các tập đều thành công.

### 00:04:28.240 - 00:04:30.240
Vì vậy, đây là những lần hạ cánh thành công.

### 00:04:30.240 - 00:04:36.240
Và chúng ta cũng có thể thấy rằng chúng ta có rất ít lần hạ cánh hoàn toàn sai lầm.

### 00:04:36.240 - 00:04:37.240
Vì vậy, sự cố.

### 00:04:37.240 - 00:04:41.240
Và ở đây chúng ta có một cú va chạm khác.

### 00:04:41.240 - 00:04:43.240
Và đây là những lần hạ cánh hoàn toàn sai lầm.

### 00:04:43.240 - 00:04:48.240
Vì vậy, sự cố.

### 00:04:48.240 - 00:04:49.240
Và ở đây chúng ta có một cú va chạm khác.

### 00:04:50.240 - 00:04:55.240
Và đây là những lần hạ cánh.

### 00:04:55.240 - 00:05:00.240
Và chúng ta sẽ thấy trong bài giảng tiếp theo rằng đây là những kiểu hạ cánh cứng.

### 00:05:00.240 - 00:05:06.240
Vì vậy không có sự cố.

### 00:05:06.240 - 00:05:13.240
Hạ cánh khó khăn khi chúng ta không nhận được phần thưởng cộng 100.

### 00:05:13.240 - 00:05:17.240
Vì vậy, hãy nhớ lại rằng chỉ nhận được phần thưởng cộng 100 khi hạ cánh mềm.

### 00:05:17.240 - 00:05:21.240
Và ở đây chúng ta không nhận được phần thưởng hạ cánh mềm là 100.

### 00:05:21.240 - 00:05:22.240
Vì vậy, chúng ta sẽ thấy điều này trong bài giảng tiếp theo, nơi chúng ta sẽ hình dung một số giai đoạn thử nghiệm.

