# 03 triển khai lên đám mây cộng đồng-streamlit

---

Trong video này, bạn sẽ tìm hiểu cách lấy nguyên mẫu Bảng điều khiển dữ liệu Avalanche của mình

từ Snowflake và triển khai nó lên Streamlit Community Cloud.

Điều này sẽ cho phép bạn chia sẻ dự án của mình với người khác chỉ bằng cách gửi cho họ một liên kết.

Bạn đã thực hiện việc này cho nguyên mẫu của mình ở Mô-đun 1.

Bây giờ, bạn sẽ làm điều tương tự.

Nhưng lần này, bạn cũng sẽ cần thiết lập tệp bí mật.

Bí mật là thông tin xác thực và thông số

Streamlit sẽ sử dụng để kết nối với tài khoản Snowflake của bạn.

Nếu bạn chưa làm như vậy,

đã đến lúc tạo tài khoản Streamlit Community Cloud của bạn và đăng nhập vào tài khoản đó bằng GitHub.

Bạn có thể tìm thấy hướng dẫn chi tiết trong Mô-đun 1.

Trong GitHub, tạo một kho lưu trữ GitHub mới dành riêng cho ứng dụng đã triển khai của bạn,

giống như bạn đã làm ở Mô-đun 1.

Chọn một tên riêng biệt mới cho repo của bạn.

Trong kho GitHub mới của bạn, nhấp vào Tải lên tệp hiện có,

sau đó tải lên toàn bộ thư mục bài học.

Kho lưu trữ mới của bạn bây giờ sẽ chứa StreamlitApp.py và cảRequires.txt.

Khi quá trình tải lên hoàn tất, hãy nhấp vào Cam kết thay đổi.

Các tập tin của bạn hiện đã sẵn sàng để triển khai.

Tiếp theo, đăng nhập vào đám mây chém Streamlit.io.

Nhấp vào Tạo ứng dụng hoặc Ứng dụng mới ở góc trên cùng bên phải.

Chọn Triển khai ứng dụng công cộng từ GitHub,

và chọn tên người dùng GitHub của bạn và tiêu đề kho lưu trữ làm Kho lưu trữ.

Để nhánh là Main,

và đảm bảo rằng nó trỏ đến tệp StreamlitApp của bạn có tên StreamlitApp.py.

Chọn một tên miền phụ duy nhất hoặc sử dụng địa chỉ web được tạo tự động cho nguyên mẫu của bạn,

sau đó bấm vào Triển khai.

Streamlit bây giờ sẽ bắt đầu xây dựng ứng dụng của bạn, quá trình này có thể mất vài phút.

Vì bạn muốn lấy dữ liệu từ Snowflake,

ứng dụng của bạn sẽ cần định cấu hình quyền truy cập vào cơ sở dữ liệu Avalanche Snowflake.

Bạn có thể thực hiện việc này bằng cách truy cập ứng dụng đã triển khai của mình,

nhấp vào Quản lý ứng dụng ở góc dưới bên phải,

sau đó nhấp vào ba dấu chấm và sau đó Cài đặt.

Tiếp theo, trong thanh bên, nhấp vào Bí mật.

Trong hộp Bí mật xuất hiện, hãy thêm thông tin đăng nhập Snowflake của bạn, như thế này.

Đảm bảo cập nhật tất cả thông tin này bằng thông tin xác thực của riêng bạn,

chẳng hạn như tên người dùng và mật khẩu của bạn.

Mã nhận dạng tài khoản của bạn là một phần của địa chỉ web bạn nhìn thấy trong trình duyệt của mình

khi bạn đăng nhập vào Snowflake.

Nếu bạn gặp khó khăn khi tìm ID tài khoản của mình,

kiểm tra tài liệu Snowflake.

Sau khi các thay đổi của bạn được lưu,

ứng dụng sẽ tự động làm mới và hiện sử dụng dữ liệu trực tiếp từ cơ sở dữ liệu Bông tuyết của bạn.

Nếu ứng dụng của bạn không hoạt động thì đây là một số cách khắc phục phổ biến nhất.

Ứng dụng sẽ không bắt đầu?

Kiểm tra xem tất cả các tệp của bạn đã được tải lên GitHub đúng cách chưa

và đảm bảo tệp require.txt của bạn không có bất kỳ lỗi chính tả nào.

Không thể kết nối với Bông tuyết?

Kiểm tra kỹ mã nhận dạng tài khoản, tên người dùng và mật khẩu của bạn trong phần Bí mật.

Đồng thời xác minh rằng tên kho và cơ sở dữ liệu của bạn được viết đúng chính tả.

Tiếp theo, đến lượt bạn thử.