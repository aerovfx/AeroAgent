# 07 điểm chuẩn

---

Như bạn đã thấy ở video trước,

LLM rất phức tạp,

và các thước đo đánh giá đơn giản

như điểm rouge và mờ,

chỉ có thể nói với bạn như vậy

nhiều về khả năng

mô hình của bạn.

Để đo lường và so sánh

LLM một cách toàn diện hơn,

bạn có thể sử dụng

bộ dữ liệu có sẵn,

và các điểm chuẩn liên quan

đã được thành lập bởi

Các nhà nghiên cứu LLM đặc biệt

cho mục đích này.

Lựa chọn quyền

tập dữ liệu đánh giá là rất quan trọng,

để bạn có thể chính xác

đánh giá hiệu suất của LLM,

và hiểu nó

những khả năng thực sự.

Bạn sẽ thấy nó hữu ích

để chọn tập dữ liệu

cô lập cụ thể

kỹ năng làm mẫu,

thích lý luận hoặc

kiến thức thông thường,

và những thứ tập trung

về những rủi ro tiềm ẩn,

chẳng hạn như thông tin sai lệch hoặc

vi phạm bản quyền.

Một vấn đề quan trọng

rằng bạn nên

xem xét liệu mô hình

đã thấy đánh giá của bạn

dữ liệu trong quá trình huấn luyện.

Bạn sẽ nhận được nhiều hơn

ý nghĩa chính xác và hữu ích

về khả năng của mô hình bằng cách

đánh giá hiệu quả hoạt động của nó trên

dữ liệu mà nó chưa từng thấy trước đây.

Các điểm chuẩn, chẳng hạn như

KEO, SuperGLUE,

hoặc Helm, bao quát phạm vi rộng

của các nhiệm vụ và kịch bản.

Họ làm điều này bằng cách

thiết kế hoặc thu thập

bộ dữ liệu kiểm tra cụ thể

các khía cạnh của LLM.

GLUE, hoặc Ngôn ngữ chung

Hiểu đánh giá,

được giới thiệu vào năm 2018.

GLUE là một bộ sưu tập của

nhiệm vụ ngôn ngữ tự nhiên,

chẳng hạn như phân tích tình cảm

và trả lời câu hỏi.

GLUE được tạo ra để

khuyến khích sự phát triển của

các mô hình có thể khái quát hóa

qua nhiều nhiệm vụ,

và bạn có thể sử dụng điểm chuẩn để

đo và so sánh

hiệu suất của mô hình.

Là người kế thừa GLUE,

SuperGLUE cũ là

được giới thiệu vào năm 2019,

để giải quyết những hạn chế

ở người tiền nhiệm của nó.

Nó bao gồm một

chuỗi nhiệm vụ,

một số trong đó không

bao gồm trong KEO,

và một số trong số đó là

phiên bản thử thách hơn

của những nhiệm vụ giống nhau.

SuperGLUE bao gồm các nhiệm vụ như

lý luận nhiều câu,

và đọc hiểu.

Cả keo và

Điểm chuẩn SuperGLUE có

bảng xếp hạng có thể được sử dụng để

so sánh và đối chiếu

các mô hình được đánh giá

Trang kết quả là

một nguồn tài nguyên tuyệt vời khác cho

theo dõi tiến độ của LLM.

Khi các mô hình ngày càng lớn hơn,

hiệu suất của họ chống lại

các điểm chuẩn như SuperGLUE

bắt đầu phù hợp với con người

khả năng thực hiện các nhiệm vụ cụ thể.

Điều đó có nghĩa là các mô hình

có thể thực hiện như

cũng như con người trên

kiểm tra điểm chuẩn,

nhưng về mặt chủ quan chúng ta có thể

thấy rằng họ không

biểu diễn ở cấp độ con người

trong các nhiệm vụ nói chung.

Về cơ bản có

một cuộc chạy đua vũ trang giữa

các đặc tính nổi bật của LLM,

và các điểm chuẩn đó

nhằm mục đích đo lường chúng.

Dưới đây là một vài

điểm chuẩn gần đây

đang đẩy LLM đi xa hơn.

Đa nhiệm lớn

Hiểu ngôn ngữ,

hoặc MMLU, được thiết kế

đặc biệt cho LLM hiện đại.

Để thực hiện tốt

người mẫu phải sở hữu

kiến thức thế giới sâu rộng

và khả năng giải quyết vấn đề.

Các mô hình được thử nghiệm trên

toán tiểu học,

Lịch sử Hoa Kỳ, khoa học máy tính,

pháp luật, và nhiều hơn nữa.

Nói cách khác,

nhiệm vụ mở rộng

vượt xa cơ bản

sự hiểu biết ngôn ngữ.

BIG-băng ghế dự bị hiện nay

bao gồm 204 nhiệm vụ,

khác nhau thông qua ngôn ngữ học,

sự phát triển thời thơ ấu,

toán học, lẽ thường

lý luận, sinh học,

vật lý, thành kiến xã hội, phần mềm

phát triển và nhiều hơn nữa.

Ghế lớn đi vào

ba kích cỡ khác nhau,

và một phần của

lý do cho việc này là để

giữ chi phí có thể đạt được,

khi chạy những cái này

điểm chuẩn lớn có thể

phải chịu chi phí suy luận lớn.

Điểm chuẩn cuối cùng bạn

nên biết về là

Đánh giá toàn diện của

Mô hình ngôn ngữ hoặc HELM.

Khung HELM nhằm mục đích

cải thiện

tính minh bạch của các mô hình,

và đưa ra hướng dẫn

trên những mô hình nào

thực hiện tốt các công việc cụ thể.

HELM mất một

cách tiếp cận đa số,

đo lường bảy số liệu

trên 16 kịch bản cốt lõi,

đảm bảo rằng sự đánh đổi giữa

mô hình và số liệu

được bộc lộ rõ ràng.

Một đặc điểm quan trọng của

HELM là nó đánh giá

về các số liệu vượt quá cơ bản

các biện pháp chính xác,

như độ chính xác của điểm F1.

Điểm chuẩn cũng

bao gồm các số liệu

vì sự công bằng, thiên vị,

và độc tính,

đang ngày càng trở nên

quan trọng để đánh giá như

LLM trở nên có khả năng hơn

tạo ra ngôn ngữ giống con người,

và lần lượt trưng bày

hành vi có khả năng gây hại.

HELM là một chuẩn mực sống

nhằm mục đích liên tục phát triển

với việc bổ sung mới

kịch bản, thước đo và mô hình.

Bạn có thể xem qua

trang kết quả để

duyệt qua LLM đó

đã được đánh giá,

và xem xét điểm số

thích hợp với bạn

nhu cầu của dự án.