## Nội dung

### 00:00:00.000 - 00:00:04.000
Trong video này, chúng tôi sẽ trình bày các dự đoán của mạng lưới thần kinh.

### 00:00:04.000 - 00:00:11.000
Cụ thể, chúng tôi sẽ hiển thị giá trị âm của giá trị Q cao nhất cho mọi trạng thái, được biết đến

### 00:00:11.000 - 00:00:13.000
như chi phí để đi.

### 00:00:14.000 - 00:00:16.000
Đó là cái giá phải trả để đạt được mục tiêu.

### 00:00:16.000 - 00:00:18.000
Bắt đầu từ mỗi tiểu bang.

### 00:00:18.000 - 00:00:24.000
Chúng tôi sẽ sử dụng chi phí cốt truyện cho hàm mà chúng tôi đã nhập từ tệp cục bộ.

### 00:00:25.000 - 00:00:28.000
Và với chức năng này, chúng ta sẽ chuyển môi trường.

### 00:00:29.000 - 00:00:30.000
Mạng lưới thần kinh.

### 00:00:34.000 - 00:00:38.000
Và nhãn cho trục x và Y.

### 00:00:40.000 - 00:00:45.000
Trong trục x, chúng ta sẽ hiển thị chiều thứ nhất của trạng thái.

### 00:00:46.000 - 00:00:48.000
Đó là vị trí của xe.

### 00:00:49.000 - 00:00:56.000
Và trong trục y chúng ta sẽ hiển thị chiều thứ hai đó là vận tốc của ô tô.

### 00:01:00.000 - 00:01:02.000
Hãy thực thi ô này.

### 00:01:03.000 - 00:01:04.000
Và ở đây chúng tôi có nó.

### 00:01:05.000 - 00:01:12.000
Như bạn đã biết, mạng nơ-ron được khởi tạo ngẫu nhiên, điều đó có nghĩa là những dự đoán này

### 00:01:12.000 - 00:01:13.000
không chính xác chút nào.

### 00:01:13.000 - 00:01:22.000
Chúng chỉ đơn giản là các giá trị ngẫu nhiên sẽ thay đổi trong quá trình học để phản ánh các giá trị tối ưu.

### 00:01:22.000 - 00:01:30.000
Hãy chú ý đến thực tế là mỗi sự kết hợp của giá trị X và Y là sự kết hợp của vị trí

### 00:01:30.000 - 00:01:32.000
của ô tô và vận tốc của nó.

### 00:01:32.000 - 00:01:38.000
Điều đó có nghĩa là mặt phẳng dưới đây là không gian trạng thái.

### 00:01:38.000 - 00:01:48.000
Ví dụ, một trạng thái có thể là -0,5 cho vị trí của ô tô và 0 dấu phẩy hai cho vận tốc.

### 00:01:48.000 - 00:01:55.000
Và biểu đồ này cho chúng ta thấy cái giá phải trả để đạt được mục tiêu bắt đầu từ mỗi trạng thái này.

### 00:01:55.000 - 00:02:02.000
Chúng ta sẽ thấy lại biểu đồ này sau khi thực hiện thuật toán học để xem chúng ta có thể quan sát từng trạng thái như thế nào

### 00:02:02.000 - 00:02:04.000
chi phí ước tính của nó để đi.

