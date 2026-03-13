## Nội dung

### 00:00:00.000 - 00:00:06.000
Trong video này, chúng ta sẽ kết hợp kỹ thuật mã hóa ô với thuật toán RSA để giải quyết vấn đề

### 00:00:06.000 - 00:00:08.000
nhiệm vụ điều khiển xe leo núi.

### 00:00:08.000 - 00:00:14.000
Điều đầu tiên chúng ta sẽ làm là so sánh không gian trạng thái của môi trường đã sửa đổi với

### 00:00:14.000 - 00:00:16.000
bản gốc.

### 00:00:16.000 - 00:00:18.000
Hãy thực thi hai ô này.

### 00:00:20.000 - 00:00:26.000
Và ở đây bạn có thể thấy rằng sau khi sửa đổi môi trường, các trạng thái mà chúng ta sẽ làm việc sẽ có

### 00:00:26.000 - 00:00:27.000
hình thức này.

### 00:00:30.000 - 00:00:33.000
Chúng là một danh sách có bốn cặp chỉ số.

### 00:00:35.000 - 00:00:42.000
Trong đó mỗi cặp chỉ số chứa một giá trị về vị trí của ô tô và vận tốc của nó.

### 00:00:42.000 - 00:00:49.000
Và chúng tôi thu được những giá trị này thông qua việc tổng hợp trạng thái mà chúng tôi đã áp dụng trong thuật toán mã hóa khối ảnh.

### 00:00:49.000 - 00:00:55.000
Mặt khác, trong môi trường ban đầu, như bạn đã biết, trạng thái được biểu thị bằng hai số thập phân

### 00:00:55.000 - 00:00:56.000
các giá trị.

### 00:00:58.000 - 00:01:02.000
Điều tiếp theo chúng ta sẽ làm là tạo bảng giá trị Q.

### 00:01:02.000 - 00:01:09.000
Như bạn đã biết, trước đây, chúng tôi sử dụng bảng 20 x 20 x 3, nhưng bây giờ chúng tôi sẽ thêm vào đó một bảng khác.

### 00:01:09.000 - 00:01:17.000
thứ nguyên ở đầu bằng giá trị bốn để chúng ta có số mục nhập gấp bốn lần

### 00:01:17.000 - 00:01:21.000
trước đây chúng tôi đã có một cái cho mỗi tập hợp tiểu bang.

### 00:01:26.000 - 00:01:27.000
Hãy thực thi ô này.

### 00:01:27.000 - 00:01:29.000
Và bây giờ chúng ta có bàn của mình.

### 00:01:31.000 - 00:01:34.000
Việc tiếp theo chúng ta cần làm là tạo chính sách.

### 00:01:37.000 - 00:01:38.000
Giống như chúng ta đã làm trước đây.

### 00:01:38.000 - 00:01:43.000
Chúng tôi sẽ sử dụng chính sách tham lam của epsilon để đảm bảo việc khám phá môi trường.

### 00:01:44.000 - 00:01:51.000
Hãy xác định hàm chính sách và chuyển cho nó một trạng thái và một giá trị cho epsilon mà theo mặc định sẽ

### 00:01:51.000 - 00:01:53.000
khởi tạo bằng 0.

### 00:01:57.000 - 00:02:00.000
Chúng tôi sẽ trích xuất một số ngẫu nhiên.

### 00:02:03.000 - 00:02:07.000
Và nếu con số đó thấp hơn epsilon.

### 00:02:09.000 - 00:02:11.000
Chúng tôi sẽ thực hiện một hành động ngẫu nhiên.

### 00:02:18.000 - 00:02:26.000
Ngược lại, chúng ta sẽ tìm giá trị Q cao nhất cho trạng thái đó theo các tập hợp trạng thái khác nhau.

### 00:02:26.000 - 00:02:28.000
Và chúng ta sẽ tính giá trị trung bình.

### 00:02:30.000 - 00:02:36.000
Và dựa trên mức trung bình đó, chúng ta sẽ chọn hành động có giá trị Q cao nhất.

### 00:02:39.000 - 00:02:44.000
Hãy bắt đầu bằng cách tạo một danh sách các hành động mà chúng ta sẽ gọi là danh sách.

### 00:02:46.000 - 00:02:49.000
Và chúng ta sẽ khởi tạo nó như một danh sách trống.

### 00:02:51.000 - 00:02:57.000
Bây giờ chúng ta sẽ liệt kê từng cặp chỉ số mà trạng thái chứa.

### 00:03:00.000 - 00:03:03.000
Và chúng ta sẽ làm điều đó theo cách sau.

### 00:03:13.000 - 00:03:16.000
Đối với mỗi cặp chỉ số này.

### 00:03:17.000 - 00:03:21.000
Chúng ta sẽ tra cứu giá trị tương ứng của nó trong bảng giá trị.

### 00:03:24.000 - 00:03:26.000
Lập chỉ mục của nhà nước.

### 00:03:26.000 - 00:03:28.000
Tổng hợp mà chúng tôi quan tâm.

### 00:03:31.000 - 00:03:33.000
Và bên trong tập hợp trạng thái đó.

### 00:03:35.000 - 00:03:39.000
Chúng ta sẽ tra cứu các giá trị cho trạng thái đó.

### 00:03:42.000 - 00:03:45.000
Và chúng ta sẽ lưu trữ những giá trị đó vào danh sách.

### 00:03:54.000 - 00:04:00.000
Ở cuối vòng lặp này, chúng ta sẽ có các giá trị cho từng hành động trong mỗi tập hợp.

### 00:04:02.000 - 00:04:08.000
Và bây giờ chúng ta sẽ tìm giá trị trung bình cho mỗi hành động theo từng tập hợp trạng thái.

### 00:04:11.000 - 00:04:14.000
Và chúng tôi làm điều đó bằng cách gọi hàm trung bình.

### 00:04:17.000 - 00:04:19.000
Và chúng ta sẽ truyền cho nó trục 0.

### 00:04:22.000 - 00:04:24.000
Nhưng tại sao chúng ta làm điều đó?

### 00:04:24.000 - 00:04:25.000
Rất đơn giản.

### 00:04:25.000 - 00:04:29.000
Hãy tưởng tượng rằng chúng ta có hai mảng với các giá trị hành động.

### 00:04:29.000 - 00:04:31.000
Cái đầu tiên có các giá trị.

### 00:04:31.000 - 00:04:32.000
Một, hai, ba.

### 00:04:35.000 - 00:04:37.000
Và cái thứ hai với các giá trị.

### 00:04:37.000 - 00:04:38.000
Bốn, năm, sáu.

### 00:04:45.000 - 00:04:52.000
Sau đó, nếu chúng ta không chuyển bất kỳ đối số trục nào khi gọi hàm trung bình, nó sẽ tìm giá trị trung bình trong số

### 00:04:52.000 - 00:04:53.000
tất cả những giá trị này.

### 00:04:53.000 - 00:04:59.000
Nhưng đối với chúng tôi, điều chúng tôi muốn làm là tìm giá trị trung bình của các giá trị Q của từng hành động riêng biệt.

### 00:05:04.000 - 00:05:05.000
Và vì hàng triệu lý do đó.

### 00:05:05.000 - 00:05:08.000
Chúng tôi muốn kết thúc với một mảng gồm ba phần tử.

### 00:05:11.000 - 00:05:17.000
Phần tử đầu tiên có giá trị hai rưỡi, là giá trị trung bình từ 4 đến 1.

### 00:05:17.000 - 00:05:22.000
Phần tử thứ hai có giá trị ba rưỡi, là giá trị trung bình từ 2 đến 5.

### 00:05:25.000 - 00:05:31.000
Và phần tử thứ ba có giá trị 4,5, là giá trị trung bình giữa 6 và 3.

### 00:05:33.000 - 00:05:41.000
Chà, theo cách tương tự, chúng ta muốn tính toán một danh sách có giá trị trung bình cho mỗi hành động cho

### 00:05:41.000 - 00:05:44.000
rằng hàng triệu lý do chúng ta vượt qua trục bằng đối số bằng 0.

### 00:05:46.000 - 00:05:48.000
Và bây giờ chúng tôi làm những gì chúng tôi đã làm rất nhiều lần.

### 00:05:51.000 - 00:05:53.000
Không có sự lựa chọn ngẫu nhiên.

### 00:05:55.000 - 00:05:57.000
NumPy làm phẳng bằng không.

### 00:06:00.000 - 00:06:03.000
AV bằng nhau.

### 00:06:03.000 - 00:06:04.000
AV tối đa.

### 00:06:06.000 - 00:06:06.000
Sẵn sàng.

### 00:06:09.000 - 00:06:15.000
Và với điều này, chúng tôi có một chính sách sử dụng giá trị trung bình của Q để chọn hành động của nó.

### 00:06:16.000 - 00:06:18.000
Hãy thực thi ô này.

### 00:06:19.000 - 00:06:21.000
Và chúng tôi có sẵn nó.

### 00:06:21.000 - 00:06:24.000
Bây giờ hãy thực hiện phương thức.

### 00:06:25.000 - 00:06:30.000
Nhưng chúng ta phải sửa đổi nó một chút để nó hoạt động với bảng giá trị Q mới của chúng ta.

### 00:06:34.000 - 00:06:37.000
Cụ thể là khi chúng ta thực hiện quy tắc cập nhật.

### 00:06:39.000 - 00:06:44.000
Chúng tôi sẽ cập nhật từng tập hợp trạng thái một cách độc lập.

### 00:06:50.000 - 00:06:57.000
Chúng ta sẽ sử dụng phương thức zip để chọn cặp chỉ mục đầu tiên của trạng thái hiện tại và cặp chỉ số đầu tiên của trạng thái hiện tại.

### 00:06:57.000 - 00:06:59.000
chỉ số từ trạng thái tiếp theo.

### 00:07:00.000 - 00:07:04.000
Và chúng tôi sẽ cập nhật tập hợp trạng thái đầu tiên theo chúng.

### 00:07:04.000 - 00:07:09.000
Sau đó, chúng tôi sẽ chọn cặp chỉ mục thứ hai để cập nhật tập hợp thứ hai, v.v.

### 00:07:09.000 - 00:07:10.000
ra.

### 00:07:12.000 - 00:07:14.000
Đó là sự thay đổi duy nhất sẽ làm.

### 00:07:15.000 - 00:07:17.000
Vì vậy bây giờ chúng ta hãy thực thi ô.

### 00:07:20.000 - 00:07:23.000
Và bây giờ chúng tôi đã sẵn sàng để thực hiện thuật toán của mình.

### 00:07:25.000 - 00:07:25.000
Đi thôi.

### 00:07:28.000 - 00:07:31.000
Như bạn có thể thấy, việc này sẽ mất vài phút.

### 00:07:31.000 - 00:07:32.000
Tôi sẽ gặp bạn khi nó xong việc.

