## Nội dung

### 00:00:00.000 - 00:00:06.000
Trong video này, chúng ta sẽ triển khai chính sách của mình, trong trường hợp này sẽ được biểu thị bằng một nơron

### 00:00:06.000 - 00:00:13.000
mạng sẽ tạo ra xác suất thực hiện từng hành động và tính toán.

### 00:00:13.000 - 00:00:21.000
Hiệu suất của chính sách này sẽ có thể sửa đổi các tham số của nó để tìm ra chính sách tối ưu.

### 00:00:22.000 - 00:00:29.000
Hãy nhớ rằng trong các phần trước, chính sách là một hàm trả về hành động đã chọn khi

### 00:00:29.000 - 00:00:30.000
chúng tôi đã gọi nó.

### 00:00:37.000 - 00:00:41.000
Hoặc xác suất chọn từng hành động.

### 00:00:43.000 - 00:00:46.000
Trong trường hợp này, chính sách sẽ là một đối tượng.

### 00:00:48.000 - 00:00:53.000
Điều đó sẽ gọi việc chuyển một đối số trạng thái như chúng ta đã làm trước đây.

### 00:00:55.000 - 00:01:05.000
Và để tạo đối tượng này, chúng ta sẽ sử dụng lớp tuần tự giống như chúng ta đã làm trong các phần trước.

### 00:01:06.000 - 00:01:14.000
Lớp này tạo ra một mạng lưới thần kinh sẽ áp dụng một số thao tác một cách tuần tự cho đầu vào

### 00:01:14.000 - 00:01:17.000
mà chúng tôi đưa vào mạng lưới thần kinh.

### 00:01:17.000 - 00:01:24.000
Đó là khi chúng ta chuyển trạng thái làm đầu vào, mạng nơ-ron sẽ áp dụng một số thao tác để tạo ra

### 00:01:24.000 - 00:01:24.000
đầu ra.

### 00:01:26.000 - 00:01:32.000
Và đầu ra đó sẽ là một vectơ có xác suất thực hiện từng hành động.

### 00:01:32.000 - 00:01:36.000
Và với mạng lưới thần kinh này, chúng ta sẽ chuyển các thao tác sau.

### 00:01:37.000 - 00:01:45.000
Đầu tiên sẽ là một phép toán tuyến tính lấy một vectơ đầu vào, trong trường hợp này là trạng thái,

### 00:01:45.000 - 00:01:47.000
và nó sẽ tạo ra.

### 00:01:49.000 - 00:01:54.000
Một vectơ đầu ra bao gồm 128 phần tử.

### 00:01:57.000 - 00:02:05.000
Và bên cạnh vectơ 128 giá trị này, chúng ta sẽ áp dụng hàm kích hoạt để phá vỡ tính tuyến tính của

### 00:02:05.000 - 00:02:07.000
thao tác trước đó.

### 00:02:07.000 - 00:02:10.000
Trong trường hợp này, chúng tôi sẽ áp dụng hàm Relu.

### 00:02:14.000 - 00:02:19.000
Bây giờ chúng ta sẽ lặp lại hai thao tác này một lần nữa.

### 00:02:26.000 - 00:02:36.000
Thay đổi kích thước của đầu vào của lớp tuyến tính thành vectơ gồm 128 phần tử như phần tử được tạo

### 00:02:36.000 - 00:02:39.000
bởi hoạt động tuyến tính trước đó.

### 00:02:40.000 - 00:02:47.000
Và lần này đầu ra sẽ bao gồm một vectơ gồm 64 phần tử.

### 00:02:48.000 - 00:02:50.000
Và sau đó chúng tôi sẽ áp dụng.

### 00:02:50.000 - 00:02:55.000
Chúng ta sẽ áp dụng lại hàm Relu để phá vỡ tính tuyến tính của thao tác này.

### 00:02:56.000 - 00:03:06.000
Và sau đó chúng ta sẽ thêm một lớp tuyến tính cuối cùng sẽ lấy vectơ với 64 phần tử được tạo làm đầu vào

### 00:03:06.000 - 00:03:08.000
bởi lớp thứ hai.

### 00:03:10.000 - 00:03:14.000
Và nó sẽ tạo ra một vectơ có nhiều phần tử.

### 00:03:16.000 - 00:03:19.000
Như những hành động mà đại lý đã có sẵn.

### 00:03:26.000 - 00:03:35.000
Nhưng các phần tử mà thao tác này tạo ra nằm trong phạm vi từ vô cực âm đến vô cực dương.

### 00:03:38.000 - 00:03:46.000
Nhưng chúng tôi muốn vectơ này biểu thị xác suất và để làm được điều đó, chúng tôi sẽ áp dụng kích hoạt softmax

### 00:03:46.000 - 00:03:47.000
chức năng.

### 00:03:50.000 - 00:03:55.000
Chuyển làm đối số cho thứ nguyên mà chúng ta muốn áp dụng thao tác này.

### 00:03:55.000 - 00:04:00.000
Trong trường hợp này, chúng tôi muốn áp dụng nó trên chiều cuối cùng.

### 00:04:03.000 - 00:04:11.000
Bây giờ đầu ra của mạng nơ-ron này sẽ là một vectơ có các giá trị tổng bằng một.

### 00:04:16.000 - 00:04:20.000
Và bây giờ mạng lưới thần kinh của chúng tôi đã sẵn sàng để sử dụng.

### 00:04:23.000 - 00:04:26.000
Bây giờ chúng ta hãy xem một cách thực tế nó hoạt động như thế nào.

### 00:04:28.000 - 00:04:33.000
Để làm được điều đó, chúng ta sẽ gọi mạng lưới thần kinh đi qua ba trạng thái khác nhau.

### 00:04:34.000 - 00:04:40.000
Chúng ta gọi trạng thái đầu tiên là trạng thái trung lập vì trong đó lá bài sẽ ở trung tâm.

### 00:04:43.000 - 00:04:46.000
Góc của cực cũng sẽ bằng không.

### 00:04:46.000 - 00:04:53.000
Và vận tốc của cột, tức là nó rơi sang trái hay sang phải cũng sẽ bằng không.

### 00:04:54.000 - 00:05:02.000
Vì vậy, tóm lại, đây là trạng thái mà tác nhân không có nguy cơ thất bại sắp xảy ra.

### 00:05:02.000 - 00:05:11.000
Trạng thái thứ hai chúng ta gọi là bên trái Nguy hiểm, và trong đó xe đẩy nằm ở mép trái của đường ngang

### 00:05:11.000 - 00:05:12.000
trục.

### 00:05:12.000 - 00:05:19.000
Vì vậy, nếu đặc vụ di chuyển sang trái, tập phim sẽ kết thúc và đặc vụ sẽ thua cuộc.

### 00:05:19.000 - 00:05:26.000
Và chúng ta có trạng thái thứ ba trong đó xe đẩy nằm ở cạnh phải của trục hoành.

### 00:05:26.000 - 00:05:32.000
Tức là nếu chúng ta di chuyển xe sang bên phải thì tập phim sẽ kết thúc và người đại diện sẽ thua cuộc.

### 00:05:37.000 - 00:05:39.000
Hãy chạy tế bào này.

### 00:05:40.000 - 00:05:47.000
Và bây giờ những gì chúng ta sẽ làm là gọi chính sách, chuyển từng trạng thái này làm đầu vào.

### 00:05:47.000 - 00:05:55.000
Và chúng tôi sẽ sử dụng chức năng đạo cụ hành động cốt truyện để hiển thị bằng đồ họa xác suất mà chính sách chỉ định

### 00:05:55.000 - 00:05:59.000
cho mỗi hành động được thực hiện ở mỗi trạng thái này.

### 00:06:02.000 - 00:06:07.000
Hãy nhớ rằng mạng nơ-ron đã được khởi tạo với các tham số ngẫu nhiên.

### 00:06:07.000 - 00:06:13.000
Vì vậy, các xác suất mà chúng ta sắp thấy không phản ánh hành động đúng ngay từ đầu

### 00:06:13.000 - 00:06:20.000
của quá trình học, mạng nơ-ron sẽ gán các xác suất ngẫu nhiên ở trạng thái trung tính.

### 00:06:20.000 - 00:06:25.000
Như bạn có thể thấy, mặc dù xác suất di chuyển sang phải cao hơn một chút so với xác suất

### 00:06:25.000 - 00:06:33.000
di chuyển sang trái, cả hai đều khá gần nhau vì chúng được tạo ra bởi mạng lưới thần kinh với các tham số ngẫu nhiên.

### 00:06:37.000 - 00:06:38.000
Trên bất động sản.

### 00:06:38.000 - 00:06:39.000
Đại lý đâu.

### 00:06:41.000 - 00:06:43.000
Có nguy cơ thua nếu nó di chuyển sang trái.

### 00:06:47.000 - 00:06:53.000
Như chúng ta có thể thấy, các xác suất rất giống nhau vì trước khi quá trình học bắt đầu,

### 00:06:53.000 - 00:06:56.000
chính sách gán xác suất ngẫu nhiên cho mỗi hành động.

### 00:06:57.000 - 00:07:03.000
Và điều tương tự cũng xảy ra ở trạng thái mà tác nhân gặp rủi ro nếu nó di chuyển sang phải.

### 00:07:09.000 - 00:07:14.000
Như bạn có thể thấy, khi chúng ta chuyển một trạng thái sang mạng nơ-ron, nó sẽ tạo ra một vectơ xác suất

### 00:07:15.000 - 00:07:20.000
dựa vào đó chúng tôi sẽ chọn hành động cần thực hiện.

### 00:07:26.000 - 00:07:30.000
Trong phần còn lại của phần này, chúng ta sẽ đào tạo.

### 00:07:31.000 - 00:07:33.000
Chính sách sử dụng phương pháp củng cố.

### 00:07:34.000 - 00:07:37.000
Và sau đó chúng ta sẽ thực hiện lại các ô tương tự.

### 00:07:38.000 - 00:07:42.000
Để xem việc ra quyết định về chính sách đã thay đổi như thế nào.

### 00:07:43.000 - 00:07:47.000
Và chúng ta sẽ xem ở mỗi trạng thái nó sẽ cho xác suất cao hơn như thế nào.

### 00:07:48.000 - 00:07:50.000
Để hành động đúng đắn.

### 00:07:51.000 - 00:07:53.000
Tôi sẽ gặp bạn trong video tiếp theo.

