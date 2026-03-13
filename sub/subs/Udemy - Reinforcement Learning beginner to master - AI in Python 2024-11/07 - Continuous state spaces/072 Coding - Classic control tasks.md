## Nội dung

### 00:00:00.000 - 00:00:06.000
Video này sẽ giới thiệu ngắn gọn về một số nhiệm vụ điều khiển mà chúng ta sắp giải quyết

### 00:00:06.000 - 00:00:07.000
trong suốt khóa học.

### 00:00:07.000 - 00:00:15.000
Những nhiệm vụ này đi kèm với thư viện phòng tập thể dục và chúng là những nhiệm vụ kiểm soát cổ điển được sử dụng liên tục

### 00:00:15.000 - 00:00:17.000
trong nghiên cứu học tập tăng cường.

### 00:00:18.000 - 00:00:25.000
Chúng được sử dụng chính xác vì chúng đơn giản để hiểu các nhiệm vụ mà các nhà nghiên cứu sử dụng để trình bày

### 00:00:25.000 - 00:00:28.000
các thuật toán mới hoặc cải tiến trên các thuật toán hiện có.

### 00:00:33.000 - 00:00:34.000
Trước bất cứ điều gì khác.

### 00:00:34.000 - 00:00:40.000
Chúng tôi sẽ nhập các thư viện mã mà chúng tôi sẽ sử dụng, chúng hoàn toàn giống với

### 00:00:40.000 - 00:00:42.000
những cái chúng tôi đã sử dụng trong sổ ghi chép trước đây.

### 00:00:45.000 - 00:00:52.000
Chúng ta sẽ sử dụng một hàm gọi là test env, chức năng này sẽ cho phép chúng ta kiểm tra một tác nhân ngẫu nhiên đối với từng tác nhân.

### 00:00:53.000 - 00:00:54.000
của các môi trường này.

### 00:00:58.000 - 00:01:00.000
Hãy nhấn shift và nhập.

### 00:01:01.000 - 00:01:04.000
Và bây giờ chúng tôi có sẵn chức năng của chúng tôi.

### 00:01:04.000 - 00:01:11.000
Nhiệm vụ điều khiển đầu tiên mà chúng ta sắp giải quyết có tên là Cartpole và nó bao gồm một chiếc xe đẩy nhỏ.

### 00:01:11.000 - 00:01:16.000
sẽ chuyển động theo trục ngang và sẽ cân bằng một cột thẳng đứng.

### 00:01:16.000 - 00:01:24.000
Mục tiêu của nhiệm vụ này là di chuyển xe dọc theo trục ngang để giữ thăng bằng cho cột

### 00:01:25.000 - 00:01:28.000
vì cột sẽ có xu hướng đổ sang hai bên.

### 00:01:28.000 - 00:01:31.000
Và bằng cách di chuyển chiếc xe, chúng ta sẽ cố gắng giữ cho nó thẳng hàng.

### 00:01:31.000 - 00:01:35.000
Nhưng hãy chạy ô này và xem nó một cách thực tế.

### 00:01:39.000 - 00:01:41.000
Đây là tấm thẻ mà tôi đã nói với bạn.

### 00:01:41.000 - 00:01:43.000
Và đây là cái cột.

### 00:01:43.000 - 00:01:51.000
Như bạn có thể thấy ở đầu tập phim, nó đi thẳng nhưng chậm do lực của

### 00:01:51.000 - 00:01:54.000
trọng lực, cây cột đã rơi sang một bên.

### 00:01:54.000 - 00:02:01.000
Và vì chúng tôi sử dụng tác nhân ngẫu nhiên nên ngay khi cột đi qua, góc tối đa cho phép.

### 00:02:01.000 - 00:02:03.000
Nhiệm vụ đã kết thúc.

### 00:02:03.000 - 00:02:07.000
Hãy thực hiện nó một vài lần nữa để bạn thấy rõ nó hoạt động như thế nào.

### 00:02:07.000 - 00:02:08.000
Nhìn thấy?

### 00:02:11.000 - 00:02:18.000
Mỗi lần chúng tôi khởi động lại tác vụ, cuộc thăm dò sẽ quay trở lại vị trí ban đầu và tác nhân bắt đầu

### 00:02:18.000 - 00:02:20.000
điều khiển xe đẩy.

### 00:02:22.000 - 00:02:25.000
Trạng thái là một vectơ có bốn giá trị.

### 00:02:28.000 - 00:02:30.000
Đầu tiên trong số đó là vị trí của xe đẩy.

### 00:02:32.000 - 00:02:37.000
Điều đó đi từ -4,8 đến dương 4,8.

### 00:02:39.000 - 00:02:43.000
Giá trị tiếp theo là tốc độ của xe trên trục ngang.

### 00:02:45.000 - 00:02:50.000
Và các giá trị được phép đi từ vô cực âm đến vô cực dương.

### 00:02:51.000 - 00:03:01.000
Giá trị thứ ba là góc của cực tính bằng radian và phạm vi được phép đi từ -0 dấu phẩy 418 cho đến

### 00:03:01.000 - 00:03:04.000
dấu phẩy số 0 dương 418.

### 00:03:05.000 - 00:03:08.000
Và giá trị cuối cùng là vận tốc góc của cực.

### 00:03:08.000 - 00:03:13.000
Đó là tốc độ mà cột rơi xuống và bóng được phép.

### 00:03:13.000 - 00:03:16.000
Đi từ vô cực âm đến vô cực dương.

### 00:03:21.000 - 00:03:24.000
Trên thực tế, nếu chúng ta thực thi ô này, chúng ta sẽ thấy.

### 00:03:26.000 - 00:03:28.000
Là một thể hiện của lớp hộp.

### 00:03:28.000 - 00:03:31.000
Tức là nó sẽ có bốn giá trị liên tục.

### 00:03:32.000 - 00:03:36.000
Với những cái ở đây là giá trị tối thiểu.

### 00:03:37.000 - 00:03:41.000
Và cái này có giá trị tối đa.

### 00:03:42.000 - 00:03:48.000
Và điều này cho chúng ta biết là chúng ta có một trạng thái có bốn phần tử trong đó phạm vi tối đa bắt đầu từ

### 00:03:48.000 - 00:03:51.000
vô cực âm đến vô cực dương.

### 00:03:52.000 - 00:03:58.000
Và như bạn thấy trong nhiệm vụ này, có hai hành động đẩy xe sang trái hoặc đẩy xe sang phải.

### 00:04:01.000 - 00:04:02.000
Hãy thực thi ô này.

### 00:04:05.000 - 00:04:09.000
Và như chúng tôi mong đợi, chúng tôi có một không gian hành động riêng biệt.

### 00:04:11.000 - 00:04:14.000
Với hai giá trị có thể là 0 và 1.

### 00:04:16.000 - 00:04:18.000
Bây giờ hãy xem nhiệm vụ điều khiển tiếp theo.

### 00:04:18.000 - 00:04:22.000
Trong trường hợp này, chúng ta đang nói về môi trường acrobat.

### 00:04:22.000 - 00:04:29.000
Về cơ bản nó là một con lắc đôi trong đó tác nhân phải di chuyển các khớp của con lắc đó.

### 00:04:29.000 - 00:04:36.000
Và mục đích là làm cho đầu con lắc chạm vào thanh ngang phía trên nó.

### 00:04:37.000 - 00:04:40.000
Hãy chạm vào môi trường một vài lần và xem tôi đang nói về điều gì.

### 00:04:43.000 - 00:04:45.000
Hãy xem, đây là con lắc đôi.

### 00:04:45.000 - 00:04:51.000
Và mục tiêu là tác nhân di chuyển nó sao cho đầu chạm vào thanh này.

### 00:04:53.000 - 00:04:57.000
Càng chạm vào thanh sớm thì tập phim sẽ kết thúc càng sớm.

### 00:04:58.000 - 00:05:03.000
Và lợi nhuận mà đại lý nhận được càng cao.

### 00:05:03.000 - 00:05:09.000
Bởi vì tại mỗi thời điểm, khi nhiệm vụ chưa hoàn thành, tác nhân sẽ nhận được thông báo tiêu cực

### 00:05:09.000 - 00:05:10.000
phần thưởng.

### 00:05:10.000 - 00:05:14.000
Nhân tiện, trong nhiệm vụ Cartpole, nó hoạt động hoàn toàn ngược lại với nhiệm vụ này.

### 00:05:14.000 - 00:05:21.000
Chúng ta giữ cột thẳng đứng càng lâu thì phần thưởng tích cực sẽ thu được càng nhiều.

### 00:05:21.000 - 00:05:25.000
Bởi vì cứ mỗi thời điểm cột thẳng đứng, chúng ta sẽ nhận được phần thưởng tích cực.

### 00:05:31.000 - 00:05:34.000
Như tôi đã nói, trong trường hợp này thì ngược lại.

### 00:05:34.000 - 00:05:36.000
Chúng tôi muốn chạm vào thanh càng sớm càng tốt.

### 00:05:38.000 - 00:05:42.000
Trong trường hợp này, trạng thái có sáu giá trị.

### 00:05:42.000 - 00:05:48.000
Hai giá trị đầu tiên là sin và cosin của góc của khớp này.

### 00:05:48.000 - 00:05:55.000
Giá trị thứ ba và thứ tư trong trạng thái là sin và cosin của khớp ở đây.

### 00:05:55.000 - 00:05:59.000
Và hai giá trị cuối cùng là tốc độ góc của các khớp đó.

### 00:06:01.000 - 00:06:04.000
Hãy thực hiện ô này để thấy nó rõ ràng hơn một chút.

### 00:06:07.000 - 00:06:11.000
Như bạn có thể thấy, không gian trạng thái cho chúng ta biết rằng chúng ta đang xử lý một môi trường.

### 00:06:13.000 - 00:06:16.000
Trường hợp trạng thái có sáu giá trị.

### 00:06:17.000 - 00:06:23.000
Và giá trị thấp nhất mà chúng ta quan sát được là -28, dấu phẩy 27.

### 00:06:23.000 - 00:06:27.000
Và giá trị cao nhất mà chúng ta sẽ thấy là dương.

### 00:06:27.000 - 00:06:29.000
28, dấu phẩy 27.

### 00:06:31.000 - 00:06:34.000
Bây giờ hãy xem các hành động có sẵn.

### 00:06:34.000 - 00:06:37.000
Mặc dù ở đây có vẻ như chúng ta đã mắc sai lầm.

### 00:06:37.000 - 00:06:40.000
Có ba hành động.

### 00:06:42.000 - 00:06:44.000
Đầu tiên là di chuyển các khớp sang bên phải.

### 00:06:48.000 - 00:06:51.000
Thứ ba là di chuyển các khớp sang trái.

### 00:06:55.000 - 00:06:59.000
Và điều thứ hai là không áp dụng bất kỳ lực nào cả.

### 00:07:09.000 - 00:07:10.000
Hãy thực thi ô này.

### 00:07:10.000 - 00:07:16.000
Và chúng ta có nó ở đây, một không gian hành động riêng biệt với ba hành động.

### 00:07:19.000 - 00:07:22.000
Nhiệm vụ tiếp theo mà chúng ta sắp xem là ô tô leo núi.

### 00:07:22.000 - 00:07:25.000
Chúng ta sẽ thực thi ô này.

### 00:07:25.000 - 00:07:28.000
Và sau đó, tôi sẽ giải thích cho bạn cách thực hiện nhiệm vụ này.

### 00:07:38.000 - 00:07:39.000
Hãy chạy nó một lần nữa.

### 00:07:42.000 - 00:07:49.000
Và như bạn có thể thấy trong nhiệm vụ này, chúng tôi điều khiển một chiếc ô tô bị mắc kẹt giữa hai thung lũng, và nó có

### 00:07:49.000 - 00:07:55.000
đu lên các sườn dốc ở hai bên để lấy đủ động lượng đẩy mình lên núi tới vị trí của nó

### 00:07:55.000 - 00:08:02.000
sang phải và chạm tới lá cờ, đó là mục tiêu tại mọi thời điểm mà ô tô không chạm vào

### 00:08:02.000 - 00:08:09.000
cờ, nó sẽ nhận được phần thưởng âm và chỉ khi đến được cờ, tập phim mới

### 00:08:09.000 - 00:08:10.000
hoàn thành.

### 00:08:10.000 - 00:08:19.000
Như bạn thấy, tác nhân ngẫu nhiên không đạt được kết quả tốt vì chúng ta cần thực hiện các hành động mạch lạc để

### 00:08:19.000 - 00:08:23.000
rằng chiếc xe có thể leo núi bằng cách di chuyển qua lại.

### 00:08:26.000 - 00:08:29.000
Không gian trạng thái bao gồm hai phần tử.

### 00:08:32.000 - 00:08:33.000
Hai giá trị.

### 00:08:35.000 - 00:08:38.000
Có giá trị tối thiểu là -1,2.

### 00:08:40.000 - 00:08:43.000
Và giá trị tối đa của nó là 0,6.

### 00:08:45.000 - 00:08:50.000
Và giá trị đầu tiên tương ứng với vị trí của ô tô trên trục hoành.

### 00:08:51.000 - 00:09:02.000
Giá trị thứ hai là vận tốc của ô tô, có thể lấy các giá trị từ -0 dấu phẩy không bảy cho đến dương

### 00:09:02.000 - 00:09:04.000
0,07.

### 00:09:04.000 - 00:09:07.000
Và ở đây chúng ta có ba hành động có thể thực hiện được.

### 00:09:07.000 - 00:09:11.000
Đầu tiên là tăng tốc sang trái.

### 00:09:11.000 - 00:09:14.000
Điều thứ hai là không tăng tốc chút nào.

### 00:09:14.000 - 00:09:16.000
Và thứ ba là tăng tốc về bên phải.

### 00:09:17.000 - 00:09:24.000
Chúng ta hãy thực thi ô với không gian hành động và như chúng ta mong đợi, chúng ta có được một không gian hành động rời rạc với

### 00:09:24.000 - 00:09:25.000
ba hành động.

### 00:09:28.000 - 00:09:34.000
Và nhiệm vụ cuối cùng mà chúng ta sắp xem là nhiệm vụ duy nhất có các hành động liên tục.

### 00:09:34.000 - 00:09:36.000
Chúng ta đang nói về con lắc.

### 00:09:37.000 - 00:09:38.000
Hãy chạy tế bào.

### 00:09:48.000 - 00:09:56.000
Như bạn có thể thấy, chúng ta có một con lắc ngược và mục tiêu của tác nhân là giữ cho con lắc đứng thẳng

### 00:09:56.000 - 00:09:58.000
càng lâu càng tốt.

### 00:09:58.000 - 00:10:05.000
Và để làm được điều đó, nó phải tác dụng một lực nhất định để quay con lắc sang trái hoặc sang phải.

### 00:10:07.000 - 00:10:13.000
Tác nhân có khả năng duy trì cột thẳng đứng càng lâu thì lợi nhuận sẽ càng cao

### 00:10:13.000 - 00:10:14.000
mà nó có được.

### 00:10:16.000 - 00:10:20.000
Như bạn có thể thấy, không gian trạng thái bao gồm ba giá trị.

### 00:10:20.000 - 00:10:25.000
Đầu tiên là cosin của góc của con lắc.

### 00:10:25.000 - 00:10:28.000
Cái thứ hai là sin góc của con lắc.

### 00:10:28.000 - 00:10:30.000
Và thứ ba, vận tốc của nó.

### 00:10:32.000 - 00:10:40.000
Và không gian hành động là một giá trị có thể nằm giữa hai âm và hai dương.

### 00:10:43.000 - 00:10:45.000
Như bạn có thể thấy, đó là một giá trị liên tục.

### 00:10:46.000 - 00:10:50.000
Và điều mà tác nhân phải quyết định là lực tác dụng lên con lắc là bao nhiêu.

