## Nội dung

### 00:00:00.000 - 00:00:07.440
Bây giờ chúng ta hãy bắt đầu đào tạo một tác nhân học tăng cường với Qtables.

### 00:00:07.440 - 00:00:13.599
Và trong bài giảng này, tôi sẽ chỉ trình bày cách nó có thể hoạt động.

### 00:00:13.599 - 00:00:18.559
Vì vậy, chỉ một tập có thể không phải là ý tưởng hay nhất, nhưng thực ra đó là cách đơn giản nhất

### 00:00:18.559 - 00:00:19.559
.

### 00:00:19.559 - 00:00:24.400
Và sau đó, trong bài giảng tiếp theo, chúng ta sẽ xem xét mã ở đây từng bước một.

### 00:00:24.400 - 00:00:26.320
Vì vậy, đừng lo lắng ở đây.

### 00:00:26.320 - 00:00:29.359
Và chúng ta vẫn lưu ở đây đào tạo DF.

### 00:00:29.359 - 00:00:32.640
Vì vậy, việc đào tạo của chúng ta nên dựa trên đào tạo DF.

### 00:00:32.640 - 00:00:39.120
Và ở đây, trong ví dụ đầu tiên và rất đơn giản này, chúng ta chỉ xem qua tập dữ liệu

### 00:00:39.120 - 00:00:41.399
đào tạo đầy đủ một lần.

### 00:00:41.399 - 00:00:45.120
Vì vậy, một tập từ đầu đến cuối.

### 00:00:45.120 - 00:00:51.679
Vì vậy, đây có thể không phải là ý tưởng hay nhất vì một vài lý do, nhưng vì mục đích đơn giản,

### 00:00:51.679 - 00:00:54.000
hãy thực hiện điều đó ở đây.

### 00:00:54.000 - 00:00:56.960
Và chúng ta cần Numpi và Pandas.

### 00:00:56.960 - 00:01:01.679
Bây giờ trong Thử thách người cho vay Luna và Thử thách thẻ leo núi, chúng ta đã thấy điều đó

### 00:01:01.679 - 00:01:08.480
việc nhận trạng thái tiếp theo dựa trên một hành động và nhận phần thưởng được thực hiện nội bộ

### 00:01:08.480 - 00:01:11.879
trong hoặc bởi thư viện phòng tập thể dục.

### 00:01:11.879 - 00:01:14.480
Và đây là một trong những khác biệt chính.

### 00:01:14.480 - 00:01:17.599
Vì vậy, chúng ta phải tự xác định trạng thái mới.

### 00:01:17.599 - 00:01:19.920
Vì vậy, chúng ta tạo một hàm do người dùng xác định.

### 00:01:19.920 - 00:01:23.280
Và chúng ta cũng phải tự xác định phần thưởng.

### 00:01:23.280 - 00:01:28.640
Vì vậy, không có gói hoặc thư viện nào thực hiện công việc cho chúng ta ở đây.

### 00:01:28.640 - 00:01:31.680
Vì vậy, chúng ta sẽ xem mã ở phần tiếp theo bài giảng.

### 00:01:31.680 - 00:01:36.439
Nhưng bây giờ chúng ta đã xác định được trạng thái và tính toán phần thưởng.

### 00:01:36.439 - 00:01:39.159
Và sau đó chúng ta có thể bắt đầu ở đây với một tập.

### 00:01:39.159 - 00:01:44.879
Và cũng ở đây chúng ta cần một số tham số học Q như alpha, gamma và epsilon.

### 00:01:44.879 - 00:01:51.000
Và khi bạn đang làm việc ở đây, chỉ với một tập, không có sự phân rã epsilon.

### 00:01:51.000 - 00:01:56.280
Và chúng ta cần xác định cấu trúc của bảng hàng đợi rồi tạo bảng hàng đợi

### 00:01:56.280 - 00:01:57.680
chính nó.

### 00:01:57.680 - 00:02:00.200
Và sau đó chúng ta khởi tạo tập dữ liệu.

### 00:02:00.200 - 00:02:04.760
Vì vậy, chúng tôi chỉ lấy chuỗi DF đầy đủ với tất cả các hàng.

### 00:02:04.760 - 00:02:07.719
Và sau đó chúng tôi lặp lại các bước.

### 00:02:07.719 - 00:02:11.800
Vậy tổng cộng, chúng tôi có gần 10.000 bước.

### 00:02:11.800 - 00:02:14.240
Và sau đó chúng tôi thực hiện một hành động.

### 00:02:14.240 - 00:02:18.680
Và thông thường trong 50% trường hợp của chúng tôi, đó sẽ là một hành động ngẫu nhiên vì chúng tôi có ở đây

### 00:02:18.680 - 00:02:22.920
epsilon bằng 50%.

### 00:02:22.920 - 00:02:24.640
Vậy đây là mã.

### 00:02:24.640 - 00:02:26.480
Và chúng ta hãy chạy nó.

### 00:02:26.480 - 00:02:37.920
Vậy là một tập với 9,999 hoặc 98 bước.

### 00:02:37.920 - 00:02:39.520
Và chúng ta đã đi đến cuối.

### 00:02:39.520 - 00:02:43.400
Và sau đó chúng ta có thể kiểm tra tổng phần thưởng cho tập này.

### 00:02:43.400 - 00:02:48.000
Vì vậy, trong trường hợp này, nó là dương 171.

### 00:02:48.000 - 00:02:53.639
Và sau đó chúng ta cũng có thể kiểm tra khung dữ liệu ở đây.

### 00:02:53.639 - 00:02:58.159
Và ở phía bên phải, chúng ta có thể thấy các vị thế giao dịch của mình.

### 00:02:58.159 - 00:03:06.479
Vì vậy, vì lý do đơn giản và cũng vì mục đích quy ước, ở đây chúng ta có vị trí 0, 1 và

### 00:03:06.479 - 00:03:07.479
2.

### 00:03:07.479 - 00:03:13.199
Vậy 0 là viết tắt của ngắn, 1 là trung lập và 2 là mua.

### 00:03:13.199 - 00:03:17.240
Và ở đây, điều rất quan trọng là bạn phải hiểu những điều sau.

### 00:03:17.240 - 00:03:20.000
Vì vậy, chúng ta có các thanh một giờ ở đây.

### 00:03:20.000 - 00:03:29.600
Và ở cuối thanh, chúng ta biết các tín hiệu mà chúng ta có thể sử dụng cho thanh tiếp theo.

### 00:03:29.600 - 00:03:32.040
Nhưng ở đây lợi nhuận là cho thanh này.

### 00:03:32.040 - 00:03:35.560
Vì vậy, nếu bạn đã đầu tư ở đầu thanh.

### 00:03:35.560 - 00:03:41.360
Và cũng ở đây, vị thế giao dịch là vị thế mà chúng ta đã thực hiện cho thanh ở đầu

### 00:03:41.360 - 00:03:42.719
của thanh.

### 00:03:42.719 - 00:03:46.240
Và chúng ta bắt đầu ở đây với một vị trí trung lập.

### 00:03:46.240 - 00:03:51.680
Và vị trí trung lập này sẽ mang lại phần thưởng là 0 cho thanh tiếp theo.

### 00:03:51.680 - 00:03:55.719
Và sau đó chúng ta giữ vị trí trung lập cho thanh tiếp theo và cả ở đây.

### 00:03:55.719 - 00:03:58.479
Và sau đó chúng ta có một vị thế bán.

### 00:03:58.479 - 00:04:03.039
Vì vậy, chúng ta cũng sẽ thấy điều này trong bài giảng tiếp theo, động lực học.

### 00:04:03.039 - 00:04:07.719
Và bây giờ chúng ta hãy lập bản đồ ở đây các vị trí trở về âm 1 lần.

### 00:04:07.719 - 00:04:11.560
Không trung lập và một trong thời gian dài.

### 00:04:11.560 - 00:04:17.360
Và điều này làm cho việc tính toán tổng phần thưởng ở đây dễ dàng hơn.

### 00:04:17.360 - 00:04:24.079
Vì vậy, chúng ta có thể chỉ cần nhân lợi nhuận với vị trí của thanh rồi cộng lại.

### 00:04:24.079 - 00:04:31.480
Và không có gì ngạc nhiên khi chúng ta kết thúc ở đây với 171 lợi nhuận dương theo thời gian.

### 00:04:31.480 - 00:04:35.680
Và cuối cùng chúng ta cũng có thể kiểm tra các vị trí.

### 00:04:35.680 - 00:04:40.439
Vì vậy, đây ít nhiều là một chiến lược ngẫu nhiên.

### 00:04:40.439 - 00:04:50.319
Vì vậy, không có hiệu quả học tập nào ở đây trong tập đầu tiên và trong 10.000 đầu tiên bước.

### 00:04:50.319 - 00:04:59.560
Vì vậy, đây chỉ là phần giới thiệu đơn giản về đào tạo học tăng cường cho nhân viên

### 00:04:59.560 - 00:05:01.399
nhân viên của chúng tôi.

### 00:05:01.399 - 00:05:04.360
Và tất nhiên cách tiếp cận này quá đơn giản.

### 00:05:04.360 - 00:05:06.959
Vì vậy, rất nhiều thứ còn thiếu.

### 00:05:06.959 - 00:05:09.839
Vì vậy, chúng ta nên sử dụng nhiều tập.

### 00:05:09.839 - 00:05:13.199
Chúng ta nên bao gồm chi phí đào tạo và hơn thế nữa.

### 00:05:13.199 - 00:05:17.399
Nhưng hãy xây dựng mã và chương trình đào tạo của chúng ta ở đây từng bước một.

### 00:05:17.399 - 00:05:19.759
Và chúng ta sẽ tiếp tục ở đây trong bài giảng tiếp theo.

