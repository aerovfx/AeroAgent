## Nội dung

### 00:00:00.000 - 00:00:09.000
Trong bài giảng trước, chúng ta đã rời rạc hóa các trạng thái thành 18 ngăn cho trục x và 14 cho vận tốc.

### 00:00:09.000 - 00:00:15.000
Và bây giờ đến bảng q và câu hỏi là bảng q là gì.

### 00:00:15.000 - 00:00:20.000
Và nhanh hơn nữa, hãy bắt đầu với thế năng hoặc số lượng trạng thái có thể có.

### 00:00:20.000 - 00:00:25.000
Vì vậy, chúng ta có 18 ngăn cho trục x và 14 cho vận tốc.

### 00:00:25.000 - 00:00:32.000
Vậy tổng cộng chúng ta có 252 trạng thái tiềm năng khác nhau cho ngọn núi ô tô.

### 00:00:32.000 - 00:00:37.000
Vậy xe leo núi có thể thực hiện 252 trạng thái khác nhau.

### 00:00:37.000 - 00:00:45.000
Và số kết hợp hành động trạng thái có thể hoặc tiềm năng là 252 lần so với 3.

### 00:00:45.000 - 00:00:49.000
Vì vậy, chúng ta có thể đi sang trái, không làm gì hoặc chúng ta có thể tăng tốc sang bên phải.

### 00:00:49.000 - 00:00:53.000
Vì vậy, chúng ta có ba hành động và 252 trạng thái.

### 00:00:53.000 - 00:00:58.000
Và do đó có 756 kết hợp hành động trạng thái.

### 00:00:58.000 - 00:01:02.000
Vì vậy, với mỗi trạng thái, chúng ta có thể thực hiện ba hành động khác nhau.

### 00:01:02.000 - 00:01:12.000
Nhưng bây giờ ý tưởng đằng sau bảng q là rằng đối với mỗi trạng thái, tức là đối với mỗi trạng thái trong số 252 trạng thái, có một hành động tối ưu.

### 00:01:12.000 - 00:01:16.000
Vì vậy, ví dụ: tăng tốc sang phải hoặc tăng tốc sang trái.

### 00:01:16.000 - 00:01:23.000
Và mục đích của quá trình huấn luyện bây giờ là tìm ra hành động tốt nhất cho mỗi trạng thái trong quá trình huấn luyện.

### 00:01:23.000 - 00:01:29.000
Vì vậy, đặc biệt là trong quá trình khám phá, chúng tôi thực hiện các bước ngẫu nhiên và quan sát phần thưởng.

### 00:01:29.000 - 00:01:35.000
Và sau đó xem hành động nào mang lại cho chúng ta phần thưởng cao nhất.

### 00:01:35.000 - 00:01:40.000
Và sau đó chúng ta thực hiện những hành động tốt nhất dựa trên quá trình đào tạo.

### 00:01:40.000 - 00:01:43.000
Vậy đây là sự khai thác.

### 00:01:44.000 - 00:01:52.000
Vì vậy, bảng q phải là một mảng ba chiều trong đó chúng ta có 252 trạng thái.

### 00:01:52.000 - 00:01:56.000
Và đối với mỗi trạng thái, chúng ta có ba hành động.

### 00:01:56.000 - 00:02:03.000
Và đối với mỗi tổ hợp hành động trạng thái, chúng ta có một giá trị cho phần thưởng tiềm năng.

### 00:02:03.000 - 00:02:06.000
Vì vậy, đây thực sự là ý tưởng cơ bản đằng sau q bảng.

### 00:02:06.000 - 00:02:12.000
Nhưng chúng ta cũng có thể yêu cầu trò chuyện ở đây làm như vậy giải thích cấu trúc, mục đích.

### 00:02:12.000 - 00:02:15.000
Và cơ chế của bảng q.

### 00:02:15.000 - 00:02:21.000
Và bạn đề xuất khởi tạo bảng q với các giá trị ngẫu nhiên giữa âm một và một.

### 00:02:21.000 - 00:02:23.000
Có lựa chọn nào tốt hơn không, vui lòng thảo luận.

### 00:02:23.000 - 00:02:35.000
Vì vậy, tôi thấy rằng chúng ta có thể khởi tạo bảng q bằng np.random.uniform, nó chỉ gán các giá trị ngẫu nhiên cho mỗi tổ hợp hành động trạng thái.

### 00:02:35.000 - 00:02:37.000
Vì vậy, giữa âm một và một.

### 00:02:37.000 - 00:02:44.000
Vì vậy, hãy thực hiện điều này ở đây bằng cách thực hiện như vậy chúng ta tạo ra bảng q là một mảng có nhiều mảng có hình dạng sau.

### 00:02:44.000 - 00:02:49.000
Vì vậy, chúng ta có trục x 18 trên trục y 14.

### 00:02:49.000 - 00:02:55.000
Và nói như vậy ở chiều thứ ba trên trục cố định của f3.

### 00:02:55.000 - 00:03:04.000
Và làm điều này có nghĩa là tổng cộng chúng ta có ở đây.

### 00:03:05.000 - 00:03:08.000
Chúng ta cần sử dụng ở đây phương pháp được làm phẳng.

### 00:03:08.000 - 00:03:12.000
Vì vậy, tổng cộng chúng ta có ở đây 756 giá trị trong bảng q.

### 00:03:12.000 - 00:03:19.000
Và mỗi giá trị đại diện cho phần thưởng tiềm năng cho một tổ hợp hành động trạng thái nhất định.

### 00:03:19.000 - 00:03:25.000
Và khi khởi tạo, chúng ta có các giá trị ngẫu nhiên ở đây từ âm một đến một.

### 00:03:25.000 - 00:03:30.000
Vì vậy ban đầu không cần đào tạo gì cả.

### 00:03:30.000 - 00:03:42.000
Và bây giờ Hãy sử dụng lời nhắc ở đây để hiểu rõ hơn về bảng q.

### 00:03:42.000 - 00:03:46.000
Và hãy đợi ở đây để có phản hồi đầy đủ.

### 00:03:46.000 - 00:03:54.000
Vì vậy, bảng q là một bảng mảng ma trận sử dụng q learning để lưu trữ các giá trị q cho mỗi cặp hành động trạng thái.

### 00:03:54.000 - 00:03:59.000
Và điều này thực sự của bảng q phụ thuộc vào không gian trạng thái và không gian hành động.

### 00:03:59.000 - 00:04:05.000
Vì vậy, các hàng biểu thị các trạng thái của môi trường và các cột thể hiện các hành động có thể.

### 00:04:05.000 - 00:04:09.000
Và mỗi mục trong bảng biểu thị giá trị ước tính.

### 00:04:09.000 - 00:04:14.000
Vì vậy, giá trị q của việc thực hiện hành động a và trạng thái s.

### 00:04:14.000 - 00:04:19.000
Vậy phần thưởng tiềm năng của một hành động nhất định đối với một trạng thái nhất định.

### 00:04:19.000 - 00:04:24.000
Và trong môi trường có không gian trạng thái liên tục, các trạng thái thường bị rời rạc.

### 00:04:24.000 - 00:04:26.000
Vì vậy, chúng ta đã thấy điều này.

### 00:04:26.000 - 00:04:34.000
Bây giờ mục đích của bảng q là lưu trữ phần thưởng tích lũy trong tương lai dự kiến cho mỗi cặp hành động trạng thái.

### 00:04:34.000 - 00:04:40.000
Cho phép tác nhân đưa ra quyết định sao cho tối đa hóa phần thưởng mong đợi theo thời gian.

### 00:04:40.000 - 00:04:45.000
Và bằng cách cập nhật các giá trị q dựa trên kinh nghiệm.

### 00:04:45.000 - 00:04:53.000
Vì vậy, đặc biệt trong giai đoạn thăm dò, tác nhân tìm hiểu chính sách tối ưu.

### 00:04:53.000 - 00:04:55.000
Và đây là cơ chế.

### 00:04:55.000 - 00:05:00.000
Vì vậy, chúng ta có cơ chế khởi tạo các bước sau với một số giá trị ngẫu nhiên điển hình.

### 00:05:00.000 - 00:05:03.000
Vì vậy, số 0 hoặc giá trị ngẫu nhiên nhỏ.

### 00:05:03.000 - 00:05:10.000
Tương tác số hai mà tác nhân tương tác với môi trường bằng cách thực hiện hành động và nhận phần thưởng.

### 00:05:10.000 - 00:05:17.000
Và sau mỗi hành động, giá trị q cho các cặp hành động trạng thái được cập nhật bằng phương trình bell man.

### 00:05:17.000 - 00:05:23.000
Vì vậy, đây là một phương trình khá phức tạp theo quan điểm toán học.

### 00:05:23.000 - 00:05:31.000
Tùy thuộc vào trạng thái hiện tại, phần thưởng nhận được và cả phần thưởng cho trạng thái tiếp theo.

### 00:05:31.000 - 00:05:37.000
Và sau đó là bước thứ tư trong giai đoạn khai thác, tác nhân chọn hành động dựa trên giá trị q.

### 00:05:37.000 - 00:05:44.000
Vì vậy, thường sử dụng chính sách tham lam tuyệt đối để cân bằng giữa việc thăm dò và khai thác.

### 00:05:44.000 - 00:05:47.000
Và bắt đầu từ đây với việc khởi tạo.

### 00:05:47.000 - 00:05:49.000
Vì vậy, chúng ta có thể sử dụng số không.

### 00:05:49.000 - 00:05:51.000
Và điều này đơn giản và không thiên vị.

### 00:05:51.000 - 00:05:56.000
Nhưng ban đầu có thể dẫn đến việc học chậm vì tác nhân không có ưu tiên nào.

### 00:05:56.000 - 00:06:00.000
Hoặc chúng ta có thể lấy các giá trị ngẫu nhiên nhỏ.

### 00:06:00.000 - 00:06:05.000
Và điều này có thể giúp phá vỡ mối liên kết giữa các hành động ban đầu và thúc đẩy việc khám phá.

### 00:06:05.000 - 00:06:11.000
Tuy nhiên, nếu các giá trị quá lớn hoặc quá nhỏ thì chúng có thể làm sai lệch quá trình học.

### 00:06:11.000 - 00:06:17.000
Vì vậy, điều này thực sự phụ thuộc vào từng trường hợp nếu số 0 hoặc giá trị ngẫu nhiên nhỏ là tốt hơn.

### 00:06:17.000 - 00:06:24.000
Nhưng ngoài ra, chúng ta cũng có thể khởi tạo các giá trị q dựa trên kiến thức trước đó hoặc ước tính heuristic.

### 00:06:24.000 - 00:06:29.000
Vì vậy, điều này hoàn toàn ổn nếu chúng ta có sẵn các giá trị này.

### 00:06:29.000 - 00:06:33.000
Hoặc chúng ta cũng có thể sử dụng các giá trị ngẫu nhiên thống nhất như chúng ta đã làm ở đây.

### 00:06:33.000 - 00:06:44.000
Vì vậy, ví dụ: từ một phạm vi từ âm một đến một và nó bổ sung tính ngẫu nhiên cho chính sách ban đầu thúc đẩy việc khám phá.

### 00:06:44.000 - 00:06:48.000
Và đây là một ví dụ về khởi tạo bảng q.

### 00:06:48.000 - 00:06:53.000
Vì vậy, chúng ta đã thấy điều này trước đây với đồng phục ngẫu nhiên đó.

### 00:06:53.000 - 00:06:56.000
Bây giờ là gì? phương pháp khởi tạo tốt nhất?

### 00:06:56.000 - 00:07:00.000
Khởi tạo bằng 0 là điểm khởi đầu tốt nếu bạn không có kiến ​​thức trước.

### 00:07:00.000 - 00:07:03.000
Và nó phù hợp với hầu hết các vấn đề.

### 00:07:03.000 - 00:07:08.000
Hoặc chúng ta có thể sử dụng các giá trị ngẫu nhiên nhỏ.

### 00:07:08.000 - 00:07:11.000
Hoặc các giá trị kiến ​​thức trước.

### 00:07:11.000 - 00:07:14.000
Vì vậy, đây là những điều cơ bản của bảng q.

### 00:07:14.000 - 00:07:21.000
Và bây giờ chúng ta có một bảng q có hình dạng 1843 và một số giá trị ngẫu nhiên thấp.

### 00:07:21.000 - 00:07:24.000
Và chúng ta sẽ tiếp tục ở đây trong bài giảng tiếp theo.

### 00:07:24.000 - 00:07:26.000
Hẹn gặp bạn ở đó. Tạm biệt.

