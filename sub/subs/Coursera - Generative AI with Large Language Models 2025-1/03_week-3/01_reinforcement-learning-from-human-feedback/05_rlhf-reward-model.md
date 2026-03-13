# 05 rlhf-phần thưởng-mô hình

---

Ở giai đoạn này, bạn

có mọi thứ

bạn cần phải rèn luyện

mô hình khen thưởng

Trong khi nó đã mất

một số lượng khá lớn

nỗ lực của con người để

đi đến điểm này,

đến lúc bạn làm xong

đào tạo mô hình khen thưởng,

bạn sẽ không cần phải bao gồm

bất kỳ con người nào nữa trong vòng lặp.

Thay vào đó, mô hình khen thưởng sẽ

diễn ra một cách hiệu quả

tắt nhãn của con người

và tự động chọn

sự hoàn thành ưa thích

trong quá trình HF miệng.

Mô hình khen thưởng này thường

cũng là một mô hình ngôn ngữ.

Ví dụ, một con chim

đó được đào tạo

sử dụng được giám sát

phương pháp học tập trên

sự so sánh theo cặp

dữ liệu mà bạn

được chuẩn bị từ người dán nhãn

đánh giá ngoài lời nhắc.

Đối với một dấu nhắc X nhất định,

mô hình khen thưởng

học cách ủng hộ

sự hoàn thành được con người ưa thích y_ j,

đồng thời giảm thiểu khóa

sigmoid tắt phần thưởng

sự khác biệt, r_j-r_k.

Như bạn đã thấy ở slide trước,

tùy chọn ưa thích của con người là

luôn là người đầu tiên

một cái có nhãn y_j.

Một khi mô hình đã

được đào tạo về

đẳng cấp của con người

cặp hoàn thành nhanh chóng,

bạn có thể sử dụng mô hình phần thưởng

như một bộ phân loại nhị phân

để cung cấp một bộ

của logic trên

sự tích cực và

lớp tiêu cực.

Logic là

đầu ra mô hình không chuẩn hóa

trước khi áp dụng bất kỳ

chức năng kích hoạt.

Giả sử bạn muốn

giải độc LLM của bạn,

và mô hình khen thưởng cần phải

xác định xem việc hoàn thành

chứa lời nói căm thù.

Trong trường hợp này, hai

các lớp học sẽ được ghi chú,

lớp học tích cực mà bạn

cuối cùng muốn tối ưu hóa

ủng hộ và ghét tiêu cực

lớp bạn muốn tránh.

Giá trị lớn nhất của

lớp học tích cực là những gì bạn

sử dụng làm giá trị phần thưởng trong LLHF.

Chỉ để nhắc nhở bạn, nếu bạn nộp đơn

chức năng Softmax

vào nhật ký,

bạn sẽ nhận được xác suất.

Ví dụ ở đây cho thấy

một phần thưởng tốt cho

hoàn thiện không độc hại

và ví dụ thứ hai

cho thấy một phần thưởng xấu

được đưa ra để hoàn thành độc hại.

Tôi biết bài học này có

bao phủ rất nhiều cho đến nay.

Nhưng vào thời điểm này, bạn

có một công cụ mạnh mẽ

trong mô hình khen thưởng này

để sắp xếp LLM của bạn.

Bước tiếp theo là khám phá

phần thưởng như thế nào

mô hình được sử dụng trong

sự gia cố

quá trình học tập

để đào tạo LLM phù hợp với con người của bạn.

Hãy tham gia cùng tôi trong video tiếp theo

để xem nó hoạt động như thế nào.