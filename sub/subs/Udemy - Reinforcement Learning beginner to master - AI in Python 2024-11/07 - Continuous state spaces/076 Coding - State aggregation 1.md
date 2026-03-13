## Nội dung

### 00:00:01.000 - 00:00:07.000
Trong phần này, chúng ta sẽ điều chỉnh các phương pháp dạng bảng mà chúng ta đã học ở các phần trước.

### 00:00:07.000 - 00:00:11.000
để kiểm soát các nhiệm vụ có không gian trạng thái liên tục.

### 00:00:11.000 - 00:00:18.000
Những gì chúng ta sẽ làm trước tiên là sửa đổi môi trường và sau đó áp dụng một trong các phương pháp dạng bảng từ phần trước.

### 00:00:18.000 - 00:00:19.000
phần.

### 00:00:20.000 - 00:00:26.000
Trong trường hợp này, chúng ta sẽ sử dụng phương pháp này để giải quyết nhiệm vụ và sửa đổi môi trường.

### 00:00:26.000 - 00:00:29.000
Chúng tôi sẽ sử dụng hai kỹ thuật riêng biệt.

### 00:00:29.000 - 00:00:35.000
Cái đầu tiên gọi là tập hợp trạng thái và cái thứ hai gọi là mã hóa ô.

### 00:00:39.000 - 00:00:44.000
Điều đầu tiên chúng ta cần làm là nhập phần mềm mà chúng ta sẽ sử dụng.

### 00:00:45.000 - 00:00:46.000
Vì điều đó.

### 00:00:46.000 - 00:00:48.000
Hãy chạy tế bào này.

### 00:00:50.000 - 00:00:52.000
Và bây giờ mã đã có sẵn.

### 00:00:53.000 - 00:00:58.000
Chúng ta sẽ sử dụng cùng các thư viện mà chúng ta đã sử dụng trong các phần trước, ngoại trừ một số khác biệt.

### 00:00:58.000 - 00:01:05.000
Đầu tiên là chúng ta sẽ sử dụng hàm Tqdm từ thư viện Tqdm.

### 00:01:06.000 - 00:01:12.000
Hàm này sẽ hiển thị cho chúng ta một thanh tiến trình khi chúng ta thực thi thuật toán sao. Thanh này sẽ cho chúng ta biết cách thực hiện

### 00:01:12.000 - 00:01:18.000
chúng ta đã thực hiện bao nhiêu lần lặp của vòng lặp chính và còn lại bao nhiêu lần.

### 00:01:18.000 - 00:01:23.000
Và từ tệp utils cục bộ, chúng ta sẽ nhập ba hàm.

### 00:01:23.000 - 00:01:27.000
Cái đầu tiên được gọi là cốt truyện Bảng chi phí cần đi.

### 00:01:27.000 - 00:01:33.000
Cái thứ hai được gọi là số liệu thống kê cốt truyện và cái thứ ba được gọi là Mọi thứ hạt giống.

### 00:01:34.000 - 00:01:37.000
Chúng tôi sẽ giải thích tác dụng của từng cái khi chúng tôi sử dụng chúng.

### 00:01:39.000 - 00:01:44.000
Trong biểu đồ này, bạn có thể thấy một cách rất đơn giản cách hoạt động của thuật toán tổng hợp trạng thái.

### 00:01:44.000 - 00:01:52.000
Như bạn thấy, chúng ta có một nhiệm vụ điều khiển trong đó trạng thái được biểu thị bằng một biến duy nhất có giá trị hợp lệ

### 00:01:52.000 - 00:01:54.000
từ âm mười đến dương mười.

### 00:01:54.000 - 00:01:59.000
Và trên trục Y, chúng ta có thể thấy giá trị tối ưu cho từng trạng thái đó.

### 00:02:00.000 - 00:02:03.000
Dòng màu xanh lam là giá trị tối ưu thực sự.

### 00:02:05.000 - 00:02:10.000
Và với màu vàng, bạn có thể thấy kết quả của việc áp dụng kỹ thuật tổng hợp trạng thái.

### 00:02:14.000 - 00:02:15.000
Kỹ thuật này.

### 00:02:15.000 - 00:02:23.000
Những gì chúng ta sẽ làm là đưa tất cả các trạng thái vào trong một phạm vi nhất định và nhóm chúng lại với nhau như thể chúng

### 00:02:23.000 - 00:02:24.000
một trạng thái duy nhất

### 00:02:24.000 - 00:02:32.000
Bằng cách đó, các phương thức dạng bảng có thể hoạt động với tác vụ này vì tác vụ chuyển từ trạng thái vô hạn sang

### 00:02:32.000 - 00:02:33.000
đến mức chỉ có mười.

### 00:02:36.000 - 00:02:40.000
Chà, trong cuốn sổ tay này chúng ta sẽ học cách áp dụng kỹ thuật này.

### 00:02:40.000 - 00:02:44.000
Điều đầu tiên chúng ta sẽ làm là tạo ra môi trường.

### 00:02:44.000 - 00:02:51.000
Chúng ta sẽ sử dụng hàm tạo từ thư viện phòng tập thể dục và bây giờ chúng ta sẽ tạo một môi trường mới

### 00:02:51.000 - 00:02:53.000
gọi là Xe Miền Núi.

### 00:02:55.000 - 00:02:56.000
Phiên bản số không.

### 00:02:57.000 - 00:03:00.000
Và bây giờ hãy xem nhiệm vụ này là gì.

### 00:03:01.000 - 00:03:05.000
Nhưng trước tiên, hãy gọi CD Everything Function.

### 00:03:07.000 - 00:03:09.000
Và chúng ta sẽ chuyển trạng thái đó làm đối số.

### 00:03:10.000 - 00:03:12.000
Nhưng chức năng này làm gì?

### 00:03:12.000 - 00:03:20.000
Chà, những gì nó làm là đảm bảo rằng mỗi khi chúng tôi thực thi thư viện này, chúng tôi sẽ nhận được kết quả như nhau.

### 00:03:22.000 - 00:03:28.000
Bằng cách đó, khi bạn thực hiện cuốn sổ này ở nhà, kết quả của bạn sẽ giống như những gì bạn đã làm.

### 00:03:28.000 - 00:03:29.000
nhìn thấy trên màn hình.

### 00:03:29.000 - 00:03:30.000
Hãy chạy tế bào này.

### 00:03:30.000 - 00:03:33.000
Và bây giờ chúng ta có nhiệm vụ kiểm soát của mình.

### 00:03:33.000 - 00:03:34.000
Hãy xem nó nói về điều gì.

### 00:03:36.000 - 00:03:44.000
Hãy chạy phương thức reset và kiểm tra xem quan sát trạng thái của môi trường này trông như thế nào.

### 00:03:46.000 - 00:03:47.000
Đây rồi.

### 00:03:47.000 - 00:03:54.000
Giá trị đầu tiên sẽ biểu thị vị trí của ô tô trên trục ngang và giá trị thứ hai

### 00:03:54.000 - 00:03:56.000
sẽ đại diện cho vận tốc của ô tô.

### 00:03:58.000 - 00:04:00.000
Bây giờ chúng ta hãy xem nó bằng đồ họa.

### 00:04:03.000 - 00:04:04.000
Vì điều đó.

### 00:04:04.000 - 00:04:13.000
Chúng tôi sẽ sử dụng chức năng hiển thị từ thư viện Matplotlib và chúng tôi sẽ chuyển cho nó một hình ảnh

### 00:04:13.000 - 00:04:14.000
của nhà nước.

### 00:04:15.000 - 00:04:17.000
Hãy cất giữ nó ở đây.

### 00:04:17.000 - 00:04:21.000
Hãy viết khung bằng nhau và kết xuất.

### 00:04:22.000 - 00:04:25.000
Và chúng tôi chuyển sang chế độ đối số.

### 00:04:27.000 - 00:04:29.000
Mảng RGB bằng nhau.

### 00:04:33.000 - 00:04:34.000
Và đến chức năng hiển thị.

### 00:04:34.000 - 00:04:36.000
Chúng ta sẽ vượt qua khung này.

### 00:04:37.000 - 00:04:38.000
Hãy chạy tế bào.

### 00:04:39.000 - 00:04:41.000
Và ở đây chúng tôi có nó.

### 00:04:41.000 - 00:04:45.000
Như các bạn thấy trong nhiệm vụ, chúng ta điều khiển chiếc xe này ở đây.

### 00:04:46.000 - 00:04:48.000
Chiếc xe đang ở giữa thung lũng.

### 00:04:50.000 - 00:04:53.000
Bị mắc kẹt giữa hai con dốc.

### 00:04:53.000 - 00:04:57.000
Và mục tiêu của chúng ta là làm cho chiếc xe đạt được lá cờ bên phải.

### 00:04:58.000 - 00:04:59.000
Vì điều đó.

### 00:04:59.000 - 00:05:06.000
Chúng ta phải lái chiếc xe lên đồi cho đến khi nó có đủ động lượng để tự đẩy mình đến đích.

### 00:05:06.000 - 00:05:07.000
lá cờ.

### 00:05:07.000 - 00:05:13.000
Nếu chúng ta chỉ đẩy nó về phía trước, nó sẽ không có đủ tốc độ để chạm tới lá cờ.

### 00:05:13.000 - 00:05:16.000
Vì thế chúng ta phải xoay nó qua lại.

### 00:05:16.000 - 00:05:18.000
Để làm được điều đó chúng ta có thể thực hiện ba hành động.

### 00:05:18.000 - 00:05:22.000
Chúng ta có thể đẩy xe về phía trước, đẩy về phía sau hoặc không đẩy gì cả.

### 00:05:24.000 - 00:05:26.000
Tuy nhiên, nhiệm vụ này.

### 00:05:27.000 - 00:05:29.000
Tạo ra một vấn đề cho chúng tôi.

### 00:05:29.000 - 00:05:34.000
Bởi vì trạng thái của nó được biểu thị bằng các giá trị liên tục.

### 00:05:34.000 - 00:05:37.000
Vì vậy chúng ta không thể sử dụng thuật toán tìm kiếm trước.

### 00:05:37.000 - 00:05:44.000
Chúng ta phải thực hiện một số loại sửa đổi đối với môi trường để nó tạo ra các trạng thái theo một

### 00:05:44.000 - 00:05:47.000
định dạng mà thuật toán của chúng tôi có thể hoạt động.

### 00:05:47.000 - 00:05:51.000
Và để làm được điều đó, chúng ta sẽ triển khai kỹ thuật tổng hợp trạng thái.

### 00:05:51.000 - 00:05:58.000
Chiến lược tiếp theo bao gồm việc tạo ra một đối tượng bao bọc môi trường.

### 00:05:59.000 - 00:06:03.000
Và sửa đổi các trạng thái mà môi trường tạo ra.

### 00:06:03.000 - 00:06:09.000
Nghĩa là, mỗi khi chúng ta tương tác với môi trường và môi trường sẽ tạo ra một trạng thái,

### 00:06:09.000 - 00:06:16.000
đối tượng bao bọc môi trường sẽ sửa đổi trạng thái đó để chúng ta có thể làm việc với nó.

### 00:06:16.000 - 00:06:21.000
Vì vậy, chúng ta sẽ tạo một lớp sẽ bao bọc môi trường và chúng ta sẽ

### 00:06:21.000 - 00:06:25.000
gọi tập hợp trạng thái lớp đó là env.

### 00:06:31.000 - 00:06:38.000
Và lớp đó sẽ kế thừa từ một lớp trong thư viện phòng tập thể dục có tên là lớp quan sát.

### 00:06:46.000 - 00:06:53.000
Đây là một lớp từ thư viện phòng tập thể dục sẽ đơn giản hóa việc áp dụng các sửa đổi cho môi trường ban đầu,

### 00:06:53.000 - 00:06:55.000
giống như điều chúng tôi muốn thực hiện.

### 00:06:57.000 - 00:06:59.000
Vì thế, chúng ta sẽ tạo lớp.

### 00:06:59.000 - 00:07:04.000
Và trong phương thức khởi tạo của lớp đó, chúng ta sẽ truyền các đối số mà nó cần.

### 00:07:07.000 - 00:07:10.000
Chúng ta sẽ cần môi trường sẽ được bao bọc.

### 00:07:14.000 - 00:07:15.000
Một biến được gọi là thùng.

### 00:07:17.000 - 00:07:21.000
Một cái khác gọi là Thấp và cái cuối cùng sẽ được gọi là cao.

### 00:07:21.000 - 00:07:23.000
Và bây giờ chúng ta sẽ xem chúng dùng để làm gì.

### 00:07:30.000 - 00:07:31.000
Bên trong phương thức init.

### 00:07:31.000 - 00:07:37.000
Điều đầu tiên chúng ta làm là gọi phương thức init từ siêu lớp.

### 00:07:37.000 - 00:07:44.000
Truyền môi trường sẽ thực thi phương thức init của lớp trình bao bọc quan sát.

### 00:07:46.000 - 00:07:48.000
Bây giờ đến phần thú vị.

### 00:07:51.000 - 00:07:56.000
Phần mà đối với mỗi khía cạnh của trạng thái, chúng ta sẽ tổng hợp các khía cạnh khác nhau

### 00:07:56.000 - 00:07:58.000
phạm vi của các tiểu bang.

### 00:07:59.000 - 00:08:02.000
Và chiến lược mà chúng tôi sẽ theo đuổi là thế này.

### 00:08:02.000 - 00:08:08.000
Chúng tôi sẽ tra cứu giá trị tối thiểu và tối đa cho từng thứ nguyên của trạng thái.

### 00:08:09.000 - 00:08:16.000
Và sau đó chúng ta sẽ quyết định xem chúng ta muốn chia chiều đó bao nhiêu phần.

### 00:08:16.000 - 00:08:20.000
Sau đó, chúng tôi sẽ tính toán kích thước của từng phạm vi đó.

### 00:08:21.000 - 00:08:28.000
Bằng cách chia tổng phạm vi của thứ nguyên đó của trạng thái cho số giá trị mà chúng ta muốn

### 00:08:28.000 - 00:08:29.000
làm việc với.

### 00:08:29.000 - 00:08:32.000
Và chúng ta sẽ làm điều đó theo cách sau.

### 00:08:32.000 - 00:08:40.000
Chúng tôi sẽ tạo một danh sách trong đó chúng tôi sẽ lưu trữ các giá trị sẽ phân tách một phạm vi này với phạm vi khác.

### 00:08:41.000 - 00:08:44.000
Đó là giá trị của điểm này ở đây.

### 00:08:44.000 - 00:08:45.000
Điểm này đây.

### 00:08:47.000 - 00:08:54.000
Cái này, cái này, vân vân và vân vân, với tất cả những điểm ngăn cách một nhóm tổng hợp

### 00:08:54.000 - 00:08:55.000
trạng thái từ trạng thái khác.

### 00:08:58.000 - 00:09:00.000
Sau đó chúng ta sẽ viết.

### 00:09:01.000 - 00:09:02.000
NumPy.

### 00:09:04.000 - 00:09:04.000
Không gian.

### 00:09:06.000 - 00:09:08.000
Và sẽ vượt qua giá trị tối thiểu.

### 00:09:11.000 - 00:09:16.000
Giá trị tối đa và số lượng thùng trừ đi một.

### 00:09:17.000 - 00:09:18.000
Bây giờ, chúng tôi sẽ giải thích tại sao.

### 00:09:21.000 - 00:09:28.000
Hãy viết cho L, h và B dưới dạng zip.

### 00:09:29.000 - 00:09:32.000
Thùng cao thấp.

### 00:09:33.000 - 00:09:39.000
Và cái này chúng ta sẽ lưu trữ nó trong thuộc tính self dot Bucks.

### 00:09:39.000 - 00:09:42.000
Bây giờ hãy giải thích những gì chúng tôi đã làm.

### 00:09:45.000 - 00:09:54.000
Ba biến Beans, low và high này là các mảng có nhiều mảng có hình dạng sau.

### 00:10:02.000 - 00:10:10.000
Lo là một mảng có nhiều mảng có giá trị -1,2 và -0,07.

### 00:10:12.000 - 00:10:20.000
Xin chào là một mảng có nhiều mảng có giá trị 0,60,7

### 00:10:21.000 - 00:10:25.000
và Beans là một mảng có nhiều mảng có giá trị 2020.

### 00:10:27.000 - 00:10:28.000
Điều này có nghĩa là gì?

### 00:10:29.000 - 00:10:32.000
Vâng, hãy nhớ rằng trạng thái có hai chiều.

### 00:10:32.000 - 00:10:39.000
Cái đầu tiên bao gồm vị trí của ô tô trên trục x và cái thứ hai, vận tốc của nó.

### 00:10:39.000 - 00:10:47.000
Điều này có nghĩa là vị trí của ô tô sẽ có giá trị tối thiểu là -1,2 và giá trị tối đa

### 00:10:47.000 - 00:10:55.000
là 0,6 và vận tốc nằm trong khoảng -0 dấu phẩy 0 bảy.

### 00:10:56.000 - 00:10:57.000
Và tích cực.

### 00:10:57.000 - 00:10:58.000
Không.

### 00:10:58.000 - 00:10:59.000
Dấu phẩy số không bảy.

### 00:11:04.000 - 00:11:09.000
Và mỗi kích thước này sẽ chia thành 20 thùng.

### 00:11:09.000 - 00:11:11.000
20 tiểu bang tổng hợp.

### 00:11:14.000 - 00:11:22.000
Vì vậy, những gì chúng tôi đang làm ở đây là lấy giá trị đầu tiên ở mức thấp và giá trị đầu tiên ở mức cao và giá trị đầu tiên ở mức cao.

### 00:11:22.000 - 00:11:23.000
giá trị trong thùng.

### 00:11:23.000 - 00:11:33.000
Và chúng ta sẽ gán các giá trị này cho các biến L, H và B và sử dụng hàm linspace từ numpy.

### 00:11:33.000 - 00:11:42.000
Những gì chúng ta làm ở đây là lấy phạm vi từ -1,2 đến dương 0,6 và chia nó cho B trừ

### 00:11:42.000 - 00:11:45.000
một đoạn có cùng kích thước.

### 00:11:45.000 - 00:11:48.000
Giống như bạn có thể thấy ở trên đây.

### 00:11:49.000 - 00:11:49.000
Đây.

### 00:11:49.000 - 00:11:55.000
Nó được chia thành 10 đoạn và chúng ta sẽ chia nó thành 20 trừ một.

### 00:11:56.000 - 00:11:59.000
Chúng tôi làm điều đó vì thư viện đơn giản hoạt động theo cách đó.

### 00:11:59.000 - 00:12:03.000
Nhưng những gì chúng tôi nhận được là 20 phạm vi.

### 00:12:03.000 - 00:12:06.000
Sau đó, phương thức zip sẽ được chọn.

### 00:12:07.000 - 00:12:15.000
Giá trị thứ hai của Lo, sẽ biểu thị vận tốc tối thiểu và giá trị thứ hai của độ cao,

### 00:12:15.000 - 00:12:17.000
vận tốc tối đa.

### 00:12:17.000 - 00:12:19.000
Hãy cho nó một dấu ngoặc đơn ở đây.

### 00:12:21.000 - 00:12:23.000
Và giá trị thứ hai của bins.

### 00:12:27.000 - 00:12:28.000
Số lượng các trạng thái có thể.

### 00:12:30.000 - 00:12:31.000
Đối với vận tốc của ô tô.

### 00:12:32.000 - 00:12:40.000
Và những giá trị đó sẽ được gán cho các biến L, H và B và chúng tôi sẽ chia phạm vi đó thành 20 phân đoạn.

### 00:12:41.000 - 00:12:45.000
Và kết quả sẽ được lưu vào thuộc tính self dot packets.

### 00:12:47.000 - 00:12:49.000
Hãy dọn dẹp cái này đi.

### 00:12:54.000 - 00:12:58.000
Và điều tiếp theo chúng ta sẽ làm là thay đổi không gian trạng thái.

### 00:12:59.000 - 00:13:01.000
Về môi trường mà chúng tôi đang làm việc cùng.

### 00:13:05.000 - 00:13:08.000
Hãy viết không gian tập thể dục.

### 00:13:09.000 - 00:13:10.000
Đa rời rạc.

### 00:13:15.000 - 00:13:17.000
Và chúng ta chuyển nó thành không gian trạng thái mới.

### 00:13:21.000 - 00:13:25.000
Giá trị của thùng được chuyển đổi thành danh sách.

### 00:13:27.000 - 00:13:29.000
Chúng ta đang làm gì ở đây?

### 00:13:29.000 - 00:13:37.000
Chà, điều chúng ta đang nói là không gian trạng thái bây giờ sẽ hoạt động giống như không gian trạng thái mà

### 00:13:37.000 - 00:13:39.000
chúng tôi đã sử dụng trong nhiệm vụ mê cung.

### 00:13:39.000 - 00:13:46.000
Nghĩa là, chúng ta sẽ có 20 giá trị có thể có cho vị trí của giỏ hàng và 20 giá trị có thể có cho vị trí của nó.

### 00:13:46.000 - 00:13:46.000
vận tốc.

### 00:13:46.000 - 00:13:52.000
Và điều đó sẽ cho chúng ta tổng số trạng thái có thể có là 400.

### 00:13:55.000 - 00:13:56.000
Được rồi.

### 00:13:56.000 - 00:14:00.000
Chúng tôi đã khởi tạo đối tượng sẽ bao bọc môi trường.

### 00:14:01.000 - 00:14:07.000
Và bây giờ điều chúng ta cần làm là sửa đổi các trạng thái mà môi trường ban đầu tạo ra.

### 00:14:08.000 - 00:14:14.000
Bằng cách đó, chúng ta sẽ chuyển từ làm việc với các trạng thái liên tục sang làm việc với các trạng thái tổng hợp.

### 00:14:14.000 - 00:14:22.000
Để làm được điều đó, chúng tôi ghi đè phương pháp quan sát, đây là phương pháp sẽ sửa đổi các trạng thái được tạo

### 00:14:22.000 - 00:14:24.000
bởi môi trường.

### 00:14:29.000 - 00:14:33.000
Và chúng ta sẽ vượt qua nó, rõ ràng là chính giá trị và trạng thái giá trị.

### 00:14:39.000 - 00:14:43.000
Hàm này sẽ gọi lớp bao bọc quan sát.

### 00:14:43.000 - 00:14:46.000
Mỗi khi môi trường đó nó bao bọc.

### 00:14:47.000 - 00:14:49.000
Tạo ra một trạng thái.

### 00:14:50.000 - 00:14:55.000
Đó là khi chúng ta thiết lập lại môi trường hoặc khi chúng ta thực hiện một hành động.

### 00:14:57.000 - 00:15:04.000
Khi điều đó xảy ra, trạng thái mới đó sẽ được chuyển đến lớp này và lớp này sẽ gọi phương thức quan sát

### 00:15:04.000 - 00:15:09.000
và nó sẽ sửa đổi trạng thái để có định dạng mà chúng tôi quan tâm.

### 00:15:09.000 - 00:15:19.000
Một ví dụ về điều chúng tôi muốn đạt được là chuyển đổi trạng thái liên tục như -1,20 thành trạng thái này

### 00:15:19.000 - 00:15:20.000
trạng thái rời rạc.

### 00:15:23.000 - 00:15:24.000
Cho ba.

### 00:15:28.000 - 00:15:35.000
Trạng thái có giá trị tổng hợp cho vị trí của giỏ hàng và giá trị tổng hợp ba cho

### 00:15:35.000 - 00:15:36.000
vận tốc của ô tô.

### 00:15:37.000 - 00:15:40.000
Giống như chúng ta đã làm trong môi trường mê cung.

### 00:15:41.000 - 00:15:45.000
Với giá trị đầu tiên là hàng và giá trị thứ hai là cột.

### 00:15:46.000 - 00:15:49.000
Vì vậy, ở đây chúng ta sẽ tạo các chỉ số có thể thay đổi.

### 00:15:51.000 - 00:15:53.000
Đó sẽ là một tuple.

### 00:15:55.000 - 00:16:03.000
Và chúng ta cần một phương thức sẽ chọn giá trị này và chúng ta sẽ xem xét bên trong các thùng mà chúng ta đã tạo cho mỗi giá trị

### 00:16:03.000 - 00:16:04.000
của các kích thước.

### 00:16:11.000 - 00:16:15.000
Và chúng ta có thể làm điều đó với hàm số hóa gọn gàng.

### 00:16:18.000 - 00:16:20.000
Điều đó sẽ lấy giá trị liên tục làm đầu vào.

### 00:16:23.000 - 00:16:25.000
Và những chiếc xô có số đó có thể rơi xuống.

### 00:16:43.000 - 00:16:44.000
Ở đây chúng tôi có nó.

### 00:16:45.000 - 00:16:48.000
Hãy lặp lại cho từng kích thước của trạng thái.

### 00:16:49.000 - 00:16:54.000
Và đối với từng thùng mà chúng tôi đã tạo cho các trạng thái tổng hợp.

### 00:16:54.000 - 00:16:57.000
Và chúng ta sẽ làm điều đó bằng phương thức zip.

### 00:16:59.000 - 00:17:07.000
Và sẽ chuyển từng cặp phần tử của 2 phần tử này cho hàm số hóa để nó cho ta biết trong đó

### 00:17:07.000 - 00:17:14.000
phạm vi từng giá trị liên tục của trạng thái giảm và kết quả sẽ lưu trữ nó trong một bộ dữ liệu gọi là

### 00:17:14.000 - 00:17:17.000
các chỉ số sẽ có dạng này.

### 00:17:17.000 - 00:17:21.000
Và bây giờ tất cả những gì chúng ta phải làm là trả về những chỉ số này.

### 00:17:26.000 - 00:17:28.000
Hãy thực hiện lớp này.

### 00:17:29.000 - 00:17:31.000
Và bây giờ hãy kiểm tra nó.

### 00:17:33.000 - 00:17:36.000
Điều đầu tiên chúng ta cần là ba biến này.

### 00:17:39.000 - 00:17:41.000
Đậu sẽ là một mảng có nhiều mảng.

### 00:17:45.000 - 00:17:52.000
Với số lượng trạng thái riêng biệt mà chúng ta muốn cho mỗi chiều của trạng thái, hãy chọn 20.

### 00:17:52.000 - 00:17:53.000
Đối với mỗi chiều.

### 00:17:53.000 - 00:18:00.000
Điều tiếp theo chúng ta cần là mảng có nhiều mảng với các giá trị tối thiểu mà mỗi chiều của trạng thái

### 00:18:00.000 - 00:18:01.000
có thể lấy.

### 00:18:01.000 - 00:18:06.000
Và chúng ta biết rằng chúng ta có điều đó trong không gian biến thiên và không gian quan sát.

### 00:18:06.000 - 00:18:07.000
Thấp.

### 00:18:09.000 - 00:18:13.000
Và chúng ta cũng cần các giá trị tối đa cho từng chiều.

### 00:18:15.000 - 00:18:20.000
Mà chúng ta có thể nhận được từ không gian quan sát biến env.

### 00:18:20.000 - 00:18:20.000
CHÀO.

### 00:18:24.000 - 00:18:29.000
Và bây giờ chúng ta sẽ tạo một thể hiện của lớp tổng hợp trạng thái.

### 00:18:32.000 - 00:18:38.000
Chuyển qua môi trường mà nó sẽ bao bọc giá trị cho các thùng mà chúng ta đã xác định.

### 00:18:40.000 - 00:18:41.000
Giá trị thấp.

### 00:18:43.000 - 00:18:44.000
Và giá trị cho cao.

### 00:18:45.000 - 00:18:46.000
Hãy chạy tế bào.

### 00:18:48.000 - 00:18:51.000
Rất tiếc, chúng tôi đã quên viết hai dấu gạch dưới đó.

### 00:18:51.000 - 00:18:53.000
Thực hiện theo phương pháp init.

### 00:18:55.000 - 00:18:57.000
Hãy chạy lại ô.

### 00:19:00.000 - 00:19:02.000
Và ở đây chúng tôi có nó.

### 00:19:03.000 - 00:19:06.000
Chúng tôi có môi trường được bao bọc bởi lớp học của chúng tôi.

### 00:19:08.000 - 00:19:10.000
Bây giờ vì tò mò.

### 00:19:11.000 - 00:19:16.000
Chúng ta hãy xem các phạm vi trong đó mỗi kích thước được chia.

### 00:19:19.000 - 00:19:21.000
Hãy viết đi, Sam.

### 00:19:22.000 - 00:19:23.000
Cái xô.

### 00:19:29.000 - 00:19:33.000
Và như bạn có thể thấy, chúng ta có hai mảng có nhiều mảng.

### 00:19:34.000 - 00:19:41.000
Mảng đầu tiên chia các giá trị có thể có cho vị trí của ô tô ở 20 trạng thái tổng hợp.

### 00:19:45.000 - 00:19:47.000
Và giới hạn của mỗi người trong số họ.

### 00:19:48.000 - 00:19:52.000
Được xác định bởi mỗi một trong những con số này.

### 00:19:56.000 - 00:20:04.000
Và vận tốc của ô tô đi từ -0,07 đến dương 0,07.

### 00:20:04.000 - 00:20:12.000
Chúng tôi cũng đã chia phạm vi đó thành 20 giá trị có thể và mỗi phần tử trong số này là giới hạn của

### 00:20:12.000 - 00:20:13.000
những thùng đó.

### 00:20:17.000 - 00:20:21.000
Được rồi, bây giờ chúng ta có thể làm việc với môi trường này bằng các phương pháp dạng bảng.

### 00:20:21.000 - 00:20:26.000
Trong video tiếp theo, chúng ta sẽ triển khai thuật toán để giải quyết nhiệm vụ này.

### 00:20:26.000 - 00:20:27.000
Tôi sẽ gặp bạn ở đó.

