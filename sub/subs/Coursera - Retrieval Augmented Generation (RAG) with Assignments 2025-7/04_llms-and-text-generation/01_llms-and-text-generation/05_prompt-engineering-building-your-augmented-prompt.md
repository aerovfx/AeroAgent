# 05 nhắc-kỹ thuật-xây dựng-tăng cường-nhắc nhở của bạn

---

Để tận dụng tối đa mô hình ngôn ngữ lớn của bạn,

bạn sẽ cần phải viết một lời nhắc có chất lượng cao.

Kỹ thuật nhanh chóng là một thuật ngữ chung

cho nhiều kỹ thuật nhắc nhở khác nhau

có xu hướng dẫn tới kết quả có chất lượng cao hơn.

Hãy cùng khám phá một vài kỹ thuật kỹ thuật nhanh chóng

và nói về cách chúng có thể được sử dụng

để cải thiện hiệu suất tổng thể của hệ thống RAG của bạn.

Để bắt đầu, sẽ rất hữu ích nếu bạn hiểu

cách bạn thực sự xây dựng các lời nhắc trong mã.

Định dạng phổ biến nhất là định dạng tin nhắn của OpenAI,

cấu trúc nào nhắc nhở dưới dạng một chuỗi tin nhắn

sử dụng cấu trúc JSON đơn giản.

Một tin nhắn sẽ có nội dung,

đó chỉ là nội dung của tin nhắn,

cũng như vai trò

sẽ là hệ thống, người dùng hoặc trợ lý.

Thông báo hệ thống được cung cấp cho LLM

để ảnh hưởng đến hành vi tổng thể của nó

và thường bao gồm các hướng dẫn cấp cao.

Lời nhắc ghi lại tin nhắn của người dùng

mà người dùng hệ thống đã gửi.

Tin nhắn trợ lý ghi lại câu trả lời

được tạo ra trước đây bởi LLM.

Khi bạn có một cuộc trò chuyện qua lại kéo dài

với LLM, còn được gọi là cuộc trò chuyện nhiều lượt,

nó không thực sự nhớ những gì bạn đã nói trước đó.

Thay vào đó, đằng sau hậu trường,

toàn bộ cuộc trò chuyện được chuyển đổi

vào định dạng tin nhắn này,

với thông báo người dùng mới của bạn xuất hiện ở cuối.

Và sau đó, toàn bộ cuộc trò chuyện được gửi tới LLM

với mỗi lời nhắc của người dùng mới.

Đối tượng tin nhắn JSON sau đó được chuyển thành

một chuỗi văn bản duy nhất có thể được LLM xử lý.

Chuỗi mẫu trò chuyện này sử dụng các thẻ văn bản đặc biệt,

như mũi tên hoặc thanh dọc,

để chỉ ra sự bắt đầu và kết thúc của mỗi tin nhắn.

LLM được đào tạo để nhận ra các thẻ này

và hiểu sự khác biệt giữa

tin nhắn hệ thống, người dùng và trợ lý.

Hình thức này rất linh hoạt

và cho phép bạn thêm nhiều ngữ cảnh khác nhau

theo lời nhắc của bạn để giúp kiểm soát cách LLM của bạn phản hồi.

Hãy xem xét một số cách bạn có thể sử dụng nó.

Điều đầu tiên bạn muốn làm

khi xây dựng lời nhắc cho hệ thống RAG của bạn

là viết lời nhắc hệ thống của bạn.

Điều này cung cấp hướng dẫn cấp cao LLM của bạn

về cách nó nên cư xử.

Nếu bạn luôn muốn LLM của mình nói bằng một giọng cụ thể

hoặc tuân theo các thủ tục nhất định,

lời nhắc hệ thống là nơi thông tin đó sẽ đến.

Để biết một số ý tưởng về nội dung có thể đưa vào lời nhắc hệ thống,

hãy xem lời nhắc hệ thống này từ một chatbot LLM phổ biến.

Điều đầu tiên khiến bạn ấn tượng là độ dài.

Nó rất lớn.

Không phải lúc nào bạn cũng cần phải viết lời nhắc hệ thống nhiều trang,

nhưng biết rằng bạn có sự linh hoạt để làm như vậy

là một lời nhắc nhở tốt.

Ngay từ đầu lời nhắc,

có thông tin về mức giới hạn kiến thức

của dữ liệu huấn luyện của mô hình,

cũng như ngày hiện tại.

Thông tin như thế này giúp LLM

xác định mức độ lỗi thời của thông tin của nó

và liệu nó có ở vị trí tốt không

để trả lời một số câu hỏi nhất định.

Các phần sau chỉ đạo LLM

về quy trình và giọng điệu nên sử dụng

để trả lời lời nhắc.

Ví dụ, nó hỏi mô hình

suy luận thông qua các câu trả lời từng bước một,

không trợ giúp với các yêu cầu có thể gây hại,

và trả lời trong markdown.

LLM cũng được cho biết rằng nó rất tò mò về mặt trí tuệ

và thích nghe những gì mọi người nghĩ về một vấn đề

và tham gia thảo luận về nhiều chủ đề khác nhau,

có thể nói, điều này mang lại cho LLM một tính cách cụ thể.

Bạn có thể sử dụng những nguyên tắc tương tự

để xây dựng lời nhắc hệ thống của riêng bạn.

Ví dụ: bạn có thể hướng dẫn LLM của mình

để trả lời rất chi tiết

hoặc trả lời câu hỏi một cách ngắn gọn.

Vì bạn đang xây dựng lời nhắc hệ thống

cho ứng dụng RAG,

bạn có thể nói mô hình ngôn ngữ

chỉ sử dụng các tài liệu được truy xuất

để trả lời các gợi ý,

hoặc đánh giá liệu một tài liệu có liên quan hay không,

hoặc trích dẫn nguồn trong phản hồi của nó.

Lời nhắc hệ thống thường được thêm vào

theo mọi lời nhắc mà LLM của bạn sẽ xử lý,

vì vậy hãy dành thời gian tinh chỉnh chúng

là một cách tuyệt vời để cải thiện phong cách

và chất lượng của kết quả

hệ thống RAG của bạn cuối cùng sẽ tạo ra.

Tại thời điểm này,

bạn đã sẵn sàng xây dựng lời nhắc tăng cường của mình.

Lời nhắc này có khả năng bao gồm

nhiều thông tin,

vì vậy sẽ rất hữu ích khi xây dựng

một mẫu lời nhắc được cân nhắc kỹ lưỡng.

Một mẫu đặt ra

cấu trúc cấp cao của lời nhắc của bạn

và giúp quyết định

nơi một số phần nội dung nhất định sẽ được chèn vào.

Ví dụ,

bạn có thể luôn bắt đầu

với lời nhắc hệ thống cấp cao

cung cấp hướng dẫn cấp cao cho hệ thống

về cách nó nên cư xử.

Nếu hệ thống của bạn hỗ trợ

cuộc trò chuyện nhiều lượt,

bạn có thể bao gồm các tin nhắn trước đó

được gửi giữa người dùng và LLM.

Tiếp theo, bạn có thể thêm 5 vị trí hàng đầu

hoặc 10 khối hàng đầu

được con chó tha mồi của bạn lấy lại,

cũng như mọi thông tin

về cách xử lý chúng.

Cuối cùng, bạn có thể bao gồm

lời nhắc người dùng gần đây nhất

LLM sẽ phản hồi.

Đây là những gì một lời nhắc được xây dựng

từ mẫu này có thể trông như thế nào.

Điều tốt đẹp về

sử dụng một mẫu như thế này

là nó làm cho nó dễ dàng

để thử nghiệm với

các cấu trúc nhắc khác nhau.

Bạn có thể sửa đổi các thành phần riêng lẻ

của lời nhắc tổng thể

và xem điều đó tác động như thế nào

phản hồi được tạo ra cuối cùng.

Đây là những gì nó trông giống như

để xây dựng một lời nhắc điển hình

trong hệ thống RAG,

kết hợp lời nhắc hệ thống được viết tốt,

lấy bối cảnh,

chi tiết cuộc trò chuyện trước đó,

và tất nhiên,

lời nhắc của người dùng gần đây nhất.

Hãy tham gia cùng tôi trong video tiếp theo

và chúng ta hãy nhìn vào

một số kỹ thuật nâng cao

để cải thiện hơn nữa

LLM hoạt động như thế nào.