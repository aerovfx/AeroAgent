# 03 trực quan hóa dữ liệu trong bông tuyết

---

Thay vì chỉ xem xét từng đánh giá hoặc hồ sơ vận chuyển,

bạn sẽ sử dụng AI để phân tích tình cảm trên quy mô lớn nhằm phát hiện xu hướng

điều đó sẽ không thể bắt được bằng tay.

Hình dung bảng chung này sẽ trở thành nền tảng cho nguyên mẫu Streamlit cuối cùng của bạn,

biến dữ liệu cảm tính thô thành thông tin chi tiết trực quan mà các nhóm thực sự có thể hành động.

Bạn vừa hoàn thành một cột mốc quan trọng.

Phân tích dữ liệu đã chính thức hoàn tất.

Đã đến lúc kiểm tra bước 4 trong kế hoạch xây dựng MVP của bạn

và chuyển sang bước 5, Khám phá dữ liệu trực quan.

Đây là nơi những hiểu biết sâu sắc của bạn chuyển đổi từ những con số thành những câu chuyện

mà các nhóm có thể dễ dàng hiểu và hành động.

Hãy bắt đầu mọi việc bằng cách yêu cầu GenAI giúp bạn suy nghĩ.

Một lời nhắc như,

Tôi có thể tạo loại biểu đồ nào từ đánh giá của khách hàng Avalanche và nhật ký vận chuyển?

Điều này có thể giúp bạn có được một số gợi ý như,

Thêm biểu đồ thanh về số lượng nhãn cảm tính.

Tạo biểu đồ đường về cảm tính trung bình theo thời gian.

Tạo một biểu đồ phân tán về thời gian vận chuyển so với cảm tính.

Hoặc có thể tạo biểu đồ thanh nhóm theo nhà cung cấp dịch vụ hoặc khu vực.

Để đơn giản hóa mọi nguyên mẫu, hãy chỉ chọn một hoặc hai mẫu để bắt đầu.

Mở một sổ ghi chép mới và khởi tạo phiên Snowflake của bạn.

Sau đó, sử dụng truy vấn này để lấy các bài đánh giá có điểm cảm tính.

Vì bạn đã hình dung được điểm số cảm tính bằng biểu đồ trong video trước,

lần này, chúng ta hãy chia nhỏ sản phẩm phụ về điểm số tình cảm.

Để nhận mã nhanh chóng, hãy hỏi GenAI,

Làm cách nào tôi có thể nhóm sản phẩm phụ của điểm số cảm tính?

Giờ đây, bạn có thể sử dụng mã để so sánh cảm nhận của khách hàng về các sản phẩm khác nhau.

Tiếp theo, hãy yêu cầu GenAI giúp bạn hình dung các mô hình vận chuyển và các điểm bất thường bằng cách sử dụng chuỗi thời gian.

Bạn sẽ nhận lại một cái gì đó như sau.

Bây giờ, thay vì tìm kiếm những điều bất thường theo cách lỗi thời,

hãy yêu cầu GenAI giúp bạn tìm hiểu sâu hơn bằng cách sử dụng lời nhắc như,

Làm cách nào tôi có thể xác định những ngày có khối lượng lô hàng thấp hoặc tăng đột biến?

Sau đó, bạn có thể sử dụng thông tin chi tiết đó để thêm nhiều biểu đồ hơn.

Ví dụ: cái này nhóm theo nhà cung cấp dịch vụ.

Giờ đây, bạn có thể tận dụng các đánh giá đã hợp nhất và dữ liệu vận chuyển

để xem liệu việc giao hàng có ảnh hưởng đến cảm nhận của khách hàng hay không.

Hãy nhắc GenAI tạo biểu đồ thanh hiển thị cảm tính trung bình theo trạng thái vận chuyển.

GenAI có thể đề xuất mã này để nhóm tập dữ liệu theo trạng thái vận chuyển bằng cách sử dụng cột muộn.

Sau đó tính điểm cảm tính trung bình cho mỗi nhóm để sắp xếp khung dữ liệu.

Các kết quả được vẽ bằng biểu đồ thanh ngang từ biểu đồ lib đó

hiển thị cảm tính trung bình theo trạng thái vận chuyển.

Điều này giúp bạn dễ dàng biết được điểm cảm tính bị ảnh hưởng như thế nào do việc giao hàng trễ.

Trong bài học này, bạn đã sử dụng GenAI để nhanh chóng động não và tạo ra các hình ảnh trực quan.

Tiếp theo, bạn sẽ kết hợp tất cả những gì bạn đã học được trong mô-đun này

thành một ứng dụng hợp lý mà bạn có thể chạy và triển khai bên trong Snowflake.