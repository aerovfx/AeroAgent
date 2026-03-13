# 005 Cấu trúc nhúng vi

---

Bây giờ, chúng tôi đã có một ý tưởng khác hay về cách tạo một cấu trúc và sau đó là cách chỉnh sửa một số giá trị

trong đó.

Bây giờ chúng ta sẽ bắt đầu xem xét một số tính năng nâng cao hơn xung quanh cấu trúc, tính toán

khả năng đầu tiên là khả năng nhúng một cấu trúc này vào bên trong các cấu trúc khác.

Vì vậy, chúng ta hãy xem một ví dụ về điều này.

Vì vậy, hiện tại, chúng tôi có cấu trúc này ở bên trái và chúng tôi

biết rằng mỗi người đều có tên và họ.

Hãy tưởng tượng một chút rằng chương trình của chúng ta có thể cần liên kết một số thông tin liên kết

hệ với mọi người và có thể có trong liên hệ thông tin này.

Hai phần thông tin mà chúng tôi muốn ghi lại sẽ là email địa chỉ của một người và mã zip của họ.

Chà, chúng tôi có thể tạo một cấu hình thứ hai ở đây.

Vì vậy, một cấu trúc được phân tách hoàn toàn được gọi là thông tin liên hệ có thuộc tính email và zip mã hóa.

Sau đó, chúng tôi có thể nhúng cấu trúc liên hệ thông tin này vào người.

Vì vậy, chúng tôi có ý tưởng về một người, chúng tôi có ý tưởng về thông tin liên hệ và sau đó chúng tôi

có thể lấy liên hệ thông tin và nhúng nó vào đó.

Vì vậy, hãy viết mã ví dụ này và xem chính xác nó như thế nào.

Quay lại bên trong tệp chính của chúng tôi.

Trước đó, chúng tôi sẽ bắt đầu bằng cách khai báo cấu trúc thứ hai kiểu ngay trên người mà chúng tôi đã có

set together.

Vì vậy, chúng tôi sẽ nói rằng loại thông tin liên hệ sẽ là một cấu trúc và sau đó chúng tôi sẽ liệt kê hai trường

khác nhau mà nó có.

Vì vậy, trước tiên chúng ta sẽ nói rằng cấu trúc thông tin liên hệ có email thuộc loại chuỗi và nó

cũng có loại mã zip thuộc tính int.

Nhân tiện, nếu bạn không thuộc về mã zip, mã zip tương tự như một công cụ trợ giúp địa chỉ

bưu điện tồn tại ở Hoa Kỳ và một số quốc gia khác.

Vì vậy, nếu bạn đến từ một số quốc gia khác mà không có mã zip, về cơ bản thì có một số năm

chữ số giúp xác định chính xác vị trí của bạn.

Vì vậy, hiện tại chúng tôi đã tổng hợp cấu trúc thông tin liên hệ đặc biệt này, chúng tôi có thể tự động tạo

một liên hệ thông tin có giá trị với chức năng chính của mình để chúng tôi có thể tự động sử dụng liên hệ thông tin

theo ý mình.

Nhưng đối với mục tiêu ứng dụng của chúng tôi, tôi nghĩ rằng điều hợp lý nhất khi nói rằng mỗi

người có một liên hệ thông tin bản sao.

Vì vậy, bên trong cấu trúc của chúng tôi ngay tại đây sẽ bổ sung vào một trường khác và chúng tôi sẽ gọi nó đơn

đơn giản là liên hệ và loại của nó sẽ là thông tin liên hệ.

Vì vậy, đây là một ví dụ khá quan trọng vì nó cho chúng ta thấy rằng trong một cấu hình

architecture, chúng ta không giới hạn những loại cơ bản mà chúng ta đã có quyền truy cập, như string, float và boolean.

Nhưng họ cũng có thể lấy một tùy chỉnh loại và sử dụng nó để xác định một tùy chỉnh loại khác.

Vì vậy, bây giờ chúng tôi hãy tìm kiếm chính xác cách chúng tôi sẽ khai báo một người cũng có một số liên hệ thông tin.

Tôi sẽ đi xuống các chức năng chính của chúng tôi và tôi nghĩ tôi sẽ xóa tất cả mã hóa mà chúng tôi có

ở đây ngay bây giờ.

Vì vậy, tôi sẽ làm nổi bật tất cả những thứ này và chúng tôi sẽ loại bỏ nó.

Vì vậy, bây giờ hãy tưởng tượng rằng chúng tôi muốn khai báo một người mới và chúng tôi sẽ gọi người này là người mới.

Jim Bây giờ để khai báo người mới này, chúng ta sẽ sử dụng cùng một loại cú pháp nền tảng mà chúng ta đã có

đã thấy trước đây.

Vì vậy, chúng tôi sẽ bắt đầu bằng cách khai báo tên của Jim.

Hãy nhớ rằng khi chúng tôi đang sử dụng cú pháp nền tảng này để thực sự tạo ra một giá trị cho loại người,

chúng ta phải sử dụng comcom.

Trong khi ở đây về định nghĩa loại thực tế, chúng ta không cần phải làm như vậy.

Vì vậy, sau cái tên đầu tiên Jim, chúng tôi chắc chắn sẽ đặt một bình comma ngay tại đây.

Và sau đó chúng ta sẽ nói rằng Jim cũng có họ là Bữa tiệc thế nào?

Ai quan tâm?

Bây giờ đây là nơi mà mọi thứ trở về nên thú vị để tạo ra Jim hoặc tạo ra người này với thuộc tính liên hệ này.

Chúng tôi sẽ nói rằng địa chỉ liên hệ bây giờ sẽ là một cấu trúc mới của các loại liên hệ thông tin và vì vậy chúng tôi sẽ làm như vậy

thiết lập cấu trúc mới của loại thông tin liên hệ ngay tại đây.

Vì vậy, thông tin liên hệ và chúng tôi sẽ khai báo theo đúng cách mà chúng tôi đã khai báo người mới này.

Vì vậy, hãy nói thông tin liên hệ.

Chúng tôi sẽ đặt dấu ngoặc và sau đó chúng tôi sẽ cung cấp cả email mã zip và thuộc tính.

Vì vậy, chúng tôi sẽ nói rằng Jim có một email của Jim tại gmail. com và một zip mã hóa bao gồm chín cho bất cứ thứ gì, 94.000 cái hoạt động

được.

Vì vậy, đây là một ví dụ tuyệt vời về một cấu trúc được nhúng bên trong một cấu trúc khác.

Và như tôi đã nói, chúng tôi vẫn có thể tự động tạo liên kết loại thông tin cấu trúc nếu chúng tôi muốn.

Chúng tôi không giới hạn việc sử dụng chúng được gắn vào một người.

Và vì vậy, đây là một cách tuyệt vời để sử dụng hoặc sử dụng lại các biến phổ cấu trúc trên ứng dụng duy nhất của bạn,

limit.

Chắc chắn, một người có thể có một số liên hệ thông tin, nhưng có thể là một doanh nghiệp cũng có liên hệ thông tin, vì vậy

có thể chúng tôi cũng sẽ có một số loại hoặc một số xe tải, xin lỗi, một số loại cấu trúc doanh nghiệp bên trong ứng dụng của chúng tôi và chúng tôi

có thể nhúng liên hệ thông tin vào bên trong đó nữa.

Vì vậy, hiện tại chúng tôi sử dụng định dạng của chúng tôi, chúng tôi sẽ thực thi trong F và lấy toàn bộ cấu trúc của

struct vì vậy chúng tôi sẽ thực hiện cùng một phần trăm cộng với V như trước và sau đó với các đối số thứ hai, chúng tôi sẽ chuyển vào.

Jim.

Được rồi, vậy hãy lưu lại cái này.

Và có vẻ như tôi có thể có một máy đánh lỗi nhỏ ở đây.

Rất tốt.

Vì vậy, một điều mà tôi đã bỏ lỡ, và đây sẽ là một điều mà bạn

Sẽ quên rất nhiều nếu bạn đến từ Ruby hoặc JavaScript bất cứ khi nào chúng tôi khai báo cấu trúc nhiều dòng như thế này.

Vì vậy, bạn sẽ nhận ra cách chúng tôi xác định tất cả các thuộc tính của mình trên các dòng riêng biệt.

Mỗi dòng phải có dấu comma, ngay khi đó là phần khai báo thuộc tính cuối cùng hoặc loại giá trị thuộc tính

tính toán cuối cùng của tài sản tên.

Vì vậy, ngay sau mã zip 94.000 sẽ đặt một dấu comma và sau đó theo dấu ngoặc đóng cho cấu trúc thông tin liên hệ

của chúng tôi, chúng tôi cũng sẽ đặt một comma và chúng tôi sẽ lưu lại và sau đó các mũi tên bị mất.

Rất tốt.

Vì vậy, hãy chuyển sang trình soạn thảo của chúng tôi.

Chúng tôi sẽ tiến hành điều này và bây giờ chúng tôi có thể thoải mái tìm thấy chúng tôi có tên đầu tiên của Jim LastName.

Và bên trong cấu trúc, chúng tôi có các thuộc tính liên hệ hoặc trường liên hệ của chúng tôi với email và mã zip.

Vì vậy, có vẻ như công việc này diễn ra khá tốt.

Vì vậy, đó chỉ là một phần nhỏ của câu đố xung quanh cấu trúc.

Nhưng vẫn còn một số tính năng khác mà tôi muốn nói đến.

Vì vậy, chúng tôi tạm dừng một chút, quay lại trong phần tiếp theo và xem xét một số điều khác mà chúng

ta có thể làm cấu trúc.