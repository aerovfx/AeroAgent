# 01 mô hình đào tạo ngôn ngữ lớn

---

Trong video trước,

bạn đã được giới thiệu với

AI sáng tạo

vòng đời dự án.

Như bạn đã thấy, có

là một vài bước để

lấy trước khi bạn có thể

đến phần thú vị,

ra mắt của bạn

ứng dụng AI sáng tạo.

Một khi bạn đã xác định được phạm vi

ra trường hợp sử dụng của bạn,

và xác định bạn sẽ cần như thế nào

LLM hoạt động trong

ứng dụng của bạn,

bước tiếp theo của bạn là chọn

một mô hình để làm việc cùng.

Lựa chọn đầu tiên của bạn sẽ là

hoặc làm việc với

một mô hình hiện có,

hoặc đào tạo của riêng bạn từ đầu.

Có cụ thể

hoàn cảnh đào tạo

mô hình của riêng bạn từ đầu

có thể có lợi,

và bạn sẽ tìm hiểu về

những điều sau trong bài học này.

Tuy nhiên, nhìn chung, bạn sẽ

bắt đầu quá trình phát triển

ứng dụng của bạn bằng cách sử dụng một

mô hình nền tảng hiện có.

Nhiều mô hình nguồn mở được

có sẵn cho các thành viên của

cộng đồng AI như bạn

để sử dụng trong ứng dụng của bạn.

Các nhà phát triển của một số

các khuôn khổ chính

để xây dựng

ứng dụng AI sáng tạo

như Ôm Mặt và PyTorch,

có các trung tâm được quản lý nơi bạn

có thể duyệt các mô hình này.

Một tính năng thực sự hữu ích của

những trung tâm này là

bao gồm các thẻ mô hình,

mô tả chi tiết quan trọng

bao gồm cả việc sử dụng tốt nhất

trường hợp cho mỗi mô hình,

nó đã được đào tạo như thế nào,

và những hạn chế đã biết.

Bạn sẽ tìm thấy một số liên kết đến

những trung tâm mô hình này trong bài đọc

vào cuối tuần.

Mô hình chính xác mà

bạn chọn sẽ phụ thuộc

về chi tiết nhiệm vụ

bạn cần phải thực hiện.

Phương sai của máy biến áp

kiến trúc mô hình

phù hợp với khác nhau

nhiệm vụ ngôn ngữ,

phần lớn là do sự khác biệt

về cách các mô hình được đào tạo.

Để giúp bạn hiểu rõ hơn

những khác biệt này và để phát triển

trực giác về mô hình nào

để sử dụng cho một nhiệm vụ cụ thể,

chúng ta hãy xem xét kỹ hơn

ngôn ngữ lớn như thế nào

người mẫu được đào tạo.

Với kiến thức này trong tay,

bạn sẽ tìm thấy nó

dễ dàng điều hướng hơn

các trung tâm mô hình và tìm

mô hình tốt nhất cho trường hợp sử dụng của bạn.

Để bắt đầu, chúng ta hãy lấy

một cái nhìn cấp cao

ở buổi đào tạo ban đầu

quy trình cho LLM.

Giai đoạn này thường được nhắc đến

như là đào tạo trước.

Như bạn đã thấy trong Bài học 1,

Mã hóa LLM

một thống kê sâu sắc

sự thể hiện của ngôn ngữ.

Sự hiểu biết này được phát triển

trong các mô hình

giai đoạn tiền đào tạo

khi người mẫu học

từ số lượng lớn

của dữ liệu văn bản phi cấu trúc.

Đây có thể là gigabyte,

hàng terabyte, và thậm chí

petabyte văn bản.

Dữ liệu này được kéo

từ nhiều nguồn,

bao gồm cả những vết xước trên

Internet và tập hợp văn bản

đã được lắp ráp

đặc biệt để đào tạo

các mô hình ngôn ngữ

Trong cơ chế tự giám sát này

bước học tập,

mô hình nội hóa

các mẫu

và các cấu trúc hiện có

trong ngôn ngữ.

Những mẫu này sau đó

kích hoạt mô hình

để hoàn thành nó

mục tiêu đào tạo,

điều đó phụ thuộc vào

kiến trúc của mô hình,

như bạn sẽ thấy ngay sau đây.

Trong quá trình đào tạo trước,

trọng lượng mô hình nhận được

được cập nhật để giảm thiểu tổn thất

của mục tiêu đào tạo.

Bộ mã hóa tạo ra

một sự nhúng

hoặc biểu diễn vector

cho mỗi mã thông báo.

Đào tạo trước cũng

đòi hỏi một số lượng lớn

tính toán và sử dụng GPU.

Lưu ý, khi bạn

cạo dữ liệu đào tạo

từ các trang web công cộng

như Internet,

bạn thường cần xử lý

dữ liệu để nâng cao chất lượng,

giải quyết sự thiên vị và loại bỏ

nội dung có hại khác.

Kết quả của việc này

quản lý chất lượng dữ liệu,

thường chỉ 1-3% số token

được sử dụng để đào tạo trước.

Bạn nên xem xét

điều này khi bạn

ước tính bao nhiêu dữ liệu bạn

cần phải thu thập nếu bạn

quyết định đào tạo trước

mô hình của riêng bạn.

Đầu tuần này, bạn

thấy rằng có

ba phương sai của

mô hình máy biến áp;

bộ mã hóa-giải mã chỉ có bộ mã hóa

mô hình và chỉ giải mã.

Mỗi người trong số họ đều được đào tạo

theo một mục tiêu khác,

và do đó học cách mang theo

ra các nhiệm vụ khác nhau.

Các mẫu chỉ có bộ mã hóa cũng có

được gọi là mô hình Tự động mã hóa,

và họ được đào tạo trước bằng cách sử dụng

mô hình ngôn ngữ đeo mặt nạ

Ở đây, mã thông báo trong đầu vào

trình tự hoặc mặt nạ ngẫu nhiên,

và đào tạo

mục tiêu là dự đoán

mã thông báo mặt nạ để

xây dựng lại

câu gốc.

Đây còn được gọi là một

mục tiêu khử nhiễu.

Mô hình mã hóa tự động bị đổ

biểu diễn hai chiều

của chuỗi đầu vào,

có nghĩa là mô hình

có sự hiểu biết về

bối cảnh đầy đủ của mã thông báo

và không chỉ của

những từ có trước.

Các mẫu chỉ có bộ mã hóa

lý tưởng là phù hợp với

nhiệm vụ được hưởng lợi từ việc này

bối cảnh hai chiều.

Bạn có thể sử dụng chúng để thực hiện

phân loại câu

nhiệm vụ, chẳng hạn

phân tích tình cảm

hoặc nhiệm vụ cấp mã thông báo

giống như nhận dạng thực thể được đặt tên

hoặc phân loại từ.

Một số ví dụ nổi tiếng về

mô hình mã hóa tự động

là BERT và RoBERTa.

Bây giờ chúng ta hãy nhìn vào

chỉ bộ giải mã hoặc

mô hình tự hồi quy,

được đào tạo trước bằng cách sử dụng

mô hình ngôn ngữ nhân quả.

Ở đây, việc đào tạo

mục tiêu là dự đoán

mã thông báo tiếp theo dựa trên

chuỗi mã thông báo trước đó.

Dự đoán mã thông báo tiếp theo

đôi khi được gọi

mô hình ngôn ngữ đầy đủ

bởi các nhà nghiên cứu.

Dựa trên bộ giải mã

mô hình tự hồi quy,

che dấu đầu vào

trình tự và chỉ có thể

xem mã thông báo đầu vào dẫn đầu

lên đến mã thông báo được đề cập.

Người mẫu không có kiến thức

của phần cuối câu.

Mô hình sau đó lặp lại

qua trình tự đầu vào

từng người một để dự đoán

mã thông báo sau đây.

Ngược lại với

kiến trúc bộ mã hóa,

điều này có nghĩa là

bối cảnh là một chiều.

Bằng cách học cách dự đoán

mã thông báo tiếp theo

từ vô số ví dụ,

mô hình được xây dựng

một thống kê

sự thể hiện của ngôn ngữ.

Các mô hình loại này sử dụng

thành phần giải mã tắt

kiến trúc ban đầu

không có bộ mã hóa.

Các mô hình chỉ có bộ giải mã thường

được sử dụng để tạo văn bản,

mặc dù lớn hơn

mô hình chỉ có bộ giải mã

thể hiện cú sút không mạnh mẽ

khả năng suy luận,

và thường có thể biểu diễn

một loạt các nhiệm vụ tốt.

Những ví dụ nổi tiếng về

tự hồi quy dựa trên bộ giải mã

mô hình là GBT và BLOOM.

Biến thể cuối cùng của

mô hình máy biến áp là

mô hình tuần tự

sử dụng cả bộ mã hóa và

bộ phận giải mã ra khỏi bản gốc

kiến trúc máy biến áp.

Các chi tiết chính xác của

mục tiêu trước đào tạo khác nhau

từ mô hình này sang mô hình khác.

Trình tự nối tiếp phổ biến

mô hình T5,

đào tạo trước bộ mã hóa

sử dụng tham nhũng span,

mặt nạ nào ngẫu nhiên

chuỗi các mã thông báo đầu vào.

Những chuỗi khối lượng đó sau đó

được thay thế bằng một cái duy nhất

Mã thông báo trọng điểm,

được hiển thị ở đây dưới dạng x. lính gác

token là token đặc biệt

thêm vào từ vựng,

nhưng không tương ứng với

bất kỳ từ thực tế nào từ

văn bản đầu vào.

Bộ giải mã sau đó được giao nhiệm vụ

tái tạo mặt nạ

chuỗi mã thông báo

tự động hồi quy.

Đầu ra là mã thông báo Sentinel

theo sau là

token dự đoán.

Bạn có thể sử dụng

mô hình tuần tự cho

dịch thuật, tóm tắt,

và trả lời câu hỏi.

Nhìn chung chúng rất hữu ích trong

trường hợp bạn có một cơ thể

của văn bản như cả hai

đầu vào và đầu ra.

Ngoài T5,

mà bạn sẽ sử dụng trong

phòng thí nghiệm trong khóa học này,

một người nổi tiếng khác

mô hình mã hóa-giải mã

là BART, không phải chim.

Tóm lại, đây là

so sánh nhanh về

mô hình khác nhau

kiến trúc và

các mục tiêu ra khỏi

mục tiêu trước đào tạo.

Mô hình tự động mã hóa

được đào tạo trước

sử dụng mô hình ngôn ngữ đeo mặt nạ.

Chúng tương ứng với

phần mã hóa

của bản gốc

kiến trúc máy biến áp,

và thường được sử dụng với

phân loại câu

hoặc phân loại mã thông báo.

mô hình tự hồi quy

được đào tạo trước

sử dụng mô hình ngôn ngữ nhân quả.

Các mô hình loại này sử dụng

thành phần giải mã của

máy biến áp gốc

kiến trúc,

và thường được sử dụng để

tạo văn bản.

Mô hình tuần tự

sử dụng cả bộ mã hóa và

bộ giải mã bị lệch khỏi bản gốc

kiến trúc máy biến áp.

Các chi tiết chính xác của

mục tiêu trước đào tạo khác nhau

từ mô hình này sang mô hình khác.

Mô hình T5 được đào tạo trước

sử dụng tham nhũng nhịp.

Trình tự theo trình tự

Các mô hình thường được sử dụng để

dịch thuật, tóm tắt,

và trả lời câu hỏi.

Bây giờ bạn đã thấy cách

mô hình khác biệt này

kiến trúc là

được đào tạo và các công việc cụ thể

chúng rất phù hợp với,

bạn có thể chọn

loại mô hình đó

phù hợp nhất với trường hợp sử dụng của bạn.

Một điều bổ sung

để ghi nhớ

đó có phải là những mô hình lớn hơn của

bất kỳ kiến trúc

thường nhiều hơn

có khả năng chở

hoàn thành tốt nhiệm vụ của mình

Các nhà nghiên cứu đã tìm thấy

rằng mô hình càng lớn,

thì càng có nhiều khả năng

làm việc như bạn cần

không có bối cảnh bổ sung

học tập hoặc đào tạo thêm.

Xu hướng này được quan sát thấy của

tăng khả năng mô hình với

kích thước đã thúc đẩy

sự phát triển của

lớn hơn và lớn hơn

mô hình trong những năm gần đây.

Sự tăng trưởng này được thúc đẩy bởi

điểm uốn và nghiên cứu,

chẳng hạn như việc giới thiệu

khả năng mở rộng cao

kiến trúc máy biến áp,

truy cập vào số lượng lớn

dữ liệu phục vụ đào tạo,

và sự phát triển hơn nữa

nguồn tài nguyên tính toán mạnh mẽ.

Sự gia tăng ổn định này trong

kích thước mô hình thực sự dẫn

một số nhà nghiên cứu đưa ra giả thuyết

sự tồn tại của một cái mới

Định luật Moore cho LLM.

Giống như họ, bạn có thể hỏi,

chúng ta có thể giữ lại được không

thêm tham số vào

tăng hiệu suất và

làm cho người mẫu thông minh hơn?

Cái này có thể ở đâu

mô hình dẫn đầu tăng trưởng?

Mặc dù điều này nghe có vẻ tuyệt vời,

hóa ra là đào tạo

những mô hình khổng lồ này là

khó khăn và rất tốn kém,

nhiều đến nỗi nó

có thể là không khả thi

liên tục đào tạo lớn hơn

và các mô hình lớn hơn.

Chúng ta hãy xem xét kỹ hơn

ở một số thử thách

gắn liền với đào tạo lớn

các mẫu trong video tiếp theo.