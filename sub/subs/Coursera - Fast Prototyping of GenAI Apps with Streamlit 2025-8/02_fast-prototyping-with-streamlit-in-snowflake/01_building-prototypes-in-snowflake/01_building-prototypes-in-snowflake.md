# 01 mẫu tòa nhà trong bông tuyết

---

Trong mô-đun này, bạn sẽ lấy nguyên mẫu GenAI mà bạn đã xây dựng trong Mô-đun 1 và chuyển nó vào Snowflake.

Bạn sẽ sử dụng Snowflake làm nền tảng phát triển chính để có thể tạo nguyên mẫu một cách nhanh chóng

mà không phải lo lắng về việc di chuyển lượng lớn dữ liệu hoặc thiết lập cơ sở hạ tầng,

cho bạn nhiều thời gian hơn để tập trung vào việc tạo nguyên mẫu.

Trong mô-đun trước, bạn đã tạo kế hoạch xây dựng MVP cho nguyên mẫu ứng dụng bảng thông tin Avalanche trong môi trường cục bộ của mình.

Ứng dụng đó đã nhập tệp CSV chứa các bài đánh giá của khách hàng, thực hiện việc dọn dẹp và phân tích trầm tích trên dữ liệu,

trực quan hóa kết quả và sử dụng Streamlit để tạo giao diện người dùng nhanh có thể truy cập được trong trình duyệt web của bạn.

Trong thế giới thực, bạn sẽ hiếm khi có được một tập dữ liệu nhỏ và gọn gàng như Avalanche CustomerReviews.csv,

vì vậy mô-đun này sẽ chuyển mọi thứ sang Snowflake nơi bạn sẽ nhập một loạt tệp lớn hơn

và làm việc với cơ sở dữ liệu để có trải nghiệm thực tế hơn.

Trong mô-đun này, bạn sẽ tải một loạt tệp Word docx không có cấu trúc vào Snowflake.

Sử dụng bộ công cụ GNI nội bộ của Snowflake có tên là Cortex để phân tích hàng loạt tệp và biến chúng thành một bảng.

Và trong suốt phần còn lại của khóa học, bạn sẽ sử dụng ứng dụng GNI như ChatGBT hoặc Cloud

giúp bạn viết code và gỡ lỗi nhanh chóng.

Đến cuối mô-đun này, bạn sẽ có một ứng dụng GNI Streamlit hoạt động hoàn chỉnh chạy trên Snowflake.

Tôi sẽ gặp bạn trong video tiếp theo về chuyến tham quan có hướng dẫn về nền tảng Snowflake mà bạn sẽ sử dụng trong khóa học này.