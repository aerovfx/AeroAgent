## Nội dung

### 00:00:00.000 - 00:00:06.000
Trong phần này, chúng ta sẽ kết hợp thuật toán Q-learning với mạng nơ-ron.

### 00:00:06.000 - 00:00:10.000
Thuật toán kết quả sẽ được gọi là deep q-learning.

### 00:00:12.000 - 00:00:15.000
Điều đầu tiên chúng ta sẽ làm là nhập các thư viện mã.

### 00:00:17.000 - 00:00:20.000
Trong trường hợp này, sẽ giống như trong phần trước.

### 00:00:24.000 - 00:00:26.000
Hãy thực thi ô.

### 00:00:29.000 - 00:00:31.000
Và bây giờ chúng tôi có sẵn chúng.

### 00:00:32.000 - 00:00:37.000
Điều tiếp theo chúng ta sẽ làm là tạo ra môi trường mà tác nhân sẽ phải đối mặt.

### 00:00:37.000 - 00:00:46.000
Để làm được điều đó, chúng ta sẽ sử dụng hàm tạo từ phòng tập thể dục, thư viện Và môi trường mà chúng ta

### 00:00:46.000 - 00:00:50.000
sắp tạo được gọi là phiên bản Cartpole số 0.

### 00:00:51.000 - 00:00:59.000
Trong môi trường này, chúng ta sẽ tạo một chiếc xe đẩy sẽ di chuyển trên một đường ray nằm ngang và chiếc xe đẩy này

### 00:00:59.000 - 00:01:02.000
được gắn vào một cột thẳng đứng mà chúng ta phải giữ thẳng.

### 00:01:02.000 - 00:01:06.000
Và để làm được điều đó chúng ta có thể di chuyển xe sang trái hoặc sang phải.

### 00:01:07.000 - 00:01:09.000
Nhưng hãy nói điều đó một cách trực quan.

### 00:01:10.000 - 00:01:16.000
Điều đầu tiên chúng ta phải làm là khởi tạo môi trường để có thể hiển thị nó bằng đồ họa.

### 00:01:18.000 - 00:01:27.000
Bây giờ chúng ta gọi phương thức tôi hiển thị để hiển thị hình ảnh của môi trường sẽ chuyển làm đối số cho

### 00:01:27.000 - 00:01:28.000
chức năng này.

### 00:01:28.000 - 00:01:32.000
Và hình ảnh này sẽ có được nó bằng cách gọi phương thức kết xuất trên môi trường.

### 00:01:32.000 - 00:01:42.000
Chúng tôi sẽ cung cấp cho nó chế độ đối số từ khóa bằng để nó trả về hình ảnh dưới dạng một mảng pixel có nhiều pixel.

### 00:01:42.000 - 00:01:46.000
Hãy chạy ô này và bây giờ chúng ta có nhiệm vụ mà chúng ta sẽ giải quyết.

### 00:01:49.000 - 00:01:50.000
Mảnh đen này.

### 00:01:50.000 - 00:01:56.000
Đây là lá bài sẽ di chuyển theo trục ngang để giữ cho cột thẳng.

### 00:01:56.000 - 00:01:58.000
Cây cột sẽ có xu hướng rơi sang hai bên.

### 00:01:59.000 - 00:02:04.000
Và khi vượt qua một góc nhất định thì tập phim sẽ kết thúc.

### 00:02:06.000 - 00:02:07.000
Để tránh điều đó.

### 00:02:07.000 - 00:02:11.000
Nếu cột đổ về bên trái thì chúng ta sẽ phải di chuyển xe về hướng đó.

### 00:02:12.000 - 00:02:17.000
Và nếu cái bát rơi về bên phải thì chúng ta sẽ phải di chuyển chiếc xe về bên phải.

### 00:02:18.000 - 00:02:24.000
Phần thưởng sẽ tích cực cho mọi thời điểm khi cột không bị đổ.

### 00:02:24.000 - 00:02:29.000
Tức là trong khi cực vẫn nằm trong góc cho phép.

### 00:02:31.000 - 00:02:35.000
Bây giờ hãy kiểm tra không gian trạng thái và không gian hành động.

### 00:02:35.000 - 00:02:38.000
Hãy viết các tuyên bố của nhà nước.

### 00:02:39.000 - 00:02:42.000
Và hãy kiểm tra không gian trạng thái.

### 00:02:49.000 - 00:02:55.000
Từ thuộc tính hình dạng, chúng ta có thể lấy số phần tử trong trạng thái.

### 00:02:56.000 - 00:02:59.000
Bây giờ hãy kiểm tra không gian hành động.

### 00:03:01.000 - 00:03:06.000
Và số lượng hành động được phép được lưu trữ trong biến n.

### 00:03:16.000 - 00:03:20.000
Và bây giờ hãy hiển thị giá trị của từng biến này.

### 00:03:46.000 - 00:03:48.000
Hãy chạy ô này và chúng ta có nó ở đây.

### 00:03:52.000 - 00:03:56.000
Môi trường sẽ có một không gian trạng thái liên tục, bốn chiều.

### 00:03:57.000 - 00:04:01.000
Trong một không gian hành động có hai hành động sẵn có.

### 00:04:02.000 - 00:04:04.000
Di chuyển sang trái hay phải?

### 00:04:07.000 - 00:04:13.000
Bốn giá trị của trạng thái là vị trí của xe trên trục hoành, tốc độ của xe.

### 00:04:13.000 - 00:04:13.000
xe đẩy.

### 00:04:14.000 - 00:04:16.000
Góc của cột.

### 00:04:17.000 - 00:04:20.000
Và tốc độ rơi của cột.

### 00:04:23.000 - 00:04:30.000
Điều tiếp theo chúng ta sẽ làm là chuẩn bị môi trường này để làm việc với thư viện PyTorch

### 00:04:30.000 - 00:04:34.000
và chúng ta sẽ làm điều đó với lớp mà chúng ta đã viết ở phần trước.

### 00:04:34.000 - 00:04:40.000
Hãy thực thi ô này và bao bọc môi trường của chúng ta bằng trình bao bọc lớp này.

### 00:04:44.000 - 00:04:52.000
Bây giờ chúng ta hãy thực thi ô này để kiểm tra xem các trạng thái, phần thưởng và biến Don có hình dạng không

### 00:04:52.000 - 00:04:53.000
mà chúng tôi cần.

### 00:04:56.000 - 00:04:59.000
Ở đây sử dụng phương pháp thiết lập lại.

### 00:04:59.000 - 00:05:01.000
Chúng tôi đã có được trạng thái này.

### 00:05:02.000 - 00:05:09.000
Nó bao gồm một tenxơ có bốn phần tử, cùng với hai chiều bổ sung mà chúng tôi cần để làm việc

### 00:05:09.000 - 00:05:11.000
với nhiều trạng thái.

### 00:05:11.000 - 00:05:17.000
Và điều tương tự cũng xảy ra với trạng thái tiếp theo thu được sau khi gọi phương thức bước.

### 00:05:18.000 - 00:05:20.000
Và phần thưởng và biến giả.

### 00:05:20.000 - 00:05:28.000
Chúng ta có thể thấy rằng cả hai đều có một giá trị duy nhất, nhưng chúng đều có hai chiều bổ sung mà chúng ta cần

### 00:05:28.000 - 00:05:30.000
để có thể làm việc với hàng loạt.

### 00:05:31.000 - 00:05:36.000
Bây giờ hãy tạo mạng nơ-ron mà chúng ta sẽ sử dụng để ước tính các giá trị Q.

### 00:05:36.000 - 00:05:39.000
Trong trường hợp này, đầu vào sẽ có bốn phần tử.

### 00:05:41.000 - 00:05:49.000
Và nó sẽ tạo ra đầu ra gồm hai phần tử mà giá trị Q ước tính cho mỗi hành động khả dụng.

### 00:05:51.000 - 00:05:55.000
Để làm được điều đó, chúng ta sẽ tạo một biến gọi là q-network.

### 00:05:57.000 - 00:06:00.000
Mạng sẽ tạo ra ước tính giá trị Q.

### 00:06:00.000 - 00:06:07.000
Và như trước đây, chúng ta sẽ sử dụng lớp tuần tự từ thư viện PyTorch để tạo ra một

### 00:06:07.000 - 00:06:11.000
mạng nơ-ron trong đó các hoạt động được áp dụng một cách tuần tự.

### 00:06:16.000 - 00:06:21.000
Và đối với mạng lưới thần kinh đó, chúng ta sẽ đưa vào một số thao tác.

### 00:06:21.000 - 00:06:24.000
Đầu tiên trong số đó sẽ là một hoạt động tuyến tính.

### 00:06:25.000 - 00:06:31.000
Điều đó sẽ nhân đầu vào của mạng lưới thần kinh với một ma trận các tham số.

### 00:06:34.000 - 00:06:42.000
Chúng tôi chuyển nó dưới dạng đối số, kích thước của đầu vào, sẽ là trạng thái mờ mà như chúng tôi biết sẽ là bốn

### 00:06:42.000 - 00:06:52.000
và chúng ta viết kích thước đầu ra của lớp đầu tiên đó và đầu ra sẽ là một vectơ gồm 128 phần tử.

### 00:06:52.000 - 00:06:58.000
Sau khi áp dụng, các thao tác này sẽ biến đổi kết quả bằng thao tác Relu.

### 00:07:00.000 - 00:07:05.000
Hoạt động này, như bạn đã biết, phá vỡ tính tuyến tính của hoạt động trước đó.

### 00:07:07.000 - 00:07:10.000
Bây giờ chúng ta sẽ lặp lại hai thao tác này.

### 00:07:11.000 - 00:07:16.000
Nhưng sửa đổi kích thước đầu vào và đầu ra của họ.

### 00:07:17.000 - 00:07:26.000
Lớp tuyến tính thứ hai sẽ có đầu vào là vectơ gồm 128 phần tử mà lớp tuyến tính thứ nhất tạo ra

### 00:07:26.000 - 00:07:32.000
làm đầu ra và đầu ra của cái thứ hai sẽ là 64 phần tử.

### 00:07:32.000 - 00:07:38.000
Điều tiếp theo chúng ta sẽ làm là tạo một phép toán tuyến tính khác lấy vectơ đầu vào

### 00:07:38.000 - 00:07:47.000
với 64 phần tử xuất phát từ lớp tuyến tính thứ hai và sẽ có đầu ra với số lượng

### 00:07:47.000 - 00:07:47.000
hành động.

### 00:07:48.000 - 00:07:49.000
Đó là hai.

### 00:07:53.000 - 00:07:56.000
Và cùng với đó, chúng ta có mạng lưới thần kinh.

### 00:07:56.000 - 00:07:58.000
Hãy chạy tế bào này.

### 00:07:58.000 - 00:08:00.000
Và bây giờ chúng tôi đã có sẵn nó.

### 00:08:01.000 - 00:08:07.000
Trong trường hợp này, như trong phần trước, chúng ta sẽ sử dụng mạng mục tiêu là mạng nơ-ron

### 00:08:07.000 - 00:08:15.000
sẽ không tham gia vào quá trình học tập và mục đích duy nhất của nó là tính toán các giá trị đích

### 00:08:15.000 - 00:08:16.000
cho quy tắc cập nhật.

### 00:08:18.000 - 00:08:19.000
Vì điều đó.

### 00:08:19.000 - 00:08:22.000
Chúng tôi viết mạng mục tiêu.

### 00:08:24.000 - 00:08:30.000
Và chúng tôi sử dụng chức năng Deepcopy để tạo một bản sao chính xác của mạng lưới thần kinh.

### 00:08:33.000 - 00:08:37.000
Và trên mạng lưới thần kinh này, chúng tôi gọi là phương thức.

### 00:08:38.000 - 00:08:44.000
Để tránh những dự đoán của mạng lưới thần kinh này hãy tham gia vào quá trình học tập.

### 00:08:44.000 - 00:08:45.000
Hãy chạy tế bào này.

### 00:08:45.000 - 00:08:47.000
Và bây giờ chúng tôi đã có sẵn nó.

### 00:08:49.000 - 00:08:55.000
Điều tiếp theo chúng ta sẽ làm là tạo chính sách sẽ sử dụng để khám phá môi trường.

### 00:08:55.000 - 00:09:01.000
Trong trường hợp này, chúng ta sẽ sử dụng chính sách tham lam epsilon, giống như chính sách chúng ta đã sử dụng ở phần trước.

### 00:09:01.000 - 00:09:02.000
phần.

### 00:09:03.000 - 00:09:05.000
Vì vậy, hãy chạy tế bào này.

### 00:09:06.000 - 00:09:08.000
Và ở đây chúng tôi có nó.

### 00:09:09.000 - 00:09:15.000
Ngoài ra, như trong phần trước, chúng ta sẽ tạo ra một trải nghiệm, phát lại ký ức mà chúng ta

### 00:09:15.000 - 00:09:20.000
sẽ sử dụng để tạo ra hàng loạt trải nghiệm mà chúng tôi sẽ sử dụng để cập nhật mạng lưới thần kinh.

### 00:09:24.000 - 00:09:29.000
Chúng tôi đã sao chép lớp mà chúng tôi đã tạo trong phần trước và với nó, chúng tôi sẽ triển khai

### 00:09:29.000 - 00:09:30.000
bộ nhớ phát lại của chúng tôi.

### 00:09:33.000 - 00:09:34.000
Xong.

### 00:09:36.000 - 00:09:40.000
Trong video tiếp theo, chúng ta sẽ bắt đầu triển khai thuật toán.

