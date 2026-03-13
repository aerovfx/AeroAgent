## Nội dung

### 00:00:01.000 - 00:00:06.000
Trong video này, chúng ta sẽ bắt đầu triển khai thuật toán tìm kiếm sâu, như bạn đã biết,

### 00:00:06.000 - 00:00:11.000
kết hợp phương pháp khác biệt thời gian với mạng lưới thần kinh.

### 00:00:11.000 - 00:00:17.000
Nhưng trước tiên, như mọi khi, hãy nhập các thư viện mã mà chúng ta sẽ sử dụng để triển khai nó.

### 00:00:18.000 - 00:00:21.000
Cái đầu tiên được gọi là ngẫu nhiên và cho phép chúng ta làm việc.

### 00:00:22.000 - 00:00:28.000
Với các số ngẫu nhiên, chúng ta sẽ sử dụng nó để chọn ngẫu nhiên các phần tử từ danh sách.

### 00:00:30.000 - 00:00:35.000
Thư viện tiếp theo có tên là Copy và nó sẽ cho phép chúng ta sao chép các đối tượng.

### 00:00:38.000 - 00:00:44.000
Cái thứ ba là thư viện phòng tập, như bạn biết, sẽ cho phép chúng ta tạo giao diện để điều khiển

### 00:00:44.000 - 00:00:45.000
nhiệm vụ.

### 00:00:49.000 - 00:00:52.000
Thư viện thứ tư được gọi là PyTorch.

### 00:00:54.000 - 00:00:58.000
Và nó sẽ cho phép chúng ta làm việc với mạng lưới thần kinh.

### 00:01:02.000 - 00:01:04.000
Bên trong PyTorch.

### 00:01:04.000 - 00:01:07.000
Chúng tôi sẽ nhập mô-đun chức năng.

### 00:01:09.000 - 00:01:11.000
Chúng tôi sẽ nhập nó dưới dạng F.

### 00:01:11.000 - 00:01:17.000
Mô-đun này sẽ cho phép chúng ta áp dụng một số chức năng mà chúng ta sẽ cần trong quá trình học tập.

### 00:01:20.000 - 00:01:23.000
Ngoài ra, chúng tôi sẽ nhập thư viện Matplotlib.

### 00:01:26.000 - 00:01:29.000
Như bạn biết, cho phép chúng tôi vẽ dữ liệu.

### 00:01:35.000 - 00:01:36.000
Bây giờ từ PyTorch.

### 00:01:36.000 - 00:01:40.000
Chúng tôi sẽ nhập mô-đun N.

### 00:01:43.000 - 00:01:47.000
Điều đó sẽ cho phép chúng ta truy cập vào các lớp chính mà chúng ta sẽ sử dụng.

### 00:01:47.000 - 00:01:49.000
Làm việc với mạng lưới thần kinh.

### 00:01:52.000 - 00:01:55.000
Cũng từ bên trong PyTorch, chúng tôi sẽ nhập.

### 00:01:59.000 - 00:02:01.000
Lớp Adam W.

### 00:02:02.000 - 00:02:11.000
Lớp này chỉ đơn giản là một sửa đổi của quy tắc cập nhật giảm độ dốc ngẫu nhiên mà chúng ta đã thấy.

### 00:02:12.000 - 00:02:16.000
Nhưng với một số sửa đổi sẽ làm cho nó hiệu quả hơn.

### 00:02:17.000 - 00:02:20.000
Chúng ta sẽ bỏ qua phần giải thích những sửa đổi đó là gì.

### 00:02:21.000 - 00:02:25.000
Bởi vì điều đó không liên quan trực tiếp đến việc học tăng cường.

### 00:02:26.000 - 00:02:31.000
Nhưng nếu bạn muốn tìm hiểu thêm về nó, bạn có thể truy cập tài liệu PyTorch.

### 00:02:33.000 - 00:02:38.000
Thứ tiếp theo chúng ta sẽ nhập là một thư viện có tên Tqdm.

### 00:02:41.000 - 00:02:47.000
Làm việc với mạng nơ-ron, Quá trình học thường mất nhiều thời gian hơn làm việc với mạng dạng bảng

### 00:02:47.000 - 00:02:48.000
phương pháp.

### 00:02:49.000 - 00:02:56.000
Thư viện này sẽ cho phép chúng tôi có một thanh tiến trình cho chúng tôi biết còn lại bao nhiêu thời gian cho việc học

### 00:02:56.000 - 00:02:57.000
quá trình để kết thúc.

### 00:02:58.000 - 00:03:02.000
Cũng từ tệp cục bộ, chúng tôi sẽ nhập một số hàm.

### 00:03:04.000 - 00:03:07.000
Cái đầu tiên được gọi là chi phí cốt truyện để đi.

### 00:03:10.000 - 00:03:13.000
Cái thứ hai có tên là Plot Max Q.

### 00:03:15.000 - 00:03:16.000
Và cái thứ ba?

### 00:03:16.000 - 00:03:18.000
Bạn đã biết điều đó rồi.

### 00:03:20.000 - 00:03:23.000
Cái thứ tư được gọi là số liệu thống kê cốt truyện.

### 00:03:24.000 - 00:03:26.000
Và cái cuối cùng được gọi là hạt giống.

### 00:03:26.000 - 00:03:27.000
Mọi thứ.

### 00:03:30.000 - 00:03:33.000
Chúng tôi sẽ giải thích chức năng của từng chức năng này khi chúng tôi sử dụng chúng.

### 00:03:37.000 - 00:03:42.000
Bây giờ chúng ta sẽ chạy một lệnh có tên Matplotlib Notebook.

### 00:03:43.000 - 00:03:46.000
Điều đó sẽ cho phép chúng tôi làm việc với các ô tương tác.

### 00:03:48.000 - 00:03:51.000
Khi đã có nó, chúng ta sẽ chạy ô này.

### 00:03:51.000 - 00:03:54.000
Và những thư viện mà chúng ta cần sẽ có sẵn.

### 00:03:55.000 - 00:03:56.000
Kế tiếp.

### 00:03:56.000 - 00:03:59.000
Như mọi khi, chúng ta cần tạo ra môi trường.

### 00:03:59.000 - 00:04:03.000
Trong trường hợp này, chúng tôi cũng sẽ làm việc với môi trường ô tô leo núi.

### 00:04:05.000 - 00:04:08.000
Vì thế chúng tôi viết Xe leo núi.

### 00:04:10.000 - 00:04:11.000
Phiên bản số không.

### 00:04:14.000 - 00:04:20.000
Như bạn đã biết, nhiệm vụ này bao gồm một chiếc ô tô bị mắc kẹt giữa hai con dốc và nó cần phải đạt được

### 00:04:20.000 - 00:04:25.000
lá cờ ở trên đỉnh dốc bên phải nó.

### 00:04:29.000 - 00:04:30.000
Được rồi.

### 00:04:30.000 - 00:04:34.000
Sau khi có được môi trường của mình, chúng ta sẽ sử dụng một trong những hàm mà chúng ta đã thấy trước đây.

### 00:04:34.000 - 00:04:41.000
Cụ thể, chúng ta sẽ sử dụng chức năng mọi thứ của hạt giống và chúng ta sẽ cung cấp cho nó môi trường.

### 00:04:42.000 - 00:04:44.000
Nhưng chức năng này làm gì?

### 00:04:44.000 - 00:04:52.000
Chà, nhiều thư viện cần sử dụng một số loại hành vi ngẫu nhiên và để làm được điều đó, họ sử dụng các số ngẫu nhiên.

### 00:04:52.000 - 00:04:59.000
Ví dụ: thư viện phòng tập thể dục trong nhiều môi trường khởi tạo tác vụ ở trạng thái ngẫu nhiên và điều đó

### 00:04:59.000 - 00:05:03.000
trạng thái ngẫu nhiên ban đầu có được bằng cách sử dụng số ngẫu nhiên.

### 00:05:03.000 - 00:05:09.000
Với chức năng này, chúng tôi đảm bảo rằng các số ngẫu nhiên được tạo bởi tất cả các thư viện mà chúng tôi đang sử dụng

### 00:05:09.000 - 00:05:14.000
sẽ sử dụng trong ví dụ này giống nhau mỗi khi chúng ta chạy Notebook.

### 00:05:14.000 - 00:05:19.000
Bằng cách đó, nếu bạn đang làm việc ở nhà, bạn sẽ có thể so sánh kết quả của mình với kết quả của tôi.

### 00:05:20.000 - 00:05:21.000
Hãy chạy tế bào này.

### 00:05:22.000 - 00:05:28.000
Và điều tiếp theo chúng ta sẽ làm là quan sát số chiều trong không gian trạng thái.

### 00:05:29.000 - 00:05:32.000
Và sau đó tôi sẽ đến các phe phái mà chúng tôi có sẵn.

### 00:05:34.000 - 00:05:37.000
Để làm được điều đó, chúng tôi tạo một biến gọi là dims.

### 00:05:38.000 - 00:05:41.000
Và sau đó chúng tôi sẽ lấy số thứ nguyên.

### 00:05:45.000 - 00:05:49.000
Từ không gian quan sát của đối tượng môi trường.

### 00:05:51.000 - 00:05:57.000
Không gian quan sát có một thuộc tính gọi là hình dạng nơi chúng ta có thể nhìn thấy.

### 00:05:57.000 - 00:06:03.000
Chà, hình dạng của các trạng thái và hình dạng đó sẽ được biểu thị bằng một bộ dữ liệu.

### 00:06:03.000 - 00:06:09.000
Trong trường hợp môi trường này, phần tử đầu tiên của bộ dữ liệu đó sẽ là số thứ nguyên.

### 00:06:09.000 - 00:06:14.000
Điều tiếp theo chúng ta sẽ làm là xác định một biến số cho số lượng hành động.

### 00:06:14.000 - 00:06:21.000
Và chúng ta biết rằng số lượng hành động được lưu trữ trong không gian hành động của đối tượng môi trường trong một

### 00:06:21.000 - 00:06:23.000
thuộc tính có tên N.

### 00:06:23.000 - 00:06:27.000
Và bây giờ hãy in hai giá trị này lên màn hình.

### 00:06:59.000 - 00:07:00.000
Hãy chạy tế bào này.

### 00:07:03.000 - 00:07:08.000
Và đúng như chúng ta mong đợi, không gian trạng thái có hai chiều.

### 00:07:08.000 - 00:07:11.000
Đầu tiên là vị trí của ô tô trên trục ngang.

### 00:07:12.000 - 00:07:15.000
Và cái thứ hai là vận tốc.

### 00:07:18.000 - 00:07:21.000
Và tác nhân có sẵn ba hành động.

### 00:07:21.000 - 00:07:23.000
Hành động số 0 sẽ di chuyển xe lùi lại.

### 00:07:24.000 - 00:07:26.000
Hành động một không làm gì cả.

### 00:07:26.000 - 00:07:27.000
Và hành động.

### 00:07:27.000 - 00:07:29.000
Hai người di chuyển xe sang phải.

### 00:07:31.000 - 00:07:37.000
Trong video tiếp theo, chúng ta sẽ sửa đổi môi trường để nó cho phép chúng ta làm việc dễ dàng với PyTorch

### 00:07:37.000 - 00:07:38.000
thư viện.

