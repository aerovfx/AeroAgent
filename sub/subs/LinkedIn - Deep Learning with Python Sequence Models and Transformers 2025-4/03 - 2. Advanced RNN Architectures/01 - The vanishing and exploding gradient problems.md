# 01 - Các vấn đề về độ dốc biến mất và bùng nổ

---

- [Người hướng dẫn] Như đã thảo luận ở video trước,

kiến trúc của mạng lưới thần kinh tái phát

làm cho chúng đặc biệt hiệu quả

cho các nhiệm vụ liên quan đến dữ liệu trình tự,

chẳng hạn như tạo văn bản, phân tích tình cảm,

và phân tích chuỗi thời gian.

Tuy nhiên, bất chấp lợi thế của họ,

RNN không phải là không có thách thức.

Một trong những vấn đề quan trọng nhất mà họ phải đối mặt

là sự nhạy cảm với những gì đã biết

như các vấn đề độ dốc biến mất và bùng nổ.

Trong mạng lưới thần kinh,

một gradient đại diện cho đạo hàm riêng

của hàm mất mát

đối với các tham số của mô hình.

Nó hướng dẫn phương hướng

và mức độ cập nhật trong quá trình đào tạo

để giảm thiểu tổn thất.

Để được giải thích chi tiết hơn về gradient là gì

và vai trò của chúng trong việc huấn luyện mạng lưới thần kinh như thế nào,

xem Mạng lưới thần kinh học như thế nào

và các video giảm độ dốc

trong Khóa học Deep Learning với Python Foundations.

Trong giai đoạn lùi của quá trình lan truyền ngược,

gradient chảy ngược qua mạng,

bắt đầu từ lớp đầu ra

và lan truyền đến các lớp trước đó trong mạng.

Trong RNN, không chỉ các gradient được truyền ngược

thông qua các lớp của mạng,

chúng cũng được truyền bá qua nhiều bước.

Điều này được gọi là sự lan truyền ngược theo thời gian.

Đó là thứ cho phép RNN

để học hỏi từ tính chất tuần tự của dữ liệu đầu vào của họ.

Thật không may, đó cũng là lý do tại sao mọi thứ trở nên phức tạp.

Truyền gradient ngược

qua cả hai lớp và các bước thời gian

liên quan đến việc nhân số nhiều lần.

Về mặt toán học, độ dốc của mỗi lớp

là tích của gradient ở lớp tiếp theo

và đạo hàm của hàm kích hoạt.

Nếu các số được nhân nhỏ,

độ dốc có thể co lại theo cấp số nhân,

khi chúng được truyền ngược qua các lớp

hoặc bước thời gian.

Ví dụ: hãy xem xét việc nhân nhiều lần một giá trị

0,5 trên 10 bước thời gian.

Chỉ sau 10 bước,

độ dốc đã biến mất một cách hiệu quả.

Đây được gọi là vấn đề độ dốc biến mất.

Khi điều này xảy ra, việc đào tạo chậm lại đáng kể

khi cập nhật trọng lượng trở nên không đáng kể.

Các lớp hoặc bước thời gian trước đó trong mạng

nhận được độ dốc gần bằng 0.

Kết quả là mạng bị lỗi

để tìm hiểu sự phụ thuộc lâu dài

bởi vì sự đóng góp

của các đầu vào trước đó thực sự bị bỏ qua.

Điều này có nghĩa là RNN có thể gặp khó khăn khi kết nối

ý nghĩa của từ ở cuối câu

thông qua ngữ cảnh được cung cấp bởi các từ ở đầu.

Vấn đề bùng nổ độ dốc

ngược lại với gradient biến mất.

Nó xảy ra khi các số được nhân

trong quá trình lan truyền ngược là lớn.

Điều này làm cho độ dốc tăng theo cấp số nhân hoặc bùng nổ.

Khi độ dốc bùng nổ,

trọng lượng của mô hình có thể trở nên quá lớn

được thể hiện chính xác trong bộ nhớ,

dẫn tới lỗi tràn.

Thứ hai, độ dốc lớn dẫn đến cập nhật cực độ

đến quả tạ,

làm cho mô hình dao động dữ dội

và không hội tụ được.

Cả gradient biến mất và bùng nổ

đặc biệt rõ rệt trong RNN

do cấu trúc tái diễn của chúng,

nơi trọng số được chia sẻ qua nhiều bước thời gian.

Trong video tiếp theo, chúng ta sẽ khám phá các kỹ thuật

và các kiến trúc tiên tiến được thiết kế

để giúp giảm thiểu hai thách thức này.