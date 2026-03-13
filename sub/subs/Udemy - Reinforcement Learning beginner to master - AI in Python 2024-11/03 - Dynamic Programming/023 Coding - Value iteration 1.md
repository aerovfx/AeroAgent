# Lập Trình - Lặp Giá Trị 1

## Nội dung

### 00:00:00 - 00:00:05
Trong video này, chúng ta sẽ bắt đầu triển khai thuật toán lặp chính sách mà chúng ta đã thấy trong

### 00:00:05 - 00:00:07
Phần về lập trình động.

### 00:00:10 - 00:00:16
Điều đầu tiên chúng ta sẽ làm là nhập các thư viện mã mà chúng ta sẽ sử dụng, cái đầu tiên được gọi là

### 00:00:16 - 00:00:18
NumPy.

### 00:00:18 - 00:00:24
Nó sẽ cho phép chúng ta làm việc với các vectơ và ma trận và sẽ cho phép chúng ta thể hiện các bảng giá trị của chúng ta.

### 00:00:25 - 00:00:31
Thư viện thứ hai mà chúng ta sẽ sử dụng được gọi là PyPlot, và chúng ta nhập nó dưới dạng plt.

### 00:00:34 - 00:00:40
Cũng từ các tệp cục bộ mà chúng ta đã tải xuống từ GitHub, chúng ta sẽ nhập môi trường

### 00:00:40 - 00:00:46
Mà chúng ta sẽ giải quyết và một số chức năng sẽ cho phép chúng ta hình dung quá trình học tập.

### 00:00:47 - 00:00:52
Môi trường mà chúng ta sẽ giải quyết được gọi là Mê cung, và chúng ta có thể tìm thấy nó trong tệp cục bộ.

### 00:00:52 - 00:00:53
envs.py.

### 00:00:57 - 00:01:01
Và từ tệp utils.py, chúng ta sẽ nhập hàm plot_policy()

### 01:06:00 - 00:01:07
cũng plot_values()

### 01:09:00 - 00:01:11
Và một hàm khác gọi là test_agent().

### 01:13:00 - 00:01:15
Sau đó, chúng ta sẽ thấy mỗi chức năng này làm gì.

### 01:18:00 - 00:01:24
Điều tiếp theo chúng ta sẽ làm là khởi tạo môi trường, và để làm điều đó, chúng ta sẽ tạo ra một ví dụ

### 01:24:00 - 00:01:29
Của lớp Maze và chúng ta sẽ lưu trữ nó trong biến env.

### 01:30:00 - 00:01:38
Môi trường này là maze 5x5 trong đó tác tử có thể di chuyển lên, xuống, trái hoặc phải theo thứ tự

### 01:38:00 - 00:01:39
Để tìm ra lối ra.

### 01:40:00 - 00:01:46
Bây giờ chúng ta sẽ thấy môi trường này một cách trực quan. Để làm điều đó, chúng ta sẽ sử dụng phương thức render()

### 01:47:00 - 00:01:54
Và phương thức đó sẽ cung cấp cho chúng ta một khung hình, là biểu diễn trực quan của trạng thái nhiệm vụ. Chúng ta
