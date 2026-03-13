# 09 tạo-văn bản-với-máy biến áp

---

Tại thời điểm này, bạn đã thấy một

tổng quan cấp cao về một số

của các thành phần chính

bên trong máy biến áp

kiến trúc.

Nhưng bạn vẫn chưa thấy làm thế nào

quá trình dự đoán tổng thể

hoạt động từ đầu đến cuối.

Hãy đi bộ qua

một ví dụ đơn giản

Trong ví dụ này, bạn sẽ xem xét

một nhiệm vụ dịch thuật hoặc một

nhiệm vụ theo trình tự,

tình cờ là

mục tiêu ban đầu

của máy biến áp

các nhà thiết kế kiến trúc.

Bạn sẽ sử dụng một máy biến áp

mô hình dịch

cụm từ tiếng Pháp

[NƯỚC NGOÀI] sang tiếng Anh.

Đầu tiên, bạn sẽ token hóa

các từ đầu vào bằng cách sử dụng

cùng một tokenizer này

dùng để huấn luyện mạng.

Những mã thông báo này sau đó được thêm vào

đầu vào trên bộ mã hóa

bên của mạng,

đi qua

lớp nhúng,

và sau đó được đưa vào

lớp chú ý nhiều đầu.

Đầu ra của đa đầu

các lớp chú ý được đưa qua

một mạng chuyển tiếp nguồn cấp dữ liệu tới

đầu ra của bộ mã hóa.

Tại thời điểm này, dữ liệu

rời khỏi bộ mã hóa là

một đại diện sâu sắc của

cấu trúc và ý nghĩa

của chuỗi đầu vào.

Sự đại diện này là

chèn vào giữa

bộ giải mã ảnh hưởng

bộ giải mã

cơ chế tự chú ý.

Tiếp theo, bắt đầu mã thông báo chuỗi

được thêm vào đầu vào

của bộ giải mã.

Điều này kích hoạt bộ giải mã

để dự đoán mã thông báo tiếp theo,

mà nó làm dựa trên

bối cảnh

hiểu rằng đó là

được cung cấp từ bộ mã hóa.

Đầu ra của bộ giải mã

lớp tự chú ý

được thông qua

bộ giải mã truyền tiếp

mạng và

qua một trận chung kết

lớp đầu ra softmax.

Tại thời điểm này, chúng tôi

có mã thông báo đầu tiên của chúng tôi.

Bạn sẽ tiếp tục vòng lặp này,

chuyển mã thông báo đầu ra trở lại

đầu vào để kích hoạt

tạo mã thông báo tiếp theo,

cho đến khi mô hình dự đoán

một mã thông báo cuối chuỗi.

Lúc này, trận chung kết

chuỗi token

có thể được giải mã thành từ ngữ,

và bạn có đầu ra của bạn.

Trong trường hợp này, tôi yêu

học máy.

Có nhiều cách trong

mà bạn có thể sử dụng đầu ra

từ lớp softmax đến

dự đoán mã thông báo tiếp theo.

Những điều này có thể ảnh hưởng

bạn thật sáng tạo

văn bản được tạo ra là

Bạn sẽ xem xét những điều này trong

chi tiết hơn vào cuối tuần này.

Hãy tóm tắt những gì

bạn đã thấy cho đến nay.

Máy biến áp hoàn chỉnh

kiến trúc bao gồm

của một bộ mã hóa và

thành phần giải mã.

Bộ mã hóa mã hóa

trình tự đầu vào vào

một đại diện sâu sắc của

cấu trúc và

nghĩa của đầu vào.

Bộ giải mã làm việc từ

trình kích hoạt mã thông báo đầu vào,

sử dụng bộ mã hóa

hiểu biết theo ngữ cảnh

để tạo ra các token mới.

Nó thực hiện điều này trong một vòng lặp

cho đến khi có điều kiện dừng

đã đạt được.

Trong khi ví dụ dịch

bạn đã khám phá ở đây đã sử dụng

cả bộ mã hóa và bộ giải mã

các bộ phận của máy biến áp,

bạn có thể chia chúng

các thành phần ngoài

cho các biến thể của

kiến trúc.

Các mô hình chỉ có bộ mã hóa cũng

làm việc theo trình tự

mô hình,

nhưng không cần thêm

sửa đổi,

trình tự đầu vào và

trình tự đầu ra

hoặc có cùng chiều dài.

Việc sử dụng chúng ít hơn

phổ biến ngày nay,

nhưng bằng cách bổ sung thêm

các lớp cho kiến trúc,

bạn chỉ có thể huấn luyện bộ mã hóa

mô hình để thực hiện

nhiệm vụ phân loại như

như phân tích tình cảm,

BERT là một ví dụ về

một mô hình chỉ dành cho bộ mã hóa.

Mô hình mã hóa-giải mã,

như bạn đã thấy,

thực hiện tốt trên

nhiệm vụ tuần tự

chẳng hạn như dịch thuật,

trong đó trình tự đầu vào và

trình tự đầu ra có thể

có độ dài khác nhau.

Bạn cũng có thể mở rộng quy mô và

đào tạo loại mô hình này

để thực hiện chung

nhiệm vụ tạo văn bản.

Ví dụ về

mô hình mã hóa-giải mã

bao gồm BART trái ngược

tới BERT và T5,

mô hình mà bạn sẽ sử dụng

trong phòng thí nghiệm trong khóa học này.

Cuối cùng, các mô hình chỉ có bộ giải mã

là một số trong số nhiều nhất

được sử dụng phổ biến hiện nay.

Một lần nữa, khi họ đã mở rộng quy mô,

khả năng của họ đã phát triển.

Những mô hình này bây giờ có thể

khái quát hóa cho hầu hết các nhiệm vụ.

Chỉ bộ giải mã phổ biến

mô hình bao gồm

dòng mô hình GPT,

BLOOM, kỷ Jura,

LLaMA, và nhiều hơn nữa.

Bạn sẽ tìm hiểu thêm về

những loại khác nhau này

máy biến áp và cách chúng

sẽ được đào tạo vào cuối tuần này.

Đó là khá nhiều.

Mục tiêu chính của

cái nhìn tổng quan này

mô hình máy biến áp là để cung cấp

bạn có đủ nền tảng để

hiểu

sự khác biệt giữa

các mô hình khác nhau đang được sử dụng

ra thế giới và để có thể

để đọc tài liệu mô hình.

Tôi muốn nhấn mạnh rằng

bạn không cần phải lo lắng

về việc ghi nhớ tất cả

chi tiết bạn đã thấy ở đây,

như bạn có thể quay lại

lời giải thích này như

thường xuyên khi bạn cần.

Hãy nhớ rằng bạn sẽ

tương tác với

mô hình máy biến áp

thông qua ngôn ngữ tự nhiên,

tạo lời nhắc bằng cách sử dụng

từ viết, không phải mã.

Bạn không cần phải

hiểu tất cả

các chi tiết cơ bản

kiến trúc để làm điều này.

Đây được gọi là

kỹ thuật nhanh chóng,

và đó là những gì bạn sẽ khám phá

trong phần tiếp theo của khóa học này.

Hãy chuyển sang

video tiếp theo để tìm hiểu thêm