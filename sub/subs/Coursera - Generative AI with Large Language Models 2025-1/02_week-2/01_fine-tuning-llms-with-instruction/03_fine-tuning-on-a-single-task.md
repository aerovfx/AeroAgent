# 03 tinh chỉnh trong một tác vụ

---

Trong khi LLM đã trở thành

nổi tiếng với họ

khả năng thực hiện

nhiều ngôn ngữ khác nhau

nhiệm vụ trong một mô hình duy nhất,

ứng dụng của bạn có thể chỉ cần

để thực hiện một nhiệm vụ duy nhất.

Trong trường hợp này, bạn có thể tinh chỉnh

một mô hình được đào tạo trước để

cải thiện hiệu suất

chỉ trong nhiệm vụ

đó là điều bạn quan tâm.

Ví dụ: tóm tắt bằng cách sử dụng

một tập dữ liệu ví dụ

cho nhiệm vụ đó.

Điều thú vị là tốt

kết quả có thể được

đạt được tương đối

vài ví dụ.

Thường chỉ 500-1.000

ví dụ có thể dẫn đến

hiệu suất tốt trong

tương phản với hàng tỷ

các đoạn văn bản mà mô hình

đã thấy trong quá trình đào tạo trước.

Tuy nhiên, có một

nhược điểm tiềm ẩn

để tinh chỉnh trên một nhiệm vụ duy nhất.

Quá trình có thể dẫn đến

một hiện tượng gọi là

sự lãng quên thảm khốc.

Sự lãng quên thảm khốc

xảy ra bởi vì

toàn bộ quá trình tinh chỉnh

sửa đổi trọng số

của LLM gốc.

Trong khi điều này dẫn đến

hiệu suất tuyệt vời

trong một nhiệm vụ tinh chỉnh duy nhất,

nó có thể làm giảm hiệu suất

về các nhiệm vụ khác.

Ví dụ, trong khi

hộp tinh chỉnh

cải thiện khả năng

của một mô hình để thực hiện

phân tích tình cảm trên một bài đánh giá

và dẫn đến một

hoàn thiện chất lượng,

người mẫu có thể quên

cách thực hiện các công việc khác.

Mô hình này đã biết cách thực hiện

nhận dạng thực thể được đặt tên trước đó

tinh chỉnh chính xác

xác định Charlie

như tên của

con mèo trong câu.

Nhưng sau khi tinh chỉnh,

mô hình không còn có thể

thực hiện nhiệm vụ này,

gây nhầm lẫn cả hai

thực thể mà nó được cho là

xác định và thể hiện hành vi

liên quan đến nhiệm vụ mới.

Bạn có những lựa chọn nào

để tránh thảm họa

quên à?

Trước hết, đó là

quan trọng là quyết định xem

sự lãng quên thảm khốc

thực sự ảnh hưởng đến trường hợp sử dụng của bạn.

Nếu tất cả những gì bạn cần là

hiệu suất đáng tin cậy trên

nhiệm vụ duy nhất

bạn đã tinh chỉnh,

nó có thể không phải là một

vấn đề là mô hình

không thể khái quát hóa cho các nhiệm vụ khác.

Nếu bạn muốn hoặc

cần mô hình để

duy trì đa nhiệm của nó

năng lực tổng quát,

bạn có thể thực hiện tinh chỉnh trên

nhiều nhiệm vụ cùng một lúc.

Tinh chỉnh đa nhiệm tốt có thể

yêu cầu 50-100.000 ví dụ

qua nhiều nhiệm vụ,

và vì thế sẽ cần nhiều hơn

dữ liệu và tính toán để huấn luyện.

Sẽ thảo luận về lựa chọn này

chi tiết hơn trong thời gian ngắn.

Lựa chọn thứ hai của chúng tôi là thực hiện

tinh chỉnh tham số hiệu quả,

hoặc viết tắt là PEFT

tinh chỉnh đầy đủ.

PEFT là một tập hợp các kỹ thuật

bảo toàn trọng lượng

của LLM gốc và

chỉ đào tạo một số ít

bộ điều hợp dành riêng cho nhiệm vụ

lớp và tham số.

PEFT cho thấy độ bền cao hơn đối với

sự lãng quên thảm khốc

vì hầu hết

trọng lượng được đào tạo trước

được giữ nguyên không thay đổi.

PEFT là một điều thú vị

và khu vực hoạt động của

nghiên cứu mà chúng tôi sẽ

trang trải vào cuối tuần này.

Trong lúc chờ đợi, hãy di chuyển

sang video tiếp theo và

nhìn kỹ hơn vào

tinh chỉnh đa nhiệm.