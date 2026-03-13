# 02 tác nhân phản xạ xây dựng

---

Chào mừng bạn đến với video này về cách xây dựng Tác nhân phản xạ.

Trong video này, bạn sẽ xây dựng Tác nhân phản xạ bằng cách

áp dụng kỹ thuật nhanh chóng và thiết kế lược đồ.

Bạn sẽ phân tích các phản hồi của AI và đầu ra của lệnh gọi công cụ, đồng thời tạo

một vòng phản hồi lặp lại bằng cách sử dụng các nút Replyer và Revisor.

Cuối cùng, bạn sẽ đánh giá cách trích dẫn được hỗ trợ

các sửa đổi cải thiện độ sâu của phản hồi.

Để xây dựng Tác nhân phản xạ, hãy bắt đầu với

nhập khẩu thiết yếu để thiết lập môi trường của bạn.

Bước tiếp theo là cấu hình Tavily

Công cụ tìm kiếm để sử dụng trong quy trình làm việc của đại lý của bạn.

Thiết lập khóa API cho dịch vụ Tavily Search.

Tạo phiên bản công cụ Tavily Search trả về tối đa 5 kết quả cho mỗi truy vấn.

Kiểm tra công cụ tìm kiếm bằng truy vấn mẫu về công thức bữa sáng.

Phương thức gọi thực hiện tìm kiếm và trả về kết quả có cấu trúc.

Kết quả tìm kiếm trả về dưới dạng danh sách JSON

từ điển, mỗi từ điển có một từ điển chứa

các khóa như tiêu đề, URL và nội dung.

Tiếp theo, tạo một phiên bản của mô hình ChatOpenAI bằng GPT.

Gửi câu hỏi đến LLM và trích xuất câu trả lời bằng văn bản, chẳng hạn như,

Bạn có ý tưởng nào cho bữa sáng lành mạnh không?

Câu trả lời là những lời khuyên chung chung, như việc ăn uống

bột yến mạch, sữa chua Hy Lạp hoặc bánh mì nướng bơ.

Mục đích là tạo ra Tác nhân phản xạ

tạo ra những gì tiên tiến nhất, nhưng

chưa được chứng minh, ý tưởng sức khỏe.

Tác nhân sử dụng Phản xạ để cải thiện và phát triển các phản hồi của mình theo thời gian.

Tạo một thông báo hệ thống để báo cho LLM biết

cư xử như Tiến sĩ Paul Saladino, chuyên

trong những cách tiếp cận gây tranh cãi như chế độ ăn thịt và nhịn ăn kéo dài.

First_instruction là một biến để thay đổi lời nhắc.

Điền vào biến lệnh đầu tiên bằng một

lời nhắc cụ thể yêu cầu phản hồi 250 từ.

Kết nối LLM với thông báo hệ thống.

Mô hình lúc này sẽ hoạt động theo

tính cách được xác định, như được minh họa trong sơ đồ.

Thiết lập này chỉ nhằm mục đích trình diễn.

Vượt qua cùng một câu hỏi.

LLM phản hồi bằng gợi ý về động vật ăn thịt

chế độ ăn kiêng, một chế độ ăn kiêng có thể có một số lợi ích nhưng

thường không được các cơ quan y tế chính thống khuyến cáo.

Bây giờ thay đổi đầu ra LLM để phù hợp với yêu cầu.

Tạo lược đồ hoặc lớp phản ánh.

Các trường mô tả chức năng của từng trường.

LLM xuất ra trường bị thiếu cho nội dung

thông tin là cần thiết và những thông tin thừa

trường cho những gì không cần thiết.

Lớp AnswerQuestion bao gồm

câu trả lời, phản ánh và truy vấn tìm kiếm.

Lớp Reflection được khởi tạo trong lớp AnswerQuestion.

LLM cuối cùng xuất ra một đối tượng JSON với các thuộc tính đã được điền.

Giống như trước đây, xâu chuỗi LLM vào thông báo hệ thống.

Đây sẽ là một nút trong biểu đồ LangGraph.

Bạn cũng cần liên kết LLM với

Lược đồ AnswerQuestion sử dụng phương thức bind_tools.

Về cơ bản, LLM sẽ coi lớp AnswerQuestion giống như một hàm.

Truyền cùng một thông điệp với cùng một câu hỏi.

LLM phản hồi bằng đề xuất về chế độ ăn dành cho động vật ăn thịt.

Kết quả không phải là văn bản mà là tin nhắn AI

lớp chứa nhiều thông tin.

Nhưng để phản ánh, trọng tâm là thuộc tính tool_calls.

Thuộc tính tool_calls chứa

tên lớp của các cặp khóa-giá trị

chẳng hạn như câu trả lời, phản ánh, thiếu, và

không cần thiết với kết quả đầu ra văn bản tương ứng của họ.

Response_list sẽ được sử dụng để kiểm tra quy trình trong một lần lặp.

Nó sẽ tương tự như biến trạng thái trong LangGraph.

Thêm câu hỏi của người dùng và thêm câu trả lời từ người trả lời.

Bạn có thể trích xuất các truy vấn tìm kiếm từ phản hồi.

Nhưng hãy tạo một hàm LangGraph cho mục đích này.

Tạo hàm trích xuất truy vấn tìm kiếm

từ thông báo phản hồi dưới dạng nút cho LangGraph.

Nút này cũng sẽ được sử dụng cho trình sửa đổi.

Trạng thái sẽ giống như danh sách phản hồi.

Trích xuất thông báo AI từ trạng thái.

Tiếp theo, trích xuất các tham số lệnh gọi công cụ.

Nhận các truy vấn tìm kiếm từ LLM.

Gọi công cụ tìm kiếm và gói kết quả trong một thông báo công cụ.

Gọi công cụ và thêm phản hồi của công cụ vào reply_list.

Có rất nhiều mẫu nhắc nhở Reflexion.

Thêm thông báo hệ thống sửa đổi hướng dẫn

LLM hành động như Tiến sĩ Peter Accia, một chuyên gia về

tuổi thọ và sức khỏe dựa trên bằng chứng,

và hỗ trợ các câu trả lời bằng bằng chứng.

Cập nhật mẫu lời nhắc để phản ánh vai trò chuyên gia này.

Tạo một lược đồ cho người sửa đổi.

Lớp này là một lớp con của lược đồ câu hỏi trả lời,

vì vậy nó sẽ có các trường giống nhau và danh sách trích dẫn.

Xâu chuỗi thông báo hệ thống và liên kết LLM với lược đồ câu trả lời sửa đổi.

Đây là một nút khác trong biểu đồ LangGraph.

Trình sửa đổi chuyển danh sách phản hồi tới revisor_chain.

Kết quả là một tin nhắn AI.

Thuộc tính args tool_call có tất cả

các cặp khóa-giá trị của lược đồ.

Nối phản hồi vào danh sách phản hồi.

Bây giờ bạn có thông báo AI thứ hai từ người sửa đổi.

Bạn có thể lặp đi lặp lại việc cung cấp dữ liệu đầu vào cho công cụ.

Tạo một hàm nút có điều kiện đếm

thông báo công cụ như một proxy cho số lượng

lặp lại giữa trình sửa đổi và các công cụ tìm kiếm.

Nó sẽ đếm mỗi lần công cụ được gọi.

Xây dựng biểu đồ bằng cách nhập các thành phần cần thiết.

Sau đó khởi tạo biểu đồ thông báo và đặt giới hạn lặp lại tối đa là 4.

Để tạo biểu đồ, trước tiên hãy thêm phản hồi

nút vào biểu đồ sử dụng init_chain.

Sau đó, thêm nút exec_tools chạy

truy vấn tìm kiếm được tạo bởi nút dự thảo.

Cuối cùng, thêm nút "revisor" sử dụng

revisor_chain để cải thiện bản nháp

phản hồi bằng cách sử dụng kết quả tìm kiếm và phê bình ban đầu.

Tiếp theo, kết nối nút phản hồi để thực thi các công cụ thông qua một cạnh.

Và kết nối công cụ với bộ chỉnh sửa thông qua một cạnh.

Tiếp theo, thêm điểm bắt đầu và kết thúc.

Đầu tiên, thêm một cạnh có điều kiện từ

trình sửa đổi thông qua hàm event_loop để

quyết định nên tiếp tục lặp lại hay kết thúc.

Nút kết thúc được ẩn trong event_loop.

Điều này tạo ra phản hồi sau một số lần lặp đã đặt.

Cuối cùng, đặt điểm vào thành nút phản hồi dự thảo.

Đây là nơi truy vấn được xử lý đầu tiên.

Biên dịch biểu đồ.

Nhập truy vấn, tôi bị tiền tiểu đường và cần

làm giảm lượng đường trong máu và tôi có vấn đề về tim.

Kết quả là một thông điệp của con người theo sau là

một danh sách các thông báo công cụ và AI xen kẽ.

Bạn có thể trích xuất câu trả lời từ phản hồi của AI.

Người phản hồi ban đầu đã đưa ra quan điểm ủng hộ chung

về dinh dưỡng dựa vào động vật, khuyến nghị

trứng, thịt mỡ và nội tạng, đồng thời tránh ăn ngũ cốc

và thực phẩm thực vật dựa trên triết lý dinh dưỡng rộng rãi.

Đây không phải là lời khuyên y tế.

Tương tự, bạn có thể nhận được câu trả lời từ lần lặp lại của trình sửa đổi cuối cùng.

Người sửa đổi đã cải thiện nó bằng cách thêm năm

trích dẫn, kết quả có thể đo lường được như sau bữa ăn

mức đường huyết và hướng dẫn chính xác hơn

phân biệt thực phẩm đã qua chế biến với thực phẩm chưa qua chế biến.

Mặt khác, không có phản hồi nào giải quyết thỏa đáng

mối quan tâm về sức khỏe tim mạch ngay từ đầu

truy vấn, thay vào đó tập trung vào quản lý lượng đường trong máu

trong khi phần lớn bỏ qua các khía cạnh tim mạch.

Trong video này, bạn đã học được rằng

Một công cụ tìm kiếm như Tavily có thể được cấu hình và

được viện dẫn để tăng cường phản hồi của AI với dữ liệu bên ngoài.

Hướng dẫn thiết kế sơ đồ và kỹ thuật nhanh chóng

LLM để tạo ra sự phản ánh có cấu trúc

và câu trả lời tập trung.

Câu hỏi trả lời và lược đồ phản ánh

nắm bắt câu trả lời, cờ bị thiếu hoặc không liên quan

chi tiết và tạo ra các truy vấn.

Kết quả đầu ra của công cụ như trường tool_calls và lược đồ

giúp trích xuất thông tin chi tiết có cấu trúc từ các tin nhắn AI.

Các nút phản hồi và sửa đổi chuỗi LangGraph

vào một vòng phản hồi lặp lại bằng cách sử dụng dấu nhắc

cập nhật và sửa đổi dựa trên bằng chứng.

Một biểu đồ thông báo sắp xếp tác nhân Phản xạ,

quản lý định tuyến nút, giới hạn lặp lại và luồng điều khiển.