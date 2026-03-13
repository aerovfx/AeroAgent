# 04 khả năng ghi nhật ký-giám sát và quan sát

---

Khi bạn biết bạn muốn thu thập số liệu nào về hệ thống RAG của mình,

bạn thực sự cần xây dựng hệ thống để thu thập dữ liệu đó.

Hãy xem xét các công cụ có sẵn để bạn triển khai hệ thống quan sát của mình.

Có nhiều nền tảng quan sát có sẵn cho các ứng dụng dựa trên LLM.

Chúng được thiết kế để thực hiện các nhiệm vụ đánh giá chung như thu thập số liệu ở cấp độ thành phần hoặc toàn hệ thống,

giúp ghi lại lưu lượng truy cập hệ thống và cho phép thử nghiệm các cài đặt hệ thống mới.

Sử dụng một nền tảng như thế này có nghĩa là bạn sẽ tốn ít thời gian hơn để thiết kế và triển khai hệ thống quan sát của mình,

và có nhiều thời gian hơn để theo dõi hiệu suất hệ thống RAG của bạn và thử nghiệm các cách để cải thiện nó.

Ví dụ: hãy xem nền tảng đánh giá và quan sát nguồn mở có tên Phoenix,

được xây dựng bởi công ty Arise.

Nó cung cấp một số công cụ giúp bạn đánh giá hiệu suất của hệ thống RAG.

Chúng ta hãy xem xét một số công cụ đó, bắt đầu với công cụ được sử dụng phổ biến nhất, dấu vết.

Dấu vết cho phép bạn đi theo đường dẫn của lời nhắc trong toàn bộ đường dẫn RAG,

xem nó được sửa đổi như thế nào bởi từng thành phần trong hệ thống.

Ví dụ: bạn có thể thấy lời nhắc văn bản ban đầu, truy vấn được gửi tới trình truy xuất của bạn,

những phần mà người truy tìm đã trả về, những phần đó được người xếp hạng lại của bạn xử lý như thế nào,

lời nhắc nào cuối cùng đã được gửi đến mô hình ngôn ngữ cốt lõi của bạn và phản hồi cuối cùng đã được tạo ra.

Thông tin hữu ích như độ trễ của từng bước cũng có thể được ghi lại.

Theo dõi dấu vết là công cụ phổ biến để đánh giá hệ thống RAG của bạn,

cho dù đó là nguyên mẫu ban đầu hay đã được sản xuất.

Ví dụ: nếu bạn biết rằng lời nhắc hoạt động kém trong hệ thống RAG của bạn,

bạn có thể theo dõi đường dẫn của nó và cố gắng xác định bước nào là nguồn gốc của lỗi.

Nền tảng Phoenix cũng giúp bạn dễ dàng thu thập nhiều đánh giá mà bạn đã thấy trong mô-đun này.

Ví dụ: nó tích hợp với thư viện RAGAS mà bạn đã sử dụng cho các số liệu đánh giá khác nhau.

Vì vậy, nếu bạn muốn tính toán mức độ liên quan khi tìm kiếm của chú chó săn mồi của mình,

hoặc liệu LLM của bạn có trích dẫn chính xác các nguồn được truy xuất hay không, thật dễ dàng để thêm các bước đánh giá đó.

Sau khi thiết lập quy trình đánh giá cơ bản, bạn có thể bắt đầu chạy các thử nghiệm đơn giản.

Ví dụ: bạn có thể thử lặp đi lặp lại các lời nhắc của riêng mình và xem chúng sẽ được xử lý như thế nào bởi quy trình RAG của bạn.

Bạn cũng có thể kiểm tra A-B các thay đổi đối với hệ thống của mình để xem chúng tác động như thế nào đến hiệu suất hệ thống.

Các tính năng như thế này giúp bạn quyết định xem lời nhắc hệ thống mới có thực sự cải thiện chất lượng phản hồi hay không,

hoặc xem bạn nhận được loại hiệu suất nào khi thêm người xếp hạng lại.

Trong khi việc theo dõi cho phép bạn tiếp cận thông tin cấp thấp,

bạn cũng thường muốn có số liệu thống kê tổng hợp cấp cao để theo dõi hiệu suất hệ thống.

Phoenix có thể cung cấp báo cáo hàng ngày về các số liệu chính từ độ chính xác của thiết bị thu hồi đến tỷ lệ ảo giác của mô hình của bạn.

Mặc dù Phoenix và các nền tảng quan sát LLM khác bao gồm hầu hết các đánh giá mà bạn muốn thu thập về hệ thống RAG của mình,

sẽ có một số khoảng trống.

Ví dụ: đây không phải là công cụ tuyệt vời để theo dõi việc sử dụng tính toán và bộ nhớ của cơ sở dữ liệu vectơ của bạn.

Trong những trường hợp này, bạn có thể sử dụng các công cụ giám sát và quan sát cổ điển hơn như Datadog và Grafana.

Một quy trình có khả năng quan sát tốt cuối cùng sẽ dẫn đến bánh đà cải tiến hệ thống.

Bằng cách xem cách hệ thống của bạn xử lý lưu lượng sản xuất thực tế, bạn có thể xác định các lỗi hoặc khu vực mục tiêu để cải thiện,

và sau đó xem tác động của những thay đổi bạn thực hiện.

Theo thời gian, điều này cho phép bạn điều chỉnh từng thành phần trên hệ thống của mình để phù hợp nhất với cách người dùng thực sự sử dụng nó.

Một công cụ có giá trị trong quá trình này là khả năng tạo tập dữ liệu tùy chỉnh về các lời nhắc mà hệ thống RAG của bạn đã xử lý trước đó.

Bằng cách lưu và sau đó chạy lại những lời nhắc này thông qua hệ thống của bạn,

bạn có thể thấy tác động của các thay đổi hệ thống đối với lời nhắc thực tế mà ứng dụng của bạn đã nhận được.

Vì vậy, hãy chuyển sang video tiếp theo và xem quá trình xây dựng một trong những tập dữ liệu tùy chỉnh đó trông như thế nào.