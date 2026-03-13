# 07 mất chức năng cho phân đoạn hình ảnh

---

Chúng ta có thể biểu diễn các giá trị của p và

g qua từng pixel trong một bảng.

Ở đây, mỗi hàng của bảng

là vị trí ô,

cùng với tương ứng của họ

giá trị dự đoán và giá trị chân lý cơ bản.

Ví dụ: i4, ở đây,

tương ứng với ô này ở đây,

trong đó chỉ rõ rằng

đầu ra xác suất là 0,8,

và sự thật cơ bản là 0.

Đại diện cho p và

g trong bảng này sẽ cho phép chúng tôi làm được nhiều việc hơn

hiểu rõ hàm mất mát.

Chúng ta sẽ sử dụng số xúc xắc mềm để

tối ưu hóa mô hình phân đoạn.

Mất xúc xắc mềm là một mất mát phổ biến

chức năng cho các mô hình phân đoạn.

Ưu điểm của xúc xắc mềm

mất mát là nó hoạt động tốt

trong trường hợp dữ liệu mất cân bằng.

Điều này đặc biệt quan trọng trong chúng ta

nhiệm vụ phân chia khối u não,

khi một phần rất nhỏ của

não sẽ là vùng khối u.

Chúng ta hãy nhìn vào việc mất xúc xắc mềm.

Việc mất xúc xắc mềm sẽ đo lường

lỗi giữa bản đồ dự đoán của chúng tôi,

P và bản đồ sự thật mặt đất của chúng tôi, G.

Phần mất mát này, ở đây,

đo sự chồng chéo giữa

những dự đoán và sự thật cơ bản,

và chúng ta muốn phân số này lớn.

Ở đây, khi G ở đây bằng 1,

thì chúng ta muốn P gần bằng 1 nên

rằng tử số này lớn.

Chúng tôi cũng muốn mẫu số nhỏ.

Vậy khi G bằng 0,

chúng tôi muốn P ở gần

0. Nếu không, số hạng này sẽ lớn và

mẫu số sẽ lớn.

Bây giờ, chúng ta lấy 1 trừ phân số này,

cao hơn

mất mát tương ứng với một sự chồng chéo nhỏ và

tổn thất thấp tương ứng với sự chồng chéo cao.

Với trực giác này, bây giờ chúng ta hãy tính toán

sự mất mát cho ví dụ cụ thể này.

Để tính tử số của tổn thất

ví dụ này,

chúng tôi nhân P và

Yếu tố G khôn ngoan để có được lợn.

Ví dụ: 0,9 nhân 1 cho ta 0,9,

vậy là nó đã được nhập vào đây.

Để tính mẫu số,

chúng ta cần tổng bình phương của pi và

tổng bình phương của gi.

Tương tự, chúng ta có thể tính toán

những cái này bằng cách bình phương cột p

để có được pi bình phương và

cột g để có được gi bình phương.

Sau đó chúng ta có thể tổng hợp các cột này thành

lấy tổng trên tất cả các pixel.

Chúng ta có thể cắm những giá trị này vào

vào việc mất xúc xắc mềm cho

ví dụ cụ thể này như

1- 2 lần 2,2/2,47 + 3,

đó là 1- 4,4/5,47.

Và kết quả này là khoảng 0,2,

đó là sự mất mát với điều này

dự đoán cụ thể,

và với sự thật nền tảng đặc biệt này

cho ví dụ này.

Mô hình tối ưu hóa hàm mất mát này

để có được những phân đoạn ngày càng tốt hơn.

Điều này hoàn thành tất cả những phần chúng ta cần

để có thể rèn luyện trí não của chúng ta

mô hình phân chia khối u

Chúng ta sẽ xem xét việc đánh giá

mô hình phân đoạn tiếp theo.