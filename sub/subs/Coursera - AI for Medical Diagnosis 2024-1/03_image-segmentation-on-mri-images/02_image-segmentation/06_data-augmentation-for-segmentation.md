# 06 tăng cường dữ liệu cho phân đoạn

---

Bây giờ chúng ta đã nói về

kiến trúc phân đoạn,

hãy nói về một kỹ thuật mà chúng ta có thể

áp dụng vào việc đào tạo một mô hình như vậy,

tăng cường dữ liệu.

Trước đó chúng ta đã thấy cách chúng ta có thể tiếp cận

sự biến đổi của ngực

tia X sao cho nhãn phân loại

của mỗi ví dụ nêu giống nhau.

Bây giờ hãy xem cách chúng ta có thể áp dụng

nguyên tắc tương tự để phân khúc

với một vài điểm khác biệt chính.

Một điểm khác biệt chính với dữ liệu

tăng cường trong quá trình phân đoạn

bây giờ chúng ta có đầu ra phân đoạn.

Vì vậy, khi chúng ta xoay hình ảnh đầu vào 90

độ để tạo ra một đầu vào được chuyển đổi,

chúng ta cũng cần xoay đầu ra

phân đoạn 90 độ

để chúng tôi được biến đổi

phân đoạn đầu ra.

Sự khác biệt thứ hai là bây giờ chúng ta

có khối lượng 3D thay vì hình ảnh 2D.

Vì vậy, các phép biến đổi phải

áp dụng cho toàn bộ khối lượng 3D.

Với điều này, chúng tôi gần như có tất cả

những phần cần thiết để rèn luyện khối u não của chúng ta

mô hình phân đoạn.

Điều cuối cùng chúng ta cần

nhìn vào là hàm mất mát.

Trong hàm mất mát của chúng tôi,

chúng tôi muốn có thể chỉ định lỗi.

Chúng ta nên chỉ định một ví dụ, đưa ra

dự đoán mô hình và sự thật cơ bản.

Hãy lấy một ví dụ rất đơn giản.

Trong thực tế, chúng ta sẽ có

độ phân giải cao hơn nhiều

hình ảnh và chúng ta sẽ xem xét một khối 3D.

Nhưng ví dụ 2D đơn giản của chúng tôi ở đây sẽ

cho phép chúng ta có được trực giác nhanh chóng.

Ở đây vốn P đại diện cho sản lượng của

mô hình phân đoạn trên 9

pixel. Trong đó mỗi vị trí, chúng tôi có

xác suất dự đoán của một khối u.

Viết hoa G chỉ rõ sự thật cơ bản trên

từng vị trí pixel này.

Ba trong số chín pixel

khối u được biểu thị bằng 1,

và sáu điều còn lại là bình thường

mô não được biểu thị bằng 0.