# 03 - Đạo hàm, đạo hàm riêng và quy tắc dây chuyền

---

- [Giảng viên] Có 2 nội dung chính

và các nhánh liên kết với nhau để tính toán:

phép tính vi phân và phép tính tích phân.

phép tính vi phân

tập trung vào việc định lượng tốc độ thay đổi,

điều quan trọng để hiểu các biến thay đổi như thế nào

và phản ứng với các biến khác.

Tuy nhiên, phép tính tích phân

đề cập đến việc tích lũy số lượng.

Cả phép tính vi phân và tích phân

là nền tảng trong nhiều thuật toán học máy

và được sử dụng để giải các bài toán tối ưu khác nhau.

Trong học máy,

hai nhánh tính toán này hoạt động thông qua các hàm,

đó là các cấu trúc toán học

xác định mối quan hệ giữa các tập hợp biến.

Chức năng cho phép chúng ta chính thức hóa mối quan hệ

giữa một tập hợp đầu vào hoặc các biến độc lập

và một kết quả còn được gọi là biến phụ thuộc.

Hãy xem xét một hàm rất đơn giản,

chẳng hạn như x mũ 2 cộng 3,

trong đó x đại diện cho đầu vào hoặc biến độc lập.

Nếu x bằng 5 thì

thì đầu ra của hàm sẽ là 28.

Đạo hàm của một hàm

đo lường tốc độ mà tại đó giá trị

hoặc đầu ra của một hàm thay đổi khi đầu vào của nó thay đổi.

Về mặt trực quan, nó biểu thị độ dốc của hàm

tại bất kỳ điểm nào dọc theo đường cong.

Ví dụ, hãy xem xét đường cong của hàm

x bình cộng 3 được hiển thị ở đây.

Đạo hàm của hàm

mô tả độ dốc hoặc độ dốc

của một đường tiếp tuyến giả định

tại bất kỳ điểm nào trên đường cong.

Để tính đạo hàm của biến x,

chúng ta biến số mũ n của biến thành một số nhân

và giảm số mũ đi 1.

Do đó, đạo hàm của x bình cộng 3

đối với x là 2x.

Điều này cho chúng ta biết rằng tỷ lệ

tại đó đầu ra của hàm thay đổi

phụ thuộc vào giá trị của x.

Ví dụ: khi x là 3 thì tốc độ thay đổi là 6.

Tuy nhiên, khi x bằng 1 thì tốc độ thay đổi là 2.

Trong học sâu,

đạo hàm được sử dụng trong thuật toán giảm độ dốc

để xác định các điểm trong hàm chi phí

trong đó độ dốc là 0.

Những điểm này tương ứng với trọng số và độ lệch tối ưu

cho mạng lưới thần kinh.

Trong các hàm có nhiều biến,

đạo hàm riêng biểu thị tỷ lệ

tại đó giá trị của hàm thay đổi

đối với một trong các biến,

giả sử những cái khác được giữ không đổi.

Ví dụ, hãy xem xét hàm,

3x bình phương cộng 2y mũ thứ ba.

Đạo hàm riêng của hàm số đối với x

là 6x,

và đạo hàm riêng của hàm

đối với y là 6y bình phương.

Các mô hình deep learning thường có nhiều tham số

cần điều chỉnh trong quá trình đào tạo.

Đạo hàm riêng đóng vai trò quan trọng

trong việc tìm giá trị tối ưu

của các tham số này cùng một lúc.

Quy tắc dây chuyền được sử dụng để tính đạo hàm

của hàm tổng hợp.

Nó nói rằng nếu bạn có một hàm g

bên trong một hàm f khác,

đạo hàm của hàm tổng hợp, f của g x,

đối với x,

có thể được tìm thấy bằng cách nhân đạo hàm

của hàm ngoài f

đối với hàm bên trong g,

bằng đạo hàm của hàm bên trong g đối với x.

Để minh họa cách thức hoạt động của nó,

đó được coi là hàm tổng hợp,

3x bình cộng 5, tất cả đều có lũy thừa bằng 4.

Để tính đạo hàm của y theo x,

trước tiên chúng ta cần xác định hàm bên trong g của x,

trong trường hợp này là 3x bình cộng 5.

Điều này có nghĩa là hàm ngoài f

đối với hàm bên trong g

là g lũy thừa 4.

Đạo hàm của hàm ngoài

đối với chức năng bên trong là 4g đến thứ ba,

trong khi đạo hàm của hàm bên trong

đối với x là 6x.

Sử dụng quy tắc dây chuyền,

đạo hàm của hàm tổng hợp

là 4g đến lần thứ ba là 6x.

Thay g của x,

bằng 3x bình cộng 5, trở lại phương trình,

chúng ta có 24x, 3x bình phương cộng 5, tất cả đều có lũy thừa bằng 3.

Các mô hình deep learning được đào tạo

thông qua một quá trình được gọi là lan truyền ngược,

liên quan đến việc tính toán đạo hàm của hàm chi phí

đối với từng tham số và mạng.

Quy tắc dây chuyền

được sử dụng để tính toán các đạo hàm này một cách hiệu quả

bằng cách xây dựng mối quan hệ giữa các tham số

như lồng nhau.