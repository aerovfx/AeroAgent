# 09 tải lên một loạt tập tin

---

Đôi khi bạn cần tải lên một lượng lớn tệp cùng một lúc.

Và tin tôi đi, lôi từng người một vào sẽ không giải quyết được đâu.

Trong video này, bạn sẽ tạo lại bảng đánh giá của khách hàng từ đầu.

Nhưng lần này, bạn thực hiện điều đó bằng cách kết hợp hơn 100 tài liệu Word vào một bảng duy nhất.

Bạn đã tải lên phiên bản CSV sạch của dữ liệu này trong video trước.

Nhưng bây giờ bạn sẽ xây dựng nó một cách khó khăn.

Trước khi bắt đầu tải tệp, hãy xem lại lý do tại sao việc dàn dựng lại quan trọng đến vậy.

Snowflake không tải tệp trực tiếp vào bảng.

Thay vào đó, trước tiên bạn tải chúng lên một thứ gọi là giai đoạn.

Hãy nhớ rằng, các giai đoạn giống như một vùng lưu giữ an toàn cho các tập tin của bạn.

Chúng giúp bạn xem trước và xác thực tệp trước khi nhập,

giữ cho nội dung tải lên của bạn được sắp xếp ngăn nắp và cho phép bạn sử dụng lại cùng một tệp trên nhiều quy trình công việc.

Tải tập tin lên một giai đoạn thay vì trực tiếp cũng an toàn hơn.

Nếu xảy ra sự cố trong quá trình tải lên, tệp của bạn sẽ không bị mất.

Nhưng tin tốt là bạn đã tạo được cơ sở dữ liệu,

lược đồ và giai đoạn trong video cuối cùng.

Bây giờ chúng ta sẽ sử dụng lại chúng.

Cơ sở dữ liệu của bạn là avalanche.db, lược đồ của bạn là avalanche.schema,

và sân khấu của bạn là avalanche.stage.

Đã đến lúc tải lên 100 tài liệu Word đó.

Từ kho lưu trữ GitHub của khóa học, hãy tải xuống tệp zip.

Sau đó giải nén nó cục bộ.

Sau khi giải nén cục bộ, bạn sẽ thấy 100 tệp docx trong một thư mục.

Để đưa chúng vào Snowflake,

từ trang chủ của trang Snow trên thanh bên trái, hãy nhấp vào Dữ liệu.

Điều hướng đến Cơ sở dữ liệu và nhấp vào avalanche.db của bạn.

Sau đó, chọn avalanche.schema của bạn.

Chọn Giai đoạn từ thanh bên.

Sau đó nhấp vào Giai đoạn và chọn avalanche.stage của bạn.

Nhấn nút tập tin cộng ở phía trên bên phải màn hình của bạn.

Kéo và thả hoặc duyệt đến bất cứ nơi nào bạn đã lưu trữ 100 tài liệu Word đã giải nén đó.

Chọn tất cả 100 tài liệu Word rồi nhấn Open.

Bạn sẽ thấy một cửa sổ có tên Tải lên tệp của bạn.

Bên dưới tiêu đề cửa sổ, bạn sẽ thấy một mô tả nhỏ nêu rõ

100 tệp đó sẽ được tải lên avalanche.stage của bạn.

Hãy chắc chắn rằng avalanche.db và avalanche.stage của bạn được chọn,

sau đó bấm vào Tải lên.

Mặc dù có 100 tệp nhưng việc này sẽ di chuyển khá nhanh trên Snowflake.

Hãy sử dụng sổ ghi chép Snowflake mới để kiểm tra xem mọi thứ có diễn ra như mong đợi hay không.

Từ trang Snow, trong thanh điều hướng bên trái,

mở một sổ ghi chép mới bằng cách nhấp vào Dự án, sau đó nhấp vào Sổ ghi chép.

Từ cửa sổ Notebooks, nhấp vào nút sổ tay cộng màu xanh sáng

ở phía trên bên phải của màn hình.

Đặt tên cho sổ ghi chép của bạn.

Chọn cơ sở dữ liệu và lược đồ tuyết lở của bạn.

Để tất cả các tùy chọn khác theo mặc định và nhấp vào Tạo.

Khi đã ở trong sổ ghi chép mới, hãy xóa hai ô mã phía dưới.

Ở cuối khối mã đầu tiên có chứa Nhận phiên hoạt động,

đó là kết nối của bạn với dữ liệu của bạn, hãy di chuột qua ô.

Bạn sẽ thấy một vài tùy chọn bật lên để tạo ô mới.

Chọn Plus SQL từ danh sách, sau đó dán câu lệnh SQL này.

Trên bàn phím của bạn, nhấn Shift-Enter để chạy.

Điều này sẽ trả về một danh sách tất cả các tập tin trong giai đoạn này.

Bạn có thể đếm tất cả các tệp đã tải lên bằng tay để xác nhận có 100.

Nhưng hãy làm điều này một cách dễ dàng.

Yêu cầu ứng dụng Genii giúp bạn viết lệnh SQL bằng lời nhắc như thế này.

Làm cách nào tôi có thể đếm số lượng tệp hiện được lưu trữ trong giai đoạn nội bộ của mình

được gọi là giai đoạn tuyết lở bên trong lược đồ tuyết lở

và cơ sở dữ liệu DB bị lở bằng SQL?

Nó sẽ trả lại cho bạn một cái gì đó như thế này.

Sao chép và dán mã đó vào khối mã SQL trong sổ ghi chép Bông tuyết của bạn và chạy nó.

Nếu bạn giống tôi và không xóa tệp customerreviews.csv

mà chúng tôi đã tải lên ở video trước, bạn sẽ nhận được số đếm là 101.

Sau khi xác minh các tệp đã được tải lên, bạn đã sẵn sàng chuyển sang bước tiếp theo,

phân tích cú pháp và kết hợp chúng thành một bảng cấu trúc duy nhất.

Hãy làm điều đó ngay bây giờ.

Công việc tuyệt vời.

Trong video này, bạn đã sử dụng lại cơ sở dữ liệu, lược đồ và giai đoạn mà bạn đã tạo trước đó,

đã tải xuống một loạt 100 tài liệu Word, tải chúng lên sân khấu Bông tuyết có tên của bạn,

và xác minh việc tải lên bằng SQL.

Bây giờ bạn đã thành thạo việc tải lên tệp hàng loạt trong Snowflake

và bạn hoàn toàn có thể kiểm tra bước hai trong kế hoạch xây dựng MVP của mình.

Bạn biết cách tải cả một tệp và một loạt tệp lớn hơn lên Snowflake.

Tiếp theo, bạn sẽ được thực hành thực hành với dữ liệu vận chuyển khi có tuyết lở.