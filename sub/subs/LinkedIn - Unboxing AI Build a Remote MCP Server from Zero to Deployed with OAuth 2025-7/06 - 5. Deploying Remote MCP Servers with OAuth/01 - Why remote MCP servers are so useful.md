# 01 - Tại sao máy chủ MCP từ xa lại hữu ích đến vậy

---

- Nếu bạn đang xây dựng một máy chủ MCP cho chính mình,

bạn có thể lưu trữ nó cục bộ trên máy tính của bạn

và khởi động nó bất cứ lúc nào bạn cần sử dụng nó.

Nhưng điều đó thật rắc rối nếu bạn làm việc theo nhóm

hoặc bạn muốn xuất bản máy chủ MCP

những người khác bên ngoài tổ chức của bạn

hoặc thậm chí trong tổ chức của bạn có nhu cầu sử dụng.

Trong hoàn cảnh đó,

sẽ hợp lý hơn nếu tạo một máy chủ MCP từ xa.

Và có nhiều lợi ích cho việc này.

Đầu tiên là,

máy chủ MCP từ xa rất dễ cài đặt cho bất kỳ người dùng nào.

Tất cả những gì họ phải làm là trỏ vào đúng URI

và máy chủ MCP sẽ chỉ hoạt động trong ứng dụng của họ.

Thứ hai, bạn có thể cập nhật máy chủ MCP từ xa bất cứ lúc nào

với các tính năng mới hoặc sửa lỗi hoặc bất kỳ điều gì khác,

và những đặc điểm đó sẽ tự động biểu hiện

cho người dùng cuối.

Miễn là họ chỉ ra máy chủ MCP từ xa đó,

họ không phải tự chạy bản cập nhật,

họ không cần phải chạy bất kỳ phần mềm cục bộ nào để nó hoạt động.

Nó chỉ là một dịch vụ bên ngoài mà họ cắm vào.

Có hai loại máy chủ MCP từ xa cơ bản.

Bạn có phiên bản công khai,

chỉ là các máy chủ MCP mở mà ai cũng có thể sử dụng,

và họ là những người đã không còn liên kết với họ,

vì vậy bạn phải đăng nhập theo cách nào đó

để có quyền truy cập vào dịch vụ.

Trong hướng dẫn này, tôi sẽ chỉ cho bạn cả hai.