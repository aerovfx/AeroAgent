## Nội dung

### 00:00:00.000 - 00:00:05.000
Trong video này, chúng ta sẽ tìm hiểu về một kỹ thuật sẽ giúp chúng ta trong quá trình học tập.

### 00:00:06.000 - 00:00:08.000
Kỹ thuật này là học song song.

### 00:00:09.000 - 00:00:15.000
Khi tác nhân thực hiện một nhiệm vụ, nó sẽ thực hiện các hành động sửa đổi trạng thái của môi trường.

### 00:00:15.000 - 00:00:19.000
Thông thường, những hành động này có ảnh hưởng vừa phải đến trạng thái của nhiệm vụ.

### 00:00:19.000 - 00:00:26.000
Điều này có nghĩa là các trạng thái kế tiếp có xu hướng rất giống với trạng thái trước đó, và đây là

### 00:00:26.000 - 00:00:28.000
một vấn đề khi chúng ta làm việc với mạng lưới thần kinh.

### 00:00:28.000 - 00:00:35.000
Vấn đề là khi chúng ta cập nhật một giá trị do mạng nơ-ron tạo ra, chúng ta không chỉ sửa đổi

### 00:00:35.000 - 00:00:38.000
giá trị đó mà còn cả các giá trị lân cận.

### 00:00:39.000 - 00:00:46.000
Nếu chúng ta cập nhật mạng lưới thần kinh với một loạt trạng thái rất giống nhau thì thực tế sẽ lặp lại

### 00:00:46.000 - 00:00:53.000
cùng một bản cập nhật nhiều lần và chính sách có thể bắt đầu đề xuất một số hành động quá thường xuyên.

### 00:00:54.000 - 00:00:58.000
Ngay cả ở những bang không thể khắc phục vấn đề này, chúng tôi có hai lựa chọn.

### 00:00:58.000 - 00:01:04.000
Cái đầu tiên, bạn đã biết rồi vì nó là cái chúng tôi đã sử dụng với q-learning sâu và sâu

### 00:01:04.000 - 00:01:05.000
thuật toán.

### 00:01:06.000 - 00:01:08.000
Tôi đang nói về việc phát lại trải nghiệm.

### 00:01:09.000 - 00:01:16.000
Khi sử dụng kỹ thuật này, chúng tôi cập nhật mạng lưới thần kinh bằng một loạt trải nghiệm được chọn ngẫu nhiên

### 00:01:16.000 - 00:01:19.000
nên chúng độc lập với nhau và do đó khác nhau.

### 00:01:20.000 - 00:01:25.000
Những trải nghiệm có thể thuộc về những giai đoạn khác nhau và những trạng thái hoàn toàn khác nhau.

### 00:01:25.000 - 00:01:31.000
Vì vậy, khi chúng tôi cập nhật mạng nơ-ron, chúng tôi sẽ sửa đổi nó theo cách ảnh hưởng đến tất cả các trạng thái khác nhau này

### 00:01:31.000 - 00:01:33.000
một cách cân bằng.

### 00:01:34.000 - 00:01:40.000
Một cách khác để giải quyết vấn đề về các trạng thái liên quan là cách mà chúng ta sẽ sử dụng với chính sách.

### 00:01:40.000 - 00:01:47.000
các phương pháp gradient và nó bao gồm việc tạo ra một số môi trường song song với đó tác nhân

### 00:01:47.000 - 00:01:49.000
sẽ tương tác cùng một lúc.

### 00:01:50.000 - 00:01:56.000
Nó hơi giống những người chơi cờ vua chơi mười ván cùng một lúc với những đối thủ khác nhau.

### 00:01:56.000 - 00:02:04.000
Chúng tôi sẽ tạo ra một môi trường song song sẽ giữ bên trong một số môi trường bình thường nhất định.

### 00:02:04.000 - 00:02:10.000
Và cách tương tác với môi trường song song này cũng giống như khi tác nhân gặp một tình huống bình thường

### 00:02:10.000 - 00:02:11.000
môi trường.

### 00:02:11.000 - 00:02:18.000
Khi môi trường bắt đầu tác vụ, tác nhân sẽ nhận được một trạng thái cho mỗi môi trường độc lập

### 00:02:18.000 - 00:02:26.000
mà nó sắp phải đối mặt, và nó sẽ nhận các trạng thái đó dưới dạng một vectơ cột trong đó mỗi hàng là một cá thể

### 00:02:26.000 - 00:02:26.000
tình trạng.

### 00:02:27.000 - 00:02:34.000
Sau đó, tác nhân sẽ chọn một hành động cho từng trạng thái nhận được và sẽ chuyển hành động đó tới

### 00:02:34.000 - 00:02:37.000
môi trường song song dưới dạng vectơ cột.

### 00:02:37.000 - 00:02:40.000
Trong vectơ cột này, mỗi hàng là một hành động riêng lẻ.

### 00:02:41.000 - 00:02:47.000
Môi trường song song sẽ đảm nhiệm việc chuyển từng hành động đó sang môi trường tương ứng của nó

### 00:02:47.000 - 00:02:48.000
và môi trường.

### 00:02:48.000 - 00:02:55.000
Để đáp lại hành động đó sẽ quay trở lại các vectơ cột, một vectơ có phần thưởng nhận được do đó

### 00:02:55.000 - 00:03:03.000
thực hiện những hành động đó trong môi trường của nó và hành động khác với các trạng thái tiếp theo đạt được sau khi thực hiện

### 00:03:03.000 - 00:03:05.000
từng hành động trong từng môi trường.

