# 01 khái niệm lõi langchain

---

Chào mừng bạn đến với Khái niệm cốt lõi của LangChain.

Sau khi xem video này, bạn sẽ có thể xác định LangChain và mô tả các thành phần của nó.

Hãy bắt đầu bằng cách hiểu LangChain là gì.

LangChain là một giao diện nguồn mở giúp đơn giản hóa quá trình phát triển ứng dụng

sử dụng LLM.

Nó tạo điều kiện thuận lợi cho việc tích hợp các mô hình ngôn ngữ vào các trường hợp sử dụng khác nhau một cách có cấu trúc, bao gồm

Xử lý ngôn ngữ tự nhiên hoặc NLP và truy xuất dữ liệu.

Nó bao gồm một số thành phần – Tài liệu, Chuỗi, Đại lý, Mô hình ngôn ngữ, Mô hình trò chuyện,

Tin nhắn trò chuyện, Mẫu lời nhắc và Trình phân tích cú pháp đầu ra.

Trong video này, bạn sẽ xem lại Mô hình ngôn ngữ, Mô hình trò chuyện, Tin nhắn trò chuyện, Mẫu lời nhắc,

và Trình phân tích cú pháp đầu ra của LangChain.

Mô hình ngôn ngữ trong LangChain là nền tảng của LLM.

Nó sử dụng kiểu nhập văn bản để tạo đầu ra văn bản và giúp hoàn thành các tác vụ cũng như tóm tắt tài liệu.

LangChain sử dụng IBM, OpenAI, Google và Meta làm mô hình ngôn ngữ chính.

Ví dụ: để tạo phản hồi cho phương pháp bán hàng mới bằng mô hình ngôn ngữ,

hãy sử dụng WatsonX.AI của IBM để tạo LLM dựa trên Hướng dẫn Mixtral 8x7 Billion

mô hình.

Đảm bảo rằng các phần phụ thuộc cần thiết, chẳng hạn như GenParams và Model Inference, được nhập

từ Gói học máy IBM Watson.

Bây giờ, hãy tùy chỉnh mô hình bằng cách điều chỉnh các cài đặt như mã thông báo và nhiệt độ.

Một đối tượng mô hình đã tạo sẽ xuất hiện.

Tiếp theo, mô hình hiển thị văn bản phản hồi được tạo cho lời nhắc được chèn.

Bạn có thể xem phản hồi mẫu được tạo.

Thành phần tiếp theo của LangChain là Mô hình trò chuyện và Mô hình ngôn ngữ.

Mô hình trò chuyện được thiết kế để trò chuyện hiệu quả.

Điều đó có nghĩa là nó hiểu các câu hỏi hoặc lời nhắc và trả lời chúng như một con người.

Tiếp theo, để tạo phản hồi, trước tiên hãy tạo mô hình ngôn ngữ bằng WatsonX.AI và chuyển đổi

mô hình thành mô hình trò chuyện bằng chức năng LLM của WatsonX.

Điều này chuyển đổi mô hình trò chuyện thành LLM đàm thoại để tham gia vào các cuộc đối thoại.

Ví dụ: để xem câu trả lời, hãy chèn một câu hỏi vào mô hình, chẳng hạn như Ai là đàn ông?

bạn thân nhất?

Bạn có thể xem câu trả lời mẫu được tạo cho câu hỏi.

Các mô hình trò chuyện xử lý các tin nhắn trò chuyện khác nhau để làm cho mô hình trở nên hiệu quả trong cuộc trò chuyện động

môi trường.

Ví dụ: thông báo của con người giúp người dùng nhập liệu, thông báo AI được tạo bởi

model, thông báo hệ thống giúp hướng dẫn model, thông báo chức năng giúp chức năng

để gọi kết quả bằng tham số tên và thông báo công cụ sẽ giúp tương tác với công cụ

để đạt được kết quả.

Trong tin nhắn trò chuyện, mỗi tin nhắn trò chuyện bao gồm hai thuộc tính chính.

Vai trò có nghĩa là ai đang nói và nội dung có nghĩa là những gì đang được nói.

Hãy xem ví dụ về thông báo do hệ thống tạo ra, trong đó mô hình đã đưa ra hướng dẫn

trở thành một AI bot để trả lời câu hỏi Ăn gì chỉ bằng một câu ngắn gọn.

Để trả lời câu hỏi này, mô hình trò chuyện sẽ tạo một danh sách tin nhắn.

Đầu tiên, hãy định cấu hình mô hình này làm bot hoạt động thể dục bằng thông báo hệ thống.

Sau đó mô phỏng cuộc trò chuyện trước đây bằng tin nhắn của con người và tin nhắn AI.

Tiếp theo, bằng cách sử dụng các cài đặt này, mô hình sẽ tạo phản hồi dựa trên đoạn hội thoại trước đó.

Bạn có thể vận hành mô hình trò chuyện bằng cách sử dụng tin nhắn của con người làm đầu vào và cho phép mô hình tạo

phản hồi mà không có tin nhắn hệ thống hoặc hàng đợi tin nhắn AI.

Điều đó có nghĩa là bot trò chuyện sẽ phản hồi trực tiếp với thông tin đầu vào của con người.

Thành phần tiếp theo của LangChain là các mẫu nhắc nhở.

Các mẫu lời nhắc trong LangChain dịch các câu hỏi hoặc tin nhắn của người dùng thành rõ ràng

hướng dẫn.

Mô hình ngôn ngữ sử dụng các hướng dẫn này để tạo ra các phản hồi phù hợp và mạch lạc.

Các loại mẫu nhắc nhở là Chuỗi mẫu nhắc nhở rất hữu ích cho chuỗi đơn

định dạng.

Mẫu lời nhắc trò chuyện rất hữu ích cho danh sách tin nhắn và các mẫu cụ thể như Tin nhắn

mẫu lời nhắc bao gồm Mẫu lời nhắc tin nhắn AI, Mẫu lời nhắc tin nhắn hệ thống, Con người

Mẫu nhắc tin nhắn và Mẫu nhắc tin nhắn trò chuyện cho phép phân công vai trò linh hoạt.

Trình giữ chỗ Tin nhắn cung cấp toàn quyền kiểm soát việc hiển thị tin nhắn.

Và Xem mẫu nhắc bắn cung cấp các ví dụ hoặc ảnh chụp cụ thể cho LLM.

Hãy sử dụng mẫu lời nhắc trò chuyện để tạo phản hồi.

Trong mẫu lời nhắc này, hãy chỉ định vai trò và nội dung của tin nhắn.

Tiếp theo, trong nội dung, hãy bao gồm các phần giữ chỗ tham số để sử dụng nhiều lần nhằm tạo ra

tin nhắn động và linh hoạt dựa trên các thông số đầu vào và định dạng lời nhắc của bạn.

Bây giờ chúng ta hãy xem các bộ chọn ví dụ trong mẫu lời nhắc.

Điều quan trọng là chọn những ví dụ phù hợp nhất từ thư viện ví dụ để đưa chúng vào

vào lời nhắc.

Bộ chọn ví dụ trong mẫu lời nhắc giúp quá trình này trở nên hiệu quả.

Ví dụ: Mẫu lời nhắc xem ảnh cung cấp các ví dụ hoặc ảnh cụ thể cho LLM.

Những ví dụ hoặc ảnh chụp này thông báo cho mô hình về bối cảnh được chèn và hướng dẫn LLM

tạo ra đầu ra mong muốn.

Bằng cách sử dụng các bộ chọn ví dụ từ LangChain, bạn có thể tối ưu hóa Mẫu nhắc nhở Xem ảnh

bằng cách chọn Tương tự về ngữ nghĩa, Mức độ liên quan cận biên tối đa cho tính đa dạng, Ví dụ về hiệu quả

Lời nhắc và sự chồng chéo N-Gram để tạo ra sự tương đồng về văn bản.

Màn hình hiển thị mã để chọn các ví dụ bằng cách sử dụng bộ chọn ví dụ N-Gram Overlap để

tạo thành một vài lời nhắc bắn.

Thành phần tiếp theo của LangChain là Trình phân tích cú pháp đầu ra.

Bộ phân tích cú pháp đầu ra chuyển đổi đầu ra của LLM thành định dạng phù hợp hơn để tạo

dữ liệu có cấu trúc.

LangChain cung cấp một thư viện Trình phân tích cú pháp đầu ra cho các định dạng dữ liệu khác nhau bao gồm

Các khung dữ liệu JSON, XML, CSV và Panda.

Trình phân tích cú pháp đầu ra cho phép bạn điều chỉnh đầu ra của mô hình để đáp ứng các nhu cầu xử lý dữ liệu cụ thể.

Ví dụ: hãy sử dụng Trình phân tích cú pháp đầu ra danh sách được phân tách bằng dấu phẩy để chuyển đổi phản hồi của LLM

sang định dạng CSV.

Trình phân tích cú pháp đầu ra này cấu trúc đầu ra một cách hiệu quả và đơn giản hóa nó để xử lý và

phân tích trong các ứng dụng bảng tính.

Bây giờ hãy tóm tắt lại.

Trong video này, bạn đã tìm hiểu về các thành phần của LangChain.

LangChain là một giao diện nguồn mở giúp đơn giản hóa quá trình phát triển ứng dụng

sử dụng LLM.

Các thành phần cốt lõi của LangChain là

Các mô hình ngôn ngữ trong LangChain sử dụng kiểu nhập văn bản để tạo đầu ra văn bản.

Mô hình trò chuyện hiểu câu hỏi hoặc lời nhắc và trả lời như con người.

Mô hình trò chuyện xử lý nhiều tin nhắn trò chuyện khác nhau như tin nhắn của con người, tin nhắn AI, tin nhắn hệ thống

thông báo, thông báo chức năng và thông báo công cụ.

Các mẫu lời nhắc trong LangChain chuyển các câu hỏi hoặc tin nhắn thành hướng dẫn rõ ràng.

Bạn cũng đã tìm hiểu về bộ chọn ví dụ hướng dẫn mô hình cho phần được chèn

bối cảnh và hướng dẫn LLM tạo ra đầu ra mong muốn.

Cuối cùng, bạn đã tìm hiểu về Trình phân tích cú pháp đầu ra giúp chuyển đổi đầu ra từ LLM thành

một định dạng phù hợp.