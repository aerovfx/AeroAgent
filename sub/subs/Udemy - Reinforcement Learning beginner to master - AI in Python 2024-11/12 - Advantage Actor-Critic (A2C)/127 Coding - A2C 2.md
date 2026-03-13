## Nội dung

### 00:00:00.000 - 00:00:06.000
Trong video này, chúng ta sẽ tạo mạng lưới thần kinh cho chính sách và hàm giá trị. Cái đó

### 00:00:06.000 - 00:00:08.000
là diễn viên và nhà phê bình.

### 00:00:10.000 - 00:00:16.000
Hãy tạo một biến có chính sách tên và cho biến này, chúng ta sẽ gán một thể hiện

### 00:00:16.000 - 00:00:18.000
của lớp Tuần tự.

### 00:00:20.000 - 00:00:26.000
Như chúng ta biết, đó là lớp của mạng lưới thần kinh của chúng ta. Và với mạng này trước tiên chúng ta sẽ chuyển một tuyến tính

### 00:00:26.000 - 00:00:33.000
hoạt động sẽ lấy đầu vào là một vectơ có kích thước bằng kích thước của trạng thái.

### 00:00:34.000 - 00:00:35.000
Đó là sáu yếu tố

### 00:00:37.000 - 00:00:38.000
như chúng ta thấy ở đây,

### 00:00:42.000 - 00:00:48.000
và thao tác này sẽ có đầu ra là một vectơ gồm 128 phần tử.

### 00:00:52.000 - 00:01:00.000
Sau đó, đối với kết quả của thao tác trước, chúng ta sẽ áp dụng hàm kích hoạt RELU để phá vỡ tính tuyến tính của nó.

### 00:01:03.000 - 00:01:09.000
Và sau đó chúng ta sẽ lặp lại hai thao tác này, nhưng chúng ta sẽ phải thay đổi kích thước.

### 00:01:11.000 - 00:01:19.000
Phép toán tuyến tính thứ hai sẽ lấy đầu vào là một vectơ 128 đơn vị và sẽ trả về một vectơ có

### 00:01:19.000 - 00:01:20.000
64.

### 00:01:22.000 - 00:01:26.000
Và đối với kết quả của phép toán tuyến tính này, chúng ta sẽ áp dụng hàm RELU.

### 00:01:28.000 - 00:01:35.000
Và bây giờ chúng ta sẽ tạo một phép toán tuyến tính khác có đầu vào là một vectơ gồm 64 phần tử.

### 00:01:36.000 - 00:01:39.000
Và đầu ra của nó sẽ là một vector

### 00:01:41.000 - 00:01:43.000
với nhiều yếu tố như hành động mà chúng tôi có sẵn.

### 00:01:51.000 - 00:01:56.000
Hoạt động tuyến tính này sẽ tạo ra một giá trị cho mỗi hành động.

### 00:01:57.000 - 00:01:59.000
Nhưng giá trị được tạo ra bởi hoạt động này

### 00:02:01.000 - 00:02:08.000
sẽ nằm trong khoảng giữa vô cực âm và vô cực dương, nhưng chúng ta cần tạo ra một vectơ

### 00:02:08.000 - 00:02:14.000
xác suất, do đó mỗi phần tử phải nằm trong phạm vi [0, 1] và tổng của tất cả các phần tử phải

### 00:02:14.000 - 00:02:14.000
là 1.

### 00:02:16.000 - 00:02:24.000
Để đạt được điều này, đối với kết quả của lớp tuyến tính, chúng ta sẽ áp dụng hàm kích hoạt softmax.

### 00:02:30.000 - 00:02:38.000
Và chúng tôi sẽ chuyển nó làm đối số cho chiều cuối cùng vì chúng tôi muốn áp dụng thao tác softmax này cho mỗi hàng

### 00:02:38.000 - 00:02:39.000
của vectơ cột.

### 00:02:41.000 - 00:02:47.000
Hãy nhớ rằng vì chúng ta đang làm việc với một số môi trường nên trạng thái sẽ là một vectơ cột có

### 00:02:47.000 - 00:02:53.000
từng trạng thái riêng lẻ từ mỗi môi trường riêng lẻ trong mỗi hàng.

### 00:02:53.000 - 00:03:01.000
Vì vậy, việc chuyển giá trị dim=-1 cho hàm softmax này sẽ đảm bảo rằng thao tác này

### 00:03:01.000 - 00:03:09.000
được áp dụng cho từng trạng thái riêng lẻ và thao tác softmax sẽ trả về một vectơ có xác suất.

### 00:03:11.000 - 00:03:18.000
Mạng nơ-ron đại diện cho hàm giá trị sẽ rất giống với mạng này, với một số khác biệt.

### 00:03:19.000 - 00:03:21.000
Chúng tôi sẽ sao chép chính sách.

### 00:03:22.000 - 00:03:27.000
Đã dán ở đây và chúng tôi sẽ gọi nó là giá trị ròng.

### 00:03:33.000 - 00:03:39.000
Điểm khác biệt đầu tiên là lớp tuyến tính cuối cùng sẽ có một đầu ra duy nhất.

### 00:03:40.000 - 00:03:46.000
Đó là một giá trị duy nhất cho trạng thái mà chúng tôi chuyển nó làm đầu vào.

### 00:03:49.000 - 00:03:55.000
Nhưng vì chúng ta đang làm việc với nhiều môi trường nên chúng ta sẽ có một giá trị cho từng môi trường riêng lẻ

### 00:03:56.000 - 00:04:01.000
và hàm softmax, chúng ta sẽ loại bỏ nó vì giá trị của trạng thái không nhất thiết phải là

### 00:04:01.000 - 00:04:03.000
bị ràng buộc trong phạm vi [0, 1],

### 00:04:06.000 - 00:04:08.000
nó có thể nhận bất kỳ giá trị thập phân nào.

### 00:04:13.000 - 00:04:13.000
ĐƯỢC RỒI.

### 00:04:15.000 - 00:04:19.000
Hãy chạy hai ô này và bây giờ chúng ta có mạng lưới thần kinh.

### 00:04:22.000 - 00:04:24.000
Trong video tiếp theo sẽ bắt đầu thực hiện thuật toán.

### 00:04:26.000 - 00:04:27.000
Tôi sẽ gặp bạn ở đó.

