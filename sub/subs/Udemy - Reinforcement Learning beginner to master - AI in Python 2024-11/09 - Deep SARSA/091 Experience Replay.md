## Nội dung

### 00:00:00.000 - 00:00:01.000
Trong video này.

### 00:00:01.000 - 00:00:05.000
Chúng ta sẽ xem bộ nhớ phát lại là gì và chúng ta sẽ sử dụng nó như thế nào.

### 00:00:05.000 - 00:00:13.000
Trong thuật toán Dbsa, bộ nhớ phát lại là cơ sở dữ liệu trong đó chúng ta sẽ lưu trữ các chuyển đổi trạng thái

### 00:00:13.000 - 00:00:16.000
mà tác nhân quan sát được khi đối mặt với nhiệm vụ điều khiển.

### 00:00:17.000 - 00:00:24.000
Mỗi khi tác nhân thực hiện một hành động, chúng ta sẽ ghi vào bộ nhớ trạng thái mà tác nhân đó thực hiện.

### 00:00:24.000 - 00:00:26.000
đã có trong hành động được thực hiện bởi người đại diện.

### 00:00:26.000 - 00:00:33.000
Phần thưởng nhận được do thực hiện hành động đó và trạng thái tiếp theo mà tác nhân đạt được.

### 00:00:33.000 - 00:00:39.000
Bộ nhớ có số lượng mục nhập tối đa và khi vượt quá số lượng này, nó sẽ bắt đầu xóa

### 00:00:39.000 - 00:00:46.000
các mục nhập cũ nhất và thay thế chúng bằng các chuyển đổi mới nhất mà tác nhân quan sát được.

### 00:00:46.000 - 00:00:51.000
Bằng cách này, bộ nhớ phát lại sẽ giữ một nhóm chuyển đổi trạng thái mới.

### 00:00:51.000 - 00:00:57.000
Sau đó, khi đến lúc cập nhật mạng nơ-ron, chúng tôi sẽ sử dụng trải nghiệm mà chúng tôi đã lưu trữ trong

### 00:00:57.000 - 00:00:58.000
bộ nhớ để làm điều đó.

### 00:00:59.000 - 00:01:00.000
Từ khắp tiểu bang.

### 00:01:00.000 - 00:01:06.000
Các chuyển tiếp được lưu trong bộ nhớ sẽ chọn ngẫu nhiên một loạt các chuyển tiếp.

### 00:01:06.000 - 00:01:09.000
Kích thước của lô được chúng tôi lựa chọn.

### 00:01:09.000 - 00:01:14.000
Khi có lô đó, chúng tôi sẽ sử dụng nó để tính hàm chi phí.

### 00:01:14.000 - 00:01:18.000
Và dựa trên ước tính của hàm chi phí đó, chúng tôi sẽ cập nhật mạng lưới thần kinh.

### 00:01:19.000 - 00:01:23.000
Bộ nhớ phát lại có liên quan đến ba dòng thuật toán này.

### 00:01:23.000 - 00:01:28.000
Đầu tiên, trước khi vào vòng lặp chính, chúng ta sẽ tạo một bộ nhớ phát lại trống.

### 00:01:29.000 - 00:01:35.000
Tại mỗi thời điểm, trong tập, chúng tôi sẽ lưu trữ quá trình chuyển đổi trạng thái ngay sau

### 00:01:35.000 - 00:01:36.000
đại lý trải nghiệm nó.

### 00:01:37.000 - 00:01:43.000
Và cũng tại thời điểm này, trong tập này, chúng tôi sẽ lấy mẫu một loạt chuyển đổi để cập nhật

### 00:01:43.000 - 00:01:45.000
mạng lưới thần kinh.

### 00:01:45.000 - 00:01:46.000
Vì điều đó.

### 00:01:46.000 - 00:01:49.000
Chúng tôi sẽ lấy lô từ bộ nhớ.

### 00:01:49.000 - 00:01:54.000
Chúng ta sẽ tính toán ước tính của hàm chi phí và dựa vào đó, chúng ta sẽ thực hiện một gradient ngẫu nhiên

### 00:01:54.000 - 00:01:56.000
bước đi xuống.

