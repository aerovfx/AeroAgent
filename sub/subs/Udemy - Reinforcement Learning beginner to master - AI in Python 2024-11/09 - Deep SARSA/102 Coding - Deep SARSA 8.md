## Nội dung

### 00:00:02.000 - 00:00:06.000
Trong video này, chúng ta sẽ bắt đầu triển khai thuật toán tìm kiếm sâu.

### 00:00:08.000 - 00:00:12.000
Để làm được điều đó, chúng ta sẽ tạo một hàm gọi là dbsa.

### 00:00:14.000 - 00:00:21.000
Và hàm này sẽ lấy mạng thần kinh tạo ra ước tính giá trị q làm đầu vào.

### 00:00:23.000 - 00:00:24.000
Chính sách.

### 00:00:25.000 - 00:00:28.000
Và một số tập phim.

### 00:00:29.000 - 00:00:32.000
Cũng như một vài thông số khác mà chúng ta có thể điều chỉnh.

### 00:00:33.000 - 00:00:40.000
Cái đầu tiên trong số đó là Alpha, như bạn biết, là tốc độ học mà chúng tôi thay đổi các tham số

### 00:00:40.000 - 00:00:41.000
của mạng lưới thần kinh.

### 00:00:43.000 - 00:00:50.000
Tham số thứ hai là kích thước lô, số lần chuyển đổi trạng thái được đưa vào mỗi lần trải nghiệm.

### 00:00:50.000 - 00:00:54.000
batch và chúng tôi sẽ khởi tạo giá trị này là 32.

### 00:00:56.000 - 00:01:02.000
Tham số tiếp theo là gamma, như bạn biết, là hệ số chiết khấu cho các giá trị và phần thưởng trong tương lai.

### 00:01:04.000 - 00:01:11.000
Và tham số cuối cùng là epsilon, xác suất chính sách sẽ chọn một hành động ngẫu nhiên.

### 00:01:14.000 - 00:01:20.000
Trong trường hợp này, chúng tôi sẽ thực hiện một hành động ngẫu nhiên trong 5% thời gian.

### 00:01:22.000 - 00:01:24.000
Bây giờ chúng ta hãy cuộn một chút.

### 00:01:26.000 - 00:01:33.000
Và hãy tạo một thể hiện của một đối tượng sẽ đảm nhiệm việc áp dụng quy tắc cập nhật để sửa đổi

### 00:01:33.000 - 00:01:34.000
các thông số mạng nơ-ron.

### 00:01:34.000 - 00:01:42.000
Đối tượng này là một thể hiện của lớp Adam W và nó sẽ lấy hai giá trị đầu vào.

### 00:01:42.000 - 00:01:46.000
Đầu tiên là danh sách các tham số của mạng lưới thần kinh.

### 00:01:48.000 - 00:01:54.000
Đó sẽ là những thông số mà đối tượng này sẽ sửa đổi trong quá trình học.

### 00:01:55.000 - 00:01:59.000
Và tham số thứ hai là tốc độ học tập.

### 00:02:00.000 - 00:02:01.000
Đó là Alpha.

### 00:02:04.000 - 00:02:11.000
Đối tượng này là một sửa đổi nhỏ của quy tắc cập nhật giảm độ dốc ngẫu nhiên sẽ làm cho

### 00:02:11.000 - 00:02:14.000
quá trình học tập hiệu quả hơn.

### 00:02:14.000 - 00:02:20.000
Trên thực tế, đây không phải là sửa đổi duy nhất đối với quy tắc cập nhật này tồn tại trong những năm qua.

### 00:02:20.000 - 00:02:26.000
Một số cải tiến về giảm độ dốc ngẫu nhiên đã được phát hiện, mỗi cải tiến đều đạt được

### 00:02:26.000 - 00:02:29.000
cải thiện nhỏ trong hiệu suất của họ.

### 00:02:29.000 - 00:02:35.000
Vì điều này không liên quan trực tiếp đến học tăng cường nên chúng tôi sẽ không đề cập đến nó trong

### 00:02:35.000 - 00:02:35.000
chi tiết hơn.

### 00:02:35.000 - 00:02:42.000
Nhưng nếu bạn quan tâm, tôi khuyên bạn nên xem tài liệu PyTorch để làm quen

### 00:02:42.000 - 00:02:44.000
với các quy tắc cập nhật hiện có.

### 00:02:44.000 - 00:02:47.000
Điều tiếp theo chúng ta sẽ làm là khởi tạo bộ nhớ.

### 00:02:49.000 - 00:02:57.000
Chúng ta sẽ làm điều đó bằng cách tạo một thể hiện của lớp bộ nhớ phát lại và chúng ta sẽ cung cấp cho nó một dung lượng

### 00:02:57.000 - 00:02:59.000
của một triệu lần chuyển đổi.

### 00:03:00.000 - 00:03:08.000
Tiếp theo, điều chúng ta sẽ làm là lưu trữ một từ điển với số liệu thống kê thực thi của thuật toán.

### 00:03:08.000 - 00:03:14.000
Một mặt, chúng ta muốn lưu trữ các giá trị của hàm chi phí vì chúng sẽ cho chúng ta biết liệu

### 00:03:14.000 - 00:03:18.000
mạng lưới thần kinh đang cải thiện ước tính của nó về các giá trị Q.

### 00:03:19.000 - 00:03:22.000
Và chúng tôi sẽ khởi tạo mục này dưới dạng danh sách trống.

### 00:03:23.000 - 00:03:27.000
Mặt khác, chúng tôi muốn lưu trữ lợi nhuận.

### 00:03:28.000 - 00:03:33.000
Mà tác nhân có được trong mỗi tập phim đối mặt với môi trường.

### 00:03:36.000 - 00:03:42.000
Và sau khi quá trình thực hiện thuật toán này kết thúc, chúng tôi sẽ vẽ biểu đồ thống kê này.

### 00:03:47.000 - 00:03:50.000
Bây giờ chúng ta sẽ vào vòng lặp chính.

### 00:03:51.000 - 00:03:56.000
Điều đó sẽ thực thi đối với số tập được cung cấp cho thuật toán làm đối số.

### 00:03:58.000 - 00:04:01.000
Và chúng ta sẽ làm điều đó bằng cách tạo một vòng lặp for.

### 00:04:10.000 - 00:04:13.000
Nhưng đối với vòng lặp này, chúng ta sẽ thực hiện một sửa đổi nhỏ.

### 00:04:13.000 - 00:04:21.000
Chúng ta sẽ gói nó bằng hàm tqdm, hàm này sẽ hiển thị cho chúng ta một thanh tiến trình nơi chúng ta sẽ xem cách thực hiện

### 00:04:21.000 - 00:04:26.000
nhiều lần lặp của vòng lặp đã kết thúc và còn lại bao nhiêu lần.

### 00:04:26.000 - 00:04:32.000
Và chúng ta sẽ làm điều đó vì bắt đầu từ phần này, các thuật toán sẽ mất nhiều thời gian hơn một chút để

### 00:04:32.000 - 00:04:36.000
kết thúc, vì vậy tốt hơn chúng ta nên nhận được một số phản hồi về những gì đang diễn ra.

### 00:04:36.000 - 00:04:39.000
Điều tiếp theo chúng ta sẽ làm là khởi tạo môi trường.

### 00:04:41.000 - 00:04:43.000
Và cũng khởi tạo biến.

### 00:04:44.000 - 00:04:45.000
Xong.

### 00:04:46.000 - 00:04:52.000
Ngoài ra, chúng tôi sẽ giữ một biến để theo dõi phần thưởng mà chúng tôi nhận được trong

### 00:04:52.000 - 00:04:54.000
để tính toán lợi nhuận.

### 00:04:54.000 - 00:04:57.000
Để chúng tôi có thể hiển thị nó trong biểu đồ thống kê của mình.

### 00:05:01.000 - 00:05:02.000
Sau đó chúng ta sẽ vào.

### 00:05:03.000 - 00:05:04.000
Một vòng lặp bên trong.

### 00:05:06.000 - 00:05:06.000
Viết.

### 00:05:08.000 - 00:05:10.000
Trong khi chưa xong.

### 00:05:15.000 - 00:05:19.000
Và bên trong vòng lặp bên trong, điều đầu tiên chúng ta làm là chọn một hành động.

### 00:05:20.000 - 00:05:25.000
Và hành động đó sẽ là kết quả của việc gọi chính sách với trạng thái hiện tại.

### 00:05:28.000 - 00:05:30.000
Và giá trị của Epsilon.

### 00:05:31.000 - 00:05:33.000
Như chúng ta có thể thấy ở đây.

### 00:05:36.000 - 00:05:40.000
Tiếp theo, chúng ta sẽ thực hiện hành động kết quả trong môi trường.

### 00:05:44.000 - 00:05:48.000
Hãy nhớ rằng chúng ta đang sử dụng một lớp bao bọc môi trường.

### 00:05:54.000 - 00:05:57.000
Và điều đó chuẩn bị cho mọi yếu tố mà môi trường mang lại cho chúng ta.

### 00:05:59.000 - 00:06:05.000
Được sử dụng với thư viện PyTorch và nó cũng chuẩn bị các hành động mà chúng ta chuyển qua để chúng

### 00:06:05.000 - 00:06:08.000
có thể được sử dụng bên trong môi trường.

### 00:06:12.000 - 00:06:17.000
Điều tiếp theo chúng ta sẽ làm là lưu trữ quá trình chuyển đổi này trong bộ nhớ của mình.

### 00:06:19.000 - 00:06:22.000
Bằng cách gọi phương thức chèn.

### 00:06:24.000 - 00:06:30.000
Chúng ta sẽ lưu trữ một danh sách với trạng thái, hành động, phần thưởng, giá trị thu được khi thực hiện,

### 00:06:30.000 - 00:06:33.000
và trạng thái tiếp theo trong bộ nhớ của chúng ta.

### 00:06:35.000 - 00:06:39.000
Và trong video tiếp theo, chúng ta sẽ xem cách cập nhật mạng nơ-ron.

### 00:06:39.000 - 00:06:40.000
Tôi sẽ gặp bạn ở đó.

