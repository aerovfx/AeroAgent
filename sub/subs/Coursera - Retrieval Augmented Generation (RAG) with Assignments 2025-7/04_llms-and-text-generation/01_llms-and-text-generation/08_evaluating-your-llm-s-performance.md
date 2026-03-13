# 08 đánh giá-llm-s-hiệu suất của bạn

---

Cho dù bạn vừa xây dựng hệ thống RAG chứng minh khái niệm đầu tiên của mình,

hoặc đang lặp lại trên một hệ thống đã được sản xuất,

bạn sẽ muốn biết LLM của bạn hoạt động tốt như thế nào.

Cho dù bạn đang cân nhắc việc điều chỉnh nhiệt độ của mô hình,

cập nhật lời nhắc hệ thống của bạn,

hoặc thậm chí đổi sang một mẫu hoàn toàn mới.

Để đưa ra quyết định sáng suốt,

bạn sẽ cần có sẵn số liệu để đo lường tác động của từng quyết định.

Hãy xem xét một số phương pháp phổ biến để đánh giá hiệu suất LLM của bạn.

Vì LLM của bạn đang hoạt động bên trong một hệ thống phức tạp,

Để bắt đầu, điều quan trọng là phải rõ ràng về những nhiệm vụ cụ thể mà LLM của bạn chịu trách nhiệm.

Công việc của chú chó tha mồi của bạn là tìm thông tin liên quan từ cơ sở kiến ​​thức.

Công việc LLM của bạn là sử dụng thông tin đó để xây dựng phản hồi chất lượng cao.

Điều này có nghĩa là khi xem xét điều chỉnh LLM của bạn,

hoặc thậm chí thay thế hoàn toàn mô hình cơ bản,

bạn muốn đảm bảo các số liệu bạn đang sử dụng tập trung vào vai trò của LLM trong quy trình RAG rộng hơn.

Nếu vấn đề cuối cùng nằm ở chú chó tha mồi của bạn,

bạn không muốn lãng phí thời gian viết lại lời nhắc hệ thống của mình.

Nếu bạn cho rằng chó tha mồi của bạn đang hoạt động tốt,

thì nó sẽ tìm thấy những thông tin chủ yếu có liên quan,

có lẽ đã thêm vào một vài tài liệu không liên quan.

Khi đó, công việc của LLM của bạn là phản hồi lời nhắc của người dùng,

kết hợp các thông tin liên quan vào phản hồi của nó,

trích dẫn nó một cách thích hợp,

và chống lại việc bị phân tâm bởi bất kỳ thông tin không liên quan nào được lấy ra.

Lưu ý, hầu hết các hành vi dành riêng cho LLM này đều mang tính chủ quan.

Làm thế nào bạn có thể nói một cách định lượng rằng một phản hồi thực hiện tốt công việc

trả lời câu hỏi ban đầu của người dùng,

hoặc bỏ qua những thông tin không liên quan?

Do đó, hầu hết các số liệu dành riêng cho LLM đều dựa vào việc sử dụng các LLM khác

để đánh giá chất lượng của câu trả lời.

Kết hợp LLM vào quá trình đánh giá

cho phép một số mức độ linh hoạt hoặc tính chủ quan theo cách có thể mở rộng.

Nguồn tốt của các số liệu dành riêng cho RAG này là thư viện Ragas nguồn mở.

Hãy xem xét một vài số liệu nó cung cấp.

Mức độ liên quan của phản hồi đo lường xem phản hồi có thực sự phù hợp với lời nhắc của người dùng hay không.

Số liệu này kiểm tra xem phản hồi có phù hợp với lời nhắc ban đầu hay không,

bất kể nó có chính xác về mặt thực tế hay không.

Đây là cách nó hoạt động.

Đầu tiên, phản hồi do hệ thống RAG của bạn tạo ra sẽ được cung cấp cho LLM mới

tạo ra một số lời nhắc mẫu mà nó tin rằng có thể dẫn đến phản hồi đó.

Sau đó, cả lời nhắc người dùng ban đầu và các lời nhắc mẫu này

được nhúng vào một vectơ ngữ nghĩa.

Tiếp theo, độ tương tự cosine giữa lời nhắc người dùng thực tế

và mỗi lời nhắc mẫu được tính toán.

Cuối cùng, những điểm tương đồng này được tính trung bình,

đưa ra thước đo cuối cùng về mức độ phù hợp của phản hồi.

Lưu ý, số liệu này không nhất thiết đảm bảo phản hồi cung cấp thông tin thực tế,

nhưng nó kiểm tra xem liệu bạn có thể làm việc ngược lại một cách hợp lý hay không

từ phản hồi mà LLM đưa ra cho đến lời nhắc ban đầu được đưa ra.

Để đo xem LLM có thực sự sử dụng thông tin được truy xuất hay không,

bạn có thể sử dụng thước đo độ trung thực.

Số liệu này sử dụng mô hình ngôn ngữ để xác định tất cả các tuyên bố thực tế

được thực hiện trong phản hồi.

Sau đó, nó sử dụng nhiều lệnh gọi mô hình ngôn ngữ hơn để xác định có bao nhiêu xác nhận quyền sở hữu trong số này

được hỗ trợ bởi một trong những thông tin lấy được từ cơ sở tri thức.

Tỷ lệ phần trăm các tuyên bố được hỗ trợ là tính trung thực

cho lời nhắc, truy xuất và phản hồi cụ thể đó.

Các số liệu khác có trong thư viện RAGAS có cách tiếp cận tương tự

để đánh giá những thứ như độ nhạy cảm với thông tin không liên quan

được lấy từ cơ sở kiến ​​thức hoặc khả năng trích dẫn nguồn chính xác.

Tuy nhiên, một mô hình trên tất cả các số liệu này,

là sự phụ thuộc vào các cuộc gọi LLM tại một thời điểm nào đó trong quá trình đánh giá

và thậm chí có thể là ví dụ về câu trả lời đúng sự thật.

Điều này nói lên thực tế rằng vai trò của LLM trong hệ thống RAG

rất phức tạp và khó đánh giá bằng các số liệu tự động đơn giản hơn.

Ngoài những đánh giá cụ thể về LLM này,

có nhiều cách bạn có thể sử dụng số liệu chạy trên toàn bộ hệ thống của mình

để đánh giá hiệu quả LLM.

Ví dụ: nếu người dùng của bạn có thể đánh dấu phản hồi từ hệ thống RAG của bạn

với đánh giá không thích hoặc không thích,

sau đó bạn có thể kiểm tra A-B các thay đổi đối với lời nhắc hệ thống của mình

và xem tác động của thay đổi này đến mức độ hài lòng chung của người dùng.

Ý tưởng ở đây là bạn đo lường hiệu suất toàn hệ thống

nhưng tách biệt các thay đổi đối với cài đặt LLM,

cho phép bạn quy những thay đổi về hiệu suất tổng thể là do những thay đổi đối với LLM của bạn.

Số liệu hiệu suất LLM là công cụ hữu ích để quyết định điều chỉnh cài đặt LLM của bạn

hoặc thậm chí chuyển sang một mô hình mới.

Vì chất lượng phản hồi của LLM mang tính chủ quan nên

bạn nên lên kế hoạch sử dụng LLM làm đánh giá dựa trên đánh giá

hoặc phản hồi của con người để đánh giá chất lượng LLM.

Sự kết hợp của những kỹ thuật này sẽ cho phép bạn tự tin đánh giá

LLM của bạn hoạt động tốt như thế nào.