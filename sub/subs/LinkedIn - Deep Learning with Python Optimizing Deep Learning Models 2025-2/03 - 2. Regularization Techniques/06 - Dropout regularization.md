# 06 - Chính quy bỏ học

---

- [Người hướng dẫn] Chính quy hóa bỏ học là một công cụ mạnh mẽ

và kỹ thuật được sử dụng rộng rãi trong học sâu được thiết kế

để ngăn chặn việc trang bị quá mức trong mạng lưới thần kinh.

Quá khớp xảy ra khi một mô hình học

không chỉ là các mẫu cơ bản thực sự trong dữ liệu huấn luyện,

mà còn cả tiếng ồn và những chi tiết không liên quan,

dẫn đến khả năng khái quát hóa kém trên dữ liệu chưa được nhìn thấy.

Chính quy bỏ học giúp giảm thiểu vấn đề này

bằng cách gây ra tiếng ồn trong quá trình huấn luyện,

buộc mô hình trở nên mạnh mẽ hơn

và có khả năng khái quát hóa dữ liệu mới.

Ý tưởng cơ bản là đơn giản nhưng hiệu quả.

Trong mỗi lần lặp lại huấn luyện,

một tập hợp con ngẫu nhiên của nơ-ron

trong một lớp nhất định tạm thời bị loại bỏ hoặc bị bỏ qua.

Những tế bào thần kinh bị khuyết tật này

không đóng góp cho giai đoạn tiếp theo,

hoặc giai đoạn lùi của quá trình lan truyền ngược.

Điều này có nghĩa là với mỗi lượt đào tạo,

các phần khác nhau của mạng bị vô hiệu hóa một cách ngẫu nhiên.

Dropout ngăn chặn hiệu quả việc trang bị quá mức

bằng cách giải quyết hai vấn đề chính.

Nếu không bỏ học, tế bào thần kinh có thể trở nên phụ thuộc nhiều

lẫn nhau, cùng nhau tìm hiểu các tính năng cụ thể,

và làm giảm độ bền của mô hình.

Việc chính quy hóa bỏ học ngăn chặn sự đồng thích ứng này

bằng cách loại bỏ ngẫu nhiên các tế bào thần kinh trong quá trình huấn luyện,

buộc mạng phải học các biểu diễn dư thừa

không dựa vào sự tương tác cụ thể giữa các tế bào thần kinh.

Điều này dẫn đến một mạng tổng quát hơn.

Thứ hai, bằng cách che giấu ngẫu nhiên các đầu ra nơ-ron,

bỏ học đưa tiếng ồn vào quá trình đào tạo.

Tiếng ồn này hoạt động như một bộ điều chỉnh,

ngăn chặn mạng trở nên quá tinh chỉnh

đến dữ liệu huấn luyện.

Việc chính quy hóa bỏ học mang lại một số lợi ích.

Bằng cách đảm bảo rằng không một nơron nào trở nên quá quan trọng,

chính quy bỏ học khuyến khích mạng

để phát triển nhiều tính năng độc lập.

Thứ hai, bỏ học rất dễ thực hiện

và không tốn kém về mặt tính toán,

làm cho nó trở thành một lựa chọn hấp dẫn

để chuẩn hóa mạng lưới thần kinh.

Cuối cùng, tình trạng bỏ học đã được hiển thị

để cải thiện việc khái quát hóa các loại khác nhau

của mạng lưới thần kinh, bao gồm cả mạng chuyển tiếp,

mạng lưới thần kinh tích chập,

và mạng lưới thần kinh tái phát.

Có một số hạn chế đối với việc chính quy hóa bỏ học.

Bỏ học có thể tăng thời gian đào tạo

bởi vì mỗi lần lặp lại sử dụng một giá trị nhỏ hơn,

phiên bản rút gọn ngẫu nhiên của mạng,

có thể cần nhiều kỷ nguyên hơn để hội tụ.

Trong một số kiến trúc nhất định,

chẳng hạn như các lớp chập được tối ưu hóa cao trong CNN,

bỏ học có thể kém hiệu quả hơn so với

đến các kỹ thuật chính quy hóa khác như chuẩn hóa hàng loạt.