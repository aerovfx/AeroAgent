# 08 đạo hàm của hàm kích hoạt

---

Khi bạn thực hiện lan truyền ngược

cho mạng lưới thần kinh của bạn,

bạn cần tính toán độ dốc hoặc

đạo hàm của hàm kích hoạt.

Vì vậy, chúng ta hãy xem xét sự lựa chọn của chúng ta về

chức năng kích hoạt và cách bạn có thể

tính độ dốc của các hàm này.

Đây là Sigmoid quen thuộc

chức năng kích hoạt.

Vì vậy, với mọi giá trị cho trước của z,

có lẽ giá trị này của z.

Hàm này sẽ có độ dốc hoặc

một số đạo hàm tương ứng với,

nếu bạn vẽ một đường nhỏ ở đó,

chiều cao trên chiều rộng của cái này

tam giác dưới đây.

Vì vậy, nếu g(z) là hàm sigmoid,

thì độ dốc của hàm số là d,

dz g của z,

và vì vậy chúng ta biết từ phép tính rằng

nó là độ dốc của g của x tại z.

Nếu bạn đã quen với phép tính

và biết cách lấy đạo hàm,

nếu bạn lấy đạo hàm của

hàm sigmoid,

có thể chứng tỏ rằng đó là

bằng công thức này.

Một lần nữa, tôi sẽ không làm

các bước tính toán,

nhưng nếu bạn quen với phép tính,

vui lòng đăng video và

hãy cố gắng tự mình chứng minh điều này.

Vì vậy, cái này bằng g(z),

nhân 1 trừ g của z.

Vì vậy, hãy tỉnh táo kiểm tra xem

biểu hiện này có ý nghĩa.

Đầu tiên, nếu z rất lớn,

vậy nói z bằng 10,

thì g của z sẽ gần bằng 1,

và do đó công thức chúng ta có ở bên trái cho biết

chúng ta rằng d dz g của z gần bằng g của z,

nó bằng 1 nhân 1 trừ 1,

do đó nó rất gần với 0.

Điều này không đúng vì

khi z rất lớn,

độ dốc gần bằng 0.

Ngược lại, nếu z bằng âm 10,

vì vậy nó nói tốt ở đó,

thì g của z gần bằng 0.

Vì vậy, công thức bên trái cho chúng ta biết

d dz g của z sẽ gần bằng g của z,

đó là 0 nhân 1 trừ 0.

Vậy nó cũng rất gần với 0,

cái nào đúng.

Cuối cùng, nếu z bằng 0,

thì g của z bằng một nửa,

đó là hàm sigmoid ở đây,

và do đó đạo hàm bằng

một nửa nhân 1 trừ một nửa,

bằng một phần tư,

và điều đó thực sự hóa ra là

là giá trị đúng của

đạo hàm hoặc độ dốc của cái này

hàm khi z bằng 0.

Cuối cùng chỉ để giới thiệu

thêm một phần ký hiệu nữa,

đôi khi thay vì viết điều này,

viết tắt của đạo hàm

là g nguyên tố của z.

Vì vậy, g nguyên tố z trong phép tính,

dấu gạch ngang nhỏ ở trên được gọi là số nguyên tố,

nhưng vậy g nguyên tố của z là a

viết tắt của phép tính cho

đạo hàm của hàm g

đối với biến đầu vào z.

Sau đó, trong một mạng lưới thần kinh,

chúng ta có g bằng z,

bằng cái này thì công thức này

cũng rút gọn thành a nhân 1 trừ a.

Vì vậy, đôi khi trong quá trình thực hiện,

bạn có thể thấy một cái gì đó như

g số nguyên tố của z bằng a nhân 1 trừ a,

và điều đó chỉ đề cập đến

quan sát rằng g nguyên tố,

nó chỉ có nghĩa là đạo hàm,

bằng với cái này ở đây.

Ưu điểm của công thức này là

nếu bạn đã tính giá trị của a,

sau đó bằng cách sử dụng biểu thức này,

bạn có thể tính toán rất nhanh

giá trị cho độ dốc của g prime.

Được rồi. Vì vậy, đó là

chức năng kích hoạt sigmoid.

Bây giờ chúng ta hãy nhìn vào Tánh

chức năng kích hoạt.

Tương tự như những gì chúng tôi đã có trước đây,

định nghĩa của d dz g của z là

độ dốc của g của z tại

một điểm cụ thể của z,

và nếu bạn nhìn vào công thức của

hàm tang hyperbol,

và nếu bạn biết tính toán,

bạn có thể lấy công cụ phái sinh và

chứng tỏ rằng điều này đơn giản hóa thành

công thức này và sử dụng

cách viết tắt chúng ta có trước đây

khi chúng ta gọi lại đây là g phẩy của z.

Vì vậy, nếu bạn muốn, bạn có thể kiểm tra sự tỉnh táo

rằng công thức này có ý nghĩa.

Vì vậy, ví dụ, nếu z bằng 10,

Tính của z sẽ rất gần với 1.

Điều này đi từ cộng 1 đến trừ 1.

Khi đó g nguyên tố của z,

theo công thức này,

sẽ bằng khoảng 1 trừ 1 bình phương,

nên nó rất gần với 0.

Vì vậy, đó là nếu z rất lớn,

độ dốc gần bằng 0.

Ngược lại, nếu z rất nhỏ,

nói z bằng trừ 10,

thì Tánh của z sẽ tiến gần đến âm 1,

và do đó g nguyên tố của z sẽ là

gần bằng 1 trừ âm 1 bình phương.

Vì vậy, nó gần bằng 1 trừ 1,

cũng gần bằng 0.

Cuối cùng, nếu z bằng 0,

thì Tánh của z bằng 0,

và khi đó độ dốc là

thực sự bằng 1,

đó thực sự là độ dốc

khi z bằng 0.

Vì vậy, chỉ để tóm tắt,

nếu a bằng g của z,

vậy nếu a bằng cái này

Tính của z thì đạo hàm,

g số nguyên tố của z, bằng

1 trừ một bình phương.

Vì vậy, một lần nữa, nếu bạn đã

tính giá trị của a,

bạn có thể sử dụng công thức này để

tính đạo hàm nhanh chóng.

Cuối cùng, đây là cách bạn

tính đạo hàm cho

ReLU và ReLU bị rò rỉ

các chức năng kích hoạt.

Với giá trị g của z là

bằng tối đa 0, z,

nên đạo hàm bằng,

hóa ra là 0,

nếu z nhỏ hơn 0 và 1

nếu z lớn hơn 0.

Về mặt kỹ thuật, nó thực sự không được xác định

không xác định nếu z bằng chính xác 0.

Nhưng nếu bạn đang triển khai

cái này trong phần mềm,

nó có thể không phải là 100 phần trăm

đúng về mặt toán học,

nhưng nó sẽ hoạt động tốt

nếu z chính xác là 0,

nếu bạn đặt đạo hàm

bằng 1.

Nó luôn phải là 0,

nó không quan trọng

Nếu bạn là một chuyên gia trong

tối ưu hóa về mặt kỹ thuật,

g prime sau đó sẽ trở thành cái được gọi là a

gradient con của hàm kích hoạt g của z,

đó là lý do tại sao độ dốc

đi xuống vẫn hoạt động.

Nhưng bạn có thể nghĩ về nó như thế,

cơ hội của z là

chính xác là 0,000000.

Nó nhỏ đến mức gần như

không quan trọng bạn ở đâu

đặt đạo hàm bằng

khi z bằng 0.

Vì vậy, trong thực tế, đây là điều

người ta thực hiện tính đạo hàm của z.

Cuối cùng, nếu bạn đang huấn luyện một mạng lưới thần kinh

với chức năng kích hoạt Leaky ReLU,

thì g của z sẽ bằng

tối đa là 0,01 z, z, v.v.,

g số nguyên tố của z bằng 0,01 nếu z

nhỏ hơn 0 và 1 nếu z lớn hơn 0.

Một lần nữa, độ dốc là về mặt kỹ thuật

không được xác định khi z chính xác bằng 0,

nhưng nếu bạn thực hiện một

đoạn mã đặt

đạo hàm hoặc bộ đó

g nguyên tố bằng 0,01 hoặc hoặc bằng 1,

dù sao đi nữa, nó không thực sự quan trọng.

Khi z chính xác bằng 0,

mã của bạn sẽ hoạt động bình thường.

Vì vậy, theo các công thức này,

bạn nên tính toán độ dốc hoặc

đạo hàm của các hàm kích hoạt của bạn.

Bây giờ chúng ta có khối xây dựng này,

bạn đã sẵn sàng để xem cách triển khai

giảm độ dốc cho mạng lưới thần kinh của bạn.

Chúng ta hãy chuyển sang video tiếp theo để thấy điều đó.