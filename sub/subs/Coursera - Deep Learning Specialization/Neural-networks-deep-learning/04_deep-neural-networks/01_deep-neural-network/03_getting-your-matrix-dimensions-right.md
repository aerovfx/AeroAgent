# 03 xác định đúng kích thước ma trận của bạn

---

Khi triển khai một

mạng lưới thần kinh sâu,

một trong những cách gỡ lỗi

công cụ tôi thường xuyên

sử dụng để kiểm tra

tính đúng đắn của mã của tôi

là kéo một mảnh

bằng giấy và chỉ

làm việc thông qua các kích thước

trong ma trận tôi đang làm việc.

Hãy để tôi chỉ cho bạn cách làm

đó là vì tôi hy vọng điều này

sẽ giúp bạn dễ dàng hơn

để thực hiện sâu của bạn

mạng cũng vậy.

Vậy chữ L viết hoa bằng 5.

Tôi đếm chúng một cách nhanh chóng.

Không tính lớp đầu vào,

có năm lớp ở đây,

bốn lớp ẩn

và một lớp đầu ra.

Nếu bạn thực hiện

sự lan truyền về phía trước,

bước đầu tiên sẽ là Z1 bằng

W1 nhân đầu vào

tính năng x cộng với b1.

Hãy bỏ qua các số hạng thiên vị B

bây giờ và tập trung vào

các tham số W. Bây giờ,

lớp ẩn đầu tiên này

có ba đơn vị ẩn.

Vậy đây là Lớp 0,

Lớp 1, Lớp 2, Lớp 3,

Lớp 4 và Lớp 5.

Sử dụng ký hiệu chúng tôi đã có

từ video trước,

chúng ta có n1 đó, đó là

số lượng ẩn

đơn vị ở lớp 1,

bằng 3.

Ở đây chúng ta sẽ có

n2 đó bằng 5,

n3 bằng 4,

n4 bằng 2,

và n5 bằng 1.

Cho đến nay chúng ta chỉ thấy

mạng lưới thần kinh với

một đơn vị đầu ra duy nhất,

nhưng trong các khóa học sau

chúng ta sẽ nói về

mạng lưới thần kinh với nhiều

các đơn vị đầu ra cũng vậy.

Cuối cùng, đối với lớp đầu vào,

chúng ta cũng có n0 bằng

nX bằng 2.

Bây giờ, chúng ta hãy nghĩ về

kích thước của Z, W và X.

Z là vectơ kích hoạt

cho lớp ẩn đầu tiên này.

Vậy Z sẽ là 3 x 1,

sẽ là một

vectơ ba chiều.

Tôi sẽ viết nó là n1

bằng ma trận một chiều,

3 x 1 trong trường hợp này.

Bây giờ thì sao

tính năng đầu vào x?

X chúng tôi có hai tính năng đầu vào.

Vậy x là, trong ví dụ này,

2 x 1, nhưng tổng quát hơn

nó sẽ là n0 x 1.

Điều chúng tôi cần là dành cho

ma trận W1 là cái gì đó

rằng khi chúng ta nhân một

n0 x 1 vectơ với nó,

chúng ta nhận được một vectơ n1 x 1.

Vì vậy bạn có một

vectơ ba chiều

bằng cái gì đó nhân với a

vectơ hai chiều.

Theo quy luật ma trận

phép nhân,

điều này phải như vậy

một ma trận 3 x 2.

Bởi vì 3 x 2

ma trận nhân a 2 bằng

1 ma trận hoặc lần

một vectơ 2 x 1,

nó mang lại cho bạn một vectơ 3 x 1.

Tổng quát hơn,

điều này sẽ xảy ra

một ma trận n1 x n0 chiều.

Vì vậy, những gì chúng tôi đã tìm ra ở đây

đó là kích thước của W1

phải là n1 nhân n0,

và tổng quát hơn,

kích thước của

WL phải bằng nL x nL trừ 1.

Ví dụ,

kích thước của W2,

đối với điều này, nó sẽ

phải là 5 x 3,

hoặc nó sẽ là n2 nhân n1,

bởi vì chúng tôi đang đi

để tính Z2

bằng W2 nhân a1.

Một lần nữa, hãy bỏ qua

sự thiên vị cho bây giờ.

Đây sẽ là 3 x 1.

Chúng ta cần tỷ lệ này là 5 x 1.

Vì vậy, tỷ lệ này tốt hơn là 5 x 3.

Tương tự, W3 thực sự là

kích thước của lớp tiếp theo,

kích thước của

lớp trước đó.

Vậy cái này sẽ là 4 x 5.

W4 sẽ

là 2 x 4,

và W5 sẽ là 1 x 2.

Công thức chung để

kiểm tra xem đó là khi bạn

thực hiện các

ma trận cho lớp L,

rằng kích thước của nó

ma trận được nL bằng nL trừ 1.

Bây giờ, chúng ta hãy nghĩ về

chiều của vectơ này B.

Đây sẽ là

một vectơ 3 x 1,

vì vậy bạn phải thêm

cái đó đến 3 cái khác

1 vectơ để có được 3

bằng 1 vectơ làm đầu ra.

Đây sẽ là 5 x 1,

vậy là sẽ có

một vectơ 5 x 1 khác

để tính tổng

trong hai điều này

Tôi có trong hộp để

chính nó là một vectơ 5 x 1.

Nguyên tắc tổng quát hơn là

trong ví dụ bên trái,

b^[1] bằng n^[1] x 1,

như thế này 3 x 1.

Trong ví dụ thứ hai,

nó là n^[2] x 1 và như vậy

tổng quát hơn

trường hợp đó là b^[l]

nên là n^[l]

theo 1 chiều.

Hy vọng rằng hai điều này

phương trình giúp bạn

kiểm tra kỹ xem

kích thước của ma trận của bạn,

w, cũng như của

vectơ b của bạn là

đúng kích thước.

Tất nhiên, nếu bạn

thực hiện lan truyền ngược,

thì kích thước của

dw nên là

giống như kích thước của

w. Vì vậy dw nên là

cùng chiều với w,

và db phải là

cùng chiều với b.

Bây giờ, chiếc chìa khóa còn lại

bộ số lượng

kích thước của nó để

kiểm tra xem đây có phải là z không,

x, cũng như a của l,

điều mà chúng ta đã không nói chuyện

quá nhiều thứ ở đây.

Nhưng vì z của l là

bằng g của a của l,

áp dụng phần tử khôn ngoan sau đó z và

a phải có cùng kích thước

trong các loại mạng này.

Bây giờ chúng ta hãy xem những gì

xảy ra khi bạn có

một triển khai được vector hóa

nhìn vào nhiều

ví dụ tại một thời điểm.

Ngay cả đối với một vector hóa

tất nhiên là việc thực hiện

kích thước của w,

b, dw và db sẽ

giữ nguyên như cũ.

Nhưng kích thước của za,

cũng như x, sẽ thay đổi một chút

trong vector hóa của bạn

thực hiện.

Trước đây chúng ta có z^[1] bằng

w^[1] nhân x cộng b^]1],

trong đó đây là n^[1] x 1.

Đây là n^[1] bởi n^[0],

x là n^[0] x 1,

và b là n^[1] x 1.

Bây giờ, trong một vector hóa

thực hiện,

bạn sẽ có z^[1] bằng

w^[1] nhân x cộng b^[1].

Bây giờ z^[1] có được bằng cách

lấy z^[1] cho

các ví dụ riêng lẻ.

Vậy có z^[1][1],

z^[1][2] lên tới z^[1][m] và

xếp chúng như sau

và điều này mang lại cho bạn z^[1].

Kích thước của z^[1] là

thay vì n^[1] x 1,

cuối cùng nó là n^[1] by m,

nếu m là tập huấn luyện quyết định.

Kích thước của

w^[1] vẫn giữ nguyên

n^[1] của n^[0] cũng vậy và

x thay vì là n^[0] bởi

1 bây giờ là tất cả đào tạo của bạn

ví dụ được đóng dấu theo chiều ngang,

vậy bây giờ nó là n^[0] by m. bạn

chú ý rằng khi bạn lấy một,

n^[1] theo ma trận n^[0] và

nhân số đó với một

n^[0] theo m ma trận

rằng họ cùng nhau

thực sự mang lại cho bạn một

n^[1] theo m chiều

ma trận như mong đợi.

Bây giờ chi tiết cuối cùng là

b^[1] vẫn là n^[1] x 1.

Nhưng khi bạn lấy

cái này và thêm nó vào b,

sau đó thông qua phát sóng python

cái này sẽ bị trùng lặp

thành ma trận n^[1] by m

và sau đó thêm phần tử khôn ngoan.

Ở slide trước,

chúng tôi đã nói về

kích thước của w,

b, dw và db.

Đây là những gì chúng ta thấy

trong khi z^[l],

cũng như một^[l],

có kích thước n^[l] x 1,

thay vào đó chúng ta có bây giờ

vốn Z^[l] đó,

cũng như vốn A^[l],

là n^[l] bởi m.

Trường hợp đặc biệt này

là khi l bằng 0,

trong trường hợp đó A^[0],

bằng với

chỉ là sự đào tạo của bạn

thiết lập các tính năng đầu vào x sẽ diễn ra

bằng n^[0]

bởi m như mong đợi.

Tất nhiên, khi bạn

thực hiện điều này ở

lan truyền ngược,

chúng ta sẽ gặp bạn sau

tính toán dz cũng như da.

Tất nhiên, cách này có

cùng chiều với z và a.

Hy vọng bài tập thấp

đã trải qua sự giúp đỡ

làm rõ các kích thước của

các ma trận khác nhau

bạn sẽ làm việc cùng.

Khi bạn triển khai

lan truyền ngược

cho một mạng lưới thần kinh sâu,

miễn là bạn cố gắng vượt qua

mã của bạn và đảm bảo rằng

tất cả các ma trận hoặc

kích thước nhất quán,

điều đó thường sẽ

giúp bạn đi một số con đường

hướng tới loại bỏ một số

lớp lỗi có thể xảy ra.

Tôi hy vọng bài tập đó

để tìm ra

kích thước của

các ma trận khác nhau

bạn sẽ làm việc

với là hữu ích.

Khi bạn triển khai một mạng lưới thần kinh sâu

mạng nếu bạn giữ thẳng

kích thước của

những ma trận khác nhau này

và vectơ bạn đang làm việc,

hy vọng điều đó sẽ

giúp bạn loại bỏ

một số loại lỗi có thể xảy ra.

Nó chắc chắn giúp tôi

lấy đúng mã của tôi.

Tiếp theo, bây giờ chúng ta đã thấy

một số cơ chế của

làm thế nào để tiến về phía trước

lan truyền trong mạng nơ-ron.

Nhưng tại sao thần kinh sâu

mạng lưới rất hiệu quả và

tại sao họ làm tốt hơn

biểu diễn nông cạn?

Chúng ta hãy dành một vài phút trong

video tiếp theo để thảo luận.