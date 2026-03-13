## Nội dung

### 00:00:00.000 - 00:00:05.160
Xin chào và chào mừng bạn đến với dự án cuối cùng và cuối cùng này đào tạo một tác nhân học tập tăng cường

### 00:00:05.160 - 00:00:10.200
 cho giao dịch thuật toán và trong dự án này, chúng ta có thể áp dụng

### 00:00:10.200 - 00:00:15.679
thực hành những gì chúng ta đã học được cho đến nay và chúng ta sẽ xác định một số cạm bẫy và

### 00:00:15.679 - 00:00:21.280
thách thức mà chúng ta chưa từng thấy trong các dự án khác nên theo một cách nào đó, dự án này

### 00:00:21.280 - 00:00:26.640
phức tạp hơn các dự án trước vì chúng ta phải tự viết mã mọi thứ từ đầu

### 00:00:26.640 - 00:00:32.840
 nên chúng ta không có thư viện phòng tập thể dục trả về 

### 00:00:32.840 - 00:00:38.760
ngày tiếp theo hoặc phần thưởng của một hành động tự động nhưng chúng ta có thể và

### 00:00:38.760 - 00:00:46.079
chúng ta nên sử dụng lại càng nhiều dòng mã hóa càng tốt từ các dự án trước đó

### 00:00:46.079 - 00:00:51.000
chúng ta có thể làm điều này để có thể tái chế nhiều thứ nhưng chúng ta cũng nên ghi nhớ

### 00:00:51.000 - 00:00:56.040
một số khía cạnh cụ thể của dự án vì vậy bây giờ chúng ta sẽ quay lại với tập dữ liệu tài chính

### 00:00:56.039 - 00:01:02.519
 với đồng euro Mỹ nên đây là bộ dữ liệu hai năm với

### 00:01:02.519 - 00:01:09.159
dữ liệu giá hàng giờ cho tỷ giá hối đoái euro vâng đô la và chúng tôi có ở đây một vài của

### 00:01:09.159 - 00:01:16.719
các chỉ báo kỹ thuật cũng như lợi nhuận hàng giờ và trước hết chúng ta nên

### 00:01:16.719 - 00:01:23.079
đảm bảo rằng chúng ta chia toàn bộ dữ liệu thành một tập huấn luyện và nó đã được thiết lập sao cho

### 00:01:23.079 - 00:01:30.400
tỷ lệ phân chia có thể là 8020, vì vậy điều quan trọng là chúng ta

### 00:01:30.400 - 00:01:35.120
huấn luyện tác nhân trên tập huấn luyện và sau đó kiểm tra tác nhân trên tập kiểm tra

### 00:01:35.120 - 00:01:42.200
 và cũng ở đây chúng tôi sẽ cố gắng sử dụng thuật toán học Q để có bảng Q

### 00:01:42.200 - 00:01:49.039
 và điều này có nghĩa là chúng tôi cần rời rạc hóa thùng của mình các tính năng liên tục nên

### 00:01:49.040 - 00:01:54.160
các chỉ báo kỹ thuật cũng như lợi nhuận hàng giờ và xác định đúng

### 00:01:54.160 - 00:01:59.240
độ chi tiết chắc chắn là một điểm thách thức ở đây vì vậy chúng ta sẽ thấy có một

### 00:01:59.240 - 00:02:06.840
một vài ưu và nhược điểm để có một sự rời rạc hóa chi tiết hơn và như thế Tôi

### 00:02:06.840 - 00:02:12.480
đã nói lần này chúng ta không có bất kỳ gói bao bọc nào như phòng tập thể dục nên khi chúng ta

### 00:02:12.480 - 00:02:18.400
thực hiện một hành động kéo dài, ngắn hạn và trung lập thì chúng ta cần xác định và

### 00:02:18.400 - 00:02:24.400
tìm trạng thái tiếp theo cũng như phần thưởng sau hành động này nên có thêm một chút

### 00:02:24.400 - 00:02:30.000
mã hóa ở đây và chúng ta cũng không nên quên chi phí giao dịch nên đại lý

### 00:02:30.000 - 00:02:35.280
cần xem xét chi phí giao dịch và ít nhất chúng ta nên phạt đại lý

### 00:02:35.280 - 00:02:41.560
 về các chi phí nếu không chỉ là chi phí giao dịch trên thực tế

### 00:02:41.560 - 00:02:50.240
phạt đại lý vì giao dịch quá mức nên giao dịch quá mức hiếm khi hiệu quả và

### 00:02:50.240 - 00:02:55.920
bạn cũng sẽ thấy rằng cần phải xác định phân tích và quản lý việc trang bị quá mức vậy

### 00:02:55.920 - 00:03:01.680
tại sao việc trang bị quá mức lại hiện diện trong đại lý để trang bị quá mức có nghĩa là

### 00:03:01.680 - 00:03:07.240
hiệu suất trên tập huấn luyện cao hơn hoặc tốt hơn trên tập kiểm tra và

### 00:03:07.240 - 00:03:12.719
trang bị quá mức đặc biệt là một vấn đề ở đây đối với các tác nhân học tăng cường

### 00:03:12.719 - 00:03:20.640
đối với giao dịch thuật toán nên chúng ta sẽ thấy điều này sau ở đây trong phần này nhưng về cơ bản

### 00:03:20.640 - 00:03:26.240
đây là những điểm chính mà bạn cần tính đến và cả ở đây

### 00:03:26.240 - 00:03:31.960
Tôi thực sự khuyên bạn nên tự mình bắt đầu dự án và cuối cùng chúng ta cũng hãy xem

### 00:03:31.960 - 00:03:37.120
các tài liệu chi phí có sẵn cho phần này nên chúng ta sẽ ở đây trong các tài liệu về chi phí

### 00:03:37.120 - 00:03:44.040
 và bạn sẽ tìm thấy giải pháp ở đây trên học tăng cường

### 00:03:44.040 - 00:03:52.080
tác nhân giao dịch nên ở đây chúng ta bắt đầu với tệp CSV dữ liệu vây và ví dụ

### 00:03:52.080 - 00:03:56.439
chúng ta có thể bắt đầu ở đây bằng cách bỏ một số cột mà chúng ta không cần nữa và

### 00:03:56.960 - 00:04:03.840
cũng ở đây bên dưới bạn sẽ thấy một số kết quả trung gian nên chúng ta phải chia tập hợp

### 00:04:03.840 - 00:04:09.000
dữ liệu đầy đủ thành tập kiểm tra và tập huấn luyện và tôi đã lưu ở đây kết quả trung gian

### 00:04:09.000 - 00:04:15.039
để thuận tiện nhưng tất nhiên bạn có thể thực hiện điều này theo cách khác

### 00:04:15.039 - 00:04:21.240
hơi khác một chút nên đó là dự án cuối cùng và cuối cùng ở đây vì vậy đào tạo

### 00:04:21.240 - 00:04:25.839
một tác nhân học tập tăng cường cho giao dịch thuật toán, cảm ơn vì đã xem và

### 00:04:25.839 - 00:04:29.799
mong được gặp bạn trong các bài giảng tiếp theo, tạm biệt

