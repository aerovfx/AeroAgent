## Nội dung

### 00:00:00.000 - 00:00:06.000
Trong video này, chúng ta sẽ triển khai phương pháp thứ hai mà chúng ta sẽ sử dụng để làm việc với các trạng thái liên tục.

### 00:00:08.000 - 00:00:11.000
Phương pháp này được gọi là mã hóa ô.

### 00:00:12.000 - 00:00:18.000
Và đó chỉ là sự khái quát hóa của kỹ thuật tổng hợp trạng thái mà chúng ta đã thấy trong video trước.

### 00:00:19.000 - 00:00:27.000
Trong thực tế, mã hóa khối ảnh bao gồm việc tạo ra một số tập hợp trạng thái độc lập nhất định để biểu diễn

### 00:00:27.000 - 00:00:28.000
các tiểu bang.

### 00:00:28.000 - 00:00:37.000
Và bằng cách lấy trung bình các ước tính giá trị q của mỗi trạng thái, việc tổng hợp thông thường sẽ thu được kết quả

### 00:00:37.000 - 00:00:41.000
chính xác hơn so với việc họ sử dụng một tập hợp trạng thái duy nhất.

### 00:00:42.000 - 00:00:48.000
Trên thực tế, nếu bạn nhìn vào hàm giá trị trạng thái tối ưu từ biểu đồ này và bạn hình dung ra giá trị trung bình là bao nhiêu.

### 00:00:48.000 - 00:00:55.000
trong số các ước tính sẽ dành cho từng trạng thái đó, như bạn có thể thấy, mức trung bình của chúng gần với

### 00:00:55.000 - 00:00:56.000
những giá trị thực tế.

### 00:00:56.000 - 00:01:01.000
Đó chính là ưu điểm lớn của phương pháp mã hóa ô xếp, nâng cao độ chính xác.

### 00:01:02.000 - 00:01:05.000
Vậy hãy cùng sử dụng và xem kết quả mà chúng ta nhận được nhé.

### 00:01:07.000 - 00:01:13.000
Như mọi khi, điều đầu tiên chúng ta sẽ làm là tạo môi trường bằng hàm make

### 00:01:14.000 - 00:01:15.000
từ thư viện phòng tập thể dục.

### 00:01:20.000 - 00:01:25.000
Trong trường hợp này, chúng ta cũng sẽ sử dụng nhiệm vụ xe leo núi.

### 00:01:29.000 - 00:01:37.000
Và như trước đây, chúng ta sẽ sử dụng chức năng xem mọi thứ để đảm bảo rằng kết quả của chúng ta có thể lặp lại được.

### 00:01:38.000 - 00:01:40.000
Và chúng tôi thực hiện ô này.

### 00:01:44.000 - 00:01:48.000
Bây giờ hãy tạo lớp sẽ bao bọc môi trường của chúng ta.

### 00:01:50.000 - 00:01:54.000
Và chúng tôi sẽ triển khai nó giống như cách chúng tôi đã làm với việc tổng hợp trạng thái.

### 00:01:54.000 - 00:01:59.000
Chúng ta sẽ tạo một lớp có tên là Tile Coding và.

### 00:02:06.000 - 00:02:09.000
Trong lớp này sẽ kế thừa từ lớp bao bọc quan sát.

### 00:02:10.000 - 00:02:12.000
Từ thư viện phòng tập thể dục.

### 00:02:15.000 - 00:02:16.000
Hãy tạo một số phòng.

### 00:02:19.000 - 00:02:22.000
Và bây giờ chúng ta cần làm ba việc.

### 00:02:22.000 - 00:02:24.000
Đầu tiên là.

### 00:02:25.000 - 00:02:27.000
Khởi tạo lớp.

### 00:02:28.000 - 00:02:33.000
Cách thứ hai là thực hiện phương pháp quan sát.

### 00:02:36.000 - 00:02:42.000
Điều đó sẽ cho phép chúng ta chuyển đổi trạng thái như trạng thái ban đầu tạo ra chúng.

### 00:02:42.000 - 00:02:47.000
Và điều cuối cùng chúng ta cần làm là tạo một hàm để tạo.

### 00:02:49.000 - 00:02:51.000
Những tấm ốp lát riêng biệt.

### 00:02:51.000 - 00:02:55.000
Đó là mỗi tập hợp trạng thái khác nhau.

### 00:02:56.000 - 00:02:59.000
Hãy bắt đầu bằng cách khởi tạo lớp.

### 00:03:02.000 - 00:03:04.000
Hãy tạo phương thức init.

### 00:03:05.000 - 00:03:07.000
Và chúng ta sẽ vượt qua nó.

### 00:03:08.000 - 00:03:11.000
Môi trường mà nó sẽ bao bọc.

### 00:03:14.000 - 00:03:16.000
Và như trước đây, chúng ta sẽ vượt qua nó.

### 00:03:16.000 - 00:03:17.000
Các thùng biến.

### 00:03:17.000 - 00:03:18.000
Biến.

### 00:03:18.000 - 00:03:19.000
Thấp.

### 00:03:19.000 - 00:03:20.000
Cao.

### 00:03:21.000 - 00:03:29.000
Và một biến khác gọi là N, biến này sẽ cho chúng ta biết chúng ta muốn tạo bao nhiêu tập hợp trạng thái.

### 00:03:30.000 - 00:03:35.000
Sau đó, theo cách tương tự như chúng ta đã làm với kỹ thuật tổng hợp trạng thái.

### 00:03:37.000 - 00:03:46.000
Chúng ta sẽ gọi phương thức init từ trình bao bọc quan sát siêu lớp và chúng ta sẽ truyền nó vào môi trường

### 00:03:46.000 - 00:03:47.000
như lý lẽ.

### 00:03:47.000 - 00:03:51.000
Và bây giờ chúng ta sẽ định nghĩa biến được gọi là tilings.

### 00:03:53.000 - 00:04:01.000
Và biến này sẽ chứa các tập hợp trạng thái khác nhau mà chúng ta sẽ xây dựng bằng cách sử dụng

### 00:04:01.000 - 00:04:02.000
tạo phương pháp ốp lát.

### 00:04:05.000 - 00:04:07.000
Điều đó chúng ta sẽ xác định bây giờ.

### 00:04:08.000 - 00:04:14.000
Đối với phương thức này, chúng ta truyền các biến mà lớp thu được trong phương thức init đó là bins.

### 00:04:16.000 - 00:04:17.000
CHÀO.

### 00:04:18.000 - 00:04:20.000
Thấp và n.

### 00:04:22.000 - 00:04:25.000
Và điều cuối cùng chúng ta sẽ làm trong phương thức init.

### 00:04:27.000 - 00:04:28.000
Đã được sửa đổi.

### 00:04:29.000 - 00:04:30.000
Không gian trạng thái.

### 00:04:34.000 - 00:04:40.000
Chúng tôi sẽ viết không gian tập thể dục và chúng tôi sẽ tạo ra một không gian trạng thái.

### 00:04:41.000 - 00:04:43.000
Thuộc lớp đa rời rạc.

### 00:04:46.000 - 00:04:47.000
Chúng tôi chuyển cho nó một biến.

### 00:04:49.000 - 00:04:51.000
Thùng để liệt kê.

### 00:04:53.000 - 00:04:59.000
Và như chúng ta đã biết, Beans chứa số lượng giá trị cho từng kích thước của trạng thái.

### 00:05:01.000 - 00:05:07.000
Nhưng vì chúng ta sẽ có n tập hợp trạng thái nên chúng ta phải nhân danh sách đó lên.

### 00:05:09.000 - 00:05:11.000
Bởi một.

### 00:05:11.000 - 00:05:15.000
Vì vậy, chúng tôi lặp lại các giá trị của danh sách và thời gian đó.

### 00:05:17.000 - 00:05:25.000
Và bây giờ không gian trạng thái này sẽ phản ánh số chiều của trạng thái với n tập hợp trạng thái.

### 00:05:28.000 - 00:05:29.000
Và thì đấy.

### 00:05:31.000 - 00:05:36.000
Điều tiếp theo chúng ta phải làm là tạo hàm tạo ra các ô xếp.

### 00:05:37.000 - 00:05:41.000
Hãy viết Dev, tạo ốp lát.

### 00:05:42.000 - 00:05:50.000
Như chúng ta biết sẽ lấy biến thùng, cao, thấp và n làm đối số.

### 00:05:53.000 - 00:05:54.000
Và nó sẽ trở lại.

### 00:05:55.000 - 00:05:57.000
Tổng hợp của nhà nước.

### 00:05:58.000 - 00:06:03.000
Những tập hợp này, chúng ta sẽ lưu trữ chúng trong một biến gọi là tilings.

### 00:06:04.000 - 00:06:07.000
Rằng chúng ta sẽ khởi tạo như một danh sách trống.

### 00:06:08.000 - 00:06:10.000
Và bây giờ chúng ta sẽ lặp lại.

### 00:06:13.000 - 00:06:18.000
Giá trị Ober bắt đầu từ một và kết thúc ở n cộng một.

### 00:06:18.000 - 00:06:21.000
Để tạo ra từng ô riêng lẻ.

### 00:06:22.000 - 00:06:26.000
Bây giờ tất cả các tập hợp trạng thái phải khác nhau.

### 00:06:27.000 - 00:06:31.000
Và để làm điều đó, chúng ta sẽ áp dụng ba phép biến đổi cho mỗi phép biến đổi.

### 00:06:32.000 - 00:06:37.000
Điều đầu tiên chúng ta sẽ làm là di chuyển các giá trị tối thiểu của các trạng thái tổng hợp đó.

### 00:06:37.000 - 00:06:45.000
Chúng tôi cũng sẽ di chuyển giá trị cao nhất cho các trạng thái này và chúng tôi cũng sẽ thay đổi kích thước của các trạng thái tổng hợp đó

### 00:06:45.000 - 00:06:45.000
tiểu bang.

### 00:06:47.000 - 00:06:54.000
Như bạn có thể thấy trong ô màu vàng, mỗi trạng thái có kích thước lớn hơn các trạng thái trong tập hợp màu xanh lá cây.

### 00:06:56.000 - 00:06:59.000
Vì vậy những gì chúng ta sắp làm là dành cho từng người trong số họ.

### 00:07:00.000 - 00:07:04.000
Chúng ta sẽ viết một biến gọi là low.

### 00:07:06.000 - 00:07:09.000
Đó là giá trị tối thiểu của tập hợp.

### 00:07:11.000 - 00:07:17.000
Và chúng ta sẽ làm cho nó bằng điểm ngẫu nhiên trừ điểm thấp ngẫu nhiên.

### 00:07:19.000 - 00:07:21.000
Lần 0 dấu phẩy hai.

### 00:07:22.000 - 00:07:23.000
Thời gian chậm lại.

### 00:07:26.000 - 00:07:28.000
Chúng ta đang làm gì ở đây?

### 00:07:28.000 - 00:07:35.000
Những gì chúng tôi đang làm là chọn điểm bắt đầu của một trong các chiều của trạng thái và chúng tôi sẽ tiến hành

### 00:07:35.000 - 00:07:38.000
để trừ đi một tỷ lệ phần trăm nhất định từ nó.

### 00:07:38.000 - 00:07:44.000
Như bạn đã biết, hàm ngẫu nhiên sẽ tạo ra một số từ 0 đến 1 nếu nó tạo ra số 0.

### 00:07:44.000 - 00:07:51.000
Việc tập hợp trạng thái này sẽ bắt đầu tại cùng điểm với kích thước ban đầu của trạng thái.

### 00:07:52.000 - 00:07:59.000
Nếu ngẫu nhiên lấy giá trị bằng 1, chúng tôi sẽ trừ 20% vào giá trị tối thiểu của thứ nguyên đó và

### 00:07:59.000 - 00:08:06.000
thứ nguyên sẽ bắt đầu ở một điểm xa hơn bên trái so với giá trị tối thiểu ban đầu cho thứ nguyên đó.

### 00:08:07.000 - 00:08:14.000
Nghĩa là, thay vì có thể bắt đầu ở âm 10, nó sẽ bắt đầu ở -11,5.

### 00:08:15.000 - 00:08:21.000
Bằng cách đó, chúng ta sẽ di chuyển tập hợp trạng thái theo chiều ngang và bây giờ chúng ta sẽ làm tương tự với

### 00:08:21.000 - 00:08:22.000
những giá trị tối đa.

### 00:08:23.000 - 00:08:24.000
Hãy viết.

### 00:08:24.000 - 00:08:25.000
CHÀO.

### 00:08:27.000 - 00:08:30.000
Dấu chấm ngẫu nhiên ngẫu nhiên.

### 00:08:31.000 - 00:08:33.000
Lần 0,2.

### 00:08:35.000 - 00:08:39.000
Và 0,2 này, chúng tôi chọn nó vì chúng tôi muốn di chuyển.

### 00:08:41.000 - 00:08:42.000
Giá trị cao nhất.

### 00:08:43.000 - 00:08:45.000
Chỉ bằng một phần nhỏ.

### 00:08:45.000 - 00:08:47.000
Đó là 20%.

### 00:08:48.000 - 00:08:54.000
Và bây giờ điều chúng ta sẽ làm là chọn giá trị tối thiểu và tối đa đó rồi chia cho số

### 00:08:54.000 - 00:08:57.000
những giá trị mà chúng ta muốn thứ nguyên đó có.

### 00:09:00.000 - 00:09:03.000
Và sau đó chúng ta sẽ nhận được kích thước của các phân đoạn.

### 00:09:07.000 - 00:09:10.000
Hãy viết cao, trừ thấp.

### 00:09:13.000 - 00:09:15.000
Chia theo thùng.

### 00:09:16.000 - 00:09:21.000
Và bây giờ chúng ta biết các khoảng mà chúng ta nhóm lại phải lớn đến mức nào.

### 00:09:25.000 - 00:09:28.000
Và bây giờ chúng ta đã kéo dài tập hợp trạng thái theo chiều ngang.

### 00:09:30.000 - 00:09:33.000
Chúng ta sẽ di chuyển nó sang bên này hay bên kia.

### 00:09:35.000 - 00:09:37.000
Đối với mỗi kích thước của nhà nước.

### 00:09:40.000 - 00:09:43.000
Và chúng ta sẽ làm điều đó bằng cách sử dụng vectơ dịch chuyển.

### 00:10:11.000 - 00:10:14.000
Vectơ đó sẽ chứa các số lẻ.

### 00:10:15.000 - 00:10:16.000
Bắt đầu từ một.

### 00:10:19.000 - 00:10:22.000
Lên đến số lượng kích thước của nhà nước.

### 00:10:22.000 - 00:10:23.000
Lần hai.

### 00:10:25.000 - 00:10:28.000
Thùng chứa một phần tử cho mỗi chiều của trạng thái.

### 00:10:29.000 - 00:10:34.000
Nếu lấy kích thước của thùng, chúng ta sẽ có số thứ nguyên ở trạng thái đó.

### 00:10:36.000 - 00:10:40.000
Trong trường hợp này, chúng ta sẽ có hai chiều nhân hai.

### 00:10:42.000 - 00:10:49.000
Và điều này có nghĩa là vectơ dịch chuyển sẽ có giá trị một và ba.

### 00:10:52.000 - 00:10:55.000
Và bây giờ chúng ta sẽ xem vector này sẽ làm gì.

### 00:10:59.000 - 00:11:03.000
Bây giờ chúng ta sẽ tạo một biến gọi là độ dịch chuyển.

### 00:11:04.000 - 00:11:07.000
Điều đó sẽ bằng với vectơ dịch chuyển.

### 00:11:11.000 - 00:11:11.000
Thời đại.

### 00:11:11.000 - 00:11:12.000
TÔI.

### 00:11:14.000 - 00:11:15.000
Modulo n.

### 00:11:18.000 - 00:11:19.000
Điều này có nghĩa là gì?

### 00:11:19.000 - 00:11:26.000
Chà, điều đó có nghĩa là lần đầu tiên chúng ta tạo một tập hợp trạng thái, tôi sẽ bằng một.

### 00:11:26.000 - 00:11:34.000
Và chúng ta sẽ dịch chuyển chiều thứ nhất của trạng thái một đơn vị và chiều thứ hai thêm ba đơn vị.

### 00:11:35.000 - 00:11:38.000
Sau đó, khi chúng ta tạo ô xếp thứ hai.

### 00:11:39.000 - 00:11:42.000
Điều này sẽ đặt kích thước đầu tiên bằng hai đơn vị?

### 00:11:45.000 - 00:11:48.000
Và chiều thứ hai bằng sáu modulo n.

### 00:11:50.000 - 00:11:55.000
Giả sử rằng N là dành cho vì chúng tôi muốn tập hợp trạng thái.

### 00:11:56.000 - 00:12:03.000
Sau đó, chúng tôi sẽ thay đổi chiều thứ hai của tập hợp dữ liệu này bằng sáu modulo bốn đơn vị.

### 00:12:05.000 - 00:12:07.000
Sáu modulo bốn bằng hai.

### 00:12:09.000 - 00:12:15.000
Nghĩa là, chúng ta sẽ di chuyển chiều thứ nhất của tập hợp trạng thái theo hai đơn vị và chiều thứ hai

### 00:12:15.000 - 00:12:17.000
cũng bằng hai đơn vị.

### 00:12:17.000 - 00:12:25.000
Khi tôi bằng ba, chúng ta sẽ di chuyển tập hợp thứ nhất thêm ba đơn vị và tập hợp thứ hai thêm chín modulo

### 00:12:25.000 - 00:12:26.000
bốn.

### 00:12:26.000 - 00:12:28.000
Đó là bởi một đơn vị.

### 00:12:31.000 - 00:12:32.000
Và vân vân và vân vân.

### 00:12:35.000 - 00:12:38.000
Hãy viết chuyển vị bằng.

### 00:12:40.000 - 00:12:43.000
Những vị trí này lần.

### 00:12:45.000 - 00:12:47.000
Kích thước phân khúc.

### 00:12:48.000 - 00:12:51.000
Chia cho n.

### 00:12:52.000 - 00:12:54.000
Kích thước phân đoạn trên n.

### 00:12:56.000 - 00:13:04.000
Kích thước phân đoạn trên n chia kích thước của trạng thái tổng hợp cho số ô mà chúng ta muốn

### 00:13:04.000 - 00:13:05.000
để tạo ra.

### 00:13:05.000 - 00:13:10.000
Tức là chúng ta sẽ chia kích thước của trạng thái tổng hợp này cho bốn.

### 00:13:11.000 - 00:13:15.000
Và cuối cùng, chúng ta sẽ di chuyển các giá trị tối thiểu của tập hợp trạng thái.

### 00:13:20.000 - 00:13:24.000
Bằng các giá trị được tính toán trong biến chuyển vị.

### 00:13:25.000 - 00:13:28.000
Và chúng ta sẽ làm tương tự với các giá trị tối đa.

### 00:13:41.000 - 00:13:48.000
Và bây giờ chúng ta có giá trị tối thiểu của tập hợp trạng thái đó, giá trị tối đa và kích thước của

### 00:13:48.000 - 00:13:49.000
từng phân đoạn.

### 00:13:53.000 - 00:13:57.000
Chúng ta có thể sao chép dòng này từ kỹ thuật tổng hợp trạng thái.

### 00:14:01.000 - 00:14:02.000
Và dán nó vào đây.

### 00:14:06.000 - 00:14:11.000
Nhưng bây giờ chúng ta sẽ thực hiện một số phép tổng hợp.

### 00:14:11.000 - 00:14:17.000
Vì vậy, chúng tôi sẽ cung cấp cho nó chỉ mục I và chúng tôi sẽ xóa.

### 00:14:18.000 - 00:14:19.000
Bản thân tham khảo.

### 00:14:21.000 - 00:14:28.000
Và chúng ta cũng sẽ gán chỉ số I cho giá trị cao và giá trị thấp.

### 00:14:35.000 - 00:14:39.000
Và bây giờ chúng ta sẽ thêm vào danh sách các ô xếp.

### 00:14:40.000 - 00:14:42.000
Ốp lát cụ thể này.

### 00:14:47.000 - 00:14:50.000
Chúng tôi sẽ lặp lại điều đó nhiều lần.

### 00:14:52.000 - 00:14:54.000
Theo số lượng ốp lát mà chúng tôi muốn.

### 00:14:54.000 - 00:14:57.000
Và cuối cùng, chức năng này sẽ trở lại.

### 00:14:58.000 - 00:15:00.000
Những tấm lát gạch.

### 00:15:15.000 - 00:15:18.000
Chúng tôi đã thấy nhiều điều mới trong phương pháp này.

### 00:15:18.000 - 00:15:22.000
Vì vậy, nếu bạn cần dừng video và xem lại, hãy thoải mái làm như vậy.

### 00:15:22.000 - 00:15:29.000
Bây giờ chúng ta hãy quay lại phương thức init và chúng ta thấy rằng việc gọi phương thức này mà chúng ta lưu trữ.

### 00:15:30.000 - 00:15:32.000
Trong biến ốp lát.

### 00:15:33.000 - 00:15:36.000
Mỗi tập hợp trạng thái mà chúng tôi đã tạo.

### 00:15:37.000 - 00:15:44.000
Bây giờ tất cả những gì chúng ta phải làm là xác định phương thức quan sát mà siêu lớp sẽ sử dụng để sửa đổi các trạng thái.

### 00:15:54.000 - 00:16:01.000
Trong phương pháp trước khi chúng tôi xử lý trạng thái, những gì chúng tôi nhận được là một bộ dữ liệu có các chỉ mục.

### 00:16:02.000 - 00:16:06.000
Của giá trị tổng hợp trong mỗi một trong các thứ nguyên.

### 00:16:08.000 - 00:16:13.000
Giá trị đầu tiên trong bộ dữ liệu đó là chỉ số vị trí của ô tô.

### 00:16:14.000 - 00:16:18.000
Và thứ hai là chỉ số vận tốc của nó.

### 00:16:19.000 - 00:16:22.000
Bây giờ vì chúng tôi có một số ốp lát.

### 00:16:23.000 - 00:16:26.000
Chúng ta sẽ có một danh sách.

### 00:16:26.000 - 00:16:29.000
Với một số bộ chỉ số.

### 00:16:34.000 - 00:16:38.000
Nếu chúng ta có bốn ô, thì chúng ta sẽ có bốn bộ dữ liệu.

### 00:16:42.000 - 00:16:47.000
Nghĩa là, chúng ta sẽ có bốn cách biểu diễn độc lập cho trạng thái đó.

### 00:16:53.000 - 00:17:01.000
Tức là, hãy tưởng tượng rằng chúng ta đang làm việc với trạng thái -6,75.

### 00:17:03.000 - 00:17:12.000
Ốp lát màu đỏ sẽ gán nó cho trạng thái tổng hợp thứ hai trong khi ốp lát màu xanh lá cây sẽ gán nó cho trạng thái tổng hợp thứ hai.

### 00:17:12.000 - 00:17:13.000
đến cái thứ ba.

### 00:17:14.000 - 00:17:18.000
Do đó, chỉ số của mỗi ô có thể hơi khác nhau.

### 00:17:20.000 - 00:17:23.000
Và đó chính xác là điều làm cho phương pháp này trở nên hiệu quả.

### 00:17:24.000 - 00:17:31.000
Vì vậy, điều đầu tiên chúng ta sẽ làm là tạo một danh sách các chỉ mục sẽ khởi tạo dưới dạng trống

### 00:17:31.000 - 00:17:32.000
danh sách.

### 00:17:34.000 - 00:17:35.000
Sau đó cho mỗi kiểu dáng.

### 00:17:42.000 - 00:17:45.000
Chúng ta sẽ tính toán các chỉ số của nó.

### 00:17:48.000 - 00:17:49.000
Cùng một cách.

### 00:17:53.000 - 00:17:57.000
Như chúng ta đã làm ở phương pháp trước đó trong việc tổng hợp trạng thái.

### 00:18:00.000 - 00:18:06.000
Chúng tôi viết số hóa gọn gàng và chúng tôi chuyển nó dưới dạng đối số.

### 00:18:06.000 - 00:18:07.000
TÔI.

### 00:18:07.000 - 00:18:13.000
V cho mỗi cặp tôi có được bằng cách gọi zip.

### 00:18:21.000 - 00:18:22.000
Từ nhà nước.

### 00:18:24.000 - 00:18:25.000
Và việc lát gạch.

### 00:18:27.000 - 00:18:39.000
Điều đó sẽ làm là đối với mỗi phần tử trong trạng thái, nó sẽ tìm ra chỉ mục nào cho nó

### 00:18:39.000 - 00:18:42.000
thuộc về tập hợp trạng thái.

### 00:18:43.000 - 00:18:46.000
Và bây giờ chúng tôi thêm các chỉ số đó.

### 00:18:48.000 - 00:18:49.000
Vào danh sách.

### 00:18:55.000 - 00:18:58.000
Và chúng tôi trả lại danh sách các chỉ số.

### 00:19:04.000 - 00:19:05.000
Được rồi, điều đó thật khó khăn.

### 00:19:05.000 - 00:19:08.000
Nhưng bây giờ chúng ta đã có trình bao bọc môi trường.

### 00:19:09.000 - 00:19:14.000
Trình bao bọc này sẽ sửa đổi môi trường để áp dụng phương pháp mã hóa khối ảnh.

### 00:19:16.000 - 00:19:20.000
Bây giờ chúng ta sẽ bao bọc môi trường ban đầu bằng lớp này.

### 00:19:21.000 - 00:19:23.000
Chúng ta sẽ tạo ra bốn ô xếp.

### 00:19:25.000 - 00:19:28.000
Các thùng giống như trước đây sẽ có kích thước mảng 20 x 20.

### 00:19:32.000 - 00:19:37.000
Nghĩa là, nó sẽ có 20 giá trị có thể có cho mỗi chiều của trạng thái ban đầu.

### 00:19:38.000 - 00:19:43.000
Thấp là một mảng có các giá trị tối thiểu cho từng chiều của trạng thái.

### 00:19:46.000 - 00:19:49.000
Và chúng tôi biết rằng chúng tôi có nó trong biến này.

### 00:19:50.000 - 00:19:52.000
Còn cao thì ngược lại.

### 00:19:53.000 - 00:19:56.000
Số lượng cao nhất cho mỗi chiều của trạng thái.

### 00:19:56.000 - 00:19:59.000
Và chúng tôi biết chúng tôi có nó trong biến này.

### 00:20:01.000 - 00:20:05.000
Và bây giờ chúng ta đã sẵn sàng để tạo lớp bao bọc cho môi trường.

### 00:20:10.000 - 00:20:13.000
Chúng tôi sẽ cung cấp cho nó trạng thái làm đối số.

### 00:20:14.000 - 00:20:15.000
Các thùng biến.

### 00:20:17.000 - 00:20:17.000
Thấp.

### 00:20:21.000 - 00:20:23.000
Và số lượng gạch ốp lát.

### 00:20:26.000 - 00:20:29.000
Hãy xem liệu chúng ta đã thực thi ô này chưa.

### 00:20:29.000 - 00:20:33.000
Bây giờ hãy thực thi ô này.

### 00:20:34.000 - 00:20:35.000
Và cái này đây.

### 00:20:38.000 - 00:20:40.000
Rất tiếc, có lỗi đánh máy ở đây.

### 00:20:40.000 - 00:20:42.000
Đó là những quan sát.

### 00:20:45.000 - 00:20:47.000
Bây giờ hãy chạy ô.

### 00:20:51.000 - 00:20:53.000
Rất tiếc, có một chút nhầm lẫn ở đây.

### 00:20:56.000 - 00:21:00.000
Không gian phòng tập chấm đa dạng rời rạc.

### 00:21:04.000 - 00:21:06.000
Hãy loại bỏ các dấu ngoặc đơn này.

### 00:21:09.000 - 00:21:11.000
Hãy chạy tế bào này.

### 00:21:14.000 - 00:21:20.000
Và bây giờ chúng ta đã có môi trường sẵn sàng để sử dụng với bất kỳ phương pháp dạng bảng nào.

### 00:21:21.000 - 00:21:25.000
Trong video tiếp theo, chúng ta sẽ giải quyết nó bằng thuật toán.

