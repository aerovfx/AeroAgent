# 05 thiết lập-a-rag-pipeline-sử dụng vỏ não-tìm kiếm

---

Trong video trước, bạn đã tìm hiểu cách RAG có thể cải thiện việc truy xuất thông tin.

Video này sẽ hướng dẫn bạn cách áp dụng điều đó vào thực tế.

Đã đến lúc hoàn thành phần cuối cùng của nguyên mẫu của bạn.

Đi thôi!

Cortex Search là dịch vụ tìm kiếm được quản lý của Snowflake dành cho các ứng dụng AI.

Nó tự động tạo các chỉ mục và phần nhúng từ dữ liệu của bạn,

sau đó cung cấp các API đơn giản để bạn có thể xây dựng các ứng dụng RAG hoặc Thế hệ tăng cường truy xuất

mà không cần tự mình quản lý cơ sở hạ tầng phức tạp.

Mở một sổ ghi chép mới trong Snowflake.

Nếu bạn muốn viết mã hoặc tìm mã trong kho GitHub tại đường dẫn tệp hiển thị trên màn hình.

Bắt đầu bằng cách xem trước nội dung của bảng đánh giá được phân tích cú pháp

để kiểm tra cấu trúc và nội dung dữ liệu hiện có trước khi tiến hành các thao tác mới.

Bây giờ, bạn sẽ tạo một bảng mới có tên

phân đoạn nội dung bằng cách sử dụng câu lệnh tạo hoặc thay thế bảng.

Sau khi tạo bảng, hãy sử dụng câu lệnh chèn cùng với snow.cortex.splittext

ký tự đệ quy, là một chức năng phân tích văn bản mạnh mẽ

chia văn bản đánh giá của khách hàng thành nhiều phần để xử lý dễ dàng hơn.

Và thế là xong!

Dữ liệu của bạn bây giờ đã được chia nhỏ và tải vào nội dung được chia nhỏ.

Hãy xem nhanh bảng mới bằng cách chọn một vài hàng đầu tiên

để đảm bảo rằng quy trình chunking đã được triển khai chính xác

và dữ liệu hiện đã được chuẩn bị cho phân tích tiếp theo.

Bây giờ, đã đến lúc thiết lập Dịch vụ tìm kiếm Avalanche bằng cách sử dụng dịch vụ tạo hoặc thay thế tìm kiếm vỏ não.

Thêm khối mã này.

Khối mã này tạo ra một công cụ tìm kiếm hoạt động trên dữ liệu được chia nhỏ của bạn,

để bạn có thể nhanh chóng truy vấn thông tin cụ thể, chẳng hạn như đánh giá sản phẩm có trong văn bản.

Bây giờ là phần thú vị nhất, hãy kiểm tra tìm kiếm của bạn.

Chạy truy vấn SQL trên bảng nội dung chunked

để tìm nội dung cụ thể như tất cả các bài đánh giá về kính bảo hộ.

Một cái gì đó như thế này.

Bạn có thể thực hiện việc này bằng cách chuyển cụm từ tìm kiếm của mình tới chức năng xem trước tìm kiếm

và nhận được kết quả phù hợp.

Như thế này.

Phần tốt nhất?

Bạn cũng có thể sử dụng Python.

Đây là mã bạn cần để tìm kiếm các bài đánh giá về kính bảo hộ bằng công cụ tìm kiếm mới xây dựng của bạn.

Như mọi khi, bạn cần thiết lập phần bông tuyết và bạn có thể viết một lời nhắc đơn giản.

Sau đó, bạn cần tạo dịch vụ truy vấn và bạn có thể tìm kiếm nó bằng cách sử dụng lời nhắc của mình

và chỉ định cột nào cần tìm kiếm.

Bạn có thể định dạng nó dưới dạng JSON và trích xuất thông tin từ nó.

Sau đó, chỉ cần hiển thị nó trong ứng dụng Streamlit của bạn.