# 003 Lập trình cập nhật chương trình cơ sở OTA Phần II vi

---

Được rồi, hãy tiếp tục.

Và lấy phần xử lý trạng thái OTA của tên hàm.

Và hãy định nghĩa nó ở đây.

Và nhận xét rằng trình xử lý trạng thái OTA phản hồi với trạng thái cập nhật chương trình cơ sở sau khi cập nhật OTA

bắt đầu.

Và phản hồi với thời gian biên dịch.

Và hẹn hò.

Khi trang được yêu cầu lần đầu tiên.

Và tham số Q đã có là các yêu cầu HTTP mà bạn đúng cần được xử lý.

Và kết quả trả về là ESP, được chứ?

Được rồi.

Và đây là loại ESP.

Và đó là trình xử lý trạng thái trạng thái của chúng tôi, sử dụng loại yêu cầu ftpd.

Con trỏ chỉ số IQ của chúng tôi.

Và hãy tạo một bộ đệm Jason chăm sóc.

Với chiều dài 100.

Và sau đó đăng nhập trạng thái OTA được yêu cầu.

Bây giờ chúng ta sẽ bắt Jeff làm gì, Jason?

Và bây giờ hãy theo dõi tôi khi chúng ta bước vào chuỗi Jason Escape được yêu cầu.

Cứ như vậy và vào trạng thái cập nhật OTA của chúng tôi.

Và sau đó tiếp tục.

Và sau đó vào thời gian biên dịch.

Và tiếp theo là ngày biên dịch.

Và sau đó chúng ta có thể đóng nó lại và cung cấp cho nó trạng thái cập nhật chương trình cơ sở toàn cầu.

Và sau đó đưa ra định nghĩa về thời gian.

Và ngày tháng.

Và đó là điều dành cho Jason.

Vì vậy, bây giờ hãy đặt loại phản hồi.

Đối với yêu cầu này dưới dạng ứng dụng JSON.

Và sau đó chúng tôi sẽ gửi phản hồi cho yêu cầu.

Từ The Sun, và chúng tôi muốn Star of the Sun.

Và ESP vừa được trả lại, được chứ?

Được rồi, như vậy ở đây chúng ta vừa cập nhật trang Web với trạng thái cập nhật OTA, thời gian biên dịch và biên dịch

date bằng cách sử dụng các giá trị từ đây.

Vì vậy, bây giờ hãy xem cách thức hoạt động của tính năng này bằng cách truy cập James và nhận trạng thái cập nhật.

Ở đây chúng tôi cần cập nhật ngày và giờ biên dịch cho ID ngày của phần tử chương trình cơ sở mới nhất này, đó là

ở đây trong chỉ mục HTML đó.

Được rồi.

Và sau đó, tùy thuộc vào trạng thái cập nhật OTA, chúng tôi sẽ phản hồi bằng cách bắt đầu hẹn giờ khởi động lại hoặc

thông báo lỗi tải lên được hiển thị trên trang.

Và thời gian khởi động lại cập nhật với thông báo ở đây và bộ hẹn giờ khởi động lại được gọi đệ quy ở đây,

trang trí mỗi lần.

Được rồi, vì vậy chúng ta cũng cần định cấu hình bộ hẹn giờ này ở phía máy chủ web.

Vì vậy chúng ta hãy quay trở lại máy chủ FTP xem file.

Và ở đầu tập tin.

Chúng ta có thể tạo cấu hình hẹn giờ ECP 32.

Điều này được chuyển tới thời điểm tạo ESP.

Và sau đó nói, bộ đếm thời gian Konst ESP, tạo loại đối số.

Và gọi nó là cập nhật chương trình cơ sở, đặt lại vòng cung.

Và bây giờ chúng tôi cần một cuộc gọi lại.

Lệnh gọi lại thiết lập lại bản cập nhật chương trình cơ sở của chúng tôi là gì

ngay tại đây.

Và bây giờ là ARG của chúng ta và phương thức điều phối là tác vụ hẹn giờ ESP.

Và tên là thiết lập lại cập nhật firmware.

Được rồi, bây giờ, hãy nói thể thao điện tử, đồng hồ bấm giờ, tay cầm, loại.

Cập nhật chương trình cơ sở có được thiết lập lại không?

Và tiếp theo, chúng ta cần một hàm khác và chúng ta sẽ định nghĩa một hàm khác ở đây.

Kiểm tra trạng thái cập nhật chương trình cơ sở toàn cầu.

Biến này ở đây là gì?

Vì vậy, chúng tôi sẽ kiểm tra nó.

Và nó tạo ra bộ đếm thời gian thiết lập lại cập nhật chương trình cơ sở.

Nếu trạng thái cập nhật chương trình cơ sở toàn cầu là đúng.

Và đó sẽ là một khoảng trống tĩnh.

Máy chủ HTTP.

Cập nhật chương trình cơ sở, đặt lại bộ đếm thời gian.

Và nó trống rỗng.

Được rồi, vậy hãy nói xem trạng thái cập nhật firmware toàn cầu có cập nhật OTA thành công không?

Sau đó đăng nhập ESG.

Cái đó.

Cập nhật firmware thành công.

Và sau đó chúng tôi sẽ cho trang Web cơ hội nhận và xác nhận lại.

Và khởi tạo bộ đếm thời gian.

Sau đó SPRO, kiểm tra.

Thời gian ESP hoặc tạo.

Và chuyển một tham chiếu đến các đối số thiết lập lại và một tham chiếu đến thiết lập lại bản cập nhật chương trình cơ sở.

Bây giờ chúng ta cần kiểm tra Espero.

Bộ đếm thời gian BSP bắt đầu một lần.

Và vượt qua quá trình thiết lập lại bản cập nhật chương trình cơ sở và thời gian tính bằng micro giây.

Điều mà chúng ta có thể làm ở đây có lẽ là tám giây.

Vậy chúng ta sẽ nói khác.

Nhật ký S.P.

Rằng việc cập nhật firmware không thành công.

OK, vậy bây giờ hãy nắm bắt chức năng này.

Và chúng tôi sẽ gọi nó ở đây theo bản cập nhật chương trình cơ sở.

Trường hợp thành công.

Được rồi.

Tiếp theo chúng ta hãy đi xuống.

Và chúng ta cần xác định một cuộc gọi lại.

Vậy hãy lấy nguyên mẫu nhé bạn.

Và sau đó hãy thả nó ngay tại đây.

Và chúng ta sẽ nói nhật ký ESP.

Đó là thời gian hoặc thời gian xử lý.

Khởi động lại thiết bị.

Được rồi, hãy gọi Khởi động lại ESP.

Được rồi, điều đó có vẻ tốt.

Và còn một điều nữa mà tôi quên mất ở đây.

Và bản cập nhật nhằm tăng nội dung nhận được theo độ dài phần nội dung.

Vì vậy, hãy làm điều đó.

Bây giờ, hãy xây dựng dự án.

Và chúng tôi không có lỗi.

Tuyệt vời, vậy chúng ta hãy kiểm tra điều này trong bài học tiếp theo.