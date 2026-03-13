# 08 máy biến áp-kiến trúc

---

Tòa nhà lớn

mô hình ngôn ngữ sử dụng

máy biến áp

kiến trúc ấn tượng

cải thiện hiệu suất của

nhiệm vụ ngôn ngữ tự nhiên kết thúc

thế hệ RNN trước đó,

và dẫn đến một vụ nổ ở

khả năng tái tạo.

Sức mạnh của

kiến trúc máy biến áp

nằm ở khả năng của nó

tìm hiểu sự liên quan và bối cảnh

của tất cả các từ

trong một câu.

Không chỉ như bạn thấy ở đây,

đến từng từ tiếp theo

tới hàng xóm của nó,

nhưng với nhau

từ trong câu.

Để áp dụng trọng số chú ý vào

những mối quan hệ đó để

mô hình tìm hiểu sự liên quan

của mỗi từ để

lời nói của nhau không có vấn đề gì

chúng ở đâu trong đầu vào.

Điều này mang lại cho

thuật toán khả năng

để biết ai có cuốn sách,

ai có thể có cuốn sách,

và nếu nó thậm chí có liên quan

đến bối cảnh rộng hơn

của tài liệu.

Những trọng lượng chú ý này

được học trong thời gian

đào tạo LLM và bạn sẽ

tìm hiểu thêm về điều này

vào cuối tuần này.

Sơ đồ này được gọi là sơ đồ

bản đồ chú ý và

có thể hữu ích để

minh họa sự chú ý

trọng lượng giữa

từng từ và từng từ khác.

Ở đây trong ví dụ cách điệu này,

bạn có thể thấy rằng cuốn sách từ

được kết nối chặt chẽ với hoặc

chú ý đến

từ giáo viên

và từ sinh viên.

Đây được gọi là

sự tự chú ý và

khả năng học hỏi

một sự căng thẳng theo cách này

trên toàn bộ

đầu vào đáng kể

phê duyệt mô hình

khả năng mã hóa ngôn ngữ.

Bây giờ bạn đã thấy một trong

các thuộc tính chính của

kiến trúc máy biến áp,

tự chú ý, hãy che đậy tại

mức độ cao như thế nào

mô hình hoạt động.

Đây là một sơ đồ đơn giản hóa của

kiến trúc máy biến áp

để bạn có thể

tập trung ở mức độ cao vào

nơi các quá trình này

đang diễn ra.

Cấu trúc máy biến áp là

chia thành hai phần riêng biệt,

bộ mã hóa và bộ giải mã.

Các thành phần này hoạt động trong

kết hợp với mỗi

khác và họ chia sẻ một

số điểm tương đồng.

Ngoài ra, lưu ý ở đây,

sơ đồ bạn nhìn thấy là

bắt nguồn từ

sự chú ý ban đầu

là tất cả những gì bạn cần giấy.

Lưu ý cách đầu vào

đến mô hình đang ở

đáy và

đầu ra ở trên cùng,

nếu có thể chúng tôi sẽ cố gắng

vẫn trung thành với điều này

trong suốt khóa học.

Hiện nay, các mô hình học máy đang

chỉ là những máy tính thống kê lớn

và họ làm việc với

những con số chứ không phải từ ngữ.

Vì vậy trước khi chuyển văn bản

vào mô hình để xử lý,

trước tiên bạn phải

mã hóa các từ.

Nói một cách đơn giản, điều này chuyển đổi

các từ thành số,

với mỗi số

đại diện cho một vị trí trong

một từ điển của tất cả

những từ có thể

mà mô hình có thể làm việc được.

Bạn có thể chọn từ nhiều

các phương pháp token hóa.

Ví dụ: ID mã thông báo

ghép hai từ hoàn chỉnh,

hoặc sử dụng ID mã thông báo để

biểu thị các phần của từ.

Như bạn có thể thấy ở đây.

Điều quan trọng là

đó là một khi bạn đã

đã chọn một mã thông báo

để huấn luyện mô hình,

bạn phải sử dụng cùng một mã thông báo

khi bạn tạo văn bản.

Bây giờ đầu vào của bạn là

được biểu diễn dưới dạng số,

bạn có thể chuyển nó cho

lớp nhúng.

Lớp này có thể huấn luyện được

không gian nhúng vector,

một không gian nhiều chiều nơi

mỗi mã thông báo được thể hiện dưới dạng

một vectơ và chiếm

một vị trí độc đáo

trong không gian đó.

Mỗi ID mã thông báo trong từ vựng

được khớp với một

vectơ đa chiều,

và trực giác là thế

những vectơ này học cách mã hóa

ý nghĩa và bối cảnh của

mã thông báo riêng lẻ trong

trình tự đầu vào.

Nhúng không gian vectơ

đã được sử dụng trong

ngôn ngữ tự nhiên

xử lý một thời gian,

thế hệ trước

thuật toán ngôn ngữ

như Word2vec sử dụng khái niệm này.

Đừng lo lắng nếu bạn

không quen với việc này.

Bạn sẽ thấy ví dụ về điều này

trong suốt khóa học,

và có một số liên kết đến

nguồn lực bổ sung trong

bài tập đọc

vào cuối tuần này.

Nhìn lại

trình tự mẫu,

bạn có thể thấy điều đó trong

trường hợp đơn giản này,

mỗi từ đã được

khớp với ID mã thông báo,

và mỗi mã thông báo là

ánh xạ vào một vector.

Trong bản gốc

giấy biến áp,

kích thước vectơ

thực ra là 512,

lớn hơn chúng ta rất nhiều

có thể phù hợp với hình ảnh này.

Để đơn giản, nếu bạn tưởng tượng

kích thước vector chỉ bằng ba,

bạn có thể vẽ các từ thành

không gian ba chiều và

xem các mối quan hệ

giữa những từ đó.

Bây giờ bạn có thể thấy bạn thế nào

có thể liên hệ những từ

nằm gần nhau

trong không gian nhúng,

và làm thế nào bạn có thể

tính khoảng cách

giữa các từ như một góc,

mang lại cho

mô hình hóa khả năng

về mặt toán học

hiểu ngôn ngữ.

Khi bạn thêm

vectơ mã thông báo vào

cơ sở của bộ mã hóa

hoặc bộ giải mã,

bạn cũng thêm

mã hóa vị trí.

Mô hình xử lý từng

các mã thông báo đầu vào song song.

Vì vậy bằng cách thêm

mã hóa vị trí,

bạn bảo quản thông tin

về thứ tự từ và không

mất đi sự liên quan của

vị trí của

từ trong câu.

Một khi bạn đã tổng hợp

mã thông báo đầu vào

và mã hóa vị trí,

bạn chuyển các vectơ kết quả

đến lớp tự chú ý.

Ở đây, mô hình phân tích

các mối quan hệ

giữa các token

trong chuỗi đầu vào của bạn.

Như bạn đã thấy trước đó,

điều này cho phép mô hình

tham gia vào các phần khác nhau của

trình tự đầu vào

để nắm bắt tốt hơn

sự phụ thuộc theo ngữ cảnh

giữa các từ.

Sự tự chú ý

trọng số đã học

trong quá trình đào tạo và

được lưu trữ trong các lớp này

phản ánh tầm quan trọng

của mỗi từ trong

trình tự đầu vào đó cho tất cả

các từ khác trong chuỗi.

Nhưng điều này không

chỉ xảy ra một lần,

máy biến áp

kiến trúc thực sự

có sự chú ý nhiều đầu.

Điều này có nghĩa là nhiều bộ

về trọng lượng tự chú ý hoặc

cái đầu được học trong

song song độc lập

của nhau.

Số lượng chú ý

đầu bao gồm trong

lớp chú ý khác nhau

từ mô hình này sang mô hình khác,

nhưng những con số trong phạm vi

12-100 là phổ biến.

Trực giác ở đây là như vậy

mỗi cái đầu tự chú ý sẽ

học cách khác

khía cạnh của ngôn ngữ.

Ví dụ, một cái đầu có thể nhìn thấy

mối quan hệ giữa

các thực thể con người

trong câu của chúng tôi.

Trong khi một cái đầu khác có thể tập trung

về hoạt động của câu.

Trong khi một người khác

đầu có thể tập trung vào

một số tính chất khác như

như thể các từ có vần điệu.

Điều quan trọng cần lưu ý là

bạn không ra lệnh trước

thời gian những khía cạnh của

ngôn ngữ sự chú ý

người đứng đầu sẽ học.

Trọng lượng của mỗi

đầu ngẫu nhiên

khởi tạo và cung cấp đủ

dữ liệu và thời gian đào tạo,

mỗi người sẽ học khác nhau

các khía cạnh của ngôn ngữ.

Trong khi một số bản đồ chú ý

rất dễ giải thích,

giống như các ví dụ đã thảo luận

ở đây, những người khác có thể không.

Bây giờ tất cả các

trọng lượng chú ý có

đã được áp dụng cho dữ liệu đầu vào của bạn,

đầu ra được xử lý thông qua

được kết nối đầy đủ

mạng chuyển tiếp nguồn cấp dữ liệu.

Đầu ra của lớp này là

một vectơ logit

tỷ lệ thuận với

xác suất

cho điểm từng và

mọi mã thông báo trong

từ điển tokenizer.

Sau đó bạn có thể chuyển các nhật ký này

đến lớp softmax cuối cùng,

nơi chúng được chuẩn hóa thành

điểm xác suất

cho mỗi từ.

Đầu ra này bao gồm

một xác suất

cho mỗi từ

trong từ vựng,

vậy có khả năng sẽ có

hàng ngàn điểm ở đây.

Một mã thông báo duy nhất sẽ có

đạt điểm cao hơn những người còn lại.

Đây là khả năng cao nhất

mã thông báo dự đoán.

Nhưng như bạn sẽ thấy

sau này trong khóa học,

có một số phương pháp

mà bạn có thể sử dụng để thay đổi

sự lựa chọn cuối cùng từ đây

vectơ xác suất.