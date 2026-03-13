# 01-Trích-nhãn-tự động cho hình ảnh y tế

---

Trong bài học này, bạn sẽ

tìm hiểu về trích xuất nhãn.

Trong Khóa học 1, bạn đã xây dựng

phân loại x-quang ngực của bạn

mô hình từ dữ liệu được dán nhãn.

Trong bài học này, bạn sẽ học

làm thế nào bạn có thể tự động tạo

những nhãn đó bởi

trích xuất đề cập đến

bệnh tật từ các báo cáo X quang.

Bạn đã thấy ở Khóa 1 cách

một thuật toán cho

nhận biết bệnh ở

hình ảnh X-quang ngực có thể được đào tạo

sử dụng nhãn có hoặc không

cho từng bệnh.

Tuy nhiên, đối với bất kỳ hình ảnh nào,

chúng ta chưa nói chuyện

về cách để có được

nhãn tương ứng cho

mỗi hình ảnh cần thiết để

huấn luyện thuật toán này.

Một ý tưởng sẽ là có

một chuyên gia X quang chú thích

mỗi hình ảnh với nó

nhãn tương ứng.

Tuy nhiên, đây sẽ là

tốn nhiều thời gian và chi phí,

yêu cầu bác sĩ X quang

để giải nghĩa từng cái

của hàng ngàn hình ảnh này.

Một giải pháp thay thế cho việc sử dụng

hình ảnh x-quang sẽ là

sử dụng các báo cáo X quang

để trích xuất nhãn.

Khi bác sĩ yêu cầu và

kiểm tra hình ảnh, giống như chụp x-quang,

một bác sĩ X quang viết

một báo cáo bao gồm

cách giải thích của họ về

bài kiểm tra và nêu bật các kết quả.

Sự thay thế cho việc nhìn vào

hình ảnh để có được những nhãn này là

để chú thích bằng cách sử dụng văn bản này

từ báo cáo X quang.

Ở đây, ví dụ,

không có bệnh tật gì

được đề cập là có mặt,

vì vậy chúng ta có thể đánh dấu nhãn bằng

số không cho tất cả các bệnh.

Tất nhiên, đây cũng là

một công việc tốn nhiều thời gian cho

một người chú thích con người để làm,

mặc dù nó có khả năng nhanh hơn

hơn là nhìn qua tất cả

của các hình ảnh một lần nữa.

Một giải pháp tiềm năng là

sử dụng máy để đọc qua

những báo cáo X quang này cho

tự động thực hiện

việc dán nhãn này.

Nếu có nhãn X quang

báo cáo và dán nhãn các cặp,

đó là một học tập có giám sát

vấn đề và chúng ta có thể sử dụng

phương pháp học máy trên

văn bản để xuất nhãn.

Một ví dụ về mô hình có thể

ủng hộ việc ghi nhãn này

sẽ là BERT,

mà bạn đã thấy trong

bài học trước.

Thử thách là khi chúng ta

không có hàng ngàn

báo cáo và dán nhãn cặp

cần thiết cho việc học có giám sát.

Chúng ta sẽ xem làm thế nào chúng ta vẫn có thể

thực hiện nhiệm vụ này

không có dữ liệu được dán nhãn.

Báo cáo X quang bao gồm

nhiều phần, trong đó có

bệnh sử lâm sàng,

mô tả về cách

kỳ thi đã xong,

phần phát hiện,

bao gồm những gì

bác sĩ X quang đã nhìn thấy trong

từng bộ phận của cơ thể.

Cuối cùng, có một ấn tượng hoặc

phần tóm tắt

tóm tắt

quan sát của bác sĩ X quang.

Các quan sát có thể dao động từ

không cụ thể nhất,

thích làm nổi bật hình ảnh

các đặc điểm trên một hình ảnh,

một cách cụ thể nhất,

như chẩn đoán bệnh.