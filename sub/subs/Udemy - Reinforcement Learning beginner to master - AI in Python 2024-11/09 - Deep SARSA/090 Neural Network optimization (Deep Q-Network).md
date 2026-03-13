## Nội dung

### 00:00:00.000 - 00:00:06.000
Trong video này, chúng ta sẽ xem cách tối ưu hóa mạng lưới thần kinh của mình để tạo ra kết quả ngày càng chính xác hơn.

### 00:00:06.000 - 00:00:07.000
ước lượng giá trị q.

### 00:00:07.000 - 00:00:13.000
Những gì chúng ta sẽ làm là so sánh các ước tính do mạng nơ-ron đưa ra với giá trị chính xác.

### 00:00:13.000 - 00:00:17.000
Sự khác biệt giữa hai giá trị này là lỗi ước tính.

### 00:00:17.000 - 00:00:24.000
Với lỗi này, chúng ta sẽ xác định hàm chi phí là hàm biểu thị kích thước của lỗi

### 00:00:24.000 - 00:00:28.000
và chúng ta sẽ giảm thiểu trong thuật toán sarsa sâu.

### 00:00:28.000 - 00:00:35.000
Chúng ta sẽ giảm thiểu hàm chi phí được gọi là sai số bình phương trung bình, bao gồm giá trị trung bình của

### 00:00:35.000 - 00:00:38.000
bình phương của sai số.

### 00:00:38.000 - 00:00:44.000
Trong trường hợp của chúng tôi, các ước tính sẽ là giá trị Q do mạng nơ-ron tạo ra cho một trạng thái cụ thể

### 00:00:44.000 - 00:00:47.000
và một hành động cụ thể

### 00:00:48.000 - 00:00:55.000
Giá trị mục tiêu, như trong thuật toán Sarsa ban đầu, sẽ là kết quả thu được ước tính trong một bước.

### 00:00:56.000 - 00:01:03.000
Tức là phần thưởng nhận được khi thực hiện hành động và giá trị Q chiết khấu của hành động đã chọn

### 00:01:03.000 - 00:01:06.000
bởi chính sách ở trạng thái tiếp theo.

### 00:01:07.000 - 00:01:14.000
Chính sự khác biệt này sẽ phải giảm thiểu bằng cách xác định và giảm thiểu hàm chi phí.

### 00:01:15.000 - 00:01:22.000
Để làm được điều đó, chúng ta sẽ tính giá trị của hàm chi phí dựa trên một loạt kinh nghiệm được lấy từ

### 00:01:22.000 - 00:01:23.000
bộ nhớ phát lại.

### 00:01:23.000 - 00:01:30.000
Dựa trên chúng, chúng tôi sẽ tính toán các giá trị Q ước tính và các giá trị mục tiêu cho mỗi lần chuyển đổi trạng thái,

### 00:01:31.000 - 00:01:34.000
và dựa vào đó chúng ta sẽ tính hàm chi phí.

### 00:01:35.000 - 00:01:42.000
Khi chúng ta có giá trị của hàm chi phí, chúng ta sẽ tính độ dốc của nó đối với từng

### 00:01:42.000 - 00:01:44.000
các tham số của mạng nơ-ron.

### 00:01:44.000 - 00:01:52.000
Vectơ này sẽ chỉ ra hướng sửa đổi các tham số mạng thần kinh để tối đa hóa

### 00:01:52.000 - 00:01:53.000
hàm chi phí.

### 00:01:54.000 - 00:02:01.000
Nhưng vì chúng ta đang thực hiện nên việc giảm độ dốc ngẫu nhiên sẽ quan tâm đến việc giảm thiểu tổn thất

### 00:02:01.000 - 00:02:02.000
chức năng.

### 00:02:03.000 - 00:02:09.000
Do đó, chúng ta sẽ di chuyển các tham số của mạng nơ-ron theo hướng ngược lại với gradient

### 00:02:09.000 - 00:02:14.000
vectơ của hàm mất mát tỷ lệ với alpha.

### 00:02:15.000 - 00:02:21.000
Như bạn có thể thấy, quy tắc cập nhật rất giống với quy tắc mà chúng ta đã thấy trong các thuật toán dạng bảng,

### 00:02:21.000 - 00:02:26.000
ngoại trừ việc bây giờ, thay vì sửa đổi giá trị của các bảng, chúng tôi đang sửa đổi các tham số của

### 00:02:26.000 - 00:02:27.000
mạng lưới thần kinh.

### 00:02:28.000 - 00:02:32.000
Đó là quá trình được gọi là giảm độ dốc ngẫu nhiên.

### 00:02:32.000 - 00:02:38.000
Chúng tôi sẽ thực hiện cập nhật này vào mọi thời điểm trong suốt thời gian thực hiện nhiệm vụ kiểm soát ngay sau khi

### 00:02:38.000 - 00:02:41.000
Agent tương tác với môi trường.

