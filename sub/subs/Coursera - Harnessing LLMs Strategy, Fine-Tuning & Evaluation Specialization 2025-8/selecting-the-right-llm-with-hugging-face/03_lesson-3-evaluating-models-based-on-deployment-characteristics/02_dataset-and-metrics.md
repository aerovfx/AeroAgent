# 02 tập dữ liệu và số liệu

---

Xin chào các bạn học viên. Trong quá khứ,

Tôi gặp khó khăn trong việc đánh giá

mô hình ngôn ngữ một cách thủ công.

Thật là tẻ nhạt và dễ mắc lỗi.

Bây giờ đang thiết lập một

hệ thống tự động để

xử lý công việc này có

đã thay đổi cách tiếp cận của tôi,

làm cho nó hiệu quả

và đáng tin cậy.

Tôi rất vui được chia sẻ

quy trình hợp lý với

bạn để bạn có thể giải quyết việc viết mã

thách thức hiệu quả hơn.

Trong phần đầu tiên ở đây,

chúng tôi sẽ tập trung

về quá trình thiết lập.

Đây là nơi tất cả bắt đầu.

Đặt nền móng

để chúng tôi so sánh bằng

đảm bảo chúng tôi có công cụ phù hợp

và môi trường tại chỗ.

Chúng ta sẽ đi bộ qua

các bước quan trọng

để nhập khẩu

thư viện cần thiết

và cấu hình môi trường của chúng tôi

để xác định các mô hình

chúng tôi sẽ thử nghiệm.

Đến cuối phần này,

bạn sẽ hiểu rõ ràng

về cách chuẩn bị cho

mạnh mẽ và

đánh giá tự động

của các mô hình ngôn ngữ khác nhau,

sẵn sàng giải quyết

thách thức mã hóa phía trước.

Chúng ta hãy đi tiếp. Chào mừng đến với

video của chúng tôi về xây dựng kịch bản

để đánh giá và so sánh

mô hình ngôn ngữ lớn cho

tạo tự động

mã lập trình.

Trong phần đầu tiên này,

chúng tôi đang đi làm

thông qua quá trình thiết lập.

Hãy bắt đầu.

Trong phần đầu tiên của mã của chúng tôi,

chúng tôi sẽ nhập khẩu một

số lượng thư viện khác nhau,

bao gồm mô-đun đường ống

từ thư viện máy biến áp,

điều đó sẽ xảy ra

cho chúng tôi khả năng

để làm việc với

mô hình khác nhau,

ngôn ngữ lớn

những người mẫu mà chúng tôi là

sẽ sử dụng từ Ôm Mặt.

Thư viện Matplotlib là

sẽ được sử dụng

cho trực quan hóa.

Chúng ta sẽ so sánh

kết quả từ

đánh giá của chúng tôi tốt đẹp

hình dung ở cuối,

và Matplotlib là

sẽ được sử dụng cho việc đó.

Chúng tôi cũng đang nhập khẩu

một số

các thư viện khác

sẽ rất cần thiết trong

chương trình này: NumPy,

OpenAI, OS, JSON và RE.

Điều quan trọng tiếp theo là

rằng chúng tôi đang nhập khẩu một vài

của thư viện LangChain.

LangChain là một RAG

khuôn khổ phát triển

hoặc tăng cường truy xuất

khuôn khổ thế hệ.

Chương trình này được thiết lập

như một ứng dụng giẻ rách.

Khung LangChain là

sẽ được sử dụng trong chương trình này

để tận dụng

Các tính năng của OpenAI LLM.

Trong phần thiết lập tiếp theo,

chúng ta sẽ truy cập vào

Khóa API OpenAI vì

đánh giá của chúng tôi là

sắp được biểu diễn

tự động sử dụng OpenAI

mô hình ngôn ngữ lớn 4o,

cái nào mới nhất

mô hình như bây giờ.

Để truy cập LLM đó,

chúng tôi cần khóa API,

mà tôi đã thiết lập

lên tài khoản của tôi.

Nếu bạn chưa và

bạn đang có ý định

hãy thử mã này,

vui lòng truy cập trang web OpenAI

và thiết lập khóa API OpenAI của bạn.

Phần mã này là

đang tải tập tin dotenv,

và tập tin dotenv là một

tập tin biến môi trường.

Khóa API mở này là

đã đăng ký trong dotenv

tập tin trong thư mục hiện tại của tôi,

và hàm Load_dotenv,

đến từ

thư viện Load_dotenv

đang tải dotenv

tập tin trong bộ nhớ,

và chúng tôi đang truy cập

Khóa API OpenAI từ đó.

Bây giờ, một phần quan trọng khác

thiết lập của chúng tôi là thế

sự lựa chọn của chúng tôi về các mô hình.

Đây là ba mô hình

rằng chúng tôi đã chọn rằng chúng tôi

sẽ đánh giá cho

chương trình phi công phụ của chúng tôi,

và chúng ta sẽ đánh giá

ba mô hình này từ

Ôm mặt với một

thử thách lập trình,

và chúng ta sẽ xem chất lượng thế nào

đầu ra của những mô hình này

đang tạo ra.

Bây giờ, nếu bạn để ý kỹ,

những mô hình này có

nhiều thông số thế này

có trong tên.

Mô hình mã hóa Salesforce

có 350 triệu tham số,

mô hình Ôm Mặt có

360 triệu thông số,

và mẫu EleutherAI GPT-Neo

có 125 triệu tham số.

Bây giờ, một điều cần

hiểu là thế

chúng tôi đang thử nghiệm điều này

mô hình trên máy tính xách tay của chúng tôi,

và những mô hình này là

mô hình rất nhỏ,

và do đó các mô hình có ít khả năng hơn.

Trong thời đại ngày nay,

ngôn ngữ lớn hoặc chung chung

mô hình ngôn ngữ lớn

chúng ta thường sử dụng như

OpenAI 4o hoặc Llama 3,

v.v., theo nghĩa đen họ

đi vào miền

hàng trăm tỷ hoặc

thậm chí hàng nghìn tỷ tham số.

Bây giờ, lý do chúng tôi dùng

những mô hình này với kích thước nhỏ như vậy

số lượng tham số và

do đó các mô hình ít có khả năng hơn

là chúng tôi không có

cơ sở hạ tầng.

Chúng tôi không sử dụng một

Cơ sở hạ tầng GPT,

điều này giúp chúng tôi chạy

lớn hơn nhiều và nhiều

những mô hình có khả năng hơn.

Vì mục đích thử nghiệm của chúng tôi,

chúng tôi đang sử dụng ba cái này

nhỏ và do đó ít hơn

những mô hình có khả năng.

Nhưng thử nghiệm của chúng tôi là

sẽ giống nhau

Cách tiếp cận sẽ đi đến

tuy nhiên vẫn giống nhau,

dù sao đi nữa, nó là một vấn đề lớn

mô hình hoặc mô hình nhỏ.

Phần tiếp theo của mã là

mà chúng tôi đang thiết lập hoặc

tạo mô hình

đối tượng sử dụng GPT-4o,

đó là mẫu mới nhất

Hiện tại còn có cái này

thông số nhiệt độ

Tôi đang chuyển sang OpenAI,

đó là Số lần hoàn thành trò chuyện

API của OpenAI,

đó thực sự là

một cái bọc đó là

được cung cấp bởi LangChain

Khung RAG ở đây.

Đây là API mà tôi đang sử dụng

đang sử dụng và tôi đang vượt qua

tên mẫu này.

chúng tôi đang đi

sử dụng mô hình này cho

đánh giá và nhiệt độ

tham số được đặt bằng 0.

Điều đó có nghĩa là các câu trả lời

rằng OpenAI sẽ quay trở lại

chống lại chúng tôi

câu hỏi hoặc chống lại

lời nhắc của chúng tôi sẽ

phải hoàn toàn dựa trên thực tế.

Giá trị càng cao

nhiệt độ,

và cao nhất

giá trị có thể là hai,

mô hình ngôn ngữ lớn

có xu hướng trở nên sáng tạo hơn.

Nhưng đây là một trường hợp sử dụng mà chúng tôi

cần hoàn toàn dựa trên thực tế

câu trả lời cụ thể,

vì vậy không cần thiết

cho bất kỳ sự sáng tạo nào

và do đó nhiệt độ

tham số được đặt bằng 0.

Đó là thiết lập của chúng tôi và

phần đầu tiên của mã.

Với điều này, mọi thứ đã sẵn sàng,

chúng tôi đã sẵn sàng để bắt đầu

kiểm tra và so sánh các

ngôn ngữ lớn

những mô hình mà chúng tôi có

được coi là ứng cử viên

trong chương trình này.

Trong phân đoạn tiếp theo,

chúng ta sẽ đi sâu vào thử nghiệm

quá trình này, vì vậy hãy chú ý theo dõi.

Trong phần đầu tiên này, bạn có

đặt thành công

nền tảng cho

so sánh mô hình của chúng tôi bằng

thiết lập những thứ cần thiết

công cụ và môi trường.

Bạn đã nói chuyện qua

các bước thiết yếu

từ việc nhập thư viện

để cấu hình môi trường của bạn

và xác định các

các mô hình để thử nghiệm.

Với nền tảng vững chắc này,

bây giờ bạn đã chuẩn bị

để tiến về phía trước với

mạnh mẽ và tự động

quá trình đánh giá.

Làm tốt lắm

mọi thứ tại chỗ.

Bạn đã sẵn sàng đón nhận

thách thức mã hóa phía trước.

Bây giờ tôi có một câu hỏi dành cho bạn.