# 021 Đọc từ ổ cứng vi

---

Người hướng dẫn: Bây giờ chúng ta đã ghép xong một hàm

để lưu một bộ bài vào một tập tin, đã đến lúc tập hợp lại với nhau

chức năng ngược lại trong đó chúng tôi sẽ loại bỏ một tập tin

của ổ cứng của chúng tôi và sau đó cố gắng biến nó trở lại

vào một bộ bài thực tế hoặc một danh sách các lá bài.

Vì vậy, hãy bắt đầu với nó.

Việc đầu tiên chúng ta cần làm là xem lại một số tài liệu

xung quanh gói ioutil mà chúng ta vừa sử dụng

trong video cuối cùng.

Vậy bên trong đây có một chức năng khác

mà chúng ta sắp sử dụng bây giờ

để đọc một tập tin từ ổ cứng.

Và nó được đặt tên rất hợp lý là ReadFile.

Vì vậy, chúng tôi có thể kiểm tra tài liệu cho nó.

Chúng tôi gọi ReadFile, chúng tôi chỉ định tên của tệp

mà chúng tôi muốn mở dưới dạng một chuỗi,

và đổi lại chúng ta sẽ quay trở lại

một lát byte khác và một đối tượng lỗi.

Bây giờ chúng ta sẽ nói một chút về đối tượng lỗi này

chỉ trong chốc lát, nhưng ngay bây giờ

hãy tập trung vào lát byte.

Hãy nhớ rằng bất cứ khi nào chúng ta nhìn thấy một lát byte

chúng tôi muốn nghĩ về một chuỗi.

Vì vậy sau khi chúng ta đọc một tập tin từ ổ cứng

chúng ta sẽ lấy lại một chuỗi ký tự,

về cơ bản là danh sách các thẻ được phân tách bằng dấu phẩy.

Vì vậy, việc chia chuỗi đó sẽ tùy thuộc vào chúng ta

bởi tất cả các dấu phẩy ở giữa mỗi thẻ

và sau đó biến nó trở lại thành một bộ bài thực sự.

Vì vậy, hãy bắt đầu với nó.

Trong trình soạn thảo mã của tôi, tôi sẽ tạo một hàm khác

ở dưới cùng của tập tin,

chúng ta sẽ gọi cái này là newDeckFromFile

để chỉ ra rất rõ ràng,

này, cái này sẽ cung cấp cho bạn một bộ bài từ một tập tin.

(bấm bàn phím)

Bây giờ một lần nữa, chúng ta sẽ nghĩ về chữ ký hàm

đây một chút.

Tôi không nghĩ chúng ta cần bất kỳ máy thu nào

vào chức năng vì này, chúng tôi chưa có bộ bài.

Bạn biết đấy, nếu chúng ta gọi thứ này là,

rất có thể đó là vì chúng ta muốn có quyền truy cập vào một bộ bài.

Vì vậy tôi nghĩ rằng chúng ta cần phải chuyển tiếp

làm đối số cho hàm, tên của tệp

mà chúng ta muốn thử mở ra và biến thành một bộ bài.

Và vì vậy hãy đón nhận điều đó

như một đối số mà chúng tôi sẽ gọi tên tệp

và chúng tôi sẽ chú thích điều đó bằng kiểu chuỗi.

Bây giờ, sau khi gọi newDeckFromFile,

không còn nghi ngờ gì nữa, kỳ vọng là nhận lại một bộ bài.

Vì vậy tôi nghĩ rằng kiểu trả về của chúng ta ở đây sẽ là kiểu deck.

Được rồi, bây giờ chúng ta đến phần thú vị

nơi chúng tôi thực sự sẽ gọi

chức năng ReadFile đó ở đây.

Vì vậy, một lần nữa, lưu ý rằng chúng ta lấy lại một lát byte

và một đối tượng lỗi bất cứ khi nào chúng ta gọi ReadFile.

Vì vậy, hãy thiết lập lệnh gọi hàm.

Chúng tôi sẽ nói ioutil vì đó là gói

mà chúng tôi đang gọi hàm ReadFile này.

Và chúng ta sẽ nói ReadFile, chúng ta sẽ chuyển tên tệp

mà chúng tôi nhận được như một đối số.

Và sau đó hãy nhớ, ReadFile trả về cả một lát byte

and an error if one occurred.

Vậy là chúng ta đã trải qua quá trình

đã nhận được hai đối số riêng biệt từ một hàm.

Hãy nhớ rằng chúng ta chỉ liệt kê hai biến

mà chúng ta muốn gán những giá trị này.

Vì vậy chúng ta sẽ dán lát byte

được trả về từ ReadFile thành một biến

mà chúng ta sẽ gọi là bs, viết tắt của byte slice,

và sau đó là đối tượng lỗi

chúng ta sẽ gán cho một biến mà chúng ta gọi là err,

viết tắt của lỗi.

Và sau đó hãy nhớ rằng những

thực sự là khởi tạo có thể thay đổi ngay tại đây.

Vì vậy chúng ta phải sử dụng cú pháp bằng dấu hai chấm để gán.

Được rồi, vậy là bây giờ chúng ta đã có lát byte,

đó là chuỗi ký tự

hoặc chuỗi thẻ được phân tách bằng dấu phẩy,

và chúng ta có đối tượng lỗi.

Vậy bây giờ chúng ta hãy nói về

đối tượng lỗi ở đây là gì.

Được rồi, tôi sẽ vẽ sơ đồ.

Bắt đầu nào.

Được rồi, chúng ta vừa gọi ReadFile

và về cơ bản chúng tôi đã quay trở lại,

lát byte của chúng tôi và một đối tượng lỗi.

Vì vậy, đây là một giá trị lỗi loại.

Nếu có lỗi xảy ra trong quá trình ReadFile

lỗi này sẽ được phổ biến.

Nói cách khác, sẽ có một giá trị thực sự bên trong nó.

Nhưng nếu mọi việc diễn ra đúng

với việc đọc tập tin từ ổ cứng

thì giá trị lỗi ở đây sẽ bằng không.

Vậy nil là một giá trị trong Go

về cơ bản có nghĩa là không có giá trị,

hoặc thứ này không có giá trị,

không có giá trị nào được chứa ở đây.

Và một mô hình rất phổ biến mà chúng ta sắp thấy

với rất nhiều mã Go

ngay sau khi quay lại

đối tượng lỗi có thể là gì,

vì vậy nói cách khác, điều này có thể chứa giá trị lỗi

hoặc có thể là 0, chúng ta thường đặt câu lệnh if

ngay sau đó và kiểm tra xem lỗi có bằng không hay không.

Vì vậy, chúng tôi sẽ nói nếu lỗi không bằng 0

sau đó thực thi mã này bên trong đây.

Nhân tiện, tôi nghĩ đây là lần đầu tiên

chúng tôi thực sự đã thấy một câu lệnh if,

nhưng giống như nhiều thứ khác với Go,

nó chỉ là một câu lệnh if thông thường,

thực sự không có sự khác biệt so với các ngôn ngữ lập trình khác

mà có lẽ bạn đã quen.

Vì vậy chúng tôi đặt từ khóa if,

chúng tôi đặt ra điều kiện để kiểm tra

và sau đó là một bộ dấu ngoặc nhọn chỉ được thực thi,

hoặc tất cả mã bên trong của bạn sẽ chỉ được thực thi,

nếu tuyên bố này đánh giá một giá trị thực sự.

Vậy bên trong đây là nơi chúng ta sẽ tập hợp lại

một chút xử lý lỗi.

Vì vậy chúng ta sẽ chỉ vào bên trong đây

nếu có lỗi được trả về từ lệnh gọi ReadFile.

Nếu không lỗi sẽ bằng không

và chúng ta sẽ bỏ qua hoàn toàn câu lệnh if này.

Bây giờ việc xử lý lỗi bằng Go là một việc khó khăn

bởi vì nó thực sự đi xuống

đến lỗi rất cụ thể đã xảy ra

để quyết định phải làm gì ở đây.

Ví dụ, hãy tưởng tượng rằng vì lý do nào đó

đã xảy ra lỗi trong cuộc gọi ReadFile này,

kiểu như có thể chúng tôi đã cố đọc một tập tin không tồn tại

trên ổ cứng.

Nếu đúng như vậy, thì nếu chúng ta quay lại thì hoàn toàn không có gì

từ lệnh gọi ReadFile, như lát byte hoàn toàn trống,

Tôi muốn hỏi bạn câu hỏi ở đây.

Cá nhân bạn nghĩ chương trình của chúng ta nên làm gì?

Giống như, chúng tôi gọi hàm này là newDeckFromFile,

nhưng chúng tôi đang nói rằng này,

chúng ta thực sự có thể lấy được một bộ bài từ tập tin này.

Vậy chúng ta nên làm gì trong trường hợp có sự cố xảy ra ở đây?

Bất cứ khi nào bạn đang cố gắng tìm hiểu

cách xử lý lỗi với Go,

Tôi khuyên bạn nên áp dụng

câu hỏi rất thông thường đó

và tự hỏi bản thân, "Này, nếu có chuyện gì xảy ra ở đây

"Tôi thực sự muốn điều gì xảy ra?"

Và đối với cá nhân tôi, tôi nghĩ

rằng có lẽ có hai lựa chọn khả thi

mà chúng ta có thể làm ngay tại đây

nếu có điều gì đó thực sự, thực sự không ổn.

Hoặc chúng ta có thể nói tùy chọn số một, ghi lại lỗi.

Vì vậy, về cơ bản hãy in nó ra và gọi lại newDeck.

(nhấp chuột máy tính)

Vì vậy, đây sẽ là lựa chọn số một.

Và đây chỉ là một lựa chọn mà tôi đưa ra,

Tôi không nói đó là sự lựa chọn đúng đắn

Tôi chỉ nói rằng đó là một cách chúng ta có thể giải quyết chuyện này.

Vì vậy, nếu có sự cố xảy ra trong khi chúng ta đang đọc một tập tin

tắt ổ cứng, một điều chúng ta có thể làm

là in ra lỗi xảy ra

để chúng tôi, với tư cách là nhà phát triển, biết rằng đã xảy ra sự cố.

Nhưng sau đó để đảm bảo rằng hàm newDeckFromFile của chúng tôi

vẫn thực sự trả về một số bộ bài có thể sử dụng được,

chúng ta có thể gọi hàm newDeck của mình,

điều mà bạn và tôi biết rất rõ, sẽ luôn trả lại một bộ bài.

Nói cách khác, chúng ta có thể nói ở đây,

à nếu chúng ta không tải được một bộ bài ra khỏi ổ cứng

ít nhất hãy cho ai gọi hàm này

một bộ bài để thực sự làm việc.

Và đó chỉ là một lựa chọn khả thi, bạn biết đấy,

đó là một cách chúng ta có thể thực hiện việc này.

Bây giờ, lựa chọn khác mà chúng ta có thể thực hiện là nói,

bạn biết không, nếu chúng ta đang cố gắng đọc một bộ bài

từ ổ cứng và nó hoàn toàn thất bại

và chúng tôi không thể có được nó,

điều đó có thể có nghĩa là có điều gì đó cực kỳ không ổn

với chương trình của chúng tôi và có lẽ chúng tôi chỉ nên giả định

rằng chúng tôi không muốn làm bất cứ điều gì khác

và chúng ta nên thoát khỏi chương trình hoàn toàn.

Vì vậy, tùy chọn hai sẽ là ghi lại lỗi

và thoát hoàn toàn khỏi chương trình.

Vì vậy, đây thực sự là hai lựa chọn của chúng tôi theo như tôi thấy.

Hai cách mà chúng ta có thể xử lý lỗi này.

Một lần nữa, bất cứ khi nào bạn xử lý lỗi với Go

Tôi thực sự khuyên bạn chỉ nên áp dụng những điều này

loại câu hỏi thông thường

về điều bạn nghĩ là điều tốt nhất đã xảy ra

là bất cứ khi nào có điều gì đó không ổn.

Bây giờ đối với chúng tôi, tôi nghĩ rằng chúng tôi sẽ thực hiện

lựa chọn số hai ngay tại đây.

Chúng ta sẽ nói điều đó nếu có chuyện gì xảy ra

với việc đọc một tập tin từ ổ cứng,

điều đó có lẽ có nghĩa là có điều gì đó

chỉ là sai lầm thảm khốc.

Giống như chúng ta nghĩ có một cái boong ở đó,

chúng tôi nghĩ rằng có một bộ bài có tên tập tin nhất định,

nhưng hình như không có,

có điều gì đó thực sự tồi tệ đang xảy ra,

vì vậy hãy nói, "Này, chúng tôi không thể tải tệp

"Xong rồi, đưa chúng tôi ra khỏi đây, thoát khỏi chương trình."

Vì vậy, trước tiên chúng ta sẽ ghi nhật ký bảng điều khiển hoặc không phải nhật ký bảng điều khiển,

nhưng chúng ta sẽ in ra giá trị lỗi ngay tại đây,

để chúng tôi, với tư cách là nhà phát triển, biết chính xác điều gì đã xảy ra

và chúng ta có thể xem lại nó và nói,

"Ồ, tôi đoán chúng ta đã đặt một tên tập tin xấu

"hay gì đó tương tự."

Vì vậy chúng ta sẽ nói fmt.Println

và sau đó chúng ta sẽ chuyển vào đối tượng lỗi đó.

Bây giờ là một mẫu mà tôi thực sự thích làm

là viết lỗi và sau đó là dấu phẩy như vậy,

để chúng tôi thấy lỗi văn bản

và nó thực sự rõ ràng,

này, đây là một lỗi mà chúng tôi đang in ra.

Bây giờ thông báo lỗi thực tế có thể cũng sẽ có nội dung:

như "Đây là lỗi" hay gì đó.

Nhưng bằng cách nhập "Lỗi:" thì nó thực sự rõ ràng

này, đây là thông báo lỗi để xem xét.

Và ngay sau đó

chúng ta có thể thoát khỏi chương trình hoàn toàn

bằng cách sử dụng gói thư viện chuẩn Go khác

được gọi là gói os.

Và vì vậy chúng ta sẽ kiểm tra tài liệu

xung quanh nó thật nhanh chóng.

Tôi sẽ quay lại danh sách tài liệu của mình,

vì vậy đây là tất cả các gói của chúng tôi.

Và tôi sẽ tìm kiếm gói os

và có một vài trường hợp của os, bắt đầu nào.

Vì vậy, mô tả về gói này, về cơ bản,

giao diện độc lập với nền tảng với hệ điều hành.

Và vì vậy cho dù bạn có đang chạy hay không

chương trình Go của bạn trên Windows, trên bản phân phối Linux,

hoặc Mac OS, đây là một số chức năng

điều đó sẽ hoạt động tốt như nhau

trên tất cả các hệ điều hành khác nhau.

Vì vậy, nếu chúng ta cuộn xuống chỉ mục ngay tại đây, bạn sẽ thấy

rằng một trong những chức năng khả thi mà chúng ta có thể gọi là Thoát.

Vì vậy nếu chúng ta gọi Thoát, theo quy ước

nếu chúng ta gọi nó và đưa ra một đối số bằng 0

điều đó có nghĩa là chương trình của chúng tôi đã chạy thành công.

Nhưng nếu chúng ta chuyển vào bất kỳ giá trị nào ngoài số 0

điều đó có nghĩa là, ồ, nó sẽ chỉ ra

rằng đã xảy ra sự cố khi chúng tôi đang chạy chương trình.

Và về cơ bản tôi nghĩ chúng ta có thể gọi hàm Thoát này là

chuyển mã lỗi như, một và điều đó sẽ cho biết

rằng đã xảy ra lỗi với chương trình của chúng tôi.

Vì vậy hãy quay lại bên trong trình soạn thảo mã của chúng tôi

chúng ta sẽ gọi os.Exit và chuyển vào giá trị 1.

Bây giờ hãy nhớ rằng, khi bạn lưu tệp bên trong VS Code,

os là gói mà chúng ta cần nhập

và vì vậy VS Code sẽ đảm nhiệm việc này

trong số đó được nhập tự động cho chúng tôi ở trên cùng.

Nhưng nếu bạn đang sử dụng bất kỳ trình soạn thảo mã nào khác,

nhớ ghi bản import của os lên đây nhé.

Được rồi, vậy là có khá nhiều thứ được xử lý

trường hợp xử lý lỗi của chúng tôi ở đây.

Chúng tôi đang nói rằng nếu có gì sai sót

trong khi đọc tập tin này từ ổ cứng,

này, chắc chắn đó là một lỗi nghiêm trọng,

hãy đăng xuất xem đã xảy ra chuyện gì

và sau đó thoát khỏi chương trình hoàn toàn.

Sau chuyện này, nếu chúng ta vượt qua được vụ án này ngay tại đây

điều đó có nghĩa là chúng ta chắc hẳn đã đọc thành công thứ gì đó

tắt ổ cứng.

Và vì vậy chúng ta phải có một giá trị

bên trong lát byte này ngay tại đây

mà chúng ta cần biến thành một bộ bài thực sự.

Vậy chúng ta hãy nghỉ ngơi nhanh thôi,

chúng ta sẽ tiếp tục trong phần tiếp theo

và chúng ta sẽ tìm ra chính xác cách chúng ta sẽ thực hiện

lát byte này và biến nó thành một bộ bài.

Vậy tôi sẽ gặp bạn sau một phút nữa.