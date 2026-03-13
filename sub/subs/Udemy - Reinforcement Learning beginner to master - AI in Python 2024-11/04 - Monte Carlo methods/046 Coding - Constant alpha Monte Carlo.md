## Nội dung

### 00:00:00.000 - 00:00:06.000
Trong video này, chúng ta sẽ thực hiện một sửa đổi nhỏ đối với thuật toán Montecarlo theo chính sách để

### 00:00:06.000 - 00:00:10.000
sẽ cho phép chúng tôi cập nhật các ước tính giá trị hiệu quả hơn.

### 00:00:12.000 - 00:00:17.000
Vì tất cả những gì chúng ta sắp làm là một thay đổi nhỏ đối với thuật toán ban đầu, nên chúng ta sẽ thực hiện tất cả

### 00:00:17.000 - 00:00:21.000
những ô này giống hệt với các ô trong sổ ghi chép gốc.

### 00:00:21.000 - 00:00:23.000
Hãy nhập các thư viện mã.

### 00:00:24.000 - 00:00:27.000
Bây giờ hãy tạo môi trường và hiển thị nó.

### 00:00:31.000 - 00:00:36.000
Tiếp theo sẽ tạo bảng giá trị q, giống như chúng ta đã làm trong thuật toán ban đầu.

### 00:00:39.000 - 00:00:42.000
Và hãy nhanh chóng xem các giá trị bằng đồ họa,

### 00:00:44.000 - 00:00:46.000
mà, như chúng ta mong đợi, đầy 0.

### 00:00:48.000 - 00:00:50.000
Bây giờ, hãy nhập chính sách và kiểm tra nó.

### 00:00:56.000 - 00:00:58.000
Và cuối cùng, hãy xem trực quan.

### 00:01:00.000 - 00:01:06.000
Và bây giờ chúng tôi sẽ cập nhật thuật toán Montecarlo theo chính sách để cập nhật các giá trị của nó hiệu quả hơn.

### 00:01:09.000 - 00:01:16.000
Sự khác biệt đầu tiên với thuật toán ban đầu là chúng tôi sẽ không theo dõi kết quả trả về

### 00:01:16.000 - 00:01:17.000
được quan sát bởi đại lý.

### 00:01:19.000 - 00:01:25.000
Ngược lại, khi đến lúc cập nhật ước tính giá trị q, chúng ta sẽ đẩy ước tính

### 00:01:25.000 - 00:01:29.000
theo hướng của lợi nhuận mới mà chúng tôi quan sát được theo tỷ lệ phần trăm alpha.

### 00:01:33.000 - 00:01:40.000
Nó sẽ giống như việc tính toán mức trung bình có trọng số giữa lợi nhuận mới được quan sát dựa trên kinh nghiệm.

### 00:01:42.000 - 00:01:44.000
Và ước tính cũ.

### 00:01:46.000 - 00:01:52.000
Vì vậy, khi chúng tôi quan sát các khoản lợi nhuận mới, chúng tôi từ từ đẩy các ước tính của mình theo hướng đó.

### 00:01:55.000 - 00:01:58.000
Để làm được điều đó, việc đầu tiên chúng ta cần làm là khai báo một tham số alpha.

### 00:02:01.000 - 00:02:09.000
Điều đó sẽ đo lường tốc độ chúng tôi đẩy ước tính theo hướng mang lại lợi nhuận mới và

### 00:02:09.000 - 00:02:16.000
chúng ta sẽ đặt giá trị đó thành 0,2. Nghĩa là, bất cứ khi nào chúng ta quan sát thấy một lợi nhuận mới, bắt đầu

### 00:02:17.000 - 00:02:23.000
ở một trạng thái nhất định, thực hiện một hành động nhất định, chúng ta sẽ di chuyển ước tính giá trị q thêm 20%

### 00:02:23.000 - 00:02:26.000
theo hướng của lợi nhuận thực tế được quan sát.

### 00:02:28.000 - 00:02:34.000
Chúng tôi đã sao chép thuật toán từ sổ ghi chép trước vì tất cả những gì chúng tôi phải làm là một sửa đổi nhỏ

### 00:02:34.000 - 00:02:37.000
vào dòng mã này, nơi chúng tôi cập nhật các giá trị q.

### 00:02:40.000 - 00:02:47.000
Điều đầu tiên chúng ta cần làm là tạo một biến mới gọi là 'qsa' sẽ giữ giá trị q cũ

### 00:02:47.000 - 00:02:49.000
ước tính từ bảng giá trị q.

### 00:02:58.000 - 00:03:01.000
Và bây giờ chúng ta sẽ cập nhật ước tính giá trị q.

### 00:03:11.000 - 00:03:17.000
Với ước tính hiện tại, chúng ta sẽ cộng alpha lần chênh lệch giữa lợi nhuận mà chúng ta

### 00:03:17.000 - 00:03:19.000
chỉ quan sát dựa trên kinh nghiệm

### 00:03:24.000 - 00:03:31.000
và ước tính giá trị q cũ, thế là xong. Bây giờ chúng ta có thể chạy ô này và thuật toán đã sẵn sàng để

### 00:03:31.000 - 00:03:32.000
được thực thi.

### 00:03:33.000 - 00:03:39.000
Bây giờ, hãy xem kết quả mà chúng tôi thu được khi sử dụng phiên bản này có giống với kết quả chúng tôi thu được không

### 00:03:40.000 - 00:03:41.000
với thuật toán ban đầu.

### 00:03:45.000 - 00:03:51.000
Và như bạn có thể thấy ở đây, trong con đường tối ưu, những hành động đưa chúng ta đến mục tiêu là những hành động có

### 00:03:51.000 - 00:03:52.000
giá trị q cao nhất.

### 00:03:59.000 - 00:04:03.000
Và do đó, chính sách quy định các hành động đưa chúng ta đến mục tiêu.

### 00:04:08.000 - 00:04:13.000
Hãy đảm bảo rằng tác nhân có khả năng tìm ra lối ra bằng cách đặt nó đối mặt với môi trường.

### 00:04:13.000 - 00:04:14.000
Hãy chạy ô này...

### 00:04:17.000 - 00:04:22.000
...và như bạn có thể thấy, phiên bản mới này của thuật toán đơn giản hóa việc triển khai Montecarlo này

### 00:04:22.000 - 00:04:25.000
pháp mà vẫn bảo toàn được hiệu quả của nó.

