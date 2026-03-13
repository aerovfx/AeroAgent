# 004 Lập trình đồng bộ hóa thời gian SNTP Phần III vi

---

Vậy chúng ta hãy tiếp tục và thành phố server biển đó.

Và ở đây, hãy bao gồm khoảng thời gian S&P.

Và bây giờ chúng ta hãy đi xuống và đăng ký một người xử lý nước tiểu mới.

Và chúng ta sẽ bắt đầu bằng cách sao chép cái này.

Và hãy cập nhật bình luận theo giờ địa phương.

Và cập nhật cấu trúc theo giờ địa phương.

Và đồng euro ở đây là giờ địa phương Dutch Jason.

Và phương pháp là HTP get.

Và sau đó cập nhật trình xử lý để lấy giờ địa phương.

Cứ như thế này.

Và sau đó hãy chuyển tên.

Để đăng ký trình xử lý.

Bây giờ chúng ta cùng đi tìm nó trên đây nhé.

Và tôi sẽ bắt đầu bằng việc sao chép bình luận này.

Vậy thì ở đây tôi sẽ đổi sang giờ địa phương.

Và tôi sẽ nói ở đây phản hồi.

Bằng cách gửi giờ địa phương.

OK, bây giờ chúng ta hãy lấy tên hàm.

Và sau đó quay trở lại.

Và sau đó, loại tên hàm siêu năng lực tĩnh.

Và đó là loại yêu cầu HD DVD.

Con trỏ RFQ.

Và sau đó chúng ta sẽ cắm ISP đầu tiên.

Chúc bạn có thời gian vui vẻ, Jason yêu cầu.

Và bây giờ chúng ta cần quan tâm đến giờ địa phương, Jason.

Bộ đệm 100 byte.

Và đặt nó về 0 rồi nói liệu sau này nó có xác định một biến toàn cục sẽ sử dụng ở đây để kiểm tra không

tại thời điểm đã được thiết lập và chúng ta sẽ gọi nó là Gee Underscore, giờ địa phương đã được thiết lập chưa?

Và nếu nó được đặt, thì anh ta sẽ cập nhật JSON theo giờ địa phương và sử dụng in f thành giờ địa phương

JSON.

Và chúng ta sẽ dành thời gian ở đây.

Và sau đó chúng ta sẽ lấy thời gian bằng cách sử dụng hàm get time.

Và đó là sự đồng bộ hóa thời gian của S&P.

Bây giờ, hãy lấy loại phản hồi.

Đối với yêu cầu.

Là ứng dụng JSON.

Phản hồi httpd tiếp theo, hãy gửi.

Hoặc yêu cầu từ bộ đệm.

Nhưng Starlin của giờ địa phương, Jason.

Và sau đó chúng ta hãy quay trở lại.

ESP, được rồi.

Được rồi, bây giờ hãy tạo biến toàn cục này.

Vậy chúng ta hãy đi lên.

Và đưa ra nhận xét ở đây.

Trạng thái giờ địa phương.

Và đó là một con bò tĩnh.

Thay vào đó, nó là sai.

Và bây giờ chúng ta hãy lấy một trường hợp cho nó.

Và chúng ta có thể sử dụng cái này.

Và thay đổi nó thành.

Thay đổi nó thành thời gian khởi tạo dịch vụ.

Bây giờ chúng ta hãy cập nhật tin nhắn nhé.

Và sau đó thay đổi biến toàn cục này thành toàn cục là giờ địa phương được đặt.

Và sau đó ở đây chúng tôi đã nói đúng sự thật.

Được rồi, bây giờ chúng ta hãy đến Wi-Fi Bridge.

Bởi vì ở đây tôi muốn tạo một chức năng gọi lại để chức năng bắt đầu tác vụ đồng bộ hóa thời gian của S&P có thể

được gọi thông qua một cuộc gọi lại tùy chỉnh.

Và điều này sẽ được gọi khi ESP 32 có địa chỉ IP.

Vì vậy, thay vì gọi nó một cách rõ ràng là nó được chôn ở đâu đó trong mã, chúng tôi có thể thực hiện điều đó từ nam giới và bạn sẽ

hãy xem nó hoạt động như thế nào khi chúng ta hoàn thành.

Vì vậy, đầu tiên ở đây, hãy bình luận.

Gọi lại, typedef.

Và đó là typedef.

Vô hiệu.

Đã kết nối Wi-Fi.

Sự kiện trở lại.

Đội gạch dưới.

Và nó trống rỗng.

Được rồi, điều này tạo ra một loại có tên Sự kiện được kết nối Wi-Fi được gọi ngược lại là dấu gạch dưới T cho một con trỏ

đến một hàm không có đối số và không trả về gì.

OK, bây giờ chúng ta hãy đi đến phần cuối của tập tin.

Và tạo ra một nguyên mẫu.

Mà thiết lập chức năng gọi lại.

Và đó là một khoảng trống.

Gọi lại bộ ứng dụng Wi-Fi.

Và nó cần kết nối wi fi.

Sự kiện gọi lại.

KB.

Được rồi, bây giờ hãy tạo một nguyên mẫu khác gọi hàm gọi lại.

Và nó sẽ là một ứng dụng Wi-Fi trống.

Gọi lại.

Và nó trống rỗng.

Được rồi, giờ chúng ta đi tìm hai người này nhé.

Nhưng trước tiên, hãy lên đỉnh.

Và gửi tới bạn, hãy viết bình luận.

Tại sao ứng dụng fi lại gọi lại?

Và nó tĩnh.

Gọi lại sự kiện được kết nối WI fi.

Và gọi nó là sự kiện kết nối Wi-Fi.

CB.

Được rồi, có vẻ ổn, vậy chúng ta hãy đi xuống phía dưới để biết các chức năng công cộng.

Và hãy định nghĩa chúng ở đây.

Và cho cuộc gọi lại đã thiết lập.

Chà, chỉ cần đặt CB sự kiện được kết nối Wi-Fi của chúng tôi.

Đối với lệnh gọi lại được chuyển đến hàm và đó chỉ là cbrm.

Thế thôi.

Được rồi, vậy tiếp theo chúng ta hãy đi tìm cái này.

Và ở đây chúng ta sẽ gọi nó là một cuộc gọi lại.

Giống như vậy.

Bây giờ chúng ta hãy chuyển sang trường hợp IP cốt lõi.

Và trước tiên hãy kiểm tra nhận xét để gọi lại kết nối.

Và nói nếu sự kiện kết nối Wi-Fi gọi lại.

Sau đó gọi ứng dụng wi fi.

Gọi cho Colbeck.

Được rồi, vậy nếu cuộc gọi lại được thiết lập thì chúng ta sẽ gọi lại.

OK, vậy chúng ta vào phần chính xem nhé.

Và trước tiên, hãy bao gồm.

Nhật ký ESB.

Và sau đó hãy bao gồm.

S&P mất thời gian.

Và sau đó ở đây.

Nó sẽ tạo ra một thẻ.

Và gọi đó là đàn ông.

Và tiếp theo sẽ tạo một cuộc gọi lại dưới dạng ứng dụng Wi-Fi trống, các sự kiện được kết nối.

Và nó trống rỗng.

Và sau đó ở đây, ESB sẽ đăng nhập.

Tại sao ứng dụng fi được kết nối?

Và bây giờ chúng ta có thể gọi S&P Time Sink.

Các cuộc thử nghiệm bắt đầu.

Và hãy tiếp tục bằng cách đặt chức năng này làm hàm gọi lại.

Vì vậy hãy sao chép nó.

Ở dưới đây sẽ thiết lập cuộc gọi lại sự kiện được kết nối.

Sử dụng ứng dụng wi fi của chúng tôi.

Caldbeck nói.

Trong pass, một tham chiếu đến tên hàm.

Và thế là xong.

Vì vậy, hãy xây dựng.

Thịt quả hạch.

Sau đó mở một màn hình.

Và sau đó kết nối với ESPN.

Và vào trang Web với Graham.

Bây giờ, hãy kết nối ESP.

Và hãy xem.

Thật tuyệt, giờ địa phương đã được hiển thị, thật tuyệt.

Và màn hình hiển thị tin nhắn từ đàn ông.

Và tất cả những tin nhắn được mong đợi tiếp theo.

Vì vậy chúng ta hãy lập trình thêm trong bài học tiếp theo.