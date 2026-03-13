# 11 khởi tạo ngẫu nhiên

---

Khi bạn thay đổi mạng lưới thần kinh của mình,

điều quan trọng là phải khởi tạo

trọng số một cách ngẫu nhiên.

Đối với hồi quy logistic thì không sao

để khởi tạo trọng số về 0.

Nhưng đối với một mạng lưới thần kinh khởi tạo

trọng số cho các tham số đều bằng 0 và

sau đó áp dụng giảm độ dốc,

nó sẽ không hoạt động.

Hãy xem tại sao.

Vì vậy, bạn có ở đây hai tính năng đầu vào, vì vậy

n0=2, và hai đơn vị ẩn, nên n1=2.

Và do đó ma trận liên kết

với lớp ẩn,

w 1, sẽ là hai nhân hai.

Giả sử bạn khởi tạo nó thành

tất cả đều là 0, nên 0 0 0 0, ma trận hai nhân hai.

Và giả sử B1 cũng bằng 0 0.

Hóa ra việc khởi tạo độ lệch

số hạng b đến 0 thực ra là được,

nhưng việc khởi tạo w thành tất cả số 0 là một vấn đề.

Vì vậy vấn đề với điều này

chính thức hóa là dành cho

bất kỳ ví dụ nào bạn đưa ra,

bạn sẽ có a1,1 đó và

a1,2 sẽ bằng nhau phải không?

Vì vậy việc kích hoạt này và

lần kích hoạt này sẽ giống nhau,

bởi vì cả hai đơn vị ẩn này

đang tính toán chính xác chức năng tương tự.

Và sau đó,

khi bạn tính toán lan truyền ngược,

hóa ra là dz11 và

dz12 cũng sẽ như vậy

được tô màu bởi sự đối xứng, phải không?

Cả hai đơn vị ẩn này

sẽ khởi tạo theo cách tương tự.

Về mặt kỹ thuật, theo những gì tôi đang nói,

Tôi giả định rằng trọng lượng gửi đi hoặc

cũng giống hệt nhau.

Vậy đó là w2 bằng 0 0.

Nhưng nếu bạn khởi tạo

mạng lưới thần kinh theo cách này,

sau đó đơn vị ẩn này và

đơn vị ẩn này hoàn toàn giống nhau.

Đôi khi bạn nói họ

hoàn toàn đối xứng,

điều đó chỉ có nghĩa là họ

hoàn thành chính xác chức năng tương tự.

Và bằng một cách chứng minh bằng quy nạp,

hóa ra là sau mỗi lần

lặp đi lặp lại việc đào tạo hai bạn ẩn

các đơn vị vẫn đang tính toán

chính xác cùng một chức năng.

Vì đồ thị sẽ chỉ ra rằng dw sẽ

là một ma trận trông như thế này.

Trong đó mỗi hàng có cùng một giá trị.

Vì vậy, chúng tôi thực hiện cập nhật trọng lượng.

Vì vậy, khi bạn thực hiện cập nhật cân nặng,

w1 được cập nhật dưới dạng w1- alpha nhân dw.

Bạn thấy rằng w1, sau mỗi lần lặp,

sẽ có hàng đầu tiên

bằng hàng thứ hai.

Vì vậy có thể xây dựng

một bằng chứng bằng quy nạp rằng nếu bạn

khởi tạo mọi cách,

tất cả các giá trị của w đến 0,

sau đó bởi vì cả hai đơn vị ẩn đều bắt đầu

tắt tính toán chức năng tương tự.

Và cả hai đơn vị ẩn đều có

ảnh hưởng tương tự đến đơn vị đầu ra,

sau đó sau một lần lặp,

câu nói đó vẫn đúng,

hai đơn vị ẩn vẫn đối xứng.

Và do đó, bằng quy nạp, sau hai

lần lặp, ba lần lặp, v.v.,

bất kể bạn bao lâu

đào tạo mạng lưới thần kinh của bạn,

cả hai đơn vị ẩn vẫn còn

tính toán chính xác chức năng tương tự.

Và trong trường hợp này, thực sự không có

chỉ ra việc có nhiều hơn một đơn vị ẩn.

Bởi vì họ đều là

tính toán điều tương tự.

Và tất nhiên, đối với các mạng lưới thần kinh lớn hơn,

hãy nói về ba tính năng và

có thể có một số lượng rất lớn các đơn vị ẩn,

một lập luận tương tự có tác dụng chứng tỏ rằng

với một mạng lưới thần kinh như thế này.

Hãy để tôi vẽ tất cả các cạnh,

nếu bạn khởi tạo trọng số bằng 0,

sau đó tất cả những điều ẩn giấu của bạn

đơn vị là đối xứng.

Và dù có bao lâu đi chăng nữa

bạn đang nâng cấp trung tâm,

tất cả tiếp tục tính toán

chính xác cùng một chức năng.

Vì vậy, điều đó không hữu ích,

bởi vì bạn muốn sự khác biệt

đơn vị ẩn để tính toán

chức năng khác nhau.

Giải pháp cho vấn đề này là

khởi tạo các tham số của bạn một cách ngẫu nhiên.

Vì vậy đây là những gì bạn làm.

Bạn có thể đặt w1 = np.random.randn.

Điều này tạo ra một gaussian

biến ngẫu nhiên (2,2).

Và thông thường, bạn nhân số này

với số lượng rất nhỏ, chẳng hạn như 0,01.

Vì vậy, bạn khởi tạo nó thành

giá trị ngẫu nhiên rất nhỏ.

Và sau đó b, hóa ra b

không có vấn đề đối xứng,

cái gọi là sự đối xứng

vấn đề phá vỡ.

Vì vậy, khởi tạo là được

b chỉ còn số không.

Bởi vì vậy

miễn là w được khởi tạo ngẫu nhiên,

bạn bắt đầu với những điều ẩn khác

các đơn vị tính toán những thứ khác nhau.

Và thế là bạn không còn có thứ này nữa

vấn đề phá vỡ đối xứng.

Và tương tự, với w2,

bạn sẽ khởi tạo nó một cách ngẫu nhiên.

Và b2, bạn có thể khởi tạo nó thành 0.

Vì vậy, bạn có thể tự hỏi, điều này đã xảy ra ở đâu

hằng số đến từ đâu và tại sao nó lại là 0,01?

Tại sao không đặt số 100 hoặc 1000?

Hóa ra chúng ta thường

thích khởi tạo hơn

trọng số thành các giá trị ngẫu nhiên rất nhỏ.

Bởi vì nếu bạn đang sử dụng tanh hoặc

chức năng kích hoạt sigmoid, hoặc

sigmoid khác,

thậm chí chỉ ở lớp đầu ra.

Nếu trọng lượng quá lớn,

sau đó khi bạn tính toán

các giá trị kích hoạt,

hãy nhớ rằng z[1]=w1 x + b.

Và sau đó a1 là kích hoạt

hàm áp dụng cho z1.

Vì vậy, nếu w rất lớn,

z sẽ rất, hoặc ít nhất là một số

giá trị của z sẽ rất lớn hoặc

rất nhỏ.

Và trong trường hợp đó, nhiều khả năng bạn

để kết thúc ở những phần mỡ của tanh

hàm hoặc hàm sigmoid, trong đó

độ dốc hoặc độ dốc rất nhỏ.

Ý nghĩa độ dốc đó

xuống dốc sẽ rất chậm.

Vì thế việc học rất chậm.

Vì vậy, chỉ là tóm tắt lại, nếu w quá lớn,

bạn có nhiều khả năng kết thúc

ngay cả khi bắt đầu đào tạo,

với giá trị z rất lớn.

Điều gì gây ra tanh hoặc sigmoid của bạn

chức năng kích hoạt được bão hòa,

do đó làm chậm quá trình học tập.

Nếu bạn không có bất kỳ sigmoid hoặc

tanh chức năng kích hoạt xuyên suốt của bạn

mạng lưới thần kinh, đây không còn là vấn đề nữa.

Nhưng nếu bạn đang phân loại nhị phân,

và đơn vị đầu ra của bạn là sigmoid

hoạt động, thì bạn chỉ không muốn

tham số ban đầu quá lớn.

Vì vậy, đó là lý do tại sao nhân với 0,01 sẽ

là một cái gì đó hợp lý để thử, hoặc

số nhỏ nào khác.

Và w2 cũng vậy phải không?

Đây có thể là ngẫu nhiên.ngẫu nhiên.

Tôi đoán đây sẽ là 1 x 2

trong ví dụ này, nhân với 0,01.

Thiếu chữ s đó.

Vì vậy, cuối cùng, hóa ra đôi khi

chúng có thể là hằng số tốt hơn 0,01.

Khi bạn đang huấn luyện một nơ-ron

mạng chỉ có một lớp ẩn,

nó là một mạng lưới thần kinh tương đối nông,

không có quá nhiều lớp ẩn.

Đặt nó thành 0,01 có thể sẽ hoạt động tốt.

Nhưng khi bạn đang tập luyện rất

mạng lưới thần kinh rất sâu,

thì bạn có thể muốn chọn

một hằng số khác 0,01.

Và trong tài liệu của tuần tới,

chúng ta sẽ nói một chút về cách thức và

khi nào bạn có thể muốn chọn

một hằng số khác 0,01.

Nhưng dù thế nào đi nữa, nó thường sẽ kết thúc

lên là một con số tương đối nhỏ.

Vậy là xong video của tuần này.

Bây giờ bạn đã biết cách thiết lập một nơ-ron

mạng của một lớp ẩn,

khởi tạo các tham số,

đưa ra dự đoán bằng cách sử dụng

Đồng thời tính đạo hàm và

thực hiện giảm độ dốc,

sử dụng backprop.

Vì vậy,

bạn sẽ có thể làm được các câu đố,

cũng như tuần này

bài tập lập trình.

Chúc may mắn với điều đó.

Tôi hy vọng bạn vui vẻ với

bài tập giải quyết vấn đề và

mong được gặp bạn

trong tài liệu tuần 4.