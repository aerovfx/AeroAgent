# Tổng kết 01 khóa học

---

Chúc mừng bạn đã hoàn thành khóa học này! Bây giờ bạn đã có sự hiểu biết toàn diện

về cách bắt đầu với RAG với Gradio và LlamaIndex. Tiếp theo là lúc khám phá

cơ hội để tiếp tục học tập và áp dụng các kỹ năng mới của bạn. Nhưng trước đó, hãy

xem lại một số khái niệm chính bạn đã học trong suốt khóa học này.

Bạn đã biết rằng Thế hệ tăng cường truy xuất, hay RAG, là một kỹ thuật máy học

kết hợp việc truy xuất thông tin với AI tổng hợp để tạo ra các phản hồi chính xác, nhận biết ngữ cảnh.

RAG cải thiện LLM bằng cách tích hợp kiến thức bên ngoài hoặc kiến thức theo miền cụ thể mà không cần đào tạo lại,

giúp họ tạo ra kết quả đầu ra chuyên biệt và chính xác hơn.

Bạn đã biết rằng RAG bao gồm một số bước, có thể tóm tắt như sau:

Đầu tiên, trong quá trình nhúng văn bản và mã hóa lời nhắc, lời nhắc và tài liệu được chia thành nhiều phần

và chuyển đổi thành các vectơ chiều cao bằng cách sử dụng các mô hình AI như Bộ mã hóa hai chiều

Đại diện từ Transformers, được gọi là BERT và Generative Pre-training Transformers

hoặc GPT. Tiếp theo, trong quá trình truy xuất, tài liệu liên quan

vectơ được truy xuất dựa trên số liệu khoảng cách, chẳng hạn như tích số chấm hoặc độ tương tự cosine.

Sau đó, trong quá trình tạo truy vấn nâng cao, nội dung được truy xuất sẽ được kết hợp với lời nhắc của người dùng.

Và cuối cùng, trong quá trình tạo mô hình, hệ thống sử dụng dấu nhắc tăng cường để tạo

một phản hồi thông tin, chính xác.

Bây giờ bạn cũng biết rằng RAG bao gồm hai thành phần chính là Retriever và Generator.

Retriever tìm thấy dữ liệu liên quan từ cơ sở kiến thức và Generator sử dụng dữ liệu đã truy xuất

dữ liệu để tạo ra phản hồi bằng ngôn ngữ tự nhiên. Các nhà phát triển và nhà khoa học dữ liệu sử dụng RAG vì

RAG chỉ truy xuất thông tin phù hợp nhất, đảm bảo phản hồi chính xác, theo miền cụ thể,

và cập nhật mà không cần đào tạo lại mô hình. Và bạn biết rằng RAG kích hoạt chatbot và

Hệ thống AI cung cấp các câu trả lời chuyên biệt, đáng tin cậy bằng cách tích hợp kiến thức bên ngoài,

làm cho chúng trở nên đáng tin cậy đối với các chủ đề bí mật hoặc đặc thù của ngành.

Tiếp theo, bạn đã tìm hiểu về cách Gradio, một thư viện Python nguồn mở, có thể tạo các ứng dụng dựa trên web có thể tùy chỉnh.

giao diện người dùng, đặc biệt đối với các mô hình học máy và các công cụ tính toán.

Bạn có thể chia sẻ giao diện Gradio thông qua các URL duy nhất, tạo điều kiện cộng tác dễ dàng và

thu thập phản hồi. Thiết lập giao diện Gradio gồm 4 bước, viết code Python,

tạo giao diện, khởi chạy máy chủ web và truy cập giao diện web.

Gradio cung cấp các công cụ sau mà bạn có thể sử dụng để xây dựng các khả năng vào ứng dụng web.

"gr.Textbox" cho phép người dùng nhập văn bản vào ứng dụng hoặc hiển thị văn bản từ ứng dụng.

Ví dụ: bạn có thể sử dụng gr.Textbox với ứng dụng chatbot để người dùng nhập câu hỏi và

xem câu trả lời. Tiếp theo, gr.Number cho phép người dùng nhập số. Ví dụ: một ứng dụng máy tính có thể

sử dụng gr.Number để cho phép người dùng gõ số cho các phép toán. Cuối cùng, gr.File cho phép người dùng

tải tập tin lên một ứng dụng. Bây giờ bạn cũng biết rằng LLAMAIndex là một chỉ số linh hoạt

khuôn khổ để xây dựng các ứng dụng hỗ trợ LLM tập trung vào việc tăng cường ngữ cảnh thông qua

nhập, phân nhóm, lập chỉ mục và truy xuất tài liệu có cấu trúc. Các trường hợp sử dụng cho LLAMAIndex bao gồm

trả lời câu hỏi bằng RAG cho chatbot, hiểu tài liệu và trích xuất dữ liệu.

LLAMAIndex cung cấp trình tải tài liệu tích hợp và công cụ truy vấn có thể tùy chỉnh không giống như LengChain,

trong đó nhấn mạnh các bước xâu chuỗi và quy trình công việc. Để thiết kế ứng dụng RAG đàm thoại với LLAMAIndex,

nhập dữ liệu, chia dữ liệu thành các nút, nhúng và lưu trữ dữ liệu dưới dạng vectơ,

và sử dụng bộ tổng hợp phản hồi hoặc công cụ truy vấn để tạo phản hồi được cá nhân hóa từ người dùng

lời nhắc. Bạn có thể áp dụng tính năng tải, phân nhóm, lập chỉ mục và truy vấn đường dẫn RAG bằng cách sử dụng LLAMAIndex

các lớp tài liệu, nút, chỉ mục và công cụ truy vấn. LLAMAIndex tải tài liệu nguồn bằng cách chuyển đổi

văn bản, PDF, Markdown, CSV, JSON và HTML vào các đối tượng tài liệu LLAMAIndex.

Lớp tài liệu LLAMAIndex tạo một đối tượng tài liệu với một số thành phần chính, bao gồm

ID duy nhất, trình giữ chỗ nhúng, từ điển siêu dữ liệu, từ điển mối quan hệ cho

liên kết đến các tài liệu khác và văn bản trong tài liệu nguồn. Bạn có thể sử dụng

SimpleDirectoryReader để nhập và tải tệp từ một thư mục hoặc các thư mục con của nó, nhập các tệp cụ thể,

hoặc nhập các loại tệp cụ thể. Bạn có thể sử dụng Bộ tách câu của LLAMAIndex để đệ quy

chia tài liệu thành các phần dựa trên các dấu phân cách được xác định trước. Bạn cũng có thể chia nhỏ tài liệu bằng cách sử dụng

các bộ chia khác, chẳng hạn như Bộ tách ngữ nghĩa hoặc bằng cách sử dụng trình bao bọc xung quanh bất kỳ LangChain nào

bộ chia. Chúng tôi khuyến khích bạn mở rộng việc học của mình và áp dụng khóa học này vào một

Chứng chỉ chuyên nghiệp của IBM. Tùy thuộc vào lịch trình của bạn và số lượng các khóa học trong

chương trình, bạn có thể hoàn thành Chứng chỉ Chuyên nghiệp này trong khoảng hai đến sáu tháng.

Bạn sẽ tìm thấy các liên kết đến Chứng chỉ Chuyên môn và một số khóa học liên quan trong

phần đọc Xin chúc mừng và các bước tiếp theo ở cuối khóa học này. Chúng tôi khuyên bạn nên như vậy

bạn tiếp tục áp dụng kiến thức về RAG mà bạn thu được từ khóa học này vào công việc của mình.

Chúng tôi hy vọng những kỹ năng mới của bạn sẽ hỗ trợ công việc của bạn và giúp bạn thăng tiến một cách chuyên nghiệp.

Chúc mừng bạn đã hoàn thành khóa học này! Chúng tôi đánh giá cao sự tham gia của bạn vào việc học này

cuộc hành trình và chúc bạn mọi điều tốt đẹp nhất!