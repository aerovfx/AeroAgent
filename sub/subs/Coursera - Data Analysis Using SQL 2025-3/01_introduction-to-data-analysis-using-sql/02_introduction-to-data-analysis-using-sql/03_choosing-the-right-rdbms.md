# 03 câu chọn-đúng-rdbms đã dịch

---

Xin chào và chào mừng trở lại. Cho đến nay, chúng ta đã đề cập đến các loại cơ sở dữ liệu khác nhau và xem xét cách cơ sở dữ liệu quan hệ lưu trữ dữ liệu.

Để quản lý cơ sở dữ liệu quan hệ, chúng ta cần có một hệ thống.

Ở cấp độ cao, một loại hệ thống quản lý cơ sở dữ liệu lưu trữ dữ liệu dưới dạng cấu trúc bảng dựa trên hàng được gọi là hệ thống quản lý cơ sở dữ liệu quan hệ hoặc viết tắt là RDBMS.

Chúng ta hãy xem xét một số hệ thống quản lý cơ sở dữ liệu quan hệ hàng đầu hiện có cùng với những ưu và nhược điểm của chúng.

Truyền hình Oracle. Tập đoàn Oracle đã phát triển và duy trì Oracle.

Phần mềm này yêu cầu kiến ​​thức sâu rộng về SQL và kinh nghiệm quản lý cơ sở dữ liệu, điều này không thân thiện với những người mới như bạn.

Nó có cả lựa chọn thay thế miễn phí và trả phí.

Một trong những lý do chính để chọn Oracle là khả năng xử lý lượng lớn dữ liệu bằng xử lý trong bộ nhớ.

Nhưng việc cấp phép đi kèm với chi phí cực kỳ cao, gần 48.000 USD mỗi đơn vị và nhu cầu về dung lượng ổ đĩa rất cao cũng như cập nhật phần cứng liên tục.

MySQL. Tiếp theo là MySQL, một trong những RDBMS được yêu thích nhất trong ngành.

Ban đầu là một giải pháp nguồn mở, Tập đoàn Oracle hiện sở hữu MySQL.

Vì được xây dựng bằng C và C++ nên MySQL tương thích với nhiều hệ điều hành khác nhau, bao gồm Windows, Linux và các hệ điều hành khác.

Hơn 50 triệu bản ghi có thể được MySQL xử lý nhờ khả năng mở rộng của nó.

Nhược điểm lớn duy nhất của MySQL là MySQL không có công cụ phát triển và gỡ lỗi tốt so với các cơ sở dữ liệu trả phí khác.

Sau đó chúng ta có PostgreSQL. Hệ thống quản lý cơ sở dữ liệu này cũng phổ biến như MySQL.

Mặc dù nó có một số tính năng ít nhiều giống với MySQL nhưng nó vẫn để lại dấu ấn.

Điều này chủ yếu là do PostgreSQL tập trung nhiều hơn vào khả năng tương thích hơn là tốc độ.

Nhược điểm của phần mềm này chủ yếu là thiếu tài liệu, không đầy đủ.

Việc thiếu các công cụ báo cáo và kiểm tra cũng gây ra nguy cơ kỹ sư cơ sở dữ liệu nhận thấy lỗi quá muộn.

Hiện có một số hệ thống quản lý cơ sở dữ liệu quan hệ có sẵn trên thị trường.

Chúng tôi sẽ không đi vào chi tiết cho từng hệ thống quản lý cơ sở dữ liệu.

Bây giờ chúng ta hãy xem số liệu thống kê thị trường nói gì về các hệ thống quản lý cơ sở dữ liệu khác nhau.

Theo cuộc khảo sát do Stack Overflow thực hiện với hơn 70.000 người tham gia, đây là kết quả về RDBMS được sử dụng nhiều nhất tính đến tháng 7 năm 2022.

Như bạn có thể thấy, MySQL rõ ràng sẽ chiếm phần của người chiến thắng về nhà.

MySQL đã đứng đầu nhiều bảng xếp hạng trong nhiều năm nay.

Nó được Facebook, Twitter, YouTube và WordPress sử dụng và đi kèm với một loạt các tính năng hữu ích.

Đây là những lý do chính tại sao chúng tôi chọn MySQL làm RDBMS mà chúng tôi sẽ sử dụng để quản lý cơ sở dữ liệu của mình.

Có một số giao diện người dùng đồ họa và ID có sẵn cho MySQL.

MySQL Workbench là một trong những IDE cung cấp chức năng thiết kế, phát triển và quản trị cơ sở dữ liệu MySQL của bạn.

MySQL Workbench là một trong những IDE cung cấp chức năng thiết kế, phát triển và quản trị cơ sở dữ liệu MySQL của bạn.

MySQL cũng tương thích với Windows, Mac và Linux.

Đây là máy khách SQL duy nhất được hỗ trợ và phát triển bởi Oracle, công ty đứng sau chính MySQL.

Vì vậy, bạn có thể chắc chắn rằng nó sẽ chứa tất cả các tính năng gần đây để phù hợp với các bản cập nhật cho máy chủ MySQL.

Vì vậy, chúng tôi đã chọn MySQL Workbench để hướng dẫn bạn cách sử dụng SQL hiệu quả để phân tích dữ liệu cho khóa học này.

Ngoài ra, hãy lưu ý rằng đối với các câu hỏi và bài tập trong video, bạn sẽ sử dụng các khối mã của Coursera do tính dễ truy cập.

Trong video tiếp theo, chúng tôi có đính kèm hướng dẫn cài đặt MySQL Workbench cho Windows, Mac và Linux.

Vì vậy, bạn còn chờ gì nữa? Hãy tiếp tục và cài đặt MySQL Workbench tùy thuộc vào hệ điều hành của bạn trước khi chúng ta bắt đầu hành trình phân tích dữ liệu bằng SQL này.