# 01 một bàn để cai trị tất cả

---

Được rồi, bây giờ bạn đã tải lên, làm sạch và sắp xếp các đánh giá của khách hàng cũng như nhật ký vận chuyển,

đã đến lúc tập hợp chúng lại thành một tập dữ liệu thống nhất và hoàn tất việc chuẩn bị cho việc phân tích cảm tính.

Trong video này, bạn sẽ hoàn thành bước thứ ba trong kế hoạch xây dựng MVP của mình,

dọn dẹp dữ liệu bằng cách tập hợp các đánh giá của khách hàng Avalanche

và nhật ký vận chuyển cũng như thực hiện phân tích cú pháp cuối cùng.

Để làm điều này, bạn sẽ đi sâu vào SQL. Vì vậy, nếu SQL của bạn bị rỉ sét,

đây là thời điểm hoàn hảo để nhờ trợ lý Gen AI yêu thích của bạn trợ giúp.

Nếu bạn đã theo dõi video trước và hoàn thành video thực hành trong phòng thí nghiệm,

bạn hẳn đã có sẵn thiết lập và dữ liệu bạn cần trong video này.

Nếu không, hãy nhớ quay lại và hoàn thành các video từ một đến ba của học phần hai.

Bạn sẽ làm việc bên trong Avalanche DB, lược đồ Avalanche và giai đoạn Avalanche.

Từ đó, bạn sẽ nối hai bảng mà bạn đã tạo lại với nhau.

Đánh giá của khách hàng và nhật ký vận chuyển.

Để giúp bạn thực hiện những công việc nặng nhọc, bạn sẽ sử dụng Snowflake Cortex.

Bạn có nhớ Cortex không? Cortex là công cụ Gen AI tích hợp của Snowflake.

Hãy coi Cortex AI như một tập hợp các công cụ AI đã được tích hợp sẵn trong Snowflake.

Cortex cho phép bạn thực hiện những việc như dễ dàng tạo và chạy các truy vấn SQL,

nhanh chóng phân tích tài liệu và trích xuất văn bản, tóm tắt và phân loại nội dung,

và phân tích dữ liệu bằng các mô hình ngôn ngữ lớn, tất cả đều không cần rời khỏi Snowflake.

Bạn đã thấy Cortex hoạt động rồi.

Bây giờ bạn sẽ sử dụng nó để nối, dọn dẹp và chuẩn bị các bảng cho việc phân tích cảm tính.

Bạn sẽ viết SQL trực tiếp bên trong sổ ghi chép Snowflake,

nhưng đừng cảm thấy như bạn cần phải đưa ra các truy vấn từ đầu.

Vì các bảng đó đã được tạo từ vài video trước,

có thể hữu ích nếu yêu cầu ứng dụng Gen AI làm mới bộ nhớ của bạn

về những gì các bảng đó chứa.

Mở sổ ghi chép Snowflake và viết Snowflake SQL

để xem trước các bảng Nhật ký vận chuyển và Đánh giá của khách hàng.

Bạn có thể thực hiện việc này một cách nhanh chóng bằng cách yêu cầu ứng dụng Gen AI của bạn trợ giúp bằng lời nhắc như,

Viết Snowflake SQL để cho tôi xem bản xem trước của hai bảng

được đặt tên là Đánh giá của Khách hàng và Nhật ký Vận chuyển.

Nó có thể sẽ cung cấp cho bạn một cái gì đó như thế này.

Chạy từng mã SQL một để cập nhật

về tên cột trong mỗi bảng và các chi tiết hữu ích khác,

tương tự như những gì được hiển thị khi bạn sử dụng phương pháp mô tả Pandas.

Tiếp theo, hãy hỏi trợ lý Gen AI của bạn những câu như:

Viết Snowflake SQL để nối hai bảng, Đánh giá của khách hàng và Nhật ký vận chuyển.

Trên ID đơn đặt hàng, bao gồm văn bản đánh giá, thông tin vận chuyển, ngày, hãng vận chuyển và trạng thái.

Nó có thể sẽ cung cấp cho bạn một cái gì đó như thế này.

Nếu mọi thứ không thành công trong lần thử đầu tiên,

sao chép và dán bất kỳ thông báo lỗi nào bạn nhận được vào ứng dụng Gen AI của mình,

và nó sẽ giúp bạn khắc phục sự cố.

Sau khi các bảng của bạn được hợp nhất,

kiểm tra kết quả bằng cách xem 10 dòng đầu tiên của khung dữ liệu được hợp nhất

bằng một câu lệnh SQL SELECT nhanh chóng.

Chọn tất cả từ giới hạn đánh giá hợp nhất đến 10.

Xin chúc mừng, bây giờ các bảng của bạn đã được nối

và mọi đánh giá của khách hàng đều có thông tin vận chuyển trong cùng một hàng.

Trước khi phân tích tình cảm,

bạn nên dọn dẹp và tóm tắt các đánh giá của khách hàng.

Bạn có thể thắc mắc tại sao bạn cần dành thời gian để làm rõ các đánh giá của khách hàng

khi bạn định đưa nó vào mô hình AI để phân tích tình cảm.

Đúng là các mô hình Gen AI thực hiện tốt công việc xử lý bất kỳ dữ liệu nào bạn cung cấp cho chúng,

nhưng chất lượng kết quả của bạn vẫn phụ thuộc vào chất lượng dữ liệu đầu vào của bạn.

Ví dụ: các hàng trống không cung cấp thông tin hữu ích cho việc phân tích.

Định dạng không nhất quán có thể khiến việc đạt được kết quả nhất quán trở nên khó khăn hơn

khi bạn đang thực hiện phân tích văn bản hoặc tìm kiếm các mẫu.

Vì vậy, khi bạn làm sạch dữ liệu của mình trước tiên,

bạn đang chuẩn bị cho mình những kết quả tốt hơn và một quy trình hiệu quả hơn.

Quay lại Sổ tay Bông tuyết của bạn,

đã đến lúc dọn dẹp văn bản đánh giá của bạn bằng cách chuyển đổi nó thành chữ thường.

Điều này sẽ giúp việc tìm kiếm và đối sánh văn bản sau này trong phân tích của bạn trở nên dễ dàng hơn.

Bắt đầu bằng cách chuyển đổi bảng đánh giá đã hợp nhất của bạn thành khung dữ liệu Snowpark.

Sau đó áp dụng hàm dưới của Snowpark để chuẩn hóa cột văn bản đánh giá

để tất cả văn bản xuất hiện ở định dạng chữ thường.

Tiếp theo, sử dụng tính năng cắt bớt để loại bỏ mọi khoảng trống thừa

điều đó có thể xuất hiện ở đầu hoặc cuối bài đánh giá.

Đây là một bước quan trọng vì bạn không muốn sản phẩm tuyệt vời

và sản phẩm tuyệt vời được viết hoa ở tất cả các chữ cái được coi là các đánh giá khác nhau

chỉ vì sự khác biệt về cách viết hoa.

Việc chuẩn hóa văn bản đánh giá bây giờ có nghĩa là

phân tích của bạn sẽ chính xác và nhất quán hơn.

Bây giờ là lúc để lưu công việc của bạn.

Dòng mã này tạo một bảng mới trong Snowflake có tên là

Các bài đánh giá đã được làm sạch để lưu trữ các bài đánh giá của khách hàng đã được làm sạch của bạn.

Đối số ghi đè chế độ có nghĩa là nếu có bất kỳ bảng nào khác có cùng tên,

Python sẽ ghi đè lên nó để tránh trùng lặp tên bảng.

Hãy cẩn thận với điều này để không vô tình viết lên bảng mà bạn định giữ lại.

Được rồi, hãy chạy khối này và bây giờ bạn đã có một bộ dữ liệu rõ ràng

đã sẵn sàng cho bất kỳ phân tích nào bạn muốn thực hiện.

Làm tốt lắm.

Giờ đây, dữ liệu của bạn đã sạch sẽ và có tổ chức, bạn đã sẵn sàng cho những điều thú vị.

Bước tiếp theo là sử dụng GenAI để cung cấp hỗ trợ mã hóa cho bạn

mà bạn sẽ sử dụng trong nền tảng Snowflake.