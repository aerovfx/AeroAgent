# Chương 1. Tóm tắt Học tập tăng cường sâu trong thực tế, Phiên bản video đã được dịch

---

Bản tóm tắt. Học tăng cường là một lớp con của học máy.

Thuật toán RL học bằng cách tối đa hóa phần thưởng trong một số môi trường và chúng hữu ích khi có vấn đề liên quan đến việc đưa ra quyết định hoặc thực hiện hành động.

Về nguyên tắc, các thuật toán RL có thể sử dụng bất kỳ mô hình học thống kê nào, nhưng việc sử dụng mạng lưới thần kinh sâu ngày càng trở nên phổ biến và hiệu quả.

Tác nhân là trọng tâm của bất kỳ vấn đề RL nào. Đây là một phần của thuật toán RL xử lý đầu vào để xác định hành động nào cần thực hiện.

Trong cuốn sách này, chúng tôi chủ yếu tập trung vào các tác nhân được triển khai dưới dạng mạng lưới thần kinh sâu.

Môi trường là các điều kiện năng động tiềm tàng trong đó tác nhân hoạt động.

Tổng quát hơn, môi trường là bất kỳ quá trình nào tạo ra dữ liệu đầu vào cho tác nhân.

Ví dụ: chúng ta có thể có một đặc vụ lái máy bay trong trình mô phỏng chuyến bay nên trình mô phỏng sẽ là môi trường.

Trạng thái là ảnh chụp nhanh về môi trường mà tác nhân có quyền truy cập và sử dụng để đưa ra quyết định.

Môi trường thường là một tập hợp các điều kiện thay đổi liên tục, nhưng chúng ta có thể lấy mẫu từ môi trường và những mẫu này tại những thời điểm cụ thể là thông tin trạng thái của môi trường mà chúng ta cung cấp cho tác nhân.

Một hành động là một quyết định được thực hiện bởi một tác nhân tạo ra sự thay đổi trong môi trường của nó.

Di chuyển một phần ngực cụ thể là một hành động và việc nhấn bàn đạp ga trên ô tô cũng vậy.

Phần thưởng là tín hiệu tích cực hoặc tiêu cực được môi trường trao cho tác nhân sau khi tác nhân thực hiện một hành động.

Phần thưởng là tín hiệu học tập duy nhất mà tác nhân được trao.

Mục tiêu của thuật toán RL, tức là tác nhân, là tối đa hóa phần thưởng.

Đường dẫn chung cho thuật toán RL là một vòng lặp trong đó tác nhân nhận dữ liệu đầu vào, trạng thái của môi trường.

Tác nhân đánh giá dữ liệu đó và thực hiện hành động từ một tập hợp các hành động có thể có dựa trên trạng thái hiện tại của nó.

Hành động sẽ thay đổi môi trường và sau đó môi trường sẽ gửi tín hiệu khen thưởng và thông tin trạng thái mới cho tác nhân.

Sau đó, chu kỳ lặp lại.

Khi tác nhân được triển khai dưới dạng mạng nơ-ron sâu, mỗi lần lặp sẽ đánh giá hàm mất mát dựa trên tín hiệu khen thưởng và lan truyền ngược để cải thiện hiệu suất của tác nhân.