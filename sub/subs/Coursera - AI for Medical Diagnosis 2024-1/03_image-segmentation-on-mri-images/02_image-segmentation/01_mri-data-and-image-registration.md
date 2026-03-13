# 01 mri-data-and-image-đăng ký

---

Trong bài học rất thú vị này,

bạn sẽ học cách bạn

có thể đào tạo và đánh giá bạn

mô hình phân đoạn cho

xác định khối u trong dữ liệu MRI.

Bạn sẽ tìm hiểu về

Kiến trúc UNet và

quy trình mà chúng ta có thể sử dụng để

đào tạo thành công một

mô hình phân đoạn.

Như bạn sẽ nhanh chóng thấy,

làm việc với 3D

dữ liệu y tế cung cấp một số

những thách thức đáng kể

và bạn sẽ học

về một số sáng tạo

ý tưởng để giải quyết chúng.

Đầu tiên chúng ta sẽ bắt đầu bằng việc nói chuyện

về việc biểu diễn dữ liệu MRI.

Chúng tôi muốn có thể

đại diện cho dữ liệu MRI trong

một biểu mẫu mà chúng ta có thể nhập vào

vào mô hình phân đoạn.

Như bạn đã thấy, chúng tôi

Hình ảnh MRI không chỉ

một 2D duy nhất

hình ảnh như tia X,

và trình tự MRI là

một khối 3D được nhìn thấy ở đây

trong chế độ xem trục.

Hơn nữa, một ví dụ MRI sẽ

được tạo thành từ nhiều chuỗi,

và do đó sẽ bao gồm

của nhiều tập 3D.

Chúng ta sẽ xem xét cách chúng ta có thể kết hợp

nhiều tập 3D này

thành một khối 3D.

Để làm như vậy, hãy chọn một

cắt xuyên não.

Đây là một lát cắt qua

bộ não đã xem

trên ba chuỗi MRI khác nhau.

Ý tưởng chính mà chúng tôi sẽ

sử dụng để kết hợp các

thông tin từ

trình tự khác nhau là

coi chúng như những kênh khác nhau.

Có thể nói một trong những kênh

là màu đỏ, một là màu xanh lá cây,

và một là kênh màu xanh

theo cách tương tự như vậy

chúng tôi có ba kênh

của một hình ảnh RGB.

Sự tương tự của ba kênh

đại diện cho các kênh RGB là

chủ yếu hữu ích cho chúng ta

hình dung chúng ta đang đi như thế nào

để kết hợp các kênh.

Không có gì đặc biệt

về số ba.

Ý tưởng sử dụng

các kênh khác nhau cũng

kéo dài đến khi chúng ta có thể có

bốn hoặc năm chuỗi,

có thể được đại diện

với bốn hoặc năm kênh.

Một khi mỗi trình tự được

đại diện với

kênh khác nhau,

những gì chúng tôi làm bây giờ là kết hợp

các trình tự với nhau

để tạo ra một hình ảnh,

đó là sự kết hợp

của tất cả các trình tự.

Đối với chúng tôi, đây bây giờ là hình ảnh RGB.

Đối với máy, đây là những

các kênh xếp chồng lên nhau

chiều sâu.

Một thách thức với việc kết hợp

những trình tự này là chúng có thể

không được xếp thẳng hàng với nhau.

Ví dụ, nếu bệnh nhân di chuyển

giữa việc mua lại

mỗi trình tự này,

đầu của họ có thể nghiêng vào trong

so sánh một trình tự

với những người khác.

Nếu những hình ảnh đó

không liên kết với

lẫn nhau khi chúng ta kết hợp chúng,

vùng não ở

một địa điểm trong

kênh màu đỏ thì không

tương ứng với cùng một vị trí

trong màu xanh lá cây hoặc

các kênh màu xanh.

Vậy làm cách nào để khắc phục điều này

vấn đề liên kết?

Phương pháp tiền xử lý

cái đó thường được sử dụng

để khắc phục điều này được gọi là

đăng ký hình ảnh.

Ý tưởng cơ bản với

đăng ký hình ảnh

là biến đổi

những hình ảnh đó

chúng được căn chỉnh hoặc

đã đăng ký với nhau.

Chúng tôi sẽ không đi vào hình ảnh

đăng ký chi tiết hơn.

Trong nhiệm vụ,

bạn sẽ làm việc với

những hình ảnh đã có rồi

đã được đăng ký.

Tuy nhiên, nó rất hữu ích

để nhận thức được

đăng ký hình ảnh

như một công cụ hữu ích

khi cố gắng kết hợp các khối 3D.