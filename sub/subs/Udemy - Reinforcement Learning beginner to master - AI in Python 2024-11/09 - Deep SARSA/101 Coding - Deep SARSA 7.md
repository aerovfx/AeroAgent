## Nội dung

### 00:00:00.000 - 00:00:04.000
Trong video này, chúng ta sẽ triển khai phương pháp mẫu của bộ nhớ.

### 00:00:04.000 - 00:00:11.000
Phương pháp này sẽ cho phép chúng tôi thu được nhiều kinh nghiệm mà chúng tôi sẽ sử dụng để cập nhật mạng nơ-ron.

### 00:00:12.000 - 00:00:14.000
Hãy xác định phương pháp.

### 00:00:17.000 - 00:00:20.000
Và đặt cho nó một đối số gọi là kích thước lô.

### 00:00:22.000 - 00:00:28.000
Đó sẽ là số phần tử cần đưa vào lô mà chúng ta sẽ thu được.

### 00:00:31.000 - 00:00:33.000
Nhưng trước tiên chúng ta phải đảm bảo rằng chúng ta có thể có được.

### 00:00:34.000 - 00:00:36.000
Một lô cỡ đó.

### 00:00:43.000 - 00:00:50.000
Và để làm được điều đó, chúng ta cần tạo một phương thức gọi là can sample để cho chúng ta biết liệu bộ nhớ có

### 00:00:50.000 - 00:00:55.000
đủ đầy để trích xuất hàng loạt trải nghiệm ở quy mô đó.

### 00:00:57.000 - 00:00:59.000
Hãy xác định phương pháp.

### 00:01:04.000 - 00:01:06.000
Và cung cấp cho nó một tham số.

### 00:01:07.000 - 00:01:10.000
Cái nào sẽ giống như trong phương pháp mẫu.

### 00:01:10.000 - 00:01:14.000
Đó là số phần tử cần đưa vào.

### 00:01:16.000 - 00:01:22.000
Và quy tắc mà chúng ta sẽ sử dụng để quyết định xem liệu chúng ta có thể bắt đầu rút ra các đợt trải nghiệm hay không.

### 00:01:24.000 - 00:01:26.000
Sau đây là

### 00:01:39.000 - 00:01:40.000
Đây rồi.

### 00:01:43.000 - 00:01:45.000
Khi số lượng chuyển tiếp trong bộ nhớ.

### 00:01:48.000 - 00:01:53.000
Ít nhất phải gấp mười lần kích thước của lô mà chúng tôi muốn lấy.

### 00:01:54.000 - 00:01:57.000
Sẽ có thể lấy mẫu hàng loạt từ bộ nhớ.

### 00:01:57.000 - 00:02:05.000
Chúng tôi đợi cho đến khi bộ nhớ có số lần chuyển đổi gấp mười lần để tránh thực hiện các đợt chuyển đổi giống nhau nhiều lần.

### 00:02:05.000 - 00:02:11.000
Khi biết rằng đã có đủ chuyển đổi, chúng ta có thể tiếp tục triển khai phương pháp mẫu.

### 00:02:13.000 - 00:02:16.000
Chúa ơi, việc chúng ta sắp làm là xác định biến batch.

### 00:02:18.000 - 00:02:24.000
Đó sẽ là lô chuyển đổi và chúng tôi sẽ sử dụng thư viện ngẫu nhiên để lấy lô đó.

### 00:02:26.000 - 00:02:29.000
Cụ thể, chúng tôi sẽ sử dụng phương pháp mẫu.

### 00:02:31.000 - 00:02:38.000
Phương pháp này sẽ chọn ngẫu nhiên từ bộ nhớ một số phần tử cụ thể và số lượng mục

### 00:02:38.000 - 00:02:43.000
mà nó sẽ lấy là kích thước mà chúng tôi chỉ định làm kích thước lô tham số.

### 00:02:44.000 - 00:02:49.000
Bây giờ chúng tôi có một lô, chúng tôi sẽ chuẩn bị nó để có thể làm việc với nó.

### 00:02:50.000 - 00:02:54.000
Bây giờ những gì chúng ta có là một danh sách các chuyển tiếp.

### 00:02:58.000 - 00:03:01.000
Trong quá trình chuyển đổi có hình dạng này.

### 00:03:07.000 - 00:03:10.000
Đây là một quá trình chuyển đổi khác cùng loại.

### 00:03:12.000 - 00:03:12.000
Vân vân.

### 00:03:15.000 - 00:03:19.000
Nhưng thực sự những gì chúng ta muốn là một cái gì đó như thế này.

### 00:03:19.000 - 00:03:20.000
Chúng tôi muốn.

### 00:03:24.000 - 00:03:26.000
Tất cả các tiểu bang cùng nhau.

### 00:03:28.000 - 00:03:30.000
Tất cả các hành động cùng nhau.

### 00:03:32.000 - 00:03:33.000
Tất cả các phần thưởng.

### 00:03:36.000 - 00:03:38.000
Và tất cả các trạng thái tiếp theo.

### 00:03:42.000 - 00:03:45.000
Để chúng ta có thể làm việc với họ một cách hiệu quả.

### 00:03:46.000 - 00:03:49.000
Và sẽ đạt được điều đó với dòng mã sau.

### 00:03:50.000 - 00:03:52.000
Hãy viết nhưng bằng nhau.

### 00:03:53.000 - 00:03:54.000
Khóa kéo.

### 00:03:58.000 - 00:04:00.000
Huy hiệu dấu hoa thị.

### 00:04:04.000 - 00:04:05.000
Điều này có nghĩa là gì?

### 00:04:05.000 - 00:04:06.000
Dấu hoa thị.

### 00:04:06.000 - 00:04:09.000
Những gì chúng ta sẽ làm là giải nén khỏi danh sách.

### 00:04:10.000 - 00:04:12.000
Tất cả các chuyển tiếp.

### 00:04:13.000 - 00:04:18.000
Và điều chúng ta sẽ làm là chọn phần tử đầu tiên trong mỗi phần tử đó.

### 00:04:21.000 - 00:04:28.000
Và nhóm chúng lại với nhau, sau đó nó sẽ lấy phần tử thứ hai từ mỗi danh sách và nhóm chúng lại

### 00:04:28.000 - 00:04:28.000
cùng nhau.

### 00:04:28.000 - 00:04:30.000
Sau đó là thứ ba.

### 00:04:30.000 - 00:04:32.000
Và cuối cùng, thứ tư.

### 00:04:33.000 - 00:04:40.000
Nghĩa là, nó sẽ nhóm các yếu tố của từng quá trình chuyển đổi theo cách mà chúng ta quan tâm và nó sẽ

### 00:04:40.000 - 00:04:43.000
lưu lại chúng trong biến hàng loạt.

### 00:04:43.000 - 00:04:50.000
Sau khi hoàn thành việc này, chúng ta sẽ chuyển đổi từng phần tử trong số các phần tử này thành một tenxơ pytorch.

### 00:04:52.000 - 00:04:55.000
Để nó có thể hoạt động với mạng lưới thần kinh của chúng ta.

### 00:04:57.000 - 00:04:59.000
Hãy viết sự trở lại.

### 00:05:02.000 - 00:05:08.000
Và chúng tôi sẽ lưu trữ từng phần tử được chuyển đổi thành tenxơ pytorch trong danh sách này.

### 00:05:09.000 - 00:05:11.000
Đầu tiên, chúng ta sẽ tạo nó dưới dạng một danh sách trống.

### 00:05:13.000 - 00:05:15.000
Và sau đó chúng ta sẽ lặp lại.

### 00:05:16.000 - 00:05:18.000
Trên các mục trong lô.

### 00:05:18.000 - 00:05:24.000
Đó là lần đầu tiên chúng tôi thực thi các mục trong vòng lặp for sẽ là các Bang.

### 00:05:26.000 - 00:05:33.000
Lần tiếp theo sẽ là hành động, sau đó là phần thưởng và cuối cùng là giai đoạn tiếp theo.

### 00:05:33.000 - 00:05:40.000
Và những gì chúng ta sẽ làm với mỗi đợt này là áp dụng chức năng con mèo chấm đuốc.

### 00:05:44.000 - 00:05:49.000
Nhân tiện, bạn nên tra cứu hàm này trong tài liệu.

### 00:05:51.000 - 00:05:53.000
Những gì chúng ta sẽ làm là nối.

### 00:05:54.000 - 00:05:57.000
Mỗi phần tử này nằm trong một tensor duy nhất.

### 00:06:00.000 - 00:06:05.000
Và tensor đầu ra sẽ có kích thước n lần d.

### 00:06:06.000 - 00:06:13.000
Tức là nó sẽ có n hàng trong đó n là số phần tử trong batch.

### 00:06:14.000 - 00:06:18.000
Và bạn sẽ là số chiều của phần tử đó.

### 00:06:18.000 - 00:06:20.000
Ví dụ.

### 00:06:20.000 - 00:06:22.000
Trong trường hợp của các bang.

### 00:06:23.000 - 00:06:31.000
Giả sử chúng ta có 32 phần tử trong lô, nó sẽ có thứ nguyên 32 nhân hai vì

### 00:06:31.000 - 00:06:34.000
trạng thái có hai chiều.

### 00:06:34.000 - 00:06:34.000
Được rồi.

### 00:06:34.000 - 00:06:38.000
Và thế là chúng ta đã hoàn thành phương pháp mẫu.

### 00:06:38.000 - 00:06:45.000
Bây giờ tất cả những gì chúng ta phải làm là xác định hàm cuối cùng sẽ cho chúng ta biết bộ nhớ có bao nhiêu phần tử.

### 00:06:47.000 - 00:06:49.000
Chúng tôi định nghĩa hàm này là Len.

### 00:06:53.000 - 00:06:54.000
Và nó sẽ trở lại.

### 00:06:56.000 - 00:06:58.000
Kích thước của bộ nhớ của chúng tôi.

### 00:06:59.000 - 00:07:03.000
Đó là biến nơi chúng tôi lưu trữ các chuyển đổi.

### 00:07:05.000 - 00:07:08.000
Và cuối cùng chúng ta đã hoàn thành việc triển khai bộ nhớ.

### 00:07:09.000 - 00:07:13.000
Trong video tiếp theo, chúng ta sẽ bắt đầu làm việc với thuật toán.

### 00:07:13.000 - 00:07:14.000
Tôi sẽ gặp bạn ở đó.

