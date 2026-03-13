# Chương 5. Tóm tắt Học tập tăng cường sâu trong thực tế, Phiên bản video đã được dịch

---

Bản tóm tắt.

Q-learning học cách dự đoán phần thưởng giảm giá theo trạng thái và hành động.

Các phương pháp chính sách tìm hiểu phân phối xác suất đối với các hành động trong một trạng thái.

Các mô hình diễn viên-phê bình kết hợp người học Q với người học chính sách.

Nhà phê bình-tác nhân lợi thế học cách tính toán lợi thế bằng cách so sánh giá trị mong đợi của một hành động với phần thưởng thực sự được quan sát thấy.

Vì vậy, nếu một hành động được cho là sẽ dẫn đến phần thưởng trừ một nhưng thực tế lại dẫn đến phần thưởng cộng mười,

lợi thế của nó sẽ cao hơn một hành động được kỳ vọng sẽ mang lại kết quả cộng chín và thực sự mang lại kết quả cộng mười.

Đa xử lý đang chạy mã trên nhiều bộ xử lý khác nhau có thể hoạt động đồng thời và độc lập.

Đa luồng cũng giống như đa nhiệm.

Nó cho phép bạn chạy nhiều tác vụ nhanh hơn bằng cách cho phép hệ điều hành nhanh chóng chuyển đổi giữa chúng.

Khi một tác vụ ở trạng thái rảnh, có thể đang chờ tệp tải xuống, hệ điều hành có thể tiếp tục thực hiện tác vụ khác.

Đào tạo phân tán hoạt động bằng cách chạy đồng thời nhiều phiên bản của môi trường và một phiên bản dùng chung duy nhất của mô hình DRL.

Sau mỗi bước thời gian, chúng tôi tính toán tổn thất cho từng mô hình riêng lẻ, thu thập độ dốc cho từng bản sao của mô hình,

sau đó tính tổng hoặc tính trung bình chúng lại với nhau để cập nhật các tham số được chia sẻ.

Điều này cho phép chúng tôi thực hiện đào tạo theo đợt nhỏ mà không cần bộ đệm phát lại kinh nghiệm.

Quá trình học tập cuối cùng nằm giữa học tập trực tuyến hoàn toàn, đào tạo từng bước một và học tập hoàn toàn ở Monte Carlo, chỉ đào tạo khi kết thúc một tập.

Do đó, học tập cuối bước có những ưu điểm của cả hai, hiệu quả của học một bước và tính chính xác của Monte Carlo.