# 02 đường cong-với-hồi quy logistic

---

Chúng ta đã học được rằng hồi quy logistic

được sử dụng cho các vấn đề phân loại,

đó là,

các vấn đề trong đó đầu ra được phân loại.

Dựa trên bài toán về tác dụng cộng hưởng,

chúng ta cần xác định những sản phẩm nào

sẽ bán được hơn một nghìn chiếc.

Trong vấn đề này, biến mục tiêu của chúng tôi

là số lượng bán được lớn hơn 1000.

Điều đó có nghĩa là đầu ra sẽ là 1 nếu

số lượng bán được là hơn 1000,

và 0 nếu nó nhỏ hơn hoặc bằng 1000.

Đầu ra mong muốn này làm cho điều này

vấn đề một vấn đề phân loại.

Hãy hiểu hồi quy logistic như thế nào

hoạt động bằng cách khám phá lý do tại sao tuyến tính

hồi quy không phù hợp

để giải quyết vấn đề này.

Như chúng ta đã học,

hồi quy tuyến tính điển hình

phương trình được biểu diễn như thế này.

Đối với phát biểu vấn đề phân loại

được đưa ra bởi sự hiệp lực y, sự phụ thuộc

biến, đại diện cho đơn vị bán hàng

vượt qua hàng nghìn, có thể là 0 hoặc 1.

Điều này làm cho phương trình này không phù hợp với

một phương trình tuyến tính trực tiếp,

vì những người dự đoán hoặc

các biến độc lập x có thể thay đổi

giữa âm vô cực

đến dương vô cùng.

Vì vậy, chúng ta có sự không phù hợp trong phạm vi

giá trị ở cả hai vế của phương trình của chúng tôi.

Làm thế nào để chúng ta điều chỉnh cho sự không phù hợp này?

Chúng ta có thể biểu diễn y dưới dạng p, xác suất

sản phẩm của chúng tôi thuộc loại 1,

nghĩa là doanh số bán hàng lớn hơn 1000.

Điều này cho phép phía bên trái của

phương trình thay đổi từ 0 đến 1,

trong khi trước đó nó có thể

chỉ là 0 hoặc 1.

Tuy nhiên, chúng ta vẫn bị mắc kẹt bởi

sự chênh lệch trong các phạm vi.

Làm thế nào chúng ta có thể thu hẹp khoảng cách này?

Chúng ta có thể sử dụng khái niệm tỷ lệ cược.

Tỷ lệ chênh lệch là so sánh cơ hội hoặc

xác suất xảy ra một sự kiện

khả năng sự kiện đó không xảy ra.

Nó được đưa ra bởi xác suất

trên 1- xác suất.

Tỷ lệ chênh lệch có phạm vi từ

0 đến dương vô cùng.

Nếu chúng ta sử dụng tỷ lệ chênh lệch,

phương trình của chúng ta trở nên như thế này.

Với điều này, chúng ta có thể thấy rằng chúng ta gần gũi hơn

để phù hợp với phạm vi ở cả hai bên, nhưng

vẫn chưa phù hợp với phạm vi trên

vế phải của phương trình.

Vậy làm thế nào chúng ta có thể điều chỉnh phương trình này

để bao gồm các giá trị âm?

Lấy logarit tự nhiên của

tỷ lệ cược sẽ giải quyết vấn đề này.

Nó thường được gọi là tỷ lệ cược nhật ký hoặc

logit và

chuyển đổi tỷ lệ cược từ 0 thành

phạm vi vô cực dương đến thang đo

dao động từ âm vô cực

đến dương vô cùng.

Sự chuyển đổi này không chỉ phù hợp

phạm vi dự đoán của chúng tôi, nhưng

cũng mở đường cho sigmoid

chức năng hồi quy logistic,

điều này cuối cùng sẽ giúp chúng ta

dự đoán xác suất p.

Bây giờ, bằng cách áp dụng đơn giản

các phép toán,

phương trình này có thể tiếp tục

được viết như thế này hoặc

ở đây z= m1x1 +m2 x2 + MnXn và

vân vân.

Vì trong các bài toán phân loại nhị phân

biến mục tiêu của chúng tôi có thể là 0 hoặc

1, sẽ tốt hơn nếu chúng ta sắp xếp lại

phương trình này để giải cho p.

xác suất là bao nhiêu

số lượng đơn vị được bán lớn hơn

1000 trong trường hợp hiệp đồng.

Vì vậy việc áp dụng một số cách đơn giản

các thao tác đại số,

chúng ta có được phương trình này hoặc thế này.

Cuối cùng, nếu chúng ta sắp xếp lại các số hạng,

chúng ta sẽ đạt được điều này.

Đây là dạng chức năng của

phương trình hồi quy logistic.

Cách biểu diễn này cũng có thể được cho là

như áp dụng hàm sigmoid để

phương trình hồi quy tuyến tính.

Hàm Sigmoid chuyển đổi bất kỳ

giá trị trong phạm vi âm vô cực đến

vô cực dương với các giá trị từ 0 đến

1.

Khi vẽ đồ thị, một Sigmoid điển hình

hàm tạo ra một đường cong hình chữ S.

Với chức năng Sigmoid tại chỗ

dự đoán trở nên trực quan vì nó

có thể đè bẹp ngay cả những giá trị rất cao

vào khoảng từ 0 đến 1,

làm cho chúng có thể giải thích được

như xác suất.

Độ dốc của đường cong được điều chỉnh

bởi các giá trị của hệ số và

giao điểm trong phương trình m1x1 + m2 x2 và

vân vân.

Để hiểu rõ hơn điều này, hãy hình dung

hai đường cong Sigmoid để đưa ra dự đoán cho

đơn vị biến mục tiêu của chúng tôi

bán được hơn 1000.

Chúng tôi sẽ làm điều này bằng cách chỉ sử dụng một tính năng

lưu lượng truy cập trang từ tập dữ liệu tổng hợp.

Ở dạng phương trình,

những đường cong này có thể được biểu diễn như thế này.

Mỗi đường cong này đang sử dụng

một giá trị khác của m1 và c.

Các giá trị khác nhau của m1 và c là

hiện diện trong chú giải của biểu đồ trên.

Chúng tôi cũng đã đính kèm một cuốn sổ tay cho bạn

thông qua đó bạn có thể thay đổi các giá trị của

Mn C để xem đường cong Sigmoid thay đổi như thế nào.

Chúng tôi đã đề cập đến khá nhiều điều quan trọng

Các khái niệm liên quan đến hồi quy logistic

video này.

Trong video tiếp theo chúng ta sẽ học cách

dự đoán được thực hiện bằng cách sử dụng các đường cong này

và làm thế nào để chúng ta tìm được đường cong phù hợp nhất cho

tuyên bố vấn đề của chúng tôi.