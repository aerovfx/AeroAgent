# 06 - Tuyên truyền bình phương trung bình gốc (RMSProp)

---

- [Người hướng dẫn] RMSProp, viết tắt của

cho sự lan truyền bình phương trung bình gốc,

được phát triển để giải quyết

vấn đề tỷ lệ học tập giảm dần được quan sát thấy trong AdaGrad.

Nó sửa đổi AdaGrad

bằng cách đưa ra một mức trung bình phân rã theo cấp số nhân,

hoặc đường trung bình động của gradient bình phương.

Thay vì tích lũy tất cả các gradient bình phương trong quá khứ,

RMSProp duy trì mức trung bình đang hoạt động và giảm dần theo thời gian.

Điều này cho phép thuật toán quên đi các gradient cũ hơn

và tập trung vào những cái gần đây hơn.

Một trong những lợi ích đáng kể của RMSProp là khả năng

để duy trì tốc độ học tập thích ứng mà không gặp vấn đề gì

về tốc độ học tập suy giảm quá nhanh.

Bằng cách sử dụng đường trung bình động hàm mũ,

RMSProp đảm bảo rằng gradient bình phương tích lũy

không phát triển vô thời hạn, ngăn cản tốc độ học tập

khỏi trở nên quá nhỏ bé.

RMSProp đặc biệt hiệu quả trong các mô hình đào tạo

về các mục tiêu không cố định, trong đó dữ liệu cơ bản

sự phân bố thay đổi theo thời gian.

Nó cũng xử lý tốt độ dốc nhiễu và thưa thớt,

làm cho nó phù hợp để đào tạo mạng lưới thần kinh tái phát

và các kiến trúc phức tạp khác.

Hơn nữa, RMSProp tương đối dễ thực hiện.

Nó được xây dựng dựa trên AdaGrad bằng cách thêm một sửa đổi đơn giản

đến cách tích lũy gradient bình phương.

Điều này làm cho nó trở thành một lựa chọn thiết thực cho những người đang tìm kiếm

để cải thiện những hạn chế của AdaGrad

mà không gây ra sự phức tạp đáng kể.

Mặc dù có những ưu điểm,

RMSProp giới thiệu các siêu tham số bổ sung,

chẳng hạn như tốc độ phân rã, cần được điều chỉnh cẩn thận.

Hiệu suất của RMSProp có thể nhạy cảm với sự lựa chọn

của các siêu tham số này và việc điều chỉnh không đúng cách có thể dẫn đến

đến kết quả dưới mức tối ưu hoặc các vấn đề về hội tụ.

Trong một số trường hợp, RMSProp có thể không hội tụ hoặc có thể hội tụ

đến một giải pháp dưới mức tối ưu, đặc biệt nếu các siêu tham số

không được lựa chọn tốt.

Đây có thể là một thách thức đối với những người thực hành

những người có thể không có thời gian hoặc nguồn lực

để thực hiện tối ưu hóa siêu tham số mở rộng.

Hơn nữa, RMSProp thiếu nền tảng lý thuyết vững chắc

so với một số trình tối ưu hóa khác.

Điều này có thể khiến việc dự đoán hành vi của nó trở nên khó khăn hơn

trong những tình huống nhất định và có thể đặt ra những thách thức khi cố gắng

để hiểu hoặc gỡ lỗi quá trình đào tạo.