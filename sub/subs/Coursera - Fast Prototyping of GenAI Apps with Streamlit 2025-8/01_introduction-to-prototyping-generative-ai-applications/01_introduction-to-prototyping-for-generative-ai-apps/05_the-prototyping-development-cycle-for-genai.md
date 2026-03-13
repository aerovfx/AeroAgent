# 05 chu trình phát triển nguyên mẫu cho genai

---

Trước khi bạn bắt đầu xây dựng, sẽ rất hữu ích nếu bạn thu nhỏ và xem vị trí của nguyên mẫu phù hợp trong phạm vi lớn hơn.

hình ảnh. Trong chu trình phát triển truyền thống, bạn bắt đầu với một kế hoạch chi tiết,

thiết kế một hệ thống đầy đủ, viết mã, kiểm tra và cuối cùng là triển khai nó.

Điều đó phù hợp với các dự án có yêu cầu rõ ràng, cố định,

nhưng quá chậm để thử nghiệm Gen AI.

Với các ứng dụng Gen AI, quy trình sẽ khác. Bạn không phải lúc nào cũng biết đầu ra sẽ như thế nào.

Mô hình Gen AI có thể làm bạn ngạc nhiên.

Lời nhắc của bạn có thể bị hỏng, gây ra hành vi không mong muốn, lỗi hoặc kết quả kém.

Người dùng của bạn có thể hành xử theo cách bạn không mong đợi.

Vì vậy, thay vì tuân theo một kế hoạch chặt chẽ, bạn cần xây dựng nhanh, kiểm tra thường xuyên và điều chỉnh nhanh chóng.

Đó là nơi tạo mẫu phù hợp.

Việc tạo nguyên mẫu xuất hiện ngay sau khi bạn có ý tưởng và ngay trước khi bạn cam kết phát triển toàn diện.

Đó là nơi bạn nhanh chóng thử nghiệm ý tưởng của mình bằng đầu vào thực, đầu ra thực và phản hồi thực.

Đặc biệt là khi bạn đang xây dựng bằng Gen AI, việc tạo nguyên mẫu không chỉ hữu ích mà còn rất cần thiết.

Tạo nguyên mẫu giúp bạn khám phá cách mô hình hoạt động,

và những thay đổi nhỏ có thể tạo ra sự khác biệt lớn như thế nào.

Ngay cả một sự thay đổi nhỏ trong cách bạn nhắc

có thể là sự khác biệt giữa vàng ròng và những điều vô nghĩa.

Tạo nguyên mẫu cũng cho phép bạn thử nghiệm ứng dụng của mình với người dùng thực để xem họ nghĩ như thế nào,

nhấp chuột, và đôi khi hoàn toàn bỏ lỡ điều hiển nhiên.

Bạn sẽ sớm phát hiện được các trường hợp khó khăn khi mô hình của bạn tự tin trả lời câu hỏi mà bạn thậm chí còn không hỏi.

Và bạn sẽ học nhanh xem ý tưởng của bạn có vững chắc, đáng ngạc nhiên hay cần một điểm xoay,

trước khi bạn chìm đắm trong đó hàng tuần.

Bạn sẽ quay lại việc tạo mẫu nhiều lần,

và mỗi lần bạn sẽ có một tính năng mới để kiểm tra hoặc một vấn đề mới cần giải quyết.

Và trong khóa học này, bạn sẽ coi việc tạo nguyên mẫu là chế độ phát triển mặc định của mình.

Điều đó có nghĩa là luôn xây dựng một cái gì đó, một cái gì đó bạn có thể thử nghiệm,

chia sẻ hoặc lặp lại, ngay cả khi đó chỉ là bản nháp rất thô.

Mỗi ứng dụng GenAI cơ bản đều có bốn phần chính.

Đầu tiên, bạn cần một giao diện người dùng.

Đây là cách mọi người sẽ sử dụng và tương tác với ứng dụng của bạn.

Nó có thể ở dạng một ứng dụng Streamlit đơn giản,

một chatbot hoặc thậm chí chỉ chạy mã trong sổ ghi chép.

Thứ hai, bạn cần thêm logic.

Đây là trái tim của ứng dụng của bạn.

Nó yêu cầu người dùng nhập câu hỏi hoặc dữ liệu,

và gửi nó đến AI để phản hồi.

Dẫn đến thành phần thứ ba.

Bạn cần dữ liệu.

Bắt đầu nguyên mẫu của bạn bằng thứ gì đó dễ dàng, chẳng hạn như tệp CSV hoặc tài liệu mẫu.

Điều này cung cấp cho bạn thông tin thực tế để làm việc trong quá trình thử nghiệm,

nhưng không đòi hỏi nhiều sự phức tạp đối với các tập dữ liệu phức tạp.

Cuối cùng, bạn cần kết nối với dịch vụ AI như GPT-4 hoặc Claude.

Dịch vụ AI thực hiện tư duy thông minh,

trong khi ứng dụng của bạn xử lý mọi thứ khác xung quanh nó.

Hãy nghĩ về nó như thế này.

Giao diện cho phép mọi người nói chuyện với ứng dụng của bạn.

Logic chỉ ra những gì cần làm.

Dữ liệu cung cấp cho bạn thứ gì đó để làm việc,

và AI thực hiện công việc nặng nhọc.

Đặt bốn mảnh này lại với nhau và bạn sẽ có một nguyên mẫu hoạt động được.

Đây là ví dụ về chu trình phát triển GenAI của bạn sẽ như thế nào.

Bạn bắt đầu bằng việc nảy ra một ý tưởng.

Sau đó xây dựng một nguyên mẫu nhanh bằng Python và Streamlit.

Tiếp theo, bạn thử nghiệm một nguyên mẫu với tập hợp dữ liệu thực tế nhỏ hơn,

và chia sẻ nguyên mẫu để nhận phản hồi từ người dùng của bạn.

Cuối cùng, bạn cải thiện lời nhắc, mã hoặc giao diện

dựa trên những gì bạn đã học được và quyết định xem liệu ứng dụng đó có đáng để chuyển thành một ứng dụng đầy đủ tính năng hay không.

Những việc trước đây phải mất hàng tuần giờ có thể được thực hiện chỉ trong vài phút.

Đó là sức mạnh của việc tạo mẫu nhanh chóng.

Điều quan trọng là phải biết sự khác biệt giữa ứng dụng nguyên mẫu và ứng dụng sản xuất hoàn chỉnh.

Bằng cách đó, bạn có thể đặt mục tiêu phù hợp.

Một nguyên mẫu giúp bạn khám phá ý tưởng.

Nó giúp bạn trả lời các câu hỏi.

Mặt khác, một ứng dụng sản xuất cần phải đáng tin cậy và an toàn.

Đây là cách họ so sánh.

Mục đích.

Một nguyên mẫu là để thử nghiệm và học tập.

Ứng dụng sản xuất nhằm cung cấp một sản phẩm hoàn chỉnh, ổn định.

Sự ưu tiên.

Nguyên mẫu tập trung vào tốc độ.

Ứng dụng sản xuất tập trung vào kiến ​​trúc và độ tin cậy.

Chất lượng mã.

Mã nguyên mẫu có thể lộn xộn nhưng đầy đủ chức năng.

Mã sản xuất phải được tái cấu trúc, sạch sẽ và có thể bảo trì.

Dữ liệu.

Nguyên mẫu có thể sử dụng bộ dữ liệu nhỏ hoặc mô phỏng.

Ứng dụng sản xuất yêu cầu dữ liệu thực, rõ ràng và được xác thực.

Bạn xây dựng một cái gì đó nhỏ, đưa nó ra trước dữ liệu thực hoặc con người thực,

và xem nó chịu đựng thế nào.

Vì với Genii, cách học nhanh nhất là xây dựng sớm,

kiểm tra thường xuyên và điều chỉnh theo thời gian thực.

Trong video tiếp theo, bạn sẽ tìm hiểu thêm về những sai lầm lớn nhất

Tôi thấy các nhà phát triển kiếm được tiền khi họ lao vào tạo nguyên mẫu GenAI

và những bước kiểm tra đơn giản có thể giúp bạn tránh được nhiều giờ thất vọng.

Hãy đi sâu vào.