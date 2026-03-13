# Tổng kết 01 khóa học

---

Chúc mừng bạn đã hoàn thành khóa học.

Bây giờ bạn đã đạt được sự hiểu biết toàn diện về

xây dựng các ứng dụng AI tự động với LangChain và LangGraph.

Bạn có thể bắt đầu khám phá các cơ hội để tiếp tục

học tập và áp dụng các kỹ năng đã học được.

Nhưng trước đó, hãy xem lại một số khái niệm chính

bạn đã học trong suốt khóa học.

AI sáng tạo là một hệ thống phản ứng tạo ra

nội dung như văn bản hoặc hình ảnh dựa trên lời nhắc.

Nó dừng lại khi tạo ra phản hồi.

Mặt khác, Agentic AI có tính chủ động

và sử dụng những gợi ý để theo đuổi mục tiêu thông qua

vòng lặp của việc ra quyết định, hành động và học tập.

Nó có thể hoạt động với sự can thiệp tối thiểu của con người, giúp nó tiến xa hơn

năng động và tự chủ hơn genAI truyền thống.

LangGraph cấu trúc quy trình làm việc AI một cách linh hoạt

đồ thị sử dụng các nút, cạnh và trạng thái chia sẻ.

Nó hỗ trợ vòng lặp, phân nhánh, duy trì trạng thái,

và chức năng con người trong vòng lặp, tạo ra

nó lý tưởng để xây dựng các tác nhân phức tạp, thích ứng.

LangChain giúp các nhà phát triển xây dựng dựa trên LLM

các ứng dụng sử dụng các thành phần mô-đun như

lời nhắc, bộ nhớ và công cụ.

Nó hoạt động tốt nhất cho quy trình công việc tuyến tính, từng bước.

Mặt khác, LangGraph mở rộng phạm vi hoạt động của LangChain

khả năng bằng cách cho phép trạng thái, đa tác nhân

quy trình công việc thông qua đồ thị của các nút và cạnh.

Đó là lý tưởng để xử lý các nhiệm vụ phức tạp liên quan đến

phân nhánh, bộ nhớ và bối cảnh dài hạn.

Đây là bản phân tích về cách LangGraph

cấu trúc và thực hiện các quy trình công việc có trạng thái.

TypedDict được sử dụng để xác định trạng thái có cấu trúc.

Trạng thái có thể bao gồm các loại phức tạp như danh sách,

từ điển lồng nhau hoặc chuỗi tin nhắn.

Các nút được liên kết với các chức năng biến đổi hoặc quan sát trạng thái.

Các cạnh xác định sự chuyển tiếp giữa các nút.

Các cạnh có điều kiện đánh giá trạng thái hiện tại để kiểm soát luồng.

Các hàm sử dụng giải nén trạng thái để cập nhật trạng thái một cách bất biến.

Và cuối cùng, StateGraph được biên dịch và

được thực thi với trạng thái ban đầu bằng cách sử dụng lệnh gọi.

Dưới đây là một cái nhìn nhanh về các tác nhân phản ánh.

Tác nhân phản ánh là hệ thống AI cải tiến lặp đi lặp lại

kết quả đầu ra bằng cách phân tích và tinh chỉnh các phản hồi trước đó.

Quá trình này bao gồm hai vai trò LLM cốt lõi, bộ tạo và bộ phản xạ.

Các tác nhân phản xạ cơ bản hoạt động trong phản hồi

các vòng lặp để tinh chỉnh kết quả qua nhiều lần lặp.

LangChain được sử dụng để thiết lập cấu trúc

lời nhắc và bộ nhớ cho từng vai trò của tác nhân.

Biểu đồ thông báo của LangGraph theo dõi tin nhắn

luồng và xác định trạng thái tác nhân qua các lượt

sử dụng các loại tin nhắn như tin nhắn của con người và tin nhắn AI.

Tiếp theo, đây là cái nhìn về các tác nhân phản xạ.

Các tác nhân phản xạ liên tục tinh chỉnh đầu ra AI

sử dụng các công cụ tự phê bình và bên ngoài.

Chúng khác với sự phản ánh cơ bản bằng cách tích hợp thời gian thực

dữ liệu và tạo ra các phản hồi có cấu trúc, được trích dẫn.

Đầu ra tuân theo một lược đồ với các trường được gắn nhãn

như phản hồi, phê bình và trích dẫn.

Vòng lặp này tiếp tục cho đến khi đạt được kết quả có thể kiểm chứng được.

Tiếp theo là các tác nhân ReAct, lý do

lặp đi lặp lại và chỉ sử dụng các công cụ khi cần thiết.

Luồng phản hồi có cấu trúc của họ là Suy nghĩ, Hành động,

Hành động đầu vào, quan sát và câu trả lời cuối cùng.

Agent duy trì lịch sử tin nhắn để thông báo cho từng bước lý luận.

Quá trình thực thi dừng khi không có lệnh gọi công cụ nào nữa

được yêu cầu, mang lại câu trả lời cuối cùng.

Dưới đây là cái nhìn về các hệ thống đa tác nhân, bao gồm

của các đại lý tự trị với vai trò chuyên biệt.

Họ tương tác thông qua quy trình làm việc có cấu trúc biểu đồ

sử dụng các mẫu cộng tác như quy trình

và các mô hình trục và nan hoa.

Các đại lý tổng hợp thường phối hợp các đại lý chuyên biệt,

cân bằng giữa chiều sâu chuyên môn với quản lý nhiệm vụ rộng.

Các khung điều phối như LangGraph,

CrewAI, AutoGen và BeeAI cho phép mở rộng và

hợp tác đại lý mô-đun.

Agentic RAG tăng cường RAG bằng cách cho phép LLM hoạt động

với tư cách là người đưa ra quyết định chứ không chỉ là người phản hồi.

Các đại lý lựa chọn phù hợp nhất

nguồn dữ liệu dựa trên ngữ cảnh truy vấn.

Nó tăng cường độ chính xác, khả năng thích ứng và

khả năng ứng dụng thực tế trong các ngành công nghiệp.

Nếu bạn chưa đăng ký học Chuyên nghiệp

Chương trình chứng chỉ, trong đó khóa học này

là một phần, chúng tôi khuyến khích bạn làm như vậy.

Tùy thuộc vào lịch trình của bạn và số lượng

của các khóa học trong chương trình, bạn có thể hoàn thành

nó trong khoảng hai đến sáu tháng.

Chúng tôi khuyên bạn nên tiếp tục áp dụng

kiến thức thu được từ khóa học này trong

sự nghiệp phát triển AI tác nhân.

Chúng tôi hy vọng những nguyên tắc này sẽ rèn luyện kỹ năng của bạn

và trao quyền cho bạn để thăng tiến một cách chuyên nghiệp.

Chúc mừng bạn đã hoàn thành khóa học này!

Chúng tôi đánh giá cao sự tham gia của bạn vào việc này

hành trình học tập và chúc bạn mọi điều tốt đẹp nhất!