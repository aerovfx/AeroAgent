# 07 viết-your-first-code-to-explorer-orders-table-part-1 đã dịch

---

Xin chào và chào mừng trở lại. Trong video trước, chúng ta đã xem xét báo cáo vấn đề và sau đó tiến hành nhập cơ sở dữ liệu vào MySQL Workbench.

Tiếp theo, hãy khám phá các bảng khác nhau có trong cơ sở dữ liệu Food Hunter.

Đây là các bảng khác nhau có trong cơ sở dữ liệu Food Hunter.

Vì vậy, bạn có bàn dành cho khách hàng, đơn đặt hàng, mặt hàng thực phẩm, mặt hàng đặt hàng, nhà hàng và thậm chí cả tài xế.

Chúng ta hãy xem nhanh các cột khác nhau có trong các bảng này và chúng có liên quan với nhau như thế nào.

Vì vậy, đây là mối quan hệ và nó khá phức tạp.

Nhưng đừng lo lắng, khi chuyển sang các mô-đun sau, chúng ta sẽ hiểu lược đồ này tốt hơn.

Bây giờ, trước tiên hãy tập trung vào một bảng duy nhất, bảng đơn hàng.

Và điều này là do nó chứa nhiều mối quan hệ nhất với các bảng khác.

Như bạn có thể thấy, ở đây có nhiều cột như ID đơn hàng, ID khách hàng, địa chỉ giao hàng, giá cuối cùng, v.v.

Vì vậy, hãy nhanh chóng dành vài giây và xem tập dữ liệu trước khi chúng ta tiếp tục.

Chúng tôi đã được thông báo về sự sụt giảm doanh thu từ bánh bao.

Để xác nhận điều tương tự, bảng đơn hàng có tất cả các cột mà chúng tôi yêu cầu.

Để rút ra những hiểu biết sâu sắc này, hãy sử dụng SQL và khám phá bộ dữ liệu Food Hunter, cụ thể là bảng đơn hàng.

Và tôi hứa nó sẽ rất vui.

Vì tập dữ liệu của chúng tôi đã được nhập, bạn còn chờ gì nữa?

Hãy bắt đầu bằng việc viết nhóm truy vấn đầu tiên của bạn trên MySQL Workbench.

Nhưng trước khi bắt đầu, hãy để tôi chia sẻ một cái nhìn sâu sắc rất thú vị liên quan đến SQL.

Viết truy vấn SQL rất giống với viết tiếng Anh.

Vì vậy, trước tiên hãy để tôi chỉ cho bạn cách viết các truy vấn bằng tiếng Anh và sau đó ánh xạ chúng tới cách viết truy vấn bằng SQL.

Nếu bạn muốn xem tất cả dữ liệu có trong bảng đơn hàng trong cơ sở dữ liệu, bằng tiếng Anh, chúng ta sẽ nhập hiển thị tất cả dữ liệu trong bảng đơn hàng.

Mã mà bạn sử dụng trong SQL để truy xuất bất kỳ dữ liệu nào được gọi là truy vấn.

Câu lệnh trên không hoạt động trực tiếp trong không gian làm việc SQL, nhưng chỉ cần chỉnh sửa một chút, chúng ta có thể thu được truy vấn SQL tương đương.

Một câu lệnh SQL cơ bản nhất khác được sử dụng trong mọi truy vấn SQL là câu lệnh SELECT.

Tất cả các truy vấn SQL để lấy dữ liệu đều có câu lệnh SELECT.

Vì vậy, trong phần hiển thị tất cả dữ liệu trong bảng đơn hàng, hãy thay thế hiển thị bằng CHỌN.

Để xem toàn bộ dữ liệu chúng ta không thể sử dụng từ khóa ALL DATA. Thay vào đó, chúng tôi sử dụng dấu hoa thị để truy xuất tất cả dữ liệu trong bảng cụ thể đó.

Vì vậy, hãy tiếp tục và thay thế TẤT CẢ DỮ LIỆU bằng dấu hoa thị.

Tiếp theo, bảng chúng ta muốn lấy dữ liệu là bảng ORDERS.

Để làm điều này, chúng ta có thể sử dụng một từ khóa cơ bản khác TỪ.

Cũng giống như câu lệnh SELECT, tất cả các truy vấn SQL để lấy dữ liệu cũng phải đề cập đến từ khóa FROM.

Từ khóa FROM được sử dụng trước tên bảng là ORDER trong trường hợp của chúng tôi.

Vì vậy, hãy thay thế IN D ở đây bằng từ khóa FROM và sau đó theo sau nó là tên của bảng là ORDERS trong trường hợp của chúng ta.

Cuối cùng, cú pháp của SQL yêu cầu bạn thêm dấu chấm phẩy vào cuối truy vấn SQL.

Vì vậy, hãy xem mã SQL đã hoàn thành.

Bây giờ, hãy chọn dòng có mã của chúng tôi và nhấn CTRL cộng với ENTER để thực thi mã của bạn.

Bạn thấy việc viết mã bằng SQL đơn giản như thế nào không?

Như bạn có thể thấy, đầu ra truy vấn của bạn nằm trong lưới kết quả với tất cả các cột của bảng ORDERS.

Có rất nhiều cột trong bảng này và chúng ta có thể không thực sự cần tất cả các cột này để rút ra những hiểu biết sâu sắc.

Hãy xem cách chỉ chọn các cột cụ thể như ID ĐẶT HÀNG, THỜI GIAN GIAO HÀNG, GIÁ CUỐI CÙNG và ĐÁNH GIÁ ĐƠN HÀNG.

Trong tiếng Anh, chúng ta có thể sử dụng ORDER để chỉ chọn các cột trong bảng.

Trong tiếng Anh, chúng tôi sẽ nhập nó dưới dạng ID ĐẶT HÀNG HIỂN THỊ, THỜI GIAN GIAO HÀNG, GIÁ CUỐI CÙNG và XẾP HẠNG ĐƠN HÀNG trong bảng ĐƠN HÀNG.

Bằng cách thực hiện các chỉnh sửa nhỏ đối với câu lệnh viết bằng tiếng Anh này, chúng ta có thể truy xuất dữ liệu cần thiết bằng SQL.

Như chúng ta đã làm trước đó, hãy thay thế SHOW bằng từ khóa SELECT.

Tiếp theo, chỉ cần nhập tên của các cột bạn muốn truy xuất.

Tiếp theo, chỉ cần nhập tên của các cột bạn muốn truy xuất, đó là ID ĐẶT HÀNG, THỜI GIAN GIAO HÀNG, GIÁ CUỐI CÙNG và ĐẶT HÀNG, phân tách bằng dấu phẩy.

Một lần nữa, như chúng ta đã làm trước đó, chúng ta thêm từ khóa FROM theo sau là tên bảng là ORDERS trong trường hợp của chúng ta.

Và hãy nhớ thêm dấu chấm phẩy này vào cuối câu lệnh của bạn.

Vậy đây là mã SQL hoàn chỉnh của bạn. Bây giờ hãy chọn dòng này và thực hiện nó bằng CTRL-Enter.

Như bạn có thể thấy, chúng tôi chỉ truy xuất thành công các cột có thể cung cấp cho chúng tôi thông tin chi tiết hơn về doanh thu của Food Hunter.

Hãy cuộn xuống và xem dữ liệu trong bảng.

Nhưng đợi một chút, tại sao chúng ta chỉ có thể xem 1000 bản ghi đầu tiên từ tập dữ liệu của mình?

Điều này là do SQL theo mặc định chỉ hiển thị 1000 bản ghi đầu tiên trừ khi có quy định khác.

Điều này có thể được khắc phục bằng cách sử dụng một từ khóa quan trọng khác LIMIT.

Từ khóa LIMIT được sử dụng để chỉ định số lượng bản ghi cần trả về.

Hãy tiếp tục và đặt giới hạn của chúng tôi là 10.000 và xem kết quả đầu ra của chúng tôi trông như thế nào.

Hãy nhanh chóng quan sát dữ liệu để tìm thấy một số thông tin chi tiết.

Vì vậy, đây là đầu ra của mã đó và nếu bạn cuộn xuống, bạn sẽ thấy 10.000 bản ghi.

Một từ khóa quan trọng khác giúp chúng ta kiểm soát số lượng quan sát mà chúng ta thấy là OFFSET.

OFFSET quy định số lượng bản ghi được ghi lại.

Vì vậy, nếu bạn đã xem 10.000 bản ghi đầu tiên trong đoạn mã trên,

bây giờ bạn có thể xem 20.000 bản ghi tiếp theo bằng cách bỏ qua 10.000 bản ghi đầu tiên bằng cách sử dụng OFFSET.

Vì vậy, đây là truy vấn cập nhật của chúng tôi.

Chúng ta có thể thấy rằng 10.000 bản ghi đầu tiên đã được ghi lại.

Vì vậy, hãy tiếp tục và kiểm tra kết quả.

Vì vậy, đây là truy vấn được cập nhật của chúng tôi và hãy thực hiện nó ngay bây giờ.

Như bạn có thể thấy, SQL hiện đã bỏ qua 10.000 bản ghi đầu tiên và gửi các bản ghi bắt đầu từ số ID đơn hàng 1001.

Và điều này tiếp tục cho đến 30.000 từ MẪU ĐẶT HÀNG.

Chúng tôi có thể quan sát 20.000 bản ghi vì chúng tôi đặt giới hạn là 20.000.

Cho đến bây giờ, chúng tôi đã bảo hiểm rất nhiều. Chúng ta hãy nghỉ ngơi ở đây.

Chúng ta sẽ khám phá thêm trong video tiếp theo.