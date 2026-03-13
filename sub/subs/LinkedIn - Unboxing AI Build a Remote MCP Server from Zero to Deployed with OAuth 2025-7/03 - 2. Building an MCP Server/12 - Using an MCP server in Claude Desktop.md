# 12 - Sử dụng máy chủ MCP trong Claude Desktop

---

- Trong file README cũng có hướng dẫn

về cách thực hiện điều tương tự bằng cách cài đặt nó trong Claude.

Vậy ở Claude, tôi sẽ chỉ cho bạn.

Chúng tôi sẽ tạo máy chủ Open-Meteo cho Claude.

Vì vậy, tôi sẽ để nó ở đây.

Tôi sẽ mở Claude ra.

Vì vậy ở Claude,

nếu bạn đến, hãy xem, chúng ta có thể bắt đầu lại từ đầu ở đây,

để bạn có thể thấy chính xác những gì đang xảy ra.

Chúng ta sẽ bắt đầu một cuộc trò chuyện mới.

Chỉ là một cuộc trò chuyện mới.

Sau đó chúng ta sẽ nói Claude, Cài đặt.

Và bởi vì đây là buổi trực tiếp,

điều này thực sự trông khác với những gì nó đã làm ngày hôm qua

khi tôi đang chuẩn bị thứ này.

Vì vậy, chúng tôi đi đến Nhà phát triển.

Dưới quyền của Nhà phát triển,

bạn sẽ thấy danh sách các máy chủ có sẵn

hiện đang chạy.

Cái mà tôi có ở đây đã chạy rồi.

Và để xem config đó ở đâu các bạn nhấn Edit Config.

Điều này làm lộ một tập tin cấu hình trên máy tính của bạn,

và sau đó bạn có thể mở nó trong trình chỉnh sửa ưa thích của mình.

Đây là tập tin đó.

Bạn sẽ thấy tập tin trống.

Vậy điều đang xảy ra ở đây là Claude cần được khởi động lại.

Vì vậy, tôi sẽ nói Khởi động lại Claude.

Quay trở lại Cài đặt, Nhà phát triển, máy chủ MCP cục bộ.

Hiện tại không có máy chủ MCP phải không?

Vì vậy, chúng ta quay lại Chỉnh sửa cấu hình tại đây.

Bạn sẽ thấy chẳng có gì cả.

Bây giờ, bạn có thể vào README

và sao chép mã này theo cách thủ công và dán vào tệp đó.

Nhưng MCP CLI thực sự có một công cụ cho việc đó,

đặc biệt dành cho Claude.

Vì vậy, nếu bạn đang ở trong một dự án hiện có

đã có máy chủ MCP đang chạy,

bạn có thể thoát khỏi điều này.

Và sau đó bạn có thể nói điều này ở đây, uv run mcp,

không, uv install mcp dev server chính là như vậy.

Hãy xem. Nó đâu rồi?

Ở đây uv chạy mcp install server.py

Vì vậy, hãy để tôi kéo cái này sang một bên

để bạn có thể thấy điều này xảy ra trong thời gian thực.

Vì vậy, tôi sẽ nói,

uv chạy mcp cài đặt server.py

và sau đó mọi thứ sẽ được điền tự động vào đây.

Điều này thực sự hữu ích

bởi vì thiết lập cái này hơi rắc rối một chút

vì bạn cần biết chính xác vị trí của tia cực tím.

Bạn cần biết chính xác vị trí của tập tin.

Bạn cần biết trình tự các cuộc gọi cho Claude

để có được điều này để chạy.

Lệnh này thực hiện tự động cho bạn.

Sau đó, tất cả những gì bạn phải làm là lưu nó,

đóng Claude và mở lại nó.

Bây giờ chúng ta quay lại Cài đặt.

Và bạn sẽ thấy trong phần Nhà phát triển,

đây là Máy chủ MCP đơn giản, nó đang chạy.

Không có vấn đề gì.

Nếu có vấn đề,

họ sẽ hiển thị ở đây với một liên kết tới nhật ký.

Và bạn có thể sử dụng máy chủ MCP.

Vì vậy, điều đó có nghĩa là khi bạn bắt đầu làm việc với những tệp này

có trong dự án này, bạn có thể kiểm tra chúng ở Claude,

bạn có thể kiểm tra chúng trong Mã VS.

Bạn có thể kiểm tra chúng trong Cursor.

Bạn có thể kiểm tra chúng trong mọi môi trường

hỗ trợ máy chủ MCP cục bộ

và sau đó xây dựng máy chủ khi bạn đang thử nghiệm nó

để đảm bảo rằng mọi thứ đang hoạt động như mong đợi.

Vì vậy, sau khi tôi hoàn tất buổi phát trực tiếp này,

Tôi sẽ cập nhật kho lưu trữ này một chút

với một chút hướng dẫn thêm

trên Máy chủ MCP đơn giản

vì tôi có một ví dụ thực tế mà tôi nghĩ ra,

chẳng hạn như năm phút trước khi luồng trực tiếp bắt đầu

về cách bạn có thể mở rộng cái này và thử nghiệm với nó

để làm điều gì đó có ý nghĩa hơn là chỉ làm toán cơ bản.