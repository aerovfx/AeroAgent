# 003 Lặp lại bản đồ vi

---

Steven: Bây giờ chúng ta đã có cơ hội

để chơi đùa với bản đồ một chút,

Tôi muốn tìm ra cách chúng ta có thể lấy bản đồ

và lặp lại tất cả các

cặp giá trị khóa bên trong nó.

Vì vậy trước tiên chúng ta hãy bắt đầu

bằng cách thực hiện một chút dọn dẹp mã.

Tôi sẽ thực hiện hai cách ban đầu này

về việc khai báo một bản đồ ngay tại đây.

Chúng ta sẽ loại bỏ chúng

và sau đó tôi sẽ bỏ bình luận về toàn bộ mã

mà trước đây chúng tôi đã tập hợp lại với nhau

để khai báo bản đồ màu này.

Và tôi sẽ thêm vào một cặp giá trị khóa nữa

chỉ để làm cho mọi thứ trở nên thú vị một chút.

Chúng ta sẽ nói màu trắng là fffff,

và sau đó chúng ta sẽ dọn dẹp

nơi chúng tôi đã thêm cặp giá trị khóa bổ sung này

rồi xóa nó đi.

Được rồi, điều đó có vẻ tốt.

Vậy điều tôi muốn làm bây giờ là

Tôi muốn tạo một chức năng mới

chấp nhận bản đồ, lặp lại bản đồ

và in ra mọi cặp giá trị khóa bên trong nó.

Và điều này sẽ cho chúng ta cảm giác khá tốt

không chỉ về cách lặp đi lặp lại

một tập hợp các cặp giá trị khóa

nhưng nó cũng sẽ cho chúng ta cảm giác tốt

về cách chuyển bản đồ sang một chức năng khác.

Vì vậy chúng ta sẽ xem trước một chút

trên mã chỉ để bắt đầu,

và sau đó chúng tôi sẽ quay lại

qua trình soạn thảo mã của chúng tôi

và thực hiện thực tế.

Được rồi, vậy thì mơ hồ nó sẽ trông như thế này.

Bây giờ khi chúng ta đang xem mã này ngay tại đây

Tôi muốn nhấn mạnh rằng mọi thứ

mà chúng ta sắp thấy ở đây

sẽ rất giống nhau

để viết mã mà chúng ta đã thấy xung quanh các lát cắt

và lặp lại các lát rồi.

Vì vậy chúng ta sẽ khai báo một hàm gọi là in bản đồ

và sau đó chúng ta sẽ thêm một đối số vào đó.

Chúng ta sẽ nói rằng đối số sẽ được đặt tên là C,

hãy nhớ giữ chủ đề

về việc sử dụng tên biến rất ngắn ở đây,

và sau đó chúng tôi sẽ chú thích loại bản đồ

điều đó đang xảy ra hoặc kiểu tranh luận đó.

Và vì vậy chúng ta sẽ vượt qua bản đồ màu sắc đó.

Vì vậy, nó thuộc loại bản đồ với các khóa kiểu chuỗi

và các giá trị của kiểu chuỗi.

Sau đó, bên trong chức năng in bản đồ này,

chúng tôi sẽ viết mã để thực sự

lặp lại trên bản đồ.

Và đây có lẽ là phần trông

rất giống với phép lặp lát cắt

cú pháp mà chúng ta đã thấy nhiều lần rồi.

Vì vậy chúng ta sẽ đặt từ khóa for

và sau đó chúng ta sẽ đưa vào hai biến

ngay tại đây để nhận từng key

và giá trị qua từng bước của vòng lặp.

Bây giờ tôi đang sử dụng tên ở đây, C, hoặc màu và hex.

Những điều này thực sự có thể được nghĩ đến

giống như khóa và giá trị, giống như vậy.

Vì vậy, thực sự quan trọng và giá trị.

Tôi chỉ đang sử dụng, thêm một chút nữa

tên mô tả ở đây có màu sắc và mã hex.

Và sau đó chúng tôi sử dụng lại từ khóa phạm vi đó

để nói rằng chúng tôi đang cố gắng

để lặp lại trên bản đồ C.

Vì vậy, bên trong phần thân thực sự của vòng lặp for

sau đó chúng ta có thể đặt một số mã sẽ được thực thi

cho mỗi cặp giá trị khóa khác nhau.

Được rồi, bây giờ chúng ta đã có bản xem trước nhỏ này,

hãy quay lại trình soạn thảo mã của chúng tôi

và đặt cái này lại với nhau.

Vì vậy, bên dưới chức năng chính của chúng tôi

chúng ta sẽ tạo một chức năng mới

được gọi là bản đồ in, như vậy.

Chúng ta sẽ bắt đầu bằng cách thêm vào đối số duy nhất

mà chúng tôi mong đợi điều này sẽ được gọi với.

Vì vậy, bất cứ bản đồ nào được gọi với

chúng ta sẽ gọi nó là C,

viết tắt của màu sắc trong trường hợp này.

Và sau đó chúng ta sẽ thêm vào loại

mà chúng tôi mong đợi ở bản đồ này.

Vì vậy tôi hy vọng nó sẽ là một bản đồ

với các khóa kiểu chuỗi

và các giá trị của kiểu chuỗi.

Sau đó, bên trong hàm chúng ta sẽ thiết lập

lên vòng lặp for của chúng tôi để lặp lại bản đồ này C.

Vì vậy, chúng tôi sẽ nói cho từng màu và mã hex

đến từ phạm vi bản đồ C, hãy chạy mã này.

Bây giờ hãy nhớ rằng khi chúng ta đang phân công

các biến này hoặc tạo và gán

các biến màu và hệ lục phân ở ngay đây,

chúng tôi đang khai báo và khởi tạo

và gán cho chúng một giá trị tất cả chỉ trong một bước.

Và vì vậy chúng tôi đảm bảo rằng chúng tôi

sử dụng cú pháp bằng dấu hai chấm đó.

Sau đó, bên trong đây chúng ta sẽ thêm

một ít mã để in ra

mỗi màu và mã hex bên trong bản đồ.

Vì vậy, giả sử dòng in định dạng

mã hex cho màu nhất định.

Và màu sắc ở đây là chìa khóa của chúng ta, là,

và sau đó chúng ta sẽ đặt giá trị xuống,

đó sẽ là hex.

Hex, như thế đấy.

Được rồi, có vẻ khá tốt.

Bây giờ chúng ta hãy quay lại chức năng chính của chúng ta

và đảm bảo rằng chúng tôi gọi bản đồ in.

Vì vậy tôi sẽ thay thế cái hiện có

in dòng tuyên bố ở đây với bản đồ in

và sau đó chúng ta sẽ vượt qua bản đồ C của mình, như vậy.

Được rồi, tôi sẽ lưu tập tin.

Có vẻ như tôi có một lỗi đánh máy ở đây.

Tôi không đặt dấu phẩy sau cặp giá trị khóa cuối cùng này.

Rất giống cấu trúc,

hãy nhớ chúng ta phải đặt dấu phẩy

sau mỗi thuộc tính mà chúng tôi thêm vào đây.

Vì vậy tôi sẽ thêm vào dấu phẩy,

Tôi sẽ lưu tập tin

và bây giờ mọi thứ trông khá tốt.

Được rồi, chúng ta sẽ quay lại thiết bị đầu cuối của mình,

chúng tôi sẽ chạy chương trình của mình

và sau đó chúng ta thấy một dòng lệnh in khác

cho mọi cặp giá trị khóa bên trong bản đồ.

Vì vậy, điều này có vẻ khá tốt.

Bây giờ, như tôi đã nói, chỉ một lúc trước,

lúc này có lẽ bạn đang ngồi đó suy nghĩ

"Steven, cái này khác với cấu trúc như thế nào"?

"Tôi sẽ sử dụng cấu trúc và bản đồ ở đâu"?

Thôi chúng ta hãy nghỉ ngơi nhanh thôi.

Chúng ta sẽ quay lại phần tiếp theo

và sau đó chúng ta sẽ chỉ làm một

tóm tắt nhanh trên bản đồ

và nói về lý do tại sao chúng ta có thể sử dụng

một cấu trúc thay vì bản đồ,

hoặc ngược lại.

Nghỉ nhanh thế

và chúng ta sẽ trả lời câu hỏi đó

chỉ trong một phút.