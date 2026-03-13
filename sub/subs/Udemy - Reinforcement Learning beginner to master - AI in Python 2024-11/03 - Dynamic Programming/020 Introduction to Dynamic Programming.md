# Giới Thiệu Về Lập Trình Động

## Nội dung

### 00:00:00 - 00:00:05
Trong video này, chúng ta sẽ khám phá họ phương pháp đầu tiên có khả năng giải quyết các nhiệm vụ điều khiển.

### 00:00:06 - 00:00:08
Chúng được gọi là lập trình động.

### 00:00:10 - 00:00:16
Các phương pháp này tìm giải pháp cho các vấn đề bằng cách chia nhỏ chúng thành các vấn đề nhỏ hơn dễ giải quyết hơn.

### 00:00:16 - 00:00:16
Để giải quyết.

### 00:00:17 - 00:00:26
Trong trường hợp của chúng ta, như bạn biết, vấn đề mà chúng ta đang cố gắng giải quyết là tìm chính sách tối ưu. Để

### 00:00:26 - 00:00:29
Chúng ta có thể áp dụng lập trình động cho một vấn đề

### 00:00:29 - 00:00:32
Nó phải có hai thuộc tính.

### 00:00:32 - 00:00:36
Thuộc tính đầu tiên là cấu trúc con tối ưu.

### 00:00:37 - 00:00:44
Điều này có nghĩa là trong việc tìm giải pháp cho mỗi vấn đề con của nó và kết hợp các giải pháp cá nhân đó,

### 00:00:44 - 00:00:49
Chúng ta sẽ tìm được giải pháp tối ưu cho vấn đề ban đầu.

### 00:00:50 - 00:00:57
Chúng ta muốn tìm chính sách tối ưu. Chính sách đó chọn hành động tối đa hóa lợi nhuận kỳ vọng trong

### 00:00:57 - 00:01:06
Mỗi trạng thái. Chúng ta có thể chia nhỏ nhiệm vụ này thành việc tìm chính sách tối ưu cho mỗi trạng thái riêng lẻ

### 01:07:00 - 00:01:12
Nếu chúng ta tìm chính sách tối ưu cho mỗi trạng thái

### 01:13:00 - 00:01:17
Chúng ta sẽ có được chính sách tối ưu cho toàn bộ vấn đề.

### 01:19:00 - 00:01:26
Chúng ta có thể hướng dẫn và cấu trúc việc tìm kiếm chính sách này sử dụng các hàm giá trị. Chính sách tối ưu

### 01:26:00 - 00:01:29
Thực hiện các hành động dựa trên giá trị trạng thái hoặc giá trị q.

### 01:29:00 - 00:01:34
Do đó, để tìm chính sách tối ưu, chúng ta cần tìm các giá trị tối ưu.

### 01:34:00 - 00:01:41
Nếu chúng ta tìm giá trị tối ưu cho mỗi trạng thái độc lập, thì chúng ta sẽ có hàm giá trị tối ưu

### 01:41:00 - 00:01:43
Cho toàn bộ vấn đề.

### 01:44:00 - 00:01:49
Vì vậy, như bạn thấy, các vấn đề mà chúng ta muốn giải quyết thực sự có cấu trúc con tối ưu.

### 01:51:00 - 00:01:55
Thuộc tính thứ hai là chứa các vấn đề con chồng chéo.

### 01:57:00 - 00:02:00
Hãy gọi vấn đề cần giải quyết là vấn đề P.

### 02:01:00 - 00:02:10
Chúng ta có thể phân rã P thành một tập hợp các vấn đề con. Giải pháp cho mỗi vấn đề con này phải phụ thuộc

### 02:10:00 - 00:02:14
Vào giải pháp của các vấn đề con khác.

### 02:14:00 - 00:02:21
Ví dụ, giải pháp tối ưu cho vấn đề A sẽ phụ thuộc vào vấn đề B và giải pháp cho

### 02:21:00 - 00:02:26
Vấn đề B sẽ phụ thuộc vào cả vấn đề A và vấn đề C.

### 02:27:00 - 00:02:30
Nói cách khác, các giải pháp phụ thuộc lẫn nhau.

### 02:31:00 - 00:02:35
Bây giờ chúng ta tự hỏi liệu tính năng này có mặt trong các vấn đề mà chúng ta sẽ cố gắng giải quyết không.

### 02:36:00 - 00:02:41
Chà, nếu bạn nhớ các phương trình Bellman, bạn sẽ biết điều này cũng đúng.

### 02:41:00 - 00:02:49
Các phương trình này biểu diễn giá trị của một trạng thái bằng các giá trị của các trạng thái khác hoặc trong trường hợp

### 02:49:00 - 00:02:58
Của hàm q, giá trị của một hành động trong một trạng thái như một hàm của giá trị của các hành động khác trong

### 02:58:00 - 00:02:58
Các trạng thái khác.

### 03:00:00 - 00:03:05
Vì vậy, như bạn có thể thấy, các vấn đề mà chúng ta sẽ cố gắng giải quyết thực sự thỏa mãn yêu cầu thứ hai.

### 03:06:00 - 00:03:09
Vậy lập trình động chính xác làm gì?

### 03:10:00 - 00:03:14
Chúng ta sẽ duy trì một bảng giá trị với một mục cho mỗi trạng thái.

### 03:15:00 - 00:03:20
Và trong bảng đó, chúng ta sẽ duy trì một ước lượng về giá trị của mỗi trạng thái.

### 03:21:00 - 00:03:27
Ước lượng đó lúc đầu không cần chính xác, nhưng chúng ta sẽ cải thiện nó theo cách lặp đi lặp lại.

### 03:27:00 - 00:03:35
Để làm điều đó, chúng ta sẽ chuyển phương trình Bellman mà bạn thấy ở đây thành một quy tắc cập nhật.

### 03:35:00 - 00:03:42
Và với nó, chúng ta sẽ duyệt qua không gian trạng thái và cập nhật giá trị ước lượng của mỗi trạng thái theo

### 03:42:00 - 00:03:44
Biểu thức vế phải.

### 03:45:00 - 00:03:52
Mỗi khi chúng ta cập nhật giá trị ước lượng của một trạng thái, chúng ta sẽ có các ước lượng tốt hơn cho các giá trị liên quan.

### 03:53:00 - 00:03:57
Và do đó, ước lượng mới sẽ chính xác hơn ước lượng cũ.

### 04:00:00 - 00:04:06
Tuy nhiên, chúng ta có một vấn đề. Để thực hiện cập nhật, chúng ta cần biết trước các xác suất chuyển đổi trạng thái,

### 04:06:00 - 00:04:13
Tức là, chúng ta cần biết trước những trạng thái nào có thể theo sau sau khi chúng ta chọn một hành động

### 04:14:00 - 00:04:15
Và với xác suất nào.

### 04:16:00 - 00:04:22
Một hạn chế lớn của lập trình động là nó cần một mô hình hoàn hảo của môi trường.

### 04:22:00 - 00:04:26
Tức là, chúng ta cần quyền truy cập vào các xác suất chuyển đổi trạng thái này.

### 04:28:00 - 00:04:32
Một ví dụ về nhiệm vụ mà chúng ta có một mô hình như vậy là khối Rubik.

### 04:33:00 - 00:04:39
Chúng ta biết khối Rubik sẽ trông như thế nào sau khi chúng ta xoay nó dọc theo một trong các trục của nó.

### 04:40:00 - 00:04:46
Tuy nhiên, trong một số lượng lớn các nhiệm vụ, mô hình đó sẽ không có sẵn và chúng ta sẽ phải sử dụng các thuật toán khác

### 04:46:00 - 00:04:46
Để giải quyết chúng.

### 04:48:00 - 04:55:00
Một điều quan trọng cuối cùng về lập trình động là nó giải quyết các vấn đề sử dụng các giá trị kỳ vọng,

### 04:56:00 - 00:05:02
Nó tính đến mọi kết quả có thể của việc thực hiện một hành động và sử dụng nó để cập nhật các giá trị ước lượng.

### 05:02:00 - 00:05:03
Giá trị.

### 05:04:00 - 00:05:09
Ngược lại, các phương pháp mà chúng ta sẽ bắt đầu trong phần tiếp theo sẽ không có mô hình động lực học của môi trường,

### 05:09:00 - 00:05:15
Và chúng sẽ sử dụng các mẫu kinh nghiệm được thu thập bởi tác tử tương tác với

### 05:15:00 - 00:05:18
Môi trường để cập nhật các giá trị ước lượng.
