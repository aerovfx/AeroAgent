# 08 - Lấy mẫu MCP Máy chủ sử dụng công cụ AI

---

- Đó là sự khơi gợi.

Bây giờ chúng ta hãy nhìn vào việc lấy mẫu.

Lấy mẫu là khả năng của máy chủ MCP

để yêu cầu tạo thêm từ LLM.

Việc này thường được thực hiện bởi máy chủ MCP

gửi yêu cầu trở lại LLM ban đầu

để thực hiện một số hành động.

Hành động đó xảy ra trong nền.

Sau đó, máy chủ MCP sẽ đưa ra phản hồi.

Cũng giống như sự khơi gợi,

điều đó có nghĩa là bây giờ chúng ta có sự qua lại,

ngoại trừ thay vì máy chủ

yêu cầu phản hồi từ người dùng, người dùng con người,

máy chủ đang yêu cầu phản hồi

từ một đại lý LLM để làm điều gì đó.

Và có nhiều tình huống

nơi mà điều đó có thể có ý nghĩa.

Bạn có thể nhận được phản hồi từ cơ sở dữ liệu

và sau đó bạn muốn chuyển nó thành một cái gì đó cụ thể

trước khi bạn chuyển lại cho người dùng.

Trong trường hợp đó, bạn có thể sử dụng phương pháp lấy mẫu để gửi nó đến LLM,

yêu cầu LLM làm gì đó với dữ liệu,

sau đó chụp nó, kiểm tra nó, hoặc bất cứ điều gì,

và sau đó chuyển nó cho người dùng, v.v.

Có rất nhiều kịch bản khác nhau

nơi bạn có thể sử dụng cái này

Lấy mẫu cũng được hỗ trợ trong Mã VS.

Lấy mẫu cũng được hỗ trợ trong VS Code Insiders.

Và có một ví dụ, trong ví dụ trích dẫn của tôi.

Nếu bạn quay trở lại thư mục ở đây,

vẫn ở dưới máy chủ khơi gợi đơn giản,

bạn sẽ thấy nếu chúng ta tiếp tục lướt qua ví dụ toán học,

có một cái khác ở đây tên là generate_haiku.

Vì vậy, ở đây tôi đã thiết lập một lớp mới cho mô hình cơ sở

cái đó được gọi là HaikuInput.

Đó là một lược đồ để thu thập các chủ đề haiku từ người dùng.

Đầu ra là động vật có thể thay đổi,

và chúng tôi đang tìm kiếm một chuỗi có tên

của một con vật cho thơ haiku.

Và vâng, điều đó có nghĩa là, một lần nữa,

Tôi đang yêu cầu người dùng nhập một chuỗi

chỉ với một số thông tin ngẫu nhiên.

Vì vậy trong tương lai điều này có thể không hiệu quả,

nhưng bây giờ thì có, nên chúng ta sẽ sử dụng nó.

Công cụ này tạo ra một bài thơ haiku

bằng cách nắm bắt bối cảnh đầu tiên, giống như trước đây.

Sau đó, định nghĩa của công cụ

là Tạo một bài thơ haiku bằng cách sử dụng gợi ý

để lấy chủ đề động vật từ người dùng.

Lời gợi ý nói rằng, "Chúng ta hãy tạo một bài thơ haiku!

Hãy cho tôi biết bạn thích con vật nào

bài thơ haiku sẽ nói về."

Và chúng tôi kích hoạt đầu vào haiku.

Sau đó, khi chúng tôi nhận được nó, chúng tôi cố gắng tạo một tin nhắn.

Vì vậy, ở đây bạn thấy phiên ngữ cảnh, create_message.

Đây là mẫu.

Đây là mẫu.

Đây là yêu cầu tiêu chuẩn mà bạn sẽ gửi tới bất kỳ LLM nào

bạn sẽ thấy đối tượng tin nhắn.

Đó là đối tượng tin nhắn tiêu chuẩn.

Chúng tôi đang gửi tin nhắn mẫu với tư cách là người dùng,

nội dung là nội dung văn bản.

Vì vậy, trong trường hợp này, đó là những gì bạn thấy ở đây,

Viết một bài thơ haiku truyền thống về,

và sau đó là con vật, từ sự khơi gợi,

và cái đó được đưa vào.

Chúng tôi có mã thông báo tối đa là 100,

vì vậy ở đây bạn có thể định cấu hình lấy mẫu

chính xác như bạn muốn

khi bạn đang tương tác với bất kỳ LLM nào khác.

Sau đó chúng tôi chỉ ghi lại phản hồi và xuất ra.

Nhìn thấy điều này, câu hỏi mà bạn có thể có là LLM nào?

Điều gì sẽ xảy ra nếu khách hàng này có nhiều cái khác nhau?

Và đó là trường hợp ở đây trong Mã VS,

bởi vì chúng ta không nói về LLM

có sẵn từ đại lý, đó là một danh sách rất lớn.

Nếu tôi vào đại lý ở đây

và chỉ cần tạo một cái mới, nếu bạn sử dụng danh sách thả xuống này,

có rất nhiều mô hình khác nhau mà tôi có thể sử dụng.

Vậy hệ thống sẽ chọn mô hình nào?

Chà, đây là lúc mọi thứ trở nên thực sự thú vị.

Nếu bạn truy cập mcp.json,

nhấp vào Thêm và sau đó đi xuống,

bạn sẽ thấy Định cấu hình quyền truy cập mô hình.

Vì máy chủ MCP này đã tích hợp tính năng lấy mẫu,

vì vậy máy chủ MCP này đã tích hợp tính năng lấy mẫu,

bạn có thể định cấu hình quyền truy cập mô hình cho máy chủ MCP.

Vì vậy, đây không phải là biểu mẫu truy cập mô hình,

bất cứ điều gì đang xảy ra trên máy tính.

Đây là mô hình cụ thể của máy chủ MCP

có thể sử dụng để lấy mẫu.

Khi tôi nhấp vào đây,

Tôi nhận được danh sách tất cả các mẫu có sẵn trong hệ thống.

Đây là tất cả các mẫu có sẵn

tới GitHub Copilot.

Và từ đây tôi có thể chọn bất kỳ một trong những mô hình này

và nói, "Đây là cái

nó nên được sử dụng bất cứ lúc nào bạn đang lấy mẫu."

Và mặc định hiện nay là GPT-4.1.

Tôi sẽ để nó ở đó.

Điều đó có nghĩa là khi quá trình lấy mẫu được kích hoạt,

nó sẽ sử dụng GPT-4.1

để thực hiện thế hệ đó để thực hiện lấy mẫu.