# 06 - Lập kế hoạch học tập

---

- [Giảng viên] Lập kế hoạch học tập

là một kỹ thuật được sử dụng trong học sâu

để điều chỉnh tốc độ học tập trong quá trình đào tạo

để cải thiện sự hội tụ và hiệu suất mô hình.

Tốc độ học tập là một trong những cài đặt quan trọng nhất

vì nó quyết định

cách mô hình điều chỉnh các tham số bên trong của nó,

trọng số và độ lệch cũng như phản hồi đối với lỗi.

Nếu tốc độ học tập quá cao,

mô hình có thể bỏ qua giải pháp tốt nhất

và không bao giờ hội tụ.

Nếu nó quá thấp, việc tập luyện sẽ trở nên chậm chạp

và có thể bị mắc kẹt trong những giải pháp kém tối ưu hơn.

Lập kế hoạch tốc độ học tập giải quyết vấn đề này

bằng cách tự động điều chỉnh tốc độ học tập theo thời gian

để việc tập luyện diễn ra nhanh chóng và hiệu quả hơn.

Khi bắt đầu đào tạo,

các mô hình thường được hưởng lợi từ tốc độ học tập cao hơn

vì nó cho phép điều chỉnh nhanh chóng

giúp người mẫu di chuyển

hướng tới một lĩnh vực chung tốt của giải pháp.

Khi quá trình đào tạo tiến triển,

tốc độ học tập giảm dần,

để mô hình có thể tinh chỉnh các thông số của nó

với những điều chỉnh nhỏ hơn,

giảm khả năng vượt quá giải pháp tốt nhất.

Có một số chiến lược để học với việc lập kế hoạch,

mỗi cái có những đặc điểm độc đáo riêng.

Phân rã bước làm giảm tốc độ học tập

bởi một hệ số cố định theo những khoảng thời gian đều đặn,

cung cấp một cách đơn giản

để tăng tốc quá trình đào tạo sớm đồng thời tinh chỉnh sau này.

Điều này giống như giảm âm lượng loa theo từng bước.

Nó hoạt động tốt cho các mô hình đào tạo

nơi tiến độ tự nhiên chậm lại sau một vài giai đoạn.

Tuy nhiên, những thay đổi đột ngột trong quá trình phân rã bước

đôi khi có thể làm mất ổn định quá trình đào tạo.

Với sự phân rã theo cấp số nhân,

thay vì thực hiện những thay đổi đột ngột,

tốc độ học tập giảm dần theo thời gian

theo một đường cong.

Hãy nghĩ về nó như việc nhẹ nhàng nới lỏng bàn đạp ga trong ô tô

thay vì đạp phanh.

Nó tránh được những thay đổi nhất định trong tốc độ học tập,

nhưng đòi hỏi phải điều chỉnh cẩn thận tốc độ phân rã.

Một phương pháp phổ biến khác là ủ cosin,

sử dụng hàm cosin

để giảm tốc độ học tập một cách suôn sẻ theo thời gian,

thường xuyên đặt lại định kỳ để khuyến khích khám phá

của cảnh quan đã mất.

Ủ cosine có thể được so sánh

để làm mờ ánh sáng trong phòng bằng công tắc điều chỉnh độ sáng.

Lúc đầu, độ sáng giảm dần và mượt mà,

tạo ra một sự chuyển tiếp êm dịu.

Đặt lại định kỳ giống như trong giây lát

đèn lại sáng lên

để kiểm tra căn phòng trước khi giảm độ sáng của chúng một lần nữa.

Nó đặc biệt hữu ích cho các nhiệm vụ

nơi tiến bộ có thể bị đình trệ

và khởi động lại với tốc độ học tập cao hơn một chút

đôi khi có thể giúp mô hình tìm ra giải pháp tốt hơn.

Trong khi hiệu quả,

ủ cosine đòi hỏi kiến thức trước

tổng thời gian đào tạo để lập kế hoạch cho mình.

Thay vì luôn giảm tốc độ học tập,

phương pháp tiếp cận chu kỳ tốc độ học tập theo chu kỳ

chu kỳ tốc độ học tập lên xuống

giữa giá trị tối thiểu và tối đa.

Tỷ lệ học tập theo chu kỳ có thể được so sánh với việc đi xe đạp

lên xuống một loạt các ngọn đồi và thung lũng.

Khi bạn đến gần một con dốc nghiêng,

tương tự như những vùng khó khăn của cảnh quan bị mất,

bạn đạp mạnh hơn với nỗ lực nhiều hơn để vượt qua.

Khi bạn lên tới đỉnh và bắt đầu lao xuống dốc,

tương tự với các vùng dễ dàng hơn,

bạn giảm bớt và giảm tốc độ để lấy lại quyền kiểm soát.

Sự điều chỉnh kỹ thuật này

giúp cân bằng việc khám phá và sàng lọc,

đảm bảo tiến độ ổn định

mà không bị mắc kẹt hoặc vượt quá giới hạn.

Việc sử dụng tỷ lệ học tập theo chu kỳ

giúp mô hình thoát khỏi khu vực nơi tiến độ bị đình trệ,

đặc biệt là trong các vấn đề

nơi mà giải pháp không phải là một con đường thẳng tắp,

nhưng bao gồm rất nhiều đỉnh và thung lũng.

Tuy nhiên, nó giới thiệu các siêu tham số bổ sung

chẳng hạn như độ dài và biên độ chu kỳ,

có thể làm phức tạp việc điều chỉnh.

Lập kế hoạch tốc độ học tập thích ứng

là một cách tiếp cận dựa trên hiệu suất,

nơi tốc độ học tập được điều chỉnh

dựa trên cách mô hình đang hoạt động.

Ví dụ: nếu hiệu suất của mô hình

về dữ liệu xác nhận không cải thiện

sau một số kỷ nguyên nhất định,

tốc độ học tập được tự động điều chỉnh.

Lập kế hoạch tốc độ học tập thích ứng

giống như lái một chiếc ô tô có hộp số tự động.

Khi bạn lái xe, ô tô sẽ điều chỉnh bánh răng

dựa trên địa hình và tốc độ.

Nó chuyển sang số thấp hơn khi leo dốc

và số cao hơn để có đường bằng phẳng.

Sử dụng lịch trình tỷ lệ học tập thích ứng

tránh lãng phí thời gian

khi tốc độ học tập hiện tại không còn hiệu quả.

Tuy nhiên, nó có thể kéo dài thời gian tập luyện

nếu tham số kiên nhẫn không được điều chỉnh tốt.