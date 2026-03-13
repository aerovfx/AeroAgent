# 2 -Dịch nội dung khóa học

---

Trong video này, tôi sẽ cung cấp đề cương cho khóa học này để bạn biết điều gì sẽ xảy ra, v.v.

bạn sẽ có được ý tưởng chung về con đường học tập của mình.

Khóa học này sẽ được chia nhỏ như sau.

Đầu tiên, chúng ta sẽ xem xét rất ngắn gọn về tất cả các khái niệm học tăng cường mà bạn nên áp dụng.

biết trước khi tìm hiểu về DQN và A2C.

Trên thực tế, sẽ có hai phần đánh giá trong khóa học này nhưng cả hai đều phục vụ một mục đích khác nhau.

mục đích.

Phần đánh giá đầu tiên ở đầu khóa học này ngắn gọn hơn nhưng cũng trực quan hơn.

Điều này được thiết kế để nhắc nhở bạn về những ý tưởng chính trong học tập tăng cường.

Bài đánh giá thứ hai mà tôi đặt ở gần cuối khóa học được thiết kế dành cho những người

trong số các bạn cần xem xét thêm một chút và nó cung cấp thêm một chút chi tiết về mặt toán học.

Sự đánh đổi là nó di chuyển nhanh hơn nhiều.

Sau khi xem xét, chúng tôi sẽ đề cập đến DQN.

Như thường lệ, chúng ta sẽ luôn tiến hành từ lý thuyết đến viết mã.

Nghĩa là, đầu tiên chúng ta thảo luận về lý thuyết hoặc các khái niệm mà cuối cùng chúng ta sẽ đưa vào

mã.

Bước thứ hai là xem mã để triển khai các khái niệm này.

Xin nhắc lại, khóa học này sẽ không dạy bạn Python cơ bản hoặc thậm chí là cơ bản.

học sâu vì đó là những điều kiện tiên quyết cho khóa học này và nó sẽ không phù hợp

đang học những khái niệm đó vào lúc này.

Vì vậy, nếu bạn thấy mình đang gặp khó khăn để theo kịp hoặc không hiểu điều gì đó mà tôi dường như

để xem nhanh quá, vui lòng sử dụng phần Hỏi đáp hoặc xem lại các chủ đề tiên quyết

được đề cập trong phần mô tả khóa học.

Sau DQN, chúng ta sẽ xem xét độ dốc chính sách trong A2C, mạng lưới thần kinh sâu được áp dụng

để lập chính sách cho các phương pháp chuyển màu, một lần nữa kèm theo một số thủ thuật ở trên.

Vì phương pháp chuyển màu chính sách là hoàn toàn mới nên chúng tôi sẽ lấy nó từ đầu như sau:

trái ngược với việc học Q, được dạy trong điều kiện tiên quyết.

Đối với cả DQN và A2C, mục tiêu của chúng tôi trước tiên là phát triển sự hiểu biết về cách thức và

tại sao chúng hoạt động nên chúng ta sẽ không tập trung vào việc sử dụng các môi trường phức tạp.

Nhưng sau khi bạn hiểu được những điều cơ bản, phần tiếp theo chúng ta sẽ xem xét cách áp dụng DQN tại

Môi trường A2C đến Atari.

Nếu bạn còn quá trẻ để nhớ thì Atari là người tiên phong trong ngành công nghiệp game và đã phát triển

nhiều trò chơi điện tử phổ biến trong thập niên 70 như Pong, Breakout và Astroids.

Điều này sẽ khó giải quyết hơn nhiều vì không gian trạng thái lớn hơn và phức tạp hơn nhiều

hơn là với những môi trường đơn giản như Đi chung xe.

Chúng ta sẽ cần sử dụng các mạng nơ-ron tiên tiến hơn, cụ thể là mạng nơ-ron tích chập và

chúng ta sẽ cần phải lo lắng về các vấn đề như hết RAM.

Trong phiên bản VIP của khóa học này, chúng ta cũng sẽ xem xét một trong những ứng dụng yêu thích của tôi,

đó là áp dụng học tập tăng cường vào giao dịch trên thị trường chứng khoán.

Trong các khóa học trước, chúng ta đã xem xét một số cách cơ bản để thực hiện việc này, nhưng trong khóa học này, chúng ta

sẽ tiến thêm một bước nữa.

Cụ thể, chúng ta sẽ xem xét cách áp dụng các phương pháp gradient chính sách cho danh mục đầu tư nhiều kỳ.

tối ưu hóa.

Trong khóa học kỹ thuật tài chính của tôi, chúng tôi đã xem xét lý thuyết danh mục đầu tư nổi tiếng của Markowitz,

điều này giải thích cách tối ưu hóa danh mục đầu tư khi bạn biết lợi nhuận và hệ số bên trong

một khung thời gian xác định.

Vấn đề là chúng ta không biết kết quả và hệ quy chiếu, và thực tế còn có nhiều điều hơn thế.

hơn một khung thời gian để xem xét.

Ví dụ: bạn có thể muốn cân bằng lại danh mục đầu tư của mình hàng tháng hoặc hàng quý.

Trong khóa học này, bạn sẽ tìm hiểu cách ATUC hoàn hảo cho việc này.

Nếu bạn không chắc ý tôi khi nói phiên bản VIP là gì, bạn có phiên bản VIP hay không, hoặc

làm thế nào để có được phiên bản VIP, sau đó vui lòng truy cập trang web của tôi, trong đó có một trang mô tả tất cả

thứ của VIP.

Đó là lười lập trình viên.me chém các khóa học VIP hoạt động như thế nào?