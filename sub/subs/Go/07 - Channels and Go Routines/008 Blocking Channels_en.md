# 008 Chặn kênh vi

---

Giáo viên: Ở phần cuối,

chúng tôi đã tạo kênh đầu tiên của mình.

Chúng tôi đã tạo ra kênh này.

Chúng tôi đã chuyển nó vào hàm checkLink.

Sau đó, sau khi yêu cầu nhận của chúng tôi thành công hoặc thất bại,

sau đó chúng tôi đã gửi một tin nhắn chuỗi vào kênh.

Sau đó quay lại bên trong chức năng chính,

chúng tôi đã nghe một tin nhắn

và in nó ra khi chúng tôi nhận được.

Chỉ có một vấn đề nhỏ.

Chúng tôi thấy rằng khi chạy mã này,

chúng tôi chỉ có một báo cáo nhật ký

và sau đó chương trình được thực thi ngay lập tức

hoặc xin lỗi, thoát ngay, không bị xử tử.

Vì vậy hãy đi sâu vào vấn đề này

và tìm hiểu chính xác chuyện gì đang xảy ra.

Bây giờ khi chúng ta bắt đầu giải quyết vấn đề này,

đây chắc chắn là một trong những khái niệm thách thức nhất

xung quanh các kênh.

Vì vậy hy vọng chúng ta sẽ giải quyết vấn đề này một cách thực sự khó khăn

và nắm bắt rất tốt

về một số nguyên tắc cơ bản của kênh.

Vì vậy, hãy bắt đầu với nó.

Được rồi, đây là sơ đồ về hai hàm của chúng ta.

Đây là chức năng chính của chúng tôi và đây là chức năng checkLink của chúng tôi.

Vì vậy chúng ta hãy đi qua điều này

và tưởng tượng từng dòng mã khi nó được thực thi.

Vì vậy, thói quen chính bắt đầu

ngay khi chúng tôi tạo chương trình của mình.

Sau đó, chúng tôi tạo lát chuỗi của mình,

chúng tôi tạo ra kênh của chúng tôi.

Sau đó chúng ta đi vào vòng lặp for

và chúng tôi tạo ra goroutine đầu tiên của mình.

Chúng tôi chuyển vào cả hai liên kết

và kênh tới chức năng checkLink.

Và vì vậy về cơ bản chúng ta có thể tưởng tượng

goroutine đầu tiên của chúng tôi sẽ hoạt động.

Chúng ta sẽ tưởng tượng rằng goroutine đầu tiên hoạt động

là phần tử đầu tiên bên trong lát chuỗi của chúng ta,

vậy là Google.com.

Vì vậy, goroutine của chúng tôi thức dậy,

nó bắt đầu thực thi mã bên trong đây

và ngay lập tức đưa ra yêu cầu nhận.

Vì vậy tại thời điểm đó, chúng ta có thể tưởng tượng

rằng con goroutine này hiện đã bị tạm dừng, giống như ở đây.

Vì vậy, trên dòng mã ngay tại đó.

Bây giờ quy trình chính sẽ hoạt động trở lại

và nó bắt đầu tạo ra các goroutines khác

bên trong chương trình của chúng tôi.

Vì vậy, một goroutine cho mỗi liên kết khác.

Bây giờ đây là điều thực sự quan trọng,

điều rất quan trọng cần hiểu.

Sau khi chúng ta tạo từng goroutine riêng lẻ,

thói quen chính sau đó nói,

"Được rồi tôi ngồi đây

và chờ tin nhắn đến qua kênh."

Bất cứ khi nào chúng ta chờ đợi một tin nhắn đến qua một kênh,

đây là một cuộc gọi chặn, một dòng mã chặn

theo cách chính xác như vậy

rằng chức năng get của chúng tôi ở đây cũng bị chặn.

Vì vậy ngay khi thời gian chạy Go

thấy rằng chúng tôi muốn nhận tin nhắn từ một kênh,

nó nói, "Ồ, thói quen này

đang chờ đợi điều gì đó xảy ra.

Không có mã nào khác để nó chạy ngay bây giờ.

Chúng ta chỉ cần tạm dừng và để nó làm việc của nó."

Vì vậy, công việc chính là đưa vào giấc ngủ và nó nói,

"Được rồi, sẽ không chạy công việc chính nữa.

Chúng ta sẽ chờ đợi điều gì đó xảy ra."

Rồi thời gian trôi qua, thời gian trôi qua, thời gian trôi qua

và cuối cùng là goroutine của chúng tôi,

ai có yêu cầu thì giải quyết trước.

Và trong trường hợp này, đối với cá nhân tôi thì đó là Google,

vì đó là trang web tải nhanh nhất.

Đối với bạn, bạn có thể đã nhận được một kết quả khác.

Bạn có thể đã thấy một số kết quả khác

nếu bạn có tốc độ kết nối khác với tôi.

Vì vậy, ngay lập tức goroutine đầu tiên

giải quyết yêu cầu, goroutine đó sẽ thức dậy

và nó bắt đầu thực thi phần còn lại của mã

bên trong chức năng này.

Và cuối cùng nó đi xuống

hoặc gửi tin nhắn này ngay tại đây

trong trường hợp thất bại hoặc trường hợp ở dưới cùng bên phải ở đây,

thay vào đó là trường hợp thành công.

Vì vậy, về cơ bản goroutine thức dậy

và cuối cùng gửi một tin nhắn vào kênh.

Bây giờ, khi tin nhắn này được gửi

thời gian chạy Go sau đó nói: "Được rồi, có vẻ như

chúng tôi đang nhận được một số dữ liệu trên kênh này.

Có con goroutine nào ngoài kia không

đang chờ đợi một số thông tin trên kênh này?"

Và thói quen chính sẽ vui vẻ hơn và nói, "Ồ, đúng vậy.

Tôi đang chờ một số tin nhắn trên kênh này."

Và thế là quy trình chính được thực hiện trở lại,

nó nhận được giá trị mà chúng tôi đã gửi vào kênh,

nó in ra và sau đó quy trình chính sẽ nói,

"Vậy thôi, tôi không còn mã nào khác để chạy nữa.

Chúng tôi sẽ thoát khỏi chương trình hoàn toàn."

Và bài học rút ra ở đây

đó là việc nhận tin nhắn từ một kênh

là một điều ngăn chặn.

Đó là một dòng mã chặn.

Chúng ta phải đợi một tin nhắn đến

trước thời gian chạy,

hoặc trước khi thói quen này tiếp tục

vượt qua dòng mã này ngay tại đây.

Và vì vậy trong thực tế

chúng ta có thể tưởng tượng ra một sơ đồ trông như thế này.

Vì thế việc này hơi phức tạp một chút,

nhưng chúng ta hãy đi từng bước một.

Vì vậy, chương trình của chúng tôi lần đầu tiên bắt đầu

ở đây, phía bên tay trái.

Chúng tôi bước vào thói quen chính,

chúng tôi tạo ra một lát chuỗi đã gõ,

và sau đó chúng ta bước vào vòng lặp for.

Sau đó chúng tôi tạo ra một số thói quen khác nhau.

Đầu tiên là quy trình google.com, sau đó là Facebook

và sau đó là Amazon, hoặc bạn biết đấy, bất kỳ liên kết nào khác mà chúng tôi có.

Vì vậy ngay sau khi vòng lặp kết thúc

và về cơ bản chúng ta có thể tưởng tượng vòng lặp đã hoàn thành

tại thời điểm đó Amazon hoặc bất cứ liên kết cuối cùng là gì.

Về cơ bản ở dòng này ngay tại đây

bây giờ chúng ta đã hoàn thành vòng lặp

và chúng tôi hiện đang chờ đợi trên kênh của mình.

Vì vậy, dòng này ở đây có nghĩa là để đại diện

về cơ bản dòng mã này ở ngay đây.

Vì vậy, bây giờ chúng tôi đang chờ đợi điều này.

Chúng tôi đang chờ một số dữ liệu được truyền qua kênh.

Vì vậy, tất cả các thói quen khác nhau của chúng tôi đang chạy

và không có gì trong thói quen chính

đang chạy vào thời điểm đó.

Bây giờ đó là một sự cường điệu của sự thật ở đây.

Bạn biết đấy, quy trình chính là bị tạm dừng trong quá trình thực thi.

Và thành thật mà nói, tất cả các thói quen khác cũng vậy,

khi họ chờ đợi phản hồi

từ yêu cầu HTTP của chúng tôi quay trở lại.

Nhưng chúng ta chỉ có thể ở dạng sơ đồ

chúng ta có thể tưởng tượng nó xảy ra như thế này.

Vì vậy, cuối cùng tại một thời điểm nào đó

google.com là nơi đầu tiên thức dậy và nói,

"Ồ, có vẻ như chúng ta vừa nhận được phản hồi."

Và ngay khi chúng tôi nhận được phản hồi đó

quy trình của Google sẽ gửi dữ liệu vào kênh,

thói quen chính được thức dậy trở lại,

sau đó nó lấy giá trị đó, in ra,

nó thấy rằng không có mã nào khác

để chạy bên trong chức năng đó.

Và thế là thủ tục chính kết thúc

và các goroutine khác mà chúng tôi có

về cơ bản bị bỏ lại trong hư vô

và họ không bao giờ thực sự kết thúc.

Họ chỉ bị chấm dứt hoàn toàn.

Vậy chúng ta hãy đưa vấn đề này lên cấp độ tiếp theo ở đây

và chúng ta hãy thực sự tìm ra

và chỉ chơi đùa với cái này

về cơ bản một chút.

Vì vậy, tôi sẽ tìm dòng lệnh in của chúng ta.

Tôi sẽ sao chép nó

và tôi sẽ đặt một bản sao khác ngay bên dưới nó.

Vì vậy, bây giờ chúng tôi có hai địa điểm mà chúng tôi đang chờ đợi

cho một tin nhắn trên kênh của chúng tôi.

Bây giờ tôi sẽ lưu tập tin này

và tôi muốn bạn tạm dừng ngay bây giờ.

Và tôi muốn bạn nghĩ trong đầu

bạn mong đợi điều gì sẽ xảy ra vào thời điểm này?

Tôi chỉ muốn bạn đoán mò thôi.

Bạn nghĩ điều gì sẽ xảy ra bây giờ

khi chúng tôi chạy chương trình của mình?

Được rồi, hy vọng bạn có ý tưởng nào đó.

Bây giờ chúng ta hãy đi đến thiết bị đầu cuối của chúng tôi

và chúng ta sẽ chạy lại chương trình.

Bây giờ, lần này chúng ta nhận được hai báo cáo nhật ký riêng biệt

đối với google.com và tràn ngăn xếp.

Bây giờ một lần nữa, bạn có thể thấy một thứ tự khác ở đây

nếu yêu cầu của bạn được giải quyết

theo thứ tự khác với thứ tự của tôi, điều đó hoàn toàn ổn.

Vì vậy bây giờ chúng ta hãy xem điều gì đang xảy ra

ở dạng sơ đồ ở đây.

Được rồi, vậy bây giờ về cơ bản đây là cùng một sơ đồ

chỉ với một hoặc hai bước bổ sung.

Vì vậy tôi sẽ chỉnh sửa dòng này ngay tại đây

để thực sự phù hợp với những gì tôi có,

đó là Stack Overflow.

Được rồi, bây giờ chúng ta có thể tưởng tượng rằng quy trình chính của chúng ta bắt đầu,

nó lặp qua lát chuỗi của chúng ta

và khởi động một loạt goroutine khác nhau.

Sau đó, thói quen chính của chúng tôi nói,

"Được rồi, tôi đang nghe trên kênh này.

Tôi đang đợi một số dữ liệu được đưa ra."

Sau đó, quy trình của Google cuối cùng cũng kết thúc,

nó in ra hoặc gửi một số dữ liệu vào kênh

nơi mà thói quen chính sau đó nhận được nó.

Vì vậy, thủ tục chính nhận được dữ liệu đó

và thức dậy rồi in ra dữ liệu

rồi chuyển sang dòng mã tiếp theo.

Và dòng mã tiếp theo ngay tại đây

cũng đang nói,

"Đợi một số dữ liệu đi qua kênh của chúng tôi."

Và vì vậy chúng ta lại bước vào điều tương tự một lần nữa.

Công việc chính sau đó lại đi ngủ

và chỉ thức dậy khi đối với tôi, ngăn xếp đã hoàn thành

và gửi một số dữ liệu vào kênh.

Thủ tục chính sau đó nhận dữ liệu đó, in ra

và sau đó nói, "Tôi không còn mã nào khác để viết,

nên tôi sẽ thoát hoàn toàn."

Và vì vậy chúng ta có thể bắt đầu xếp chồng lên nhau

những dòng lệnh in này ngay tại đây

và xem một số hành vi thú vị.

Vì vậy đối với tôi, tôi có danh sách năm liên kết ngay tại đây,

năm liên kết.

Vì thế nếu tôi muốn tôi có thể nói,

dán năm tin nhắn sẽ được nhận ở đây.

Chính xác là năm.

Vì vậy bây giờ chúng ta sẽ đợi năm tin nhắn trong kênh

trước khi chúng ta thoát khỏi chương trình này.

Vì vậy tôi sẽ lưu cái này, tôi sẽ chạy nó

và bây giờ chúng ta sẽ thấy năm kết quả ở đây.

Vậy 1, 2, 3, 4, 5.

Vậy thì không còn mã nào nữa, hoặc xin lỗi,

không còn mã để thực thi.

Và vì vậy chúng tôi thoát hoàn toàn.

Và bây giờ chúng ta có thể thấy một số hành vi thực sự kỳ lạ

nếu tôi đặt thêm một báo cáo nhật ký ở đây.

Và đây là số sáu,

nhưng bạn và tôi biết

rằng chúng ta sẽ chỉ nhìn thấy năm tin nhắn

đã gửi vào kênh của chúng tôi,

bởi vì chúng tôi chỉ tạo ra năm goroutine mới.

Vì vậy, bây giờ khi tôi lưu cái này và chạy mã của chúng tôi

chúng ta sẽ thấy năm tin nhắn

và sau đó chương trình của chúng tôi bị treo,

bởi vì công việc chính bây giờ chỉ là ngồi đó

chờ đợi ai đó gửi một số thông tin

vào kênh của chúng tôi.

Và cá nhân tôi nghĩ

đây thực sự là hành vi thú vị ở đây.

Vì vậy, như bạn có thể tưởng tượng,

nó bắt đầu trở nên rất quan trọng

phải suy nghĩ thật kỹ về các kênh của chúng tôi

và cách chúng được thiết lập bên trong ứng dụng của chúng tôi.

Tất nhiên bây giờ, có lẽ chúng ta không muốn có

chương trình của chúng tôi chỉ treo ở đây và chạy.

Vì vậy chúng ta hãy nghỉ ngơi nhanh chóng.

Chúng ta sẽ quay lại ở phần tiếp theo

và chúng tôi sẽ tìm ra cách có thể in ra

tất cả tin nhắn đến từ kênh của chúng tôi

mà không cần phải viết ra

một loạt các dòng lệnh in khác nhau ở đây.

Vì rõ ràng, bạn biết đấy, chúng ta không muốn phải xếp chồng lên nhau

giống như năm dòng lệnh in như thế này,

đặc biệt nếu chúng ta bắt đầu có

một số lượng URL khác nhau ở đây

mà chúng tôi muốn in ra.

Được rồi, nghỉ nhanh nhé, quay lại ở phần tiếp theo

và chúng tôi sẽ tìm ra cách giải quyết vấn đề này

tất cả những thứ chặn kênh này.