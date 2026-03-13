# 06 lab-2-tuyết-tình cảm-phân tích-bảng điều khiển-với-genai

---

Để kết thúc bài học này, bạn sẽ kiểm tra tất cả các kỹ năng mới của mình

bằng cách xây dựng phiên bản ứng dụng bảng điều khiển Avalanche của riêng bạn bằng cách sử dụng mọi thứ bạn đã học được.

Đối với phòng thí nghiệm này, bạn sẽ tự mình xây dựng một ứng dụng bảng điều khiển Streamlit cho tập dữ liệu Avalanche.

Ứng dụng của bạn nên tải tập dữ liệu có gấu trúc,

phân tích cảm xúc của các đánh giá của khách hàng Avalanche bằng GenAI,

hiển thị tập dữ liệu trong khung dữ liệu,

sau đó hình dung kết quả phân tích tình cảm bằng biểu đồ thanh.

Bạn sẽ tìm thấy mọi thứ bạn cần trong thư mục M1/Lesson_03/Lab2 của kho lưu trữ github của khóa học.

Ở đó, bạn sẽ tìm thấy một tệp trống mà bạn có thể sử dụng để xây dựng phòng thí nghiệm này.

Ngoài ra còn có tệp giải pháp có giải pháp mã hoàn chỉnh.

Để giúp bạn thực hiện bài thí nghiệm này, chúng ta hãy xem một ví dụ về những gì bạn sẽ xây dựng.

Trong video này, tôi đang sử dụng Streamlit và các tính năng bạn đã học được trong mô-đun này.

Nhưng hãy thoải mái thêm ý tưởng của riêng bạn và sửa đổi ứng dụng theo ý thích của bạn.

Ứng dụng của bạn phải có ít nhất hai nút.

Một để tải tập dữ liệu đánh giá của khách hàng Avalanche,

và một để phân tích tình cảm.

Nút tải tập dữ liệu sẽ tải và hiển thị tập dữ liệu.

Nút phân tích cảm tính nên sử dụng mô hình GenAI

để xác định xem các đánh giá là tích cực, trung lập hay tiêu cực.

Hãy nhớ rằng không phải lúc nào bạn cũng nhận được câu trả lời giống nhau.

Một số mẫu GenAI, đặc biệt là những mẫu cũ hơn,

có thể cho kết quả bất ngờ hoặc không nhất quán.

Bởi vì phân tích tình cảm có thể mất một thời gian để xử lý,

Tôi khuyên bạn chỉ nên tải một vài hàng trong tập dữ liệu của mình để thử nghiệm

để giúp bạn đẩy nhanh quá trình.

Để tập hợp dữ liệu của bạn, bạn có thể sử dụng hàm pandas.head

để lưu 10 hoặc 20 hàng đầu tiên vào trạng thái phiên,

như bạn đã thấy trong các video trước.

Đừng quên lưu trữ kết quả

vì vậy bạn không tính toán lại chúng một cách không cần thiết.

Tiếp theo, tạo bộ lọc thả xuống cho phép người dùng chọn sản phẩm

và hiển thị dữ liệu đã lọc, giống như chúng tôi đã tạo trước đó.

Sau đó, hãy vẽ sơ đồ phân phối các đánh giá tích cực, trung lập và tiêu cực.

Bạn có thể sử dụng bất kỳ thư viện vẽ đồ thị nào

và thoải mái sáng tạo với màu sắc và thiết kế.

Cốt truyện hiển thị ở đây sử dụng Plotly với màu sắc tùy chỉnh,

nhưng hãy sử dụng trí tưởng tượng của bạn cho phần này.

Sau khi hoàn thành bài thực hành này, bạn sẽ hoàn thành Mô-đun 1

và có bảng điều khiển cảm tính được hỗ trợ bởi GenAI đầy đủ chức năng

sử dụng một tập dữ liệu trong thế giới thực,

phân loại tình cảm bằng OpenAI,

trực quan hóa kết quả,

hỗ trợ lọc tương tác.

Bây giờ bạn đã đặt nền móng,

bạn đã sẵn sàng nâng cao kỹ năng của mình hơn nữa

bằng cách tích hợp trợ lý dữ liệu GenAI vào ứng dụng của bạn trên Snowflake.

Hẹn gặp bạn ở đó!