## Nội dung

### 00:00:00.000 - 00:00:05.000
Trong video này, chúng ta sẽ xem các phương pháp sai phân tạm thời giải quyết các nhiệm vụ điều khiển như thế nào.

### 00:00:05.000 - 00:00:11.000
Như chúng ta đã nói trước đây, chúng ta sẽ có một bảng giá trị với một mục nhập cho mỗi tổ hợp trạng thái và

### 00:00:11.000 - 00:00:12.000
hoạt động.

### 00:00:12.000 - 00:00:18.000
Mỗi mục sẽ chứa giá trị Q ước tính cho sự kết hợp đó.

### 00:00:19.000 - 00:00:21.000
Bây giờ hãy nhớ các phương trình bellman.

### 00:00:21.000 - 00:00:32.000
Giá trị Q là lợi nhuận kỳ vọng của một quỹ đạo bắt đầu ở trạng thái hiện tại và lấy

### 00:00:32.000 - 00:00:33.000
hành động hiện tại.

### 00:00:34.000 - 00:00:40.000
Lợi nhuận kỳ vọng này có thể được viết dưới dạng xác suất đạt được từng trạng thái kế tiếp.

### 00:00:41.000 - 00:00:49.000
Sau khi thực hiện các lần hành động, phần thưởng đạt được khi chúng ta đạt đến trạng thái đó, cộng với lợi nhuận chiết khấu

### 00:00:49.000 - 00:00:53.000
bắt đầu từ trạng thái đó, đó là giá trị của trạng thái đó.

### 00:00:54.000 - 00:01:02.000
Giá trị của trạng thái tiếp theo có thể được viết dưới dạng xác suất thực hiện mỗi hành động theo thời gian chính sách

### 00:01:02.000 - 00:01:07.000
giá trị Q của hành động đó, tức là hành động đó được kỳ vọng mang lại lợi nhuận.

### 00:01:09.000 - 00:01:14.000
Nhờ biểu thức này, chúng ta có thể sử dụng các giá trị mà tác nhân thu thập tương tác với môi trường

### 00:01:14.000 - 00:01:16.000
để ước tính các giá trị Q.

### 00:01:18.000 - 00:01:24.000
Mỗi khi tác nhân thực hiện một hành động, chúng tôi sẽ sử dụng phần thưởng mà nó đạt được trạng thái tiếp theo

### 00:01:24.000 - 00:01:30.000
nó đạt đến hành động mà chính sách chọn cho trạng thái tiếp theo đó.

### 00:01:30.000 - 00:01:34.000
Và bảng giá trị Q với các ước tính giá trị Q.

### 00:01:34.000 - 00:01:38.000
Để đưa ra ước tính về giá trị Q đó.

### 00:01:41.000 - 00:01:50.000
Với những yếu tố đó, chúng ta có thể ước tính giá trị Q theo cách này dưới dạng phần thưởng nhận được cộng với mức chiết khấu

### 00:01:50.000 - 00:01:52.000
ước lượng giá trị Q tiếp theo.

### 00:01:55.000 - 00:01:58.000
Nhưng bây giờ chúng tôi có hai ước tính riêng biệt.

### 00:01:59.000 - 00:02:06.000
Cái cũ và cái mới kết hợp thông tin thực tế từ môi trường.

### 00:02:07.000 - 00:02:14.000
Chúng ta sẽ so sánh hai ước tính này và sự khác biệt sẽ được gọi là sai số chênh lệch tạm thời.

### 00:02:16.000 - 00:02:24.000
Các phương pháp sai phân thời gian sử dụng sai số này, sai phân này để cập nhật các ước lượng giá trị Q, và chúng sẽ

### 00:02:24.000 - 00:02:26.000
làm theo công thức này.

### 00:02:28.000 - 00:02:30.000
Nếu bạn đang gặp deja vu.

### 00:02:30.000 - 00:02:34.000
Đó là bởi vì đây là cách hoạt động liên tục của Alpha Monte Carlo.

### 00:02:35.000 - 00:02:43.000
Chúng tôi đẩy ước tính theo hướng lợi nhuận mới được quan sát bởi một tỷ lệ phần trăm Alpha nhất định.

### 00:02:44.000 - 00:02:47.000
Sự khác biệt là bây giờ chúng tôi đang ước tính lợi nhuận.

### 00:02:48.000 - 00:02:57.000
Theo biểu thức này, phần thưởng nhận được ngay sau khi thực hiện hành động, cộng với số tiền chiết khấu

### 00:02:57.000 - 00:03:00.000
giá trị của hành động tiếp theo ở trạng thái tiếp theo.

### 00:03:01.000 - 00:03:10.000
Và điều này sẽ cho phép chúng tôi cập nhật ước tính cho giá trị Q ngay sau khi chúng tôi thực hiện hành động tại thời điểm

### 00:03:10.000 - 00:03:11.000
vào thời điểm tiếp theo.

### 00:03:12.000 - 00:03:18.000
Trong slide này, chúng ta có thể thấy rõ hơn điều gì sẽ xảy ra nếu chúng ta phân phối Alpha và tập hợp lại các thuật ngữ.

### 00:03:18.000 - 00:03:22.000
Chúng ta có thể diễn đạt quy tắc cập nhật như sau.

### 00:03:23.000 - 00:03:31.000
Bây giờ chúng ta có thể thấy rằng ước tính mới là trung bình có trọng số giữa ước tính cũ và ước tính mới.

### 00:03:32.000 - 00:03:36.000
Ước tính mới của giá trị Q sẽ là phần trăm alpha.

### 00:03:36.000 - 00:03:42.000
Ước tính mới cộng với một phần trăm trừ alpha.

### 00:03:42.000 - 00:03:44.000
Ước tính cũ.

### 00:03:45.000 - 00:03:52.000
Nếu Alpha là 20% thì ước tính trước đó sẽ chiếm 80% ước tính mới.

### 00:03:53.000 - 00:03:55.000
Và ước tính dựa trên kinh nghiệm?

### 00:03:55.000 - 00:03:57.000
20%.

