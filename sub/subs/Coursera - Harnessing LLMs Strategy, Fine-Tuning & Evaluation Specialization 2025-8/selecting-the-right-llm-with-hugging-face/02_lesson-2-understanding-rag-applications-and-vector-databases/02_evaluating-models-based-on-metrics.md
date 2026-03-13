# 02 đánh giá-mô hình-dựa trên số liệu

---

[ÂM NHẠC]

Hãy tưởng tượng bạn đang đánh giá hai LLM cho

một nhiệm vụ đạt điểm cao hơn trong

độ chính xác và đòi hỏi đáng kể

sức mạnh tính toán nhiều hơn.

Cái kia thực hiện thấp hơn một chút nhưng

hiệu quả hơn nhiều,

làm thế nào để bạn quyết định sử dụng cái nào?

Video này sẽ trang bị cho bạn

kiến thức để đưa ra sự lựa chọn

hiểu các điểm chuẩn và số liệu chính.

Đến cuối video này, bạn sẽ học được

để hiểu các tiêu chuẩn đánh giá chung

cho LLM và cách giải thích

ma trận hiệu suất trong khi cân bằng

hiệu suất với những hạn chế về nguồn lực.

Hãy bắt đầu bản demo của chúng tôi

bảng xếp hạng mặt ôm.

Hãy cùng tham quan cái ôm

đối mặt với bảng xếp hạng LLM.

Nó là một công cụ mạnh mẽ cho

so sánh các mô hình ngôn ngữ,

Tôi sẽ đưa bạn đến bảng xếp hạng ngay bây giờ.

Vì vậy, điều đầu tiên,

Tôi sẽ tìm kiếm

ôm mặt bảng xếp hạng LLM và

Tôi sẽ nhấp vào tùy chọn đầu tiên.

Như bạn có thể thấy, bảng xếp hạng

cung cấp một cái nhìn tổng quan toàn diện về

LLM khác nhau và hiệu suất của chúng trên

những tiêu chuẩn khác nhau để đánh giá.

Chúng ta hãy xem xét một số thông số.

Vì vậy đây là những LLM được đánh giá

đang đạt điểm rất cao trong

thứ hạng của tất cả các LLM, và

đây là những thông số đánh giá.

Vậy nếu chúng ta nhìn vào điểm trung bình,

nó cho chúng ta một ảnh chụp nhanh

về hiệu suất tổng thể của mô hình

trên tất cả các điểm chuẩn.

Nó rất hữu ích cho việc so sánh cấp cao,

nhưng hãy nhớ, mô hình tốt nhất cho

nhiệm vụ cụ thể của bạn có thể không

luôn có mức trung bình cao nhất.

Cái tiếp theo là IFEval,

điều này đo lường sự ổn định của mô hình

để làm theo hướng dẫn một cách chính xác.

Nó rất quan trọng đối với những nhiệm vụ đòi hỏi

tuân thủ chính xác các lời nhắc.

Tham số đánh giá BBH lớn

điểm chuẩn quy mô kiểm tra các mô hình ngôn ngữ

trên một loạt các nhiệm vụ sử dụng lý luận,

số học, lẽ thường, và nhiều hơn nữa.

Và điểm chuẩn toán học là một tập dữ liệu được sử dụng

để đánh giá khả năng của mô hình

giải quyết các vấn đề toán học.

Điều này bao gồm các nhiệm vụ như số học,

đại số, phép tính và

lĩnh vực khác của toán học.

GPQA là viết tắt của câu hỏi điểm lớn

trả lời, điều này đánh giá mô hình

khả năng trả lời tốt nghiệp phức tạp

câu hỏi cấp độ trên các lĩnh vực khác nhau.

MUSR, hay sự hiểu biết đa nhiệm và

tóm tắt đo lường tốt như thế nào

một mô hình có thể hiểu, tóm tắt,

và lý do về các chủ đề đa dạng và

đặc biệt có liên quan đến

ứng dụng yêu cầu

phân tích văn bản toàn diện.

Cuối cùng, tham số MMLU-PRO là một phần

của ngôn ngữ đa nhiệm khổng lồ

hiểu điểm chuẩn tập trung

về kiến thức chuyên môn.

Điều này có giá trị nếu bạn

đang phát triển các ứng dụng cho

lĩnh vực chuyên môn như luật,

y học, và kỹ thuật.

Chúng tôi lướt qua bảng xếp hạng,

chúng tôi nhận thấy rằng thật khác biệt

mô hình xuất sắc trong các lĩnh vực khác nhau.

Một số có thể hoạt động rất tốt

trong môn toán, nhưng giảng dạy chậm trễ

theo sau trong khi những người khác có thể tỏ ra cân bằng

hiệu suất trên tất cả các số liệu.

Vì vậy chúng ta phải nhớ rằng khi

lựa chọn một mô hình xem xét

của tham số này căn chỉnh chặt chẽ nhất

vào trường hợp sử dụng cụ thể của bạn và

bảng xếp hạng là điểm khởi đầu tuyệt vời.

Nhưng luôn đi sâu hơn vào mô hình

thẻ và tài liệu cho

một sự hiểu biết đầy đủ.

Bảng xếp hạng cũng được cập nhật thường xuyên,

vì vậy đây là một nguồn tài nguyên tuyệt vời để đánh dấu và

kiểm tra định kỳ như bạn

làm việc trên các dự án LLM của bạn.

Chào mừng đến với bài học của chúng tôi về điểm chuẩn chung

để đánh giá các mô hình ngôn ngữ lớn.

Trong phần này chúng ta sẽ thảo luận một số

số liệu chính được sử dụng trên khuôn mặt ôm LLM

bảng xếp hạng để so sánh hiệu suất của mô hình.

Những điểm chuẩn này giúp chúng tôi

hiểu rõ điểm mạnh và

hạn chế của các mô hình khác nhau.

Đầu tiên, điểm trung bình cung cấp một

tổng quan chung về hiệu suất của một mô hình

qua nhiều nhiệm vụ khác nhau, nó vẫn đơn giản

cách hiệu quả để đánh giá năng lực tổng thể.

IFEval là viết tắt của

đánh giá thực tế thông tin.

Nó đo lường khả năng của mô hình để

cung cấp thông tin chính xác và thực tế,

điều này rất quan trọng đối với các ứng dụng

yêu cầu dữ liệu đáng tin cậy như tin tức

tổng hợp và tìm kiếm kiến thức.

BBH, hay băng ghế lớn cứng,

là một chuẩn mực được thiết kế để kiểm tra khả năng của một mô hình

hiệu suất cao hơn trong các nhiệm vụ khó khăn hơn.

Nó đánh giá khả năng của một mô hình

để xử lý các lý luận phức tạp và

sự hiểu biết sâu sắc hơn

nhiệm vụ ngôn ngữ đơn giản.

Toán cấp 5 đo lường mô hình

thành thạo giải các bài toán nâng cao

các vấn đề toán học.

Điểm chuẩn này rất cần thiết để đánh giá

Các mô hình được sử dụng trong giáo dục, nghiên cứu và

các ngành kỹ thuật.

GPQA là viết tắt của

trả lời câu hỏi mục đích chung,

nó đánh giá khả năng của một mô hình để

trả lời một loạt các câu hỏi,

kiểm tra chính xác chung của nó

kiến thức và hiểu biết.

MUSR, hay lý luận đa tầng,

kiểm tra khả năng của mô hình để

xử lý các công việc yêu cầu nhiều

bước đi đến kết luận.

Nó rất quan trọng đối với các ứng dụng như phức tạp

ra quyết định và giải quyết vấn đề.

MMLU-PRO, viết tắt của đa nhiệm lớn

hiểu ngôn ngữ chuyên nghiệp,

là một chuẩn mực toàn diện để đánh giá

hiệu suất của mô hình từ nhiều khía cạnh khác nhau

nhiệm vụ, lĩnh vực chuyên môn.

Nó bao gồm một loạt các chủ đề từ

pháp luật đối với y học, làm cho nó trở nên lý tưởng cho

đánh giá các mô hình chuyên ngành.

Những điểm chuẩn này cung cấp những hiểu biết có giá trị

vào các khía cạnh khác nhau của LLM,

cho phép chúng tôi cung cấp thông tin

quyết định khi lựa chọn mô hình cho

các ứng dụng cụ thể.

Hiểu ma trận này giúp chúng ta căn chỉnh

các chủng mô hình với dự án của chúng tôi

yêu cầu.

Trong video này, bạn đã học được cách

đánh giá LLM bằng cách sử dụng các tiêu chuẩn chung và

giải thích các số liệu hiệu suất một cách hiệu quả.

Bây giờ bạn đã hiểu làm thế nào để

cân đối chính xác nguồn tài nguyên

những ràng buộc trang bị cho bạn để có được thông tin đầy đủ

quyết định khi lựa chọn giữa các mô hình.

Cho dù ưu tiên hiệu quả hay

nhằm mục đích

độ chính xác cao nhất, bạn đã sẵn sàng

điều hướng những sự đánh đổi này một cách tự tin.

Hãy ghi nhớ những hiểu biết sâu sắc này khi bạn

tiếp tục làm việc với LLM, công việc tuyệt vời và

Tôi sẽ gặp bạn trong bài học tiếp theo.

Bây giờ tôi có một câu hỏi cho bạn.

[ÂM NHẠC]