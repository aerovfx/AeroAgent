## Nội dung

### 00:00:00.000 - 00:00:05.000
Trong video này, chúng ta sẽ bắt đầu triển khai thuật toán q-learning sâu.

### 00:00:06.000 - 00:00:12.000
Điều đầu tiên chúng ta sẽ làm là tạo hàm gọi là deep q-learning.

### 00:00:16.000 - 00:00:20.000
Và chức năng này sẽ truyền các tham số sau.

### 00:00:21.000 - 00:00:25.000
Đầu tiên là mạng nơ-ron sẽ ước tính các giá trị Q.

### 00:00:27.000 - 00:00:30.000
Thứ hai là chính sách thăm dò.

### 00:00:33.000 - 00:00:38.000
Tham số thứ ba là số tập mà chúng tôi muốn thực hiện.

### 00:00:41.000 - 00:00:43.000
Người thứ tư là Alpha.

### 00:00:43.000 - 00:00:51.000
Tốc độ học mà chúng tôi sẽ sử dụng để cập nhật các tham số mạng thần kinh và chúng tôi sẽ khởi tạo giá trị này

### 00:00:51.000 - 00:00:54.000
dưới dạng không dấu phẩy không một.

### 00:00:56.000 - 00:01:03.000
Đối số tiếp theo là kích thước của các lô sẽ lấy mẫu từ bộ nhớ phát lại để thực hiện

### 00:01:03.000 - 00:01:05.000
cập nhật mạng lưới thần kinh.

### 00:01:05.000 - 00:01:09.000
Và chúng ta sẽ cung cấp giá trị cho tham số này.

### 00:01:09.000 - 00:01:09.000
32.

### 00:01:11.000 - 00:01:18.000
Đối số tiếp theo là Gamma, như bạn đã biết, là hệ số chiết khấu để chiết khấu các phần thưởng trong tương lai.

### 00:01:18.000 - 00:01:25.000
Và cái cuối cùng là Epsilon, xác suất của chính sách khám phá, chọn một hành động ngẫu nhiên.

### 00:01:37.000 - 00:01:44.000
Và bây giờ chúng ta sẽ khởi tạo đối tượng sẽ thực hiện quy tắc cập nhật các tham số của

### 00:01:44.000 - 00:01:45.000
mạng lưới thần kinh.

### 00:01:48.000 - 00:01:52.000
Đối tượng này là một thể hiện của lớp Adam W.

### 00:01:53.000 - 00:01:56.000
Lớp này lấy hai phần tử làm đầu vào.

### 00:01:58.000 - 00:02:04.000
Đầu tiên là danh sách các tham số của mạng nơron mà chúng ta muốn cập nhật.

### 00:02:04.000 - 00:02:07.000
Và giá trị thứ hai là giá trị của tốc độ học tập.

### 00:02:07.000 - 00:02:10.000
Giá trị mà chúng tôi gọi là Alpha.

### 00:02:14.000 - 00:02:18.000
Việc tiếp theo chúng ta cần làm là tạo bộ nhớ phát lại.

### 00:02:19.000 - 00:02:25.000
Và chúng ta sẽ làm điều đó bằng cách tạo một thể hiện của lớp bộ nhớ phát lại.

### 00:02:30.000 - 00:02:37.000
Và sau đó, chúng ta sẽ tạo một từ điển có tên Stats, trong đó chúng ta sẽ lưu trữ

### 00:02:37.000 - 00:02:43.000
số liệu thống kê thực hiện cho thuật toán này và sau đó chúng tôi sẽ vẽ biểu đồ để xem số liệu thống kê bằng đồ họa

### 00:02:44.000 - 00:02:46.000
bên trong từ điển này.

### 00:02:46.000 - 00:02:49.000
Chúng ta sẽ tạo ra hai mục.

### 00:02:49.000 - 00:02:52.000
Điều đầu tiên, chúng ta sẽ gọi đó là sự mất mát.

### 00:02:52.000 - 00:02:58.000
Và trong mục này, chúng ta sẽ lưu trữ từng giá trị của hàm chi phí để tính toán mọi

### 00:02:58.000 - 00:03:03.000
thời gian chúng tôi thực hiện cập nhật các tham số mạng thần kinh.

### 00:03:03.000 - 00:03:09.000
Và mục thứ hai của từ điển này sẽ lưu trữ kết quả quan sát được ở mỗi tập.

### 00:03:13.000 - 00:03:15.000
Bây giờ chúng ta có thể vào vòng lặp chính.

### 00:03:19.000 - 00:03:23.000
Bằng cách viết cho tập trong phạm vi.

### 00:03:24.000 - 00:03:27.000
Từ một đến tập cộng một.

### 00:03:30.000 - 00:03:32.000
Vì vậy, nó bắt đầu đếm từ một.

### 00:03:34.000 - 00:03:38.000
Và đối với vòng lặp for này, chúng ta sẽ áp dụng một sửa đổi nhỏ.

### 00:03:38.000 - 00:03:43.000
Chúng ta sẽ bao bọc phạm vi này bằng hàm tqdm.

### 00:03:45.000 - 00:03:46.000
Chức năng này.

### 00:03:46.000 - 00:03:51.000
Những gì nó sẽ làm là hiển thị bên dưới ô trong quá trình thực hiện thuật toán.

### 00:03:52.000 - 00:03:59.000
Thanh tiến trình sẽ cho chúng ta biết thuật toán đã thực hiện bao nhiêu tập và bao nhiêu tập

### 00:03:59.000 - 00:04:00.000
bên trái.

### 00:04:05.000 - 00:04:06.000
Bên trong vòng lặp.

### 00:04:06.000 - 00:04:11.000
Điều đầu tiên chúng ta sẽ làm, như mọi khi, là thiết lập lại môi trường.

### 00:04:16.000 - 00:04:17.000
Và tạo biến.

### 00:04:17.000 - 00:04:20.000
Don cho nó giá trị sai.

### 00:04:22.000 - 00:04:30.000
Sau đó, chúng ta sẽ tạo một biến có tên là EP return, trong đó chúng ta sẽ tính toán lợi nhuận của mỗi

### 00:04:30.000 - 00:04:31.000
tập.

### 00:04:33.000 - 00:04:35.000
Hãy khởi tạo nó bằng 0.

### 00:04:37.000 - 00:04:41.000
Và bây giờ chúng ta sẽ nhập một vòng lặp bên trong mà chúng ta sẽ thực hiện.

### 00:04:41.000 - 00:04:44.000
Tại mỗi thời điểm trong tập phim.

### 00:04:47.000 - 00:04:50.000
Chúng tôi làm điều đó bằng cách viết trong khi chưa hoàn thành.

### 00:04:51.000 - 00:04:57.000
Trong khi nhiệm vụ được thực hiện và bên trong vòng lặp bên trong này, điều đầu tiên chúng ta sẽ làm là chọn một hành động.

### 00:04:58.000 - 00:05:05.000
Chúng tôi sẽ gọi chính sách khám phá, lấy trạng thái hiện tại và epsilon làm đầu vào.

### 00:05:10.000 - 00:05:15.000
Và sau đó chúng ta sẽ thực hiện hành động này trong môi trường để có được trạng thái tiếp theo.

### 00:05:16.000 - 00:05:18.000
Và cả phần thưởng nữa.

### 00:05:18.000 - 00:05:24.000
Giá trị tiếp theo cho done và từ điển trống mà chúng ta không cần trong trường hợp này.

### 00:05:27.000 - 00:05:28.000
Được rồi.

### 00:05:29.000 - 00:05:33.000
Việc tiếp theo chúng ta cần làm là lưu trữ vào bộ nhớ phát lại.

### 00:05:35.000 - 00:05:42.000
Một danh sách có quá trình chuyển đổi trạng thái, bao gồm cả trạng thái mà chúng ta đã ở trước khi thực hiện hành động.

### 00:05:42.000 - 00:05:44.000
Hành động được thực hiện.

### 00:05:44.000 - 00:05:47.000
Kết quả là phần thưởng thu được.

### 00:05:49.000 - 00:05:55.000
Và giá trị mới cho done cũng như trạng thái tiếp theo mà chúng ta đạt được sau khi thực hiện hành động.

### 00:05:56.000 - 00:06:01.000
Trong video tiếp theo, chúng ta sẽ xem cách cập nhật mạng nơ-ron theo thuật toán

### 00:06:02.000 - 00:06:02.000
quy tắc cập nhật.

### 00:06:03.000 - 00:06:04.000
Tôi sẽ gặp bạn ở đó.

