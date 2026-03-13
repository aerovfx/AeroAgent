# 05 - Các phương pháp thực hành tốt nhất về ủy quyền MCP

---

- Đây là các phương pháp hay nhất được khuyến nghị

để xây dựng bất kỳ loại ủy quyền nào cho MCP.

Trước hết, bất cứ khi nào bạn kết nối với dữ liệu không công khai,

luôn giả định

trừ khi có lý do rõ ràng để không làm vậy.

Có nghĩa là, bất cứ lúc nào bạn đang làm việc trên một hệ thống

mà bạn thường mong đợi phải đăng nhập vào,

xây dựng máy chủ MCP có tích hợp xác thực.

Đừng bắt đầu xây dựng nó mà không có.

Bắt đầu ngay từ đầu với tắt.

Bởi vì theo cách đó khi bạn xây dựng nó,

bạn đã xây dựng các mảnh trong

và bạn đang thử nghiệm xuyên suốt

để đảm bảo mọi thứ đều hoạt động

thay vì tập trung vào tất cả những thứ bảo mật này

sau sự thật, điều này có thể thực sự khó khăn.

Thứ hai, như tôi đã nói, đừng tự mình làm điều đó.

Sử dụng các giải pháp đã được hiệu đính đã tồn tại

bởi vì nếu bạn cố gắng tự mình cuộn nó,

điều gì đó, nó chắc chắn sẽ đi sai hướng.

Và mặc dù đây là một bài tập lập trình thú vị

mà mọi người nên làm vì những điều có ý nghĩa,

nó đơn giản không phải là một ý tưởng tốt.

Số ba,

tận dụng các giải pháp hiện có bất cứ khi nào có thể.

Ý tôi là, khi bạn có khả năng sử dụng,

ví dụ: Google để đăng nhập hoặc GitHub để đăng nhập

hoặc một số dịch vụ khác,

sử dụng nó hoặc ít nhất là cho phép người dùng

để sử dụng nó như một tùy chọn.

Bằng cách đó, bạn không cần phải quản lý bất kỳ điều gì trong số đó.

Bạn chỉ có thể xác thực toàn bộ quá trình xác thực

và có rất nhiều dịch vụ ngoài kia

cung cấp giải pháp đặc biệt này,

để bạn có thể cắm vào nó

thay vì cố gắng tự mình xây dựng nó.

Nếu bạn đang xây dựng máy chủ MCP trong doanh nghiệp

vì bất kỳ lý do gì, trước khi bạn làm bất cứ điều gì,

hãy nói chuyện với nhân viên CNTT để đảm bảo

rằng bạn đang tuân theo các quy tắc InfoSec chính xác

và rằng bạn đang thực hiện đúng quy trình xác thực.

Cũng giống như với...

Như tôi đã nói lúc đầu,

rằng nếu bạn đang xây dựng cơ chế xác thực của riêng mình...

Không. Xin lỗi.

Nếu bạn đang xây dựng ứng dụng của riêng mình,

bạn nên luôn bắt đầu với bảo mật.

Đó là trường hợp gấp đôi, gấp ba, gấp bốn

nếu bạn đang làm việc trong bất kỳ loại hình doanh nghiệp tư nhân nào,

và bên trong bất kỳ loại hình doanh nghiệp nào nói chung.

Bởi doanh nghiệp là mục tiêu của kẻ xấu

và xây dựng phần mềm không an toàn là cách mà họ xâm nhập.

Và cuối cùng,

có quy tắc này mà chúng tôi hoạt động theo

khi chúng tôi xây dựng phần mềm có nội dung "Đừng tin tưởng người dùng".

Bây giờ chúng ta đang ở thời điểm mà chúng ta cũng phải nói rằng,

“Đừng tin người đại diện.”

Ý tôi là, khi ai đó đang sử dụng máy chủ MCP,

người đó không sử dụng máy chủ MCP.

Máy chủ MCP đang thay mặt người dùng,

và đó là một cỗ máy ngôn ngữ đang đùn ngôn ngữ

trông giống như hướng dẫn

và sau đó đọc những hướng dẫn đó

và sau đó hành động theo những hướng dẫn đó.

Và rất có thể, thỉnh thoảng, đôi khi rất hiếm,

đôi khi rất thường xuyên, máy chủ MCP sẽ làm như vậy,

mô hình ngôn ngữ, sẽ làm những điều bất ngờ.

Người đại diện sẽ hành động theo cách mà ở phía bên nhận,

sẽ trông giống một người,

nhưng thực tế là một hành động ngẫu nhiên

đó không phải là ý định của người dùng.

Vì vậy, khi bạn đang xây dựng các máy chủ MCP

và trao cho các đại lý khả năng,

bạn phải suy nghĩ rất cẩn thận về hậu quả

về việc cung cấp cho một đại lý một khả năng

khi nào tác nhân có thể đang sử dụng khả năng đó

theo những cách ngoài ý muốn thay mặt cho người dùng.

Bây giờ, tôi đã nói về gợi ý trước đây.

Đây là một trong những nơi mà sự khơi gợi xuất hiện.

Ngay cả sau khi máy chủ MCP đã được xác thực

vào một hệ thống, thật sự là một ý tưởng hay nếu bạn suy nghĩ thấu đáo,

tại thời điểm nào nên có một con người trong vòng lặp?

Tôi đang cung cấp những loại khả năng nào cho đại lý?

Và khả năng nào trong số đó cần có con người

trong vòng lặp được xây dựng sẵn

để người đại diện không thể đi và làm điều gì đó

có thể gây hậu quả đáng kể cho người dùng?

Vì vậy, và điều này quan trọng hơn khi bạn làm việc

với những hệ thống được tích hợp ủy quyền này,

bởi vì những hệ thống đó có nhiều khả năng tương tác với dữ liệu hơn

dữ liệu đó nhạy cảm hơn và

và làm những việc có thể gây hại cho dữ liệu hơn.

Vì vậy đây là những điều bạn cần lưu ý,

không chỉ là phần đảm bảo an toàn,

mà còn cả tính bảo mật của dữ liệu thực tế

một khi chúng ta bắt đầu loay hoay với nó.

Toàn bộ môi trường này rất khác

từ cách chúng ta từng làm mọi việc,

đơn giản vì diễn viên

thực thể đi vào hệ thống có thể là AI

đó là làm những việc mà không ai bảo AI làm.

Và những thứ đó có thể là những thứ

mà bạn thường cho là

một con người đang ngồi đó và đi,

"Đây có phải là một ý tưởng tốt không?

Không, tôi sẽ không làm điều này vì nó sẽ gây ra hậu quả.”

Nhưng AI sẽ làm điều đó

bởi vì AI không suy nghĩ, không có ý định,

và chỉ viết hướng dẫn riêng của mình.