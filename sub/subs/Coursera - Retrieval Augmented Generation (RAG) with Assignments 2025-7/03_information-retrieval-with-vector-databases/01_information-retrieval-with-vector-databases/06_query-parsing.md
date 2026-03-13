# 06 truy vấn phân tích cú pháp

---

Một bước quan trọng trong hệ thống RAG sản xuất

đang dọn dẹp các lời nhắc do người dùng gửi.

Hệ thống RAG thường được triển khai trong bối cảnh

nơi người dùng cuối mong đợi tương tác với LLM

theo cách trò chuyện,

như thể họ đang trò chuyện với một người khác.

Kết quả là lời nhắc LLM do con người viết

tạo ra các truy vấn tìm kiếm xấu.

Thay vì trực tiếp đưa ra những lời nhắc đó

tới cơ sở dữ liệu vectơ,

người truy tìm có thể phân tích lời nhắc

để xác định mục đích của nó và chỉnh sửa, viết lại,

hoặc chuyển đổi hoàn toàn lời nhắc

để tối ưu hóa nó cho việc truy xuất.

Có nhiều kỹ thuật phân tích truy vấn được sử dụng.

Vì vậy, chúng ta hãy nhìn vào một vài trong số họ.

Giải pháp đơn giản nhất và được sử dụng rộng rãi nhất

với lời nhắc lộn xộn đang sử dụng LLM để viết lại truy vấn

trước khi nó được gửi đến người truy tìm.

Ví dụ, hãy xem xét một hệ thống RAG

được xây dựng xung quanh nền tảng kiến thức về thông tin y tế.

Bạn có thể thiết lập LLM làm trình ghi lại truy vấn

với lời nhắc sau.

Lời nhắc sau đây được gửi bởi người dùng

để truy vấn cơ sở dữ liệu các tài liệu y tế

liên kết các triệu chứng với chẩn đoán.

Viết lại lời nhắc để tối ưu hóa nó

để tìm kiếm cơ sở dữ liệu bằng cách thực hiện như sau.

Làm rõ các cụm từ mơ hồ,

sử dụng thuật ngữ y tế nếu có,

thêm từ đồng nghĩa làm tăng tỷ lệ cược

tìm tài liệu phù hợp,

xóa thông tin không cần thiết hoặc gây mất tập trung,

và sau đó bạn chèn lời nhắc của người dùng.

Một bệnh nhân có thể gửi lời nhắc,

Tôi ra ngoài dắt chó đi dạo,

một phòng thí nghiệm màu đen xinh đẹp tên là Poppy

khi cô ấy chạy khỏi tôi và giật mạnh dây xích

trong khi tôi đang giữ nó.

Ba ngày sau, vai tôi vẫn còn tê

và các ngón tay của tôi đều là kim châm.

Chuyện gì đang xảy ra vậy?

Lời nhắc này rõ ràng không được tối ưu hóa cho việc truy xuất.

Đây là lời nhắc viết lại

sau khi nó được chuyển qua trình ghi lại truy vấn.

Trải qua một lực kéo mạnh đột ngột trên vai

dẫn đến tê vai dai dẳng

và ngón tay bị tê trong ba ngày.

Nguyên nhân hoặc chẩn đoán tiềm ẩn là gì

chẳng hạn như bệnh thần kinh hoặc tác động lên dây thần kinh?

Lời nhắc mới này sẽ loại bỏ những thông tin không cần thiết,

làm rõ sự mơ hồ,

và thậm chí sử dụng một số thuật ngữ y tế

điều đó có thể làm tăng khả năng tìm được người phù hợp

trong cơ sở tri thức.

Mặc dù bạn có thể và nên lặp lại lời nhắc

bạn sử dụng để viết lại truy vấn,

nói chung, lợi ích bạn đạt được từ nó là rất đáng kể

và dễ dàng biện minh cho các chi phí bổ sung

của cuộc gọi LLM cần thiết để dọn sạch từng lời nhắc.

Trong khi viết lại truy vấn cơ bản

thường là kỹ thuật phân tích truy vấn duy nhất

bạn sẽ cần cân nhắc,

kỹ thuật tiên tiến hơn tồn tại.

Ví dụ: nhận dạng thực thể được đặt tên

là một kỹ thuật để nhận biết các loại thông tin

trong truy vấn, như địa điểm, con người, ngày tháng,

nhân vật hư cấu, v.v.

Thông tin này sau đó có thể được sử dụng để thông báo

hoặc tìm kiếm vector được thực hiện bởi người truy tìm

hoặc việc lọc siêu dữ liệu được thực hiện sau này trong quy trình.

Một ví dụ ở đây là cho một mô hình có tên Gliner,

đó là một mô hình nhận dạng thực thể được đặt tên chung.

Bạn có thể cho nó một đoạn văn bản

và sau đó là danh sách các loại thực thể

bạn muốn nó xác định, chẳng hạn như người hoặc ngày tháng.

Mô hình sẽ phân tích truy vấn

và trả về một truy vấn được gắn nhãn

với sự xác định của các loại đó.

Trong ví dụ cụ thể này,

Tôi đã cung cấp một số văn bản đầu vào

và bảo người mẫu Gliner thử và dán nhãn

bất kỳ đề cập nào về một người, sách, địa điểm,

ngày tháng, diễn viên và nhân vật.

Trong phản hồi, bạn có thể thấy rằng nó được gắn nhãn

bất cứ lúc nào nó nhìn thấy những thực thể khác nhau này.

Đây là mô hình rất hiệu quả

và chúng tôi có thể chạy nó mỗi khi có truy vấn xuất hiện.

Bao gồm bước này sẽ tăng thêm một chút độ trễ,

nhưng chất lượng của việc truy xuất

bây giờ có thể được cải thiện đáng kể nhờ điều này.

Một kỹ thuật phân tích truy vấn nâng cao khác

được gọi là phần nhúng tài liệu giả định hoặc HIDE.

Cách tiếp cận này tinh chỉnh một truy vấn tìm kiếm

bằng cách tạo ra một tài liệu giả định

đó sẽ là kết quả lý tưởng của quá trình tìm kiếm.

Ví dụ: nếu bạn đang cố truy xuất thông tin

về câu hỏi y tế trước đó,

LLM sẽ được sử dụng để tạo ra một tài liệu giả định

về tình trạng tê vai và tay do bị kéo nhanh.

Sau đó, tài liệu giả định đó được nhúng

và biểu diễn vector của nó

là những gì thực sự được sử dụng để hoàn thành việc tìm kiếm.

Ý tưởng ở đây là bạn đang giúp chú chó tha mồi

hiểu không chỉ mục đích của lời nhắc hoặc câu hỏi,

nhưng kết quả chất lượng cao sẽ như thế nào.

Thông thường, chó tha mồi cần khớp lời nhắc với tài liệu.

Vì vậy, ở một mức độ nào đó, con chó tha mồi phù hợp

các loại văn bản khác nhau, hoặc từ táo đến cam.

Bằng cách tạo ra một tài liệu giả định,

công cụ truy tìm hiện đang so sánh nhiều văn bản tương tự hơn,

một tài liệu hoàn hảo giả định,

và các tài liệu thực sự có trong cơ sở tri thức.

Trong thực tế,

Hyde thực sự cung cấp những cải tiến về hiệu suất

với cái giá phải trả là độ trễ tăng thêm trong quá trình tìm kiếm

và một số tài nguyên tính toán để chạy LLM

tạo ra các tài liệu giả định.

Theo kinh nghiệm của tôi, có một số loại phân tích truy vấn

là một phần quan trọng trong hệ thống RAG của bạn.

Trong hầu hết mọi trường hợp, việc viết lại truy vấn cơ bản,

chỉ cần sử dụng LLM được nhắc nhở độc đáo để thực hiện các thao tác chỉnh sửa cơ bản

trên lời nhắc do người dùng gửi là cách tiếp cận phù hợp.

Kỹ thuật tiên tiến hơn,

như sử dụng nhận dạng thực thể được đặt tên,

Hyde và những người khác có thể mang lại lợi ích bổ sung,

nhưng chúng có thể phức tạp hơn để chạy

và không nhất thiết mang lại kết quả tốt hơn.

Hãy thử nghiệm những kỹ thuật tiên tiến này

và để kết quả quyết định dự án của bạn cần phát triển như thế nào.