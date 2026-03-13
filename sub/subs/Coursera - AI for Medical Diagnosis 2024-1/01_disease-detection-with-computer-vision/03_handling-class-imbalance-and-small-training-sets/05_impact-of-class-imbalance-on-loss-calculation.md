# 05 tác động của tính toán mất cân bằng lớp

---

Chúng ta đã thấy sự mất mát như thế nào

áp dụng cho một ví dụ duy nhất

Hãy xem nó áp dụng như thế nào

đến một loạt các ví dụ.

Ở đây chúng tôi có sáu ví dụ

điều đó là bình thường,

và hai ví dụ có khối lượng.

Lưu ý rằng P2, P3,

P4 ở đây là ID bệnh nhân.

Khi việc huấn luyện chưa bắt đầu,

giả sử thuật toán tạo ra

xác suất đầu ra là 0,5

cho tất cả các ví dụ,

sự mất mát sau đó có thể được tính toán

cho mỗi ví dụ.

Đối với một ví dụ bình thường,

chúng ta sẽ sử dụng tiêu cực

log của 1 trừ 0,5,

điều đó sẽ xảy ra

đi ra đến 0,3.

Đối với một ví dụ đại chúng,

chúng ta sẽ sử dụng

nhật ký âm 0,5,

điều đó cũng đang diễn ra

để đi đến 0,3.

Tổng đóng góp vào

sự mất mát từ các ví dụ đại chúng,

tăng lên 0,3 lần

2 là 0,6.

Trong khi tổng thiệt hại

từ ví dụ bình thường,

tăng gấp 0,3 lần

6 ví dụ bình thường, đó là 1,8.

Vì vậy hãy chú ý xem hầu hết

sự đóng góp cho

sự mất mát đến từ

những ví dụ bình thường,

chứ không phải từ

những ví dụ đại chúng.

Vì vậy thuật toán đang tối ưu hóa

bản cập nhật của nó để có được

những ví dụ bình thường,

và không cho nhiều người thân

trọng lượng cho các ví dụ đại chúng.

Trong thực tế, điều này không

tạo ra một bộ phân loại rất tốt.

Đây là lớp học

vấn đề mất cân bằng.

Giải pháp cho

vấn đề mất cân bằng lớp

là sửa đổi hàm mất mát,

để cân nặng bình thường và

các lớp đại chúng khác nhau.

Wp sẽ là trọng lượng chúng tôi chỉ định

theo hướng tích cực hoặc để

những ví dụ đại chúng,

và wn về phía tiêu cực

hoặc những ví dụ thông thường.

Hãy xem điều gì xảy ra khi chúng ta

trọng lượng tích cực

ví dụ nhiều hơn nữa.

Chúng tôi muốn cân nhắc

ví dụ đại chúng hơn,

để họ có thể có

đóng góp bình đẳng

nói chung là thua lỗ,

như những ví dụ bình thường.

Hãy chọn sáu trên tám vì

sức nặng chúng ta đang mang

những ví dụ đại chúng,

và hai trên tám

như trọng lượng chúng tôi

có trên các ví dụ bình thường.

Sau đó, bạn có thể thấy rằng nếu bạn tính tổng

tăng tổng số tổn thất từ

ví dụ đại chúng,

chúng ta nhận được 0,45, và đây là

bằng tổng thiệt hại từ

các ví dụ bình thường ở đây.

Trong trường hợp tổng quát,

trọng lượng chúng ta sẽ đặt lên

lớp tích cực sẽ là

số lượng ví dụ tiêu cực

trên tổng số

số ví dụ.

Trong trường hợp của chúng tôi, đây là

sáu ví dụ bình thường

tổng cộng hơn tám ví dụ.

Trọng lượng chúng tôi sẽ đặt

trên lớp tiêu cực

sẽ là số lượng

những ví dụ tích cực về

tổng số ví dụ,

tức là hai trên tám.

Với cài đặt này của wp và wn,

chúng ta có thể có tất cả

trong số các ví dụ cho

khoản đóng góp tổn thất từ

tích cực và tiêu cực

lớp phải giống nhau.

Vì vậy, đây là ý tưởng sửa đổi

giảm cân khi sử dụng tạ,

trong phương pháp này đó là

gọi là giảm cân,

để giải quyết lớp học

vấn đề mất cân bằng.