# 007 Thực hiện kênh vi

---

Người hướng dẫn: Trong video cuối cùng,

chúng tôi thấy rằng thói quen chính của chúng tôi dường như đã kết thúc

ngay lập tức nó đã tạo ra tất cả các goroutine con của nó.

Và thế là chúng tôi nhanh chóng học được

điều đó ngay khi thói quen chính của chúng tôi

đã hết mã để thực thi,

toàn bộ chương trình sẽ thoát,

mặc dù chúng ta vẫn có

những thói quen trẻ em khác đang chạy.

Sau đó chúng tôi đã nói về cách chúng tôi có thể giải quyết vấn đề này

bằng cách sử dụng một kênh để liên lạc

giữa tất cả các goroutine khác nhau này.

Về cơ bản, chúng tôi sẽ tạo một kênh mà chúng tôi có thể sử dụng

để nói: "Này, con goroutine này đã hoàn thành chưa?

Goroutine này đã kết thúc chưa?

Cái này xong chưa?

Được rồi, bây giờ công việc chính có thể thoát ra, không sớm nữa."

Bây giờ, việc sử dụng các kênh không phải là điều dễ dàng,

vì vậy chúng ta sẽ tìm hiểu rất nhiều quy tắc thú vị

và một số điều kỳ lạ xung quanh họ

khi chúng ta bắt đầu sử dụng chúng.

Điều quan trọng khác mà chúng tôi đã học được về kênh

là chúng được gõ.

Vì vậy, dữ liệu hoặc tin nhắn mà chúng ta gửi qua một kênh

phải luôn cùng loại tương ứng

tuy nhiên chúng tôi đã tạo kênh.

Vì vậy, hãy nhìn lại mã của chúng tôi.

Vì vậy, đây là chức năng chính của chúng tôi.

Bên trong đây,

chúng tôi sẽ tạo kênh đầu tiên của mình,

và sau đó chúng ta sẽ sử dụng nó để liên lạc

giữa các goroutine khác nhau của chúng tôi.

Vì vậy, ngay bên dưới lát cắt của chúng ta ngay tại đây,

Tôi sẽ tạo kênh mới của chúng tôi.

Tôi sẽ nói c, viết tắt của kênh,

sẽ là make chan,

và sau đó chúng ta sẽ đặt loại dữ liệu

mà chúng tôi muốn giao tiếp qua kênh này.

Vì vậy trong trường hợp này,

chúng tôi sẽ nói rằng chúng tôi muốn liên lạc qua kênh

với các giá trị kiểu chuỗi.

Đây là cách chúng tôi tạo một kênh hoàn toàn mới.

Chúng ta đã từng thấy từ khóa make trước đây.

Đó là một chức năng tích hợp

điều đó sẽ tạo ra một giá trị ngoài loại đã cho.

Vì vậy chúng tôi tạo ra kênh này

và chúng tôi gán nó cho chuỗi biến này.

Xin lỗi, c, không phải chuỗi.

Vậy bây giờ c là kênh của chúng tôi

và chúng tôi có thể tự do chuyển nó đi khắp ứng dụng của mình.

Bây giờ chúng ta phải xử lý kênh này.

Mặc dù chúng ta sử dụng nó để liên lạc

và tất cả những thứ đặc biệt này,

chúng tôi coi nó giống như bất kỳ giá trị nào khác bên trong

của ứng dụng của chúng tôi.

Vì vậy, nếu chúng ta mong đợi goroutine

được khởi chạy bởi dòng mã này ngay tại đây,

giống như nếu chúng ta mong đợi mã bên trong checkLink,

thích chức năng thực tế này để có thể sử dụng kênh này,

chúng ta phải chuyển kênh vào chức năng đó.

Giá trị ở đây, hoặc biến này,

sử dụng tất cả các quy tắc phạm vi giống nhau

mà chúng tôi sử dụng với các biến khác trong Go.

Vì vậy biến c này chỉ có thể truy cập được bên trong

của chức năng chính này.

Chúng ta không thể tham khảo nó một cách kỳ diệu

bên trong checkLink.

Vì vậy, về cơ bản, chúng ta cần đảm bảo

mà chúng tôi chuyển kênh này tới hàm checkLink.

Sau đó kiểm traLink,

sẽ được thực thi bên trong goroutine,

sẽ có khả năng giao tiếp trở lại

đến chức năng chính này.

Vì vậy, đối số thứ hai cho checkLink,

Tôi sẽ chuyển qua kênh mà chúng tôi vừa tạo.

Vậy biến c này như thế nào.

Bây giờ, tất nhiên, chúng tôi vừa đi qua

một đối số bổ sung cho checkLink,

vì vậy chúng ta cần đảm bảo rằng chúng ta sửa đổi

danh sách đối số ở đây một cách thích hợp.

Vì vậy, như một lập luận thứ hai,

chúng ta sẽ mong đợi thấy một biến mà chúng ta sẽ gọi là c,

lại viết tắt cho kênh.

Nó thuộc loại kênh,

được viết tắt đơn giản là chan.

Và ngay cả ở đây,

chúng tôi cũng phải khai báo loại dữ liệu chúng tôi muốn chia sẻ

qua kênh.

Và giống như chúng tôi đã nói trước đây,

chúng tôi mong muốn chia sẻ các giá trị của loại chuỗi,

chúng ta cũng phải tuyên bố điều đó ở dưới đây.

Vì vậy tôi sẽ nói c sẽ là một kênh.

Bạn chỉ có thể giao tiếp qua nó bằng dây.

Được rồi, bây giờ chức năng checkLink của chúng ta

có quyền truy cập vào kênh,

và chúng ta có thể sử dụng nó để liên lạc từ bất kỳ goroutine nào

đang chạy chức năng checkLink

và chức năng chính của chúng tôi.

Vì vậy, bây giờ câu hỏi rất nhanh chóng trở thành,

à, thực ra chúng ta giao tiếp bằng cách nào?

Làm cách nào để gửi tin nhắn giữa chức năng chính của chúng tôi

và chức năng checkLink?

Vì vậy đây là nơi chúng tôi sẽ giới thiệu

một đoạn cú pháp mới trong Go.

Và đây thực sự là một đoạn cú pháp thú vị.

Bản thân tôi thích nó hơn.

Được rồi, nó trông như thế này đây.

Đây là cách chúng tôi gửi dữ liệu qua các kênh.

Vì vậy hãy nhớ rằng kênh của chúng tôi

giống như một thiết bị nhắn tin hai chiều.

Chúng ta có thể coi nó giống như nhắn tin văn bản.

Vì thế luôn luôn có một người

ai đang gửi tin nhắn

và sau đó là một người khác, hoặc một thực thể khác, tôi nên nói,

cho chương trình của chúng tôi, người đang nhận được tin nhắn đó.

Vì vậy, đối với chúng tôi, chúng tôi có thể muốn gửi dữ liệu từ quy trình chính

tới tất cả các con goroutine con của chúng ta,

hoặc chúng tôi có thể muốn gửi dữ liệu từ goroutine của mình

và tiếp nhận nó trong quy trình chính.

Vì vậy, với ý nghĩ đó,

chúng ta hãy đi qua các phần cú pháp khác nhau này.

Đầu tiên là cách chúng tôi gửi một số dữ liệu

vào một kênh.

Vì vậy nếu chúng ta muốn gửi số 5 vào kênh của mình,

chúng ta sẽ nói kênh và sau đó là một mũi tên nhỏ như vậy,

và sau đó là giá trị mà chúng ta muốn gửi vào đó.

Điều đó giống như nếu bạn rút điện thoại ra ngay bây giờ

và bạn đã mở ứng dụng Messenger của mình,

bạn đã nhập một tin nhắn và nhấp vào Gửi.

Đó là những gì chúng tôi đang làm ở đây.

Chúng tôi đang nhập một giá trị và gửi nó vào kênh.

Bây giờ, mặt khác,

cuối cùng ai đó phải nhận được giá trị đó.

Vì vậy, chúng tôi có thể nhận được các giá trị từ một kênh.

Và bạn có thể nghĩ điều này giống như ai đó

ai nhận được tin nhắn văn bản của bạn

và rút điện thoại ra, mở khóa,

và đọc tin nhắn văn bản của bạn.

Điều đó được thực hiện bằng cách đặt một biến

để nhận tin nhắn vào, một mũi tên,

và sau đó là tên kênh.

Vì vậy, về cơ bản chúng tôi đang nói chờ một giá trị

đến thông qua kênh của chúng tôi.

Và khi đó, hãy gán giá trị đó cho số của tôi.

Và sau đó là một chút cú pháp nâng cao,

không phải lúc nào chúng ta cũng phải lấy giá trị ra khỏi kênh

và gán nó cho một biến.

Chúng ta có thể dễ dàng nói: "Này, hãy xem kênh;

bất cứ khi nào một giá trị xuất hiện từ nó,

sử dụng nó làm đối số cho chức năng dòng in này."

Vì vậy chúng ta có thể lấy giá trị trực tiếp từ một kênh

và chuyển chúng tới các chức năng như thế này ngay tại đây.

Và thực tế là,

Tôi nghĩ đây sẽ là cú pháp nhỏ đầu tiên mà chúng tôi thử.

Vì vậy, thay vì cố gắng nhận thông điệp vào một biến,

Tôi nghĩ rằng trước tiên chúng ta sẽ bắt đầu bằng cách thử in

một tin nhắn trực tiếp.

Vì vậy, hãy thử điều này ngay bây giờ.

Giả sử chúng tôi không muốn làm bất cứ điều gì với checkLink

cho đến khi nó truy xuất thành công một số URL thực tế.

Vì vậy, giả sử sau khi chúng tôi truy xuất được một URL,

hãy gửi tin nhắn tới kênh của chúng tôi,

và sau đó chúng tôi sẽ nhận nó ở bên trong

chức năng chính của chúng tôi ngay tại đây.

Và chúng tôi sẽ in ra bất cứ điều gì chúng tôi đã gửi.

Vì thế tôi sẽ đặt kênh này gửi tin nhắn

ở hai địa điểm rất cụ thể,

và chúng ta sẽ nói chuyện trong thời gian ngắn

về lý do tại sao chúng tôi chọn hai địa điểm cụ thể này.

Vì vậy, ngay bên dưới tuyên bố dòng in của chúng tôi

bên trong câu lệnh if ở đây,

Tôi định nói hãy gửi tin nhắn vào kênh của chúng tôi.

Vì vậy, chúng tôi nói vào kênh, gửi,

và sau đó là giá trị mà chúng tôi muốn gửi.

Vì vậy tôi sẽ gửi một chuỗi có nội dung:

"Tôi nghĩ có thể xuống."

Và sau đó nếu chúng tôi thấy rằng trang web thực sự đã hoạt động

hoặc liên kết thực sự đã hoạt động,

chúng ta sẽ gửi một tin nhắn khác.

Vì vậy, ở dưới đây bên dưới dòng lệnh in khác,

chúng ta sẽ nói, "Ừ, xong rồi," giống như vậy.

Bây giờ, quay lại bên trong chức năng chính của chúng ta,

chúng tôi sẽ thêm một câu lệnh để nhận dữ liệu đó

từ kênh.

Vì vậy, bên dưới câu lệnh for của chúng tôi,

ngay bên dưới vòng lặp for ngay tại đây,

hãy in ra, vì vậy chúng ta sẽ nói fmt.Println

và sau đó chúng ta sẽ nhận được một giá trị từ kênh.

Vì vậy chúng ta sẽ nói mũi tên như vậy, và sau đó là c.

Được rồi, cú pháp chúng tôi sử dụng trong cả hai trường hợp ở đây

đang làm theo chính xác những gì chúng ta vừa thấy

trong slide ngay tại đây.

Vì vậy, chúng ta có thể đặt một giá trị, mũi tên,

và sau đó là kênh chúng tôi muốn gửi tin nhắn tới.

Và mặt trái của điều đó, trong một goroutine khác,

chúng ta có thể thêm vào một phép gán biến

hoặc một lời gọi hàm.

Vì vậy, trong trường hợp này, chúng tôi đang sử dụng lệnh gọi hàm.

Chúng tôi đang nói rằng hãy nhận được giá trị từ kênh này

và ngay lập tức đăng nhập nó.

Vì vậy, hãy chạy mã này và xem điều gì sẽ xảy ra.

Tôi sẽ lưu tập tin.

Tôi sẽ đảm bảo rằng tôi không có bất kỳ đường nguệch ngoạc màu đỏ nào ở đây

đó chỉ ra một lỗi.

Có vẻ như tôi ổn.

Vì vậy tôi sẽ quay trở lại thiết bị đầu cuối của mình

và tôi sẽ chạy lại chương trình này.

Được rồi, lần này,

chúng tôi có chính xác một báo cáo nhật ký ở đây,

và sau đó có vẻ như chúng ta đã thoát khỏi chương trình một lần nữa.

Vì vậy, có vẻ như thứ chúng tôi nhận được là google.com.

Ở đây nó ghi là google.com đã hoạt động.

Và sau đó chúng tôi thấy sự liên lạc của chúng tôi thông qua kênh này,

dòng chữ "Ừ, xong rồi."

Bây giờ, nếu tôi tiếp tục chạy cái này, hả?

Có vẻ như lần nào đó cũng là Google.

Bây giờ, nó có vẻ hơi kỳ lạ

rằng chúng ta chỉ nhận được một thông tin liên lạc ở đây

hơn là tất cả các phần giao tiếp khác nhau.

Vì vậy, điều này thực sự đang phơi bày chúng ta

đến một trong những điều thực sự thú vị xung quanh các kênh.

Vì vậy chúng ta hãy tạm dừng nhanh chóng.

Chúng ta sẽ quay lại ở phần tiếp theo

và chúng ta sẽ nói về chính xác

tại sao chúng tôi chỉ nhận được một thông tin liên lạc qua kênh

và sau đó thoát khỏi chương trình của chúng tôi.

Vì vậy, hãy nghỉ ngơi nhanh chóng, chúng ta sẽ quay lại sau một giây.