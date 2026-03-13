# 02 mạng lan truyền tiếp trong mạng sâu

---

Trong video trước, chúng tôi đã mô tả những gì

mạng lưới thần kinh lớp L sâu

và cũng đã nói chuyện

về ký hiệu chúng ta sử dụng để

mô tả các mạng như vậy.

Trong video này, bạn sẽ thấy cách bạn có thể

thực hiện lan truyền về phía trước,

trong một mạng sâu.

Như thường lệ, trước tiên chúng ta hãy xem qua

sự lan truyền về phía trước sẽ như thế nào

cho một ví dụ đào tạo x,

và sau đó chúng ta sẽ nói về

phiên bản vector hóa,

nơi bạn muốn thực hiện

sự lan truyền về phía trước

trên toàn bộ tập huấn luyện

cùng một lúc.

Nhưng với một ví dụ huấn luyện x,

đây là cách bạn tính toán

kích hoạt lớp đầu tiên.

Vì vậy, đối với lớp đầu tiên này,

bạn tính z1 bằng

w1 nhân x cộng b1.

Vậy w1 và b1 là các tham số

ảnh hưởng đến các kích hoạt ở lớp một.

Đây là lớp một của mạng lưới thần kinh,

và sau đó bạn tính toán kích hoạt

để lớp đó bằng g của z1.

Hàm kích hoạt g

phụ thuộc vào lớp bạn đang ở và

có thể chỉ số nào được đặt làm

chức năng kích hoạt từ lớp một.

Vì vậy, nếu bạn làm điều đó, bây giờ bạn đã tính toán

kích hoạt cho lớp một.

Còn lớp hai thì sao? Nói lớp đó.

Vâng, sau đó bạn sẽ tính z2 bằng

w2 a1 cộng b2.

Sau đó, việc kích hoạt lớp hai là

ma trận y nhân với đầu ra của lớp một.

Vì vậy, đó là giá trị,

cộng với vectơ thiên vị cho lớp hai.

Khi đó a2 bằng hàm kích hoạt

áp dụng cho z2.

Được rồi? Vậy là xong phần thứ hai,

vân vân và vân vân.

Cho đến khi bạn lên được tầng trên,

đó là lớp bốn.

Nơi bạn sẽ có z4 đó bằng nhau

đến các tham số cho thời gian của lớp đó

các kích hoạt từ lớp trước,

cộng với vectơ thiên vị đó.

Khi đó tương tự, a4 bằng g của z4.

Vì vậy, đó là cách bạn tính toán

sản lượng ước tính, y hat.

Vì vậy, chỉ cần chú ý một điều,

x ở đây cũng bằng a0,

bởi vì vectơ đặc tính đầu vào x là

cũng là sự kích hoạt của lớp không.

Vì vậy chúng ta gạch bỏ x.

Khi tôi gạch bỏ x và đặt a0 ở đây,

thì tất cả các phương trình này

về cơ bản trông giống nhau.

Nguyên tắc chung là zl bằng

wl nhân a của l trừ 1 cộng bl.

Có một cái ở đó. Và sau đó,

kích hoạt cho lớp đó là

chức năng kích hoạt

áp dụng cho các giá trị của z.

Vì vậy, đó là cái chung

phương trình lan truyền thuận.

Vì vậy, chúng tôi đã thực hiện tất cả điều này cho một

ví dụ đào tạo duy nhất.

Còn việc thực hiện nó theo cách vector hóa thì sao

cho toàn bộ tập huấn luyện cùng một lúc?

Các phương trình trông khá giống như trước đây.

Đối với lớp đầu tiên, bạn sẽ

có vốn Z1 bằng

w1 nhân vốn X cộng b1.

Khi đó, A1 bằng g của Z1.

Hãy nhớ rằng X bằng A0.

Đây chỉ là những ví dụ đào tạo

xếp thành các cột khác nhau.

Bạn có thể lấy cái này, để tôi gạch bỏ chữ X,

họ có thể đặt A0 ở đó.

Sau đó, đối với lớp tiếp theo, trông tương tự,

Z2 bằng w2

A1 cộng b2 và A2 bằng g của Z2.

Chúng tôi chỉ lấy những thứ này

vectơ z hoặc a, v.v.,

và xếp chúng lên.

Đây là vectơ z cho

ví dụ đào tạo đầu tiên,

vectơ z cho

ví dụ đào tạo thứ hai,

vân vân, cho đến

ví dụ đào tạo thứ n,

xếp chồng những cái này và cột

và gọi thủ đô này là Z.

Tương tự, đối với vốn A,

giống như vốn X.

Tất cả các ví dụ huấn luyện đều

vectơ cột xếp chồng từ trái sang phải.

Trong quá trình này, bạn kết thúc với

y mũ bằng g của Z4,

cái này cũng bằng A4.

Đó là những dự đoán trên tất cả của bạn

ví dụ đào tạo xếp chồng lên nhau theo chiều ngang.

Vì vậy, chỉ để tóm tắt về ký hiệu,

Tôi sẽ sửa đổi điều này ở đây.

Một ký hiệu cho phép chúng ta thay thế chữ z thường

và a với các chữ viết hoa,

đó là chữ Z viết hoa.

Điều đó mang lại cho bạn phiên bản vector hóa của

truyền bá về phía trước mà bạn thực hiện

trên toàn bộ tập huấn luyện tại một thời điểm,

trong đó A0 là X.

Bây giờ, nếu bạn nhìn vào đây

thực hiện vector hóa,

có vẻ như có

sẽ là một vòng lặp For ở đây.

Vì vậy l bằng 1-4.

Với L bằng 1 đến chữ L viết hoa. Khi đó bạn

phải tính toán kích hoạt cho lớp một,

rồi đến lớp hai, rồi đến lớp ba,

và sau đó là lớp bốn.

Vì vậy, có vẻ như có vòng lặp For ở đây.

Tôi biết rằng khi thực hiện

mạng lưới thần kinh,

chúng ta thường muốn loại bỏ

vòng lặp For rõ ràng.

Nhưng đây là một nơi mà tôi không nghĩ

có cách nào để thực hiện điều này

không có vòng lặp For rõ ràng.

Vì vậy, khi thực hiện việc truyền bá về phía trước,

hoàn toàn ổn nếu có vòng lặp For

để tính toán kích hoạt cho lớp một,

rồi lớp hai, rồi lớp ba,

sau đó lớp bốn.

Không ai biết và tôi cũng không nghĩ

có cách nào để làm

cái này không có vòng lặp For

đi từ một đến chữ hoa L,

từ một đến tổng số

các lớp trong mạng nơ-ron.

Vì vậy, ở nơi này, thật hoàn hảo

được nếu có một vòng lặp For rõ ràng.

Vậy là xong phần ký hiệu

cho mạng lưới thần kinh sâu,

cũng như cách thực hiện việc truyền bá tiếp theo

trong các mạng này.

Nếu những mảnh chúng ta đã thấy cho đến nay

trông hơi quen với bạn,

đó là vì những gì chúng ta đang thấy đang diễn ra

một phần rất giống với những gì bạn đã thấy trong

mạng lưới thần kinh với một mạng ẩn duy nhất

lớp và chỉ lặp lại điều đó nhiều lần hơn.

Bây giờ, hóa ra là chúng tôi thực hiện

một mạng lưới thần kinh sâu sắc,

một trong những cách để tăng

khả năng triển khai không có lỗi

là suy nghĩ rất có hệ thống và

cẩn thận về ma trận

kích thước bạn đang làm việc.

Vì vậy, khi tôi đang cố gỡ lỗi mã của riêng mình,

Tôi thường rút một mảnh giấy ra,

và chỉ cần suy nghĩ cẩn thận,

vậy các kích thước của

ma trận tôi đang làm việc.

Hãy xem bạn có thể làm thế nào

làm điều đó trong video tiếp theo.