# 10 từ-giai đoạn-đến-bàn-với-vỏ não

---

Xin chào và chào mừng trở lại.

Trong video trước, bạn đã tải lên hơn 100 đánh giá của khách hàng

tài liệu từ vào giai đoạn Bông tuyết của bạn.

Bây giờ bạn sẽ biến đống tài liệu lớn đó thành một

bảng có cấu trúc không sử dụng gì ngoài Python

ngay tại đây trong cuốn sổ tay Snowflake của bạn.

Hãy bắt đầu.

Hiện tại, bạn đang chuyển từ bước một trong kế hoạch xây dựng MVP của mình

nhập dữ liệu vào bước hai, phân tích cú pháp và cấu trúc.

Vì vậy, trong video này, bạn sẽ sử dụng tài liệu phân tích cú pháp

để trích xuất nội dung từ mỗi tài liệu từ theo giai đoạn của bạn.

Tự động tạo bảng với tên file và trích xuất văn bản.

Sau đó xem trước kết quả trong sổ ghi chép Bông tuyết của bạn

để đảm bảo mọi thứ đều hoạt động.

Tất cả những điều này sẽ xảy ra bên trong cuốn sổ tay Snowflake

sử dụng Avalanche DB, lược đồ Avalanche

và giai đoạn Avalanche mà bạn đã tạo trước đó.

Trước khi bắt đầu, hãy xem lại nhanh lý do chúng ta sử dụng Cortex.

Snowflake Cortex là một bộ công cụ JDI tích hợp

cho phép bạn xử lý và phân tích dữ liệu bằng SQL đơn giản.

Không cần thiết lập.

Nó bao gồm các chức năng như phân tích tài liệu,

mà bạn sẽ sử dụng trong video này

có thể trích xuất nội dung từ tài liệu, tệp PDF và văn bản.

Điều này có nghĩa là bạn không cần sử dụng Python

hoặc các thư viện bên ngoài để trích xuất văn bản.

Cortex xử lý tất cả cho bạn.

Nó nhanh chóng, an toàn và ngay bên trong Snowflake.

Hãy bắt đầu bằng cách xác minh rằng các tệp của bạn đang ở trạng thái ổn định.

Trong một ô SQL mới trong sổ ghi chép của bạn,

chạy dòng này, liệt kê giai đoạn Avalanche.

Bạn sẽ thấy danh sách các tệp docx,

một cho mỗi đánh giá của khách hàng.

Nếu bạn thấy 101 tệp thay vì 100,

đó có thể là do customerreviews.csv

vẫn ngồi đó từ lúc trước.

Hoàn toàn ổn, chúng tôi sẽ lọc nó ra.

Như mọi khi, bạn có thể hỏi ứng dụng JNI yêu thích của mình

để giúp bạn tạo SQL.

Hãy thử viết SQL bằng Snowflake Cortex

để trích xuất văn bản từ tất cả các tệp docx trong giai đoạn Avalanche

và lưu nó vào một bảng có tên là đánh giá thô của khách hàng.

Nó có thể sẽ cung cấp cho bạn một cái gì đó gần như thế này.

Đây là những gì nó đang làm.

Giai đoạn thư mục Avalanche cung cấp cho bạn siêu dữ liệu

về mọi tập tin trong giai đoạn của bạn.

Đường dẫn tương đối chỉ là tên tệp

như review43.docs.

Hàm phân tích tài liệu lấy tên sân khấu và tên tệp

sau đó trích xuất văn bản từ tài liệu.

Kết quả được lưu trữ trong một bảng dưới dạng hai cột,

tên file và nội dung được trích xuất

dưới dạng đối tượng JSON bán cấu trúc.

Chạy mã này bên trong ô SQL của sổ ghi chép Snowflake.

Sau khi hoàn tất, hãy đảm bảo mọi thứ đều hoạt động

bằng cách chạy như sau.

Điều này sẽ hiển thị một vài dòng đầu tiên của mỗi tài liệu

để bạn có thể tỉnh táo kiểm tra xem phân tích cú pháp có hoạt động như mong đợi hay không.

Nếu bạn thấy kết quả ở đây, thật tuyệt vời.

Điều đó có nghĩa là 100 tài liệu Word của bạn hiện đã được sắp xếp gọn gàng

và sẵn sàng dọn dẹp.

Làm tốt lắm.

Bạn vừa làm được điều gì đó khá tiên tiến.

Đó là xử lý hơn 800 tài liệu Word

trực tiếp bên trong Bông tuyết

không sử dụng gì ngoài SQL và Cortex.

Bạn đã bắt đầu với một đống lớn các tệp nén không có cấu trúc

và bây giờ bạn đã có một bảng có thể truy vấn rõ ràng

được gọi là đánh giá thô của khách hàng đã sẵn sàng để phân tích.

Trong video tiếp theo,

bạn sẽ chuyển số và đi sâu vào tập dữ liệu mới

để tăng thêm chiều sâu cho phân tích tình cảm của bạn

với nhật ký vận chuyển của Avalanche.