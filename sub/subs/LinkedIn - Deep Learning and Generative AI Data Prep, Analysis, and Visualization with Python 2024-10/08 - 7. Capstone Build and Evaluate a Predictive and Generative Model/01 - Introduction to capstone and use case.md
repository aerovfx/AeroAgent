# 01 - Giới thiệu về capstone và ca sử dụng

---

- [Giảng viên] Chào mừng đến với Dự án Capstone.

Trong dự án Capstone này,

bạn sẽ áp dụng những kỹ năng và kiến thức bạn đã đạt được

trong suốt khóa học sang tập dữ liệu thế giới thực.

Dự án này sẽ đưa bạn qua

toàn bộ quá trình phân tích dữ liệu,

từ việc tải tập dữ liệu đến tiền xử lý,

và cuối cùng là xây dựng và đào tạo

một mô hình học máy.

Để thực hành bổ sung với dữ liệu văn bản,

có một dự án tùy chọn là tốt.

Capstone bao gồm hai trường hợp sử dụng mới

và hai bộ dữ liệu mới cho nhóm Viễn thông của chúng tôi.

Bằng cách tận dụng AI dự đoán

trên tập dữ liệu tiếp thị viễn thông,

công ty viễn thông có thể đưa ra quyết định dựa trên dữ liệu

để nâng cao hiệu quả tiếp thị của họ,

cải thiện sự tương tác của khách hàng,

và cuối cùng thúc đẩy doanh số bán hàng cao hơn.

Bằng cách tận dụng AI sáng tạo

trên tập dữ liệu phản hồi của khách hàng,

công ty viễn thông có thể đưa ra quyết định dựa trên dữ liệu

để tăng cường hỗ trợ khách hàng

bằng cách thực hiện phân tích tình cảm.

Mục tiêu dự đoán của chúng tôi là dự đoán doanh số kênh truyền thông.

Điều này giúp công ty ưu tiên những khách hàng có giá trị cao

và tối ưu hóa các chiến lược tiếp thị.

Bạn sẽ làm việc với tập dữ liệu bao gồm dữ liệu bán hàng,

hiệu suất kênh truyền thông,

và các số liệu viễn thông khác.

Mục đích là để phân tích dữ liệu này,

xử lý trước để đảm bảo chất lượng của nó

và xây dựng mô hình dự đoán

để cung cấp những hiểu biết sâu sắc và dự đoán

có thể giúp cải thiện các quyết định kinh doanh.

Đầu tiên, bạn tải và xuất tập dữ liệu.

Mục tiêu là thực hiện thăm dò ban đầu

hiểu cấu trúc và nội dung của nó.

Vì vậy, bạn sẽ tải tập dữ liệu bằng Pandas,

hiển thị một vài hàng đầu tiên của tập dữ liệu,

xem xét thông tin trên tập dữ liệu,

và kiểm tra các giá trị và kiểu dữ liệu còn thiếu của từng cột.

Trong phần tiền xử lý dữ liệu,

you will clean and pre-process the data

để chuẩn bị cho việc phân tích và mô hình hóa.

Vì vậy, bạn sẽ xử lý các giá trị còn thiếu

và mã hóa các biến phân loại

và bất kỳ dữ liệu lộn xộn nào khác mà bạn có thể gặp phải.

Tiếp theo, bạn thực hiện phân tích dữ liệu thăm dò.

Bạn có thể tạo trực quan hóa và xác định bất kỳ ngoại lệ nào

hoặc sự bất thường trong dữ liệu.

Sau khi EDA được hoàn thành,

bạn chạy mã để xây dựng và đào tạo mô hình dự đoán.

Khi mô hình đã hoàn thành quá trình huấn luyện,

bạn vẽ đồ thị trực quan.

Cuối cùng, bạn đánh giá hiệu suất của mô hình

sử dụng AI sáng tạo.

Điều này có nghĩa là sao chép và dán đồ thị

từ âm mưu của bạn thành bot trò chuyện AI.

Một bài tập tùy chọn là tạo Báo cáo Capstone.

Bạn có thể sử dụng báo cáo này làm mẫu của mình

cho nhu cầu xử lý trước dữ liệu và phân tích dữ liệu trong tương lai

khi bạn tiếp tục cuộc hành trình học tập của mình.

Mục tiêu AI tổng quát của chúng tôi

là để tạo ra xếp hạng cảm tính của khách hàng

từ một tập dữ liệu phản hồi của khách hàng không được gắn nhãn.

Bạn sẽ tải một tập dữ liệu nhỏ về phản hồi của khách hàng

và bạn sẽ thực hiện quá trình xử lý trước văn bản đơn giản,

và sau đó bạn sẽ đưa phản hồi vào BERT,

một mô hình ngôn ngữ lớn mang tính khái quát,

để tạo ra xếp hạng tình cảm.

Phân tích đánh giá, nhận xét và phản hồi của khách hàng

cho phép các doanh nghiệp đánh giá tình cảm tổng thể

hướng tới sản phẩm hoặc dịch vụ của họ.

Nhiệm vụ của bạn là tạo ra các hình ảnh trực quan

để đánh giá các phản hồi.

Bạn sẽ tạo đám mây Word, biểu đồ hình tròn và biểu đồ thanh.