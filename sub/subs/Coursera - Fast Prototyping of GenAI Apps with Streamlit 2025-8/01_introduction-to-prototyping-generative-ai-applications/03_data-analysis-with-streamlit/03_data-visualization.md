# 03 trực quan hóa dữ liệu

---

Được rồi, sau khi dữ liệu của bạn được dọn sạch, bước tiếp theo là giúp mọi người hiểu dữ liệu đó.

Chỉ cần in ra danh sách các số hoặc hàng có thể phù hợp để kiểm tra nhanh.

Nhưng đó không phải là lựa chọn tốt nhất để giúp các bên liên quan hình dung ra mục tiêu cuối cùng của bạn.

Đó là nơi hình dung xuất hiện.

Trong bài học này, bạn sẽ tìm hiểu cách thêm biểu đồ vào ứng dụng của mình

sử dụng bốn thư viện trực quan khác nhau.

Các chức năng biểu đồ tích hợp sẵn, Matplotlib, Plotly và Altair.

Mỗi người đều có thế mạnh riêng.

Và tùy thuộc vào loại biểu đồ bạn muốn xây dựng, bạn sẽ biết khi nào nên sử dụng loại biểu đồ nào.

Hãy bắt đầu đơn giản.

Cách dễ nhất để hiển thị biểu đồ trong Streamlit là sử dụng một trong các chức năng tích hợp sẵn của nó.

Ví dụ: bạn có thể sử dụng một dòng mã đó sẽ biến một cột điểm cảm tính

thành một biểu đồ thanh gọn gàng.

Và vâng, nó hoạt động trực tiếp với khung hoặc chuỗi dữ liệu gấu trúc.

Streamlit cũng có các tùy chọn biểu đồ sẵn sàng hoạt động này.

st.lineChart, st.areaChart, st.scatterChart.

Đây là những điều tuyệt vời để khám phá dữ liệu của bạn một cách nhanh chóng.

Chỉ cần chuyển khung dữ liệu vào và nó sẽ xử lý bố cục cũng như hiển thị cho bạn.

Bây giờ, nếu bạn muốn so sánh những thứ như cảm tính giữa các sản phẩm khác nhau, hãy thử cách này.

Dòng này sử dụng nhóm gấu trúc để chia nhỏ dữ liệu theo danh mục.

Vì vậy bạn có thể xây dựng các biểu đồ thể hiện tâm lý cho từng sản phẩm

chứ không phải là những đánh giá riêng lẻ.

Bây giờ chúng ta hãy xem điều này trong thực tế.

Tất cả những gì bạn cần làm là thêm ba dòng mã này vào ứng dụng

mà bạn đã xây dựng trong video trước để trực quan hóa cảm xúc trung bình trên mỗi sản phẩm.

Khi bạn chạy ứng dụng và nhập tập dữ liệu bằng cách nhấp vào nút,

bạn có thể thấy ngay biểu đồ của mình.

Được rồi, nếu bạn đã quen với Matplotlib thì sao?

Bạn hoàn toàn có thể sử dụng nó ở đây.

Điều này hoàn hảo cho biểu đồ, ô phân tán,

hoặc bất cứ điều gì mà bạn không cần nhiều tương tác.

Lưu ý rằng bạn đã sử dụng biến df bộ lọc ở đây.

Vì vậy, cốt truyện sẽ thay đổi khi bạn chọn thứ khác trong menu thả xuống.

Nếu bạn muốn tương tác như chú giải công cụ hoặc thu phóng,

Plotly là một sự lựa chọn vững chắc.

Biểu đồ vẽ có cảm giác hiện đại và mượt mà.

Người dùng có thể di chuột qua các điểm, phóng to hoặc nhấp để biết thêm chi tiết.

Và bạn không phải viết thêm bất kỳ mã giao diện người dùng nào.

Để viết biểu đồ Plotly, hãy sử dụng phần cuối cùng đó,

sử dụng chiều rộng vùng chứa bằng true.

Chỉ cần đảm bảo rằng biểu đồ trải dài để vừa với toàn bộ chiều rộng của ứng dụng.

Một lựa chọn tuyệt vời khác là Altair.

Altair hoạt động rất tốt với gấu trúc.

Và thật tuyệt vời đối với các ô xếp lớp hoặc bất kỳ thứ gì có các lựa chọn, chú giải công cụ hoặc bộ lọc.

Bạn có thể kết xuất nó với

Bây giờ, đây là bản tóm tắt nhanh về chức năng của từng công cụ.

Biểu đồ tích hợp không cần luồng có tốc độ siêu nhanh và hoàn hảo để phản hồi nhanh chóng.

Matplotlib đơn giản và cổ điển.

Tuyệt vời cho các lô tĩnh.

Plotly có tính tương tác, rất tốt cho việc khám phá dữ liệu.

Và Altair phù hợp cho những hình ảnh trực quan nâng cao hơn.

Bắt đầu với bất cứ điều gì dễ dàng nhất cho bạn và chỉ chuyển đổi công cụ khi bạn thực sự cần.

Chúng ta hãy xem qua một số ví dụ nhanh để bạn có thể thấy sự khác biệt.

Giả sử chúng ta muốn xây dựng một biểu đồ phân tán.

Đây là cách chúng tôi triển khai nó bằng Matplotlib, Plotly, Altair,

và cuối cùng là chức năng gốc Streamlit.

Mỗi công cụ này cho phép bạn tạo hình ảnh rõ ràng, hữu ích chỉ với một vài dòng mã.

Đây chỉ là một vài ví dụ, nhưng bạn có thể tìm hiểu thêm các kỹ thuật trực quan bằng cách

kiểm tra phần thành phần biểu đồ trong tài liệu Streamless.

Liên kết nằm ở cuối màn hình của bạn.

Hãy xem bạn đã tiến được bao xa trong việc tạo các hàm Python bằng GenAI

để xử lý dữ liệu thực với gấu trúc để tạo ra nhiều hình ảnh trực quan.

Bạn đang tận mắt chứng kiến cách GenAI thích ứng với bất kỳ công cụ nào bạn cần

và cách mọi thứ hoạt động với Streamlit.

Bạn đã xây dựng từng phần riêng lẻ.

Bây giờ là lúc kết hợp tất cả chúng lại thành một ứng dụng bảng điều khiển hoàn chỉnh

mà bạn sẽ xây dựng từ đầu bằng cách sử dụng GenAI làm đối tác mã hóa của mình.