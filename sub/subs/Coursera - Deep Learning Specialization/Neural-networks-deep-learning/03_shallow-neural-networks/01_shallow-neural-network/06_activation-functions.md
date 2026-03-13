# 06 chức năng kích hoạt

---

Khi bạn xây dựng mạng lưới thần kinh của mình,

một trong những lựa chọn bạn có thể thực hiện là những gì

chức năng kích hoạt để

sử dụng trong các lớp ẩn

cũng như ở đầu ra

các đơn vị của mạng lưới thần kinh của bạn.

Cho đến nay, chúng tôi mới sử dụng

chức năng kích hoạt sigmoid, nhưng

đôi khi những lựa chọn khác

có thể làm việc tốt hơn nhiều.

Chúng ta hãy xem xét một số tùy chọn.

Trong các bước lan truyền tiến cho

mạng lưới thần kinh,

chúng tôi đã có hai bước này để chúng tôi

sử dụng hàm sigmoid ở đây.

Vì vậy sigmoid đó được gọi là

một chức năng kích hoạt.

Và đây là hàm sigmoid quen thuộc,

a = 1/1 + e đến -z.

Vì vậy, trong trường hợp tổng quát hơn,

chúng ta có thể có một hàm g(z) khác.

Mà tôi sẽ viết ở đây ở đâu

g có thể là một hàm phi tuyến

đó có thể không phải là hàm sigmoid.

Vì vậy, ví dụ, sigmoid

hàm đi giữa 0 và một.

Một chức năng kích hoạt gần như

luôn hoạt động tốt hơn sigmoid

hàm là hàm tiếp tuyến hoặc

hàm tang hyperbol.

Vậy đây là z, đây là a,

đây là a = tan h(z).

Và điều này nằm trong khoảng từ +1 đến -1.

Công thức của hàm tan h là e

z trừ e đến-z trên tổng của chúng.

Và nó thực sự là một sự dịch chuyển về mặt toán học

phiên bản của hàm sigmoid.

Vì vậy, như một hàm sigmoid chỉ

như thế nhưng chuyển như vậy

rằng bây giờ nó vượt qua số 0

điểm 0 trên thang đo.

Vì vậy, nó đi giữa âm một và cộng một.

Và hóa ra là đối với các đơn vị ẩn,

nếu bạn để chức năng

g(z) bằng tan h(z).

Điều này hầu như luôn hoạt động tốt hơn

hàm sigmoid vì với các giá trị

giữa cộng một và trừ một,

ý nghĩa của các kích hoạt xuất hiện

lớp ẩn của bạn gần hơn

để có một ý nghĩa bằng không.

Và cũng giống như đôi khi khi

bạn đào tạo một thuật toán học tập,

bạn có thể tập trung dữ liệu và

dữ liệu của bạn không có ý nghĩa gì khi sử dụng

một tan h thay vì hàm sigmoid.

Loại đó có tác dụng

tập trung dữ liệu của bạn để

rằng giá trị trung bình của dữ liệu của bạn là gần

về 0 thay vì có thể là 0,5.

Và điều này thực sự làm cho việc học tập trở nên

lớp tiếp theo dễ dàng hơn một chút.

Chúng tôi sẽ nói nhiều hơn về điều này trong phần thứ hai

tất nhiên khi chúng ta nói về tối ưu hóa

các thuật toán cũng vậy.

Nhưng có một điểm đáng chú ý là

Tôi hầu như không bao giờ sử dụng

chức năng kích hoạt sigmoid nữa.

Hàm tan h gần như

luôn luôn vượt trội.

Một ngoại lệ là cho đầu ra

lớp vì nếu y bằng 0 hoặc

một, thì nó có ý nghĩa đối với

y mũ là một con số mà bạn muốn

để xuất ra giá trị nằm trong khoảng từ 0 đến

một chứ không phải giữa -1 và 1.

Vì vậy, một ngoại lệ mà tôi sẽ sử dụng

hàm kích hoạt sigmoid là khi

bạn đang sử dụng phân loại nhị phân.

Trong trường hợp đó bạn có thể sử dụng sigmoid

chức năng kích hoạt cho lớp trên.

Vậy g(z2) ở đây bằng sigmoid của z2.

Và những gì bạn thấy trong này

ví dụ là nơi bạn có thể có

một chức năng kích hoạt tan h cho ẩn

lớp và sigmoid cho lớp đầu ra.

Vì vậy, các hàm kích hoạt có thể

khác nhau cho các lớp khác nhau.

Và đôi khi để biểu thị rằng

các chức năng kích hoạt là khác nhau đối với

các lớp khác nhau,

chúng ta có thể sử dụng những dấu ngoặc vuông này

chỉ số trên cũng để chỉ ra rằng

gf dấu ngoặc vuông có thể khác

hơn gf dấu ngoặc vuông hai, phải.

Một lần nữa, dấu ngoặc vuông một

chỉ số trên đề cập đến lớp này và

dấu ngoặc vuông số 2 phía trên

đề cập đến lớp đầu ra.

Hiện nay, một trong những nhược điểm của

cả hàm sigmoid và

hàm tan h là nếu z là

hoặc rất lớn hoặc rất nhỏ,

thì gradient của đạo hàm của

độ dốc của hàm này trở nên rất nhỏ.

Vì vậy, nếu z rất lớn hoặc z rất nhỏ,

độ dốc của hàm số ở hai đầu

gần bằng 0 và vì thế

điều này có thể làm chậm quá trình giảm độ dốc.

Vì vậy, một sự lựa chọn khác rất

phổ biến trong học máy là

cái được gọi là đơn vị tuyến tính được chỉnh lưu.

Vì vậy, hàm giá trị trông như thế này và

công thức là a = max(0,z).

Vậy đạo hàm là một như vậy

miễn là z dương và

phái sinh hoặc

độ dốc bằng 0 khi z âm.

Nếu bạn đang triển khai điều này,

về mặt kỹ thuật là đạo hàm khi z là

chính xác bằng 0 không được xác định rõ ràng.

Nhưng khi bạn thực hiện

cái này trong máy tính,

khả năng bạn nhận được chính xác là z

bằng 000000000000 là rất nhỏ.

Vì vậy bạn không cần phải lo lắng về nó.

Trong thực tế, bạn có thể giả vờ

một đạo hàm khi z bằng 0,

bạn có thể giả vờ là một hoặc không.

Và bạn có thể làm việc tốt.

Vì vậy, thực tế là không thể phân biệt được.

Thực tế là, đây là một số quy tắc của

ngón tay cái để chọn chức năng kích hoạt.

Nếu đầu ra của bạn bằng 0 một giá trị,

nếu bạn đang sử dụng phân loại nhị phân,

thì hàm kích hoạt sigmoid là

sự lựa chọn rất tự nhiên cho lớp đầu ra.

Và sau đó đối với tất cả các giá trị đơn vị khác hoặc

đơn vị tuyến tính được chỉnh lưu ngày càng

sự lựa chọn mặc định của chức năng kích hoạt.

Vì vậy, nếu bạn không chắc chắn nên sử dụng để làm gì

lớp ẩn của bạn, tôi sẽ chỉ sử dụng

hàm kích hoạt giá trị là gì

bạn thấy hầu hết mọi người sử dụng những ngày này.

Mặc dù đôi khi người ta cũng sử dụng

hàm kích hoạt tan h.

Một nhược điểm của giá trị là

đạo hàm bằng 0 khi z

là tiêu cực.

Trong thực tế điều này hoạt động tốt.

Nhưng có một phiên bản khác của

giá trị được gọi là Leaky ReLU.

Chúng tôi sẽ cung cấp cho bạn công thức tiếp theo

trượt nhưng thay vì nó bằng 0

khi z âm,

nó chỉ có một độ dốc nhẹ như vậy.

Vì thế cái này được gọi là Leaky ReLU.

Điều này thường hoạt động tốt hơn

hàm kích hoạt giá trị

Mặc dù, nó chỉ không

được sử dụng nhiều trong thực tế.

Một trong hai sẽ ổn thôi.

Mặc dù, nếu bạn phải chọn một,

Tôi thường chỉ sử dụng giá trị.

Và lợi thế của cả giá trị và

Leaky ReLU là dành cho

rất nhiều không gian của z,

đạo hàm của hàm kích hoạt,

độ dốc của hàm kích hoạt

rất khác với số không.

Và vì vậy trong thực tế,

sử dụng hàm kích hoạt giá trị,

mạng lưới thần kinh của bạn sẽ thường xuyên học

nhanh hơn nhiều so với khi sử dụng tan h hoặc

hàm kích hoạt sigmoid.

Và lý do chính là có

ít ảnh hưởng của độ dốc này

hàm số sẽ tiến về 0,

điều đó làm chậm quá trình học tập.

Và tôi biết rằng trong một nửa phạm vi

của z, độ dốc của giá trị bằng 0.

Nhưng trong thực tế, đủ ẩn ý của bạn

đơn vị sẽ có z lớn hơn 0.

Vì vậy việc học vẫn có thể diễn ra khá nhanh đối với

hầu hết các ví dụ đào tạo.

Vì vậy, hãy tóm tắt nhanh những ưu điểm và

nhược điểm của các chức năng kích hoạt khác nhau.

Đây là chức năng kích hoạt sigmoid.

Tôi sẽ nói không bao giờ sử dụng cái này ngoại trừ

lớp đầu ra nếu bạn đang thực hiện nhị thức

phân loại hoặc

có lẽ hầu như không bao giờ sử dụng cái này.

Và lý do tôi gần như không bao giờ

sử dụng cái này là vì tan h là

khá nhiều vượt trội.

Vậy hàm kích hoạt tan h là thế này.

Và sau đó là mặc định,

kích hoạt được sử dụng phổ biến nhất

chức năng là ReLU, chính là cái này.

Vì vậy, nếu bạn không chắc chắn nên sử dụng cái gì khác,

sử dụng cái này

Và có lẽ, hãy thoải mái thử

ReLU bị rò rỉ có thể ở đâu

0,01(z,z), phải không?

Vậy a là giá trị lớn nhất của 0,1 nhân z và z.

Vì vậy, điều đó mang lại cho bạn điều này

uốn cong trong chức năng.

Và bạn có thể nói,

tại sao hằng số đó là 0,01?

Chà, bạn cũng có thể làm cái đó khác

tham số của thuật toán học.

Và một số người nói rằng điều đó thậm chí còn hiệu quả

tốt hơn, nhưng cách họ nhìn thấy mọi người làm điều đó.

Vì vậy, nhưng nếu bạn muốn thử nó trong

ứng dụng, xin vui lòng làm như vậy.

Và bạn có thể thấy nó hoạt động như thế nào và

nó hoạt động tốt như thế nào và

hãy kiên trì nếu nó

mang lại cho bạn một kết quả tốt.

Vì vậy tôi hy vọng điều đó mang lại cho bạn cảm giác nào đó

các lựa chọn của hàm kích hoạt

bạn có thể sử dụng trong mạng lưới thần kinh của mình.

Một trong những điều chúng ta sẽ thấy sâu sắc

học tập là bạn thường có rất nhiều

những lựa chọn khác nhau trong cách bạn

xây dựng mạng lưới thần kinh của bạn.

Khác nhau, từ một số đơn vị ẩn

đến chức năng kích hoạt lựa chọn,

về cách bạn khởi tạo các cách

mà chúng ta sẽ thấy sau.

Rất nhiều sự lựa chọn như thế.

Và hóa ra là đôi khi

khó có được hướng dẫn tốt cho

chính xác những gì sẽ làm việc tốt nhất cho

vấn đề của bạn.

Vì vậy, xuyên suốt các khóa học này,

Tôi sẽ tiếp tục cho bạn biết những gì tôi

xem xét trong ngành về mặt

những gì ít nhiều phổ biến.

Nhưng đối với ứng dụng của bạn với

các ứng dụng, đặc điểm riêng thực sự là

rất khó biết trước

chính xác những gì sẽ hoạt động tốt nhất.

Vì vậy, lời khuyên phổ biến sẽ là,

nếu bạn không chắc chắn cái nào trong số này

chức năng kích hoạt hoạt động tốt nhất,

hãy thử tất cả.

Và đánh giá giống như xác nhận giữ lại

bộ hoặc giống như một bộ phát triển,

mà chúng ta sẽ nói về sau.

Và xem cái nào hoạt động tốt hơn và

thì hãy bỏ việc đó đi.

Và tôi nghĩ rằng bằng cách thử nghiệm

những lựa chọn khác nhau này cho

ứng dụng của bạn, bạn sẽ tốt hơn

trong tương lai việc chứng minh thần kinh của bạn

kiến trúc mạng chống lại

những vấn đề về phong cách riêng.

Cũng như diễn biến của

các thuật toán thay vì,

nếu tôi bảo bạn luôn sử dụng một giá trị

kích hoạt và không sử dụng bất cứ điều gì khác.

Điều đó chỉ có thể áp dụng hoặc không

bất kể vấn đề gì bạn đang giải quyết.

Trong thời gian sắp tới hoặc

trong tương lai xa.

Được rồi, đó là sự lựa chọn

của hàm kích hoạt và

bạn thấy phổ biến nhất

các chức năng kích hoạt.

Có một câu hỏi khác đó

đôi khi bạn có thể hỏi cái nào là,

tại sao bạn thậm chí cần phải sử dụng

một chức năng kích hoạt nào cả?

Tại sao không loại bỏ điều đó?

Vì vậy, hãy nói về điều đó ở phần tiếp theo

video nơi bạn hiểu tại sao thần kinh

mạng cần một số loại

hàm kích hoạt phi tuyến tính.