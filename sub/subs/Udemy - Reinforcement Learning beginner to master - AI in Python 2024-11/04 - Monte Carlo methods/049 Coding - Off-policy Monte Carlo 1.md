## Nội dung

### 00:00:00.000 - 00:00:06.000
Trong video này, chúng ta sẽ bắt đầu triển khai phương pháp Montecarlo thứ hai, phương pháp này sẽ tuân theo

### 00:00:07.000 - 00:00:14.000
và chiến lược thăm dò chính sách. Theo chiến lược này, chúng tôi sẽ có hai chính sách riêng biệt.

### 00:00:15.000 - 00:00:21.000
Chính sách đầu tiên mà chúng tôi gọi là 'b' sẽ chịu trách nhiệm khám phá môi trường và thu thập

### 00:00:21.000 - 00:00:24.000
kinh nghiệm mà chúng ta sẽ sử dụng trong quá trình học tập.

### 00:00:24.000 - 00:00:28.000
Và chính sách thứ hai được gọi là 'pi' là chính sách mà chúng tôi sẽ tối ưu hóa.

### 00:00:28.000 - 00:00:33.000
Điều đầu tiên chúng ta cần làm là nhập các thư viện mã mà chúng ta sẽ sử dụng.

### 00:00:33.000 - 00:00:38.000
Trong trường hợp này, chúng ta sẽ sử dụng các thư viện giống như trong thuật toán trước. Điều tiếp theo

### 00:00:38.000 - 00:00:41.000
điều chúng tôi sắp làm là tạo ra môi trường.

### 00:00:41.000 - 00:00:50.000
Và chúng ta sẽ làm điều đó bằng cách tạo một thể hiện của lớp Mê cung và chúng ta sẽ lưu trữ thể hiện đó trong biến 'env'.

### 00:00:50.000 - 00:00:54.000
Khi chúng ta đã có được môi trường, đã đến lúc thể hiện nó trông như thế nào.

### 00:00:56.000 - 00:00:59.000
Như bạn đã biết, đó là Mê cung 5x5.

### 00:01:07.000 - 00:01:13.000
Như các bạn đã biết, chúng ta có sẵn 4 hành động: di chuyển lên, di chuyển xuống, di chuyển sang phải hoặc di chuyển sang trái,

### 00:01:15.000 - 00:01:21.000
và mỗi trạng thái được tạo thành từ sự kết hợp giữa hàng của trạng thái đó và cột của nó.

### 00:01:24.000 - 00:01:31.000
Tiếp theo, chúng ta sẽ khởi tạo bảng giá trị q. Bảng này sẽ phản ánh ước tính về các giá trị

### 00:01:31.000 - 00:01:32.000
của từng hành động.

### 00:01:32.000 - 00:01:39.000
Đó là lợi nhuận mà chúng ta mong đợi nhận được khi thực hiện hành động đó trong một trạng thái cụ thể.

### 00:01:40.000 - 00:01:43.000
Hãy nhớ rằng bảng giá trị q có thể được khởi tạo tùy ý.

### 00:01:44.000 - 00:01:49.000
Và điều duy nhất chúng ta phải tính đến là ở trạng thái đại diện cho mục tiêu,

### 00:01:49.000 - 00:01:52.000
giá trị q của tất cả các hành động là 0.

### 00:01:53.000 - 00:02:01.000
Vì vậy, để khởi tạo bảng này, chúng ta tạo biến giá trị hành động và sử dụng hàm từ NumPy

### 00:02:02.000 - 00:02:04.000
được gọi là np.full() để điền vào bảng này.

### 00:02:05.000 - 00:02:09.000
Hình dạng của bảng sẽ là 5x5x4.

### 00:02:10.000 - 00:02:15.000
Đó là 5 hàng, 5 cột và 4 hành động ở mỗi trạng thái đó.

### 00:02:16.000 - 00:02:23.000
Và như ước tính ban đầu của các giá trị q đó, hãy gán giá trị -100 cho mỗi mục

### 00:02:23.000 - 00:02:24.000
trong bảng này.

### 00:02:25.000 - 00:02:32.000
Hãy nhớ rằng giá trị ban đầu có thể tùy ý và sau quá trình học, các mục

### 00:02:32.000 - 00:02:35.000
của bảng giá trị q sẽ chuyển về giá trị tối ưu.

### 00:02:35.000 - 00:02:41.000
Điều tiếp theo chúng ta sẽ làm là đảm bảo rằng các giá trị ở mục tiêu là 0.

### 00:02:44.000 - 00:02:46.000
Hãy chạy ô này để tạo bảng.

### 00:02:47.000 - 00:02:54.000
Bây giờ chúng ta hãy vẽ bảng giá trị q này và xem nó trông như thế nào. Chúng tôi sẽ làm điều đó bằng cách sử dụng các giá trị hành động cốt truyện

### 00:02:54.000 - 00:02:58.000
hàm, chuyển bảng giá trị hành động làm đối số.

### 00:03:05.000 - 00:03:13.000
Đây rồi. Như chúng ta mong đợi, giá trị của tất cả các hành động ngoại trừ trạng thái mục tiêu là -100

### 00:03:14.000 - 00:03:17.000
và giá trị của các hành động ở trạng thái mục tiêu là 0.

### 00:03:18.000 - 00:03:24.000
Rõ ràng, khi đến đích, chúng ta không mong đợi có thêm bất kỳ phần thưởng nào.

### 00:03:27.000 - 00:03:32.000
Điều tiếp theo chúng ta sẽ làm là tạo hai chính sách, đầu tiên, chúng ta sẽ tạo

### 00:03:32.000 - 00:03:38.000
chính sách mà chúng tôi sẽ tối ưu hóa và sau đó sẽ tạo chính sách mà chúng tôi sẽ sử dụng để khám phá

### 00:03:38.000 - 00:03:38.000
môi trường.

### 00:03:41.000 - 00:03:49.000
Như bạn đã biết, chính sách luôn là một chức năng, nhưng tùy thuộc vào điều gì thuận tiện hơn cho chúng ta,

### 00:03:49.000 - 00:03:55.000
chính sách có thể trả về xác suất chọn từng hành động có sẵn hoặc nếu nó nhiều hơn

### 00:03:55.000 - 00:03:59.000
thuận tiện, nó có thể trả lại hành động được thực hiện.

### 00:03:59.000 - 00:04:01.000
Trong trường hợp này, chúng ta sẽ thực hiện nó

### 00:04:01.000 - 00:04:09.000
cách thứ hai. Chúng tôi sẽ tạo chính sách mục tiêu, đây là chính sách mà chúng tôi sẽ tối ưu hóa và nó

### 00:04:09.000 - 00:04:16.000
lấy đối số là một trạng thái và nó trả về hành động có giá trị q cao nhất cho trạng thái đó.

### 00:04:19.000 - 00:04:23.000
Đầu tiên, chúng tôi tìm nạp giá trị q cho các hành động ở trạng thái đó.

### 00:04:25.000 - 00:04:32.000
Để làm điều đó, chúng tôi lập chỉ mục cho bảng giá trị q chuyển dưới dạng chỉ mục trạng thái tham chiếu và được lưu trữ bên trong

### 00:04:32.000 - 00:04:36.000
Biến 'av' này sẽ có một vectơ có 4 giá trị.

### 00:04:36.000 - 00:04:42.000
Mỗi một trong số chúng sẽ là giá trị q của từng hành động có sẵn ở trạng thái này.

### 00:04:43.000 - 00:04:51.000
Bây giờ, câu hỏi mà chúng ta tự hỏi mình là, trong trường hợp có sự ràng buộc giữa các giá trị của hai hoặc nhiều hơn

### 00:04:51.000 - 00:04:52.000
hành động, chúng ta phải làm gì?

### 00:04:53.000 - 00:04:56.000
Thôi, nếu có hòa thì chúng ta sẽ bẻ ngẫu nhiên.

### 00:04:56.000 - 00:05:03.000
Đó là một trong những hành động có giá trị q cao nhất, chúng tôi sẽ chọn ngẫu nhiên một hành động mỗi khi gọi chính sách.

### 00:05:04.000 - 00:05:07.000
Hãy sử dụng hàm np.random.choice().

### 00:05:09.000 - 00:05:14.000
Và bên trong hàm này, chúng ta sẽ gọi hàm np.flatnonzero().

### 00:05:16.000 - 00:05:27.000
Và bên trong hàm np.flatnonzero() này, chúng ta sẽ truyền biểu thức này: 'av == av.max()'.

### 00:05:27.000 - 00:05:28.000
Chúng ta đang làm gì ở đây?

### 00:05:30.000 - 00:05:37.000
Chà, điều đầu tiên chúng ta đang làm là kiểm tra giá trị q trong biến 'av', nếu điều đó

### 00:05:38.000 - 00:05:43.000
giá trị q là cao nhất. Nếu đúng như vậy, hàm np.flatnonzero() sẽ chọn nó.

### 00:05:43.000 - 00:05:50.000
Và trong số tất cả các hành động có giá trị q cao nhất, hàm lựa chọn sẽ chọn ngẫu nhiên một hành động.

### 00:05:51.000 - 00:05:59.000
Về cơ bản, những gì chúng ta đang làm là chọn ngẫu nhiên một trong những hành động có giá trị cao nhất và bây giờ

### 00:05:59.000 - 00:06:01.000
chúng tôi có chính sách của chúng tôi.

### 00:06:02.000 - 00:06:11.000
Hãy kiểm tra nó với trạng thái (0, 0), đó là trạng thái ban đầu. Hãy viết: hành động bằng kết quả

### 00:06:11.000 - 00:06:16.000
gọi chính sách đích, chuyển trạng thái (0, 0) làm đối số.

### 00:06:23.000 - 00:06:25.000
Khi chúng tôi chọn hành động này,

### 00:06:29.000 - 00:06:34.000
hãy để chúng tôi thể hiện nó. Hãy viết rằng hành động được thực hiện ở trạng thái (0, 0)

### 00:06:41.000 - 00:06:42.000
Đây có phải là cái này

### 00:06:43.000 - 00:06:44.000
Hãy thực thi ô

### 00:06:47.000 - 00:06:53.000
và như bạn có thể thấy, nó đã chọn hành động số hai, nhưng thực ra, vì mọi hành động đều có cùng một

### 00:06:53.000 - 00:06:57.000
giá trị q, nó có thể chọn ngẫu nhiên bất kỳ giá trị nào trong số đó.

### 00:06:57.000 - 00:07:01.000
Chúng ta hãy chạy lại ô này và xem hành động được chọn thay đổi như thế nào.

### 00:07:02.000 - 00:07:08.000
Hãy xem, điều đó là như vậy bởi vì tại thời điểm này tất cả các giá trị q đều giống nhau.

### 00:07:08.000 - 00:07:15.000
Ngay khi có một giá trị tốt hơn các giá trị khác, chính sách này sẽ luôn chọn giá trị tương ứng

### 00:07:15.000 - 00:07:15.000
hoạt động.

### 00:07:16.000 - 00:07:21.000
Điều tiếp theo chúng ta sẽ làm là vẽ chính sách bằng cách sử dụng hàmplot_policy().

### 00:07:22.000 - 00:07:26.000
Và chúng tôi sẽ lấy nó làm đối số, bảng giá trị q mà chúng tôi sử dụng để xác định chính sách tối ưu này.

### 00:07:33.000 - 00:07:43.000
Chúng ta cũng hãy chuyển cho nó một hình ảnh của môi trường làm tham chiếu và loại trừ ô.  Đối với

### 00:07:43.000 - 00:07:45.000
thời điểm, mọi hành động đều có giá trị như nhau.

### 00:07:46.000 - 00:07:50.000
Nhưng khi chúng ta tiến bộ trong quá trình học tập, giá trị của mỗi hành động sẽ thay đổi.

### 00:07:53.000 - 00:07:57.000
Điều tiếp theo chúng ta sẽ làm là tạo chính sách thăm dò.

### 00:07:57.000 - 00:08:01.000
Rõ ràng, đây là chính sách mà chúng tôi sẽ sử dụng để khám phá môi trường.

### 00:08:02.000 - 00:08:09.000
Và đôi khi nó sẽ làm điều đó với một xác suất nhất định, chọn một hành động ngẫu nhiên và phần còn lại

### 00:08:09.000 - 00:08:13.000
thời điểm nó sẽ chọn hành động có giá trị ước tính cao nhất.

### 00:08:13.000 - 00:08:20.000
Tức là nó sẽ lấy bảng giá trị q và chọn hành động có giá trị ước tính cao nhất.

### 00:08:21.000 - 00:08:28.000
Giống như chính sách mục tiêu sẽ làm. Để làm được điều đó, chúng ta định nghĩa một hàm có tên là explorer_policy() và chúng ta sẽ

### 00:08:28.000 - 00:08:30.000
chuyển cho nó hai đầu vào khác nhau.

### 00:08:31.000 - 00:08:39.000
Cái đầu tiên là trạng thái trong đó hành động phải được chọn và cái thứ hai là epsilon, trạng thái này

### 00:08:39.000 - 00:08:41.000
theo mặc định sẽ được đặt thành 0.

### 00:08:42.000 - 00:08:44.000
Và epsilon sẽ làm gì?

### 00:08:47.000 - 00:08:50.000
Chà, mỗi lần chúng ta phải chọn một hành động sẽ lật một đồng xu.

### 00:08:55.000 - 00:09:04.000
Hàm np.random.random() này sẽ tạo ra một số ngẫu nhiên trong khoảng từ 0 đến 1. Nếu số này

### 00:09:04.000 - 00:09:09.000
nhỏ hơn epsilon thì chúng ta sẽ chọn một hành động ngẫu nhiên.

### 00:09:15.000 - 00:09:22.000
Tức là chúng ta sẽ chọn một số nguyên ngẫu nhiên trong khoảng từ 0 đến 4, không bao gồm. Tức là chúng ta sẽ chọn

### 00:09:22.000 - 00:09:25.000
hoặc 0, 1, 2 hoặc 3.

### 00:09:27.000 - 00:09:35.000
Và nếu số mà chúng ta thu được bằng hàm ngẫu nhiên lớn hơn epsilon thì sẽ chọn

### 00:09:35.000 - 00:09:44.000
hành động giống như cách chúng tôi đã làm với chính sách đích: bằng cách kiểm tra các bảng giá trị q và chọn

### 00:09:45.000 - 00:09:46.000
hành động có giá trị cao nhất.

### 00:09:53.000 - 00:09:58.000
Chúng tôi sẽ thực hiện điều đó bằng cách sử dụng cùng một dòng mã mà chúng tôi đã sử dụng trong chính sách trước đó.

### 00:10:03.000 - 00:10:08.000
Vì vậy, hãy để nó chọn ngẫu nhiên một trong những hành động có giá trị cao nhất.

### 00:10:09.000 - 00:10:13.000
Hãy để chúng tôi thực thi ô và bây giờ chúng tôi có chính sách của mình.

### 00:10:15.000 - 00:10:19.000
Bây giờ, hãy kiểm tra lại chính sách này với trạng thái (0, 0)

### 00:10:24.000 - 00:10:31.000
và xem kết quả của việc thực hiện chính sách khám phá này, mang lại cho nó 50% cơ hội chọn

### 00:10:31.000 - 00:10:32.000
một hành động ngẫu nhiên

### 00:11:07.000 - 00:11:08.000
Hãy thực thi ô này.

### 00:11:10.000 - 00:11:16.000
Như bạn thấy, hành động mà chúng ta thu được là hành động có nhãn ba đang di chuyển sang trái, nhưng chúng ta

### 00:11:16.000 - 00:11:22.000
có thể đã đạt được bất kỳ hành động nào khác vì hiện tại, tất cả các hành động đều có cùng giá trị q.

### 00:11:25.000 - 00:11:28.000
Và trong video tiếp theo, chúng ta sẽ bắt đầu triển khai thuật toán.

