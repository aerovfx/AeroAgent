# 04 sử dụng-rag-để cải thiện hiệu suất mô hình

---

Bạn xây dựng các ứng dụng LLM có thể phân tích dữ liệu và tạo ra thông tin chi tiết.

Nhưng điều gì sẽ xảy ra khi người dùng đặt câu hỏi mà mô hình của bạn không thể trả lời chỉ dựa vào dữ liệu huấn luyện của nó?

Có lẽ họ muốn biết về khiếu nại của khách hàng tuần trước

hoặc chính sách của công ty đã thay đổi ngày hôm qua.

Mô hình của bạn có thể đưa ra câu trả lời có vẻ tự tin nhưng cũng có thể sai hoàn toàn.

Đây là lúc Thế hệ tăng cường truy xuất, hay RAG, xuất hiện.

Nó biến LLM của bạn từ một người thông minh thành trợ lý nghiên cứu

tra cứu sự thật trước khi trả lời.

Trong bài học này, bạn sẽ khám phá cách RAG hoạt động,

khi nào nên sử dụng nó và điều gì đang trở nên cần thiết để xây dựng các ứng dụng LLM đáng tin cậy.

Bạn sẽ thấy chính xác nó hoạt động như thế nào với tập dữ liệu Avalanche của bạn

và hiểu tại sao RAG không chỉ là thứ tốt để có mà còn rất quan trọng đối với các ứng dụng sản xuất.

Bạn đã sẵn sàng biến LLM của mình thành một cỗ máy kiểm tra thực tế mạnh mẽ chưa?

Hãy đi sâu vào.

RAG là một kỹ thuật giúp LLM cung cấp câu trả lời tốt hơn bằng cách truy xuất thông tin liên quan

từ các nguồn bên ngoài trước khi tạo ra phản hồi,

điều này giống như giao cho người mẫu của bạn một thực tập sinh để lấy thông tin hữu ích cho bạn.

RAG có hai bước chính.

Đầu tiên, thu hồi.

Nó tìm kiếm cơ sở kiến thức của bạn, chẳng hạn như một bộ tài liệu hoặc cơ sở dữ liệu,

để tìm được những thông tin phù hợp nhất.

Điều này có thể bao gồm tìm kiếm dựa trên từ khóa hoặc tìm kiếm ngữ nghĩa bằng cách sử dụng các vectơ nhúng.

Tiếp theo, thế hệ.

Nó lấy thông tin tìm thấy và sau đó đưa nó vào một mô hình ngôn ngữ lớn

để viết câu trả lời chính xác hơn.

Sự kết hợp này làm cho mô hình của bạn trở nên thực tế, phù hợp và ít gây ảo giác hơn.

LLM rất mạnh mẽ nhưng họ không biết mọi thứ,

đặc biệt không phải về dữ liệu sản phẩm mới nhất của bạn,

chính sách nội bộ hoặc các lĩnh vực thích hợp như y học hoặc luật.

Với RAG, bạn không cần phải đào tạo lại mô hình của mình để làm cho mô hình trở nên thông minh hơn.

Thay vào đó, bạn để nó lấy dữ kiện trong thời gian chạy.

Điều này lý tưởng khi độ chính xác, tính minh bạch và độ tin cậy thực sự quan trọng,

như với nghiên cứu y học hoặc luật hợp đồng.

Là một phần thưởng, nó cũng làm cho ứng dụng của bạn rẻ hơn và nhanh hơn bằng cách giảm kích thước lời nhắc

và tránh việc đào tạo lại mô hình không cần thiết.

Sử dụng RAG khi nền tảng kiến ​​thức của bạn quá lớn để có thể đưa vào lời nhắc.

Nội dung của bạn thay đổi thường xuyên và bạn cần câu trả lời theo thời gian thực.

Bạn muốn ghi nguồn để tuân thủ hoặc tin cậy.

Bạn đang làm việc trong một lĩnh vực chuyên biệt như chăm sóc sức khỏe, nơi độ chính xác là rất quan trọng.

Bạn muốn cá nhân hóa câu trả lời bằng cách sử dụng dữ liệu cụ thể của người dùng.

Hoặc bạn muốn tối ưu hóa việc sử dụng token để tiết kiệm chi phí.

Quay lại với tập dữ liệu Avalanche, giả sử người dùng hỏi:

khách hàng nói gì về chính sách hoàn trả của chúng tôi trong tháng này?

Nếu bạn chỉ sử dụng lời nhắc, mô hình sẽ đoán dựa trên quá trình đào tạo chung.

Với RAG, nó tìm kiếm các bài đánh giá Avalanche gần đây của bạn,

tìm những câu trả lời phù hợp nhất và đưa ra câu trả lời dựa trên phản hồi thực tế của khách hàng.

Đây là cách nó hoạt động đằng sau hậu trường.

Mô hình nhận được câu hỏi của người dùng.

Hệ thống của bạn chia các đánh giá thành nhiều phần nhỏ để chúng phù hợp với lời nhắc.

Một công cụ truy xuất sẽ tìm thấy những phần có liên quan nhất.

LLM kết hợp bối cảnh đó với câu hỏi để tạo ra câu trả lời có căn cứ.

Trong Snowflake, toàn bộ quá trình này có thể được xử lý bằng cách sử dụng tìm kiếm vỏ não,

công cụ này thực hiện tìm kiếm, sắp xếp lại và truy xuất vectơ cho bạn.

Bạn có thể đọc thêm về nó trong tài liệu Snowflake,

và liên kết nằm ở cuối màn hình của bạn.

RAG tìm nạp các ngữ cảnh mới tại thời điểm truy vấn, tinh chỉnh hành vi dựa trên chúng vào chính mô hình.

Tinh chỉnh là tốt nhất khi bạn cần một phong cách hoặc giọng điệu viết cụ thể,

đang làm đi làm lại cùng một công việc như tóm tắt hợp đồng,

cần logic hoặc lý luận nhất quán, không muốn quản lý tài liệu hoặc lưu trữ bên ngoài.

Tuy nhiên, nó thiết lập chậm hơn, yêu cầu dữ liệu huấn luyện được gắn nhãn,

và sẽ khó thích ứng hơn nếu dữ liệu của bạn thay đổi.

Đây là công thức chiến thắng được nhiều đội hàng đầu sử dụng.

Sử dụng kỹ thuật nhanh chóng để hướng dẫn mô hình từng bước.

Sử dụng RAG để đưa vào bối cảnh thực tế có liên quan.

Sử dụng tính năng tinh chỉnh để khóa phong cách, hành vi hoặc lý luận cho các nhiệm vụ lặp đi lặp lại.

Bây giờ bạn đã hiểu tại sao RAG trở thành xương sống của các ứng dụng LLM sản xuất.

Đó là sự khác biệt giữa một bản demo thông minh và một thứ mà các nhóm thực sự tin tưởng.

Điều quan trọng là đừng bắt LLM của bạn phải ghi nhớ mọi thứ, hãy dạy nó cách nghiên cứu.

Tiếp theo, chúng tôi sẽ triển khai hệ thống RAG bằng Snowflake và Streamlit

có thể trả lời các câu hỏi về dữ liệu Avalanche của bạn bằng các trích dẫn và độ tin cậy.

Đã đến lúc xem RAG hoạt động.