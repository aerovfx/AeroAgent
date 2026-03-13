# 02 giới thiệu-bông tuyết

---

Trong video này, bạn sẽ thấy bản demo về cách ứng dụng Streamlit chạy trực tiếp bên trong Snowflake,

cho phép bạn tạo nguyên mẫu nhanh hơn mà không phải lo lắng về việc thiết lập bất cứ điều gì.

Nhưng lý do lớn nhất để sử dụng Streamlit trong Snowflake là gì?

Ứng dụng của bạn có thể được kết nối trực tiếp với dữ liệu,

và Snowflake hỗ trợ Pandas và các công cụ Python quen thuộc khác,

vì vậy nó phù hợp ngay với quy trình làm việc của bạn.

Điều này có nghĩa là không cần phải di chuyển tệp xung quanh hoặc chuyển đổi giữa các công cụ bên ngoài,

và ứng dụng của bạn sẽ có tốc độ tốt hơn, độ trễ thấp hơn và tính năng bảo mật tích hợp.

Nó cũng làm cho việc triển khai thực sự dễ dàng,

chỉ cần một vài cú nhấp chuột và ứng dụng của bạn sẽ xuất hiện trên nền tảng Snowflake.

Hãy bắt đầu bằng cách xem ứng dụng Streamlit của bạn sẽ hoạt động như thế nào bên trong Snowflake,

và sau đó bạn sẽ làm quen với môi trường làm việc Snowflake mới của mình.

Là sinh viên của khóa học này,

bạn có 120 ngày truy cập miễn phí vào nền tảng Snowflake đầy đủ.

Để theo dõi phần còn lại của video, hãy đăng ký tại đây.

Đây là phiên bản hơi lạ hơn của bảng điều khiển Avalanche

mà bạn đã xây dựng trong Mô-đun 1.

Nguyên mẫu bạn đang xem hiện đã được triển khai nội bộ trên Snowflake,

để nó có thể được chia sẻ một cách an toàn với bất kỳ đồng nghiệp nào của bạn

có quyền truy cập vào các bảng cơ bản và liên kết đến ứng dụng.

Khi bạn ở trang đăng ký Snowflake, hãy điền vào mẫu đăng ký,

sau đó chọn lý do đăng ký từ menu thả xuống.

Việc bạn chọn gì ở đây không quan trọng,

việc bạn chọn gì ở đây không quan trọng,

chỉ cần chọn một tùy chọn và sau đó nhấp vào tiếp tục.

Trên trang thứ hai của mẫu đăng ký, nhập tên công ty và chức danh công việc.

Bạn có thể bịa ra chuyện này nếu muốn, tùy bạn.

Tìm menu thả xuống có nhãn chọn phiên bản Bông tuyết của riêng bạn.

Để nó ở Enterprise sẽ cung cấp cho bạn tất cả các tùy chọn bạn cần cho khóa học này.

Tiếp theo, chọn khu vực gần bạn nhất.

Ví dụ mình ở West Coast nên mình sẽ chọn US West.

Đọc qua các điều khoản, sau đó nhấp vào dấu kiểm ở cuối màn hình

nếu bạn đồng ý với họ.

Bây giờ, hãy nhấp vào bắt đầu và chúng ta bắt đầu.

Trong khi tài khoản của bạn đang được thiết lập, đằng sau hậu trường,

bạn sẽ thấy thêm một vài hộp kiểm tùy chọn

điều đó sẽ tinh chỉnh một số tùy chọn tài khoản của bạn.

Tối thiểu, hãy chọn Python làm ngôn ngữ bạn chọn,

sau đó điền vào hoặc bỏ qua phần còn lại.

Tiếp theo, hãy kiểm tra hộp thư đến email của bạn để tìm email xác minh.

Khi bạn nhận được email từ Snowflake,

nhấp vào liên kết xác minh trong email,

và bạn sẽ có thể đăng nhập và truy cập vào nền tảng này.

Bây giờ tài khoản của bạn đã được thiết lập, chào mừng bạn đến với sân chơi mới.

Được rồi, khi bạn đã đăng nhập vào Snowflake,

bạn sẽ thấy từ home ở đâu đó gần đầu màn hình.

Đây là không gian làm việc chính của bạn có tên là Snow Sites,

giống như một nhiệm vụ kiểm soát dữ liệu của bạn.

Hãy nhanh chóng lưu ý, Snowflake không ngừng phát triển,

vì vậy mọi thứ trên màn hình của bạn có thể trông hơi khác so với những gì bạn thấy ở đây.

Đừng lo lắng, dòng chảy tổng thể sẽ có ý nghĩa

và bạn sẽ có thể làm theo tốt.

Nếu bạn có bao giờ gặp khó khăn,

Các tài liệu và hướng dẫn chính thức của Snowflake cực kỳ chi tiết và rất hữu ích.

Ngay bây giờ, bạn có thể nhận được một cửa sổ bật lên cung cấp chuyến tham quan nhanh về tập dữ liệu mẫu.

Hoàn toàn tùy thuộc vào bạn.

Hãy tham quan nếu bạn tò mò.

Nếu bạn muốn lao thẳng vào,

hãy tiếp tục và nhấn bỏ qua ngay bây giờ.

Xuống phía dưới bên phải,

có một số cách khác nhau để tương tác với Snowflake,

tùy vào phong cách làm việc của bạn.

Trang web tuyết là trang web chính.

Đó là giao diện web mà bạn sẽ sống trong đó.

Nó nhanh, sạch và siêu trực quan.

Nếu bạn là người hâm mộ thiết bị đầu cuối,

có cả giao diện dòng lệnh nữa.

Và nếu bạn đang ở chế độ phát triển,

Snowflake thậm chí còn có tiện ích mở rộng VS Code,

để bạn có thể ở ngay trong vùng mã hóa của mình.

Vì khóa học này chạy trong trình duyệt của bạn,

Snow Site sẽ là căn cứ của bạn.

Bây giờ là phần thú vị.

Bạn đã biết Streamlit rất tốt để tạo các ứng dụng web,

và bây giờ Snowflake cho phép bạn chạy các ứng dụng Streamlit trực tiếp bên trong kho dữ liệu của mình.

Không cần thiết lập thêm,

không có API tung hứng hoặc di chuyển tệp xung quanh.

Chỉ cần xây dựng với Streamlit trên Snowflake.

Bạn có thể tạo bảng thông tin trực tiếp từ bảng Snowflake

thay vì phải làm công việc chuẩn bị mọi lúc.

Khám phá và trực quan hóa dữ liệu của bạn trong thời gian thực

để đảm bảo người dùng của bạn sẽ luôn có kết quả chính xác và cập nhật nhất.

Giữ toàn bộ quy trình làm việc của bạn,

tất cả mã, dữ liệu, logic và giao diện người dùng ở cùng một nơi.

Có hai cách chính để làm điều này.

Sổ tay bông tuyết,

rất phù hợp để tạo mẫu nhanh và làm việc với đồng đội.

Ứng dụng Streamlit và Snowflake,

điều này hoàn hảo khi bạn sẵn sàng chia sẻ ứng dụng của mình một cách rộng rãi hơn.

Hầu hết mọi người đều bắt đầu trong Notebook

và sau đó chuyển sang ứng dụng Streamlit và Snowflake khi nguyên mẫu của chúng đã ổn định.

Bạn sẽ sử dụng cả hai,

Sổ ghi chép Snowflake và ứng dụng Streamlit và Snowflake trong khóa học này.

Vì vậy, hãy kết nối điều này với những gì bạn đã xây dựng.

Quay lại Mô-đun 1,

bạn đã tạo một nguyên mẫu Streamlit đang hoạt động

để phân tích đánh giá sản phẩm trong tập dữ liệu Avalanche.

Bây giờ trong Mô-đun 2,

bạn sẽ tăng cường nguyên mẫu của mình bằng Bông tuyết

bằng cách kết nối ứng dụng của bạn với các bảng Snowflake bên trong nền tảng

và thêm bộ lọc, tiện ích tương tác và hình ảnh trực quan.

Tiếp theo, đã đến lúc tìm hiểu môi trường phát triển Snowflake

để bạn có thể học theo cách của mình.