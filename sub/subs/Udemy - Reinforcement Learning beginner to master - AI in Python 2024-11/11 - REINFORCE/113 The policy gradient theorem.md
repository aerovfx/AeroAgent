## Nội dung

### 00:00:00.000 - 00:00:04.000
Chúng ta đã biết cách tối ưu hóa chính sách bằng cách sử dụng phương pháp giảm độ dốc.

### 00:00:04.000 - 00:00:11.000
Nhưng để làm được điều đó, chúng ta cần có khả năng ước tính hiệu quả của chính sách từ kinh nghiệm

### 00:00:11.000 - 00:00:14.000
mà tác nhân thu thập, tương tác với môi trường.

### 00:00:14.000 - 00:00:19.000
Để biết cách thực hiện điều đó, chúng ta cần biết định lý gradient chính sách.

### 00:00:20.000 - 00:00:27.000
Định lý này là kết quả cho chúng ta biết chính xác những giá trị nào chúng ta cần thu thập từ môi trường

### 00:00:27.000 - 00:00:30.000
để đánh giá hiệu quả của chính sách.

### 00:00:31.000 - 00:00:36.000
Điều đầu tiên chúng ta cần làm là xác định chính xác ý nghĩa của hiệu suất.

### 00:00:36.000 - 00:00:39.000
Để làm được điều đó, chúng ta hãy dừng lại và suy nghĩ một lát.

### 00:00:39.000 - 00:00:43.000
Chúng ta muốn đạt được điều gì khi thực hiện nhiệm vụ kiểm soát?

### 00:00:44.000 - 00:00:50.000
Chà, chúng tôi muốn thực hiện các hành động nhằm tối đa hóa số tiền chiết khấu của phần thưởng dự kiến.

### 00:00:50.000 - 00:00:55.000
Và điều đó cũng giống như việc tối đa hóa giá trị của trạng thái ban đầu.

### 00:00:56.000 - 00:01:03.000
Vì vậy, chúng tôi muốn tối đa hóa giá trị của trạng thái ban đầu đó dựa trên chính sách sẽ bắt đầu

### 00:01:03.000 - 00:01:04.000
ở trạng thái đó.

### 00:01:05.000 - 00:01:07.000
Đó sẽ là định nghĩa của chúng tôi về hiệu suất.

### 00:01:07.000 - 00:01:11.000
Từ định nghĩa đó, ta có thể đi đến kết quả sau.

### 00:01:11.000 - 00:01:17.000
Để tránh làm phức tạp việc giải thích, chúng tôi đã bỏ qua phần dẫn xuất của biểu thức này.

### 00:01:17.000 - 00:01:19.000
Nhưng bạn có thể tìm thấy nó trong cuốn sách này.

### 00:01:20.000 - 00:01:23.000
Hãy giải thích từng bước ý nghĩa của biểu thức này.

### 00:01:23.000 - 00:01:28.000
Ở phía bên trái, chúng ta có độ dốc hiệu suất của chính sách.

### 00:01:28.000 - 00:01:31.000
Đây là số lượng mà chúng tôi muốn ước tính.

### 00:01:31.000 - 00:01:36.000
Thuật ngữ thứ hai là sự phân bổ các quốc gia tuân theo chính sách.

### 00:01:36.000 - 00:01:42.000
Đó là tỷ lệ phần trăm số lần mà chúng tôi mong đợi sẽ thấy bất kỳ trạng thái nhất định nào trên tổng số.

### 00:01:43.000 - 00:01:50.000
Thuật ngữ thứ ba này bạn đã biết đó là giá trị Q của một cặp trạng thái và hành động tuân theo chính sách

### 00:01:50.000 - 00:01:57.000
và số hạng cuối cùng này là độ dốc của xác suất thực hiện hành động A ở trạng thái.

### 00:01:57.000 - 00:02:03.000
Đó là hướng mà chúng ta phải di chuyển các tham số của chính sách, đó là các tham số

### 00:02:03.000 - 00:02:10.000
của mạng nơ-ron sao cho xác suất chọn hành động đó tăng lên nhiều nhất có thể.

### 00:02:10.000 - 00:02:11.000
Được rồi.

### 00:02:11.000 - 00:02:18.000
Khi chúng ta biết ý nghĩa của từng thuật ngữ này, câu hỏi đặt ra là tổng thể biểu thức này có ý nghĩa gì?

### 00:02:19.000 - 00:02:25.000
Vâng, điều đó có nghĩa là độ dốc của hiệu suất của chính sách tỷ lệ thuận với lợi nhuận

### 00:02:25.000 - 00:02:33.000
của từng hành động ở mỗi trạng thái, nhân với độ dốc của xác suất thực hiện hành động đó trong

### 00:02:33.000 - 00:02:41.000
trạng thái đó và được tính theo tần suất chúng tôi quan sát từng trạng thái tuân theo chính sách đó.

### 00:02:41.000 - 00:02:48.000
Theo trực giác, nếu một hành động trong một trạng thái tạo ra lợi nhuận dương để tăng lợi nhuận, chúng ta phải tăng

### 00:02:48.000 - 00:02:51.000
xác suất chọn hành động đó.

### 00:02:51.000 - 00:02:57.000
Và nếu hành động đó tạo ra lợi nhuận âm thì xác suất lựa chọn hành động đó phải giảm đi.

### 00:02:57.000 - 00:03:04.000
Chà, nhờ biểu thức này, giờ đây chúng ta có thể cải thiện chính sách bằng cách sử dụng các giá trị mà tác nhân có thể

### 00:03:04.000 - 00:03:05.000
quan sát.

### 00:03:06.000 - 00:03:08.000
Chúng tôi chỉ cần lấy mẫu.

### 00:03:08.000 - 00:03:11.000
Giá trị kỳ vọng của biểu thức này là của ai?

### 00:03:11.000 - 00:03:16.000
Trong nhóm phương pháp này, có nhiều thuật toán khác nhau và mỗi thuật toán thực hiện việc này một cách khác nhau.

### 00:03:17.000 - 00:03:20.000
Tôi sẽ gặp bạn trong video tiếp theo nơi chúng ta sẽ xem xét video đầu tiên.

