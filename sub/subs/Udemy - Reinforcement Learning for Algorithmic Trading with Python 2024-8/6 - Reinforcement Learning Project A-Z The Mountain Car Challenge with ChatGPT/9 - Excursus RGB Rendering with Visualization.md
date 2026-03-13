## Nội dung

### 00:00:00.000 - 00:00:05.600
Trong bài giảng trước, chúng ta đã thấy rằng chúng ta có thể lên tới đỉnh núi một cách tình cờ

### 00:00:05.600 - 00:00:12.000
và chúng ta chỉ cần tăng số tập, số bước cũng như với sự kết xuất của con người.

### 00:00:12.000 - 00:00:17.800
Tuy nhiên, sẽ thật tuyệt nếu chỉ thấy ít nhất một tập thành công hoạt động trực tiếp.

### 00:00:17.800 - 00:00:26.800
Và trong bài giảng nhỏ này, tôi sẽ trình bày cách chúng ta có thể lưu và hiển thị các khung cho một tập thành công.

### 00:00:26.800 - 00:00:32.799
Vì vậy, đây chỉ là một công cụ kiểm tra và chúng ta sẽ không cần mã ở đây cho một trong những tập tiếp theo bài giảng.

### 00:00:32.799 - 00:00:37.799
Vì vậy, hãy để tôi nêu bật những thay đổi và sửa đổi.

### 00:00:37.799 - 00:00:42.399
Vì vậy, bây giờ chúng ta phải chọn mảng RGB chế độ kết xuất.

### 00:00:42.399 - 00:00:47.200
Vì vậy, chúng ta lưu các khung hình trong một mảng RGB trong một mảng có nhiều mảng.

### 00:00:47.200 - 00:00:51.600
Và sau đó chúng ta thêm vào danh sách trống các khung hình thành công.

### 00:00:51.600 - 00:00:57.200
Vì vậy, ở đây chúng ta lưu tất cả các khung hình của các tập thành công.

### 00:00:57.200 - 00:01:02.200
Và sau đó, đối với mỗi tập phim, chúng ta an toàn và thu thập tất cả các khung hình.

### 00:01:02.200 - 00:01:06.200
Vì vậy, tất cả hình ảnh sau mỗi hành động.

### 00:01:06.200 - 00:01:13.799
Và sau đó rất quan trọng, chúng ta phải chụp lại khung, mỗi khung hình là một mảng RGB.

### 00:01:13.799 - 00:01:17.599
Và điều này thực sự làm chậm mã ở đây.

### 00:01:17.599 - 00:01:21.599
Và sau đó chúng tôi nối từng khung hình vào khung hình.

### 00:01:21.599 - 00:01:28.399
Vì vậy, với mỗi tập, chúng ta có các khung danh sách với nhiều khung.

### 00:01:28.399 - 00:01:30.199
Và phần còn lại giống nhau.

### 00:01:30.199 - 00:01:34.199
Và sau đó chúng ta nói rằng nếu tập thành công,

### 00:01:34.199 - 00:01:43.099
chúng ta không chỉ tăng số lượng thành công này mà còn thêm danh sách khung vào danh sách khung thành công.

### 00:01:43.199 - 00:01:48.699
Vì vậy, ở đây chúng ta lưu tất cả các khung của các tập thành công.

### 00:01:51.500 - 00:01:52.899
Và bây giờ chúng ta hãy làm điều này ở đây.

### 00:01:52.899 - 00:01:56.699
Vì vậy, chẳng hạn, chúng ta có thể chạy 100 tập.

### 00:01:56.699 - 00:02:02.899
Và chúng ta có thể tăng hoặc tăng thêm số tập tối đa là 3000.

### 00:02:02.899 - 00:02:08.099
Và thật tình cờ, chúng ta sẽ có tập này hoặc tập kia thành công.

### 00:02:08.099 - 00:02:09.699
Vì vậy, hãy chạy mã ở đây.

### 00:02:09.699 - 00:02:18.099
Và quá trình này có thể mất vài phút vì phương pháp ngẫu nhiên làm chậm hoạt động của chúng tôi ở đây.

### 00:02:18.099 - 00:02:25.899
Vì vậy, hãy chạy và đợi ở đây cho đến khi chúng ta đạt đến 100 tập ngẫu nhiên.

### 00:02:27.899 - 00:02:30.500
Vì vậy, bây giờ nó đang chạy.

### 00:02:30.500 - 00:02:35.500
Và vì chúng tôi chỉ in ra mỗi 100 tập. các tập.

### 00:02:35.500 - 00:02:38.000
Vì vậy chúng ta sẽ chỉ xem tập cuối cùng.

### 00:02:38.000 - 00:02:41.800
Vì vậy, hãy đợi ở đây, có thể là vài phút.

### 00:02:41.800 - 00:02:51.800
Được rồi, sau 100 tập, chúng ta có đúng một tập thành công với 2783 bước.

### 00:02:51.800 - 00:02:57.800
Và do đó cần có một số nội dung ở đây trong các khung hình thành công.

### 00:02:57.800 - 00:03:04.099
Vậy tổng cộng, chúng ta có ở đây 2783 khung hình cho một tập.

### 00:03:04.099 - 00:03:07.199
Và bây giờ chúng ta hãy cố gắng làm cho những khung hình này trở nên sống động.

### 00:03:07.199 - 00:03:11.199
Và chúng ta có thể làm điều này với hình ảnh từ PIL.

### 00:03:11.199 - 00:03:14.099
Vậy đó là cái gối thư viện.

### 00:03:14.099 - 00:03:17.699
Và có thể bạn cần cài đặt nó.

### 00:03:17.699 - 00:03:22.299
Vì vậy, trong môi trường phòng tập thể dục của tôi, tôi đã cài đặt gối ở đây.

### 00:03:22.299 - 00:03:27.299
Và có thể bạn cần cài đặt nó trước.

### 00:03:27.299 - 00:03:29.599
Nhưng sẽ không có vấn đề gì ở đây.

### 00:03:29.599 - 00:03:35.399
Vì vậy, trước tiên chúng ta cần chuyển đổi các khung được lưu trữ trong NAMPIA RACE thành hình ảnh PIL.

### 00:03:37.899 - 00:03:43.899
Và sau đó chúng ta thực sự có thể hiển thị các hình ảnh dưới dạng một bộ phim nhỏ.

### 00:03:46.399 - 00:03:47.399
Và hãy xem này.

### 00:03:47.399 - 00:03:51.599
Vậy đây là tập thành công, tập ngẫu nhiên.

### 00:03:51.599 - 00:03:56.399
Và nó khá nhanh vì chúng ta đã vô hiệu hóa chế độ ngủ ở đây.

### 00:03:59.099 - 00:04:02.399
Vì vậy, chúng ta có thể làm cho nó chậm hơn nếu chúng ta cho phép chế độ ngủ ở đây.

### 00:04:02.500 - 00:04:05.200
Bây giờ chúng ta có thể thấy rằng nó lấy được động lượng.

### 00:04:05.200 - 00:04:07.200
Vì vậy, ô tô của chúng ta lấy được động lượng.

### 00:04:09.300 - 00:04:15.200
Và sau đó nó sẽ tình cờ lên đến đỉnh núi.

### 00:04:15.200 - 00:04:16.500
Vậy là đây.

### 00:04:16.500 - 00:04:19.899
Vậy đây là tập thành công này.

### 00:04:19.899 - 00:04:22.000
Và đây là một công cụ tìm kiếm nhỏ.

### 00:04:22.000 - 00:04:29.899
Làm thế nào chúng ta có thể bắt được các tập phim thành công từ đây trong trường hợp này 100 ngẫu nhiên các tập.

### 00:04:29.899 - 00:04:33.099
Nhưng bây giờ thực sự đã đến lúc đào tạo đặc vụ của chúng ta.

### 00:04:33.099 - 00:04:40.500
Để chúng ta có thể lên đến đỉnh núi trong mỗi tập phim chỉ với 150 bước hoặc hơn.

### 00:04:40.500 - 00:04:43.399
Và đó là kế hoạch cho các bài giảng tiếp theo.

### 00:04:43.399 - 00:04:45.299
Cảm ơn bạn đã xem và hẹn gặp lại bạn ở đó.

### 00:04:45.299 - 00:04:46.299
Tạm biệt.

