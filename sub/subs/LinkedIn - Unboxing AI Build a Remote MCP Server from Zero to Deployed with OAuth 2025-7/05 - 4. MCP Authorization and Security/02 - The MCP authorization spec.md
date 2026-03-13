# 02 - Thông số ủy quyền MCP

---

- Hầu hết những điều ý nghĩa chúng ta làm trực tuyến

được thực hiện theo cách bạn kiểm soát tài khoản của mình

và bạn phải chắc chắn rằng những người khác

không thể kiểm soát tài khoản.

Khi chúng tôi có máy chủ MCP hoạt động,

cho phép LLM thay mặt chúng tôi hành động,

chúng ta cần đảm bảo rằng họ có quyền truy cập vào các dịch vụ đó,

nhưng chúng ta cần đảm bảo rằng họ đang thực hiện việc đó một cách an toàn.

MCP có thông số ủy quyền.

Như bạn có thể thấy trên trang này, nó vẫn ở dạng bản nháp,

nhưng nó đã được triển khai khá rộng rãi.

Và thông số ủy quyền dựa trên

trên các tiêu chuẩn ủy quyền hiện có có ý nghĩa.

Chúng được thiết lập cho OAuth 2.0 và 2.1,

đó là cách tiêu chuẩn

về việc cho phép khá nhiều thứ

và thông số ủy quyền hỗ trợ mọi thứ

giống như ủy quyền của bên thứ ba.

Bạn biết đấy, khi bạn truy cập một trang web

và bạn có thể đăng nhập vào trang web

thông qua Google hoặc GitHub hoặc một số bên thứ ba khác,

bạn có thể thiết lập máy chủ MCP của mình

để sử dụng các loại thông số ủy quyền đó.

Bằng cách đó, khi người dùng truy cập,

họ không phải thiết lập tài khoản với dịch vụ của bạn,

bạn có thể xác thực người dùng thông qua bên thứ ba,

vì vậy bạn không cần phải quản lý

toàn bộ hệ thống xác thực.

Vì vậy, để bắt đầu,

khi chúng tôi nghĩ về việc ủy quyền và xác thực,

điều rất quan trọng là phải hiểu

hệ thống thực tế hoạt động như thế nào.

Trong máy chủ MCP thông thường,

một máy chủ MCP trực tiếp chạy trên máy tính của bạn,

đó là kết nối với một số dịch vụ công cộng,

không cần có sự cho phép,

bởi vì bạn vừa gọi một dịch vụ bên ngoài,

hoặc bạn có thể gọi,

thứ gì đó đang chạy cục bộ trên máy tính,

truy cập một tập tin,

truy cập phần mềm trên máy tính, cái gì đó khác.

Trong hoàn cảnh đó,

không cần xác thực người dùng

hoặc đưa ra bất kỳ mức độ ủy quyền nào cho việc sử dụng chúng,

bởi vì hoặc trên máy tính của bạn,

hệ thống sẽ thực hiện loại công việc đó

khi người dùng đăng nhập vào hệ thống,

và đối với các dịch vụ công có dữ liệu mở,

bạn chỉ đang truy cập dữ liệu mở.

Vì vậy, trong kịch bản cơ bản này,

không có lớp ủy quyền hoặc xác thực.

Và đây là nơi chúng tôi đã làm việc cho đến nay.

Đây là mô hình MCP cơ bản.

Nhưng điều gì xảy ra khi máy chủ MCP đang kết nối

đến một dịch vụ doanh nghiệp

hoặc một số dịch vụ yêu cầu xác thực,

một dịch vụ mà khả năng của bạn có

tùy thuộc vào loại tài khoản bạn có,

và do đó, máy chủ MCP thay mặt bạn

nên có những khả năng tương tự,

tùy thuộc vào tài khoản của bạn?

Trong những hoàn cảnh này,

chúng ta cần bằng cách nào đó ủy quyền cho máy chủ MCP

để hành động thay mặt chúng tôi,

đăng nhập hiệu quả vào máy chủ MCP với tư cách là chính chúng tôi.

Bây giờ, bạn đã trải nghiệm điều này.

Có một số dịch vụ mà bạn sử dụng hàng ngày

nơi bạn thực hiện loại ủy quyền này.

Nếu bạn có một trong những thứ này, bạn biết đấy,

cỗ máy gây xao lãng mà bạn luôn chọc vào

điều đó lấy đi tất cả sự chú ý của bạn.

Bất cứ khi nào bạn đăng nhập vào một dịch vụ lần đầu tiên,

bạn phải trải qua một số loại

của vòng lặp ủy quyền, phải không?

Bạn phải xác thực chính mình

rồi nói: "Ứng dụng này có quyền truy cập vào máy ảnh"

hoặc "Tôi đang đăng nhập vào tài khoản này" hoặc nội dung nào đó khác.

Đó chính là vòng lặp mà chúng ta đang nói đến.

Điện thoại của bạn và ứng dụng trên điện thoại của bạn

là một tác nhân người dùng thay mặt bạn.

Vì thế bạn chọc vào điện thoại,

ứng dụng trên điện thoại sau đó đăng nhập vào dịch vụ

và thực hiện hành động thay mặt bạn,

và bạn đang ngồi đó làm việc đó.

Vì vậy, trong trường hợp này với MCP,

điều chúng tôi đang xem xét là thiết lập nó sao cho,

khi bạn tương tác với hệ thống AI,

và hệ thống AI sử dụng máy chủ MCP,

máy chủ MCP cũng đang làm điều tương tự,

đang hành động thay mặt bạn,

nghĩa là chúng tôi cần một cách để máy chủ MCP đăng nhập với tư cách là bạn,

và chúng ta cần làm điều đó một cách an toàn.