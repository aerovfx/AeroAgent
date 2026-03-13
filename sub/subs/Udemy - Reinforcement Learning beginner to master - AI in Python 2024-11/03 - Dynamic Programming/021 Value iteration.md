# Lặp Giá Trị

## Nội dung

### 00:00:00 - 00:00:06
Trong video này, chúng ta sẽ xem thuật toán lập trình động đầu tiên gọi là Lặp giá trị.

### 00:00:08 - 00:00:10
Chúng ta muốn tìm chính sách tối ưu.

### 00:00:11 - 00:00:16
Chính sách này là chính sách trong mỗi trạng thái thực hiện hành động tối đa hóa lợi nhuận.

### 00:00:17 - 00:00:24
Để tính lợi nhuận kỳ vọng để chọn hành động, chúng ta phải biết giá trị tối ưu của

### 00:00:24 - 00:00:27
Các trạng thái có thể theo sau trạng thái hiện tại.

### 00:00:28 - 00:00:32
Chúng ta ước lượng các giá trị này theo một quá trình lặp.

### 00:00:33 - 00:00:37
Chúng ta sẽ duy trì một bảng với các giá trị ước lượng của mỗi trạng thái.

### 00:00:38 - 00:00:40
Ước lượng ban đầu không cần phải tốt.

### 00:00:42 - 00:00:47
Sau đó chúng ta sẽ đi từng trạng thái một cải thiện các ước lượng này theo quy tắc này.

### 00:00:49 - 00:00:55
Chúng ta sẽ lặp lại quá trình này bao nhiêu lần cần thiết cho đến khi các ước lượng rất gần với các giá trị

### 00:00:55 - 00:00:56
Theo chính sách tối ưu.

### 00:00:57 - 00:01:04
Đây là thuật toán, như bạn có thể thấy, nó khá đơn giản, chúng ta sẽ chỉ lặp lại một vòng lặp nơi sẽ cập nhật

### 01:04:00 - 00:01:07
Giá trị ước lượng của mọi trạng thái.

### 01:09:00 - 00:01:13
Lúc đầu, các giá trị sẽ thay đổi nhiều giữa một cập nhật và cập nhật tiếp theo.

### 01:13:00 - 00:01:17
Nhưng khi chúng tiến gần đến giá trị tối ưu, chúng sẽ thay đổi ít hơn và ít hơn.

### 01:18:00 - 00:01:25
Khi các thay đổi nhỏ hơn tham số theta do chúng ta chọn, chúng ta sẽ dừng chạy vòng lặp vì

### 01:25:00 - 00:01:27
Xấp xỉ sẽ đủ tốt.

### 01:28:00 - 00:01:34
Sau đó, dựa trên các ước lượng này của các giá trị tối ưu, chúng ta sẽ định nghĩa chính sách, chọn các hành động

### 01:34:00 - 00:01:36
Tối đa hóa lợi nhuận kỳ vọng.

### 01:38:00 - 00:01:44
Hãy xem nó với một ví dụ. Ở bên phải, chúng ta có một nhiệm vụ điều khiển mà chúng ta đã thấy trong phần trước:

### 01:44:00 - 00:01:45
Mê cung 5x5.

### 01:46:00 - 00:01:50
Sau mỗi bước đi, tác tử nhận được phần thưởng là -1.

### 01:51:00 - 00:01:54
Mục tiêu là tìm lối ra qua con đường ngắn nhất.

### 01:55:00 - 00:02:01
Môi trường này là tất định, có nghĩa là nếu tác tử di chuyển sang phải, nó sẽ kết thúc

### 02:01:00 - 00:02:07
Ở ô bên phải với xác suất 100%, trừ khi có tường ở giữa.
