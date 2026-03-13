# 01 giới thiệu-tuần-3

---

Chào mừng trở lại.

Tuần trước bạn đã tìm hiểu về

điều chỉnh hướng dẫn cho

mô hình ngôn ngữ lớn cũng như peft.

Tuần này chúng ta sẽ đi sâu vào RLHF,

học tăng cường

từ phản hồi của con người.

Một trong những kỹ thuật mà bạn có thể

có thể đã nghe về tin tức này, nhưng

nó thực sự hoạt động như thế nào?

Chúng ta sẽ đi sâu vào vấn đề đó

cũng như điều thứ hai, tôi nghĩ,

chủ đề rất thú vị về cách sử dụng

LLM như một công cụ lý luận và

hãy để nó gây ra cái riêng của chúng ta

các thủ tục để tạo ra một đại lý.

Họ có thể hành động.

>> RLHF thực sự rất thú vị.

Nó giúp căn chỉnh mô hình

với những giá trị nhân văn.

Vì vậy, ví dụ,

LLM có thể có một thách thức ở chỗ

tạo ra nội dung đôi khi có hại hoặc

như một giọng điệu hoặc giọng nói độc hại.

Và bằng cách căn chỉnh mô hình

với phản hồi của con người và

sử dụng cốt thép

học như một thuật toán.

Bạn có thể giúp căn chỉnh mô hình cho phù hợp

giảm bớt điều đó và hướng tới,

nội dung ít độc hại hơn và

nội dung hữu ích hơn nhiều.

>> Đôi khi người ta cảm thấy như

LLM huấn luyện về điều khủng khiếp này,

một số dữ liệu internet khủng khiếp cảm thấy như vậy

nguy hiểm.

Tôi nghĩ nhiều người dưới

đánh giá cao RLHF mạnh mẽ như thế nào.

Nó chắc chắn là không hoàn hảo.

LLM tạo ra đầu ra có vấn đề.

Nhưng có cảm giác như với

sự tiến bộ của công nghệ,

các nhà nghiên cứu đang liên tục thực hiện

họ nhiều hơn, tôi đoán là HS, phải không?

Trung thực, hy vọng và vô hại.

>> Vâng, hoàn toàn có.

Và tôi sẽ tham gia vào tuần này,

Nhân tiện,

bởi một nhà khoa học ứng dụng từ Amazon

ai sẽ giải thích phía sau một chút

các thuật toán đang được sử dụng trong

học tăng cường cho mục đích này.

Vì vậy, tôi đang mong chờ điều đó.

Đây là Ek phải không?

Ai sẽ tham gia cùng chúng tôi?

Chắc chắn, chúng tôi cũng đã mời Dr.

Nashley Sepus, người sẽ nói chuyện

với chúng tôi về AI có trách nhiệm.

>> Đúng vậy.

Ashley sẽ tham gia cùng chúng tôi,

và tôi sẽ có một cuộc thảo luận

với cô ấy xung quanh chủ đề trách nhiệm

AI, điều này cũng rất quan trọng.

>> Và tôi thực sự vui mừng vì bạn

đã dành rất nhiều thời gian cho việc này.

Rủi ro AI là điều mà rất nhiều người gặp phải

mọi người đang suy nghĩ đúng đắn.

Và tôi nghĩ mức độ nghiêm trọng của nó

Sophie, tất cả các đội AI lớn mà tôi biết

đang thực hiện điều này và nỗ lực về nguồn lực

không suy nghĩ được, chúng ta còn lâu mới hoàn hảo.

Nhưng Sophie cảm thấy như cộng đồng

làm việc rất chăm chỉ để cải thiện điều này

hàng năm.

Và ngoài AI có trách nhiệm và

điều chỉnh các mô hình bằng RLHF,

kỹ thuật khác mà tôi rất hào hứng

về việc sử dụng OMS làm công cụ suy luận.

Và trao cho họ sức mạnh để thực hiện

các lệnh gọi chương trình con riêng để có thể thực hiện một trang web

tìm kiếm hoặc thực hiện các hành động khác.

>> Chắc chắn và

chúng ta sẽ tìm hiểu điều đó trong bài học này.

Và chúng ta sẽ nói về một số kỹ thuật

cho phép bạn di chuyển xung quanh một số

những hạn chế mà chúng ta thấy với quy mô lớn

mô hình ngôn ngữ bằng cách cho phép họ

lý do hành động thông qua

các kỹ thuật như phản ứng.

Chúng ta cũng sẽ nói về Rag, cho phép

bạn cũng có thể truy cập các nguồn bên ngoài

thông tin để bạn có thể truy cập

thông tin cụ thể về tên miền.

Chúng tôi thấy rất nhiều khách hàng muốn

để có thể kết hợp thông tin

từ các nguồn dữ liệu độc quyền vào

các ứng dụng sáng tạo của chúng.

Vì vậy chúng ta nói một chút về

một số kỹ thuật đó và

phương pháp cho phép bạn làm điều đó.

>> Một điều về người khổng lồ

mô hình ngôn ngữ là như vậy

giỏi ghi nhớ sự thật.

Bạn đang tìm hiểu thông tin thực tế trên Internet.

Đôi khi người ta sử dụng chúng như một kho lưu trữ

sự thật để có được câu trả lời cho

câu hỏi.

Nhưng tôi nghĩ có một sự khác biệt và

có lẽ tôi nghĩ,

cách hữu ích hơn để nghĩ về OMS,

đó là nếu nó là một công cụ lý luận và

bạn cung cấp cho nó API để lấy nó

sự thật của riêng mình bởi vì nó ổn.

Nhưng không phải là cơ sở dữ liệu thực tế tốt nhất,

nhưng nó là một công cụ lý luận rất tốt.

Và điều đó, tôi nghĩ,

là sức mạnh thực sự của những mô hình này.

>> Chắc chắn là tiết kiệm chi phí hơn rất nhiều,

đúng.

Sử dụng cơ sở dữ liệu cho thông tin đó,

và sau đó là AI sáng tạo của bạn cho việc đó,

nó dùng để làm gì.

>> Đó thực sự là một điểm tuyệt vời.

>> [CƯỜI]

>> Và cùng với đó, tuần cuối cùng này

có rất nhiều điều thú vị,

Tôi tin chắc rằng bạn sẽ thích nó.

Và vì vậy hãy chuyển sang video tiếp theo

Antir sẽ bắt đầu đi sâu vào RLHF.