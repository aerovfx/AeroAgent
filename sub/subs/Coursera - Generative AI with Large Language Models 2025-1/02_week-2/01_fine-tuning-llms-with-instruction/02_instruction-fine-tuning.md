# 02 lệnh tinh chỉnh

---

Tuần trước, bạn đã được giới thiệu

vòng đời dự án AI tổng quát.

Bạn đã khám phá các trường hợp sử dụng mẫu cho

mô hình ngôn ngữ lớn và

đã thảo luận về các loại nhiệm vụ

đã có khả năng thực hiện.

Trong bài học này, bạn sẽ tìm hiểu về

phương pháp mà bạn có thể sử dụng để cải thiện

hiệu suất của một mô hình hiện có cho

trường hợp sử dụng cụ thể của bạn.

Bạn cũng sẽ tìm hiểu về tầm quan trọng

những thước đo có thể được sử dụng để đánh giá

hiệu suất của LLM đã được tinh chỉnh của bạn và

định lượng sự cải thiện của nó

mô hình cơ sở mà bạn đã bắt đầu.

Hãy bắt đầu bằng cách thảo luận về cách xử lý

điều chỉnh LLM bằng lời nhắc hướng dẫn.

Trước đó trong khóa học,

bạn thấy rằng một số mô hình có khả năng

hướng dẫn xác định

chứa trong một dấu nhắc và

thực hiện đúng số 0

bắn suy luận, trong khi những người khác,

chẳng hạn như LLM nhỏ hơn, có thể không mang được

thực hiện nhiệm vụ, giống như ví dụ hiển thị ở đây.

Bạn cũng thấy rằng bao gồm một hoặc nhiều

ví dụ về những gì bạn muốn mô hình thực hiện,

được gọi là suy luận một phát hoặc vài phát,

có thể đủ để giúp mô hình xác định

nhiệm vụ và tạo ra sự hoàn thành tốt.

Tuy nhiên, chiến lược này có

một vài nhược điểm.

Đầu tiên, đối với các mô hình nhỏ hơn,

nó không phải lúc nào cũng hoạt động,

ngay cả khi năm hoặc

sáu ví dụ được bao gồm.

Thứ hai, bất kỳ ví dụ nào bạn đưa vào

lời nhắc của bạn chiếm không gian quý giá

trong cửa sổ ngữ cảnh,

giảm số lượng phòng bạn có

để bao gồm các thông tin hữu ích khác.

May mắn thay, có một giải pháp khác,

bạn có thể tận dụng

một quá trình được gọi là tinh chỉnh

để đào tạo thêm một mô hình cơ sở.

Ngược lại với đào tạo trước,

nơi bạn đào tạo LLM bằng cách sử dụng rộng rãi

số lượng văn bản phi cấu trúc

dữ liệu thông qua học tập tự giám sát,

tinh chỉnh là một học tập có giám sát

quá trình bạn sử dụng dữ liệu

tập hợp các ví dụ được gắn nhãn để

cập nhật trọng số của LLM.

Các ví dụ được gắn nhãn

là các cặp hoàn thành nhanh chóng,

quá trình tinh chỉnh kéo dài

đào tạo mô hình để cải thiện

khả năng của nó để tạo ra tốt

hoàn thành một nhiệm vụ cụ thể.

Một chiến lược,

được gọi là tinh chỉnh hướng dẫn,

đặc biệt tốt trong việc cải thiện

hiệu suất của mô hình trong nhiều nhiệm vụ khác nhau.

Chúng ta hãy đến gần hơn

hãy xem cách nó hoạt động,

hướng dẫn tinh chỉnh xe lửa

mô hình sử dụng các ví dụ

chứng minh nó sẽ phản ứng như thế nào

theo một hướng dẫn cụ thể.

Dưới đây là một vài ví dụ

gợi ý để chứng minh ý tưởng này.

Hướng dẫn trong cả hai ví dụ

đang phân loại bài đánh giá này,

và sự hoàn thành mong muốn là

một chuỗi văn bản bắt đầu bằng

tình cảm theo sau là tích cực hoặc

tiêu cực.

Tập dữ liệu bạn sử dụng để đào tạo bao gồm

nhiều cặp ví dụ hoàn thành nhanh chóng

cho nhiệm vụ mà bạn quan tâm,

mỗi trong số đó bao gồm một hướng dẫn.

Ví dụ, nếu bạn muốn phạt

điều chỉnh mô hình của bạn để cải thiện nó

khả năng tóm tắt, bạn sẽ xây dựng

thiết lập một tập hợp dữ liệu các ví dụ bắt đầu

với hướng dẫn tóm tắt,

văn bản sau đây hoặc một cụm từ tương tự.

Và nếu bạn đang cải thiện

kỹ năng dịch thuật của người mẫu,

ví dụ của bạn sẽ bao gồm hướng dẫn

thích dịch câu này.

Những ví dụ hoàn thành nhanh chóng này

cho phép mô hình học cách tạo ra

những câu trả lời theo sau

các hướng dẫn đã cho.

Hướng dẫn tinh chỉnh,

trong đó tất cả trọng lượng của mô hình

được cập nhật được gọi là tinh chỉnh đầy đủ.

Quá trình này dẫn đến một phiên bản mới

của mô hình với trọng số được cập nhật.

Điều quan trọng cần lưu ý là giống như

yêu cầu đào tạo trước, tinh chỉnh đầy đủ

đủ bộ nhớ và ngân sách điện toán để

lưu trữ và xử lý tất cả các gradient,

trình tối ưu hóa và các thành phần khác

đang được cập nhật trong quá trình đào tạo.

Vì vậy bạn có thể hưởng lợi từ

tối ưu hóa bộ nhớ và

chiến lược tính toán song song

mà bạn đã học tuần trước.

Vậy bạn thực sự tiến hành như thế nào

hướng dẫn, tinh chỉnh và LLM?

Bước đầu tiên là

chuẩn bị dữ liệu đào tạo của bạn.

Có rất nhiều công khai

các tập dữ liệu đã được sử dụng để

đào tạo thế hệ trước

của các mô hình ngôn ngữ,

mặc dù hầu hết trong số họ không

định dạng như hướng dẫn.

May mắn thay, các nhà phát triển đã tập hợp lời nhắc

thư viện mẫu có thể được sử dụng

để lấy các tập dữ liệu hiện có, ví dụ:

bộ dữ liệu lớn của sản phẩm Amazon

đánh giá và biến chúng thành hướng dẫn

bộ dữ liệu nhanh chóng để tinh chỉnh.

Thư viện mẫu nhắc nhở bao gồm nhiều

mẫu cho các nhiệm vụ khác nhau và

bộ dữ liệu khác nhau.

Dưới đây là ba lời nhắc

được thiết kế để hoạt động với Amazon

đánh giá tập dữ liệu và

có thể được sử dụng để tinh chỉnh các mô hình cho

phân loại, tạo văn bản và

nhiệm vụ tóm tắt văn bản.

Bạn có thể thấy rằng trong mỗi trường hợp bạn vượt qua

đánh giá ban đầu, ở đây được gọi là review_body,

vào mẫu, nơi nó được chèn vào

vào văn bản bắt đầu bằng

một hướng dẫn như dự đoán liên quan

xếp hạng, tạo đánh giá theo sao,

hoặc đưa ra một câu ngắn mô tả

đánh giá sản phẩm sau.

Kết quả là một lời nhắc rằng bây giờ

chứa cả hướng dẫn và

ví dụ từ tập dữ liệu.

Khi bạn có dữ liệu hướng dẫn của mình

chuẩn bị sẵn sàng, như với tiêu chuẩn được giám sát

học, bạn chia tập dữ liệu thành

xác nhận đào tạo và phân chia kiểm tra.

Trong quá trình tinh chỉnh, bạn chọn lời nhắc

từ tập dữ liệu đào tạo của bạn và

chuyển chúng cho LLM,

sau đó tạo ra sự hoàn thành.

Tiếp theo, bạn so sánh việc hoàn thành LLM với

phản hồi được chỉ định

trong dữ liệu huấn luyện.

Bạn có thể thấy ở đây rằng mô hình

đã không làm tốt công việc,

nó phân loại đánh giá là trung lập,

đó là một cách nói nhẹ nhàng.

Đánh giá rõ ràng là rất tích cực.

Hãy nhớ rằng đầu ra của LLM là

phân phối xác suất trên các mã thông báo.

Vì vậy, bạn có thể so sánh sự phân phối

về việc hoàn thành và

của nhãn đào tạo và

sử dụng hàm crossentropy tiêu chuẩn để

tính toán tổn thất giữa

hai phân phối mã thông báo.

Và sau đó sử dụng tổn thất được tính toán để cập nhật

mô hình của bạn nặng

lan truyền ngược tiêu chuẩn.

Bạn sẽ làm điều này trong nhiều đợt nhắc nhở

cặp hoàn thành và qua nhiều kỷ nguyên,

cập nhật các trọng số để mô hình

hiệu suất thực hiện nhiệm vụ được cải thiện.

Giống như trong học tập có giám sát tiêu chuẩn,

bạn có thể xác định đánh giá riêng biệt

các bước để đo lường hiệu suất LLM của bạn

bằng cách sử dụng tập dữ liệu xác thực giữ lại.

Điều này sẽ cho bạn

độ chính xác xác nhận và

sau khi bạn hoàn thành việc tinh chỉnh,

bạn có thể biểu diễn màn trình diễn cuối cùng

đánh giá bằng cách sử dụng

tập dữ liệu thử nghiệm nắm giữ.

Điều này sẽ cung cấp cho bạn độ chính xác kiểm tra.

Quá trình tinh chỉnh dẫn đến

một phiên bản mới của mẫu cơ sở,

thường được gọi là mô hình hướng dẫn

tốt hơn trong các nhiệm vụ mà bạn quan tâm.

Tinh chỉnh với lời nhắc hướng dẫn là

cách phổ biến nhất để

tinh chỉnh LLM ngày nay.

Từ thời điểm này trở đi, khi bạn nghe hoặc

xem thuật ngữ tinh chỉnh,

bạn có thể cho rằng nó luôn luôn

có nghĩa là hướng dẫn tinh chỉnh.