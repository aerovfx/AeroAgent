# 07 giới thiệu về máy học

---

Xin chào và chào mừng trở lại.

Trong video trước, chúng tôi

đã tạo ra một hoạt động tốt

mô hình điểm chuẩn.

Chúng tôi đã sử dụng dữ liệu POS,

và sử dụng giá trị trung bình của đơn vị

bán để dự đoán đơn vị bán.

Sau đó, chúng tôi đã thêm một quy tắc biểu thị

tầm quan trọng của các phân khúc.

Chúng tôi đã tính toán giá trị trung bình

dựa trên phân khúc,

và sử dụng nó làm dự đoán

cho đơn vị đã bán.

Tuy nhiên, trong một khu phức hợp

vấn đề kinh doanh

chẳng hạn như vấn đề tổng hợp,

bạn không thể dự đoán

một biến mục tiêu

chỉ bằng giá trị trung bình hoặc trung vị của nó.

Hãy hiểu

tại sao trong video này.

Trong khi những ý nghĩa và quy tắc này

hướng dẫn mô hình dựa

dự đoán của chúng tôi,

hiệu suất đó

chúng tôi đã đạt được từ

những mô hình này khá bình thường.

Sai số tuyệt đối trung bình của

dự đoán dựa trên quy tắc của chúng tôi

mô hình là khoảng 307,

khá cao

coi đó là ý nghĩa

số lượng đơn vị bán được là khoảng 1.150.

Điều cần thiết là phải hiểu

rằng một vấn đề có nhiều mặt.

Chúng ta phải xem xét

nhiều tính năng khác,

và phức tạp

mối quan hệ với

dự đoán mục tiêu

biến chính xác hơn.

Chẳng hạn, yếu tố

như đánh giá của khách hàng,

lưu lượng truy cập trang hoặc thậm chí

các yếu tố bên ngoài như

mùa lễ hội có thể

ảnh hưởng đến số lượng đơn vị được bán.

Thử thách nằm ở chỗ

ghép những thứ này lại với nhau

điểm dữ liệu để tạo thành một

dự đoán thống nhất.

Nó giống như giải một câu đố bằng

hàng trăm thậm chí hàng nghìn

của những mảnh phức tạp,

mỗi mảnh ở đâu

đại diện cho một tính năng của

dữ liệu và mối quan hệ của nó

đến kết quả mong muốn.

Vì vậy, bằng tay

tìm quy tắc bằng cách phân tích

dữ liệu phức tạp như vậy có thể

áp đảo và

dường như là không thể.

Đó là nơi học máy

đến như một bàn tay giúp đỡ.

Học máy là một

trợ lý thông minh

có thể học hỏi từ dữ liệu,

xác định các mẫu ẩn và

tự động xây dựng

quy luật phức tạp.

Hãy hiểu

học máy ở

so sánh với quy tắc

dự đoán dựa trên

Trong hệ thống dựa trên quy tắc,

con người phân tích dữ liệu để

rút ra quy luật cho

đưa ra dự đoán,

trong học máy

hệ thống dựa trên,

một thuật toán học máy

phân tích dữ liệu,

và rút ra quy luật về

đưa ra dự đoán.

Đối với những vấn đề đơn giản, con người có thể

tìm các quy tắc theo cách thủ công

đưa ra những dự đoán tốt.

Tuy nhiên, đối với những vấn đề phức tạp,

học máy

thuật toán nhiều hơn

hiệu quả trong việc tìm kiếm

quy luật dự đoán.

Nó tương tự như cách

chúng tôi sử dụng trí nhớ của mình

để định hướng những địa điểm quen thuộc,

nhưng dựa vào GPS lâu hơn

và các tuyến đường phức tạp hơn.

Không có tiêu chuẩn

định nghĩa của

học máy mà

mọi người đều đồng ý,

nhưng định nghĩa dưới đây của

Arthur Samuel là

được nhiều người sử dụng.

Học máy là một

lĩnh vực nghiên cứu mang lại

máy tính có khả năng

học mà không bị

được lập trình rõ ràng.

Các thuật toán học máy

tìm hiểu các quy tắc để thực hiện

dự đoán về dữ liệu bằng

học hỏi từ những điều khác nhau

trường hợp dữ liệu,

mà không được đưa ra

hướng dẫn mã hóa cứng.

Có rất nhiều khác nhau

thuật toán học máy,

và mỗi người học những điều này

quy định theo một cách khác,

nhưng hầu hết trong số họ đều rời bỏ

đưa ra các quy tắc bằng cách làm việc trên

một logic cơ bản để giảm

lỗi trong dữ liệu được cung cấp.

Cách mắc lỗi đó

được xác định có thể

thay đổi từ một

thuật toán này sang thuật toán khác.

Dưới đây là những ưu điểm của

một thuật toán học máy

trên một hệ thống dựa trên quy tắc.

Khả năng thích ứng và tốc độ.

Các thuật toán học máy có thể

nhanh chóng học hỏi từ

lượng lớn dữ liệu,

trong khi con người có thể đấu tranh để

phân tích các tập dữ liệu mở rộng.

Khả năng mở rộng. Học máy

thuật toán có thể hiệu quả

xử lý và phân tích các

thông tin khi tập dữ liệu phát triển.

Ngược lại, dựa trên quy tắc

hệ thống có thể trở nên ít hơn

hiệu quả với một

số lượng ngày càng tăng

của các quy tắc và điểm dữ liệu.

Tính nhất quán và khách quan.

Các thuật toán học máy làm

không mệt mỏi khi học

quy tắc dự đoán

hoặc đưa ra dự đoán

dựa trên các quy tắc.

Ngoài ra,

thuật toán không có

thành kiến cá nhân mà

con người có thể có.

Tôi chắc chắn bây giờ bạn có một

sự hiểu biết rõ ràng về

học máy

và lợi thế của nó

trên các hệ thống dựa trên quy tắc.

Trong video sau đây,

hãy hiểu

các ứng dụng khác nhau

của học máy.