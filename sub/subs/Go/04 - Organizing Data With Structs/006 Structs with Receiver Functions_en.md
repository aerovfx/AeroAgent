# 006 Cấu trúc có chức năng nhận vi

---

Giáo viên: Ở phần cuối,

chúng tôi đã tìm ra cách tạo một cấu trúc mới

và sau đó nhúng nó vào một cái hiện có.

Vì vậy chúng tôi đã tạo contactInfo,

sau đó chúng tôi đã thêm tên trường liên hệ mới cho người đó

và chúng tôi đã nói rằng trường liên hệ

sẽ luôn có giá trị contactInfo.

Sau đó, khi chúng tôi tạo ra một người, chúng tôi nói,

được rồi, đây là trường liên hệ của chúng tôi

và đây là thông tin liên hệ để sử dụng cho nó.

Bây giờ vẫn còn vài điều

Tôi muốn cho bạn thấy xung quanh các cấu trúc,

và phần đầu tiên là một phần nhỏ cuối cùng của, đại loại là,

những câu đố xung quanh việc tạo một cấu trúc nhúng như chúng ta vừa làm.

Vì vậy chúng tôi đã nói

rằng chúng tôi có tên trường liên hệ ngay tại đây

và loại của nó được cho là contactInfo.

Bây giờ tôi muốn chỉ cho bạn một cách khác để nhúng cấu trúc

điều đó gần như tương đương,

nó chỉ là cú pháp hơi khác một chút.

Vì vậy nếu muốn chúng ta có thể bỏ tên trường ngay tại đây.

Chúng tôi có thể xóa liên hệ và chúng tôi có thể nói một cách đơn giản là contactInfo.

Bây giờ cái này làm gì

nó vẫn khai báo tên trường của thông tin liên hệ

và nó cũng nói

rằng nó phải có một loại, contactInfo.

Nói cách khác, chỉ sử dụng contactInfo ngay tại đây

tương đương một trăm phần trăm với việc nói

contactInfo là tên trường

và nó có một loại contactInfo.

Tôi biết đó là một trò uốn lưỡi.

Vì vậy hãy để nó ở contactInfo

và xem chúng ta sẽ thực sự tận dụng điều này như thế nào.

Vì vậy tôi sẽ để lại contactInfo ngay tại đây.

Và bên trong tác phẩm Jim của chúng tôi,

thay vì khai báo tên trường của liên hệ

và gán nó contactInfo,

chúng ta sẽ nói contactInfo lẽ ra phải là

thuộc loại contactInfo.

Tôi biết tôi đang nói điều đó rất nhiều.

Được rồi, hãy lưu cái này lại và kiểm tra nó.

Vì vậy, về cơ bản tất cả những gì chúng tôi đã làm là đổi tên một trường đó

để chúng ta không phải nói liên lạc, liên lạc.

Bạn biết đấy, chúng ta chỉ đang tiết kiệm cho mình một số lần nhấn phím ở đây.

Đó là tất cả những gì chúng tôi thực sự đang làm.

Vì vậy, hãy kiểm tra nó một lần nữa.

Và bạn sẽ nhận thấy, được thôi,

đây là tên trường, vẫn là contactInfo,

và nó có giá trị kiểu contactInfo.

Được rồi, bây giờ điều đó có vẻ

giống như một chuyện vặt vãnh không quan trọng

nhưng điều đó thực sự sẽ trở nên quan trọng sau này

đặc biệt là khi chúng ta nói về

sử dụng lại một số mã thực sự với Go.

Vì vậy tôi muốn bạn, đại loại là, lưu lại thông tin nhỏ này đi

rằng chúng ta thực sự không phải chỉ định tên trường ở đây

nếu chúng ta không muốn.

Được rồi, vậy chúng ta hãy tiếp tục.

Có một điều cuối cùng tôi muốn xem xét,

hơi nhanh chóng, xung quanh các cấu trúc.

Bên trong ứng dụng bộ bài của chúng tôi hoặc ứng dụng thẻ bài,

bạn sẽ nhớ lại điều đó khi chúng tôi tạo ra loại bộ bài mới đó

sau đó chúng tôi thiết lập một số chức năng

đã lấy bộ bài làm máy thu.

Và kết quả của việc đó là chúng tôi có thể viết mã

trông giống như,

bạn biết đấy, cards.shuffle hoặc những gì bạn có.

Và vì vậy chúng ta có thể thiết lập cùng loại chức năng

cũng có máy thu với cấu trúc.

Vì vậy, hãy tạo một chức năng mới

điều đó sẽ đưa một người, như Jim, làm người nhận,

và có lẽ chúng ta sẽ in ra tất cả các chi tiết

của người đó.

Vì vậy, chúng ta sẽ phải, gần như chạm tới ký ức của mình ở đây

và hãy nhớ cách chúng ta tạo ra các hàm sử dụng bộ thu.

Bên dưới chức năng chính của chúng tôi,

chúng ta sẽ viết ra func,

sau đó chúng tôi sẽ viết ra người nhận.

Vậy đây sẽ là p người,

có nghĩa là bạn có thể gọi hàm này

mà chúng ta sắp xác định trên bất kỳ loại nào

hoặc bất kỳ giá trị nào của loại người.

Và sau đó bên trong phần thân của hàm này

bạn có thể gọi người đó là biến P.

Vì vậy chúng ta sẽ đặt tên cho thứ này,

còn việc chỉ in thì sao.

Và vì vậy, về cơ bản chúng ta sẽ nói,

chính xác những gì chúng tôi đang làm ở đây

bằng câu lệnh Printf.

Vì vậy chúng ta sẽ cắt dòng này và dán nó vào đây.

Và tất nhiên, thay vì cố gắng in ra Jim,

chúng tôi muốn in người được đưa vào hàm này.

Vì vậy chúng ta sẽ nói đối số thứ hai Printf của P.

Được rồi, bây giờ bên trong chức năng chính của chúng ta

chúng ta có thể thoải mái gọi jim.print.

Cụ thể là vì chúng ta mới setup chức năng này

với loại người là người nhận và Jim là một người.

Được rồi, hãy lưu cái này lại

và kiểm tra nó và xem chúng tôi đang làm như thế nào.

Vì vậy, tôi sẽ lưu tập tin, chúng ta sẽ lật lại,

và được rồi, có vẻ tốt.

Bây giờ có một điều cuối cùng tôi muốn làm với cấu trúc này

nó rất giống với thứ máy thu này ở đây

điều đó sẽ dẫn dắt chủ đề tiếp theo của chúng ta rất tốt đẹp, được chứ?

Vì vậy chủ đề tiếp theo mà chúng ta sẽ thảo luận

sẽ hơi choáng váng một chút,

nhưng chúng ta sẽ tập hợp một đoạn mã nhỏ ngay bây giờ

điều đó sẽ có tác dụng hơi bất ngờ một chút, được chứ?

Hoặc có thể nó sẽ hoạt động chính xác như bạn mong đợi, chúng ta sẽ xem.

Hãy viết mã ra và chúng ta sẽ xem điều gì sẽ xảy ra.

Vì vậy, tôi muốn tạo một chức năng khác gọi là...

thế còn thứ gì đó như, updateName.

Được rồi, tôi muốn viết một hàm tên là updateName

điều đó coi một người là người nhận

và sau đó cập nhật thuộc tính tên của người đó.

Vì vậy, hãy thử điều này.

Tôi sẽ nói vui vẻ nhé mọi người,

tên hàm sẽ là updateName,

và sau đó có thể chúng ta sẽ có tên mới.

Vì vậy chúng ta sẽ gọi nó một cách rõ ràng là newFirstName

đó phải là một chuỗi.

Vì vậy chúng ta sẽ nói p.firstName = newFirstName như vậy.

Được rồi, vậy là chúng ta vừa khai báo hàm này, updateName.

Nó có một máy thu kiểu người

và chúng ta phải gọi nó bằng newFirstName.

Và khi chúng tôi làm vậy, nó sẽ cập nhật tên của người đó.

Vậy hãy gọi điều này là Jim

và hãy đặt cho Jim một cái tên mới

và xem điều gì sẽ xảy ra.

Vì vậy chúng ta sẽ nói jim.updateName

và chúng ta sẽ đặt cho anh ấy một cái tên mới là...

còn Jimmy thì sao?

Được rồi, tôi muốn bạn ngồi xuống một lát

và tôi muốn bạn xem mã

mà chúng tôi vừa viết ở đây.

Tôi muốn bạn nhìn vào chức năng này,

và tôi muốn bạn đưa ra ý kiến ngay bây giờ.

Khi chúng tôi chạy mã này,

bạn nghĩ chính xác điều gì sẽ xảy ra?

Được rồi? Tôi muốn bạn nghĩ về nó

trong một giây.

Hãy nghĩ xem điều gì sẽ xảy ra khi chúng ta thực hiện điều này.

Tôi có thể đảm bảo với bạn rằng nó sẽ chạy được,

như thể chúng ta sẽ không gặp lỗi,

nhưng tôi chỉ muốn bạn làm vậy, đại loại là,

có được một số ý tưởng về những gì bạn nghĩ sẽ xảy ra.

Được rồi? Và khi bạn có ý tưởng đó,

chúng ta sẽ chuyển sang thiết bị đầu cuối

và chúng ta sẽ chạy lại chương trình của mình.

Vì vậy, khi chúng tôi chạy chương trình của mình,

bạn sẽ nhận thấy rằng chúng tôi có tên ở đây là Jim.

Bây giờ điều đó có thể thú vị một chút với bạn

bởi vì trên dòng này ngay tại đây

chúng tôi đang nói hãy bắt Jim, chuyển anh ấy vào tên cập nhật,

vậy Jim sẽ là người ở đây,

và đặt cho Jim một cái tên hoàn toàn mới,

như cập nhật thuộc tính tên đầu tiên đó.

Và ngay sau đó chúng tôi in lại Jim.

Vì vậy đối với tôi có vẻ như

như khi chúng tôi in Jim ra đây,

chúng tôi vừa cập nhật tên anh ấy thành Jimmy,

nhưng rõ ràng, như chúng ta vừa thấy khi in nó ra,

có vẻ như bản cập nhật đó không có hiệu lực,

nó không hề ổn chút nào.

So this is an actually very interesting part of Go

và nó sẽ rất phù hợp với chủ đề lớn tiếp theo của chúng ta

đó là nói một chút về con trỏ trong Go.

Vì vậy chúng ta hãy nghỉ ngơi nhanh chóng.

Chúng ta sẽ quay lại ở phần tiếp theo

và chúng ta sẽ chuyển sang chủ đề lớn tiếp theo

và nói rất nhiều về con trỏ

và chính xác chúng được sử dụng để làm gì trong Go.

Vậy nên hãy nghỉ ngơi nhanh và tôi sẽ gặp bạn sau một phút nữa.