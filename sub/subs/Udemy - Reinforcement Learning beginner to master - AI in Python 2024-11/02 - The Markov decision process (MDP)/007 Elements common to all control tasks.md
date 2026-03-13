# Các Yếu Tố Chung Của Tất Cả Các Nhiệm Vụ Điều Khiển

## Nội dung

### 00:00:00 - 00:00:05
Trong phần này, chúng ta sẽ học các khái niệm cơ bản của học tập củng cố và từ đó,

### 00:00:05 - 00:00:12
Chúng ta sẽ phát triển một mẫu chung cho tất cả các nhiệm vụ điều khiển. Từ mẫu này trong các phần tiếp theo

### 00:00:12 - 00:00:16
Chúng ta sẽ có thể phát triển các phương pháp để giải quyết các nhiệm vụ này.

### 00:00:17 - 00:00:25
Để bắt đầu, chúng ta sẽ xem xét năm yếu tố mà chúng ta thấy trong tất cả các nhiệm vụ điều khiển, và chúng ta

### 00:00:25 - 00:00:30
Sẽ xem chúng thông qua các ví dụ mà chúng ta đã thấy trong phần trước, trò chơi cờ,

### 00:00:30 - 00:00:36
Điều khiển một cánh tay máy móc và điều khiển một nhân vật trò chơi điện tử.

### 00:00:37 - 00:00:42
Cả ba đều là ví dụ về các nhiệm vụ điều khiển trong đó các hành động phù hợp phải được thực hiện tại mỗi thời điểm

### 00:00:42 - 00:00:45
Để giải quyết một nhiệm vụ nhất định.

### 00:00:48 - 00:00:53
Yếu tố đầu tiên chung cho tất cả các nhiệm vụ điều khiển là trạng thái tại thời điểm đó.

### 00:00:55 - 00:01:02
Trạng thái là tất cả thông tin liên quan mô tả tình huống mà môi trường nhiệm vụ hiện đang ở trong.

### 01:02:00 - 00:01:02
Hiện tại.

### 01:03:00 - 00:01:09
Trong trường hợp cờ, trạng thái của trò chơi bao gồm vị trí của các quân cờ trên bàn cờ và

### 01:09:00 - 00:01:10
Thời gian còn lại.

### 01:12:00 - 00:01:18
Trong trường hợp cánh tay robot, trạng thái là vị trí của đối tượng cần thao tác và xoay

### 01:18:00 - 00:01:22
Các khớp của cánh tay. Trong trường hợp trò chơi Pacman.

### 01:23:00 - 00:01:29
Trạng thái là vị trí của nhân vật của chúng ta, vị trí của các viên thuốc màu vàng và vị trí của các bóng ma

### 01:29:00 - 00:01:30
Trong mê cung.

### 01:32:00 - 00:01:40
Trạng thái luôn gắn liền với một thời điểm. Tức là, chúng ta đề cập đến trạng thái tại thời điểm t.

### 01:42:00 - 00:01:48
Yếu tố tiếp theo mà chúng ta thấy trong tất cả các nhiệm vụ điều khiển là các hành động được thực hiện trong nhiệm vụ.

### 01:50:00 - 00:01:56
Các hành động là các nước đi mà người chơi có thể thực hiện tại mỗi thời điểm. Trong trường hợp cánh tay máy

### 01:56:00 - 00:01:57
Cánh tay.

### 01:57:00 - 00:02:04
Các hành động bao gồm việc thay đổi xoay của các khớp để nhặt và di chuyển đối tượng.

### 02:05:00 - 00:02:11
Trong trường hợp Pacman, các hành động bao gồm các nút mà người chơi nhấn trên bộ điều khiển để di chuyển

### 02:11:00 - 00:02:12
Nhân vật.

### 02:13:00 - 00:02:16
Các hành động cũng gắn với một thời điểm.

### 02:17:00 - 00:02:21
Và chúng được chọn dựa trên trạng thái của nhiệm vụ.

### 02:22:00 - 00:02:29
Điều đó có nghĩa là gì, chúng ta có nghĩa là tác quan sát trạng thái và dựa trên các đặc điểm của trạng thái

### 02:29:00 - 00:02:34
Trong đó nhiệm vụ tìm thấy chính nó, nó sẽ thực hiện một số hành động hoặc các hành động khác.

### 02:38:00 - 00:02:45
Thứ ba, khi làm việc với một nhiệm vụ điều khiển, chúng ta cần một cơ chế thông báo cho tác tử về hiệu quả

### 02:45:00 - 00:02:49
Việc ra quyết định của nó. Cơ chế đó là phần thưởng.

### 02:50:00 - 00:02:56
Phần thưởng là một giá trị số mà tác tử nhận được sau khi thực hiện một hành động.

### 02:58:00 - 00:03:04
Và nó xác định hiệu ứng tức thì của việc thực hiện hành động đó. Trong cờ

### 03:04:00 - 00:03:05
Mục tiêu là giành chiến thắng trong trò chơi.

### 03:06:00 - 00:03:13
Do đó, khi người chơi thực hiện một nước đi chiếu tướng đối thủ, nhiệm vụ phải cho nó một

### 03:13:00 - 00:03:13
Phần thưởng dương.

### 03:15:00 - 00:03:22
Khi nó thực hiện một nước đi mà sau đó đối thủ sẽ chiếu tướng nó, nhiệm vụ nên cho nó một

### 03:22:00 - 00:03:22
Phần thưởng âm.

### 03:23:00 - 00:03:27
Và nếu nước đi không kết thúc trò chơi, phần thưởng nên bằng không.

### 03:28:00 - 00:03:34
Trong trường hợp cánh tay robot, phần thưởng nên bằng không cho đến khi robot di chuyển đối tượng

### 03:34:00 - 00:03:42
Đúng cách, và chỉ khi đạt được mục tiêu, nó mới nhận được phần thưởng dương từ môi trường.

### 03:43:00 - 00:03:50
Cuối cùng, trong trò chơi Pacman, mỗi khi tác tử ăn một viên thuốc màu vàng, nó nên được thưởng tích cực.

### 03:50:00 - 00:03:56
Các phần thưởng này là biểu diễn của các mục tiêu nhiệm vụ dưới dạng phản hồi.

### 03:57:00 - 00:04:02
Vì vậy, phần thưởng càng lớn, chúng ta càng đạt được các mục tiêu của nhiệm vụ tốt hơn.

### 04:03:00 - 00:04:10
Yếu tố thứ tư chung cho tất cả các nhiệm vụ điều khiển là tác tử. Tác tử là thực thể sẽ tham gia

### 04:10:00 - 00:04:16
Trong nhiệm vụ bằng cách quan sát trạng thái của nó và thực hiện các hành động tại mỗi thời điểm.

### 04:17:00 - 00:04:24
Trong cả ba trường hợp, tác tử có thể là một con người quan sát trạng thái của nhiệm vụ bằng mắt

### 04:24:00 - 00:04:27
Và thực hiện các hành động cần thiết dựa trên nó.

### 04:27:00 - 00:04:34
Nhưng vì đây là khóa học về học tập củng cố, tác tử của chúng ta sẽ luôn là các thuật toán

### 04:34:00 - 00:04:36
Thực hiện các hành động này.

### 04:37:00 - 00:04:44
Cuối cùng, yếu tố cuối cùng là môi trường, bao gồm tất cả các khía cạnh của nhiệm vụ mà

### 04:44:00 - 00:04:46
Tác tử không kiểm soát 100%.

### 04:47:00 - 00:04:53
Ví dụ, trong trường hợp cờ, thời gian còn lại là một phần của môi trường vì tác tử

### 04:53:00 - 00:04:56
Không thể quyết định tăng nó một cách tùy ý.

### 04:57:00 - 00:05:04
Ngoài ra, các nước đi của đối thủ là một phần của môi trường, vì tác tử không kiểm soát

### 05:05:00 - 00:05:06
Đối thủ của nó thực hiện những nước đi nào.

### 05:08:00 - 00:05:14
Trong trường hợp cánh tay robot, tất cả các khía cạnh vật lý là một phần của môi trường.

### 05:14:00 - 00:05:20
Ví dụ, tác tử không thể thay đổi lực hấp dẫn hay ma sát của các đối tượng.

### 05:22:00 - 00:05:29
Trong trường hợp Pacman, chuyển động của kẻ thù cũng là một phần của môi trường cũng như hình dạng

### 05:29:00 - 00:05:31
Của mê cung và vị trí của các viên thuốc.

### 05:33:00 - 00:05:39
Nếu bạn nghĩ lại về trạng thái của nhiệm vụ, nó có thể được xem là biểu diễn của các khía cạnh

### 05:39:00 - 00:05:42
Của môi trường có liên quan đến việc ra quyết định.
