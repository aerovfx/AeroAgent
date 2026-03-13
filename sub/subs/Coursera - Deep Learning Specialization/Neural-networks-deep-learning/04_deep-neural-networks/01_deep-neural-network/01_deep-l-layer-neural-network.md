# 01 mạng nơ-ron sâu-l-lớp

---

Chào mừng bạn đến với tuần thứ tư của khóa học này.

Đến bây giờ, bạn đã thấy sự lan truyền về phía trước và

lan truyền ngược trong bối cảnh

của một mạng lưới thần kinh, với một ẩn duy nhất

lớp, cũng như hồi quy logistic, và

bạn đã học về vector hóa, và

khi điều quan trọng là phải

khởi tạo các cách ngẫu nhiên.

Nếu bạn đã thực hiện trong vài tuần qua

bài tập về nhà, bạn cũng đã thực hiện và

thấy một số ý tưởng này có hiệu quả

chính bạn.

Vì thế đến bây giờ,

bạn thực sự đã nhìn thấy hầu hết các ý tưởng mà bạn

cần phải triển khai một mạng lưới thần kinh sâu.

Những gì chúng ta sẽ làm trong tuần này là thực hiện

những ý tưởng đó và tập hợp chúng lại với nhau để

mà bạn sẽ có thể thực hiện

mạng lưới thần kinh sâu sắc của riêng bạn.

Bởi vì vấn đề của tuần này

bài tập kéo dài hơn,

chỉ là có nhiều việc hơn thôi,

Tôi sẽ giữ các video cho

tuần này ngắn hơn khi bạn có thể vượt qua

các video nhanh hơn một chút và

sau đó có nhiều thời gian hơn để làm một việc quan trọng

bài tập có vấn đề ở phần cuối, điều mà tôi hy vọng

sẽ để lại cho bạn những suy nghĩ sâu sắc

mạng lưới thần kinh, nếu bạn cảm thấy tự hào.

Vậy mạng lưới thần kinh sâu là gì?

Bạn đã nhìn thấy bức ảnh này

hồi quy logistic và

bạn cũng đã thấy mạng lưới thần kinh

với một lớp ẩn duy nhất.

Vì vậy, đây là một ví dụ về thần kinh

mạng có hai lớp ẩn và

một mạng lưới thần kinh với 5 lớp ẩn.

Chúng tôi nói rằng hồi quy logistic

là một mô hình rất "nông cạn",

trong khi mô hình này ở đây là

một mô hình sâu sắc hơn nhiều, và

nông so với độ sâu

là vấn đề mức độ.

Vì vậy mạng nơ-ron của

một lớp ẩn duy nhất,

đây sẽ là một mạng lưới thần kinh 2 lớp.

Hãy nhớ khi chúng ta đếm các lớp trong một nơ-ron

mạng, chúng tôi không tính lớp đầu vào,

chúng tôi chỉ đếm các lớp ẩn

lớp đầu ra cũng vậy.

Vì vậy, đây sẽ là mạng thần kinh 2 lớp

mạng vẫn còn khá nông,

nhưng không nông cạn như hồi quy logistic.

Hồi quy logistic về mặt kỹ thuật

là mạng nơ-ron một lớp,

lúc đó chúng ta có thể, nhưng

trong vài năm qua AI,

trong cộng đồng học máy,

đã nhận ra rằng có những chức năng

mạng lưới thần kinh rất sâu có thể học được điều đó

các mô hình nông hơn thường không thể làm được.

Mặc dù đối với bất kỳ vấn đề nào, nó có thể

khó có thể dự đoán trước chính xác như thế nào

nằm sâu trong mạng lưới của bạn mà bạn mong muốn.

Vì vậy sẽ là hợp lý nếu thử

hồi quy logistic, hãy thử một và

sau đó hai lớp ẩn và xem

số lớp ẩn như một siêu khác

tham số mà bạn có thể thử

nhiều giá trị khác nhau và

đánh giá tất cả những điều đó qua quá trình xác thực

dữ liệu hoặc trên bộ phát triển của bạn.

Xem thêm về điều đó sau này là tốt.

Bây giờ chúng ta hãy đi qua ký hiệu chúng ta

được sử dụng để mô tả mạng lưới thần kinh sâu.

Đây là một, hai, ba,

mạng lưới thần kinh bốn lớp,

Với ba lớp ẩn, và

số lượng đơn vị ẩn này

tôi đoán là lớp 5, 5, 3 và

thì có một đơn vị phía trên.

Vậy ký hiệu chúng ta sẽ sử dụng,

sẽ sử dụng chữ L viết hoa để biểu thị

số lớp trong mạng.

Vì vậy, trong trường hợp này, L = 4, và như vậy

số lượng lớp, và

chúng ta sẽ sử dụng chữ N siêu ký tự

[l] để biểu thị số lượng nút,

hoặc số lượng đơn vị

trong lớp chữ thường l.

Vì vậy nếu chúng ta lập chỉ mục này,

đầu vào là lớp "0".

Đây là lớp 1, đây là lớp 2,

đây là lớp 3 và đây là lớp 4.

Sau đó, chúng ta có điều đó, ví dụ,

n[1], đó sẽ là thế này,

số đầu tiên ở đó sẽ bằng 5,

bởi vì chúng tôi có 5 đơn vị ẩn ở đó.

Đối với cái này, chúng ta có n[2],

số lượng đơn vị trong

lớp ẩn thứ hai

cũng bằng 5, n[3] = 3, và

n[4] = n[L] số này

của đơn vị trên là 01,

bởi vì chữ L viết hoa của bạn bằng 4,

và chúng ta cũng sẽ có ở đây cái đó cho

lớp đầu vào n[0] = nx = 3.

Vì vậy, đó là ký hiệu chúng tôi sử dụng để mô tả

số lượng nút chúng tôi có khác nhau

các lớp.

Đối với mỗi lớp L, chúng tôi cũng sẽ sử dụng

a[l] để biểu thị các kích hoạt trong lớp l.

Vì vậy chúng ta sẽ thấy điều đó sau

sự lan truyền,

cuối cùng bạn tính toán a[l] là

kích hoạt g(z[l]) và

có lẽ việc kích hoạt là

cũng được lập chỉ mục bởi lớp l,

và sau đó chúng ta sẽ sử dụng W[l ] để biểu thị,

trọng lượng cho

tính toán giá trị z[l] trong lớp l và

tương tự, b[l] được dùng để tính z [l].

Cuối cùng, chỉ để tóm tắt ký hiệu,

các tính năng đầu vào được gọi là x,

nhưng x cũng là số lần kích hoạt

của lớp 0, do đó a[0] = x,

và kích hoạt lớp cuối cùng,

a[L] = y-mũ.

Vì vậy a[L] bằng với sản lượng dự đoán

để dự đoán y-hat cho mạng lưới thần kinh.

Vậy bây giờ bạn đã biết sâu sắc thế nào

mạng lưới thần kinh trông giống như,

cũng như ký hiệu mà chúng tôi sẽ sử dụng để mô tả

và tính toán với các mạng sâu.

Tôi biết chúng tôi đã giới thiệu rất nhiều ký hiệu

trong video này, nhưng nếu bạn quên

ý nghĩa của một số biểu tượng, chúng tôi cũng đã đăng

trên trang web của khóa học, một bảng ký hiệu hoặc

hướng dẫn ký hiệu mà bạn có thể sử dụng để xem

tìm hiểu ý nghĩa của những biểu tượng khác nhau này.

Tiếp theo, tôi muốn mô tả những gì về phía trước

lan truyền trong loại mạng này

trông giống như.

Chúng ta hãy đi vào video tiếp theo.