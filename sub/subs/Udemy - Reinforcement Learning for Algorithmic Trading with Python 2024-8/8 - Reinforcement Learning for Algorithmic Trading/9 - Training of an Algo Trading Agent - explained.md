## Nội dung

### 00:00:00.000 - 00:00:04.320
Được rồi, hãy tiếp tục ở đây với hướng dẫn từng bước.

### 00:00:04.320 - 00:00:10.720
Vì vậy, hãy giải thích ngắn gọn những gì chúng tôi đã làm ở đây trong bài giảng trước.

### 00:00:10.720 - 00:00:17.400
Vì vậy, chúng tôi huấn luyện đặc vụ của mình ở đây cho một tập với gần 10.000 bước.

### 00:00:17.400 - 00:00:21.160
Và bây giờ chúng ta hãy kiểm tra ở đây một hoặc hai bước đầu tiên.

### 00:00:21.160 - 00:00:26.760
Vậy động lực và chúng ta có ở đây một số thông số học tập Q.

### 00:00:26.760 - 00:00:29.600
Và sau đó chúng ta xác định ở đây số lượng thùng.

### 00:00:29.600 - 00:00:38.000
Vì vậy, chúng ta có năm tính năng liên tục và chúng ta có ở đây phân tách các tính năng đó thành 11 thùng.

### 00:00:38.000 - 00:00:44.120
Và sau đó chúng tôi cũng sử dụng vị trí giao dịch hiện tại làm tính năng khác.

### 00:00:44.120 - 00:00:46.960
Và ở đây chúng tôi có ba giá trị có thể.

### 00:00:46.960 - 00:00:52.280
Và chúng ta không nên quên rằng bảng Q chứa tất cả các cặp hành động trạng thái.

### 00:00:52.280 - 00:00:59.320
Vì vậy, chúng tôi đã đưa ba hành động ở đây vào số lượng thùng.

### 00:00:59.320 - 00:01:06.000
Và với điều này, chúng ta có thể dễ dàng xác định và tạo bảng Q với các kích thước sau.

### 00:01:06.000 - 00:01:09.240
Vì vậy, bảng Q chứa tất cả các cặp hành động trạng thái.

### 00:01:09.240 - 00:01:15.960
Và với điều này, chúng ta có thể dễ dàng xác định và tạo bảng Q với các kích thước sau.

### 00:01:15.959 - 00:01:24.639
Vì vậy, bảng Q chứa tất cả các cặp hành động trạng thái.

### 00:01:24.639 - 00:01:28.280
Và chúng ta khởi tạo Q bảng chỉ có các số ngẫu nhiên giữa trừ một và cộng một.

### 00:01:28.280 - 00:01:31.919
Và trước đây chúng ta đã thấy rằng chúng ta có khoảng 1,44 triệu cặp hành động trạng thái khác nhau.

### 00:01:31.919 - 00:01:34.879
Và chúng ta hãy kiểm tra ở đây giá trị tối thiểu và giá trị tối đa.

### 00:01:34.879 - 00:01:41.919
Vậy chúng gần bằng âm một và cộng một.

### 00:01:41.920 - 00:01:47.920
Và sau đó chúng ta có hai hàm trợ giúp ở đây.

### 00:01:47.920 - 00:01:50.760
Vì vậy, hãy lấy trạng thái, lấy trạng thái hiện tại dựa trên một hành động và tính toán phần thưởng.

### 00:01:50.760 - 00:01:53.079
Vì vậy, chúng ta sẽ thấy điều này sau vài phút nữa.

### 00:01:53.079 - 00:01:55.680
Nhưng bây giờ, hãy bắt đầu ở đây với các khung dữ liệu huấn luyện.

### 00:01:55.680 - 00:01:58.359
Vì vậy, đây là tập dữ liệu đầy đủ.

### 00:01:58.359 - 00:02:03.760
Và chúng ta khởi tạo tổng số phần thưởng.

### 00:02:03.760 - 00:02:07.480
Vì vậy, chúng tôi bắt đầu với số 0.

### 00:02:07.480 - 00:02:14.960
Và bây giờ nếu bạn chỉ muốn đào tạo tác nhân trên toàn bộ tập dữ liệu,

### 00:02:14.960 - 00:02:18.039
thì chúng tôi thường bắt đầu với hàng số 0.

### 00:02:18.039 - 00:02:20.920
Vì vậy, ngay hàng đầu tiên và do đó chúng tôi chọn ở đây tất cả các hàng từ tàu DF.

### 00:02:20.920 - 00:02:23.719
Và tất nhiên chúng tôi có thể làm điều này khác đi.

### 00:02:23.719 - 00:02:28.039
Vì vậy, chúng tôi chỉ có thể chọn các tập hợp con.

### 00:02:28.039 - 00:02:31.960
Và chúng ta sẽ thấy điều này trong một trong các bài giảng tiếp theo.

### 00:02:31.960 - 00:02:34.240
Nhưng bây giờ, hãy tạo dữ liệu khung dữ liệu ở đây.

### 00:02:34.240 - 00:02:36.879
Và sau đó chúng ta khởi tạo vị trí đối tượng trạng thái bổ sung.

### 00:02:36.879 - 00:02:42.919
Vì vậy, đó là vị trí hiện tại.

### 00:02:42.919 - 00:02:47.680
Và chúng ta sử dụng ở đây một.

### 00:02:47.680 - 00:02:58.159
Vì vậy, ở đây chúng ta sử dụng số 0 cho ngắn gọn, một cho trung tính và hai cho dài hạn.

### 00:02:58.159 - 00:03:04.800
Vì vậy, chúng ta không muốn có số âm ở đây.

### 00:03:04.840 - 00:03:08.439
Vì vậy, đây là khung dữ liệu thực sự có sáu tính năng và lợi nhuận của chúng ta.

### 00:03:08.439 - 00:03:12.400
Và sau đó, trong bước đầu tiên, chúng ta chỉ đi vào phần đầu tiên bar.

### 00:03:12.400 - 00:03:20.880
Vậy đó là hàng.

### 00:03:20.880 - 00:03:24.040
Và giả định là chúng ta đang ở cuối thanh.

### 00:03:24.040 - 00:03:28.480
Vì vậy, nếu không thì chúng ta sẽ không biết ở đây giá trị hoặc lợi nhuận của thanh.

### 00:03:28.479 - 00:03:31.359
Và sau đó chúng ta có thể chuyển đổi hàng ở đây thành trạng thái.

### 00:03:31.359 - 00:03:35.359
Vì vậy, đây chỉ là một bộ dữ liệu có các tính năng trạng thái.

### 00:03:35.359 - 00:03:38.679
Vì vậy, tỷ lệ SMA chi tiêu trả về,

### 00:03:38.679 - 00:03:41.319
xây dựng biểu đồ MACD.

### 00:03:41.319 - 00:03:43.239
RSI, đây là bộ dao động Custick.

### 00:03:43.239 - 00:03:49.159
Và cuối cùng cũng là vị trí ở đây.

### 00:03:49.159 - 00:03:53.439
Rất trung lập.

### 00:03:53.439 - 00:03:59.120
Và dựa trên trạng thái ở đây, chúng ta có thể xác định hành động của hành động tiếp theo.

### 00:03:59.120 - 00:04:01.199
Và hãy nhớ rằng ở đây chúng ta có epsilon là 50%.

### 00:04:01.199 - 00:04:04.039
Vì vậy, có 50% khả năng là chúng ta chỉ thực hiện một hành động ngẫu nhiên ở đây.

### 00:04:04.039 - 00:04:08.039
0, 1 hoặc 2.

### 00:04:08.039 - 00:04:10.840
Và như thể chúng ta không lấy ngẫu nhiên hành động,

### 00:04:10.840 - 00:04:13.840
chúng ta chỉ thực hiện hành động tốt nhất theo bảng xếp hàng.

### 00:04:13.840 - 00:04:17.560
Vì vậy, đó là giá trị cao nhất.

### 00:04:17.560 - 00:04:19.319
Vì vậy, chúng ta có thể chạy ở đây nhiều lần.

### 00:04:19.319 - 00:04:23.279
Và vì có một quá trình ngẫu nhiên liên quan,

### 00:04:23.279 - 00:04:25.759
chúng ta sẽ có những hành động khác nhau ở đây.

### 00:04:25.759 - 00:04:31.920
Vì vậy, chúng ta hãy tiếp tục ở đây để tiếp tục.

### 00:04:31.920 - 00:04:39.159
Vì vậy, hãy đợi cả hai ở đây.

### 00:04:39.159 - 00:04:45.120
Và bây giờ, hãy kiểm tra các giá trị trong bảng hàng đợi cho trạng thái hiện tại của chúng ta.

### 00:04:45.120 - 00:04:49.840
Vậy đây là cho hành động 0, cho hành động 1 và cho hành động 2.

### 00:04:49.840 - 00:04:55.480
Và dựa trên điều này, chúng ta sẽ nhận được phần thưởng cao nhất khi mua.

### 00:04:55.480 - 00:04:58.040
Vì vậy, đây chỉ là những con số ngẫu nhiên, nên những con số ban đầu.

### 00:04:58.040 - 00:05:00.920
Và nếu chúng ta kiểm tra điều này với np.argmax, chúng ta sẽ đưa ra hành động 2.

### 00:05:00.920 - 00:05:04.639
Vì vậy, hãy mua.

### 00:05:04.639 - 00:05:09.240
Vì vậy, trong trường hợp này ở đây, hành động của chúng ta là 2.

### 00:05:09.240 - 00:05:11.959
Và sau đó chúng ta có thể xác định vị trí giao dịch tiếp theo.

### 00:05:11.959 - 00:05:16.000
Và hành động trực tiếp chuyển sang vị trí mới.

### 00:05:16.000 - 00:05:22.199
Vì vậy, chúng ta mua công cụ.

### 00:05:22.199 - 00:05:27.439
Và sau đó vị trí tiếp theo ngay lập tức là 2.

### 00:05:27.439 - 00:05:32.159
Và sau đó chúng ta nên thực hiện tất cả các bước để xác định trạng thái tiếp theo và phần thưởng.

### 00:05:32.159 - 00:05:33.919
Và hiện tại chúng ta đang ở bước đầu tiên ở vị trí chỉ số 0.

### 00:05:33.919 - 00:05:37.319
Và vì vậy, chúng ta có thể cập nhật vị trí cho hàng tiếp theo.

### 00:05:37.319 - 00:05:43.439
Vì vậy, hãy quay lại đây.

### 00:05:43.439 - 00:05:48.040
Vì vậy, chúng ta đang ở đây, ở cuối thanh đầu tiên.

### 00:05:48.040 - 00:05:50.600
Và sau đó dựa trên trạng thái hoặc dựa trên một quyết định ngẫu nhiên,

### 00:05:50.600 - 00:05:54.439
chúng ta lấy vị trí 2 cho thanh tiếp theo.

### 00:05:54.439 - 00:06:00.199
Vì vậy, đây là những gì chúng ta đang làm ở đây.

### 00:06:00.199 - 00:06:03.319
Vì vậy, bây giờ chúng ta có một vị thế mua cho thanh tiếp theo.

### 00:06:03.319 - 00:06:07.279
Vì vậy, chúng ta giữ nhạc cụ từ đầu đến cuối.

### 00:06:07.279 - 00:06:12.359
Và sau đó chúng ta cũng có thể đến hàng tiếp theo.

### 00:06:12.359 - 00:06:20.279
Vì vậy, đây là vị trí mới.

### 00:06:20.279 - 00:06:22.439
Vì vậy, chúng ta có ở đây 10, 10, 8, 9.

### 00:06:22.439 - 00:06:27.599
Và có hàng tiếp theo, chúng ta có thể xác định trạng thái tiếp theo bằng hàm get trạng thái.

### 00:06:27.599 - 00:06:33.159
Vì vậy, điều này đơn giản được dịch ở đây.

### 00:06:33.160 - 00:06:38.840
Những con số này thành một cú lật đổ đơn giản, giảm lợi nhuận xuống đây.

### 00:06:38.840 - 00:06:43.400
Vì vậy, chúng ta có một cú lật đổ ở đây với sáu tính năng trạng thái.

### 00:06:43.400 - 00:06:45.960
Và sau đó có vị thế giao dịch cho hàng tiếp theo và lợi nhuận cho hàng tiếp theo,

### 00:06:45.960 - 00:06:49.320
chúng ta có thể xác định và tính toán phần thưởng của hàng tiếp theo.

### 00:06:49.320 - 00:06:51.480
Vì vậy, hãy kiểm tra điều này ở đây.

### 00:06:51.480 - 00:06:54.440
Vì vậy, lợi nhuận cho hàng tiếp theo là cộng 1,34.

### 00:06:54.440 - 00:07:02.200
Và chúng ta có một vị thế mua.

### 00:07:02.199 - 00:07:08.360
Và do đó phần thưởng sẽ là số dương.

### 00:07:08.360 - 00:07:13.879
Vì vậy, 1,34 nếu lợi nhuận trực tiếp chuyển thành phần thưởng.

### 00:07:13.879 - 00:07:20.680
Vì vậy, đây có thể là thời điểm tốt nhất để kiểm tra ở đây, tính toán phần thưởng.

### 00:07:20.680 - 00:07:23.159
Vì vậy, chúng ta chuyển vị trí và lợi nhuận sang đây để tính phần thưởng.

### 00:07:23.159 - 00:07:29.639
Và nếu chúng ta có một vị thế mua, thì tính toán phần thưởng sẽ quay trở lại lợi nhuận.

### 00:07:29.639 - 00:07:34.680
Rất tích cực cho lợi nhuận dương.

### 00:07:34.680 - 00:07:39.240
Và nếu không, nếu vị trí là 0, thì chúng ta có phần thưởng nghịch đảo.

### 00:07:39.240 - 00:07:44.039
Và nếu không, nếu chúng ta có vị trí trung lập, tức là 1, thì chúng ta quay lại đây 0.

### 00:07:44.039 - 00:07:50.519
Vì vậy, nếu chúng ta không có bất kỳ vị trí nào, thì phần thưởng là 0.

### 00:07:50.519 - 00:07:54.439
Nhưng một lần nữa, đây là cách tính phần thưởng đơn giản và dễ hiểu nhất.

### 00:07:54.519 - 00:07:59.319
Và chúng ta có thể làm điều này phức tạp hơn nhiều với nhiều tính năng hơn.

### 00:07:59.319 - 00:08:03.240
Nhưng hãy bắt đầu ở đây với giải pháp đơn giản.

### 00:08:03.240 - 00:08:06.600
Vì vậy, nếu chúng ta vượt qua vị trí tiếp theo và lợi nhuận của thanh tiếp theo ở đây,

### 00:08:06.600 - 00:08:09.399
thì chúng ta sẽ nhận được phần thưởng của thanh đó cộng với 1,34.

### 00:08:09.399 - 00:08:15.240
Và bây giờ có phần thưởng, chúng ta có thể cập nhật bảng xếp hàng.

### 00:08:15.240 - 00:08:20.519
Vì vậy, trạng thái hiện tại như sau.

### 00:08:20.519 - 00:08:23.159
Vì vậy, chúng ta có giá trị 0,86 cho công cụ hành động.

### 00:08:23.240 - 00:08:25.720
Và đây chính là mã mà chúng ta đã sử dụng trong Thử thách người cho vay Luna.

### 00:08:25.720 - 00:08:27.800
Và thử thách thẻ núi.

### 00:08:27.800 - 00:08:33.160
Vì vậy, chúng tôi xác định điều tốt nhất hành động tiếp theo.

### 00:08:33.160 - 00:08:38.120
Chúng tôi tính toán mục tiêu TD.

### 00:08:38.920 - 00:08:42.920
Và sau đó chúng tôi cập nhật giá trị cho trạng thái và hành động nhất định.

### 00:08:42.920 - 00:08:48.920
Và ở đây chúng tôi cũng tính đến tác động của việc truyền ngược.

### 00:08:48.919 - 00:08:54.839
Vì vậy, việc cập nhật giá trị hàng đợi không chỉ phụ thuộc vào phần thưởng hiện tại,

### 00:08:54.839 - 00:08:57.079
 mà còn phụ thuộc vào phần thưởng trong tương lai, điều quan trọng ở đây và ở đây.

### 00:08:58.599 - 00:09:04.919
Chúng tôi có thể thấy rằng chúng tôi có thể tăng thêm giá trị cho hành động số hai

### 00:09:04.919 - 00:09:07.240
 vì nó mang lại phần thưởng tích cực.

### 00:09:07.799 - 00:09:11.079
Và cuối cùng, chúng tôi có thể tăng tổng phần thưởng của tập theo phần thưởng theo bước.

### 00:09:12.439 - 00:09:16.120
Và sau đó chúng tôi ghi đè trạng thái.

### 00:09:16.840 - 00:09:18.919
Vì vậy, trong bước tiếp theo, chúng tôi thực sự làm việc với trạng thái tiếp theo.

### 00:09:20.200 - 00:09:23.240
Và sau đó chúng tôi đã hoàn tất một bước.

### 00:09:24.759 - 00:09:26.679
Và sau đó chúng tôi có bước tiếp theo.

### 00:09:28.279 - 00:09:33.159
Vì vậy, chúng tôi có một trạng thái mới nên ở bước cuối cùng.

### 00:09:33.960 - 00:09:36.120
Chúng tôi đã xác định trạng thái mới.

### 00:09:38.039 - 00:09:42.039
Và dựa trên trạng thái mới, chúng tôi thực sự có thể xác định hành động tiếp theo một lần nữa.

### 00:09:42.120 - 00:09:46.919
Và điều này đã đến lúc nó chuyển sang trạng thái trung lập.

### 00:09:50.120 - 00:09:52.039
Và sau đó chúng ta cũng có thể kiểm tra các giá trị trong bảng hàng đợi cho trạng thái này.

### 00:09:52.039 - 00:09:54.039
Vì vậy, giá trị cao nhất thực sự ở đây là trung lập.

### 00:09:55.240 - 00:09:57.240
Và vị trí tiếp theo.

### 00:09:58.039 - 00:09:59.959
Vì vậy, nếu chúng ta chuyển sang trạng thái trung tính là một.

### 00:10:03.079 - 00:10:06.360
Vì vậy, hãy tăng dần bước.

### 00:10:06.360 - 00:10:08.039
Và chúng ta hiện đang ở bước thứ hai.

### 00:10:08.039 - 00:10:10.839
Và sau đó chúng ta cập nhật vị trí cho hàng tiếp theo.

### 00:10:11.399 - 00:10:12.280
Vậy là hàng thứ ba.

### 00:10:14.040 - 00:10:16.280
Và bây giờ chúng ta nên có một hàng ở đây.

### 00:10:17.800 - 00:10:20.360
Vậy vẫn còn một.

### 00:10:22.680 - 00:10:26.920
Nhưng có lẽ chúng ta hãy thử lấy số 0 ở đây.

### 00:10:28.519 - 00:10:29.879
Như vậy sẽ tốt hơn cho mục đích trình diễn.

### 00:10:31.480 - 00:10:33.560
Vì vậy, bây giờ chúng ta nên có một số 0 ở đây và sau đó là thanh tiếp theo.

### 00:10:34.360 - 00:10:36.280
Đó là trường hợp ở đây.

### 00:10:36.280 - 00:10:37.800
Và sau đó chúng ta có thể có hàng thứ ba.

### 00:10:37.879 - 00:10:38.679
Với vị trí mới.

### 00:10:39.399 - 00:10:41.240
Sau đó, trạng thái tiếp theo.

### 00:10:41.879 - 00:10:43.399
Là một bộ dữ liệu.

### 00:10:43.959 - 00:10:48.439
Và sau đó chúng ta có thể tính toán phần thưởng.

### 00:10:48.439 - 00:10:53.559
Vì vậy, chúng ta có một vị thế bán.

### 00:10:53.559 - 00:10:54.759
Và lợi nhuận hơi âm đối với vị thế mua.

### 00:10:55.479 - 00:10:57.639
Và do đó, chúng ta sẽ có phần thưởng dương ở đây cho vị thế bán.

### 00:10:58.359 - 00:11:01.719
Vì vậy, hãy kiểm tra điều này ở đây.

### 00:11:02.279 - 00:11:06.279
Chúng ta sẽ nhận được cộng 0,2.

### 00:11:06.919 - 00:11:08.199
Và sau đó chúng ta cập nhật giá trị bảng hàng đợi một lần nữa.

### 00:11:08.839 - 00:11:13.720
Vì vậy, giá trị ban đầu là âm 0,866.

### 00:11:13.720 - 00:11:17.399
Và sau khi cập nhật.

### 00:11:17.959 - 00:11:20.360
Chúng ta có giá trị cao hơn ở đây vì phần thưởng là dương.

### 00:11:20.919 - 00:11:23.240
Vì vậy, bây giờ nó ít âm hơn trừ 0,68.

### 00:11:23.240 - 00:11:24.839
Và sau đó chúng ta tăng tổng số phần thưởng.

### 00:11:25.399 - 00:11:28.120
Và trạng thái ghi đè.

### 00:11:30.199 - 00:11:31.399
Vì vậy, chúng tôi thiết lập trạng thái tiếp theo.

### 00:11:31.399 - 00:11:34.199
Là trạng thái cho lần chạy tiếp theo.

### 00:11:34.840 - 00:11:38.520
Vì vậy, đây là cách nó hoạt động.

### 00:11:38.520 - 00:11:41.320
Vì vậy, đó là động lực chung đằng sau.

