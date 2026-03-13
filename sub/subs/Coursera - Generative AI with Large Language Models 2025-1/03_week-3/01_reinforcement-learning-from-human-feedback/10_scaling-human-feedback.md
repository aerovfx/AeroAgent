# 10 phản hồi mở rộng của con người

---

Mặc dù bạn có thể

sử dụng mô hình khen thưởng

để loại bỏ sự cần thiết

đánh giá con người trong quá trình

Tinh chỉnh RLHF,

nỗ lực của con người

cần thiết để sản xuất

mô hình khen thưởng được đào tạo trong

vị trí đầu tiên là rất lớn.

Dữ liệu được dán nhãn

bộ dùng để tập luyện

mô hình phần thưởng thường

đòi hỏi lớn

đội dán nhãn,

đôi khi hàng ngàn

mọi người đánh giá nhé

nhiều lời nhắc mỗi.

Công việc này đòi hỏi

rất nhiều thời gian và

các tài nguyên khác có thể

yếu tố hạn chế quan trọng.

Theo số lượng mẫu mã

và các trường hợp sử dụng tăng lên,

nỗ lực của con người trở thành

một nguồn lực hạn chế

Các phương pháp để mở rộng phản hồi của con người

là một lĩnh vực nghiên cứu tích cực.

Một ý tưởng để vượt qua

những hạn chế này

là mở rộng quy mô thông qua

mô hình tự giám sát

AI hiến pháp là một

phương pháp giám sát quy mô

Được đề xuất lần đầu tiên vào năm 2022 bởi

các nhà nghiên cứu tại Anthropic,

AI hiến pháp là một phương pháp

cho các mô hình đào tạo sử dụng

một bộ quy tắc và

nguyên tắc chi phối

hành vi của mô hình.

Cùng với một bộ

lời nhắc mẫu,

những điều này tạo thành hiến pháp.

Sau đó, bạn huấn luyện mô hình để

tự phê bình và sửa lại

phản ứng của nó để tuân thủ

với những nguyên tắc đó.

AI hiến pháp rất hữu ích

không chỉ để mở rộng phản hồi,

nó cũng có thể giúp giải quyết

một số ngoài ý muốn

hậu quả của RLHF

Ví dụ, tùy theo cách

lời nhắc được cấu trúc,

một mô hình liên kết có thể

cuối cùng tiết lộ

thông tin có hại khi nó cố gắng

để cung cấp nhiều nhất

phản ứng hữu ích nó có thể.

Ví dụ, hãy tưởng tượng

bạn yêu cầu người mẫu

cung cấp cho bạn hướng dẫn về

làm thế nào để hack của bạn

WiFi của hàng xóm.

Bởi vì mô hình này

đã được căn chỉnh

ưu tiên sự hữu ích,

nó thực sự cho bạn biết về

một ứng dụng cho phép bạn làm điều này,

mặc dù điều này

hoạt động là bất hợp pháp.

Cung cấp cho người mẫu một bộ

các nguyên tắc hiến pháp có thể

giúp mô hình cân bằng

những lợi ích cạnh tranh này

và giảm thiểu tác hại.

Dưới đây là một số quy tắc ví dụ

từ bài nghiên cứu

AI Hiến pháp đó

Tôi yêu cầu LLM làm theo.

Ví dụ, bạn có thể

bảo người mẫu chọn

câu trả lời hay nhất

hữu ích, trung thực và vô hại.

Nhưng bạn có thể chơi

một số giới hạn về điều này,

yêu cầu người mẫu

ưu tiên sự vô hại bằng cách

đánh giá liệu nó có

phản ứng khuyến khích bất hợp pháp,

hoạt động phi đạo đức hoặc vô đạo đức.

Lưu ý rằng bạn không cần phải

sử dụng các quy tắc từ giấy,

bạn có thể xác định của riêng bạn

bộ quy tắc tốt nhất

phù hợp với bạn

miền và trường hợp sử dụng.

Khi triển khai các

Phương pháp AI hiến pháp,

bạn đào tạo mô hình của mình trong

hai giai đoạn riêng biệt.

Trong giai đoạn đầu tiên, bạn mang theo

học tập có giám sát,

để bắt đầu lời nhắc của bạn

mô hình theo những cách mà

cố gắng làm cho nó tạo ra

phản ứng có hại,

quá trình này là

được gọi là đội đỏ.

Sau đó bạn hỏi

mô hình để phê bình

nó có hại riêng

phản hồi theo

hiến pháp

nguyên tắc và

sửa đổi chúng để tuân thủ

với những quy tắc đó.

Sau khi hoàn tất, bạn sẽ tinh chỉnh

mô hình sử dụng

cặp đội đỏ

nhắc nhở và sửa đổi

những phản ứng mang tính hiến pháp.

Hãy xem một ví dụ về

làm thế nào một trong những lời nhắc này

cặp hoàn thành được tạo ra.

Hãy quay lại với

Vấn đề hack WiFi.

Như bạn đã thấy trước đó,

mô hình này mang lại cho bạn

phản ứng có hại

khi nó cố gắng tối đa hóa

sự hữu ích của nó.

Để giảm thiểu điều này, bạn

tăng cường lời nhắc

sử dụng sự hoàn thành có hại và

một tập hợp được xác định trước

hướng dẫn đó

yêu cầu người mẫu

phê bình phản ứng của nó.

Sử dụng các quy tắc được nêu

trong Hiến pháp,

mô hình phát hiện

vấn đề trong phản ứng của nó.

Trong trường hợp này, nó

thừa nhận chính xác

việc hack vào

WiFi của ai đó là bất hợp pháp.

Cuối cùng, bạn đặt tất cả các phần

cùng nhau và hỏi

mô hình để viết

một phản hồi mới loại bỏ

tất cả những điều có hại

hoặc nội dung bất hợp pháp.

Mô hình tạo ra một câu trả lời mới

điều đó đặt

nguyên tắc hiến pháp

vào thực tế và không

bao gồm tài liệu tham khảo

đến ứng dụng bất hợp pháp.

Lời nhắc ban đầu của đội đỏ,

và trận chung kết này

phản ứng hiến pháp

sau đó có thể được sử dụng

như dữ liệu huấn luyện.

You'll build up a data set of

nhiều ví dụ như

cái này để tạo ra

một NLM được tinh chỉnh

điều đó đã học được cách

để tạo ra

những phản ứng mang tính hiến pháp.

Phần thứ hai của

quá trình thực hiện

học tăng cường.

Giai đoạn này tương tự như RLHF,

ngoại trừ điều đó thay vào đó

phản hồi của con người,

bây giờ chúng tôi sử dụng phản hồi

được tạo ra bởi một mô hình.

Điều này đôi khi được đề cập

học tập củng cố

từ phản hồi AI hoặc RLAIF.

Ở đây bạn sử dụng

mô hình tinh chỉnh từ

bước trước đó để tạo

một tập hợp các câu trả lời

theo lời nhắc của bạn.

Sau đó bạn hỏi người mẫu

câu trả lời nào là

ưu tiên theo

nguyên tắc hiến pháp.

Kết quả là một mô hình được tạo ra

tập dữ liệu ưu tiên mà bạn

có thể sử dụng để đào tạo một mô hình phần thưởng.

Với mô hình khen thưởng này, bạn có thể

bây giờ hãy tinh chỉnh mô hình của bạn hơn nữa

sử dụng cốt thép

thuật toán học tập

giống như PPO, như đã thảo luận trước đó.

Căn chỉnh các mô hình là một

chủ đề rất quan trọng

và một lĩnh vực nghiên cứu tích cực.

Nền tảng của RLHF

mà bạn đã khám phá trong

bài học này sẽ cho phép bạn

làm theo như

lĩnh vực này phát triển.

Tôi thực sự vui mừng khi thấy

những khám phá mới nào

các nhà nghiên cứu thực hiện trong lĩnh vực này.

Tôi khuyến khích bạn giữ một

để ý đến bất kỳ phương pháp mới nào

và các phương pháp hay nhất

xuất hiện trong thời gian tới

tháng và năm