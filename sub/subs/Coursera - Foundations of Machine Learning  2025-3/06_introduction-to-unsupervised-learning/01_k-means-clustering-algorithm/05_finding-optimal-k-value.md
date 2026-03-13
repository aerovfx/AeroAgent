# 05 tìm-tối ưu-k-giá trị

---

Bước thứ năm trong xây dựng

một mô hình không giám sát sử dụng

K có nghĩa là tìm

số lượng cụm tối ưu,

đó là K. Có

hai phương pháp phổ biến để tìm

số cụm tối ưu.

Phương pháp đầu tiên

là đồ thị khuỷu tay,

và phương pháp thứ hai là

sử dụng điểm hình bóng.

Chúng ta hãy đi qua từng người trong số họ

để hiểu họ tốt hơn,

bắt đầu với âm mưu khuỷu tay.

Mục tiêu của chúng tôi là tập hợp

dữ liệu thành các nhóm,

nơi mỗi nhóm hoặc cụm

chứa các sản phẩm tương tự.

Bây giờ trong mỗi cụm,

có một điểm trung tâm

gọi là trọng tâm.

Một thước đo chất lượng

của cụm có thể là như thế nào

đóng các điểm khác nhau

đến từ họ

trọng tâm tương ứng.

Chúng ta có thể kiểm tra khoảng cách này

mỗi điểm trong mỗi cụm.

Về mặt toán học, chúng ta gọi

khoảng cách này

the-Trong-Cụm-Tổng bình phương,

hoặc viết tắt là WCSS.

WCSS là tổng bình phương

về khoảng cách của

mỗi điểm dữ liệu trong

tất cả các cụm của họ

trọng tâm tương ứng.

Ý định đầu tiên của chúng tôi có thể

có thể hạ WCSS xuống,

các cụm càng tốt,

bởi vì số điểm sẽ là

gần các trọng tâm hơn.

Tuy nhiên, đây không phải là trường hợp.

Giả sử có n

quan sát trong một dữ liệu nhất định

đặt và chúng tôi cũng chỉ định n cho

là số cụm.

Nói cách khác, điều này có nghĩa

rằng mỗi điểm

sẽ là một trung tâm

của cụm riêng của nó và

khoảng cách giữa

chúng sẽ bằng không.

Trong kịch bản này,

WCSS cũng sẽ bằng không.

Tuy nhiên, điều này không

có ý nghĩa bởi vì chúng tôi

sẽ có nhiều cụm như

số lượng quan sát.

Chúng ta phải tìm một giá trị

cho số lượng

các cụm có WCSS thấp,

nhưng không thấp đến mức chúng ta có

không thể quản lý được

số cụm.

Đây là nơi

quy ước phổ biến

của phương pháp khuỷu tay giúp chúng tôi.

Hãy hiểu nó bằng cách đi

qua một số ví dụ.

Chúng ta có thể tạo ra một đồ thị

Các giá trị WCSS so với

số cụm để

tìm giá trị tối ưu của

K dùng khuỷu tay

điểm trong đồ thị.

Biểu đồ kết quả sẽ

trông giống như thế này

Chúng ta có thể quan sát từ biểu đồ

đó là số lượng

cụm tăng lên,

giá trị WCSS giảm xuống,

nhưng tốc độ giảm WCSS

đột nhiên giảm xuống sau một

số cụm nhất định.

Điểm này là điểm khuỷu tay.

Trong biểu đồ hiển thị

đây, đúng như mong đợi,

Giá trị WCSS là

lớn nhất khi K = 1.

Nếu bạn nhìn kỹ,

sau K = 3,

sau đó giảm WCSS

đã giảm đáng kể.

Trong ví dụ này, K =

3 là điểm khuỷu tay,

có nghĩa là giá trị K tối ưu

đối với tập dữ liệu này là ba.

Điều quan trọng cần lưu ý

rằng phương pháp khuỷu tay là

một quy ước và không

một lý thuyết đã được thiết lập,

vì vậy nó không hoạt động

cho tất cả các kịch bản.

Ví dụ, trong

cốt truyện hiển thị ở đây,

khuỷu tay có thể là 3,

hoặc 4, thậm chí 5.

Nó phụ thuộc vào con người

giải thích.

Điều này gây khó khăn cho việc tìm kiếm

giá trị K phù hợp

trong những tình huống như vậy.

Trong những tình huống này,

phương pháp tiếp theo,

điểm hình bóng, có thể giúp chúng tôi.

Điểm số hình bóng có tác dụng

về hai biện pháp quan trọng.

Số 1, gần thế nào

mỗi điểm trong

một cụm là khác

các điểm trong cùng một cụm.

Số 2, mỗi điểm cách nhau bao xa

một cụm là từ các điểm

ở nơi gần nhất

cụm lân cận.

Giá trị của hình bóng

điểm số dao động từ -1-1,

nơi người ta có nghĩa là các điểm

được phân công hoàn hảo trong một cụm,

và các cụm dễ dàng

có thể phân biệt được.

Số không có nghĩa là các cụm

đang chồng chéo lên nhau,

và -1 có nghĩa là điểm

được giao sai

trong một cụm.

Chúng ta hãy tiếp tục và tìm

số lượng tối ưu

cụm cho sự hiệp lực

sử dụng cả hai cách tiếp cận,

phương pháp vẽ đồ thị khuỷu tay và

phương pháp tính điểm hình bóng.

Hãy bắt đầu với

vẽ khuỷu tay để

tìm K. Ở đây chúng ta có

đã nhập hết rồi

các thư viện cần thiết

sớm hơn nên chúng tôi không cần

để nhập nó một lần nữa.

Bây giờ hãy xem mã.

Ở đây, chúng tôi đã tạo

phạm vi cụm khung dữ liệu

để xác định phạm vi của các cụm.

Chúng tôi đã thiết lập phạm vi

để vẽ đồ thị của

Giá trị K từ 1-11.

Để sửa đổi phạm vi này,

bạn có thể sửa đổi giá trị

có trong ngoặc.

Ví dụ, nếu bạn muốn

để thay đổi phạm vi thành 20,

bạn chỉ có thể thay thế

11 này với 20.

Sau đó bạn có thể có được

cốt truyện WCSS so với K

cho đến K = 20.

Sau đó chúng tôi tiến hành

khởi tạo WCSS cho

mỗi kết quả của K là

được lưu trữ trong phạm vi 1-11 của chúng tôi.

Dòng mã tiếp theo

khởi tạo phương tiện K

thuật toán cho những điều này

các giá trị khác nhau của

K và vẽ đồ thị khuỷu tay cho

WCSS so với K bằng cách sử dụng

thư viện matplotlib.

WCSS có sẵn ở

thuộc tính quán tính.

Dựa vào cốt truyện đó

chúng tôi đã có được,

khuỷu tay của chúng tôi không rõ ràng lắm.

Giá trị tối ưu

của K có thể là 3,

hoặc 4, thậm chí có thể là 5.

Đây là nhược điểm

của phương pháp khuỷu tay,

mà chúng ta đã thảo luận trước đó.

Vì vậy hãy thử phương pháp tiếp theo

để có được

giá trị tối ưu của K,

đó là điểm số hình bóng

phương pháp, trên tập dữ liệu của chúng tôi.

Hãy nhập khẩu

điểm hình bóng

từ sklearn.metrics và sau đó

tiến hành chạy code để tìm

hình bóng ghi điểm.

Hãy nhìn vào mã này.

Giống như chúng ta đã làm trước đó,

đầu tiên chúng ta định nghĩa một

khoảng giá trị K đến

tính toán

điểm hình bóng cho,

trong trường hợp của chúng tôi, 2-10.

Để tính điểm hình bóng,

chúng ta cần phải có tại

ít nhất hai cụm.

Sau khi khởi tạo

phạm vi cụm,

sau đó chúng tôi tiến hành chạy

K có nghĩa là thuật toán để

tập dữ liệu của chúng tôi

cho các giá trị khác nhau

của K từ 2-10.

Điều này sau đó được in

cái này nối tiếp cái kia.

Hãy nhìn vào

hình bóng ghi điểm ở đây.

Rõ ràng là cao nhất

cho số cụm là hai.

Do đó, K = 2 là

giá trị K tối ưu của chúng tôi cho

vấn đề hiệp lực này dựa trên

về điểm số hình bóng.

Hãy tiếp tục và chạy K

có nghĩa là thuật toán một lần nữa,

nhưng lần này với

số cụm

bằng 2. Đây là

mã cho điều đó.

Điều đó khá thú vị.

Tôi chắc chắn với bất kỳ

tập dữ liệu trong tương lai,

bạn sẽ dễ dàng tìm thấy

số tối ưu

của các cụm sử dụng

các phương pháp khác nhau như

cốt truyện khuỷu tay và hình bóng

điểm cho K có nghĩa là.

Cũng lưu ý rằng chúng tôi đã chọn

hai là tối ưu của chúng tôi

số cụm.

Tiếp theo, chúng ta sẽ thực hiện

một biểu đồ phân tán với

một số tính năng liên quan

để cố gắng phân tích

các cụm và đạt được

một số hiểu biết có giá trị.