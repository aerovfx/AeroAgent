# 03 kiểm tra đánh giá

---

Chào các bạn học viên. Làm thế nào bạn có thể thiết lập

lập một tập lệnh tự động để

đánh giá và so sánh

mô hình ngôn ngữ

để tạo mã hiệu quả?

Trong video này, chúng ta sẽ làm việc

qua phần còn lại

quá trình thiết lập

thiết lập tập lệnh tự động của chúng tôi

Đánh giá mô hình ngôn ngữ

để tạo mã.

Bạn sẽ học cách thực hiện

LLM về thử thách mã hóa,

nắm bắt và phân tích

ma trận kết quả,

và so sánh hiệu suất

khắp các mô hình.

Cuối cùng, bạn

sẽ được trang bị để

xác định điều tốt nhất

LLM để phát triển

trợ lý mã hóa dựa trên

số liệu cụ thể và

so sánh tự động.

Hãy đi sâu vào cốt lõi

của quá trình đánh giá của chúng tôi,

bắt đầu với

hàm đánh giá_code.

Chức năng này là trung tâm của

nhiệm vụ của chúng tôi là xác định

LLM hoạt động tốt nhất cho

tạo mã tự động.

Nó lấy đầu ra mã đó

từ mỗi mô hình và

đánh giá nó chống lại

bộ của

ma trận xác định trước để

đo sự bình đẳng

và hiệu quả.

Hãy nhìn vào

mã đánh giá

đầu tiên xây dựng hàm

Lúc đầu, chúng tôi

thiết lập lời nhắc cho

đánh giá mã đó

được gửi đến

hàm đánh giá_code.

Phải mất hai tham số.

Một là tuyên bố vấn đề,

và thứ hai là một mã

do mô hình tạo ra.

Bây giờ, nếu chúng ta nhìn lại một chút,

tuyên bố vấn đề được đặt là,

viết mã Python đó

tìm thấy dài nhất

từ trong câu.

Đây là chương trình

thách thức chúng tôi đang đưa ra

mỗi người trong số ba ứng cử viên

những mô hình mà chúng tôi đã chụp,

đó là Salesforce/codegen,

Ôm mặt/SmolLM, và

EleutherAI/gpt-neo-125M.

Mỗi mô hình này

sẽ tạo ra

mã chống lại vấn đề

tuyên bố được đưa ra,

và hàm đánh giá_code

sẽ nhận được câu hỏi,

tuyên bố vấn đề này là gì

và mã được tạo

theo từng mô hình này.

Hàm đánh giá_code này sẽ

thực sự bị xử tử

ba lần.

Bây giờ, trong lời nhắc này

của việc đánh giá,

chúng tôi đang thiết lập bối cảnh bằng cách

nói rằng bạn là

người đánh giá mã,

trong đó đánh giá một

đã cho mã Python

chống lại một tuyên bố vấn đề,

và vấn đề mã hóa

như sau.

Nó sẽ như vậy

gắn liền với một vấn đề,

cái này là gì, viết

một mã Python.

Đánh giá

theo mã Python

về tính chính xác và chất lượng,

và mã Python

sẽ là

được nhúng từ giá trị

rằng chúng ta đang đến đây.

Đây là những thông số

chống lại cái nào

mã này đang đi

để được đánh giá,

sự đúng đắn,

hiệu quả, dễ đọc,

thực tiễn tốt nhất và nhận xét.

Bây giờ chúng ta sẽ làm thế nào

đánh giá mã chống lại

câu hỏi bằng cách làm

một cuộc gọi LLM thông qua điều này

phần của mã này?

Về cơ bản, những gì chúng tôi đang làm

đây là chúng ta

xây dựng lời nhắc bằng cách sử dụng

mô-đun mẫu lời nhắc trò chuyện

từ LangChain và sau đó tạo

chuỗi LangChain

chuyển lời nhắc tới

mô hình và gọi chuỗi

với tuyên bố vấn đề,

cũng như mã.

Điều này về cơ bản thực hiện một cuộc gọi đến

LLM sử dụng lời nhắc này,

cái nào có vấn đề

và mã Python

đã nhúng mã Python đó

được tạo ra bởi mô hình.

Sau đó, phản hồi chứa

vật liền kề với

điểm số chống lại điều này

năm thông số đánh giá

chống lại mã được thông qua.

Sau đó, trong đối tượng phản hồi,

sắp có

một số phần trên và

phía trên đối tượng JSON thực tế,

mà chúng tôi muốn loại bỏ.

Do đó, chúng tôi đang sử dụng

chức năng khác,

cái được gọi là

trích xuất JSON từ

đánh giá vượt qua

văn bản phản hồi.

Điều này về cơ bản,

trích xuất JSON từ

sử dụng hàm đánh giá

biểu thức chính quy chuyển đến

truyền đi phần JSON

từ phản hồi,

trong văn bản đánh giá,

và nó chỉ trả về

dữ liệu JSON,

phần còn lại mọi thứ bị loại bỏ,

phần còn lại tất cả các văn bản và

rác bị loại bỏ.

Nó trả về dữ liệu JSON

vào chương trình gọi

hoặc chức năng gọi điện,

đó là mã đánh giá.

Hàm JSON được truyền đi,

và bây giờ cái này

chức năng trực quan_scores

là để tạo biểu đồ thanh

với điểm đánh giá.

Bây giờ chức năng này

trực quan_scores là

sắp sản xuất

biểu đồ thanh với

sự so sánh tất cả

ba mô hình và

tham số kết quả

ghi điểm với từng người trong số họ.

Bây giờ lái xe chính

mã ở đây,

và ở đây chúng tôi đang lặp lại

thông qua các biến mô hình,

trong đó có ba của chúng tôi

mô hình ứng cử viên, đó là điều này.

Đối với mỗi mô hình,

chúng ta sẽ tạo ra

một đối tượng máy phát điện,

một đối tượng đường ống

máy phát điện có tên

với nhiệm vụ văn bản

thế hệ với tên mẫu,

vì vậy tên mô hình lặp lại,

và với người khác

mã tham số thiết bị=-1,

nói rằng, chúng tôi

không có GPU,

vui lòng sử dụng CPU của

phần cứng đó

bạn đang chạy tiếp.

Với đường ống

đối tượng được tạo bây giờ,

chúng tôi đang kêu gọi

đối tượng đường ống

với tuyên bố vấn đề,

đó là yêu cầu nó

tạo chương trình Python,

và chúng tôi đang in

mã được tạo ra.

Bây giờ, sau khi in

mã được tạo ra,

chúng ta sẽ đánh giá

mã được tạo bằng cách gọi

hàm đánh giá_code

mà chúng tôi đã giải thích,

cái ở đằng này, và cái đó

sẽ thực hiện cuộc gọi OpenAI LLM

để đánh giá các

mã được tạo

chống lại từng thông số này.

Khi đã xong việc đó, bây giờ

chúng tôi sẽ lấy

đối tượng JSON đó

sẽ quay trở lại

và được gửi vào

điểm đánh giá,

và chúng ta sẽ nối nó vào

một danh sách Python được gọi là kết quả.

Cuối cùng chúng ta sẽ đi đến

lấy danh sách kết quả này,

trong đó có chứa

ba đối tượng JSON,

và chúng ta sẽ gọi

trực quan_scores

chức năng sản xuất

biểu đồ thanh so sánh

kết quả cho tất cả

ba mô hình.

Bây giờ với mã này được giải thích,

bây giờ chúng ta sẽ đi

để quay trở lại và

chúng tôi đang đi

chạy chương trình này.

Phải mất một thời gian. Mã

đã thực hiện xong,

vậy chúng ta hãy nhìn vào

những gì nó đã in.

Nó đang đánh giá mô hình

chuỗi mã lực lượng bán hàng,

và nó đã viết

ra chương trình.

Việc đánh giá

đã trở lại như thế này.

Tất nhiên, lực lượng bán hàng

mô hình không được tốt lắm.

Nó có mã một trong số

năm là đúng,

hai trong số năm về hiệu quả,

hai về khả năng đọc, tốt nhất

thực hành hai và bình luận một.

Chúng ta hãy nhìn vào đầu ra của

mô hình từ

Ôm mặt/SmolLM,

và điều này đã tạo ra

chương trình này.

Đây là kết quả của

đánh giá theo mô hình này.

Đúng là năm,

hiệu quả là năm,

khả năng đọc bốn, thực hành tốt nhất

bốn và ý kiến, vv.

Eleuther, có vẻ không

cũng đã làm như vậy,

và đây là kết quả

trên mô hình Eleuther.

Đây là những giá trị đánh giá

đã trở lại từ

OpenAI kêu gọi đánh giá.

Bây giờ chúng tôi đã lấy

các đối tượng JSON,

và chúng tôi thực hiện một hình dung

với Visual_score của chúng tôi

chức năng,

và đây là kết quả

mà chúng tôi đã thấy.

Chắc chắn là Model 2

đang làm rất tốt,

so với

những mô hình khác,

và các mô hình khác thì không

đều ghi điểm tốt.

Mô hình đầu tiên đang ghi điểm

một trong tham số đầu tiên,

hai trong giây

tham số, hai,

hai, và một ở cái cuối cùng,

và mô hình thứ ba là

cũng làm không tốt lắm.

Mô hình thứ hai trong

danh sách ứng cử viên của chúng tôi,

là

ÔmFaceTB/SmolLM-360M,

và đây là mô hình ứng cử viên

mà chúng ta sẽ đi cùng,

nếu chúng ta phải chọn một trong

ba mô hình này cho

tạo trợ lý mã hóa của chúng tôi.

Bằng cách làm theo cấu trúc này

quá trình đánh giá,

chúng tôi không chỉ

dựa vào giả định

hoặc danh tiếng chung

của các mô hình.

Thay vào đó, chúng tôi đang thực hiện

một sự lựa chọn sáng suốt dựa trên

trên những dữ liệu liên quan cụ thể,

đảm bảo rằng

LLM được chọn thực sự đáp ứng

mong đợi của chúng tôi để tạo ra

mã chất lượng cao và dễ đọc.

Bây giờ tôi có một câu hỏi dành cho bạn.