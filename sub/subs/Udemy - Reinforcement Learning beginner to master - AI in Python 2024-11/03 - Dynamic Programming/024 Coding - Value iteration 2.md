# Lập Trình - Lặp Giá Trị 2

## Nội dung

### 00:00:01 - 00:00:07
Trong video này, chúng ta sẽ định nghĩa chính sách của tác tử và chúng ta sẽ thấy nó hiệu quả như thế nào khi cố gắng

### 00:00:07 - 00:00:09
Giải quyết môi trường.

### 00:00:10 - 00:00:16
Điều đầu tiên chúng ta sẽ làm là tạo một bảng sẽ chứa các xác suất của tác tử

### 00:00:17 - 00:00:19
Chọn mỗi hành động trong mỗi trạng thái.

### 00:00:20 - 00:00:29
Hãy gọi bảng này là policy_probs và chúng ta sẽ điền nó bằng phương thức full của NumPy sẽ gán

### 00:00:29 - 00:00:32
Cùng một giá trị cho tất cả các mục trong bảng.

### 00:00:32 - 00:00:40
Kích thước của bảng sẽ là 5x5x4 vì chúng ta có 5 giá trị có thể cho hàng,

### 00:00:40 - 00:00:43
5 cho cột và 4 hành động có thể.

### 00:00:44 - 00:00:49
Và chúng ta muốn một mục cho mỗi hành động có thể trong mỗi trạng thái có thể.

### 00:00:51 - 00:00:56
Và trong bảng này, mỗi hành động có 25% xác suất được chọn.

### 00:00:57 - 00:01:00
Những xác suất đó sẽ thay đổi trong quá trình học tập.

### 01:04:00 - 00:01:10
Điều tiếp theo chúng ta sẽ làm là định nghĩa chính sách. Như bạn biết, chính sách là một hàm lấy

### 01:10:00 - 00:01:16
Đầu vào là một trạng thái và trả về các xác suất của mỗi hành động được thực hiện bởi tác tử.

### 01:19:00 - 00:01:25
Trong trường hợp này, kể từ đầu quá trình học tập, tác tử theo một chính sách ngẫu nhiên, mỗi

### 01:25:00 - 00:01:29
Hành động sẽ có cùng xác suất được chọn: 0,25.
