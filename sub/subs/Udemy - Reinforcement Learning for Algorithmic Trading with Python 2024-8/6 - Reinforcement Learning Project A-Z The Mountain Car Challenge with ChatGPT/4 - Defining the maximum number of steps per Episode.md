## Nội dung

### 00:00:00.000 - 00:00:05.719
Được rồi, trong bài giảng trước chúng ta đã thấy rằng tập ngẫu nhiên của chúng ta sẽ chạy mãi mãi trừ khi

### 00:00:05.719 - 00:00:09.380
chúng ta ngẫu nhiên lên đến đỉnh núi.

### 00:00:09.380 - 00:00:15.759
Tuy nhiên, có thể tốt hơn là dừng tập sau một số bước tối đa được xác định trước và

### 00:00:15.759 - 00:00:23.559
đó là lý do tại sao trong một trong các phiên bản gần đây, tính năng cắt ngắn đã được thêm vào đây vào đầu ra.

### 00:00:23.559 - 00:00:29.600
Và giá trị mặc định thực sự là sai, nhưng sẽ trở thành true nếu bạn đạt đến số bước tối đa

### 00:00:29.600 - 00:00:31.360
.

### 00:00:31.360 - 00:00:37.960
Nhưng hãy hỏi ở đây để làm theo để điều chỉnh một chút.

### 00:00:37.960 - 00:00:42.600
Và chúng ta có thể sử dụng lời nhắc sau ở đây.

### 00:00:42.600 - 00:00:46.040
Vì vậy, nó không tự động dừng trừ khi đạt được mục tiêu.

### 00:00:46.040 - 00:00:51.600
Hãy điều chỉnh và thêm số bước tối đa cho mỗi tập.

### 00:00:51.600 - 00:00:59.560
Vì vậy, hãy xem những gì chúng ta nhận được ở đây.

### 00:00:59.560 - 00:01:06.280
Vì vậy, chắc chắn đây là mã được cập nhật với số bước tối đa cho mỗi tập.

### 00:01:06.280 - 00:01:12.159
Vì vậy, nó thêm vào đây số bước tối đa bằng ví dụ 200 và sau đó nó cũng thêm một số thứ vào

### 00:01:12.159 - 00:01:13.640
 Value.

### 00:01:13.640 - 00:01:20.640
Vì vậy, chúng tôi tiếp tục thực hiện các hành động ở đây chừng nào chúng tôi chưa hoàn thành và chừng nào chúng tôi chưa đạt được

### 00:01:20.640 - 00:01:25.040
đến các bước tối đa.

### 00:01:25.040 - 00:01:30.280
Thậm chí thực tế thì điều này sẽ hoạt động, nhưng có một tùy chọn tốt hơn, một tùy chọn mới hơn và có vẻ như

### 00:01:30.280 - 00:01:35.520
GPT40 cũng không thực sự biết về nó.

### 00:01:35.520 - 00:01:44.760
Vì vậy, thực tế khi tạo môi trường ở đây, chúng ta cũng có thể xác định số lượng

### 00:01:44.760 - 00:01:45.760
tập tối đa ở đây.

### 00:01:45.760 - 00:01:49.360
Vì vậy, đây là tham số các bước tập tối đa.

### 00:01:49.359 - 00:01:59.079
Và chúng ta cũng có thể sử dụng ở đây đầu ra mới bị cắt bớt và hãy yêu cầu GPT40 sử dụng những cái này

### 00:01:59.079 - 00:02:00.840
mới Hàm.

### 00:02:00.840 - 00:02:03.319
Vì vậy, chúng ta hãy thử lời nhắc sau đây.

### 00:02:03.319 - 00:02:11.360
Vui lòng sử dụng tham số số bước tập tối đa trong gym.make và cũng bị cắt bớt.

### 00:02:11.360 - 00:02:17.560
Vì vậy, chúng tôi trích xuất ở đây từ hành động.

### 00:02:17.560 - 00:02:24.759
Vì vậy, bây giờ nó sử dụng ở đây số bước tập tối đa bằng ví dụ 200 và sau đó nó cũng sử dụng bị cắt ngắn.

### 00:02:24.759 - 00:02:29.039
Vì vậy, mặc dù chúng tôi chưa lên đến đỉnh núi và chưa đạt đến

### 00:02:29.039 - 00:02:36.920
đến các bước tập tối đa, chúng tôi thực sự thực hiện hết hành động này đến hành động khác và kiểm tra new

### 00:02:36.920 - 00:02:39.759
nêu và cập nhật phần thưởng.

### 00:02:40.759 - 00:02:49.479
Và bây giờ, hãy sao chép mã ở đây và thử xem.

### 00:02:49.479 - 00:03:05.919
Vì vậy, hãy sao chép và dán và bây giờ hãy chạy mã mới.

### 00:03:05.919 - 00:03:11.839
Vì vậy, đây là một tập ngẫu nhiên khác nhưng nó sẽ tự động dừng sau 200 hành động.

### 00:03:11.839 - 00:03:16.159
Vì vậy, đó là trường hợp hiện tại và chúng tôi có bản in cuối cùng.

### 00:03:16.159 - 00:03:21.119
Vì vậy, chúng tôi có 200 bước và 200 lần chúng tôi có phần thưởng là trừ một.

### 00:03:21.119 - 00:03:26.759
Vì vậy, chúng tôi đã không đạt đến đỉnh của phần này. Mountain.

### 00:03:26.759 - 00:03:29.919
Vậy đây là tập ngẫu nhiên đầu tiên.

### 00:03:29.919 - 00:03:33.919
Cảm ơn bạn đã xem và mong được gặp bạn trong các bài giảng tiếp theo.

### 00:03:33.919 - 00:03:34.919
Tạm biệt.

