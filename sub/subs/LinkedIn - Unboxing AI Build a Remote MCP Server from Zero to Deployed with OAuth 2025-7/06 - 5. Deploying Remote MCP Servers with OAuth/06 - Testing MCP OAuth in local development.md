# 06 - Thử nghiệm MCP OAuth trong quá trình phát triển cục bộ

---

- [Người hướng dẫn] Đầu tiên hãy vào dev.vars.example

và tạo một bản sao của tập tin này.

Gọi nó là dev.vars.

Bây giờ tôi đã làm xong việc đó và nó có chìa khóa bên trong.

Tôi sẽ không cho bạn xem tập tin đó.

Nó hoàn toàn giống nhau.

Tôi vừa thay đổi những giá trị này ở đây.

Tiếp theo bạn cần tạo một ứng dụng mới trên GitHub.

Bạn có thể thấy tôi đã tạo hai thứ tôi cần,

nhưng tôi sẽ hướng dẫn bạn thực hiện quy trình.

Vì vậy, bạn truy cập github.com/settings/developers

và nhấp vào ứng dụng OAuth mới.

Từ đây, bạn đặt tên cho ứng dụng.

Từ đây bạn đặt tên cho ứng dụng

và đây là cái tên để bạn nhận ra nó.

Vì vậy, đây sẽ giống như thử nghiệm ứng dụng thời tiết tại địa phương của tôi.

Sau đó bạn đưa URL trang chủ vào.

Và khi bạn đang chạy cục bộ,

URL đó là HTTP://localhost:8788.

Và bạn sao chép nó và dán nó xuống đây

trong URL gọi lại và thêm /callback.

Không kiểm tra luồng thiết bị đã bật này

vì bạn không muốn dòng chảy của thiết bị.

Thay vào đó chỉ cần nhấp vào đăng ký ứng dụng.

Khi bạn làm điều đó, bạn sẽ đến một trang trông như thế này

nơi bạn có thể thấy ID khách hàng

và bạn có thể tạo bí mật khách hàng mới.

Lấy ID khách hàng này và sao chép nó

và sau đó dán nó vào đây nơi nó nói

ID khách hàng GitHub của bạn.

Sau đó tạo một bí mật khách hàng mới,

sao chép nó và dán nó vào đây để giữ bí mật cho khách hàng của bạn.

Đối với môi trường phát triển

bạn không cần tạo khóa mã hóa cookie

bởi vì bạn là người địa phương nên điều đó không thành vấn đề.

Và chỉ cần nhớ tất cả những giá trị này nên ngồi

trong tập tin này dev.vars.

Khi đã xong, bạn có thể khởi động máy chủ cục bộ.

Vì vậy tôi sẽ đi ra khỏi thư mục

và sau đó vào

máy chủ thời tiết GitHub auth.

Và sau đó tôi sẽ khởi động máy chủ

bằng cách gõ vào npm run start.

Máy chủ hiện đang chạy trên localhost 8788.

Điều đó có nghĩa là tôi có thể đến gặp Thanh tra MCP,

ngắt kết nối,

thay đổi URI ở đây thành

HTTP://localhost

8788/sse.

Bây giờ khi tôi nhấp vào kết nối, bạn sẽ gặp lỗi này.

Lỗi kết nối, kiểm tra xem máy chủ MCP của bạn có đang chạy không,

đó là vì chúng tôi hiện có vòng lặp OAuth

và chúng ta cần chạy qua vòng lặp OAuth.

Có thể làm điều đó ở đây bằng cách nhấp vào mở cài đặt OAuth.

Và tại đây bạn có thể nhấp vào nút luồng OAuth nhanh

điều đó sẽ thúc đẩy bạn hoàn thành quá trình

hoặc bạn có thể thực hiện quá trình này một cách thủ công

để xem chính xác những gì đang xảy ra.

Vì vậy, chúng ta có thể làm điều đó ở đây.

Đầu tiên chúng tôi khám phá siêu dữ liệu

để kiểm tra xem có siêu dữ liệu hay không.

Vì vậy, ở đây chúng ta có thể thấy tất cả thông tin

về vị trí của điểm cuối ủy quyền và điểm cuối mã thông báo

và điểm cuối đăng ký, tất cả điều đó.

Tiếp theo chạy đăng ký khách hàng.

Điều này đăng ký khách hàng.

Đây là ID khách hàng và tất cả những thứ khác.

Sau đó chuẩn bị ủy quyền.

Điều này sẽ cung cấp cho bạn một URI.

Đó là URI gọi lại.

Vì vậy, ở đây chúng ta sẽ tìm hiểu quy trình xác thực thực tế,

chúng tôi được gửi tới GitHub.

Đổi lại chúng ta nhận được một chìa khóa, sao chép chìa khóa đó,

đi xuống mã ủy quyền và dán vào.

Sau đó tiếp tục, thực hiện yêu cầu mã thông báo.

Và khi mọi việc đã xong,

bạn nhận được xác thực hoàn tất.

Và bây giờ bạn có thể kết nối.

Liệt kê các công cụ

Và đây là tất cả các công cụ thời tiết.

Điều đó có nghĩa là ứng dụng đang hoạt động bình thường trên localhost

và luồng OAuth đang hoạt động theo cách nó được yêu cầu.