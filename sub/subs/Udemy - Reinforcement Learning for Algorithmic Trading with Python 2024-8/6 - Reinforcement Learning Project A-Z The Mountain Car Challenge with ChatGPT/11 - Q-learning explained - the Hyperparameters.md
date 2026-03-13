## Nội dung

### 00:00:00.000 - 00:00:04.960
Trong bài giảng trước, chúng tôi đã tạo mã để đào tạo một tác nhân học tăng cường, vì vậy

### 00:00:04.960 - 00:00:11.720
với Q learning và chúng tôi đã thấy rằng kết quả khá hứa hẹn. Vì vậy, với tỷ lệ thành công

### 00:00:11.720 - 00:00:20.719
 trong quá trình đào tạo ở đây là từ 85 đến 90%, khá tốt. Và đây thực ra là

### 00:00:20.719 - 00:00:26.800
vì vậy đoạn mã ở đây, đây là phần rất cơ bản của việc học Q, và tôi thực sự nghĩ rằng bạn

### 00:00:26.800 - 00:00:36.399
nên hiểu ở đây dòng mã cho dòng và lý thuyết cơ bản đằng sau việc học Q.

### 00:00:36.399 - 00:00:43.280
Và do đó trong bài giảng này và các bài giảng tiếp theo, chúng tôi cố gắng đi từng dòng một ở đây và cố gắng

### 00:00:43.280 - 00:00:49.359
hiểu nó thực sự hoạt động như thế nào. Vì vậy, Q đã được giải thích và trước hết, chúng ta cần

### 00:00:49.359 - 00:00:56.560
cắt tỉa và làm gọn gàng. Và đây là hai thông số rất quan trọng. Vậy số tập

### 00:00:56.560 - 00:01:04.799
 và số bước tối đa. Vì vậy, số bước tối đa phải đủ lớn để thực sự

### 00:01:04.799 - 00:01:13.480
tiếp cận được mục tiêu một cách tình cờ. Vì vậy, trong các tập ngẫu nhiên và chúng tôi cần số lượng tập tối thiểu

### 00:01:13.480 - 00:01:21.800
 để đào tạo hiệu quả và hiệu quả ở đây, đặc vụ và 2500 chỉ là những ví dụ ban đầu.

### 00:01:21.800 - 00:01:29.800
Vì vậy, chúng tôi sẽ tinh chỉnh điều này sau. Và sau đó, điều quan trọng nhất là chúng tôi tạo ra môi trường cho thử thách xe leo núi.

### 00:01:31.800 - 00:01:37.320
Và sau đó chúng tôi có ở đây một vài siêu thông số. Vì vậy, chúng ta có alpha, tốc độ học tập là 0,1,

### 00:01:37.399 - 00:01:46.519
sau đó là gamma, hệ số chiết khấu, epsilon, tốc độ khám phá và cả mức phân rã epsilon là 99,5%

### 00:01:46.519 - 00:01:52.919
 và epsilon tối thiểu. Và vì vậy chúng ta có thể tìm thấy ở đây những siêu tham số này trong mã.

### 00:01:54.839 - 00:01:59.719
Vì vậy, ví dụ, ở đây chúng tôi có bản cập nhật các giá trị Q. Chúng ta có thể tìm thấy gamma và alpha.

### 00:02:00.120 - 00:02:11.560
Và ở đây cũng là epsilon khi quyết định xem chúng ta thực hiện một hành động ngẫu nhiên hay một hành động tối ưu cho một trạng thái nhất định.

### 00:02:13.719 - 00:02:21.800
Và để thực sự hiểu thêm thông tin cơ bản ở đây, chúng tôi có thể hỏi bạn những câu hỏi sau. Vì vậy, vui lòng giải thích các tham số học tập Q

### 00:02:21.800 - 00:02:29.319
 chi tiết hơn cũng như phác thảo phạm vi các giá trị có thể có và thảo luận về việc sử dụng các giá trị cao so với thấp

### 00:02:29.319 - 00:02:39.000
 ở đây cho các tham số học tập Q này. Vì vậy, hãy quay lại cuộc trò chuyện GPT của chúng ta.

### 00:02:39.799 - 00:02:45.239
Và hãy sử dụng lời nhắc ở đây, gửi nó và đợi phản hồi ở đây.

### 00:02:47.000 - 00:02:53.639
Được rồi, hãy kiểm tra phản hồi ở đây. Vì vậy, Q learning là một thuật toán học tăng cường miễn phí theo mô hình để tìm hiểu giá trị của một hành động

### 00:02:53.719 - 00:02:59.559
 trong một trạng thái cụ thể. Và các tham số học tập Q đóng vai trò quan trọng trong quá trình học tập.

### 00:03:00.199 - 00:03:07.399
Có, giá trị này ảnh hưởng đáng kể đến hiệu suất của tác nhân. Vì vậy, hãy kiểm tra ở đây các siêu thông số khác nhau.

### 00:03:07.399 - 00:03:13.239
Và trước tiên chúng ta có tốc độ học và tốc độ học được xác định ở đây. Vậy mức độ thông tin mới

### 00:03:13.239 - 00:03:19.879
 lấn át thông tin cũ. Vì vậy, nó kiểm soát mức độ cập nhật của các giá trị Q trong quá trình học.

### 00:03:20.519 - 00:03:27.799
Và nó có thể lấy các giá trị từ 0 đến 1 và các giá trị gần bằng 1 nghĩa là tác nhân chú trọng hơn vào

### 00:03:27.799 - 00:03:36.759
các trải nghiệm gần đây đang cập nhật giá trị Q một cách tích cực hơn. Và giá trị thấp có nghĩa là tác nhân cập nhật giá trị Q

### 00:03:36.759 - 00:03:44.840
 từ từ dựa nhiều hơn vào kiến ​​thức trước đó. Vì vậy, có sự cân bằng giữa giá trị cao và giá trị thấp. Và hiện tại

### 00:03:45.000 - 00:03:59.000
chúng tôi có ở đây giá trị là 0,1. Sau đó, chúng ta có hệ số chiết khấu gamma và hệ số chiết khấu xác định tầm quan trọng của phần thưởng trong tương lai.

### 00:03:59.400 - 00:04:10.439
Vì vậy, khi cập nhật các giá trị trong bảng Q, chúng tôi không chỉ tính đến phần thưởng hiện tại của bước hiện tại mà còn tính đến phần thưởng của bước tiếp theo.

### 00:04:10.840 - 00:04:23.879
Và nó kiểm soát số lượng phần thưởng trong tương lai được tính đến. Vì vậy, giá trị cao có nghĩa là đại lý xem xét các phần thưởng trong tương lai nhiều hơn để thúc đẩy các chiến lược dài hạn. Vì vậy, điều đó quan trọng ở đây.

### 00:04:26.040 - 00:04:37.000
Và điều này có thể có lợi trong những môi trường mà phần thưởng trong tương lai rất đáng kể. Vì vậy, kết quả cuối cùng là quan trọng. Và đây là trường hợp trong ví dụ của chúng tôi.

### 00:04:37.959 - 00:04:48.120
Có giá trị thấp nên tác nhân tập trung nhiều hơn vào phần thưởng ngay lập tức của bước hiện tại có khả năng bỏ qua lợi ích của việc lập kế hoạch dài hạn.

### 00:04:50.600 - 00:05:01.720
Vì vậy, điều này sẽ phụ thuộc vào môi trường và trường hợp cụ thể giá trị nào tốt hơn ở đây. Sau đó, số ba chúng ta có tốc độ khám phá epsilon, cũng khá quan trọng.

### 00:05:02.200 - 00:05:11.400
Vì vậy, tốc độ khám phá xác định xác suất chọn một hành động ngẫu nhiên thay vì hành động có giá trị Q cao nhất.

### 00:05:12.040 - 00:05:17.000
Vì vậy, chúng ta có thể thấy điều này ở đây trong các dòng mã hóa này.

### 00:05:19.080 - 00:05:29.160
Vì vậy, với mỗi bước chúng ta tạo ra một giá trị ngẫu nhiên trong khoảng từ âm 1 đến 1. Và nếu giá trị này thấp hơn giá trị epsilon thì chúng ta sẽ thực hiện một hành động ngẫu nhiên.

### 00:05:30.120 - 00:05:39.240
Vì vậy, nếu epsilon cao như 1 thì rất có thể tác nhân chọn một hành động ngẫu nhiên và nếu epsilon thấp.

### 00:05:39.240 - 00:05:49.720
Có nhiều khả năng tác nhân sẽ chọn hành động phù hợp nhất với phần thưởng ước tính cao nhất. Vì vậy, đây là epsilon.

### 00:05:50.520 - 00:06:11.800
Vì vậy, nó có thể nhận các giá trị từ 0 đến 1 và tham số này kiểm soát sự cân bằng giữa quá trình khám phá. Vì vậy, hãy thử các hành động ngẫu nhiên mới và xem phần thưởng là sự lợi dụng. Vì vậy, không sử dụng hành động nào sẽ được thưởng cao và sau đó chọn giá trị cao.

### 00:06:11.800 - 00:06:23.639
Vì vậy, tác nhân khám phá nhiều hơn, thử nhiều hành động ngẫu nhiên khác nhau và điều này giúp khám phá các chiến lược mới nhưng chủ yếu dẫn đến hiệu suất dưới mức tối ưu nếu thăm dò quá thường xuyên.

### 00:06:24.360 - 00:06:31.160
Và ngược lại, khi chọn giá trị thấp, tác nhân không khai thác hành động nào, không có hành động tối ưu.

### 00:06:31.879 - 00:06:36.199
Điều này có thể cải thiện hiệu suất nhanh chóng nếu các giá trị Q gần như đã được học.

### 00:06:36.519 - 00:06:42.279
Nhưng nó có thể dẫn đến các chính sách dưới mức tối ưu nếu tác nhân bị mắc kẹt trong đó clopptima thấp.

### 00:06:43.079 - 00:06:54.599
Và trên thực tế, cách tốt nhất để làm điều này là bắt đầu với một giá trị cao để cho phép tác nhân khám phá các hành động ngẫu nhiên và quan sát kết quả.

### 00:06:54.840 - 00:07:08.280
Và sau đó khi nó đã học được thì chúng ta nên giảm giá trị epsilon và khai thác những gì chúng ta đã học trước đó và ở đây, sự phân rã epsilon sẽ diễn ra.

### 00:07:08.520 - 00:07:21.000
Vì vậy, sự phân rã epsilon là tốc độ mà tốc độ thăm dò giảm theo thời gian. Vì vậy, nó đảm bảo rằng tác nhân khám phá ít hơn khi nó trở nên tự tin hơn với các giá trị Q đã học.

### 00:07:21.480 - 00:07:30.680
Và các giá trị điển hình nằm trong khoảng từ 0 đến 1 và thường gần bằng 1 nên khoảng 99,5%.

### 00:07:31.319 - 00:07:39.079
Vì vậy, trong mỗi bước, epsilon giảm khoảng 0,5% trong trường hợp này.

### 00:07:41.160 - 00:07:48.360
Và thực tế khi chọn giá trị cao, epsilon giảm chậm cho phép khám phá nhiều hơn trong một khoảng thời gian dài hơn.

### 00:07:49.000 - 00:08:02.120
Và điều này có thể có lợi trong các môi trường phức tạp và mặt khác Bên cạnh đó, các giá trị thấp với giá trị thấp epsilon giảm nhanh dẫn đến việc khai thác nhanh chóng các chiến lược đã biết.

### 00:08:02.759 - 00:08:09.960
Vì vậy, tùy thuộc vào việc tác nhân của chúng tôi cảnh báo nhanh hay chậm, chúng tôi có thể điều chỉnh sự phân rã epsilon ở đây.

### 00:08:10.680 - 00:08:16.680
Và cuối cùng ở đây chúng tôi có một số giá trị ví dụ và những cân nhắc cho tốc độ học.

### 00:08:17.159 - 00:08:23.799
Vì vậy, 0,1 là lựa chọn phổ biến mang lại sự cân bằng giữa việc học thông tin mới và giữ lại thông tin cũ.

### 00:08:24.759 - 00:08:31.159
Và chúng tôi đối chiếu rằng 0,5 có nghĩa là học nhanh hơn với rủi ro không ổn định.

### 00:08:31.799 - 00:08:33.960
Sau đó, chúng tôi có ở đây hệ số chiết khấu gamma.

### 00:08:35.159 - 00:08:38.759
Và 0,9 là một cách tiếp cận cân bằng thường được sử dụng.

### 00:08:40.519 - 00:08:49.240
Nhưng khi sử dụng các giá trị cao hơn thì phần thưởng trong tương lai là rất quan trọng và tuân theo các giá trị của chúng tôi, phần thưởng ngay lập tức sẽ được ưu tiên.

### 00:08:50.200 - 00:08:57.879
Và sau đó chúng tôi có ở đây tốc độ khám phá nên thường có trong môi trường không xác định và không cần đào tạo gì cả.

### 00:08:57.879 - 00:09:04.840
Chúng ta nên bắt đầu với epsilon cao để khả năng khám phá cao hữu ích khi môi trường hầu như không được biết đến.

### 00:09:05.480 - 00:09:15.399
Và sau đó khi quá trình đào tạo tiếp tục, chúng ta nên giảm epsilon và cuối cùng chúng ta sẽ kết thúc với epsilon thấp để việc khám phá thấp sẽ khai thác nhiều hơn.

### 00:09:16.200 - 00:09:20.280
Và điều này tốt cho những môi trường mà tác nhân có chính sách hợp lý.

### 00:09:20.840 - 00:09:27.639
Vì vậy, khi đã có chính sách ban đầu phù hợp, chúng ta có thể bắt đầu với epsilon thấp, điều đó hoàn toàn ổn.

### 00:09:28.600 - 00:09:32.360
Và sau đó chúng ta có thể quản lý tốc độ của epsilon giảm.

### 00:09:32.919 - 00:09:36.679
Vì vậy, với sự phân rã chậm thì sự phân rã nhanh chóng.

### 00:09:38.279 - 00:09:41.639
Cũng tùy thuộc vào số bước và tập mà chúng ta có.

### 00:09:42.439 - 00:09:45.080
Vì vậy, đây là những cân nhắc thực tế.

### 00:09:45.080 - 00:09:53.639
Vì vậy, hãy bắt đầu với một epsilon cao hơn để khuyến khích khám phá ngẫu nhiên và phân rã nó theo thời gian để chuyển sang khai thác.

### 00:09:53.639 - 00:09:55.240
Vì vậy, đó là một ý tưởng hay.

### 00:09:56.200 - 00:10:01.320
Điều chỉnh số hai là theo dõi hiệu suất và điều chỉnh các tham số nếu cần.

### 00:10:01.320 - 00:10:08.120
Ví dụ: nếu tác nhân hội tụ quá chậm, hãy cân nhắc tăng hoặc giảm alpha epsilon.

### 00:10:08.120 - 00:10:14.039
Và thực tế nó thực sự phụ thuộc vào môi trường nên chúng tôi phải điều chỉnh các giá trị tham số cho phù hợp với môi trường cụ thể này.

### 00:10:14.680 - 00:10:20.039
Và các môi trường phức tạp có thể yêu cầu nhiều khả năng khám phá hơn và tốc độ học tập chậm hơn.

### 00:10:21.000 - 00:10:26.439
Vì vậy, bằng cách điều chỉnh các tham số này một cách thích hợp, bạn có thể nâng cao đáng kể hiệu suất.

### 00:10:27.319 - 00:10:28.519
Vì vậy, hãy quay lại đây.

### 00:10:31.559 - 00:10:36.919
Và trong trường hợp của chúng tôi, chúng tôi đã bắt đầu với tốc độ học tập 0,1, điều đó là ổn.

### 00:10:37.399 - 00:10:42.519
0,99 gamma rồi 0,1 epsilon có thể quá cao ở đây.

### 00:10:42.519 - 00:10:45.159
Vì vậy, chúng tôi có thể bắt đầu với một epsilon gần bằng 1.

### 00:10:45.719 - 00:10:53.480
Và bạn lắng nghe sự phân rã của epsilon là 0,995 với epsilon tối thiểu là 0,01.

### 00:10:54.039 - 00:10:59.480
Vì vậy, sau này chúng ta sẽ chơi quanh đây với các tham số và cố gắng tối ưu hóa chúng.

### 00:10:59.480 - 00:11:03.319
Nhưng tạm thời chúng ta hãy giữ các tham số ở đây.

### 00:11:04.279 - 00:11:08.439
Và chúng ta sẽ tiếp tục trong bài giảng tiếp theo với khía cạnh tiếp theo.

### 00:11:08.439 - 00:11:11.639
Vậy sự rời rạc hóa của các không gian trạng thái này.

