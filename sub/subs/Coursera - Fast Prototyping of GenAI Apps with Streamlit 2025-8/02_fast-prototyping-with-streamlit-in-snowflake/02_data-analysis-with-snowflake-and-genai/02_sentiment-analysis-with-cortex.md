# 02 phân tích tình cảm với vỏ não

---

Trong bài học này, bạn sẽ sử dụng các hàm Cortex để thực hiện phân tích cảm tính về các đánh giá của khách hàng Avalanche.

Thay vì viết mã theo cách thủ công, bạn sẽ tận dụng các công cụ Genii để tăng tốc quy trình làm việc của mình.

Đã đến lúc quay lại kế hoạch xây dựng MVP và kiểm tra xem chúng tôi đang ở đâu trong quá trình này.

Video này sẽ đưa bạn qua bước 4, phân tích dữ liệu.

Vì dữ liệu đã được làm sạch và chuẩn bị trước nên phần này sẽ diễn ra khá nhanh.

Mở sổ ghi chép Snowflake mới trong trang Snow và đảm bảo bạn đã chọn Avalanche DB và Avalanche Schema.

Và để mọi thứ khác ở chế độ mặc định.

Hãy tiếp tục và chạy khối mã đầu tiên để khởi tạo phiên Snowflake của bạn.

Sau đó, xóa hai khối mã mặc định và bạn đã sẵn sàng.

Bây giờ là lúc yêu cầu ứng dụng Genii giúp bạn chọn Cortex để chấm điểm cảm tính.

Đầu tiên, đặt vai trò bằng một câu lệnh như thế này.

Bạn là chuyên gia nền tảng dữ liệu Snowflake chuyên về tích hợp Python và SQL.

Vai trò của bạn là dạy Snowflake cách phân tích dữ liệu bằng cách cung cấp các giải pháp đơn giản nhất, thân thiện với người mới bắt đầu.

Sau đó sử dụng lời nhắc như thế này để nhận điểm cảm tính.

Viết Snowflake SQL sử dụng hàm cảm tính Snowflake Cortex trên cột văn bản đánh giá trong bảng đánh giá của khách hàng để trả về nhãn và điểm cảm tính.

Bạn sẽ nhận được một truy vấn giống như truy vấn này sử dụng Snowflake SQL.

Vì đây là cách đơn giản nhất để lấy điểm cảm tính cho khung dữ liệu của bạn.

Ở đây, Cortex sử dụng cảm tính trên cột văn bản đánh giá để trả về điểm cảm tính cho mỗi bài đánh giá.

Bạn có thể chạy truy vấn trong sổ ghi chép của mình bằng cách sử dụng một dòng tải kết quả vào khung dữ liệu gấu trúc.

Sau đó, bạn có thể xem kết quả bằng hàm pandas df.head.

Khung dữ liệu kết quả có văn bản đánh giá ban đầu và điểm cảm tính cho mỗi bài đánh giá.

Hoạt động này diễn ra nhanh chóng vì Cortex đã xử lý việc chấm điểm ở quy mô lớn bên trong Snowflake.

Bây giờ chúng ta đã có điểm cảm tính, thật dễ dàng để hình dung sự phân bổ điểm bằng cách sử dụng biểu đồ trong matplotlib.

Ồ, nhìn này, chúng ta đang gặp lỗi không tìm thấy mô-đun.

Hãy cài đặt gói matplotlib.

Để cài đặt các gói, hãy đi tới phía trên bên phải sổ ghi chép của bạn và nhấp vào các gói.

Trong menu thả xuống bật lên, hãy để lựa chọn ở các gói anaconda.

Chỉ sử dụng các gói theo giai đoạn nếu bạn cần cài đặt thủ công thứ gì đó thay vì sử dụng pip hoặc conda.

Trong thanh tìm kiếm, tìm kiếm gói bạn muốn cài đặt, matplotlib.

Khi tìm thấy gói, nó sẽ hiển thị trong danh sách những thứ sẽ được cài đặt.

Chỉ cần nhấp vào lưu và bạn đã sẵn sàng.

Bây giờ hãy quay lại và chạy khối mã đó.

Được rồi, đã đến lúc lưu lại công việc của bạn.

Dòng mã này tạo một bảng mới trong Snowflake.

Trong suốt quá trình này, GenAI có thể giúp bạn.

Hỏi những chức năng nào có sẵn trong Cortex.

Viết và gỡ lỗi Python.

Phân tích và trích xuất dữ liệu từ các trường phức tạp.

Trực quan hóa kết quả đầu ra trong matplotlib hoặc Streamlib.

Và đề xuất xử lý lỗi hoặc thay thế mô hình.

Trong bài học này, bạn đã sử dụng GenAI để tạo mã, ghi điểm đánh giá bằng chức năng cảm tính Cortex,

sau đó hình dung kết quả bằng matplotlib.

Tiếp theo, bạn sẽ tiếp tục làm việc với GenAI để bổ sung thêm hình ảnh và khả năng tương tác cho ứng dụng Avalanche của mình.