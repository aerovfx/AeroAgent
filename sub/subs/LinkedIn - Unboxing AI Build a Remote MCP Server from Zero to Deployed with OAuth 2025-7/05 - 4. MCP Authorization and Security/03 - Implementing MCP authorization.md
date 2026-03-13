# 03 - Thực hiện ủy quyền MCP

---

- Cách hoạt động của ủy quyền MCP

là khách hàng MCP,

vậy chatbot, VS Code,

Con trỏ, bất kể bạn đang sử dụng gì,

trở thành ứng dụng khách OAuth 2.1,

và máy chủ MCP trở thành máy chủ tài nguyên OAuth 2.1.

Bằng cách đó, thay vì thêm lớp xác thực

giữa máy chủ MCP và API bên ngoài,

chính máy chủ MCP là ủy quyền

và lớp xác thực.

Điều đó trông như thế nào trong thực tế?

Chà, bạn phải trải qua cái được gọi là vòng lặp OAuth,

và cách mạnh mẽ nhất để làm điều này là thiết lập nó

để máy chủ MCP có thể,

trích dẫn, bỏ trích dẫn, "không hiểu người dùng"

nghĩa là máy chủ MCP có thể hành động thay mặt cho bất kỳ người dùng nào,

miễn là họ đăng nhập,

nhưng vòng đăng nhập đó cần phải diễn ra ở cuối người dùng.

Vì vậy, vòng lặp đó thực sự trông như thế nào trong thực tế,

chỉ để cho bạn biết có bao nhiêu bước liên quan

để đảm bảo rằng không có gì sai sót.

Thực ra, trước khi tôi nói điều này,

Tôi nên chỉ ra

cho đến khi thông số xác thực cho MCP được đưa ra,

mọi người vẫn đăng nhập vào hệ thống bằng máy chủ MCP,

và cách họ làm là bằng cách đóng gói tên người dùng

và các khóa bên trong máy chủ MCP

và chỉ gửi thông tin đó qua máy chủ MCP,

hoặc bằng cách thiết lập một số loại hệ thống đầu vào của người dùng

khi bạn cố gắng làm điều gì đó,

máy chủ MCP sẽ đưa ra yêu cầu nói như thế nào,

"Nhập tên người dùng và mật khẩu của bạn,"

hoặc "Nhập khóa mã hóa của bạn" hoặc bất cứ điều gì.

Đó là chức năng như trong nó hoạt động.

Nó cũng không an toàn một cách ngoạn mục.

Và nếu bạn xem tin tức về MCP khi nó mới xuất hiện,

bạn sẽ thấy rằng có rất nhiều câu chuyện

những người sẽ thiết lập máy chủ MCP,

và sau đó những người khác sẽ có thể

thích truy cập vào tài khoản AI của họ

hoặc sử dụng nhiều tài nguyên và thực hiện một số việc,

những điều thực sự không an toàn vì lúc đầu,

không có thông số kỹ thuật về cách thực hiện ủy quyền

và xác thực trong các máy chủ MCP.

Vì vậy, điều này, như tôi đã nói, là mở đường cho bò đi.

Đây là điều mà rất nhiều công ty lớn nhìn thấy được giá trị của MCP

và thấy được sự cần thiết

vì đã đặt một số lan can vào đúng vị trí,

và sau đó xây dựng thông số xác thực cho MCP

để đảm bảo rằng có một cách nhất quán để thực hiện việc này.