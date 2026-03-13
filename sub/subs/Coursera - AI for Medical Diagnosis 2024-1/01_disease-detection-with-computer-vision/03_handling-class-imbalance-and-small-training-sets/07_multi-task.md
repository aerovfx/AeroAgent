# 07 đa nhiệm

---

Hãy trò chuyện về chuyện khác

thách thức mà chúng tôi

gặp phải trong y tế

cài đặt phân loại hình ảnh,

đó là thách thức đa nhiệm.

Cho đến nay, chúng tôi đã xem xét

ở phân loại nhị phân,

nơi chúng tôi quan tâm

phân loại liệu

một ví dụ là một

khối lượng hay không phải khối lượng.

Tuy nhiên, trong thế giới thực,

chúng tôi quan tâm đến việc phân loại

sự hiện diện hoặc

không có nhiều bệnh như vậy.

Bây giờ, một cách đơn giản để làm điều này,

là có những mô hình mà mỗi

học một trong những nhiệm vụ này.

Tuy nhiên, có lẽ chúng ta có thể học cách

làm tất cả các nhiệm vụ

sử dụng một mô hình.

Một lợi thế của điều này

là chúng ta có thể học

những đặc điểm chung cho

xác định thêm

hơn một căn bệnh,

cho phép chúng tôi sử dụng hiện có của chúng tôi

dữ liệu hiệu quả hơn.

Đây là thiết lập của

học tập đa nhiệm.

Hãy xem làm thế nào chúng ta có thể

huấn luyện thuật toán để

tìm hiểu tất cả những nhiệm vụ này

cùng một lúc.

Vì vậy, thay vì các ví dụ

có một nhãn,

bây giờ họ có một nhãn cho

mọi bệnh tật ở

ví dụ ở đâu

số 0 biểu thị sự vắng mặt của

căn bệnh đó và một

biểu thị sự hiện diện

của căn bệnh đó.

Đối với điều đầu tiên, chúng tôi

không có khối lượng,

sự hiện diện của bệnh viêm phổi và

sự vắng mặt của một bệnh khác,

phù nề, dư thừa

chất lỏng trong phổi.

Thay vì có một

đầu ra từ mô hình,

mô hình hiện có ba

đầu ra khác nhau

biểu thị xác suất của

ba căn bệnh khác nhau.

Để huấn luyện một thuật toán như vậy,

chúng ta cũng cần phải thực hiện

việc sửa đổi để

hàm mất mát từ

các nhiệm vụ nhị phân để

cài đặt đa nhiệm.

Hãy xem làm thế nào chúng ta có thể làm điều đó.