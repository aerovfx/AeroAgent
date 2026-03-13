# 03 - Cách tiếp cận mang tính cách mạng của MCP

---

- MCP là công nhân trung gian,

một lớp giữa dịch vụ bên ngoài và AI.

Nó cho phép dịch vụ bên ngoài xác định

chính xác những khả năng mà AI nên có,

và sau đó thông báo cho AI về loại

đầu vào là cần thiết để tạo ra kết quả cụ thể.

Và điều thú vị về giao thức của MCP

bạn, với tư cách là người dùng, có thể chọn viết

máy chủ MCP của riêng bạn để thực hiện mọi việc,

hoặc nhà cung cấp dịch vụ có thể viết máy chủ MCP của họ

để làm mọi việc.

Và sau đó, khi bạn là người dùng sử dụng tác nhân trò chuyện,

hoặc bạn sử dụng IDE để mã hóa,

hoặc bạn sử dụng bất kỳ công cụ nào khác hỗ trợ MCP,

bạn có thể cắm bao nhiêu máy chủ MCP tùy thích

và sau đó dựa vào AI, tác nhân trò chuyện,

để tìm ra máy chủ nào sẽ được sử dụng trong trường hợp nào.

Đó là phần cách mạng.

Đó là sự tách biệt những mối quan tâm

nơi bạn có dữ liệu một mặt,

bạn có tác nhân trò chuyện ở bên kia,

và sau đó bạn có lớp công nhân ở giữa này

tạo điều kiện thuận lợi cho việc giao tiếp giữa hai phần.

Bây giờ, khi mọi người nói về MCP,

họ thường nói về nó như USB phải không?

Bạn lấy USB, một giao thức được tiêu chuẩn hóa,

và bạn cắm bất kỳ thiết bị USB nào

vào bất kỳ thiết bị hỗ trợ USB nào như máy tính,

và nó sẽ chỉ chạy.

Đó là một loại ý tưởng, trong đó nhà cung cấp,

công ty đã tạo ra một dịch vụ,

có thể xác định cách kết nối nó,

và sau đó bạn chỉ cần cắm nó vào và nó sẽ hoạt động.

Bây giờ, máy chủ MCP

nói với khách hàng MCP,

đó có thể là bot trò chuyện hoặc công cụ bạn đang sử dụng,

những gì có sẵn, nghĩa là bạn có thể lấy thông tin,

bạn có thể thực hiện các hành động,

đây là hướng dẫn về cách thực hiện mọi việc, v.v.

Nó cung cấp hướng dẫn cho AI

về những gì có thể thực hiện được trong dịch vụ bên ngoài.

Những thứ này có thể là công cụ,

nghĩa là các hành động mà AI có thể thực hiện trên máy chủ.

Hãy nghĩ đến việc gửi email, sắp xếp lại thư mục,

tạo một tập tin mới, thực hiện tìm kiếm một thứ cụ thể,

làm điều gì đó với dữ liệu

Nó cũng có thể là tài nguyên, tức là thông tin thụ động.

Vì vậy, nếu bạn truy cập cơ sở dữ liệu

và bạn muốn lấy thông tin,

đó sẽ được lấy từ một tài nguyên.

Vì vậy, một thư viện, giống như một thư viện vật lý trên thế giới,

có thể cung cấp các tài nguyên mà sau đó có thể cho phép bạn

để trò chuyện với thư viện

để tìm hiểu xem có sách hay không.

Và cuối cùng, nó có cái gọi là lời nhắc,

đó là hướng dẫn từ máy chủ MCP

với bot trò chuyện AI của bạn về những gì có thể làm được.

Và tùy thuộc vào cách thực hiện điều đó,

đôi khi máy chủ MCP

sẽ chỉ viết lời nhắc cho bạn.

Những lúc khác, bạn thực sự có thể hiển thị lời nhắc

trong ứng dụng trò chuyện và sau đó sử dụng chúng.

Và những lần khác, một lần nữa,

ứng dụng trò chuyện sẽ làm theo hướng dẫn của bạn,

kết hợp chúng với lời nhắc rồi gửi chúng vào.

Và điều đó phụ thuộc vào cách nó được thực hiện.

Bạn có các chức năng tùy chỉnh trong các công cụ,

bạn có khả năng truy xuất dữ liệu và tài nguyên,

và bạn có các mẫu nhắc nhở trong dấu nhắc.

Và đây mới chỉ là sự khởi đầu.

Đây là bước đầu tiên trong giao thức MCP.

Đây là những gì đã được phát hành lúc đầu

và là những gì thường được hỗ trợ trên tất cả các thiết bị

sử dụng MCP ngay bây giờ.

Nhưng đó không phải là điều duy nhất.

Sắp tới là gợi ý,

cho phép máy chủ MCP chuyển câu hỏi

quay lại với khách hàng, với ứng dụng trò chuyện AI,

để biết thêm thông tin.

Bạn có, nó được gọi là gì, lấy mẫu,

cho phép máy chủ MCP

để yêu cầu khách hàng chạy thêm thế hệ AI

hoặc đi nơi khác

và chạy thêm quá trình tạo AI trên dữ liệu được trả về

trước khi nó được trả lại cho người dùng.

Vì vậy, hãy suy nghĩ, bạn đặt một câu hỏi

để tìm một số thông tin từ thư viện,

máy chủ MCP kết nối bạn với thư viện

và truy xuất thông tin.

Sau đó máy chủ nói: "Thật ra,

tóm tắt điều này một cách rất cụ thể

với các liên kết và bất cứ điều gì khác cần thiết."

Và nó dựa vào đại lý trò chuyện của bạn

để thực sự làm công việc tóm tắt đó

trước khi nó được trả lại cho bạn.

Vì vậy, máy chủ đang hành động thay mặt cho tài nguyên

trong đại lý của bạn.

Và vâng, điều đó phức tạp vì vô số lý do,

bao gồm cả bạn, người dùng,

không nhất thiết phải biết chuyện gì đang xảy ra.

Vì vậy, đây hiện không phải là thứ tồn tại ở bất cứ đâu.

Bạn thực sự chưa thể làm điều này, nhưng nó đang đến.

Khách hàng, vì vậy ứng dụng

được kết nối với máy chủ MCP,

đó sẽ là ChatGPT, Claude, Gemini,

ứng dụng của bạn, bất kể bạn đang sử dụng gì

có hỗ trợ MCP, xác định cách tiến hành.

Và khi tôi nói khách hàng,

Ý tôi thực sự là AI xác định cách tiến hành.