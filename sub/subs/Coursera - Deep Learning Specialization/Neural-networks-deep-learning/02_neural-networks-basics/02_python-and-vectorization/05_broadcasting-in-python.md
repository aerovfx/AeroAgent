# 05 phát sóng trong python

---

Trong video trước,

Tôi đã đề cập đến việc phát sóng

là một kỹ thuật khác mà bạn có thể sử dụng

để làm cho mã Python của bạn chạy nhanh hơn.

Trong video này, chúng ta hãy đi sâu vào cách

phát sóng bằng Python thực sự hoạt động.

Hãy cùng khám phá

phát sóng với một ví dụ.

Trong ma trận này, tôi đã hiển thị số

lượng calo từ carbohydrate,

protein và

chất béo trong 100 gram của bốn loại thực phẩm khác nhau.

Vì vậy, ví dụ,

hóa ra là 100 gram táo,

có 56 calo từ carbs, và

ít hơn nhiều từ protein và chất béo.

Trong khi đó, ngược lại, 100 gam

thịt bò có 104 calo từ protein và

135 calo từ chất béo.

Bây giờ, giả sử mục tiêu của bạn là

tính toán phần trăm calo

từ carbs, protein và

chất béo cho mỗi loại trong số bốn loại thực phẩm.

Vì vậy, ví dụ,

nếu bạn nhìn vào cột này và

cộng các số ở cột đó

bạn nhận được 100 gam táo đó

có 56 cộng 1,2 cộng 1,8 vậy

đó là 59 calo.

Và do đó tính theo tỷ lệ phần trăm của

calo từ carbohydrate

trong một quả táo sẽ

là 56 trên 59, tức là khoảng 94,9%.

Vì vậy hầu hết lượng calo trong một quả táo

đến từ carbs, trong khi ngược lại,

hầu hết lượng calo của thịt bò đều đến

từ protein và chất béo, v.v.

Vì vậy, phép tính bạn muốn thực sự là

để tổng hợp từng cột trong bốn cột

của ma trận này để có được tổng số

lượng calo trong 100 gram táo,

thịt bò, trứng và khoai tây.

Và sau đó để chia toàn bộ ma trận,

để có được tỷ lệ phần trăm của

calo từ carbs, protein và

chất béo cho mỗi loại trong số bốn loại thực phẩm.

Vì vậy, câu hỏi là, bạn có thể làm

điều này mà không có vòng lặp for rõ ràng?

Chúng ta hãy nhìn vào

sao bạn có thể làm được điều đó.

Những gì tôi sẽ làm là

chỉ cho bạn cách bạn có thể thiết lập,

nói ma trận này bằng

ma trận ba nhân bốn A.

Và sau đó với một dòng mã Python

chúng ta sẽ tổng hợp các cột.

Vậy chúng ta sẽ có bốn số

tương ứng với tổng số

lượng calo trong bốn thứ này

các loại thực phẩm khác nhau,

100 gram của bốn thứ này

các loại thực phẩm khác nhau.

Và tôi sẽ sử dụng dòng thứ hai

mã Python để chia từng

bốn cột bởi

tổng tương ứng của chúng.

Nếu sự mô tả bằng lời đó

không rõ ràng lắm,

hy vọng nó sẽ rõ ràng hơn trong giây lát

khi chúng ta nhìn vào mã Python.

Vì vậy, chúng ta đang ở đây trong sổ ghi chép của Sao Mộc.

Tôi đã viết cái này đầu tiên

đoạn mã để điền trước

ma trận A với các số ta có

ngay bây giờ, vì vậy chúng ta sẽ nhấn shift enter và

chỉ cần chạy nó, vậy là có ma trận A.

Và bây giờ đây là hai

dòng mã Python.

Đầu tiên chúng ta sẽ tính toán

tau bằng a, tổng đó.

Và x bằng 0 tức là tính tổng theo chiều dọc.

Chúng ta sẽ nói nhiều hơn về điều đó sau.

Và sau đó in cal.

Vì vậy chúng ta sẽ tính tổng theo chiều dọc.

Bây giờ 59 là tổng số

lượng calo trong quả táo là 239

tổng số calo trong thịt bò

và trứng và khoai tây, v.v.

Và sau đó với tỷ lệ phần trăm tính toán

bằng A/cal.reshape 1,4.

Thực ra chúng tôi muốn tỷ lệ phần trăm,

vậy hãy nhân với 100 ở đây.

Và sau đó hãy in tỷ lệ phần trăm.

Hãy chạy nó đi.

Và thế là

lệnh đó chúng ta đã lấy ma trận A và

chia nó cho ma trận một cho bốn này.

Và điều này cho chúng ta

ma trận tỷ lệ phần trăm.

Vì vậy, khi chúng tôi làm việc bằng cách

vừa mới đưa tay vào quả táo kìa

là cột đầu tiên 94,9% của

lượng calo đến từ carbs.

Chúng ta hãy quay trở lại các slide.

Vì vậy, chỉ cần lặp lại hai

dòng mã chúng tôi có,

đây là những gì đã viết

vào cuốn sổ tay của Jupiter.

Để thêm một chút chi tiết về tham số này,

(trục = 0), nghĩa là bạn

muốn Python tính tổng theo chiều dọc.

Vậy nếu đây là trục 0 thì đây

có nghĩa là tính tổng theo chiều dọc,

trong đó trục hoành là trục 1.

Vậy có thể viết trục 1 hoặc tổng

theo chiều ngang thay vì tổng theo chiều dọc.

Và sau đó lệnh này ở đây,

đây là một ví dụ về Python

phát sóng trong đó bạn lấy ma trận A.

Vì vậy, đây là ma trận ba nhân bốn và

bạn chia nó cho ma trận một x bốn.

Và về mặt kỹ thuật, sau lần đầu tiên này

dòng mã cal, biến cal,

đã là ma trận một x bốn.

Vì vậy, về mặt kỹ thuật, bạn không cần

gọi định hình lại ở đây một lần nữa, vì vậy

điều đó thực sự có chút dư thừa.

Nhưng khi tôi đang viết mã Python nếu

Tôi không hoàn toàn chắc chắn về ma trận nào,

liệu kích thước của ma trận tôi thường

sẽ chỉ gọi một lệnh định hình lại chỉ để

hãy chắc chắn rằng nó đúng

vectơ cột hoặc vectơ hàng hoặc

bất cứ điều gì bạn muốn nó được.

Lệnh định hình lại là một thời gian không đổi.

Đó là một hoạt động theo thứ tự

gọi như vậy là rất rẻ.

Vì vậy, đừng ngại sử dụng công cụ định hình lại

lệnh để đảm bảo rằng ma trận của bạn

kích thước bạn cần là như thế nào.

Bây giờ, hãy giải thích chi tiết hơn về cách

kiểu hoạt động này có hiệu quả phải không?

Chúng tôi đã có một ma trận ba nhân bốn và

chúng tôi chia nó cho một ma trận một bốn.

Vì vậy, làm thế nào bạn có thể chia ba cho

bốn ma trận bằng một ma trận một bốn?

Hoặc bằng một trong bốn vector?

Chúng ta hãy đi qua một vài chi tiết

ví dụ về phát sóng

Nếu bạn lấy một vectơ 4 x 1 và

thêm nó vào một số, cái gì

Python sẽ làm là lấy số này và

tự động mở rộng

nó cũng thành một vectơ bốn nhân một,

như sau.

Và vectơ [1, 2, 3,

4] cộng với số 100 kết thúc

với vectơ đó ở bên phải.

Bạn đang thêm 100 vào mọi phần tử,

và trên thực tế chúng tôi sử dụng hình thức này

phát sóng ở nơi hằng số đó

tham số b trong video trước đó.

Và kiểu phát sóng này hoạt động với

cả vectơ cột và vectơ hàng,

và trên thực tế, chúng tôi sử dụng một dạng tương tự

phát sóng sớm hơn với hằng số

chúng tôi đang thêm vào một vectơ

tham số b trong hồi quy logistic.

Đây là một ví dụ khác.

Giả sử bạn có hai

bởi ba ma trận và

bạn thêm nó vào cái này theo ma trận n.

Vì vậy, trường hợp chung sẽ là nếu bạn

có một số ma trận (m,n) ở đây và

bạn thêm nó vào ma trận (1,n).

Những gì Python sẽ làm là sao chép ma trận m,

lần để biến cái này thành ma trận m x n,

vì vậy thay vì cái này bằng

ba ma trận nó sẽ sao chép nó hai lần trong

ví dụ này để biến nó thành cái này.

Ngoài ra, ma trận hai nhân ba và

chúng ta sẽ thêm những thứ này để

bạn sẽ có tổng ở bên phải,

được không?

Vậy là bạn đã lấy,

bạn đã thêm 100 vào cột đầu tiên,

đã thêm 200 vào cột thứ hai,

thêm 300 vào cột thứ ba.

Và về cơ bản đây là điều chúng tôi

đã làm ở slide trước,

ngoại trừ việc chúng ta sử dụng phép chia

thay vì một hoạt động bổ sung.

Vì vậy, một ví dụ cuối cùng,

cho dù bạn có ma trận (m,n) và

bạn thêm phần này vào một vectơ (m,1),

(m,1) ma trận.

Sau đó chỉ cần sao chép n lần theo chiều ngang.

Vì vậy, bạn kết thúc với một ma trận (m,n).

Vì vậy, như bạn có thể tưởng tượng, bạn sao chép

nó theo chiều ngang ba lần.

Và bạn thêm những thứ đó.

Vì vậy, khi bạn thêm chúng, bạn sẽ có kết quả này.

Vì vậy chúng tôi đã thêm 100 vào hàng đầu tiên và

thêm 200 vào hàng thứ hai.

Đây là nguyên tắc tổng quát hơn

phát sóng bằng Python.

Nếu bạn có ma trận (m,n) và bạn thêm hoặc

trừ hoặc nhân hoặc

chia với ma trận (1,n),

sau đó cái này sẽ sao chép nó n

lần vào một ma trận (m,n).

Và sau đó áp dụng phép cộng,

phép trừ và

phép nhân phần tử chia một cách khôn ngoan.

Nếu ngược lại, bạn phải lấy (m,n)

ma trận và cộng, trừ, nhân,

chia cho ma trận (m,1),

thì điều này cũng sẽ sao chép nó bây giờ n lần.

Và biến nó thành ma trận (m,n) và

sau đó áp dụng yếu tố hoạt động một cách khôn ngoan.

Chỉ là một trong những chương trình phát sóng,

đó là nếu bạn có ma trận (m,1),

vậy đó thực sự là một vectơ cột

như [1,2,3], và bạn thêm,

trừ, nhân hoặc

chia cho một số hàng.

Vì vậy, có thể là ma trận (1,1).

Vì vậy, chẳng hạn như cộng với 100,

sau đó bạn sẽ sao chép

số thực này n lần cho đến khi bạn

cũng nhận được một ma trận (n,1) khác.

Và sau đó bạn thực hiện thao tác như vậy

như là phần bổ sung cho ví dụ này về mặt yếu tố.

Và một cái gì đó tương tự cũng có tác dụng với

vectơ hàng.

Phiên bản phát sóng đầy đủ chung

thậm chí có thể làm nhiều hơn thế này một chút.

Nếu bạn quan tâm bạn có thể

đọc tài liệu cho

NumPy và xem việc phát sóng

trong tài liệu đó.

Điều đó mang lại nhiều hơn một chút

định nghĩa chung về truyền hình

Nhưng những cái trên slide là chính

các hình thức phát sóng mà bạn kết thúc

cần sử dụng khi bạn

thực hiện một mạng lưới thần kinh.

Trước khi chúng ta kết thúc,

chỉ một bình luận cuối cùng, đó là dành cho

những người trong số các bạn đã quen với việc này

lập trình bằng MATLAB hoặc

Octave, nếu bạn đã từng sử dụng MATLAB hoặc

Hàm quãng tám bsxfun

trong lập trình mạng lưới thần kinh bsxfun có

một cái gì đó tương tự, không hoàn toàn giống nhau.

Nhưng nó thường được sử dụng cho mục đích tương tự

như những gì chúng tôi sử dụng tính năng phát sóng bằng Python.

Nhưng điều này thực sự chỉ dành cho

MATLAB rất tiên tiến và

Người dùng Octave, nếu bạn chưa nghe đến điều này,

đừng lo lắng về nó

Bạn không cần phải biết điều đó khi bạn

mã hóa mạng lưới thần kinh bằng Python.

Vì vậy, nó đã được phát sóng bằng Python.

Tôi hy vọng rằng khi bạn lập trình

bài tập về nhà mà việc phát sóng sẽ cho phép bạn

không chỉ làm cho mã chạy nhanh hơn,

mà còn giúp bạn có được điều bạn muốn

được thực hiện với ít dòng mã hơn.

Trước khi bạn đi sâu vào lập trình

bài tập, tôi muốn chia sẻ với bạn

thêm một nhóm ý tưởng nữa,

đó là có một số lời khuyên và

thủ thuật mà tôi đã tìm thấy làm giảm

số lượng lỗi trong mã Python của tôi và

mà tôi hy vọng cũng sẽ giúp được bạn.

Vì vậy, với điều đó,

hãy nói về điều đó trong video tiếp theo.