# 03-làm-quyết định-cây-quyết định

---

Trong video trước, chúng tôi đã xây dựng

cây quyết định bằng cách sử dụng

phân loại cây quyết định,

và chúng tôi hình dung ra cái cây

sử dụng phương pháp cây lô.

Nhưng câu hỏi vẫn còn đó,

tiêu chí đó là gì

chi phối cách mỗi nút

sẽ bị chia cắt?

Trong video này, chúng tôi sẽ

cùng nhau tìm ra câu trả lời.

Chúng tôi sẽ thực hiện một số

tính toán nhanh trong

Máy tính xách tay Jupyter để

nâng cao sự hiểu biết của chúng tôi

của cây quyết định.

Để có được nhiều nhất

ra khỏi video này,

Tôi khuyên bạn nên

thực hiện các phép tính

bên cạnh. Hãy bắt đầu.

Có hai tiêu chí mà

quyết định cách chia tốt nhất

trong cây quyết định,

họ là Gini Gain

được tính bằng cách sử dụng

Tạp chất Gini hoặc Gini

Chỉ số và thu thập thông tin

được tính toán

sử dụng Entropy.

Cả tạp chất Gini

và thu thập Entropy

tạp chất trong một nút

và thường dẫn đến

kết quả rất giống nhau.

Nhưng về mặt tính toán,

Tạp chất Gini

nhanh hơn Entropy một chút.

Trong khóa học này, chúng tôi

sẽ tập trung vào

tạp chất Gini và

tính Gini Gain.

Nhưng con đường chia đôi

được hình thành bằng cách sử dụng

thu được thông tin là

cũng rất giống nhau.

Để hiểu Gini Gain chúng ta hãy

đầu tiên hãy hiểu cái gì

Tạp chất Gini là.

Tạp chất Gini hoặc chỉ số Gini

đo lường xác suất của

một trường hợp ngẫu nhiên

phân loại sai khi

được chọn ngẫu nhiên.

Chỉ số Gini càng thấp thì

khả năng càng thấp

của việc phân loại sai.

Đây là cách tạp chất Gini

cho một tập hợp S được xác định.

C là số lớp

trong tập dữ liệu trong khi

p_i là xác suất của

xuất hiện ở lớp thứ i.

Vì vấn đề của chúng tôi liên quan đến

chỉ có hai lớp,

doanh số cao và doanh số thấp,

chúng ta có thể mở rộng biểu thức này

như vậy p_0 ở đâu

xác suất của

xảy ra ở lớp 0

trong khi p_1 là xác suất

xảy ra ở Lớp 1.

Hãy thử tính toán

tạp chất Gini cho

ba nút đầu tiên của

cây quyết định của chúng tôi

dựa trên công thức này.

Chúng tôi sẽ tạo ra một

hàm tính toán

tạp chất Gini và trả lại

giá trị được làm tròn thành

ba chữ số thập phân.

Chức năng này mất

hai lý lẽ,

num_Class_0 và num_Class_1.

Trong trường hợp của chúng tôi num_Class_0

đại diện cho số lượng

quan sát thuộc về

lớp doanh thu thấp hoặc bằng không.

Num_Class_1 đại diện

số lượng

quan sát thuộc về

cao cấp hoặc một.

Bây giờ hãy sử dụng cái này

thực hiện chức năng và tính toán

tạp chất Gini của

nút gốc và

cả các nút con.

Trong nút gốc của

cây quyết định

như chúng ta có thể thấy từ cốt truyện,

có 15 mẫu

của từng lớp.

Tạp chất Gini

của nút gốc là

0,5 đó chính xác là những gì

chúng ta có thể thấy trên cốt truyện.

Bây giờ hãy tính Gini

Tạp chất của các nút con.

Ở nút nhánh trái của

cây quyết định

10 mẫu thuộc về

xếp vào loại doanh số bán hàng thấp và

14 mẫu thuộc về

doanh số bán hàng cao cấp.

Mặt khác ở

nút nhánh phải

của cây quyết định,

có năm

mẫu thuộc về

doanh số bán hàng thấp và

một mẫu thuộc về

lớp bán hàng cao.

Tạp chất Gini của

nút con trái là 0,486 và

tạp chất Gini của

đứa trẻ đúng là

0,278 khớp chính xác

giá trị chúng ta thấy trong cốt truyện.

Đến nay chúng tôi đã tính toán

tạp chất Gini của rễ

nút và hai nút nhánh.

Trong số cả ba,

chúng tôi đã có giá trị cao nhất,

0,5 cho nút gốc.

Điều này là do nút gốc

là nút duy nhất chứa

toàn bộ dữ liệu với

mẫu bằng nhau thuộc về

cho cả hai lớp,

vì vậy nó là một nút rất không trong sạch,

hoặc chúng ta có thể nói đó là một

hỗn hợp không đồng nhất hoàn hảo.

Tương tự, gini_child_node2

có số lượng mẫu nhiều nhất

thuộc loại bán hàng thấp

do đó tạp chất của nó và

Giá trị Gini thấp hơn.

Nhưng còn nút có độ tinh khiết cao thì sao

chứa mẫu

chỉ có một lớp?

Hãy lấy nút lá này.

Nó chỉ chứa hai mẫu

thuộc về

lớp bán hàng thấp.

Như bạn có thể thấy,

Tạp chất Gini bằng không,

vì vậy tạp chất Gini

của nút lá

có mẫu của một đơn

lớp học là thấp nhất,

cho biết đó là một nút thuần túy.

Bây giờ chúng ta đã hiểu Gini

chúng ta hãy di chuyển

tập trung vào Gini Gain.

Gini Gain chính là sự khác biệt

giữa tạp chất Gini của

nút gốc và

tạp chất Gini có trọng số

của các nút con.

Tăng Gini về mặt toán học

bằng với tạp chất Gini

của Nút gốc trừ đi trọng số

Tạp chất Gini của các nút con.

Sự phân chia tốt nhất ở mỗi nút

được chọn bằng cách sử dụng phép chia

dẫn đến

mức tăng Gini tối đa

cho bước tiếp theo ngay lập tức.

Đây cũng là lý do tại sao

thuật toán cây quyết định là

gọi là thuật toán tham lam.

Họ chỉ nhìn vào

kết quả tốt nhất có thể cho

chỉ là bước tiếp theo ngay lập tức

không nhìn vào

bức tranh tổng thể.

Hãy tính Gini

Đạt được bằng cách sử dụng công thức này.

Tổng cộng 30 mẫu

được phân chia dựa trên

các phân đoạn tính năng

thành hai nút con

có 24 và sáu

mẫu tương ứng.

Tạp chất Gini có trọng số của

nút con sẽ là

tính theo công thức này.

Hãy thực hiện phép tính ngay bây giờ và

hiển thị giá trị lên tới

ba dấu thập phân.

Tạp chất Gini có trọng số

của nút con là 0,444.

Trừ nó từ

tạp chất Gini

của nút gốc,

chúng ta sẽ nhận được Gini Gain.

Như bạn có thể thấy, Gini

Mức tăng hóa ra là 0,055.

This way to form each split in

cây quyết định Gini Gains

trong nhiều lần chia tay

được tính toán.

Từ những kết quả khác nhau,

sự phân chia với mức tối đa

Gini Gain được chọn.

Tôi hy vọng bây giờ bạn

có một ý tưởng tốt hơn

về sự phân chia được hình thành như thế nào

trong một cây quyết định.

Giống như tạp chất Gini,

Entropy là một tiêu chí khác

đo lường sự

chất lượng của sự phân chia.

Entropy trong bối cảnh của

classification problems is

thước đo sự rối loạn

hoặc tạp chất trong một nút.

Đối với tập S đối với

một sự phân loại

vấn đề về công thức

cho Entropy như sau.

C là số lớp

trong tập dữ liệu trong khi

p_i là xác suất của

xuất hiện ở lớp thứ i.

Giá trị của Entropy

thay đổi từ 0-1 trong đó một

đại diện cho mức độ cao nhất của

tạp chất và số không

đại diện cho một nút thuần túy.

Về mặt toán học, thông tin

đạt được bằng

Entropy của nút gốc trừ

Entropy có trọng số của các nút con.

Để có được sự hiểu biết tốt hơn

hãy thoải mái vẽ một cái cây với

Entropy và xác minh các con số

bằng cách sử dụng tính toán của riêng bạn.

Tôi chắc chắn bây giờ bạn đã rõ ràng

về cây quyết định như thế nào

chọn cách chia tốt nhất

và độ tinh khiết của

một nút được đo.

Trong video tiếp theo

chúng ta sẽ lặn

đi sâu vào quyết định như thế nào

cây đưa ra dự đoán.

Hãy tin tôi đi, điều đó sẽ xảy ra

trở nên thực sự thú vị