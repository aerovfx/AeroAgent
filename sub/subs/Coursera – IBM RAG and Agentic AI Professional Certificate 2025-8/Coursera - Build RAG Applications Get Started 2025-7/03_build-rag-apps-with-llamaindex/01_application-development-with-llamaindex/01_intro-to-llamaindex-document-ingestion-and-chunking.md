# 01 phần giới thiệu về llamaindex-tài liệu-nhập-và-phân đoạn

---

Chào mừng bạn đến với video giới thiệu cho bạn cách nhập và phân chia tài liệu LlamaIndex.

Sau khi xem video này, bạn sẽ có thể:

Mô tả LlamaIndex bao gồm một số trường hợp sử dụng điển hình của nó.

Giải thích cách LlamaIndex hoạt động với RAG.

Tải tài liệu nguồn từ nhiều định dạng khác nhau vào lớp tài liệu của LlamaIndex và

Chia tài liệu thành các khối hoặc nút bằng cách sử dụng LlamaIndex.

Hãy bắt đầu với cái nhìn tổng quan cấp cao về LlamaIndex.

LlamaIndex là một khuôn khổ để xây dựng khả năng tăng cường ngữ cảnh do LLM cung cấp.

Tăng cường ngữ cảnh là quá trình cung cấp dữ liệu của bạn cho LLM, cho phép

LLM để thực hiện một nhiệm vụ cụ thể trong khi căn cứ các phản hồi của nó trong bối cảnh được cung cấp.

Các trường hợp sử dụng điển hình bao gồm trả lời câu hỏi bằng Thế hệ tăng cường truy xuất hoặc RAG

đó là trọng tâm chính của video này. Chatbots mở rộng đường dẫn RAG cơ bản

bằng cách cho phép thực hiện nhiều truy vấn và câu trả lời qua lại, cho phép LLM yêu cầu làm rõ

hoặc trả lời các câu hỏi tiếp theo, hiểu tài liệu và trích xuất dữ liệu, cho phép

LLM để đọc ngôn ngữ tự nhiên và xác định ngữ nghĩa các chi tiết quan trọng như tên, ngày tháng,

địa chỉ và số liệu từ lượng lớn dữ liệu có cấu trúc hoặc không có cấu trúc.

Hãy cùng tìm hiểu cách LlamaIndex hoạt động trong bối cảnh Thế hệ tăng cường truy xuất

hoặc RAG vì nhiều trường hợp sử dụng khác của LlamaIndex phụ thuộc hoặc có liên quan đến các thành phần

được sử dụng trong RAG.

Quá trình RAG bắt đầu bằng việc tải và chia nhỏ các tài liệu nguồn.

Sau đó, các đoạn tài liệu này được nhúng bằng mô hình nhúng, nhúng văn bản dưới dạng

các vectơ có kích thước bằng nhau, một vectơ cho mỗi đoạn văn bản.

Các vectơ này sau đó được đưa vào kho lưu trữ vectơ, đây là cơ sở dữ liệu rất phù hợp với

lưu trữ và thao tác các vectơ.

Khi người dùng cung cấp lời nhắc, lời nhắc đó sẽ được nhúng bằng cùng một mô hình

vì tài liệu nguồn và một công cụ truy xuất được sử dụng để truy xuất văn bản có liên quan từ

cửa hàng vector.

Sau đó, văn bản được truy xuất sẽ được sử dụng để tăng cường lời nhắc và sau đó lời nhắc được tăng cường này sẽ được

được đưa vào LLM để cung cấp phản hồi nhận biết ngữ cảnh được coi là phù hợp nhất

dữ liệu từ các tài liệu nguồn.

Hãy bắt đầu với bước RAG đầu tiên, bao gồm việc tải các đối tượng tệp dữ liệu văn bản

vào tài liệu LlamaIndex, là nơi chứa chung của LlamaIndex cho các nguồn tài liệu.

Bạn có thể tải dữ liệu văn bản từ nhiều định dạng khác nhau bao gồm tệp văn bản, tệp PDF, đánh dấu

tệp, tệp CSV được phân tách bằng dấu phẩy hoặc tệp CSV, tệp JSON và tệp HTML.

Ngoài việc hỗ trợ tải tài liệu cục bộ, LlamaIndex còn cung cấp nhiều

kết nối để tích hợp liền mạch với nhiều cơ sở dữ liệu và dịch vụ lưu trữ đám mây khác nhau.

Hãy nhanh chóng kiểm tra lớp tài liệu của LlamaIndex và một số tính năng độc đáo của nó.

Đầu tiên, bạn tạo một đối tượng của lớp tài liệu bằng cách chuyển văn bản Hello LlamaIndex

vào tham số văn bản của lớp tài liệu.

Sau đó, bằng cách gọi phương thức dict của đối tượng tài liệu thu được, bạn có thể kiểm tra các mục được lưu trữ

trong tài liệu.

Lưu ý rằng tài liệu LlamaIndex có một số thành phần chính.

ID xác định duy nhất tài liệu, phần giữ chỗ để nhúng nếu bạn quyết định

để nhúng toàn bộ tài liệu, một lệnh siêu dữ liệu nơi bạn có thể lưu trữ siêu dữ liệu được liên kết với

tài liệu, chẳng hạn như nguồn gốc hoặc ngày tạo của nó, một mệnh lệnh về mối quan hệ liên kết

tài liệu đến các mục liên quan khác chẳng hạn như các tài liệu khác và văn bản hiện tại

trong tài liệu.

Do đó, lớp tài liệu đóng vai trò là nơi lưu trữ văn bản của tài liệu.

để cung cấp cho mỗi tài liệu một ID duy nhất và lưu trữ siêu dữ liệu cũng như các mối quan hệ của tài liệu

trong các từ điển.

Bây giờ hãy xem cách tải tài liệu từ bộ nhớ cục bộ.

LlamaIndex cung cấp trình tải tài liệu mạnh mẽ có tên SimpleDirectoryReader có thể tải

nhiều loại tệp bao gồm các tệp văn bản thuần túy, đánh dấu, CSV và PDF.

Để sử dụng trình tải tệp SimpleDirectoryReader, hãy nhập nó từ Llama_index.core

Sau đó, bạn có thể tải tất cả các tệp trong thư mục bằng cách chuyển đường dẫn của thư mục đó làm đường dẫn

đối số đầu tiên cho SimpleDirectoryReader và gọi phương thức Load_data.

Mặt khác, nếu bạn muốn tải tất cả các tệp từ một đường dẫn có tất cả các thư mục con của nó,

bạn có thể chuyển recursive = True làm tham số cho SimpleDirectoryReader.

Ngoài ra, nếu bạn muốn tải các tệp cụ thể, bạn có thể chuyển đường dẫn của tệp dưới dạng

list vào tham số input_files.

Cuối cùng, để chỉ tải các loại tệp cụ thể, hãy chuyển danh sách các phần mở rộng loại tệp được yêu cầu

đến tham số _ext được yêu cầu.

Lưu ý rằng SimpleDirectoryReader xuất ra danh sách các đối tượng lớp tài liệu LlamaIndex

thuộc loại bạn vừa thấy.

Nút LlamaIndex chỉ đơn giản là một đoạn văn bản.

Việc chia nhỏ văn bản dài giúp giữ lại ngữ cảnh cụ thể của từng phân đoạn, dẫn đến kết quả chính xác hơn

và các phần nhúng có liên quan.

LlamaIndex cung cấp một bộ phân đoạn văn bản dễ sử dụng nhưng hiệu quả đáng ngạc nhiên được gọi là SentenceSplitter.

SentenceSplitter sử dụng phương pháp đệ quy, chia văn bản dài quá mức dựa trên

các ký tự như ký tự dòng mới và dấu chấm.

Để sử dụng SentenceSplitter, trước tiên hãy nhập nó từ Llama_index.core.node_parser.

Sau đó, xác định trình phân tích cú pháp nút bằng cách chuyển các tham số chunk_size và chunk_overlap.

Tham số chunk_size kiểm soát kích thước tối đa của từng đoạn trong mã thông báo và

chunk_overlap kiểm soát số lượng mã thông báo tối đa có thể chồng lên nhau

từ đoạn này sang đoạn khác.

Sau đó sử dụng phương thức get_nodes_from_documents để phân chia

tài liệu vào các nút riêng lẻ.

Lưu ý rằng trình phân tích cú pháp nút trả về danh sách các phiên bản nút văn bản LlamaIndex, đó là

có cấu trúc tương tự như cấu trúc của phiên bản tài liệu LlamaIndex mà bạn đã thấy trước đây.

Ngoài SentenceSplitter, LlamaIndex còn cung cấp nhiều bộ tách khác, chẳng hạn như Semantic

Bộ tách tách ở bất cứ nơi nào độ tương tự của câu giảm xuống dưới một ngưỡng nhất định hoặc một trình bao bọc

dành cho Bộ tách Langchain cho phép bạn sử dụng bất kỳ Bộ tách Langchain nào trong LlamaIndex.

Tiếp theo, hãy tóm tắt những gì bạn đã học được cho đến nay.

Bạn đã biết rằng LlamaIndex là một khuôn khổ để xây dựng tính năng tăng cường ngữ cảnh được hỗ trợ bởi LLM.

Các trường hợp sử dụng điển hình của LlamaIndex bao gồm trả lời câu hỏi bằng RAG, chatbot, tài liệu

hiểu và khai thác dữ liệu.

Trong bước RAG đầu tiên, LlamaIndex tải tài liệu nguồn bằng cách chuyển đổi văn bản, PDF, Markdown,

Các tệp CSV, JSON và HTML vào các đối tượng tài liệu LlamaIndex.

Lớp tài liệu LlamaIndex tạo một đối tượng tài liệu với một số thành phần chính, bao gồm

ID duy nhất, trình giữ chỗ nhúng, từ điển siêu dữ liệu, từ điển mối quan hệ cho

liên kết đến các tài liệu khác và văn bản trong tài liệu nguồn.

Bạn có thể sử dụng SimpleDirectoryReader của LlamaIndex để nhập và tải tệp từ một thư mục,

thư mục con, tệp cụ thể và loại tệp cụ thể của nó.

Bạn có thể sử dụng SentenceSplitter của LlamaIndex để chia tài liệu thành các phần dựa trên

dải phân cách.

Và bạn cũng có thể chia nhỏ tài liệu bằng cách sử dụng các bộ tách khác, chẳng hạn như bộ tách ngữ nghĩa hoặc bằng

sử dụng trình bao bọc xung quanh bất kỳ bộ chia Langchain nào.