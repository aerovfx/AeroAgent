# 05 bài toán với thuật toán dựa trên khoảng cách

---

Đồ thị. Trên trục X,

chúng tôi có giá ở Mỹ

đô la và trên trục Y,

chúng ta có khoảng cách tính bằng km.

Chú ý rằng cả hai trục đều có

phạm vi dữ liệu khác nhau.

Bạn có thể trả lời trực quan được không

điểm gần điểm B hơn?

Đó là điểm A hay điểm C?

Nó khá rõ ràng

trực quan rằng đó là điểm

C. Nhưng nếu

chúng tôi sử dụng khoảng cách Manhattan

để tính toán điều này?

Như bạn có thể thấy, A chỉ là

cách B 0,6 đơn vị.

trong khi C cách nhau 10 đơn vị,

điều đó thực hiện một cách trực quan

không có ý nghĩa gì

Đây chính xác là vấn đề

với các thuật toán dựa trên khoảng cách.

Độ lớn lớn

của một biến

có thể ảnh hưởng quá mức

thước đo khoảng cách,

thực hiện các biến khác

gần như không liên quan,

ngay cả khi nó có thể quan trọng

trong bối cảnh của vấn đề.

Trong trường hợp của chúng tôi, giá thay đổi từ

$0-50 trong khi khoảng cách

thay đổi từ 0-1 km.

Giá có độ lớn cao hơn

và ảnh hưởng rõ ràng

khoảng cách để làm cho nó trông

giống như một thước đo không liên quan.

Câu trích dẫn hợp lý tiếp theo sẽ

sẽ là gì

giải pháp phù hợp?

Vâng, câu trả lời nằm ở

nhân rộng các biến.

Các biến tỷ lệ đề cập đến

quá trình của

thay đổi phạm vi và

phân phối của

giá trị dữ liệu để thực hiện

chúng nhất quán

trên các biến.

Quá trình này đảm bảo rằng

tính năng với

độ lớn khác nhau,

đơn vị hoặc phạm vi đóng góp

ngang bằng với hiệu suất

của mô hình Machine Learning.

Khi bạn chia tỷ lệ các biến,

họ trở nên không có đơn vị,

trong khi không thua

bất kỳ thông tin nào về

sự liên kết của họ với

biến mục tiêu.

Có nhiều phương pháp khác nhau

để mở rộng các biến.

Sự lựa chọn thường phụ thuộc

về bản chất của

dữ liệu và các yêu cầu

của thuật toán cụ thể.

Dưới đây là một số phổ biến

các loại tỉ lệ.

Kiểu chia tỷ lệ đầu tiên

là tỷ lệ Min-Max.

Chia tỷ lệ tối thiểu-tối đa

biến đổi các tính năng bằng cách

chia tỷ lệ từng tính năng thành một

khoảng giữa không và một.

Công thức như sau.

Kiểu chia tỷ lệ thứ hai

là tỷ lệ tiêu chuẩn.

Trung tâm cân tiêu chuẩn

tính năng xung quanh

không với một tiêu chuẩn

độ lệch của một.

Nó giả định rằng dữ liệu tuân theo

một phân phối Gaussian.

Lưu ý rằng cả hai

Bộ chia tỷ lệ Min-Max và

bộ chia tỷ lệ tiêu chuẩn là

nhạy cảm với các ngoại lệ.

Đây là nơi

kiểu chia tỷ lệ thứ ba,

đó là khả năng mở rộng mạnh mẽ

phát huy tác dụng.

Không giống như các công cụ chia tỷ lệ trước đó,

sự định tâm và

thống kê tỷ lệ

của vô hướng mạnh mẽ dựa trên

gạch người và đang

do đó không

bị ảnh hưởng bởi các ngoại lệ.

Sử dụng quy mô mạnh mẽ

trung vị và

phạm vi liên tứ phân vị

để mở rộng quy mô các tính năng.

Sự lựa chọn của quy mô

phương pháp thường phụ thuộc vào

bản chất của dữ liệu và

thuật toán đó

đang được sử dụng.

Tuy nhiên, thường tác động của

kiểu chia tỷ lệ là

không đáng kể lắm.

Các nhà khoa học dữ liệu thường phát triển

sở thích sử dụng một hoặc

phương pháp chia tỷ lệ khác.

Nó cũng quan trọng để

lưu ý rằng trong khi chia tỷ lệ là

một bước được đề xuất cho khoảng cách

dựa trên các mô hình như KNN,

chúng ta đánh mất bối cảnh của

giá trị có tham chiếu

đến các phát biểu vấn đề.

Ví dụ, một

giá trị 5.000 cho

lưu lượng truy cập trang có thể nhận được

chuyển đổi thành 0,5,

điều đó không hay lắm

trực quan để hiểu.

Xin chúc mừng, chúng tôi

đã đạt đến một

tiến gần hơn đến việc tạo ra

mô hình Machine Learning đầu tiên.

Bây giờ chúng ta đã biết tất cả những điều chính

các khái niệm liên quan đến KNN,

chúng ta hãy chuyển sang

bài học tiếp theo và xây dựng

mô hình KNN đầu tiên của chúng tôi.

Hẹn gặp bạn ở đó.