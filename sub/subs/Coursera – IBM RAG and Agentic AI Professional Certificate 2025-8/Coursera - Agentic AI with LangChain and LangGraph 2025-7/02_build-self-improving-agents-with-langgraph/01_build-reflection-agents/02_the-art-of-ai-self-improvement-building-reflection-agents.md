# 02 the-art-of-ai-tự-hoàn thiện-xây dựng-phản ánh-đại lý

---

Chào mừng bạn đến với video này về Nghệ thuật tự cải thiện trí tuệ nhân tạo: Xây dựng tác nhân phản ánh.

Trong video này, bạn sẽ khám phá khái niệm về các tác nhân phản chiếu cơ bản, hiểu biết

cách họ liên tục cải thiện kết quả đầu ra AI cũng như cách thiết lập vai trò trình tạo và phản xạ

để tự sửa lỗi.

Sau đó, bạn sẽ học cách áp dụng cả LengChain và LengGraph để phát triển đại lý.

xây dựng và chạy một tác nhân phản ánh hoàn chỉnh nhằm tinh chỉnh nội dung của chính nó.

Hãy tưởng tượng một AI được cải thiện bằng cách học hỏi từ những sai lầm.

Đây là cốt lõi của tác nhân phản ánh, được thiết kế để phân tích hiệu suất và nâng cao chiến lược

phê phán.

Tác nhân phản xạ chủ yếu chia thành ba loại, tác nhân phản xạ cơ bản, tác nhân phản xạ,

và tìm kiếm cây tác nhân ngôn ngữ, hoặc LATS.

Video này tập trung vào các tác nhân phản chiếu cơ bản.

Hãy xem xét lời nhắc của người dùng, làm thế nào để tôi trông ngầu?

Điều này kích hoạt hai vai trò LLM.

Máy phát điện gợi ý ý tưởng ban đầu - "Hãy đội mũ fedora."

Người phản ánh đánh giá và phê bình nó.

Fedoras đã lỗi thời và thường bị rập khuôn tiêu cực.

Vòng lặp này chạy trong một số bước đã đặt, tinh chỉnh phản hồi trước khi trả về

câu trả lời cuối cùng.

Đối với lần lặp thứ hai, trình tạo sẽ tạo ra phản hồi được cải thiện.

Mặc quần áo vừa vặn, có tư thế tốt và tự tin.

Tính xác thực đang cố gắng để trông thật ngầu.

Bộ phản xạ đánh giá phản hồi được cải thiện.

Lời khuyên tốt tập trung vào tính xác thực hơn là các mặt hàng cụ thể.

Có thể thêm một cái gì đó về phong cách cá nhân.

Máy phát điện cung cấp đầu ra cuối cùng.

Tìm quần áo phù hợp với phong cách cá nhân của bạn, duy trì tư thế tốt và tự tin.

Sự ngầu thực sự đến từ sự chân thực, không chạy theo xu hướng.

Vì vậy, một cuộc khủng hoảng đã được ngăn chặn.

Không còn mũ fedora nữa, chỉ có những rung cảm hoàn hảo!

Bạn sẽ sử dụng sự phản chiếu để xây dựng tác nhân tối ưu hóa bài đăng trên LinkedIn.

Tác nhân sẽ tạo một bài đăng, phê bình kết quả đầu ra của chính nó và tinh chỉnh nội dung nhiều lần.

Bạn sẽ xây dựng một hệ thống với giai đoạn hậu tạo, sau đó là giai đoạn phản ánh hoặc đánh giá AI

giai đoạn.

Chu kỳ này đảm bảo nội dung chất lượng cao hơn.

Ban đầu, trình tạo truy cập HumanMessage và tạo ra kết quả đầu ra.

Bộ phản xạ sử dụng cả đầu ra của bộ tạo và thông báo gốc.

Cả bộ tạo và bộ phản xạ đều tích lũy quyền truy cập vào các đầu ra trước đó, xây dựng bộ nhớ

qua các lần lặp lại.

Bắt đầu bằng cách khởi tạo tác nhân LLM sẽ tạo và phê bình nội dung.

Trong ví dụ này, bạn sẽ sử dụng mô hình Granite của IBM thông qua LangChain.

Để hướng dẫn trình tạo LLM, hãy sử dụng mẫu lời nhắc trò chuyện của LangChain.

SystemMessage xác định vai trò của LLM.

Phần giữ chỗ của tin nhắn đóng vai trò là bộ nhớ, duy trì đầu vào của người dùng cho trình tạo.

Sử dụng toán tử pipe, kết nối dấu nhắc có cấu trúc với LLM, tạo generate_chain.

Tương tự, tạo lời nhắc cho LLM phản ánh trong đó trợ lý đánh giá dữ liệu được tạo

Bài đăng trên LinkedIn.

Xác định lời nhắc phản ánh bằng cách sử dụng mẫu lời nhắc trò chuyện bao gồm SystemMessage

đóng khung mô hình như một nhà chiến lược nội dung LinkedIn chuyên nghiệp.

Bao gồm phần giữ chỗ của tin nhắn để chèn bài đăng cần phê bình.

Cuối cùng, xâu chuỗi lời nhắc tới LLM bằng toán tử đường ống.

Sử dụng LangGraph để xây dựng quy trình làm việc hội thoại bằng cách xác định trạng thái tổng đài viên, một cấu trúc giúp

theo dõi bối cảnh đang phát triển.

LangGraph đơn giản hóa việc này bằng MessageGraph, một loại biểu đồ đặc biệt có trạng thái chỉ chứa

một mảng tin nhắn, chẳng hạn như HumanMessage, AIMessage, SystemMessage.

Hãy coi MessageGraph như một biểu đồ trạng thái chuyên biệt tích lũy các loại thông báo khác nhau.

Mỗi lượt người dùng sẽ thêm HumanMessage, sau đó là AIMessage.

Để xây dựng nút tạo, hãy nhập BaseMessage, HumanMessage và AIMessage cho tin nhắn

các loại.

Nhập danh sách và trình tự nhập dữ liệu.

Công cụ này nhận và trả về một đối tượng giống như danh sách của BaseMessages.

Nút tạo lấy biến trạng thái làm đầu vào bao gồm HumanMessage ban đầu,

làm cho tôi trông thật ngầu trên LinkedIn.

HumanMessage đầu vào được chuyển tới hàm gọi dưới dạng trạng thái.

Chuỗi sử dụng bối cảnh đó để tạo ra câu trả lời, "Hãy đội mũ fedora và đeo kính râm trong

ảnh hồ sơ của bạn."

Cuối cùng, hàm trả về kết quả, được gói trong AIMessage và sẵn sàng cho

giai đoạn tiếp theo trong quy trình làm việc.

Biến trạng thái chứa thông báo đầu vào dưới dạng danh sách.

Khi nút trả về một phản hồi, nó ngầm cập nhật biến trạng thái, thêm vào

Tin nhắn AIM.

LangGraph xử lý việc này bằng cơ chế hợp nhất được tối ưu hóa.

Hàm Reflect_node cải thiện phản hồi do AI tạo ra từ Generation_node.

Nó hoạt động như một cơ chế phê bình, phân tích bối cảnh hội thoại và phản hồi

để tinh chỉnh đầu ra.

Nó nhận các tin nhắn, một chuỗi các đối tượng BaseMessage và chuyển chúng vào Reflect_chain.

Chuỗi trả về một lời phê bình sâu sắc về đầu ra AI cuối cùng.

Bài phê bình này được gói gọn trong HumanMessage vì Generation_node mong đợi

đầu vào của con người;

việc trả lại AIMessage sẽ phá vỡ vòng phản hồi.

Bằng cách sử dụng HumanMessage, tác nhân phản chiếu sẽ giao tiếp với nút tạo với tư cách là người dùng, yêu cầu

sàng lọc đầu ra hiện có.

Tiếp theo, thêm nút tạo vào biểu đồ bằng phương thức add_node, cung cấp

một tên duy nhất, tạo và hàm để thực thi thế hệ_node.

Thêm nút phản ánh theo cách tương tự.

Tiếp theo, xác định luồng thực thi giữa các nút bằng hàm add_edge,

tạo ra sự kết nối một chiều từ sự phản ánh trở lại thế hệ.

Đặt điểm vào của quy trình công việc bằng cách sử dụng set_entry_point, chỉ định

nút tạo.

Điều này bắt đầu với phản hồi ban đầu dựa trên thông tin đầu vào hoặc lịch sử của người dùng.

Thêm nút bộ định tuyến để kiểm soát luồng của biểu đồ.

Nhập nút cuối, nút này đánh dấu việc chấm dứt quy trình làm việc.

Hàm Should_continue kiểm tra lịch sử tin nhắn.

Nếu tin nhắn vượt quá 6, nó sẽ kết thúc quy trình làm việc.

Nếu không, nó sẽ định tuyến để phản ánh.

Các thiết lập nâng cao hơn có thể sử dụng LLM để đưa ra quyết định.

Các liên kết phương thức add_conditional_edges tạo ra để phản ánh hoặc

end dựa trên đầu ra Should_continues.

Bước cuối cùng là biên dịch quy trình làm việc bằng hàm biên dịch.

Để kiểm tra, hãy xác định thông tin đầu vào ban đầu của người dùng bằng HumanMessage.

Viết một bài đăng trên LinkedIn về việc xin việc làm nhà phát triển phần mềm tại IBM dưới 160 ký tự.

Thông báo này khởi động giai đoạn tạo.

Cuối cùng, chạy quy trình làm việc bằng hàm gọi, kích hoạt vòng lặp đầy đủ cho đến khi

đầu ra cuối cùng.

Đây là một ví dụ về tác nhân phản chiếu đang hoạt động.

Khi bạn gọi quy trình làm việc, phản hồi là danh sách các thông báo.

HumanMessage đầu vào đi tới nút tạo, tạo ra bản nháp đầu tiên của LinkedIn

bài viết.

AIMessage này và lời nhắc ban đầu chuyển đến nút phản ánh, nút này sẽ phê bình và đề xuất

cải tiến, được gói gọn dưới dạng HumanMessage.

Phản hồi đó sẽ quay trở lại nút tạo, tạo ra AIMessage bài đã được sửa đổi.

Quá trình này lặp đi lặp lại, bổ sung thêm những lời phê bình và phản hồi cho nhà nước, liên tục cải thiện.

AIMessage cuối cùng là bài viết tinh tế của bạn.

Trong video này, bạn đã biết rằng tác nhân phản chiếu liên tục cải thiện kết quả đầu ra của AI bằng cách

phân tích hiệu suất của họ thông qua một vòng phản hồi.

Trình tạo tạo ra nội dung, trong khi phản xạ cung cấp phản hồi quan trọng.

Kỹ thuật nhanh chóng với LengChain hướng dẫn LLM trong việc tạo nội dung và phản ánh cấu trúc

thông qua các mẫu lời nhắc trò chuyện động và phần giữ chỗ tin nhắn.

Trạng thái tác nhân trong LengGraph được xác định thông qua MessageGraph.

Nó theo dõi cuộc trò chuyện, tích lũy tin nhắn và bối cảnh qua các lần lặp lại.

Xây dựng đồ thị bao gồm việc xác định các nút, kết nối chúng với các cạnh, thiết lập một mục

điểm và sử dụng các nút của bộ định tuyến để đưa ra quyết định động và lặp lại các vòng lặp.