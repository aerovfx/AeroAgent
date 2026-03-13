## Nội dung

### 00:00:02.000 - 00:00:08.000
Bây giờ chúng ta đã có cả chính sách và bảng giá trị q, chúng ta có thể bắt đầu triển khai thuật toán.

### 00:00:10.000 - 00:00:13.000
Điều đầu tiên chúng ta sẽ làm là tạo một hàm.

### 00:00:15.000 - 00:00:18.000
được gọi là ngoài chính sách, kiểm soát Montecarlo.

### 00:00:23.000 - 00:00:23.000
Hãy tạo một số phòng.

### 00:00:29.000 - 00:00:33.000
Và chúng ta sẽ chuyển nó làm đối số cho bảng giá trị q,

### 00:00:35.000 - 00:00:37.000
Chính sách mục tiêu

### 00:00:41.000 - 00:00:42.000
Chính sách thăm dò

### 00:00:47.000 - 00:00:49.000
Và một số tập nhất định.

### 00:00:53.000 - 00:00:59.000
Chúng tôi cũng sẽ cung cấp cho nó hai giá trị: một cho gamma, là hệ số chiết khấu để tính lợi nhuận

### 00:01:01.000 - 00:01:08.000
và một giá trị khác cho epsilon, đó là xác suất mà chính sách khám phá chọn một hành động ngẫu nhiên.

### 00:01:09.000 - 00:01:12.000
Hãy đặt epsilon thành 0,2.

### 00:01:13.000 - 00:01:20.000
Được rồi. Bây giờ, bên trong hàm, điều đầu tiên chúng ta sẽ làm là tạo một bảng trong đó

### 00:01:20.000 - 00:01:25.000
chúng tôi sẽ lưu trữ tổng các tỷ lệ lấy mẫu quan trọng.

### 00:01:25.000 - 00:01:29.000
Hãy gọi bảng này là 'csa' và tạo nó

### 00:01:29.000 - 00:01:37.000
sử dụng hàm np.zeros(). Hình dạng của bảng sẽ là 5x5x4

### 00:01:41.000 - 00:01:48.000
một mục nhập cho mỗi tổ hợp trạng thái đang hoạt động và khi có bảng, chúng ta có thể nhập mục chính

### 00:01:48.000 - 00:01:49.000
vòng lặp.

### 00:01:52.000 - 00:01:55.000
Vòng lặp này sẽ lặp lại qua một số tập.

### 00:01:59.000 - 00:02:04.000
Từ một cho đến số mà chúng ta đã cho nó cộng một.

### 00:02:08.000 - 00:02:17.000
Và điều đầu tiên chúng ta cần làm là khởi tạo giá trị trả về là 0 và chúng ta cũng sẽ

### 00:02:17.000 - 00:02:26.000
khởi tạo giá trị cho tỷ lệ lấy mẫu quan trọng là 1. Sau đó, chúng tôi sẽ khởi tạo tác vụ cho việc này

### 00:02:26.000 - 00:02:26.000
tập.

### 00:02:31.000 - 00:02:33.000
Chúng tôi sẽ gọi phương thức đặt lại trên môi trường.

### 00:02:36.000 - 00:02:39.000
Và chúng ta sẽ bắt đầu quan sát ban đầu về trạng thái.

### 00:02:42.000 - 00:02:50.000
Chúng tôi sẽ khai báo một biến khác gọi là 'xong' sẽ cho chúng tôi biết tập phim đã kết thúc hay chưa và rõ ràng là

### 00:02:50.000 - 00:02:59.000
chúng tôi sẽ khởi tạo nó là 'Sai' và sau đó chúng tôi sẽ tạo một danh sách có tên là chuyển tiếp, nơi chúng tôi sẽ lưu trữ

### 00:02:59.000 - 00:03:06.000
quỹ đạo mà chúng tôi sẽ tạo trong tập phim tại mỗi thời điểm chúng tôi sẽ lưu trữ trạng thái hiện tại,

### 00:03:06.000 - 00:03:11.000
hành động được thực hiện ở trạng thái đó và phần thưởng nhận được sau khi thực hiện hành động đó.

### 00:03:12.000 - 00:03:14.000
Hãy khởi tạo biến này dưới dạng danh sách trống.

### 00:03:15.000 - 00:03:19.000
Tiếp theo, chúng tôi sẽ sử dụng chính sách khám phá để đối mặt với môi trường.

### 00:03:21.000 - 00:03:22.000
Và tạo ra trải nghiệm.

### 00:03:26.000 - 00:03:32.000
Và để làm được điều đó, chúng ta sẽ nhập một vòng lặp bên trong sẽ lặp lại cho đến khi nhiệm vụ hoàn thành.

### 00:03:34.000 - 00:03:41.000
Bên trong vòng lặp bên trong đó vào mọi thời điểm, chúng tôi sẽ chọn một hành động dựa trên chính sách khám phá

### 00:03:47.000 - 00:03:54.000
và chúng tôi sẽ cung cấp cho nó trạng thái hiện tại cũng như giá trị của epsilon mà chúng tôi đã khai báo trong thuật toán.

### 00:03:59.000 - 00:04:04.000
Tiếp theo, chúng ta sẽ thực thi hành động đó trong môi trường và quan sát trạng thái tiếp theo,

### 00:04:07.000 - 00:04:11.000
phần thưởng mà chúng tôi nhận được, giá trị tiếp theo cho biến done

### 00:04:14.000 - 00:04:22.000
và một từ điển thông tin bổ sung mà chúng tôi sẽ không sử dụng lần này và tất cả những thứ này sẽ nhận được

### 00:04:22.000 - 00:04:29.000
nó bằng cách thực thi phương thức bước trên môi trường và chuyển hành động mà chúng ta đã chọn.

### 00:04:35.000 - 00:04:38.000
Sau đó, vào danh sách chuyển tiếp, chúng ta sẽ dành một mục mới.

### 00:04:41.000 - 00:04:49.000
Đó sẽ là danh sách với trạng thái mà chúng tôi đã truy cập, hành động mà chúng tôi đã thực hiện và phần thưởng mà chúng tôi

### 00:04:49.000 - 00:04:49.000
thu được.

### 00:04:51.000 - 00:04:55.000
Và cuối cùng, chúng tôi sẽ cập nhật giá trị của trạng thái.

### 00:04:59.000 - 00:05:04.000
Vì vậy, trong lần lặp tiếp theo của vòng lặp, trạng thái sẽ là trạng thái hiện tại là trạng thái mới.

### 00:05:07.000 - 00:05:12.000
Vòng lặp này sẽ lặp lại cho đến khi tập phim kết thúc và khi đó chúng ta sẽ có danh sách

### 00:05:15.000 - 00:05:20.000
được gọi là các chuyển đổi sẽ chứa trải nghiệm mà chúng tôi quan sát được ở mỗi trạng thái.

### 00:05:23.000 - 00:05:29.000
Sau khi chúng ta đã khám phá môi trường, giờ là lúc chúng ta học hỏi kinh nghiệm mà chúng ta đã thu thập được.

### 00:05:31.000 - 00:05:37.000
Vì vậy, những gì chúng tôi làm là đến thăm từng tiểu bang theo thứ tự ngược lại. Tức là đầu tiên sẽ ghé thăm trạng thái cuối cùng

### 00:05:38.000 - 00:05:44.000
trước khi nhiệm vụ kết thúc, rồi nhiệm vụ trước đó, v.v., cho đến khi bắt đầu tập phim.

### 00:05:45.000 - 00:05:49.000
Và tại mỗi thời điểm đó, chúng tôi sẽ tính toán lợi nhuận.

### 00:05:51.000 - 00:05:52.000
Chúng ta sẽ vào một vòng lặp khác

### 00:05:54.000 - 00:05:56.000
Đối với trạng thái tại thời điểm 't'

### 00:05:58.000 - 00:05:59.000
Hành động tại thời điểm 't'.

### 00:06:02.000 - 00:06:03.000
Và phần thưởng tại thời điểm 't'.

### 00:06:08.000 - 00:06:14.000
Hãy nhớ rằng 't' đề cập đến thời điểm và nó sẽ thay đổi trong suốt quá trình thực hiện vòng lặp

### 00:06:14.000 - 00:06:22.000
và chúng ta sẽ nhận được những giá trị này bằng cách lặp lại danh sách chuyển đổi theo thứ tự ngược lại và bên trong vòng lặp sẽ

### 00:06:22.000 - 00:06:26.000
tuyên bố sự trở lại là phần thưởng nhận được tại thời điểm đó.

### 00:06:27.000 - 00:06:35.000
Cộng với lợi nhuận đang chạy được lưu trữ trong biến G được chiết khấu bởi gamma.

### 00:06:39.000 - 00:06:41.000
Chúng ta sẽ tính nó theo công thức này.

### 00:06:44.000 - 00:06:51.000
Điều tiếp theo chúng ta cần làm là cập nhật bảng các tỷ lệ lấy mẫu quan trọng để nó

### 00:06:51.000 - 00:06:58.000
có giá trị đúng. Khi chúng tôi sử dụng nó trong quy tắc cập nhật sẽ cập nhật nó, thêm mẫu quan trọng

### 00:06:58.000 - 00:07:05.000
tỷ lệ mà chúng ta có tại thời điểm đó với mục nhập của bảng cho trạng thái và hành động đó.

### 00:07:09.000 - 00:07:13.000
Vì điều đó sẽ lập chỉ mục cho bảng csa chuyển trạng thái 't'

### 00:07:14.000 - 00:07:21.000
và hành động 't' dưới dạng chỉ mục và điều đó sẽ lập chỉ mục cho bảng để tìm mục nhập phù hợp và

### 00:07:21.000 - 00:07:26.000
với giá trị đó sẽ thêm giá trị của W mà chúng ta có ngay bây giờ.

### 00:07:27.000 - 00:07:30.000
Điều tiếp theo chúng ta phải làm là cập nhật giá trị q.

### 00:07:31.000 - 00:07:37.000
Đó là bước đánh giá chính sách từ sơ đồ Lặp lại chính sách tổng quát (GPI).

### 00:07:37.000 - 00:07:44.000
Như bạn đã biết, ước tính mới sẽ là mức trung bình có trọng số của lợi nhuận mà chúng tôi quan sát được.

### 00:07:47.000 - 00:07:52.000
Vì vậy, điều chúng ta sẽ làm là lưu trữ trong một biến riêng biệt, giá trị cũ của giá trị q đó

### 00:07:55.000 - 00:08:00.000
và bây giờ chúng tôi có một bản sao lưu của giá trị q cũ để đề phòng.

### 00:08:06.000 - 00:08:08.000
Sau đó theo công thức.

### 00:08:19.000 - 00:08:22.000
Với ước tính giá trị q mà chúng ta có tại thời điểm đó

### 00:08:23.000 - 00:08:27.000
chúng ta sẽ cộng tỉ số giữa W và C.

### 00:08:39.000 - 00:08:43.000
nhân với chênh lệch giữa lợi nhuận mà chúng ta vừa thu được

### 00:08:45.000 - 00:08:46.000
và giá trị q cũ.

### 00:08:52.000 - 00:08:55.000
Và với quy tắc cập nhật này, chúng tôi sẽ cập nhật giá trị q.

### 00:08:58.000 - 00:09:05.000
Bây giờ chúng ta cần biết liệu hành động được chọn trong chính sách khám phá có giống với chính sách mục tiêu hay không

### 00:09:05.000 - 00:09:07.000
sẽ được chọn sau khi được cập nhật.

### 00:09:11.000 - 00:09:16.000
Nếu không, chúng ta sẽ phá vỡ vòng lặp và chuyển sang tập tiếp theo.

### 00:09:21.000 - 00:09:25.000
Hãy để chúng tôi kiểm tra xem hành động có khác với mục tiêu hay không.

### 00:09:32.000 - 00:09:34.000
Sau đó chúng ta sử dụng từ khóa 'break'.

### 00:09:42.000 - 00:09:45.000
Điều đó sẽ đưa chúng ta đến lần lặp tiếp theo của vòng lặp.

### 00:09:45.000 - 00:09:54.000
Bây giờ, điều cuối cùng chúng ta phải làm trong trường hợp hành động tối ưu không thay đổi là cập nhật tầm quan trọng

### 00:09:54.000 - 00:09:56.000
tỷ lệ lấy mẫu theo cách bạn thấy ở đây.

### 00:10:00.000 - 00:10:11.000
Chúng ta sẽ đặt W bằng giá trị của W nhân một trên xác suất mà chính sách giải thích phải

### 00:10:11.000 - 00:10:12.000
chọn hành động.

### 00:10:19.000 - 00:10:26.000
Và xác suất để chính sách thăm dò thực hiện hành động đó là bao nhiêu, một trừ epsilon

### 00:10:31.000 - 00:10:33.000
cộng, epsilon chia cho 4.

### 00:10:38.000 - 00:10:39.000
Nhưng chính xác thì tại sao?

### 00:10:40.000 - 00:10:47.000
Vâng, hãy chú ý đến thực tế rằng hành động được thực hiện bởi chính sách thăm dò cũng giống như hành động mà

### 00:10:47.000 - 00:10:53.000
chính sách mục tiêu lẽ ra đã chọn, nghĩa là chính sách đó đã thực hiện hành động có giá trị q cao nhất. Và cái gì

### 00:10:53.000 - 00:10:59.000
xác suất thực hiện hành động có giá trị cao nhất bằng cách sử dụng chính sách khám phá,

### 00:10:59.000 - 00:10:59.000
Ý tôi là.

### 00:11:00.000 - 00:11:07.000
Chà, chúng ta biết rằng với xác suất epsilon, nó chọn một hành động ngẫu nhiên và xác suất chọn

### 00:11:07.000 - 00:11:13.000
hành động này ngẫu nhiên được chia cho epsilon cho bốn hành động có sẵn.

### 00:11:14.000 - 00:11:20.000
Nhưng bên cạnh đó, trong trường hợp nó không thực hiện một hành động ngẫu nhiên nào thì nó sẽ chọn hành động có giá trị cao nhất.

### 00:11:20.000 - 00:11:25.000
giá trị q, và nó thực hiện điều đó với xác suất một trừ epsilon.

### 00:11:26.000 - 00:11:26.000
Rất tốt.

### 00:11:27.000 - 00:11:29.000
Bây giờ chúng tôi có thuật toán của chúng tôi.

### 00:11:29.000 - 00:11:32.000
Điều tiếp theo chúng ta sẽ làm là kiểm tra nó.

### 00:11:32.000 - 00:11:36.000
Chúng tôi sẽ gọi nó bằng cách loại bỏ chính sách.

### 00:11:36.000 - 00:11:37.000
Kiểm soát Montecarlo.

### 00:11:38.000 - 00:11:41.000
Nhân tiện, chúng ta phải thực thi ô này. Xong.

### 00:11:42.000 - 00:11:49.000
Và bây giờ chúng ta sẽ gọi thuật toán với bảng giá trị, chính sách đích và khám phá

### 00:11:49.000 - 00:11:50.000
chính sách.

### 00:11:58.000 - 00:12:01.000
Và chúng tôi muốn chạy nó trong một nghìn tập.

### 00:12:09.000 - 00:12:13.000
Và giá trị của epsilon mà chúng ta sắp cho nó là 0,3,

### 00:12:16.000 - 00:12:16.000
Ví dụ.

### 00:12:18.000 - 00:12:20.000
Hãy thực hiện thuật toán.

### 00:12:23.000 - 00:12:24.000
Xong.

### 00:12:28.000 - 00:12:31.000
Trong video tiếp theo, chúng tôi sẽ phân tích kết quả mà chúng tôi thu được.

