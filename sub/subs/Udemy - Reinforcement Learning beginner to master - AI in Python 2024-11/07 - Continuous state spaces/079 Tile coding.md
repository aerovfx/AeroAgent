## Nội dung

### 00:00:00.000 - 00:00:04.000
Trong video này, chúng ta sẽ tìm hiểu kỹ thuật thứ hai cho phép chúng ta làm việc với các

### 00:00:04.000 - 00:00:07.000
không gian trạng thái được gọi là mã hóa khối ảnh.

### 00:00:08.000 - 00:00:10.000
Hãy quay trở lại nhiệm vụ của người chơi gôn.

### 00:00:10.000 - 00:00:17.000
Như bạn đã biết, đây là hàm giá trị tối ưu với phương pháp gộp trạng thái.

### 00:00:17.000 - 00:00:21.000
Chúng tôi nhóm các vị trí hợp lệ thành một tập hợp các trạng thái mà chúng tôi làm việc cùng.

### 00:00:22.000 - 00:00:28.000
Tuy nhiên, khi thực hiện việc này, chúng tôi chấp nhận mất một số độ chính xác vì chúng tôi sử dụng cùng một giá trị ước tính

### 00:00:28.000 - 00:00:31.000
cho tất cả các trạng thái trong một phạm vi giá trị.

### 00:00:31.000 - 00:00:40.000
Ví dụ: ở đây trạng thái tối ưu lớn hơn ước tính và ở đây nhỏ hơn.

### 00:00:41.000 - 00:00:48.000
Trong cả hai trường hợp, thuật toán tổng hợp trạng thái đều tạo ra lỗi rời rạc.

### 00:00:49.000 - 00:00:54.000
Sự mất đi độ chính xác này là một vấn đề mà chúng tôi sẽ giảm thiểu bằng cách sử dụng mã hóa ô.

### 00:00:56.000 - 00:01:03.000
Kỹ thuật này chỉ là sự khái quát hóa của tập hợp trạng thái trong đó chúng ta tạo ra một số lượng độc lập nhất định

### 00:01:03.000 - 00:01:07.000
tập hợp và nó trông như thế này.

### 00:01:08.000 - 00:01:13.000
Chúng tôi thực hiện một số tập hợp trạng thái, mỗi tập hợp có một màu khác nhau.

### 00:01:13.000 - 00:01:18.000
Các tập hợp này độc lập với nhau và tổng hợp các phạm vi giá trị khác nhau.

### 00:01:19.000 - 00:01:21.000
Đối với mỗi tập hợp.

### 00:01:21.000 - 00:01:26.000
Chúng tôi sẽ giữ một bảng giá trị riêng với các ước tính độc lập cho từng giá trị tổng hợp của nó.

### 00:01:27.000 - 00:01:33.000
Ước tính của chúng tôi về giá trị của một trạng thái sẽ là giá trị trung bình của giá trị được lưu trữ trong các giá trị khác nhau đó

### 00:01:33.000 - 00:01:33.000
các bảng.

### 00:01:34.000 - 00:01:43.000
Ví dụ: ước tính của chúng tôi về giá trị của trạng thái này sẽ là giá trị trung bình của ước tính này, ước tính này,

### 00:01:44.000 - 00:01:49.000
chiếc này, và chiếc màu đỏ, sẽ hạ cánh đâu đó quanh đây.

### 00:01:50.000 - 00:01:56.000
Nếu bạn để ý, giá trị trung bình của các ước tính sẽ gần với hàm giá trị thực hơn nhiều và mượt mà hơn.

### 00:01:57.000 - 00:01:58.000
cho hầu hết các bang.

### 00:01:58.000 - 00:02:02.000
Chúng ta có thể mong đợi ước tính của nó sẽ gần với mức tối ưu hơn.

### 00:02:03.000 - 00:02:08.000
Nhưng làm thế nào chúng ta có thể áp dụng kỹ thuật này cho các bài toán có không gian trạng thái phức tạp hơn?

### 00:02:08.000 - 00:02:12.000
Nào chúng ta hãy nhìn qua bài toán xe leo núi nhé.

### 00:02:12.000 - 00:02:17.000
Như bạn đã biết, đây là một nhiệm vụ trong đó trạng thái có hai giá trị, hai chiều.

### 00:02:19.000 - 00:02:23.000
Đầu tiên là vị trí của xe và thứ hai là vận tốc của nó.

### 00:02:25.000 - 00:02:28.000
Đây là không gian trạng thái hai chiều.

### 00:02:30.000 - 00:02:36.000
Như bạn có thể thấy, chúng tôi đã tạo một số lưới tổng hợp các phần khác nhau của không gian trạng thái.

### 00:02:36.000 - 00:02:43.000
Và tất cả các trạng thái theo sau trong cùng một ô trong một tập hợp cụ thể được biểu thị bằng một

### 00:02:43.000 - 00:02:44.000
tình trạng.

### 00:02:45.000 - 00:02:48.000
Vì chúng tôi có một số tập hợp độc lập.

### 00:02:49.000 - 00:02:54.000
Một trạng thái có thể thuộc về các ô khác nhau trong các tập hợp khác nhau.

### 00:02:55.000 - 00:03:04.000
Ví dụ: trạng thái này ở đây thuộc về ô ở hàng thứ hai, cột thứ hai trong tập hợp màu đỏ.

### 00:03:05.000 - 00:03:11.000
Nó cũng thuộc về ô ở hàng thứ hai và cột thứ hai trên ô màu xanh lá cây.

### 00:03:12.000 - 00:03:14.000
Nhưng nó thuộc về ô ở hàng thứ ba.

### 00:03:14.000 - 00:03:17.000
Cột thứ hai trên cột vàng.

### 00:03:19.000 - 00:03:23.000
Để thực hiện kỹ thuật mã hóa ô sẽ làm theo các bước sau.

### 00:03:23.000 - 00:03:30.000
Đầu tiên, chúng ta sẽ tạo một lưới bằng cách chia từng chiều của trạng thái thành các phân đoạn.

### 00:03:30.000 - 00:03:31.000
Như chúng ta thấy ở đây.

### 00:03:33.000 - 00:03:39.000
Sau đó, chúng ta sẽ thay đổi kích thước của lưới, phóng to hoặc thu nhỏ nó theo một hệ số ngẫu nhiên.

### 00:03:40.000 - 00:03:45.000
Điều này sẽ giúp chúng ta tạo ra các tập hợp khác nhau độc lập với nhau.

### 00:03:48.000 - 00:03:56.000
Tiếp theo, chúng ta sẽ sử dụng vectơ dịch chuyển để di chuyển lưới một lượng nhỏ theo từng chiều của trạng thái.

### 00:03:57.000 - 00:04:04.000
Ví dụ: tập hợp trạng thái đã được chuyển sang bên trái một lượng nhất định được mô tả trong

### 00:04:04.000 - 00:04:06.000
phần tử đầu tiên của vectơ.

### 00:04:06.000 - 00:04:13.000
Và theo hướng Y bởi phần tử thứ hai của vectơ dịch chuyển này.

### 00:04:15.000 - 00:04:24.000
Vectơ này chứa các số lẻ từ một đến hai lần số chiều của không gian trạng thái.

### 00:04:24.000 - 00:04:34.000
Ví dụ, trong trường hợp này, vì chúng ta có hai chiều nên vectơ này sẽ chứa một và ba vì

### 00:04:34.000 - 00:04:40.000
gấp đôi số chiều là bốn và vectơ này chỉ chứa các số lẻ.

### 00:04:42.000 - 00:04:48.000
Cuối cùng, chúng ta sẽ lặp lại quá trình này nhiều lần tùy theo số lượng lưới mà chúng ta cần.

### 00:04:48.000 - 00:04:52.000
Mỗi lưới mới mà chúng tôi tạo sẽ lấy lưới cuối cùng làm tham chiếu.

### 00:04:53.000 - 00:05:01.000
Ví dụ: chúng ta sẽ tạo hình màu xanh lá cây bắt đầu từ vị trí của hình màu đỏ, phóng to hoặc thu nhỏ

### 00:05:01.000 - 00:05:07.000
nó rồi di chuyển nó dựa trên vectơ dịch chuyển và sau đó bắt đầu từ vị trí của green

### 00:05:07.000 - 00:05:07.000
một.

### 00:05:07.000 - 00:05:12.000
Chúng ta sẽ tạo hình màu vàng, thay đổi kích thước và di chuyển nó xung quanh.

