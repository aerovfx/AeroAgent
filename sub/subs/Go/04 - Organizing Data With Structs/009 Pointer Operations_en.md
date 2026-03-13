# 009 Các thao tác con trỏ vi

---

Giáo viên: Ở phần cuối,

chúng tôi đã thực hiện một chút thay đổi đối với cơ sở mã của mình

và kết quả là bất cứ khi nào chúng tôi gọi

chức năng tên cập nhật này với một chuỗi jimmy

có vẻ như jim đã được cập nhật thành công.

Vì vậy, bây giờ chúng ta sẽ chia nhỏ mã này

và nói về chính xác những gì chúng tôi vừa làm.

Vì vậy điều đầu tiên tôi muốn làm là nói chuyện một chút

về toán tử dấu và ở đây là gì,

và toán tử ngôi sao hoặc dấu sao ở dưới đây là gì.

Vì vậy, hãy nói về những toán tử đó là gì

và điều đó có thể sẽ giúp chúng ta

làm quen thêm một chút

với những gì mã thực sự đang làm ở đây.

Được rồi, đầu tiên chúng ta sẽ nói về ký hiệu và dấu đó.

Dấu và là một toán tử.

Chúng tôi đặt ký hiệu và sau đó là một số tên biến.

Và đó chính xác là những gì chúng ta vừa thấy trong cơ sở mã của mình

nơi chúng tôi đặt ký hiệu và sau đó là biến jim,

ôi, &jim.

Bây giờ khi chúng ta làm điều đó, chúng ta đang nói hãy nhìn vào biến này

và cấp cho chúng tôi quyền truy cập vào địa chỉ bộ nhớ

mà biến này đang trỏ tới.

Vì vậy, nói cách khác, nếu chúng ta có &jim

jim đang chỉ vào cấu trúc của chúng tôi trong bộ nhớ,

và cấu trúc đó tồn tại ở một số địa chỉ RAM cụ thể.

Vì vậy, khi chúng tôi viết &jim, chúng tôi nói,

"Cho tôi quyền truy cập vào địa chỉ bộ nhớ

mà cấu trúc này đang nằm ở đó."

Và ví dụ, nó có thể là 0001.

Chúng tôi lấy giá trị đó và sau đó gán nó cho jimPointer.

Vì vậy bây giờ biến jimPointer này

mà chúng tôi vừa giới thiệu vào ứng dụng của mình không trỏ

hoặc nó không phải là một tham chiếu trực tiếp đến cấu trúc.

Thay vào đó nó là một tham chiếu đến địa chỉ bộ nhớ

mà cấu trúc tồn tại ở đó.

Nếu bây giờ chúng ta in ra giá trị của jimPointer,

chúng ta có thể sẽ thấy một số loại địa chỉ bộ nhớ

như 0x0abcd123.

Vì vậy, jimPointer hiện đang trỏ

trực tiếp tại không gian này trong bộ nhớ.

Bây giờ với ý nghĩ đó, hãy nói về toán tử khác

mà chúng ta vừa thấy.

Thế là ngôi sao điều hành.

Vì vậy, bất cứ khi nào chúng ta sử dụng toán tử ngôi sao,

chúng ta đặt dấu sao và sau đó là địa chỉ bộ nhớ hoặc con trỏ.

Bất cứ khi nào chúng tôi làm điều đó, chúng tôi đang nói,

"Lấy địa chỉ bộ nhớ này và đưa cho tôi giá trị tồn tại

tại địa chỉ bộ nhớ đó."

Vì vậy, bên trong hàm cập nhật tên của chúng tôi, ngay tại đây,

chúng tôi đã nói *pointerToPerson.

con trỏToPerson là địa chỉ bộ nhớ mà jim tồn tại.

Và bằng cách nói *pointerToPerson,

chúng ta đang nói, "Đây là con trỏ.

Tôi không muốn nhìn vào địa chỉ bộ nhớ nữa.

Thay vào đó hãy cho tôi quyền truy cập trực tiếp vào bất cứ thứ gì

hoặc bất cứ giá trị nào thực sự đang nằm ở đây."

Và thế là *jimPointer biến thành cấu trúc thực sự

thuộc loại người.

Vì vậy, hãy lưu ý đến hai toán tử đó

và hiểu chính xác những gì họ làm,

bây giờ chúng ta hãy xem qua mã của chúng tôi

và xem liệu chúng ta có thể tìm ra chính xác chuyện gì đang xảy ra không.

Được rồi, ngay tại dòng một,

đầu tiên chúng ta bắt đầu bằng cách lấy biến jim.

Hãy nhớ rằng, jim là một tham chiếu đến cấu trúc trong bộ nhớ,

giá trị thực của cấu trúc.

Chúng tôi sử dụng toán tử dấu và.

Khi chúng tôi làm điều đó, chúng tôi biến &jim thành một địa chỉ bộ nhớ

hoặc một con trỏ rồi gán giá trị đó cho jimPointer.

Tiếp theo chúng ta gọi jimPointer.updateName.

Bây giờ hãy chú ý, và điều này thực sự quan trọng,

hãy chú ý cách chúng tôi thay đổi loại máy thu ở đây

trở thành * người.

Bạn có thể đọc cái này ngay tại đây

như một con trỏ chỉ vào một người.

Bây giờ có một điều tôi muốn chỉ ra,

và điều này thực sự quan trọng để hiểu,

và đây có lẽ là một trong những điều khó hiểu nhất

về con trỏ trong Go, tôi vừa nói với bạn hai giây trước

rằng bất cứ khi nào chúng ta đặt ngôi sao và sau đó là con trỏ,

điều đó biến điều đó thành một giá trị.

Vậy cái này ở đây sẽ được chuyển thành một giá trị, phải không?

Như tôi vừa nói hai giây trước.

Nhưng bây giờ tôi cũng đang nói với bạn rằng *người ở ngay đây

đang nói một loại con trỏ chỉ vào một người.

Và đây là sự khác biệt thực sự quan trọng

rằng tôi muốn dành nhiều thời gian để thực sự tìm hiểu sâu về nhà.

Được rồi, điều này có lẽ, theo ý kiến của tôi,

một trong những điều khó hiểu nhất về con trỏ

đó là khi chúng ta nhìn thấy một ngôi sao ở phía trước một loại chữ,

nó có nghĩa là một cái gì đó hoàn toàn khác

hơn là khi chúng ta nhìn thấy một ngôi sao ở phía trước một con trỏ thực sự.

Vì vậy, hãy chia nhỏ cả hai điều này

và tìm ra sự khác biệt giữa hai điều này.

Vì vậy, trong máy thu, chúng tôi đã nói con trỏ đó tới người

là giá trị kiểu *person.

Bất cứ khi nào bạn nhìn thấy một ngôi sao và sau đó là bất cứ thứ gì,

về cơ bản là bất kỳ từ nào,

ở một nơi mà một loại được cho là?

Và hãy nhớ trong máy thu chúng ta luôn đặt giá trị

và sau đó là loại đó.

Vì vậy, bất cứ khi nào bạn nhìn thấy một ngôi sao nơi đáng lẽ phải có một loại,

điều đó có nghĩa rằng đây là một mô tả về một loại.

Chúng tôi đang tìm kiếm một con trỏ cho một người.

Vậy trong trường hợp này, ngôi sao ở đây

thực sự có lẽ không nên nghĩ đến

nghiêm túc với tư cách là người điều hành.

Giống như chúng tôi đã nói rằng đó là trước đây.

Hãy nhớ rằng chúng ta vừa nói hai giây trước

con trỏ * đó là một toán tử cho biết,

"Hãy cho tôi giá trị mà địa chỉ bộ nhớ này đang trỏ tới."

Nhưng khi chúng ta nhìn thấy ngôi sao đó ở phía trước một hình mẫu thực tế,

đó là một mô tả kiểu,

và nó có nghĩa là chức năng tên cập nhật này

chỉ có thể được gọi với người nhận

của một con trỏ tới một người.

Được rồi, tôi hy vọng điều này có ý nghĩa

khi tôi đang cố gắng làm rõ

rằng đây thực sự là một chủ đề khó hiểu

và hy vọng sự khác biệt giữa hai điều này

có ý nghĩa.

Vì vậy, điều này xác định rằng chúng ta muốn một loại con trỏ

đến một người.

Đây là một toán tử thực tế lấy con trỏ này,

và biến nó thành một giá trị thực tế.

Được rồi, hãy quay lại mã của chúng ta

và tiếp tục đi qua.

Vậy là chúng ta có hàm updateName,

có thể được gọi với bất kỳ máy thu nào

thuộc loại con trỏToPerson,

đó chính xác là jimPointer.

Vì vậy chúng tôi gọi jimPointer.updateName.

JimPointer này ngay tại đây, hoặc địa chỉ bộ nhớ này,

sau đó được chuyển vào hàm này dưới dạng con trỏToPerson.

Vì vậy, bạn có thể tưởng tượng jimPointer và con trỏToPerson

hiện tại đều giống hệt nhau.

Vì vậy, bên trong hàm chúng ta nói *pointerToPerson.

Vì vậy, hãy nhớ ngôi sao và con trỏ thực tế có nghĩa là gì.

Nó bảo lấy địa chỉ bộ nhớ này là con trỏToPerson

và biến nó thành một giá trị thực tế.

Vì vậy, khối dấu ngoặc đơn nhỏ này ở đây,

thứ này ở ngay đây,

được biến thành con người jim thực sự

đó là ngồi trong bộ nhớ.

Vì vậy, chúng tôi lấy lại cấu trúc này ngay tại đây

điều đó đang nằm trong ký ức.

Sau đó chúng tôi tham chiếu thuộc tính firstName của nó,

và chúng tôi cập nhật thuộc tính firstName của nó thành Jimmy,

hoặc bất kể newFirstName là gì.

Được rồi, đó là hướng dẫn số một ở đây.

Và nếu nó khó hiểu,

Tôi phải nói với bạn rằng điều đó hoàn toàn ổn.

Chưa ai từng học con trỏ

mà không hề nghe về họ trước đây

giống như lần đầu tiên họ được kể về họ.

Chưa ai từng hiểu các con trỏ ngay từ đầu.

Và nếu bạn nói, "Ồ, xin chúc mừng bạn,"

Tôi đoán đó là điều tốt nhất tôi có thể nói. (cười khúc khích)

Vì vậy nếu điều này gây nhầm lẫn thì cũng không sao cả,

và chúng ta sẽ có rất nhiều bài tập

để thực sự tìm hiểu chính xác những gì đang diễn ra ở đây.

Bây giờ, trước khi chúng ta tiếp tục,

có một vài điểm tôi thực sự muốn nhấn mạnh.

Được rồi, đây là điểm số một.

Trước hết, khi chúng ta nghĩ về các biến số ở đây

và mọi thứ đang diễn ra với cấu trúc đó ngay bây giờ,

chúng tôi thực sự đang làm việc với hai loại biến khác nhau.

Một biến chứa những thứ trỏ đến một địa chỉ.

Vì vậy, nó sẽ giống như con trỏ thực sự của chúng ta,

jimPointer của chúng tôi ngay tại đây.

Đây là một địa chỉ bộ nhớ.

Và mặt khác,

chúng ta có các biến tạo ra giá trị thực tế,

và điều đó sẽ giống như Jim, ngay tại đây.

Vậy jim là một giá trị.

Bây giờ khi chúng ta bắt đầu nghĩ về địa chỉ

và chúng liên quan như thế nào đến các giá trị

rằng chúng được chứa bên trong,

hãy nhớ rằng đó là lý do tại sao chúng ta đang sử dụng ngôi sao đó

và toán tử dấu và.

Vì vậy, đây là các quy tắc.

Đây là quy tắc cần thực sự ghi nhớ.

Nếu bạn có một địa chỉ, vậy nếu bạn có một địa chỉ,

bạn có thể biến địa chỉ đó thành một giá trị

bằng cách nói ngôi sao và sau đó là địa chỉ hoặc con trỏ.

Nếu bạn có một giá trị, bạn có thể biến nó thành một địa chỉ

bằng cách viết giá trị ký hiệu.

Và đó chính xác là những gì chúng ta vừa thấy

trong đoạn mã của chúng tôi ngay tại đây.

Ngay tại đây, chúng ta có một giá trị,

chúng tôi biến nó thành một địa chỉ bộ nhớ hoặc một con trỏ

bằng cách viết &jim.

Và sau đó, đây cũng là con trỏ chính xác đó,

hoặc địa chỉ bộ nhớ chính xác đó,

và chúng tôi biến nó trở lại thành một giá trị

bằng cách viết ngôi sao và sau đó là con trỏ.

Vì vậy, đó là lời nhắc nhở lớn số một.

Và sau đó là lời nhắc nhở lớn thứ hai

là hiểu sự khác biệt

giữa khi chúng ta sử dụng ngôi sao đó trước một loại

hoặc trước một địa chỉ bộ nhớ.

Vì vậy, một lần nữa, bất cứ khi nào bạn nhìn thấy ngôi sao

tại một vị trí mà thông thường chúng tôi sẽ chỉ định một loại,

điều đó có nghĩa là, này, chúng tôi đang tìm kiếm một loại

đó là một dấu hiệu cho thấy điều này, cho một người,

một con trỏ tới một người.

Đó chính là biến con trỏ tới người.

Vì vậy, trong trường hợp này, ngôi sao không thực sự được nghĩ đến

với tư cách là người điều hành.

Chỉ khi chúng ta có địa chỉ bộ nhớ thực,

hoặc một con trỏ thực tế ngay tại đây,

toán tử sao biến nó trở lại thành một giá trị.

Được rồi, với tất cả những điều đó trong đầu,

điều đó giống như phép lặp số một thông qua con trỏ.

Hy vọng là nó không quá tệ, vì tôi có vài tin xấu.

Điều này giống như sửa đổi một trong những con trỏ, (cười khúc khích)

và thật không may trong cờ vây,

thực sự có một vài trường hợp đặc biệt

mà chúng ta thực sự, thực sự, thực sự cần phải nhận thức được.

Vì vậy chúng ta hãy nghỉ ngơi nhanh chóng.

Chúng ta sẽ quay lại trong phần tiếp theo,

chúng ta sẽ dọn dẹp mã một chút ở đây,

và tôi muốn nói về một điều gì đó, bạn biết đấy,

một hoặc hai bổ sung nhỏ.

Và sau đó chúng ta sẽ nói nhanh về một

của các trường hợp cạnh lớn xung quanh con trỏ

và cách họ được đối xử trong Go.

Vì vậy, hãy nghỉ ngơi nhanh chóng và chúng ta sẽ theo dõi trong phần tiếp theo.