# 10 lan truyền ngược-trực giác-tùy chọn

---

Ở video trước các bạn đã thấy

các phương trình cho

lan truyền ngược.

Trong video này, chúng ta hãy đi

qua một số trực giác bằng cách sử dụng

đồ thị tính toán cho

những phương trình đó như thế nào

đã được bắt nguồn.

Video này là

hoàn toàn tùy chọn

nên cứ thoải mái xem hay không.

Bạn sẽ có thể làm

toàn bộ hoạt động theo một trong hai cách.

Hãy nhớ lại rằng khi chúng ta nói chuyện

về hồi quy logistic,

chúng tôi đã có đường chuyển tiếp này

trong đó chúng tôi tính z, rồi A,

và sau đó là một sự mất mát và

để lấy đạo hàm chúng ta

đã có điều này lạc hậu

vượt qua nơi chúng ta có thể

đầu tiên tính da và sau đó

tiếp tục tính dz,

và sau đó tiếp tục

tính toán dw và db.

Định nghĩa về tổn thất

L của dấu phẩy y bằng

âm y log A trừ 1

trừ y nhân log 1 trừ A.

Nếu bạn quen thuộc với

tính toán và bạn lấy

đạo hàm của

điều này đối với A

điều đó sẽ cho bạn

công thức cho da.

Vậy da bằng đó.

Nếu bạn thực sự hình dung

ra phép tính,

bạn có thể chứng minh rằng đây là

âm y trên A cộng 1

trừ y trên một trừ A.

Chỉ là bắt nguồn từ đó

tính toán bằng cách lấy

dẫn xuất của điều này.

Hóa ra khi bạn lấy

một bước lùi nữa

để tính dz,

sau đó chúng tôi đã làm việc

dz đó bằng A

trừ y. Tôi đã không

giải thích tại sao trước đây,

nhưng hóa ra là từ

quy tắc dây chuyền của phép tính,

dz bằng da

nhân g số nguyên tố của z.

g của z ở đâu đây

bằng sigmoid của

z là chức năng kích hoạt của chúng tôi

cho đơn vị đầu ra này trong

hồi quy logistic.

Chỉ cần nhớ, đây là

vẫn là hồi quy logistic,

sẽ có X_1, X_2,

X_3, và sau đó chỉ

một đơn vị sigmoid,

và sau đó điều đó mang lại

chúng tôi a, cho chúng tôi y mũ.

Ở đây chức năng kích hoạt

là hàm sigmoid.

Là một bên, chỉ dành cho

những người bạn quen thuộc

với quy tắc dây chuyền của phép tính.

Lý do cho điều này là

vì a bằng

tới sigmoid của z,

và một phần của L đối với

đến z bằng một phần của

L đối với

a nhân da, dz.

Vì A bằng

tới sigmoid của z.

Điều này bằng với d,

dz g của z,

bằng g phẩy của z.

Đó là lý do tại sao biểu hiện này,

dz trong mã của chúng tôi là

bằng biểu thức này,

đó là da trong mã của chúng tôi

nhân g số nguyên tố của z

và thế này chỉ thế thôi.

Đạo hàm cuối cùng đó sẽ

chỉ có ý nghĩa nếu bạn

quen với phép tính và

đặc biệt là chuỗi

quy tắc từ phép tính.

Nhưng nếu không thì đừng

lo lắng về điều đó,

Tôi sẽ cố gắng giải thích

trực giác ở bất cứ nơi nào cần thiết.

Rồi cuối cùng, tính toán xong

dz cho hồi quy logistic,

chúng ta sẽ tính dw,

hóa ra là vậy

là dz nhân x và

db chỉ là

dz nơi bạn có

ví dụ đào tạo duy nhất.

Đó là hồi quy logistic.

Chúng ta sẽ làm gì

làm khi tính toán

lan truyền ngược cho

một mạng lưới thần kinh

là một phép tính

rất nhiều thứ như thế này,

nhưng chỉ có chúng tôi sẽ làm điều đó hai lần.

Bởi vì bây giờ chúng ta không có x

đi đến một đơn vị đầu ra,

nhưng x đang đi đến một lớp ẩn

và sau đó đi đến

một đơn vị đầu ra.

Thay vì tính toán này

là một bước như chúng ta có ở đây,

chúng ta sẽ có hai bước ở đây

trong mạng lưới thần kinh này

với hai lớp.

Trong hai lớp này

mạng lưới thần kinh,

đó là với lớp đầu vào,

lớp ẩn và

một lớp đầu ra.

Ghi nhớ các bước

của một phép tính.

Đầu tiên bạn tính z_1

sử dụng phương trình này

và sau đó tính a_1,

và sau đó bạn tính z_2.

Chú ý z_2 cũng phụ thuộc vào

các tham số W_2 và b_2,

và sau đó dựa vào

z_2 bạn tính a_2.

Rồi cuối cùng, điều đó

mang lại cho bạn sự mất mát.

Lan truyền ngược làm gì,

là nó sẽ quay trở lại

tính da_2 và sau đó tính dz_2,

sau đó quay trở lại

tính dW_2 và db_2.

Quay lại tính da_1,

dz_1, v.v.

Chúng ta không cần phải lấy

dẫn xuất với

đối với đầu vào x,

kể từ khi nhập x cho được giám sát

học vì

Chúng tôi không cố gắng tối ưu hóa x,

vì vậy chúng tôi sẽ không làm phiền

lấy đạo hàm,

ít nhất là để được giám sát

học tập đối với

x. tôi sẽ bỏ qua

tính toán rõ ràng da.

Nếu bạn muốn, bạn có thể

thực sự tính toán da^2,

và sau đó sử dụng nó

để tính dz^2.

Nhưng trong thực tế, bạn

có thể sụp đổ cả hai

các bước này thành một bước.

Cuối cùng bạn kết luận rằng dz^2 là

bằng a^2 trừ y,

giống như trước đây và

bạn cũng sẽ đi

viết dw^2 và db^2

ở dưới đây.

Bạn có dw^2 bằng nhau

sang dz^2 nhân a^1 chuyển đổi,

và db^2 bằng dz^2.

Bước này khá giống

cho hồi quy logistic,

nơi chúng tôi có cái dw đó

bằng dz nhân x,

ngoại trừ điều đó bây giờ, a^1

đóng vai x,

và có thêm một cái nữa

chuyển vị ở đó.

Bởi vì mối quan hệ giữa

ma trận vốn W

và cá nhân của chúng tôi

tham số w là,

có một chuyển âm ở đó,

bởi vì w bằng

tới một vectơ hàng.

Trong trường hợp của

hồi quy logistic

với đầu ra duy nhất,

dw^2 là như thế, trong khi

đây là một vectơ cột.

Đó là lý do tại sao có một

chuyển vị bổ sung cho a^1,

trong khi chúng tôi không làm vậy với x ở đây

cho hồi quy logistic.

Điều này hoàn thành một nửa

của sự lan truyền ngược.

Sau đó, một lần nữa, bạn

có thể tính da^1,

nếu bạn muốn mặc dù

trong thực tế,

tính toán cho da^1,

và dz^1 thường là

sụp đổ trong một bước.

Những gì bạn thực sự sẽ triển khai

có phải dz^1 bằng

w^2 lần chuyển đổi

dz^2 và sau đó,

lần một yếu tố khôn ngoan

tích của g^1 số nguyên tố của z^1.

Chỉ để kiểm tra

trên các kích thước.

Nếu bạn có một mạng lưới thần kinh

trông như thế này,

đầu ra y nếu vậy.

Nếu bạn có n^0

và x bằng n^0,

và đối với các tính năng,

n^1 đơn vị ẩn,

và n^2 cho đến nay,

và n^2 trong trường hợp của chúng tôi,

chỉ một đơn vị đầu ra,

thì ma trận w^2 là

n^2 x n^1 chiều,

z^2, và do đó,

dz^2 sắp diễn ra

là n^2 một chiều.

Thực sự đang diễn ra

là từng người một

khi chúng tôi đang làm

phân loại nhị phân,

và z^1, và do đó cũng có dz^1

sẽ là n^1

theo một chiều.

Lưu ý rằng đối với bất kỳ biến nào,

foo và dfoo luôn có

các kích thước giống nhau.

Đó là lý do tại sao, w và dw luôn

có cùng kích thước.

Tương tự, đối với b và db,

và z và dz, v.v.

Để đảm bảo rằng các kích thước

trong số này tất cả đều trùng khớp,

chúng ta có dz^1 bằng

w^2 hoán vị, nhân dz^2.

Sau đó, đây là một

thời gian sản phẩm theo yếu tố

g^1 số nguyên tố của z^1.

Nghiền các kích thước

từ trên cao,

cái này sẽ là n^1 x 1,

bằng với w^2 chuyển vị,

chúng tôi chuyển đổi điều này.

Nó sẽ như vậy thôi,

n^1 bởi n^2 chiều,

dz^2 sẽ là n^2

theo một chiều.

Sau đó, điều này là tương tự

thứ nguyên là z^.

Đây cũng là, n^1 bởi

một chiều, do đó

sản phẩm theo yếu tố.

Các kích thước có ý nghĩa.

N^1 theo một chiều

vectơ có thể là

thu được bởi n^1 bởi n^2

ma trận chiều,

nhân n^2 với n^1,

bởi vì sản phẩm của

hai điều này mang lại cho bạn

một n^1 bởi

ma trận một chiều.

Điều này trở thành

tích phần tử của 2,

n^1 bởi vectơ một chiều,

vì vậy kích thước phù hợp với nhau.

Một mẹo khi

thực hiện backprop,

nếu bạn chỉ cần chắc chắn

rằng kích thước của

ma trận của bạn khớp với nhau,

nếu bạn nghĩ kỹ,

kích thước của là gì

ma trận khác nhau của bạn

bao gồm w^1,

w^2, z^1, z^2, a^1,

a^2, v.v.,

và chỉ cần đảm bảo rằng

kích thước của ma trận này

hoạt động có thể phù hợp với nhau,

đôi khi điều đó sẽ xảy ra

loại bỏ khá nhiều

lỗi trong backprop.

Điều này mang lại cho chúng tôi dz^1.

Rồi cuối cùng,

chỉ để kết thúc, dw^1 và db^1,

chúng ta nên viết

họ ở đây, tôi đoán vậy.

Nhưng vì tôi đang chạy

hết chỗ,

Tôi sẽ viết chúng trên

bên phải slide,

dw^1 và db^1 được cho bởi

các công thức sau.

Điều này sẽ bằng

dz^1 lần x hoán vị,

và điều này đang diễn ra

bằng dz.

Bạn có thể nhận thấy một

sự tương đồng giữa

các phương trình này và

những phương trình này,

thực sự không phải ngẫu nhiên,

vì x đóng vai trò là a^0.

Chuyển vị X là chuyển vị^0.

Các phương trình đó là

thực sự rất giống nhau.

Điều đó mang lại ý nghĩa về cách

lan truyền ngược được bắt nguồn.

Chúng tôi có sáu chìa khóa

phương trình ở đây cho dz_2,

dw_2, db_2, dz_1,

dw_1 và db_1.

Hãy để tôi lấy những thứ này

sáu phương trình và

sao chép chúng sang

slide tiếp theo.

Họ đây rồi. Vì vậy

đến nay chúng tôi đã bắt nguồn

sự tuyên truyền đó cho việc đào tạo

trong một khóa đào tạo duy nhất

ví dụ tại một thời điểm

Nhưng nó sẽ đến

không có gì ngạc nhiên khi điều đó

thay vì làm việc trên một

một ví dụ tại một thời điểm,

chúng tôi muốn vector hóa

xuyên suốt khác nhau

ví dụ đào tạo.

Bạn nhớ điều đó cho

một sự lan truyền khi chúng ta

hoạt động trên một

ví dụ tại một thời điểm,

chúng ta đã có những phương trình như thế này,

cũng như nói a^1

bằng g^1 cộng z^1.

Để vector hóa,

chúng tôi đã nói,

chữ z và xếp chúng lại

lên thành cột như thế này,

z^1m và gọi đây là chữ Z viết hoa.

Sau đó chúng tôi tìm thấy điều đó bằng cách

xếp đồ đạc thành cột

và xác định thủ đô

phiên bản viết hoa của những cái này,

lúc đó chúng ta vừa có z^1

bằng với w^1x cộng

b và a^1 bằng g^1 của z^1.

Chúng tôi đã xác định ký hiệu

rất cẩn thận

trong khóa học này để đảm bảo rằng

xếp các ví dụ vào

cột khác nhau

của một ma trận làm cho

tất cả bài tập này.

Hóa ra là nếu bạn đi

thông qua toán học một cách cẩn thận,

thủ thuật tương tự cũng có tác dụng

cho sự lan truyền ngược.

Các phương trình vector hóa

như sau.

Đầu tiên, nếu bạn lấy dzs này cho

đào tạo khác nhau

ví dụ và ngăn xếp

chúng khác nhau

các cột của ma trận,

Tương tự cho điều này, tương tự cho điều này.

Thế thì đây là

thực hiện vector hóa.

Đây là cách bạn có thể tính dW^2.

Có cái này thêm 1 trên n

bởi vì hàm chi phí J là

1 trên m này của số tiền từ tôi

bằng 1 đến

m của những mất mát.

Khi tính đạo hàm, chúng ta

có thêm 1 trong số hạng m,

giống như chúng ta đã làm khi chúng ta còn

tính toán cập nhật trọng lượng

cho hồi quy logistic.

Đó là bản cập nhật

bạn nhận được db^2,

một lần nữa, một số dz.

Khi đó, chúng ta có 1 trên m. Dz^1

được tính như sau.

Một lần nữa, đây là một

chỉ sản phẩm có yếu tố khôn ngoan,

trong khi trước đây chúng ta đã thấy trên

slide trước nói rằng đây là

một n1 theo vectơ một chiều.

Không, đây là n1 x m

ma trận chiều.

Cả hai điều này cũng

n1 theo m chiều.

Đó là lý do tại sao dấu hoa thị đó là

sản phẩm theo từng yếu tố.

Cuối cùng,

hai bản cập nhật còn lại

có lẽ không nên

nhìn bất ngờ quá.

Tôi hy vọng điều đó mang lại cho bạn

một số trực giác về việc làm thế nào

sự lan truyền ngược

thuật toán được dẫn xuất.

Trong tất cả các lĩnh vực học máy,

Tôi nghĩ rằng đạo hàm của

thuật toán lan truyền ngược

thực sự là một trong những

phần phức tạp

toán học mà tôi đã thấy.

Nó đòi hỏi phải biết cả hai

đại số tuyến tính cũng như

đạo hàm của

ma trận thực sự

bắt nguồn từ đầu

từ những nguyên tắc đầu tiên.

Nếu bạn là một chuyên gia

trong phép tính ma trận,

bằng cách sử dụng quá trình này, bạn

có thể muốn rút ra

thuật toán của chính bạn.

Nhưng tôi nghĩ rằng có

thực sự là rất nhiều

những người thực hành học sâu

đã thấy

đạo hàm tại

về mức độ bạn đã

nhìn thấy trong video này

và đã

có thể có tất cả các quyền

trực giác và có thể

để thực hiện thuật toán này

rất hiệu quả.

Nếu bạn là chuyên gia tính toán

hãy xem liệu bạn có thể rút ra được

toàn bộ sự việc từ đầu.

Đó là một trong những điều khó khăn nhất

phần toán học trên

những dẫn xuất khó nhất

mà tôi đã thấy ở tất cả

của học máy.

Nhưng dù sao đi nữa, nếu

bạn thực hiện điều này,

cái này sẽ hoạt động và

Tôi nghĩ bạn có

đủ trực giác để điều chỉnh

vào và làm cho nó hoạt động.

Chỉ còn một chi tiết cuối cùng,

chia sẻ của tôi về bạn trước bạn

triển khai mạng lưới thần kinh của bạn,

đó là cách để

khởi tạo trọng số

của mạng lưới thần kinh của bạn.

Hoá ra là thế

khởi tạo của bạn

các tham số không bằng 0,

nhưng ngẫu nhiên hóa ra là

rất quan trọng cho việc đào tạo

mạng lưới thần kinh của bạn.

Trong video tiếp theo,

bạn sẽ thấy tại sao.