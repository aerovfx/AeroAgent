## Nội dung

### 00:00:00.000 - 00:00:07.000
Trong video này, chúng ta sẽ thấy phần mở rộng của thuật toán SARSA thành các phương pháp n bước được gọi là

### 00:00:07.000 - 00:00:08.000
SARSA bước n.

### 00:00:11.000 - 00:00:19.000
Đây đơn giản là một phiên bản của SARSA sử dụng quá trình khởi động n bước. Nghĩa là, chúng tôi sẽ sử dụng làm mục tiêu cho

### 00:00:19.000 - 00:00:29.000
cập nhật, ước tính lợi nhuận theo n bước, trong đó chúng tôi sẽ có 'n' phần thưởng thực và ước tính

### 00:00:29.000 - 00:00:30.000
những điều sau đây.

### 00:00:32.000 - 00:00:36.000
Đây là quy tắc cập nhật mà chúng tôi sẽ sử dụng để cải thiện ước tính của chúng tôi về giá trị q.

### 00:00:37.000 - 00:00:46.000
Nó trông giống như SARSA, ngoại trừ việc bây giờ chúng ta sẽ sử dụng ước tính n bước làm mục tiêu

### 00:00:46.000 - 00:00:46.000
của sự trở lại.

### 00:00:49.000 - 00:00:54.000
Như trong phiên bản SARSA mà chúng ta đã thấy, thuật toán này sẽ tuân theo quá trình tìm hiểu về chính sách

### 00:00:54.000 - 00:01:01.000
chiến lược và sẽ sử dụng chính sách tham lam epsilon mà đôi khi sẽ chọn một hành động ngẫu nhiên.

### 00:01:02.000 - 00:01:04.000
Mỗi lần chúng ta phải chọn một hành động, chúng ta sẽ tung một đồng xu.

### 00:01:05.000 - 00:01:12.000
Và với xác suất epsilon chúng ta sẽ chọn một hành động ngẫu nhiên và với xác suất một trừ epsilon chúng ta sẽ

### 00:01:12.000 - 00:01:16.000
chọn hành động có giá trị ước tính cao nhất.

### 00:01:18.000 - 00:01:19.000
Đây là thuật toán hoàn chỉnh.

### 00:01:21.000 - 00:01:26.000
Nó khá giống với SARSA, nhưng chúng tôi buộc phải thực hiện một số thay đổi để phù hợp với việc sử dụng n bước

### 00:01:26.000 - 00:01:27.000
trở lại.

### 00:01:27.000 - 00:01:33.000
Điều đầu tiên chúng ta sẽ làm, như mọi khi, là khởi tạo chính sách và bảng giá trị.

### 00:01:34.000 - 00:01:42.000
Sau đó, chúng ta sẽ vào vòng lặp chính, bắt đầu tập, chọn một hành động cho trạng thái ban đầu đó và

### 00:01:42.000 - 00:01:51.000
sau đó chúng ta sẽ vào vòng lặp bên trong, chúng ta sẽ chạy t+n lần cho đến khi cập nhật xong tất cả các trạng thái.

### 00:01:53.000 - 00:01:54.000
Trong mỗi lần lặp

### 00:01:54.000 - 00:01:58.000
nếu nhiệm vụ chưa kết thúc, chúng tôi sẽ thực hiện hành động

### 00:01:59.000 - 00:02:08.000
và quan sát phần thưởng cũng như trạng thái tiếp theo đạt được, sau đó đối với trạng thái mới, chúng ta sẽ chọn một hành động khác.

### 00:02:09.000 - 00:02:17.000
Sau đó, nếu chúng ta có đủ quan sát để tính toán lợi nhuận n bước, chúng ta sẽ tính toán nó và sử dụng nó để

### 00:02:17.000 - 00:02:18.000
cập nhật các giá trị q.

### 00:02:20.000 - 00:02:29.000
B này ở đây là giá trị bootstrap. Nếu sau 'n' bước mà tập phim vẫn chưa hoàn thành, giá trị bootstrap

### 00:02:29.000 - 00:02:34.000
sẽ là giá trị q của trạng thái đó và hành động được chọn ở trạng thái đó.

### 00:02:34.000 - 00:02:41.000
Ngược lại, nó sẽ là 0 vì nếu tập đã kết thúc thì chúng ta sẽ không nhận được thêm bất kỳ thông tin nào nữa.

### 00:02:41.000 - 00:02:42.000
phần thưởng.

### 00:02:44.000 - 00:02:51.000
Khi quá trình kết thúc, chúng ta sẽ có chính sách gần tối ưu và giá trị q gần tối ưu. Như bạn đã biết, gần

### 00:02:51.000 - 00:02:57.000
tối ưu, vì chính sách của chúng tôi cũng chịu trách nhiệm khám phá môi trường

### 00:02:57.000 - 00:03:00.000
và đôi khi nó sẽ chọn một hành động ngẫu nhiên.

