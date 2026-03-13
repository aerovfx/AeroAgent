## Nội dung

### 00:00:00.000 - 00:00:04.000
Trong phần này, chúng ta sẽ thấy một nhóm phương pháp mới học hỏi từ kinh nghiệm.

### 00:00:04.000 - 00:00:09.000
Những phương pháp này là nền tảng của nhiều thuật toán nâng cao và chúng ta sẽ xem các khái niệm mà chúng ta sẽ học

### 00:00:09.000 - 00:00:11.000
ở đây trong suốt phần còn lại của khóa học.

### 00:00:12.000 - 00:00:14.000
Chúng được gọi là các phương pháp sai phân tạm thời.

### 00:00:15.000 - 00:00:20.000
Chúng là một nhóm các phương pháp tìm hiểu các giá trị tối ưu dựa trên kinh nghiệm.

### 00:00:20.000 - 00:00:22.000
Giống như phương pháp Monte Carlo.

### 00:00:23.000 - 00:00:27.000
Trên thực tế, các phương pháp sai phân theo thời gian kết hợp các đặc điểm của Monte Carlo.

### 00:00:27.000 - 00:00:30.000
Các phương pháp có tính chất quy hoạch động.

### 00:00:31.000 - 00:00:38.000
Như trong phương pháp Monte Carlo, tác nhân sẽ đối mặt với môi trường tạo ra quỹ đạo với các trạng thái

### 00:00:38.000 - 00:00:43.000
đã ghé thăm, các hành động đã thực hiện và phần thưởng nhận được ở cuối tập.

### 00:00:43.000 - 00:00:49.000
Chúng tôi sẽ sử dụng trải nghiệm đó để cập nhật ước tính giá trị Q và chính sách.

### 00:00:50.000 - 00:00:55.000
Ngoài ra, như trong phương pháp Monte Carlo, chúng tôi không có mô hình động lực học môi trường.

### 00:00:56.000 - 00:01:02.000
Vì không có mô hình nên chúng tôi không thể sử dụng các giá trị trạng thái để hướng dẫn chính sách vì để làm được điều đó, chúng tôi sẽ

### 00:01:02.000 - 00:01:04.000
cần sự năng động của môi trường.

### 00:01:05.000 - 00:01:10.000
Thay vào đó, chúng tôi sẽ sử dụng giá trị Q để hướng dẫn chính sách.

### 00:01:10.000 - 00:01:14.000
Bởi vì các giá trị Q ngầm ước tính động thái môi trường.

### 00:01:14.000 - 00:01:19.000
Bằng cách đó, chính sách sẽ chỉ chọn hành động có giá trị Q cao nhất.

### 00:01:20.000 - 00:01:24.000
Ngoài ra, giống như trong lập trình động, chúng ta sẽ sử dụng bootstrapping.

### 00:01:25.000 - 00:01:34.000
Nghĩa là, chúng ta sẽ dựa vào ước tính của giá trị Q để đưa ra ước tính mới chính xác hơn.

### 00:01:36.000 - 00:01:40.000
Đây là quy tắc cập nhật của phương pháp đầu tiên mà chúng ta sẽ học có tên là Sahsa.

### 00:01:41.000 - 00:01:44.000
Như bạn thấy, chúng tôi cập nhật một giá trị.

### 00:01:44.000 - 00:01:50.000
Ước tính giá trị Q bằng cách sử dụng ước tính của giá trị Q khác.

### 00:01:52.000 - 00:01:57.000
Giá trị đại diện cho hành động tiếp theo được thực hiện ở trạng thái tiếp theo đã đạt được.

### 00:01:57.000 - 00:02:00.000
Và kỹ thuật này được gọi là bootstrapping.

### 00:02:02.000 - 00:02:07.000
Như ở Monte Carlo và các phương pháp lập trình động sẽ tuân theo mẫu lặp chính sách tổng quát

### 00:02:07.000 - 00:02:12.000
trong đó việc đánh giá chính sách và cải tiến chính sách sẽ luân phiên nhau.

### 00:02:12.000 - 00:02:18.000
Hãy nhớ rằng hai quá trình này cạnh tranh với nhau nhưng chúng cũng thúc đẩy nhau hướng tới mục tiêu chung.

### 00:02:18.000 - 00:02:23.000
giá trị q tối ưu và chính sách tối ưu.

### 00:02:26.000 - 00:02:31.000
Phương pháp Monte Carlo đợi đến cuối tập để cập nhật giá trị Q.

### 00:02:31.000 - 00:02:37.000
Họ chờ đợi vì họ cần tính toán lợi nhuận cho từng thời điểm và để làm được điều đó, chúng tôi cần tất cả

### 00:02:37.000 - 00:02:41.000
phần thưởng nhận được sau thời điểm đó.

### 00:02:42.000 - 00:02:49.000
Không giống như các phương pháp Monte Carlo, các phương pháp khác biệt theo thời gian thực hiện chu trình đánh giá chính sách này và

### 00:02:49.000 - 00:02:50.000
sự cải tiến.

### 00:02:50.000 - 00:02:55.000
Mỗi lần chúng ta thực hiện một hành động trong suốt tập phim mà không đợi đến cuối.

### 00:02:56.000 - 00:03:00.000
Bằng cách này, quá trình học tập diễn ra liên tục và thống nhất.

### 00:03:01.000 - 00:03:06.000
Đó là một lợi thế lớn vì việc học mà chúng ta thực hiện ở đầu tập phim sẽ ảnh hưởng đến

### 00:03:06.000 - 00:03:13.000
chính sách trong phần còn lại của tập phim, cải thiện việc ra quyết định và điều đó đơn giản là không thể

### 00:03:13.000 - 00:03:15.000
bằng phương pháp Monte Carlo.

