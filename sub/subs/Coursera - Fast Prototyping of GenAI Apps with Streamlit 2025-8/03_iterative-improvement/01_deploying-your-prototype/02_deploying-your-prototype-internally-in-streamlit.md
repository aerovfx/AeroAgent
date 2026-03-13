# 02 triển khai-nguyên mẫu-nội bộ-trong-streamlit

---

Trong video này, bạn sẽ triển khai nguyên mẫu Avalanche đã hoàn thiện của mình ngay bên trong

Bông tuyết, nơi đồng nghiệp của bạn có thể truy cập nó một cách an toàn và

cung cấp phản hồi trước khi bạn công khai.

Đến cuối bài học này, bạn sẽ triển khai bảng thông tin hoàn chỉnh của mình trong

Snowflake là một ứng dụng nội bộ mà đồng nghiệp của bạn có thể truy cập dựa trên vai trò của họ.

Hãy bắt đầu bằng cách triển khai ứng dụng đã hoàn thành của bạn.

Bạn đã tạo một ứng dụng Streamlit chạy trực tiếp bên trong Snowflake Notebook.

Bạn có thể tìm thấy mã cho ứng dụng đó trong kho GitHub ở liên kết sau.

Tải xuống tệp Streamlitapp.py chứa phân tích cảm tính của bạn

mã bảng điều khiển.

Bây giờ, hãy đăng nhập vào tài khoản Snowflake của bạn để triển khai nội bộ ứng dụng của bạn bằng cách sử dụng

Trang web tuyết.

Trong thanh điều hướng bên trái, chọn Dự án, sau đó chọn Streamlit.

Ở góc trên bên phải, nhấp vào nút ứng dụng Streamlit dấu cộng màu xanh lam.

Cửa sổ Tạo ứng dụng Streamlit sẽ mở ra.

Trong cửa sổ bật lên Tạo ứng dụng Streamlit, hãy đặt tên cho ứng dụng của bạn.

Trong trình đơn thả xuống vị trí ứng dụng, hãy chọn cơ sở dữ liệu AvalancheDB và

Lược đồ Avalanche mà bạn đã tạo ở video trước.

Chọn kho điện toán mặc định.

Nhấp vào Tạo để khởi tạo ứng dụng Streamlit mới.

Bạn sẽ được đưa đến trình soạn thảo Streamlit với chế độ xem mã song song và

ứng dụng.

Trong trình chỉnh sửa Streamlit, bạn sẽ thấy một số mã Hello World mặc định.

Xóa tất cả mã hiện có trong trình chỉnh sửa.

Sao chép tất cả mã từ tệp Streamlitapp.py đã tải xuống của bạn và

dán nó vào trình soạn thảo.

Trước khi chạy ứng dụng, bạn cần thêm các gói cần thiết.

Tập lệnh này sử dụng matplotlib và snow-ml-python.

Vì vậy hãy chọn Gói ở trên cùng bên trái.

Nhập matplotlib và snow-ml-python rồi chọn nó.

Nhấp vào nút Chạy trong trình chỉnh sửa để triển khai ứng dụng của bạn.

Bản xem trước ứng dụng sẽ xuất hiện ở khung bên phải của trình chỉnh sửa.

Sau khi ứng dụng của bạn tải xong, ứng dụng sẽ hoạt động và chạy bên trong Snowflake.

Trình chỉnh sửa song song và

màn hình xem trước cho phép bạn xem các thay đổi trong thời gian thực khi bạn sửa đổi mã của mình.

Ứng dụng đang chạy của bạn sẽ trông giống như thế này.

Khi chạy ứng dụng Streamlit trong Snowflake,

những thay đổi đối với mã của bạn sẽ xuất hiện ngay trong khung xem trước.

Ứng dụng của bạn sử dụng các phương thức kết nối tích hợp của Snowflake, vì vậy

việc này sẽ tự động xử lý những việc sau.

Xác thực thông qua phiên Snowflake hiện tại của bạn.

Kiểm soát truy cập dựa trên vai trò hoặc RBAC để bảo mật dữ liệu.

Và quản lý phiên tự động và tổng hợp kết nối cho các truy vấn SQL.

Nếu bạn không quen với những điều khoản này, đừng lo lắng.

Chúng tôi sẽ giải thích chúng chi tiết hơn một chút sau này.

Nhưng vì bạn đang làm việc ở Snowflake,

nó sẽ chỉ lo những việc này cho bạn.

Ứng dụng của bạn hiện đã được triển khai nội bộ và sẵn sàng chia sẻ với đồng nghiệp.

Để chia sẻ ứng dụng của bạn,

nhấp vào nút Chia sẻ ở góc trên bên phải của ứng dụng Streamlit của bạn.

Bạn sẽ được cung cấp một liên kết web mà các đồng nghiệp trên nền tảng Snowflake

có thể sử dụng để truy cập ứng dụng của bạn.

Chia sẻ ứng dụng của bạn với những người dùng khác trong tài khoản Snowflake của bạn

thông qua kiểm soát truy cập dựa trên vai trò hoặc RBAC.

Điều này có nghĩa là quyền truy cập được kiểm soát bởi các quyền và vai trò hiện có của Snowflake.

Người dùng sẽ cần quyền truy cập vào cơ sở dữ liệu và lược đồ cơ bản để xem dữ liệu.

Ứng dụng vẫn an toàn trong môi trường Bông tuyết của bạn.

Đối với ứng dụng Avalanche, điều này có nghĩa là người dùng có quyền truy cập vào Avalanche DB

và lược đồ Avalanche có thể xem ứng dụng.

Bất kỳ ai có vai trò quản trị viên đều có thể sửa đổi cài đặt và quyền của ứng dụng.

Và việc truy cập dữ liệu sẽ tuân theo các chính sách bảo mật Snowflake hiện có.

Khi bạn triển khai ứng dụng Streamlit trong Snowflake,

nó tiêu thụ tài nguyên máy tính thông qua kho ảo.

Ứng dụng của bạn cần một kho lưu trữ để thực thi các truy vấn SQL đối với dữ liệu của bạn.

Kho vẫn hoạt động trong khi người dùng đang tích cực sử dụng ứng dụng của bạn,

và mỗi phần người dùng có thể kích hoạt nhiều truy vấn

thông qua việc tải dữ liệu, lọc, tổng hợp, v.v.

Do đó, quy mô kho của bạn ảnh hưởng trực tiếp đến cả hiệu suất và chi phí.

Để theo dõi hiệu suất, có một số số liệu chính cần theo dõi,

chẳng hạn như sức chứa kho của bạn đang được sử dụng bao nhiêu,

mất bao lâu để hoàn thành các truy vấn riêng lẻ,

chi phí vận hành kho của bạn theo thời gian,

có bao nhiêu người đang sử dụng ứng dụng của bạn cùng một lúc.

Snowflake cung cấp một số công cụ để theo dõi hiệu suất ứng dụng của bạn từ bên trong Snowsite.

Để kiểm tra lịch sử truy vấn, hãy đi tới Hoạt động rồi đến Lịch sử truy vấn.

Điều này sẽ hiển thị cho bạn mọi truy vấn SQL mà ứng dụng Streamlit của bạn thực hiện

và có thể giúp bạn theo dõi thời lượng truy vấn, thời gian thực hiện, kho và tính toán được sử dụng,

các khoản tín dụng đã sử dụng và kế hoạch thực hiện.

Để kiểm tra việc sử dụng kho từ Snowsite, hãy truy cập Quản trị viên rồi đến Kho.

Công cụ Warehouses hiển thị cả hiệu suất kho hàng theo thời gian thực và lịch sử,

giúp bạn có được bức tranh rõ hơn về thời gian hoạt động và nhàn rỗi,

độ sâu hàng đợi, thời gian thực hiện trung bình và mức sử dụng tín dụng theo thời gian.

Bảng quản trị cũng có một công cụ tên là Resource Monitors

điều đó sẽ hiển thị cho bạn các cảnh báo về việc kiểm soát chi phí và sử dụng.

Điều này có thể giúp bạn đặt ra giới hạn chi tiêu cho kho hàng,

nhận thông báo khi đạt đến ngưỡng,

và tự động tạm dừng kho để kiểm soát chi phí.

Nếu nguyên mẫu của bạn trở thành những ý tưởng tuyệt vời mà tất cả chúng ta đều hy vọng,

bạn nên đưa ra quy trình đánh giá hàng tuần

để theo dõi việc sử dụng ứng dụng của bạn.

Hàng tuần, bạn nên kiểm tra lịch sử truy vấn,

để xác định các truy vấn chậm hoặc tốn kém,

phân tích các mẫu để tìm kiếm các hoạt động lặp lại mà bạn có thể lưu vào bộ nhớ đệm để đạt hiệu quả,

xem xét việc sử dụng kho để đảm bảo kích thước phù hợp với tải thực tế,

thử nghiệm tối ưu hóa bằng cách thực hiện các thay đổi nhỏ và đo lường tác động của chúng,

và theo dõi kết quả để theo dõi sự cải thiện về số liệu hiệu suất.

Phương pháp giám sát này giúp bạn duy trì một hệ thống giám sát hiệu quả về mặt chi phí,

ứng dụng Streamlit hiệu suất cao,

đồng thời đảm bảo trải nghiệm người dùng tốt cho đồng nghiệp của bạn khi truy cập trang tổng quan nội bộ.

Dưới đây là một số mẹo để cải thiện trải nghiệm người dùng khi triển khai nguyên mẫu của bạn.

Cung cấp điều hướng và hướng dẫn rõ ràng.

Bao gồm các lời khuyên và mô tả công cụ hữu ích.

Đảm bảo thiết kế đáp ứng cho các kích thước màn hình khác nhau.

Thử nghiệm với các vai trò và quyền khác nhau của người dùng trước khi triển khai.

Và thế là xong, ứng dụng của bạn đã có mặt trên Snowflake.

Chúc mừng!

Bạn đã triển khai thành công bảng thông tin phân tích cảm tính bằng Streamlit trong Snowflake.

Việc triển khai nội bộ của bạn trong Snowflake cung cấp nền tảng thử nghiệm hoàn hảo

để tinh chỉnh trang tổng quan của bạn và đảm bảo trang tổng quan sẵn sàng cho truy cập công cộng rộng rãi hơn.