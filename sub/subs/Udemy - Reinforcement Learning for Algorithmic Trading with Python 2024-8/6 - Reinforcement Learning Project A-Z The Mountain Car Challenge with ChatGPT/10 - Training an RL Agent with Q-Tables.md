## Nội dung

### 00:00:00.000 - 00:00:05.000
Được rồi, hãy tiếp tục đào tạo một tác nhân học tập có khả năng đọc và được tạo nhanh.

### 00:00:05.000 - 00:00:12.200
Và đây chắc chắn là thời điểm tốt để bắt đầu một cuộc trò chuyện rõ ràng mới và chỉ cung cấp

### 00:00:12.200 - 00:00:14.839
mã mà chúng tôi đã phát triển cho đến nay.

### 00:00:14.839 - 00:00:21.160
Vì vậy, chúng ta có thể bắt đầu ở đây với lời nhắc sau, bất kể bạn sử dụng GPT4 hay GPT 3.5.

### 00:00:21.160 - 00:00:27.839
Tôi đã tạo mã sau để chạy nhiều tập ngẫu nhiên của thử thách thẻ núi.

### 00:00:27.839 - 00:00:31.120
Vì vậy, đây là mã hiện tại của chúng tôi.

### 00:00:31.120 - 00:00:33.840
Và sau đó chúng ta có thể tiếp tục với lời nhắc sau.

### 00:00:33.840 - 00:00:40.079
Vì vậy, bây giờ tôi muốn tạo và huấn luyện một tác nhân học tăng cường có thể tiếp cận mục tiêu với

### 00:00:40.079 - 00:00:46.640
 càng ít bước càng tốt và với tỷ lệ thành công cao, vui lòng xây dựng dựa trên mã hiện có và

### 00:00:46.640 - 00:00:49.760
đào tạo tác nhân.

### 00:00:49.760 - 00:00:52.519
Vì vậy, hãy xem những gì chúng ta nhận được ở đây.

### 00:00:52.520 - 00:01:04.439
Và đây là một lời nhắc khá mở, nhưng tôi đoán GPT sẽ chọn phương thức bảng hàng đợi.

### 00:01:04.439 - 00:01:06.920
Vì vậy, hãy đợi ở đây để có phản hồi đầy đủ.

### 00:01:06.920 - 00:01:12.159
Bây giờ chúng ta hãy kiểm tra phản hồi đầy đủ để tạo và đào tạo một tác nhân học tập được thực hiện nhanh, đọc

### 00:01:12.159 - 00:01:18.400
 cho thử thách thẻ núi, chúng tôi sẽ sử dụng phương pháp học theo hàng đợi với cái gọi là

### 00:01:18.400 - 00:01:23.920
bảng hàng đợi và chúng ta sẽ kiểm tra bảng hàng đợi chi tiết hơn sau.

### 00:01:23.920 - 00:01:29.760
Vì vậy, học hàng đợi là một phương pháp RL dựa trên giá trị nhằm tìm hiểu giá trị của các cặp trạng thái

### 00:01:29.760 - 00:01:31.200
hành động.

### 00:01:31.200 - 00:01:37.480
Vậy đối với một trạng thái nhất định, hành động tốt nhất mang lại phần thưởng cao nhất và các giá trị hàng đợi

### 00:01:37.480 - 00:01:43.980
 đã học được sau đó được sử dụng để chọn hành động tốt nhất để thực hiện trong mỗi trạng thái và

### 00:01:43.980 - 00:01:48.500
GPT được xây dựng ở đây trên mã hiện có.

### 00:01:48.500 - 00:01:56.340
Và ví dụ: chúng ta có thể chạy 2.000 tập mỗi bước có 1.200 bước nên hơi quá nhiều

### 00:01:56.340 - 00:01:58.939
vì vậy chúng ta nên giảm mức này.

### 00:01:58.939 - 00:02:03.700
Sau đó, chúng ta tạo môi trường mà không kết xuất và sau đó chúng ta có một số thông số học hàng đợi

### 00:02:03.700 - 00:02:10.420
như alpha là tốc độ học, sau đó là gamma hệ số chiết khấu và epsilon

### 00:02:10.500 - 00:02:16.139
tỷ lệ thăm dò cũng như phân rã epsilon và epsilon tối thiểu.

### 00:02:16.139 - 00:02:19.579
Vì vậy, chúng ta sẽ đánh dấu các chi tiết ở đây sau.

### 00:02:19.579 - 00:02:26.099
Và do không gian trạng thái là liên tục nên vị trí trên trục x là liên tục

### 00:02:26.099 - 00:02:28.699
và cả vận tốc.

### 00:02:28.699 - 00:02:37.219
Và để sử dụng việc học hàng đợi ở đây, chúng ta cần rời rạc hóa thành các thùng cho bảng hàng đợi và ví dụ

### 00:02:37.300 - 00:02:46.819
chúng ta có thể chia vị trí của chiếc xe để giá trị x thành 18 thùng và vận tốc

### 00:02:46.819 - 00:02:49.060
thành 14 thùng.

### 00:02:49.060 - 00:02:51.939
Vì vậy, đây là điểm bắt đầu.

### 00:02:51.939 - 00:02:56.819
Vì vậy, chúng ta có số lượng thùng ở đây và sau đó nó tạo ra không gian quan sát.

### 00:02:56.819 - 00:03:04.939
Vì vậy, ở đây chúng ta có tham số vị trí trên trục x, chúng ta có các giá trị trong khoảng âm

### 00:03:04.939 - 00:03:13.340
1,2 và 0,6 và không gian np.lin này nó thực sự tạo ra loại đường viền thùng.

### 00:03:13.340 - 00:03:21.139
Vì vậy, chúng ta có 18 ngăn có chiều rộng bằng nhau trong khoảng từ âm 1,2 đến 0,6 và đối với vận tốc nên vận tốc

### 00:03:21.139 - 00:03:30.979
có thể nhận các giá trị trong khoảng từ âm 0,07 đến cộng 0,07 và điều này chúng ta cũng có thể chia thành 14 thùng.

### 00:03:30.979 - 00:03:37.299
Đây là không gian quan sát và cơ sở trên các thùng này, chúng ta thực sự có thể tạo bảng hàng đợi

### 00:03:37.299 - 00:03:42.500
với các giá trị ngẫu nhiên trong khoảng từ âm 1 đến 1.

### 00:03:42.500 - 00:03:49.099
Vì vậy, chúng ta bắt đầu với một bảng xếp hàng ngẫu nhiên và sau đó chúng ta cập nhật các giá trị trong quá trình đào tạo quá trình

### 00:03:49.099 - 00:03:52.579
vì vậy chúng ta sẽ đi vào chi tiết ở đây sau.

### 00:03:52.579 - 00:03:54.060
Và thế là xong.

### 00:03:54.060 - 00:04:02.460
Chúng ta cũng tạo một trạng thái rời rạc của hàm do người dùng xác định để khi chúng ta có một trạng thái là sự kết hợp

### 00:04:02.460 - 00:04:09.099
 của vị trí và vận tốc nên khi chúng ta có một trạng thái thì hàm này sẽ biến nó thành

### 00:04:09.099 - 00:04:12.020
các thùng.

### 00:04:12.020 - 00:04:18.899
Vì vậy, đây thực sự là phần chính, phần chính mới và chúng tôi sẽ kiểm tra phần này chi tiết hơn

### 00:04:18.899 - 00:04:23.819
sau này và sau đó chúng tôi khởi tạo ở đây ma trận hiệu suất hoặc tổng phần thưởng

### 00:04:23.819 - 00:04:30.060
và số lần thành công sau đó chúng tôi lặp lại số tập để chúng tôi chạy tất cả các tập

### 00:04:30.060 - 00:04:39.740
và mỗi lần chúng tôi thực sự đặt lại trạng thái và rời rạc hóa trạng thái ban đầu thì chúng tôi

### 00:04:39.740 - 00:04:47.339
đặt tổng phần thưởng thành 0 và thực hiện và cắt bớt một giá trị sai và sau đó chúng tôi thực hiện hành động sao cho các bước tối đa

### 00:04:47.339 - 00:04:56.699
tối đa và sau đó chúng tôi tạo một số ngẫu nhiên trong khoảng từ 0 đến 1 và nếu số này nhỏ hơn epsilon

### 00:04:56.699 - 00:05:05.099
 ban đầu là 0,1 vì vậy nếu số này nhỏ hơn 0,1 thì chúng tôi thực hiện một hành động ngẫu nhiên và ngược lại

### 00:05:05.099 - 00:05:12.579
nếu các số ngẫu nhiên lớn hơn epsilon thì chúng tôi thực sự thực hiện hành động tối ưu dựa trên bảng xếp hàng

### 00:05:12.579 - 00:05:20.659
 nên đây được gọi là lựa chọn hành động tham lam epsilon nên ở đây chúng tôi cũng sẽ

### 00:05:20.659 - 00:05:27.219
tìm hiểu chi tiết hơn và sau đó chúng tôi thực hiện một hành động như một hành động ngẫu nhiên hoặc hành động tốt nhất

### 00:05:27.219 - 00:05:33.299
hành động có thể xảy ra cho trạng thái nhất định và sau đó chúng tôi quan sát kết quả của hành động để tiếp theo

### 00:05:33.300 - 00:05:42.900
 nêu phần thưởng được thực hiện và cắt bớt, sau đó chúng tôi cũng rời rạc hóa trạng thái tiếp theo và sau đó cập nhật

### 00:05:42.900 - 00:05:52.980
 giá trị hàng đợi với một công thức khá phức tạp và sau đó chúng tôi cập nhật tổng phần thưởng và kiểm tra trạng thái

### 00:05:53.620 - 00:06:04.180
 rằng tập đã hoàn thành hoặc bị cắt bớt và sau đó chúng tôi cũng cập nhật epsilon với phân rã epsilon

### 00:06:04.180 - 00:06:16.740
con số là 99,5% mỗi bước thì ở cuối tập, chúng tôi đính kèm tổng phần thưởng vào tổng số

### 00:06:17.699 - 00:06:26.500
 phần thưởng và số lượng thành công tăng dần nếu đây là một thành công thì chúng tôi in mỗi tập thứ 100

### 00:06:28.500 - 00:06:33.620
gần với môi trường và sau đó chúng tôi tính toán số liệu hiệu suất của quá trình đào tạo

### 00:06:34.819 - 00:06:39.699
và bạn cũng sẽ tìm thấy ở đây một lời giải thích ngắn gọn để các tham số học tập xếp hàng chúng tôi khởi tạo hệ số chiết khấu tốc độ học tập và tỷ lệ khám phá sau đó chúng tôi có sự phân tách trạng thái nên không gian trạng thái

### 00:06:39.699 - 00:06:45.939
 là liên tục và đó là tại sao chúng ta cần phân tách nó thành các chân để lập chỉ mục bảng hàng đợi dễ dàng hơn

### 00:06:45.939 - 00:06:53.139
sau đó chúng ta khởi tạo một bảng hàng đợi ngẫu nhiên với các giá trị ngẫu nhiên cho mỗi cặp hành động trạng thái

### 00:06:53.779 - 00:06:59.620
và sau đó đánh số cho lựa chọn hành động tham lam của epsilon để các hành động được chọn bằng cách sử dụng chiến lược tham lam

### 00:07:00.259 - 00:07:05.860
epsilon để cân bằng việc khám phá và khai thác, sau đó dựa trên hành động đó

### 00:07:05.860 - 00:07:12.579
chúng tôi cập nhật các giá trị hàng đợi và sau đó chúng tôi đo lường hiệu suất để mã này sẽ huấn luyện một tác nhân học hàng đợi

### 00:07:12.659 - 00:07:20.099
để giải quyết vấn đề xe leo núi và chúng ta chỉ cần sao chép code

### 00:07:20.099 - 00:07:25.539
và hãy dán nó vào sổ ghi chép và chạy mã và kiểm tra những gì chúng ta nhận được ở đây

### 00:07:28.819 - 00:07:35.620
vì vậy có lẽ chúng ta nên giảm số bước tối đa trong một tập chẳng hạn xuống còn 500 và tổng cộng chúng ta

### 00:07:36.259 - 00:07:45.780
có 2.000 tập nên ở đây chúng ta có tập 100 200 300 và ở đây chúng ta có thể thấy tổng phần thưởng

### 00:07:45.780 - 00:07:55.060
vì vậy nó đang giảm dần nên chúng ta có thể và nên xem đây là một buổi đào tạo thành công

### 00:07:55.699 - 00:08:00.980
vì vậy đây là các chỉ số hiệu suất nên tổng phần thưởng trung bình là 250 và tập tệ nhất chỉ là

### 00:08:01.060 - 00:08:10.740
thất bại nhưng chúng tôi cũng có tập hay nhất thành công chỉ sau 96 bước và thực sự chúng tôi có ở đây

### 00:08:10.740 - 00:08:21.939
tỷ lệ thành công là 88,15%, khá cao nên trong số 2.000 tập chúng tôi có thể đạt được

### 00:08:21.939 - 00:08:32.100
đỉnh núi trong 1763 trường hợp và đây là quá trình đào tạo của đặc vụ

### 00:08:32.100 - 00:08:41.779
và rõ ràng là điều này đã thành công và chúng ta sẽ khám phá thêm và cũng cải thiện mã trong các bài giảng tiếp theo

### 00:08:42.500 - 00:08:49.539
cảm ơn vì đã xem và hẹn gặp lại ở đó, tạm biệt

### 00:08:49.539 - 00:08:53.860
next lectures thanks for watching and see you there bye

