# 07 giới thiệu dự án và bộ dữ liệu khóa học

---

Trong phần còn lại của khóa học này, bạn sẽ vào vai một nhà khoa học dữ liệu

tại một công ty thiết bị ngoài trời tên là Avalanche.

Sếp của bạn vừa giao cho bạn một nhiệm vụ quá quen thuộc.

Bạn có thể tìm ra sản phẩm mùa đông nào đang bán chạy và sản phẩm nào khách hàng ghét không?

Bạn đã thực hiện phân tích cảm tính trên cùng tập dữ liệu đánh giá khách hàng Avalanche này nhiều lần

trước đây. Quá nhiều lần.

Nhưng lần này, bạn sẽ xây dựng một nguyên mẫu AI để tự động hóa toàn bộ quy trình làm việc.

Đây là loại nhiệm vụ trong thế giới thực mà GenAI hoàn hảo.

Nó lặp đi lặp lại, có những thước đo thành công rõ ràng và sếp của bạn muốn có câu trả lời nhanh chóng.

Trong suốt khóa học này, bạn sẽ xây dựng một ứng dụng hoạt động thực sự được hỗ trợ bởi Gen AI

biểu thị điểm cảm tính trung bình theo sản phẩm và trạng thái giao hàng,

phân tích cảm xúc của khách hàng, cho phép người dùng đặt câu hỏi bằng ngôn ngữ tự nhiên về dữ liệu.

Bạn sẽ bắt đầu từ việc nhỏ với giao diện Streamlit đơn giản,

sau đó bạn sẽ lên cấp thành bảng điều khiển đầy đủ và trợ lý Gen AI.

Đến cuối khóa học, bạn sẽ có một nguyên mẫu hoạt động được để trả lời câu hỏi,

GenAI có thể giúp nhóm của chúng tôi hiểu phản hồi của khách hàng nhanh hơn không?

Trong giai đoạn một, bạn sẽ sử dụng Streamlit và OpenAI để tải và dọn dẹp tập dữ liệu của mình bằng gấu trúc,

xây dựng giao diện tương tác đơn giản, trực quan hóa kết quả bằng biểu đồ và bộ lọc,

và xuất bản nguyên mẫu đầu tiên của bạn trực tuyến.

Và bạn sẽ sử dụng GenAI để giúp bạn viết mã.

Sau đó, trong giai đoạn hai, bạn sẽ chuyển sang nền tảng Snowflake để tải lên các tệp docx thô,

nhập và lưu trữ chúng ở định dạng có cấu trúc, sử dụng các công cụ AI tích hợp của Snowflake để phân tích chúng,

sau đó triển khai ứng dụng đầy đủ chức năng của bạn, hoàn chỉnh bằng chatbot.

Sau đó, ở giai đoạn ba, bạn sẽ kết nối chatbot của mình với dữ liệu,

thêm kỹ thuật nhanh chóng và RAG để cải thiện phản hồi,

học các kỹ thuật để nhận được phản hồi nhanh chóng.

Đây là một dự án được hướng dẫn nhưng bạn sẽ có nhiều chỗ để tùy chỉnh

và thử nghiệm trên đường đi.

Bạn muốn dùng thử LangChain hoặc API GenAI khác? Đi cho nó.

Bạn sẽ làm việc với tập dữ liệu Avalanche, một tập dữ liệu hư cấu mà tôi đã xây dựng chỉ cho khóa học này.

Hãy cùng khám phá tệp đánh giá của khách hàng ở định dạng CSV.

Trong tệp này, mỗi hàng thể hiện một đánh giá của khách hàng.

Điều đó bao gồm tên sản phẩm, ngày đánh giá, văn bản đánh giá,

và điểm tình cảm giữa âm một, rất tiêu cực và cộng một, rất tích cực.

Bạn bắt đầu với tệp CSV được làm sạch trước có tên là customer_reviews.csv.

Ở phần sau của khóa học, bạn sẽ học cách xây dựng và dọn dẹp

tự mình thực hiện từng bước một tập dữ liệu đánh giá của khách hàng Avalanche.

Bạn muốn đi sâu hơn? Chúng tôi cũng đã đưa vào các phiên bản .docx của các tệp đánh giá thô,

để bạn có thể kiểm tra việc nhập tệp sau trong mô-đun hai.

Bây giờ, bạn sẽ thấy bản xem trước của ứng dụng Streamlit cuối cùng của mình.

Ở trên cùng, bạn sẽ có hai tab.

Tab đầu tiên hiển thị biểu đồ về điểm cảm tính theo sản phẩm,

và sau đó là bản xem trước của bảng dữ liệu.

Bạn có thể lọc bảng theo sản phẩm,

và bạn có thể xem điểm cảm tính theo trạng thái giao hàng của từng sản phẩm.

Tab thứ hai có hộp nhập văn bản

cho phép bạn đặt câu hỏi bằng ngôn ngữ tự nhiên về dữ liệu.

Nó sử dụng LLM có thể truy cập dữ liệu của bạn và trả lời các câu hỏi về dữ liệu đó.

Bây giờ bạn đã thấy dự án cuối cùng của mình sẽ trông như thế nào,

chúng tôi đã sẵn sàng để đi sâu vào.

Trong video tiếp theo, bạn sẽ học cách áp dụng một framework đơn giản để xây dựng nguyên mẫu

điều đó sẽ giúp bạn tìm ra những gì cần xây dựng và những tính năng nào là quan trọng nhất.

Hãy xây dựng thứ gì đó thông minh và làm cho cuộc sống của bạn dễ dàng hơn rất nhiều.