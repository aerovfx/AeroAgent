## Nội dung

### 00:00:00.000 - 00:00:04.000
Trong video này, chúng ta sẽ có cái nhìn thực tế về sự khác biệt giữa Monte Carlo và tạm thời.

### 00:00:04.000 - 00:00:05.000
các phương pháp khác biệt.

### 00:00:06.000 - 00:00:13.000
Chúng tôi đã tạo một đặc vụ phải đối mặt với một tập của Mê cung năm x năm bằng cách sử dụng phương pháp monte Carlo và phương pháp tạm thời.

### 00:00:13.000 - 00:00:16.000
phương pháp sai phân với phương pháp Monte Carlo.

### 00:00:16.000 - 00:00:23.000
Sau khi thực hiện nước đi đầu tiên, bảng giá trị Q không thay đổi sau khi thực hiện năm hành động.

### 00:00:23.000 - 00:00:25.000
Cái bàn vẫn như cũ.

### 00:00:26.000 - 00:00:29.000
Ngay cả sau khi thực hiện 120 hành động.

### 00:00:29.000 - 00:00:35.000
Bảng vẫn giữ nguyên như lúc đầu, vì phương pháp Monte Carlo cần đợi cho đến khi

### 00:00:35.000 - 00:00:38.000
cuối tập để cập nhật giá trị Q.

### 00:00:39.000 - 00:00:46.000
Mặt khác, các phương pháp sai phân thời gian có thể bắt đầu cập nhật bảng giá trị Q ngay sau

### 00:00:46.000 - 00:00:47.000
thực hiện hành động đầu tiên.

### 00:00:48.000 - 00:00:53.000
Điều này có nghĩa là các hành động được thực hiện ở đầu tập phim bắt đầu ảnh hưởng đến hành vi.

### 00:00:53.000 - 00:00:55.000
của đại lý ngay lập tức.

### 00:00:56.000 - 00:00:58.000
Sau 20 hành động.

### 00:00:58.000 - 00:01:07.000
Thuật toán đã truy cập nhiều trạng thái và đã cập nhật tất cả các giá trị Q này và sau 120 lần di chuyển, nó

### 00:01:07.000 - 00:01:09.000
sẽ cập nhật tất cả các giá trị này.

### 00:01:10.000 - 00:01:13.000
Các giá trị ước tính tại thời điểm này không hoàn hảo.

### 00:01:13.000 - 00:01:19.000
Chúng thậm chí có thể không tốt, nhưng quá trình tối ưu hóa đã bắt đầu mà không cần đợi đến cuối

### 00:01:19.000 - 00:01:22.000
tập để thực hiện tất cả các cập nhật cùng một lúc.

