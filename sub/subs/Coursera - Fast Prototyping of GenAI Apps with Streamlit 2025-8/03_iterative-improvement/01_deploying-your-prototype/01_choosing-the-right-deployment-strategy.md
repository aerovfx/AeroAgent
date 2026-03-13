# 01 lựa chọn chiến lược triển khai phù hợp

---

Trong video này, bạn sẽ tìm hiểu cách chọn chiến lược triển khai phù hợp cho ứng dụng Streamlit của mình.

Điều quan trọng là hiểu khán giả của bạn.

Bạn đang xây dựng cho đồng đội nội bộ, đối tác bên ngoài hay công chúng?

Sau khi biết ai sẽ sử dụng ứng dụng của mình, bạn có thể chọn tùy chọn triển khai

mang đến cho bạn sự cân bằng phù hợp về khả năng truy cập, bảo mật và hiệu suất.

Đến cuối video này, bạn sẽ biết tùy chọn triển khai nào phù hợp với nhu cầu của khán giả.

Xin chúc mừng, bạn đã hoàn thành hầu hết các bước trong kế hoạch xây dựng MVP trên Snowflake.

Bây giờ chỉ còn một bước cuối cùng là triển khai.

Điều này có nghĩa là đưa ứng dụng của bạn đến nơi những người khác thực sự có thể sử dụng ứng dụng đó và cung cấp phản hồi cho bạn.

Khi xây dựng ứng dụng Streamlit bằng Snowflake, bạn có hai lựa chọn triển khai chính.

Tùy chọn 1, Đám mây cộng đồng Streamlit.

Bạn đã sử dụng điều này trong Mô-đun 1,

nhưng điều tuyệt vời hơn nữa là bạn có thể kết nối trực tiếp nó với Snowflake.

Sử dụng Streamlit Community Cloud khi bạn muốn chia sẻ công khai ứng dụng của mình.

Có thể bạn đang xây dựng một portfolio hoặc một trang demo.

Với Community Cloud, bạn có thể nhận được URL công khai mà bất kỳ ai cũng có thể truy cập.

Tùy chọn 2, Streamlit và Bông tuyết.

Sử dụng Streamlit và Snowflake khi ứng dụng của bạn cần ở chế độ riêng tư.

Điều này hoàn hảo khi bạn đang làm việc với dữ liệu nhạy cảm hoặc cần kiểm soát ai có thể truy cập ứng dụng của mình.

Khi bạn triển khai trên Snowflake, ứng dụng của bạn sẽ chạy an toàn trong tài khoản Snowflake của bạn,

cho phép bạn kiểm soát hoàn toàn quyền truy cập.

Có, có nhiều cách khác để triển khai ứng dụng Streamlit.

Ví dụ: Repl.it và Vercel là những công cụ tuyệt vời để tạo ứng dụng web miễn phí,

nhưng chúng tôi khuyên bạn nên gắn bó với Streamlit Community Cloud hoặc Streamlit và Snowflake để bảo mật và dễ sử dụng.

Trong Snowflake, bạn nhận được hỗ trợ riêng cho các ứng dụng Python,

và các tùy chọn bảo mật được xây dựng riêng cho việc tích hợp Snowflake.

Vì vậy, bạn có thể giữ dữ liệu nhạy cảm ở chế độ riêng tư và kiểm soát quyền truy cập bằng vai trò của người dùng.

Vì vậy, mặc dù có rất nhiều công cụ khác có thể thực hiện được điều này,

khi bạn xây dựng nguyên mẫu Gen AI kết nối với dữ liệu trực tiếp,

Bông tuyết và Đám mây Streamlit có ý nghĩa hơn.

Khi bạn triển khai ứng dụng của mình trên Đám mây cộng đồng Streamlit,

mã của bạn có thể được giữ ở chế độ riêng tư nhưng bản thân ứng dụng hoạt động hơi khác một chút.

Có một menu cài đặt ứng dụng nơi bạn có thể chọn xem ứng dụng của mình ở chế độ riêng tư hay công khai.

Bạn sẽ xem xét cả hai tùy chọn trong các video sắp tới.

Nhưng đây là điều quan trọng cần biết ngay bây giờ.

Bạn chỉ có thể có một ứng dụng riêng cho mỗi tài khoản,

vì vậy hãy lựa chọn cẩn thận nếu bạn đang đi theo con đường riêng.

Trong video này, bạn khám phá những cách khác nhau để triển khai ứng dụng Streamlit trên Snowflake.

Bạn tìm hiểu khi nào nên giữ ứng dụng của mình ở chế độ nội bộ và an toàn cũng như khi nào nên công khai.

Bây giờ bạn đã hiểu cảnh quan,

bạn có thể chọn tùy chọn phù hợp dựa trên đối tượng ứng dụng của mình và cách sử dụng ứng dụng đó.

Bây giờ bạn đã sẵn sàng tiếp tục và tập trung vào việc xây dựng một ứng dụng vừa mạnh mẽ vừa dễ chia sẻ.