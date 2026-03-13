## Nội dung

### 00:00:00.000 - 00:00:06.000
Trong video này, chúng ta sẽ kết hợp phương pháp chênh lệch thời gian SARSA với quá trình khởi động n bước

### 00:00:06.000 - 00:00:06.000
kỹ thuật.

### 00:00:06.000 - 00:00:12.000
Sự khác biệt so với thuật toán SARSA cổ điển là mục tiêu trong quy tắc cập nhật sẽ

### 00:00:12.000 - 00:00:16.000
chứa phần thưởng 'n' và ước tính những phần thưởng sau.

### 00:00:17.000 - 00:00:23.000
Và ước tính đó sẽ được biểu thị bằng giá trị q của trạng thái và hành động 'n' bước vào

### 00:00:23.000 - 00:00:23.000
tương lai.

### 00:00:24.000 - 00:00:28.000
Như thường lệ, điều đầu tiên chúng ta sẽ làm là nhập các thư viện mã mà chúng ta sắp

### 00:00:28.000 - 00:00:29.000
sử dụng.

### 00:00:29.000 - 00:00:34.000
Trong trường hợp này, chúng sẽ giống như các thuật toán ở phần trước,

### 00:00:34.000 - 00:00:37.000
vì vậy chúng tôi chỉ sao chép chúng từ các sổ ghi chép trước đó.

### 00:00:37.000 - 00:00:42.000
Hãy chạy ô và bây giờ chúng ta có thư viện mã.

### 00:00:43.000 - 00:00:45.000
Tiếp theo, hãy tạo nhiệm vụ sẽ giải quyết được.

### 00:00:46.000 - 00:00:52.000
Như trong các thuật toán trước, chúng ta sẽ làm việc với mê cung 5x5 nơi tác nhân cố gắng tìm

### 00:00:52.000 - 00:00:56.000
lối ra nằm ở góc dưới bên phải.

### 00:00:58.000 - 00:01:03.000
Hãy thực thi ô và bây giờ chúng ta có môi trường của mình.

### 00:01:05.000 - 00:01:08.000
Tiếp theo, chúng ta sẽ tạo bảng giá trị q.

### 00:01:09.000 - 00:01:16.000
Như mọi khi, chúng ta sẽ khởi tạo nó dưới dạng một mảng 5x5x4 chứa đầy các số 0.

### 00:01:22.000 - 00:01:25.000
Hãy chạy nó ra và chúng ta có nó ở đây.

### 00:01:25.000 - 00:01:28.000
Việc tiếp theo chúng ta cần làm là tạo chính sách.

### 00:01:28.000 - 00:01:35.000
Như bạn đã biết, SARSA là một phương pháp dựa trên chính sách, có nghĩa là nó tuân theo chiến lược thăm dò chính sách.

### 00:01:36.000 - 00:01:42.000
Điều đó có nghĩa là chính sách tương tự sẽ chịu trách nhiệm khám phá môi trường và tham gia

### 00:01:43.000 - 00:01:44.000
trong quá trình học tập.

### 00:01:45.000 - 00:01:52.000
Hãy biến nó thành một chính sách tham lam của epsilon, chính sách này sẽ thực hiện một tỷ lệ phần trăm hành động ngẫu nhiên nhất định

### 00:01:54.000 - 00:02:01.000
được mô tả bằng giá trị của epsilon và thời gian còn lại, nó sẽ chọn hành động có giá trị cao nhất

### 00:02:01.000 - 00:02:02.000
giá trị ước tính.

### 00:02:03.000 - 00:02:04.000
Hãy thực thi ô này

### 00:02:06.000 - 00:02:12.000
Và nó đây rồi. Điều tiếp theo chúng ta sẽ làm, như mọi khi, là trực quan hóa bảng giá trị q.

### 00:02:13.000 - 00:02:20.000
Như chúng ta mong đợi, tất cả các mục trong bảng giá trị q đều bằng 0. Tiếp theo, hãy hình dung chính sách.

### 00:02:21.000 - 00:02:27.000
Như chúng ta đã biết khi bắt đầu quá trình học tập, tất cả các hành động đều có giá trị như nhau.

### 00:02:29.000 - 00:02:35.000
Và cuối cùng, chúng ta sẽ triển khai thuật toán, điều đầu tiên chúng ta cần làm là xác định

### 00:02:35.000 - 00:02:35.000
chức năng.

### 00:02:42.000 - 00:02:45.000
Và hàm này sẽ lấy làm đầu vào là bảng giá trị q,

### 00:02:48.000 - 00:02:48.000
chính sách,

### 00:02:50.000 - 00:02:57.000
số tập (số lần chúng tôi muốn chạy vòng lặp chính) và bốn tham số

### 00:02:57.000 - 00:03:05.000
mà chúng tôi có thể tinh chỉnh để tối ưu hóa quá trình học tập. Đầu tiên, như mọi khi, là alpha, quá trình học tập

### 00:03:05.000 - 00:03:05.000
tỷ lệ.

### 00:03:06.000 - 00:03:11.000
Yếu tố thứ hai là gamma, hệ số chiết khấu cho các phần thưởng và giá trị trong tương lai.

### 00:03:18.000 - 00:03:26.000
Cái thứ ba là epsilon, xác định tần suất chính sách chọn các hành động ngẫu nhiên.

### 00:03:28.000 - 00:03:38.000
Và bước cuối cùng là 'n', số bước trước khi chúng ta thay thế phần thưởng còn lại bằng giá trị q

### 00:03:38.000 - 00:03:38.000
ước lượng.

### 00:03:42.000 - 00:03:43.000
Hãy tạo một số phòng.

### 00:03:47.000 - 00:03:53.000
Và bây giờ chúng ta đã sẵn sàng triển khai thuật toán, hãy vào vòng lặp chính và viết: cho tập.

### 00:03:56.000 - 00:04:01.000
Trong phạm vi từ một đến tập cộng một.

### 00:04:04.000 - 00:04:10.000
Và trong mỗi tập này, chúng ta sẽ bắt đầu nhiệm vụ và quan sát trạng thái ban đầu.

### 00:04:13.000 - 00:04:19.000
Sau đó, điều chúng ta sẽ làm là chọn một hành động áp dụng chính sách cho trạng thái ban đầu đó.

### 00:04:21.000 - 00:04:27.000
Hãy viết: hành động tương đương với tác động của việc kêu gọi chính sách đối với nhà nước.

### 00:04:28.000 - 00:04:30.000
Đó là trạng thái ban đầu.

### 00:04:33.000 - 00:04:37.000
Và vượt qua lập luận của anh ta về xác suất chọn một hành động ngẫu nhiên.

### 00:04:42.000 - 00:04:50.000
Sau đó, chúng tôi tạo một danh sách gọi là chuyển đổi, nơi chúng tôi sẽ lưu trữ các chuyển đổi trạng thái mà chúng tôi sẽ sử dụng để cập nhật

### 00:04:51.000 - 00:04:52.000
các giá trị q.

### 00:04:56.000 - 00:04:58.000
Hãy khởi tạo nó như một danh sách trống.

### 00:05:01.000 - 00:05:03.000
Tiếp theo, chúng ta sẽ khởi tạo một biến có tên là done

### 00:05:05.000 - 00:05:06.000
và đặt nó thành sai.

### 00:05:07.000 - 00:05:15.000
Và ngay bên dưới, hãy tạo một biến khác gọi là 't' sẽ cho chúng ta biết thời điểm đang trải qua

### 00:05:15.000 - 00:05:16.000
bên trong tập phim.

### 00:05:19.000 - 00:05:21.000
Và bây giờ chúng ta đã sẵn sàng bước vào vòng lặp bên trong.

### 00:05:24.000 - 00:05:30.000
Hãy viết trong khi 't-n' nhỏ hơn số lần chuyển đổi.

### 00:05:37.000 - 00:05:43.000
Điều này đảm bảo rằng vòng lặp sẽ lặp lại t+n-1 lần.

### 00:05:46.000 - 00:05:53.000
Và bên trong vòng lặp này, chúng ta sẽ thực hiện những điều sau: một mặt, nếu nhiệm vụ không được hoàn thành, chúng ta sẽ

### 00:05:53.000 - 00:05:55.000
thực hiện một hành động trong môi trường

### 00:06:03.000 - 00:06:04.000
Và mặt khác.

### 00:06:07.000 - 00:06:15.000
Nếu chúng tôi đã thu thập đủ bản dịch để tính toán lợi nhuận ước tính thì chúng tôi sẽ thực hiện cập nhật

### 00:06:15.000 - 00:06:16.000
trên bảng giá trị q.

### 00:06:22.000 - 00:06:31.000
Hãy đi từng bước một. Hãy thực hiện một hành động trong khi nhiệm vụ chưa được thực hiện. Hãy viết nếu chưa xong.

### 00:06:33.000 - 00:06:35.000
Và nếu nhiệm vụ không được thực hiện.

### 00:06:37.000 - 00:06:41.000
Chúng ta sẽ thực hiện một bước trong môi trường bằng cách thực hiện hành động mà chúng ta đã chọn trước đó.

### 00:06:44.000 - 00:06:47.000
Và phương pháp này sẽ cho chúng ta trạng thái sau,

### 00:06:48.000 - 00:06:52.000
phần thưởng tiếp theo, giá trị tiếp theo cho việc hoàn thành

### 00:06:55.000 - 00:06:59.000
và từ điển thông tin trống rỗng mà chúng ta sẽ không sử dụng.

### 00:07:01.000 - 00:07:08.000
Khi có trạng thái tiếp theo, chúng tôi sẽ gọi chính sách ở trạng thái tiếp theo đó và chuyển epsilon làm đối số cho

### 00:07:08.000 - 00:07:11.000
nhận được hành động mới sẽ được thực hiện trong trạng thái mới.

### 00:07:19.000 - 00:07:22.000
Tiếp theo, chúng tôi sẽ cập nhật danh sách chuyển tiếp.

### 00:07:25.000 - 00:07:26.000
Với những giá trị mà chúng ta vừa quan sát được.

### 00:07:28.000 - 00:07:35.000
Trạng thái mà chúng ta thực hiện hành động ở trạng thái đó và phần thưởng nhận được sau khi thực hiện hành động đó

### 00:07:35.000 - 00:07:35.000
hoạt động.

### 00:07:47.000 - 00:07:53.000
Và điều tiếp theo chúng ta sẽ làm là cập nhật bảng giá trị q và để làm được điều đó, chúng ta cần phải quan sát

### 00:07:55.000 - 00:07:57.000
Ít nhất 'n' chuyển tiếp

### 00:07:59.000 - 00:08:03.000
để chúng ta có thể tính toán ước tính lợi nhuận theo 'n' bước.

### 00:08:08.000 - 00:08:15.000
Bây giờ, hãy tính lợi nhuận ước tính, như bạn đã biết, là sự kết hợp của chữ 'n' đầu tiên

### 00:08:15.000 - 00:08:21.000
phần thưởng được giảm giá, cộng với giá trị của trạng thái và hành động được thực hiện trong tương lai.

### 00:08:22.000 - 00:08:26.000
Chúng ta hãy đưa ra một nhận xét nhỏ để ghi nhớ những gì chúng ta đang tính toán.

### 00:08:27.000 - 00:08:37.000
Hãy viết (mã bình luận)

### 00:08:43.000 - 00:08:43.000
Vân vân.

### 00:08:48.000 - 00:08:55.000
Cho đến số hạng cuối cùng, tức là gamma lũy thừa thứ n, giá trị của trạng thái 'n' bước vào

### 00:08:55.000 - 00:08:59.000
tương lai và hành động thực hiện 'n' bước vào tương lai.

### 00:09:05.000 - 00:09:12.000
Bây giờ, hãy tạo một vòng lặp sẽ thêm từng số hạng này và nó sẽ áp dụng hệ số chiết khấu cho

### 00:09:12.000 - 00:09:12.000
họ.

### 00:09:13.000 - 00:09:20.000
Hãy khởi tạo ước tính trả về dưới dạng giá trị q cho trạng thái tiếp theo và hành động tiếp theo.

### 00:09:30.000 - 00:09:34.000
Và bây giờ chúng ta sẽ đi vào vòng lặp ngược lại. Hãy viết:

### 00:09:36.000 - 00:09:39.000
Đối với trạng thái_t, hành động_t và phần thưởng_t

### 00:09:41.000 - 00:09:46.000
Trong quá trình chuyển tiếp từ 'n' bước vào quá khứ cho đến bây giờ.

### 00:09:52.000 - 00:09:55.000
Dấu hai chấm này có nghĩa là cho đến hết danh sách.

### 00:09:58.000 - 00:10:02.000
Nghĩa là, chúng ta sẽ lặp lại chuyển tiếp 'n' cuối cùng.

### 00:10:05.000 - 00:10:07.000
Và chúng ta sẽ làm điều đó theo thứ tự ngược lại.

### 00:10:10.000 - 00:10:19.000
Và đối với mỗi lần lặp này, chúng tôi sẽ cập nhật giá trị của ước tính lợi nhuận dưới dạng lợi nhuận tại thời điểm 't'

### 00:10:20.000 - 00:10:24.000
cộng gamma nhân với giá trị hiện tại của ước tính.

### 00:10:26.000 - 00:10:33.000
Sau tất cả các lần lặp, điều này sẽ tính toán chính xác công thức trả về n bước mà chúng ta

### 00:10:33.000 - 00:10:34.000
được mô tả.

### 00:10:37.000 - 00:10:43.000
Chúng tôi sẽ bắt đầu gán các ước tính giá trị q này cho lợi nhuận và tại mỗi thời điểm, chúng tôi sẽ

### 00:10:43.000 - 00:10:45.000
sẽ cập nhật nó bằng cách nhân nó với gamma.

### 00:10:46.000 - 00:10:53.000
Phần thưởng tiếp theo, là phần thưởng đầu tiên mà chúng tôi đưa vào ước tính, sẽ được nhân với gamma

### 00:10:53.000 - 00:11:00.000
đến lũy thừa n-1, v.v. cho đến phần thưởng đầu tiên.

### 00:11:00.000 - 00:11:02.000
Điều đó sẽ không được Gamma giảm giá.

### 00:11:03.000 - 00:11:07.000
Đây là một thủ thuật đơn giản mà chúng tôi sử dụng để tính toán một cách hiệu quả.

### 00:11:07.000 - 00:11:10.000
Lợi nhuận ước tính theo 'n' bước.

### 00:11:11.000 - 00:11:14.000
Và cuối cùng, chúng ta sẽ áp dụng quy tắc cập nhật.

### 00:11:18.000 - 00:11:20.000
Hãy viết: giá trị hành động.

### 00:11:22.000 - 00:11:25.000
Về trạng thái tại thời điểm 't' và hành động tại thời điểm 't'.

### 00:11:28.000 - 00:11:34.000
Bởi vì sau khi thực hiện vòng lặp, chúng sẽ là trạng thái và hành động 'n' bước về quá khứ.

### 00:11:36.000 - 00:11:39.000
Đó là thời điểm mà chúng tôi sẽ cập nhật.

### 00:11:43.000 - 00:11:51.000
Vâng, với giá trị này, chúng ta sẽ cộng alpha lần chênh lệch giữa ước tính n bước

### 00:11:51.000 - 00:11:54.000
của lợi nhuận và ước tính hiện tại.

### 00:12:07.000 - 00:12:10.000
Và bây giờ việc cập nhật bảng giá trị q của chúng ta đã hoàn tất.

### 00:12:11.000 - 00:12:16.000
Điều tiếp theo chúng ta sẽ làm là cập nhật giá trị của 't' và tăng nó lên một.

### 00:12:17.000 - 00:12:21.000
Để cho thuật toán biết rằng chúng tôi đã chuyển sang thời điểm tiếp theo.

### 00:12:24.000 - 00:12:28.000
Và rõ ràng là gán trạng thái mới cho biến trạng thái

### 00:12:30.000 - 00:12:37.000
Và hành động mới được biến thành hành động. Bằng cách đó, lần tiếp theo khi thực hiện vòng lặp, chúng tôi sẽ cập nhật

### 00:12:38.000 - 00:12:40.000
Những trạng thái và hành động tiếp theo.

### 00:12:44.000 - 00:12:46.000
Và với điều đó, thuật toán của chúng tôi đã sẵn sàng.

### 00:12:47.000 - 00:12:53.000
Tất cả những gì còn lại là thực hiện một chút sửa đổi mà chúng ta sẽ áp dụng cho lợi nhuận ước tính.

### 00:12:55.000 - 00:13:01.000
Hãy tưởng tượng điều gì sẽ xảy ra vào giây phút cuối cùng của tập phim, chúng ta thực hiện hành động và nhận được thiết bị đầu cuối

### 00:13:01.000 - 00:13:09.000
trạng thái của nhiệm vụ, đó là trạng thái khi nhiệm vụ kết thúc và biến done trở thành True.

### 00:13:13.000 - 00:13:20.000
Trong trường hợp đó, khi chúng tôi ước tính giá trị của trạng thái mà chúng tôi đã đạt đến, chúng tôi sẽ ước tính giá trị q

### 00:13:20.000 - 00:13:26.000
của mục tiêu, như bạn biết, là 0. Khi đạt được mục tiêu, chúng tôi không mong đợi đạt được bất kỳ

### 00:13:26.000 - 00:13:27.000
phần thưởng thêm.

### 00:13:28.000 - 00:13:31.000
Nhưng làm thế nào chúng ta có thể phản ánh điều đó trong ước tính lợi nhuận của mình?

### 00:13:31.000 - 00:13:34.000
Chúng ta sẽ làm điều đó bằng một thủ thuật rất đơn giản.

### 00:13:35.000 - 00:13:39.000
Sẽ mở dấu ngoặc đơn và viết

### 00:13:39.000 - 00:13:45.000
(1-done) và giá trị này chúng ta sẽ nhân nó với ước tính của giá trị q.

### 00:13:47.000 - 00:13:49.000
Nhưng chính xác thì chúng ta đang làm gì?

### 00:13:50.000 - 00:13:56.000
Chà, rất đơn giản, điều chúng tôi đang nói là nếu điều đó đúng, hãy nhớ rằng giá trị số của

### 00:13:56.000 - 00:14:02.000
true là 1, nếu thực hiện đúng thì ta sẽ nhân 1-1

### 00:14:02.000 - 00:14:09.000
nghĩa là, 0 lần ước tính lợi nhuận và điều đó sẽ tạo ra ước tính 0.

### 00:14:10.000 - 00:14:11.000
Và nếu thực hiện, là Sai.

### 00:14:13.000 - 00:14:21.000
Hãy nhớ rằng giá trị số của Sai là 0 thì sẽ nhân với 1-0.

### 00:14:21.000 - 00:14:26.000
Đó là 1 theo ước tính, sẽ không thay đổi.

### 00:14:27.000 - 00:14:35.000
Vì vậy, những gì chúng tôi đang làm với thủ thuật này là loại bỏ các bước ước tính giá trị q 'n' trong tương lai

### 00:14:35.000 - 00:14:43.000
nếu đến thời điểm đó nhiệm vụ đã kết thúc và nó sẽ không được sửa đổi theo cách khác. Bằng cách đó, chúng ta sẽ đạt được chính xác

### 00:14:43.000 - 00:14:44.000
những gì chúng tôi muốn làm.

### 00:14:45.000 - 00:14:49.000
Hãy chạy ô này và bây giờ thuật toán của chúng tôi có sẵn cho chúng tôi.

### 00:14:49.000 - 00:14:52.000
Hãy gọi nó bằng cách gõ n_step_sarsa()

### 00:14:54.000 - 00:14:59.000
Và chuyển cho nó bảng giá trị q, chính sách và một nghìn tập.

### 00:15:04.000 - 00:15:05.000
Hãy thực thi ô.

### 00:15:07.000 - 00:15:10.000
Và chúng tôi sẽ hiển thị các giá trị ước tính.

### 00:15:15.000 - 00:15:22.000
Họ đây rồi. Đúng như chúng ta mong đợi, trên con đường tối ưu, những hành động đưa chúng ta đến mục tiêu đều có

### 00:15:22.000 - 00:15:23.000
giá trị tối đa.

### 00:15:26.000 - 00:15:28.000
Và đây là chính sách mà chúng tôi đã có được.

### 00:15:31.000 - 00:15:38.000
Các hành động được chính sách quy định ở các trạng thái bên trong đường dẫn tối ưu thực sự là những hành động tối ưu.

### 00:15:38.000 - 00:15:44.000
Và trường hợp đó cũng xảy ra ở một số ô không nằm trên đường đi tối ưu, mặc dù ở những ô khác

### 00:15:44.000 - 00:15:48.000
chính sách chưa có cơ hội khám phá chúng một cách sâu sắc.

### 00:15:49.000 - 00:15:54.000
Nó chưa đầu tư đủ thời gian để xác định các hành động tối ưu ở những trạng thái đó.

### 00:15:55.000 - 00:15:59.000
Hãy đảm bảo rằng chính sách mà chúng tôi thu được có khả năng tìm ra lối thoát.

### 00:16:02.000 - 00:16:03.000
Vâng, có vẻ như vậy.

