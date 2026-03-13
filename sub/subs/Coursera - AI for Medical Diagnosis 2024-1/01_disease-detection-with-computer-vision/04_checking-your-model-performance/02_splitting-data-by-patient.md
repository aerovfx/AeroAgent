# 02 phần chia dữ liệu theo bệnh nhân

---

Để giải quyết vấn đề này trong tập dữ liệu của chúng tôi,

chúng ta có thể đảm bảo rằng bệnh nhân

Tia X chỉ xảy ra ở một trong các bộ.

Bây giờ, nếu mô hình ghi nhớ

chiếc vòng cổ trên người bệnh nhân,

nó không giúp nó đạt được

hiệu suất cao hơn

trên tập kiểm tra vì nó

không gặp cùng một bệnh nhân.

Hãy xem điều này trong thực tế

trên tất cả các bệnh nhân.

Khi chúng tôi chia một tập dữ liệu

theo cách truyền thống,

hình ảnh được gán ngẫu nhiên

đến một trong các bộ.

Lưu ý rằng theo cách này chúng ta thu được tia X

thuộc về cùng một bệnh nhân

trong các bộ khác nhau.

Ví dụ, tia X thuộc về

bệnh nhân 20 và là một phần của khóa đào tạo.

X-quang số 2 cũng thuộc về bệnh nhân 20 và

là một phần của xác nhận.

Và tia X số 0 cũng thuộc về bệnh nhân 20,

đó là một phần của bài kiểm tra

Đây là vấn đề chồng chéo bệnh nhân.

Thay vào đó, khi chúng tôi chia tay

một tập dữ liệu của bệnh nhân,

tất cả các tia X thuộc về

cùng một bệnh nhân ở trong cùng một bộ.

Ví dụ, chụp X-quang,

X-quang hai, và X-quang số 0,

tất cả đều thuộc về bệnh nhân 20,

đều là một phần của đào tạo.

Ở đây bảy, tám và chín,

đều là bộ phận của bệnh nhân 32,

tất cả đều nằm trong bộ xác thực và

chúng ta không thấy 20 và 32 ở đây trong bài kiểm tra.

Bằng cách này, chúng ta có thể đảm bảo có

không có bệnh nhân chồng chéo giữa các bộ.

Điều này bao gồm giải pháp của chúng tôi

đến thử thách đầu tiên.