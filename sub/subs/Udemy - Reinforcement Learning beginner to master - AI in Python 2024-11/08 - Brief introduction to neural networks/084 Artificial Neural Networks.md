## Nội dung

### 00:00:00.000 - 00:00:05.000
Trong video này, chúng ta sẽ tìm hiểu về một công cụ có khả năng xấp xỉ các hàm một cách rất linh hoạt.

### 00:00:05.000 - 00:00:07.000
và cách chính xác.

### 00:00:07.000 - 00:00:14.000
Trên thực tế, mạng nơ ron ngày nay đạt được kết quả tốt nhất với số lượng lớn các hàm xấp xỉ

### 00:00:14.000 - 00:00:15.000
nhiệm vụ.

### 00:00:15.000 - 00:00:21.000
Mạng lưới thần kinh là một lĩnh vực rất rộng lớn và phức tạp, nhưng chúng ta sẽ chỉ tập trung vào những điều cơ bản

### 00:00:21.000 - 00:00:24.000
chúng ta sẽ sử dụng trong học tăng cường sâu.

### 00:00:24.000 - 00:00:27.000
Mọi thứ khác đều là một chủ đề hấp dẫn.

### 00:00:27.000 - 00:00:29.000
Chúng ta sẽ để nó cho một khóa học khác.

### 00:00:29.000 - 00:00:32.000
Nhưng chính xác thì mạng lưới thần kinh nhân tạo là gì?

### 00:00:32.000 - 00:00:40.000
Chà, chúng là một hệ thống máy tính lấy cảm hứng từ mạng lưới thần kinh sinh học cấu thành nên bộ não của chúng ta.

### 00:00:41.000 - 00:00:48.000
Và chúng tôi nghiên cứu chúng vì hệ thống máy tính này có thể giúp chúng tôi trong việc tính gần đúng các hàm giá trị.

### 00:00:48.000 - 00:00:55.000
Mạng nơ-ron có thể ước chừng các hàm bằng cách điều chỉnh một tập hợp các tham số mà chúng chứa.

### 00:00:56.000 - 00:01:03.000
Mạng lưới thần kinh có thể được biểu diễn bằng biểu đồ như thế này trong đó mỗi nút là một biểu đồ nhân tạo

### 00:01:03.000 - 00:01:06.000
nơ-ron mà chúng ta sẽ thảo luận sau.

### 00:01:07.000 - 00:01:13.000
Mỗi nơ-ron này được kết nối với những nơ-ron khác và kết nối đó được thể hiện bằng các cạnh

### 00:01:13.000 - 00:01:15.000
bạn nhìn thấy trong sơ đồ này.

### 00:01:16.000 - 00:01:18.000
Các nơ-ron được tổ chức theo lớp.

### 00:01:18.000 - 00:01:27.000
Đó là một nhóm các nơron được sắp xếp song song và một nhóm các lớp được kết nối với nhau gọi là nơron

### 00:01:27.000 - 00:01:28.000
mạng.

### 00:01:28.000 - 00:01:33.000
Các lớp có tên khác nhau tùy thuộc vào vị trí của chúng trong mạng lưới thần kinh.

### 00:01:34.000 - 00:01:41.000
Lớp đầu tiên nhận đầu vào bên ngoài và truyền chúng sang lớp tiếp theo, được gọi là

### 00:01:41.000 - 00:01:43.000
lớp đầu vào.

### 00:01:43.000 - 00:01:50.000
Hai lớp tiếp theo nằm bên trong mạng lưới thần kinh và không phát ra cũng như không nhận thông tin

### 00:01:50.000 - 00:01:54.000
từ bên ngoài, được gọi là các lớp ẩn.

### 00:01:55.000 - 00:02:01.000
Cuối cùng, lớp cuối cùng tạo ra kết quả của việc áp dụng mạng nơ-ron ra bên ngoài là

### 00:02:01.000 - 00:02:04.000
được gọi là lớp đầu ra.

### 00:02:04.000 - 00:02:11.000
Có một số lượng lớn các loại mạng lưới thần kinh tùy thuộc vào loại tổ chức và kết nối

### 00:02:11.000 - 00:02:12.000
của các nơ-ron thần kinh của nó.

### 00:02:12.000 - 00:02:18.000
Nhưng chúng ta sẽ sử dụng một loại cơ bản và rất nổi tiếng được gọi là mạng nơ-ron tiếp nối.

### 00:02:20.000 - 00:02:26.000
Loại mạng nơ-ron này được đặc trưng bởi thực tế là thông tin của mỗi lớp được truyền đi

### 00:02:26.000 - 00:02:30.000
chỉ chuyển tiếp đến lớp tiếp theo.

### 00:02:30.000 - 00:02:34.000
Tế bào thần kinh nhận tín hiệu từ các tế bào thần kinh khác.

### 00:02:34.000 - 00:02:39.000
Trong trường hợp này, nơ-ron này nhận đầu vào từ hai nơ-ron này.

### 00:02:39.000 - 00:02:47.000
Sau đó, nơ-ron này sẽ xử lý và tổng hợp các đầu vào đó và chuyển kết quả đến tất cả các nơ-ron khác.

### 00:02:47.000 - 00:02:48.000
mà nó được kết nối.

### 00:02:50.000 - 00:02:54.000
Tín hiệu này mà nơron lan truyền là các giá trị số.

### 00:02:54.000 - 00:03:01.000
Tế bào thần kinh nào sẽ ức chế hoặc khuếch đại trước khi chuyển nó sang lớp tiếp theo.

### 00:03:02.000 - 00:03:08.000
Nếu mỗi nơ-ron được kết nối với tất cả các nơ-ron ở lớp trước và lớp tiếp theo, chẳng hạn như lớp này

### 00:03:08.000 - 00:03:14.000
một ở đây, được kết nối với tất cả các nơ-ron ở lớp đầu vào và tất cả các nơ-ron ở lớp đầu ra

### 00:03:14.000 - 00:03:15.000
lớp.

### 00:03:16.000 - 00:03:23.000
Nếu đó là trường hợp của mọi nơ-ron trong lớp đó thì lớp này được gọi là lớp được kết nối đầy đủ.

### 00:03:24.000 - 00:03:31.000
Trong video sau, chúng ta sẽ xem từng tế bào thần kinh nhân tạo này là gì và vai trò của chúng trong cơ thể con người.

### 00:03:31.000 - 00:03:32.000
mạng lưới thần kinh.

