# 01 hệ thống tác nhân-rag-tăng cường-truy xuất-với-đa tác nhân

---

Như vậy chúng ta đều biết Retrieval Augmented Generation là gì.

Chúng ta hãy làm một bản bồi dưỡng nhanh chóng.

Retrieval Augmented Generation là một hệ thống mạnh mẽ và phổ biến

giúp tăng cường phản hồi từ một mô hình ngôn ngữ lớn.

Nó thực hiện điều này bằng cách kết hợp dữ liệu liên quan được lấy từ cơ sở dữ liệu vectơ,

thêm nó làm ngữ cảnh vào lời nhắc và gửi nó đến LLM để tạo.

Điều này làm được là nó cho phép LLM đưa ra phản hồi của mình bằng thông tin cụ thể và chính xác,

và điều đó cải thiện chất lượng và độ tin cậy của phản hồi.

Hãy để tôi phác thảo nó nhanh chóng.

Vì vậy, giả sử chúng ta có một người dùng hoặc thậm chí một ứng dụng,

và họ gửi một truy vấn.

Bây giờ, không có Thế hệ tăng cường truy xuất,

truy vấn này sẽ được thực hiện và tự nội suy vào một dấu nhắc.

Và từ đó, nó sẽ chạm đến LLM,

và điều đó sẽ tạo ra một đầu ra.

Để tạo RAG này, chúng ta có thể thêm cơ sở dữ liệu vectơ.

Vì vậy, thay vì chỉ đi trực tiếp và tự nội suy vào dấu nhắc,

nó sẽ chạm vào vector DB này,

và phản hồi từ vectơ DB đó sẽ được sử dụng làm ngữ cảnh cho lời nhắc.

Bây giờ, trong quy trình RAG điển hình này, chúng tôi chỉ gọi LLM một lần,

và chúng tôi chỉ sử dụng nó để tạo ra phản hồi.

Nhưng điều gì sẽ xảy ra nếu chúng ta có thể tận dụng LLM không chỉ để phản hồi,

mà còn cho các nhiệm vụ bổ sung,

như quyết định truy vấn cơ sở dữ liệu vectơ nào nếu chúng ta có nhiều cơ sở dữ liệu,

hoặc thậm chí xác định loại phản hồi để đưa ra?

Nó có nên trả lời bằng văn bản, tạo biểu đồ hay thậm chí cung cấp đoạn mã không?

Và tất cả điều đó sẽ phụ thuộc vào bối cảnh của truy vấn đó.

Vì vậy, đây là lúc đường ống RAG tác nhân phát huy tác dụng.

Trong RAG tác nhân, chúng tôi sử dụng LLM làm tác nhân,

và LLM không chỉ đơn thuần là tạo ra phản hồi.

Nó đảm nhận vai trò tích cực và có thể đưa ra những quyết định cải thiện cả

sự liên quan và độ chính xác của dữ liệu được truy xuất.

Bây giờ hãy khám phá cách chúng ta có thể tăng cường quy trình ban đầu với một tác nhân

và một số nguồn dữ liệu khác nhau.

Vì vậy, thay vì chỉ một nguồn duy nhất, hãy thêm một nguồn thứ hai.

Và cái đầu tiên có thể là tài liệu nội bộ, phải không?

Và thứ hai có thể là kiến ​​thức chung về ngành.

Bây giờ trong tài liệu nội bộ, chúng ta sẽ có những thứ như chính sách,

các thủ tục, hướng dẫn.

Và nền tảng kiến thức chung sẽ có những thứ như tiêu chuẩn ngành,

các phương pháp thực hành tốt nhất và nguồn lực công cộng.

Vậy làm cách nào chúng ta có thể khiến LLM sử dụng cơ sở dữ liệu vectơ chứa dữ liệu

điều đó sẽ phù hợp nhất với truy vấn?

Hãy thêm tác nhân đó vào đường dẫn này.

Bây giờ tác nhân này có thể quyết định một cách thông minh cơ sở dữ liệu nào sẽ truy vấn

dựa trên câu hỏi của người dùng.

Và người đại diện không đoán ngẫu nhiên.

Nó tận dụng khả năng hiểu ngôn ngữ của LLM

để diễn giải truy vấn và xác định ngữ cảnh của nó.

Vì vậy, nếu một nhân viên hỏi,

"Chính sách của công ty về làm việc từ xa trong kỳ nghỉ là gì?"

Nó sẽ định tuyến điều đó đến tài liệu nội bộ.

Và phản hồi đó sẽ được sử dụng làm ngữ cảnh cho lời nhắc.

Nhưng nếu câu hỏi tổng quát hơn, như,

"Các tiêu chuẩn ngành cho công việc từ xa ở các công ty công nghệ là gì?"

Tác nhân sẽ định tuyến thông tin đó tới cơ sở dữ liệu kiến ​​thức chung.

Và bối cảnh đó sẽ được sử dụng trong lời nhắc đó.

Được hỗ trợ bởi LLM và được đào tạo bài bản,

tác nhân phân tích truy vấn,

và dựa trên sự hiểu biết về nội dung và bối cảnh,

quyết định sử dụng cơ sở dữ liệu nào.

Nhưng không phải lúc nào họ cũng đặt những câu hỏi chung chung

hoặc thực sự có liên quan đến bất kỳ nội dung nào chúng tôi có trong vectơ DB của mình.

Vậy điều gì sẽ xảy ra nếu ai đó hỏi một câu hỏi hoàn toàn nằm ngoài lĩnh vực bên trái?

Giống như "Ai đã vô địch World Series năm 2015?"

Những gì tác nhân có thể làm vào thời điểm đó là nó có thể định tuyến nó đến nơi không an toàn.

Vì tác nhân có thể nhận ra ngữ cảnh của truy vấn,

nó có thể nhận ra rằng nó không phải là một phần của hai cơ sở dữ liệu mà chúng tôi có.

Nó có thể định tuyến nó đến nơi an toàn và quay trở lại,

"Xin lỗi, tôi không có thông tin bạn đang tìm kiếm."

Đường dẫn RAG tác nhân này có thể được sử dụng trong các hệ thống hỗ trợ khách hàng và công nghệ pháp lý.

Ví dụ: một luật sư có thể tìm ra câu trả lời cho câu hỏi của họ

từ bản tóm tắt nội bộ của họ,

và sau đó trong một truy vấn khác, chỉ cần lấy nội dung từ cơ sở dữ liệu tải trường hợp công khai.

Tác nhân có thể được sử dụng theo nhiều cách.

Agentic RAG là một bước tiến trong cách chúng tôi tăng cường quy trình RAG

bằng cách vượt ra ngoài việc tạo phản hồi đơn giản

để đưa ra quyết định thông minh hơn.

Bằng cách cho phép một tác nhân chọn nguồn dữ liệu tốt nhất

và thậm chí có khả năng kết hợp thông tin bên ngoài,

như dữ liệu thời gian thực hoặc dịch vụ của bên thứ ba,

chúng ta có thể tạo ra một quy trình phản hồi nhanh hơn,

chính xác hơn và thích ứng hơn.

Cách tiếp cận này mở ra rất nhiều khả năng

cho các ứng dụng trong dịch vụ khách hàng, công nghệ pháp lý, chăm sóc sức khỏe,

hầu như bất kỳ lĩnh vực nào.

Khi công nghệ tiếp tục phát triển,

chúng ta sẽ thấy các hệ thống AI thực sự hiểu ngữ cảnh

và có thể mang lại những giá trị đáng kinh ngạc.