# 02 đại diện mạng lưới thần kinh

---

Bạn thấy tôi vẽ một vài

hình ảnh của mạng lưới thần kinh.

Trong video này, chúng ta sẽ nói về

chính xác ý nghĩa của những hình ảnh đó

Nói cách khác,

chính xác thì những mạng lưới thần kinh đó là gì

mà chúng tôi đã vẽ đại diện.

Và chúng ta sẽ bắt đầu bằng việc tập trung vào

trường hợp của mạng lưới thần kinh với

cái được gọi là một lớp ẩn duy nhất.

Đây là hình ảnh của một mạng lưới thần kinh.

Hãy đưa ra những phần khác nhau của

những hình ảnh này một số tên.

Chúng tôi có các tính năng đầu vào, x1,

x2, x3 xếp chồng lên nhau theo chiều dọc.

Và đây được gọi là đầu vào

lớp của mạng lưới thần kinh.

Vì vậy có lẽ không có gì đáng ngạc nhiên, cái này chứa

đầu vào của mạng nơ-ron.

Sau đó là một lớp vòng tròn khác.

Và đây được gọi là ẩn

lớp của mạng lưới thần kinh.

Tôi sẽ quay lại sau một giây để

nói từ ẩn có nghĩa là gì.

Nhưng lớp cuối cùng ở đây được hình thành bởi,

trong trường hợp này, chỉ một nút.

Và lớp nút đơn này được gọi là

lớp đầu ra và chịu trách nhiệm về

tạo ra giá trị dự đoán y hat.

Trong một mạng lưới thần kinh

bạn luyện tập với phương pháp học có giám sát,

tập huấn luyện chứa các giá trị của

đầu vào x cũng như đầu ra mục tiêu y.

Vì vậy, thuật ngữ lớp ẩn đề cập đến

thực tế là trong tập huấn luyện,

những giá trị đích thực cho

những nút ở giữa không được quan sát.

Tức là bạn không thấy những gì họ

nên có trong tập huấn luyện.

Bạn thấy đầu vào là gì.

Bạn thấy đầu ra sẽ như thế nào.

Nhưng những thứ ở lớp ẩn

không được nhìn thấy trong tập huấn luyện.

Vì vậy, điều đó giải thích cái tên

lớp ẩn; chỉ vì bạn

không nhìn thấy nó trong tập huấn luyện.

Hãy giới thiệu thêm một chút ký hiệu.

Trong khi trước đó, chúng tôi đã sử dụng

vectơ X để biểu thị các tính năng đầu vào và

ký hiệu thay thế cho

các giá trị của các tính năng đầu vào sẽ

là dấu ngoặc vuông siêu ký tự 0.

Và chữ A còn là viết tắt của

kích hoạt và

nó đề cập đến các giá trị

các lớp khác nhau đó

của mạng lưới thần kinh đang đi qua

sang các lớp tiếp theo.

Vì vậy lớp đầu vào tiếp tục

giá trị x cho lớp ẩn, vì vậy

chúng ta sẽ gọi đó là kích hoạt

của lớp đầu vào A siêu tập lệnh 0.

Lớp tiếp theo, lớp ẩn, sẽ

lần lượt tạo ra một số tập hợp kích hoạt,

mà tôi sẽ viết là

Dấu ngoặc vuông chỉ số trên 1.

Vì vậy, đặc biệt,

đơn vị đầu tiên này hoặc nút đầu tiên này,

chúng tôi tạo ra một giá trị A siêu ký tự

dấu ngoặc vuông 1 chỉ số dưới 1.

Nút thứ hai này chúng tôi tạo ra một giá trị.

Bây giờ chúng ta có chỉ số dưới 2, v.v.

Và như vậy, dấu ngoặc vuông chỉ số trên 1,

đây là một vector bốn chiều

bạn muốn bằng Python

bởi vì ma trận 4x1, hoặc

một vector 4 cột trông như thế này.

Và nó là bốn chiều, bởi vì

trong trường hợp này chúng ta có bốn nút, hoặc

bốn đơn vị, hoặc

bốn đơn vị ẩn trong lớp ẩn này.

Và cuối cùng,

lớp mở sẽ tạo lại một số giá trị A2,

đó chỉ là một số thực.

Và thế là

y hat sẽ nhận giá trị của A2.

Vì vậy, điều này tương tự như cách trong

hồi quy logistic chúng ta có y hat bằng a và

trong hồi quy logistic mà chúng tôi

chỉ có một lớp đầu ra đó, vì vậy

chúng tôi không sử dụng chỉ số trên

dấu ngoặc vuông.

Nhưng với mạng lưới thần kinh của chúng tôi,

bây giờ chúng ta sẽ sử dụng hình vuông chỉ số trên

dấu ngoặc để biểu thị rõ ràng

nó đến từ lớp nào.

Một điều buồn cười về ký hiệu

quy ước trong mạng lưới thần kinh

đó có phải là mạng lưới mà bạn đã thấy ở đây

được gọi là mạng nơ-ron hai lớp.

Và lý do là khi chúng ta

đếm các lớp trong mạng lưới thần kinh,

chúng tôi không tính lớp đầu vào.

Vì vậy lớp ẩn là lớp một và

lớp đầu ra là lớp hai.

Trong quy ước ký hiệu của chúng tôi, chúng tôi

gọi lớp đầu vào là 0, vì vậy

về mặt kỹ thuật có thể có ba

các lớp trong mạng lưới thần kinh này.

Bởi vì có lớp đầu vào,

lớp ẩn và lớp đầu ra.

Nhưng trong cách sử dụng thông thường, nếu bạn

đọc các tài liệu nghiên cứu và những nơi khác trong

khóa học, bạn thấy mọi người nhắc đến điều này

mạng lưới thần kinh cụ thể là hai lớp

mạng lưới thần kinh, bởi vì chúng tôi không đếm

lớp đầu vào là lớp chính thức.

Cuối cùng, thứ mà chúng ta sẽ đạt được

sau đó là lớp ẩn và

các lớp đầu ra sẽ có

các tham số liên quan đến chúng.

Vì vậy lớp ẩn sẽ có

liên kết với nó các tham số w và b.

Và tôi sẽ viết chỉ số trên

dấu ngoặc vuông 1 để chỉ ra rằng những

là các tham số liên quan đến

lớp một với lớp ẩn.

Sau này chúng ta sẽ thấy rằng chúng ta sẽ

là ma trận 4 x 3 và

b sẽ là một vectơ 4 x 1 trong ví dụ này.

Nơi tọa độ đầu tiên bốn

xuất phát từ thực tế là chúng ta có

bốn nút của các đơn vị ẩn của chúng tôi và

một lớp và

ba xuất phát từ thực tế là

chúng tôi có ba tính năng đầu vào.

Chúng ta sẽ nói chuyện sau về

kích thước của các ma trận này.

Và nó có thể có ý nghĩa hơn vào thời điểm đó.

Nhưng ở một số lớp đầu ra có

cũng được liên kết với nó, các tham số w

dấu ngoặc vuông chỉ số trên 2 và

b dấu ngoặc vuông chỉ số trên 2.

Và hóa ra kích thước

trong số này là 1 x 4 và 1 x 1.

Và 1 x 4 này là do ẩn

lớp có bốn đơn vị ẩn,

lớp đầu ra chỉ có một đơn vị.

Nhưng chúng ta sẽ đi sâu vào kích thước của những thứ này

ma trận và vectơ trong video sau.

Vậy là bạn vừa thấy hai thứ tuyệt vời thế nào

mạng lưới thần kinh nhiều lớp trông như thế nào.

Đó là mạng lưới thần kinh

với một lớp ẩn.

Trong video tiếp theo,

chúng ta hãy đi sâu hơn vào chính xác những gì

mạng lưới thần kinh này đang tính toán.

Đó là cách mà dây thần kinh này

đầu vào mạng x và

đi đến tận cùng

tính toán đầu ra y hat của nó.