# 01 - Sự đánh đổi độ lệch-phương sai

---

- [Người hướng dẫn] Sự cân bằng độ lệch-phương sai

là một khái niệm quan trọng trong học máy

mô tả sự cân bằng giữa hai loại lỗi

một mô hình có thể thực hiện trong khi học từ dữ liệu,

sai lệch và phương sai.

Sự thiên vị đề cập đến những lỗi gây ra

bởi những giả định quá đơn giản về dữ liệu.

Khi một mô hình có độ chệch cao, nó sẽ gặp khó khăn trong việc nắm bắt

sự phức tạp cơ bản của dữ liệu,

dẫn đến hiệu suất kém

trên cả tập huấn luyện và tập kiểm tra,

một tình huống được gọi là thiếu trang bị.

Ví dụ, sử dụng mô hình hồi quy tuyến tính

trên dữ liệu phi tuyến tính dẫn đến độ lệch cao

bởi vì mô hình tuyến tính đơn giản hóa quá mức mối quan hệ,

thiếu các mẫu quan trọng

và đưa ra những dự đoán không chính xác.

Ngược lại, phương sai đề cập đến những lỗi gây ra

bởi một người mẫu quá nhạy cảm

đến các chi tiết của dữ liệu huấn luyện.

Một mô hình có phương sai cao nắm bắt cả hai mẫu thực

và tiếng ồn, dẫn đến hiệu suất tuyệt vời

trên tập huấn luyện nhưng khả năng khái quát hóa kém đối với dữ liệu mới.

Điều này được gọi là trang bị quá mức.

Ví dụ: giả sử dữ liệu của chúng tôi được chia

vào các tập huấn luyện và kiểm tra như được hiển thị ở đây.

Một mô hình hồi quy đa thức rất phức tạp

có thể phù hợp hoàn hảo với dữ liệu huấn luyện,

nhưng không đưa ra dự đoán chính xác về dữ liệu thử nghiệm

vì nó quá phù hợp với đặc thù của tập huấn luyện.

Bản chất của sự thiên vị đánh đổi khác nhau

nằm ở việc tìm kiếm sự cân bằng phù hợp

giữa độ phức tạp của mô hình

và khả năng khái quát hóa tốt.

Một mô hình cân bằng tốt là đủ phức tạp

để nắm bắt các mẫu có ý nghĩa trong dữ liệu

mà không quá nhạy cảm với tiếng ồn.

Để giải quyết phương sai cao, chúng ta có thể sử dụng một số kỹ thuật

để giảm độ nhạy của mô hình với nhiễu

và cải thiện tính tổng quát.

Một cách tiếp cận là đơn giản hóa mô hình

bằng cách giảm độ phức tạp của nó, đảm bảo nó tập trung vào việc nắm bắt

các mẫu thiết yếu trong dữ liệu

thay vì trang bị quá nhiều đến những chi tiết nhỏ.

Một phương pháp phổ biến khác là áp dụng

của các kỹ thuật chính quy hóa như hình phạt L1 hoặc L2,

thêm các ràng buộc vào các tham số của mô hình,

không khuyến khích những cách trình bày quá phức tạp.

Sử dụng các lớp bỏ học cũng đặc biệt hiệu quả

vì họ tạo ra tiếng ồn trong quá trình luyện tập

bằng cách tạm thời vô hiệu hóa các tế bào thần kinh ngẫu nhiên,

ngăn chặn mô hình trở nên quá phụ thuộc

trên những con đường cụ thể

và khuyến khích sự hiểu biết tổng quát hơn

của dữ liệu.

Mặt khác, việc giải quyết sự thiên vị cao đòi hỏi các chiến lược

làm tăng khả năng học hỏi từ dữ liệu của mô hình.

Điều chỉnh các siêu tham số chính như tốc độ học tập,

kích thước lô hoặc độ sâu mô hình có thể cho phép mô hình

để nắm bắt tốt hơn các mô hình cơ bản.

Lựa chọn kiến trúc nâng cao hơn

như mạng lưới thần kinh tích chập cũng có thể có ích,

đặc biệt khi làm việc với dữ liệu phức tạp

nơi các mô hình đơn giản hơn bị thiếu hụt.

Ngoài ra, sử dụng trình tối ưu hóa thích hợp

có thể cải thiện đáng kể quá trình đào tạo,

cho phép mô hình hội tụ hiệu quả hơn

và tìm hiểu các mẫu phức tạp.

Bằng cách quản lý cẩn thận sự đánh đổi độ lệch-phương sai,

chúng ta có thể tạo ra các mô hình hoạt động tốt trong cả quá trình đào tạo

và dữ liệu chưa được nhìn thấy, tạo ra các mô hình mạnh mẽ và đáng tin cậy

thích hợp cho các ứng dụng trong thế giới thực.