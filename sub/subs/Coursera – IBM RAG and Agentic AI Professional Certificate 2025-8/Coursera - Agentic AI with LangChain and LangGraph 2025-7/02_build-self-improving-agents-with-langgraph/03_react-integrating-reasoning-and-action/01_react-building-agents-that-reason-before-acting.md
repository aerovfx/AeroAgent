# 01 tác nhân xây dựng phản ứng-lý do trước khi hành động

---

Chào mừng bạn đến với video này trên ReAct: Xây dựng các đại lý có lý do trước khi hành động.

Trong video này, bạn sẽ khám phá cách React kích hoạt tác nhân suy luận từng bước. Bạn sẽ

xác định các thành phần chính như suy nghĩ, hành động và quan sát.

Bạn sẽ xây dựng một tác nhân React đang hoạt động trong LangGraph.

Và cuối cùng, bạn sẽ phân tích cách nhân viên xử lý thông qua các cuộc gọi công cụ để tạo ra kết quả cuối cùng

phản hồi.

Tác nhân phản ứng được thiết kế cho các nhiệm vụ phức tạp đòi hỏi phải suy luận từng bước. Ví dụ,

bạn có thể bắt đầu với lời nhắc hệ thống như,

Bạn là trợ lý AI hữu ích, suy nghĩ từng bước và sử dụng các công cụ khi cần.

Bạn cũng có thể nhắc LLM phản hồi theo những cách sau.

Xác định thông tin cần thiết. Sử dụng các công cụ khi thích hợp.

Nhận câu trả lời rõ ràng và hữu ích. Và cuối cùng, hãy xem qua quá trình lý luận của nó.

Thông báo hệ thống sẽ hướng dẫn LLM định dạng đầu ra của nó bằng cách sử dụng mẫu có cấu trúc.

Đầu tiên, nó bắt đầu với Suy nghĩ, nơi LLM đưa ra lý do về những việc cần làm tiếp theo.

Sau đó đến Action, tên của công cụ sẽ sử dụng.

Tiếp theo là Hành động đầu vào, đầu vào được cung cấp cho công cụ đã chọn.

Sau đó là Quan sát, kết quả được công cụ trả về.

Và sau đó là Câu trả lời cuối cùng, câu trả lời hoàn chỉnh cho người dùng dựa trên những gì công cụ trả về.

Hãy bắt đầu với một ví dụ đơn giản. Bạn là khách du lịch thường xuyên sở hữu nhiều căn hộ

ở các thành phố khác nhau và truy cập vào LLM có thể sử dụng hai công cụ.

Một công cụ tìm kiếm cung cấp thời tiết hiện tại.

Và một công cụ gợi ý quần áo gợi ý nên mặc gì dựa trên những gì có trong tủ quần áo của bạn.

Trong sơ đồ khối, LLM được hiển thị bằng màu xanh lam.

Hộp màu xanh lá cây đại diện cho môi trường.

LLM phải tương tác với môi trường thông qua các công cụ này.

Nó suy luận từng bước, sử dụng phản hồi của công cụ và lặp lại để đưa ra câu trả lời cuối cùng.

Trong trường hợp này, nên mặc gì.

Hãy xem xét câu hỏi, thời tiết ở Tokyo thế nào và tôi nên mặc gì?

LLM phải sử dụng các công cụ để lấy dữ liệu từ môi trường, trong trường hợp này là dữ liệu hiện tại

thời tiết và kiểm tra xem quần áo nào có sẵn bằng công cụ đề xuất quần áo.

LLM đưa ra ý nghĩ, trước tiên tôi cần tra cứu thời tiết ở Tokyo.

LLM xác định hành động, trong trường hợp này là sử dụng công cụ tìm kiếm.

Đồng thời, LLM tạo ra đầu vào hành động, thời tiết Tokyo hôm nay.

Điều này đóng vai trò là đầu vào cho công cụ, từ đó tương tác với môi trường để truy xuất

những thông tin liên quan.

Công cụ trả về một quan sát sau khi truy cập vào môi trường.

Tokyo có nhiệt độ 22°C với bầu trời đầy nắng.

Lịch sử quan sát và trò chuyện được chuyển trở lại LLM.

Lịch sử trò chuyện luôn được bao gồm, ngay cả khi không được hiển thị rõ ràng.

LLM lấy thông tin đầu vào mới và xử lý một ý nghĩ.

Bây giờ tôi nên khuyên bạn nên mặc quần áo khi thời tiết nắng 22°C.

Tiếp theo, hành động.

Nó chọn công cụ recommend_clothing.

Đầu vào hành động được tạo ra, thời tiết nắng 22°C.

Sau khi quan sát, nên mặc quần áo nhẹ, áo phông, quần short, kính râm.

Cuối cùng, LLM đạt được suy nghĩ cuối cùng.

Bây giờ nó có tất cả thông tin nó cần.

Nó cung cấp câu trả lời cuối cùng.

Tokyo hôm nay nhiệt độ 22°C và có nắng.

Tôi khuyên bạn nên mặc quần áo nhẹ như áo phông, quần short và kính râm.

Vì không còn lệnh gọi công cụ nào nữa nên quá trình kết thúc tại đây.

Bây giờ hãy xem cách triển khai điều này trong LangGraph.

Ví dụ về mã bạn sắp xem xét nhấn mạnh tính đơn giản bằng cách giảm thiểu lược đồ,

lời nhắc và các chức năng phụ trợ.

Nó hoạt động tốt cho các trường hợp sử dụng cơ bản, nhưng hãy tham khảo tài liệu LangGraph để biết thêm thông tin nâng cao

triển khai.

Xác định công cụ tìm kiếm bằng cách gói đối tượng TavilySearchResults bằng công cụ trang trí @.

Tạo công cụ recommend_clothing để phân tích các từ khóa trong phản hồi của LLM,

chẳng hạn như mưa hoặc ướt, để gợi ý trang phục phù hợp, như được mô tả trong chuỗi tài liệu.

Lược đồ về cơ bản là một trạng thái giống như từ điển trong đó khóa là thông điệp và giá trị

là danh sách ngày càng tăng các tin nhắn được trao đổi trong cuộc trò chuyện.

Sequence[BaseMessage] chứa danh sách bất kỳ loại tin nhắn nào, HumanMessage, AIMessage hoặc

Công cụMessage.

Add_messages nối thêm tin nhắn mới mỗi khi nút chạy.

Cần có chú thích để biến trường thông báo về dạng chính xác để LangGraph

biết áp dụng add_messages.

Đối tượng trạng thái tác nhân hoạt động giống như một từ điển trong đó các thông điệp là khóa và giá trị của nó là một

list lưu trữ tất cả các tin nhắn được trao đổi trong cuộc trò chuyện.

Tiếp theo, tải mô hình GPT bằng trình bao bọc OpenAI của Lengchain.

Sau đó, tạo danh sách các công cụ và từ điển ánh xạ tên của từng công cụ vào chính công cụ đó.

Xác định thông báo hệ thống hướng dẫn tổng đài viên phản hồi từng bước và sử dụng các công cụ

khi cần thiết.

Biến Agent_scratchpad tự động lưu trữ lịch sử lý luận theo định dạng.

Suy nghĩ, hành động, đầu vào hành động, quan sát, cùng với trình tự đầu vào của người dùng.

Mặc dù nhiều triển khai lưu trữ thông tin đầu vào, câu hỏi và thông báo công cụ của người dùng một cách riêng biệt,

để cho ngắn gọn, hãy lưu trữ mọi thứ trong bảng ghi nhớ.

Tiếp theo, xâu chuỗi lời nhắc vào mô hình và liên kết các công cụ để tạo thành tác nhân.

Xác định nút đầu tiên trong biểu đồ, nút này có trạng thái tác nhân.

Trạng thái được chuyển đến mô hình thông qua Scratch_pad.

Phản hồi của mô hình được trả về và thêm vào lịch sử tin nhắn.

Tạo một công cụ gọi node.

Tạo biểu đồ mới sử dụng trạng thái tác nhân để theo dõi dữ liệu.

Thêm một nút có tên là tác nhân chạy hàm call_model.

Tiếp theo, thêm một nút có tên là tools chạy hàm tool_node.

Cuối cùng, thêm một cạnh từ tác nhân đến công cụ.

Xác định hàm Should_continue để kiểm soát luồng của tác nhân.

Ghép nối nó với một cạnh có điều kiện để quyết định bước tiếp theo.

Nó lấy trạng thái từ tác nhân và lấy tin nhắn cuối cùng.

Dựa trên thông báo đó, biểu đồ sẽ định tuyến đến nút công cụ hoặc nút kết thúc.

Nếu tin nhắn không có lệnh gọi công cụ, nó sẽ trả về kết thúc.

Điều này ánh xạ tới nút cuối trong biểu đồ.

Nếu không, nó sẽ trả về tiếp tục và các bản đồ cạnh có điều kiện sẽ tiếp tục đến nút công cụ.

Ở đây, tác nhân được đặt ở nút bắt đầu của biểu đồ.

Nó biên dịch quy trình làm việc thành một biểu đồ có thể thực thi được.

Chức năng này sẽ giúp in ra kết quả từ biểu đồ.

Xác định thông báo đầu vào từ người dùng để bắt đầu biểu đồ.

Thời tiết ở Zürich như thế nào?

Và tôi nên mặc gì dựa trên nhiệt độ?

Tiếp theo, chạy biểu đồ và in từng bước cập nhật trạng thái bằng print_stream

chức năng.

Có thể thấy dấu vết của quá trình lý luận đầy đủ bắt đầu từ thông điệp của con người.

Thông báo AI đầu tiên bao gồm lệnh gọi công cụ tới công cụ tìm kiếm cùng với các tham số của nó.

Công cụ trả về một kết quả.

Tin nhắn AI thứ hai gọi đến công cụ gợi ý quần áo.

Kết quả công cụ thứ hai được thêm vào trạng thái.

Cuối cùng, LLM tạo thông báo AI cuối cùng với câu trả lời hoàn chỉnh.

Bạn có thể phác họa những gì đang xảy ra trong biểu đồ.

Tin nhắn ban đầu của con người được chuyển đến call_model thông qua trạng thái.

LLM phản hồi và một thông báo AI được thêm vào biến thông báo trạng thái.

Trạng thái sau đó được chuyển đến nút Should_continue.

Tin nhắn cuối cùng, tin nhắn AI, được trích xuất từ ​​trạng thái.

Nếu nó bao gồm lệnh gọi công cụ, cạnh có điều kiện sẽ tiếp tục trả về và định tuyến đến công cụ

nút.

Tương tự, nút công cụ trích xuất lệnh gọi công cụ từ trạng thái.

Tên công cụ được xác định.

Các tham số dao được chọn dựa trên dao đã chọn.

Kết quả được gói trong một thông báo công cụ và gửi lại cho mô hình.

Quá trình này lặp lại cho đến khi không còn lệnh gọi công cụ nào được thực hiện nữa.

Tại thời điểm đó, phản hồi cuối cùng được tạo ra.

Biểu đồ đạt đến nút cuối.

Trong video này, bạn đã học được rằng

Tác nhân phản ứng thực hiện lý luận từng bước và sử dụng các công cụ để trả lời các truy vấn phức tạp.

Đầu ra của họ tuân theo một định dạng có cấu trúc.

Suy nghĩ ➝ hành động ➝ hành động đầu vào ➝ quan sát ➝ câu trả lời cuối cùng.

Kết quả của công cụ (quan sát) phản hồi lại quá trình suy luận để hướng dẫn các bước tiếp theo.

LangGraph được sử dụng để triển khai quy trình làm việc React kết nối các nút công cụ và lý do.

Quá trình tiếp tục cho đến khi tạo ra câu trả lời cuối cùng mà không cần gọi thêm công cụ nào nữa.