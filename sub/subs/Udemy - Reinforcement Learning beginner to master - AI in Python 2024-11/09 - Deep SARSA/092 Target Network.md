## Nội dung

### 00:00:00.000 - 00:00:05.000
Trong video này, chúng ta sẽ thấy thay đổi cuối cùng sẽ thực hiện đối với thuật toán để điều chỉnh thuật toán cho phù hợp với

### 00:00:05.000 - 00:00:12.000
sử dụng mạng lưới thần kinh Trong thuật toán sarsa sâu, chúng ta sẽ kết hợp hai kỹ thuật có thể

### 00:00:12.000 - 00:00:15.000
dẫn đến quá trình học tập không ổn định.

### 00:00:16.000 - 00:00:18.000
Một mặt, chúng ta sẽ thực hiện bootstrapping.

### 00:00:18.000 - 00:00:24.000
Nghĩa là, chúng tôi sẽ cập nhật ước tính bằng cách lấy một ước tính khác làm tham chiếu.

### 00:00:24.000 - 00:00:30.000
Như bạn có thể thấy, mục tiêu mà chúng tôi hướng tới ước tính giá trị Q chứa ước tính về

### 00:00:30.000 - 00:00:33.000
giá trị của trạng thái tiếp theo và hành động tiếp theo.

### 00:00:34.000 - 00:00:39.000
Mặt khác, chúng ta sẽ sử dụng một hàm gần đúng, trong trường hợp này sẽ là một hàm thần kinh

### 00:00:39.000 - 00:00:40.000
mạng.

### 00:00:41.000 - 00:00:46.000
Nhưng tại sao hai kỹ thuật này kết hợp lại có thể tạo ra một quá trình học tập không ổn định?

### 00:00:46.000 - 00:00:51.000
Chà, hãy nhìn vào biểu đồ bên phải, biểu thị các ước tính giá trị Q được tính toán bởi một nơron

### 00:00:51.000 - 00:00:57.000
mạng cho một hành động cụ thể ở mỗi trạng thái của tác vụ điều khiển nhúng này.

### 00:00:58.000 - 00:01:05.000
Khi chúng tôi cập nhật ước tính cho một trạng thái thông qua việc giảm độ dốc, chúng tôi không chỉ sửa đổi ước tính cho trạng thái đó

### 00:01:05.000 - 00:01:09.000
bang mà còn cho tất cả các bang gần nó.

### 00:01:09.000 - 00:01:16.000
Trong biểu đồ, hàm màu xanh biểu thị ước tính giá trị Q trước khi thực hiện giảm độ dốc

### 00:01:16.000 - 00:01:19.000
bước và bước màu đỏ là ước tính sau đó.

### 00:01:20.000 - 00:01:26.000
Khi tác nhân thực hiện một hành động, trạng thái tiếp theo thường rất giống với trạng thái trước đó.

### 00:01:26.000 - 00:01:32.000
Điều này có nghĩa là khi chúng tôi cập nhật giá trị Q ước tính mà chúng tôi muốn tối ưu hóa, chúng tôi cũng sẽ

### 00:01:32.000 - 00:01:34.000
chuyển mục tiêu của nó.

### 00:01:35.000 - 00:01:39.000
Đó là giá trị mà chúng tôi muốn ước tính của mình tuân theo.

### 00:01:40.000 - 00:01:46.000
Vì ước tính của chúng tôi về giá trị Q sẽ tiếp cận mục tiêu đang di chuyển nên quá trình này sẽ không ổn định.

### 00:01:46.000 - 00:01:52.000
Để quá trình học tập được ổn định, các mục tiêu cũng phải ổn định vì chúng thể hiện đúng mục tiêu.

### 00:01:52.000 - 00:01:55.000
các giá trị mà ước tính của chúng tôi phải chuyển tới.

### 00:01:56.000 - 00:01:58.000
Nhưng làm thế nào chúng ta có thể đạt được điều này?

### 00:01:59.000 - 00:02:04.000
Chà, điều chúng ta sắp làm là tạo một bản sao chính xác của mạng lưới thần kinh ước tính Q

### 00:02:04.000 - 00:02:05.000
các giá trị.

### 00:02:05.000 - 00:02:09.000
Và chúng tôi sẽ chỉ sử dụng bản sao đó để ước tính các giá trị mục tiêu.

### 00:02:10.000 - 00:02:14.000
Mạng lưới thần kinh này được gọi là mạng mục tiêu.

### 00:02:15.000 - 00:02:21.000
Sự khác biệt là khi chúng tôi thực hiện giảm độ dốc để giảm thiểu sai số của ước tính, mục tiêu này

### 00:02:21.000 - 00:02:23.000
mạng sẽ không được sửa đổi.

### 00:02:24.000 - 00:02:26.000
Các thông số của nó sẽ giữ nguyên.

### 00:02:26.000 - 00:02:32.000
Điều này có nghĩa là ước tính mục tiêu sẽ duy trì ổn định trong quá trình học tập.

### 00:02:32.000 - 00:02:39.000
Vì lý do này, trong biểu thức của hàm chi phí, chúng ta viết mục tiêu theta là mạng nơ-ron

### 00:02:39.000 - 00:02:44.000
tham số vì những ước tính này được thực hiện bằng cách sử dụng mạng mục tiêu.

### 00:02:45.000 - 00:02:53.000
Sau đó, cứ sau vài tập sẽ tạo một bản sao mới của mạng lưới thần kinh chính và chúng tôi sẽ sử dụng bản sao mới đó

### 00:02:53.000 - 00:02:59.000
để ước tính các giá trị mục tiêu để những ước tính giá trị mục tiêu đó cũng trở nên chính xác hơn trong suốt

### 00:02:59.000 - 00:03:01.000
quá trình học tập.

### 00:03:01.000 - 00:03:06.000
Mạng mục tiêu sẽ can thiệp vào ba dòng mã này.

### 00:03:06.000 - 00:03:12.000
Đầu tiên, trước khi vào vòng lặp chính, chúng ta sẽ tạo bản sao của mạng nơ-ron.

### 00:03:12.000 - 00:03:19.000
Sau đó, khi tính hàm mất mát, chúng tôi sẽ sử dụng bản sao của mạng nơ-ron để tạo ra các ước tính

### 00:03:19.000 - 00:03:21.000
được bao gồm trong giá trị mục tiêu.

### 00:03:21.000 - 00:03:27.000
Và sau đó mỗi K tập của môi trường sẽ đồng bộ hóa mạng lưới thần kinh.

