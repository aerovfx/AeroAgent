# 08 - Ước tính thời điểm thích ứng (Adam)

---

- [Giảng viên] ADAM, viết tắt

để ước tính động lượng thích ứng,

kết hợp các ý tưởng của RMSProp và động lượng.

Nó duy trì mức trung bình giảm dần theo cấp số nhân

của độ dốc trong quá khứ, được gọi là ước tính thời điểm đầu tiên,

và gradient bình phương, được gọi là ước tính thời điểm thứ hai.

Bằng cách đó, ADAM điều chỉnh

tốc độ học tập cho từng tham số

và kết hợp động lượng

để tăng tốc độ hội tụ và làm mịn

con đường tối ưu hóa.

Động lượng có thể được coi là thêm quán tính

đến quá trình tối ưu hóa.

Thay vì chỉ cập nhật

dựa trên độ dốc hiện tại,

nó cũng xem xét hướng

và tầm quan trọng của các bản cập nhật gần đây.

Điều này cho phép quá trình tối ưu hóa

để duy trì động lượng theo hướng

có độ dốc giảm nhất quán.

ADAM được thiết kế để mang lại hiệu quả cạnh tranh,

có ít yêu cầu về bộ nhớ,

và phù hợp với các vấn đề

với dữ liệu và tham số lớn.

Nó đã trở thành một trong những trình tối ưu hóa phổ biến nhất

trong học sâu nhờ hiệu suất mạnh mẽ của nó

trên một loạt các ứng dụng.

Trên thực tế, nó là một lựa chọn mặc định tốt cho hầu hết các vấn đề.

Một trong những lợi ích chính của ADAM,

đây là tốc độ học tập thích ứng kết hợp với động lượng.

Bằng cách xem xét cả hai điều đầu tiên

và khoảnh khắc thứ hai của độ dốc,

ADAM điều chỉnh tỷ lệ học tập

hiệu quả hơn và có thể hội tụ nhanh hơn

hơn các trình tối ưu hóa khác.

Điều này làm cho nó đặc biệt hữu ích

để đào tạo mạng lưới thần kinh sâu

và các mô hình có không gian tham số lớn.

ADAM thường yêu cầu ít điều chỉnh siêu tham số hơn,

so với RMSProp và AdaGrad.

Cài đặt mặc định cho siêu tham số của nó

nhìn chung hoạt động tốt trên nhiều vấn đề,

làm cho nó trở thành một lựa chọn thuận tiện hơn cho các học viên

ai có thể không có thời gian

hoặc tài nguyên để tối ưu hóa siêu tham số mở rộng.

Ngoài ra, ADAM còn phù hợp

để đào tạo mạng lưới thần kinh quy mô lớn

và xử lý các tập dữ liệu lớn.

Nó sử dụng hiệu quả các tài nguyên tính toán

và có thể xử lý

không gian tham số nhiều chiều một cách hiệu quả.

Khả năng hội tụ nhanh chóng của nó

và đã biến nó thành một trình tối ưu hóa tiêu chuẩn một cách hiệu quả

trong nhiều framework học sâu.

Mặc dù được sử dụng rộng rãi nhưng ADAM không phải không có những hạn chế.

Một trong những mối quan tâm là khả năng trang bị quá mức

do sự hội tụ nhanh của nó.

Nếu dừng sớm hoặc kỹ thuật chính quy hóa

không được áp dụng đúng cách,

mô hình có thể quá khớp với dữ liệu huấn luyện

và hoạt động kém trên dữ liệu không nhìn thấy được.

Điều này đòi hỏi phải theo dõi cẩn thận

của các số liệu xác nhận trong quá trình đào tạo.

Ngoài ra, ADAM yêu cầu bộ nhớ bổ sung để lưu trữ

ước tính khoảnh khắc thứ nhất và thứ hai

cho từng tham số.

Đối với các mô hình rất lớn,

điều này có thể dẫn đến tăng mức sử dụng bộ nhớ,

có thể là một hạn chế trong một số môi trường,

đặc biệt là khi sử dụng tài nguyên phần cứng hạn chế.