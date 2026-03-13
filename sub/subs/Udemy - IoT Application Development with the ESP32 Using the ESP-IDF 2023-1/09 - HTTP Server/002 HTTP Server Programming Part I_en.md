# 002 Lập trình máy chủ HTTP Phần I vi

---

OK, điều đầu tiên chúng ta sẽ làm là tạo một thư mục mới trên main.

Và gọi nó là trang Web.

ĐƯỢC RỒI.

Và Hugh sẽ bao gồm các tệp trang Web của chúng tôi, vì vậy hãy chuẩn bị sẵn các tệp trang Web được cung cấp từ

tài nguyên cho phần này để chúng tôi có thể đưa chúng vào thư mục này.

Và tôi có cái của tôi ở đây, nên tôi sẽ lấy tất cả những tập tin này rồi sao chép chúng vào trang web

thư mục như vậy.

Và ở đây chỉ cần chọn sao chép file.

ĐƯỢC RỒI.

Vì vậy, bây giờ hãy mở các tệp mà chúng ta sẽ phát triển thêm trong suốt khóa học.

Đầu tiên, hãy truy cập APT, thành công và nhấp chuột phải và mở bằng.

Và sau đó chọn khác.

Và tôi sẽ chỉ chọn trình soạn thảo C C++, nhưng nếu bạn có thứ gì đó tốt hơn như VSCO, thì

bằng mọi cách hãy sử dụng nó thay thế.

ĐƯỢC RỒI.

Và bây giờ hãy chọn tệp giám khảo và hiển thị lại các biên tập viên nội bộ.

Và một lần nữa, tôi sẽ chọn trình soạn thảo C C++.

Sau đó mở tài liệu HTML nghiên cứu chỉ mục theo cách tương tự.

Và tôi sẽ chọn cùng một biên tập viên.

Và đây là mẫu sẽ được mở rộng trong suốt khóa học.

Ở đây chúng tôi có ứng dụng của mình, tệp CSIS được chỉ định làm biểu định kiểu, một ứng dụng mà tệp JS ở đây và chúng tôi

có truy vấn J ở đây làm thư viện JavaScript của chúng tôi.

Và nếu chúng ta tới chỗ D.J.s.

Ở đó chúng tôi đã có sẵn các chức năng sẽ xử lý việc cập nhật chương trình cơ sở ở phía trang web.

Vì vậy, hãy thoải mái xem xét điều này và hiểu cơ bản về nó, rồi chúng ta sẽ thêm khá nhiều mã

đến nó sau này.

Ngoài ra, có một biểu định kiểu rất cơ bản ở đây và cũng có một số kiểu dáng nút ở đây

cũng như một số màu sắc và phông chữ.

Bạn luôn có thể tùy chỉnh điều này sao cho phù hợp với nhu cầu của bạn.

Được rồi, vậy chúng ta hãy đi tới để xem tập tin tạo danh sách.

Và ở đây chúng ta sẽ nói đến các tập tin nhúng.

Bởi vì chúng ta cần nhúng các tập tin trang Web.

Vậy là chúng ta sẽ nói đường dẫn trang web gạch chéo ứng dụng, đó là thành công.

Và sau đó trang web gạch chéo thích hợp, James.

Và trang web gạch chéo favicon, Iko.

Và sau đó là trang Web.

Lập chỉ mục HTML đó và sau đó gạch chéo trang web Lesli.

Và sau đó hãy sao chép truy vấn J.

Và dán vào đây và sau đó chúng ta có thể lưu nó.

Được rồi, bây giờ chúng ta hãy chuyển sang thư mục chính và sau đó là tệp nguồn mới.

Và gọi nó là máy chủ HTP nào thấy.

Được rồi.

Và bây giờ tạo một -- file mới.

Và gọi nó là HTP Server Dot H.

Được rồi, trước tiên, hãy quay lại để xem danh sách tạo và thêm tệp nguồn máy chủ HTP.

Và lưu nó.

Vì vậy bây giờ chúng ta hãy đi đến nhiệm vụ chung.

Và ở đây chúng ta sẽ xác định thông tin tác vụ của máy chủ HTP.

Vì vậy bây giờ hãy xác định máy chủ HTP.

Kích thước ngăn xếp nhiệm vụ.

Như tám nghìn một trăm chín mươi hai vết cắn.

Và sau đó để tìm thấy.

Ưu tiên nhiệm vụ của máy chủ HTTP.

Và chúng ta sẽ xác định nó là dành cho.

Đây chỉ là một mức độ ưu tiên trong bàn ứng dụng Wi-Fi.

Ngay tại đây chúng ta có thể xác định nhiệm vụ của máy chủ HGTV.

Viện trợ cốt lõi.

Và chúng ta cũng sẽ biến nó thành con số 0.

Vì vậy, bây giờ chúng ta có thể xác định máy chủ HGTV, theo dõi thông tin tác vụ.

Và đầu tiên sẽ xác định.

Màn hình máy chủ HGTV.

Kích thước ngăn xếp.

Như bốn nghìn chín mươi sáu byte.

Và sau đó là màn hình máy chủ HTP.

Sự ưu tiên.

Chúng ta sẽ nói ba.

Và sau đó chúng ta hãy làm điều đó.

Màn hình máy chủ HGTV được mang theo.

Và điều này chúng ta có thể để lại ở mức 0.

OK, vậy hãy quan tâm đến thông tin nhiệm vụ của chúng ta.

Vì vậy, bây giờ chúng ta hãy đi tới phần đầu của tập tin và anh ta sẽ tạo các thông báo cho màn hình HTP.

Và hãy typedef enum.

Tin nhắn máy chủ HTP.

Và cái đầu tiên sẽ là Tin nhắn 8TB, kết nối wi fi và nó.

Và rõ ràng sẽ đặt nó về 0.

OK, sau đó có thông báo 8TB, kết nối wi fi thành công.

Và sau đó chúng ta cũng sẽ có thông báo tại sao nếu tôi kết nối thì lại thất bại.

Và sau đó cũng có tin nhắn HTP cập nhật OTA thành công.

Và sau đó cập nhật OTA tin nhắn HTP không thành công.

Và cũng đã khởi tạo bản cập nhật OTA tin nhắn HTP.

Được rồi.

Vì vậy hãy đặt tên nó là tin nhắn máy chủ HGTV.

Gạch dưới E cho Enum, do đó đây là những thông báo mà trình giám sát máy chủ HTP sẽ xử lý lúc này.

Màn hình thực sự không làm được điều gì phức tạp.

Tôi vừa có ý tưởng đưa nó vào để phản ứng với các sự kiện và cập nhật các biến toàn cục trong màn hình

chỉ để việc theo dõi những gì đang diễn ra trong máy chủ HTP trở nên dễ dàng hơn, như bạn sẽ thấy sau, và bạn

có thể dễ dàng sửa đổi điều này như bạn muốn.

Được rồi, bây giờ hãy tạo cấu trúc cho hàng đợi tin nhắn.

Và ở đây sẽ báo typedef bị đánh.

Và gắn thẻ nó dưới dạng tin nhắn Q của máy chủ.

Và ở đây chúng ta sẽ chỉ bao gồm phần bên trong.

Và gọi nó là tin nhắn I.D..

Sau đó, hãy gọi thông báo Q của máy chủ HTP này gạch dưới T.

Và đừng quên dấu chấm phẩy ở đây.

Và tương tự như tin nhắn của người vợ qua ABC, đây là điều mà bạn có thể dễ dàng mở rộng dựa trên

về nhu cầu của bạn.

Được rồi, bây giờ chúng ta hãy xuống đây và tạo một nguyên mẫu cho hàm gửi thông báo đến khối.

Và tham số đầu tiên là ID tin nhắn.

Từ tin nhắn máy chủ HTP trong.

Và sự trở lại là đúng.

Nếu một mục đã được gửi thành công vào hàng đợi.

Ngược lại, PD sai.

Và tôi sẽ để lại ghi chú ở đây để bạn mở rộng danh sách tham số dựa trên yêu cầu của bạn.

Ví dụ: cách bạn đã mở rộng cấu trúc thông báo khối máy chủ HTP.

Được rồi, bạn chỉ cần mở rộng cấu trúc và hàm theo cách bạn muốn.

Bây giờ, giả sử loại cơ sở được gạch dưới T.

Giám sát máy chủ HTTP.

Gửi tin nhắn.

Và sau đó chúng ta hãy nắm lấy phần bên trong.

Và thả nó ở đây.

Và chúng ta sẽ tạo một nguyên mẫu khác để khởi động máy chủ HTTP.

Và nói máy chủ HGTV void khởi động.

Và nó trống rỗng.

Được rồi, bây giờ hãy tạo một nguyên mẫu khác để dừng máy chủ HGTV.

Và nó vô hiệu hóa việc dừng máy chủ HGTV.

Và vô hiệu.

Vì vậy, bây giờ đó là nó.

Và trong phần tiếp theo chúng ta sẽ gọi tới file nợ máy chủ HP.