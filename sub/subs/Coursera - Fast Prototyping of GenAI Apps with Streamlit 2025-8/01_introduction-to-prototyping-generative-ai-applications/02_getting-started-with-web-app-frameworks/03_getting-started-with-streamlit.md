# 03 bắt đầu với tinh giản

---

Đã đến lúc biến tập lệnh GenAI của bạn thành một ứng dụng web tương tác chạy trên trình duyệt của bạn.

Bạn sẽ sử dụng Streamlit, hoạt động như một chất kết dính giữa mã Python của bạn và giao diện web đầy đủ,

không cần giao diện người dùng. Đến cuối video này, bạn sẽ có một nguyên mẫu hoạt động được

lấy thông tin đầu vào của người dùng, gửi nó đến mô hình GenAI và hiển thị phản hồi trong trình duyệt của bạn.

Hãy xây dựng.

Ở video trước các bạn đã cài đặt Streamlit khi cài đặt file require.txt.

Để xác minh rằng quá trình cài đặt đã hoạt động, hãy nhập phiên bản dấu gạch ngang có đèn chiếu sáng. Bạn sẽ thấy số phiên bản.

Nếu không, hãy kiểm tra xem môi trường ảo của bạn có đang hoạt động không và thử lại.

Trong video này, bạn có thể tiếp tục làm việc với tệp bạn có từ video trước,

hoặc nếu bạn muốn xem trực tiếp giải pháp, hãy mở tệp này.

Tập lệnh của bạn đã kết nối với OpenAI. Đã đến lúc biến nó thành một ứng dụng đầy đủ.

Để biến tập lệnh Python của bạn từ video cuối cùng thành một ứng dụng web đơn giản,

bạn chỉ cần thêm một vài dòng mã.

Nhập Streamlit dưới dạng st.

Dòng này nhập gói Streamlit và đặt cho nó phím tắt st,

để bạn có thể dễ dàng sử dụng chức năng của nó trong toàn bộ ứng dụng của mình.

Ở đầu tập lệnh, bạn sẽ thấy st.title Hello GenAI.

Điều này tạo ra một tiêu đề lớn cho ứng dụng của bạn.

Bên dưới nó, bạn có thể viết một số văn bản về chức năng của ứng dụng.

st.write, đây là ứng dụng Streamlit đầu tiên của bạn.

st.write là một hàm linh hoạt có thể hiển thị văn bản, số, khung dữ liệu, v.v.

Sau đó, thay vì sử dụng chức năng in để in phản hồi của mô hình tới thiết bị đầu cuối,

chúng tôi sẽ sử dụng lại st.write để hiển thị kết quả đầu ra của mô hình trong ứng dụng của bạn.

Thế thôi. Chỉ cần bốn dòng mã và tập lệnh dòng lệnh của bạn giờ đây đã là một ứng dụng web.

Lưu tập tin và sẵn sàng khởi chạy.

Bây giờ, phần thú vị nhất là bạn sẽ thấy ứng dụng của mình hoạt động như thế nào.

Một lần nữa, bạn sẽ chạy ứng dụng của mình từ thiết bị đầu cuối,

nhưng lần này bạn sẽ sử dụng Streamlit để chạy script.

Trong terminal của bạn, gõ lệnh này, chạy app.py.

Thao tác này khởi động máy chủ web cục bộ và mở ứng dụng của bạn trong trình duyệt.

Bạn sẽ thấy một thông báo như thế này.

Bây giờ bạn có thể xem ứng dụng Streamlit trong trình duyệt của mình.

Nếu nó không tự động mở, hãy truy cập http://localhost 8501.

Xin chúc mừng, bạn đang sống.

Đã đến lúc kiểm tra ứng dụng của bạn trong trình duyệt.

Bạn sẽ thấy tiêu đề ứng dụng của mình và bên dưới tiêu đề đó,

phản hồi một câu từ mô hình GenAI mà bạn đã in ra trước đó trên dòng lệnh.

Việc gọi đến mô hình GenAI không phải lúc nào cũng diễn ra ngay lập tức,

vì vậy đừng lo lắng nếu có sự chậm trễ trước khi bạn nhận được phản hồi.

Miễn là thiết bị đầu cuối của bạn mở, ứng dụng của bạn sẽ hoạt động.

Bất kỳ ai trên máy của bạn truy cập URL đó đều có thể tương tác với nó.

Khi bạn đã sẵn sàng dừng ứng dụng,

chỉ cần quay lại thiết bị đầu cuối của bạn và nhấn Ctrl-C để tắt nó.

Ứng dụng của bạn lúc này có thể trông đơn giản,

nhưng đây là nền tảng cho mọi thứ tiếp theo.

Streamlit tự động làm mới ứng dụng của bạn bất cứ khi nào bạn lưu tập lệnh của mình.

Chỉ cần nhấn lưu, không cần khởi động lại hay tải lại.

Vòng phản hồi tức thời này giúp bạn dễ dàng lặp lại.

Thực hiện thay đổi, lưu tệp rồi xem bản cập nhật xuất hiện ngay lập tức.

Bạn đã làm được điều đó. Chúc mừng.

Bây giờ bạn đã có một ứng dụng web hỗ trợ GenAI đang hoạt động.

Không có bình, không có JavaScript, không đau đớn.

Streamlit tạo ra một máy chủ web mini, xử lý bố cục và giám sát mọi thứ.

Điều đó có nghĩa là bạn vẫn sử dụng Python,

bạn tạo mẫu nhanh và người dùng của bạn nhận được kết quả theo thời gian thực.

Trong video tiếp theo, bạn sẽ phát triển ứng dụng của mình hơn nữa,

thêm tính tương tác, đánh bóng và các tính năng nâng cao hơn.

Hãy tiếp tục xây dựng.