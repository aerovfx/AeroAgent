## Nội dung

### 00:00:01.000 - 00:00:07.000
Trong video trước, chúng tôi đã chèn quá trình chuyển đổi trạng thái vào bộ nhớ phát lại.

### 00:00:08.000 - 00:00:12.000
Bây giờ là lúc cập nhật mạng lưới thần kinh.

### 00:00:16.000 - 00:00:20.000
Và để làm được điều đó, chúng tôi sẽ kiểm tra xem bộ nhớ có thể tạo mẫu hay không.

### 00:00:22.000 - 00:00:28.000
Ý tôi là chúng ta cần kiểm tra xem bộ nhớ có đủ đầy để rút ra những đợt trải nghiệm hay không.

### 00:00:34.000 - 00:00:39.000
Nếu đúng như vậy thì chúng ta sẽ gọi phương thức mẫu trên bộ nhớ.

### 00:00:40.000 - 00:00:43.000
Để tạo ra một loạt các chuyển tiếp.

### 00:00:44.000 - 00:00:46.000
Đó là một loạt các trạng thái.

### 00:00:48.000 - 00:00:49.000
Một hai phe.

### 00:00:51.000 - 00:00:56.000
Một loạt phần thưởng, một loạt giá trị cho biến Don.

### 00:00:58.000 - 00:01:00.000
Và một loạt các ngày tiếp theo.

### 00:01:04.000 - 00:01:08.000
Và như tôi đã nói, chúng ta đạt được điều đó bằng cách gọi phương thức mẫu.

### 00:01:09.000 - 00:01:12.000
Vượt qua kích thước của lô.

### 00:01:16.000 - 00:01:19.000
Việc tiếp theo chúng ta cần làm là tính toán.

### 00:01:20.000 - 00:01:22.000
Những yếu tố này của quy tắc cập nhật.

### 00:01:24.000 - 00:01:27.000
Giá trị q cho trạng thái tiếp theo và hành động tiếp theo.

### 00:01:28.000 - 00:01:30.000
Của mỗi lần chuyển đổi.

### 00:01:33.000 - 00:01:36.000
Mà bây giờ sẽ được lựa chọn bởi chính sách tham lam.

### 00:01:40.000 - 00:01:46.000
Một cái khác khám phá môi trường, nhưng chính sách luôn chọn hành động cao nhất

### 00:01:47.000 - 00:01:47.000
giá trị.

### 00:01:47.000 - 00:01:51.000
Và dựa trên những yếu tố đó, chúng ta sẽ tính hàm chi phí.

### 00:01:53.000 - 00:01:57.000
Chúng ta sẽ bắt đầu với giá trị của các trạng thái hiện tại.

### 00:02:01.000 - 00:02:04.000
Và chúng ta sẽ gọi mạng lưới thần kinh.

### 00:02:07.000 - 00:02:09.000
Chuyển các trạng thái làm đầu vào.

### 00:02:12.000 - 00:02:16.000
Sau đó, chúng tôi sẽ chọn tại mỗi hàng, tại mỗi lần chuyển đổi.

### 00:02:18.000 - 00:02:20.000
Hành động mà chính sách khám phá đã chọn.

### 00:02:25.000 - 00:02:28.000
Và bây giờ chúng ta sẽ tính các giá trị Q.

### 00:02:30.000 - 00:02:35.000
Đối với trạng thái tiếp theo và hành động tiếp theo của mỗi lần chuyển đổi.

### 00:02:35.000 - 00:02:38.000
Để làm điều đó, chúng tôi sẽ sử dụng mạng mục tiêu.

### 00:02:39.000 - 00:02:46.000
Điều đó sẽ thực hiện các ước tính ổn định vì các tham số của nó không thay đổi sau mỗi lần cập nhật mạng thần kinh.

### 00:02:46.000 - 00:02:52.000
mạng và chúng tôi gọi mạng mục tiêu theo loạt trạng thái tiếp theo.

### 00:02:53.000 - 00:02:58.000
Điều đó sẽ tạo ra giá trị Q của tất cả các hành động cho trạng thái tiếp theo đó.

### 00:03:00.000 - 00:03:02.000
Và bây giờ việc chúng ta phải làm là chọn lọc.

### 00:03:03.000 - 00:03:04.000
Từ những giá trị đó

### 00:03:06.000 - 00:03:10.000
Hành động tương ứng với hành động được chính sách mục tiêu chọn.

### 00:03:10.000 - 00:03:14.000
Tức là chúng ta sẽ chọn giá trị Q cao nhất.

### 00:03:21.000 - 00:03:25.000
Chúng ta sẽ thực hiện điều đó bằng cách gọi hàm max từ thư viện PyTorch.

### 00:03:27.000 - 00:03:29.000
Và chúng tôi muốn áp dụng chức năng này.

### 00:03:30.000 - 00:03:33.000
Hàng khôn ngoan, đó là chiều hướng cuối cùng.

### 00:03:34.000 - 00:03:38.000
Tại mỗi lần chuyển trạng thái, nó phải tìm giá trị cao nhất.

### 00:03:41.000 - 00:03:47.000
Và bên cạnh đó, chúng ta muốn nói với hàm này rằng chúng ta muốn giữ nguyên kích thước của tensor

### 00:03:47.000 - 00:03:55.000
như hiện tại, bởi vì theo mặc định, pytorch, khi nó nhìn thấy một tensor có một phần tử duy nhất trong

### 00:03:55.000 - 00:03:59.000
một chiều cụ thể, nó cố gắng loại bỏ chiều đó.

### 00:04:00.000 - 00:04:07.000
Và khi gọi hàm max bằng thư viện PyTorch, chúng ta phải lấy chỉ mục đầu tiên để có được

### 00:04:07.000 - 00:04:08.000
kết quả thực tế.

### 00:04:10.000 - 00:04:13.000
Chúng ta đã có thể tính toán mục tiêu của hàm chi phí.

### 00:04:16.000 - 00:04:18.000
Hãy viết mục tiêu bằng nhau.

### 00:04:20.000 - 00:04:24.000
Phần thưởng được quan sát thấy ở mỗi lần chuyển đổi trạng thái.

### 00:04:26.000 - 00:04:30.000
Cộng gamma nhân với giá trị Q tiếp theo.

### 00:04:39.000 - 00:04:42.000
Tuy nhiên, để đảm bảo rằng giá trị Q tiếp theo.

### 00:04:43.000 - 00:04:44.000
Bằng không.

### 00:04:44.000 - 00:04:46.000
Nếu nhiệm vụ đã hoàn thành.

### 00:04:47.000 - 00:04:50.000
Chúng ta sẽ làm như trong phần trước.

### 00:04:52.000 - 00:04:55.000
Và nhân mục tiêu với số lần chưa hoàn thành.

### 00:04:58.000 - 00:05:02.000
Điều duy nhất mà điều này sẽ làm là nếu nhiệm vụ kết thúc vào thời điểm này.

### 00:05:05.000 - 00:05:08.000
Ước tính giá trị Q tiếp theo sẽ bằng 0.

### 00:05:08.000 - 00:05:09.000
Như chúng ta có thể mong đợi.

### 00:05:13.000 - 00:05:17.000
Và khi đã có mục tiêu, bây giờ chúng ta có thể tính hàm chi phí.

### 00:05:19.000 - 00:05:22.000
Chúng tôi làm điều đó bằng cách sử dụng chức năng MSG?

### 00:05:24.000 - 00:05:30.000
Từ thư viện PyTorch và chúng tôi chuyển cho nó giá trị cần tối ưu hóa.

### 00:05:31.000 - 00:05:36.000
Và sau đó là mục tiêu mà chúng tôi muốn đẩy các ước tính giá trị tới.

### 00:05:41.000 - 00:05:47.000
Sau đó, chúng tôi sẽ xóa các gradient được tính toán trong mạng nơ-ron để có thể bắt đầu quá trình cập nhật

### 00:05:47.000 - 00:05:48.000
từ đầu.

### 00:05:57.000 - 00:06:01.000
Sau đó chúng ta sẽ gọi phương thức lùi trên tensor mất mát.

### 00:06:03.000 - 00:06:08.000
Để tính toán độ dốc của hàm chi phí đối với các tham số của mạng lưới thần kinh.

### 00:06:09.000 - 00:06:19.000
Và sau đó đối tượng tối ưu hóa chính là đối tượng Adam W này sẽ thực hiện cập nhật các tham số của

### 00:06:19.000 - 00:06:21.000
mạng lưới thần kinh.

### 00:06:22.000 - 00:06:31.000
Hãy nhớ rằng Adam W là một quy tắc cập nhật tương tự như quy tắc giảm độ dốc ngẫu nhiên nhưng có một số cải tiến nhỏ.

### 00:06:32.000 - 00:06:32.000
Được rồi.

### 00:06:32.000 - 00:06:38.000
Chúng tôi đã cập nhật các giá trị của mạng lưới thần kinh và bây giờ là điều tiếp theo chúng tôi sẽ làm

### 00:06:38.000 - 00:06:45.000
là lưu trữ trong từ điển thống kê của chúng tôi giá trị của hàm mất để có thể hiển thị nó bằng đồ họa.

### 00:06:49.000 - 00:06:53.000
Bây giờ tất cả những gì chúng ta phải làm là đóng vòng lặp bên trong.

### 00:06:54.000 - 00:06:56.000
Đang cập nhật trạng thái.

### 00:06:59.000 - 00:07:00.000
Và thêm phần thưởng.

### 00:07:03.000 - 00:07:06.000
Đối với biến trả về EP.

### 00:07:08.000 - 00:07:16.000
Hãy nhớ rằng vì phần thưởng là một tenxơ nên chúng ta gọi mục phương thức để chỉ lưu trữ giá trị số của nó.

### 00:07:16.000 - 00:07:23.000
Việc tiếp theo chúng ta làm là lưu trữ khi tập phim hoàn thành, lợi nhuận mà đại lý đã đạt được

### 00:07:23.000 - 00:07:25.000
trong từ điển thống kê của chúng tôi.

### 00:07:38.000 - 00:07:38.000
Thì đấy.

### 00:07:39.000 - 00:07:46.000
Và bây giờ điều cuối cùng chúng ta phải làm là cứ mỗi số lượng tập nhất định lại cập nhật mạng mục tiêu.

### 00:07:50.000 - 00:07:57.000
Chúng tôi sẽ cập nhật các giá trị của mạng lưới thần kinh mục tiêu cứ sau mười tập, sao chép các giá trị từ

### 00:07:57.000 - 00:08:01.000
mạng đang học trên mạng mục tiêu.

### 00:08:07.000 - 00:08:15.000
Và để làm được điều đó, chúng tôi gọi phương thức trạng thái tải trên mạng mục tiêu và cung cấp cho nó từ điển trạng thái.

### 00:08:17.000 - 00:08:19.000
Của mạng lưới thần kinh khác.

### 00:08:28.000 - 00:08:32.000
Bây giờ tất cả những gì chúng ta phải làm là trả về từ điển thống kê.

### 00:08:34.000 - 00:08:34.000
Xong.

### 00:08:36.000 - 00:08:37.000
Ối.

### 00:08:37.000 - 00:08:39.000
Có một chút sai lầm ở đây.

### 00:08:39.000 - 00:08:40.000
Chúng tôi đã viết.

### 00:08:40.000 - 00:08:42.000
Xong và chúng ta nên viết.

### 00:08:42.000 - 00:08:43.000
Đã xong lô.

### 00:08:44.000 - 00:08:46.000
Được rồi, hãy thực hiện lại ô này.

### 00:08:46.000 - 00:08:48.000
Và bây giờ chúng ta có thuật toán của mình.

### 00:08:50.000 - 00:08:51.000
Bây giờ, hãy gọi nó.

### 00:08:52.000 - 00:08:56.000
Số liệu thống kê, là kết quả của việc thực hiện thuật toán này.

### 00:08:58.000 - 00:09:00.000
Và chúng tôi vượt qua chức năng này.

### 00:09:00.000 - 00:09:01.000
Mạng lưới thần kinh.

### 00:09:05.000 - 00:09:10.000
Chính sách khám phá và 500 tập.

### 00:09:12.000 - 00:09:13.000
Hãy chạy tế bào.

### 00:09:17.000 - 00:09:19.000
Và một phút sau, việc thực hiện được thực hiện.

### 00:09:21.000 - 00:09:23.000
Bây giờ hãy hiển thị số liệu thống kê.

### 00:09:30.000 - 00:09:31.000
Họ đây rồi.

### 00:09:33.000 - 00:09:40.000
Như bạn có thể thấy lúc đầu, đại lý đã thu được lợi nhuận khoảng mười.

### 00:09:40.000 - 00:09:49.000
Và đến tập 150, lợi nhuận đã bắt đầu được cải thiện cho đến khi đạt giá trị tối đa,

### 00:09:49.000 - 00:09:50.000
đó là 200.

### 00:09:52.000 - 00:10:00.000
Điều cuối cùng mà chúng ta phải làm là thực hiện một bài kiểm tra để xem liệu tác nhân có khả năng giữ pole hay không

### 00:10:00.000 - 00:10:00.000
thẳng.

### 00:10:03.000 - 00:10:08.000
Như bạn có thể thấy, nó có khả năng giữ thẳng cho đến hết tập phim.

