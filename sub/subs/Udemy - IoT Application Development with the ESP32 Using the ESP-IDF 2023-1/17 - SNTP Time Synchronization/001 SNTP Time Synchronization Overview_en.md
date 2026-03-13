# 001 SNTP Tổng quan về đồng bộ hóa thời gian vi

---

Chào mừng bạn đến với phần đồng bộ hóa thời gian sắp ra mắt tại đây, tôi sẽ mô tả cách triển khai và cung cấp

một số thông tin cơ bản rất ngắn gọn về Giao thức thời gian mạng đơn giản và thảo luận về ESP có liên quan

API RDF cũng vậy.

Vì vậy, hãy bắt tay ngay vào việc thực hiện.

Khi ESP 32 có kết nối, nghĩa là bạn đã kết nối với điểm truy cập có kết nối internet,

chức năng bắt đầu Nhiệm vụ S&P sẽ được gọi là chức năng bắt đầu nhiệm vụ sẽ đặt thời gian tự động miễn phí

tác vụ đồng bộ hóa, tác vụ này sẽ gọi một hàm lấy thời gian cập nhật.

Ngoài ra, tôi nên đề cập rằng trong quá trình triển khai này, tác vụ sẽ tiếp tục đồng bộ hóa và kiểm tra

rằng thời gian đã được cập nhật.

Về hàm thời gian thu được, hàm này sẽ khởi tạo cùng một dịch vụ TV để truy vấn Nesson

Máy chủ TBE cho Giờ quốc tế.

Hơn nữa, hàm thời gian thu được sẽ được khởi tạo trong trường hợp thời gian không được cập nhật.

Múi giờ địa phương sẽ được đặt sau khi dịch vụ SMTP được khởi tạo.

Máy chủ Web sẽ được cảnh báo khi khởi tạo và sẽ phản hồi theo thời gian cập nhật.

Được rồi, chúng ta hãy xem một số thông tin bổ sung về giao thức thời gian Mạng Đơn giản.

S&P hay Giao thức thời gian mạng đơn giản là giao thức được thiết kế để đồng bộ hóa đồng hồ của các thiết bị được kết nối

lên mạng.

Hoạt động cơ bản như sau Máy khách hoặc ESP 32 kết nối với máy chủ bằng giao thức UDP

trên cổng 123.

Máy khách truyền gói yêu cầu đến máy chủ, sau đó máy chủ phản hồi bằng dấu thời gian

gói.

Sau đó, khách hàng có thể chuyển các giá trị ngày và giờ hiện tại.

Vì vậy, nói chung, nếu ESP 32 được kết nối với internet, nó có thể lấy ngày giờ bằng S&P.

Ngoài ra, tôi nên đề cập rằng S&P trong SPF được hỗ trợ bởi các chức năng IP nhẹ.

Bây giờ, hãy xem lại SPF có thể giúp chúng ta thiết lập và hoạt động như thế nào.

Tôi khuyên bạn nên xem lại tài liệu A.P. từ Impressive.

Bạn có thể tìm thấy tất cả thông tin liên quan tại đây cũng như một số chức năng mà chúng tôi sẽ sử dụng.

Ngoài ra, tôi nên đề cập rằng sẽ đặt múi giờ bằng cách sử dụng các chức năng sau được thiết lập ở đây, chúng tôi sẽ

được sử dụng để đặt múi giờ cụ thể và để khởi tạo quy trình chuyển đổi múi giờ.

Thông tin thêm về điều này sẽ được trình bày trong các slide tiếp theo.

Được rồi, một số thứ này có thể không kết hợp được với nhau cho đến khi chúng ta thực sự bắt đầu viết mã.

Nhưng tôi nghĩ việc xem xét nhanh có thể hữu ích khi chúng tôi thực sự làm điều đó.

Được rồi, sau khi tác vụ ô tô miễn phí bắt đầu và hàm thời gian thu được được gọi, Khởi tạo

Chức năng S.P. được gọi, chức năng SMTP đầu tiên được sử dụng để định cấu hình máy khách trong quá trình kéo

chế độ truy vấn máy chủ mỗi giây.

Chức năng thực hiện điều này là chức năng chế độ vận hành sẽ sớm được thiết lập bằng cách sử dụng bước tăng cường

chế độ thăm dò ý kiến làm tham số đầu vào.

Cũng trong chức năng Khởi tạo S.A., chúng tôi sẽ cho khách hàng biết máy chủ nào sẽ sử dụng lựa chọn chung

S&P cho biết là một cụm máy chủ từ nhóm mà tổ chức A.P. sẽ chỉ định điều này trong chức năng.

Tên máy chủ.

Sau đó, chúng ta sẽ khởi tạo dịch vụ bằng S.P. Khởi tạo sau khi hoàn tất, chúng ta có thể đặt thời gian

biến vùng và khởi tạo chuyển đổi múi giờ.

Chúng tôi sẽ đặt múi giờ bằng cách sử dụng chức năng EMV đã đặt, chỉ định Tzi cho múi giờ và địa phương của bạn.

chuỗi múi giờ, sau đó gọi hàm đặt múi giờ để khởi tạo quy trình chuyển đổi múi giờ.

Sau khi dịch vụ được khởi tạo, chúng ta cần kiểm tra xem đồng hồ hệ thống đã được cập nhật chưa, thời gian để thực hiện dịch vụ đó chưa.

lấy thời gian thực tế từ đồng hồ hệ thống.

Chúng ta sẽ sử dụng hàm thời gian để cập nhật biến loại thời gian và chia biến thành các phần khác nhau.

giá trị thời gian như năm, tháng, ngày.

Giờ địa phương gạch dưới chức năng của chúng tôi được sử dụng, cập nhật cấu trúc nhóm như trong hình

ở đây.

Thôi thì kiểm tra thông tin từ đội đánh xem đã ấn định thời gian chưa.

Giống như trong hình ảnh hiển thị dưới đây.

Được rồi, bây giờ thế là đủ rồi.

Hãy bắt đầu viết mã trong phần tiếp theo.