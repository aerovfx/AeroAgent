# 03 tính toán-a-neural-mạng-đầu ra

---

Trong video trước, bạn đã thấy mạng nơ-ron một lớp ẩn trông như thế nào.

Trong video này chúng ta cùng tìm hiểu chi tiết về

chính xác cách mạng lưới thần kinh này tính toán các kết quả đầu ra này.

Những gì bạn thấy là nó giống như hồi quy logistic,

nhưng lặp đi lặp lại rất nhiều lần.

Chúng ta hãy xem xét. Vì vậy, mạng lưới thần kinh hai lớp trông như thế này.

Chúng ta hãy đi sâu hơn vào chính xác những gì mạng lưới thần kinh này tính toán.

Bây giờ, chúng ta đã nói trước hồi quy logistic đó,

vòng tròn trong hồi quy logistic,

thực sự đại diện cho hai bước của hàng tính toán.

Bạn tính z như sau, và một giây,

bạn tính toán kích hoạt dưới dạng hàm sigmoid của z.

Vì vậy, mạng lưới thần kinh thực hiện điều này nhiều lần hơn.

Hãy bắt đầu bằng cách chỉ tập trung vào một trong các nút trong lớp ẩn.

Hãy nhìn vào nút đầu tiên trong lớp ẩn.

Vì vậy, hiện tại tôi đã chuyển sang màu xám các nút khác.

Vì vậy, tương tự như hồi quy logistic ở bên trái,

các nút này trong lớp ẩn thực hiện hai bước tính toán.

Bước đầu tiên được coi là nửa bên trái của nút này,

nó tính z bằng w hoán vị x cộng b,

và ký hiệu chúng ta sẽ sử dụng là,

đây là tất cả số lượng liên quan đến lớp ẩn đầu tiên.

Vì vậy, đó là lý do tại sao chúng ta có nhiều dấu ngoặc vuông ở đó.

Đây là nút đầu tiên trong lớp ẩn.

Vì vậy, đó là lý do tại sao chúng ta có chỉ số dưới ở đó.

Đầu tiên, nó thực hiện điều đó,

và sau đó là bước thứ hai,

nó tính a_[1]_1 bằng sigmoid của z_[1]_1, như vậy.

Vì vậy, với cả z và a,

quy ước ký hiệu là a, l, i,

chữ l ở đây nằm trong ngoặc vuông chỉ số trên,

đề cập đến số lớp,

và chỉ số i ở đây,

đề cập đến các nút trong lớp đó.

Vì vậy, nút chúng ta sẽ xem xét là lớp một,

đó là một nút lớp ẩn.

Vì vậy, đó là lý do tại sao chỉ số trên và chỉ số dưới đều là một.

Vì vậy, vòng tròn nhỏ đó,

nút đầu tiên trong mạng lưới thần kinh,

thể hiện việc thực hiện hai bước tính toán này.

Bây giờ, hãy xem nút thứ hai trong mạng lưới thần kinh,

hoặc nút thứ hai trong lớp ẩn của mạng lưới thần kinh.

Tương tự như đơn vị hồi quy logistic ở bên trái,

vòng tròn nhỏ này tượng trưng cho hai bước tính toán.

Bước đầu tiên là tính z.

Đây vẫn là lớp một,

nhưng bây giờ nút thứ hai bằng w hoán vị x,

cộng b_[1]_2, rồi a_[1] hai bằng sigmoid của z_[1]_2.

Một lần nữa, vui lòng tạm dừng video nếu bạn muốn,

nhưng bạn có thể kiểm tra kỹ xem chỉ số trên và

ký hiệu chỉ số dưới phù hợp với những gì chúng tôi đã viết ở trên bằng màu tím.

Vậy là chúng ta đã nói về hai đơn vị ẩn đầu tiên trong mạng lưới thần kinh,

có đơn vị ba và bốn cũng đại diện cho một số tính toán.

Bây giờ, hãy để tôi lấy cặp phương trình này,

và cặp phương trình này,

và hãy sao chép chúng sang slide tiếp theo.

Vì vậy, đây là mạng lưới thần kinh của chúng tôi,

và đây là lần đầu tiên,

và đây là phương trình thứ hai mà chúng tôi đã giải được

trước đó cho đơn vị ẩn thứ nhất và thứ hai.

Nếu sau đó bạn đi qua và viết ra các phương trình tương ứng

đối với đơn vị ẩn thứ ba và thứ tư, bạn sẽ nhận được những điều sau.

Vì vậy, hãy để tôi chỉ ra ký hiệu này là rõ ràng,

đây là vectơ w_[1]_1,

đây là một chuyển vị vector nhân x.

Vì vậy, đó chính là ý nghĩa của chữ T trên đó.

Đó là một chuyển vị vector.

Bây giờ, như bạn có thể đoán,

nếu bạn thực sự đang triển khai một mạng lưới thần kinh,

làm điều này với một vòng lặp for, có vẻ thực sự không hiệu quả.

Vì vậy, điều chúng ta sắp làm,

là lấy bốn phương trình này và vector hóa.

Vì vậy, chúng ta sẽ bắt đầu bằng cách tính z dưới dạng vectơ,

hóa ra bạn có thể làm điều đó như sau.

Hãy để tôi lấy những chữ w này và xếp chúng thành một ma trận,

sau đó bạn có w_[1]_1 hoán vị,

vậy đó là một vectơ hàng,

hoặc chuyển đổi vectơ cột này cung cấp cho bạn một vectơ hàng, sau đó w_[1]_2,

chuyển dịch, chuyển dịch w_[1]_3, chuyển dịch w_[1]_4.

Vì vậy, bằng cách xếp chồng bốn vectơ w đó lại với nhau,

bạn kết thúc với một ma trận.

Vì vậy, một cách khác để nghĩ về điều này là chúng ta có bốn đơn vị hồi quy logistic ở đó,

và mỗi đơn vị hồi quy logistic,

có một vectơ tham số tương ứng,

w. Bằng cách xếp chồng bốn vectơ đó lại với nhau,

bạn kết thúc với ma trận 4 x 3 này.

Vì vậy, nếu sau đó bạn lấy ma trận này và nhân nó với các đặc điểm đầu vào x1,

x2, x3, bạn sẽ hiểu được cách hoạt động của phép nhân ma trận.

Bạn kết thúc với w_[1]_1 hoán vị x,

w_2_[1] hoán vị x, w_3_[1] hoán vị x, w_4_[1] hoán vị x.

Vậy thì chúng ta đừng tính b.

Vì vậy, bây giờ chúng ta thêm vào đây một vectơ b_[1]_1 một, b_[1]_2, b_[1]_3, b_[1]_4.

Vì vậy, về cơ bản là thế này,

thì đây là b_[1]_1, b_[1]_2, b_[1]_3, b_[1]_4.

Vì vậy, bạn thấy rằng mỗi hàng trong số bốn hàng

kết quả này tương ứng chính xác với từng hàng trong số bốn hàng này,

mỗi đại lượng trong số bốn đại lượng mà chúng ta có ở trên.

Vì vậy, nói cách khác, chúng ta vừa chỉ ra rằng vật này do đó bằng

z_[1]_1, z_[1]_2, z_[1]_3, z_[1]_4, như được định nghĩa ở đây.

Có lẽ không có gì đáng ngạc nhiên, chúng ta sẽ gọi toàn bộ cái này là vectơ z_[1],

được thực hiện bằng cách xếp chồng các cá thể z này thành một vectơ cột.

Khi chúng ta vector hóa, một trong những quy tắc kinh nghiệm có thể giúp bạn định hướng điều này,

là trong khi chúng ta có các nút khác nhau trong lớp,

chúng ta sẽ xếp chúng theo chiều dọc.

Vì vậy, đó là lý do tại sao chúng ta có z_[1]_1 đến z_[1]_4,

chúng tương ứng với bốn nút khác nhau trong lớp ẩn,

và vì vậy chúng tôi xếp bốn số này theo chiều dọc để tạo thành vectơ z[1].

Để sử dụng thêm một phần ký hiệu,

ma trận bốn nhân ba này ở đây mà chúng ta thu được bằng cách xếp chồng chữ thường w_[1]_1,

w_[1]_2, v.v., chúng ta sẽ gọi ma trận này là W viết hoa [1].

Tương tự, vectơ này, chúng ta sẽ gọi b là chỉ số trên [1] dấu ngoặc vuông.

Vì vậy, đây là một vectơ bốn nhân một.

Vậy bây giờ, chúng ta đã tính z bằng cách sử dụng ký hiệu ma trận vectơ này,

điều cuối cùng chúng ta cần làm là tính các giá trị này của a.

Vì vậy, Prior sẽ không làm bạn ngạc nhiên khi thấy rằng chúng ta sẽ định nghĩa a_[1],

như chỉ xếp chồng lên nhau,

những giá trị kích hoạt đó, a [1],

1 đến a [1], 4.

Vì vậy, chỉ cần lấy bốn giá trị này và xếp chúng lại với nhau trong một vectơ gọi là a[1].

Đây sẽ là một sigmoid của z[1],

nơi điều này hiện đã được thực hiện

hàm sigmoid chứa bốn phần tử của z,

và áp dụng hàm sigmoid theo từng phần tử cho nó.

Vì vậy, chỉ là một bản tóm tắt,

chúng ta đã tìm ra rằng z_[1] bằng w_[1] nhân vectơ x cộng với vectơ b_[1],

và a_[1] là sigmoid nhân z_[1].

Chúng ta hãy sao chép nó vào slide tiếp theo.

Những gì chúng ta thấy là đối với lớp đầu tiên của mạng nơ-ron với đầu vào x,

chúng ta có z_[1] bằng w_[1] nhân x cộng b_[1],

và a_[1] là sigmoid của z_[1].

Kích thước của cái này là bốn nhân một bằng nhau,

đây là ma trận bốn nhân ba nhân vectơ ba nhân một cộng vectơ bốn nhân một b,

và đây là bốn chiều cùng một chiều với phần cuối.

Hãy nhớ rằng chúng ta đã nói x bằng a_[0].

Chỉ cần nói y hat cũng bằng hai.

Nếu muốn, bạn thực sự có thể lấy x này và thay thế nó bằng a_[0],

vì a_[0] là nếu bạn muốn làm bí danh cho vectơ của các tính năng đầu vào, x.

Bây giờ, thông qua một dẫn xuất tương tự,

bạn có thể nhận ra rằng cách biểu diễn cho lớp tiếp theo có thể

cũng được viết tương tự ở chỗ lớp đầu ra làm gì,

nó đã liên kết với nó,

vậy các tham số w_[2] và b_[2].

Vì vậy, w_[2] trong trường hợp này sẽ là ma trận một nhân bốn,

và b_[2] chỉ là một số thực lần lượt.

Vì vậy, z_[2] sẽ là một số thực mà chúng ta sẽ viết dưới dạng ma trận từng cái một.

Sẽ là một nhân bốn vật nhân a là bốn nhân một,

cộng b_[2] từng cái một,

vì vậy đây chỉ là một con số thực.

Nếu bạn nghĩ đơn vị phía trên cuối cùng này chỉ là

tương tự như hồi quy logistic có tham số w và b,

w thực sự đóng một vai trò tương tự như w_[2] hoán vị,

hoặc w_[2] thực sự là W chuyển vị và b bằng b_[2].

Tôi đã nói là chúng ta muốn che đậy phần bên trái của mạng lưới này và bỏ qua tất cả những điều đó vào lúc này,

thì đơn vị phía trên cuối cùng này rất giống với hồi quy logistic,

ngoại trừ việc thay vì viết các tham số là w và b,

chúng ta đang viết chúng dưới dạng w_[2] và b_[2],

với kích thước một x bốn và một x một.

Vì vậy, chỉ là một bản tóm tắt.

Đối với hồi quy logistic, để triển khai đầu ra hoặc triển khai dự đoán,

bạn tính z bằng w hoán vị x cộng b,

và mũ a hoặc y bằng a,

bằng sigmoid của z.

Khi bạn có một mạng lưới thần kinh với một lớp ẩn,

những gì bạn cần thực hiện,

đối với máy tính kết quả này chỉ là bốn phương trình này.

Bạn có thể coi đây là một triển khai điện toán được vector hóa

đầu ra của những cái đầu tiên này cho các đơn vị hồi quy logistic trong lớp ẩn,

đó là những gì nó làm, và

sau đó, hồi quy logistic này ở lớp đầu ra chính là tác dụng của nó.

Tôi hy vọng mô tả này có ý nghĩa,

nhưng bài học rút ra là tính toán đầu ra của mạng lưới thần kinh này,

tất cả những gì bạn cần là bốn dòng mã đó.

Bây giờ, bạn đã thấy cách cung cấp một tính năng đầu vào duy nhất,

vector a, bạn có thể làm được với bốn dòng mã,

tính toán đầu ra của mạng lưới thần kinh này.

Tương tự như những gì chúng tôi đã làm cho hồi quy logistic,

chúng tôi cũng muốn vector hóa nhiều ví dụ đào tạo.

Chúng ta sẽ thấy điều đó bằng cách xếp chồng các ví dụ huấn luyện vào các cột khác nhau trong ma trận,

chỉ cần sửa đổi một chút cho điều này, bạn cũng vậy,

tương tự như những gì bạn thấy trong hồi quy này,

có thể tính toán đầu ra của mạng lưới thần kinh này,

không chỉ một ví dụ tại một thời điểm,

kéo dài thời gian của bạn, chẳng hạn như toàn bộ tập luyện của bạn cùng một lúc.

Vì vậy, chúng ta hãy xem chi tiết về điều đó trong video tiếp theo.