# 09 - Xây dựng máy chủ MCP từ mẫu

---

- [Giảng viên] Và điều này mang lại cho chúng tôi

tới bản demo chính cho luồng trực tiếp này,

đó là cách xây dựng một cái cho chính bạn.

Vì thế tôi sẽ đóng mọi thứ ở đây,

thoát ra khỏi thứ ở dưới này,

và gõ vô hiệu hóa

để tôi có thể quay trở lại,

và tôi sẽ đi CD.

Hãy xem.

Vì vậy, bạn thấy những gì tôi đang làm.

Vậy tôi sẽ đi ra ngoài,

và sau đó tôi sẽ vào CD,

Máy chủ đơn giản thay thế.

Bởi vì nhìn vào

cách thức hoạt động của máy chủ hiện tại là một chuyện,

xây dựng máy chủ của riêng bạn từ đầu

là một điều hoàn toàn khác.

Vì vậy, trong thư mục Máy chủ đơn giản,

Tôi đã tạo một tệp README toàn diện

điều đó sẽ dẫn bạn đi qua

mỗi bước bạn cần thực hiện

để thiết lập một máy chủ cho chính mình.

Và như tôi đã giải thích trước đó,

máy chủ này dựa trên hướng dẫn

từ SDK Python MCP,

đó là những gì bạn thấy ở đây

Vì vậy, nếu bạn vào Bắt đầu nhanh,

mã trong máy chủ MCP này

hiện tại giống với mã bạn thấy ở đây

trong Bắt đầu nhanh.

Và máy chủ này có một công cụ, một nguồn tài nguyên,

và một lời nhắc duy nhất.

Lý do tại sao tôi cung cấp điều này

là đến được nơi bạn cần

tinh tế hơn một chút

hơn những gì được ghi lại trong SDK.

Vì vậy, tôi đã cung cấp tất cả các bước.

Vì vậy, nếu bạn chưa bao giờ làm điều này trước đây,

và bạn đang bắt đầu lại từ đầu,

nếu bạn làm theo các bước trong này,

bạn sẽ có một máy chủ MCP hoạt động đầy đủ

chạy trong Mã VS

mà bạn có thể trò chuyện trong VS Code,

và chạy vào Claude,

và bạn có thể trò chuyện với nó trong Claude.

Máy chủ đã được xây dựng hoàn chỉnh rồi

nên bạn có thể sử dụng nó như cũ,

nhưng tôi khuyên bạn nên làm theo các bước

bởi vì khi đó bạn thực sự phải trải qua nó,

và tôi sẽ hướng dẫn bạn thực hiện điều đó ngay bây giờ

để cho bạn thấy những gì liên quan ở đây.

Vì vậy, bạn bắt đầu bằng cách cài đặt UV.

UV giống như tôi đã nói, môi trường Python.

Bạn cần phải làm bất cứ điều gì để làm việc.

Môi trường đó sau khi được cài đặt,

chỉ cần ngồi trên máy tính của bạn,

và bạn không bao giờ phải cài đặt lại.

Bạn có thể chỉ cần cập nhật nó.

Dưới đây là hướng dẫn đầy đủ về cách thực hiện.

Sau đó, để tạo một dự án hoàn toàn mới,

bạn vào thư mục bắt đầu

mà bạn muốn làm việc,

và sau đó bạn gõ UV vào đó

để khởi tạo một dự án UV mới.

Và sau đó bạn gõ tên của cái mới

thư mục con.

Vì vậy, tên của bất kỳ dự án nào

bạn muốn sử dụng.

Trong trường hợp này tôi gọi nó là Máy chủ MCP đơn giản.

Khi bạn vào thư mục đó,

bây giờ bạn sẽ thấy một loạt các tập tin.

Cụ thể bạn sẽ thấy phiên bản Python,

tệp dự án PY, tệp README,

một tập tin có tên main.py

và tập tin khóa UV.

Đây là những tập tin được thiết lập theo mặc định,

và những tập tin này có phần cốt lõi

mà bạn cần

để mọi thứ hoạt động tốt.

Từ đó, bạn cần

để cài đặt MCP CLI.

Bây giờ bạn sẽ nhận thấy định dạng này ở đây,

thay vì nói UV hãy thêm MCP,

sẽ thêm thư viện MCP Python,

bạn phải chỉ định CLI trong ngoặc ở đây

bởi vì bạn cần phần mở rộng CLI,

phần mở rộng giao diện dòng lệnh

để nó hoạt động bình thường,

và đây là cách bạn làm điều đó trong tia cực tím.

UV khác với PY.

Khi bạn đã làm xong việc đó,

bạn có thể khởi động môi trường ảo của mình

bởi vì UV này thêm MCP CLI

sẽ khởi động môi trường ảo.

Nếu nó đã chạy rồi,

bạn sẽ gõ đồng bộ UV

thay vào đó và bạn nhận được kết quả tương tự.

Vì vậy, trong trường hợp này, tôi gõ UV sync,

Tôi nhận được thư mục Venv.

Sau đó, bạn nhập nguồn .venv/bin/activate.

Và...

Xin lỗi.

Không phải nguồn.

Máy chủ đơn giản.

Ồ, tôi phải vào thêm một máy chủ nữa.

Cd máy chủ MCP đơn giản.

Cd máy chủ MCP đơn giản.

Thế đấy.

Hãy thử lại lần nữa.

Vì vậy tôi gõ vào source.venv/bin/activate.

Vì vậy bây giờ tôi đang ở trong môi trường ảo đó

hoặc thư mục máy chủ MCP đơn giản.

Từ đây...

Và nhân tiện, nếu bạn muốn tắt tính năng này,

bạn gõ vô hiệu hóa trong thiết bị đầu cuối,

và sau đó bạn hủy kích hoạt môi trường ảo.

Lúc này tôi đang ngồi

bên trong môi trường ảo đó.

Tại thời điểm này,

bạn cần thiết lập

môi trường VS Code để phù hợp.

Vì vậy, bạn mở một tệp Python.

Nếu bạn đã thay đổi nó một lần,

bạn sẽ thấy nó ghi ở dưới đây

bạn đang chạy cái nào.

Đó không phải là điều tôi muốn.

Vì vậy tôi sẽ nhấp chuột vào đây,

và thay đổi nó thành Máy chủ MCP đơn giản.

Điều đó mang lại cho tôi môi trường phù hợp để làm việc.

Vì vậy, tôi có quyền truy cập vào các phần bên phải.

Và sau đó tôi có thể xem tập tin này.

Vì vậy, theo mặc định,

tập tin này, tập tin main.py,

bạn đổi tên thành server.py,

và sau đó bạn thêm mã mà bạn thấy ở đây.

Và tôi sẽ chia nhỏ điều này từ đầu

để bạn có thể thực sự thấy điều gì đang diễn ra.

Vì vậy, trong mã này, bạn bắt đầu từ đầu

bằng cách nhập MCP nhanh.

từ máy chủ MCP bên trong SDK.

Fast MCP là một trình bao bọc cho phép bạn

để nhanh chóng xây dựng các máy chủ MCP.

Bạn không cần phải sử dụng Fast MCP.

Trong thực tế, nếu bạn đi đến tài liệu

cho các giao thức bối cảnh mô hình,

nếu bạn đi đến mô hình bối cảnh giao thức.io

và đọc tài liệu ở đó,

bạn nhận được phiên bản không phải SDK của nó,

Python thuần túy, các tập lệnh kiểu thuần túy,

phiên bản Java thuần túy của mã này.

Và bạn có thể viết tất cả những điều này

sử dụng ngôn ngữ thuần túy

bởi vì nó chỉ là ngôn ngữ thuần túy.

Lý do bạn muốn

hoặc có thể muốn sử dụng SDK

bạn có nhận được tất cả những giấy gói đẹp đẽ này không

điều đó chỉ làm cho mọi việc dễ dàng hơn.

Và tôi sẽ cho bạn thấy ý tôi là gì

bằng cách làm cho mọi việc dễ dàng hơn.