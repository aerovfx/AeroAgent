# 07 tại sao bạn cần chức năng kích hoạt phi tuyến tính

---

Tại sao mạng nơ-ron cần

một hàm kích hoạt phi tuyến tính?

Hóa ra mạng lưới thần kinh của bạn

để tính toán các hàm thú vị,

bạn cần phải chọn một phi tuyến tính

chức năng kích hoạt, chúng ta hãy xem một.

Vì vậy, đây là bốn phương trình hỗ trợ cho

mạng lưới thần kinh.

Tại sao chúng ta không thoát khỏi điều này?

Loại bỏ chức năng g?

Và đặt a1 bằng z1.

Hoặc cách khác, bạn có thể nói rằng

g của z bằng z, được chứ?

Đôi khi điều này được gọi

hàm kích hoạt tuyến tính.

Có lẽ một cái tên hay hơn cho nó sẽ là

chức năng kích hoạt danh tính

bởi vì nó chỉ xuất ra

bất cứ điều gì đã được đầu vào.

Vì mục đích này,

Điều gì sẽ xảy ra nếu a(2) bằng z(2)?

Hóa ra nếu bạn làm điều này,

thì mô hình này chỉ tính toán y hoặc

y-hat là hàm tuyến tính

các tính năng đầu vào của bạn,

x, để lấy hai phương trình đầu tiên.

Nếu bạn có điều đó (1)

= Z(1) = W(1)x + b, và

thì a(2) = z (2) =

W(2)a(1) + b.

Sau đó, nếu bạn lấy định nghĩa này của a1 và

cắm nó vào đó bạn sẽ thấy a2 =

w2(w1x + b1), hãy di chuyển nó lên một chút.

Phải?

Vậy đây là a1 + b2, và vì vậy

điều này đơn giản hóa thành:

(W2w1)x +

(w2b1 + b2).

Vậy đây chỉ là,

hãy gọi đây là w prime b prime.

Vì vậy, cái này chỉ bằng w' x + b'.

Nếu bạn sử dụng tuyến tính

chức năng kích hoạt hoặc

chúng ta cũng có thể gọi chúng là danh tính

chức năng kích hoạt,

sau đó mạng lưới thần kinh chỉ xuất ra

hàm tuyến tính của đầu vào.

Và chúng ta sẽ nói về mạng sâu sau,

mạng lưới thần kinh có nhiều, nhiều lớp,

nhiều lớp ẩn. Và hóa ra là

nếu bạn sử dụng hàm kích hoạt tuyến tính hoặc

cách khác,

nếu bạn không có chức năng kích hoạt,

thì cho dù thần kinh của bạn có bao nhiêu lớp

mạng có, tất cả những gì nó làm chỉ là

tính toán hàm kích hoạt tuyến tính.

Vì vậy bạn có thể không

có bất kỳ lớp ẩn nào.

Một số trường hợp được tóm tắt ngắn gọn

đã đề cập, hóa ra là nếu bạn có

một hàm kích hoạt tuyến tính ở đây và một

hàm sigmoid ở đây thì mô hình này là

không biểu cảm hơn logistic tiêu chuẩn

hồi quy mà không có bất kỳ lớp ẩn nào.

Vì vậy tôi sẽ không buồn chứng minh điều đó, nhưng

bạn có thể thử làm như vậy nếu bạn muốn.

Nhưng điều rút ra được là tuyến tính

lớp ẩn ít nhiều vô dụng

bởi vì thành phần của hai tuyến tính

bản thân các hàm là một hàm tuyến tính.

Vì vậy, trừ khi bạn ném một mục phi tuyến tính

trong đó thì bạn sẽ không tính toán thêm nữa

chức năng thú vị ngay cả khi bạn

đi sâu hơn vào mạng lưới.

Chỉ có một nơi mà bạn có thể

sử dụng hàm kích hoạt tuyến tính.

g(x) = z.

Và đó là nếu bạn đang làm máy

học về bài toán hồi quy.

Vậy nếu y là số thực.

Vì vậy, ví dụ, nếu bạn đang cố gắng

để dự đoán giá nhà.

Vậy y không phải là 0, 1, mà là số thực

số điện thoại, từ đâu đó - tôi không biết -

Tuy nhiên, $0 là giá nhà

đắt tiền, phải, nhà có được, tôi đoán vậy.

Có lẽ những ngôi nhà có thể có khả năng

hàng triệu đô la, vậy

tuy nhiên chi phí của ngôi nhà trong tập dữ liệu của bạn là bao nhiêu.

Nhưng nếu y nhận những giá trị thực này,

thì có thể sẽ ổn thôi nếu có

một hàm kích hoạt tuyến tính ở đây

rằng mũ y đầu ra của bạn cũng là

một số thực đi bất cứ đâu từ

trừ vô cực đến cộng vô cùng.

Nhưng sau đó các đơn vị ẩn sẽ

không sử dụng các chức năng kích hoạt.

Họ có thể sử dụng ReLU hoặc tanh hoặc

ReLU bị rò rỉ hoặc có thể là thứ gì khác.

Vì vậy, một nơi bạn có thể sử dụng

hàm kích hoạt tuyến tính

thường ở lớp đầu ra.

Nhưng ngoài ra, việc sử dụng tuyến tính

chức năng kích hoạt trong lớp ẩn

ngoại trừ một số trường hợp rất đặc biệt

liên quan đến việc nén mà chúng tôi đang

sẽ nói về việc sử dụng tuyến tính

chức năng kích hoạt là cực kỳ hiếm.

Và tất nhiên, nếu chúng ta

thực tế là dự đoán giá nhà đất,

như bạn đã thấy trong video tuần thứ nhất, bởi vì

giá nhà đất đều không âm,

Có lẽ thậm chí sau đó bạn có thể sử dụng

một hàm kích hoạt giá trị nên

rằng tất cả mũ y đầu ra của bạn đều là

lớn hơn hoặc bằng 0.

Vì vậy tôi hy vọng điều đó mang lại cho bạn cảm giác

tại sao có kích hoạt phi tuyến tính

chức năng là rất quan trọng

một phần của mạng lưới thần kinh.

Tiếp theo chúng ta sẽ bắt đầu

nói về việc giảm độ dốc và

làm điều đó để thiết lập cho

cuộc thảo luận của chúng ta về việc giảm độ dốc,

trong video tiếp theo tôi muốn chỉ cho bạn cách

ước tính-cách tính-độ dốc hoặc

đạo hàm của cá nhân

các chức năng kích hoạt.

Vậy chúng ta hãy chuyển sang video tiếp theo.