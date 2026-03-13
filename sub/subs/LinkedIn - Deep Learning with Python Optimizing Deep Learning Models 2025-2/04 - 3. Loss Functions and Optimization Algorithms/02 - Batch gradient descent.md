# 02 - Giảm độ dốc hàng loạt

---

- [Người hướng dẫn] Trong học sâu,

Các thuật toán tối ưu hóa đóng vai trò cơ bản

về cách mạng lưới thần kinh được đào tạo.

Chúng chi phối cách thức trọng số và độ lệch của một mô hình

được cập nhật trong mỗi lần lặp lại quá trình đào tạo

để giảm thiểu hàm mất mát.

Bằng cách điều chỉnh lặp đi lặp lại các thông số

dựa trên độ dốc của hàm mất mát,

các thuật toán này nhằm mục đích tìm ra các giá trị tối ưu

mang lại những dự đoán tốt nhất.

Kairos cung cấp nhiều thuật toán tối ưu hóa khác nhau,

từ các phương pháp dựa trên gradient đơn giản

đến các phương pháp thích ứng tiên tiến hơn.

Mỗi phương pháp đều có điểm mạnh và hạn chế riêng,

và hiểu những khác biệt này

là điều cần thiết để lựa chọn phương pháp phù hợp.

Một trong những thuật toán tối ưu hóa cơ bản nhất

là độ dốc gốc hàng loạt.

Nó tính toán độ dốc của hàm mất

Sử dụng toàn bộ tập dữ liệu huấn luyện trong một lần duy nhất,

sau đó sử dụng gradient này để cập nhật các tham số của mô hình.

Hãy tưởng tượng con đường chạy xuống dốc.

Tính toán giảm độ dốc hàng loạt

con đường tốt nhất xuống đồi

bằng cách xem xét tất cả các tuyến đường có thể cùng một lúc.

Cách tiếp cận toàn diện này

đảm bảo rằng mỗi bản cập nhật sẽ di chuyển mô hình

tiến gần hơn đến giải pháp tối ưu

một cách ổn định và có thể dự đoán được.

Một trong những lợi ích đáng kể của việc giảm độ dốc hàng loạt

là sự ổn định của nó.

Vì nó sử dụng tất cả dữ liệu có sẵn,

việc cập nhật các tham số của mô hình là nhất quán,

và di chuyển đều đặn theo hướng giảm thiểu hàm tổn thất.

Điều này có nghĩa là sự hội tụ hướng tới tổn thất tối thiểu

diễn ra suôn sẻ và có thể dễ dàng theo dõi và dự đoán.

Một ưu điểm khác là tính chất quyết định của nó.

Với cùng một tập dữ liệu và điều kiện ban đầu,

giảm độ dốc hàng loạt sẽ tạo ra các bản cập nhật tương tự

mỗi khi bạn chạy nó.

Khả năng dự đoán này có thể có lợi

khi bạn cần kết quả có thể lặp lại,

chẳng hạn như trong nghiên cứu học thuật

hoặc khi xác minh tính nhất quán của một mô hình.

Hơn nữa, việc giảm độ dốc hàng loạt

rất đơn giản để thực hiện và hiểu.

Tính đơn giản về mặt thuật toán của nó

làm cho nó trở thành một điểm khởi đầu tuyệt vời

dành cho những người mới làm quen với kỹ thuật học sâu và tối ưu hóa.

Tuy nhiên, việc giảm độ dốc hàng loạt

không phải là không có những hạn chế của nó.

Một trong những nhược điểm cơ bản

là nó có thể đòi hỏi nhiều tính toán.

Xử lý toàn bộ tập dữ liệu trong mỗi lần lặp

đòi hỏi nguồn lực tính toán đáng kể,

đặc biệt là khi xử lý các tập dữ liệu lớn

phổ biến trong các ứng dụng thực tế.

Điều này có thể dẫn đến thời gian đào tạo dài hơn

có thể không thực tế trong các dự án nhạy cảm về thời gian.

Ngoài ra, yêu cầu tải toàn bộ tập dữ liệu

vào bộ nhớ cho mỗi lần cập nhật có thể có vấn đề.

Đối với các tập dữ liệu lớn,

điều này có thể vượt quá dung lượng bộ nhớ sẵn có,

dẫn đến hệ thống bị chậm hoặc bị treo.

Điều này đòi hỏi phải sử dụng

các tài nguyên tính toán hiệu năng cao,

mà có thể không phải ai cũng có thể truy cập được.

Một hạn chế khác là khả năng

bị mắc kẹt trong cực tiểu địa phương.

Trong các dịch vụ mất mát không lồi phức tạp,

điển hình của mô hình học sâu,

độ dốc giảm dần hàng loạt có thể hội tụ

đến một giải pháp dưới mức tối ưu.

Vì nó lấy độ dốc trung bình trên toàn bộ tập dữ liệu,

nó có thể không có tính linh hoạt

để thoát khỏi những cực tiểu cục bộ này

và tìm ra một cực tiểu toàn cục tốt hơn.