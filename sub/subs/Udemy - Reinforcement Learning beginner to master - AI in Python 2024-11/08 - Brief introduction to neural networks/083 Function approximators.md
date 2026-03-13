## Nội dung

### 00:00:00.000 - 00:00:05.000
Trong phần trước, chúng ta đã thấy chiến lược đầu tiên trong hai chiến lược mà chúng ta sẽ học cách sử dụng.

### 00:00:05.000 - 00:00:07.000
không gian trạng thái liên tục.

### 00:00:07.000 - 00:00:15.000
Trong phần này chúng ta sẽ tìm hiểu phần thứ hai liên quan đến việc sử dụng một công cụ được gọi là hàm xấp xỉ.

### 00:00:16.000 - 00:00:22.000
Chiến lược mà chúng ta đã sử dụng trong phần trước bao gồm việc lấy một không gian trạng thái liên tục như

### 00:00:22.000 - 00:00:28.000
cái bạn nhìn thấy trên màn hình và biến nó thành một không gian trạng thái rời rạc với số lượng hữu hạn

### 00:00:28.000 - 00:00:29.000
tiểu bang.

### 00:00:29.000 - 00:00:31.000
Các phương pháp dạng bảng có thể hoạt động được.

### 00:00:31.000 - 00:00:34.000
Để làm điều đó, chúng tôi sử dụng hai kỹ thuật khác nhau.

### 00:00:35.000 - 00:00:42.000
Cái đầu tiên, được gọi là tập hợp trạng thái, bao gồm việc cắt phạm vi các giá trị hợp lệ cho trạng thái

### 00:00:42.000 - 00:00:45.000
thành một số hữu hạn các khoảng.

### 00:00:45.000 - 00:00:51.000
Sau đó, chúng tôi tổng hợp tất cả các giá trị bên trong phạm vi đó thành một trạng thái duy nhất.

### 00:00:51.000 - 00:00:58.000
Sau đó, chúng tôi đã học một kỹ thuật thứ hai gọi là mã hóa ô, đó là sự khái quát hóa của tập hợp trạng thái

### 00:00:58.000 - 00:01:06.000
kỹ thuật trong mã hóa ô, chúng tôi tạo ra một số tập hợp trạng thái với kích thước và vị trí khác nhau.

### 00:01:07.000 - 00:01:10.000
Nhờ kỹ thuật này, chúng tôi có được ước tính tốt hơn về các giá trị.

### 00:01:11.000 - 00:01:16.000
Tuy nhiên, hai kỹ thuật này và nói chung chiến lược này có một số điểm yếu khiến chúng

### 00:01:16.000 - 00:01:20.000
không có khả năng xử lý các công việc có độ phức tạp vừa phải.

### 00:01:20.000 - 00:01:26.000
Hạn chế đầu tiên là độ chính xác của các ước tính sẽ bị hạn chế do thực tế

### 00:01:26.000 - 00:01:29.000
rằng chúng tôi đang tập hợp nhiều trạng thái thành một.

### 00:01:29.000 - 00:01:36.000
Hơn nữa, độ phức tạp tính toán của chiến lược này tăng rất nhanh khi số chiều trạng thái

### 00:01:36.000 - 00:01:37.000
lớn lên.

### 00:01:37.000 - 00:01:43.000
Hãy tưởng tượng rằng chúng ta muốn chia mỗi chiều của trạng thái thành 20 phân đoạn và trạng thái đó chỉ

### 00:01:43.000 - 00:01:45.000
có một chiều.

### 00:01:45.000 - 00:01:48.000
Trong trường hợp đó, sẽ có 20 trạng thái có thể xảy ra.

### 00:01:48.000 - 00:01:51.000
Bây giờ hãy tưởng tượng rằng trạng thái có hai chiều.

### 00:01:51.000 - 00:01:54.000
Trong trường hợp đó, sẽ có 20 x 20.

### 00:01:54.000 - 00:01:57.000
Đó là 400 trạng thái có thể.

### 00:01:57.000 - 00:02:02.000
Và nếu có năm chiều thì sẽ có từ 20 đến trạng thái lũy thừa thứ năm.

### 00:02:02.000 - 00:02:06.000
Đó là 3.200.000 trạng thái có thể.

### 00:02:07.000 - 00:02:13.000
Trong một số nhiệm vụ kiểm soát thế giới thực, trạng thái có thể chứa hàng trăm hoặc hàng nghìn chiều khác nhau.

### 00:02:13.000 - 00:02:17.000
Vì vậy, với chiến lược này, những vấn đề đó sẽ không thể giải quyết được.

### 00:02:18.000 - 00:02:23.000
Vì vậy, những gì chúng ta cần là một giải pháp thay thế chính xác với độ phức tạp hạn chế.

### 00:02:23.000 - 00:02:25.000
Nhập hàm xấp xỉ.

### 00:02:26.000 - 00:02:28.000
Hãy nhìn vào biểu đồ màu xanh lam.

### 00:02:28.000 - 00:02:33.000
Bạn có thể thấy hàm giá trị tối ưu của một tác vụ điều khiển nhất định mà chúng tôi vừa phát minh ra.

### 00:02:33.000 - 00:02:37.000
Hình dạng cụ thể của chức năng này hiện không quan trọng.

### 00:02:37.000 - 00:02:44.000
Trong màu cam, bạn có thể thấy một chức năng khác cố gắng phù hợp nhất có thể với chức năng màu xanh lam.

### 00:02:44.000 - 00:02:47.000
Nghĩa là, nó cố gắng xấp xỉ hàm màu xanh lam.

### 00:02:47.000 - 00:02:53.000
Hàm màu cam này là công cụ sẽ thay thế bảng giá trị mà chúng ta đã sử dụng ở phần trước.

### 00:02:53.000 - 00:02:54.000
phần.

### 00:02:54.000 - 00:03:01.000
Trước mỗi điểm trên trục x là một trạng thái và đối với mỗi điểm đó, chúng tôi lưu trữ một ước tính trên

### 00:03:01.000 - 00:03:02.000
bảng giá trị.

### 00:03:03.000 - 00:03:09.000
Bây giờ, thay vào đó chúng ta sẽ có một hàm với một loạt các tham số sẽ quyết định

### 00:03:09.000 - 00:03:11.000
hình của hàm đó.

### 00:03:12.000 - 00:03:17.000
Trong quá trình học, chúng ta sẽ sửa đổi giá trị của các tham số đó để hàm

### 00:03:17.000 - 00:03:19.000
phù hợp nhất có thể.

### 00:03:19.000 - 00:03:22.000
Hàm giá trị thực hoặc hàm giá trị Q.

### 00:03:24.000 - 00:03:31.000
Hãy nhớ lại rằng quá trình học tập tuân theo khuôn mẫu lặp lại chính sách tổng quát, trong đó việc đánh giá

### 00:03:31.000 - 00:03:37.000
và việc cải tiến chính sách lần lượt cho đến khi tìm được giá trị, chức năng và chính sách tối ưu.

### 00:03:37.000 - 00:03:44.000
Hàm giá trị tối ưu không được biết trước nhưng chúng ta đạt được nó bằng cách đánh giá liên tục

### 00:03:44.000 - 00:03:45.000
chính sách.

### 00:03:46.000 - 00:03:51.000
Khi chính sách tiếp cận, chính sách tối ưu khi bắt đầu quá trình học tập, hàm

### 00:03:51.000 - 00:03:58.000
mà chúng ta sắp tối ưu hóa có thể có bất kỳ hình dạng nhất định nào và nó có thể ước tính kém các giá trị tối ưu

### 00:03:58.000 - 00:04:00.000
cho mỗi tiểu bang.

### 00:04:00.000 - 00:04:06.000
Khi quá trình học tiến triển, hàm này sẽ tiếp cận hàm giá trị tối ưu và theo

### 00:04:06.000 - 00:04:11.000
kết thúc quá trình, nếu hàm chúng ta đã chọn là đúng thì nó sẽ càng gần càng tốt

### 00:04:12.000 - 00:04:16.000
đến hàm giá trị tối ưu như bạn thấy trong biểu đồ.

### 00:04:17.000 - 00:04:23.000
Như bạn có thể thấy, chúng ta có thể bắt đầu với bất kỳ hàm ban đầu nào được biểu thị bằng hàm F.

### 00:04:23.000 - 00:04:30.000
Đó là một hàm lấy trạng thái làm đầu vào và chứa một số tham số xác định hình dạng

### 00:04:30.000 - 00:04:31.000
của chức năng.

### 00:04:32.000 - 00:04:34.000
Mỗi lần chúng tôi biểu diễn.

### 00:04:34.000 - 00:04:41.000
Một chu trình đánh giá chính sách sẽ sửa đổi các tham số trên hàm đó và thu được hàm đó.

### 00:04:41.000 - 00:04:42.000
F hai.

### 00:04:42.000 - 00:04:50.000
Chúng ta sẽ lặp lại chu trình này như thường lệ cho đến khi đạt được hàm f n đủ

### 00:04:50.000 - 00:04:52.000
gần với hàm giá trị tối ưu.

### 00:04:54.000 - 00:04:58.000
Bây giờ chúng ta sẽ xem hai ví dụ về hàm xấp xỉ.

### 00:04:59.000 - 00:05:06.000
Cái đầu tiên được gọi là Công cụ xấp xỉ tuyến tính và bao gồm tổng trọng số của từng chiều của

### 00:05:06.000 - 00:05:13.000
trạng thái theo một tham số nhất định w sẽ đo lường tầm quan trọng của phần tử đó ở đây.

### 00:05:13.000 - 00:05:20.000
Việc gọi hàm trên một trạng thái cụ thể sẽ tạo ra ước tính giá trị của trạng thái đó và điều đó

### 00:05:20.000 - 00:05:27.000
giá trị được tính bằng mỗi thứ nguyên của trạng thái nhân với tham số tương ứng của nó.

### 00:05:28.000 - 00:05:30.000
Hãy xem nó với một ví dụ.

### 00:05:30.000 - 00:05:37.000
Trong biểu đồ màu xanh lam, chúng ta có hàm giá trị tối ưu của một nhiệm vụ nhất định và trong màu cam, chúng ta có

### 00:05:37.000 - 00:05:39.000
xấp xỉ tuyến tính.

### 00:05:40.000 - 00:05:45.000
Vì trạng thái chỉ có một giá trị nên nó chỉ có một chiều.

### 00:05:45.000 - 00:05:49.000
Công cụ xấp xỉ tuyến tính sẽ có một tham số W duy nhất.

### 00:05:49.000 - 00:05:53.000
Sự phù hợp tốt nhất có thể xảy ra với giá trị này cho tham số.

### 00:05:55.000 - 00:05:59.000
Giá trị gần đúng khá tốt trong trường hợp này, nhưng nó có thể tốt hơn.

### 00:05:59.000 - 00:06:02.000
Chúng ta hãy xem xét một công cụ gần đúng sẽ đạt được sự phù hợp tốt hơn.

### 00:06:03.000 - 00:06:10.000
Công cụ xấp xỉ mới này được gọi là Công cụ xấp xỉ đa thức và nó cũng sẽ là tổng có trọng số của mỗi công cụ gần đúng.

### 00:06:10.000 - 00:06:15.000
phần tử trạng thái và số mũ của các phần tử đó đến một giá trị nhất định.

### 00:06:15.000 - 00:06:17.000
K. Trong trường hợp này.

### 00:06:18.000 - 00:06:24.000
Ví dụ: chúng ta có thể bao gồm phần tử đầu tiên, phần tử đầu tiên bình phương, phần tử đầu tiên lập phương,

### 00:06:24.000 - 00:06:28.000
vân vân cho đến khi chúng ta đạt đến số mũ nhất định.

### 00:06:28.000 - 00:06:31.000
Và tương tự với các yếu tố còn lại của nhà nước.

### 00:06:31.000 - 00:06:36.000
Và mỗi phần tử trong số này sẽ được nhân với tham số tương ứng của nó.

### 00:06:37.000 - 00:06:42.000
Và đây là sự phù hợp mà chúng tôi đạt được với công cụ ước tính đa thức hai phần tử.

### 00:06:42.000 - 00:06:49.000
Phần tử đầu tiên là giá trị của trạng thái và phần tử thứ hai là giá trị của bình phương trạng thái.

### 00:06:49.000 - 00:06:56.000
Mỗi phần tử này được tính trọng số bởi tham số W và khi mức độ phù hợp đạt mức tối ưu, giá trị của từng phần tử sẽ

### 00:06:56.000 - 00:06:58.000
tham số là những cái này.

### 00:06:59.000 - 00:07:05.000
Đây chỉ là hai ví dụ về hàm thích ứng mà chúng ta có thể sử dụng để biểu diễn hàm giá trị của

### 00:07:05.000 - 00:07:06.000
một nhiệm vụ kiểm soát

### 00:07:06.000 - 00:07:09.000
Và làm điều đó có một số lợi thế quan trọng.

### 00:07:09.000 - 00:07:16.000
Ví dụ, chúng yêu cầu ít bộ nhớ vì tất cả những gì chúng ta phải lưu trữ là vectơ có tham số W.

### 00:07:17.000 - 00:07:23.000
Một ưu điểm khác là có thể sử dụng cùng một bộ xấp xỉ hàm để tính gần đúng các hàm khác nhau.

### 00:07:24.000 - 00:07:27.000
Đơn giản bằng cách sửa đổi các tham số W.

### 00:07:28.000 - 00:07:34.000
Tuy nhiên, một ưu điểm khác là nếu chúng ta chọn đúng công cụ xấp xỉ hàm, chúng ta có thể có được kết quả rất chính xác.

### 00:07:34.000 - 00:07:35.000
cho ăn.

