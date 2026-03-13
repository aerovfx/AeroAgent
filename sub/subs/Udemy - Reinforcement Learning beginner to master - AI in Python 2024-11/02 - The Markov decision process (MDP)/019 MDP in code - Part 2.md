# MDP Trong Code - Phần 2

## Nội dung

### 00:00:00 - 00:00:06
Bây giờ chúng ta đã biết cách thực hiện các hành động trong môi trường, chúng ta đã sẵn sàng tạo quỹ đạo đầu tiên,

### 00:00:08 - 00:00:15
Một quỹ đạo là chuỗi được tạo ra khi chúng ta di chuyển từ một trạng thái sang trạng thái khác bằng cách thực hiện các hành động.

### 00:00:17 - 00:00:20
Chúng ta sẽ tạo một quỹ đạo với ba bước đi.

### 00:00:21 - 00:00:28
Điều đầu tiên chúng ta làm là tạo một đối tượng đại diện cho môi trường, sau đó chúng ta sẽ reset nó và

### 00:00:28 - 00:00:34
Chúng ta sẽ tạo một danh sách nơi chúng ta sẽ lưu trữ tất cả các phần tử được tạo ra sau khi thực hiện các hành động.

### 00:00:35 - 00:00:36
Tức là: quỹ đạo.

### 00:00:41 - 00:00:46
Sau đó chúng ta sẽ lặp ba lần thực hiện một hành động trong môi trường.

### 00:00:47 - 00:00:49
Mà chúng ta sẽ chọn ngẫu nhiên.

### 00:00:50 - 00:00:57
Sau đó chúng ta sẽ lưu trữ trong danh sách đại diện cho quỹ đạo, một mục với các phần tử sau:

### 00:00:58 - 00:01:05
Trạng thái bắt đầu, hành động được thực hiện, phần thưởng thu được sau khi thực hiện hành động, một biến cho biết

### 01:05:00 - 00:01:08
Liệu chúng ta đã hoàn thành đợt hay chưa,

### 01:08:00 - 00:01:11
Và trạng thái tiếp theo đạt được sau khi thực hiện hành động.

### 01:12:00 - 00:01:16
Khi chúng ta hoàn thành việc tạo quỹ đạo, chúng ta sẽ đóng môi trường.

### 01:17:00 - 00:01:20
Hãy nhấn shift+enter để thực thi ô này.

### 01:22:00 - 00:01:24
Và đây nó là, quỹ đạo đầu tiên của bạn.

### 01:26:00 - 00:01:31
Như bạn có thể thấy, vì đó là quỹ đạo 3 bước, chúng ta có ba phần tử trong danh sách.

### 01:38:00 - 00:01:40
Và mỗi mục chứa trạng thái bắt đầu,

### 01:43:00 - 00:01:50
Hành động được thực hiện, phần thưởng thu được, biến cho biết đợt đã kết thúc chưa và trạng thái tiếp theo

### 01:50:00 - 00:01:50
Đạt được.

### 01:51:00 - 00:01:52
Được rồi.

### 01:52:00 - 00:01:57
Bây giờ chúng ta đã có quỹ đạo đầu tiên, hãy tạo đợt đầu tiên của chúng ta.

### 01:59:00 - 00:02:05
Nhưng đợt là gì? Một đợt là một quỹ đạo bắt đầu ở trạng thái ban đầu của nhiệm vụ và

### 02:05:00 - 00:02:14
Kết thúc ở trạng thái kết thúc, trạng thái nơi nhiệm vụ kết thúc, dù là vì chúng ta giải quyết nhiệm vụ đúng cách

### 02:14:00 - 00:02:20
Hay vì tác tử tìm thấy chính nó trong trạng thái thất bại.

### 02:21:00 - 00:02:24
Vì vậy, bây giờ chúng ta sẽ chạy một vòng lặp rất giống với vòng lặp trước đó.

### 02:25:00 - 00:02:31
Nhưng thay vì chứa ba mục, nó sẽ chứa bao nhiêu mục tùy thuộc vào độ dài của đợt.

### 02:32:00 - 00:02:35
Nó sẽ chạy miễn là đợt chưa kết thúc.

### 02:38:00 - 00:02:47
Để làm điều đó sẽ tạo một môi trường mới, chúng ta sẽ reset nó, chúng ta sẽ tạo danh sách sẽ lưu trữ các phần tử

### 02:47:00 - 00:02:54
Của đợt, chúng ta sẽ khởi tạo biến done là false vì chúng ta đang ở đầu đợt

### 02:54:00 - 00:02:55
Và do đó nó chưa kết thúc.

### 02:56:00 - 00:03:06
Và điều tiếp theo chúng ta sẽ làm là chọn một hành động ngẫu nhiên và thực hiện nó trong môi trường để lấy trạng thái tiếp theo,

### 03:08:00 - 00:03:11
Phần thưởng và giá trị mới cho done.

### 03:13:00 - 00:03:20
Và sau đó chúng ta sẽ lưu trữ chuyển đổi đó trong danh sách chứa các phần tử của đợt.

### 03:21:00 - 00:03:28
Khi biến done là True, đợt sẽ kết thúc và chúng ta sẽ dừng thực hiện vòng lặp này.

### 03:29:00 - 00:03:31
Hãy chạy ô này bằng cách nhấn shift+enter.

### 03:32:00 - 00:03:34
Và đây bạn có. Bạn đã đối mặt

### 03:34:00 - 00:03:36
Một nhiệm vụ điều khiển lần đầu tiên.

### 03:38:00 - 00:03:46
Mỗi mục trong danh sách này tương ứng với một chuyển đổi trạng thái thuộc về quỹ đạo của đợt này.

### 03:48:00 - 00:03:55
Nếu chúng ta cuộn xuống đến hành động cuối cùng được thực hiện, bạn có thể thấy mục tương ứng với chuyển đổi cuối cùng

### 03:55:00 - 00:03:57
Nơi tác tử tìm thấy mục tiêu.

### 03:58:00 - 00:04:07
Chúng ta ở ô (3, 4), chúng ta đi xuống, và điều đó có nghĩa là chúng ta đã đạt được mục tiêu, nằm ở

### 04:07:00 - 00:04:15
Trạng thái (4, 4), và môi trường cho chúng ta biết rằng bây giờ đợt đã kết thúc, cung cấp cho chúng ta giá trị True

### 04:15:00 - 00:04:17
Cho biến done.

### 04:18:00 - 00:04:20
Như bạn có thể thấy, tất cả phần thưởng đều là -1.

### 04:23:00 - 00:04:28
Bây giờ, hãy sử dụng các quỹ đạo này để xem trong thực tế cách tính lợi nhuận.

### 04:31:00 - 00:04:34
Điều đầu tiên chúng ta sẽ thấy là các phần thưởng cá nhân là gì.

### 04:36:00 - 00:04:38
Hãy thực thi ô này

### 04:40:00 - 00:04:45
Nơi chúng ta đã thực hiện một hành động ngẫu nhiên và chúng ta đã lưu trữ phần thưởng mà chúng ta nhận được.

### 04:47:00 - 00:04:52
Như tôi đã nói, tất cả phần thưởng trong môi trường này sẽ là -1.

### 04:53:00 - 00:04:56
Bất kể hành động nào chúng ta thực hiện cho đến khi kết thúc đợt.

### 04:58:00 - 00:05:02
Hãy nhớ rằng phần thưởng là hiệu ứng tức thì của việc thực hiện một hành động.

### 05:03:00 - 00:05:10
Và ngược lại, lợi nhuận là hiệu ứng dài hạn của các hành động được thực hiện trong một quỹ đạo. Lợi nhuận

### 05:10:00 - 00:05:14
Tại thời điểm 0 là tổng các phần thưởng chiết khấu

### 05:17:00 - 00:05:23
Mà chúng ta nhận được sau khi thực hiện mỗi hành động từ đầu đợt cho đến khi kết thúc.

### 05:25:00 - 00:05:31
Và hãy nhớ rằng chúng ta áp dụng hệ số chiết khấu cho mỗi phần thưởng vì chúng ta muốn nói với

### 05:31:00 - 00:05:36
Tác tử rằng chúng ta thích nhận phần thưởng sớm hơn là muộn.

### 05:38:00 - 00:05:39
Hãy xem nó trong thực tế.

### 05:44:00 - 00:05:50
Trong ô này, chúng ta sẽ tạo một môi trường, như trước đây và chúng ta sẽ khởi tạo nó. Chúng ta cũng sẽ khởi tạo

### 05:50:00 - 00:05:56
Biến done là False và hệ số chiết khấu, gamma là 0,99.

### 05:58:00 - 00:06:06
Hãy khởi tạo lợi nhuận tại t=0 là 0, vì lúc này, chúng ta chưa nhận được bất kỳ

### 06:06:00 - 00:06:14
Phần thưởng nào, dương hoặc âm. Chúng ta cũng sẽ giữ một biến 't' theo dõi thời điểm

### 06:14:00 - 00:06:14
Mà chúng ta đang ở.

### 06:16:00 - 00:06:17
Sau đó chúng ta sẽ vào vòng lặp.

### 06:19:00 - 00:06:23
Sẽ được thực hiện miễn là đợt chưa kết thúc.

### 06:28:00 - 00:06:30
Và trong vòng lặp, chúng ta sẽ chọn một hành động ngẫu nhiên

### 06:31:00 - 00:06:33
Và chúng ta sẽ thực hiện nó trong môi trường.

### 06:37:00 - 00:06:42
Để lấy phần thưởng và giá trị mới cho done

### 06:44:00 - 00:06:48
Bây giờ, chúng ta sẽ cập nhật tổng này với phần thưởng mà chúng ta vừa nhận được.

### 06:50:00 - 00:06:51
Để làm điều đó.

### 06:53:00 - 00:07:00
Chúng ta sẽ lấy giá trị hiện tại của lợi nhuận và chúng ta sẽ cộng với gamma lũy thừa 't' nhân phần thưởng.

### 07:01:00 - 00:07:04
Tại t=0, gamma lũy thừa 't'.

### 07:05:00 - 00:07:07
Sẽ là gamma lũy thừa 0.

### 07:10:00 - 00:07:19
Và vì lý do đó, phần thưởng sẽ không được chiết khấu. Khi t=1, chúng ta sẽ có gamma lũy thừa

### 07:19:00 - 00:07:27
Lũy thừa đầu tiên, là gamma, và do đó chúng ta sẽ có phần thưởng thứ hai chiết khấu bởi gamma.

### 07:30:00 - 00:07:36
Và khi chúng ta tiến qua thời gian, chúng ta sẽ nâng gamma lên lũy thợ cao hơn để chiết khấu nhiều hơn

### 07:36:00 - 00:07:37
Phần thưởng mà chúng ta nhận được.

### 07:41:00 - 00:07:47
Và khi chúng ta hoàn thành việc bước qua vòng lặp, biến G_0 sẽ có giá trị của lợi nhuận

### 07:48:00 - 00:07:50
Và chúng ta sẽ có thể đóng môi trường.

### 07:51:00 - 00:07:52
Hãy thực thi ô.

### 07:52:00 - 00:07:53
Và đây nó là.

### 07:56:00 - 00:08:06
Tác tử đã mất 280 bước, thực hiện các hành động ngẫu nhiên để tìm lối ra, và tổng chiết khấu của

### 08:06:00 - 00:08:10
Phần thưởng nhận được là âm 94.

### 08:14:00 - 00:08:16
Nếu bạn thấy một giá trị khác trong notebook của bạn.

### 08:17:00 - 00:08:24
Đừng lo lắng về điều đó, vì tác tử của bạn đã ngẫu nhiên chọn các hành động khác, có nghĩa là nó sẽ

### 08:24:00 - 00:08:27
Tìm lối ra tại một bước thời gian khác.

### 08:32:00 - 00:08:39
Được rồi, cho đến nay chúng ta đã thấy các trạng thái của nhiệm vụ, các hành động mà chúng ta có thể thực hiện trong đó, các phần thưởng mà

### 08:39:00 - 00:08:42
Chúng ta nhận được như một hậu quả, cách tính lợi nhuận,

### 08:44:00 - 00:08:47
Và chúng ta đã tạo một quỹ đạo và một đợt.

### 08:49:00 - 00:08:53
Bây giờ chúng ta đã sẵn sàng tạo chính sách đầu tiên của mình.

### 08:56:00 - 00:09:02
Hãy nhớ rằng chính sách là một hàm cho chúng ta biết xác suất chọn một hành động trong một trạng thái

### 09:03:00 - 00:09:11
Hoặc hành động được chọn tại trạng thái đó trong tất cả các hành động có thể. Trong trường hợp này, chúng ta sẽ tạo một chính sách

### 09:11:00 - 00:09:14
Sẽ cung cấp cho chúng ta xác suất chọn mỗi hành động.

### 09:15:00 - 00:09:19
Chính sách đó sẽ là một hàm và do đó chúng ta khai báo nó như vậy.

### 09:22:00 - 00:09:29
Và chính sách mà chúng ta sẽ tạo là chính sách dễ nhất mà chúng ta có thể nghĩ đến: một chính sách ngẫu nhiên. Khi

### 09:29:00 - 00:09:33
Chúng ta truyền một trạng thái làm đối số, chính sách sẽ trả về

### 09:33:00 - 00:09:39
Xác suất chọn mỗi hành động trong trạng thái đó, và tất cả các xác suất sẽ giống nhau:

### 09:40:00 - 00:09:41
0,25

### 09:43:00 - 00:09:46
Hãy khai báo chính sách này bằng cách thực thi ô.

### 09:47:00 - 00:09:51
Nhấn shift+enter và bây giờ chúng ta có một chính sách ngẫu nhiên sẵn sàng.

### 09:54:00 - 00:09:59
Và bây giờ với chính sách mới của mình, chúng ta sẽ nhìn thấy một cách trực quan một tác tử sử dụng chính sách đó

### 10:01:00 - 00:10:03
Cố gắng giải quyết môi trường (nhiệm vụ).

### 10:08:00 - 00:10:17
Để làm điều đó, chúng ta tạo một môi trường mới và chúng ta reset nó. Hãy thực thi ô này và tiếp theo chúng ta sẽ

### 10:17:00 - 00:10:22
Biểu diễn bằng đồ thị các xác suất thực hiện mỗi hành động bởi chính sách.

### 10:22:00 - 00:10:30
Hãy thực thi chính sách, là một hàm cung cấp cho nó đầu vào là trạng thái nơi

### 10:30:00 - 00:10:31
Tác tử tìm thấy chính nó.

### 10:34:00 - 00:10:41
Và chúng ta sẽ lấy biến action probabilities với vector chứa xác suất chọn

### 10:41:00 - 00:10:42
Mỗi hành động.

### 10:42:00 - 00:10:46
Và bây giờ hãy vẽ các xác suất đó trên biểu đồ.

### 10:48:00 - 00:10:50
Sử dụng thư viện matplotlib.

### 10:52:00 - 00:10:59
Hãy chạy ô. Vì chúng ta đang sử dụng một chính sách ngẫu nhiên, xác suất chọn

### 10:59:00 - 00:11:03
Mỗi hành động là giống nhau: 0,25.

### 11:05:00 - 00:11:09
Điều cuối cùng chúng ta sẽ làm là sử dụng chính sách này để cố gắng giải quyết nhiệm vụ.

### 11:11:00 - 00:11:21
Để làm điều đó, chúng ta sẽ reset nhiệm vụ điều khiển, chúng ta sẽ đặt biến done là False và chúng ta sẽ vào vòng lặp chính

### 11:21:00 - 00:11:29
Mà chúng ta sẽ thực hiện cho đến khi đợt kết thúc. Trong vòng lặp đó, chúng ta sẽ chọn một hành động ngẫu nhiên sử dụng

### 11:29:00 - 00:11:31
Vector xác suất,

### 11:35:00 - 00:11:38
Chúng ta sẽ thực hiện hành động đó trong môi trường,

### 11:40:00 - 00:11:45
Và sau đó chúng ta sẽ hiển thị trực quan trạng thái của nhiệm vụ sau khi thực hiện hành động đó.

### 11:49:00 - 00:11:53
Hãy nhấn shift+enter, và đây chúng ta có.

### 11:58:00 - 00:12:03
Như bạn biết, chúng ta đang sử dụng một tác tử chọn hành động ngẫu nhiên, vì vậy sẽ còn một lúc cho đến khi

### 12:03:00 - 00:12:04
Nó tìm thấy lối ra.

### 12:11:00 - 00:12:12
Đây bạn có.

### 12:14:00 - 00:12:20
Đây kết thúc liên hệ đầu tiên của chúng ta với mã. Bây giờ bạn đã quen thuộc với giao diện mà thư viện gym

### 12:20:00 - 00:12:28
Cung cấp cho chúng ta để có thể tương tác và giải quyết các nhiệm vụ điều khiển. Chúng ta đã thấy các trạng thái và hành động trông như thế nào

### 12:28:00 - 00:12:33
Và cách sử dụng phương thức step, chúng ta có thể tương tác với môi trường.

### 12:34:00 - 00:12:39
Chúng ta cũng đã thấy cách định nghĩa một chính sách, mặc dù trong trường hợp này chúng ta đã sử dụng chính sách đơn giản nhất,

### 12:41:00 - 00:12:49
Và chúng ta cũng đã thấy cách sử dụng các phần thưởng tức thì theo sau mỗi hành động để tính lợi nhuận,

### 12:50:00 - 00:12:52
Là giá trị mà chúng ta muốn tối đa hóa.

### 12:54:00 - 00:13:00
Và bây giờ chúng ta có tất cả các công cụ cần thiết để xem họ thuật toán đầu tiên mà chúng ta sẽ học trong

### 13:00:00 - 00:13:02
Khóa học này gọi là lập trình động.

### 13:03:00 - 00:13:05
Tôi sẽ gặp bạn trong phần tiếp theo.
