# 06 - Tại sao MCP giúp tự động hóa dễ dàng hơn

---

- Tôi muốn giới thiệu một điều nữa ở đây.

Nếu bạn sử dụng một công cụ tự động hóa như n8n,

bạn biết rằng để xây dựng các quy trình tự động hóa nâng cao,

đặc biệt là được xây dựng dựa trên các công cụ AI,

bạn cần xây dựng rất nhiều tích hợp phức tạp

để đảm bảo rằng hành vi đúng đắn

được kích hoạt vào đúng thời điểm.

Và bạn phải thực sự kiểm soát cách hoạt động đầu vào của AI

và kết quả đầu ra như thế nào, đồng thời đưa ra đề xuất.

Vì vậy, ví dụ, trong công cụ này mà tôi đã tạo ở đây,

bạn sẽ thấy phần này ở đây,

switch nhận được phản hồi từ tác nhân AI,

và sau đó dựa vào phản hồi là gì,

nó sẽ bắn hạ các đặc vụ phụ khác nhau.

Và cách tôi làm điều này là nhờ tác nhân AI đầu tiên

chỉ xuất ra các câu lệnh rõ ràng như lấy thông tin,

cập nhật thông tin hoặc ngoài phạm vi,

và sau đó kích hoạt các chức năng này, điều này thực sự rắc rối.

Bây giờ n8n hiện cũng hỗ trợ máy chủ và máy khách MCP.

Và dựa trên những gì tôi đã chứng minh cho đến nay,

nghe có vẻ kỳ lạ nhưng thực ra nó có ý nghĩa.

Bên trong n8n, bây giờ bạn có thể thiết lập máy chủ MCP

cái đó có rất nhiều,

let's see, this one, MCP Server Trigger,

đó là những gì nó được gọi ở đây,

có các công cụ bên dưới nó.

Và sau đó bạn yêu cầu tác nhân AI chỉ gọi máy chủ MCP đó.

Những gì xảy ra bây giờ là thay vì tôi

phải viết tất cả các tích phân phức tạp và nói,

"Nếu người dùng hỏi câu hỏi này,"

đó là một câu hỏi nhắm mục tiêu thông tin.

Vì vậy AI đọc dữ liệu đầu vào của người dùng, diễn giải nó,

và sau đó nếu đó là một yêu cầu thông tin,

sau đó nói rõ ràng lấy thông tin,

và sau đó tôi sẽ có một công tắc

phát hiện xem liệu thông tin có được đưa vào hay không

và sau đó tôi sa thải đúng người đại diện.

Giòn, phức tạp để thiết lập,

dễ dàng không hoạt động bình thường.

Với máy chủ MCP, tôi chỉ nói đơn giản:

"Nhận thông tin từ người dùng,

nhìn vào các công cụ có sẵn của bạn,

và làm bất cứ điều gì có vẻ đúng."

AI sau đó sẽ đi vào và xem,

ồ, đây là danh sách tất cả các công cụ

có sẵn dưới dạng máy chủ MCP.

Các máy chủ MCP này tự khai báo và giải thích,

đây là một nguồn tài nguyên, đây là những gì tôi cần.

Đây là một công cụ, đây là thứ tôi cần.

Đây là một lời nhắc, đây là những gì tôi cần.

Và tôi sẽ lấy nó và xác nhận nó,

và sau đó chỉ cần kích hoạt dịch vụ phù hợp.

Vì vậy, thay vì làm việc này rất phức tạp,

thiết lập rất dễ vỡ, nhờ MCP,

thiết lập tự động hóa này bây giờ đơn giản hơn nhiều

và cũng có thể mở rộng.

Vì vậy tôi có thể sử dụng cùng một máy chủ MCP

trong nhiều quy trình tự động hóa khác nhau

và tôi có thể dễ dàng thêm hoặc thay đổi máy chủ MCP

mà không cần phải chạm vào toàn bộ quá trình tự động hóa.

Đây là lý do tại sao MCP rất thú vị.

Các nhà phát triển có thể tiết lộ dữ liệu của họ

thông qua máy chủ MCP hoặc xây dựng các ứng dụng AI,

Máy khách MCP kết nối với các máy chủ này.

Ứng dụng AI không có nghĩa là phải là ChatGPT hay Claude,

nó có thể là bất cứ điều gì khác

Nó có thể là bất kỳ tác nhân tùy chỉnh nào bạn xây dựng.

Vì vậy, bạn có thể xây dựng ứng dụng khách MCP của riêng mình

sau đó có thể sử dụng thông tin từ MCP

để tương tác với các dịch vụ bên ngoài,

nơi bạn không phải tự mình xây dựng sự tích hợp đó.

Bạn chỉ cần nói, "Đây là máy chủ MCP, hãy sử dụng nó,"

và sau đó AI sẽ móc vào nó và sử dụng nó.