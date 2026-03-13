# 02 - Chính quy hóa Lasso và sườn núi

---

- [Người hướng dẫn] Chính quy hóa là một kỹ thuật quan trọng

được sử dụng để ngăn ngừa việc trang bị quá mức.

Một tình huống trong đó một mô hình học dữ liệu huấn luyện quá tốt,

bao gồm tiếng ồn và biến động nhỏ

không đại diện cho các mẫu thực sự.

Trang bị quá mức dẫn đến một mô hình

hoạt động tốt trên dữ liệu huấn luyện,

nhưng gặp khó khăn trong việc khái quát hóa một cách hiệu quả những dữ liệu chưa được nhìn thấy.

Để giải quyết vấn đề này,

Chính quy hóa L1 và L2 là hai phương pháp được sử dụng rộng rãi

thêm một hình phạt cho hàm mất trong quá trình đào tạo,

từ đó khuyến khích các mô hình đơn giản hơn

và giảm khả năng trang bị quá mức.

Chính quy hóa L1, còn được gọi là chính quy hóa Lasso,

sửa đổi hàm mất bằng cách thêm tổng

giá trị tuyệt đối của các trọng số như một điều kiện phạt.

Về mặt toán học, chính quy hóa L1

được thể hiện như thể hiện ở đây,

trong đó L đại diện cho hàm mất ban đầu,

lambda là một tham số chính quy

kiểm soát sức mạnh của hình phạt,

và wi là trọng số hoặc tham số của mô hình.

Bằng cách cộng các giá trị tuyệt đối của các trọng số,

Chính quy hóa L1 khuyến khích sự thưa thớt,

có nghĩa là nó đẩy một số trọng số về đúng 0.

Điều này loại bỏ các tính năng đó khỏi mô hình một cách hiệu quả,

dẫn đến những mô hình đơn giản hơn, dễ hiểu hơn,

nơi chỉ có những tính năng quan trọng nhất

góp phần đưa ra dự đoán cuối cùng.

Đặc điểm này làm cho việc chính quy hóa L1

đặc biệt có giá trị cho việc lựa chọn tính năng,

đặc biệt là khi xử lý dữ liệu nhiều chiều

trong đó nhiều tính năng có thể không liên quan.

Ví dụ, hãy xem xét một mô hình

được đào tạo trên tập dữ liệu với hàng ngàn tính năng

nơi chỉ có một tập hợp con

thực sự có ý nghĩa đối với nhiệm vụ hiện tại.

Áp dụng chính quy L1 giúp tự động chọn

những tính năng liên quan này bằng cách buộc những tính năng ít quan trọng hơn

có trọng lượng bằng 0,

đơn giản hóa mô hình và tăng cường khả năng diễn giải của nó.

Tuy nhiên, trong khi mô hình trở nên đơn giản hơn

và có khả năng ít bị trang bị quá mức,

nó cũng có thể loại trừ các tính năng

có thể đã đóng góp những thông tin nhỏ nhưng hữu ích.

Chính quy hóa L2, còn được gọi là chính quy hóa sườn núi,

sửa đổi hàm mất

bằng cách cộng tổng các giá trị bình phương

của trọng lượng như một thời hạn phạt.

Về mặt toán học, chính quy hóa L2

được thể hiện như ở đây.

Khác với L1,

Chính quy hóa L2 không đẩy trọng số về chính xác 0.

Thay vào đó, nó không khuyến khích giá trị trọng số lớn

bằng cách trừng phạt độ lớn bình phương,

dẫn đến nhỏ hơn

và trọng lượng được phân bổ đồng đều hơn trên mạng.

Loại hình phạt này làm giảm sự phụ thuộc của mô hình

trên bất kỳ tính năng nào,

thúc đẩy khái quát hóa

bằng cách làm cho mô hình trở nên chắc chắn hơn trước những biến đổi của dữ liệu.

Chính quy hóa L2 đặc biệt hiệu quả trong các tình huống

nơi tất cả các tính năng đầu vào được mong đợi

đóng góp một cách có ý nghĩa vào việc dự đoán

những gì cần được kiểm soát để ngăn chặn việc trang bị quá mức.

Ví dụ, trong mô hình học sâu

dùng để phân loại ảnh

nơi mỗi pixel có thể có tầm quan trọng nào đó,

Chính quy hóa L2 giúp cân bằng sự đóng góp

của từng tính năng bằng cách ngăn chặn một số trọng số

khỏi trở nên quá lớn.

Điều này giúp duy trì ranh giới quyết định suôn sẻ,

điều đó rất quan trọng để làm

dự đoán chính xác về dữ liệu mới.

Lựa chọn giữa chính quy hóa L1 và L2

phụ thuộc vào yêu cầu cụ thể của vấn đề.

Tóm lại, sử dụng chính quy L1

khi bạn mong đợi rằng chỉ một tập hợp con các tính năng có liên quan

và bạn cần lựa chọn tính năng

như một phần của quá trình đào tạo.

Sử dụng chính quy L2

khi bạn muốn kiểm soát trọng lượng và tránh trang bị quá mức

mà không loại bỏ bất kỳ tính năng nào khỏi việc xem xét.