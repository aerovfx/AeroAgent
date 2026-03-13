# 01 - Sự chú ý và tầm quan trọng của nó trong các mô hình trình tự

---

- [Người hướng dẫn] Mạng bộ nhớ ngắn hạn dài

và các đơn vị định kỳ có kiểm soát

là hai kiến trúc deep learning phổ biến,

được thiết kế đặc biệt để khắc phục

vấn đề thành phần biến mất.

Mặc dù những mô hình này có thể nắm bắt

nhiều ngữ cảnh hơn RNN cơ bản,

họ vẫn dựa vào một vector duy nhất

để mang thông tin quan trọng qua nhiều bước thời gian.

Sự phụ thuộc này cuối cùng đã hạn chế

bao nhiêu bối cảnh có thể được giữ lại

và sử dụng có hiệu quả,

đặc biệt là khi xử lý các chuỗi rất dài.

Năm 2017, một sự thay đổi lớn đã xảy ra trong mô hình trình tự

với sự giới thiệu của máy biến áp trong bài báo,

"Sự chú ý là tất cả những gì bạn cần."

Thay vì phụ thuộc vào sự tái diễn,

máy biến áp sử dụng sự chú ý,

một cơ chế mạnh mẽ cho phép các mô hình

để nhìn trực tiếp vào bất kỳ phần nào của đầu vào

khi tạo hoặc phân tích đầu ra.

Tự chú ý, một biến thể của sự chú ý,

cho phép mỗi phần tử trong một chuỗi,

ví dụ, một từ,

để kiểm tra mọi yếu tố khác

trong dãy, kể cả chính nó,

để quyết định mức độ chú ý dành cho nó.

Điều này cho phép mô hình nắm bắt được bối cảnh

từ toàn bộ chuỗi trong một bước

thay vì dựa vào

về phương pháp xử lý từ trái sang phải truyền thống

được sử dụng bởi các biến thể RNN và RNN.

Sự chú ý giải quyết một số thách thức

mà các kiến trúc dựa trên RNN trước đó phải đối mặt.

Bằng cách tham chiếu trực tiếp bất kỳ phần nào của đầu vào,

sự chú ý bỏ qua sự cần thiết

để nén mọi thứ vào một vectơ ẩn duy nhất,

làm cho nó hiệu quả hơn nhiều trong việc xử lý lâu dài

hoặc trình tự phức tạp.

Trình tự xử lý RNN truyền thống và các biến thể RNN

một cách tuần tự chặt chẽ,

trong khi sự chú ý cho phép xử lý mã thông báo song song.

Điều này tăng tốc độ đào tạo

và suy luận trong các nhiệm vụ quy mô lớn.

Trọng số chú ý có thể được hiển thị để tiết lộ mã thông báo nào

hoặc những từ mà mô hình tập trung vào.

Tính minh bạch này có thể giúp các nhà phát triển hiểu

và gỡ lỗi hành vi mô hình.

Cuối cùng, sự chú ý tăng cường

hiệu suất của các mô hình trình tự

bằng cách cải thiện khả năng nắm bắt bối cảnh của họ.

Hãy xem xét hai kịch bản

giúp minh họa điểm cuối cùng này.

Hãy xem xét một mô hình đang cố gắng hoàn thành câu,

"Con mèo béo ngồi trên chiếu vì nó."

Nó ám chỉ con mèo hay tấm thảm?

Một mô hình sử dụng sự tự chú ý có thể học hỏi

để gán trọng lượng cao hơn cho con mèo

nếu nó suy ra rằng nó đang đề cập đến con vật,

dẫn đến việc hoàn thành câu, như,

"muốn một chỗ thoải mái để ngủ trưa."

Mặt khác, nếu mô hình tập trung nhiều hơn vào thảm,

nó có thể tạo ra "là thứ gần gũi nhất xung quanh."

Bởi vì sự tự chú ý gán trọng số đã học cho mỗi từ,

nó có thể xử lý việc định hướng đại từ hiệu quả hơn

hơn các mô hình dựa vào một trạng thái ẩn duy nhất

để lưu trữ tất cả bối cảnh.

Bây giờ, giả sử chúng ta dự định

để dịch câu sau từ tiếng Anh sang tiếng Pháp,

"Con mèo đen đang ngủ."

Khi dịch từ ngôn ngữ này sang ngôn ngữ khác,

dịch trực tiếp từng từ thường thất bại,

Trong tiếng Pháp hầu hết nhưng không phải tất cả tính từ

làm theo danh từ mà họ mô tả.

Thế là con mèo đen đang ngủ được dịch (nói tiếng Pháp)

và không (nói tiếng Pháp).

Đây là cơ chế chú ý của mô hình

học cách sắp xếp các từ mèo

và màu đen phù hợp trong câu dịch

sử dụng cơ chế chú ý bộ mã hóa-giải mã,

đó là một loại chú ý cụ thể trong máy biến áp.

Nó biết rằng màu đen thay đổi con mèo

và nên được đặt sau nó

khi nó được dịch sang tiếng Pháp.

Để được giải thích chi tiết hơn về cơ chế chú ý

và nó thực sự hoạt động như thế nào,

Tôi giới thiệu hai video

trong AI sáng tạo:

Giới thiệu khóa học Mô hình ngôn ngữ lớn.

Các video có tiêu đề "Cơ chế chú ý"

và "Tính tự chú ý hoạt động như thế nào?"

Nhìn chung, địa chỉ tự chú ý

nhiều nhược điểm của các mô hình trình tự cũ

bằng cách cho phép tham chiếu trực tiếp

đến bất kỳ phần nào của đầu vào,

đến lượt nó, hỗ trợ nắm bắt các phần phụ thuộc tầm xa,

xử lý các cấu trúc ngôn ngữ phức tạp,

và làm tê liệt quá trình xử lý các trình tự.

Trong video tiếp theo,

chúng tôi sẽ kiểm tra

làm thế nào những ý tưởng này kết hợp với nhau trong máy biến áp

và kiến trúc bộ mã hóa-giải mã.