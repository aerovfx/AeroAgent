# 04 hàm mất entropy chéo nhị phân

---

Điều này tạo ra một vấn đề cho

thuật toán học tập

sẽ nắm bắt chủ yếu

những ví dụ bình thường.

Điều này mang lại một mô hình

điều đó bắt đầu dự đoán

xác suất rất thấp

bệnh tật cho

tất cả mọi người và sẽ không thể

xác định khi nào một

Ví dụ có một căn bệnh.

Hãy xem chúng ta có thể làm thế nào

theo dõi vấn đề này để

hàm mất mát mà chúng ta

dùng để huấn luyện thuật toán.

Chúng ta cũng sẽ xem cách chúng ta có thể sửa đổi

hàm mất mát này trong

sự hiện diện của dữ liệu mất cân bằng.

Sự mất mát ở đây được gọi là

entropy chéo nhị phân

mất mát và điều này

đo lường hiệu suất của

một sự phân loại

mô hình có đầu ra là

giữa số không và

một. Hãy nhìn vào

một ví dụ để xem điều này như thế nào

hàm mất mát đánh giá.

Ở đây chúng ta có một ví dụ về

chụp X-quang ngực đó

chứa một khối lượng,

vì vậy nó được dán nhãn với

một và thuật toán

cho ra xác suất là 0,2.

Bây giờ, 0,2 ở đây

là xác suất

theo thuật toán

của Y bằng 1,

xác suất đó

ví dụ này là một khối lượng.

Vì vậy bây giờ chúng ta có thể áp dụng

hàm mất mát để tính toán

sự mất mát trong ví dụ này.

Bây giờ hãy chú ý rằng nhãn của chúng tôi là một,

vì vậy chúng tôi sẽ

sử dụng thuật ngữ đầu tiên.

Sự mất mát của chúng tôi là âm

log và sau đó chúng tôi

sẽ lấy

đầu ra thuật toán, 0,2.

Vì vậy, điều này đánh giá là 0,70.

Vậy đây là sự mất mát

thuật toán đó

lấy ví dụ cụ thể này.

Hãy xem một ví dụ khác.

Lần này là một ví dụ không có mặt nạ,

sẽ có nhãn bằng không.

Đầu ra thuật toán của chúng tôi

xác suất là 0,7.

Bây giờ, lần này chúng ta sẽ sử dụng

thời hạn này của tỷ lệ tổn thất

ở đây vì Y bằng 0.

Vậy bây giờ sự mất mát sẽ là

nhật ký phủ định của thuật ngữ

PY bằng 0 cho X.

Chúng ta có thể nhận được PY bằng 0 cho X

sử dụng P của Y bằng 1 cho X.

Cách chúng ta có thể tính toán

số lượng này từ

cái đó là bằng cách nhận ra điều đó

xác suất đó

một ví dụ là số không

là 1 trừ

xác suất đó là 1.

Một ví dụ về khối lượng hoặc không.

Vì vậy, thuật toán nói

xác suất 70 phần trăm

rằng thứ gì đó có khối lượng,

sau đó có 30 phần trăm

có lẽ là không.

Vì vậy, ở đây chúng ta sẽ

cắm 1 trừ 0,7,

điều đó sẽ xảy ra

đi đến 0,3 và

biểu hiện này

đánh giá là 0,52.