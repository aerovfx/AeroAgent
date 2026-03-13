## Nội dung

### 00:00:03.000 - 00:00:05.000
Bây giờ hãy xem kết quả của thuật toán.

### 00:00:07.000 - 00:00:08.000
Vì điều đó.

### 00:00:08.000 - 00:00:11.000
Chúng ta sẽ sử dụng chức năng thống kê cốt truyện.

### 00:00:12.000 - 00:00:16.000
Và chúng ta sẽ cung cấp cho nó từ điển thống kê làm đầu vào.

### 00:00:16.000 - 00:00:18.000
Hãy chạy tế bào.

### 00:00:21.000 - 00:00:27.000
Và như bạn có thể thấy khi bắt đầu quá trình học tập, người đại diện nhận được kết quả rất tệ.

### 00:00:27.000 - 00:00:31.000
Như bạn có thể thấy ở đây, nó nhận được kết quả là -200.

### 00:00:32.000 - 00:00:41.000
Nhưng khi kết thúc quá trình học tập, sau khoảng 1500 tập, nó thu được lợi nhuận xấp xỉ

### 00:00:41.000 - 00:00:43.000
-120.

### 00:00:43.000 - 00:00:46.000
Tức là nó có khả năng giải quyết nhiệm vụ.

### 00:00:46.000 - 00:00:49.000
Sau khoảng 120 lần di chuyển.

### 00:00:50.000 - 00:00:57.000
Tiếp theo, chúng ta sẽ kiểm tra chi phí để đi từ mỗi tiểu bang đến mục tiêu.

### 00:00:57.000 - 00:01:04.000
Để làm được điều đó, chúng ta sẽ sử dụng chi phí cốt truyện để hoạt động và chúng ta sẽ cung cấp cho nó môi trường,

### 00:01:04.000 - 00:01:08.000
mạng lưới thần kinh và hai nhãn.

### 00:01:11.000 - 00:01:15.000
Một cho trục x, sẽ là vị trí ô tô.

### 00:01:20.000 - 00:01:25.000
Và một cho trục y tương ứng với vận tốc của ô tô.

### 00:01:29.000 - 00:01:30.000
Hãy chạy tế bào này.

### 00:01:31.000 - 00:01:33.000
Và ở đây chúng tôi có nó.

### 00:01:33.000 - 00:01:35.000
Chi phí ước tính để đi.

### 00:01:37.000 - 00:01:42.000
Trạng thái này có chi phí cao nhất để đi vì mạng lưới thần kinh ước tính rằng sẽ mất nhiều thời gian

### 00:01:42.000 - 00:01:45.000
thời gian để người đại diện đạt được mục tiêu từ trạng thái đó.

### 00:01:45.000 - 00:01:52.000
Mặt khác, bang có chi phí đi thấp nhất là bang tương ứng với địa điểm

### 00:01:52.000 - 00:01:53.000
của lá cờ.

### 00:01:53.000 - 00:01:58.000
Đó là khi xe ở vị trí 0,6.

### 00:02:03.000 - 00:02:10.000
Nếu bạn còn nhớ, chi phí để sử dụng mạng nơ-ron rất giống với chi phí để sử dụng mà chúng tôi đã thu được

### 00:02:10.000 - 00:02:13.000
sử dụng các phương pháp tổng hợp trạng thái từ phần trước.

### 00:02:13.000 - 00:02:21.000
Sự khác biệt là trong trường hợp này, chức năng sẽ mượt mà hơn nhiều mà không có sự thay đổi lớn từ trạng thái này sang trạng thái khác.

### 00:02:21.000 - 00:02:23.000
những cái liền kề.

### 00:02:25.000 - 00:02:31.000
Điều tiếp theo chúng ta cần làm là hiển thị chính sách và chúng ta sẽ thực hiện điều đó bằng cách sử dụng cốt truyện.

### 00:02:31.000 - 00:02:33.000
Chức năng Q tối đa.

### 00:02:35.000 - 00:02:42.000
Và chúng ta sẽ chuyển sang hàm này môi trường, mạng lưới thần kinh và các nhãn cho trục X và Y.

### 00:02:55.000 - 00:03:02.000
Cũng như một đối số khác sẽ bao gồm các nhãn cho từng hành động mà tác nhân có thể

### 00:03:02.000 - 00:03:02.000
lấy.

### 00:03:04.000 - 00:03:06.000
Đó là sự di chuyển trở lại.

### 00:03:10.000 - 00:03:12.000
Không hề di chuyển chút nào.

### 00:03:14.000 - 00:03:16.000
Hoặc tiến về phía trước.

### 00:03:17.000 - 00:03:18.000
Hãy chạy tế bào này.

### 00:03:20.000 - 00:03:21.000
Và ở đây chúng tôi có nó.

### 00:03:22.000 - 00:03:25.000
Hình vuông này ở đây là không gian trạng thái.

### 00:03:26.000 - 00:03:32.000
Và ở mỗi sự kết hợp giữa vị trí của ô tô và vận tốc của nó, chính sách sẽ đề xuất một

### 00:03:32.000 - 00:03:32.000
hoạt động.

### 00:03:33.000 - 00:03:37.000
Ở nhóm bang này, chính sách khuyến nghị nên tiến về phía trước.

### 00:03:38.000 - 00:03:39.000
Trong tất cả điều này.

### 00:03:39.000 - 00:03:41.000
Nó khuyên bạn nên quay lại.

### 00:03:45.000 - 00:03:48.000
Và có một số nơi khuyến nghị không nên di chuyển.

### 00:03:51.000 - 00:03:54.000
Nếu bạn nhìn vào vị trí ban đầu, điều nó khuyến nghị là hãy lùi lại.

### 00:03:56.000 - 00:04:00.000
Tức là ô tô sẽ chuyển động lùi lại và vận tốc của nó sẽ giảm đi.

### 00:04:02.000 - 00:04:11.000
Sau đó khi chúng ta quay lại đây, chính sách quy định xe di chuyển về phía trước cho đến khi vào

### 00:04:11.000 - 00:04:12.000
trong khu vực này.

### 00:04:13.000 - 00:04:21.000
Và sau đó nó quy định xe phải lùi lại để lấy thêm xung lực trước khi tiến về phía trước để đạt được

### 00:04:21.000 - 00:04:21.000
mục tiêu.

### 00:04:23.000 - 00:04:26.000
Điều cuối cùng mà chúng tôi sẽ kiểm tra là đại lý của chúng tôi.

### 00:04:29.000 - 00:04:34.000
Nhưng trước đó, chúng ta phải gọi lệnh Matplotlib trong dòng.

### 00:04:37.000 - 00:04:45.000
Vì vậy, Matplotlib ngừng sử dụng các biểu đồ tương tác và hiển thị kết quả của hàm tác nhân kiểm tra.

### 00:04:54.000 - 00:04:56.000
Hãy lặp lại tập phim hai lần.

### 00:04:59.000 - 00:05:02.000
Hãy xem kết quả mà chúng tôi thu được.

### 00:05:07.000 - 00:05:12.000
Và đúng như chúng ta mong đợi, nó tuân theo chính sách mà chúng ta đã thấy trong phần trước.

