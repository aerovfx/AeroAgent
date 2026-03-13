## Nội dung

### 00:00:00.000 - 00:00:05.000
Trong video này, chúng ta sẽ tìm hiểu cách tối ưu hóa mạng lưới thần kinh của mình để ước tính các giá trị của

### 00:00:05.000 - 00:00:06.000
các tiểu bang.

### 00:00:07.000 - 00:00:13.000
Điều chúng tôi muốn đạt được là bằng cách chuyển một trạng thái làm đầu vào cho mạng nơ-ron thông qua đầu vào

### 00:00:13.000 - 00:00:20.000
lớp, mạng lưới thần kinh sẽ tạo ra các ước tính chính xác đầu ra về các giá trị Q cho mỗi hành động

### 00:00:20.000 - 00:00:22.000
ở trạng thái đó.

### 00:00:23.000 - 00:00:29.000
Để đạt được điều đó, chúng ta phải tìm các giá trị tối ưu cho tham số W của mạng nơ-ron, trong đó,

### 00:00:29.000 - 00:00:33.000
như bạn đã biết, đo lường sức mạnh của các kết nối giữa các tế bào thần kinh.

### 00:00:34.000 - 00:00:40.000
Các giá trị tối ưu cho W là những giá trị giảm thiểu sai sót mà mạng lưới thần kinh mắc phải khi ước tính

### 00:00:40.000 - 00:00:42.000
các giá trị Q.

### 00:00:43.000 - 00:00:46.000
Nhưng có nhiều cách để xác định sai số của ước tính.

### 00:00:47.000 - 00:00:51.000
Hai trong số đó là những cái bạn nhìn thấy trên màn hình, nhưng còn nhiều cái nữa.

### 00:00:51.000 - 00:00:53.000
Tất cả đều hoàn toàn hợp lệ.

### 00:00:54.000 - 00:01:00.000
Cái ở bên trái được gọi là Sai số tuyệt đối trung bình tính trung bình của các khác biệt giữa sai số thực

### 00:01:00.000 - 00:01:03.000
giá trị và giá trị ước lượng.

### 00:01:04.000 - 00:01:13.000
Biểu thức bên phải được gọi là sai số bình phương trung bình tìm giá trị trung bình của bình phương của những khác biệt đó.

### 00:01:14.000 - 00:01:19.000
Tùy thuộc vào biểu thức lỗi mà chúng ta chọn để giảm thiểu, chúng ta sẽ có được một giải pháp khác cho

### 00:01:19.000 - 00:01:25.000
các tham số W và mỗi giải pháp có những đặc điểm khác nhau.

### 00:01:25.000 - 00:01:32.000
Chúng ta sẽ chọn giảm thiểu sai số bình phương trung bình và chúng ta sẽ làm điều đó dựa trên kinh nghiệm

### 00:01:32.000 - 00:01:34.000
sẽ lấy mẫu từ môi trường.

### 00:01:34.000 - 00:01:41.000
Giá trị đích cho một trạng thái và hành động cụ thể là biểu thức mà chúng ta coi là giá trị thực của

### 00:01:41.000 - 00:01:46.000
hành động đó ở trạng thái đó và nó được thể hiện bằng biểu thức này.

### 00:01:47.000 - 00:01:56.000
Như bạn có thể thấy, nó bao gồm phần thưởng nhận được sau khi thực hiện hành động, cộng với ước tính đã chiết khấu

### 00:01:56.000 - 00:02:01.000
giá trị Q của hành động tiếp theo được thực hiện ở trạng thái tiếp theo đã đạt được.

### 00:02:02.000 - 00:02:05.000
Và tất nhiên, ước tính đó được tạo ra bởi mạng lưới thần kinh.

### 00:02:07.000 - 00:02:14.000
Và thuật ngữ còn lại trong biểu thức này là giá trị ước tính do mạng nơ-ron tạo ra cho giá trị đó

### 00:02:14.000 - 00:02:15.000
tình trạng.

### 00:02:15.000 - 00:02:16.000
Và hành động.

### 00:02:16.000 - 00:02:20.000
Bây giờ hãy hình dung một ví dụ rất đơn giản về hàm chi phí.

### 00:02:21.000 - 00:02:28.000
Hàm chi phí này chỉ phụ thuộc vào hai tham số thay vì vài triệu như cách làm việc bình thường.

### 00:02:28.000 - 00:02:30.000
với mạng lưới thần kinh.

### 00:02:30.000 - 00:02:37.000
Nhưng bằng cách chỉ sử dụng hai tham số, chúng ta sẽ có thể thấy hàm mất mát một cách trực quan trên trục tung.

### 00:02:37.000 - 00:02:44.000
Chúng ta thấy giá trị mà hàm chi phí nhận cho mỗi tổ hợp tham số.

### 00:02:44.000 - 00:02:51.000
Mục tiêu của chúng ta là tìm giá trị cho các tham số mà hàm chi phí này có giá trị thấp nhất.

### 00:02:53.000 - 00:03:00.000
Trong ví dụ rất đơn giản này, hàm chi phí đạt giá trị tối thiểu khi cả hai tham số

### 00:03:00.000 - 00:03:04.000
W một và W hai có giá trị bằng 0.

### 00:03:05.000 - 00:03:11.000
Bây giờ chúng ta hãy xem một ví dụ khác, đây vẫn là một sự đơn giản hóa tuyệt vời về hàm chi phí thực sự.

### 00:03:11.000 - 00:03:15.000
trông giống như vậy, nhưng nó phức tạp hơn một chút so với cái trước.

### 00:03:15.000 - 00:03:22.000
Hàm chi phí này có một số cực tiểu cục bộ, ví dụ như cái này ở đây, cái này, cái này

### 00:03:22.000 - 00:03:27.000
một và cái này, nhưng chỉ có một mức tối thiểu toàn cầu duy nhất.

### 00:03:27.000 - 00:03:29.000
Điểm tối thiểu trong hàm chi phí.

### 00:03:30.000 - 00:03:37.000
Trong trường hợp này, sẽ là lý tưởng khi tìm các giá trị cho các tham số tạo ra mức tối thiểu toàn cục

### 00:03:37.000 - 00:03:38.000
cho hàm chi phí.

### 00:03:39.000 - 00:03:46.000
Nhưng các thuật toán lặp như những thuật toán chúng ta sắp sử dụng chỉ đảm bảo tìm được mức tối thiểu cục bộ.

### 00:03:46.000 - 00:03:49.000
Đó là một trong số đó.

### 00:03:49.000 - 00:03:55.000
Tuy nhiên, theo nguyên tắc chung, điều này là đủ vì các ước tính do mạng nơron tạo ra

### 00:03:55.000 - 00:04:00.000
với các thông số này sẽ đủ tốt để giải quyết các nhiệm vụ điều khiển.

