# 03 - Kiểm tra máy chủ MCP từ xa

---

- Trước tiên hãy để tôi chỉ cho bạn cách xuất bản máy chủ MCP công cộng,

một cái không có bất kỳ xác thực nào,

và sau đó tôi sẽ chỉ cho bạn cách quản lý

một cái có OAuth thông qua GitHub,

và những phần phức tạp cần được đặt đúng chỗ

để làm tất cả những việc đó, được chứ?

Để tham khảo, nếu bạn muốn theo dõi tại đây

và bạn chỉ muốn khởi động một máy chủ MCP cơ bản,

bạn có thể sử dụng hướng dẫn mà Cloudflare có,

nó được gọi là Xây dựng máy chủ MCP từ xa.

Sự khởi đầu ở đây chính là sự khởi đầu tôi sẽ sử dụng.

Vì vậy tôi sẽ sao chép lệnh đầu tiên này

ở trên cùng đây.

Và để ghi lại, để làm điều này,

bạn cần có tài khoản Cloudflare miễn phí.

Chẳng tốn gì cả,

nhưng bạn cần thiết lập tài khoản Cloudflare.

Và lần đầu tiên bạn trải qua quá trình này,

bạn sẽ phải xác thực chính mình thông qua Cloudflare

để lấy IDE của bạn, có thể là Mã VS,

để làm việc với Cloudflare,

để bạn có thể đẩy và lấy nội dung từ dịch vụ.

Trong Mã VS, tôi mở thư mục ngày-5.

Và ở dưới đây, trong nhà ga,

Tôi đã điều hướng đến ngày-5,

và tôi sẽ dán lệnh mà tôi vừa sao chép vào.

Nó nói npm tạo cloudflare@latest,

vì vậy điều này mang lại Cloudflare CLI.

Sau đó, chúng ta tạo một thư mục mới có tên my-mcp-server,

và sử dụng mẫu

cloudflare/ai/demos/remote-mcp-authless.

Khi tôi chạy lệnh này,

tất cả các tập tin cần thiết đã được cài đặt trên máy tính của tôi.

Như tôi đã nói, nếu cần thiết, bạn phải thông qua quá trình xác thực.

Như tôi đã nói, lần đầu tiên bạn làm điều này,

bạn cũng phải trải qua vòng lặp xác thực

để đảm bảo bạn đã kết nối,

và bạn có thể nhận được một số câu hỏi.

Vì vậy, trong trường hợp này, câu hỏi là,

"Bạn đang ở trong kho git hiện có.

Bạn có muốn sử dụng git để kiểm soát phiên bản không?"

Tôi sẽ nói có với điều đó.

Và câu hỏi tiếp theo là,

"Bạn có muốn triển khai ứng dụng của mình không?"

Và tôi thực sự cũng sẽ nói đồng ý với điều đó

và chỉ cần triển khai nó ngay lập tức.

Vậy là việc này sẽ triển khai ứng dụng lên Cloudflare,

và nó sẽ có sẵn thông qua URI trên Cloudflare.

Và lý do tôi làm điều đó là vì tôi muốn cho bạn thấy

rằng máy chủ MCP này không chạy trên máy tính của tôi.

Nó không có,

nó không tồn tại trên máy tính của tôi theo cách nó có thể chạy,

nó chỉ tồn tại trên Cloudflare.

Bây giờ chúng tôi nhận được một URL ở đây,

bạn có thể thấy đó là my-mcp-server.morten-122.workers.dev.

Trước khi chúng ta truy cập URL đó,

hãy đến với công nhân của Cloudflare.

Đây chỉ là bảng điều khiển Cloudflare.

Và bây giờ,

trong phần tổng quan về Công nhân & Trang,

Tôi có máy chủ MCP của mình đang chạy.

Vậy đây là máy chủ mới được triển khai.

Trong khi điều này là như vậy,

điều đó cũng có thể có nghĩa là việc đếm ngược này

mà bạn nhìn thấy ở phía dưới ở đây sắp hết thời gian,

rằng cái này đang hoạt động bình thường,

chỉ là CLI bị kẹt thôi.

Điều đó nói rằng, tôi muốn kiểm tra máy chủ này ngay lập tức.

Vì vậy, tôi sẽ mở một thiết bị đầu cuối mới.

Sau đó, trong thiết bị đầu cuối đó,

Tôi sẽ khởi động thanh tra MCP.

Vì vậy, tôi sẽ nhập npx @modelontextprotocol/inspector@latest.

Tôi đang sử dụng npx chứ không phải npm ở đây

bởi vì với npx tôi đang chạy nó trên npm, dịch vụ đám mây.

Tôi không cần phải tải toàn bộ nội dung xuống máy tính của mình,

và tôi cũng không phải duy trì phiên bản mới nhất,

nó chỉ luôn chạy phiên bản mới nhất.

Điều này quay lên máy chủ.

Và từ đây, bây giờ tôi có thể chọn loại vận chuyển là SSE,

rồi dán vào URI.

Vì vậy,

nên tôi quay lại thiết bị đầu cuối khác,

sao chép URL tôi cần ở đây.

Và sau đó dán nó vào đây.

Vì vậy, bây giờ chúng tôi đang hướng tới Cloudflare.

mcp-server.morten-122.workers.dev và sau đó là /sse.

Bấm vào Kết nối.

Và hiện tôi đã kết nối với máy chủ MCP trên Cloudflare.

Từ đây, tôi có thể liệt kê các công cụ.

Tôi có thể kiểm tra một trong những công cụ.

Tôi sẽ nói cộng 9 cộng 6.

Chạy công cụ.

Nhận được phản hồi, 15.

Vì vậy, nó hoạt động đúng.

Và thế là xong.

Tôi vừa tạo một máy chủ MCP từ máy tính của mình,

đã triển khai nó lên đám mây,

hiện đang hoạt động với tư cách là nhân viên của Cloudflare,

và bây giờ tôi có thể kết nối nó.

Nếu muốn, tôi có thể kết nối máy chủ này

tới Claude, hoặc tới VS Code, hoặc tới Phi công phụ,

hoặc bất kỳ thứ gì khác hỗ trợ máy chủ MCP,

và nó sẽ tắt dịch vụ Cloudflare.