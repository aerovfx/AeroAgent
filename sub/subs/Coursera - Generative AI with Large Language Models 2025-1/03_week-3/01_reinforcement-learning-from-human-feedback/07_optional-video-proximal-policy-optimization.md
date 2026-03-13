# 07 tùy chọn-video-proximal-tối ưu hóa chính sách

---

Tiến sĩ Ehsan Kamalinejad,

người thường gọi là EK,

là một máy học

nhà khoa học ứng dụng.

Anh hiện là nhà khoa học ưu tú

làm việc về NLP

sự phát triển ở Amazon.

Trước đây, anh ấy

đồng sáng lập Visual One,

khởi động Y Combinator

trong thị giác máy tính.

Trước đó, anh ấy đã

một máy dẫn đầu công nghệ

kỹ sư đang học tại Apple,

làm việc trên các dự án

chẳng hạn như ký ức.

EK cũng là một

Phó giáo sư của

Toán học ở California

Đại học bang, Vịnh Đông.

EK, cảm ơn vì

tham gia cùng tôi hôm nay để

thảo luận về việc tăng cường PPO

thuật toán học tập.

Cảm ơn vì đã có tôi.

PPO có ý nghĩa gì

để làm gì và làm gì

những thuật ngữ đó có nghĩa là

bối cảnh của

học tăng cường?

PPO là viết tắt của Gần.

Tối ưu hóa chính sách,

đó là một sức mạnh

thuật toán cho

giải quyết củng cố

vấn đề học tập.

Đúng như tên gọi,

PPO tối ưu hóa chính sách,

trong trường hợp này là LLM,

để phù hợp hơn với

sở thích của con người.

Trải qua nhiều lần lặp lại, PPO

thực hiện cập nhật cho LLM.

Các bản cập nhật nhỏ và

trong một vùng giới hạn,

dẫn đến LLM được cập nhật

cái đó gần với

phiên bản trước,

do đó có tên là Proximal

Tối ưu hóa chính sách.

Giữ những thay đổi bên trong

kết quả khu vực nhỏ này

học tập ổn định hơn.

Mục tiêu là cập nhật

chính sách sao cho

phần thưởng được tối đa hóa.

Bạn có thể thảo luận

cái này hoạt động như thế nào

bối cảnh cụ thể của

mô hình ngôn ngữ lớn?

Vâng, rất vui được.

Bạn bắt đầu PPO với

hướng dẫn ban đầu LLM,

thì ở mức độ cao,

mỗi chu kỳ của PPO

trải qua hai giai đoạn.

Trong Giai đoạn I, LLM,

được sử dụng để thực hiện một

số thí nghiệm,

hoàn thành các gợi ý đã cho.

Những thí nghiệm này

cho phép bạn cập nhật

LLM chống lại

mô hình khen thưởng trong Giai đoạn II.

Hãy nhớ rằng mô hình phần thưởng

nắm bắt được sở thích của con người.

Ví dụ như phần thưởng

có thể xác định mức độ hữu ích,

vô hại và trung thực

các câu trả lời là

Phần thưởng dự kiến

hoàn thành là

một lượng quan trọng được sử dụng

trong mục tiêu PPO.

Chúng tôi ước tính điều này

số lượng thông qua

một người đứng đầu riêng của LLM

gọi là hàm giá trị.

Chúng ta hãy xem xét kỹ hơn

hàm giá trị

và sự mất giá trị.

Giả sử một số

lời nhắc được đưa ra.

Đầu tiên, bạn tạo LLM

trả lời các gợi ý,

sau đó bạn tính toán

phần thưởng cho

sự hoàn thành nhanh chóng

sử dụng mô hình khen thưởng.

Ví dụ, lần đầu tiên

hoàn thành nhanh chóng được hiển thị

ở đây có thể nhận được

phần thưởng là 1,87.

Người tiếp theo có thể nhận được một

phần thưởng -1,24, v.v.

Bạn có một bộ

hoàn thành nhanh chóng

và phần thưởng tương ứng của họ.

Hàm giá trị ước lượng

tổng phần thưởng dự kiến cho một

cho trạng thái S. Nói cách khác,

khi LLM tạo ra mỗi

dấu hiệu của sự hoàn thành,

bạn muốn ước tính

tổng phần thưởng trong tương lai

dựa trên hiện tại

chuỗi các token.

Bạn có thể nghĩ về điều này như

cơ sở để đánh giá

chất lượng hoàn thiện

chống lại các tiêu chí liên kết của bạn.

Hãy nói điều đó vào lúc này

bước hoàn thiện,

tương lai ước tính

tổng phần thưởng là 0,34.

Với mã thông báo được tạo tiếp theo,

tổng số ước tính trong tương lai

phần thưởng tăng lên 1,23.

Mục tiêu là giảm thiểu

sự mất giá trị đó là

sự khác biệt giữa

tổng số thực tế trong tương lai

phần thưởng trong ví dụ này,

1,87 và giá trị gần đúng của nó

đến hàm giá trị,

trong ví dụ này là 1,23.

Sự mất giá trị làm cho

ước tính cho tương lai

thưởng chính xác hơn.

Hàm giá trị

sau đó được sử dụng trong

Ước tính lợi thế trong Giai đoạn 2,

mà chúng ta sẽ thảo luận một chút.

Điều này tương tự như khi bạn

bắt đầu viết một đoạn văn,

và bạn có một ý tưởng sơ bộ về

hình thức cuối cùng của nó thậm chí

trước khi bạn viết nó.

[không nghe được] bạn đã đề cập đến điều đó

những tổn thất và

phần thưởng được xác định trong

Giai đoạn 1 được sử dụng ở giai đoạn 2

để cập nhật trọng số

dẫn đến một LLM được cập nhật.

Bạn có thể giải thích quá trình này

chi tiết hơn một chút?

Chắc chắn. Trong giai đoạn 2,

bạn thực hiện một cập nhật nhỏ

vào mô hình và đánh giá

tác động của những cập nhật đó đối với

mục tiêu liên kết của bạn

cho mô hình.

Các cập nhật trọng lượng mô hình là

được hướng dẫn bởi việc hoàn thành nhanh chóng,

tổn thất và phần thưởng.

PPO cũng đảm bảo giữ

mô hình cập nhật bên trong

một khu vực nhỏ nhất định

gọi là vùng tin cậy.

Đây là nơi gần nhất

khía cạnh của PPO phát huy tác dụng.

Lý tưởng nhất là loạt bài này

những cập nhật nhỏ

sẽ di chuyển mô hình

hướng tới phần thưởng cao hơn.

Mục tiêu chính sách PPO

là thành phần chính

của phương pháp này.

Hãy nhớ rằng,

mục tiêu là tìm

một chính sách được kỳ vọng

phần thưởng rất cao.

Nói cách khác, bạn đang cố gắng

thực hiện cập nhật cho

LLM cân nhắc điều đó

kết quả là hoàn thành

phù hợp hơn với

sở thích của con người và như vậy

nhận được phần thưởng cao hơn.

Sự mất mát chính sách là

mục tiêu chính đó

thuật toán PPO cố gắng

tối ưu hóa trong quá trình đào tạo.

Tôi biết toán

có vẻ phức tạp,

nhưng nó thực sự là

đơn giản hơn nó xuất hiện.

Hãy phá vỡ nó

xuống từng bước.

Đầu tiên, hãy tập trung vào

biểu hiện quan trọng nhất

và tạm thời bỏ qua phần còn lại.

Pi của A_t cho S_t vào

bối cảnh này của LLM,

là xác suất của

mã thông báo tiếp theo A_t được đưa ra

lời nhắc hiện tại S_t.

Hành động A_t là

mã thông báo tiếp theo,

và trạng thái S_t là

lời nhắc hoàn thành

lên đến mã thông báo t.

Mẫu số là

xác suất của

mã thông báo tiếp theo với

phiên bản đầu tiên của

LLM đã bị đóng băng.

Tử số là

xác suất của mã thông báo tiếp theo,

thông qua LLM được cập nhật,

mà chúng ta có thể thay đổi

để có phần thưởng tốt hơn.

A-hat_t được gọi là ước tính

điều kiện thuận lợi của một

được lựa chọn hành động.

Ước tính thuật ngữ lợi thế

tốt hơn hay tệ hơn bao nhiêu

hành động hiện tại

được so sánh với

tất cả các hành động có thể

ở trạng thái dữ liệu.

Chúng tôi nhìn vào dự kiến

phần thưởng trong tương lai

sự hoàn thành

theo mã thông báo mới,

và chúng tôi ước tính mức độ thuận lợi

sự hoàn thành này là

so với phần còn lại.

Có một đệ quy

công thức ước lượng

số lượng này dựa trên

hàm giá trị đó

chúng ta đã thảo luận trước đó.

Ở đây, chúng tôi tập trung vào

sự hiểu biết trực quan.

Đây là một đại diện trực quan

về những gì tôi vừa mô tả.

Bạn có dấu nhắc S,

và bạn có sự khác biệt

đường dẫn để hoàn thành nó,

minh họa bằng cách khác nhau

các đường dẫn trên hình.

Thuật ngữ lợi thế cho biết

bạn tốt hơn thế nào hoặc

tệ hơn hiện tại

mã thông báo A_t là sự tôn trọng

cho tất cả các mã thông báo có thể.

Trong hình dung này,

con đường trên cùng đi

cao hơn là hoàn thành tốt hơn,

nhận được phần thưởng cao hơn.

Đường dẫn phía dưới đi xuống

đó là một sự hoàn thành tồi tệ nhất.

Vì vậy tôi có một câu hỏi EK,

tại sao tối đa hóa điều này

thời hạn dẫn đến phần thưởng cao hơn?

Hãy xem xét trường hợp ở đó

lợi thế là tích cực

cho mã thông báo được đề xuất.

Một lợi thế tích cực

có nghĩa là

mã thông báo được đề xuất là

tốt hơn mức trung bình.

Vì thế, ngày càng tăng

xác suất

của mã thông báo hiện tại

có vẻ như là một chiến lược tốt

dẫn đến phần thưởng cao hơn.

Điều này có nghĩa là tối đa hóa

biểu hiện chúng ta có ở đây.

Nếu mã thông báo được đề xuất

tệ hơn mức trung bình,

lợi thế sẽ là tiêu cực.

Một lần nữa, tối đa hóa biểu thức

sẽ hạ cấp mã thông báo,

đâu là chiến lược đúng đắn.

Vì vậy kết luận chung

đó là tối đa hóa

kết quả biểu hiện này

trong một LLM phù hợp hơn.

Tuyệt vời. Vì vậy hãy tối đa hóa

biểu hiện này sau đó.

Tối đa hóa trực tiếp

biểu thức sẽ

dẫn đến vấn đề

bởi vì tính toán của chúng tôi

đáng tin cậy dưới

giả định

đó là lợi thế của chúng tôi

ước tính là hợp lệ.

Ước tính lợi thế

chỉ có hiệu lực khi

chính sách cũ và mới

đang ở gần nhau.

Đây là nơi phần còn lại của

các điều khoản có hiệu lực.

Thế nên hãy lùi lại và nhìn

ở toàn bộ phương trình một lần nữa,

điều xảy ra ở đây là bạn

chọn cái nhỏ hơn

của hai thuật ngữ.

Vấn đề chúng ta vừa thảo luận

và thứ hai này

phiên bản sửa đổi của nó.

Chú ý rằng giây phút này

biểu thức xác định một vùng,

nơi có hai chính sách

đang ở gần nhau.

Những điều khoản bổ sung này

là những lan can,

và chỉ cần xác định một khu vực

ở gần LLM,

ước tính của chúng tôi ở đâu

có những lỗi nhỏ.

Đây được gọi là vùng tin cậy.

Những điều khoản bổ sung này đảm bảo rằng chúng tôi

khó có thể rời đi

khu vực tin cậy.

Tóm lại, tối ưu hóa

chính sách PPO

kết quả khách quan trong

LLM tốt hơn mà không bị vượt quá

tới những khu vực không đáng tin cậy.

Có cái nào không

thành phần bổ sung?

Đúng. Bạn cũng có

sự mất mát entropy.

Trong khi tổn thất chính sách di chuyển

mô hình hướng tới

mục tiêu liên kết,

entropy cho phép mô hình

để duy trì sự sáng tạo.

Nếu bạn giữ entropy ở mức thấp,

bạn có thể sẽ kết thúc

luôn luôn hoàn thành

lời nhắc tương tự

theo cách như được hiển thị ở đây.

Entropy cao hơn hướng dẫn

LLM hướng tới sự sáng tạo hơn.

Điều này tương tự như

cài đặt nhiệt độ

của LLM mà bạn đã

thấy ở Tuần 1.

Sự khác biệt là

rằng nhiệt độ

ảnh hưởng đến sự sáng tạo của người mẫu

tại thời điểm suy luận,

trong khi entropy ảnh hưởng

sự sáng tạo của người mẫu

trong quá trình đào tạo.

Đặt tất cả các điều khoản lại với nhau

dưới dạng tổng có trọng số,

chúng tôi đạt được mục tiêu PPO của mình,

cập nhật mô hình theo hướng

sở thích của con người trong

một cách ổn định.

Đây là tổng thể

Mục tiêu PPO.

Các hệ số C1 và C2

là các siêu tham số.

Cập nhật mục tiêu PPO

mô hình có trọng lượng thông qua

sự lan truyền ngược

qua nhiều bước.

Một khi mô hình

trọng số được cập nhật,

PPO bắt đầu một chu kỳ mới.

Đối với lần lặp tiếp theo,

LLM được thay thế

với LLM được cập nhật,

và một chu kỳ PPO mới bắt đầu.

Sau nhiều lần lặp lại, bạn

đến LLM phù hợp với con người.

Bây giờ, có cái nào khác không

kỹ thuật học tập củng cố

được sử dụng cho RLHF?

Đúng. Ví dụ, Q-learning là

một kỹ thuật thay thế cho

tinh chỉnh LLM thông qua RL,

nhưng PPO hiện là

phương pháp phổ biến nhất.

Theo tôi, PPO là

phổ biến vì nó có

sự cân bằng hợp lý của

độ phức tạp và hiệu suất.

Nói như vậy, việc tinh chỉnh

LLM thông qua

Phản hồi của con người hoặc AI là một

lĩnh vực nghiên cứu tích cực.

Chúng ta có thể mong đợi nhiều

nhiều sự phát triển hơn

ở khu vực này trong thời gian tới.

Ví dụ, ngay trước khi chúng tôi

đang quay video này,

các nhà nghiên cứu ở Stanford

đã xuất bản một bài báo

mô tả một kỹ thuật

gọi là ưu tiên trực tiếp

tối ưu hóa,

cái nào đơn giản hơn

thay thế cho RLHF.

Những phương pháp mới như thế này

vẫn đang trong quá trình phát triển tích cực,

và còn nhiều việc phải làm

để hiểu rõ hơn

lợi ích của họ,

nhưng tôi nghĩ đây là một điều rất

lĩnh vực nghiên cứu thú vị.

Đồng ý. Cảm ơn vậy

nhiều EK để chia sẻ

những hiểu biết sâu sắc về PPO và

học tăng cường.

Cảm ơn, Andrea.

Cảm ơn vì đã có tôi.