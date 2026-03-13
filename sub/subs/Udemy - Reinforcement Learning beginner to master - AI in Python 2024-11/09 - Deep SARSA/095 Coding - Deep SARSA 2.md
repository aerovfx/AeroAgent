## Nội dung

### 00:00:00.000 - 00:00:06.000
Trong video này, chúng ta sẽ chuẩn bị môi trường để thư viện PyTorch có thể dễ dàng hoạt động

### 00:00:06.000 - 00:00:06.000
với nó.

### 00:00:07.000 - 00:00:13.000
Và chúng ta sẽ làm điều đó bằng cách tạo một đối tượng bao bọc môi trường và cho chúng ta khả năng

### 00:00:13.000 - 00:00:18.000
để sửa đổi từng yếu tố thoát ra khỏi môi trường.

### 00:00:19.000 - 00:00:24.000
Ý tôi là khi chúng ta thực hiện một hành động trong môi trường, trước tiên chúng ta sẽ chuyển nó tới đây

### 00:00:24.000 - 00:00:32.000
lớp trình bao bọc sẽ chuẩn bị nó để gửi đến môi trường và các phần tử kết quả từ việc thực thi

### 00:00:32.000 - 00:00:37.000
hành động đó sẽ được lớp này xử lý trước trước khi chúng tôi lấy lại chúng.

### 00:00:38.000 - 00:00:39.000
Lớp này sẽ kế thừa.

### 00:00:41.000 - 00:00:46.000
Từ một lớp khác từ thư viện phòng tập tên là Rapper.

### 00:00:50.000 - 00:00:54.000
Điều đó sẽ cho phép chúng tôi sửa đổi đầu vào và đầu ra của môi trường.

### 00:00:55.000 - 00:00:58.000
Vì vậy, hãy triển khai lớp này cho điều đó.

### 00:00:58.000 - 00:01:03.000
Điều đầu tiên chúng ta cần làm là khởi tạo nó, truyền nó, môi trường mà nó sẽ bao bọc

### 00:01:04.000 - 00:01:07.000
và chuẩn bị cho lớp này tương tác với môi trường.

### 00:01:08.000 - 00:01:11.000
Đầu tiên chúng ta sẽ gọi phương thức init từ lớp trình bao bọc.

### 00:01:12.000 - 00:01:14.000
Điều đó sẽ làm công việc nền.

### 00:01:16.000 - 00:01:19.000
Điều đó cần phải được thực thi để trình bao bọc này.

### 00:01:19.000 - 00:01:22.000
Hoạt động như mong đợi.

### 00:01:26.000 - 00:01:28.000
Bây giờ chúng ta chỉ cần làm hai việc.

### 00:01:28.000 - 00:01:33.000
Cách đầu tiên là tạo một phương thức sẽ ghi đè.

### 00:01:34.000 - 00:01:37.000
Phương pháp thiết lập lại từ môi trường.

### 00:01:39.000 - 00:01:43.000
Và tiếp theo chúng ta cần tạo một phương thức khác để ghi đè.

### 00:01:44.000 - 00:01:47.000
Phương pháp bước từ môi trường.

### 00:01:50.000 - 00:01:55.000
Hãy bắt đầu bằng cách triển khai phương thức đặt lại sẽ đặt lại môi trường và chuẩn bị ban đầu

### 00:01:55.000 - 00:01:58.000
quan sát được sử dụng với PyTorch.

### 00:02:01.000 - 00:02:04.000
Hãy tạo một hàm gọi là reset.

### 00:02:04.000 - 00:02:06.000
Và bên trong hàm này chúng ta sẽ thu được.

### 00:02:07.000 - 00:02:10.000
Từ môi trường ban đầu.

### 00:02:14.000 - 00:02:22.000
Quan sát ban đầu của tác vụ bằng cách gọi phương thức đặt lại của nó, như bạn biết, là một mảng có nhiều mảng

### 00:02:22.000 - 00:02:26.000
với sự biểu diễn bằng số của trạng thái của nhiệm vụ.

### 00:02:27.000 - 00:02:30.000
Tiếp theo chúng ta cần sửa đổi mảng numpy này.

### 00:02:32.000 - 00:02:35.000
Để chuyển đổi nó thành một tensor pytorch.

### 00:02:38.000 - 00:02:39.000
Vì điều đó.

### 00:02:39.000 - 00:02:46.000
Chúng ta sẽ gọi ngọn đuốc từ hàm numpy và chuyển trạng thái của nó làm đối số.

### 00:02:48.000 - 00:02:50.000
Tiếp theo, chúng ta sẽ sửa đổi hình dạng.

### 00:02:51.000 - 00:02:52.000
Của tensor này.

### 00:02:55.000 - 00:02:59.000
Bởi vì hiện tại trạng thái chỉ là một quan sát duy nhất.

### 00:03:01.000 - 00:03:09.000
Nhưng vì chúng ta muốn làm việc với nhiều đợt quan sát nên chúng ta phải cung cấp cho nó một chiều bổ sung.

### 00:03:10.000 - 00:03:14.000
Vì vậy, những quan sát này có thể được kết hợp thành một đợt.

### 00:03:17.000 - 00:03:19.000
Nhưng tại sao vậy?

### 00:03:21.000 - 00:03:27.000
Chà, bởi vì khi chúng ta làm việc với các lô, sẽ có một số quan sát về trạng thái môi trường.

### 00:03:27.000 - 00:03:32.000
Và vì lý do đó mà mẻ sẽ có hình dạng n lần D.

### 00:03:35.000 - 00:03:39.000
Trong đó N là số lượng quan sát trong đợt đó.

### 00:03:40.000 - 00:03:43.000
Và đó là số lượng kích thước.

### 00:03:46.000 - 00:03:46.000
Đây.

### 00:03:46.000 - 00:03:56.000
Như bạn có thể thấy, n bằng hai vì có một và hai quan sát và D cũng bằng hai vì

### 00:03:56.000 - 00:03:59.000
mỗi quan sát có hai chiều.

### 00:04:01.000 - 00:04:08.000
Đây là một trong những sửa đổi nhỏ mà chúng tôi phải thực hiện khi làm việc với nhiều trải nghiệm.

### 00:04:08.000 - 00:04:10.000
Các hành động cũng sẽ có hình dạng.

### 00:04:10.000 - 00:04:14.000
Nghĩa là, chúng ta biết rằng một hành động chỉ là một số vô hướng.

### 00:04:15.000 - 00:04:18.000
Ví dụ, hành động một.

### 00:04:18.000 - 00:04:22.000
Giả sử rằng trong giai đoạn thứ hai, chúng ta thực hiện hành động.

### 00:04:23.000 - 00:04:28.000
Sau đó, loạt hành động này sẽ có hình dạng giống nhau.

### 00:04:29.000 - 00:04:30.000
Tại sao vậy?

### 00:04:31.000 - 00:04:39.000
Vâng, bởi vì chúng ta có hai hành động và mỗi hành động có một phần tử duy nhất, một chiều duy nhất.

### 00:04:39.000 - 00:04:46.000
Và hãy nhớ rằng chúng tôi làm điều này để làm việc với nhiều trải nghiệm thay vì quan sát riêng lẻ.

### 00:04:46.000 - 00:04:51.000
Và làm thế nào chúng ta có thể làm cho các quan sát riêng lẻ sẵn sàng được đưa vào theo đợt?

### 00:04:51.000 - 00:04:56.000
Chà, để làm được điều đó, chúng tôi gọi phương thức Unsqueezed từ Thư viện PyTorch.

### 00:05:00.000 - 00:05:05.000
Điều đó sẽ thêm thứ nguyên bổ sung đó vào vị trí mà chúng tôi chỉ định.

### 00:05:05.000 - 00:05:08.000
Chúng tôi muốn thêm nó vào chiều thứ 0.

### 00:05:10.000 - 00:05:12.000
Vì vậy, chúng tôi sẽ vượt qua cuộc tranh luận.

### 00:05:12.000 - 00:05:15.000
Dim bằng 0 đối với hàm.

### 00:05:17.000 - 00:05:22.000
Và tất nhiên chúng tôi muốn tensor mới này chứa số float, số thập phân.

### 00:05:27.000 - 00:05:27.000
Được rồi.

### 00:05:27.000 - 00:05:33.000
Đây là những gì trình bao bọc môi trường sẽ trả về và nó sẽ cho phép chúng ta làm việc với thư viện PyTorch.

### 00:05:35.000 - 00:05:41.000
Được rồi, bây giờ chúng ta đã có phương thức đầu tiên, chúng ta cần tạo phương thức thứ hai.

### 00:05:41.000 - 00:05:45.000
Chúng ta sẽ tạo một phương thức gọi là step.

### 00:05:46.000 - 00:05:50.000
Điều đó sẽ thực hiện hành động mà chúng ta chuyển đến môi trường.

### 00:05:51.000 - 00:05:53.000
Và nó sẽ làm hai việc.

### 00:05:53.000 - 00:05:59.000
Đầu tiên là thực hiện hành động mà mạng lưới thần kinh sẽ tạo ra, đó sẽ là một tenxơ pytorch.

### 00:06:00.000 - 00:06:03.000
Và nó sẽ chuyển đổi nó thành số nguyên python.

### 00:06:04.000 - 00:06:07.000
Và chúng ta sẽ làm điều đó với dòng mã sau.

### 00:06:08.000 - 00:06:16.000
Hãy viết hành động bằng hành động do mạng nơ-ron tạo ra và chúng ta sẽ gọi phương thức item.

### 00:06:17.000 - 00:06:20.000
Vì vậy, chúng tôi trích xuất giá trị số.

### 00:06:21.000 - 00:06:24.000
Từ tenxơ đó dưới dạng số nguyên python.

### 00:06:26.000 - 00:06:31.000
Sau đó, khi hành động đã sẵn sàng được chuyển đến môi trường, chúng tôi sẽ thực hiện chính xác điều đó.

### 00:06:39.000 - 00:06:40.000
Chúng ta sẽ gọi phương thức bước.

### 00:06:43.000 - 00:06:46.000
Và chúng ta biết rằng phương pháp này sẽ cho ra kết quả như sau.

### 00:06:47.000 - 00:06:48.000
Trạng thái tiếp theo.

### 00:06:52.000 - 00:06:52.000
Một phần thưởng.

### 00:06:54.000 - 00:06:56.000
Giá trị thực hiện.

### 00:06:58.000 - 00:07:03.000
Và một từ điển có thông tin bổ sung, trong trường hợp này, như mọi khi, chúng tôi sẽ không

### 00:07:03.000 - 00:07:04.000
sử dụng.

### 00:07:06.000 - 00:07:09.000
Được rồi, bây giờ chúng ta có kết quả thực hiện hành động.

### 00:07:10.000 - 00:07:13.000
Nhưng như chúng ta đã biết, trạng thái tiếp theo là một mảng có nhiều mảng.

### 00:07:13.000 - 00:07:18.000
Phần thưởng là số nguyên và Don là giá trị boolean.

### 00:07:18.000 - 00:07:21.000
Nhưng vì chúng tôi đang làm việc với thư viện PyTorch.

### 00:07:23.000 - 00:07:26.000
Chúng ta phải chuyển đổi các giá trị này thành tensor.

### 00:07:28.000 - 00:07:34.000
Và không chỉ vậy, chúng ta còn phải chuẩn bị chúng để có thể đưa vào các lô dữ liệu.

### 00:07:34.000 - 00:07:41.000
Và để làm được điều đó, những gì chúng ta sắp làm chính xác là những gì chúng ta đã làm với trạng thái ban đầu của nhiệm vụ.

### 00:07:41.000 - 00:07:48.000
Nghĩa là, chúng ta sẽ gọi ngọn đuốc từ hàm numpy truyền làm đối số cho mảng trạng thái tiếp theo.

### 00:07:50.000 - 00:07:53.000
Sau đó, chúng tôi sẽ cung cấp cho nó một chiều bổ sung.

### 00:07:53.000 - 00:07:55.000
Ở vị trí thứ không.

### 00:07:58.000 - 00:08:02.000
Và chúng ta sẽ đảm bảo rằng đó là một tenxơ dấu phẩy động.

### 00:08:07.000 - 00:08:07.000
Kế tiếp.

### 00:08:07.000 - 00:08:09.000
Chúng ta cần chuẩn bị phần thưởng.

### 00:08:11.000 - 00:08:15.000
Như bạn đã biết, chúng tôi muốn biến nó thành một tensor pytorch.

### 00:08:16.000 - 00:08:18.000
Và để làm được điều đó, chúng ta sẽ sử dụng dòng mã này.

### 00:08:19.000 - 00:08:25.000
Phần thưởng sẽ không còn là giá trị dấu phẩy động mà là tenxơ.

### 00:08:25.000 - 00:08:28.000
Mặc dù nó vẫn chưa có hình dạng phù hợp.

### 00:08:28.000 - 00:08:35.000
Hãy nhớ rằng đợt thưởng cần phải có hình dạng này thì phần tử đầu tiên của đợt sẽ

### 00:08:35.000 - 00:08:42.000
được liên kết với phần tử đầu tiên của lô hành động và với phần tử đầu tiên của lô trạng thái.

### 00:08:42.000 - 00:08:43.000
Và vì điều đó chúng tôi sẽ cung cấp cho nó.

### 00:08:44.000 - 00:08:46.000
Và vì điều đó chúng tôi sẽ trao phần thưởng.

### 00:08:46.000 - 00:08:48.000
Hai chiều bổ sung này.

### 00:08:49.000 - 00:08:57.000
Và chúng ta sẽ làm điều đó bằng cách gọi phương thức xem sẽ xác định lại hình dạng mà chúng ta nhìn thấy tensor này

### 00:08:57.000 - 00:09:01.000
và chúng ta sẽ chuyển cho nó giá trị một và giá trị âm.

### 00:09:09.000 - 00:09:17.000
Điều này có nghĩa là chúng ta sẽ có một tensor của một phần tử vì chúng ta biết rằng chúng ta đang làm việc với một phần tử duy nhất.

### 00:09:17.000 - 00:09:25.000
phần thưởng mà chúng ta nhận được từ môi trường, và phần thưởng tiêu cực này sẽ mang lại cho nó chiều hướng bên trong bổ sung.

### 00:09:27.000 - 00:09:32.000
Tôi khuyên bạn nên xem chức năng xem trong tài liệu PyTorch để bạn có thể thấy

### 00:09:32.000 - 00:09:34.000
sâu hơn với phương pháp này.

### 00:09:34.000 - 00:09:40.000
Bây giờ, điều cuối cùng chúng ta cần làm là đảm bảo rằng tensor mà chúng ta tạo ra có dạng dấu phẩy động

### 00:09:40.000 - 00:09:40.000
kiểu.

### 00:09:41.000 - 00:09:45.000
Và cuối cùng, chúng ta sẽ làm tương tự với biến done.

### 00:09:46.000 - 00:09:51.000
Như bạn đã biết, đây là một biến Boolean sẽ cho chúng ta biết tập phim đã kết thúc hay chưa.

### 00:09:51.000 - 00:09:57.000
Chúng ta sẽ chuyển nó thành một tenxơ và tạo cho nó một hình âm.

### 00:09:58.000 - 00:10:05.000
Và một khi chúng tôi đã sửa đổi ba yếu tố này để chúng có thể được đưa vào các đợt quan sát

### 00:10:05.000 - 00:10:10.000
và được sử dụng với thư viện PyTorch, chúng ta có thể trả lại các giá trị này cho thuật toán.

### 00:10:15.000 - 00:10:17.000
Hãy làm sạch cái này một chút.

### 00:10:24.000 - 00:10:25.000
Sẵn sàng.

### 00:10:27.000 - 00:10:28.000
Bây giờ chúng ta hãy xóa bình luận này.

### 00:10:32.000 - 00:10:33.000
Hãy chạy tế bào này.

### 00:10:35.000 - 00:10:38.000
Và bây giờ rapper của chúng tôi đã sẵn sàng.

### 00:10:40.000 - 00:10:44.000
Hãy tạo một thể hiện của tiền xử lý và lớp.

### 00:10:47.000 - 00:10:50.000
Và đưa nó làm đối số cho môi trường.

### 00:10:51.000 - 00:10:53.000
Ở đó chúng tôi có nó.

### 00:10:54.000 - 00:10:58.000
Bây giờ hãy kiểm tra các phần tử mà trình bao bọc tạo ra.

### 00:11:00.000 - 00:11:02.000
Nó sẽ sẵn sàng hoạt động với PyTorch.

### 00:11:03.000 - 00:11:06.000
Hãy bắt đầu bằng cách thiết lập lại môi trường.

### 00:11:09.000 - 00:11:16.000
Hãy gọi phương thức đặt lại trong trình bao bọc, lần lượt nó sẽ gọi phương thức đặt lại trên bản gốc

### 00:11:16.000 - 00:11:17.000
môi trường.

### 00:11:17.000 - 00:11:20.000
Và hãy giữ kết quả ở trạng thái thay đổi.

### 00:11:21.000 - 00:11:23.000
Hãy làm tương tự với hành động.

### 00:11:24.000 - 00:11:27.000
Đầu tiên, hãy tạo một tensor bằng hành động.

### 00:11:27.000 - 00:11:27.000
Không.

### 00:11:29.000 - 00:11:31.000
Cái nào sẽ được chuyển cho rapper.

### 00:11:36.000 - 00:11:41.000
Và hãy gọi phương thức bước trên trình bao bọc vượt qua lớp này.

### 00:11:42.000 - 00:11:48.000
Như bạn đã biết, sẽ chuyển tensor này thành một số nguyên và chúng ta sẽ chuyển nó về số nguyên

### 00:11:48.000 - 00:11:49.000
môi trường.

### 00:11:52.000 - 00:11:56.000
Và chúng tôi sẽ giữ nguyên các nhà sản xuất rapper ở một số khía cạnh.

### 00:12:03.000 - 00:12:06.000
Bây giờ hãy kiểm tra xem rapper đã sản xuất những gì.

### 00:12:06.000 - 00:12:07.000
Vì điều đó.

### 00:12:07.000 - 00:12:08.000
Hãy gọi hàm print.

### 00:12:11.000 - 00:12:13.000
Hãy in trạng thái ban đầu.

### 00:12:14.000 - 00:12:18.000
Và hãy gọi lại hàm print với các phần tử còn lại.

### 00:12:26.000 - 00:12:27.000
Trạng thái tiếp theo.

### 00:12:30.000 - 00:12:31.000
Phần thưởng.

### 00:12:37.000 - 00:12:38.000
Và xong.

### 00:12:39.000 - 00:12:41.000
Và bây giờ hãy chạy ô này.

### 00:12:46.000 - 00:12:52.000
Như bạn có thể thấy, các trạng thái, trước đây là một mảng có nhiều mảng với hai phần tử, giờ đây là một tensor với

### 00:12:52.000 - 00:12:53.000
hai phần tử.

### 00:12:56.000 - 00:13:02.000
Với chiều hướng bổ sung này sẽ cho phép chúng tôi kết hợp nó thành nhiều trải nghiệm.

### 00:13:02.000 - 00:13:07.000
Điều tương tự cũng xảy ra với trạng thái tiếp theo được tạo sau khi gọi phương thức bước.

### 00:13:07.000 - 00:13:14.000
Phần thưởng có giá trị giống hệt như giá trị mà môi trường đã trao cho chúng tôi, nhưng chúng tôi đã thêm hai giá trị này vào

### 00:13:14.000 - 00:13:18.000
các kích thước bổ sung để phần thưởng này có thể được đưa vào theo đợt.

### 00:13:22.000 - 00:13:25.000
Và điều tương tự cũng xảy ra với biến Don.

### 00:13:28.000 - 00:13:31.000
Mà vẫn có giá trị tương tự bởi môi trường.

### 00:13:33.000 - 00:13:36.000
Nhưng bây giờ nó đã có hình dạng phù hợp để làm việc với các lô.

### 00:13:38.000 - 00:13:44.000
Trong video tiếp theo, chúng ta sẽ tạo mạng nơ-ron sẽ sử dụng để ước tính các giá trị Q.

### 00:13:44.000 - 00:13:46.000
Tôi sẽ gặp bạn trong video tiếp theo.

