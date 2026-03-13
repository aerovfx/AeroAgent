# 001 Lập trình nút ngắt kết nối WiFi vi

---

Và bài học này sẽ triển khai chức năng đằng sau nút Disconnect.

Chúng ta sẽ bắt đầu từ đây và bắt cóc James, và trong chức năng chuẩn bị tài liệu, chúng ta sẽ tạo một cái khác trên

chức năng nhấp chuột.

Vì vậy hãy sao chép cái này ngay tại đây.

Và tốc độ bên dưới.

Và thay đổi nó thành ngắt kết nối, tại sao tốt?

Và thay đổi tên chức năng ngắt kết nối bằng điện thoại.

Được rồi, hãy sao chép chức năng này.

Và chúng ta hãy đi xuống cuối tập tin.

Và bây giờ hãy đưa ra nhận xét.

Ngắt kết nối vuốt năm.

Sau khi nhấn nút ngắt kết nối.

Và tải lại trang Web.

Và đó là một chức năng.

Ngắt kết nối wi fi.

Và ở đây sẽ sử dụng Ajax.

Và đối với Irwell, đó là ngắt kết nối Wi-Fi về phía trước, Jason.

Và kiểu dữ liệu

Cái này, Jason.

Và phương pháp.

Là xóa.

Điều này sai.

Dữ liệu.

Là dấu thời gian.

Dữ liệu bây giờ.

Bây giờ ở dấu chấm phẩy.

Và ở đây sẽ cập nhật trang Web.

Và sử dụng thời gian chờ đã đặt.

Và chỉ cần theo tôi ở đây.

Vị trí, không tải lại.

Đúng với dấu chấm phẩy bên trong.

Sau đó, dấu phẩy và hãy đặt trang tải lại sau 20 mili giây.

ĐƯỢC RỒI.

Vì vậy, khi nhấn nút ngắt kết nối, chức năng này sẽ được gọi và nó sẽ làm mới trang sau đó.

hai giây.

Trong khi đó, ở phía máy chủ web, Wi-Fi bị ngắt kết nối và điều đó sẽ được triển khai trong trình xử lý.

Được rồi, vì vậy hãy triển khai điều đó ngay bây giờ và chuyển sang HTP, Máy chủ sẽ thấy.

Vì vậy, chúng ta sẽ bắt đầu bằng cách sao chép thông tin xử lý mắt của bạn.

Và hãy sử dụng lại nó bên dưới.

Và trước tiên, hãy thay đổi điều này thành ngắt kết nối Wi-Fi.

Đó, Jason.

Và tên cấu trúc để ngắt kết nối Wi-Fi.

Và nước tiểu.

Wi-Fi có bị ngắt kết nối không, Jason?

Phương pháp là xóa HTP.

Và trình xử lý, đó là máy chủ HTP, ngắt kết nối Wi-Fi.

Jason Handler.

Được rồi, hãy chuyển tên cấu trúc để đăng ký rằng bạn là người xử lý.

Và hãy đi lên và định nghĩa nó.

Bây giờ hãy sao chép bình luận này.

Và nó.

Và thay đổi điều này thành ngắt kết nối Wi-Fi, Jason.

Và chúng ta sẽ nói phản hồi bằng cách gửi tin nhắn cho vợ bằng ứng dụng để ngắt kết nối.

Sau đó hãy lấy tên.

Sao chép nó.

Và bây giờ giả sử băng siêu tốc tĩnh, hãy bỏ tên và con trỏ loại yêu cầu http tuổi của nó.

Ari Kim.

Và bây giờ nhật ký SP.

Tại sao lại ngắt kết nối, Jason yêu cầu?

Trong các ứng dụng và tin nhắn wi fi của năm tới.

Và chúng ta sẽ nói ở đây, tin nhắn wi fi.

Trạng thái ngắt kết nối do người dùng yêu cầu.

Và sẽ xác định điều đó sau.

Giờ hãy trả lại ESP, được chứ?

Tiếp theo, hãy sao chép cái này.

Và chúng ta sẽ tạo một tin nhắn trong ứng dụng Wi-Fi.

Vì vậy hãy truy cập ứng dụng Wi-Fi Dunwich.

Và chúng ta hãy thả nó ngay tại đây.

OK, bây giờ chúng ta hãy chuyển sang phần xử lý tin nhắn của tệp xem.

Và bây giờ hãy sao chép thông báo trường hợp này.

Và dán ở đây.

Và trước tiên, hãy loại bỏ điều này và bây giờ hãy cập nhật trường hợp thông báo mà người dùng yêu cầu duy trì ngắt kết nối.

Và bây giờ hãy cập nhật thông điệp tường trình.

Và bây giờ ở đây sẽ cập nhật số thử lại toàn cầu.

Và chúng tôi sẽ đặt nó ở Max Connection Retrace.

Bởi vì chúng tôi không muốn thử kết nối lại khi nhấn nút ngắt kết nối.

Được rồi, tiếp theo chúng ta sẽ gọi hàm ngắt kết nối, điều này sẽ dẫn đến trường hợp bên dưới và sau đó

thông báo không được gửi đến máy chủ web và chúng tôi sẽ cần điều chỉnh máy trạng thái của mình ở đây để bù lại

cho việc này sau.

Bây giờ chúng ta hãy tiếp tục.

Và đó là kiểm tra siêu năng lực.

Ngắt kết nối Wi-Fi ESP.

Và bây giờ chúng ta cùng thay đổi trạng thái led Ogbe thành nhé.

Máy chủ FTP dẫn đầu GB của chúng tôi đã bắt đầu.

OK, vậy nên tôi không chắc cái tên này có ý nghĩa gì nữa nên tôi chỉ góp ý cho bạn hay để làm thôi.

Việc đổi tên trạng thái này dẫn đến một cái tên có ý nghĩa hơn.

Hoặc theo ý thích của bạn.

Vì vậy, có thể bạn nên thay đổi nó nếu muốn.

Bây giờ, chúng ta hãy xây dựng dự án.

Và một khi bạn thịt nó.

Bây giờ, hãy kết nối với ESPN.

Sau đó bây giờ tôi sẽ đi đến trang Web.

Và bây giờ, thực sự, chúng tôi muốn mở màn hình.

Ngoài ra, tôi đã làm ngược lại, vì vậy đừng làm theo cách này.

Bạn sẽ muốn thực hiện theo dõi trước, sau đó truy cập trang web.

Bởi vì bây giờ có lẽ tôi sẽ phải tải lại trang Web.

Vậy hãy để tôi làm điều đó.

Và sau đó tôi sẽ đảm bảo rằng tôi đã kết nối.

ĐƯỢC RỒI.

Và bây giờ chúng ta quay lại, được chứ?

Vì vậy, hãy kết nối, bạn biết đấy, mật khẩu.

Và kết nối.

Được rồi, tốt, bây giờ chúng ta hãy tải lại để kiểm tra.

Được rồi, bây giờ chúng ta hãy ngắt kết nối.

Đẹp.

Thông tin Trang được tải lại và Kết nối bị xóa và chúng tôi không còn kết nối với điểm truy cập nữa.

Xuất sắc.

Tuyệt vời.

Vậy chúng ta cùng tiếp tục phát triển ở bài học tiếp theo nhé.