## Nội dung

### 00:00:00.000 - 00:00:05.000
Trong video này, chúng ta sẽ chuẩn bị môi trường để làm việc với thư viện PyTorch.

### 00:00:05.000 - 00:00:12.000
Để làm được điều đó, chúng ta sẽ tạo một lớp có tên preprocess env sẽ bao bọc.

### 00:00:12.000 - 00:00:15.000
Điều đó sẽ bao bọc môi trường song song.

### 00:00:17.000 - 00:00:23.000
Và nó sẽ sửa đổi các yếu tố đi vào môi trường và các yếu tố thoát ra khỏi môi trường.

### 00:00:24.000 - 00:00:31.000
Lớp này sẽ kế thừa từ lớp trình bao bọc song song mà chúng ta đã nhập ở trên.

### 00:00:35.000 - 00:00:38.000
Và nó sẽ đảm nhiệm việc áp dụng các thay đổi.

### 00:00:39.000 - 00:00:46.000
Điều đó sẽ mô tả trong trình bao bọc này cho từng môi trường trong lớp môi trường song song.

### 00:00:48.000 - 00:00:55.000
Điều đầu tiên chúng ta sẽ làm là viết phương thức init sẽ đảm nhiệm việc khởi tạo

### 00:00:56.000 - 00:00:59.000
instance của lớp này.

### 00:01:00.000 - 00:01:08.000
Nó sẽ lấy môi trường song song làm đầu vào và nó sẽ chuyển nó làm đối số cho phương thức init của

### 00:01:08.000 - 00:01:09.000
siêu lớp.

### 00:01:19.000 - 00:01:22.000
Vì vậy, lớp này bao bọc môi trường song song.

### 00:01:31.000 - 00:01:32.000
Được rồi.

### 00:01:33.000 - 00:01:39.000
Điều tiếp theo chúng ta sẽ làm là ghi đè các phương thức mà chúng ta sẽ sử dụng để tương tác

### 00:01:39.000 - 00:01:40.000
với môi trường.

### 00:01:41.000 - 00:01:46.000
Như bạn đã biết, những phương pháp này là phương pháp đặt lại và bước.

### 00:01:48.000 - 00:01:53.000
Nhưng vì chúng tôi đang làm việc với nhiều môi trường nên phương pháp bước này.

### 00:01:53.000 - 00:01:55.000
Từ lớp học này.

### 00:01:55.000 - 00:01:57.000
Chúng ta sẽ chia làm hai phần.

### 00:01:59.000 - 00:02:08.000
Cái đầu tiên được gọi là Step Sync sẽ đảm nhiệm việc thực thi các hành động được thực hiện bởi tác nhân trong mỗi

### 00:02:08.000 - 00:02:17.000
các môi trường và phương pháp chờ từng bước sẽ đợi cho đến khi mỗi môi trường xử lý xong

### 00:02:17.000 - 00:02:21.000
hành động để thu thập các phần thưởng đạt được.

### 00:02:21.000 - 00:02:27.000
Trạng thái tiếp theo và tất cả các biến mà tác nhân cần làm việc.

### 00:02:27.000 - 00:02:34.000
Vì vậy, một phương thức bắt đầu tương tác và phương thức còn lại đợi nó kết thúc.

### 00:02:36.000 - 00:02:38.000
Nhưng chúng ta hãy xem nó chi tiết hơn.

### 00:02:38.000 - 00:02:43.000
Điều đầu tiên chúng ta sẽ làm là ghi đè phương thức reset.

### 00:02:47.000 - 00:02:54.000
Và trong đó chúng ta sẽ tìm nạp trạng thái ban đầu của từng môi trường bằng cách gọi phương thức reset.

### 00:02:58.000 - 00:03:02.000
Trên đối tượng V và V được lưu trữ bên trong lớp này.

### 00:03:06.000 - 00:03:14.000
Khi chúng ta khởi tạo trình bao bọc này, siêu lớp sẽ đảm nhiệm việc lưu trữ môi trường song song.

### 00:03:15.000 - 00:03:16.000
Trong tài sản này.

### 00:03:17.000 - 00:03:24.000
Vì vậy, bằng cách gọi phương thức đặt lại trên đối tượng này, chúng ta sẽ đặt lại môi trường song song và tìm nạp

### 00:03:24.000 - 00:03:25.000
quan sát ban đầu.

### 00:03:27.000 - 00:03:30.000
Giống như chúng tôi đã làm ở đây.

### 00:03:33.000 - 00:03:38.000
Bây giờ những gì chúng ta phải làm là chuyển đổi mảng gọn gàng này thành một tenxơ pytorch.

### 00:03:40.000 - 00:03:49.000
Và chúng ta sẽ làm điều đó bằng cách sử dụng hàm từ numpy, như chúng ta đã biết, hàm này sẽ chuyển đổi một mảng có nhiều mảng thành một

### 00:03:49.000 - 00:03:51.000
tenxơ pytorch.

### 00:03:52.000 - 00:04:00.000
Và chúng ta sẽ chuyển cho nó trạng thái cần chuyển đổi và để đảm bảo rằng chúng ta đang làm việc với một tenxơ

### 00:04:00.000 - 00:04:02.000
của các giá trị dấu phẩy động.

### 00:04:02.000 - 00:04:06.000
Chúng ta sẽ gọi phương thức float trên tensor thu được.

### 00:04:07.000 - 00:04:11.000
Và sau khi thực hiện việc này, phương pháp đặt lại đã sẵn sàng.

### 00:04:12.000 - 00:04:15.000
Bây giờ hãy chuẩn bị phương pháp thứ hai.

### 00:04:17.000 - 00:04:18.000
Hãy.

### 00:04:18.000 - 00:04:18.000
Phải.

### 00:04:18.000 - 00:04:20.000
Bước một bồn rửa.

### 00:04:22.000 - 00:04:29.000
Và phương pháp này sẽ lấy đầu vào là các hành động được thực hiện bởi tác nhân đối với từng môi trường.

### 00:04:30.000 - 00:04:39.000
Và trên tensor hành động, chúng ta sẽ gọi phương thức bóp và sau đó gọi là numpy.

### 00:04:40.000 - 00:04:42.000
Chúng ta đang làm gì ở đây?

### 00:04:43.000 - 00:04:49.000
Chà, khi chúng ta làm việc với một số môi trường, các hành động sẽ là một vectơ cột.

### 00:04:50.000 - 00:04:51.000
Điều này có nghĩa là gì?

### 00:04:53.000 - 00:04:56.000
Nó có nghĩa là họ sẽ có hình dạng này.

### 00:05:13.000 - 00:05:20.000
Tuy nhiên, để chuyển các hành động của chúng ta sang môi trường song song, chúng ta cần một vectơ hàng.

### 00:05:21.000 - 00:05:26.000
Và hãy nhớ rằng môi trường song song hoạt động với các mảng có nhiều mảng.

### 00:05:27.000 - 00:05:32.000
Vì vậy chúng ta gọi phương pháp ép để loại bỏ những chiều không cần thiết.

### 00:05:33.000 - 00:05:34.000
Từ tensor.

### 00:05:35.000 - 00:05:36.000
Và sau đó.

### 00:05:38.000 - 00:05:46.000
Chúng tôi gọi phương thức NumPy để chuyển đổi tensor thành một mảng gọn gàng để hoạt động với môi trường.

### 00:05:51.000 - 00:05:54.000
Và bây giờ hành động của chúng ta có hình dạng này.

### 00:05:56.000 - 00:06:04.000
Hãy viết self v và v dot step async và chúng ta chuyển các hành động.

### 00:06:08.000 - 00:06:14.000
Hãy nhớ rằng B và B là môi trường song song được lưu trữ trong lớp này.

### 00:06:17.000 - 00:06:20.000
Và bây giờ việc thực hiện phương pháp này của chúng ta đã kết thúc.

### 00:06:22.000 - 00:06:29.000
Điều tiếp theo chúng ta sẽ làm sau khi bắt đầu thực hiện các hành động trong môi trường

### 00:06:30.000 - 00:06:33.000
đang đợi quá trình kết thúc.

### 00:06:36.000 - 00:06:37.000
Vì điều đó.

### 00:06:37.000 - 00:06:44.000
Chúng tôi sẽ sử dụng phương pháp này để chặn việc thực thi thuật toán cho đến khi chúng tôi có các biến kết quả

### 00:06:44.000 - 00:06:47.000
từ môi trường chúng ta viết.

### 00:06:47.000 - 00:06:48.000
Tiểu bang tiếp theo.

### 00:06:49.000 - 00:06:52.000
Thưởng xong.

### 00:06:52.000 - 00:06:53.000
Và thông tin.

### 00:06:54.000 - 00:06:59.000
Và đó sẽ là kết quả của việc gọi phương pháp trọng số bước.

### 00:07:01.000 - 00:07:03.000
Trên môi trường song song.

### 00:07:04.000 - 00:07:08.000
Và bây giờ chúng ta sẽ xử lý từng phần tử này một cách riêng lẻ.

### 00:07:09.000 - 00:07:14.000
Các quan sát sẽ chuẩn bị chúng theo cách tương tự như chúng ta đã làm với phương pháp đặt lại.

### 00:07:15.000 - 00:07:17.000
Chúng tôi ngay vào ngày tiếp theo.

### 00:07:17.000 - 00:07:22.000
Và chúng tôi dán dòng này mà chúng tôi đã sao chép từ phương thức đặt lại.

### 00:07:22.000 - 00:07:24.000
Chúng tôi sửa đổi lập luận này.

### 00:07:30.000 - 00:07:31.000
Và thì đấy.

### 00:07:34.000 - 00:07:41.000
Tiếp theo, chúng ta cần sửa đổi phần thưởng và trước tiên chúng ta sẽ thực hiện điều đó bằng cách chuyển đổi nó thành tensor.

### 00:07:47.000 - 00:07:51.000
Và sau đó bằng cách sử dụng phương pháp Unsqueeze.

### 00:07:52.000 - 00:08:00.000
Trong chiều thứ nhất và cuối cùng là gọi phương thức float để đảm bảo rằng chúng ta đang làm việc với số thập phân

### 00:08:00.000 - 00:08:00.000
những con số.

### 00:08:02.000 - 00:08:03.000
Đây.

### 00:08:03.000 - 00:08:09.000
Những gì chúng tôi đang làm với phương pháp Unsqueeze trái ngược với những gì chúng tôi đã làm ở đây.

### 00:08:11.000 - 00:08:20.000
Phần thưởng là một vectơ hàng được biểu thị bằng một mảng gọn gàng và chúng tôi muốn chuyển đổi nó thành một vectơ cột.

### 00:08:20.000 - 00:08:28.000
Sau đó, chúng ta sẽ xử lý biến Don giống như cách chuyển nó thành tensor.

### 00:08:35.000 - 00:08:39.000
Khi gọi phương thức Unsqueeze trong Thứ nguyên.

### 00:08:42.000 - 00:08:48.000
Vì biến Don chứa các giá trị boolean ở đây nên chúng ta sẽ không gọi phương thức float.

### 00:08:51.000 - 00:08:52.000
Từ môi trường.

### 00:08:52.000 - 00:08:56.000
Chúng tôi sẽ nhận được một mảng có nhiều giá trị boolean.

### 00:08:58.000 - 00:08:58.000
Ví dụ.

### 00:08:58.000 - 00:08:59.000
SAI.

### 00:08:59.000 - 00:09:00.000
ĐÚNG VẬY.

### 00:09:00.000 - 00:09:01.000
SAI.

### 00:09:03.000 - 00:09:10.000
Điều đó cho chúng ta biết tập phim đã kết thúc ở mỗi môi trường hay chưa.

### 00:09:12.000 - 00:09:16.000
Và chúng ta sẽ chuyển đổi mảng có nhiều mảng này thành một vectơ cột.

### 00:09:18.000 - 00:09:19.000
Lối này.

### 00:09:24.000 - 00:09:28.000
Và cuối cùng, chúng ta sẽ trả về những giá trị mà chúng ta đã sửa đổi.

### 00:09:35.000 - 00:09:40.000
Và với rapper này, chúng tôi sẵn sàng làm việc với môi trường song song.

### 00:09:42.000 - 00:09:44.000
Sử dụng thư viện PyTorch.

### 00:09:47.000 - 00:09:48.000
Hãy chạy tế bào này.

### 00:09:48.000 - 00:09:53.000
Và bây giờ hãy áp dụng trình bao bọc này cho môi trường của chúng ta.

### 00:10:01.000 - 00:10:03.000
Chúng tôi gọi env tiền xử lý.

### 00:10:03.000 - 00:10:05.000
Chuyển làm đầu vào cho môi trường.

### 00:10:12.000 - 00:10:13.000
Ối.

### 00:10:13.000 - 00:10:15.000
Có vẻ như chúng ta có một cái hẹp hơn ở đây.

### 00:10:16.000 - 00:10:18.000
Chúng tôi đã quên chữ L.

### 00:10:20.000 - 00:10:21.000
Hãy chạy lại ô này.

### 00:10:22.000 - 00:10:23.000
Và bây giờ chúng tôi có nó.

### 00:10:25.000 - 00:10:27.000
Môi trường song song của chúng tôi.

### 00:10:27.000 - 00:10:30.000
Sẵn sàng làm việc với PyTorch?

### 00:10:31.000 - 00:10:42.000
Bây giờ chúng ta sẽ xem xét các trạng thái, phần thưởng và các biến giả sau khi được xử lý bởi

### 00:10:42.000 - 00:10:44.000
bao bọc môi trường.

### 00:10:44.000 - 00:10:45.000
Và vì điều đó.

### 00:10:47.000 - 00:10:50.000
Chúng ta sẽ viết trạng thái bằng nhau.

### 00:10:51.000 - 00:10:54.000
Đặt lại dấu chấm EMF song song.

### 00:10:56.000 - 00:11:01.000
Và chúng ta cũng sẽ gọi phương thức step để quan sát.

### 00:11:04.000 - 00:11:07.000
Các biến phần thưởng và thực hiện.

### 00:11:10.000 - 00:11:14.000
Vì chúng tôi đang làm việc với một môi trường song song.

### 00:11:15.000 - 00:11:17.000
Chúng ta phải vượt qua phương pháp này.

### 00:11:17.000 - 00:11:22.000
Một vectơ cột chứa các hành động mà tổng đài viên sẽ thực hiện.

### 00:11:23.000 - 00:11:26.000
Chúng ta sẽ tạo ra một tensor chứa đầy các số 0.

### 00:11:27.000 - 00:11:37.000
Và chúng ta sẽ truyền cho nó các chiều num ams và 1 và chúng ta sẽ đảm bảo rằng tensor này chứa số nguyên

### 00:11:37.000 - 00:11:38.000
những con số.

### 00:11:46.000 - 00:11:47.000
Được rồi.

### 00:11:51.000 - 00:11:59.000
Và bây giờ chúng ta sẽ gọi lệnh in và hiển thị giá trị của từng phần tử này.

### 00:12:01.000 - 00:12:01.000
Tình trạng.

### 00:12:05.000 - 00:12:06.000
Phần thưởng

### 00:12:08.000 - 00:12:10.000
và xong.

### 00:12:13.000 - 00:12:15.000
Được rồi, hãy chạy lệnh này.

### 00:12:15.000 - 00:12:18.000
Và ở đây chúng tôi có nó.

### 00:12:18.000 - 00:12:21.000
Các tiểu bang sẽ giống như những gì chúng ta đã thấy trước đây.

### 00:12:23.000 - 00:12:29.000
Một vectơ cột có các trạng thái riêng của từng môi trường trong mỗi hàng.

### 00:12:32.000 - 00:12:39.000
Mặc dù tùy thuộc vào máy tính mà bạn đang làm việc, có thể có nhiều hoặc ít môi trường.

### 00:12:45.000 - 00:12:52.000
Phần thưởng sẽ là một vectơ cột với mỗi phần thưởng riêng lẻ ở mỗi hàng.

### 00:12:56.000 - 00:13:02.000
Và điều tương tự cũng xảy ra với các giá trị cho biến được thực hiện trong từng môi trường.

### 00:13:05.000 - 00:13:08.000
Trong video tiếp theo, chúng ta sẽ tạo chính sách của mình.

### 00:13:10.000 - 00:13:11.000
Tôi sẽ gặp bạn ở đó.

