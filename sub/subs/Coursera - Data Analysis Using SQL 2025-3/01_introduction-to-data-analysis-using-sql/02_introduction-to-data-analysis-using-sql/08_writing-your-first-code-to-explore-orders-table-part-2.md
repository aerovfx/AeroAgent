# 08 viết-your-first-code-to-explorer-orders-table-part-2 đã dịch

---

Xin chào và chào mừng trở lại. Hãy tiếp tục từ nơi chúng ta đã dừng lại trong video trước.

Chúng tôi hiểu rõ nội dung trong bảng đơn đặt hàng.

Hãy tiếp tục và cố gắng lấy lại một số thông tin chi tiết.

Trong báo cáo vấn đề của mình, chúng tôi được thông báo rằng Foodhunter đang phải đối mặt với xu hướng giảm doanh thu.

Doanh thu được tạo thành từ hai thành phần, số lượng và giá cả.

Trong video này, chúng ta hãy tập trung phân tích số lượng, tức là số lượng đơn đặt hàng.

Hãy thử khám phá kịch bản đầu tiên và kiểm tra xem đơn đặt hàng có giảm qua các tháng hay không.

Vì vậy, hãy lấy số lượng đơn đặt hàng trong tập dữ liệu này.

Để hoàn thành thao tác này trong SQL, bạn chỉ cần sử dụng hàm COUNT.

Hàm COUNT là hàm tổng hợp.

Tương tự, còn có các hàm tổng hợp khác như MAX, MIN, SUM và AVERAGE.

Chúng hoạt động trên các cột giống như tên gợi ý.

Vì vậy, hãy sử dụng truy vấn.

Như bạn có thể thấy, đầu ra ở đây là 43.118.

Có nghĩa là có 43.118 đơn hàng trong toàn bộ cơ sở dữ liệu.

Nhưng đợi một chút, làm sao chúng ta biết rằng mỗi ID đơn hàng trong tập dữ liệu này là duy nhất?

Hãy xác nhận điều đó bằng cách sử dụng câu lệnh DISTINCT.

Câu lệnh DISTINCT cung cấp số lượng mục duy nhất trong một cột.

Đây là truy vấn SQL được cập nhật của bạn.

Bây giờ hãy thực hiện điều này.

Chúng tôi lại quan sát thấy số lượng đơn đặt hàng là 43.118.

Điều này xác nhận rằng số lượng ID đơn đặt hàng trong tập dữ liệu này là duy nhất.

Hãy kiểm tra việc sử dụng DISTINCT với các cột khác.

Ở đây, chúng ta hãy thử tìm xem có bao nhiêu tài xế đã được sử dụng để giao 43.118 đơn hàng này mà không sử dụng DISTINCT.

Và thấy sự khác biệt.

Vì vậy, đây là truy vấn được cập nhật của chúng tôi và hãy thực hiện nó ngay bây giờ.

Như bạn có thể thấy, chúng tôi nhận được kết quả đầu ra là 43.118.

Điều này chắc chắn không xảy ra vì Foodhunter không thể có nhiều tài xế như vậy cho 43.118 đơn hàng.

Vì vậy, chúng ta hãy xem xét điều gì sẽ xảy ra nếu từ khóa DISTINCT được sử dụng.

Như bạn có thể thấy hiện tại, có tổng cộng 250 tài xế đã giao 43.118 đơn hàng này cho ứng dụng Foodhunter.

Đây là mức thấp hơn một chút so với tiêu chuẩn ngành.

Chúng tôi sẽ ghi nhớ điều này khi thực hiện phân tích trong tương lai.

Nhưng đợi một chút. Cho đến nay, chúng tôi đã xem xét tổng số đơn đặt hàng.

Để thực sự xác minh việc giảm doanh thu hàng tháng, chúng ta sẽ cần xem xét số lượng đơn đặt hàng mỗi tháng và quan sát xu hướng.

Thật không may, chúng tôi không thể làm điều đó với kho tuyên bố của mình.

Để có được số lượng đơn hàng hàng tháng, chúng ta cần có câu lệnh VAR.

Vì vậy, hãy làm điều đó trong mô-đun tiếp theo.

Bây giờ, hãy chuyển sang bài tập để củng cố việc học của bạn từ mô-đun này.

Hãy thử truy xuất dữ liệu từ các bảng khác bằng cách chuyển đổi tiếng Anh đơn giản sang mã bằng cách sử dụng SELECT, FROM, COUNT và DISTINCT.

Tôi sẽ gặp bạn trong mô-đun tiếp theo, nơi chúng ta sẽ tiếp tục tìm hiểu thông tin chi tiết về Foodhunter.