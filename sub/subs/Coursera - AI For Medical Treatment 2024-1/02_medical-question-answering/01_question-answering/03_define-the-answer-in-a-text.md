# 03 xác định câu trả lời trong văn bản

---

Như chúng ta đã thấy trước đây đối với

nhiệm vụ trả lời câu hỏi,

đầu vào sẽ là

câu hỏi và đoạn văn,

và đầu ra sẽ

là câu trả lời cho

câu hỏi đó là một

đoạn của đoạn văn.

Ở đây giảm máu

mức glucose có thể

được tìm thấy trong

lối đi ngay tại đây.

Chúng ta có thể biểu thị câu trả lời bằng cách sử dụng

sự bắt đầu và kết thúc

lời của câu trả lời.

Vì vậy việc giảm lượng đường trong máu có

từ bắt đầu 'giảm'

và từ cuối cùng 'cấp độ'.

Giảm là từ thứ 11

nếu chúng ta bắt đầu đếm

trong đoạn văn,

và cấp độ là từ thứ 14

trong đoạn văn nếu chúng ta

tính từ đầu.

Vì vậy quay trở lại

các từ biểu diễn

BERT học,

Nhiệm vụ của mô hình là

có thể xác định

liệu mỗi từ trong

đoạn văn là một trong

sự bắt đầu hoặc kết thúc của

một câu trả lời cho một câu hỏi

Đây là cách người mẫu học cách

xác định xem một từ có phải là

có thể là sự khởi đầu hoặc

từ kết thúc cho một câu trả lời.

Mô hình học hai vectơ,

S và E cho mỗi

cách biểu diễn từ,

cho mỗi từ

trong đoạn văn.

Biểu hiện của từ là

nhân với S để

lấy một số duy nhất,

đó là sự khởi đầu

chấm điểm cho từ đó.

Điểm đầu càng cao thì

thì càng có nhiều khả năng là như vậy

sự bắt đầu của câu trả lời.

Ví dụ, từ

'giảm' là nhiều hơn

có khả năng là sự khởi đầu của

câu trả lời hơn là từ 'máu'.

Tương tự, đối với mỗi

các từ biểu diễn,

sự đại diện của từ

được nhân với

vectơ E để có được

một số vô hướng khác,

đó là điểm cuối cùng.

Điểm cuối cùng càng cao,

từ đó càng có nhiều khả năng

là sự kết thúc của một câu trả lời.

Ví dụ: từ 'cấp độ'

có nhiều khả năng là sự kết thúc của

một câu trả lời hơn là từ 'by'.

Sử dụng phần đầu và phần cuối

tính điểm cho mỗi từ,

chúng ta có thể tìm hiểu những gì

câu trả lời rất có thể là.

Chúng tôi làm điều này bằng cách tính toán

một mạng lưới các từ.

Trong lưới này, chúng tôi nhập vào

điểm bắt đầu này cộng với điểm kết thúc

ghi điểm trong mỗi ô,

điểm khởi đầu

đến từ các hàng,

và điểm cuối cùng

đến từ cột.

Ví dụ, để tính toán

số điểm mà câu trả lời

bắt đầu bằng máu và

kết thúc bằng glucose,

chúng tôi sẽ điền vào đây

tế bào và chúng tôi sẽ

có được điểm khởi đầu này

từ máu, đó là 0,1,

và thêm nó vào cuối

ghi điểm từ glucose,

ở đây lại là 0,1,

để giúp chúng tôi ghi điểm

trong ô 0,2.

Do đó chúng ta có thể tính được điểm

cho tất cả các mục trong lưới.

Chúng ta có thể ép buộc từ cuối

xuất hiện không sớm hơn

từ bắt đầu chỉ bằng cách tính toán

điểm số ở phần trên này

vùng hình tam giác.

Hãy nhớ rằng nếu chúng ta muốn ở đây,

thì chúng ta đang nói rằng

sự bắt đầu sẽ ở sau sự kết thúc,

điều đó là không thể.

Do đó, mô hình xuất ra

sự bắt đầu và kết thúc

từ tương ứng với

điểm cao nhất ở đây.

Điểm cao nhất ở đây là 8,2,

bắt đầu bằng 'reduce'

và kết thúc với các cấp độ.

Vì vậy, chúng tôi có đầu ra mô hình

'giảm' khi bắt đầu

câu trả lời ở mã thông báo 11,

và 'cấp độ' là kết thúc của

câu trả lời ở mã thông báo 14.

Người mẫu tìm hiểu

vectơ S và E và cập nhật

cách biểu diễn từ của nó dựa trên

được chiếu nhiều

của những câu hỏi này,

đoạn văn và trả lời bộ ba.

Thông thường, mô hình

lần đầu tiên được hiển thị

câu hỏi tự nhiên và

câu trả lời bằng tiếng anh trong

miền chung sử dụng

các bộ dữ liệu như SQuAD và

sau đó tinh chỉnh về y tế

bộ dữ liệu như BioASQ.