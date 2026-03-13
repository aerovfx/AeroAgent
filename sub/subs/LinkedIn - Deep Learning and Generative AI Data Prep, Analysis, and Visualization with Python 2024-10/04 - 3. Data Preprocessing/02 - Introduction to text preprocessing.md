# 02 - Giới thiệu về tiền xử lý văn bản

---

- [Giảng viên] Trong chương này,

chúng tôi giới thiệu cho bạn cách xử lý trước văn bản.

Tại sao chúng ta cần

để xử lý trước văn bản khác với xử lý số?

Bởi vì máy tính không hiểu được từ ngữ,

họ chỉ nhìn thấy một chuỗi ký tự.

Mặc dù máy tính không thể hiểu trực tiếp các từ

và các câu, các em có thể hiểu được các con số.

Chẳng hạn, Python không biết

từ "tự nhiên" có nghĩa là gì.

Nó chỉ biết nó dài bảy ký tự,

nhưng mỗi nhân vật riêng lẻ không thực sự có ý nghĩa nhiều

sang Python và bộ sưu tập

của các nhân vật cùng nhau chắc chắn không có nghĩa là

bất cứ điều gì với Python.

Đây là một ví dụ khái niệm đơn giản

hiển thị từ "tự nhiên",

được biểu diễn dưới dạng vectơ hoặc một dãy số.

Trong xử lý ngôn ngữ tự nhiên,

một vectơ đề cập đến một biểu diễn số của một khái niệm,

và bạn có thể thấy ở đây, từ "tự nhiên" được thể hiện

dưới dạng biểu diễn số.

Bằng cách chuyển đổi văn bản thành vectơ,

sau đó chúng ta có thể sử dụng các phép toán

và các thuật toán học máy

để phân tích và thao tác nó.

Token hóa thường là bước đầu tiên

nơi bạn chia văn bản thành các từ riêng lẻ, từ phụ,

hoặc các ký tự được gọi là mã thông báo.

Câu trong tập dữ liệu viễn thông của chúng tôi được chia nhỏ

thành các token riêng biệt.

Mã thông báo biến đổi dữ liệu văn bản phi cấu trúc

thành một dạng có cấu trúc.

Tiếp theo chúng ta viết chữ thường để giảm kích thước

từ vựng của dữ liệu văn bản của chúng tôi.

Từ dừng loại bỏ những từ thường xuyên,

nhưng mang theo ít thông tin hữu ích.

Quá trình loại bỏ các từ thông dụng

không thêm ý nghĩa quan trọng cho văn bản,

chẳng hạn như "và," "the," "là,"

giảm nhiễu trong dữ liệu.

Loại bỏ mật khẩu giúp tập trung vào thông tin chính

bằng cách tập trung vào những từ quan trọng hơn

cho việc phân tích.

Loại bỏ mật khẩu cũng làm giảm kích thước

của dữ liệu văn bản, làm cho việc xử lý hiệu quả hơn.

Lemmatization là quá trình rút gọn các từ

về dạng cơ sở hoặc gốc của chúng,

sử dụng một từ điển, ví dụ,

từ “trải nghiệm” đến “trải nghiệm”.

Lemmatization cải thiện độ chính xác

phân tích kiểm tra bằng cách xử lý các dạng khác nhau của một từ

như một thực thể duy nhất.

Không giống như bắt nguồn, loại bỏ tiền tố

hoặc hậu tố của một từ,

lemmatization bảo tồn ý nghĩa của từ.

Nhận dạng thực thể được đặt tên,

or NER, is as it sounds, it recognizes the names

của các thực thể cụ thể.

NER chuyển đổi văn bản phi cấu trúc thành dữ liệu có cấu trúc

bằng cách gắn thẻ các thực thể cụ thể.

Ví dụ: gắn thẻ cụm từ "Hai tuần qua"

như ngày tháng và San Francisco là một thực thể địa chính trị,

cung cấp cấu trúc cho văn bản.

gắn thẻ POS hoặc gắn thẻ một phần của bài phát biểu,

là một quá trình xử lý ngôn ngữ tự nhiên

nơi mỗi từ trong văn bản được gán

một phần tương ứng của lời nói, một danh từ, động từ,

tính từ chẳng hạn.

Điều này cung cấp ngữ pháp quan trọng

thông tin về văn bản.

Gắn thẻ POS là điều cần thiết,

bởi vì nó cung cấp thông tin cú pháp có giá trị

về một câu.

Thông tin này rất quan trọng để hiểu cấu trúc

và ý nghĩa của văn bản.

Ví dụ, biết một từ có phải là danh từ, động từ hay không,

hoặc tính từ giúp xác định vai trò của nó trong câu.

Vector hóa là quá trình

chuyển đổi văn bản thành biểu diễn số

được gọi là nhúng.

Những phần nhúng này nắm bắt được ý nghĩa và ngữ cảnh của các từ

hoặc toàn bộ câu, cho phép máy móc hiểu được

và xử lý dữ liệu văn bản.

Đây là quy trình làm việc cuối cùng với ví dụ về viễn thông của chúng tôi.

Những kỹ thuật xử lý này giúp chuyển đổi dữ liệu văn bản thô

thành thông tin có cấu trúc có thể được phân tích

và được sử dụng để cải thiện dịch vụ khách hàng, xác định xu hướng,

và giải quyết vấn đề hiệu quả hơn.

Một số thư viện Python NLP phổ biến nhất bao gồm NLTK,

hoặc Bộ công cụ ngôn ngữ tự nhiên,

đó là thư viện nền tảng để xử lý văn bản.

Và spaCy, một thư viện sức mạnh công nghiệp được biết đến

cho hiệu quả và các tính năng sẵn sàng sản xuất

như Nhận dạng thực thể được đặt tên.

Và Gensim, công cụ vượt trội trong việc lập mô hình chủ đề,

sự giống nhau của tài liệu và phân tích văn bản quy mô lớn.

Và TextBlob, một thư viện đơn giản hơn

cho các nhiệm vụ NLP phổ biến như phân tích tình cảm,

gắn thẻ một phần của lời nói và phân loại văn bản.