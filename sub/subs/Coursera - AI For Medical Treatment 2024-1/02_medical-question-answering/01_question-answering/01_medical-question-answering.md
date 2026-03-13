# 01 câu hỏi y tế

---

Trong bài học này, bạn sẽ học

về việc trả lời câu hỏi y tế.

Chúng tôi sẽ đề cập đến một trong những phổ biến nhất

Sự phát triển của xử lý ngôn ngữ tự nhiên

được gọi là BERT và xem nó có thể như thế nào

được áp dụng để trả lời các câu hỏi y học.

Trong bài học này,

bạn sẽ tìm hiểu về trích xuất nhãn.

Trong khóa học thứ nhất, bạn đã thực hiện chụp X-quang ngực của mình

mô hình phân loại từ dữ liệu được dán nhãn.

Trong bài học này, bạn sẽ học cách

bạn có thể tự động tạo các nhãn đó

bằng cách trích xuất đề cập đến

bệnh tật từ các báo cáo X quang.

Vì vậy, giả sử một bệnh nhân hoặc

một bác sĩ muốn biết thêm về

một chẩn đoán y tế hoặc một điều trị.

Một cách họ có thể học là hỏi

một câu hỏi bằng ngôn ngữ tự nhiên và

nhận được câu trả lời cho câu hỏi đó.

Đây là nhiệm vụ trả lời câu hỏi

một nhiệm vụ quan trọng trong tự nhiên

language processing.

Và hệ thống trả lời câu hỏi,

còn được gọi là hệ thống QA, được sử dụng trong tìm kiếm

các công cụ như Google và trong điện thoại

giao diện hội thoại như Siri.

Đối với nhiều câu hỏi được nhập

vào công cụ tìm kiếm, công cụ tìm kiếm

thường có thể tìm thấy lối đi

văn bản chứa câu trả lời.

Thử thách là lần cuối cùng

bước trích xuất câu trả lời,

đó là tìm đoạn ngắn nhất

của đoạn văn trả lời một câu hỏi.

Ở đây cho câu hỏi,

thuốc forxiga dùng để làm gì?

Câu trả lời giảm đi

mức đường huyết.

Do đó, mô hình của chúng tôi sẽ đưa vào

một câu hỏi của người dùng, được gọi là Q, và

một đoạn văn có chứa

câu trả lời cho câu hỏi.

Đây có thể là một đoạn văn có thể

được trả về bởi tìm kiếm của Google.

Và mô hình sẽ đưa ra câu trả lời

được trích từ đoạn văn này,

ở đây được trích xuất từ ​​phần này

của lối đi ở đây.

Gần đây có nhiều tiến bộ về

nhiệm vụ trả lời câu hỏi một cách tự nhiên

xử lý ngôn ngữ, bao gồm cả gần đây

các mô hình được gọi là ELMo, BERT và XLNet.

Chúng ta sẽ xem xét BERT

người mẫu nói riêng.

Mô hình BERT bao gồm một số

các lớp gọi là khối biến áp.

Chúng ta hãy nhìn vào đầu vào cho

mô hình BERT đầu tiên.

Hai đầu vào là câu hỏi và

đoạn văn.

Chúng tôi đã thấy cách chúng tôi có thể nhập hình ảnh

vào một mô hình, nhưng làm cách nào để nhập văn bản?

Chúng ta có thể chia nhỏ câu hỏi và

đoạn văn thành các thẻ hoặc từ.

Chúng tôi tách các đầu vào

từ câu hỏi và

từ đoạn văn sử dụng một từ đặc biệt

mã thông báo được gọi là mã thông báo phân cách.

Trên thực tế, BERT còn tách biệt hơn nữa

từ thành các mảnh từ và

cũng có mã thông báo bắt đầu khi bắt đầu,

nhưng chúng ta có thể làm việc với sự đơn giản hóa

không mất tính tổng quát.

Bây giờ những đầu vào này được chuyển vào mô hình,

nơi họ đi qua một số

khối máy biến áp và cuối cùng là

được chuyển thành một danh sách các vectơ.

Có một vectơ 768 chiều cho

mỗi từ.

Đây được gọi là từ đại diện cho

một từ.

Cách biểu diễn bằng từ thể hiện

từ theo cách nắm bắt được ý nghĩa

mối quan hệ liên quan giữa các từ.

Khoảng cách giữa các từ chụp

họ có liên quan như thế nào hoặc

tần suất chúng được sử dụng trong bối cảnh tương tự.

Vì vậy, những từ không liên quan,

như 15 và lực lượng, là xa,

sao cho vectơ của chúng ở xa

cách xa nhau, trong khi lời nói

tương tự hoặc gần gũi,

sao cho khoảng cách của chúng nhỏ.

Chúng ta có thể cố gắng hình dung những từ này

kích thước bằng cách giảm kích thước

của các vectơ thành hai chiều

sử dụng các phương pháp như t-SNE nên

chúng ta có thể nhìn thấy chúng bằng đồ họa.

Thấy rằng khoảng cách giữa 15 và lực

lớn, trong khi khoảng cách

giữa lực lượng và quân sự là nhỏ.

Khoảng cách giữa 15 và từ

tương tự như 15, như 30, là rất nhỏ.