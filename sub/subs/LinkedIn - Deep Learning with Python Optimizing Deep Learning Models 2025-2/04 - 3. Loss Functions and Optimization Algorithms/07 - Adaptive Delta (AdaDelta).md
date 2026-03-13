# 07 - Đồng bằng thích ứng (AdaDelta)

---

- [Người hướng dẫn] Adaptive Delta, thường được gọi là AdaDelta,

giải quyết vấn đề tốc độ học tập giảm dần của AdaGrad

bằng cách hạn chế cửa sổ

độ dốc tích lũy trong quá khứ đến một kích thước cố định.

Thay vì tích lũy tất cả các gradient bình phương trong quá khứ,

AdaDelta sử dụng đường trung bình động của độ dốc,

tương tự như RMSprop, tuy nhiên, nó tiến thêm một bước

bằng cách điều chỉnh kích thước bước cập nhật,

một cách hiệu quả, loại bỏ sự cần thiết

cho một tỷ lệ học tập mặc định.

AdaDelta điều chỉnh tốc độ học tập

dựa trên cửa sổ chuyển động của các bản cập nhật độ dốc,

giải quyết vấn đề tỷ lệ học tập giảm dần

được quan sát trong AdaGrad.

Bằng cách tập trung vào độ dốc gần đây,

nó duy trì tốc độ học tập nhất quán trong suốt quá trình đào tạo,

tạo điều kiện cho sự hội tụ tốt hơn.

Ngoài ra, AdaDelta hoạt động tốt

về các vấn đề với độ dốc thưa thớt, tương tự như AdaGrad,

làm cho nó phù hợp cho các ứng dụng khác nhau

trong xử lý ngôn ngữ tự nhiên

trên các miền khác nơi mà sự thưa thớt dữ liệu là mối lo ngại.

Mặc dù AdaDelta giải quyết một số hạn chế của AdaGrad,

nó giới thiệu sự phức tạp bổ sung

đến thuật toán tối ưu hóa.

Tính toán của nó phức tạp hơn,

điều này có thể làm cho việc hiểu trở nên khó khăn hơn

và thực hiện đúng,

đặc biệt là đối với những người mới học sâu.

AdaDelta ít được sử dụng rộng rãi

so với các trình tối ưu hóa như Adam và RMSprop.

Kết quả là có thể có ít sự hỗ trợ của cộng đồng hơn,

ít hướng dẫn hơn và nghiên cứu thực nghiệm hạn chế

về hiệu suất của nó trên các loại vấn đề khác nhau.

Điều này có thể khiến việc tìm tài nguyên trở nên khó khăn hơn

khi khắc phục sự cố hoặc tối ưu hóa mô hình bằng AdaDelta.