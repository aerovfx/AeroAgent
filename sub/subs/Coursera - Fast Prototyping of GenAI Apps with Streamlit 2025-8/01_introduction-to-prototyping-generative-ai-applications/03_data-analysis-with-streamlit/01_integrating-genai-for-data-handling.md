# 01 tích hợp-genai-để xử lý dữ liệu

---

Trong bài học trước, bạn đã xây dựng ứng dụng Streamlit đầu tiên được hỗ trợ bởi GenAI,

đây là một giao diện đơn giản cho phép người dùng nhập lời nhắc và xem phản hồi.

Bây giờ, bạn sẽ nâng cấp ứng dụng của mình bằng cách sắp xếp quy trình làm việc.

Đối với bản demo này, bạn có thể làm theo bằng cách mở M1L3V1_starting.py

hoặc mở M1L3V1.py để tìm tệp giải pháp.

Lần này, bạn sẽ xây dựng một ứng dụng có nhiều chức năng.

Vì vậy, thật tốt khi được tổ chức.

Bạn có thể sử dụng st.columns để hiển thị các nút cạnh nhau như thế này.

Sau đó đặt một nút vào mỗi cột.

Hãy thử chạy ứng dụng bằng Streamlit run với đường dẫn đến tệp của bạn.

Và bạn sẽ thấy một cái gì đó như thế này.

Bây giờ bạn có hai nút cạnh nhau.

Nhưng nếu bạn nhấp vào chúng, vẫn chưa có gì xảy ra.

Bạn có thể sử dụng st.columns để tinh chỉnh độ rộng của cột,

điều chỉnh khoảng cách giữa các cột và hơn thế nữa.

Kiểm tra liên kết ở cuối màn hình của bạn để biết thêm thông tin.

Bây giờ, hãy triển khai chức năng của nút đầu tiên.

Bạn có thể sao chép mã này để thay thế đường dẫn ở nút đầu tiên.

Một điều quan trọng bạn cần chú ý ở đây là khung dữ liệu

không chỉ được lưu vào biến df như thường lệ,

mà là một thứ gọi là trạng thái phiên.

Lý do bạn cần làm điều này là vì Streamlit chạy lại toàn bộ script từ trên xuống dưới.

Mỗi khi người dùng tương tác với ứng dụng.

Điều này có nghĩa là nếu bạn nhấp vào nút, tất cả các biến sẽ bị mất.

Trừ khi bạn lưu trữ chúng ở đâu đó liên tục giữa các lần chạy.

Để đạt được điều này, bạn có thể sử dụng thứ gọi là trạng thái phiên.

Bằng cách lưu trữ khung dữ liệu trong st.session_state df,

ứng dụng của bạn ghi nhớ nó ngay cả khi tập lệnh chạy lại.

Điều này cho phép người dùng nhập tập dữ liệu để sau này thực hiện các thao tác trên đó

mà không cần phải ăn lại.

Bây giờ, thật tuyệt khi hiển thị tập dữ liệu này.

Sử dụng mã này ở cuối tập lệnh để thực hiện.

Nhưng hãy chú ý đến cách viết mã này.

Nó nằm trong khối if.

Bạn cần câu lệnh if này để kiểm tra xem tập dữ liệu đã được nhập hay chưa

và được lưu vào trạng thái phiên.

Hãy nhớ rằng, mỗi khi ứng dụng được tải lại, nó sẽ chạy toàn bộ tập lệnh.

Nếu không có dữ liệu được nhập, nó không thể được hiển thị.

Bây giờ, hãy mở lại ứng dụng và kiểm tra xem nó có hoạt động không.

Bây giờ, nếu bạn nhấn nút đầu tiên, tập dữ liệu sẽ được tải và hiển thị bên dưới.

Tiếp theo, bạn sẽ cần thêm chức năng vào nút còn lại.

Bạn có rất nhiều thứ để xây dựng.

Tại sao không ủy thác những việc nhàm chán?

Giả sử ứng dụng của bạn cần xóa văn bản đến.

Bạn có thể viết tất cả bằng tay hoặc nhắc GenAI viết bản nháp.

Đây là một ví dụ.

Nhắc nhở.

Viết hàm Python để xóa văn bản bằng cách xóa dấu câu,

vỏ dưới, mọi thứ và loại bỏ khoảng trắng.

Mô hình có thể trả về một cái gì đó như thế này.

Nó không cầu kỳ nhưng sạch sẽ, có thể kiểm tra và dễ tích hợp vào ứng dụng của bạn.

Sao chép mã và dán vào đầu ứng dụng của bạn.

Sau đó, bạn cần thêm chức năng đó vào nút của mình.

Bạn muốn xóa tập dữ liệu đã nhập.

Vì vậy, trước tiên bạn cần kiểm tra xem tập dữ liệu có tồn tại ở trạng thái phiên hay không.

Tất cả những gì bạn cần làm bây giờ là áp dụng thao tác này cho một cột trong tập dữ liệu của bạn

và lưu nó vào trạng thái phiên.

Hãy tiếp tục và kiểm tra ứng dụng.

Bây giờ, bạn có một nút để nhập tập dữ liệu và một nút khác để xóa tập dữ liệu đó.

Bạn có thể nhận thấy rằng dường như không có gì xảy ra khi bạn nhấp vào nút này.

Nhưng đừng lo lắng.

Điều này chỉ là do tập dữ liệu này có nhiều cột hơn những gì hiển thị trên màn hình.

Nếu bạn sử dụng thanh trượt, bạn có thể thấy cột đã được làm sạch ở đây.

Bây giờ, bạn có thể thêm một chút tính tương tác vào ứng dụng của mình.

Người dùng của bạn có thể chỉ quan tâm đến những đánh giá về các sản phẩm cụ thể.

Vì vậy, bạn có thể thêm menu thả xuống để lọc tập dữ liệu được hiển thị

để chỉ hiển thị các cột có liên quan.

Để làm điều này, bạn có thể thêm st.selectbox vào mã của mình

và chuyển nó làm tham số cho danh sách sản phẩm.

Sau đó, bạn cần thêm logic để lọc tập dữ liệu.

Bạn cũng có thể thêm tùy chọn tất cả sản phẩm trong trường hợp người dùng muốn phân tích tất cả sản phẩm.

Bạn có thể thực hiện việc này bằng cách cập nhật logic lọc.

Nếu một sản phẩm được chọn, bạn muốn lọc khung dữ liệu.

Nhưng nếu tất cả các sản phẩm được chọn,

bạn muốn sử dụng khung dữ liệu gốc để hiển thị.

Lưu và làm mới ứng dụng của bạn để xem nó có hoạt động không.