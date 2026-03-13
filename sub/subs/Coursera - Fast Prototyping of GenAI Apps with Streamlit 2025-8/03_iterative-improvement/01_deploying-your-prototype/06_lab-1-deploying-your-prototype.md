# 06 lab-1-triển khai-nguyên mẫu của bạn

---

Trong phòng thí nghiệm này, bạn sẽ kết hợp mọi thứ bạn đã học,

Prom Engineering, Kết nối dữ liệu, Giao diện người dùng và GenAI để triển khai ứng dụng của bạn,

cả nội bộ, trong Snowflake và công khai trên Streamlit Community Cloud.

Bạn cũng sẽ học cách theo dõi số liệu thống kê, kiểm soát quyền truy cập,

và sử dụng các công cụ GenAI để cộng tác tốt hơn.

Bây giờ là lúc triển khai nguyên mẫu Avalanche hoàn chỉnh của bạn một cách an toàn bên trong Snowflake.

Mở Snowflake và đi tới phần Projects, sau đó là phần Streamlit.

Nhấp vào nút ứng dụng Streamlit màu xanh lam ở trên cùng bên phải.

Đặt tên cho ứng dụng của bạn giống như nguyên mẫu Avalanche.

Chọn lược đồ Avalanche DB và Avalanche của bạn.

Nhấp vào Tạo.

Trong trình chỉnh sửa, xóa mã Hello World mặc định,

sau đó sao chép mọi thứ từ Streamlit app.py của bạn và dán vào.

Đảm bảo mã của bạn kết nối bằng st.connection hoặc getActiveSession.

Hãy nhớ rằng, các hàm này xử lý việc xác thực

và truy cập tự động khi bạn triển khai bên trong Snowflake.

Nhấp vào Chạy để khởi chạy nguyên mẫu của bạn.

Ứng dụng của bạn hiện đang hoạt động và có thể xem được bên trong Snowflake.

Tiếp theo nhấn Share để lấy link có thể chia sẻ cho đồng đội có quyền truy cập.

Chỉ cần đảm bảo ứng dụng đã triển khai của bạn đang chạy trơn tru

bằng cách kiểm tra lịch sử truy vấn để xem các truy vấn đang mất bao nhiêu thời gian và những gì đang được chạy.

Giám sát việc sử dụng kho để theo dõi chi phí, tải hàng và thời gian nhàn rỗi.

Sau đó đặt trình giám sát tài nguyên để nhận thông báo và quản lý chi tiêu.

Mẹo chuyên nghiệp, hãy đánh giá hàng tuần để tìm kiếm các truy vấn chậm,

các hoạt động dư thừa mà bạn có thể lưu vào bộ nhớ đệm và các đợt tính toán có chi phí cao.

Nếu bạn muốn tiến xa hơn nữa, hãy sử dụng ứng dụng Genii để giúp bạn

dự thảo tài liệu, đề xuất cải tiến mã,

tạo hướng dẫn triển khai và khắc phục các vấn đề về hiệu suất.

Bây giờ, hãy cung cấp ứng dụng của bạn cho thế giới.

Tạo một kho lưu trữ GitHub công khai mới.

Tải lên các tệp sau, streamletapp.py, require.txt, streamletconfig.toml,

và mọi thư mục dữ liệu có liên quan hoặc đẩy qua thiết bị đầu cuối.

Đầu tiên, đăng nhập vào Streamlet.io Slash Cloud và chọn tùy chọn đăng nhập bằng GitHub.

Sau đó nhấp vào Tạo ứng dụng, chọn kho lưu trữ bạn muốn triển khai,

và trỏ nó tới Streamletapp.py.

Và bây giờ bạn có thể nhấp vào Triển khai.

Sau khi thiết lập và chạy ứng dụng, bạn có thể truy cập menu quản lý ứng dụng của mình

bằng cách nhấp vào ba dấu chấm ở góc trên bên phải của ứng dụng của bạn.

Từ menu quản lý ứng dụng, chọn Quản lý ứng dụng từ trình đơn thả xuống.

Trên thanh bên xuất hiện, nhấp vào Cài đặt.

Thao tác này sẽ mở bảng cài đặt ứng dụng của bạn.

Bây giờ, bạn có thể nhấp vào Bí mật để thêm thông tin đăng nhập Snowflake của mình

để Streamlet luôn có thể truy cập dữ liệu của bạn.

Dán vào khối mã sau,

nhưng tất nhiên, hãy đảm bảo cập nhật thông tin này bằng thông tin đăng nhập của riêng bạn.

Khi bạn hoàn tất, hãy nhấp vào Lưu.

Ứng dụng của bạn sẽ tự động tải lại với thông tin đăng nhập mới.

Để kiểm tra và giám sát ứng dụng của bạn trên Streamlet Community Cloud,

truy cập URL cho ứng dụng đã triển khai của bạn.

Đây thường là một cái gì đó như thế này.

Bạn nên tự mình kiểm tra ứng dụng

trước khi gửi nguyên mẫu của bạn cho người khác.

Hãy kiểm tra nhanh để đảm bảo mỗi tab và tiện ích đều hoạt động.

Sau đó vào menu Cài đặt và nhấp vào Quản lý ứng dụng,

sau đó Nhật ký để kiểm tra mọi vấn đề.

Menu tương tự là nơi sau này bạn có thể xem số liệu thống kê sử dụng trong Analytics.

Bây giờ ứng dụng của bạn đã được triển khai,

bạn sẽ có thể nhanh chóng lặp lại nó và làm cho nó tốt hơn.

Làm tốt lắm!

Bạn đã triển khai nguyên mẫu Avalanche của mình một cách an toàn bên trong Snowflake

và công khai cho cả thế giới xem.

Bây giờ bạn có thể chia sẻ liên kết với nhóm của mình,

thêm nó vào danh mục đầu tư của bạn,

đăng nó lên LinkedIn hoặc X,

và quan trọng nhất là bắt đầu thu thập phản hồi để lặp lại.

Trong phòng thí nghiệm tiếp theo, bạn sẽ học cách thu thập và ưu tiên phản hồi

để làm cho ứng dụng của bạn thậm chí còn tốt hơn.

Nhưng bây giờ, hãy tận hưởng chiến thắng.

Bạn đã lấy ý tưởng của mình và biến nó thành hiện thực.