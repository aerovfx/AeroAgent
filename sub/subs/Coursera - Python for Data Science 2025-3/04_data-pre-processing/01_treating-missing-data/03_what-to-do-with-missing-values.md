# 03 việc cần làm với các giá trị bị thiếu

---

Trong bài học này, chúng ta sẽ

đang đi sâu vào

các khía cạnh quan trọng

của quá trình tiền xử lý dữ liệu.

Điều này bao gồm việc giải quyết

thiếu dữ liệu,

đó là chìa khóa

thử thách có thể

tác động đáng kể đến dữ liệu của chúng tôi

phân tích và mô hình hóa của chúng tôi.

Chúng ta sẽ khám phá nhiều

chiến lược như

xóa và áp đặt

để xử lý dữ liệu còn thiếu.

Thống kê nhất và

kỹ thuật học máy

không thể xử lý dữ liệu bị thiếu.

Vì vậy điều quan trọng là

chúng ta giải quyết một cách hiệu quả

vấn đề này trước khi chúng ta có thể di chuyển

hơn nữa trong dữ liệu

đường ống khoa học.

Xin chào, xử lý các giá trị bị thiếu.

Đây là những gì chúng ta sẽ trở thành

nói đến trong bài học này.

Xác định nơi chúng tôi

có dữ liệu bị thiếu,

chúng ta đối phó với chúng như thế nào.

Chúng ta có xóa hàng hoặc cột không?

Chúng ta có thay thế chúng không?

Nếu chúng ta thay thế thì sao

kỹ thuật chúng tôi sử dụng?

Chúng ta sẽ đi sâu vào vấn đề đó trong

rất sâu sắc trong bài học này.

Sau đó là việc dọn dẹp dữ liệu,

tìm ra những sai sót, sự không nhất quán,

lỗi chính tả, trùng lặp,

các ngoại lệ, xác nhận xem

một ngoại lệ cụ thể,

ví dụ, nó có phải là một

nhầm lẫn hay là thật.

Những điều như thế. Sau đó

chúng ta có sự biến đổi.

Mã hóa biến phân loại thành

định dạng số để thực hiện

chúng phù hợp với những thứ

như học máy.

Kỹ thuật khác nhau

làm điều đó,

chúng ta sẽ tìm hiểu nó sau.

Binning các biến liên tục nếu

yêu cầu những thứ như thế.

Bình thường hóa hoặc

tiêu chuẩn hóa,

đưa dữ liệu về cùng một quy mô,

chuyển đổi dữ liệu

nếu chúng bị lệch.

Những thứ như chuyển đổi nhật ký,

những thứ như thế.

xử lý

outliers, which we'll

đi sâu vào bài học sắp tới.

Xem xét liệu các ngoại lệ có

điểm dữ liệu chính hãng hoặc là

họ mắc lỗi. Chúng ta có loại bỏ chúng không?

Chúng ta có biến đổi chúng không?

Chúng ta có thay thế chúng không? rất nhiều

về những lựa chọn cần phải thực hiện.

Lựa chọn tính năng,

tìm ra những đặc điểm mà

đóng góp nhiều nhất cho

phân tích hoặc mô hình,

và loại bỏ những cái đó

không thêm nhiều giá trị.

Removing features is valuable,

quan trọng bởi vì nó

làm giảm tính chiều,

nó làm giảm chi phí của

tính toán và

những thứ như thế.

Cuối cùng, kỹ thuật tính năng,

tạo ra các tính năng mới,

sửa đổi hiện có

các tính năng, v.v.

Chúng ta sẽ xem xét

tất cả những điều này,

một số chúng tôi đã xem xét trước đây,

một số chúng ta sẽ xem xét.

Nhưng không cần phải nói,

tất cả những thứ này là

những phần rất quan trọng

về những gì một nhà khoa học dữ liệu làm.

Hãy nói về việc mất tích

giá trị trong bài học này.

Đây là một điều quan trọng

bước tiền xử lý

bởi vì giao dịch

với dữ liệu bị thiếu

là quan trọng bởi vì

nếu bạn không làm điều đó,

bạn có thể trở nên không đáng tin cậy,

kết quả sai lệch, hoặc nhất định

các thuật toán thậm chí sẽ không hoạt động.

Một số cách phổ biến để

xử lý dữ liệu bị thiếu,

một là xóa.

Chúng tôi đã làm điều này một cách thô thiển,

rất sớm về việc xóa toàn bộ

hàng hoặc toàn bộ cột.

Nhưng nhược điểm là

về mặt tích cực, điều này

rất dễ làm.

Nhưng điểm trừ

bên cạnh, bạn sẽ mất dữ liệu.

Nếu bạn có nhiều

của những giá trị còn thiếu,

you could potentially

mất rất nhiều dữ liệu.

Chúng tôi không biết trước

nhất thiết điều đó quan trọng đến mức nào

dữ liệu có thể dành cho

phân tích tương lai

vì vậy đây là một điều khó khăn.

Có một số trường hợp khi

đó là điều thông minh nên làm,

nhưng trong nhiều trường hợp,

nó không đơn giản như vậy.

Nhưng nó chắc chắn là một

tùy chọn có sẵn cho chúng tôi.

Chúng ta là ai

sẽ nhìn vào

rất nhiều trong bài học này

là sự quy kết.

Sự quy kết chỉ là từ được sử dụng

để thay thế

các giá trị còn thiếu.

Có rất nhiều kỹ thuật

chúng ta có thể làm theo.

Một cách đơn giản là sử dụng

giá trị trung bình hoặc trung vị

nếu đó là một con số.

Nếu có nhiều ngoại lệ,

chúng ta có thể muốn sử dụng số trung vị

bởi vì ý nghĩa là nhiều

bị ảnh hưởng bất lợi hơn bởi

số ngoại lệ so với số trung vị.

Không có nhiều ngoại lệ,

chúng ta có thể sử dụng giá trị trung bình

Nếu nó là phân loại, chúng tôi

có thể sử dụng chế độ này,

cái nào nhiều nhất

hạng mục thường xuyên.

Nhưng có những lưu ý

cho tất cả những điều này

như bạn sẽ thấy trong bài học này.

Chúng ta có thể thực hiện phép nội suy,

bằng cách vẽ một đường thẳng và

tìm giá trị còn thiếu dựa trên

trên các giá trị lân cận,

đặc biệt là ví dụ,

cho chuỗi thời gian.

Trên một lưu ý liên quan,

chúng ta có thể thực hiện hồi quy.

Chúng ta có thể tạo mô hình hồi quy

và dự đoán các giá trị

that are missing,

hoặc chúng ta có thể sử dụng K-Gần nhất

Hàng xóm và

bạn sẽ tìm hiểu về những điều này

các kỹ thuật trong học máy,

về cơ bản chúng tôi dự đoán

giá trị phải dựa trên những gì

về các tính năng khác trong dữ liệu.

Hoặc chúng ta có thể có sự kết hợp

của nhiều cách tiếp cận khác nhau,

thường có thể là

cách tiếp cận phổ biến nhất.

Kiến thức miền là

rất quan trọng ở đây,

như bạn sẽ thấy trong ví dụ này

mà chúng ta sẽ đi sâu vào

dữ liệu trong quá khứ của chúng tôi bởi vì nó

giúp chúng tôi kiếm được nhiều tiền

đoán tốt hơn.

Nếu chúng ta hiểu được dữ liệu,

chúng tôi hiểu miền,

bối cảnh đó

nó đến từ,

nó sẽ có ý nghĩa hơn rất nhiều

hơn là chỉ đưa ra những phỏng đoán.

Giữ tất cả những điều này trong

tâm trí, và với điều này,

hãy đi sâu vào cách chúng ta giải quyết

giá trị còn thiếu trong

tập dữ liệu thực tế của chúng tôi.