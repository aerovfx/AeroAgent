# 01 - Chuẩn hóa hàng loạt

---

- [Người hướng dẫn] Trong học sâu,

khi các tham số mô hình được cập nhật trong quá trình đào tạo,

sự phân bố các giá trị đầu vào trong mỗi lớp

có thể thay đổi khi mô hình học hỏi.

Sự thay đổi này được gọi là sự thay đổi hiệp phương sai nội bộ

có thể làm chậm quá trình học tập

và làm cho nó trở nên khó khăn hơn.

Chuẩn hóa hàng loạt giải quyết điều này

bằng cách chuẩn hóa đầu vào cho mỗi lớp

để chúng có quy mô nhất quán

và phân phối trong quá trình đào tạo.

Quá trình chuẩn hóa hàng loạt hoạt động

trong ba bước chính.

Đầu tiên, nó tính giá trị trung bình và phương sai

của từng tính năng trong lô nhỏ.

Điều này cung cấp một ảnh chụp nhanh

về cách phân phối đầu vào cho lô đó.

Tiếp theo, nó chuẩn hóa các đầu vào để có giá trị trung bình bằng 0

và độ lệch chuẩn của một.

Điều này đảm bảo rằng đầu vào của lớp được chuẩn hóa,

làm cho mô hình dễ huấn luyện hơn.

Với một lô đầu vào B nhỏ, phương pháp chuẩn hóa

được biểu diễn bằng toán học như được hiển thị ở đây,

trong đó Xi hat là đầu vào được tiêu chuẩn hóa mới,

Xi là đầu vào ban đầu,

Thanh B là giá trị trung bình của lô nhỏ,

và sigma B là độ lệch chuẩn của lô nhỏ.

Bước thứ ba trong quá trình chuẩn hóa hàng loạt

là mở rộng quy mô và dịch chuyển các giá trị chuẩn hóa

sử dụng hai tham số có thể huấn luyện là gamma và beta.

Việc sử dụng các tham số này cho phép mô hình

để điều chỉnh các giá trị chuẩn hóa nếu cần thiết,

vì vậy nó vẫn có thể học được cách trình bày dữ liệu tốt nhất.

Về mặt toán học, quá trình chia tỷ lệ và dịch chuyển

được thể hiện như ở đây,

trong đó Yi là đầu vào được chia tỷ lệ và dịch chuyển,

gamma là một tham số chia tỷ lệ,

mũ yxi là đầu vào được chuẩn hóa,

và beta là tham số dịch chuyển.

Ưu điểm của việc chuẩn hóa hàng loạt là rất đáng kể.

Nó tăng tốc đào tạo bằng cách ổn định quá trình học tập,

cho phép sử dụng tỷ lệ học tập cao hơn,

và giảm độ nhạy đối với việc khởi tạo trọng số.

Nó cũng cải thiện tính tổng quát

bằng cách hoạt động như một hình thức chính quy hóa,

giảm nguy cơ trang bị quá mức.

Hơn nữa, chuẩn hóa hàng loạt

đơn giản hóa việc điều chỉnh siêu tham số

và hỗ trợ đào tạo mạng lưới sâu hơn

bằng cách giảm thiểu các vấn đề như biến mất

hoặc độ dốc bùng nổ.

Mặc dù lợi ích của nó,

chuẩn hóa hàng loạt có một số hạn chế.

Nó phụ thuộc rất nhiều vào kích thước lô nhỏ,

vì các lô nhỏ có thể không mang lại ước tính chính xác

của giá trị trung bình và phương sai,

dẫn đến hiệu suất bị suy giảm.

Ngoài ra, chi phí tính toán

từ các hoạt động bổ sung,

chẳng hạn như tính toán số liệu thống kê và chuẩn hóa đầu vào

có thể tăng nhẹ thời gian đào tạo.

Cuối cùng, chuẩn hóa hàng loạt ít hiệu quả hơn đối với các tác vụ

trong đó kích thước lô nhỏ

hoặc cho các kiến trúc lặp lại với các chuỗi dài.