# 04 - Luồng MCP OAuth 2.0 được hiển thị

---

- Tất nhiên, vấn đề là, như bạn sẽ thấy bây giờ,

vòng lặp là xác thực và nó có mục đích.

Chúng tôi muốn một vòng lặp xác thực rất khó giả mạo

và vòng lặp xác thực rất dễ bị vô hiệu hóa,

để những kẻ độc hại không thể vào được

và gây rối với nó.

Vì vậy, vòng lặp đó thực sự trông như thế này với MCP.

Máy khách MCP, vậy là bạn đang nói chuyện với AI

và AI đang cố gắng kết nối với MCP sẽ gửi yêu cầu

đến máy chủ MCP mà không cần mã thông báo.

Vì vậy, nó chỉ nói, "Này, hãy để tôi làm việc đó."

Máy chủ phản hồi bằng thông báo 401 cho biết:

"Bạn không được phép.

Bạn không có quyền truy cập vào các dịch vụ này.

Tôi từ chối yêu cầu này."

Sau đó, khách hàng sẽ gửi lại yêu cầu với nội dung:

"Cấp cho tôi quyền truy cập vào dữ liệu được bảo vệ trên máy chủ"

mà máy chủ phản hồi với siêu dữ liệu

cho dữ liệu được bảo vệ.

Và trong siêu dữ liệu này sẽ có một liên kết

đến máy chủ ủy quyền.

Sau đó, khách hàng có thể gửi yêu cầu

đến máy chủ ủy quyền và nói,

"Này, tôi muốn đăng nhập."

Máy chủ ủy quyền sau đó sẽ tiến hành bắt tay

để đảm bảo rằng nó có kết nối an toàn với máy khách

và một loạt thông tin được gửi qua lại,

và cuối cùng, khách hàng nhận được URL ủy quyền.

URL đó cần phải mở trong trình duyệt.

Và sau đó người dùng, con người, phải bấm vào một nút

hoặc làm điều gì khác để thực sự ủy quyền.

Cái bắt tay đó xảy ra

và mã ủy quyền được trả lại

từ máy chủ ủy quyền đến tác nhân người dùng

và từ tác nhân người dùng đến máy khách MCP.

Khi đó, khách hàng có thể quay lại

đến máy chủ ủy quyền và yêu cầu mã xác thực.

Sử dụng mã xác thực để yêu cầu mã thông báo,

máy chủ ủy quyền trả lại mã thông báo cho khách hàng,

và sau đó khách hàng có thể thực hiện yêu cầu ban đầu

sử dụng mã thông báo.

Lần này, máy chủ cho phép kết nối diễn ra.

Bạn đang đi đi lại lại giữa các máy chủ khác nhau

và các thực thể khác nhau,

và tất cả điều này là để đảm bảo rằng chỉ những người dùng được ủy quyền mới

thực sự có thể sử dụng các dịch vụ này.

Bây giờ, hầu hết những điều này xảy ra ở hậu trường.

Và thông thường khi bạn tương tác với hệ thống OAuth,

nếu bạn không phải là nhà phát triển,

bạn sẽ không biết tất cả những điều này đang diễn ra

vì tất cả đều được xử lý bằng phần mềm.

Nhưng khi bạn tự xây dựng hệ thống

có dịch vụ OAuth, dựa vào dịch vụ OAuth,

và bạn cố gắng xây dựng nó từ đầu,

bạn phải quản lý tất cả những bộ phận chuyển động này

và tất cả những tương tác này

và có rất nhiều bước đi vào vấn đề này.

Và nếu bất kỳ bước nào trong số đó bị hỏng,

thì việc ủy quyền không được xử lý.

Và hơn nữa,

những hệ thống này được thiết lập sao cho, theo thời gian,

tất cả các mã thông báo hết hạn và quá trình này phải được thực hiện lại.

Bất cứ khi nào bạn đột nhiên phải đăng nhập lại vào một dịch vụ,

đó là những gì đang xảy ra

Hệ thống chỉ nói,

"Tôi chỉ tin tưởng ai đó có quyền truy cập quá lâu,"

và sau đó bạn phải làm lại toàn bộ quá trình này một lần nữa.

Tất cả điều đó được tích hợp vào lớp máy chủ ủy quyền,

và sau đó bất kỳ khách hàng nào đang sử dụng nó đều phải rời đi

thông qua việc nhảy nhiều vòng này để làm cho nó hoạt động.

Nhìn thấy điều này, có lẽ bạn đang tự hỏi làm thế nào để thiết lập điều này.

Bạn thực sự có thể tự mình thiết lập điều này.

Bạn có thể xây dựng máy chủ ủy quyền của riêng mình,

trình xử lý ủy quyền của riêng bạn,

thiết lập toàn bộ quá trình và làm cho nó hoạt động.

Và khi bạn đang làm việc cục bộ trên máy tính của mình,

đó thường là những gì bạn làm

bởi vì theo cách đó bạn có toàn quyền kiểm soát

và bạn có thể xem tất cả các bước khác nhau này diễn ra

và đảm bảo mọi thứ đều hoạt động tốt.

Tuy nhiên, làm điều đó không phải là ý kiến hay

bởi vì ủy quyền

và xác thực là vô cùng phức tạp.

Và nó phức tạp vì các tác nhân độc hại

với mục đích xấu luôn cố gắng xâm phạm hệ thống.

Vì vậy, bất cứ khi nào bạn làm việc với các hệ thống an toàn,

cách tốt nhất là sử dụng xác thực chính thức

và các hệ thống ủy quyền đã tồn tại.

Đừng cố gắng tự cuộn nó.