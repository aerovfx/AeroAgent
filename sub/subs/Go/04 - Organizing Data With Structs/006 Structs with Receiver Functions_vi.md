# 006 Cấu trúc có chức năng nhận vi

---

Trong phần trước, chúng tôi đã tìm cách tạo một cấu trúc mới và sau đó nhúng cấu trúc đó vào một cấu trúc hiện có.

Vì vậy, chúng tôi đã tạo liên hệ thông tin.

Sau đó, chúng tôi đã thêm tên trường liên hệ mới cho từng người và chúng tôi nói rằng trường liên hệ sẽ luôn có

value of contact information.

Sau đó, khi chúng tôi tạo một người, chúng tôi nói, đã được rồi, đây là trường liên hệ của chúng tôi và đây là thông tin liên hệ

for it. use for it.

Bây giờ, vẫn còn một số điều tôi muốn cho bạn tìm thấy xung quanh cấu trúc.

Và câu hỏi đầu tiên là một phần nhỏ cuối cùng của loại câu hỏi xung quanh việc tạo ra một cấu trúc nhúng như chúng

ta vừa làm.

Vì vậy, chúng tôi đã nói rằng chúng tôi có một trường tên liên hệ ngay tại đây và loại của nó được chọn là thông tin

tin liên hệ.

Bây giờ, tôi muốn chỉ cho bạn một cách khác để nhúng một cấu trúc tương thích.

Nó chỉ là một hơi thở khác một chút.

Vì vậy, nếu muốn, chúng tôi có thể xóa trường tên ngay tại đây.

Chúng tôi có thể xóa liên hệ và chúng tôi có thể nói đơn giản là thông tin liên hệ.

Bây giờ điều này làm cho nó vẫn chưa khai báo một trường tên của liên hệ thông tin và nó cũng nói rằng nó phải có

a type contact contact.

Vì vậy, nói cách khác, chỉ sử dụng thông tin liên hệ ngay tại đây tương thích 100% với việc nói thông tin liên hệ

là trường tên và không có loại thông tin liên hệ.

Đó là một lát.

Tôi biết.

Vì vậy, hãy để nó chỉ ở liên hệ thông tin và xem chúng tôi thực sự sẽ sử dụng nó như thế nào.

Vì vậy, tôi sẽ để lại thông tin liên hệ ngay tại đây và sau đó trong quá trình tạo Jim

của chúng tôi, thay vì khai báo trường tên của liên hệ và phân bổ thông tin liên hệ, chúng tôi sẽ nói rằng thông tin

liên hệ phải thuộc loại thông tin liên hệ.

Tôi biết.

Tôi đang nói điều đó rất nhiều.

Được rồi.

Vì vậy, chúng tôi sử dụng điều này và kiểm tra nó.

Vì vậy, về cơ bản, tất cả những gì chúng tôi đã làm đều đổi tên một trường để chúng tôi không phải nói liên hệ, liên hệ.

Chúng tôi chỉ tự động tiết kiệm một số tổ hợp phím ở đây.

Đó là tất cả những gì chúng tôi đang thực hiện.

Vì vậy, hãy kiểm tra nó một lần nữa và bạn sẽ nhận được.

Đã rồi, đây là trường tên, vẫn là liên hệ thông tin và không có liên hệ thông tin có giá trị.

Được rồi.

Bây giờ, điều đó có vẻ như là một câu tranh luận nhỏ không quan trọng, nhưng điều đó thực sự sẽ rất quan trọng

Điều quan trọng sau đây là đặc biệt khi chúng ta nói về việc sử dụng lại một số mã thực tế với Go.

Vì vậy, tôi muốn bạn chỉ cần loại tệp này thực tế rằng chúng tôi không thực sự phải chỉ định trường tên

ở đây nếu chúng tôi không muốn.

Vì vậy, chúng ta hãy tiếp tục.

Có một điều cuối cùng tôi muốn xem xét nhanh chóng xung quanh các cấu trúc bên trong ứng dụng bộ bài của chúng

tôi hoặc thẻ ứng dụng.

Bạn nên nhớ rằng khi chúng tôi tạo ra loại bộ bài mới đó, chúng tôi sẽ thiết lập một số chức năng

get bộ bài làm bộ thu.

Và kết quả của công việc đó là chúng tôi có thể viết mã trông giống như thẻ, dấu chấm, trộn hoặc những thứ

bạn có gì vậy?

Và vì vậy, họ có thể thiết lập cùng một loại hàm có bộ cấu trúc.

Vì vậy, hãy tạo một hàm mới sẽ lấy một người như người nhận Jim và họ có thể sẽ ra tất cả

all chi tiết của người đó.

Vì vậy, chúng tôi sẽ phải tiếp cận bộ nhớ của chúng tôi ở đây và nhớ cách chúng tôi

tạo ra các hàm sử dụng bộ thu bên dưới các chức năng chính của chúng ta.

Chúng tôi sẽ viết ra mục đích, sau đó viết ra người nhận.

Vì vậy, đây sẽ là người P, có nghĩa là bạn có thể gọi hàm này mà chúng tôi sắp xếp xác định trên bất kỳ kiểu nào hoặc

bất kỳ giá trị nào của loại người.

Và sau đó bên trong phần thân của hàm này, bạn có thể tham chiếu người đó làm biến.

Vì vậy, chúng tôi sẽ đặt tên cho thứ này.

Làm thế nào để chỉ cần vào?

Giống như vậy và vì vậy, chúng tôi sẽ nói về cơ bản chính xác những gì chúng tôi đang làm ngay tại đây với lệnh printf.

Vì vậy, chúng tôi sẽ chỉ cắt những dòng này, dán nó ngay tại đây, và tất nhiên, thay vì cố gắng

Hãy đến với Jim, chúng tôi muốn người được đưa vào hàm này.

Vì vậy, chúng tôi sẽ nói trong F đối số thứ hai của P.

Vì vậy, hiện nay bên trong các chức năng chính của chúng tôi, chúng tôi có thể tự động gọi Jim Dot print cụ thể vì chúng tôi chỉ

thiết lập chức năng này với loại người là người nhận và Jim là người.

Vui lòng lưu lại và kiểm tra xem chúng tôi đang làm như thế nào.

Vì vậy, chúng tôi sẽ lưu tệp.

Chúng tôi sẽ nhẹ nhàng lại và OC có vẻ tốt.

Bây giờ có một điều cuối cùng mà tôi muốn làm với cấu trúc này rất giống với công cụ bộ thu này ngay bây giờ

tại đây sẽ dẫn rất hay đến chủ đề tiếp theo của chúng ta.

Vì vậy, chủ đề tiếp theo chúng ta sẽ thảo luận sẽ có một chút buồn cười, nhưng chúng ta sẽ

tập hợp lại một đoạn mã nhỏ ngay bây giờ sẽ hoạt động hơi bất ngờ một chút hoặc có thể nó sẽ hoạt động

chính xác như bạn mong đợi.

Chúng ta sẽ thấy.

Hãy viết mã ra và chúng tôi sẽ chỉ xem điều gì sẽ xảy ra.

Vì vậy, tôi muốn tạo một chức năng khác được gọi là cập nhật tên như thế nào?

Được rồi.

Tôi muốn viết một chức năng được gọi là bản cập nhật tên, lấy một người nhận và sau đó cập nhật

thuộc tính tên trên người đó.

Vì vậy, chúng tôi thử điều này.

Tôi sẽ nói với người P func.

Hàm tên sẽ là bản cập nhật tên và sau đó chúng ta có thể nhận được tên mới.

Vì vậy, chúng tôi sẽ chỉ gọi nó là tên mới rất rõ ràng, phải là một chuỗi.

Vì vậy, chúng tôi sẽ nói P chấm tên bằng tên mới như vậy.

Vì vậy, chúng tôi chỉ khai báo chức năng cập nhật tên này.

Nó có bộ thu loại người và chúng ta phải gọi nó bằng một tên mới.

Và sau đó khi chúng tôi làm như vậy, nó sẽ cập nhật tên của người đó.

Vì vậy, hãy gọi điều này với Jim và đặt cho Jim một tên mới và xem điều gì sẽ xảy ra.

Vì vậy, chúng tôi sẽ thông báo bản cập nhật tên Jim Dot và chúng tôi sẽ chọn cho anh ấy một cái tên mới đầu tiên là Just Jimmy.

Được chứ.

Vì vậy, tôi muốn bạn ngồi xuống một chút và tôi muốn bạn xem mã mà chúng tôi vừa viết ngay tại

đây.

Tôi muốn bạn nhìn vào chức năng này và tôi muốn bạn đưa ra ý kiến kiến trúc ngay bây giờ khi chúng tôi tiến hành

mã này, bạn nghĩ chính xác điều gì sẽ xảy ra?

Tôi muốn bạn chỉ nghĩ về nó trong một giây, nghĩ về những gì sẽ xảy ra khi chúng

ta run it.

Tôi có thể chắc chắn với bạn rằng nó sẽ chạy như chúng tôi sẽ không gặp lỗi.

Nhưng tôi chỉ muốn bạn hiểu một số ý tưởng về những gì bạn nghĩ sẽ xảy ra.

Và sau đó khi bạn có ý tưởng đó, chúng tôi sẽ chuyển sang thiết bị đầu cuối và chúng tôi sẽ bắt đầu lại chương trình của mình.

Vì vậy, khi chúng tôi chạy chương trình của mình, bạn sẽ nhận thấy rằng chúng tôi có một người tên đầu tiên ở đây là Jim.

Bây giờ, điều đó có thể thổi thú vị cho bạn, bởi vì trên dòng này ngay tại đây, chúng tôi

đang nói rằng hãy đưa Jim, chuyển anh ấy vào bản cập nhật tên.

Vì vậy, Jim sẽ trở thành người thứ hai ngay tại đây và đặt cho Jim một cái tên hoàn toàn mới giống như cập nhật thuộc tính

tính tên đó.

Và ngay sau đó chúng tôi gặp Jim một lần nữa.

Vì vậy, đối với tôi, chúng tôi có vẻ giống như khi chúng tôi ở Jim ra ngay tại đây, chúng tôi vừa cập nhật tên của anh ấy thành Jimmy.

Nhưng rõ ràng, như chúng ta vừa thấy khi in it ra, có vẻ như bản cập nhật or chưa có hiệu lực.

Nó đã không được giữ ở tất cả.

Vì vậy, đây là một phần thực sự thú vị của cờ vây.

Và nó sẽ chuyển chủ đề sang chủ đề tiếp theo của chúng ta, đó là nói một chút về các con trỏ

và đi.

Vì vậy, chúng tôi nghỉ ngơi nhanh chóng.

Chúng ta sẽ quay lại phần tiếp theo và chúng ta sẽ chuyển sang chủ đề tiếp theo

điều này và nói nhiều về con trỏ và độ chính xác của chúng được sử dụng để làm gì.

Vì vậy, hãy nhanh chóng nghỉ ngơi và tôi sẽ gặp bạn chỉ sau một phút.