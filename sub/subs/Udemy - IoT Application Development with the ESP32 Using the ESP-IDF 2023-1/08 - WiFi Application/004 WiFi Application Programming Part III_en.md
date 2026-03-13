# 004 Lập trình ứng dụng WiFi Phần III vi

---

Được rồi, hãy tiếp tục từ nơi chúng ta đã dừng lại và xác định trình xử lý sự kiện trong hàm.

Vì vậy hãy sao chép nó.

Và hãy bình luận ở đây.

Khởi tạo ứng dụng wi fi.

Trình xử lý sự kiện cho các sự kiện Wi-Fi và IP.

Và hàm này sẽ không có tên hàm.

Và nó không có tham số.

Và anh ta sẽ nói vòng lặp sự kiện cho người vợ lái xe.

Bây giờ, hãy kiểm tra SPRO.

Vòng lặp sự kiện ESP tạo ra.

Và chọn tạo mặc định.

Và tiếp theo, chúng ta sẽ tạo trình xử lý sự kiện cho kết nối.

Và sau đó chúng ta sẽ cần một loại phiên bản xử lý sự kiện ESP.

Và gọi nó là sự kiện cháy nổ.

Và bây giờ sao chép loại phiên bản.

Và dán nó.

Và bây giờ ở đây, hãy gọi nó là sự kiện IP mẫu.

Và tiếp theo, kiểm tra SPRO.

Trình xử lý sự kiện ESG.

Đã đăng ký phiên bản.

Và cơ sở sự kiện là sự kiện Wi-Fi.

ID sự kiện là sự kiện ESP, bất kỳ ID nào.

Và trình xử lý sự kiện là một tham chiếu đến tên hàm mà chúng ta sẽ gọi là trình xử lý sự kiện của ứng dụng wi fi.

Việc xử lý, các đối số là không.

Và instance sẽ là một tham chiếu đến instance tại sao lại xảy ra sự kiện cháy?

An bây giờ đã sao chép dòng này.

Và được đặt bên dưới.

Và bây giờ chúng tôi muốn các sự kiện IP.

Và ID cũng vậy.

Trình xử lý giống nhau, và điều này là không.

Và thay đổi tham chiếu đến phiên bản, sự kiện IP.

Và thế là xong.

Vì vậy, bây giờ chúng ta cần xác định trình xử lý sự kiện này.

Vậy chúng ta hãy đến đây.

Và hãy bình luận, trình xử lý sự kiện ứng dụng Wi-Fi.

Và tham số đầu tiên ARG là dữ liệu.

Ngoài dữ liệu sự kiện.

Điều đó được chuyển cho người xử lý.

Khi nó được gọi.

Và cơ sở sự kiện tham số thứ hai.

Hỗ trợ cơ bản của sự kiện có được đăng ký để xử lý không?

Và sự kiện tham số thứ ba, I.D..

Ý tưởng về sự kiện có phải là đăng ký trình xử lý không?

Và dữ liệu sự kiện tham số thứ tư.

Là dữ liệu sự kiện?

Vì vậy hàm này là static void.

Trình xử lý sự kiện ứng dụng WI fi và tham số đầu tiên là điểm trống đối với ARG.

Tham số tiếp theo là loại dựa trên sự kiện ESP.

Và nó thậm chí còn có cơ sở.

Tiếp theo là trong 30 tới.

ID sự kiện.

Và cuối cùng là dữ liệu sự kiện con trỏ void.

Sau đó ở đây sẽ nói nếu.

Âm trầm sự kiện.

Là một sự kiện Wi-Fi.

Sau đó chúng ta sẽ chuyển đổi.

ID sự kiện.

Và bây giờ chúng ta sẽ mở một vụ án.

Đối với sự kiện Wi-Fi.

AP bắt đầu.

Và bây giờ hãy ghi lại thông báo cho trường hợp này bằng thông tin nhật ký ESP.

Thẻ của chúng tôi.

Và ứng dụng sự kiện Tin nhắn Wi-Fi bắt đầu.

Và sau đó bao gồm nghỉ giải lao.

Và sự kiện wi fi này ở đây chỉ là một trong số rất nhiều sự kiện.

Vì vậy, hãy đến đây và xem qua loại sự kiện bạn có thể đưa vào và chỉ cần tạo chúng trong trình xử lý sự kiện

và bạn có thể xử lý chúng trong ứng dụng của mình.

Vì vậy hãy sao chép sự kiện này.

Và chúng ta sẽ tạo ra một cái khác.

Đối với ứng dụng Wi-Fi, hãy dừng lại.

Và bây giờ hãy tạo một sự kiện khác.

Để bắt đầu.

Và bây giờ chúng ta hãy làm điều tương tự.

Luôn kết nối.

Bây giờ chúng ta hãy làm một cái khác.

Để luôn bị ngắt kết nối.

Hãy quay lại đây và làm một cái khác.

Đối với AP, hãy luôn kết nối.

Và bây giờ hãy làm một cái khác.

Để ở lại bị ngắt kết nối.

Được rồi, tốt, vậy là nó sẽ đáp ứng được nhu cầu cơ bản của chúng ta bây giờ.

Và bây giờ hãy xuống đây và nói khác nếu.

Âm trầm sự kiện.

Là một sự kiện IP.

Sau đó nói Chuyển đổi ID sự kiện.

Và hãy tạo một trường hợp mới ở đây.

Sự kiện IP FDA.

IP ruột.

Và bây giờ hãy xem thông tin nhật ký của S.P.

Tin nhắn.

Đối với tiểu bang, có sự kiện IP.

Và sau đó chúng ta hãy nghỉ ngơi.

Được rồi, vậy là xong cho cái này.

Bây giờ chúng ta có thể xác định mặc định bằng niềm tin vào chức năng CNTT.

Và hãy bình luận.

Khởi tạo ngăn xếp TCP.

Trong cấu hình Wi-Fi mặc định.

Và nó là khoảng trống tĩnh của chức năng, và nó là khoảng trống.

Và trước hết, hãy khởi tạo ngăn xếp TCP.

Và kiểm tra ESPN.

Mạng tốc độ nếu.

Hàm khởi tạo.

Và tiếp theo, chúng ta sẽ thực hiện cấu hình wi fi mặc định.

Và tôi sẽ chỉ đề cập rằng các hoạt động phải theo thứ tự này.

Bây giờ chúng ta cần một phiên bản của wi fi trong loại cấu hình đó.

Và gọi nó là màu trắng, bay vào đó, config.

Và khởi tạo nó với wi fi trong cấu hình.

Chức năng mặc định.

Và ở đây, hãy kiểm tra Espera.

SPV, tôi chiến đấu trong đó.

Và chuyển một tham chiếu đến cuộc chiến trắng này trong cấu hình đó.

Và hóa đơn tiếp theo, SB air check.

S.P. Rifai cho biết lưu trữ dưới dạng Wi-Fi, lưu trữ RAM.

Và bây giờ hãy lấy đối tượng giao diện mạng của chúng ta.

Và hãy khởi tạo nó.

Sử dụng mạng ISP nếu.

Tạo màu trắng mặc định bằng.

Ở lại.

Sau đó hãy khởi tạo đối tượng AP.

Sử dụng mạng ESG nếu.

Tạo mặc định.

WI fi AP.

Tuyệt, thế thôi.

Bây giờ, hãy tạo cấu hình AP mềm.

Và hãy bình luận.

Định cấu hình cài đặt điểm truy cập wi fi.

Và thiết kế IP tĩnh.

Đến AP mềm.

Và đó là một khoảng trống tĩnh.

Ứng dụng WI fi ngoài cấu hình AP.

Và nó trống rỗng.

Ngay bây giờ, giả sử API mềm, cấu hình Điểm truy cập Wi-Fi.

Và bây giờ tạo cấu trúc cấu hình Wi-Fi.

Và gọi nó là cấu hình AP.

Và anh ta sẽ cần chỉ định cấu hình điểm truy cập.

Giống như vậy.

Và sau đó đặt sang một bên.

Đối với AP wi fi của chúng tôi, một vụ tự sát.

Tiếp theo, đặt chiều dài bờ biển.

Sử dụng Stalin của wi fi.

AP Một vụ tự tử.

Và sau đó là mật khẩu.

Sẽ là mật khẩu ứng dụng wi fi của chúng tôi.

Và đó là kênh.

Sẽ là kênh ứng dụng wi fi của chúng tôi.

Và sau đó SSD bị ẩn.

Vợ anh theo AP, tự sát.

Ẩn giấu.

Ở chế độ ủy quyền.

Chúng tôi sẽ tắt Wi-Fi.

WPA hai.

Và bây giờ là kết nối Max.

Chúng ta sẽ sử dụng Wi-Fi AP.

Kết nối tối đa.

Và sau đó là khoảng thời gian báo hiệu.

Chúng ta sẽ có wi fi, khoảng thời gian AP Beacon.

Đây thực ra phải là dấu phẩy ở đây.

Bây giờ chúng ta hãy.

Cấu hình, DHP.

Đối với điểm truy cập.

Bây giờ, hãy tạo một phiên bản của mạng ESPN nếu loại thông tin IP.

Và gọi nó là thông tin AP IP.

Và bây giờ hãy thiết lập điều này.

Thông tin API.

Hai số 0 cho kích thước của thông tin API.

Được rồi, bởi vì chúng tôi muốn chuyện này được làm rõ trước.

Và bây giờ hãy gọi mạng ESPN nếu.

Bài đăng của DHC.

Và đó là nơi mạng lưới ESG của chúng tôi nếu ứng dụng.

Và chức năng này dừng máy chủ DHP mà chúng tôi muốn thực hiện việc này trước khi thực hiện bất kỳ cập nhật nào liên quan đến DHC.

Và một lần nữa, đó là gian lận và nếu AP phản đối bạn.

Và chúng tôi sẽ nói.

Musk đã gọi điện đầu tiên cho mình.

Bởi vì chúng ta muốn gọi cái này trước khi thực hiện bất kỳ thay đổi nào.

Và sau đó hãy gọi cho Annette Piton.

Và chỉ định nếu tôi nhận được.

Vậy thì tại sao lại là một đường ống?

Với tham chiếu đến thông tin API của chúng tôi.

Địa chỉ IP.

Bây giờ tôi sẽ nói ở đây, gán điểm truy cập, IP tĩnh.

Cổng và mặt nạ mạng.

Và chức năng này làm là chuyển đổi một địa chỉ internet và định dạng văn bản tiêu chuẩn thành

dạng nhị phân số của nó.

Và đó là những gì chúng tôi muốn ở đây.

Vì vậy bây giờ chúng ta hãy sao chép dòng này và sau đó thực hiện tương tự cho Gateway.

Và Cổng ở đây.

Và một lần nữa, đối với netmask.

Và cái mặt nạ đó là bạn.

Được rồi, Greg.

Vì vậy bây giờ hãy kiểm tra Espero.

Mạng ESPN, nếu nói IP và điện thoại.

Và chỉ định ESPN của chúng tôi tại AP và tham chiếu đến thông tin IP AP của chúng tôi.

Và bây giờ là SPRO, hãy kiểm tra.

ESPN rằng nếu.

Khởi động GPS DHC.

Và một lần nữa, hãy sử dụng mạng tốc độ không khí của chúng tôi nếu đối tượng AP.

Và với bạn, tôi sẽ chỉ bình luận.

Cấu hình tĩnh giao diện mạng.

Và cái này.

Khởi động AP.

máy chủ DHC.

Đối với các trạm kết nối

Ví dụ: thiết bị di động của bạn.

Và bây giờ hãy kiểm tra Espero.

Chế độ cài đặt ESP.

Và chế độ chúng tôi muốn là chế độ wifey.

AP.

Ở lại.

Và chúng tôi ở đây.

Đặt chế độ làm điểm truy cập.

Chế độ trạm.

Và sau đó hãy kiểm tra SPRO.

Wi-Fi ESB.

Cấu hình đã nói.

Đối với giao diện ISP.

Điểm truy cập Wi-Fi.

Và tham khảo cấu hình AP.

Và đây.

Chúng tôi đã thiết lập cấu hình của mình.

Và sau đó kiểm tra ESPN.

ESP wi fi cho biết băng thông.

Đối với điểm truy cập giao diện Wi-Fi.

Và sử dụng băng thông ứng dụng wi fi của chúng tôi.

Và đó là nơi có băng thông mặc định của chúng tôi.

20 megahertz.

Và một lần nữa, hãy kiểm tra SPRO.

Wi-Fi ESB.

Đặt nguồn, lưu an toàn.

Để tiết kiệm năng lượng năm sao màu trắng của chúng tôi.

Và đó là mức tiết kiệm năng lượng của chúng tôi được đặt thành không.

Điều mà trước đây chúng tôi đã xác định bạn trong phần đầu của tệp.

OK, vậy bây giờ tôi sẽ chỉ kiểm tra cái này.

Điều này có vẻ tốt.

Và ở trên đây, tin nhắn này.

Điều này nên được ngắt kết nối.

Vì vậy, hãy đăng nhập nó một cách chính xác.

Và vì vậy chỉ cần chắc chắn về điều đó.

Và bây giờ cái này sẽ ở trạng thái tĩnh.

OK bây giờ chúng ta build cho chắc chắn, không có lỗi gì nhé.

Được rồi, điều đó có vẻ tốt.

Vì vậy chúng ta hãy hoàn thiện và kiểm tra điều này trong bài học tiếp theo.