# 04 xuất bản ứng dụng của bạn trực tuyến

---

Bây giờ bạn đã học cách xây dựng ứng dụng Streamlit tương tác,

sử dụng GenAI để tạo mã, tải tập dữ liệu, xử lý dữ liệu,

và tạo tất cả các hình ảnh trực quan trong cùng một ứng dụng web.

Chỉ còn một điều duy nhất là chia sẻ nó với thế giới.

Trong video này, bạn sẽ tìm hiểu cách triển khai ứng dụng của mình trên Đám mây cộng đồng Streamlit.

Streamlit Community Cloud là một nền tảng miễn phí

giúp bạn dễ dàng triển khai và chia sẻ ứng dụng của mình trực tuyến.

Trên Streamlit Community Cloud, bạn nhận được các ứng dụng công cộng không giới hạn,

và mã cũng sẽ được công khai.

Một ứng dụng riêng cho mỗi tài khoản,

Tích hợp kho lưu trữ GitHub để triển khai dễ dàng,

cập nhật tự động khi bạn đẩy các thay đổi lên GitHub,

phân tích tích hợp để theo dõi việc sử dụng ứng dụng.

Đó là một cách nhanh chóng, miễn phí để đưa nguyên mẫu của bạn đến với người dùng.

Bắt đầu bằng cách mở trình duyệt của bạn và hướng tới đám mây chém Streamlit.io.

Nhấp vào Tham gia cộng đồng Cloud, sau đó nhấp vào tiếp tục đăng nhập.

Chọn tùy chọn GitHub để đăng nhập.

Tiếp theo, bạn sẽ được chuyển hướng đến GitHub.

Khi được yêu cầu cho phép Streamlit kết nối với tài khoản GitHub của bạn,

bấm ủy quyền.

Nếu đây là lần đầu tiên của bạn,

GitHub sẽ gửi mã xác minh tới email của bạn.

Kiểm tra hộp thư đến của bạn để tìm email này,

sao chép mã đã được gửi,

và dán nó vào để hoàn tất quá trình đăng nhập.

Streamlit sẽ yêu cầu các chi tiết cơ bản như tên và địa chỉ email của bạn.

Hãy điền vào những thông tin này và bạn đã sẵn sàng để đi.

Bạn có thể tiếp tục với ứng dụng của mình từ video trước,

hoặc chọn bất kỳ ứng dụng nào khác để làm việc trong video này.

Nếu bạn chưa làm vậy, hãy sao chép kho lưu trữ khóa học vào máy cục bộ của bạn.

Nếu bạn muốn bắt đầu với phiên bản thử nghiệm,

bạn có thể sử dụng các tệp nằm trong thư mục repo GitHub của khóa học

tại M1/Bài_03/triển khai

Tiếp theo, tạo một kho lưu trữ GitHub mới dành riêng cho ứng dụng đã triển khai của bạn.

Đăng nhập vào tài khoản GitHub của bạn.

Bấm vào nút dấu cộng ở góc trên bên phải màn hình.

Chọn Kho lưu trữ mới.

Đặt tên cho kho lưu trữ của bạn là Avalanche hoặc tên nào đó tương tự dọc theo các dòng đó.

Đặt kho lưu trữ ở chế độ công khai để chia sẻ dễ dàng hơn.

Sau đó bấm vào Tạo kho lưu trữ.

Điều này sẽ mở ra một kho lưu trữ GitHub mới cho bạn.

Trong kho lưu trữ GitHub mới của bạn, hãy nhấp vào Tải lên tệp hiện có.

Sau đó tải lên toàn bộ thư mục M1/Lesson_03/deploy.

Kho lưu trữ mới của bạn bây giờ sẽ chứa Streamlit_app.py,

require.txt và customer_reviews.csv.

Khi quá trình tải lên hoàn tất, hãy nhấp vào Cam kết thay đổi.

Và thế là xong.

Các tập tin của bạn hiện đã sẵn sàng để triển khai.

Để triển khai nguyên mẫu của bạn từ Snowflake lên Đám mây cộng đồng Streamlit,

bắt đầu bằng cách đăng nhập vào Streamlit.io/cloud.

Nhấp vào Tạo ứng dụng hoặc Ứng dụng mới ở góc trên cùng bên phải.

Chọn Triển khai ứng dụng công cộng từ GitHub và chọn tên người dùng GitHub của bạn

và tiêu đề repo Avalanche là Kho lưu trữ.

Để nhánh là nhánh chính và đảm bảo rằng nó trỏ đến tệp ứng dụng Streamlit của bạn

được gọi là streaminglit_app.py.

Chọn một tên tùy chỉnh duy nhất hoặc sử dụng địa chỉ web được tạo tự động cho nguyên mẫu của bạn.

Và sau đó bấm vào Triển khai.

Streamlit sẽ bắt đầu xây dựng ứng dụng của bạn và quá trình này có thể mất vài phút.

Trong khi ứng dụng của bạn đang triển khai,

hãy xem một số tùy chọn của bạn để theo dõi hiệu suất ứng dụng.

Bắt đầu bằng cách nhấp vào Quản lý ứng dụng ở góc dưới bên phải của màn hình tải.

Và bạn sẽ thấy hai phần chính.

Xem Nhật ký bản dựng là nơi bạn có thể tìm thấy tệp nhật ký của ứng dụng để khắc phục sự cố.

Và các tính năng quản lý ứng dụng cho phép bạn khởi động lại ứng dụng của mình nếu nó gặp sự cố.

Tải xuống tệp nhật ký, xóa hoàn toàn ứng dụng,

hoặc cập nhật cài đặt truy cập và quản lý các tệp bí mật của bạn.

Khi ứng dụng của bạn thiết lập và chạy,

bạn sẽ nhận được thông báo thành công cung cấp cho bạn địa chỉ trang web

mà bạn có thể sử dụng để xem nó.

Địa chỉ web thường giống như

https://yourappname.streamlit.app

và cũng có thêm một số chữ cái và số ngẫu nhiên.

Để kiểm tra, hãy duyệt đến URL và kiểm tra tất cả các tiện ích tương tác.

Điều hướng giữa tất cả các tab để đảm bảo chúng hoạt động,

sau đó xác minh rằng bảng dữ liệu và hình ảnh trực quan đang hiển thị chính xác.

Xin chúc mừng, ứng dụng của bạn hiện đã hoạt động và bất kỳ ai có liên kết đều có thể truy cập được.

Bạn muốn xem có bao nhiêu người đang xem ứng dụng của bạn?

Đây là cách thực hiện.

Đi tới bảng điều khiển Đám mây cộng đồng Streamlit của bạn.

Bên cạnh ứng dụng của bạn, bạn sẽ thấy ba dấu chấm.

Nhấp vào chúng và chọn Analytics.

Điều này cho bạn biết có bao nhiêu người đã truy cập ứng dụng của bạn và thời điểm họ truy cập.

Nếu có sự cố xảy ra với ứng dụng của bạn, bạn có thể kiểm tra nhật ký.

Nhấp vào Quản lý ứng dụng trên trang ứng dụng đã triển khai của bạn, sau đó xem bảng Nhật ký.

Điều này giúp bạn tìm ra nguyên nhân gây ra bất kỳ sự cố nào với ứng dụng của mình.

Chúc mừng!

Bạn đã triển khai thành công nguyên mẫu Streamlit của mình lên đám mây

và làm cho nó có thể tiếp cận được với thế giới.

Đây là một thành tựu thực sự.

Bạn đã tiến được một bước nhiều hơn hầu hết mọi người

bằng cách biến ý tưởng thành ứng dụng web trực tiếp và có thể chia sẻ.

Bây giờ nguyên mẫu của bạn đã được triển khai, bạn có thể chia sẻ liên kết với đồng nghiệp của mình,

thêm nó vào danh mục đầu tư của bạn hoặc đăng nó lên mạng xã hội.

Bạn sẽ kết thúc bài học trong phòng thí nghiệm, nơi bạn sẽ áp dụng tất cả kiến ​​thức của mình vào công việc.