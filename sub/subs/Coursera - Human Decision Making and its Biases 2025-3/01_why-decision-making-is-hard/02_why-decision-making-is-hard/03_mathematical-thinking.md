# 03 tư duy toán học

---

Hãy xem bạn có nhớ không nhé

toán trung học của bạn.

Đây là một câu đố nhỏ để kiểm tra

bạn về kỹ năng toán học của bạn.

Mang sổ ghi chú của bạn ra.

Bây giờ, hãy tưởng tượng có

một xét nghiệm chẩn đoán,

đó là một bài kiểm tra có độ chính xác cao cho

một căn bệnh rất hiếm gặp.

Chỉ có 1% dân số mắc bệnh này.

Nếu bạn mắc bệnh này,

có 99% khả năng là bài kiểm tra

sẽ cho thấy một kết quả tích cực.

Và nếu bạn không mắc bệnh,

có 5% khả năng bài kiểm tra

vẫn sẽ cho kết quả tích cực.

Bây giờ hãy tưởng tượng một người bạn của bạn trải qua

xét nghiệm này và cô ấy cho kết quả dương tính.

Cơ hội mà bạn của bạn là gì

đang mắc phải căn bệnh này?

Chọn một tùy chọn.

Bạn đã hiểu đúng chưa?

Có vẻ như một vấn đề đơn giản,

phải không?

Nếu bạn hiểu sai,

đừng nản lòng.

Bạn đang ở trong một công ty rất tốt.

Thậm chí nhiều bác sĩ còn mắc sai lầm

trong việc giải thích kết quả từ

một bài kiểm tra như thế này

Và tại sao vậy?

Bởi vì hầu hết chúng ta thường dựa vào

trực giác của chúng ta khi thực hiện

quyết định chứ không phải về toán học.

Trực giác của con người, mặc dù thường là đồng minh, nhưng có thể

có độ tin cậy cao trong một số trường hợp.

Bây giờ hãy giải quyết vấn đề này

trước tiên một cách đơn giản.

Điểm dữ liệu đầu tiên trong này

câu hỏi chỉ nói rằng

1% dân số này mắc bệnh.

Hãy tưởng tượng chúng ta có 10.000 người.

Chúng tôi có một dân số mẫu

của 10.000 người.

Dữ liệu của chúng tôi cho thấy chỉ có 100 người

trong mẫu này sẽ có bệnh.

Điểm dữ liệu thứ hai nói rằng 99%

của những người mắc bệnh

sẽ cho thấy một kết quả tích cực

trong xét nghiệm chẩn đoán.

Vậy nếu tất cả 100 người đều làm bài kiểm tra,

99 sẽ cho kết quả dương tính.

Vậy là 99 trên một trăm

những người mắc bệnh

sẽ được chẩn đoán là

tích cực trong thử nghiệm này.

Hãy nhìn vào điểm dữ liệu cuối cùng,

rất quan trọng,

xét nghiệm chẩn đoán sai

bệnh 5% thời gian.

Điều này có nghĩa là trong số còn lại

9900 người không mắc bệnh,

5% trong số họ dù sao cũng sẽ có kết quả dương tính.

Bây giờ, 5% của 9900 là 495.

Điều đó có nghĩa là 495 người sẽ sai

xét nghiệm dương tính trong xét nghiệm chẩn đoán này.

Bây giờ, hãy đặt dữ liệu này vào

cái được gọi là ma trận nhầm lẫn hoặc

một ma trận phân loại sai.

Vì vậy, chúng tôi có 10.000 người.

100 người thực sự mắc bệnh.

9900 không có bệnh.

99 người mắc bệnh sẽ được

được xét nghiệm dương tính trong xét nghiệm chẩn đoán.

495 người không mắc bệnh

vẫn sẽ dương tính trong thử nghiệm.

Một người mắc bệnh sẽ

xét nghiệm âm tính trong xét nghiệm chẩn đoán.

Bây giờ hãy xem xét mọi người

kết quả của họ trở lại tích cực.

Có hai loại người

đã được xét nghiệm dương tính mặc dù họ

không mắc bệnh này.

Và những người đã

đã được xét nghiệm dương tính và

thực sự đã mắc bệnh,

vậy đó là tỷ lệ,

chúng tôi có 99 trường hợp chúng tôi đang tìm kiếm,

trong số 99 cộng với 495 trường hợp.

99 người mắc bệnh

xét nghiệm dương tính.

Trong khi đó 99 + 495 người

xét nghiệm tổng thể dương tính.

Vì vậy, làm tròn thành

xác suất khoảng 17%.

17%?

Điều đó nghe có vẻ không đúng phải không?

Bây giờ, chúng ta đã làm gì sai?

Trên thực tế, chúng tôi đã làm tất cả

những tính toán đúng đắn,

và câu trả lời thực sự là 17%.

Hãy dừng lại với vấn đề này một chút

dài hơn và chúng ta hãy cố gắng tìm

câu trả lời thông qua định lý Bayes

xác suất có điều kiện của một sự kiện.

Điều này có thể khó hơn một chút đối với

một số bạn đã quên

toán trung học và xác suất.

Định lý Bayes cung cấp

một cách để sửa đổi hiện có

niềm tin được đưa ra bằng chứng mới hoặc bổ sung.

Ở đây chúng ta bắt đầu với kiến thức rằng

1% dân số mắc bệnh này.

Và bây giờ chúng tôi đã gặp phải

một số thông tin mới.

Xét nghiệm chẩn đoán

cho thấy một kết quả tích cực.

Vì vậy chúng ta cần cập nhật xác suất

của người mắc bệnh

với thông tin mới này mà cô ấy hoặc

anh ấy có kết quả xét nghiệm dương tính.

Chúng ta có thể sử dụng cùng một tập dữ liệu và

sử dụng phương trình Bayes để tính toán

cơ hội của bạn bạn

mắc phải căn bệnh này.

Bây giờ, hãy hiểu đúng một số thuật ngữ.

PD là xác suất mà

có người mắc bệnh này.

P+ là xác suất

ai đó sẽ xét nghiệm dương tính với

bệnh bằng cách sử dụng xét nghiệm.

Vậy P + cho D là xác suất

rằng ai đó sẽ

xét nghiệm dương tính với cô ấy hoặc

anh ấy mắc bệnh này.

Những gì chúng tôi được yêu cầu làm là

để tìm P của D cho trước cộng hoặc

xác suất để ai đó mắc bệnh

vì cô ấy đã có kết quả xét nghiệm dương tính.

Bây giờ, để tìm P của D đã cho

kết quả xét nghiệm chẩn đoán dương tính,

chúng tôi sử dụng công thức cơ bản.

PD đã cho + là P + đã cho D

nhân với PD chia cho P +.

Bây giờ, P + cho D được cho chúng ta là 0,99,

đó là nếu bạn mắc bệnh,

kết quả xét nghiệm cho kết quả dương tính với xác suất 99%.

PD là 0,01 vì 1% dân số

thực sự có bệnh.

Vậy tử số của cái này

biểu thức là 0,01*0,99 hoặc 0,0099.

Bây giờ, tất cả những gì bạn phải làm là

tính mẫu số,

đó là P +, xác suất đầy đủ

của xét nghiệm cho kết quả dương tính.

Để làm điều đó,

bạn có thể chia nó thành hai kịch bản.

Bạn mắc bệnh này hoặc

bạn không mắc bệnh này

Vậy P + là P + cho D* PD +

P + đã cho, Không phải D*P Không phải D.

Vậy nó sẽ là 0,99 thành 0,01

+ 0,05 thành 0,99 hoặc 0,594.

Vậy chia tử số cho

mẫu số, ta được 0,0099 chia

với 0,0594, chúng ta có 0,166,

làm tròn thành 17%.

Đó là một số phép toán thú vị dành cho

bạn ơi, toán 101.

Và cuối cùng, hầu hết mọi người đều đánh giá thấp

giá trị của xác suất và

toán học trong học máy.

Bạn có biết phổ biến nhất

trả lời câu hỏi này?

94%, hầu hết mọi người đều nghĩ là 94%.

Tại sao bạn nghĩ mọi người

có xu hướng chọn 94%?

Bởi vì chúng tôi dùng đến

trực giác hơn là toán học.

Bộ não của chúng ta bác bỏ ý tưởng rằng

một bài kiểm tra với độ chính xác 99% có thể cho

chỉ có 17% khả năng mắc bệnh,

đặc biệt là khi bạn có kết quả dương tính.

Vậy câu hỏi là,

chúng ta phải làm gì nếu ai đó có kết quả xét nghiệm dương tính?

Khi một bài kiểm tra như thế này,

làm thế nào chúng ta có thể tăng cường sự đảm bảo rằng

xét nghiệm chẩn đoán này có đáng tin cậy không?

Chúng ta có thể làm một điều chắc chắn.

Chúng ta có thể thực hiện thử nghiệm nhiều lần và

xem thử có được không

tích cực nhiều lần.

Điều này sẽ cho chúng ta ước tính chính xác

về xác suất của bệnh.

Nếu bạn làm bài kiểm tra nhiều lần và

kết quả là tích cực, bạn có thể có

sự đảm bảo hoặc sự tự tin cao hơn

rằng người đó mắc bệnh.

Bây giờ, đây là điều bạn

có thể làm việc lúc rảnh rỗi.

Điều gì sẽ xảy ra nếu bạn của bạn làm bài kiểm tra

lần thứ 2 vẫn dương tính?

Xác suất để điều đó xảy ra là bao nhiêu

bạn của bạn mắc bệnh này?

Còn lần thứ ba thì sao?

Bạn có thể sử dụng định lý Bayes để

tính toán các xác suất này và

cung cấp thông tin về loại quyết định phù hợp.

Độ tin cậy của bài kiểm tra sẽ

tăng đáng kể nếu bạn

người bạn tích cực một giây và

lần thứ ba.

Bạn có thể đọc qua phần bổ sung

tài liệu được chia sẻ sau video này

để hiểu toán một cách chi tiết.

Bây giờ, thật tự nhiên khi bạn hỏi,

điều này ảnh hưởng đến cuộc sống của tôi như thế nào?

Rốt cuộc thì lần cuối cùng là khi nào

toán thời gian đã cứu mạng ai đó?

Tôi rất vui vì bạn đã hỏi.

Hãy để tôi kể cho bạn câu chuyện về Chris Evert.

Chris Evert là một trong

những tay vợt vĩ đại nhất từ trước đến nay.

Gần đây cô ấy đã phải đưa ra một quyết định quan trọng,

và chúng ta hãy xem xét điều đó một chút.

Em gái của Chris Evert,

Jean được chẩn đoán mắc bệnh ung thư buồng trứng.

Thông thường với bệnh ung thư buồng trứng,

chúng thường được phát hiện rất muộn,

và cơ hội sống sót

có xu hướng rất ảm đạm.

Thật không may, Jean đã không vượt qua được.

Các xét nghiệm cho thấy cô ấy mang theo

một đột biến gen hiếm gặp

gen BRCA được truyền lại

từ một trong những cha mẹ của cô ấy.

Gen đột biến này mang

hơn một nửa ung thư buồng trứng

những người sở hữu nó.

Có một số dấu hiệu di truyền cho

phát hiện và

xác định nguy cơ ung thư vú hoặc

ung thư buồng trứng,

được gọi là BRCA 1 và BRCA 2.

Câu hỏi tự nhiên bây giờ là, cái gì là

có khả năng Chris Evert mắc bệnh này không?

Và cô ấy nên làm gì?

Chris đã hoàn thành một số bài kiểm tra,

và hóa ra là thế

cô ấy cũng có BRACA 1

biến thể đánh dấu trong gen của cô ấy.

Trong khi điều này không nhất thiết

nghĩa là cô ấy bị ung thư,

Chris Evert vẫn quyết định

nhận được sự điều trị tích cực.

Cô ấy đã cắt bỏ buồng trứng.

Trên thực tế, có nhiều người đã thách thức cô ấy

quyết định bởi vì cô ấy thực sự không

mắc bệnh này chưa.

Nhưng những gì Chris đã làm ở đây,

cố ý, hoặc có lẽ vô tình,

là một quyết định mang tính xác suất rất tốt.

Bây giờ, chúng ta không đi sâu vào toán học

ở đây, nhưng nếu bạn phân tích xác suất

liên quan đến quyết định,

Tiền sử gia đình Chris mắc bệnh ung thư,

chị gái cô ấy đang thử nghiệm,

tích cực đánh dấu riêng của mình.

Khả năng mắc bệnh ung thư,

hóa ra,

thực sự rất cao, và do đó,

quyết định đã đúng.

Hóa ra là sau

cuộc phẫu thuật đã được thực hiện,

bệnh lý sau cuộc phẫu thuật của cô ấy

phát hiện các tế bào ác tính và một khối u.

Mãi sau này người ta mới phát hiện ra rằng

cô ấy bị ung thư buồng trứng ở giai đoạn một.

Việc cắt bỏ tử cung đã cứu sống cô.

Và toán cơ bản sẽ có

thông báo với cô ấy rằng đây thực sự là

hướng hành động đúng đắn.

Tư duy toán học và

một số lẽ thường có thể đi lâu dài

cách giúp chúng tôi cải thiện

quyết định trong cuộc sống hàng ngày của chúng ta.