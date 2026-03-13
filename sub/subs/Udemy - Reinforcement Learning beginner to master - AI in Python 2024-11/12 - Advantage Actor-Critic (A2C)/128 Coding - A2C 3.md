## Nội dung

### 00:00:00.000 - 00:00:06.000
Trong video này, chúng ta sẽ xem phần đầu tiên của thuật toán Advantage Actor-Critic.

### 00:00:08.000 - 00:00:12.000
Trong phần này, chúng ta sẽ khởi tạo mạng lưới thần kinh và viết vòng lặp bên trong.

### 00:00:14.000 - 00:00:18.000
Hãy tạo một hàm gọi là phê bình diễn viên.

### 00:00:19.000 - 00:00:21.000
Và chúng ta sẽ truyền cho nó một số tham số.

### 00:00:24.000 - 00:00:25.000
Đầu tiên sẽ là chính sách.

### 00:00:27.000 - 00:00:33.000
Mạng thứ hai sẽ là mạng giá trị, mạng ước tính giá trị của các trạng thái.

### 00:00:34.000 - 00:00:37.000
Sau đó chúng ta sẽ chuyển qua một số tập,

### 00:00:39.000 - 00:00:41.000
một giá trị cho alpha, tốc độ học tập

### 00:00:43.000 - 00:00:46.000
mà chúng ta sẽ khởi tạo là 1e-4.

### 00:00:48.000 - 00:00:51.000
và gamma giá trị, là hệ số chiết khấu.

### 00:00:53.000 - 00:01:01.000
Bây giờ, bên trong thuật toán, chúng ta sẽ tạo các đối tượng sẽ thực hiện cập nhật cho từng mạng nơ-ron.

### 00:01:05.000 - 00:01:12.000
Hãy tạo một biến gọi là chính sách tối ưu và với biến này, chúng ta sẽ gán một đối tượng của AdamW

### 00:01:12.000 - 00:01:14.000
lớp học.

### 00:01:16.000 - 00:01:20.000
Chúng tôi sẽ đưa nó làm đối số đầu tiên, các tham số của chính sách

### 00:01:22.000 - 00:01:25.000
và như đối số thứ hai, tốc độ học tập.

### 00:01:29.000 - 00:01:35.000
Tiếp theo chúng ta sẽ tạo một đối tượng sẽ cập nhật mạng giá trị.

### 00:01:37.000 - 00:01:39.000
Chúng tôi sẽ gọi đó là chính sách tối ưu

### 00:01:40.000 - 00:01:42.000
và chúng tôi cũng sẽ gán cho biến này

### 00:01:44.000 - 00:01:47.000
một thể hiện của lớp AdamW

### 00:01:48.000 - 00:01:51.000
sẽ lấy các tham số của mạng giá trị làm đầu vào

### 00:01:55.000 - 00:01:56.000
và tốc độ học tập.

### 00:02:00.000 - 00:02:07.000
Tiếp theo, chúng tôi sẽ khởi tạo một từ điển với số liệu thống kê mà chúng tôi sẽ thu thập trong quá trình thực thi

### 00:02:07.000 - 00:02:15.000
của thuật toán và bên trong từ điển thống kê, chúng tôi sẽ giữ một mục nhập cho hàm mất của chính sách,

### 00:02:21.000 - 00:02:25.000
một cái khác cho hàm mất mát của mạng giá trị,

### 00:02:30.000 - 00:02:31.000
và một cái khác

### 00:02:33.000 - 00:02:35.000
để lưu trữ lợi nhuận.

### 00:02:40.000 - 00:02:43.000
Và bây giờ chúng ta đã sẵn sàng để vào vòng lặp chính.

### 00:02:46.000 - 00:02:47.000
Hãy viết:

### 00:02:48.000 - 00:02:49.000
cho tập phim

### 00:02:51.000 - 00:03:01.000
Trong phạm vi một, tối đa các tập + 1 và chúng tôi sẽ gói vòng lặp này bằng chức năng 'tqdm' để chúng tôi có thể theo dõi

### 00:03:01.000 - 00:03:02.000
sự tiến triển của thuật toán.

### 00:03:03.000 - 00:03:07.000
Bên trong vòng lặp chúng ta sẽ khởi tạo môi trường.

### 00:03:12.000 - 00:03:16.000
Và chúng ta cũng sẽ khởi tạo một vector khác tên là done_b

### 00:03:17.000 - 00:03:24.000
điều này sẽ cho chúng ta biết tại từng thời điểm những môi trường đã kết thúc tập phim và

### 00:03:24.000 - 00:03:30.000
những tập phim chưa kết thúc. Chúng ta sẽ tạo vectơ này với hàm 'số không' từ PyTorch

### 00:03:31.000 - 00:03:33.000
và chúng ta sẽ truyền cho nó hình dạng:

### 00:03:34.000 - 00:03:36.000
(num_envs, 1)

### 00:03:36.000 - 00:03:37.000
Và tất nhiên,

### 00:03:42.000 - 00:03:44.000
chúng tôi muốn biến nó thành một vectơ boolean.

### 00:03:52.000 - 00:03:59.000
Tiếp theo, chúng ta phải khởi tạo một vectơ chứa số 0 để lưu trữ kết quả thu được trong mỗi tập

### 00:04:02.000 - 00:04:04.000
và vector này sẽ có hình dạng tương tự

### 00:04:06.000 - 00:04:08.000
dưới dạng vectơ done_b.

### 00:04:11.000 - 00:04:19.000
Và bây giờ chúng ta sẽ khởi tạo một biến mà chúng ta sẽ gọi là 'I' và biến này sẽ giúp chúng ta triển khai gamma này

### 00:04:20.000 - 00:04:21.000
nâng lên 't'

### 00:04:26.000 - 00:04:28.000
Tiếp theo sẽ vào vòng lặp bên trong.

### 00:04:29.000 - 00:04:32.000
Hãy viết, trong khi chưa xong_b.all()

### 00:04:33.000 - 00:04:34.000
Và phương thức all() này

### 00:04:36.000 - 00:04:39.000
sẽ chỉ đúng khi tất cả các tập phim

### 00:04:40.000 - 00:04:41.000
đã hoàn thành.

### 00:04:46.000 - 00:04:50.000
Bên trong vòng lặp bên trong, tại mỗi thời điểm chúng ta sẽ chọn một hành động.

### 00:04:52.000 - 00:04:57.000
Chúng tôi gọi chính sách với trạng thái hiện tại để tạo ra các vectơ xác suất.

### 00:04:59.000 - 00:05:02.000
Và từ mỗi vectơ, chúng ta sẽ sử dụng hàm đa thức.

### 00:05:04.000 - 00:05:07.000
Để chọn một hành động duy nhất dựa trên những xác suất đó.

### 00:05:09.000 - 00:05:15.000
Và chúng ta cần gọi phương thức tách() để đảm bảo rằng tensor này không tham gia vào

### 00:05:15.000 - 00:05:20.000
thuật toán lan truyền ngược mà PyTorch sẽ sử dụng để cập nhật mạng lưới thần kinh.

### 00:05:21.000 - 00:05:27.000
Tiếp theo, chúng ta phải thực hiện hành động đó trong môi trường và thu thập kết quả của nó.

### 00:05:36.000 - 00:05:43.000
Trong video tiếp theo, chúng tôi sẽ sử dụng kinh nghiệm thu thập được để cập nhật chính sách

### 00:05:44.000 - 00:05:45.000
và mạng lưới giá trị.

### 00:05:46.000 - 00:05:47.000
Tôi sẽ gặp bạn trong video tiếp theo.

