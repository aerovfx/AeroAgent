## Nội dung

### 00:00:01.000 - 00:00:06.000
Trong video này, chúng ta sẽ triển khai phần thứ hai của thuật toán Sarsa sâu ở phần trước.

### 00:00:06.000 - 00:00:12.000
video mà chúng tôi đã dừng lại tại thời điểm chúng tôi chèn chuyển đổi trạng thái vào bộ nhớ phát lại trải nghiệm.

### 00:00:14.000 - 00:00:17.000
Bây giờ những gì chúng ta phải thực hiện là phần này ở đây.

### 00:00:19.000 - 00:00:26.000
Và điều chúng ta phải làm là thu thập một loạt kinh nghiệm, chọn hành động cho trạng thái tiếp theo và tính toán

### 00:00:26.000 - 00:00:27.000
hàm chi phí.

### 00:00:30.000 - 00:00:36.000
Hàm chi phí sẽ là sai số bình phương trung bình giữa ước tính giá trị Q và mục tiêu của nó.

### 00:00:37.000 - 00:00:44.000
Mục tiêu, như bạn đã biết, là phần thưởng đầu tiên, cộng với giá trị của trạng thái tiếp theo và hành động tiếp theo

### 00:00:44.000 - 00:00:45.000
được chiết khấu bởi gamma.

### 00:00:46.000 - 00:00:48.000
Giống như chúng ta đã làm trong phương pháp dạng bảng.

### 00:00:50.000 - 00:00:55.000
Mỗi một sự khác biệt đó sẽ bình phương chúng và sau đó chúng ta sẽ tính mức trung bình của chúng.

### 00:00:56.000 - 00:01:00.000
Và đó là hàm chi phí mà chúng ta gọi là sai số bình phương trung bình.

### 00:01:00.000 - 00:01:05.000
Sự khác biệt duy nhất là bây giờ giá trị Q ước tính trong giá trị mục tiêu, chúng ta sẽ tính nó

### 00:01:05.000 - 00:01:10.000
sử dụng mạng mục tiêu để những ước tính này vẫn ổn định.

### 00:01:12.000 - 00:01:13.000
Vì vậy, hãy làm điều đó.

### 00:01:13.000 - 00:01:17.000
Đầu tiên chúng ta cần kiểm tra xem bộ nhớ có đủ chuyển tiếp hay không.

### 00:01:21.000 - 00:01:23.000
Để có thể rút ra được nhiều kinh nghiệm.

### 00:01:25.000 - 00:01:26.000
Vì điều đó.

### 00:01:26.000 - 00:01:33.000
Chúng tôi sử dụng hàm lấy mẫu can mà chúng tôi đã xác định và cung cấp cho nó kích thước của lô mà chúng tôi muốn

### 00:01:33.000 - 00:01:33.000
lấy.

### 00:01:35.000 - 00:01:38.000
Nếu có thể, chúng tôi sẽ rút kinh nghiệm.

### 00:01:39.000 - 00:01:40.000
Chúng tôi sẽ có.

### 00:01:43.000 - 00:01:44.000
Một tensor với tất cả các trạng thái.

### 00:01:45.000 - 00:01:47.000
Một cái khác với tất cả các hành động.

### 00:01:48.000 - 00:01:50.000
Một cái khác cho phần thưởng.

### 00:01:52.000 - 00:01:53.000
Một cái khác cho những giá trị ngu ngốc.

### 00:01:55.000 - 00:01:56.000
Và.

### 00:01:57.000 - 00:01:58.000
Một cái khác.

### 00:01:59.000 - 00:02:00.000
Cho tám người tiếp theo.

### 00:02:01.000 - 00:02:08.000
Và chúng ta sẽ lấy các tensor đó gọi phương thức mẫu trên bộ nhớ và đưa nó làm đối số cho lô

### 00:02:08.000 - 00:02:09.000
kích cỡ.

### 00:02:13.000 - 00:02:18.000
Khi chúng ta có những phần tử đó, việc tiếp theo chúng ta sẽ làm là tính giá trị Q của các Bang.

### 00:02:20.000 - 00:02:22.000
Chúng ta sẽ gọi lô giá trị Q.

### 00:02:23.000 - 00:02:25.000
Hoa Kỳ được.

### 00:02:26.000 - 00:02:31.000
Và chúng ta sẽ có được nó bằng cách chuyển trạng thái tới mạng lưới thần kinh.

### 00:02:33.000 - 00:02:37.000
Điều này sẽ cung cấp cho chúng ta giá trị q cho tất cả các hành động ở trạng thái đó.

### 00:02:39.000 - 00:02:42.000
Và sau đó sử dụng phương pháp thu thập.

### 00:02:43.000 - 00:02:44.000
Sẽ chọn.

### 00:02:45.000 - 00:02:47.000
Giá trị của hành động.

### 00:02:48.000 - 00:02:50.000
Mà đại lý đã chọn.

### 00:02:53.000 - 00:02:58.000
Tiếp theo, chúng ta sẽ chọn hành động mà chính sách chọn cho trạng thái tiếp theo.

### 00:03:01.000 - 00:03:03.000
Hãy nhớ rằng trong quy tắc cập nhật của.

### 00:03:06.000 - 00:03:10.000
Chúng tôi sử dụng hành động được chọn theo chính sách khám phá.

### 00:03:10.000 - 00:03:17.000
Và vì thuật toán Sarsa tuân theo chiến lược thăm dò chính sách nên chính sách thăm dò sẽ

### 00:03:17.000 - 00:03:21.000
giống như cái mà chúng ta sử dụng trong quá trình học tập.

### 00:03:25.000 - 00:03:27.000
Vì vậy, những gì chúng tôi sẽ làm là gọi chính sách.

### 00:03:29.000 - 00:03:31.000
Trên lô trạng thái tiếp theo.

### 00:03:33.000 - 00:03:39.000
Và chúng ta sẽ gán cho nó giá trị epsilon mà chúng ta đã chọn trong thuật toán.

### 00:03:40.000 - 00:03:44.000
Tiếp theo chúng ta phải lấy giá trị của mục tiêu.

### 00:03:45.000 - 00:03:46.000
Và chúng tôi sẽ làm điều đó.

### 00:03:53.000 - 00:03:55.000
Bằng cách gọi mạng lưới thần kinh.

### 00:04:00.000 - 00:04:02.000
Vào đợt hẹn hò tiếp theo.

### 00:04:05.000 - 00:04:07.000
Và sử dụng phương pháp thu thập.

### 00:04:09.000 - 00:04:14.000
Để chọn giá trị của hành động được chọn bởi chính sách.

### 00:04:19.000 - 00:04:19.000
Được rồi.

### 00:04:19.000 - 00:04:20.000
Chúng ta phải làm gì bây giờ?

### 00:04:22.000 - 00:04:29.000
Bây giờ những gì chúng ta sẽ làm là sử dụng giá trị của trạng thái tiếp theo và loạt phần thưởng để tính toán mục tiêu

### 00:04:29.000 - 00:04:30.000
giá trị.

### 00:04:31.000 - 00:04:34.000
Và giá trị mục tiêu sẽ là phần thưởng.

### 00:04:38.000 - 00:04:39.000
Gama.

### 00:04:40.000 - 00:04:42.000
Nhân với giá trị tiếp theo.

### 00:04:45.000 - 00:04:48.000
Tuy nhiên, chúng ta phải thực hiện một chút điều chỉnh.

### 00:04:48.000 - 00:04:51.000
Nếu hành động được thực hiện bởi tác nhân đưa chúng ta đến mục tiêu.

### 00:04:52.000 - 00:04:56.000
Khi đó giá trị của trạng thái tiếp theo sẽ bằng 0.

### 00:04:56.000 - 00:05:03.000
Và để thể hiện điều đó, chúng ta sẽ sử dụng biến Don mà chúng ta đã lưu trong bộ nhớ để thực hiện việc này

### 00:05:03.000 - 00:05:04.000
hoạt động.

### 00:05:11.000 - 00:05:12.000
Điều này có nghĩa là gì?

### 00:05:12.000 - 00:05:17.000
Biểu tượng này ở đây có nghĩa ngược lại với xong.

### 00:05:19.000 - 00:05:22.000
Nghĩa là, nếu được thực hiện, sẽ chứa một giá trị sai.

### 00:05:22.000 - 00:05:26.000
Khi chúng ta áp dụng thao tác này thì nó sẽ trở thành sự thật.

### 00:05:26.000 - 00:05:30.000
Và nếu giá trị là đúng thì nó sẽ trở thành sai.

### 00:05:30.000 - 00:05:35.000
Nếu kết quả của việc áp dụng thao tác này là đúng thì giá trị số của nó sẽ là một.

### 00:05:35.000 - 00:05:39.000
Và nếu sai thì giá trị số của nó sẽ bằng 0.

### 00:05:39.000 - 00:05:43.000
Nếu tập phim đã kết thúc, done sẽ là sự thật.

### 00:05:43.000 - 00:05:46.000
Với toán tử này, chúng ta sẽ chuyển nó thành sai.

### 00:05:46.000 - 00:05:54.000
Và vì false có giá trị bằng 0, nên kết quả chúng ta đạt được khi nhân giá trị với số lần thực hiện là chuyển đổi

### 00:05:54.000 - 00:05:57.000
giá trị thành 0.

### 00:05:57.000 - 00:06:03.000
Và nếu done có giá trị sai thì việc áp dụng thao tác này sẽ biến giá trị thành đúng.

### 00:06:04.000 - 00:06:12.000
Giá trị số của true là một và khi chúng ta nhân nó với giá trị thì kết quả là giá trị

### 00:06:12.000 - 00:06:13.000
mà không có bất kỳ thay đổi nào.

### 00:06:13.000 - 00:06:17.000
Vì vậy, những gì chúng tôi đạt được với sự điều chỉnh này là không.

### 00:06:17.000 - 00:06:25.000
Giá trị của trạng thái tiếp theo và hành động tiếp theo chỉ khi trạng thái đó là trạng thái cuối, nghĩa là nếu

### 00:06:25.000 - 00:06:27.000
nhiệm vụ đã kết thúc.

### 00:06:27.000 - 00:06:32.000
Khi đã có giá trị mục tiêu, chúng ta có thể tính hàm chi phí.

### 00:06:32.000 - 00:06:39.000
Chúng ta sẽ định nghĩa một biến gọi là loss và biến này sẽ lưu trữ giá trị của hàm chi phí cho

### 00:06:39.000 - 00:06:40.000
loạt trải nghiệm này.

### 00:06:40.000 - 00:06:49.000
Chúng tôi sẽ sử dụng hàm lỗi F dot MSC được nhập từ thư viện PyTorch và chúng tôi sẽ cung cấp cho nó một loạt

### 00:06:49.000 - 00:06:52.000
giá trị và lô mục tiêu.

### 00:06:52.000 - 00:06:57.000
Và hàm này sẽ tính sai số bình phương trung bình giữa các giá trị đó.

### 00:06:57.000 - 00:07:03.000
Khi chúng ta đã có hàm chi phí, bây giờ là lúc áp dụng quy tắc cập nhật cho các tham số của mạng nơron.

### 00:07:03.000 - 00:07:07.000
mạng và chúng tôi sẽ thực hiện điều đó với ba dòng mã.

### 00:07:07.000 - 00:07:13.000
Đầu tiên là gọi hàm Zerograd trên mạng nơ-ron.

### 00:07:14.000 - 00:07:20.000
Và điều này sẽ làm là loại bỏ các gradient mà chúng ta đã tính toán trước đó.

### 00:07:20.000 - 00:07:26.000
Về cơ bản, chúng tôi đang loại bỏ các gradient trước đó để có thể tính toán các gradient mới.

### 00:07:29.000 - 00:07:37.000
Sau đó, chúng ta sẽ gọi phương thức lùi trên tensor cuối cùng và điều này sẽ bắt đầu quá trình lan truyền ngược.

### 00:07:38.000 - 00:07:42.000
Đó là quá trình sẽ tính toán độ dốc.

### 00:07:43.000 - 00:07:48.000
Hàm chi phí đối với từng tham số của mạng nơ-ron.

### 00:07:51.000 - 00:07:57.000
Và bước thứ ba chúng ta sẽ làm là gọi phương thức step trên đối tượng tối ưu hóa.

### 00:07:59.000 - 00:08:04.000
Như bạn đã biết, đối tượng này thực hiện việc cập nhật các thông số của mạng nơ-ron.

### 00:08:05.000 - 00:08:11.000
Và đó là một biến thể của thuật toán giảm độ dốc ngẫu nhiên mà chúng ta đã thấy trước đây.

### 00:08:16.000 - 00:08:20.000
Và một khi chúng tôi làm xong việc đó, mạng lưới thần kinh của chúng tôi sẽ được cập nhật.

### 00:08:20.000 - 00:08:21.000
Điều tiếp theo chúng ta sẽ làm.

### 00:08:23.000 - 00:08:26.000
Được dạy trong từ điển thống kê của chúng tôi.

### 00:08:27.000 - 00:08:30.000
Giá trị của hàm chi phí cho lô này.

### 00:08:34.000 - 00:08:43.000
Hãy gọi mục dấu chấm mất mát để tensor có giá trị mất mát trở thành một python float và chúng ta có thể lưu trữ

### 00:08:43.000 - 00:08:45.000
nó trong từ điển.

### 00:08:49.000 - 00:08:52.000
Và với điều này, chúng ta đã hoàn thành vòng lặp bên trong.

### 00:08:53.000 - 00:08:55.000
Bây giờ tất cả những gì chúng ta phải làm là phân công lại.

### 00:08:58.000 - 00:09:02.000
Biến trạng thái để lần sau chúng ta cập nhật trạng thái tiếp theo.

### 00:09:05.000 - 00:09:08.000
Và chúng tôi cũng phải cập nhật sự trở lại của tập phim.

### 00:09:17.000 - 00:09:22.000
Chúng tôi sẽ gọi giá trị vật phẩm trên phần thưởng để lưu trữ dưới dạng số thập phân.

### 00:09:27.000 - 00:09:27.000
Kế tiếp.

### 00:09:27.000 - 00:09:31.000
Khi tập phim kết thúc, chúng ta sẽ bắt đầu quay lại tập phim.

### 00:09:42.000 - 00:09:47.000
Và mỗi số tập nhất định sẽ đồng bộ hóa các giá trị.

### 00:09:48.000 - 00:09:50.000
Của mạng lưới của chúng tôi.

### 00:09:51.000 - 00:09:54.000
Và mạng mục tiêu của nó.

### 00:09:56.000 - 00:09:59.000
Hãy làm điều đó cứ sau mười tập.

### 00:10:01.000 - 00:10:05.000
Nghĩa là, nếu tập modulo mười bằng 0.

### 00:10:05.000 - 00:10:13.000
Nghĩa là cứ mười tập chúng tôi sẽ gọi phương thức chính tả trạng thái tải trên mạng và chúng tôi sẽ chuyển nó sang

### 00:10:13.000 - 00:10:16.000
từ điển trạng thái của mạng nơ-ron khác.

### 00:10:27.000 - 00:10:32.000
Đây là một từ điển lưu trữ trạng thái của mạng lưới thần kinh khác.

### 00:10:32.000 - 00:10:35.000
Vì vậy, tóm lại, những gì chúng tôi đang làm.

### 00:10:36.000 - 00:10:38.000
Đang tải một bản sao.

### 00:10:41.000 - 00:10:42.000
Của Mạng Q.

### 00:10:44.000 - 00:10:46.000
Và cuối cùng chúng ta đã hoàn thành thuật toán.

### 00:10:50.000 - 00:10:52.000
Hãy dọn dẹp cái này một chút.

### 00:10:56.000 - 00:10:56.000
Rất tiếc.

### 00:10:57.000 - 00:10:58.000
Đây.

### 00:10:58.000 - 00:10:59.000
Chúng tôi đã thiếu một chữ T.

### 00:11:02.000 - 00:11:05.000
Được rồi, bây giờ chúng tôi đã sẵn sàng thuật toán của mình.

### 00:11:05.000 - 00:11:07.000
Hãy chạy tế bào này.

### 00:11:08.000 - 00:11:10.000
Và bây giờ hãy gọi thuật toán.

### 00:11:12.000 - 00:11:17.000
Hãy viết số liệu thống kê, đó là kết quả của việc gọi phương thức.

### 00:11:18.000 - 00:11:19.000
Và chúng ta sẽ vượt qua nó.

### 00:11:19.000 - 00:11:20.000
Mạng lưới thần kinh.

### 00:11:21.000 - 00:11:23.000
Ngoài ra chính sách.

### 00:11:24.000 - 00:11:27.000
1500 tập.

### 00:11:29.000 - 00:11:33.000
Và tham số cuối cùng sẽ cung cấp cho nó là Epsilon.

### 00:11:37.000 - 00:11:39.000
Hãy chạy tế bào này.

### 00:11:40.000 - 00:11:45.000
Và như bạn đã biết, tùy thuộc vào sức mạnh máy tính của bạn, việc này sẽ mất vài phút.

### 00:11:46.000 - 00:11:48.000
Tôi sẽ gặp bạn khi nó kết thúc.

