# 02 phân đoạn

---

Sau khi hình ảnh đã được đăng ký, chúng ta

có thể kết hợp các trình tự khác nhau.

Chúng tôi đã thấy cách chúng tôi có thể áp dụng điều này

kỹ thuật vào một lát não.

Ý tưởng tương tự có thể được mở rộng mà không cần

phức tạp hơn nữa cho tất cả các lát.

Bây giờ có một tập

với nhiều kênh

có thông tin kết hợp

gồm nhiều trình tự khác nhau.

Bây giờ chúng ta đã thấy cách chúng ta

có thể biểu diễn dữ liệu MRI,

chúng ta hãy chuyển sang nhiệm vụ của

phân đoạn khối u não.

Phân đoạn là quá trình xác định

ranh giới của các mô khác nhau.

Trong trường hợp này, chúng tôi đang cố gắng

xác định ranh giới của khối u.

Chúng ta cũng có thể coi phân đoạn là

nhiệm vụ xác định lớp

của mọi điểm trong khối 3D.

Những điểm này trong không gian 2D được gọi là

pixel và trong không gian 3D được gọi là voxels.

Hãy thảo luận về hai cách tiếp cận

để phân đoạn với dữ liệu MRI.

Đầu tiên là cách tiếp cận 2D và

thứ hai là cách tiếp cận 3D.

Trong phương pháp 2D, chúng tôi chia nhỏ MRI 3D

khối lượng chúng tôi đã tích hợp thành nhiều lát cắt 2D.

Mỗi lát cắt này là

được chuyển vào mô hình phân đoạn

đưa ra phân đoạn cho

lát đó.

Từng lát một được đưa qua

mô hình phân đoạn theo cách này

để tạo ra một phân đoạn cho

mỗi lát.

Các lát 2D sau đó có thể được kết hợp

một lần nữa để tạo thành đầu ra 3D

khối lượng của phân đoạn.

Nhược điểm với điều này

Cách tiếp cận 2D là chúng tôi

có thể mất bối cảnh 3D quan trọng

khi sử dụng phương pháp này.

Ví dụ,

nếu có một khối u trong một lát cắt,

có khả năng có khối u ở

các lát ngay cạnh nó.

Vì chúng ta đang chuyển thành từng lát

lần lượt vào mạng,

mạng không thể

tìm hiểu bối cảnh hữu ích này.

Hãy xem chúng ta có thể giải quyết thế nào

điều này bằng cách tiếp cận 3D.

Theo cách tiếp cận 3D, lý tưởng nhất là

chúng tôi muốn chuyển toàn bộ khối lượng MRI

vào mô hình phân đoạn và thoát ra

bản đồ phân đoạn 3D cho toàn bộ MRI.

Tuy nhiên, kích thước của khối lượng MRI

làm cho nó không thể vượt qua được

tất cả cùng một lúc vào mô hình.

Đơn giản là nó sẽ chiếm quá nhiều bộ nhớ và

tính toán.

Vậy thay vào đó chúng ta có thể làm gì để vẫn có

người mẫu có thể hiểu được bối cảnh này

thông tin theo chiều sâu?

Trong phương pháp 3D, chúng tôi chia nhỏ mô hình 3D

Khối lượng MRI thành nhiều tiểu khối 3D.

Mỗi tập con này có chiều rộng nhất định,

bối cảnh chiều cao và chiều sâu.

Vì vậy, giống như cách tiếp cận 2D,

bây giờ chúng ta có thể nạp vào các tập nhỏ

lần lượt vào mô hình và

sau đó tổng hợp chúng ở cuối để tạo thành

một bản đồ phân đoạn cho toàn bộ tập.

Nhược điểm của phương pháp 3D này

là chúng ta vẫn có thể thua

bối cảnh không gian quan trọng.

Ví dụ,

nếu có một khối u trong một tiểu thể tích,

có khả năng có khối u ở

các subvolume xung quanh nó quá.

Vì chúng ta đang chuyển qua các tập nhỏ

lần lượt vào mạng,

mạng sẽ không thể

tìm hiểu bối cảnh có thể hữu ích này.

Lớp lót bạc với 3D

cách tiếp cận là chúng tôi đang nắm bắt

một số bối cảnh ở mọi chiều rộng,

kích thước chiều cao và chiều sâu.

Điều này bao gồm cách tiếp cận 3D để phân đoạn.