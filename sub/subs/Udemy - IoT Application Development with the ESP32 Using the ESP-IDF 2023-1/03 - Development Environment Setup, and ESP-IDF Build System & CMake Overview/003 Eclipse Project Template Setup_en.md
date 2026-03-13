# 003 Thiết lập mẫu dự án Eclipse vi

---

Được rồi, hãy bắt đầu nhật thực SPDR.

Và nhân tiện, hãy khởi chạy từ không gian làm việc mà chúng tôi đã chọn trước đó.

Bây giờ bạn có thể kết nối bộ công cụ phát triển của mình và bật nó lên, chờ cho bạn một chút thời gian để bắt đầu quay video.

Và bây giờ hãy tối đa hóa.

Và đóng tab chào mừng này và đi đến tập tin.

Mới.

Dự án IDF ấn tượng trong cái gọi là dự án, bạn, Demi, nhấn mạnh ESP 32.

Và bấm kết thúc.

Bây giờ, hãy đóng phần đọc tôi và đối với mục tiêu khởi chạy, hãy chọn ESP 32.

Và trong khi chúng ta ở đây, hãy khởi động máy tính.

Và tôi đã kết nối Typekit rover nên tôi có hai thành phần ở đây và tôi sẽ chỉ chọn cái cao hơn

số.

Nếu bạn không có bộ rover, chỉ cần chọn cổng duy nhất được hiển thị và sau đó nhấp vào hoàn tất.

Mở rộng các tệp dự án và đi vào danh sách xem tại đây.

Và đổi tên dự án thành.

Bạn, Demi, gạch dưới SPF 30 để gạch dưới.

Và đây sẽ là tên của tệp nhị phân ứng dụng do bản dựng tạo ra.

Tiếp theo, hãy mở rộng thư mục chính và đi tới phần này để xem tệp danh sách tạo.

Và chúng ta hãy thoát khỏi tất cả những điều này.

Và đăng ký thành phần IDF đã chết.

Và sau đó thêm nguồn.

Ý tôi là, cảnh đó.

Và hãy để Ed bao gồm cả con nai có gạch dưới.

Với dấu chấm giữa dấu ngoặc kép và dấu ngoặc đơn đóng.

Bây giờ chúng ta hãy chuyển sang ý nghĩa biển đó.

Và hãy dọn dẹp cái này đi.

Hãy xóa cái này đi.

Và tất cả điều này ở đây là tốt.

Và xóa cái này nữa.

Và bây giờ chúng ta có thể để nó như thế này.

Bây giờ đi đến dự án.

Và xây dựng tất cả, bạn cũng có thể sử dụng điều khiển, như được hiển thị.

Và bằng cách xây dựng dự án, chúng ta sẽ tạo ra thứ được gọi là tệp cấu hình SDK.

Cấu hình SDK chứa cấu hình dự án sẽ cần điều chỉnh dựa trên nhu cầu của dự án.

Ngoài ra, có một lỗi có thể phát sinh tùy thuộc vào phiên bản SPF của bạn cần được giải quyết.

bằng cách điều chỉnh tệp cấu hình SDK.

Vì vậy, chỉ cần đợi quá trình xây dựng hoàn tất và tôi sẽ chỉ ra vấn đề này ở đây liên quan đến chứng chỉ không hợp lệ.

Vì vậy, đây là lỗi và chúng tôi sẽ sớm giải quyết nó.

Bây giờ, hãy mở cấu hình SDK.

Và điều đầu tiên chúng ta cần làm là vào cấu hình flasher nối tiếp và thay đổi kích thước flash thành bốn

megabyte.

Tiếp theo, đi tới Bảng phân vùng.

Và thay đổi nó thành định nghĩa gốc lên tới 0,8 và đó là để cho phép cập nhật OTA.

Và sau đó chúng ta hãy đi xuống HTP Server.

Và thay đổi, yêu cầu MAX http có liên kết tới một nghìn hai mươi bốn.

Cũng như Max, chiều dài của bạn.

Tiếp theo, hãy giải quyết vấn đề chứng chỉ bằng cách vào các công cụ nhúng.

Và chọn.

Chỉ sử dụng các chứng chỉ phổ biến nhất.

Bây giờ chúng ta sẽ thực hiện các điều khiển để lưu.

Và đi xây dựng dự án.

Chỉ cần cho dự án một phút để xây dựng.

Và chúng ta có thể bỏ qua cảnh báo này ở đây.

Và nó có vẻ tốt.

Tuyệt vời.

Vì vậy, bây giờ hãy khắc phục mức thâm hụt bằng cách nhấn vào mũi tên màu xanh lá cây ở góc trên cùng bên trái.

Và bây giờ hình ảnh đang được ghi vào phần thâm hụt.

Và tất cả đều có vẻ tốt.

Vì vậy, tôi đã cập nhật bài học cấu hình dự án để thêm một bước nữa.

Sau khi bắt đầu phát triển ứng dụng này, tôi nhận thấy rằng thông tin nhật ký ESP

macro không được IEEE công nhận và những dòng nguệch ngoạc màu đỏ này xuất hiện.

Bản thân ứng dụng không bị ảnh hưởng.

Tuy nhiên, tôi muốn thoát khỏi chúng.

Vì vậy, hãy làm điều đó ngay bây giờ.

Hãy đi đến dự án.

Của cải.

Và trong C C++ chung, hãy chuyển đến bộ chỉ mục.

Và để thay đổi, các tùy chọn mặc định sẽ kiểm tra bật cài đặt cụ thể của dự án và sau đó Kiểm tra chỉ mục

tất cả đều có sự khác biệt.

Đồng thời kiểm tra nguồn chỉ mục và -- được mở trong trình chỉnh sửa.

Và thế là xong.

Vì vậy, hãy áp dụng gần gũi.

Và nếu chúng ta xây dựng.

Họ đi mất.

Tuyệt vời.

Điều đó có vẻ tốt hơn nhiều.

Được rồi, vậy tôi sẽ gặp lại bạn trong những bài học sắp tới.