# 01 chroma-db-key-khái niệm và kiến ​​trúc

---

Chào mừng bạn đến với video này, Các khái niệm và kiến ​​trúc chính của Chroma DB.

Sau khi xem video này, bạn sẽ có thể

Hiểu các tính năng và khả năng cốt lõi của Chroma DB,

Hiểu các tùy chọn triển khai khác nhau của Chroma DB,

Giải thích kiến trúc và quy trình làm việc của Chroma DB,

Và hiểu các hoạt động dữ liệu có thể được thực hiện bởi Chroma DB.

Chroma DB là cơ sở dữ liệu vectơ được thiết kế đặc biệt để hỗ trợ các tác vụ truy xuất khác nhau.

Nó cung cấp các khả năng sau.

Lưu trữ các phần nhúng và siêu dữ liệu của chúng để lưu trữ và quản lý hiệu quả các biểu diễn vectơ

của dữ liệu.

Tìm kiếm vectơ so sánh các nhúng vectơ để tìm văn bản dựa trên sự tương đồng về ngữ nghĩa bằng cách sử dụng

số liệu khoảng cách như khoảng cách cosine.

Tìm kiếm toàn văn để tìm các tài liệu liên quan dựa trên sự tương đồng về từ vựng hoặc chính tả.

Lưu trữ dữ liệu để lưu trữ toàn bộ tài liệu, không chỉ phần nhúng của chúng.

Lọc siêu dữ liệu có thể được sử dụng để thu hẹp kết quả tìm kiếm dựa trên siêu dữ liệu nhằm cải thiện

độ chính xác của quá trình truy xuất dữ liệu.

Và cuối cùng là truy xuất đa phương thức để truy xuất và quản lý dữ liệu đa phương thức như hình ảnh,

âm thanh và văn bản một cách thống nhất.

Chroma DB có thể được triển khai theo một trong hai cách.

Chroma DB thường hoạt động bằng kiến trúc máy khách-máy chủ, nơi máy khách Chroma kết nối

đến máy chủ Chroma đang chạy trong một quy trình riêng biệt.

Máy chủ có thể được khởi chạy thông qua giao diện dòng lệnh Chroma, bao gồm cả

gói Chroma lõi hoặc bằng cách sử dụng hình ảnh Docker.

Các máy khách, dù là cục bộ hay từ xa, đều kết nối với máy chủ bằng giao thức HTTP.

Đối với Python, Chroma có thể chạy ở chế độ độc lập thay vì máy khách-máy chủ thông thường

thiết lập.

Ở chế độ độc lập, cả chức năng máy chủ và máy khách đều được chạy trong một quy trình duy nhất.

Chế độ này hữu ích để kiểm tra nhanh các tính năng của Chroma hoặc khi máy chủ dự kiến

luôn chạy trên cùng một máy với máy khách.

Chúng ta hãy xem sơ qua kiến ​​trúc cơ sở dữ liệu vector của Chroma.

Kiến trúc cơ sở dữ liệu vectơ Chroma hoạt động theo nhiều giai đoạn.

Trong giai đoạn đầu tiên, là giai đoạn tùy chọn, bạn sẽ nhận được các phần nhúng.

Trong giai đoạn này, bạn sẽ chuyển đổi văn bản, hình ảnh hoặc dữ liệu thành dạng biểu diễn vector của chúng

sử dụng mô hình nhúng.

Bước này là tùy chọn vì bạn có thể giảm tải bước nhúng vào Chroma DB nếu muốn.

Trong giai đoạn tiếp theo, bạn sẽ tạo các bộ sưu tập.

Tương tự như các bảng trong cơ sở dữ liệu quan hệ, Chroma DB sử dụng các bộ sưu tập để lưu trữ tất cả

dữ liệu của nó.

Giai đoạn tiếp theo là nơi bạn lưu trữ dữ liệu trong các bộ sưu tập.

Nếu bạn đã tạo các phần nhúng bên ngoài Chroma DB, bạn sẽ phải chuyển các phần nhúng sang Chroma DB

ở bước này.

Mặt khác, nếu bạn cho phép Chroma DB xử lý việc nhúng thì Chroma DB sẽ tính toán và

lưu trữ các phần nhúng từ các tài liệu ở chế độ nền.

Tiếp theo là giai đoạn bạn thực hiện các hoạt động thu thập.

Chroma DB cho phép bạn thực hiện nhiều thao tác cơ sở dữ liệu khác nhau bao gồm xóa, cập nhật hoặc

đổi tên bộ sưu tập của bạn, cung cấp cho bạn nhiều tùy chọn hơn để sắp xếp dữ liệu của mình.

Trong giai đoạn cuối cùng, bạn truy vấn và nhóm dữ liệu để có được thông tin hữu ích nhất.

Chroma DB cho phép người dùng sử dụng truy vấn văn bản hoặc vectơ để tìm thông tin trong nhóm dựa trên ngữ nghĩa

ý nghĩa hoặc sự tương đồng về văn bản.

Hơn nữa, Chroma DB cho phép người dùng lọc tài liệu về siêu dữ liệu và nội dung tài liệu của họ.

Chroma DB hỗ trợ nhiều ứng dụng khách và tích hợp.

Các ứng dụng khách được hỗ trợ chính thức cho Chroma DB là Python và JavaScript và chúng được duy trì

bởi nhóm ChromaCore.

Ngoài ra còn có một số ứng dụng khách được cộng đồng hỗ trợ không chính thức cho Chroma DB, bao gồm Ruby, Java,

Đi, C#, Rust và PHP.

Để biết thêm thông tin về các ứng dụng khách này và các tính năng được hỗ trợ của chúng, hãy truy cập Chroma

Trang Khách hàng hệ sinh thái trong Sách dạy nấu ăn Chroma tại URL được hiển thị ở đây.

Chroma DB cũng có thể được tích hợp với các framework và công cụ phổ biến như LangChain, LlamaIndex

và OLama.

Và nó cung cấp khả năng tích hợp nguyên bản với các mô hình nhúng từ Hugging Face, Google và OpenAI.

Chúng ta hãy xem xét ở mức độ cao hơn một ví dụ về quy trình làm việc Chroma DB điển hình.

Bước đầu tiên là tạo một bộ sưu tập, bao gồm việc đặt cho nó một cái tên logic.

Bước tiếp theo là thêm các đoạn văn bản và siêu dữ liệu liên quan vào bộ sưu tập.

Khi bạn thực hiện việc này, Chroma DB sẽ tự động lưu trữ văn bản và xử lý quá trình nhúng.

Ngoài ra, nếu bạn tính toán trước các phần nhúng trước bước này, bạn sẽ cung cấp các phần nhúng đó

ở đây cùng với văn bản.

Cuối cùng, bạn truy vấn bộ sưu tập và Chroma DB trả về danh sách các kết quả tương tự nhất.

Xin nhắc lại, Chroma DB tự động xử lý việc nhúng truy vấn của bạn, do đó bạn không cần phải

nhúng văn bản truy vấn trước khi chạy truy vấn của bạn.

Theo mặc định, Chroma sử dụng khoảng cách Euclide để xác định các phần giống nhau nhất trong

một bộ sưu tập.

Nó cũng hỗ trợ khoảng cách cosine và tính toán tích số chấm.

Chúng ta hãy xem nhanh các tính năng hiệu suất của Chroma DB.

Chroma DB cung cấp khả năng tìm kiếm tương tự hiệu quả vì nó được tối ưu hóa cho kết quả gần đúng

tìm kiếm hàng xóm gần nhất, cho phép người dùng tìm thấy các vectơ tương tự một cách nhanh chóng.

Trong nội bộ, Chroma sử dụng một thuật toán nâng cao được gọi là Thế giới nhỏ có thể điều hướng theo cấp bậc

hay gọi tắt là HNSW, để tìm kiếm người hàng xóm gần nhất một cách hiệu quả theo

theo thước đo khoảng cách đã chọn.

Chroma DB cũng cung cấp các phương pháp mã hóa tốt.

Cốt lõi của Chroma DB được viết bằng Rust, cho phép cải thiện tốc độ gấp 3 đến 5 lần

trong các hoạt động truy vấn và ghi khi so sánh với lõi được viết bằng Python.

Một số trường hợp sử dụng và ứng dụng phổ biến nhất cho Chroma DB bao gồm những trường hợp sau.

Xây dựng hệ thống gợi ý cá nhân hóa dựa trên sở thích của người dùng, triển khai hiệu quả

công cụ tìm kiếm tài liệu sử dụng khả năng tìm kiếm vector hoặc toàn văn bản, truy xuất hình ảnh dựa trên

về các truy vấn văn bản sử dụng truy xuất đa phương thức và cung cấp cho chatbot khả năng tìm kiếm ngữ nghĩa

và khả năng truy xuất để tăng cường bối cảnh.

Trong video này, bạn đã học được rằng

Chroma DB là cơ sở dữ liệu vectơ mạnh mẽ được thiết kế cho nhiều tác vụ truy xuất khác nhau.

Chroma DB hỗ trợ truy xuất đa phương thức, lọc siêu dữ liệu, tìm kiếm vectơ và tìm kiếm toàn văn bản.

Việc triển khai Chroma DB có thể được thực hiện bằng kiến ​​trúc máy khách-máy chủ hoặc chế độ độc lập.

Chroma DB tích hợp với các framework phổ biến và hỗ trợ nhiều ngôn ngữ lập trình.

Chroma DB sử dụng thuật toán nâng cao để tìm kiếm lân cận gần nhất một cách hiệu quả

tìm các đoạn gần đúng nhất với một truy vấn trong một bộ sưu tập.

Và Chroma DB phù hợp với nhiều ứng dụng, bao gồm các hệ thống gợi ý,

tìm kiếm tài liệu, truy xuất hình ảnh và chatbot dựa trên AI.