# 04 - Giảm độ dốc hàng loạt nhỏ

---

- [Người trình bày] Giảm độ dốc hàng loạt nhỏ

nhằm mục đích kết hợp những lợi thế

của cả hai đợt giảm độ dốc

và giảm dần độ dốc ngẫu nhiên

bằng cách cập nhật các tham số mô hình

dựa trên độ dốc được tính toán

từ một loạt nhỏ các ví dụ huấn luyện.

Kích thước lô này thường lớn hơn kích thước lô SGD,

nhưng nhỏ hơn tổng số dữ liệu

như trong quá trình giảm độ dốc hàng loạt.

Hãy tưởng tượng điều này khi đang di chuyển xuống đồi

sử dụng thông tin từ một nhóm nhỏ các đường dẫn lân cận.

Cách tiếp cận này cho phép cả tốc độ của SGD

và sự ổn định của việc giảm độ dốc hàng loạt.

Một trong những lợi ích chính

giảm độ dốc hàng loạt nhỏ

là hiệu quả tính toán của nó.

Bằng cách xử lý hàng loạt dữ liệu,

nó tận dụng sức mạnh của vector hóa

và phần cứng được tối ưu hóa như GPU và TPU.

Điều này có thể tăng tốc đáng kể việc tính toán

so với việc xử lý các mẫu đơn lẻ như trong SGD.

Việc sử dụng nhiều đợt cho phép thuật toán

để sử dụng hiệu quả hệ thống phân cấp bộ nhớ

và khả năng xử lý song song,

giảm thời gian mỗi lần lặp.

Việc sử dụng một loạt mẫu cũng giúp giảm sự sai lệch

trong phần cập nhật tham số.

Điều này dẫn đến sự hội tụ ổn định hơn

hơn những gì thường thấy với SGD.

Các bản cập nhật ít ồn ào hơn

vì chúng dựa trên mức trung bình của nhiều mẫu,

làm dịu đi những biến động ngẫu nhiên.

Sự cân bằng này có thể dẫn đến sự hội tụ tổng thể nhanh hơn

so với cả hai đợt giảm độ dốc

và thuật toán giảm độ dốc ngẫu nhiên.

Giảm độ dốc hàng loạt nhỏ cũng mang lại sự linh hoạt

trong việc lựa chọn kích thước lô.

Điều này cho phép bạn điều chỉnh kích thước lô

dựa trên các tài nguyên tính toán có sẵn

và các yêu cầu cụ thể của vấn đề của bạn.

Các lô nhỏ hơn có thể được sử dụng khi bộ nhớ bị hạn chế,

trong khi lô lớn hơn

có thể khai thác nhiều sức mạnh tính toán hơn khi có sẵn.

Khả năng thích ứng này làm cho nhiều đợt giảm độ dốc

một công cụ linh hoạt trong bộ công cụ học sâu.

Tuy nhiên, việc chọn kích thước lô tối ưu có thể khó khăn.

và có thể yêu cầu thử nghiệm.

Nếu kích thước lô quá nhỏ,

các bản cập nhật có thể vẫn còn ồn ào

và dẫn đến sự hội tụ không ổn định tương tự như SGD.

Nếu nó quá lớn,

bạn có thể mất đi lợi ích tính toán

và đối mặt với những hạn chế về bộ nhớ

tương tự như việc giảm độ dốc hàng loạt.

Tìm được sự cân bằng phù hợp là rất quan trọng,

và có thể phụ thuộc vào các yếu tố như độ phức tạp của mô hình,

kích thước của tập dữ liệu,

và các chi tiết cụ thể của phần cứng đang được sử dụng.

Một hạn chế khác là kích thước lô lớn hơn

cần nhiều bộ nhớ hơn.

Điều này có thể trở thành một vấn đề

khi xử lý các tập dữ liệu rất lớn

hoặc khi làm việc với các mô hình

có số lượng tham số lớn.

Trong những trường hợp như vậy,

thậm chí giảm độ dốc hàng loạt nhỏ

có thể trở nên cần nhiều tài nguyên,

có khả năng cần phải sử dụng phần cứng chuyên dụng

hoặc tài nguyên điện toán đám mây.

Cuối cùng, việc giảm độ dốc theo lô nhỏ vẫn có thể hội tụ

đến giải pháp dưới mức tối ưu

nếu cỡ lô không được chọn phù hợp.

Nếu kích thước lô không nắm bắt đầy đủ

sự đa dạng của dữ liệu,

độ dốc được tính toán có thể không phản ánh chính xác

độ dốc thực sự của hàm mất mát,

ảnh hưởng đến sự hội tụ và hiệu suất mô hình cuối cùng.

Vấn đề này nhấn mạnh tầm quan trọng

xử lý trước dữ liệu cẩn thận

và chiến lược lựa chọn hàng loạt.