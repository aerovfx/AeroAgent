## Nội dung

### 00:00:00.000 - 00:00:05.179
Bây giờ, trong bài giảng cuối cùng của phần này, chúng ta sẽ đến với khái niệm rất quan trọng về mã thông báo

### 00:00:05.600 - 00:00:10.400
Vì vậy, biết mã thông báo là gì và mã thông báo hoạt động như thế nào trong các mô hình ngôn ngữ như

### 00:00:10.919 - 00:00:16.600
GPT cho phép bạn hiểu rõ hơn về cách các mô hình này hoạt động ẩn và

### 00:00:17.080 - 00:00:23.859
Điều này bạn sẽ hiểu rõ hơn một số hạn chế và cạm bẫy khi làm việc với các mô hình GPT

### 00:00:24.140 - 00:00:28.800
Vì vậy, tôi ở đây trên trang web AI mở trong một bài viết trợ giúp

### 00:00:28.980 - 00:00:33.659
Vì vậy, tôi cũng sẽ cung cấp liên kết đến bài viết này kèm theo bài giảng này

### 00:00:34.619 - 00:00:40.700
Bây giờ chúng ta đã biết rằng GPT mô hình phân tích văn bản tuy nhiên họ không làm từng chữ

### 00:00:41.439 - 00:00:43.700
Nhưng họ làm điều đó bằng mã thông báo

### 00:00:43.980 - 00:00:51.939
Vì vậy, mô hình chia văn bản thành các mã thông báo và sau đó phân tích vị trí tương đối của các mã thông báo với nhau

### 00:00:52.259 - 00:00:54.259
để tìm các mẫu và

### 00:00:54.259 - 00:01:01.339
Vì vậy, để hiểu ý nghĩa của văn bản không hiểu cách con người hiểu một văn bản

### 00:01:01.500 - 00:01:06.620
Nhưng hiểu như một chuỗi các mã thông báo được chuyển đổi thành số

### 00:01:07.019 - 00:01:10.500
vì vậy mỗi mã thông báo duy nhất có một số duy nhất và

### 00:01:11.140 - 00:01:20.219
cuối cùng đối với các mô hình GPT, một văn bản là một chuỗi số và tất cả chúng ta đều biết rằng máy tính rất giỏi trong việc xử lý số

### 00:01:20.819 - 00:01:23.780
Vậy chúng ta hãy cùng xem qua bài viết và

### 00:01:25.219 - 00:01:28.500
Các mã thông báo có thể được coi là những đoạn từ

### 00:01:28.980 - 00:01:35.000
Vì vậy, trung bình một mã thông báo có bốn ký tự bằng tiếng Anh, nhưng nó phụ thuộc vào ngôn ngữ

### 00:01:35.579 - 00:01:42.859
Vì vậy, trung bình một mã thông báo là ba phần tư của một từ hoặc nói theo cách khác

### 00:01:42.859 - 00:01:46.900
Vì vậy, 100 mã thông báo tương đương với 75 từ và

### 00:01:47.380 - 00:01:52.060
Và trong một hoặc hai câu, chúng ta có thể tìm thấy 30 mã thông báo và

### 00:01:53.260 - 00:02:00.940
Ví dụ: trong trích dẫn, bạn bỏ lỡ 100% số cảnh bạn không chụp nên trong này chứa 11 mã thông báo

### 00:02:03.140 - 00:02:08.939
Bây giờ giới hạn mã thông báo thực sự quan trọng và chúng tôi sẽ đề cập đến vấn đề này trong một trong các phần tiếp theo

### 00:02:09.219 - 00:02:12.939
Vì vậy, tùy thuộc vào mô hình, một cuộc trò chuyện có thể sử dụng tới

### 00:02:12.939 - 00:02:20.099
4.097 mã thông báo nên một cuộc trò chuyện bao gồm lời nhắc và phản hồi và

### 00:02:21.620 - 00:02:24.099
Bất kỳ cuộc trò chuyện nào được giới hạn ở

### 00:02:24.939 - 00:02:30.300
4.097 mã thông báo và làm ví dụ, nếu bạn nhắc 4.000 mã thông báo này

### 00:02:30.620 - 00:02:37.740
Sau đó, phản hồi chỉ có thể lấy 97 mã thông báo và chúng ta sẽ xem ví dụ sau trong phần này khóa học

### 00:02:38.540 - 00:02:47.100
Tuy nhiên, giới hạn này phụ thuộc vào kiểu máy và ở đây chúng ta chỉ có thể kiểm tra các mẫu khác nhau hoặc mẫu mới nhất là GPT4

### 00:02:47.620 - 00:02:48.620
và

### 00:02:48.620 - 00:02:50.219
mẫu trước đó là

### 00:02:50.219 - 00:02:51.460
GPT

### 00:02:51.460 - 00:02:53.460
0.3.5 và

### 00:02:53.659 - 00:02:56.620
Tất nhiên là có các bản nâng cấp mô hình liên tục và

### 00:02:57.540 - 00:03:01.540
Ở đây chẳng hạn như đối với GPT4, số mã thông báo tối đa là

### 00:03:01.539 - 00:03:07.539
8.192 và cũng ở đây chúng ta có thể xem dữ liệu đào tạo cho đến tháng 9

### 00:03:08.259 - 00:03:10.259
2021 và

### 00:03:10.859 - 00:03:15.739
Ở đây bên dưới chúng tôi có GPT 3.5 turbo và ở đây chúng tôi có

### 00:03:16.739 - 00:03:21.099
4.097 mã thông báo và ở đây dữ liệu đào tạo sẽ chuyển sang tháng 9

### 00:03:21.579 - 00:03:23.579
2021 và

### 00:03:24.060 - 00:03:26.939
Sau đó, chúng tôi cũng vậy tìm thêm thông tin về các mô hình

### 00:03:27.659 - 00:03:31.099
khác dựa trên GPT hàng ngày để tạo hình ảnh

### 00:03:32.379 - 00:03:35.419
Thì thầm để nhận dạng tốc độ và hơn thế nữa

### 00:03:38.620 - 00:03:44.219
Và thực tế khi làm việc với API thì việc định giá cũng dựa trên mã thông báo

### 00:03:44.219 - 00:03:53.139
Vì vậy, chúng ta đã thấy điều này trong bài giảng trước. Hãy lấy một ví dụ đơn giản ở đây và chúng ta có văn bản màu sắc yêu thích của tôi là màu đỏ và

### 00:03:53.659 - 00:03:58.899
Ở đây với các màu khác nhau, chúng ta có thể thấy các mã thông báo riêng biệt. Vì vậy, của tôi là một mã thông báo

### 00:03:59.139 - 00:04:08.219
Sau đó, mục yêu thích là một mã thông báo cũng có màu đỏ và bạn có thể thấy mã thông báo ở đây bao gồm một khoảng trắng ở cuối và

### 00:04:09.339 - 00:04:13.859
Điều này đánh dấu vị trí trong một câu hoặc có một khoảng trắng ở cuối

### 00:04:13.859 - 00:04:18.860
Chúng tôi biết rằng màu đỏ không phải là từ đầu tiên trong câu và

### 00:04:19.139 - 00:04:23.540
Và sau đó, mã thông báo nội bộ của nó được chuyển đổi thành ID mã thông báo

### 00:04:23.740 - 00:04:25.740
Vì vậy, ví dụ: my is

### 00:04:26.540 - 00:04:30.060
3666 và màu đỏ là

### 00:04:31.340 - 00:04:33.340
2266 và

### 00:04:34.139 - 00:04:39.780
một dấu chấm ở cuối câu là số mã thông báo 13

### 00:04:41.540 - 00:04:47.540
Bây giờ số mã thông báo sẽ thay đổi nếu chúng ta thay đổi cách viết nên ở đây chúng ta có màu đỏ với chữ thường r

### 00:04:47.700 - 00:04:53.860
Nhưng nếu bạn sử dụng chữ r viết hoa thì ID mã thông báo sẽ thay đổi từ

### 00:04:54.939 - 00:04:58.300
2266 thành 2297

### 00:04:58.900 - 00:05:07.900
Vì vậy, vấn đề chính tả và bạn nên lưu ý điều đó và thông thường trong bối cảnh này ở đây, bạn sẽ viết màu đỏ ở đây bằng chữ thường r

### 00:05:09.460 - 00:05:12.660
Và nếu màu đỏ ở đầu câu

### 00:05:13.060 - 00:05:17.060
Vì vậy, hãy có khoảng trắng ở đầu và bắt đầu bằng chữ in hoa thì

### 00:05:17.540 - 00:05:20.420
ID mã thông báo đã khác nên bây giờ nó là

### 00:05:21.260 - 00:05:23.260
7,738 và

### 00:05:23.700 - 00:05:31.860
Điều này cho phép mô hình GPT thực sự phân tích vị trí tương đối của một từ hoặc mã thông báo

### 00:05:31.860 - 00:05:37.660
Vì vậy, sẽ tạo ra sự khác biệt nếu nó ở đâu đó trong câu hoặc ở ngay đầu câu

### 00:05:37.660 - 00:05:39.660
Và

### 00:05:40.180 - 00:05:48.300
Trên thực tế, không có gì ngạc nhiên khi mã thông báo được tạo cho các dấu chấm luôn giống nhau nên 13 ở cuối câu và

### 00:05:48.620 - 00:05:53.740
Nó chắc chắn tạo ra sự khác biệt nếu bạn sử dụng dấu chấm hay không khi viết câu

### 00:05:53.900 - 00:05:55.900
Vì vậy, bạn thực sự nên làm điều này và

### 00:05:56.460 - 00:06:01.180
Nếu không, điều này có thể dẫn đến phản hồi và đầu ra có chất lượng thấp hơn

### 00:06:01.180 - 00:06:10.660
Vì vậy, đây là khái niệm về mã thông báo và bạn có thể làm vậy nếu bạn có thể tìm thấy ở đây một số ví dụ và một số chi tiết khác

### 00:06:14.340 - 00:06:17.340
Nhưng bây giờ chúng ta hãy chuyển đến công cụ mã thông báo và

### 00:06:18.500 - 00:06:20.500
Tại đây bạn có thể phân tích

### 00:06:21.139 - 00:06:23.980
Văn bản của riêng bạn và chỉ chia thành các mã thông báo

### 00:06:24.340 - 00:06:29.220
Vì vậy, hãy sao chép và dán vào đây khối văn bản nhỏ này

### 00:06:29.500 - 00:06:34.259
Vì vậy, điều quan trọng là phải biết rằng quy trình mã thông báo chính xác blah blah blah và

### 00:06:35.020 - 00:06:40.340
Ở đây chúng ta có thể tìm thấy sự chia thành các mã thông báo. Vậy chúng ta có 48 token và

### 00:06:41.660 - 00:06:43.660
238 ký tự

### 00:06:44.379 - 00:06:46.379
vì vậy, ví dụ như nó

### 00:06:46.660 - 00:06:52.060
Ở đầu câu là một mã thông báo riêng biệt với ID ý tưởng mã thông báo

### 00:06:52.060 - 00:06:54.060
1226

### 00:06:55.660 - 00:07:01.780
Vì vậy, chơi quanh đây với mã thông báo chắc chắn rất thú vị. Vì vậy, vui lòng dùng thử và

### 00:07:03.259 - 00:07:06.060
Chúng ta đã xem hết video này

### 00:07:06.459 - 00:07:12.579
Vì vậy, các thông điệp rút ra mà ít nhất bạn nên biết và hiểu khái niệm về mã thông báo và

### 00:07:13.139 - 00:07:15.860
Đó là giới hạn trong GDP trò chuyện

### 00:07:16.139 - 00:07:20.780
Vì vậy, hiện tại, ít nhất đối với ba mô hình GPT, giới hạn này là

### 00:07:21.980 - 00:07:24.740
4.096 trên 97 mã thông báo và

### 00:07:26.060 - 00:07:32.420
Tôi sẽ nêu bật và giải thích thêm về điều này trong một trong các phần tiếp theo. Cảm ơn đã xem và hẹn gặp bạn ở đó. Tạm biệt

