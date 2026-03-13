# MDP Trong Code - Phần 1

## Nội dung

### 00:00:00 - 00:00:03
Trong video này, chúng ta sẽ thực hiện bài tập lập trình đầu tiên của khóa học.

### 00:00:07 - 00:00:13
Để làm điều đó, chúng ta sẽ mở notebook 'MDP_introduction' mà bạn có trong thư mục mà bạn đã tải xuống

### 00:00:13 - 00:00:14
Từ GitHub.

### 00:00:16 - 00:00:22
Trong notebook này, chúng ta sẽ thấy một cách thực tế các khái niệm mà chúng ta học về Quá trình quyết định Markov.

### 00:00:22 - 00:00:28
Chúng ta sẽ thấy trong thực tế một tác tử thực hiện các hành động trong một nhiệm vụ điều khiển như thế nào,

### 00:00:29 - 00:00:36
Nó nhận phần thưởng dựa trên các hành động mà nó thực hiện, cách tính lợi nhuận, v.v.

### 00:00:36 - 00:00:36
Và cứ tiếp tục như vậy.

### 00:00:40 - 00:00:46
Để làm điều đó, điều đầu tiên chúng ta cần là thư viện gym, sẽ cung cấp cho chúng ta giao diện để điều khiển

### 00:00:46 - 00:00:52
Các nhiệm vụ mà chúng ta muốn giải quyết. Thư viện gym chứa một số lượng lớn các nhiệm vụ điều khiển được định sẵn,

### 00:00:53 - 00:00:58
Nhưng nó cũng cho phép chúng ta triển khai các nhiệm vụ của riêng mình để giải quyết chúng bằng các thuật toán của mình.

### 01:01:00 - 00:01:08
Chúng ta đã tạo một nhiệm vụ có tên Maze mà chúng ta lưu trong một trong các tệp cục bộ mà bạn đã tải xuống từ GitHub.

### 01:13:00 - 00:01:21
Nhiệm vụ điều khiển này biểu diễn một mê cung năm trên năm ô trong đó tác tử phải tìm lối ra,

### 01:22:00 - 00:01:26
Và đây là nhiệm vụ mà chúng ta sẽ sử dụng để giới thiệu các thuật toán học tập củng cố cơ bản.

### 01:27:00 - 00:01:32
Nhưng điều đầu tiên chúng ta sẽ làm là chạy ô này để có mã sẵn sàng.

### 01:33:00 - 00:01:36
Chúng ta nhấn shift+enter để chạy ô.

### 01:39:00 - 00:01:45
Được rồi, bây giờ chúng ta có mã sẵn sàng. Bây giờ chúng ta sẽ làm một giới thiệu nhỏ về thư viện gym.

### 01:48:00 - 00:01:52
Thư viện này, như tôi đã nói trước đây, chứa một số lượng lớn các nhiệm vụ được định sẵn.

### 01:54:00 - 00:01:56
Và cũng cho phép chúng ta tạo các nhiệm vụ của riêng mình.

### 02:00:00 - 00:02:05
Trong số các nhiệm vụ mà nó có, nó chứa các nhiệm vụ điều khiển cổ điển, là những nhiệm vụ thường được nghiên cứu

### 02:05:00 - 00:02:08
Khi một thuật toán mới được giới thiệu.

### 02:09:00 - 00:02:15
Một số ví dụ là nhiệm vụ CartPole, con lắc và xe leo núi.

### 02:19:00 - 00:02:26
Chúng ta sẽ giải quyết các nhiệm vụ này trong phần thứ hai của khóa học với các thuật toán khác. Ngoài ra, nó chứa

### 02:26:00 - 00:02:33
Các nhiệm vụ điều khiển dựa trên trò chơi điện tử, tức là các nhiệm vụ trong đó thuật toán của chúng ta sẽ đối mặt với một trò chơi điện tử

### 02:33:00 - 00:02:35
Sử dụng các nút của bộ điều khiển.

### 02:36:00 - 00:02:42
Những trò chơi điện tử này thuộc nền tảng Atari 2600, và là những trò chơi điện tử cổ điển như

### 02:42:00 - 00:02:46
Space Invaders, Breakout, Pong, v.v.

### 02:47:00 - 00:02:50
Và như các nhiệm vụ này, thư viện gym cung cấp cho chúng ta nhiều hơn nữa.

### 02:54:00 - 00:02:58
Điều tiếp theo chúng ta sẽ làm là xem trong thực tế sơ đồ này hoạt động như thế nào.

### 03:00:00 - 00:03:06
Chúng ta sẽ làm điều đó bằng cách tạo một môi trường sử dụng thư viện gym và tương tác với nó. Cụ thể

### 03:06:00 - 00:03:08
Chúng ta sẽ tạo một thể hiện của nhiệm vụ,

### 03:13:00 - 00:03:19
Mà nhớ rằng, được lưu trong tệp cục bộ 'envs.py'. Chúng ta sẽ thực thi ô này và chúng ta sẽ lưu trữ nó

### 03:19:00 - 00:03:26
Trong biến env, sẽ chứa nhiệm vụ mà chúng ta sẽ tương tác. Đối tượng env này sẽ cung cấp cho chúng ta tất cả

### 03:26:00 - 00:03:32
Chức năng mà chúng ta cần để triển khai tương tác được biểu diễn trong sơ đồ này.

### 03:33:00 - 00:03:40
Ví dụ, nó chứa một hàm gọi là reset, chuẩn bị nhiệm vụ để tác tử có thể tương tác

### 03:40:00 - 00:03:43
Với nó trong một đợt.

### 03:49:00 - 00:03:55
Hãy chạy ô này bằng shift và enter, và chúng ta có nó rồi. Chúng ta đã gọi phương thức reset trên

### 03:55:00 - 00:03:58
Đối tượng bao bọc nhiệm vụ.

### 04:00:00 - 00:04:06
Và điều xảy ra là đối tượng đã cung cấp cho chúng ta quan sát ban đầu về trạng thái của nhiệm vụ đó.

### 04:07:00 - 00:04:14
Trạng thái ban đầu, như bạn có thể thấy, sẽ là (0, 0). Khi chúng ta bắt đầu nhiệm vụ điều khiển, tác tử

### 04:14:00 - 00:04:17
Đang ở hàng 0 và cột 0.

### 04:19:00 - 00:04:21
Bây giờ chúng ta sẽ nhìn thấy trạng thái một cách trực quan

### 04:21:00 - 00:04:24
Và để làm điều đó, chúng ta cần phương thức render của đối tượng này.

### 04:29:00 - 00:04:35
Hãy chạy ô này và đây nó là, như bạn có thể thấy, tác tử đang ở góc trên bên trái

### 04:37:00 - 00:04:40
Và mục tiêu ở góc dưới bên phải.

### 04:42:00 - 00:04:48
Vì tác tử đang ở hàng 0 và cột 0, trạng thái của nó sẽ là (0, 0).

### 04:50:00 - 00:04:57
Để hiển thị hình ảnh này trong notebook, những gì chúng ta đã làm là trước tiên gọi phương thức render của đối tượng này

### 04:57:00 - 00:05:04
Bao bọc môi trường và đã cung cấp cho chúng ta một hình ảnh, một khung hình.

### 05:05:00 - 00:05:12
Và sau đó chúng ta đã sử dụng thư viện Matplotlib để hiển thị dưới dạng hình ảnh khung hình mà phương thức render đã cung cấp cho chúng ta.

### 05:17:00 - 00:05:19
Vì vậy, chúng ta đã bắt đầu nhiệm vụ điều khiển.

### 05:20:00 - 00:05:26
Bây giờ chúng ta cần một cách để tương tác với môi trường, một cách để chọn hành động và thông báo cho môi trường,

### 05:26:00 - 00:05:28
Hành động nào đã được thực hiện.

### 05:28:00 - 00:05:32
Để làm điều đó, thư viện gym cung cấp cho chúng ta một phương thức khác gọi là step.

### 05:35:00 - 00:05:43
Phương thức này lấy đầu vào là một hành động và trả về bốn thứ: thứ đầu tiên mà nó trả về là

### 05:43:00 - 00:05:46
Quan sát tiếp theo về trạng thái của nhiệm vụ.

### 05:47:00 - 00:05:52
Thứ hai là phần thưởng mà tác tử nhận được để thực hiện hành động đó.

### 05:54:00 - 00:06:01
Thứ ba mà chúng ta nhận được là một giá trị boolean đúng hoặc sai, và giá trị này cho chúng ta biết liệu

### 06:01:00 - 00:06:09
Nhiệm vụ đã kết thúc và do đó cần được khởi động lại hay chưa. Nếu nó chưa

### 06:09:00 - 00:06:11
Kết thúc, chúng ta sẽ phải tiếp tục thực hiện các hành động.

### 06:12:00 - 00:06:16
Và thứ cuối cùng mà nó trả về là một từ điển Python với thông tin bổ sung.

### 06:17:00 - 00:06:21
Nếu nhiệm vụ không cần cung cấp bất kỳ thông tin bổ sung nào, từ điển này sẽ trống.

### 06:23:00 - 00:06:27
Nếu không, nó sẽ chứa các cặp khóa-giá trị với thông tin bổ sung đó.

### 06:28:00 - 00:06:32
Trong trường hợp của chúng ta, nó sẽ luôn là một từ điển trống mà chúng ta không cần cho bất cứ điều gì.

### 06:37:00 - 00:06:42
Một điều nữa, hành động mà chúng ta truyền cho môi trường sẽ luôn là một số nguyên, và

### 06:42:00 - 00:06:46
Số nguyên đó là nhãn được liên kết với hành động mà chúng ta đã thực hiện.

### 06:47:00 - 00:06:52
Trong trường hợp của Maze, hành động 0 là đi lên.

### 06:52:00 - 00:06:53
Hành động 1 là đi sang phải.

### 06:53:00 - 00:06:58
Hành động 2 là đi xuống và hành động 3 là đi sang trái.

### 07:01:00 - 00:07:06
Hãy chạy ô này. Chúng ta sẽ thực hiện hành động số 2, là di chuyển xuống.

### 07:13:00 - 00:07:18
Sau khi di chuyển xuống một hàng, tác tử ở hàng số 1, cột 0.

### 07:19:00 - 00:07:22
Phần thưởng chúng ta nhận được sẽ là âm một.

### 07:26:00 - 00:07:32
Trong nhiệm vụ này, bất cứ khi nào chúng ta thực hiện một bước đi, phần thưởng sẽ luôn giống nhau: -1.

### 07:34:00 - 00:07:37
Và điều đó sẽ tiếp tục cho đến khi tác tử tìm thấy lối ra.

### 07:39:00 - 00:07:44
Rõ ràng, tác tử sẽ quan tâm đến việc nhận càng ít phần thưởng âm càng tốt.

### 07:45:00 - 00:07:48
Vì vậy, nó có động lực tìm mục tiêu càng sớm càng tốt.

### 07:52:00 - 00:08:01
Hãy tiếp tục. Sau khi thực hiện bước đi đó, tác tử chưa đạt được mục tiêu, do đó nó chưa kết thúc

### 08:01:00 - 00:08:01
Nhiệm vụ điều khiển.

### 08:03:00 - 00:08:11
Dòng này là nơi bạn có thể thấy cách chúng ta thực hiện hành động. Chúng ta gọi phương thức step, cho nó hành động

### 08:11:00 - 00:08:18
Làm đầu vào và chúng ta nhận được bốn giá trị, trạng thái tiếp theo, phần thưởng, biến boolean cho biết nếu

### 08:18:00 - 00:08:21
Chúng ta đã hoàn thành hay chưa, và từ điển với thông tin bổ sung.

### 08:22:00 - 00:08:30
Bây giờ chúng ta sẽ nhìn thấy một cách trực quan, trạng thái tiếp theo đạt được sau khi thực hiện hành động. Chúng ta nhấn shift

### 08:30:00 - 00:08:30
Và enter.

### 08:31:00 - 00:08:32
Và đây nó là.

### 08:33:00 - 00:08:41
Như tôi đã nói, tác tử đang ở hàng số 1 (đánh số từ 0) và cột 0.

### 08:42:00 - 00:08:47
Bây giờ, hãy xem một phương thức khác mà chúng ta có thể sử dụng để đóng môi trường khi chúng ta hoàn thành tương tác

### 08:47:00 - 00:08:48
Với nó.

### 08:49:00 - 00:08:50
Chúng ta đang nói về phương thức close.

### 08:54:00 - 00:08:59
Hãy chạy ô này và chúng ta đã đóng nhiệm vụ điều khiển.

### 09:02:00 - 00:09:07
Điều này đặc biệt hữu ích cho các nhiệm vụ điều khiển tiêu tốn nhiều tài nguyên, và bằng cách đóng nó,

### 09:08:00 - 00:09:10
Chúng ta giải phóng các tài nguyên đó.

### 09:13:00 - 00:09:20
Được rồi, bây giờ chúng ta có một ý tưởng chung về cách làm việc với bất kỳ nhiệm vụ điều khiển nào. Bất kể nhiệm vụ điều khiển là gì,

### 09:22:00 - 00:09:24
Chúng ta sẽ luôn sử dụng các phương thức giống nhau.

### 09:27:00 - 00:09:32
Bây giờ chúng ta sẽ thấy trong thực tế các khái niệm mà chúng ta đã thấy trong lý thuyết thông qua nhiệm vụ điều khiển Maze.

### 09:32:00 - 00:09:32
Nhiệm vụ.

### 09:36:00 - 00:09:44
Chúng ta sẽ sử dụng nhiệm vụ này trong các bài học về lập trình động, phương pháp Monte Carlo và

### 09:44:00 - 00:09:50
Các phương pháp Chênh lệch Thời gian, và đây là một môi trường tuyệt vời để học các thuật toán đó vì nó có ít trạng thái,

### 09:50:00 - 00:09:52
5 hàng và 5 cột.

### 09:52:00 - 00:09:55
Tức là 25 trạng thái có thể có.

### 09:56:00 - 00:10:01
Và bởi vì khi chúng ta thực hiện một hành động, chúng ta biết chính xác kết quả sẽ như thế nào.

### 10:02:00 - 00:10:04
Tức là, các hành động là tất định.

### 10:07:00 - 00:10:13
Ngoài ra, tất cả các phần thưởng đều là -1. Vì những lý do này, rất dễ hiểu cách môi trường hoạt động.

### 10:14:00 - 00:10:18
Bây giờ, hãy xem không gian trạng thái của nhiệm vụ này.

### 10:19:00 - 00:10:24
Hãy chạy ô này bằng cách nhấn shift và enter để tạo một thể hiện mới của nhiệm vụ.

### 10:28:00 - 10:34:00
Như chúng ta đã nói, trạng thái là sự kết hợp của hàng và cột mà tác tử tìm thấy chính nó.

### 10:35:00 - 00:10:39
Và cả hai đều thuộc phạm vi [0, 4]

### 10:39:00 - 00:10:44
Tức là, các giá trị có thể của chúng là 0, 1, 2, 3, 4.

### 10:45:00 - 00:10:51
Do đó, không gian trạng thái sẽ là tất cả các kết hợp hợp lệ cho các giá trị của hàng và cột.

### 10:51:00 - 00:10:54
Và nhiệm vụ này chứa 25 trạng thái khác nhau.

### 10:56:00 - 00:11:03
Thư viện gym lưu trữ không gian trạng thái này trong một biến gọi là observation_space. Tức là, nó chứa

### 11:03:00 - 00:11:08
Một đối tượng mô tả không gian trạng thái của nhiệm vụ mà chúng ta đang xử lý sẽ như thế nào.

### 11:09:00 - 00:11:14
Và đối tượng đó sẽ cung cấp cho chúng ta thông tin hữu ích để biết nên sử dụng thuật toán nào để cố gắng giải quyết

### 11:14:00 - 00:11:14
Nó.

### 11:19:00 - 00:11:26
Hãy chạy ô này bằng cách nhấn control và enter, như bạn có thể thấy, bằng cách gọi reset trên đối tượng môi trường

### 11:26:00 - 00:11:31
Chúng ta nhận được trạng thái ban đầu, là (0, 0).

### 11:37:00 - 00:11:43
Và không gian trạng thái thuộc lớp Multidiscrete. Tôi biết nghe có vẻ hơi phức tạp, nhưng

### 11:43:00 - 00:11:43
Nó không phải.

### 11:44:00 - 00:11:52
Điều đó có nghĩa là nó có hai giá trị, mỗi giá trị có các giá trị hợp lệ, bắt đầu từ 0 đến 5,

### 11:53:00 - 00:11:54
5 không bao gồm.

### 11:54:00 - 00:11:58
Tức là: 0, 1, 2, 3 và 4.

### 12:05:00 - 00:12:08
Bây giờ, hãy xem các hành động hợp lệ là gì.

### 12:13:00 - 00:12:18
Đây là một hướng dẫn nhỏ nơi bạn có thể thấy mỗi hành động có nghĩa gì. Hãy chạy ô này và xem

### 12:18:00 - 00:12:19
Kết quả.

### 12:23:00 - 00:12:29
Nhiệm vụ cũng có một đối tượng khác gọi là action_space, mô tả các hành động mà chúng ta có thể thực hiện

### 12:29:00 - 00:12:31
Để tương tác với môi trường.

### 12:34:00 - 00:12:39
Trong trường hợp này, đó là một không gian hành động rời rạc với bốn hành động có sẵn:

### 12:41:00 - 00:12:46
0, 1, 2 và 3, mỗi hành động có ý nghĩa riêng.

### 12:49:00 - 00:12:56
Và đối tượng đó cũng có một phương thức khác gọi là sample, phương thức này chọn một hành động ngẫu nhiên từ

### 12:56:00 - 00:12:57
Phạm vi hợp lệ.

### 12:58:00 - 00:13:03
Trong video tiếp theo, chúng ta sẽ thấy cách thực hiện các hành động này, để tương tác với nhiệm vụ.
