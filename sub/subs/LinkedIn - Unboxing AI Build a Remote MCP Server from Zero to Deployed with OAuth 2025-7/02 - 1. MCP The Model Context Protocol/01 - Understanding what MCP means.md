# 01 - Hiểu ý nghĩa của MCP

---

- Hiện tại, chúng tôi đã có nhiều giao thức

mà chúng ta luôn sử dụng.

Cái mà bạn thường xuyên sử dụng,

mà bạn đang sử dụng ngay bây giờ

nếu bạn đang xem khóa học này hoặc xem buổi phát trực tiếp,

là Giao thức truyền siêu văn bản hoặc HTTP.

Và Giao thức bối cảnh mô hình là một loại giao thức khác.

Nó không phải là phần mềm chạy ở bất cứ đâu,

đó là một cách để các hệ thống giao tiếp với nhau.

MCP được phát hành vào tháng 11 năm ngoái

để không phô trương nhiều.

Nó xuất hiện dưới dạng một bài đăng trên blog của Anthropic,

Anthropic là công ty sản xuất ra Claude.

Và các nhà phát triển đã xem xét nó và nói, "Thú vị."

Lý do là do mô tả.

Giao thức bối cảnh mô hình là một tiêu chuẩn mở

cho phép các nhà phát triển xây dựng kết nối hai chiều an toàn

giữa các nguồn dữ liệu của họ và các công cụ được hỗ trợ bởi AI.

Kiến trúc rất đơn giản.

Các nhà phát triển có thể hiển thị dữ liệu của họ thông qua máy chủ MCP

hoặc xây dựng các ứng dụng AI, máy khách MCP,

kết nối với các máy chủ này.

Tên, Giao thức bối cảnh mô hình, bắt nguồn từ MCP,

thực sự mô tả nó là gì, nó chỉ ngược lại thôi.

Nó là một giao thức cung cấp ngữ cảnh cho các mô hình ngôn ngữ.

Giao thức là các quy tắc chính thức mà hệ thống máy tính sử dụng

để liên lạc với nhau.

Tôi đã đề cập đến HTTP như một giao thức.

Ngoài ra còn có các giao thức khác, chúng tôi có FTP, SMTP, SMS,

giống như tất cả các giao thức khác nhau mà chúng tôi sử dụng.

Bối cảnh là thông tin

được gửi tới hệ thống AI để làm việc,

và mô hình chính là hệ thống AI.

Bây giờ, nếu bạn đã từng làm việc với Claude hoặc ChatGPT hoặc Gemini

hoặc bất kỳ công cụ nào khác mà chúng tôi hiện có,

bạn biết rằng để khiến hệ thống thực hiện được những điều có ý nghĩa,

trước tiên bạn phải cung cấp ngữ cảnh cho họ.

Theo cách thô sơ nhất,

điều đó có nghĩa là đi tới một tài liệu hoặc một bảng tính

hoặc đến một trang web hoặc một nơi nào khác,

sao chép một loạt nội dung ra ngoài,

sau đó dán nó vào cuộc trò chuyện AI,

và nói, "Này, giúp tôi làm việc này nhé."

Hoặc "Phân tích thông tin này."

Hoặc, "Hãy giúp tôi viết lại nó."

Hoặc "Tìm thông tin từ bên trong nó."

Hoặc một cái gì đó như thế.

Đó là bối cảnh.

Nó cũng cho thấy sự khó khăn như thế nào

để AI thực sự hữu ích, bởi vì bản thân nó,

những công cụ AI đàm thoại này, như ChatGPT và Claude,

chỉ có thể hoạt động trong bối cảnh riêng của họ,

vì vậy chỉ trong cuộc trò chuyện mà bạn đang có.

Và điều đó có nghĩa là những điều chúng ta tưởng tượng ra những công cụ này

nên có thể làm được,

như lên mạng và tìm thông tin về điều gì đó

hoặc dọn sạch hộp thư đến của tôi hoặc dọn sạch bảng tính

hoặc điều gì đó tương tự không đơn giản như người ta tưởng,

bởi vì trò chuyện chỉ là trò chuyện,

và mọi kết nối bên ngoài cần phải được thực hiện thủ công.