# 04 lặp lại-cải thiện-lặp lại-nhanh-phản hồi-cho-ứng dụng-tuyết lở của bạn

---

Chào mừng trở lại. Nguyên mẫu của bạn đang hoạt động, người dùng đang dùng thử và phản hồi đang dần được đưa vào.

Bây giờ thì sao? Hầu hết các nguyên mẫu thất bại không phải vì chúng bị hỏng mà vì người chế tạo không

biết cách biến phản hồi của người dùng thành những cải tiến có ý nghĩa. Họ hoặc bỏ qua phản hồi

hoàn toàn, hoặc họ cố gắng sửa chữa mọi thứ cùng một lúc và cuối cùng chẳng sửa được gì cả.

Trong bài học này, bạn sẽ học cách tiếp cận có hệ thống để phân biệt các nguyên mẫu thành công

từ những người bị bỏ rơi. Đến cuối bài học này, bạn sẽ có thể

kiểm tra ứng dụng của bạn từ góc độ người dùng, nhanh chóng thu thập phản hồi hữu ích,

ưu tiên các cải tiến dựa trên tác động và nỗ lực, đồng thời sử dụng các công cụ AI để tăng tốc

quá trình lặp. Đầu tiên, hãy mở ứng dụng Avalanche đã triển khai của bạn. Bạn có thể truy cập nó thông qua

Giao diện Streamlit của Snowflake hoặc Streamlit Cloud nếu bạn đã triển khai nó ở đó.

Hãy đặt mình vào vị trí của người quản lý thương hiệu tại Avalanche. Mục tiêu của bạn là trả lời câu hỏi này

câu hỏi kinh doanh. Khách hàng nghĩ gì về dòng sản phẩm Winter? Điều hướng qua ứng dụng của bạn

với đôi mắt tươi mới và đánh giá. Bạn có thể nhanh chóng xác định được tính năng phân tích tình cảm không? là

kết quả được trình bày dưới dạng dễ hiểu? Liệu ai đó không quen thuộc với bạn

tập dữ liệu biết nên nhấp vào cái gì tiếp theo? Sự thay đổi quan điểm này giúp bạn xác định các vấn đề về khả năng sử dụng trước khi

người dùng thực sự gặp phải chúng. Hiển thị ứng dụng của bạn cho ai đó trong năm giây, sau đó hỏi ngay

họ, bạn nghĩ ứng dụng này làm được gì? Điều gì nổi bật nhất với bạn? Bạn có thể tìm ra

phải làm gì tiếp theo? Bài kiểm tra này đánh giá ấn tượng đầu tiên. Các tính năng chính của bạn phải là

rõ ràng ngay lập tức, không bị che giấu hoặc gây nhầm lẫn. Nếu bạn đang làm việc một mình, hãy chụp ảnh màn hình của

ứng dụng của bạn và gửi nó cho bạn bè qua tin nhắn hoặc Slack. Yêu cầu họ chỉ dành năm giây

nhìn vào nó và trả lời những câu hỏi tương tự. Xác định hành trình quan trọng nhất của người dùng

trong ứng dụng của bạn. Tải trang tổng quan, chạy phân tích cảm tính, diễn giải kết quả. Đi qua

luồng này trong khi bạn tự tính thời gian. Hãy chú ý đến nơi bạn chậm lại hoặc do dự. Hãy tự hỏi mình,

có điều gì khó hiểu hoặc khó xử trong quy trình này không? Hướng dẫn có rõ ràng và có thể thực hiện được không? Liệu

bố trí hỗ trợ nhiệm vụ chính này một cách hiệu quả? Hãy nhớ rằng, bạn không thử nghiệm mọi thứ.

Hãy tập trung vào quy trình làm việc quan trọng này để giúp quá trình thử nghiệm của bạn diễn ra nhanh chóng và tập trung. Mở ứng dụng ghi chú

hoặc lấy một mảnh giấy và tạo ra ba cái thùng này. Lỗi, bất cứ thứ gì bị hỏng hoặc không

đang làm việc. Các vấn đề về khả năng sử dụng, các tính năng hoạt động nhưng cảm thấy rắc rối hoặc khó hiểu. Ý tưởng đặc điểm,

Rất vui được bổ sung để phát triển trong tương lai. Đối với mỗi mục bạn xác định, hãy hỏi xem điều gì có tác động lớn

nhưng nỗ lực sửa chữa thấp? Tôi có thể cải thiện điều gì ngay bây giờ sau 30 phút nữa? Đây là sự nhanh chóng của bạn

thắng. Hãy tập trung giải quyết một hoặc hai vấn đề này ngay lập tức. Nếu bạn xác định được vấn đề cần

khắc phục, tận dụng các công cụ AI để trợ giúp. Đối với các vấn đề về nội dung, hãy sử dụng GitHub Copilot, ChatGBT hoặc Cloud

để diễn đạt lại các nhãn hoặc chú giải công cụ khó hiểu. Yêu cầu AI viết lại các mẫu lời nhắc để rõ ràng hơn

và yêu cầu trợ giúp dọn dẹp các khối mã. Để có trải nghiệm người dùng, hãy sử dụng tab Trợ lý JetAI của bạn

trong Snowflake để thử nghiệm những cách mới để trả lời câu hỏi của người dùng. Yêu cầu AI đề xuất biểu đồ thay thế

các loại hoặc trực quan hóa dữ liệu. Bạn không xây dựng một ứng dụng mới, bạn đang đánh bóng và tinh chỉnh những gì bạn

đã được tạo rồi. Nếu có ai đó cung cấp phản hồi trong quá trình thử nghiệm của bạn, hãy cho họ biết điều gì

bạn đã thay đổi. Một thông báo đơn giản như, này, tôi đã làm cho biểu đồ đó dễ đọc hơn dựa trên phản hồi của bạn.

Cảm ơn một lần nữa vì lời khuyên. Cách tiếp cận này có thể biến những người thử nghiệm bình thường thành người dùng và người ủng hộ liên tục

cho ứng dụng của bạn. Sự khác biệt giữa nguyên mẫu được sử dụng và nguyên mẫu thường xuyên bị lãng quên

phụ thuộc vào những gì xảy ra sau khi ra mắt. Hãy chắc chắn rằng bạn là người duy nhất được mọi người tiếp tục đến

quay lại. Trong video tiếp theo, chúng ta sẽ khám phá cách cải thiện kết quả JetAI của bạn nhanh hơn nữa bằng cách sử dụng

kỹ thuật thiết kế nhanh chóng tốt hơn.