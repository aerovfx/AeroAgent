# 005 Cấu trúc nhúng vi

---

Người hướng dẫn: Bây giờ chúng ta đã có một ý tưởng khá hay

về cách tạo một cấu trúc

và sau đó là cách chỉnh sửa một số giá trị bên trong nó.

Bây giờ chúng ta sẽ bắt đầu tìm kiếm

ở một số tính năng nâng cao hơn xung quanh cấu trúc,

đầu tiên là khả năng

để nhúng một cấu trúc bên trong một cấu trúc khác.

Vì vậy, chúng ta hãy xem một ví dụ về điều này.

Hiện tại, chúng ta có cấu trúc kiểu người này ở đây

ở phía bên trái, và chúng ta biết

rằng mọi người đều có họ và tên.

Hãy tưởng tượng trong giây lát rằng có thể chương trình của chúng ta

cũng cần liên kết một số thông tin liên lạc

với mỗi người,

và có thể bên trong thông tin liên lạc này,

hai mẩu thông tin chúng tôi muốn

để ghi lại sẽ là địa chỉ email của một người

và mã ZIP của họ.

Chà, chúng ta có thể tạo cấu trúc thứ hai ở đây,

do đó, một cấu trúc hoàn toàn tách biệt được gọi là thông tin liên hệ,

có thuộc tính email và mã ZIP.

Sau đó chúng tôi có thể nhúng cấu trúc thông tin liên hệ này vào người đó.

Vậy chúng ta có ý tưởng về một người, chúng ta có ý tưởng

của thông tin liên hệ và sau đó chúng tôi có thể lấy thông tin liên hệ

và nhúng nó vào người.

Vậy hãy viết mã ví dụ này

và xem chính xác nó trông như thế nào.

Quay lại bên trong tệp main.go của chúng tôi,

đầu tiên chúng ta sẽ bắt đầu

bằng cách khai báo đúng kiểu cấu trúc thứ hai

phía trên người mà chúng ta đã ghép lại với nhau.

Vì vậy, chúng tôi sẽ nói rằng loại thông tin liên hệ sẽ

trở thành một cấu trúc và sau đó chúng ta sẽ liệt kê

ra hai lĩnh vực khác nhau mà nó có.

Vì vậy chúng ta sẽ nói, trước hết

cấu trúc thông tin liên hệ có một email,

thuộc loại chuỗi và nó cũng có mã ZIP,

đó là kiểu int.

Nhân tiện, nếu bạn không quen với mã ZIP,

mã ZIP giống như một công cụ trợ giúp địa chỉ bưu điện tồn tại

ở Mỹ và một số nước khác.

Vì vậy, nếu bạn đến từ một quốc gia khác không có mã ZIP,

ồ, về cơ bản nó là một số có năm chữ số

điều đó chỉ giúp xác định chính xác vị trí của bạn.

Vậy bây giờ

mà chúng tôi đã tập hợp cấu trúc thông tin liên hệ riêng biệt này,

chúng ta có thể tự do tạo giá trị thông tin liên hệ

bên trong chức năng chính của chúng tôi.

Vì vậy chúng ta có thể tự do sử dụng

thông tin liên hệ của chính nó nhiều như chúng tôi muốn.

Nhưng với mục đích ứng dụng của chúng tôi, tôi nghĩ

điều đó có ý nghĩa nhất để nói

rằng mỗi người có một bản sao thông tin liên hệ.

Vì vậy bên trong con người chúng ta có cấu trúc ngay tại đây,

chúng tôi sẽ thêm vào một trường khác và chúng tôi sẽ gọi nó đơn giản là liên hệ,

và loại của nó sẽ là thông tin liên hệ.

Được rồi, đây là một ví dụ khá quan trọng

bởi vì nó cho chúng ta thấy rằng bên trong

của một cấu trúc, chúng tôi không bị giới hạn

chỉ những loại rất cơ bản mà chúng tôi có quyền truy cập

cho đến tất cả cùng, như chuỗi, int, float và Booleans.

Nhưng chúng ta cũng có thể lấy một loại tùy chỉnh

và sử dụng nó để xác định một loại tùy chỉnh khác.

Vậy bây giờ chúng ta hãy tìm hiểu chính xác

chúng ta sẽ tuyên bố một người như thế nào

đó cũng có một số thông tin liên lạc.

Tôi sẽ đi vào chức năng chính của chúng ta,

và tôi nghĩ tôi sẽ dọn sạch tất cả mã

mà chúng tôi có ở đây ngay bây giờ.

Vì vậy tôi sẽ làm nổi bật tất cả những thứ này,

và chúng ta sẽ thoát khỏi nó.

Bây giờ hãy tưởng tượng rằng chúng ta muốn khai báo một người mới,

và chúng ta sẽ gọi người mới này là Jim.

Bây giờ để khai báo người mới này, chúng ta sẽ bắt đầu

sử dụng cú pháp dấu ngoặc nhọn tương tự

mà chúng ta đã thấy trước đây.

Vì vậy, chúng ta sẽ bắt đầu bằng việc khai báo tên của Jim.

Hãy nhớ rằng khi chúng ta sử dụng cú pháp dấu ngoặc nhọn này

để thực sự tạo ra một giá trị kiểu người,

chúng ta phải sử dụng dấu phẩy.

Trong khi trước đây, ở đây về định nghĩa kiểu thực tế,

chúng tôi không cần phải làm vậy.

Vì vậy, sau cái tên Jim,

chúng tôi chắc chắn sẽ đặt dấu phẩy ngay tại đây.

Và sau đó chúng ta sẽ nói rằng Jim cũng có họ

của, tôi không biết, còn Đảng thì sao, ai quan tâm chứ?

Và bây giờ là lúc mọi thứ trở nên thú vị, tạo ra Jim

hoặc để tạo người này bằng thuộc tính liên hệ này,

chúng ta sẽ nói rằng liên hệ đó bây giờ sẽ là một cấu trúc mới

thuộc loại thông tin liên hệ.

Và vì vậy chúng ta sẽ đặt một cấu trúc mới

thuộc loại thông tin liên hệ ngay tại đây.

Vì vậy, thông tin liên hệ và chúng tôi sẽ khai báo nó

giống hệt như cách chúng tôi đã tuyên bố về người mới này.

Vì vậy, chúng ta sẽ nói thông tin liên hệ, chúng ta sẽ đặt dấu ngoặc nhọn,

và sau đó chúng tôi sẽ cung cấp

cả mã ZIP và thuộc tính email này.

Vì vậy, chúng ta sẽ nói rằng Jim có email là jim@gmail.com

và mã ZIP là 94, sao cũng được, 94.000 cũng được.

Được rồi, đây là một ví dụ tuyệt vời

của một cấu trúc nhúng bên trong một cấu trúc khác.

Và như tôi đã nói, chúng ta vẫn có thể tự do tạo cấu trúc

loại thông tin liên hệ nếu chúng tôi muốn.

Chúng tôi không chỉ giới hạn việc sử dụng chúng được nhúng bên trong

của một người, và vì vậy đây là một cách tuyệt vời để tận dụng

hoặc để sử dụng lại các cấu trúc phổ biến trên ứng dụng duy nhất của bạn.

Ví dụ: chắc chắn một người có thể có một số thông tin liên hệ,

nhưng có thể doanh nghiệp cũng có thông tin liên hệ.

Và có lẽ chúng ta cũng sẽ có một số loại

hoặc một chiếc xe tải nào đó, xin lỗi,

một số cấu trúc loại hình kinh doanh bên trong ứng dụng của chúng tôi

và chúng tôi cũng có thể nhúng thông tin liên hệ vào đó.

Vì vậy, bây giờ hãy thực hiện định dạng của chúng tôi.

Chúng tôi sẽ thực hiện in-F

và lấy toàn bộ cấu trúc của struct.

Vì vậy chúng ta sẽ tính phần trăm cộng V như trước.

Và sau đó, như lý lẽ thứ hai, chúng ta sẽ chuyển sang Jim.

Được rồi, vậy hãy lưu cái này lại.

Và có vẻ như tôi có thể mắc một lỗi đánh máy nhỏ ở đây.

À, rất tốt.

Vậy nên có một điều tôi đã bỏ lỡ,

và đây sẽ là một điều mà bạn sẽ quên

rất nhiều nếu bạn đến từ Ruby hoặc JavaScript,

bất cứ khi nào chúng ta khai báo các cấu trúc nhiều dòng như thế này,

vì vậy bạn sẽ nhận thấy cách chúng tôi xác định các thuộc tính của mình

tất cả trên các dòng riêng biệt.

Mỗi dòng phải có dấu phẩy,

ngay cả khi đó là khai báo thuộc tính cuối cùng,

hoặc loại giá trị thuộc tính tên thuộc tính cuối cùng.

Vì vậy ngay sau mã ZIP 94000, chúng ta sẽ đặt dấu phẩy

và sau dấu ngoặc nhọn đóng

đối với cấu trúc thông tin liên hệ của chúng tôi, chúng tôi cũng sẽ đặt dấu phẩy,

sau đó chúng tôi sẽ lưu và sau đó lỗi sẽ biến mất.

Rất tốt.

Được rồi, hãy chuyển sang trình soạn thảo mã của chúng tôi.

Chúng ta sẽ chạy cái này và bây giờ chúng ta có thể thoải mái thấy chúng ta có tên

của Jim, bên họ,

và bên trong cấu trúc chúng ta có thuộc tính contact

hoặc trường liên hệ của chúng tôi kèm theo email và mã ZIP.

Vì vậy, có vẻ như việc này đã diễn ra khá tốt.

Được rồi, đó chỉ là một phần nhỏ nữa thôi

của câu đố xung quanh các cấu trúc,

nhưng vẫn còn một số tính năng khác

mà tôi muốn nói đến.

Vậy hãy nghỉ ngơi nhanh chóng và quay trở lại

sang phần tiếp theo và xem qua

ở một số việc khác mà chúng ta có thể làm với cấu trúc.