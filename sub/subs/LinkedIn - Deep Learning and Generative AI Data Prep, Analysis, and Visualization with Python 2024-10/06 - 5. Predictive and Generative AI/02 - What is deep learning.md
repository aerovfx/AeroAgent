# 02 - Học sâu là gì

---

- [Người hướng dẫn] Hãy tưởng tượng bạn đang học đi xe đạp.

Lúc đầu nó là thử thách

để giữ thăng bằng, lái và đạp cùng một lúc,

nhưng với thực hành, nó trở nên dễ dàng hơn.

Bộ não của bạn bắt đầu nhận ra các mẫu

và tạo kết nối

như biết phải xoay tay lái bao nhiêu khi nghiêng người.

Vâng, nguyên tắc tương tự cũng áp dụng cho việc học sâu.

Giống như bộ não của bạn được cải thiện khi đi xe đạp

bằng cách nhận ra các mẫu và tạo ra các kết nối,

mô hình học sâu nâng cao hiệu suất của họ

bằng cách điều chỉnh các kết nối này

để nhận dạng tốt hơn các mẫu trong dữ liệu.

Các mô hình học sâu được gọi là mạng lưới thần kinh

có cấu trúc giống như bộ não con người,

bao gồm các lớp nút được kết nối với nhau.

Lớp đầu vào là lớp đầu tiên của mạng nơ-ron

nơi dữ liệu đầu vào được đưa vào mạng.

Các lớp ẩn là các lớp ở giữa

nơi họ xử lý những thông tin đầu vào này

bằng cách áp dụng trọng số và hàm kích hoạt.

Lớp đầu ra tạo ra một dự đoán

dựa trên thông tin được xử lý từ lớp ẩn.

Tôi nói nhiều hơn về mạng lưới thần kinh

trong Nền tảng trí tuệ nhân tạo của tôi:

Khóa học Mạng lưới thần kinh.

Hình ảnh này minh họa một mô hình mạng lưới thần kinh đơn giản

được sử dụng để dự đoán doanh số bán hàng dựa trên các tính năng đầu vào khác nhau.

Trong ví dụ này, các tính năng đầu vào

là kỹ thuật số hoặc chi tiêu cho quảng cáo kỹ thuật số,

truyền hình, chi tiêu cho quảng cáo truyền hình,

báo chí, chi tiêu cho quảng cáo trên báo in,

và đài phát thanh, chi tiêu cho quảng cáo trên đài phát thanh.

Trong giai đoạn huấn luyện,

mạng lưới thần kinh điều chỉnh trọng số của các kết nối

giữa các nút để cải thiện dự đoán của nó.

Quá trình này xảy ra lặp đi lặp lại

cho đến khi có sự khác biệt giữa dự đoán

và giá trị doanh thu thực tế ở mức tối thiểu.

Đây là một ví dụ khác.

Các mô hình học sâu được đào tạo trên lượng dữ liệu khổng lồ,

như hình ảnh chó và mèo,

vì vậy họ học hỏi từ các ví dụ.

Bằng cách xem xét nhiều ví dụ,

người mẫu học cách nhận ra các khuôn mẫu và sự khác biệt

giữa hình ảnh con mèo và hình ảnh con chó,

hoặc thậm chí là hình ảnh một con chim.

Trong ví dụ này, mô hình có thể nhận ra một con mèo

khi được đưa ra hình ảnh của một con mèo.

Học sâu là một lĩnh vực con của học máy,

có thể xử lý các tập dữ liệu nhỏ hơn và các mô hình đơn giản hơn.

Học máy yêu cầu xử lý trước dữ liệu rộng rãi.

Điều này bao gồm việc xử lý các giá trị bị thiếu,

chuẩn hóa dữ liệu, mã hóa các biến phân loại,

và chia tỷ lệ tính năng.

Nó cũng yêu cầu chuẩn bị dữ liệu thủ công cẩn thận

để đảm bảo hiệu suất của mô hình.

Và mặc dù học sâu vẫn yêu cầu một số bước xử lý trước,

ví dụ: chuẩn hóa, thay đổi kích thước hình ảnh,

bản thân người mẫu đã tốt hơn

trong việc học các tính năng hữu ích từ dữ liệu thô.

Cấu trúc mô hình máy biến áp

là một ví dụ về mô hình có thể nhập dữ liệu thô.

Các mô hình máy biến áp thu thập dữ liệu trên web,

nhập các trang web, tài liệu, hình ảnh, v.v.

Và sau đó sử dụng lời nhắc,

bạn có thể cung cấp dữ liệu đầu vào của mô hình,

yêu cầu nó dịch một câu,

như được hiển thị ở đây,

và mô hình sẽ trả lời.

Mô hình bao gồm một bộ mã hóa,

mã hóa cụm từ tiếng Anh,

và một bộ giải mã, giải mã cụm từ

và dịch nó sang tiếng Tây Ban Nha.

Mình nói thêm về kiến trúc máy biến áp

trong Nền tảng trí tuệ nhân tạo của tôi:

Khóa học Mạng thần kinh

Các khung học sâu phổ biến bao gồm Keras,

cung cấp API cấp cao

để xây dựng mạng lưới thần kinh,

làm cho nó dễ dàng cho người mới bắt đầu và các nhà phát triển có kinh nghiệm.

Nổi tiếng với giao diện thân thiện với người dùng

và đồ thị tính toán động,

PyTorch vượt trội về tính linh hoạt và tạo mẫu nhanh.

TensorFlow phù hợp cho nhiều ứng dụng

và có tài liệu phong phú.

Và Caffe chủ yếu được sử dụng để xử lý hình ảnh và video.

Học sâu là một công cụ mạnh mẽ

cho phép máy học từ dữ liệu

và nhận ra các mẫu phức tạp,

làm cho nó trở thành một thành phần thiết yếu trong nhiều ứng dụng AI.