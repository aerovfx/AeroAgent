## Nội dung

### 00:00:00.000 - 00:00:06.000
Trong video này, chúng ta sẽ triển khai trải nghiệm của mình, phát lại bộ nhớ trong đó chúng ta sẽ lưu trữ từng

### 00:00:06.000 - 00:00:12.000
một trong những chuyển đổi trạng thái mà tác nhân sẽ gặp phải khi tương tác với môi trường.

### 00:00:12.000 - 00:00:20.000
Và mỗi một trong những chuyển đổi này sẽ chứa trạng thái đã truy cập hành động, nhận phần thưởng nhận được,

### 00:00:20.000 - 00:00:24.000
và trạng thái tiếp theo đạt được sau khi thực hiện hành động.

### 00:00:24.000 - 00:00:31.000
Sau đó, từ ký ức này, tại mọi thời điểm, chúng ta sẽ thu được một loạt kinh nghiệm mà chúng ta sẽ sử dụng.

### 00:00:31.000 - 00:00:33.000
để cải thiện việc ước tính mạng lưới thần kinh của chúng tôi.

### 00:00:35.000 - 00:00:38.000
Lớp này sẽ gọi nó là bộ nhớ phát lại.

### 00:00:45.000 - 00:00:47.000
Và chúng ta sẽ có bốn phương pháp.

### 00:00:49.000 - 00:00:52.000
Đầu tiên trong số đó sẽ là phương thức chèn.

### 00:00:53.000 - 00:00:55.000
Điều đó sẽ cho phép chúng tôi chèn.

### 00:00:56.000 - 00:00:58.000
Sự chuyển đổi trạng thái trong bộ nhớ.

### 00:01:03.000 - 00:01:05.000
Cái tiếp theo được gọi là mẫu.

### 00:01:07.000 - 00:01:08.000
Và nó sẽ cho phép chúng tôi lấy mẫu.

### 00:01:09.000 - 00:01:12.000
Hàng loạt trải nghiệm từ ký ức.

### 00:01:25.000 - 00:01:29.000
Hàm thứ ba được gọi là can sample.

### 00:01:34.000 - 00:01:36.000
Và nó sẽ cho chúng ta một giá trị boolean.

### 00:01:38.000 - 00:01:47.000
Nó sẽ trả về true nếu bộ nhớ có đủ chuyển đổi trạng thái để bắt đầu vẽ các lô từ nó.

### 00:01:47.000 - 00:01:49.000
Nếu không nó sẽ trả về sai.

### 00:01:51.000 - 00:01:53.000
Và cuối cùng, chúng ta sẽ thực hiện.

### 00:01:55.000 - 00:01:58.000
Phương pháp thứ tư gọi là Len.

### 00:01:59.000 - 00:02:07.000
Tất cả các đối tượng có thể được lặp lại đều có phương thức này và nó cho chúng ta biết đối tượng này có bao nhiêu phần tử

### 00:02:07.000 - 00:02:08.000
chứa.

### 00:02:10.000 - 00:02:14.000
Nhưng trước khi thực hiện những phương thức đó, chúng ta phải khởi tạo lớp này.

### 00:02:16.000 - 00:02:19.000
Và để làm được điều đó, chúng ta phải ghi đè phương thức init.

### 00:02:20.000 - 00:02:22.000
Chúng tôi sẽ chuyển nó như một cuộc tranh luận.

### 00:02:22.000 - 00:02:24.000
Một giá trị được gọi là dung lượng.

### 00:02:25.000 - 00:02:29.000
Và nó sẽ cho chúng ta biết số lần chuyển đổi tối đa mà bộ nhớ này có thể lưu trữ.

### 00:02:31.000 - 00:02:33.000
Hãy cho nó một triệu.

### 00:02:37.000 - 00:02:41.000
Sau đó chúng ta sẽ khai báo biến năng lực bản thân.

### 00:02:42.000 - 00:02:47.000
Và chúng ta sẽ làm cho nó bằng tham số dung lượng được truyền cho hàm tạo.

### 00:02:48.000 - 00:02:51.000
Sau đó chúng ta sẽ lưu trữ trong một biến gọi là bộ nhớ tự chấm.

### 00:02:53.000 - 00:02:59.000
Một danh sách trống nơi chúng tôi sẽ lưu trữ các hiệu ứng chuyển tiếp mà chúng tôi sẽ chèn vào.

### 00:03:02.000 - 00:03:06.000
Và chúng ta sẽ tạo một biến thứ ba gọi là khả năng tự sở hữu bản thân.

### 00:03:08.000 - 00:03:10.000
Điều đó sẽ cho chúng ta biết vào từng thời điểm.

### 00:03:13.000 - 00:03:18.000
Vị trí mà chúng ta phải chèn quá trình chuyển đổi tiếp theo.

### 00:03:19.000 - 00:03:24.000
Bây giờ, khi đã khởi tạo lớp, chúng ta sẽ định nghĩa phương thức chèn.

### 00:03:25.000 - 00:03:29.000
Điều đó sẽ lấy làm đối số chuyển đổi trạng thái.

### 00:03:29.000 - 00:03:33.000
Và quá trình chuyển đổi trạng thái đó sẽ là một danh sách có bốn phần tử.

### 00:03:33.000 - 00:03:38.000
Trạng thái, hành động, phần thưởng và trạng thái tiếp theo.

### 00:03:40.000 - 00:03:42.000
Điều đầu tiên chúng tôi sẽ làm là kiểm tra.

### 00:03:45.000 - 00:03:48.000
Nếu số lượng chuyển tiếp được chèn vào bộ nhớ.

### 00:03:49.000 - 00:03:50.000
Nhỏ hơn khả năng của nó.

### 00:03:57.000 - 00:04:01.000
Và nếu đúng như vậy, chúng tôi sẽ thêm vào bộ nhớ.

### 00:04:02.000 - 00:04:04.000
Một mục có giá trị?

### 00:04:04.000 - 00:04:04.000
Không có.

### 00:04:08.000 - 00:04:11.000
Và ở vị trí của mục mới được chèn này.

### 00:04:20.000 - 00:04:22.000
Chúng tôi sẽ chèn quá trình chuyển đổi.

### 00:04:24.000 - 00:04:27.000
Và sau đó chúng tôi sẽ cập nhật biến vị trí.

### 00:04:28.000 - 00:04:30.000
Bằng cách thêm một vào nó.

### 00:04:32.000 - 00:04:35.000
Và điều gì sẽ xảy ra nếu chúng ta vượt quá dung lượng của bộ nhớ?

### 00:04:36.000 - 00:04:38.000
Đó là nó chúng tôi đã chèn vào.

### 00:04:40.000 - 00:04:42.000
Tất cả các hiệu ứng chuyển tiếp mà chúng tôi có thể chèn vào.

### 00:04:43.000 - 00:04:46.000
Sau đó chúng ta sẽ quay trở lại vị trí đầu tiên.

### 00:04:51.000 - 00:04:52.000
Theo cách đó.

### 00:04:52.000 - 00:04:58.000
Mỗi lần chúng tôi chèn một chuyển đổi mới, nếu chúng tôi chưa lấp đầy dung lượng, chúng tôi sẽ nhường chỗ cho

### 00:04:58.000 - 00:04:59.000
bộ nhớ.

### 00:05:00.000 - 00:05:03.000
Và chúng ta sẽ đặt ở vị trí mới đó.

### 00:05:03.000 - 00:05:04.000
Sự chuyển tiếp mới.

### 00:05:06.000 - 00:05:09.000
Và sau đó chúng ta sẽ di chuyển con trỏ đến vị trí tiếp theo.

### 00:05:09.000 - 00:05:14.000
Và nếu dung lượng bộ nhớ đầy thì chúng ta sẽ thực hiện phần này.

### 00:05:16.000 - 00:05:20.000
Và chúng ta sẽ chỉ ghi đè lên các quá trình chuyển đổi.

### 00:05:21.000 - 00:05:25.000
Rằng trước đây chúng tôi đã lưu trữ ở vị trí đó.

### 00:05:31.000 - 00:05:34.000
Được rồi, bây giờ chúng ta đã có phương thức chèn.

### 00:05:35.000 - 00:05:38.000
Trong video tiếp theo, chúng ta sẽ triển khai phương pháp mẫu.

### 00:05:39.000 - 00:05:40.000
Tôi sẽ gặp bạn ở đó.

