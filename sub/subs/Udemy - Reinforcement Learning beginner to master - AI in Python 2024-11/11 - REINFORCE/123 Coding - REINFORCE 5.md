## Nội dung

### 00:00:00.000 - 00:00:05.000
Trong video này, chúng ta sẽ triển khai phần thứ hai của thuật toán củng cố.

### 00:00:05.000 - 00:00:08.000
Đây là phần mà chúng tôi cải thiện chính sách.

### 00:00:08.000 - 00:00:15.000
Đầu tiên, chúng tôi sẽ khai báo lợi nhuận thu được cho mỗi tập trong mỗi môi trường song song dưới dạng

### 00:00:15.000 - 00:00:17.000
vectơ số không.

### 00:00:21.000 - 00:00:29.000
Hãy gọi nó là G và chúng ta sẽ khởi tạo nó bằng cách sử dụng hàm số 0 từ PyTorch, cho nó quyền

### 00:00:29.000 - 00:00:36.000
hình dạng, như bạn biết, sẽ là số lượng môi trường song song trên chiều thứ nhất.

### 00:00:36.000 - 00:00:41.000
Và một cột duy nhất vì kết quả trả về là một giá trị duy nhất.

### 00:00:43.000 - 00:00:50.000
Điều tiếp theo chúng ta cần làm, như bạn có thể thấy trong thuật toán, là lặp lại từng thời điểm trong

### 00:00:50.000 - 00:00:52.000
thời gian theo thứ tự ngược lại.

### 00:00:53.000 - 00:00:58.000
Ý tôi là chúng ta sẽ thực hiện vòng lặp này với giá trị t trừ một.

### 00:00:58.000 - 00:01:05.000
Sau đó T trừ hai, t trừ ba, v.v. và cứ tiếp tục như vậy cho đến khi chúng ta đến phần đầu của tập phim.

### 00:01:07.000 - 00:01:09.000
Và để làm điều đó, chúng ta sẽ khai báo biến T.

### 00:01:13.000 - 00:01:18.000
Và nội dung của danh sách chuyển tiếp tại thời điểm đó.

### 00:01:20.000 - 00:01:22.000
Đó là trạng thái tại thời điểm t.

### 00:01:23.000 - 00:01:25.000
Hành động tại thời điểm t và phần thưởng.

### 00:01:27.000 - 00:01:32.000
Và chúng ta sẽ làm điều đó bằng cách đảo ngược việc liệt kê danh sách các chuyển tiếp.

### 00:01:35.000 - 00:01:36.000
Liệt kê.

### 00:01:38.000 - 00:01:40.000
Sẽ cung cấp cho chúng tôi các yếu tố từ danh sách.

### 00:01:42.000 - 00:01:44.000
Cũng như một chỉ mục.

### 00:01:45.000 - 00:01:48.000
Với vị trí của từng phần tử.

### 00:01:50.000 - 00:01:58.000
Và các dòng sông sẽ thay đổi thứ tự của các phần tử được liệt kê để trước tiên chúng ta truy cập phần tử cuối cùng và

### 00:01:58.000 - 00:02:03.000
chúng tôi lặp lại theo thứ tự ngược lại cho đến khi chúng tôi đạt được phần tử ở đầu danh sách.

### 00:02:04.000 - 00:02:12.000
Bây giờ những gì chúng ta phải làm là cập nhật giá trị tiền lãi thành tổng của phần thưởng, cộng với số tiền đang chạy

### 00:02:12.000 - 00:02:15.000
giá trị lợi nhuận được chiết khấu bởi Gamma.

### 00:02:15.000 - 00:02:22.000
Hãy viết G bằng phần thưởng tại thời điểm T cộng gamma nhân G.

### 00:02:23.000 - 00:02:28.000
Và bây giờ chúng ta có phần thưởng của nhà nước đang được thực hiện vào thời điểm này.

### 00:02:28.000 - 00:02:36.000
Tiếp theo, chúng ta cần tính các giá trị của phương trình này, bắt đầu bằng logarit của xác suất

### 00:02:36.000 - 00:02:39.000
của việc lựa chọn hành động được lựa chọn bởi chính sách.

### 00:02:43.000 - 00:02:44.000
Để làm điều đó.

### 00:02:44.000 - 00:02:49.000
Điều đầu tiên chúng ta sẽ làm là gọi chính sách có trạng thái tại thời điểm T.

### 00:02:53.000 - 00:02:59.000
Và điều đó sẽ cho chúng ta một vectơ xác suất cho trạng thái của từng môi trường.

### 00:03:00.000 - 00:03:01.000
Vào thời điểm đó.

### 00:03:04.000 - 00:03:08.000
Và đối với vectơ xác suất đó sẽ tính toán.

### 00:03:10.000 - 00:03:12.000
logarit của nó.

### 00:03:14.000 - 00:03:17.000
Với chức năng ghi dấu chấm ngọn đuốc.

### 00:03:23.000 - 00:03:29.000
Hãy nhớ rằng nếu xác suất bằng 0, hàm này sẽ cho chúng ta một lỗi số.

### 00:03:31.000 - 00:03:38.000
Vì vậy, để tránh điều đó, chúng ta phải thêm một hằng số rất nhỏ vào đầu vào của hàm log.

### 00:03:39.000 - 00:03:42.000
Vì vậy mà chúng tôi giữ được sự ổn định của hoạt động này.

### 00:03:46.000 - 00:03:50.000
Tiếp theo, chúng ta phải chọn từ vectơ xác suất nhật ký đó.

### 00:03:51.000 - 00:03:53.000
Chỉ có xác suất thôi.

### 00:03:54.000 - 00:04:00.000
Liên kết với hành động được thực hiện vào thời điểm hiện tại, hành động sẽ tham gia vào quá trình cập nhật

### 00:04:00.000 - 00:04:01.000
luật lệ.

### 00:04:01.000 - 00:04:07.000
Để làm được điều đó, chúng tôi tạo một biến gọi là thuộc tính nhật ký hành động.

### 00:04:11.000 - 00:04:15.000
Và chúng ta sẽ thu được giá trị đó bằng phương thức thu thập.

### 00:04:20.000 - 00:04:26.000
Áp dụng cho chiều thứ nhất và lấy chỉ mục của hành động mà chúng ta quan tâm.

### 00:04:30.000 - 00:04:31.000
Được rồi.

### 00:04:33.000 - 00:04:41.000
Bây giờ tất cả những gì chúng ta phải làm là tính entropy của từng vectơ xác suất tại thời điểm này.

### 00:04:46.000 - 00:04:48.000
Hãy tạo một biến gọi là entropy.

### 00:04:50.000 - 00:04:54.000
Và chúng ta biết rằng entropy là số âm của tổng.

### 00:04:56.000 - 00:04:57.000
Về xác suất.

### 00:04:58.000 - 00:05:01.000
Nhân với xác suất nhật ký của họ.

### 00:05:04.000 - 00:05:06.000
Chúng tôi sẽ cung cấp cho hoạt động này.

### 00:05:06.000 - 00:05:14.000
Đối số được coi là bằng 1 để tổng được áp dụng độc lập và chúng ta nhận được giá trị cho entropy

### 00:05:14.000 - 00:05:17.000
của từng vectơ xác suất riêng lẻ.

### 00:05:17.000 - 00:05:24.000
Và điều quan trọng nữa là đưa ra lập luận cho chúng đúng như nhau, sao cho các kích thước của

### 00:05:24.000 - 00:05:30.000
tensor vẫn không thay đổi vì PyTorch, khi nó có khả năng giảm kích thước của

### 00:05:30.000 - 00:05:32.000
tensor đầu ra sẽ làm việc đó.

### 00:05:32.000 - 00:05:39.000
Ví dụ: khi lấy một phần tử từ một vectơ, theo mặc định, nó sẽ giảm kích thước của nó.

### 00:05:39.000 - 00:05:44.000
Và chúng ta muốn nó giữ nguyên kích thước của tensor như hiện tại.

### 00:05:44.000 - 00:05:52.000
Bây giờ tất cả những gì chúng ta phải làm là tính giá trị tia gamma thành t sẽ thu được khá dễ dàng chỉ bằng cách tăng

### 00:05:52.000 - 00:05:53.000
gamma không đổi.

### 00:06:01.000 - 00:06:08.000
Và bây giờ chúng ta đã sẵn sàng tính toán ước tính về hiệu quả hoạt động của chính sách.

### 00:06:13.000 - 00:06:16.000
Hãy gọi đó là mất PG.

### 00:06:16.000 - 00:06:18.000
Mất độ dốc chính sách.

### 00:06:23.000 - 00:06:27.000
Và chúng ta sẽ gán cho nó giá trị tia gamma âm.

### 00:06:30.000 - 00:06:30.000
Thời đại.

### 00:06:31.000 - 00:06:32.000
Vấn đề nhật ký hành động.

### 00:06:34.000 - 00:06:35.000
Thời đại.

### 00:06:38.000 - 00:06:42.000
Và với điều này, chúng ta đã hoàn thành phần này ở đây.

### 00:06:42.000 - 00:06:49.000
Bây giờ tất cả những gì chúng ta phải làm là trừ đi entropy, đây là một giá trị sẽ giúp chúng ta chuẩn hóa

### 00:06:49.000 - 00:06:50.000
quá trình học tập.

### 00:06:50.000 - 00:06:57.000
Sau đó, chúng tôi sẽ tính giá trị trung bình của giá trị này trên từng môi trường mà tác nhân đang phải đối mặt

### 00:06:57.000 - 00:06:58.000
song song.

### 00:06:58.000 - 00:07:01.000
Và chúng ta sẽ làm điều này theo cách chúng ta sẽ viết sau đây.

### 00:07:02.000 - 00:07:03.000
Tổng số tổn thất.

### 00:07:03.000 - 00:07:06.000
Hãy mở ngoặc và viết PG.

### 00:07:07.000 - 00:07:08.000
Bị mất điểm trừ.

### 00:07:10.000 - 00:07:13.000
Một hệ số nhỏ, chẳng hạn như 0 dấu phẩy 0 một.

### 00:07:14.000 - 00:07:15.000
Nhân lên.

### 00:07:17.000 - 00:07:18.000
Bằng entropy.

### 00:07:21.000 - 00:07:25.000
Và trên cột vectơ kết quả sẽ tính giá trị trung bình.

### 00:07:29.000 - 00:07:33.000
Tuy nhiên, theo cách đó, tổn thất sẽ là một giá trị duy nhất.

### 00:07:34.000 - 00:07:40.000
Và bây giờ, như mọi khi, khi chúng ta làm việc với mạng nơ-ron, điều đầu tiên chúng ta cần làm là xóa sạch

### 00:07:40.000 - 00:07:42.000
độ dốc của mạng lưới thần kinh.

### 00:07:44.000 - 00:07:49.000
Tiếp theo chúng ta sẽ gọi dấu chấm tổn thất tổng cộng là dấu lùi.

### 00:07:52.000 - 00:07:59.000
Phương pháp lùi này sẽ khởi chạy thuật toán Backpropagation để tính toán độ dốc của tổn thất

### 00:07:59.000 - 00:08:03.000
hoạt động tương ứng với từng tham số của mạng nơ-ron.

### 00:08:03.000 - 00:08:08.000
Và cuối cùng, chúng ta sẽ gọi phương thức step trên đối tượng tối ưu hóa.

### 00:08:11.000 - 00:08:13.000
Đó là đối tượng.

### 00:08:17.000 - 00:08:19.000
Điều đó sẽ thực hiện quy tắc cập nhật.

### 00:08:20.000 - 00:08:25.000
Tuy nhiên, hãy lưu ý rằng ở đây chúng tôi đã viết hiệu suất của chính sách ở dạng Phủ định.

### 00:08:25.000 - 00:08:26.000
Tại sao vậy?

### 00:08:26.000 - 00:08:34.000
Chà, đó là vì đối tượng Adam W mà chúng ta đã tạo chỉ có thể thực hiện giảm độ dốc.

### 00:08:34.000 - 00:08:42.000
Nghĩa là, nó di chuyển các tham số của mạng lưới thần kinh theo hướng ngược lại với tốc độ tăng trưởng tối đa.

### 00:08:42.000 - 00:08:46.000
Và trong trường hợp của chúng tôi, chúng tôi đang thực hiện tăng dần độ dốc.

### 00:08:46.000 - 00:08:49.000
Tức là chúng ta đang di chuyển các tham số của mạng lưới thần kinh.

### 00:08:50.000 - 00:08:53.000
Theo hướng tăng trưởng tối đa.

### 00:08:56.000 - 00:09:00.000
Bởi vì biểu thức này là hiệu suất của chính sách.

### 00:09:01.000 - 00:09:08.000
Vâng, ít nhất là ước tính về hiệu suất của chính sách và chúng tôi muốn tối đa hóa hiệu suất đó.

### 00:09:08.000 - 00:09:18.000
Vì vậy, những gì chúng ta đã làm là thay đổi dấu của biểu thức đó sao cho đối tượng Adam W cực tiểu hóa âm

### 00:09:18.000 - 00:09:23.000
hiệu suất, tương đương với việc tối đa hóa hiệu suất của chính sách.

### 00:09:24.000 - 00:09:31.000
Đây chỉ đơn giản là một thay đổi nhỏ mà chúng ta phải thực hiện để có thể làm việc với thư viện PyTorch.

### 00:09:31.000 - 00:09:32.000
Được rồi.

### 00:09:32.000 - 00:09:34.000
Và bây giờ thuật toán của chúng tôi đã hoàn tất.

### 00:09:34.000 - 00:09:39.000
Tất cả những gì chúng ta phải làm là lưu trữ số liệu thống kê thực hiện trong từ điển thống kê.

### 00:09:42.000 - 00:09:43.000
Bên trong nó.

### 00:09:43.000 - 00:09:45.000
Chúng tôi sẽ giữ hai giá trị.

### 00:09:47.000 - 00:09:48.000
Cái đầu tiên.

### 00:09:52.000 - 00:09:54.000
Là giá trị của hàm mất mát.

### 00:09:58.000 - 00:10:03.000
Và chúng tôi sẽ lưu trữ nó dưới dạng mục chấm tổn thất tổng cộng.

### 00:10:05.000 - 00:10:11.000
Hãy nhớ rằng mục này chuyển đổi một tensor pytorch thành một số vô hướng.

### 00:10:13.000 - 00:10:18.000
Và chúng tôi cũng sẽ lưu trữ trong từ điển của mình số tiền thu được trong các tập phim.

### 00:10:29.000 - 00:10:36.000
Chúng tôi sẽ tính toán lợi nhuận trung bình thu được trong các môi trường song song và điều đó có nghĩa là chúng tôi sẽ chuyển đổi nó thành

### 00:10:36.000 - 00:10:37.000
một giá trị trăn.

### 00:10:39.000 - 00:10:46.000
Và cuối cùng, chúng tôi sẽ trả về số liệu thống kê thực thi và bây giờ thuật toán của chúng tôi đã sẵn sàng để thực thi.

### 00:10:47.000 - 00:10:50.000
Hãy kiểm tra xem mọi thứ đã theo thứ tự chưa.

### 00:10:52.000 - 00:10:52.000
Ối.

### 00:10:52.000 - 00:10:55.000
Ví dụ ở đây, chúng ta đã mắc một lỗi nhỏ.

### 00:10:56.000 - 00:10:58.000
Chúng ta cần một dấu trừ.

### 00:11:02.000 - 00:11:03.000
Được rồi, chúng ta hãy tiếp tục tìm kiếm.

### 00:11:06.000 - 00:11:09.000
Dòng này thiếu dấu hai chấm.

### 00:11:16.000 - 00:11:19.000
Và ở đây, bản ghi nhật ký hành động bị thiếu t.

### 00:11:23.000 - 00:11:28.000
Và có vẻ như phần thưởng thiếu chữ S ở cuối.

### 00:11:30.000 - 00:11:32.000
Và bây giờ hãy thực hiện thuật toán.

### 00:11:34.000 - 00:11:40.000
Nhưng trước đó, hãy thiết lập lại môi trường vì trước đây chúng ta đã can thiệp vào nó.

### 00:11:46.000 - 00:11:50.000
Được rồi, bây giờ hãy gọi phương thức củng cố.

### 00:11:51.000 - 00:11:55.000
Với chính sách của chúng tôi và.

### 00:11:55.000 - 00:11:57.000
200 tập.

### 00:12:00.000 - 00:12:01.000
Hãy chạy tế bào này.

### 00:12:03.000 - 00:12:05.000
Và nó sẽ mất một vài giây.

### 00:12:08.000 - 00:12:09.000
Và chúng tôi đã trở lại.

### 00:12:10.000 - 00:12:12.000
Mất khoảng 55 giây.

### 00:12:14.000 - 00:12:16.000
Bây giờ chúng ta hãy xem kết quả.

### 00:12:18.000 - 00:12:20.000
Hãy chạy tế bào này.

### 00:12:21.000 - 00:12:22.000
Và họ đây rồi.

### 00:12:24.000 - 00:12:31.000
Như bạn có thể thấy trong 50 tập đầu tiên, lợi nhuận đã được cải thiện cho đến khi đạt mức tối đa

### 00:12:31.000 - 00:12:31.000
giá trị.

### 00:12:32.000 - 00:12:33.000
200.

### 00:12:35.000 - 00:12:38.000
Và hiệu quả thực hiện chính sách cũng đi theo một quỹ đạo tương tự.

### 00:12:40.000 - 00:12:43.000
Bây giờ hãy kiểm tra chính sách mà chúng ta đã học.

### 00:12:44.000 - 00:12:45.000
Vì điều đó.

### 00:12:45.000 - 00:12:49.000
Chúng ta sẽ thực thi nó ở ba trạng thái mà chúng ta đã thấy ở trên.

### 00:12:51.000 - 00:12:52.000
Một trong số đó là trung lập.

### 00:12:53.000 - 00:12:56.000
Mặt khác, sẽ nguy hiểm nếu chúng ta di chuyển sang trái.

### 00:12:57.000 - 00:13:00.000
Và điều cuối cùng, sẽ có nguy hiểm nếu chúng ta di chuyển, phải không?

### 00:13:01.000 - 00:13:04.000
Hãy chạy ba ô này cùng một lúc.

### 00:13:08.000 - 00:13:10.000
Và bây giờ hãy kiểm tra kết quả.

### 00:13:11.000 - 00:13:13.000
Ở trạng thái trung tính.

### 00:13:14.000 - 00:13:18.000
Chính sách này ấn định xác suất di chuyển sang trái cao hơn một chút.

### 00:13:18.000 - 00:13:22.000
Nhưng nhìn chung, cả hai hành động đều có xác suất rất giống nhau.

### 00:13:24.000 - 00:13:26.000
Tuy nhiên, khi có nguy hiểm.

### 00:13:27.000 - 00:13:28.000
Bên trái.

### 00:13:29.000 - 00:13:34.000
Chính sách của chúng tôi quy định khả năng chúng tôi di chuyển sẽ cao hơn nhiều, phải không?

### 00:13:37.000 - 00:13:41.000
Và khi nguy hiểm ở bên phải, chính sách quy định.

### 00:13:42.000 - 00:13:44.000
Di chuyển sang trái.

### 00:13:47.000 - 00:13:51.000
Tuy nhiên, hãy lưu ý rằng xác suất di chuyển sang phải không bằng không.

### 00:13:51.000 - 00:13:53.000
Cũng giống như ở đây, nó cũng không phải vậy.

### 00:13:53.000 - 00:13:59.000
Đó là tác dụng của việc sử dụng entropy như một phương tiện để điều chỉnh quá trình học tập.

### 00:14:01.000 - 00:14:08.000
Vì chúng ta đang cố gắng tối đa hóa entropy nên chúng ta mong muốn chính sách đó không bao giờ chọn được một

### 00:14:08.000 - 00:14:10.000
hành động 100% thời gian.

### 00:14:11.000 - 00:14:16.000
Và điều đó cho phép chúng tôi tiếp tục khám phá các hành động trong thời gian dài hơn.

### 00:14:18.000 - 00:14:24.000
Bây giờ, điều cuối cùng chúng ta phải làm là kiểm tra xem chính sách có khả năng giải quyết được nhiệm vụ hay không.

### 00:14:24.000 - 00:14:26.000
Hãy chạy tế bào này.

### 00:14:26.000 - 00:14:28.000
Và như bạn có thể thấy.

### 00:14:30.000 - 00:14:33.000
Nó có khả năng giữ cột đứng thẳng.

