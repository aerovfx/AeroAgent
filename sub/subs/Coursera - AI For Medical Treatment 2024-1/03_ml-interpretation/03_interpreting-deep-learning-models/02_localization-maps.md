# 02 bản đồ định vị

---

Vì vậy bây giờ chúng ta đã thấy cách chúng ta có thể

lấy bản đồ không gian từ

đầu ra của cuối cùng

lớp chập

khi hình ảnh được truyền vào.

Các bản đồ không gian này được

thường nhỏ hơn nhiều

có kích thước lớn hơn đầu vào,

thường là từ 7

vào 7 và 14 vào 14,

thay đổi tùy theo

đến sự lựa chọn của

kiến trúc và

kích thước đầu vào của chúng tôi.

Chiều thứ ba ở đây là

số lượng bản đồ không gian

được xuất ra bởi

lớp cuối cùng,

khác nhau dựa trên

về kiến trúc.

Vì vậy, chúng tôi chỉ sử dụng k ở đây.

Bây giờ hãy xem chúng ta có thể đi như thế nào

từ k bản đồ không gian này của

kích thước 10 x 10 đến nhiệt

bản đồ trên toàn bộ hình ảnh.

Hãy giải nén những bản đồ không gian này.

Vì vậy, chúng ta có thể đại diện

mỗi ô vuông ở đây

như một bản đồ không gian đi từ A_1,

A_2, sang A_k để biểu thị

bản đồ không gian k.

Bây giờ, điều chúng ta sắp làm là

chúng ta sẽ cân từng cái

của những bản đồ này với một

trọng lượng cho bởi a,

và sau đó cộng tất cả những thứ đó lại để có được

bản đồ định vị,

L, đối với bệnh tim to.

Chúng ta có thể viết cái này

xuống về mặt toán học

với L, bản đồ định vị,

là tổng trên k của trọng lượng,

k, nhân bản đồ, A_k.

a_k ở đây cho chúng ta biết ảnh hưởng

của từng bản đồ không gian trên

bản đồ định vị.

Câu hỏi tiếp theo

đối với chúng tôi là cách chúng tôi

tính toán các trọng số này, a_k.

Đầu tiên chúng ta cần

hiểu ảnh hưởng.

Hãy nói rằng chúng tôi muốn

biết tác dụng của

mỗi tính năng trong A_1

bản đồ không gian trên đầu ra.

A_1 có 49 tính năng,

bảy hàng, bảy cột,

và chúng tôi sẽ sử dụng Z để đại diện

số lượng các tính năng,

số phần tử trong A_1.

Hãy để y đại diện cho

điểm đầu ra của

mạng lưới tim mạch lớn

ngay trước khi

kích hoạt sigmoid.

Bây giờ chúng ta có thể tính toán

ảnh hưởng của mỗi

của những đặc điểm này trong

bản đồ không gian trên

y bằng cách tính toán

đạo hàm riêng của

y đối với

mỗi tính năng trong A_1,

và điều này cho chúng ta ảnh hưởng

của từng tính năng trên đầu ra.

Điều này cung cấp cho chúng tôi một ma trận cho chúng tôi biết

ảnh hưởng của mỗi

tính năng trên đầu ra.

Ở đây, đặc điểm ở vị trí 2,2

đang có điều tích cực nhất

ảnh hưởng đến đầu ra,

bởi vì con số này là

cao nhất trong mọi con số.

Ít nhất là những cái

chúng ta có thể thấy ở đây

Tính năng tại

vị trí 1,2 đang có

tiêu cực lớn nhất

ảnh hưởng đến

đầu ra của những thứ này,

ví dụ, các giá trị.

Chúng ta có thể có được ảnh hưởng trung bình

của bản đồ không gian

A_1 trên đầu ra

bằng cách lấy trung bình

của tính năng

ảnh hưởng ở mỗi

của những vị trí này.

Về mặt hình thức, chúng tôi thực hiện việc này bằng cách

lấy tổng của i và j,

thế là chuyện này đã kết thúc

hàng và cột của

các giá trị riêng lẻ tại

từng vị trí này.

Sau đó lấy mức trung bình của họ,

chúng ta làm 1 chia cho

số phần tử trong A_1.

Bằng cách này chúng ta có được

ảnh hưởng trung bình

của A_1 ở đầu ra.

Ảnh hưởng trung bình

sau đó có thể được sử dụng như

trọng lượng chúng tôi đang tìm kiếm

đối với bản đồ không gian,

a của k trong tính toán

bản đồ định vị.

Như vậy bây giờ chúng ta có

biểu hiện đầy đủ

cho việc tính toán

bản đồ định vị dọc theo

với a của k đến từ đâu.