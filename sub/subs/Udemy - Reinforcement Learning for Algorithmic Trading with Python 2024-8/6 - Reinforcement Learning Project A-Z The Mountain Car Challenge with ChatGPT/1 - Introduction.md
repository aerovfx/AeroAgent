## Nội dung

### 00:00:00.000 - 00:00:07.440
Xin chào và chào mừng bạn đến với dự án học tăng cường đầu tiên của chúng tôi, Thử thách Mountain Card.

### 00:00:07.440 - 00:00:12.120
Vậy Thử thách Mountain Card là một vấn đề kinh điển trong lĩnh vực tăng cường

### 00:00:12.120 - 00:00:20.080
học tập tập trung vào việc dạy các tác nhân đưa ra quyết định bằng cách tương tác với một môi trường.

### 00:00:20.080 - 00:00:26.080
Và chúng tôi có mặt ở đây trên trang web Gymnasium của OpenAI.

### 00:00:26.079 - 00:00:32.039
Vì vậy, Gymnasium là một API nổi bật cho việc học tăng cường với một bộ sưu tập môi trường tham khảo đa dạng

### 00:00:32.039 - 00:00:35.399
có thể nói là giới thiệu.

### 00:00:35.399 - 00:00:44.879
Và chúng ta có thể đi tới đây điều khiển cổ điển của môi trường và Mountain Card.

### 00:00:44.879 - 00:00:51.759
Và trong bài toán này, đặc vụ điều khiển một chiếc ô tô được đặt ở vị trí giữa hai ngọn đồi.

### 00:00:51.759 - 00:00:54.039
Vì vậy, ngọn đồi bên trái và ngọn đồi bên phải.

### 00:00:54.039 - 00:01:01.399
Và mục tiêu là lái xe lên ngọn đồi bên phải để đạt được mục tiêu trên đỉnh núi.

### 00:01:01.399 - 00:01:06.959
Tuy nhiên, động cơ của ô tô không đủ mạnh để leo thẳng lên đồi.

### 00:01:06.959 - 00:01:13.239
Và thay vào đó, đặc vụ phải học cách tận dụng năng lượng tiềm năng bằng cách lùi lại bên trái

### 00:01:13.239 - 00:01:14.239
đồi.

### 00:01:14.239 - 00:01:18.079
Vì vậy, hãy lấy đà đi đến ngọn đồi bên trái.

### 00:01:18.079 - 00:01:25.280
Và sau đó dùng đà để leo lên ngọn núi bên phải.

### 00:01:25.280 - 00:01:30.759
Vì vậy, đặc vụ phải tăng tốc sang trái và cả sang phải, đúng thời điểm tùy thuộc

### 00:01:30.759 - 00:01:37.319
vào vị trí và vận tốc của nó.

### 00:01:37.319 - 00:01:43.879
Và mục tiêu là tăng tốc cho chiếc xe một cách có chiến lược để đạt được trạng thái mục tiêu trên đỉnh

### 00:01:43.879 - 00:01:45.879
ngọn đồi bên phải.

### 00:01:45.879 - 00:01:49.719
Vì vậy, chúng tôi đang làm việc ở đây với phiên bản hành động kín đáo.

### 00:01:49.719 - 00:01:51.560
Nó đơn giản hơn một chút.

### 00:01:51.560 - 00:01:55.399
Bây giờ môi trường của thử thách thẻ leo núi khá đơn giản.

### 00:01:55.399 - 00:02:01.799
Vì vậy, trong không gian quan sát mô tả môi trường, chúng tôi chỉ có hai các biến.

### 00:02:01.799 - 00:02:08.000
Vậy chúng ta có vị trí của ô tô dọc theo trục x ở đây.

### 00:02:08.000 - 00:02:13.319
Và nó có thể nhận các giá trị trong khoảng âm 1,2 ở phía bên trái.

### 00:02:13.319 - 00:02:16.439
Và cộng 0,6 ở phía bên phải.

### 00:02:16.439 - 00:02:19.680
Và tôi nghĩ mục tiêu là 0,5.

### 00:02:19.680 - 00:02:23.519
Và sau đó số 2 chúng ta có vận tốc của ô tô.

### 00:02:23.519 - 00:02:31.240
Vậy từ âm 0,07 nên lái xe sang trái đến cộng 0,07 đi về phía đúng.

### 00:02:31.240 - 00:02:38.079
Vậy đây là không gian quan sát có thể được mô tả đầy đủ bằng hai biến ở đây.

### 00:02:38.079 - 00:02:40.280
Vị trí và vận tốc.

### 00:02:40.280 - 00:02:43.079
Và sau đó chúng ta có không gian hành động.

### 00:02:43.080 - 00:02:46.280
Vì vậy, tác nhân có thể thực hiện ba hành động khác nhau.

### 00:02:46.280 - 00:02:48.920
Vì vậy, nó có thể tăng tốc sang trái.

### 00:02:48.920 - 00:02:50.080
Nó không thể làm gì cả.

### 00:02:50.080 - 00:02:54.520
Vì vậy, không tăng tốc và nó có thể tăng tốc sang bên phải.

### 00:02:54.520 - 00:02:56.600
Và đây là một số động lực chuyển tiếp.

### 00:02:56.600 - 00:03:03.640
Vì vậy, điều này tuân theo vật lý tiêu chuẩn.

### 00:03:03.640 - 00:03:09.560
Vì vậy, một vấn đề học tăng cường điển hình bao gồm môi trường hoặc không gian quan sát

### 00:03:09.560 - 00:03:12.520
 hơn là không gian hành động.

### 00:03:12.520 - 00:03:16.120
Và thứ ba chúng ta có phần thưởng.

### 00:03:16.120 - 00:03:21.319
Vì vậy, đối với mỗi hành động của đại lý, chúng tôi nhận được phần thưởng.

### 00:03:21.319 - 00:03:27.759
Và mục tiêu là đạt được lá cờ đặt trên đỉnh ngọn đồi bên phải càng nhanh càng tốt.

### 00:03:27.759 - 00:03:33.759
Và như vậy, đại lý sẽ bị phạt trừ 1 cho mỗi bước thời gian.

### 00:03:33.759 - 00:03:42.759
Vì vậy, phần thưởng chỉ là 0 nếu đại lý đạt được mục tiêu cho đến bước này.

### 00:03:42.759 - 00:03:46.599
Và chúng ta cũng có trạng thái bắt đầu khá ngẫu nhiên.

### 00:03:46.599 - 00:03:52.759
Vì vậy, vị trí của ô tô được gán một giá trị ngẫu nhiên thống nhất trong khoảng âm 0,6 đến âm

### 00:03:52.759 - 00:03:56.799
0,4 với vận tốc bằng 0.

### 00:03:56.800 - 00:04:03.040
Thực tế có hai lý do có thể khiến một tập phim có thể kết thúc.

### 00:04:03.040 - 00:04:06.000
Vậy chấm dứt số một.

### 00:04:06.000 - 00:04:12.920
Vậy nếu vị trí của ô tô lớn hơn hoặc bằng 0,5 thì đó là mục tiêu hoặc giây

### 00:04:12.920 - 00:04:16.720
nếu độ dài của tập phim là 200.

### 00:04:16.720 - 00:04:23.439
Vậy nếu chúng tôi đã thử 200 hành động và nếu không đạt được mục tiêu thì tập phim sẽ bị

### 00:04:23.439 - 00:04:24.439
cắt ngắn.

### 00:04:24.439 - 00:04:29.600
Vì vậy, hãy chấm dứt hoặc cắt ngắn.

### 00:04:29.600 - 00:04:35.839
Và đó thực ra cũng là thử thách xe leo núi khá đơn giản và dễ hiểu.

### 00:04:35.839 - 00:04:40.120
Và do đó, chiếc xe leo núi thách thức màn trình diễn hoàn hảo để làm quen với ba

### 00:04:40.120 - 00:04:42.000
học tập thực thi.

### 00:04:42.000 - 00:04:45.199
Vì vậy, vì chúng tôi có động lực học đơn giản.

### 00:04:45.199 - 00:04:50.000
Vì vậy, động lực của thử thách xe leo núi là thẳng thắn và dễ hiểu.

### 00:04:50.000 - 00:04:54.759
Và trạng thái của môi trường chỉ được mô tả bằng hai biến số.

### 00:04:54.759 - 00:04:59.480
Và chúng tôi cũng có mục tiêu rõ ràng nên mục tiêu lên tới đỉnh núi

### 00:04:59.480 - 00:05:02.920
 là rõ ràng và có thể định lượng được.

### 00:05:02.920 - 00:05:07.920
Và số ba, thử thách xe leo núi tự nhiên đưa ra một số khái niệm chính về

### 00:05:07.920 - 00:05:09.759
học tăng cường.

### 00:05:09.759 - 00:05:11.800
Vì vậy, chúng ta sẽ thấy điều này sau.

### 00:05:11.800 - 00:05:16.480
Vì vậy, ví dụ như khái niệm khám phá và khai thác.

### 00:05:16.480 - 00:05:23.640
Vì vậy, để giải quyết vấn đề, đặc vụ phải khám phá bằng cách thử các hành động ngẫu nhiên khác nhau để tìm

### 00:05:23.640 - 00:05:30.640
cái gì hoạt động và sau đó khai thác bằng cách sử dụng các hành động đã biết để hoạt động và cân bằng hai chiến lược này

### 00:05:30.640 - 00:05:34.400
là một khái niệm ô tô và học tăng cường.

### 00:05:34.400 - 00:05:37.800
Và thách thức này cũng bao gồm các phần thưởng thưa thớt.

### 00:05:37.800 - 00:05:44.040
Vì vậy, phần thưởng không được trao ở mọi bước mà chỉ khi đạt được mục tiêu.

### 00:05:44.040 - 00:05:49.760
Và do đó, vấn đề được thiết lập là hoàn hảo để thể hiện các thuật toán như Q learning.

### 00:05:49.760 - 00:05:55.879
Vì vậy, đây là nền tảng để hiểu cách các tác nhân học hỏi từ môi trường một cách linh hoạt.

### 00:05:55.879 - 00:06:02.600
Vì vậy, mục tiêu của dự án này là bạn hiểu được lý do căn bản đằng sau việc học Q.

### 00:06:02.600 - 00:06:05.720
Và những gì chúng ta có thể thấy ở đây là một tác nhân ngẫu nhiên.

### 00:06:05.720 - 00:06:09.920
Vì vậy, anh ta cố gắng tăng tốc ngẫu nhiên sang trái và phải.

### 00:06:09.920 - 00:06:13.320
Và khá khó để lên tới đỉnh núi.

### 00:06:13.319 - 00:06:21.920
Và cuối cùng hãy để tôi cho bạn xem một đặc vụ đã được đào tạo có thể dễ dàng tiếp cận mục tiêu.

### 00:06:21.920 - 00:06:23.319
Vậy hãy kiểm tra điều này ở đây.

### 00:06:23.319 - 00:06:29.920
Đây là một đặc vụ đã được đào tạo và chúng ta có thể thấy ở đây một số tập phim thành công.

### 00:06:29.920 - 00:06:35.039
Vậy là chiếc xe đã lên đến đỉnh núi nhanh chóng.

### 00:06:35.039 - 00:06:39.159
Và điều này là mục tiêu cuối cùng của dự án này.

### 00:06:39.160 - 00:06:44.920
Vì vậy, cuối cùng hãy đào tạo đại lý để có một đại lý rất có năng lực.

### 00:06:44.920 - 00:06:49.080
Cảm ơn các bạn đã theo dõi và hẹn gặp lại các bạn trong các bài giảng tiếp theo. Tạm biệt.

