## Nội dung

### 00:00:00.000 - 00:00:06.400
Được rồi, hãy tiếp tục với nhiều tập và để thuận tiện, tôi đã lưu

### 00:00:06.400 - 00:00:14.080
tập huấn luyện và tập kiểm tra ở đây trong các tệp CSV mới, vì vậy hãy huấn luyện FCSV và kiểm tra

### 00:00:14.080 - 00:00:21.559
FCSV và tất nhiên bạn cũng có thể tìm thấy cả hai tệp trong thư mục tải xuống và chúng ta có thể bắt đầu

### 00:00:21.559 - 00:00:26.879
tại đây từ đầu nên chúng ta cần gấu trúc gọn gàng và cả metplotlib, sau đó để huấn luyện

### 00:00:26.879 - 00:00:34.560
tác nhân học tăng cường, chúng ta cần khung dữ liệu huấn luyện. Vì vậy, chúng ta ở đây với gần

### 00:00:34.560 - 00:00:40.799
10.000 hàng. Bây giờ câu hỏi quan trọng bây giờ là một tập là gì nếu chúng ta làm việc với nhiều tập

### 00:00:40.799 - 00:00:50.239
 và một tập phải là một tập hợp con ngẫu nhiên. Vì vậy, ví dụ: với 250 thanh hoặc 500 thanh

### 00:00:50.240 - 00:00:57.920
 hoặc có thể là 1000 thanh của tập huấn luyện đầy đủ và tác nhân sẽ được huấn luyện trong các điều kiện

### 00:00:57.920 - 00:01:05.840
 thay đổi và điều này dẫn đến các kỹ năng khái quát hóa tốt hơn nên việc chia tập dữ liệu

### 00:01:05.840 - 00:01:11.680
 thành các tập ngẫu nhiên nhỏ hơn là rất quan trọng vì điều quan trọng là phải huấn luyện tác nhân trong các điều kiện thay đổi

### 00:01:11.680 - 00:01:18.720
 và bằng cách đó, tác nhân sẽ khái quát hóa tốt hơn với dữ liệu mới và chưa thấy.

### 00:01:20.000 - 00:01:26.400
Bây giờ hãy để tôi cho bạn một ví dụ về cách chúng tôi có thể làm như vậy chọn các tập hợp con ngẫu nhiên nên trước hết chúng ta cần xác định

### 00:01:26.400 - 00:01:33.200
tổng số dấu thời gian trong tập huấn luyện của mình và sau đó, ví dụ: chúng ta có thể xác định kích thước

### 00:01:33.280 - 00:01:43.280
 của một tập là 250 để số thanh trong một tập hợp con và sau đó với np.random.rand int, chúng ta có thể

### 00:01:43.280 - 00:01:51.280
 thực sự xác định chỉ mục bắt đầu của tập nên ở đây, phía bên trái, chúng ta thực sự có

### 00:01:52.400 - 00:01:59.120
chỉ mục hàng vì vậy tôi đã bỏ ở đây chỉ mục ban ngày nên chúng tôi không cần ở đây ngày và giờ

### 00:02:00.079 - 00:02:09.200
cho khóa đào tạo nên bây giờ chúng tôi có chỉ số phạm vi từ 0 đến 9,998

### 00:02:11.439 - 00:02:19.280
 vì vậy việc chọn điểm bắt đầu của tập 250 bước ngẫu nhiên của chúng tôi là một quá trình ngẫu nhiên và ví dụ

### 00:02:19.280 - 00:02:28.560
chúng tôi bắt đầu ở đây với 2931 và có chỉ mục, chúng tôi thực sự có thể cắt khung dữ liệu xe lửa bằng trình truy cập

### 00:02:28.560 - 00:02:41.599
i-log và chọn tập 250 hàng bắt đầu từ chỉ mục 2931 nên đó là cách nó hoạt động và

### 00:02:41.599 - 00:02:47.120
bây giờ chúng ta hãy tiếp tục quá trình đào tạo và trước hết chúng ta phải xác định lại hai hàm

### 00:02:47.920 - 00:02:56.879
để chuyển đổi hàng thành trạng thái trên cùng và sau đó là hàm phần thưởng

### 00:02:59.039 - 00:03:06.400
và bây giờ chúng ta có ở đây mã đào tạo đầy đủ nên hãy xem từng bước một nhưng thực tế không có gì mới ở đây nên trước hết chúng ta tạo một danh sách trống tổng phần thưởng nơi chúng ta có thể tiết kiệm

### 00:03:06.400 - 00:03:12.800
tất cả phần thưởng nên tất cả phần thưởng cho mỗi phần thưởng và mỗi tập, sau đó chúng tôi tính thành công, ví dụ

### 00:03:12.800 - 00:03:20.400
một tập có lợi nhuận dương hoặc phần thưởng dương có thể được xác định là thành công thì chúng tôi cần đặt

### 00:03:20.400 - 00:03:28.000
các chỗ ngẫu nhiên để tái tạo và sau đó, chẳng hạn, chúng tôi có thể bắt đầu với độ dài tập là 250

### 00:03:28.159 - 00:03:37.199
 và trong tổng số 1.000 tập thì chúng tôi có các tham số học hàng đợi và ở đây chúng tôi cũng giới thiệu

### 00:03:37.840 - 00:03:45.680
phân rã epsilon nên chúng tôi bắt đầu với 1 hành động ngẫu nhiên 100% và sau đó chúng tôi giảm epsilon xuống time

### 00:03:45.680 - 00:03:55.199
 đến mức tối thiểu là 0,01 và mức phân rã epsilon là 99,9% thì chúng tôi khởi tạo các bảng hàng đợi hoặc ngẫu nhiên

### 00:03:55.679 - 00:04:05.919
bảng xếp hàng với định dạng sau nên chúng tôi đã rời rạc hóa tất cả các tính năng liên tục thành 11 thùng

### 00:04:05.919 - 00:04:15.599
, sau đó chúng tôi lặp lại các tập và với mỗi tập, chúng tôi chọn một tập ngẫu nhiên

### 00:04:16.480 - 00:04:24.480
và sau đó chúng tôi chọn dữ liệu ở đây và đặt vị trí ban đầu là trung lập, chúng tôi nhận được hàng của thanh đầu tiên

### 00:04:25.439 - 00:04:34.480
 và chúng tôi cũng xác định trạng thái của thanh đầu tiên rồi chúng tôi đặt tổng phần thưởng của tập này thành 0

### 00:04:34.480 - 00:04:41.520
và sau đó chúng tôi đi qua các thanh và trước tiên chúng tôi thực sự chọn một hành động với epsilon hành động tham lam

### 00:04:42.240 - 00:04:51.280
lựa chọn và sau đó đây không phải là điều gì mới ở đây

### 00:04:51.279 - 00:04:55.359
vì vậy chúng tôi thực hiện hành động và sau đó chúng tôi xác định vị thế giao dịch tiếp theo và thanh tiếp theo, đồng thời chúng tôi cũng

### 00:04:58.879 - 00:05:05.439
tính toán phần thưởng và trạng thái tiếp theo rồi cuối cùng chúng tôi cập nhật giá trị hàng đợi và sau đó ở cuối

### 00:05:05.439 - 00:05:13.279
 đó là một thành công thì chúng ta có phân rã epsilon ở đây và sau đó chúng ta cũng có thể in tổng

### 00:05:13.279 - 00:05:21.199
phần thưởng cho mỗi 100 tập và liệu nó có thành công hay không và cuối cùng chúng ta có ma trận hiệu suất

### 00:05:21.279 - 00:05:28.639
vì vậy, ví dụ như phần thưởng trung bình, tỷ lệ thành công này là tập hay nhất và tập tệ nhất

### 00:05:28.639 - 00:05:36.399
vì vậy hầu như không có gì mới ở đây và chỉ cần chạy ở đây 1000 tập

### 00:05:36.399 - 00:05:43.839
nên chúng ta có ở đây 100 200 300 và epsilon giảm dần theo thời gian

### 00:05:43.839 - 00:05:50.159
và sau 1000 tập, chúng tôi có tỷ lệ thành công là 83%

### 00:05:51.360 - 00:05:58.000
 và tổng phần thưởng trung bình là 23, phần thưởng tối thiểu là 45 và phần thưởng tối đa là 159

### 00:06:00.800 - 00:06:08.000
 và chúng tôi cũng có thể lập biểu đồ phần thưởng theo thời gian để rõ ràng có tác dụng huấn luyện ở đây đối với thành công huấn luyện

### 00:06:13.519 - 00:06:18.719
 trên tập dữ liệu huấn luyện nên điều đó rất quan trọng ở đây và sau đó chúng tôi cũng có thể phân tích tập cuối cùng

### 00:06:18.800 - 00:06:28.720
 vẫn được lưu ở đây trong dữ liệu 250 và ở phía bên phải chúng ta có

### 00:06:29.440 - 00:06:37.280
thay đổi vị trí đào tạo và chúng ta có thể ánh xạ các vị trí đó trở lại thành âm một cho ngắn 0 cho

### 00:06:39.440 - 00:06:46.240
trung tính và cộng một cho mua và điều này giúp chúng ta thực sự tính toán tổng lợi nhuận

### 00:06:46.240 - 00:06:52.960
vì vậy chúng ta có thể chỉ cần nhân vị trí với lợi nhuận và tổng hợp chúng và chúng ta có ở đây

### 00:06:52.960 - 00:07:00.400
trong tập này cộng với 24,6 và chúng ta cũng có thể phân tích ở đây các vị trí đào tạo vì vậy trong 86 trường hợp

### 00:07:00.400 - 00:07:09.280
chúng ta mua thì trong 84 trường hợp chúng ta trung lập và trong 80 trường hợp chúng ta có một vị trí ngắn nên đây là một quá trình huấn luyện khá

### 00:07:09.280 - 00:07:16.160
quá mức ở đây và sau đó chúng tôi cũng có thể hình dung phần thưởng tập tích lũy theo thời gian

### 00:07:16.160 - 00:07:27.600
 vì vậy nó gần như tăng đều đặn nên chúng tôi có thể quan sát tiến trình huấn luyện ở đây và chỉ cần kiểm tra gấp đôi

### 00:07:27.600 - 00:07:36.560
kiểm tra xem chúng tôi có loại bỏ sự phân rã epsilon ở đây hay không nên nếu chúng tôi luôn tắt một epsilon thì chúng tôi chỉ

### 00:07:36.560 - 00:07:45.280
có các hành động ngẫu nhiên và trong trường hợp này nên tỷ lệ thành công này sẽ vào khoảng 50% vì vậy hãy kiểm tra kỹ điều này

### 00:07:46.160 - 00:07:57.920
để epsilon không đổi và một như vậy chúng ta chỉ có những đặc điểm ngẫu nhiên về hành động ngẫu nhiên và điều này sẽ

### 00:07:57.920 - 00:08:05.680
dẫn đến tỷ lệ thành công khoảng 50% 50,7 và tổng trung bình là 0,40 vì vậy đây chỉ là

### 00:08:05.680 - 00:08:14.560
kiểm tra chéo để đảm bảo rằng các hành động ngẫu nhiên sẽ dẫn đến tỷ lệ thành công là 50% vòng vèo và chúng ta sẽ tiếp tục

### 00:08:16.720 - 00:08:27.200
ở đây trong bài giảng tiếp theo, cảm ơn vì đã xem và hẹn gặp lại ở đó, tạm biệt

### 00:08:27.200 - 00:08:38.720
lead to a success rate of around about 50% 50.7 and an average total of of 0.40 so this is just a

### 00:08:38.720 - 00:08:47.680
cross-check that the random actions will lead to a success rate of 50% roundabout and we will continue

### 00:08:47.680 - 00:08:52.160
here in the next lecture thanks for watching and see you there bye

