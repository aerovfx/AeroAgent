# 08 rlhf-phần thưởng-hack

---

Hãy tóm tắt lại những gì

bạn đã thấy cho đến nay.

Arlo HF là một quá trình tinh chỉnh

điều chỉnh LLM phù hợp với

sở thích của con người.

Trong quá trình này, bạn sử dụng

một mô hình khen thưởng

đánh giá và LLM

hoàn thành một dữ liệu kịp thời

chống lại một số con người

số liệu ưu tiên,

như hữu ích hoặc không hữu ích.

Tiếp theo, bạn sử dụng vật gia cố

thuật toán học tập,

trong trường hợp này là PPO,

để cập nhật trọng số

LLM dựa trên phần thưởng là

đã ký kết với

số lần hoàn thành được tạo

bởi hiện tại

phiên bản tắt LLM.

Bạn sẽ thực hiện chu trình này

nhiều lần lặp lại bằng cách sử dụng

nhiều lời nhắc khác nhau

và tắt cập nhật

trọng lượng mô hình

cho đến khi bạn nhận được

mức độ liên kết mong muốn.

Kết quả cuối cùng của bạn là

một LLM phù hợp với con người mà bạn

có thể sử dụng trong ứng dụng của bạn.

Một vấn đề thú vị

điều đó có thể xuất hiện trong

học tăng cường là

được gọi là hack phần thưởng,

nơi đặc vụ học cách gian lận

hệ thống bằng cách ủng hộ

hành động tối đa hóa

phần thưởng nhận được ngay cả khi

những hành động đó không phù hợp

tốt với

mục tiêu ban đầu.

Trong bối cảnh của LLM,

hack phần thưởng có thể biểu hiện

như việc bổ sung

từ hoặc cụm từ để

sự hoàn thành dẫn đến

điểm cao cho

số liệu được căn chỉnh.

Nhưng điều đó làm giảm tổng thể

chất lượng của ngôn ngữ.

Ví dụ, giả sử

bạn đang sử dụng

RHF để giải độc và

hướng dẫn người mẫu.

Bạn đã được đào tạo rồi

mô hình khen thưởng

điều đó có thể thực hiện

phân tích và phân loại tình cảm

hoàn thành mô hình như

độc hại hoặc không độc hại.

Bạn chọn một lời nhắc từ

dữ liệu đào tạo

sản phẩm này là,

và chuyển nó cho người hướng dẫn

một LLM tạo ra

một sự hoàn thành.

Cái này hoàn thiện

rác không nhiều lắm

tốt đẹp và bạn có thể mong đợi nó

để có được mức độ độc hại cao.

Việc hoàn thành được xử lý

bởi sự độc hại của mô hình khen thưởng,

tạo ra điểm số và điều này

được đưa vào thuật toán PPO,

sử dụng nó để cập nhật

trọng số của mô hình.

Khi bạn lặp lại RHF sẽ cập nhật

LLM để tạo ra một

phản ứng ít độc hơn.

Tuy nhiên, khi chính sách cố gắng

để tối ưu hóa phần thưởng,

nó có thể khác biệt quá nhiều so với

mô hình ngôn ngữ ban đầu

Trong ví dụ này, mô hình có

bắt đầu tạo

sự hoàn thành đó

nó đã học sẽ dẫn đến

độc tính rất thấp

ghi điểm bằng cách bao gồm

cụm từ thích nhất

tuyệt vời, đáng kinh ngạc nhất.

Ngôn ngữ này nghe có vẻ

rất cường điệu.

Mô hình cũng có thể bắt đầu

tạo ra những điều vô nghĩa,

sai ngữ pháp

văn bản đó chỉ

xảy ra để tối đa hóa

phần thưởng theo cách tương tự,

đầu ra như thế này là

chắc chắn không hữu ích lắm.

Để ngăn chặn hội đồng quản trị của chúng tôi

hack xảy ra,

bạn có thể sử dụng hướng dẫn ban đầu

LLM làm tài liệu tham khảo hiệu suất.

Hãy gọi nó là

mô hình tham khảo

Trọng số tham chiếu

mô hình bị đóng băng và đang

không được cập nhật trong thời gian

lặp lại của RHF.

Bằng cách này, bạn luôn duy trì được

một tài liệu tham khảo duy nhất

mô hình để so sánh.

Trong quá trình đào tạo, mỗi lời nhắc

được chuyển cho cả hai mô hình,

tạo ra sự hoàn thành

bằng cách tham khảo

LLM và trình độ trung cấp

Mô hình cập nhật LLM.

Tại thời điểm này, bạn có thể

so sánh hai lần hoàn thành

và tính một giá trị

được gọi là Kullback-Leibler

sự khác biệt,

hay gọi tắt là phân kỳ KL.

Phân kỳ KL là một

thước đo thống kê

hai người khác nhau thế nào

phân bố xác suất là

Bạn có thể sử dụng nó để so sánh

việc hoàn thành tắt

hai mô hình và

xác định bao nhiêu

mô hình cập nhật

đã chuyển hướng khỏi tài liệu tham khảo.

Đừng lo lắng quá nhiều về việc

chi tiết về cách thức hoạt động của nó.

Thuật toán phân kỳ KL

được bao gồm trong nhiều

máy tiêu chuẩn

thư viện học tập

và bạn có thể sử dụng

nó mà không biết tất cả

toán học đằng sau nó.

Bạn thực sự sẽ làm

sử dụng phân kỳ KL trong

phòng thí nghiệm của tuần này để bạn có thể

hãy xem cách này hiệu quả với chính bạn.

Tính phân kỳ KL

cho mỗi tạo ra một

mã thông báo trên toàn bộ

từ vựng ngoài LLM.

Điều này có thể dễ dàng

hàng chục hoặc hàng trăm

hàng nghìn token.

Tuy nhiên, sử dụng một

chức năng softmax,

bạn đã giảm số lượng

về xác suất để

ít hơn nhiều so với

kích thước từ vựng đầy đủ.

Hãy nhớ rằng đây vẫn là

tính toán tương đối

quá trình đắt tiền.

Bạn sẽ hầu như luôn luôn

hưởng lợi từ việc sử dụng GPU.

Một khi bạn đã tính toán

sự phân kỳ KL

giữa hai mô hình,

bạn đã thêm thuật ngữ axit vào

việc tính thưởng.

Điều này sẽ phạt RL

mô hình được cập nhật nếu nó cũng thay đổi

xa so với tài liệu tham khảo

LLM và tạo ra sự hoàn thành

đó là hai cái khác nhau

Lưu ý rằng bây giờ bạn

cần sao chép đầy đủ

của LLM để tính toán

sự phân kỳ KL,

LLM tham chiếu cố định,

và PPO LLM được cập nhật bằng miệng.

Nhân tiện, bạn có thể hưởng lợi từ

kết hợp của chúng tôi

mối quan hệ với phồng.

Trong trường hợp này, bạn chỉ

cập nhật trọng số

của bộ chuyển đổi đường dẫn,

không phải là trọng số đầy đủ của LLM.

Điều này có nghĩa là bạn có thể tái sử dụng

LLM cơ bản tương tự cho

cả mô hình tham khảo

và mô hình PPO,

mà bạn cập nhật với một

các tham số đường dẫn đã được huấn luyện.

Điều này làm giảm

dấu chân bộ nhớ

trong quá trình đào tạo bởi

khoảng một nửa.

Tôi biết rằng có một

có rất nhiều thứ để tiếp nhận ở đây,

nhưng đừng lo lắng, RHF

với con đường sẽ đến

được bao phủ trong phòng thí nghiệm.

Nếu bạn sẽ nhận được một

cơ hội để thấy điều này

hành động và thử nó

ra ngoài cho chính mình.

Một khi bạn đã hoàn thành

Căn chỉnh RHF của mô hình,

bạn sẽ muốn đánh giá

hiệu suất của mô hình.

Bạn có thể sử dụng

tập dữ liệu tóm tắt

để định lượng

giảm độc tính,

ví dụ như cuộc đối thoại,

một số tập dữ liệu mà bạn đã thấy

sớm hơn trong khóa học.

Số bạn sẽ sử dụng ở đây

là điểm độc tính,

đây là xác suất của

lớp tiêu cực,

trong trường hợp này,

một phản ứng độc hại hoặc đáng ghét

tính trung bình trong số lần hoàn thành.

Nếu RHF đã giảm thành công

tính độc hại của LLM của bạn,

số điểm này sẽ đi xuống.

Đầu tiên, bạn sẽ tạo một

điểm độc tính cơ bản

cho hướng dẫn ban đầu

LLM bằng cách đánh giá

sự hoàn thành của nó

tập dữ liệu tóm tắt

với một mô hình phần thưởng

có thể đánh giá ngôn ngữ độc hại.

Sau đó bạn sẽ đánh giá

mô hình mới phù hợp với con người

trên cùng một tập dữ liệu

và so sánh điểm số.

Trong ví dụ này,

điểm độc tính thực sự có

giảm sau Arlo HF,

cho thấy ít độc hơn,

mô hình liên kết tốt hơn.

Một lần nữa, bạn sẽ thấy tất cả

cái này trong phòng thí nghiệm của tuần này.