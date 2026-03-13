# 06 lan truyền tiến và lùi

---

Trong video trước các bạn đã thấy

các khối cơ bản của việc thực hiện

một mạng lưới thần kinh sâu sắc,

một bước lan truyền về phía trước cho

mỗi lớp và một lớp tương ứng

bước lan truyền ngược.

Hãy xem bạn thực sự có thể làm thế nào

thực hiện các bước này.

Chúng ta sẽ bắt đầu với

sự lan truyền về phía trước.

Hãy nhớ lại rằng điều này sẽ

làm là nhập a^l trừ 1,

và xuất ra a^l và

bộ nhớ đệm, z^l.

Chúng tôi vừa nói rằng, từ

quan điểm thực hiện,

có lẽ chúng tôi sẽ lưu vào bộ nhớ đệm

w^l và b^l nữa,

chỉ để làm cho

lệnh gọi hàm a

dễ dàng hơn một chút trong

bài tập chương trình.

Các phương trình cho điều này nên

nhìn quen quen rồi.

Cách thực hiện chuyển tiếp

chức năng chỉ có thế này thôi

bằng w^l nhân a^l

trừ 1 cộng b^l,

và sau đó a^l bằng

hàm kích hoạt được áp dụng cho z.

Nếu bạn muốn một vector hóa

thực hiện,

thì chỉ lúc đó thôi

a^l trừ 1 cộng b,

b là một chương trình phát sóng Python,

và a^l bằng g,

áp dụng theo từng phần tử cho z.

Bạn còn nhớ, trên

sơ đồ cho bước thứ 4,

hãy nhớ chúng ta đã có chuỗi này

của các hộp sắp tới,

vì vậy bạn khởi tạo

điều đó với việc cho ăn

trong a^0, bằng x.

Vì vậy, bạn khởi tạo cái này với,

đầu vào là gì

đến cái đầu tiên?

Nó thực sự là một^0,

đâu là đầu vào

tính năng cho

một ví dụ đào tạo

nếu bạn đang làm một

ví dụ tại một thời điểm,

hoặc a^0 nếu bạn đang xử lý

toàn bộ tập huấn luyện.

Đó là đầu vào để

tiền đạo đầu tiên

chức năng trong chuỗi,

và sau đó chỉ cần lặp lại

điều này cho phép bạn tính toán

sự lan truyền về phía trước

từ trái sang phải.

Tiếp theo, hãy nói về

bước lan truyền ngược.

Đây, mục tiêu của bạn

là nhập da^l,

và xuất ra da^l trừ

1 và dw^l và db^l.

Hãy để tôi viết ra

các bước bạn cần phải làm

tính toán những điều này.

Dz^l bằng da^l

sản phẩm có yếu tố khôn ngoan,

với g của l nguyên tố z của

tôi. Sau đó để tính toán

các dẫn xuất,

dw^l bằng dz^l

nhân a của l trừ 1.

Tôi đã không nói rõ ràng

đặt nó vào bộ nhớ đệm,

nhưng hóa ra bạn

cũng cần cái này.

Khi đó db^l bằng

dz^l, và cuối cùng,

da của l trừ 1 bằng

w^l chuyển đổi lần dz^l.

Tôi không muốn trải qua

chi tiết

dẫn xuất cho điều này,

nhưng hóa ra là nếu

bạn hiểu định nghĩa này

cho da và cắm nó vào đây,

sau đó bạn nhận được công thức tương tự

như chúng tôi đã có ở đó trước đây,

về cách bạn tính toán

dz^l là hàm của

dz^l trước đó.

Thực ra thì, nếu tôi

chỉ cần cắm nó vào đây,

cuối cùng thì dz^l bằng nhau

sang w^l cộng 1 hoán vị dz^l

cộng 1 nhân g^l số nguyên tố z

của tôi. Tôi biết điều này trông

giống như rất nhiều đại số.

Thực ra bạn có thể

kiểm tra kỹ xem

bản thân bạn rằng điều này

là phương trình

chúng tôi đã viết ra cho

tuyên truyền ngược vào tuần trước,

khi chúng tôi đang làm

một mạng lưới thần kinh

chỉ với một lớp ẩn duy nhất.

Xin nhắc lại, lần này

là sản phẩm có yếu tố khôn ngoan,

vì vậy tất cả những gì bạn cần là

bốn phương trình đó để thực hiện

chức năng lạc hậu của bạn.

Rồi cuối cùng, tôi sẽ chỉ viết

ra một phiên bản vector hóa.

Vì vậy, dòng đầu tiên trở thành dz^l

bằng da^l theo phần tử

sản phẩm có g^l số nguyên tố của z^l,

có lẽ không có gì ngạc nhiên ở đó.

Dw^l trở thành 1 trên m,

dz^l lần a^l

trừ đi 1 chuyển âm.

Sau đó db^l trở thành 1

hơn m np.sum dz^l.

Khi đó trục bằng 1,

keepdims bằng đúng.

Chúng tôi đã nói về việc sử dụng

np.sum ở phần trước

tuần, để tính toán db.

Rồi cuối cùng, da^l trừ

1 là w^l lần chuyển đổi

dz của l. Cái này

cho phép bạn nhập cái này

số lượng, da, ở đây.

Đầu ra dW^l, dp^l,

các công cụ phái sinh bạn cần,

cũng như da^l

trừ 1 như sau.

Đó là cách bạn thực hiện

chức năng lùi.

Chỉ để tóm tắt,

lấy đầu vào x,

bạn có thể có

lớp đầu tiên có thể

có chức năng kích hoạt ReLU.

Sau đó đi đến lớp thứ hai,

có thể sử dụng ReLU khác

chức năng kích hoạt,

đi đến thứ ba

lớp có thể có

hàm kích hoạt sigmoid

nếu bạn đang làm nhị phân

phân loại,

và điều này tạo ra y-hat.

Sau đó sử dụng y-hat, bạn

có thể tính được tổn thất.

Điều này cho phép bạn bắt đầu

sự lặp lại ngược của bạn.

Tôi sẽ vẽ mũi tên trước.

Tôi đoán là tôi không cần phải làm vậy

thay bút quá nhiều.

Lúc đó bạn sẽ ở đâu

có tính toán backprop

các dẫn xuất,

tính dW^3,

db^3, dW^2, db^2, dW^1, db^1.

Trên đường đi bạn sẽ

tính toán với tiền mặt.

Chúng ta sẽ chuyển z^1, z^2, z^3.

Ở đây bạn vượt qua ngược lại

da^2 và da^1.

Điều này có thể tính toán da^0,

nhưng chúng tôi sẽ không sử dụng nó

bạn chỉ có thể loại bỏ điều đó.

Đây là cách bạn thực hiện

chỗ dựa phía trước và chỗ dựa phía sau cho

một mạng lưới thần kinh ba lớp.

Còn cái này cuối cùng

chi tiết mà tôi đã không nói

về cái gì dành cho

đệ quy về phía trước,

chúng ta sẽ khởi tạo nó

với dữ liệu đầu vào x.

Thế còn

đệ quy ngược?

Ờ hóa ra là thế

da của l khi bạn đang sử dụng

hồi quy logistic,

khi bạn đang làm

phân loại nhị phân

bằng y trên

a cộng 1 trừ y trên 1 trừ a.

Hóa ra là đạo hàm

của hàm mất đối với

đầu ra liên quan đến

y-hat có thể được hiển thị

trở thành những gì nó là.

Nếu bạn quen

với phép tính,

nếu bạn tra cứu

hàm mất l và

lấy đạo hàm một cách tôn trọng

tới y-hat đối với a,

bạn có thể cho thấy rằng bạn

lấy công thức đó.

Đây là công thức

bạn nên sử dụng cho da,

cho lớp cuối cùng,

viết hoa L. Tất nhiên nếu bạn

đã có một vector hóa

thực hiện,

sau đó bạn khởi tạo

đệ quy ngược,

không phải với cái này,

nhưng với chữ A viết hoa cho

lớp L sẽ là

điều tương tự đối với

ví dụ khác nhau.

Hơn a cho chuyến tàu đầu tiên

ví dụ cộng 1 trừ

y lần đầu tiên

đào tạo ví dụ trên

1 trừ A cho

ví dụ về chuyến tàu đầu tiên,

chấm-chấm-chấm xuống

ví dụ về chuyến tàu thứ n.

Vậy 1 trừ a của M. Đó là cách

bạn sẽ triển khai

phiên bản vector hóa

Đó là cách bạn khởi tạo

phiên bản vector hóa

của sự lan truyền ngược.

Bây giờ chúng ta đã thấy cơ bản

khối xây dựng của

cả sự lan truyền về phía trước như

cũng như lan truyền ngược.

Bây giờ nếu bạn thực hiện

những phương trình này,

bạn sẽ nhận được đúng

thực hiện

chống đỡ phía trước và chống đỡ phía sau để

giúp bạn có được

các công cụ phái sinh mà bạn cần.

Có thể bạn đang nghĩ, à

đó là rất nhiều phương trình.

Tôi hơi bối rối.

Tôi không chắc lắm tôi thấy

nó hoạt động như thế nào và nếu

bạn đang cảm thấy như vậy,

lời khuyên của tôi là khi bạn

đến với tuần này

nhiệm vụ lập trình,

bạn sẽ có thể

thực hiện những điều này cho

chính bạn và họ sẽ

cụ thể hơn nhiều.

Tôi biết đó là một

rất nhiều phương trình,

và có thể một số phương trình

không hoàn toàn có ý nghĩa,

nhưng nếu bạn vượt qua

phép tính và tuyến tính

đại số không dễ,

nên cứ thoải mái thử nhé

nhưng đó thực sự là

một trong nhiều hơn

những dẫn xuất khó

trong học máy.

Hóa ra các phương trình

chúng tôi đã viết ra là

chỉ là các phương trình tính toán

để tính đạo hàm,

đặc biệt là ở backprop,

nhưng một lần nữa,

nếu điều này cảm thấy

trừu tượng một chút,

một chút bí ẩn đối với bạn,

lời khuyên của tôi là khi bạn đã hoàn thành

bài tập lập trình,

nó sẽ cảm thấy một chút

cụ thể hơn với bạn.

Mặc dù tôi phải nói rằng, ngay cả

hôm nay khi tôi thực hiện

một thuật toán học tập,

đôi khi ngay cả tôi cũng vậy

ngạc nhiên khi

thuật toán học tập của tôi

thực hiện

hoạt động và đó là vì

rất nhiều sự phức tạp của

học máy đến từ

dữ liệu thay vì

từ các dòng mã.

Đôi khi bạn cảm thấy như

bạn thực hiện một

vài dòng mã,

không chắc chắn nó đã làm gì,

nhưng nó gần như có tác dụng một cách kỳ diệu,

và đó là vì rất nhiều

phép thuật thực sự không có trong

đoạn mã bạn viết

mà thường không quá dài.

Nó không thực sự đơn giản,

nhưng nó không phải là 10.000,

100.000 dòng mã,

nhưng bạn cho nó ăn

rất nhiều dữ liệu mà

đôi khi mặc dù tôi đã

làm việc với máy

học lâu rồi

đôi khi vẫn còn bất ngờ

tôi một chút khi học tập

thuật toán hoạt động,

bởi vì rất nhiều

sự phức tạp của

thuật toán học tập của bạn

đến từ dữ liệu

thay vì nhất thiết phải từ bạn

viết hàng ngàn và

hàng nghìn dòng mã.

Đó là cách bạn thực hiện

mạng lưới thần kinh sâu.

Một lần nữa điều này sẽ trở nên nhiều hơn

cụ thể khi bạn đã hoàn thành

bài tập lập trình.

Trước khi tiếp tục,

trong video tiếp theo,

Tôi muốn thảo luận

siêu tham số và tham số.

Hóa ra là khi

bạn đang luyện lưới sâu,

có khả năng tổ chức

siêu thông số của bạn tốt

sẽ giúp bạn làm việc hiệu quả hơn

trong việc phát triển mạng lưới của bạn.

Trong video tiếp theo, chúng ta hãy nói chuyện

về chính xác điều đó có nghĩa là gì.