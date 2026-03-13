# Chương 8. Tiền xử lý và Học tập tăng cường sâu trong mạng Q-network, Phiên bản video được dịch

---

Phần 8.4, tiền xử lý và mạng Q.

Trạng thái RAW là khung video RGB có kích thước 240, 256, 3,

có chiều cao không cần thiết và sẽ tốn kém về mặt tính toán mà không

lợi thế. Chúng tôi sẽ chuyển đổi các trạng thái RGB này thành thang độ xám và thay đổi kích thước chúng thành

42 x 42 để cho phép mô hình của chúng tôi đào tạo nhanh hơn nhiều.

Liệt kê 8.2, giảm trạng thái mẫu và chuyển sang thang độ xám.

Hàm OBS gạch dưới tỷ lệ thấp chấp nhận mảng trạng thái, OBS, một bộ dữ liệu

cho biết kích thước mới về chiều cao và chiều rộng, đồng thời cho biết có nên chuyển đổi hay không

sang thang độ xám hay không. Chúng tôi đặt nó thành true theo mặc định vì đó là điều chúng tôi muốn.

Chúng tôi sử dụng chức năng thay đổi kích thước Thư viện hình ảnh Scikit, vì vậy bạn có thể cần phải cài đặt nó nếu

bạn chưa có nó rồi. Truy cập trang tải xuống tại scikit-image.org.

Đây là một thư viện rất hữu ích để làm việc với dữ liệu hình ảnh ở dạng

mảng đa chiều. Bạn có thể sử dụng Matplotlib để trực quan hóa khung trạng thái.

Xem mã này. Hình ảnh được lấy mẫu xuống sẽ trông khá mờ nhưng vẫn

chứa đủ thông tin trực quan để chơi trò chơi. Chúng ta cần xây dựng một số

các chức năng xử lý dữ liệu khác để chuyển đổi các trạng thái RAW này thành trạng thái hữu ích

hình thức. Chúng tôi sẽ không chỉ chuyển một khung hình 42 x 42 cho các mô hình của mình. chúng tôi sẽ

thay vào đó vượt qua ba khung hình cuối cùng của trò chơi, về bản chất là thêm một kênh

chiều kích. Vì vậy, các trạng thái sẽ là một tensor 3 x 42 x 42, hình 8.11.

Việc sử dụng ba khung cuối cùng cho phép mô hình của chúng tôi truy cập vào thông tin vận tốc.

Đó là, các vật thể đang chuyển động nhanh như thế nào và theo hướng nào, thay vì chỉ

thông tin vị trí. Hình 8.11. Mỗi trạng thái được cấp cho đại lý là một

sự kết hợp của ba khung màu xám gần đây nhất trong trò chơi. Đây là

cần thiết để mô hình có thể truy cập không chỉ vị trí của các đối tượng,

mà còn cả hướng chuyển động của chúng. Khi trò chơi bắt đầu lần đầu tiên, chúng ta chỉ có

truy cập vào khung đầu tiên, vì vậy chúng tôi chuẩn bị trạng thái ban đầu bằng cách ghép nối

cùng một trạng thái ba lần để có được trạng thái ban đầu là 3 x 42 x 42. Sau này

trạng thái ban đầu, chúng ta có thể thay thế khung hình cuối cùng ở trạng thái bằng khung hình gần đây nhất

frame từ môi trường, thay thế khung thứ hai bằng khung cũ cuối cùng,

và thay thế khung hình đầu tiên bằng khung hình thứ hai cũ. Về cơ bản, chúng tôi đã cố định

độ dài cấu trúc dữ liệu vào trước ra trước nơi chúng tôi thêm vào bên phải và

trái tự động bật ra. Python có cấu trúc dữ liệu tích hợp được gọi là

deck, trong thư viện bộ sưu tập, có thể thực hiện hành vi này khi

Thuộc tính maxlin được đặt thành 3. Chúng tôi sẽ sử dụng ba hàm để chuẩn bị

trạng thái thô ở dạng mà mô hình tác nhân và bộ mã hóa của chúng tôi sẽ sử dụng. sự chuẩn bị

hàm trạng thái gạch dưới sẽ thay đổi kích thước hình ảnh, chuyển sang thang độ xám, chuyển đổi từ

numpy vào tensor PyTorch và thêm thứ nguyên lô bằng phương pháp unsquease

với tham số dim được chỉ định. Chuẩn bị gạch dưới nhiều dấu gạch dưới

hàm trạng thái có một tensor kích thước, theo từng kênh theo chiều cao theo chiều rộng,

và cập nhật kích thước kênh bằng các khung mới. Chức năng này sẽ chỉ

được sử dụng trong quá trình thử nghiệm mô hình được đào tạo. Trong quá trình đào tạo, chúng tôi sẽ sử dụng

cấu trúc dữ liệu boong để liên tục nối và bật các khung. Cuối cùng là việc chuẩn bị

hàm gạch dưới trạng thái gạch dưới ban đầu chuẩn bị trạng thái khi chúng ta lần đầu tiên

bắt đầu trò chơi và không có lịch sử của hai khung hình trước đó. Chức năng này sẽ

sao chép một khung hình ba lần để tạo một khung ba lần theo chiều cao và chiều rộng

tensor. Liệt kê 8.3, chuẩn bị các trạng thái.