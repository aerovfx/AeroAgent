## Nội dung

### 00:00:00.000 - 00:00:07.000
Trong phần này, chúng ta sẽ triển khai một phương pháp khác thuộc họ gradient chính sách. Trong trường hợp này,

### 00:00:07.000 - 00:00:13.000
thay vì kết hợp họ này với các phương pháp Monte Carlo, chúng ta sẽ kết hợp nó với các phương pháp sai phân thời gian.

### 00:00:14.000 - 00:00:21.000
Thuật toán kết quả sẽ được gọi là Advantage Actor-Critic và trong đó, chúng tôi sẽ sử dụng ước tính về

### 00:00:21.000 - 00:00:26.000
quay lại một bước để cập nhật các tham số của mạng nơ-ron.

### 00:00:26.000 - 00:00:34.000
Ước tính lợi nhuận cho một thời điểm cụ thể bao gồm phần thưởng tiếp theo nhận được, cộng với

### 00:00:34.000 - 00:00:41.000
giá trị chiết khấu của trạng thái đã đạt được, giống như đã làm trong các phương pháp tạm thời khác nhau.

### 00:00:42.000 - 00:00:48.000
Trong video này, chúng ta sẽ tạo một số môi trường song song của tác vụ mà chúng ta sắp thực hiện

### 00:00:48.000 - 00:00:52.000
giải quyết, để có thể tương tác với tất cả chúng cùng một lúc.

### 00:00:53.000 - 00:00:57.000
Điều đầu tiên chúng ta sẽ làm, như mọi khi, là nhập các thư viện mã.

### 00:00:58.000 - 00:01:00.000
Chúng sẽ giống như trong phần trước.

### 00:01:00.000 - 00:01:01.000
Hãy chạy tế bào.

### 00:01:03.000 - 00:01:04.000
Và bây giờ chúng tôi có chúng.

### 00:01:05.000 - 00:01:11.000
Việc tiếp theo chúng ta cần làm là tạo môi trường. Trong trường hợp này, chúng ta sẽ giải quyết vấn đề

### 00:01:11.000 - 00:01:12.000
Nhiệm vụ nhào lộn.

### 00:01:15.000 - 00:01:16.000
phiên bản một.

### 00:01:19.000 - 00:01:22.000
Hãy chạy ô này và ô tiếp theo.

### 00:01:25.000 - 00:01:30.000
Như bạn có thể thấy, tác vụ này có một không gian trạng thái với sáu chiều khác nhau.

### 00:01:32.000 - 00:01:35.000
Và chúng tôi có sẵn ba hành động.

### 00:01:37.000 - 00:01:40.000
Bây giờ chúng ta hãy xem một bản trình bày trực quan của nhiệm vụ.

### 00:01:46.000 - 00:01:48.000
Như bạn thấy, chúng ta có con lắc đôi này

### 00:01:49.000 - 00:01:57.000
chỉ xuống sàn và mục tiêu là di chuyển các khớp của con lắc đôi sao cho đầu của

### 00:01:57.000 - 00:02:00.000
con lắc chạm vào thanh ngang phía trên.

### 00:02:02.000 - 00:02:06.000
Tức là ta phải cân bằng con lắc sang hai bên

### 00:02:07.000 - 00:02:09.000
với mục tiêu thăng tiến.

### 00:02:13.000 - 00:02:20.000
Để làm được điều đó, chúng ta có thể tác dụng mô-men xoắn vào bên trái, không tác dụng bất kỳ mô-men xoắn nào hoặc tác dụng nó sang bên phải.

### 00:02:22.000 - 00:02:24.000
Đó là ba hành động mà chúng tôi có sẵn.

### 00:02:27.000 - 00:02:31.000
Bây giờ chúng ta sẽ tạo một số môi trường song song cho nhiệm vụ này.

### 00:02:33.000 - 00:02:39.000
Để làm được điều đó, trước tiên, chúng ta sẽ chạy ô này để cho chúng ta biết số lượng môi trường song song

### 00:02:40.000 - 00:02:41.000
mà đại lý sẽ phải đối mặt:

### 00:02:42.000 - 00:02:46.000
một cho mỗi lõi của CPU máy tính của bạn

### 00:02:47.000 - 00:02:49.000
giống như chúng ta đã làm ở phần trước.

### 00:02:51.000 - 00:02:58.000
Bây giờ, hãy tạo một phương thức có tên 'create_env' để đảm nhiệm việc tạo từng cá thể

### 00:02:58.000 - 00:02:59.000
môi trường.

### 00:03:00.000 - 00:03:07.000
Chúng ta truyền cho hàm này hai tham số: tên của môi trường và một tham số khác gọi là hạt giống sẽ

### 00:03:07.000 - 00:03:10.000
hãy giúp chúng tôi làm cho cuốn sổ này có thể tái sản xuất được.

### 00:03:12.000 - 00:03:16.000
Và bên trong hàm này, chúng ta sẽ gọi hàm gym.make

### 00:03:18.000 - 00:03:20.000
để tạo ra môi trường.

### 00:03:21.000 - 00:03:29.000
Sau đó, chúng ta sẽ gọi hàm Seed_everything, chuyển môi trường làm đối số và cuối cùng sẽ

### 00:03:29.000 - 00:03:31.000
trả lại môi trường.

### 00:03:35.000 - 00:03:42.000
Tiếp theo, chúng ta cần tạo một danh sách với các hàm mà chúng ta sẽ thực hiện để tạo từng hàm

### 00:03:42.000 - 00:03:42.000
môi trường.

### 00:03:45.000 - 00:03:53.000
Mỗi phần tử trong danh sách này sẽ là một hàm lambda sẽ gọi hàm create_env với

### 00:03:53.000 - 00:03:54.000
tên môi trường

### 00:03:57.000 - 00:03:59.000
và giá trị hạt giống

### 00:04:01.000 - 00:04:05.000
đó sẽ là chỉ mục của môi trường này trong danh sách.

### 00:04:17.000 - 00:04:22.000
Tiếp theo, chúng ta sẽ tạo môi trường song song. Chúng ta sẽ tạo một phiên bản

### 00:04:23.000 - 00:04:31.000
của lớp ParallelEnv, giống như chúng ta đã làm trong phần trước và chúng ta sẽ chuyển nó làm đối số,

### 00:04:31.000 - 00:04:35.000
danh sách các chức năng sẽ được thực thi. Hãy chạy tế bào.

### 00:04:37.000 - 00:04:41.000
Và bây giờ chúng ta có môi trường song song.

### 00:04:42.000 - 00:04:49.000
Tiếp theo, chúng ta cần chuẩn bị môi trường này để làm việc với thư viện PyTorch và chúng ta sẽ thực hiện điều đó với

### 00:04:49.000 - 00:04:53.000
cùng một lớp trình bao bọc mà chúng tôi đã sử dụng trong thuật toán REINFORCE.

### 00:04:54.000 - 00:04:57.000
Vì vậy, những gì chúng tôi đã làm là sao chép nó và dán nó vào đây.

### 00:04:59.000 - 00:05:01.000
Chúng ta cũng hãy chạy hai ô này.

### 00:05:03.000 - 00:05:05.000
Và bây giờ chúng ta có môi trường của chúng ta

### 00:05:06.000 - 00:05:12.000
song song và sẵn sàng làm việc với PyTorch. Trong video tiếp theo, chúng ta sẽ tạo ra các mạng lưới thần kinh có khả năng

### 00:05:12.000 - 00:05:16.000
đại diện cho chính sách và hàm giá trị.

### 00:05:17.000 - 00:05:18.000
Tôi sẽ gặp bạn ở đó.

