# 002 Lập trình ứng dụng WiFi Phần I en

---

Được rồi.

Vì vậy, chúng ta sẽ thiết lập phần lập trình wi fi bằng cách thêm một vài tệp mới.

Vì vậy, trước tiên, hãy thêm một tệp nguồn mới.

Vì vậy, hãy thêm một tệp nguồn mới vào tệp chính ở đây.

Và gọi nó là ứng dụng wi fi chấm c.

Và bây giờ hãy thêm một tệp tiêu đề mới.

Và gọi nó là ứng dụng wi fi h.

Và hãy thêm một tệp tiêu đề khác.

Và gọi đó là nhiệm vụ chung.

Và trong tập hợp tệp này, chúng tôi sẽ lưu giữ tất cả thông tin cho các tác vụ ô tô miễn phí sẽ tạo trong suốt

khóa học.

Và bây giờ chúng ta hãy chuyển sang tệp danh sách tạo C và bây giờ chúng ta sẽ thêm tệp nguồn ứng dụng wi fi.

Được rồi.

Tuyệt vời.

Và bây giờ chúng ta hãy chuyển sang phần vợ của --, và anh ấy sẽ xác định cài đặt ứng dụng dành cho người vợ

và tạo các đối tượng giao diện mạng cho điểm truy cập.

Và trạm cũng sẽ thêm một số ID tin nhắn sơ bộ cho các tác vụ ứng dụng và cấu trúc

cho hàng đợi tin nhắn.

Ngoài ra, chúng ta sẽ có một nguyên mẫu cho một hàm gửi tin nhắn đến khối và một hàm khác để bắt đầu.

nhiệm vụ ứng dụng wi fi.

Vì vậy, trước tiên chúng ta cần bao gồm.

Giao diện mạng ESPN và điều đó cần thiết cho các đối tượng giao diện mạng.

Vì vậy, ở đây, hãy xác định cài đặt ứng dụng Wi-Fi.

Và trước tiên hãy xác định ứng dụng wi fi là một ứng dụng phụ.

Và chúng ta sẽ gọi nó là SB 32 AP.

Và đó là điểm truy cập.

Tên.

Và trong trường hợp bạn cần làm rõ một chút, SSA D là mã định danh được đặt dịch vụ và bạn sẽ gặp phải

điều này khi cố gắng kết nối với mạng không dây.

Vì vậy khi chúng ta kết nối sau, bạn sẽ thấy ID ISP 32 SSI hiển thị trong danh sách mạng không dây

trên PC hoặc thiết bị di động của bạn.

Được rồi.

Vì vậy, tiếp theo, hãy xác định mật khẩu Wi Fi AP.

Và đây là mật khẩu bạn sẽ sử dụng khi kết nối với ESP thông qua Asus I.D. chúng ta vừa xác định

bây giờ gọi nó là mật khẩu để đơn giản, nhưng bạn có thể gọi nó là bất cứ tên gì bạn thích.

Như vậy đây sẽ là mật khẩu điểm truy cập Wi-Fi.

Được rồi.

Vì vậy, bây giờ hãy xác định kênh ứng dụng Wi-Fi.

Và chúng tôi sẽ sử dụng Kênh một làm Kênh điểm truy cập.

Và liên quan đến các kênh Wi-Fi, ISP 32 hoạt động ở dải tần 2,4 gigahertz, trong đó có 14 kênh

cách nhau 5 megahertz, ngoại trừ cơ sở 12 megahertz trước Kênh 14.

Vì vậy đảm bảo không can thiệp trong mọi trường hợp.

Giao thức Wi-Fi yêu cầu khoảng cách kênh từ 16,25 đến 22 megahertz, như minh họa ở đây.

Và nếu bạn kiểm tra tài liệu ấn tượng và các tài nguyên mà tôi đã cung cấp, nó đã được đề cập

rằng có một số yếu tố mà nhà phát triển cần cân nhắc khi lựa chọn kênh lập trình

hành vi, đó là những lo ngại về nhiễu, những cân nhắc về mặt pháp lý cũng như các quy định của FCC và khả năng truyền tải.

Ví dụ: một máy phát tám hoặc 2.11 đang sử dụng Kênh một.

Người kia có thể sử dụng Kênh năm hoặc sáu và việc sử dụng Kênh hai hoặc ba không được khuyến khích về mặt pháp lý.

cân nhắc.

Các kênh từ 1 đến 11 có thể được sử dụng an toàn ở hầu hết các quốc gia trên thế giới.

Vì vậy, chúng tôi đã sử dụng Kênh một trong khóa học này.

Nhưng vui lòng xem tài liệu này hoặc bất kỳ tài nguyên nào khác để biết thêm thông tin nếu bạn có

mối quan tâm về việc lựa chọn kênh.

Vì vậy, tiếp theo, chúng tôi sẽ xác định khả năng hiển thị của ứng dụng wi fi mà chúng tôi sẽ gọi là ứng dụng wi fi được hỗ trợ ẩn.

Và điều này sẽ bằng không.

Và điều này xác định điểm truy cập Wi-Fi.

Khả năng hiển thị của ISP 32 và số 0 làm cho nó hiển thị, điều đó có nghĩa là bạn sẽ thực sự nhìn thấy ISP

32 SSD trong danh sách mạng của bạn khi cố gắng kết nối với nó.

Được rồi.

Vì vậy hãy bình luận.

Khả năng hiển thị ứng dụng.

Được rồi.

Vì vậy, tiếp theo, hãy xác định ứng dụng FI.

Kết nối tối đa.

Và tôi sẽ vào năm ở đây.

Nhưng bạn có thể làm nó bất cứ điều gì bạn thích.

Ví dụ: bạn có thể chỉ muốn cho phép một thiết bị kết nối.

Được rồi, đây là ứng dụng của chúng tôi, số lượng khách hàng tối đa.

Phần tiếp theo sẽ xác định khoảng thời gian báo hiệu ứng dụng wi fi.

Là 100 mili giây.

Và khoảng thời gian phát sóng đèn hiệu là độ trễ thời gian giữa mỗi đèn hiệu được gửi bởi bộ định tuyến của bạn hoặc

điểm truy cập.

Trong trường hợp đó là ESB 32.

Vì vậy, theo định nghĩa, giá trị càng thấp thì độ trễ thời gian càng nhỏ, có nghĩa là đèn hiệu được gửi đi

thường xuyên hơn, giá trị càng cao thì độ trễ thời gian càng lớn, điều đó có nghĩa là đèn hiệu

được gửi ít thường xuyên hơn.

Vì vậy, đèn hiệu là cần thiết để thiết bị của bạn nhận được thông tin về bộ định tuyến cụ thể.

Trong trường hợp của chúng tôi, ISP trong đèn hiệu bao gồm một số thông tin như dấu thời gian bên cạnh và các thông tin khác

các tham số khác nhau và hầu hết các bộ định tuyến sẵn có đều có giá trị hàm khoảng thời gian báo hiệu mặc định

được đặt ở mức 100 mili giây và ý nghĩa của khoảng thời gian báo hiệu cao có thể là bạn sẽ đạt được

thông lượng tốt hơn và do đó tốc độ và hiệu suất tốt hơn.

Và khoảng thời gian báo hiệu thấp hơn cho phép phát hiện các bộ định tuyến nhanh hơn vì nó gửi nhiều báo hiệu hơn

thường xuyên.

Và điều này có thể giúp bắt được đèn hiệu trong môi trường thu tín hiệu kém.

Và nếu chúng tôi kiểm tra tài liệu ấn tượng, khoảng thời gian đèn hiệu có sẵn nằm trong khoảng từ 100 đến 60000

mili giây với mặc định là 100 mili giây.

Vì vậy, chúng ta sẽ bắt đầu với 100 mili giây trong khóa học này.

Được rồi.

Vì vậy hãy bình luận.

Khoảng thời gian báo hiệu AP.

Là 100 mili giây.

Theo khuyến nghị.

Hoặc mặc định.

Được rồi.

Vì vậy bây giờ hãy xác định.

Địa chỉ IP của điểm truy cập wi fi.

Như 192.168.0.1

và đây sẽ là IP mặc định của chúng tôi.

Và một lần nữa, đây là IP mà chúng tôi đã gán cho băng mềm và chúng tôi đang cấu hình tĩnh giao diện

của ISP 32.

Vì vậy, tiếp theo, hãy xác định ứng dụng Wi-Fi, Gateway.

Đó cũng là 192.168.0.1.

Và đó là mặc định AP của chúng tôi.

Cổng.

Địa chỉ này phải giống với địa chỉ IP.

Được rồi.

Vì vậy, tiếp theo, hãy xác định.

Mặt nạ mạng ứng dụng wi fi.

Như 55.255.255.0.

Và đó là mặt nạ đậu phộng.

Vì vậy, tiếp theo, hãy xác định.

Băng thông ứng dụng wi fi.

Và chúng ta có thể sử dụng wi fi gạch dưới BW gạch dưới HD 20 và đó là từ trình điều khiển wi fi cho 20

băng thông megahertz.

Và 40 megahertz cũng là một lựa chọn.

Và nếu bạn kiểm tra tài liệu ấn tượng, băng thông mặc định cho chế độ trạm và AP là HD

40.

Và ở chế độ AP, băng thông thực tế được thỏa thuận giữa AP và các trạm kết nối với

AP và nó là HD 40.

Nếu AP ở một trong các trạm hỗ trợ HD 40, nếu không thì đó là HD 20.

Và có nhiều lựa chọn khác nhau cho các trạm chém chế độ AP.

Vì vậy, hãy thoải mái đọc về điều đó.

Và tôi sẽ chỉ tóm tắt đoạn cuối ở đây rằng về mặt lý thuyết, HD 40 có thể đạt được thông lượng tốt hơn

vì tốc độ dữ liệu tối đa có thể lên tới 150 megabit/giây hoặc 72 megabit/giây đối với HD

20.

Vì vậy, chỉ cần tóm tắt và dựa trên những gì tôi đã đọc qua, trong số các tài nguyên, giảm thiểu 20 megahertz

nhiễu kênh nhưng không phù hợp với các ứng dụng có tốc độ dữ liệu cao.

Vì vậy, hãy thoải mái chọn băng thông phù hợp nhất với ứng dụng của bạn trong khi xem xét môi trường xung quanh.

môi trường.

Nhưng tôi sẽ chọn 20 megahertz, vì vậy băng thông AP của chúng tôi sẽ là 20 megahertz.

Và 40 megahertz là lựa chọn khác.

Được rồi.

Vì vậy, tiếp theo hãy xác định WI bằng trạng thái tiết kiệm năng lượng.

Và từ trình điều khiển, chúng ta sẽ sử dụng nguồn wi fi.

Không lưu gì cả.

Và một lần nữa, hãy xem tài liệu và tôi sẽ chỉ nhấn mạnh điều đó khi chúng ta gọi S.P. Wife, tôi đã nói

tiết kiệm điện.

Với nguồn Wi-Fi được lưu, không có thiết bị nào có thể tắt hoàn toàn chế độ ngủ của modem và điều này tiêu thụ điện năng cao hơn nhiều

nhưng cung cấp độ trễ tối thiểu để nhận dữ liệu wi fi trong thời gian thực.

Ở chế độ mặc định, chế độ ngủ của modem là modem tiết kiệm điện tối thiểu, nhưng sẽ sử dụng chuyến bay năm

không tiết kiệm điện.

Được rồi.

Vì vậy Power Save không được sử dụng.

Được rồi.

Vì vậy, tiếp theo, hãy cung cấp một định nghĩa.

Đối với chiều dài được hỗ trợ tối đa.

Và chiều dài đó là 32.

Đó là tiêu chuẩn tối đa của tôi Tripoli.

Ngay bây giờ, hãy xác định độ dài mật khẩu tối đa.

Và đó là 64.

Và tôi tin đó cũng là tiêu chuẩn.

Và tiếp theo, chúng ta sẽ xác định.

Truy xuất kết nối tối đa.

Và tôi sẽ sử dụng năm lần thử.

Và điều này liên quan đến số thử lại.

Đang ngắt kết nối.

Vì vậy, điều này sẽ xử lý các cài đặt cháy rừng cơ bản của chúng tôi.

Và để bạn biết định nghĩa này đến từ đâu, định nghĩa này xuất phát từ tiêu đề ISP, loại Wi-Fi

tập tin.

Ngoài ra, xin lưu ý rằng đây là các tùy chọn chế độ an toàn nguồn điện có sẵn.

Được rồi.

Vì vậy, ở đây hãy tạo các đối tượng giao diện mạng cho trạm và điểm truy cập.

Và chúng tôi sẽ mở rộng điều này để nó hiển thị ở mọi nơi.

Và đó chính là cấu trúc giao diện mạng ISP như một con trỏ và gọi nó là mạng ISP nếu tôi ở lại.

Và bây giờ chúng ta sẽ làm tương tự cho điểm truy cập.

Và gọi nó là ESP nếu AP.

Tiếp theo, chúng ta sẽ tạo ID thông báo cho tác vụ ứng dụng wi fi.

Và tôi sẽ ghi chú ở đây cho bạn rằng bạn có thể mở rộng điều này.

Dựa trên yêu cầu ứng dụng của bạn.

Và chúng tôi sẽ thực sự mở rộng điều này trong khóa học và chúng tôi sẽ nói typedef enum.

Và chúng ta có thể tạo một thẻ ở đây cho nó.

Điều này thực sự không cần thiết nhưng hãy gắn thẻ này là tin nhắn ứng dụng wi fi.

Và nói tin nhắn ứng dụng wi fi.

Khởi động máy chủ HTTP.

Và nói, nó bằng không.

Và chúng tôi sẽ gửi tin nhắn SKU ảnh này đến ứng dụng Wi-Fi để nhận nó.

bài kiểm tra ô tô của bạn.

Và khi nhận được, nó sẽ xử lý việc khởi động máy chủ HTP.

Được rồi, vậy là chúng ta cũng sẽ có một tin nhắn về ứng dụng wi fi.

Kết nối từ máy chủ HTTP.

Và đó là để ứng dụng cho vợ biết khi nào chúng tôi kết nối qua máy chủ HTP.

Được rồi.

Và chúng ta cũng hãy tạo một tin nhắn ứng dụng wi fi.

Luôn kết nối.

IP.

Và chúng tôi sẽ sử dụng thông báo này để cho ứng dụng Wi-Fi biết khi nào ISP được kết nối với thiết bị bên ngoài

điểm truy cập hoặc bộ định tuyến và đã được gán một địa chỉ IP.

Được rồi.

Và hãy gọi đây là tin nhắn ứng dụng wi fi.

Gạch dưới E cho Enam.

Được rồi.

Vì vậy, bây giờ chúng ta sẽ bắt đầu với những tin nhắn này.

Và một lần nữa, những tin nhắn này sẽ được xử lý bởi ứng dụng Wi-Fi cho máy Toast Task State của bạn

và sẽ mở rộng mở rộng khi chúng tôi tiến bộ trong khóa học.

Vì vậy bây giờ hãy tạo ra.

Cấu trúc cho tin nhắn

Q.

Và bây giờ chúng tôi thực sự không làm gì nhiều với cấu trúc này ngoài việc gửi các thông điệp bên trong.

Chà, tôi sẽ để lại một ghi chú ở đây cho bạn như một lời nhắc nhở rằng bạn có thể mở rộng nó theo ý muốn.

Vì vậy, hãy mở rộng điều này dựa trên yêu cầu ứng dụng của bạn.

Ví dụ. thêm loại và tham số khác theo yêu cầu.

Vì vậy đây sẽ là một loại gây cản trở.

Tại sao lại đánh nhau bằng tin nhắn Q.

Và chúng ta sẽ sử dụng enum của chúng ta ở đây.

Ứng dụng tin nhắn WI fi enum.

Và gọi nó là ID tin nhắn.

Được rồi.

Bây giờ, hãy gọi nó là ứng dụng wi fi.

tin nhắn Q.

Đội gạch dưới.

Được rồi.

Tốt.

Vì vậy bây giờ chúng ta hãy tạo nguyên mẫu của chúng ta.

Gửi tin nhắn đến Q.

Hãy thêm ghi chú về tham số ở đây.

Và đó là tin nhắn nó.

Đó là ý tưởng tin nhắn từ enum tin nhắn wi fi.

Và sự trở lại sẽ là sự thật.

Nếu một mục đã được gửi thành công vào hàng đợi.

Nếu không thì PD sai.

Và đây thực sự là tất cả mũ bạn.

Được rồi.

Và hãy thêm ghi chú ở đây vì bạn có thể muốn tự mình mở rộng phần này.

Và tôi sẽ nói mở rộng danh sách tham số.

Dựa trên yêu cầu của bạn.

Ví dụ. cách bạn đã mở rộng cấu trúc tin nhắn khối ứng dụng wi fi.

Được rồi.

Tốt.

Vì vậy, đối với nguyên mẫu hàm, nó sẽ trả về kiểu cơ sở T.

Và chúng ta sẽ gọi nó là ứng dụng wi fi.

Gửi tin nhắn.

Và nó sẽ nhận được tin nhắn ứng dụng wi fi.

Và gọi nó là ID tin nhắn.

Được rồi.

Nó có vẻ tốt.

Và nguyên mẫu tiếp theo.

Nó bắt đầu con đường.

Khỏe.

Nhiệm vụ tự động.

Và giả sử ứng dụng void wi fi bắt đầu.

Và nó không có tham số.

Được rồi.

Vì vậy, đối với phần đầu tập tin, đó là tất cả những gì chúng ta cần bây giờ.

Và có vẻ như có lỗi đánh máy ở đây, vì vậy hãy sửa lỗi đó.

Nó phải là 2552552550 cho mặt nạ lưới.

Và.

Được rồi, tuyệt vời.

Vì vậy tôi sẽ dừng ở đây và chúng ta sẽ tiếp tục lập trình ứng dụng wi fi mà file C cho phần tiếp theo

một.

Và hãy chắc chắn kiểm tra các tài nguyên cho bài học này nếu bạn cần làm rõ thêm về các chủ đề được đề cập.