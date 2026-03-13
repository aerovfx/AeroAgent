# 04 xây dựng-your-ai-Powered-stream-app-inside-bông tuyết

---

Trong video trước, bạn đã tìm hiểu sâu về tập dữ liệu của mình

bằng cách hình dung nó với sự trợ giúp của GenAI.

Trong bài học này, bạn sẽ tổng hợp mọi thứ bạn đã học ở mô-đun 2

bằng cách xây dựng một ứng dụng Streamlit đầy đủ chức năng.

Ứng dụng của bạn sẽ bao gồm tính năng lọc tương tác của dữ liệu vận chuyển và đánh giá,

trực quan hóa bằng Matplotlib và Streamlit,

phân tích tình cảm bằng Cortex,

và cuối cùng nhưng không kém phần quan trọng, trợ lý LM tích hợp sẵn để hỏi đáp động trên dữ liệu của bạn.

Bắt đầu nào.

Bạn đang hoàn thành kế hoạch xây dựng MVP này và đã ở bước 6,

tạo bảng điều khiển.

Bước này là nơi cuối cùng bạn tập hợp nguyên mẫu của mình lại với nhau

và sẵn sàng gửi nó đi để nhận phản hồi.

Những phần khó nhất đã được thực hiện.

Nhập dữ liệu, làm sạch, phân tích, trực quan hóa.

Bạn gần như ở đó.

Đã đến lúc đưa nguyên mẫu của bạn vào cuộc sống.

Bạn sẽ xây dựng ứng dụng Avalanche Streamlit ngay bên trong Snowflake Notebook,

cùng một môi trường mà bạn đã làm việc trong suốt thời gian qua.

Tạo một sổ ghi chép mới và gọi nó là ứng dụng gạch dưới Avalanche.

Đảm bảo kết nối nó với cơ sở dữ liệu và lược đồ Avalanche hiện có của bạn

và chỉ nó vào bảng kết hợp cả đánh giá của khách hàng và dữ liệu vận chuyển.

Đây là nơi nó trở nên thú vị.

Bạn sẽ viết toàn bộ ứng dụng Streamlit của mình dưới dạng mã vào một ô sổ tay.

Nhấn chạy và xem ứng dụng web tương tác đầy đủ xuất hiện dưới dạng đầu ra của ô.

Nó giống như phép thuật, ngoại trừ trò ảo thuật này trở thành một công cụ thực sự mà mọi người có thể sử dụng.

Để bắt đầu, hãy làm cho việc này trở nên dễ dàng bằng cách chỉ tạo một trình bao Streamlit cơ bản.

Thay vì viết lại từ đầu,

sao chép và dán mã từ video trước

hoặc chỉ cần yêu cầu Genii giúp bạn với lời nhắc như,

viết ứng dụng Streamlit tải bảng trên Snowflake để phân tích cảm tính,

hiển thị một số số liệu thống kê cơ bản và thêm tiêu đề và thanh bên.

Ứng dụng Genii của bạn sẽ tạo mã Python cho ứng dụng Streamlit cơ bản.

Sao chép và dán mã vào sổ ghi chép của bạn và chạy ô.

Nếu có gì đó không ổn, hãy sử dụng Genii để gỡ lỗi hoặc sửa lại mã.

Bạn có thể hỏi điều gì đó như,

giúp mình khắc phục lỗi này hoặc bạn có thể viết lại hàm này để tránh lỗi này được không.

Tiếp tục thử nghiệm và lặp lại cho đến khi ứng dụng của bạn chạy trơn tru.

Tiếp theo, bạn có thể sử dụng biểu đồ mà bạn đã tạo trong các bài học trước.

Chúng nên bao gồm một biểu đồ đường về các chuyến hàng mỗi ngày,

biểu đồ thanh phân bổ cảm xúc,

và một số số liệu thống kê cấp sản phẩm hoặc thông tin chi tiết về sản phẩm cao cấp nhất.

Bạn có thể yêu cầu Genii tạo biểu đồ đường Streamlit để hiển thị lô hàng.

Thêm mã vào ứng dụng của bạn và nó sẽ trông giống như sau.

Bạn cũng có thể yêu cầu Genii trợ giúp về nhãn truy cập,

truyền thuyết và làm cho biểu đồ có tính tương tác.

Giờ đây, bạn có thể sử dụng tiện ích Streamlit để thêm bộ lọc

và làm cho ứng dụng của bạn trở nên tương tác và hữu ích hơn.

Nhắc Genii những điều sau,

thêm bộ lọc ngày và cảm tính vào ứng dụng Streamlit của tôi.

Nó sẽ trả lại một cái gì đó như thế này.

Bây giờ, đã đến lúc bắt đầu sử dụng Cortex để thêm chatbot

có thể trả lời các câu hỏi về tập dữ liệu.

Bạn có thể nhờ Genii tạo chatbot trên Streamlit

sử dụng Snowflake Cortex để trả lời các câu hỏi về bảng đánh giá rõ ràng.

Ứng dụng Genii của bạn có thể sẽ trả về nội dung như sau

và một cuộc gọi như thế này.

Để sử dụng Cortex trong Python,

bạn cần cài đặt gói Snowflake ML Python

từ trình đơn thả xuống trong sổ ghi chép của bạn.

Vì vậy, đừng quên làm điều đó.

Điều này mang lại cho người dùng của bạn một giao diện thân thiện để đặt các câu hỏi như,

cảm tính trung bình đối với sản phẩm A là gì?

Hoặc tại sao có ít lô hàng hơn vào ngày cụ thể này?

Chạy sổ ghi chép và bây giờ bạn đã có một chatbot trực tiếp bên trong nguyên mẫu Genii của mình.

Nếu bạn bị kẹt ở đâu đó, đừng lo lắng.

Bạn có thể tìm thấy mã trong mô-đun Cortex tại liên kết này.

Làm tốt.

Bạn đã biến phân tích cảm tính của mình thành một nguyên mẫu Streamlit đang hoạt động.

Trong mô-đun tiếp theo, bạn có thể triển khai, chia sẻ và cải thiện ứng dụng của mình

dựa trên phản hồi từ người dùng của bạn.

Bạn cũng sẽ học cách cải thiện kết quả của mình

sử dụng các kỹ thuật nhắc nhở Genii nâng cao.

Hẹn gặp bạn ở phòng thí nghiệm.