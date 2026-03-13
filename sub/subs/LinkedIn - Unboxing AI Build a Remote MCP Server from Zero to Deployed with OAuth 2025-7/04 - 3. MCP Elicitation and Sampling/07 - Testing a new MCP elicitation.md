# 07 - Thử nghiệm gợi ý MCP mới

---

- Được rồi, vậy nó trông như thế nào?

Tôi sẽ tạo một cuộc trò chuyện mới và nói: "Bắt đầu máy tính".

Nó khởi động máy chủ MCP và sau đó thông báo:

"Chúng ta hãy làm một số phép toán.

Vui lòng cung cấp những con số

và hoạt động bạn muốn thực hiện."

Hãy nhớ rằng thông điệp ở đây là "Hãy làm một phép tính.

Xin vui lòng cung cấp các con số."

Vì vậy, trong ctx.elicit,

thông báo là những gì hiển thị trong ứng dụng khách

như một thông điệp gửi tới người dùng.

Nhấp vào Trả lời.

Bây giờ nó ghi Số thứ nhất và một trong ba

vì trong trường hợp này, chúng ta có ba đầu vào.

Chúng ta có thứ nhất, thứ hai và hoạt động.

Vì vậy, chúng ta sẽ nói số đầu tiên là 98,

số thứ hai là ba,

và phép tính, tôi sẽ nói dấu hoa thị ở đây để nói là nhân lên.

Thông tin đó được chuyển trở lại,

Python thực hiện công việc của nó và tôi nhận được phản hồi.

98 x 3 là 294, tôi giả định là đúng.

Đây là cách nó hoạt động.

Và những gì bạn thấy là nó thực sự đơn giản.

Bạn thiết lập một công cụ, sau đó bạn gọi trong ngữ cảnh,

sau đó bạn thiết lập ngữ cảnh, gợi ý, rồi khai báo một thông báo,

xác định loại phản hồi bạn muốn.

Máy khách tiếp quản, gợi ra phản hồi từ người dùng,

sau đó ghi lại phản hồi và gửi lại cho máy chủ,

sau đó máy chủ sẽ tiếp tục.

Và bằng cách sử dụng phương pháp này, bạn thực sự có thể có

nhiều gợi ý khác nhau xếp chồng lên nhau.

Vì vậy, bạn có thể có một nơi mà bạn nói, tôi cần thông tin này,

người dùng chuyển nó vào, một số thao tác sẽ xảy ra,

sau đó nó quay lại với nhiều câu hỏi hơn,

nhiều hoạt động hơn xảy ra.

Vì vậy, bạn thực sự có thể xây dựng qua lại nếu bạn muốn.

Tôi không biết nó sẽ thân thiện với người dùng như thế nào,

nhưng khả năng là có.

Và như bạn đã thấy trong ví dụ về thời tiết,

trường hợp sử dụng thực sự ở đây

là khi bạn yêu cầu người dùng nhập một số thông tin,

nhưng nó không đủ thông tin.

Vì vậy bạn có thể sử dụng nó

để nắm bắt tất cả những điều không chắc chắn và mơ hồ này

điều đó có thể xảy ra khi thông tin đến từ LLM

không đủ để thực hiện một hành động.

Đó là sự khơi gợi.

Còn nhiều điều hơn thế nữa, bạn có thể xem tài liệu.

Tất cả các tài liệu đều ở đây.

Bạn có thể đọc về các hành động phản hồi khác nhau,

chuyện gì đang xảy ra vậy

Ngoài ra còn có một số bài viết blog đề cập đến điều này.

Bạn có thể xem ở đây

rằng các định dạng hiện được hỗ trợ cho lược đồ chuỗi

là email, uri, ngày và ngày giờ.

Nhưng bạn cũng thấy tôi vượt qua điều gì đó

đó không phải là những điều này.

Vì vậy hiện tại không có giới hạn nào về điều này,

nhưng như tôi đã nói, điều đó có thể xảy ra.

Ngoài ra còn có một lược đồ số cho phép bạn xác định

những thứ gì đang đi vào và ra.

Và có một số hướng dẫn

về cách khơi gợi được cho là hoạt động.

Nếu bạn truy cập SDK Python trên GitHub và cuộn xuống một chút,

bạn sẽ tìm thấy một ví dụ gợi ý.

Đây là một ví dụ mã hoàn chỉnh

thiết lập một ví dụ về tùy chọn sách,

nơi bạn có thể tạo một bảng có thông tin về sách.

Nó chỉ là một loại ví dụ khác.

Bạn cũng có thể theo liên kết này ở đây.

Nó đi đến một ví dụ trực tiếp

nằm bên trong SDK, trong thư mục ví dụ.

Bạn thấy đấy, dưới những ví dụ,

bạn có rất nhiều phiên bản khác nhau ở đây.

Vì vậy, dưới đoạn trích,

bạn có cùng một ví dụ hoặc tương tự.

Đó là ví dụ tương tự cho thấy cách thực hiện

và nó được tích hợp.

Vì vậy, bạn thực sự có thể chạy ví dụ

ngoài các ví dụ SDK.

Tuy nhiên, SDK lớn và cồng kềnh,

và cho rằng bạn đang điều hành mọi thứ,

và việc thiết lập nó không hề đơn giản.

Đó là lý do tại sao tôi xây dựng ví dụ này

bởi vì nó rất đơn giản,

nó chỉ có những phần bạn cần,

và thật dễ dàng để thấy điều gì đang diễn ra,

và bạn có thể tự mình xử lý nó.