## Nội dung

### 00:00:00.000 - 00:00:05.839
Được rồi, chúng ta đã rời rạc hóa ngăn của mình thành một tính năng của tập huấn luyện và tập kiểm tra.

### 00:00:05.839 - 00:00:11.560
Và chúng ta đã học được rằng chúng ta cũng nên sử dụng các ngăn tập huấn luyện cho tập kiểm tra để tránh

### 00:00:11.560 - 00:00:18.699
rò rỉ dữ liệu và cũng là thời gian để tập hợp tất cả lại với nhau và rời rạc hóa tất cả các tính năng

### 00:00:18.699 - 00:00:21.359
trong tập huấn luyện và tập kiểm tra.

### 00:00:21.359 - 00:00:26.519
Và thực sự không có gì ngạc nhiên khi hai vòng lặp for thực sự thực hiện công việc ở đây.

### 00:00:26.519 - 00:00:34.079
Vì vậy, hãy bắt đầu ở đây với tập huấn luyện và chúng ta vẫn có F chỉ với một tính năng

### 00:00:34.079 - 00:00:35.480
rời rạc.

### 00:00:35.480 - 00:00:42.079
Và bây giờ chúng ta hãy tạo một danh sách trống, vì vậy, hãy liệt kê các cạnh bin nơi chúng tôi lưu trữ các cạnh bin cho

### 00:00:42.079 - 00:00:45.640
tất cả năm tính năng.

### 00:00:45.640 - 00:00:47.359
Và các tính năng như sau.

### 00:00:47.359 - 00:00:56.359
Vì vậy, chúng ta có tỷ lệ SMA, biểu đồ MACD, chỉ số cường độ tương đối, bộ dao động ngẫu nhiên,

### 00:00:56.359 - 00:00:58.759
cuối cùng là lợi nhuận.

### 00:00:58.759 - 00:01:04.840
Và chúng tôi muốn rời rạc hóa tất cả năm tính năng bằng cách sử dụng 11 bins.

### 00:01:04.840 - 00:01:07.280
Vậy đó là số lượng thùng.

### 00:01:07.280 - 00:01:16.760
Và sau đó chúng tôi lặp lại danh sách tính năng và đối với mỗi tính năng, chúng tôi thực sự thực hiện

### 00:01:16.760 - 00:01:22.319
một nhóm phân vị với 11 thùng.

### 00:01:22.319 - 00:01:24.719
Vì vậy, đây không phải là điều gì mới.

### 00:01:24.719 - 00:01:30.480
Sau đó, chúng ta nối các cạnh thùng vào danh sách các cạnh thùng.

### 00:01:30.480 - 00:01:35.480
Vì vậy, hãy chạy phần tiếp theo ở đây và kiểm tra huấn luyện F một lần nữa.

### 00:01:35.480 - 00:01:42.000
Vì vậy, bây giờ ở bên phải, chúng ta có cả 5 tính năng của thùng.

### 00:01:42.000 - 00:01:46.759
Và sau đó chúng ta cũng có thể kiểm tra danh sách các cạnh thùng.

### 00:01:46.759 - 00:01:52.400
Vì vậy, trước tiên chúng ta có các cạnh thùng cho tỷ lệ SMA.

### 00:01:52.400 - 00:02:03.200
Vì vậy, từ 0,977 đến 1,02, thì chúng ta có biểu đồ MACD, sau đó cường độ tương đối

### 00:02:03.200 - 00:02:07.760
chỉ số dao động trong khoảng từ 0 đến 100.

### 00:02:07.760 - 00:02:13.400
Vì vậy, giá trị thấp nhất gần bằng 7 và giá trị cao nhất là 95.

### 00:02:13.400 - 00:02:18.319
Vì vậy, giá trị thấp nhất gần bằng 7 và giá trị cao nhất là 95.

### 00:02:18.319 - 00:02:22.560
Và chúng ta có bộ dao động, bộ dao động ngẫu nhiên.

### 00:02:22.560 - 00:02:26.639
Và ở đây chúng ta có các giá trị nằm giữa âm 61 và 58.

### 00:02:26.639 - 00:02:30.919
Và cuối cùng chúng tôi có kết quả trả về.

### 00:02:30.919 - 00:02:34.840
Và sau đó chúng tôi cũng có thể kiểm tra xem bạn có thực sự có một nhóm lượng tử hay không.

### 00:02:34.840 - 00:02:42.359
Vì vậy, chúng ta nên có cùng số lượng quan sát và tất cả các thùng, ít nhiều như vậy

### 00:02:42.359 - 00:02:46.400
ở đây.

### 00:02:46.400 - 00:02:49.800
Vì vậy, đây là ví dụ cho chỉ số RSI.

### 00:02:49.800 - 00:02:55.080
Và sau đó khi tiếp tục, chúng ta có thể bỏ một số cột.

### 00:02:55.080 - 00:03:01.480
Vì vậy, trong quá trình huấn luyện, chúng ta không cần các giá trị tuyệt đối thêm một lần nữa.

### 00:03:01.480 - 00:03:05.439
Vì vậy, ở đây chúng ta chỉ cần các giá trị rời rạc.

### 00:03:05.439 - 00:03:08.040
Và do đó chúng ta có thể bỏ chúng ở đây.

### 00:03:08.040 - 00:03:10.640
Vì vậy, chúng ta tiếp tục với phần kết thúc. giá.

### 00:03:10.639 - 00:03:18.639
Vì vậy, chúng tôi vẫn cần giá đóng cửa để tính toán phần thưởng và lợi nhuận giao dịch.

### 00:03:18.639 - 00:03:21.639
Và bây giờ chúng tôi có thể tiếp tục ở đây với bộ thử nghiệm.

### 00:03:21.639 - 00:03:26.279
Vì vậy, chúng tôi vẫn có ở đây bộ thử nghiệm với tính năng một thùng.

### 00:03:26.279 - 00:03:32.439
Và sau đó quan trọng nhất, chúng tôi sử dụng danh sách các cạnh thùng giống nhau.

### 00:03:32.439 - 00:03:35.319
Và sau đó chúng tôi lặp lại các tính năng.

### 00:03:35.319 - 00:03:39.599
Và sau đó chúng tôi rời rạc hóa với pd.cat.

### 00:03:39.599 - 00:03:44.120
Vì vậy, đây sẽ không phải là một nhóm lượng tử.

### 00:03:44.120 - 00:03:47.680
Và đối với các thùng, chúng ta sử dụng các cạnh thùng.

### 00:03:47.680 - 00:03:53.280
Và chúng ta nên đảm bảo rằng chúng ta chọn danh sách cạnh thùng bên phải ở đây.

### 00:03:53.280 - 00:03:56.599
Vì vậy, ở đây chúng ta có một biến hỗ trợ khác.

### 00:03:56.599 - 00:04:03.400
Và trước tiên, khi chúng ta bắt đầu ở đây với tính năng đầu tiên, thì chúng ta chọn trong danh sách các cạnh thùng

### 00:04:03.400 - 00:04:05.599
danh sách đầu tiên.

### 00:04:05.599 - 00:04:09.400
Vì vậy, các cạnh thùng đầu tiên cho tính năng đầu tiên.

### 00:04:09.400 - 00:04:12.560
Và sau đó chúng ta tăng I lên một.

### 00:04:12.560 - 00:04:14.560
Vì vậy, hãy chạy ở đây.

### 00:04:14.560 - 00:04:17.240
Và sau đó chúng ta có thể bỏ đi một số nữa columns.

### 00:04:17.240 - 00:04:22.879
Vì vậy, đây là test.df với các tính năng bin và giá đóng.

### 00:04:22.879 - 00:04:27.959
Và sau đó một lần nữa, không có gì đáng ngạc nhiên khi đối với tập kiểm tra, nó không phải là lượng tử

### 00:04:27.959 - 00:04:28.959
binning.

### 00:04:28.959 - 00:04:32.639
Và chúng ta cũng có thể đếm số lượng giá trị trong mỗi bin.

### 00:04:32.639 - 00:04:37.199
Vì vậy, ví dụ: đối với lợi nhuận.

### 00:04:37.199 - 00:04:42.120
Vì vậy, ở đây có ít giá trị cực trị hơn so với tỷ lệ SMA.

### 00:04:42.120 - 00:04:46.159
Và thật thú vị, không có thành phần nào của bin.

### 00:04:46.159 - 00:04:51.039
Vì vậy, không có quan sát nào ở ngăn cuối cùng ở đây.

### 00:04:51.039 - 00:04:58.519
Vì vậy, ở đây chúng tôi có ít giá trị cực trị hơn cho tỷ lệ SMA.

### 00:04:58.519 - 00:05:03.079
Và sau đó chúng tôi có thể làm tương tự cho biểu đồ MACD.

### 00:05:03.079 - 00:05:05.879
Ngoài ra, ở đây chúng tôi có ít giá trị cực trị hơn.

### 00:05:05.879 - 00:05:14.159
Vì vậy, có vẻ như trong giai đoạn huấn luyện, chúng tôi có nhiều biến động hơn và nhiều giá trị cực trị hơn.

### 00:05:14.159 - 00:05:20.759
Và điều này chắc chắn có thể gây hại cho hiệu suất của tác nhân sau này trong quá trình thử nghiệm set.

### 00:05:20.759 - 00:05:25.639
Vì vậy, chúng ta có thể nghĩ đến việc cắt tập huấn luyện ở đây.

### 00:05:25.639 - 00:05:33.319
Và có thể chỉ sử dụng 5000 thanh mới nhất hoặc bất cứ thứ gì, bởi vì tôi nghĩ hầu hết sự biến động

### 00:05:33.319 - 00:05:41.919
chỉ ở đây trong giai đoạn bắt đầu của năm 2022 và 2023.

### 00:05:41.919 - 00:05:45.240
Vì vậy, điều này không được cố định chắc chắn.

### 00:05:45.240 - 00:05:49.000
Và sau đó chúng ta cũng hãy kiểm tra chỉ số RSI ở đây.

### 00:05:49.000 - 00:05:56.360
Vì vậy, điều này ở đây có vẻ cân bằng hơn một chút và cũng là ngẫu nhiên oscillator.

### 00:05:56.360 - 00:05:59.519
Ở đây khá cân bằng.

### 00:05:59.519 - 00:06:04.319
Bây giờ đã có các giá trị rời rạc cho tập huấn luyện và cả tập kiểm tra, chúng ta đã sẵn sàng

### 00:06:04.319 - 00:06:05.319
để tiếp tục.

### 00:06:05.319 - 00:06:09.040
Cảm ơn bạn đã theo dõi và mong được gặp bạn trong bài giảng tiếp theo.

### 00:06:09.040 - 00:06:09.519
Tạm biệt.

