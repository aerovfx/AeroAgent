# 02 điều gì tạo nên thử thách trong sản xuất

---

Môi trường sản xuất đặt các dòng hoàn toàn mới vào hệ thống RAG của bạn,

và việc vượt qua những thử thách đó đòi hỏi một bộ kỹ năng khác với những kỹ năng cần thiết khi tạo nguyên mẫu.

Để bắt đầu mô-đun này, chúng ta hãy xem lại những thách thức mới mà hệ thống của bạn sẽ gặp phải khi nó được khách hàng thực tế sử dụng.

Những thách thức đầu tiên bạn sẽ gặp phải trong quá trình sản xuất chỉ đơn giản là phát sinh từ việc tăng thêm lưu lượng truy cập.

Nhiều người dùng hơn sẽ hạn chế thông lượng của hệ thống của bạn,

cho dù đó là số lượng yêu cầu có thể xử lý cùng một lúc hay độ trễ giữa việc nhận yêu cầu và trả lời.

Nhiều yêu cầu hơn cũng đồng nghĩa với việc sử dụng nhiều bộ nhớ và điện toán hơn, điều này cuối cùng đồng nghĩa với việc chi phí sẽ cao hơn.

Việc duy trì hiệu suất hệ thống thô ở quy mô lớn có thể là một thách thức.

Loại thách thức thứ hai đến từ sự đa dạng và khó đoán của các lời nhắc mà hệ thống của bạn sẽ nhận được khi nó đến tay người dùng.

Ngay cả khi kiểm tra nghiêm ngặt, rất khó để dự đoán mọi loại yêu cầu mà hệ thống RAG của bạn sẽ nhận được.

Bạn có thể thấy hệ thống của mình gặp khó khăn khi đáp ứng một số yêu cầu mới này, ngay cả khi hệ thống hoạt động tốt trong quá trình thử nghiệm trước khi ra mắt.

Một thách thức khác trong quá trình sản xuất là dữ liệu trong thế giới thực thường rất lộn xộn.

Không có gì lạ khi dữ liệu bị phân mảnh, định dạng kém, thiếu siêu dữ liệu, v.v.

Nhiều dữ liệu thậm chí không ở định dạng văn bản mà thay vào đó được tìm thấy ở dạng hình ảnh, tệp PDF và bản trình bày.

Nếu bạn muốn đưa dữ liệu này vào cơ sở kiến ​​thức của mình, bạn sẽ cần một cách để truy cập nó.

Vấn đề bảo mật và quyền riêng tư cũng là một mối quan tâm.

Rất nhiều hệ thống RAG được triển khai rõ ràng vì dữ liệu trong cơ sở tri thức của bạn là riêng tư hoặc độc quyền.

Đảm bảo dữ liệu vẫn ở chế độ riêng tư đồng thời cho phép người dùng được ủy quyền truy cập dữ liệu khi sử dụng hệ thống RAG của bạn là chức năng quan trọng.

Trên hết những thách thức này, vấn đề lớn nhất trong sản xuất là những sai sót có thể ảnh hưởng thực sự đến hoạt động kinh doanh, dù là về mặt tài chính hay danh tiếng.

Khi Google lần đầu tiên ra mắt tính năng Tóm tắt tìm kiếm AI, nó đã phản hồi một số lời nhắc bằng cách khuyên người dùng nên ăn đá vì những lợi ích dinh dưỡng mà chúng mang lại.

Khi Google điều tra nguyên nhân của vấn đề này, hóa ra là một người dùng đã hỏi:

Tôi nên ăn bao nhiêu đá?

Một câu hỏi phải thừa nhận là ngớ ngẩn và khó đoán.

Khi hệ thống truy xuất thông tin về câu hỏi, nhiều bài báo hoặc cuộc trò chuyện trên diễn đàn mà nó tìm thấy rất hài hước.

Nhưng hệ thống đã không nhận ra sự thật đó.

Google sau đó đã khắc phục sự cố này và thậm chí còn viết một bài đăng trên blog giải thích nguồn gốc của lỗi.

Nhưng họ không phải là công ty duy nhất gặp rắc rối sau khi tung ra sản phẩm dựa trên LLM.

Các chatbot của hãng hàng không đã hứa hẹn những khoản giảm giá có ý nghĩa cho khách hàng nhưng thực tế không hề tồn tại.

Những kẻ độc hại sẽ cố gắng lừa hệ thống RAG của bạn để bán cho họ sản phẩm của bạn miễn phí hoặc tiết lộ thông tin bí mật.

Sản xuất đơn giản là một môi trường đầy thách thức để hệ thống RAG của bạn hoạt động.

Và do đó, việc có sẵn các hệ thống để dự đoán các vấn đề trước khi chúng xảy ra, theo dõi chúng khi chúng xảy ra và xác minh rằng những thay đổi bạn thực hiện sẽ dẫn đến những cải tiến thực sự là rất quan trọng.

Có nhiều kỹ thuật khác nhau mà bạn có thể sử dụng để giải quyết tất cả những thách thức sản xuất này.

Hãy tham gia cùng tôi trong video tiếp theo để xem video đầu tiên trong số này, cách xây dựng một hệ thống có khả năng quan sát mạnh mẽ.