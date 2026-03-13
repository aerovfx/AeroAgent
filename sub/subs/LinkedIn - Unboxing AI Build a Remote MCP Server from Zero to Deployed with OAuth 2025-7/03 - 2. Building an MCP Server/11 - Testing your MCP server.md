# 11 - Kiểm tra máy chủ MCP của bạn

---

- Quay lại ví dụ đơn giản của chúng ta.

Bên trong máy chủ chúng tôi có, như tôi đã nói,

một công cụ, một nguồn tài nguyên và một lời nhắc.

Sau đó ở phía dưới chúng tôi nói, chúng tôi chỉ cần thiết lập nó

vì vậy chúng tôi nói mcp.run.

Nó chạy MCP, phiên bản của lớp.

Và sau đó nó sẽ nối vào mọi thứ và sau đó chạy lại nó.

Để chạy cái này trên thanh tra MCP,

bạn phải chắc chắn rằng bạn đang chạy môi trường này

bên trong bảng điều khiển của bạn.

Và sau đó bạn đi xuống đây.

Hãy xem. Tôi sẽ vượt qua tất cả những thứ đó.

Vì vậy, đây chỉ là mô tả về cách thực hiện tất cả những điều này.

Và sau đó chúng ta có thể nói uv run mcp dev server.py.

Sao chép đó.

UV là môi trường chạy.

Đó chỉ là cách điều hành mọi thứ.

MCP là MCP CLI.

Dev là máy chủ dev.

Và sau đó chúng tôi đang trỏ đến server.py.

Chạy cái đó.

Thanh tra bắt đầu từ đây.

Và nếu mọi thứ hoạt động chính xác thì nó không

bởi vì tôi cần nhớ lại máy chủ mcp đơn giản này, tôi nghĩ vậy.

Thế đấy.

Và chúng ta có thể đi xem xét các nguồn tài nguyên.

Có một tài nguyên hoặc đó là một mẫu danh sách ở đây.

Thế đấy, get_greeting.

Có lời nhắc nên chúng ta có thể vào xem lời nhắc.

Ở đây chúng tôi có danh sách các lời nhắc.

Đây là lời chào mừng người dùng.

Và chúng ta có các công cụ và chúng ta có thể có được danh sách các công cụ.

Có một công cụ bổ sung ở đây.

Chúng ta có thể thêm bốn cộng năm rồi chạy công cụ

and then we get nine as the output.

Thật tuyệt phải không?

Vì vậy, máy chủ MCP chỉ chạy Python.

Đó là tất cả, một trình bao bọc xung quanh Python.

Bây giờ hãy xem nó hoạt động như thế nào bên trong mã VS.

Vì thế nếu tôi quay lại đây,

và tôi sẽ kết thúc việc này trong giây lát,

Sau đó tôi có thể mở lại tập tin của mình.

Vậy mình sẽ vào Shifts + lệnh P,

quay lại cấu hình người dùng.

Chúng tôi đã thiết lập máy chủ thời tiết.

Tôi sẽ sao chép cái này

và sau đó chỉ cần dán vào bên dưới đây

và tôi sẽ gọi đây là một máy chủ đơn giản.

Công cụ này có vẻ giống nhau.

Vì vậy chúng tôi vẫn sử dụng tia cực tím, chúng tôi vẫn sử dụng chạy,

chúng tôi vẫn sử dụng thư mục.

Trong trường hợp này, thư mục sẽ là

máy chủ đơn giản.

Và tôi tin rằng chúng ta sẽ đi vào simple-mcp-server.

Và sau đó tôi nghĩ cuộc gọi đến máy chủ mcp đơn giản.

Chúng ta sẽ sớm thấy rõ để có thể cố gắng bắt đầu nó từ đây.

Nó đang chạy, vậy có nghĩa là nếu tôi mở cuộc trò chuyện của mình

và đi tới các công cụ ở đây và cuộn xuống,

Bây giờ tôi sẽ thấy máy chủ thời tiết

và máy chủ đơn giản có add.

Và điều đó có nghĩa là nếu tôi nói thêm hoặc/và mua,

nó có thể gọi đến máy chủ, có thể không.

Vâng, có máy chủ MCP.

Chạy, tiếp tục, bây giờ nó thực hiện phép toán.

Đây thực sự là một cách làm toán cơ bản nặng tay.

Tôi không khuyên bạn nên làm theo cách này.

Về cơ bản đây là sự lạm dụng khả năng của AI,

nhưng nó cho bạn thấy nó hoạt động như thế nào.

Nó cho bạn thấy rằng một khi bạn kết nối các hàm Python

và đặt những đồ trang trí này lên,

nó trở thành một chức năng mà bạn có thể sử dụng như một máy chủ MCP.

Và bây giờ bạn đã chạy nó trong phần trò chuyện bên trong mã VS,

bạn có thể thử mã và thay đổi nó

rồi vào mcp.json và nhấp vào khởi động lại hoặc dừng

hoặc bắt đầu lại hoặc bất cứ điều gì bạn muốn.

Và sau đó bạn có thể thay đổi nó.

Vì vậy, bạn có thể khắc phục sự cố bằng hành động

trong khi bạn đang làm việc với máy chủ MCP trong cuộc trò chuyện

và xem chuyện gì đang xảy ra.