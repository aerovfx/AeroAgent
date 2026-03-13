# 05 - Thuật toán chuyển màu thích ứng (AdaGrad)

---

- [Người hướng dẫn] Khi các mô hình trở nên sâu hơn và bộ dữ liệu lớn hơn,

những thách thức trong việc đào tạo những mô hình này một cách hiệu quả

và tăng lên một cách hiệu quả.

Lựa chọn thuật toán tối ưu hóa

quan trọng cho sự thành công của quá trình đào tạo

vì nó chi phối cách thức trọng số và độ lệch của một mô hình

được cập nhật trong mỗi lần lặp lại quá trình đào tạo

để giảm thiểu hàm mất mát.

Trong bối cảnh tối ưu hóa,

tốc độ học tập là một siêu tham số

kiểm soát kích thước của các bước và tối ưu hóa nó

hướng tới việc giảm thiểu sự mất mát hàm trong quá trình huấn luyện.

Nói cách khác, nó quyết định tốc độ

hoặc mạng lưới thần kinh cập nhật các tham số của nó một cách chậm rãi

để đáp ứng với lỗi ước tính

mỗi lần trọng số mô hình được cập nhật.

Tốc độ học tập quá cao có thể gây ra việc đào tạo

hội tụ quá nhanh đến một giải pháp dưới mức tối ưu

hoặc thậm chí phân kỳ.

Ngược lại, tỷ lệ học tập quá thấp

có thể làm cho quá trình đào tạo rất chậm,

có khả năng bị mắc kẹt ở các điểm tối thiểu hoặc tinh tế cục bộ.

Tìm tốc độ học tập phù hợp

là rất quan trọng để đào tạo hiệu quả và hiệu quả.

Các thuật toán tối ưu hóa truyền thống

giống như việc giảm độ dốc một cách châm biếm, sử dụng tốc độ học tập cố định,

điều này có thể khó khăn để điều chỉnh

và có thể không tối ưu trong suốt quá trình học tập.

Mặt khác, tối ưu hóa thích ứng

điều chỉnh tốc độ học tập một cách linh hoạt cho từng tham số

dựa trên lịch sử của gradient,

cho phép hội tụ hiệu quả hơn và nhanh hơn.

Có nhiều trình tối ưu hóa thích ứng

chúng ta có thể lựa chọn khi đào tạo một mô hình học sâu.

Hãy bắt đầu với AdaGrad,

viết tắt của thuật toán gradient thích ứng.

AdaGrad điều chỉnh tốc độ học tập

cho từng tham số riêng lẻ

bằng cách chia tỷ lệ nghịch đảo

đến căn bậc hai của tổng

của tất cả các gradient bình phương lịch sử cho tham số đó.

Điều này có nghĩa là các tham số

liên quan đến các tính năng thường xuyên xảy ra

nhận được các bản cập nhật nhỏ hơn,

trong khi những người có tính năng không thường xuyên nhận được các bản cập nhật lớn hơn.

Đặc tính này làm cho AdaGrad đặc biệt phù hợp

để xử lý dữ liệu thưa thớt

và các nhiệm vụ xử lý ngôn ngữ tự nhiên,

trong đó một số tính năng xảy ra ít thường xuyên hơn những tính năng khác.

Một trong những lợi ích chính của AdaGrad

là khả năng thích ứng với tốc độ học tập

cho từng tham số.

Điều này giúp loại bỏ nhu cầu điều chỉnh tốc độ học tập theo cách thủ công,

đó có thể là một quá trình tốn thời gian và đầy thử thách.

Bằng cách tự động điều chỉnh tốc độ học tập,

AdaGrad đơn giản hóa quá trình tối ưu hóa

và có thể dẫn đến sự hội tụ nhanh hơn.

Tỷ lệ học tập thích ứng của AdaGrad đặc biệt hiệu quả

khi xử lý dữ liệu thưa thớt.

Trong trường hợp một số tham số được cập nhật không thường xuyên,

AdaGrad bù đắp bằng cách tăng tỷ lệ học tập của họ.

Điều này đảm bảo rằng tất cả các tham số,

bất kể tần suất chúng được cập nhật,

đóng góp có ý nghĩa vào quá trình học tập.

Hơn nữa, AdaGrad tương đối đơn giản để thực hiện.

Thuật toán của nó được xây dựng dựa trên việc giảm độ dốc tiêu chuẩn

bằng cách kết hợp một sự điều chỉnh đơn giản

thông qua tỷ lệ học tập

dựa trên gradient bình phương tích lũy.

Sự đơn giản này làm cho nó dễ tiếp cận và dễ tích hợp

vào các khuôn khổ học máy hiện có.

Mặc dù có những ưu điểm,

AdaGrad có một số hạn chế đáng chú ý.

Một trong những vấn đề chính là tỷ lệ học tập suy giảm.

Vì AdaGrad tích lũy các gradient vuông

trên tất cả các lần lặp lại,

tổng trong mẫu số có thể trở nên rất lớn theo thời gian.

Điều này làm cho tỷ lệ học tập hiệu quả giảm xuống

và cuối cùng trở nên rất, rất nhỏ.

Khi điều này xảy ra,

thuật toán có thể ngừng đạt được tiến bộ có ý nghĩa

trước khi đạt cực tiểu của hàm mất mát.

Một hạn chế nữa là AdaGrad thiếu cơ chế

để thiết lập lại hoặc rèn luyện lại tốc độ học tập

một khi chúng đã mục nát.

Điều này có nghĩa là tỷ lệ học tập giảm dần

là một phần vốn có của thuật toán,

và không có phương pháp tích hợp nào để chống lại hiệu ứng này.

Kết quả là AdaGrad có thể hoạt động kém hơn trong các tình huống

nơi đòi hỏi phải học tập liên tục trong một thời gian dài.

Ngoài ra, AdaGrad yêu cầu lưu trữ một số ô vuông

độ dốc trong quá khứ cho từng tham số.

Đối với các mô hình có số lượng tham số lớn,

điều này có thể dẫn đến tăng mức tiêu thụ bộ nhớ,

đó có thể là một hạn chế

trong môi trường hạn chế về tài nguyên.