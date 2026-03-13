# Tổng quan triển khai máy chủ HTTP 001 vi

---

Trong phần này, chúng ta sẽ xem xét việc triển khai máy chủ HTP, đây là thành phần chính của

ứng dụng mạng cục bộ không dây.

Và tất nhiên, nó hỗ trợ trang web.

Vậy chúng ta cùng đi vào phần tổng quan triển khai, trước hết Web server hỗ trợ trang web

các tệp, bao gồm tài liệu HTML, tệp CSIS và tệp JavaScript và sẽ sử dụng tệp này

trang web để tương tác với SB 32.

Và điều đó bao gồm hỗ trợ cho OTA hoặc qua các bản cập nhật chương trình cơ sở và cũng hiển thị nhiệt độ và độ ẩm

chỉ số cảm biến.

Và máy chủ web cũng sẽ có thể phản hồi các nút kết nối và ngắt kết nối, ví dụ:

bằng cách nhập SSA, ID và mật khẩu vào các trường văn bản cho điểm truy cập hoặc bộ định tuyến mà bạn muốn

để kết nối và bằng cách nhấp vào Kết nối, các nỗ lực kết nối sẽ được thực hiện.

Và trong trường hợp ESP 32 đã được kết nối với điểm truy cập, việc nhấp vào ngắt kết nối sẽ kích hoạt

một hành động ở phía máy chủ web buộc SB 32 phải ngắt kết nối.

Ngoài ra, máy chủ web sẽ có thể xử lý việc gửi thông tin kết nối tới trang Web, chẳng hạn như

sự tự tử của điểm truy cập mà SB 32 được kết nối và IP, Gateway và Netmask đã được ký

tới ESB.

Và sau này trong khóa học sẽ hiển thị mặt bên của SB 32 trên trang web.

Vì vậy, khi bạn học cách thực hiện tất cả các tác vụ này, bạn sẽ biết cách gửi dữ liệu đến trang web và nhận

dữ liệu từ trang này, cho phép bạn viết các ứng dụng LAN tùy chỉnh của riêng mình.

Bây giờ hãy nói về các tệp trang Web, các tệp tài nguyên trong phần này bao gồm tệp HTML

đã bao gồm đánh dấu cho bản cập nhật OTA.

Về cơ bản, tại thời điểm này chỉ có một vài nút, tuy nhiên, sẽ mở rộng trên tệp này trong suốt

khóa học và ứng dụng sẽ thấy tệp cho biết là biểu định kiểu cho tài liệu HTML cạnh chỉ mục,

và điều đó cũng sẽ tiếp tục mở rộng khi chúng ta tiếp tục khóa học.

Và nó đã có kiểu dáng cho mẫu mà tôi đã cung cấp.

Và tệp Duchess cũng là tệp JavaScript, đã bao gồm các chức năng OTA và sẽ

cũng mở rộng điều này bằng cách thêm các chức năng trong suốt khóa học.

Và biểu tượng yêu thích mà tôi có thể gửi là biểu tượng được hiển thị trên thanh địa chỉ của trình duyệt.

Và cuối cùng, tệp J Query là thư viện JavaScript kích hoạt chức năng JavaScript

sẽ được sử dụng.

Bây giờ, hãy nói ngắn gọn về các thành phần máy chủ 8TB của IDF.

Vì vậy, đây là bài đọc gợi ý cho phần này.

Hãy nhớ kiểm tra máy chủ HTP, liên kết tham chiếu API tới phần tổng quan ở đây bao gồm rất nhiều nội dung

chúng ta thực sự sẽ thực hiện khóa học này và các chức năng được sử dụng.

Và nếu bạn theo liên kết thứ hai, nó sẽ đưa bạn đến một ví dụ.

Ở sâu hơn trên cùng một trang, bạn sẽ thấy rằng việc triển khai của chúng tôi tuân theo cấu trúc rất giống nhau

với ví dụ này được hiển thị ở đây.

Vì vậy, chúng ta hãy xem một số bước chúng ta sẽ phải thực hiện để thiết lập và chạy máy chủ web.

Một trong những bước đầu tiên sẽ thực hiện là nhúng dữ liệu nhị phân vào các tệp HTML, CSS và JavaScript, vì vậy hãy làm theo

liên kết để biết chi tiết.

Về cơ bản, chúng ta sẽ chỉnh sửa tệp xem, tạo danh sách và liệt kê các tệp trang web của chúng ta ở đó.

Sau đó, trong tệp xem máy chủ CTP, chúng tôi sẽ thêm nội dung tệp vào phần chỉ đọc trong

phần thịt, như được hiển thị ở đây, sau đó sẽ bao gồm máy chủ HTP cơ bản của chúng tôi, các chức năng bắt đầu và dừng cũng như gói

những chức năng đó để chúng ta có thể sử dụng chúng trong ứng dụng.

Tương tự như cách nó được thực hiện trong ví dụ ở đây.

Tiếp theo sẽ tạo cấu hình máy chủ 8TB mặc định, trong đó một số thành viên cấu trúc này sẽ

được khởi tạo bằng chức năng cấu hình mặc định, nhưng sẽ điều chỉnh một số thành viên này theo nhu cầu của chúng tôi,

sau đó chúng ta sẽ gọi hàm khởi động 8TB.

Mọi thứ sẽ trở nên tương tự như các ví dụ được hiển thị và trong suốt khóa học sẽ tạo cho bạn

Trình xử lý AI.

Và đây là cấu trúc bạn là người xử lý ở đây.

Và trong bài học đầu tiên, chúng ta sẽ chỉ đăng ký trình xử lý AI của bạn cho các tệp tài nguyên và chúng ta sẽ tạo

điều này theo cách rất giống, như được hiển thị ở đây.

Và điều cuối cùng tôi muốn đề cập đến là nó cũng sẽ tạo ra một tác vụ có tên là HGTV Server Monitor,

có thể gửi và nhận tin nhắn gợi ý để phản hồi các sự kiện nhất định.

Nó tương tự như những gì chúng tôi có trong ứng dụng Wi-Fi hiện nay sẽ xử lý việc liên lạc thử nghiệm giữa

ứng dụng Wi-Fi và máy chủ web theo cách này bằng cách sử dụng tín hiệu tin nhắn.

Nếu bất kỳ điều nào trong số này có vẻ khó hiểu, đừng lo lắng.

Khi chúng ta bắt đầu viết mã, nó sẽ bắt đầu có ý nghĩa hơn.

Tôi chỉ muốn cung cấp một cái nhìn tổng quan nhanh để bạn có thể tham khảo trước khi chúng ta bắt đầu sử dụng

API máy chủ HGTV.

Được rồi, chúng ta hãy bắt đầu viết mã trong phần tiếp theo.