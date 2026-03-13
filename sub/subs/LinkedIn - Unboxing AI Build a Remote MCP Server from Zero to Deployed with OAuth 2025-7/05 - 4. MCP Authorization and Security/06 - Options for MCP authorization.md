# 06 - Tùy chọn ủy quyền MCP

---

- Khi bạn bắt đầu làm việc với sự ủy quyền,

có rất nhiều ví dụ bạn có thể sử dụng.

Vì vậy, trong kho lưu trữ Python GitHub

đối với SDK, ở dạng này, xin lỗi.

Trong tất cả các SDK, SDK Python, SDK Java,

SDK TypeScript, SDK C#,

tất cả họ đều có máy chủ mẫu hiển thị xác thực đơn giản.

Điều đó khiến bạn suy sụp

về cách thức hoạt động của hệ thống ủy quyền

và cả cách khởi động nó nữa.

Và những máy chủ xác thực đơn giản này thực sự hoạt động

cả máy chủ ủy quyền của bạn

và máy chủ MCP trên máy tính của bạn

để bạn có thể thấy sự tương tác giữa hai phần.

Điều này rất hữu ích cho việc xây dựng máy chủ,

đảm bảo mọi thứ hoạt động bình thường,

nhưng điều này không dành cho việc xuất bản máy chủ trực tuyến.

Và điều thực sự quan trọng là phải hiểu

rằng việc thực hiện việc này tại địa phương chỉ nhằm mục đích phát triển.

Đến mức khi bạn nhìn vào hướng dẫn

về cách xây dựng ứng dụng OAuth, MCP

hoặc bất cứ điều gì khác, bạn sẽ thấy cách thực hành tiêu chuẩn

là tạo ra hai ứng dụng riêng biệt.

Vậy là bạn đã có ứng dụng dành cho nhà phát triển cục bộ

và bạn có ứng dụng sản xuất.

Vì vậy, nếu bạn muốn sử dụng GitHub làm thực thể xác thực chẳng hạn,

máy chủ ủy quyền,

bạn sẽ mở hai ứng dụng trên GitHub.

Một cho khi bạn đang phát triển

và một dành cho khi bạn bắt đầu sản xuất.

Vì nếu không, khả năng cao là

rằng đến một lúc nào đó bạn sẽ quên

rằng bạn đang làm việc trong môi trường phát triển

và bạn sẽ gửi mã cho môi trường phát triển

và sau đó gửi mã không an toàn mà người khác có thể khai thác.

Bởi vì điều này không đơn giản.

Tôi muốn nói rằng web được xây dựng

như một nền tảng phân phối thông tin

và kể từ khi trang web được xây dựng, chúng tôi đã cố gắng rất nhiều

để ngăn chặn việc phân phối thông tin đó xảy ra

với tất cả dữ liệu chúng tôi có

bởi vì có rất nhiều dữ liệu trên web

không nên được phân phối.

Nhưng hạt của mạng,

các thành phần nền tảng của web,

muốn phân phối mọi thứ.

Vì vậy, bất cứ khi nào bạn thêm một lớp che giấu

hoặc một khối tại chỗ, sẽ luôn có cách xung quanh nó.

Và OAuth, quá trình qua lại khổng lồ này

giữa nhiều máy chủ truyền nhiều khóa khác nhau

theo một thứ tự cụ thể

là nỗ lực mới nhất trong việc thực hiện

một nền tảng phân phối thông tin được thiết lập theo cách như vậy

rằng bạn thực sự có thể bảo vệ dữ liệu.

Và rất có thể, thậm chí OAuth cuối cùng cũng sẽ thất bại.

Và sau đó chúng ta sẽ phải tiến lên

thậm chí còn có nhiều cách phức tạp hơn để thực hiện việc này.

Vì vậy, vâng, nó phức tạp và nó phức tạp là có lý do.

Công cụ này là khó khăn.

Điều đó không có nghĩa là bạn không nên làm điều đó.

Điều đó có nghĩa là khi bạn bắt đầu tìm hiểu điều này,

hãy tìm những ví dụ hiện có

về cách nó đã hoạt động từ bất kỳ dịch vụ nào

bạn sẽ sử dụng.

Vì vậy, ví dụ: Azure có thiết lập đầy đủ

cho các máy chủ MCP từ xa an toàn

sử dụng hệ thống quản lý API của Azure.

Và như bạn có thể thấy trong hình ở đây,

cách thức hoạt động của nó là hệ thống quản lý API Azure

đảm nhận tất cả những phần phức tạp đó.

Vì vậy, tất cả những gì bạn đang làm là cắm máy chủ MCP của mình vào

và sau đó mọi người có thể sử dụng nó.

Lớp xác thực được xử lý bởi các dịch vụ Azure.

Nó không phải là duy nhất.

Cloudflare cũng cho phép bạn lưu trữ các máy chủ MCP từ xa

và có toàn bộ thư viện các nhà cung cấp OAuth mà bạn có thể kết nối

cho phép bạn cắm vào.

Và họ có các gói được cấu hình sẵn mà bạn có thể sử dụng

để xuất bản máy chủ MCP của bạn

và cũng để xuất bản máy chủ MCP của bạn

với OAuth mạnh mẽ được tích hợp sẵn.

Điều tương tự cũng xảy ra với các dịch vụ khác.

Vì vậy, tùy thuộc vào nơi bạn sẽ đến

để lưu trữ máy chủ MCP của bạn, hãy xem tài liệu

để biết cách nhận quyền ngay trong hệ thống đó

vì mọi người đều đang vận chuyển thứ này.

Đây không phải là một trong những trường hợp bạn đến,

"Tôi phải tự mình lập hóa đơn vì không ai khác có."

Nó hoàn toàn ngược lại.

Đây là một trong những tình huống

nơi dịch vụ có quyền lợi được đảm bảo

trong máy chủ MCP của bạn được an toàn,

bởi vì nếu không, nó sẽ gây ra mối đe dọa cho họ.

Vì vậy họ sẽ xây dựng những hệ thống mạnh mẽ

và tất cả những gì bạn phải làm là tận dụng chúng

và sử dụng chúng khi chúng ở đó

và sau đó đảm bảo rằng bạn đang làm theo hướng dẫn của họ.

Và điều đó cũng có nghĩa là bạn cần phải làm theo hướng dẫn

của bất kỳ dịch vụ nào bạn đang sử dụng.

Vì vậy, khi bạn đi sâu vào vấn đề này, hãy nhìn xung quanh.

Nhìn vào những gì có sẵn,

sau đó thử nghiệm một số tùy chọn khác nhau, tìm những tùy chọn

phù hợp với bạn, sau đó học cách thực hiện việc này đúng cách

thông qua tài liệu chi tiết phong phú của họ

và mã mẫu.

Trong nhiều trường hợp, vấn đề chỉ là lấy một thư viện

và đính kèm nó và sau đó chỉ cần khởi động một máy chủ

và đưa vào các URI phù hợp.

Đó là tất cả những gì bạn cần làm để nó hoạt động.

Vì vậy, thay vì tự xoay nó

và tạo ra một số hệ thống cực kỳ thiếu an toàn,

bạn có thể sử dụng các hệ thống hiện có

đã được xuất bản và được kiểm duyệt kỹ lưỡng

và nó dễ dàng hơn nhiều để làm.