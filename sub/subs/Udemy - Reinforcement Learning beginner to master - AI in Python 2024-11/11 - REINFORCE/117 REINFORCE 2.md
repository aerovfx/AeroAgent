## Nội dung

### 00:00:00.000 - 00:00:04.000
Bây giờ chúng ta đã sẵn sàng để phân tích thuật toán củng cố.

### 00:00:04.000 - 00:00:05.000
Đây rồi.

### 00:00:05.000 - 00:00:07.000
Chúng ta hãy xem nó từng phần một.

### 00:00:08.000 - 00:00:14.000
Điều đầu tiên chúng ta sẽ làm là tạo môi trường song song cho phép tác nhân thu thập

### 00:00:14.000 - 00:00:18.000
kinh nghiệm từ nhiều môi trường cùng một lúc.

### 00:00:19.000 - 00:00:23.000
Sau đó, chúng ta sẽ khởi tạo mạng nơ-ron sẽ sử dụng làm chính sách.

### 00:00:24.000 - 00:00:29.000
Sau đó, chúng ta sẽ vào vòng lặp chính sẽ lặp lại trong một số tập.

### 00:00:30.000 - 00:00:36.000
Trong mỗi tập, tác nhân sẽ tương tác với các môi trường song song để thu thập quỹ đạo của

### 00:00:36.000 - 00:00:37.000
kinh nghiệm.

### 00:00:37.000 - 00:00:43.000
Sau đó khi đại lý kết thúc tập phim và thu thập kinh nghiệm sẽ đến lúc cập nhật

### 00:00:43.000 - 00:00:44.000
mạng lưới thần kinh.

### 00:00:45.000 - 00:00:46.000
Vì điều đó.

### 00:00:46.000 - 00:00:50.000
Chúng ta sẽ lặp lại từng thời điểm theo thứ tự nghịch đảo.

### 00:00:51.000 - 00:00:56.000
Đó là từ giây phút cuối cùng cho đến khi bắt đầu tập phim.

### 00:00:56.000 - 00:01:02.000
Và tại mỗi thời điểm, chúng tôi sẽ tính lợi nhuận của nó là phần thưởng nhận được tại thời điểm đó,

### 00:01:02.000 - 00:01:06.000
cộng với lợi nhuận tích lũy nhân với Gamma.

### 00:01:07.000 - 00:01:15.000
Sau đó, chúng tôi sẽ tính toán entropy của chính sách bằng cách sử dụng xác suất thực hiện từng hành động trong trạng thái

### 00:01:15.000 - 00:01:15.000
tại thời điểm t.

### 00:01:17.000 - 00:01:22.000
Và với những giá trị đó, chúng tôi sẽ có thể ước tính hiệu suất của chính sách cho trạng thái đó với

### 00:01:22.000 - 00:01:24.000
biểu hiện mà bạn đã biết.

### 00:01:25.000 - 00:01:32.000
Và với biểu thức đó, chúng ta sẽ thêm entropy để khi chúng ta thực hiện tăng độ dốc ngẫu nhiên,

### 00:01:32.000 - 00:01:40.000
chúng tôi cũng cố gắng tối đa hóa entropy của chính sách dựa trên ước tính hiệu suất chính sách này.

### 00:01:40.000 - 00:01:48.000
Chúng ta sẽ thực hiện bước tăng dần độ dốc và chúng ta sẽ thực hiện việc đó bằng cách sử dụng biểu thức này cho giá trị trước đó cho

### 00:01:48.000 - 00:01:50.000
các tham số của mạng nơ-ron.

### 00:01:50.000 - 00:01:57.000
Chúng tôi sẽ thêm độ dốc hiệu suất của chính sách nhân với tỷ lệ phần trăm alpha.

### 00:01:58.000 - 00:01:59.000
Và thế là xong.

### 00:01:59.000 - 00:02:02.000
Tôi sẽ gặp bạn trong video tiếp theo nơi chúng ta sẽ bắt đầu triển khai thuật toán này.

