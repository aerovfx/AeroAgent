# 01 case-study-intro

---

Xin chào các bạn học viên. Có một

trợ lý mã đáng tin cậy có thể

tăng cường đáng kể mã

năng suất và giảm địa vị.

Cho dù bạn là trợ lý

nhà phát triển hoặc người mới,

một trợ lý mã nâng cao

có thể cung cấp giá trị

gợi ý,

mã tự động hoàn thành và thậm chí

tạo ra toàn bộ chức năng,

thực hiện quá trình mã hóa

mượt mà và hiệu quả hơn.

Chào mừng đến với buổi thực hành của chúng tôi

bài học về việc lựa chọn

một LLM phù hợp để phát triển

một trợ lý mã nâng cao.

Một LLM được lựa chọn tốt có thể hoạt động

như một người bạn đồng hành mạnh mẽ,

tạo mã chính xác

không có bất kỳ lỗi nào,

và cải thiện đáng kể

năng suất của nhà phát triển.

Trong video này, chúng tôi sẽ

tìm hiểu về các bước chính

liên quan đó là cách tiếp cận

để xây dựng một tập lệnh tự động,

ma trận đánh giá mà chúng tôi

sẽ dùng để so sánh

các mô hình LLM,

và lý do lựa chọn

các mô hình ứng cử viên mà chúng tôi

sẽ sử dụng trong thí nghiệm của chúng tôi.

Đến cuối bài học này,

bạn sẽ có một cái nhìn rõ ràng

sự hiểu biết về cách

chọn LLM phù hợp

cho trợ lý mã của bạn,

so sánh giữa một

danh sách ứng viên LLM

thông qua một quá trình có cấu trúc

về kiểm tra và đánh giá.

Hãy bắt đầu.

Trong cách tiếp cận của chúng tôi,

đầu tiên chúng ta sẽ thiết lập

số liệu và bài kiểm tra

thử thách mã hóa.

Điều này rất quan trọng vì nó hình thành

nền tảng của

đánh giá của chúng tôi.

Chúng ta sẽ giải quyết một vấn đề về mã hóa

cho trợ lý mã của chúng tôi

để được thử nghiệm.

Tiếp theo chúng ta sẽ chuyển sang phần thử nghiệm

và so sánh kết quả.

Sau này chúng tôi sẽ chọn

LLM tạo ra

mã tự động cho

vấn đề mã hóa nhất định.

Bước này là nơi chúng ta sẽ

nắm bắt được sự khác biệt trong

kết quả thực hiện

trên các mô hình của chúng tôi.

Bước thứ ba là hiểu

ma trận thử nghiệm và so sánh của chúng tôi.

Chúng tôi đã xác định được năm

ma trận then chốt để đánh giá

LLM trong bối cảnh

trợ lý mã hóa.

Tính đúng đắn, chúng tôi sẽ đánh giá như thế nào

logic và chính xác

các giải pháp được tạo ra là

Hiệu quả, mã

trợ lý nên

cung cấp không chỉ chính xác,

nhưng mã được tối ưu hóa.

Khả năng đọc, rõ ràng,

mã có cấu trúc tốt là

cần thiết cho khả năng bảo trì.

Cách thực hành tốt nhất, chúng tôi sẽ

kiểm tra xem mã

tuân thủ các quy định đã được thiết lập

các tiêu chuẩn và thực hành mã hóa,.

Nhận xét để đánh giá

LLM tốt thế nào

giải thích mã của nó và

logic thông qua nhận xét.

Toàn bộ quá trình được tự động hóa,

Thực hiện và tính toán LLM

điểm tổng thể cho mỗi LLM.

Cách tiếp cận theo chương trình này

cho phép chúng tôi dễ dàng chạy lại

sự so sánh của chúng tôi như

mô hình mới trở thành

có sẵn như của chúng tôi

yêu cầu phát triển.

Bằng cách làm theo tiêu chuẩn này

và trường hợp có cấu trúc

phương pháp nghiên cứu,

chúng tôi đảm bảo rằng

lựa chọn LLM cho

mã hóa nâng cao của chúng tôi

trợ lý dựa trên

trên dữ liệu liên quan cụ thể

thay vì giả định

hoặc danh tiếng chung.

Chúng tôi đã lựa chọn cẩn thận ba

các mô hình để chúng tôi đánh giá,

mỗi cái mang lại sự độc đáo

sức mạnh lên bảng.

Đầu tiên, chúng ta có

EleutherAI/gpt-neo-125 triệu,

một người mẫu được công nhận

ngôn ngữ mục đích chung của nó

khả năng thế hệ.

Đó là một sản phẩm đa năng

tùy chọn cung cấp

cơ sở vững chắc để so sánh.

Tiếp theo, chúng tôi đã chọn

lực lượng bán hàng mã hóa,

trong đó có 350

triệu tham số.

Đây là một mô hình

được thiết kế đặc biệt

cho các nhiệm vụ tạo mã.

Chuyên môn của nó trong việc này

khu vực làm cho nó trở nên mạnh mẽ

container để sản xuất cao

mã được tối ưu hóa chất lượng.

Cuối cùng, chúng tôi đã bao gồm

ÔmFaceTB/SmollM-360

triệu.

Mô hình này cũng tập trung vào

tạo mã và được biết đến

vì hiệu quả trong khi

vẫn đang giao hàng

kết quả có thẩm quyền.

Kích thước nhỏ hơn có thể cung cấp

lợi thế về mặt

tốc độ và sử dụng tài nguyên.

Bằng cách đánh giá ba mô hình,

chúng tôi mong muốn tìm hiểu

cái phù hợp nhất

để xây dựng một môi trường đáng tin cậy và

trợ lý mã hiệu quả.

Trong video này, bạn đã

được giới thiệu với

các trạng thái cần thiết cho

lựa chọn một LLM phù hợp cho

phát triển nâng cao

trợ lý mã.

Bây giờ bạn đã hiểu

cách tiếp cận dành cho

xây dựng tập lệnh tự động,

ma trận đánh giá,

điều đó sẽ hướng dẫn chúng ta

so sánh và lý do

đằng sau sự lựa chọn

của ứng cử viên

mô hình cho thí nghiệm của chúng tôi

Với nền tảng này, bạn

sẵn sàng đi sâu hơn vào

quá trình và thực hiện

những quyết định sáng suốt khi chúng ta di chuyển

tiến lên trong xây dựng

trợ lý mã của bạn.

Công việc tuyệt vời, và tôi

mong được tiếp tục

cuộc hành trình này với bạn.

Bây giờ tôi có một câu hỏi dành cho bạn.