# 06 kỹ thuật nhắc-kỹ thuật tiên tiến

---

Khi bạn đã thiết lập mẫu lời nhắc cơ bản cho hệ thống RAG của mình,

bạn có thể bắt đầu thử các kỹ thuật kỹ thuật nhanh chóng nâng cao hơn.

Chúng ta hãy xem xét một vài trong số đó và khi nào bạn muốn sử dụng chúng.

Học tập trong ngữ cảnh là một kỹ thuật cho phép bạn giúp đỡ

LLM tìm hiểu loại đầu ra của bạn

muốn tạo bằng cách thêm các ví dụ về chúng vào dấu nhắc.

Ví dụ: nếu bạn đang xây dựng một chatbot dịch vụ khách hàng,

lời nhắc của bạn có thể bao gồm các ví dụ về yêu cầu của khách hàng trước đó,

cũng như những phản hồi chất lượng cao cho những yêu cầu đó.

Những ví dụ này giúp LLM tìm hiểu cấu trúc và

âm thanh nó nên sử dụng khi tạo ra phản hồi mới.

Giống như trong RAG,

bạn đang thêm thông tin bổ sung vào lời nhắc để làm nền tảng cho cách LLM phản hồi.

Nếu bạn bao gồm nhiều ví dụ,

Cách tiếp cận này được gọi là học vài lần.

Nếu bạn chỉ đưa ra một ví dụ,

nó được gọi là học một lần.

Có một số cách để triển khai việc học theo ngữ cảnh.

Bạn chỉ có thể mã hóa cứng một hoặc nhiều câu hỏi mẫu và câu trả lời vào lời nhắc của mình.

Trong trường hợp bạn muốn có một tập hợp hành vi LLM ổn định,

riêng điều này có thể giúp cải thiện chất lượng phản hồi.

Tuy nhiên, nếu bạn muốn thay đổi các ví dụ mỗi lần,

bạn có thể sử dụng RAG để truy xuất các câu hỏi và câu trả lời mẫu từ cơ sở kiến thức của mình.

Ví dụ: nếu bạn đang làm việc trên cùng một chatbot dịch vụ khách hàng đó,

bạn có thể lập chỉ mục các cuộc trò chuyện thành công của khách hàng vào cơ sở dữ liệu vectơ của mình.

Khi một khách hàng mới viết về một chủ đề cụ thể,

bạn có thể truy xuất nội dung của các cuộc trò chuyện trước đó về

chủ đề đó và đưa văn bản đó vào lời nhắc của bạn.

Theo nhiều cách, đây chỉ là RAG bình thường.

Nhưng thực tế là bạn đang truy xuất cụ thể

các câu trả lời mẫu có thể giúp cải thiện hơn nữa chất lượng phản hồi của LLM.

Một bộ sưu tập mạnh mẽ khác về các kỹ thuật kỹ thuật nhanh chóng,

về cơ bản khuyến khích LLM suy luận thông qua các lời nhắc theo cách từng bước.

Ví dụ: bạn có thể yêu cầu LLM trước tiên hãy suy nghĩ thành tiếng hoặc suy nghĩ từng bước,

về cách tốt nhất để tiếp cận vấn đề trước khi thực sự đưa ra câu trả lời cuối cùng.

Ý tưởng là về cơ bản bạn đang đưa ra mô hình ngôn ngữ

một bảng ghi nhớ để sắp xếp suy nghĩ trước khi trả lời.

Một cách phổ biến để làm điều này là nói với LLM rằng các mã thông báo giữa

Thẻ Scratchpad được coi là không gian để suy nghĩ

và động não chứ không phải là một phần của câu trả lời cuối cùng.

Một cách tiếp cận tương tự được gọi là chuỗi nhắc nhở suy nghĩ.

Theo cách tiếp cận này, LLM được hướng dẫn giải quyết các câu hỏi theo từng bước,

thay vì trả lời chúng ngay lập tức.

LLM có thể được hướng dẫn trước tiên tạo các bước cần thiết để trả lời một câu hỏi

rồi làm theo các bước đó.

Khuyến khích LLM lập kế hoạch và thực hiện phương pháp tiếp cận gia tăng này

có thể làm tăng khả năng phản hồi cuối cùng chính xác hơn.

Có thể nói, vì LLM sẽ thể hiện công việc của nó,

việc tìm ra các vấn đề cũng dễ dàng hơn khi lý luận của LLM không thành công.

Những chiến lược định hướng lý luận như thế này đã rất thành công

rằng nhiều LLM hiện được thiết kế để trở thành mô hình suy luận ngay lập tức.

Các mô hình lý luận vượt trội trong các nhiệm vụ lý luận phức tạp,

chẳng hạn như mã hóa, toán học, lập kế hoạch, câu đố,

và quy trình công việc phức tạp đòi hỏi nhiều bước.

Dưới lớp vỏ bọc, các mô hình lý luận này trước tiên tạo ra các mã thông báo lý luận

nơi họ có thể lên kế hoạch trước và cân nhắc các lựa chọn,

rất giống với bàn di chuột mà bạn đã thấy trước đây.

Sau đó, họ xuất mã thông báo phản hồi với phản hồi cuối cùng dự định cho người dùng.

Một số nhà cung cấp mô hình lý luận sẽ chỉ cung cấp quyền truy cập vào các mã thông báo phản hồi cuối cùng đó.

Những người khác cũng cho phép bạn truy cập vào các mã thông báo lý luận.

Những mã thông báo lý luận này là một phần giúp các mô hình này chính xác hơn

hơn so với những người không có lý trí.

Nhưng chúng vẫn chỉ là những token thông thường với tất cả các chi phí liên quan để tạo ra chúng.

Kết quả là, các mô hình lý luận thường chạy chậm hơn và tốn kém hơn.

Tùy thuộc vào ngữ cảnh của bạn, việc xây dựng hệ thống RAG xung quanh mô hình lý luận

có thể xứng đáng với chi phí cao hơn cho mỗi cuộc gọi LLM.

Ví dụ, các mô hình lý luận có thể đặc biệt tốt

khi đánh giá mức độ liên quan của tài liệu được truy xuất

và có thể có kỹ năng hơn trong việc quyết định cách tốt nhất để kết hợp thông tin đó vào phản hồi,

đặc biệt là một bài đòi hỏi nhiều bước suy luận phức tạp hơn.

Điều thú vị là nhiều kỹ thuật nhắc nhở không hoạt động tốt với các mô hình suy luận.

Ví dụ, bạn không cần yêu cầu họ suy nghĩ từng bước một,

vì đây là điều họ đã được đào tạo để làm.

Họ cũng có thể không học tốt trong bối cảnh,

khi họ cố gắng kết hợp các câu trả lời mẫu được cung cấp

vào câu hỏi hiện tại đang được trả lời.

Họ có xu hướng hoạt động tốt hơn với các mục tiêu cụ thể mà bạn muốn họ hướng tới

và thông tin rất cụ thể về hình thức mà bạn muốn họ trả lời.

Bạn vẫn có thể cung cấp các nguyên tắc hướng dẫn cấp cao

và nêu rõ các cách tiếp cận mà bạn muốn mô hình thực hiện hoặc tránh.

Tuy nhiên, sau đó, bạn có thể cung cấp cho họ toàn bộ kết xuất bối cảnh

của các tài liệu được lấy từ hệ thống RAG của bạn.

Các mô hình mới, bao gồm cả các mô hình suy luận, liên tục được đưa ra, tuy nhiên,

và hầu hết các nhà cung cấp LLM sẽ bao gồm thông tin về cách tốt nhất để nhắc họ.

Khi bạn bắt đầu sử dụng các kỹ thuật kỹ thuật nhanh chóng hơn,

quản lý cửa sổ ngữ cảnh sẽ trở nên quan trọng.

Hãy nhớ rằng lời nhắc ban đầu và bất kỳ mã thông báo nào mà LLM tạo ra để hoàn thành

cả hai đều sử dụng hết các phần của cửa sổ ngữ cảnh của nó.

Cho dù bạn đang đưa tài liệu từ chó tha mồi của mình vào,

thêm các ví dụ học tập theo ngữ cảnh vào mỗi lời nhắc,

hoặc có một mô hình lý luận lên kế hoạch trả lời trước khi trả lời một câu hỏi,

tất cả các kỹ thuật nâng cao này sẽ làm tăng độ dài lời nhắc của bạn,

phản hồi được tạo ra, hoặc cả hai.

Thật dễ dàng để nhanh chóng lấp đầy cửa sổ ngữ cảnh của bạn nếu bạn không chú ý.

Với các cuộc trò chuyện một lượt,

cách khắc phục tốt nhất là chỉ xác thực bạn đang nhận được giá trị

từ kỹ thuật kỹ thuật nhanh chóng của bạn.

Nếu nhắc nhở theo chuỗi suy nghĩ hoặc học tập theo ngữ cảnh

không mang lại cho bạn hiệu suất tốt hơn,

tốt hơn là bạn chỉ cần xóa những thành phần đó khỏi hệ thống của mình.

Cuộc trò chuyện nhiều lượt có thể nhanh chóng chiếm hết cửa sổ ngữ cảnh của bạn

vì mỗi tin nhắn qua lại cần được đưa vào lời nhắc.

Một loạt các cách tiếp cận được gọi chung là cắt tỉa bối cảnh

giải quyết vấn đề này.

Một giải pháp đơn giản là chỉ giữ một số lượng tin nhắn gần đây cố định trong lời nhắc.

Ví dụ: năm thông tin cuối cùng được gửi bởi người dùng và LLM.

Các cách tiếp cận phức tạp hơn sử dụng LLM riêng

để tóm tắt các tin nhắn cũ hơn, thu nhỏ kích thước của chúng,

nhưng vẫn bảo toàn được những điểm chính của họ.

Nếu bạn đang sử dụng mô hình lý luận trong cuộc trò chuyện nhiều lượt,

gần như chắc chắn bạn sẽ muốn loại bỏ các mã thông báo lý luận khỏi lịch sử trò chuyện

và chỉ giữ lại mã thông báo phản hồi.

Tương tự như vậy, trong hệ thống RAG,

bạn thường chỉ muốn bao gồm các khối được lấy

để hỗ trợ câu trả lời cho câu hỏi gần đây nhất,

không phải mọi câu hỏi đặt ra trước nó.

Tất nhiên, nếu ứng dụng của bạn cần hội thoại nhiều lượt

với bối cảnh sâu sắc và phong phú,

bạn luôn có thể chuyển sang sử dụng mô hình có cửa sổ ngữ cảnh dài hơn.

Điều đó có nghĩa là bạn vẫn cần suy nghĩ kỹ về cách thiết kế lời nhắc

ngay cả trên các mô hình có cửa sổ ngữ cảnh dài hơn,

lời nhắc dài sẽ chậm và tốn kém khi chạy.

Kỹ thuật kỹ thuật nhanh chóng có thể cải thiện hiệu suất LLM của bạn,

nhưng hệ thống RAG của bạn không nhất thiết phải sử dụng chúng.

Mẫu lời nhắc đơn giản và lời nhắc hệ thống được viết tốt

có thể là tất cả những gì bạn cần cho dự án của mình.

Khi nói đến các kỹ thuật tiên tiến hơn,

Tôi khuyên bạn chỉ nên thêm chúng vào dự án của mình sau khi rõ ràng là bạn cần chúng.

Nhắc nhở nói chung có thể mang tính nghệ thuật hơn là khoa học.

Vì vậy, bất kể bạn sử dụng chiến lược nào,

thử nghiệm với các lời nhắc khác nhau

và tìm những cái phù hợp nhất với hệ thống của bạn.