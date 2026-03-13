## Nội dung

### 00:00:00.000 - 00:00:03.520
Bây giờ, hãy chuyển sang một chủ đề rất quan trọng,

### 00:00:03.520 - 00:00:07.640
sự rời rạc của các tính năng liên tục.

### 00:00:07.640 - 00:00:12.240
Nhưng trước khi để tôi chỉ cho bạn một điều nhỏ mà tôi đã thay đổi trong

### 00:00:12.240 - 00:00:17.719
bài giảng trước, vì vậy khi tạo train.df và test.df from.df,

### 00:00:17.719 - 00:00:20.960
chúng ta nên đảm bảo rằng đó là một bản sao thực.

### 00:00:20.960 - 00:00:26.640
Vì vậy, một đối tượng độc lập không trỏ đến khung dữ liệu gốc.

### 00:00:26.879 - 00:00:35.560
Và do đó, ở đây chúng tôi sử dụng phương pháp sao chép để tránh các vấn đề như cài đặt với một bản sao cảnh báo.

### 00:00:35.560 - 00:00:42.200
Vì vậy, tôi chỉ chỉnh sửa ở đây phương pháp sao chép để đảm bảo an toàn.

### 00:00:42.200 - 00:00:46.480
Và bây giờ chúng ta hãy tiếp tục ở đây với khung dữ liệu huấn luyện.

### 00:00:46.480 - 00:00:52.439
Và hãy nhớ rằng đối với học Q, chúng ta cần rời rạc hóa các tính năng liên tục.

### 00:00:52.439 - 00:00:55.320
Và chúng ta có ở đây nhiều tính năng liên tục.

### 00:00:55.320 - 00:01:00.879
Vậy tỷ lệ SMA, biểu đồ MACD, chỉ số sức mạnh tương đối,

### 00:01:00.879 - 00:01:04.799
và cả chỉ báo dao động châm biếm và lợi nhuận.

### 00:01:04.799 - 00:01:08.479
Vì vậy, tất cả đều liên tục tính năng.

### 00:01:08.479 - 00:01:12.599
Và nếu bạn muốn làm việc với bảng Q và bảng Q,

### 00:01:12.599 - 00:01:15.799
chúng ta cần rời rạc hóa các tính năng này.

### 00:01:15.799 - 00:01:21.200
Và chúng ta đã thấy rằng có sự cân bằng rõ ràng giữa mức độ chi tiết và

### 00:01:21.200 - 00:01:23.359
các yêu cầu tính toán.

### 00:01:23.359 - 00:01:31.799
Vì vậy, để thực sự cải thiện và tối ưu hóa tác nhân, chúng ta nên tăng số lượng thùng.

### 00:01:31.799 - 00:01:36.200
Nhưng điều này sẽ làm tăng các yêu cầu tính toán.

### 00:01:36.200 - 00:01:42.719
Và do đó chúng ta nên chọn số lượng thùng thích hợp cho các tính năng liên tục

### 00:01:42.719 - 00:01:48.760
để tác nhân học tăng cường có thể học một cách hiệu quả.

### 00:01:48.760 - 00:01:52.960
Nhưng chúng ta cũng biết rằng Q bảng chứa tất cả các cặp hành động trạng thái.

### 00:01:52.960 - 00:01:55.520
Và nó không được quá lớn.

### 00:01:55.520 - 00:01:59.080
Vì vậy, hãy tiếp tục ở đây với không gian quan sát của chúng ta.

### 00:01:59.080 - 00:02:01.960
Và tổng cộng chúng ta có năm tính năng.

### 00:02:01.960 - 00:02:05.920
Và thực tế, ở đây chúng ta có một tính năng bổ sung trong không gian quan sát.

### 00:02:05.920 - 00:02:09.920
Vì vậy, chúng ta cũng nên sử dụng vị thế giao dịch hiện tại ở đây.

### 00:02:09.920 - 00:02:14.040
Vì vậy, ngắn gọn và trung tính, có ba lựa chọn.

### 00:02:14.040 - 00:02:18.240
Và bất cứ khi nào tác nhân học tăng cường đang cân nhắc thực hiện một hành động,

### 00:02:18.240 - 00:02:22.960
nó cũng phải tính đến vị thế giao dịch hiện tại.

### 00:02:22.960 - 00:02:24.960
Vì vậy, điều đó khá quan trọng.

### 00:02:24.960 - 00:02:32.640
Vì vậy, có thể hiệu quả hơn cho đại lý nếu vị thế mua đã có

### 00:02:32.640 - 00:02:33.640
mua.

### 00:02:33.640 - 00:02:40.040
Vì vậy, nếu vị thế giao dịch hiện tại là bán và nếu có tín hiệu yếu để mua, thì

### 00:02:40.040 - 00:02:46.920
 chuyển từ bán sang mua và thanh toán chi phí giao dịch có thể không phải là ý tưởng hay nhất.

### 00:02:46.919 - 00:02:51.519
Nhưng chúng ta sẽ đi sâu hơn vào chi tiết về chi phí giao dịch và nhiều thông tin khác trong phần tiếp theo bài giảng.

### 00:02:51.519 - 00:02:55.599
Nhưng hiện tại, hãy kiểm tra không gian quan sát ở đây.

### 00:02:55.599 - 00:03:00.519
Vậy là chúng ta có một vài tính năng liên tục.

### 00:03:00.519 - 00:03:05.279
Và câu hỏi đặt ra là chúng ta sử dụng bao nhiêu thùng ở đây?

### 00:03:05.279 - 00:03:06.679
Và hãy bắt đầu từ đây.

### 00:03:06.679 - 00:03:09.399
Ví dụ: có 11 thùng.

### 00:03:09.399 - 00:03:15.879
Vì vậy, thông thường chúng ta nên sử dụng số lượng thùng lẻ không đồng đều vì các tính năng đó thường

### 00:03:15.879 - 00:03:21.960
dao động xung quanh một giá trị nhất định như 0 hoặc 1.

### 00:03:21.960 - 00:03:26.439
Và các giá trị này quanh 0 hoặc 1 nên ở thùng giữa.

### 00:03:26.439 - 00:03:29.039
Vì vậy, nên có một loại ở giữa.

### 00:03:29.039 - 00:03:34.560
Và do đó, hãy lấy một số lượng không đều các thùng như 11.

### 00:03:34.560 - 00:03:38.960
Và sau đó chúng ta có thể tính số trạng thái khác nhau.

### 00:03:38.960 - 00:03:42.000
Vậy chúng ta có 11 lũy thừa 5.

### 00:03:42.000 - 00:03:45.400
Vậy là chúng ta có 5 tính năng liên tục.

### 00:03:45.400 - 00:03:49.400
Và cuối cùng là tính năng vị trí giao dịch hiện tại.

### 00:03:49.400 - 00:03:55.120
Và điều này cho chúng ta gần 500 đến 1000 trạng thái khác nhau.

### 00:03:55.120 - 00:04:00.479
Và trong chiến lược giao dịch đơn giản nhất, chúng ta thực sự có ba hành động có thể xảy ra.

### 00:04:00.479 - 00:04:06.560
Vì vậy, đi hoặc ở ngắn, trung lập và dài hạn.

### 00:04:06.560 - 00:04:14.000
Và do đó chúng ta có thể nhân số trạng thái với 3 để có được các cặp hành động trạng thái.

### 00:04:14.000 - 00:04:21.120
Vậy bây giờ là ví dụ, gần 1,5 triệu, khá lớn nhưng vẫn có thể tiêu hóa được.

### 00:04:21.120 - 00:04:28.560
Hãy nhớ lại rằng trong thử thách Luna Lander, chúng ta có 81 triệu cặp hành động trạng thái.

### 00:04:28.560 - 00:04:32.199
Vì vậy, 1,5 triệu sẽ hoàn toàn ổn.

### 00:04:32.199 - 00:04:35.360
Và ít nhất đây có thể là một điểm khởi đầu tốt.

### 00:04:35.360 - 00:04:37.800
Và sau này chúng tôi có thể phát triển hơn nữa.

### 00:04:37.800 - 00:04:46.279
Vì vậy, ví dụ: nếu bạn sử dụng 21 thùng, thì chúng ta sẽ có 36 triệu cặp hành động trạng thái.

### 00:04:46.279 - 00:04:51.159
Vì vậy, có một số chỗ để thực sự tăng số lượng thùng ở đây.

### 00:04:51.159 - 00:04:55.000
Nhưng hãy bắt đầu với 11 thùng cho các tính năng liên tục.

### 00:04:55.000 - 00:04:56.599
Và hãy xem một ví dụ ở đây.

### 00:04:56.600 - 00:05:02.120
Vì vậy, chúng ta có ở đây trong khung dữ liệu huấn luyện, tính năng trả về.

### 00:05:02.120 - 00:05:08.040
Và các giá trị thường xuyên nhất là khoảng 0, nhưng chúng là các giá trị ngoại lệ ở bên trái và 

### 00:05:08.040 - 00:05:09.040
đúng.

### 00:05:09.040 - 00:05:18.080
Và bây giờ nếu chúng ta rời rạc hóa hoặc nếu bạn gộp ở đây, tính năng trả về thành 11 thùng, thì chúng ta

### 00:05:18.080 - 00:05:22.080
thực sự có thể thực hiện điều này với PD.q cut.

### 00:05:22.079 - 00:05:27.479
Và chúng ta có thể đảm bảo rằng chúng ta sử dụng cách tạo nhóm lượng tử ở đây.

### 00:05:27.479 - 00:05:33.560
Vì vậy, điều này đảm bảo rằng chúng ta có cùng số lượng quan sát và tất cả các thùng.

### 00:05:33.560 - 00:05:40.799
Vì vậy, các cạnh thùng được tạo theo cách mà chúng ta có kích thước tương tự hoặc giống hệt nhau trong tất cả

### 00:05:40.799 - 00:05:41.799
thùng.

### 00:05:41.799 - 00:05:48.759
Vì vậy, chúng ta chuyển tính năng trả về và sau đó chúng tôi xác định số lượng thùng.

### 00:05:48.759 - 00:05:57.079
Và thực tế, chúng tôi cũng muốn trả về các cạnh của thùng ở đây bằng cách đặt các thùng trả về thành đúng.

### 00:05:57.079 - 00:06:00.959
Và sau đó PD.q cut trả về tính năng bin.

### 00:06:00.959 - 00:06:04.519
Và chúng ta tạo ở đây một cột mới trả về bin.

### 00:06:04.519 - 00:06:08.159
Và chúng ta cũng có được các cạnh của thùng.

### 00:06:08.159 - 00:06:10.279
Vì vậy, hãy chạy đơn giản ở đây.

### 00:06:10.279 - 00:06:13.680
Và ở đây bên phải, chúng ta hiện có cột bổ sung trả về bin.

### 00:06:13.680 - 00:06:23.079
Vì vậy, ví dụ: lợi nhuận dương của điểm 0 là 1% nằm trong thùng số 10.

### 00:06:23.079 - 00:06:27.879
Vì vậy, đây là thùng cuối cùng có lợi nhuận dương cao nhất.

### 00:06:27.879 - 00:06:33.079
Và tương tự, chúng ta cũng có số thùng bằng 0.

### 00:06:33.079 - 00:06:35.920
 với giá trị thấp nhất.

### 00:06:35.920 - 00:06:38.720
Vì vậy, giá trị trả về âm nhất.

### 00:06:39.720 - 00:06:45.040
Và đâu đó ở giữa phải là thùng số 5.

### 00:06:45.040 - 00:06:49.200
Và trên thực tế, chúng ta cũng có thể kiểm tra số lượng quan sát và mỗi thùng.

### 00:06:49.200 - 00:06:55.960
Vì vậy, kích thước phải bằng hoặc giống hệt nhau.

### 00:06:55.960 - 00:07:04.360
Và chúng ta có thể thấy rằng chúng ta có khoảng 909, 9010 quan sát và mỗi thùng.

### 00:07:04.360 - 00:07:05.360
Vì vậy, đây là cách phân chia lượng tử, đảm bảo rằng chúng ta có cùng số lượng quan sát và

### 00:07:05.360 - 00:07:08.520
tất cả các thùng.

### 00:07:08.520 - 00:07:18.120
Và cuối cùng nhưng không kém phần quan trọng, chúng ta có thể kiểm tra các cạnh của thùng.

### 00:07:18.120 - 00:07:21.960
Vì vậy, lợi nhuận âm nhất là âm 1,3% và thùng đầu tiên là từ âm 1,3 đến âm

### 00:07:21.960 - 00:07:31.000
0,1%, v.v.

### 00:07:31.000 - 00:07:34.480
Và thùng cuối cùng là từ cộng 0,1% đến 1,7%.

### 00:07:34.480 - 00:07:40.240
Vì vậy, đây là cách hoạt động của việc tạo nhóm lượng tử cho một tính năng.

### 00:07:40.240 - 00:07:45.079
Và bạn có thể nhận thấy rằng chúng ta đã phân loại dựa trên tập huấn luyện.

### 00:07:45.079 - 00:07:50.519
Và bây giờ chúng ta nên sử dụng trên thực tế, các cạnh thùng cũng giống nhau đối với bộ thử nghiệm.

### 00:07:50.519 - 00:07:52.800
Vì vậy, để tránh rò rỉ dữ liệu thực sự, chúng ta nên làm điều này theo cách này.

### 00:07:52.800 - 00:07:55.000
Và chúng ta sẽ tiếp tục ở đây trong bài giảng tiếp theo.

### 00:07:55.000 - 00:07:56.000
Cảm ơn bạn đã xem và hẹn gặp lại bạn ở đó.

