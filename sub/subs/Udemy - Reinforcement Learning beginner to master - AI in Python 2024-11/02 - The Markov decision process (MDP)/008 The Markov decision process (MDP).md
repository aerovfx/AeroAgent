# Quá Trình Quyết Định Markov (MDP)

## Nội dung

### 00:00:00 - 00:00:05
Trong video này, chúng ta sẽ lấy năm yếu tố mà chúng ta đã thấy trong video trước và sử dụng chúng

### 00:00:05 - 00:00:08
Để tạo một mẫu mô tả tất cả các nhiệm vụ điều khiển.

### 00:00:09 - 00:00:13
Mẫu đó được gọi là Quá trình quyết định Markov.

### 00:00:14 - 00:00:17
Nhưng chính xác Quá trình quyết định Markov là gì?

### 00:00:18 - 00:00:22
Chà, đó là một quá trình điều khiển ngẫu nhiên thời gian rời rạc.

### 00:00:23 - 00:00:29
Nó là một quá trình điều khiển vì nó dựa trên việc ra quyết định để đạt được các mục tiêu của nhiệm vụ.

### 00:00:30 - 00:00:38
Nó là một quá trình ngẫu nhiên vì các hành động của tác tử chỉ ảnh hưởng một phần đến sự phát triển của nhiệm vụ.

### 00:00:40 - 00:00:45
Và cuối cùng, đó là một quá trình thời gian rời rạc vì trong các nhiệm vụ mà chúng ta sẽ biểu diễn bằng mẫu này,

### 00:00:45 - 00:00:49
Thời gian tiến triển trong các khoảng hữu hạn.

### 00:00:49 - 00:00:52
Tức là t=1, t=2, v.v.

### 00:00:54 - 00:00:58
Đây là sơ đồ biểu diễn Quá trình quyết định Markov.

### 01:00:00 - 00:01:04
Trong quá trình này, tác tử tương tác với môi trường.

### 01:05:00 - 00:01:13
Khi bắt đầu nhiệm vụ, tác tử quan sát trạng thái ban đầu của nhiệm vụ và dựa trên nó, nó thực hiện

### 01:13:00 - 00:01:14
Một hành động.

### 01:16:00 - 00:01:21
Hành động này tạo ra một hiệu ứng trên môi trường làm thay đổi trạng thái của nó.

### 01:23:00 - 00:01:30
Kết quả là, tác tử quan sát lại trạng thái mới mà nhiệm vụ tìm thấy chính nó và nhận được một

### 01:30:00 - 00:01:38
Phần thưởng từ môi trường, cung cấp phản hồi về hiệu ứng mà hành động trước đó có trên

### 01:38:00 - 00:01:39
Môi trường.

### 01:40:00 - 00:01:48
Sau đó, dựa trên trạng thái mới, tác tử thực hiện một hành động khác và chu kỳ lặp lại cho đến khi

### 01:48:00 - 00:01:55
Nhiệm vụ kết thúc, hoặc vì tác tử đã đạt được mục tiêu của nhiệm vụ hoặc vì nó đã thất bại vì

### 01:55:00 - 00:01:56
Một lý do nào đó.

### 01:57:00 - 00:02:04
Như bạn có thể thấy, mô hình này gọi là Quá trình quyết định Markov biểu diễn theo cách trừu tượng, hành vi

### 02:04:00 - 00:02:11
Của mọi nhiệm vụ điều khiển mà chúng ta sẽ đối mặt và cho phép chúng ta làm việc sử dụng cùng một mẫu với

### 02:11:00 - 00:02:12
Tất cả chúng.

### 02:13:00 - 00:02:20
Nhờ Quá trình quyết định Markov, chúng ta có thể phân tích các nhiệm vụ rất khác nhau sử dụng cùng các khái niệm.

### 02:21:00 - 00:02:28
Một lợi thế bổ sung là chúng ta có thể mô tả một nhiệm vụ điều khiển một cách rất đơn giản dựa trên bốn

### 02:28:00 - 00:02:29
Đối tượng.

### 02:31:00 - 00:02:38
Đối tượng đầu tiên là không gian trạng thái, bao gồm tất cả các trạng thái có thể có mà nhiệm vụ có thể

### 02:38:00 - 00:02:39
Tìm thấy chính nó.

### 02:40:00 - 00:02:48
Thứ hai là không gian hành động, bao gồm tập hợp tất cả các hành động mà tác tử có thể thực hiện

### 02:48:00 - 00:02:49
Trong môi trường.

### 02:50:00 - 00:02:57
Đối tượng thứ ba là tập hợp tất cả các phần thưởng thu được bằng cách thực hiện mỗi hành động trong mỗi trạng thái.

### 02:58:00 - 00:03:06
Và đối tượng cuối cùng là tập hợp các xác suất chuyển từ một trạng thái sang trạng thái khác bằng cách thực hiện một hành động.

### 03:07:00 - 00:03:13
Nếu chúng ta biết bốn yếu tố này, chúng ta có thể mô tả hoàn hảo một nhiệm vụ điều khiển.

### 03:14:00 - 00:03:22
Và chúng ta có thể sử dụng cùng cấu trúc để phân tích các nhiệm vụ khác nhau đơn giản bằng cách thay đổi nội dung của mỗi

### 03:23:00 - 00:03:24
Yếu tố này.

### 03:25:00 - 00:03:32
Để đưa ra một ví dụ, trong trò chơi cờ, không gian trạng thái bao gồm tất cả các cấu hình hợp lệ

### 03:32:00 - 00:03:36
Của bàn cờ và tất cả các giá trị có thể cho thời gian còn lại.

### 03:37:00 - 00:03:43
Không gian hành động bao gồm tất cả các nước đi hợp lệ trong mỗi trạng thái của bàn cờ.

### 03:45:00 - 00:03:53
Tập hợp các phần thưởng bao gồm các phần thưởng thu được bằng cách thực hiện mỗi hành động trong một trạng thái hợp lệ, và cuối cùng,

### 03:53:00 - 00:04:00
Tập hợp các chuyển đổi bao gồm các xác suất đạt được mỗi trạng thái kế thừa bằng cách di chuyển một

### 04:00:00 - 00:04:01
Quân cờ.

### 04:03:00 - 00:04:10
Các Quá trình quyết định Markov này có một thuộc tính quan trọng, và thuộc tính đó là trạng thái tiếp theo

### 04:10:00 - 00:04:10
Được thăm

### 04:10:00 - 00:04:15
Chỉ phụ thuộc vào trạng thái hiện tại và không phụ thuộc vào các trạng thái trước đó.

### 04:16:00 - 00:04:17
Đó là quá trình

### 04:17:00 - 00:04:24
Mà chúng ta đã theo để đạt được trạng thái hiện tại không ảnh hưởng đến các trạng thái tương lai

### 04:24:00 - 00:04:25
Mà chúng ta sẽ thấy.

### 04:27:00 - 00:04:31
Đó chính xác là những gì biểu thức này đang cố gắng nói với chúng ta.

### 04:32:00 - 00:04:37
Quá trình không có bộ nhớ. Nếu một quá trình thỏa mãn các đặc điểm này

### 04:38:00 - 00:04:40
Nó được gọi là quá trình Markov.

### 04:41:00 - 00:Thực t04:49
ế, Quá trình quyết định Markov là mở rộng của một quá trình được gọi là chuỗi Markov.

### 04:49:00 - 00:04:49
Trong chuỗi này

### 04:49:00 - 00:04:57
Quá trình bắt đầu ở một trạng thái cụ thể S0 và tại mỗi thời điểm nó có xác suất thay đổi

### 04:57:00 - 00:05:07
Trạng thái thành S1, và xác suất đó là 70% và cũng với xác suất 30% nó sẽ ở lại

### 05:07:00 - 00:05:08
Trong trạng thái S0.

### 05:10:00 - 00:05:17
Quá trình quyết định Markov là một loại quá trình tương tự kết hợp các hành động và phần thưởng.

### 05:18:00 - 00:05:26
Trong ví dụ này, quá trình bắt đầu ở trạng thái S0 và tác tử phải thực hiện một hành động, hoặc

### 05:26:00 - 00:05:35
A0 hoặc A1, và dựa trên một tập hợp các xác suất, có thể thay đổi trạng thái thành S1 hoặc ở lại

### 05:35:00 - 00:05:36
Trong S0.

### 05:37:00 - 00:05:43
Bây giờ chúng ta hiểu các nhiệm vụ điều khiển theo cách trừu tượng, nhờ Quá trình quyết định Markov,

### 05:43:00 - 00:05:50
Chúng ta có thể làm việc với tất cả chúng bằng một mẫu duy nhất và phát triển các giải pháp chung cho tất cả.
