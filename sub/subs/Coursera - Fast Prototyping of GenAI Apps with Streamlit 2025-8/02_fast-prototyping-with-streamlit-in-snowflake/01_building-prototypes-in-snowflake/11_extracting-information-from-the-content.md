# 11 trích xuất thông tin từ nội dung

---

Trong video trước, bạn đã tạo một bảng có nội dung thô từ các tệp docx đã tải lên của bạn.

Bây giờ là lúc để làm sạch nó.

Trong video này, bạn sẽ trích xuất những phần thông tin cụ thể từ văn bản thô đó,

những thông tin như tên sản phẩm, ngày đánh giá và bản đánh giá,

và lưu chúng vào một bảng mới có tên là Đánh giá của khách hàng.

Bạn sẽ sử dụng một chút SQL và các biểu thức chính quy để hoàn thành công việc này.

Nếu bạn không biết SQL, đừng lo lắng.

Bạn có thể yêu cầu Gen AI trợ giúp hoặc sao chép và dán mã từ kho lưu trữ GitHub của khóa học.

Hãy đi qua nó.

Đang kiểm tra kế hoạch xây dựng MVP của chúng tôi,

chúng ta có thể thấy rằng bước này sẽ kiểm tra việc phân tích dữ liệu.

Trong video này, bạn sẽ nhanh chóng chuyển từ tệp CSV khách hàng đầu vào thô

thành nội dung được phân tích cú pháp sẵn sàng để phân tích.

Bạn có thể phân tích dữ liệu này bằng Snowflake Notebook và Python hoặc SQL.

Chúng tôi sẽ hướng dẫn bạn mã SQL tại đây vì nó di chuyển nhanh hơn Python một chút.

Vì bạn đang làm việc với định dạng văn bản nhất quán trên tất cả các tệp docx,

điều đó làm cho các biểu thức chính quy trở nên đặc biệt hữu ích ở đây.

Bạn có thể xác định mẫu một lần và áp dụng mẫu đó cho mọi hàng.

Đầu tiên là tên sản phẩm.

Bạn sẽ sử dụng hàm chuỗi con biểu thức chính quy để tìm kiếm từ sản phẩm

và sau đó lấy mọi thứ sau nó cho đến ngắt dòng tiếp theo.

Điều đó chỉ cung cấp cho bạn tên sản phẩm, rõ ràng và đơn giản.

Tiếp theo là ngày đánh giá.

Ý tưởng tương tự, bạn sẽ sử dụng lại hàm chuỗi con biểu thức chính quy,

nhưng lần này bạn đang tìm kiếm một mẫu cụ thể,

một ngày ở định dạng yyyymmdd, ví dụ: 2023-10-13.

Sau đó là nội dung đánh giá.

Tại đây, bạn sẽ sử dụng một tuyên bố tình huống để kiểm tra xem nội dung có tồn tại đánh giá của khách hàng hay không.

Nếu có, bạn trích xuất văn bản theo sau nó.

Nếu không, bạn để trống.

Dễ.

Bây giờ để sáng tạo một chút, ID đơn hàng.

Mỗi tập tin có một số có ba chữ số trong tên của nó.

Vì những tập tin này là từ đợt hai,

bạn sẽ tạo một ID duy nhất bằng cách đặt số hai trước số có ba chữ số của mỗi tệp.

ID này sẽ giúp bạn kết nối các đánh giá với hồ sơ vận chuyển sau này.

Ví dụ: nếu số tệp là 045 thì ID duy nhất của bạn sẽ là 2045.

Khi bạn đã viết truy vấn SQL đầy đủ của mình,

bạn sẽ chạy nó trên bảng đánh giá thô của khách hàng

để sắp xếp dữ liệu của bạn thành các cột rõ ràng sẵn sàng để phân tích.

Và bây giờ là phần quan trọng nhất,

đã đến lúc lưu kết quả dưới dạng bảng trên Snowflake để bạn có thể sử dụng sau này.

Để làm điều này, bạn chỉ cần thêm một câu lệnh tạo bảng như thế này.

Khi bạn chạy ô này,

bạn sẽ có một phiên bản đã được làm sạch của bảng đánh giá của khách hàng mà bạn có thể sử dụng ở phần sau.

Công việc tuyệt vời.

Trong video trước, bạn đã bắt đầu với một đống tệp nén, không có cấu trúc.

Và bây giờ bạn đã có một cái sạch sẽ,

bảng có thể truy vấn được gọi là đánh giá của khách hàng sẵn sàng để phân tích.

Trong video tiếp theo, bạn sẽ chuyển đổi tập dữ liệu và bắt đầu khám phá

nhật ký vận chuyển của Avalanche để bổ sung thêm chiều sâu cho phân tích cảm tính của bạn.