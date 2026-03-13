## Nội dung

### 00:00:00.000 - 00:00:04.000
Trong phần này, chúng ta sẽ tìm hiểu về một nhóm thuật toán hoàn toàn mới.

### 00:00:04.000 - 00:00:07.000
Chúng được gọi là phương pháp gradient chính sách.

### 00:00:07.000 - 00:00:12.000
Cho đến nay, tất cả các thuật toán mà chúng ta đã học đều dựa trên ước tính giá trị Q.

### 00:00:13.000 - 00:00:19.000
Họ thuật toán đầu tiên mà chúng tôi biết sử dụng các bảng giá trị trong đó giá trị Q ước tính của mỗi

### 00:00:19.000 - 00:00:22.000
cặp trạng thái và hành động được lưu trữ độc lập.

### 00:00:23.000 - 00:00:29.000
Nhưng những phương pháp này, như chúng ta đã thấy, gặp khó khăn khi giải quyết các nhiệm vụ phức tạp khi số lượng trạng thái

### 00:00:29.000 - 00:00:30.000
là lớn.

### 00:00:31.000 - 00:00:37.000
Để làm cho các thuật toán cổ điển này trở nên linh hoạt và mạnh mẽ hơn, chúng tôi kết hợp chúng với một công cụ gọi là hàm

### 00:00:37.000 - 00:00:38.000
các máy xấp xỉ.

### 00:00:38.000 - 00:00:46.000
Thay vì giữ ước tính độc lập cho từng giá trị Q, chúng tôi duy trì một hàm có hình dạng mà chúng tôi đã sửa đổi

### 00:00:46.000 - 00:00:51.000
trong quá trình học để ước lượng giá trị Q một cách chính xác nhất có thể.

### 00:00:51.000 - 00:00:55.000
Tuy nhiên, hai gia đình này có một điểm chung.

### 00:00:55.000 - 00:01:01.000
Chính sách sẽ tính đến các giá trị Q ước tính để thực hiện hành động.

### 00:01:01.000 - 00:01:07.000
Ví dụ: một chính sách tham lam như chính sách bạn thấy ở đây, xem xét giá trị của các hành động có sẵn

### 00:01:07.000 - 00:01:13.000
trong một trạng thái và chọn hành động mà chúng tôi ước tính sẽ tạo ra lợi nhuận cao nhất.

### 00:01:14.000 - 00:01:20.000
Sự khác biệt giữa hai nhóm phương pháp này là trong trường hợp đầu tiên chúng ta tra cứu các giá trị này

### 00:01:20.000 - 00:01:25.000
trong một bảng và ở bảng kia chúng được tạo ra bởi mạng lưới thần kinh.

### 00:01:25.000 - 00:01:30.000
Nói một cách đơn giản, chính sách được xác định dựa trên các giá trị này.

### 00:01:30.000 - 00:01:36.000
Bây giờ chúng tôi sẽ trình bày một nhóm thuật toán hoàn toàn khác được gọi là phương pháp gradient chính sách.

### 00:01:37.000 - 00:01:44.000
Trong đó, chúng ta sẽ sử dụng hàm xấp xỉ không phải để ước tính các giá trị Q mà để ước tính

### 00:01:44.000 - 00:01:48.000
xác suất của chính sách thực hiện từng hành động.

### 00:01:48.000 - 00:01:50.000
Và nó sẽ hoạt động như sau.

### 00:01:50.000 - 00:01:58.000
Chúng ta sẽ có một mạng lưới thần kinh lấy đầu vào là một trạng thái và dựa trên trạng thái đó nó sẽ tạo ra

### 00:01:58.000 - 00:02:03.000
một vectơ xác suất với xác suất thực hiện từng hành động.

### 00:02:04.000 - 00:02:08.000
Tất nhiên, mỗi giá trị này sẽ nằm trong khoảng từ 0 đến 1.

### 00:02:08.000 - 00:02:15.000
Một có nghĩa là hành động đó có xác suất được thực hiện là 100% và tổng tất cả các xác suất đó

### 00:02:15.000 - 00:02:16.000
sẽ là một.

### 00:02:17.000 - 00:02:25.000
Nói cách khác trong các phương pháp gradient chính sách, mạng nơ-ron là chính sách và đây là các phương pháp ngẫu nhiên.

### 00:02:25.000 - 00:02:31.000
chính sách trong đó mỗi hành động sẽ có một xác suất gắn liền với nó.

### 00:02:32.000 - 00:02:35.000
Nhóm thuật toán này sẽ mang lại cho chúng ta những lợi thế nhất định.

### 00:02:35.000 - 00:02:42.000
Đầu tiên là các phương pháp dựa trên giá trị không hiệu quả trong việc biểu diễn các chính sách ngẫu nhiên.

### 00:02:42.000 - 00:02:49.000
Hãy tưởng tượng một trò chơi trong đó tác nhân không có tất cả thông tin cần thiết về nhiệm vụ, chẳng hạn như

### 00:02:49.000 - 00:02:50.000
như bài poker.

### 00:02:50.000 - 00:02:58.000
Trong các trò chơi có thông tin không hoàn hảo, có thể có chính sách tối ưu, ví dụ:

### 00:02:58.000 - 00:03:04.000
một hành động có xác suất 70% và hành động còn lại chỉ có 30% thời gian.

### 00:03:04.000 - 00:03:10.000
Tuy nhiên, các phương pháp dựa trên giá trị phù hợp hơn để làm việc với các chính sách xác định.

### 00:03:10.000 - 00:03:12.000
Đây là hai ví dụ.

### 00:03:12.000 - 00:03:18.000
Đầu tiên là chính sách tham lam luôn chọn hành động có giá trị Q cao nhất.

### 00:03:18.000 - 00:03:21.000
Chính sách này mang tính quyết định.

### 00:03:21.000 - 00:03:27.000
Mặt khác, chúng ta có chính sách tham lam epsilon trong đó tác nhân, thỉnh thoảng với

### 00:03:27.000 - 00:03:31.000
xác suất epsilon, sẽ thực hiện một hành động ngẫu nhiên.

### 00:03:31.000 - 00:03:36.000
Mặc dù chính sách này mang tính ngẫu nhiên nhưng nó có mục đích khám phá môi trường nhiều hơn.

### 00:03:37.000 - 00:03:44.000
Một ưu điểm khác của phương pháp gradient chính sách là với chúng, chính sách thay đổi trơn tru hơn trong quá trình

### 00:03:44.000 - 00:03:47.000
quá trình học tập với các phương pháp dựa trên giá trị.

### 00:03:47.000 - 00:03:54.000
Khi giá trị Q tối đa thay đổi trong một trạng thái từ hành động này sang hành động khác, xác suất thực hiện

### 00:03:54.000 - 00:04:02.000
hành động mới tăng từ 0 lên 100% và điều ngược lại xảy ra với hành động không còn tối ưu.

### 00:04:02.000 - 00:04:08.000
Ngược lại với các phương pháp gradient chính sách, xác suất thực hiện hành động tăng dần

### 00:04:08.000 - 00:04:15.000
nếu hành động trở nên hiệu quả và giảm dần nếu hành động trở nên không hiệu quả

### 00:04:15.000 - 00:04:16.000
Tốt.

