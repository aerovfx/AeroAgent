## Nội dung

### 00:00:00.000 - 00:00:06.000
Trong video này, chúng ta sẽ tìm hiểu cách đánh giá hiệu suất của một chính sách được triển khai bằng cách sử dụng

### 00:00:06.000 - 00:00:07.000
một mạng lưới thần kinh.

### 00:00:08.000 - 00:00:14.000
Nếu muốn tìm chính sách tối ưu, chúng ta cần có khả năng so sánh chính sách này với chính sách khác để có thể

### 00:00:14.000 - 00:00:15.000
có thể chọn cái tốt nhất.

### 00:00:16.000 - 00:00:21.000
Và để làm được điều đó, chúng ta cần một loại thước đo nào đó cho chúng ta biết hiệu quả của một chính sách là gì.

### 00:00:22.000 - 00:00:27.000
Lưu ý nếu chúng ta thay đổi tham số của mạng nơ-ron sẽ cho ra xác suất khác nhau

### 00:00:27.000 - 00:00:29.000
vectơ cho mỗi trạng thái.

### 00:00:29.000 - 00:00:35.000
Nghĩa là, bằng cách thay đổi các tham số của mạng nơ-ron, chúng ta thay đổi chính sách.

### 00:00:35.000 - 00:00:40.000
Do đó, hiệu suất của chính sách là một chức năng của các tham số của nó.

### 00:00:41.000 - 00:00:47.000
Và với thước đo hiệu suất này, chúng tôi sẽ có thể thể hiện chính sách nào chúng tôi thích.

### 00:00:47.000 - 00:00:54.000
Nếu hiệu suất của một chính sách cao hơn hiệu suất của chính sách khác thì chúng tôi sẽ ưu tiên

### 00:00:54.000 - 00:00:56.000
chính sách đầu tiên đến chính sách thứ hai.

### 00:00:56.000 - 00:01:00.000
Và mục tiêu của chúng tôi tất nhiên là tìm ra chính sách tối ưu.

### 00:01:00.000 - 00:01:06.000
Tức là chúng ta muốn tìm chính sách có hiệu suất cao nhất có thể.

### 00:01:06.000 - 00:01:13.000
Để làm được điều đó, chúng ta sẽ phải tìm các giá trị cho các tham số mạng thần kinh tạo ra chính sách này

### 00:01:13.000 - 00:01:15.000
với hiệu suất tối ưu.

### 00:01:15.000 - 00:01:19.000
Và việc tìm kiếm đó sẽ được thực hiện bằng cách tăng dần độ dốc.

### 00:01:19.000 - 00:01:26.000
Nghĩa là, chúng ta sẽ sử dụng kinh nghiệm mà tác nhân thu thập được từ môi trường để ước tính

### 00:01:26.000 - 00:01:30.000
hiệu quả của chính sách đã thu thập được kinh nghiệm đó.

### 00:01:30.000 - 00:01:35.000
Và sau đó, khi có được ước tính hiệu suất đó, chúng tôi sẽ tính toán vectơ độ dốc của nó.

### 00:01:35.000 - 00:01:43.000
Hãy nhớ rằng vectơ gradient chứa đạo hàm riêng của hiệu suất đối với

### 00:01:43.000 - 00:01:45.000
các tham số của mạng nơ-ron.

### 00:01:45.000 - 00:01:53.000
Và vectơ này chỉ ra cách sửa đổi các tham số này để tăng hiệu suất ở mức tối đa.

### 00:01:54.000 - 00:02:00.000
Khi có vectơ này, chúng tôi sẽ sử dụng nó để thực hiện cập nhật tăng dần độ dốc ngẫu nhiên.

### 00:02:00.000 - 00:02:06.000
Trong quy tắc cập nhật, chúng tôi thêm vào giá trị trước đó của các tham số độ dốc của hiệu suất

### 00:02:06.000 - 00:02:07.000
đo lường.

### 00:02:08.000 - 00:02:15.000
Alpha là tốc độ học tập sẽ quyết định mức độ lớn mà chúng ta đang thực hiện theo hướng gradient.

