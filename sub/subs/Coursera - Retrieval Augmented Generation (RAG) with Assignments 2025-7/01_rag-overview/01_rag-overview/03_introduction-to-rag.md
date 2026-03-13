# 03 giới thiệu về giẻ rách

---

LLM là công cụ đáng chú ý.

Họ có thể trả lời các câu hỏi, tóm tắt và viết lại văn bản, cung cấp phản hồi về tài liệu, tạo ra

mã, và nhiều hơn nữa.

Những loại nhiệm vụ này dường như nằm ngoài tầm với của máy tính chỉ vài năm trước đây và việc tương tác

với một người có thể cảm thấy rất giống làm việc với một người khác.

RAG là một cách tiếp cận nhằm cải thiện hơn nữa hiệu suất của các mô hình ngôn ngữ lớn bằng cách đưa ra

họ truy cập vào thông tin mà họ không biết từ quá trình đào tạo.

Để giúp làm nổi bật ý tưởng đó, chúng ta hãy xem xét một vài ví dụ.

Giả sử tôi hỏi bạn câu hỏi, tại sao khách sạn lại đắt vào cuối tuần?

Có lẽ bạn có thể trả lời câu hỏi đó.

Nhiều người đi du lịch vào cuối tuần hơn, do đó có nhiều sự cạnh tranh về phòng hơn.

Bây giờ giả sử tôi hỏi bạn, tại sao khách sạn ở Vancouver lại siêu đắt vào cuối tuần tới?

Bạn sẽ cần thêm thông tin để trả lời câu hỏi này.

Nếu tìm kiếm trên mạng, bạn có thể thấy siêu sao quốc tế Taylor Swift đang ở

thị trấn vào cuối tuần này để lưu trú hai đêm.

Với thông tin bổ sung đó, một lần nữa bạn có thể trả lời được câu hỏi.

Cuối cùng, giả sử tôi hỏi bạn, tại sao Vancouver không có nhiều khách sạn có sức chứa gần bằng

trung tâm thành phố?

Để trả lời câu hỏi này, có lẽ bạn cần phải nghiên cứu sâu về lịch sử

về sự phát triển của Vancouver, quy hoạch đô thị nói chung, v.v.

Nói cách khác, bạn cần truy cập vào rất nhiều thông tin chuyên ngành.

Bạn có thể nghĩ cách bạn trả lời những câu hỏi này gồm hai giai đoạn.

Đầu tiên, bạn thu thập bất kỳ thông tin cần thiết nào và sau đó bạn suy luận về thông tin đó

để phát triển phản ứng của bạn.

Như bạn đã thấy ở câu hỏi đầu tiên, đôi khi bạn không cần thu thập bất kỳ thông tin nào.

Dựa trên kiến ​​thức của bạn về thế giới, bạn sẵn sàng phản hồi ngay lập tức.

Tuy nhiên, đôi khi, bạn có thể cần thu thập một chút hoặc thậm chí nhiều thông tin.

Trong RAG, quá trình thu thập thông tin hữu ích được gọi là truy xuất và quá trình

lý luận về thông tin đó và phản hồi được gọi là thế hệ.

LLM được hưởng lợi từ giai đoạn truy xuất về cơ bản giống như những lý do bạn làm.

Bạn sẽ tìm hiểu thêm về LLM trong suốt khóa học này, nhưng hiện tại, bạn có thể nghĩ về chúng

giống như một người có nhiều kiến thức tổng quát từ việc đọc những khối kiến thức khổng lồ

của internet.

Khi bạn nhắc LLM, nó sẽ dựa vào kiến ​​thức này để tạo ra phản hồi.

Đối với nhiều lời nhắc, điều này hoạt động rất tốt.

Tuy nhiên, trong các trường hợp khác, LLM không biết thông tin cần thiết để phản hồi chính xác.

Lời nhắc có thể là về một sự kiện rất gần đây hoặc một số thông tin chuyên biệt mà nó chưa có.

đã thấy trước đó.

Cũng như trường hợp của bạn, thật vô lý khi mong đợi LLM trở thành chuyên gia về mọi chủ đề,

và họ đưa ra phản hồi tốt hơn nhiều khi họ có quyền truy cập vào thông tin tốt hơn.

Nhận thức rằng LLM cũng được hưởng lợi từ giai đoạn truy xuất là ý tưởng cốt lõi của RAG.

Tất nhiên, LLM không phải là những người dành nhiều thời gian trên Wikipedia.

Thay vào đó, chúng là những mô hình toán học đã được đào tạo trên các tập dữ liệu khổng lồ được lấy

từ khắp nơi trên internet mở.

Trong quá trình đào tạo, mô hình sẽ tìm hiểu mọi thông tin có trong khóa đào tạo

dữ liệu.

Khi bạn gửi lời nhắc tới LLM, bạn đang hy vọng thông tin có liên quan đến câu hỏi của mình

được đưa vào dữ liệu huấn luyện, lý tưởng nhất là nhiều lần.

Thật không may, rất nhiều thông tin sẽ không được đưa vào.

Các công ty giữ cơ sở dữ liệu riêng tư, một số thông tin bị ẩn hoặc khó truy cập, và với

tin tức được xuất bản mỗi phút trong ngày, sẽ luôn có thông tin ngoài kia

mà LLM chưa được đào tạo.

Câu hỏi đặt ra là làm cách nào để đảm bảo LLM biết thông tin hữu ích này?

Câu trả lời ngắn gọn?

Chỉ cần đặt nó trong dấu nhắc.

Ý tưởng chính của hệ thống RAG là bạn có thể sửa đổi lời nhắc trước khi gửi nó đến hệ thống lớn.

mô hình ngôn ngữ

Ngoài câu hỏi ban đầu của người dùng, bạn có thể thêm thông tin giúp

LLM trả lời.

Nếu bạn hỏi hệ thống RAG, tại sao các khách sạn ở Vancouver cuối tuần này lại siêu đắt?

Đầu tiên nó sẽ thực hiện bước truy xuất để thu thập thông tin liên quan.

Sau đó, mô hình ngôn ngữ sẽ được cung cấp lời nhắc tăng cường bao gồm cả

câu hỏi ban đầu và bất kỳ thông tin nào được truy xuất.

Bây giờ LLM có thông tin cần thiết để phản hồi chính xác.

Tất nhiên, thông tin này cần phải được lấy từ đâu đó.

Thành phần của hệ thống RAG xử lý quá trình này được gọi là bộ thu hồi.

Người truy tìm quản lý cơ sở kiến ​​thức về thông tin đáng tin cậy, có liên quan và có thể là thông tin riêng tư.

Khi hệ thống RAG nhận được lời nhắc, bộ truy xuất sẽ tìm và truy xuất thông tin phù hợp nhất

thông tin từ cơ sở tri thức để chia sẻ với LLM.

Sau đó, mô hình sẽ sử dụng thông tin được truy xuất đó khi phản hồi lời nhắc.

Cái tên Retrieval Augmented Generation, được thừa nhận là rất thú vị, giờ đây hy vọng sẽ khiến

có ý nghĩa hơn.

Tất cả những gì bạn đang làm là cải thiện hoặc nâng cao cách LLM tạo văn bản bằng cách truy xuất trước tiên

thông tin liên quan từ cơ sở tri thức.

Đây là mô tả cấp cao về cách hoạt động của RAG, nhưng đôi khi nó có thể hữu ích hơn

để xem một số ứng dụng ví dụ.

Vì vậy, hãy tham gia cùng tôi trong video tiếp theo, nơi tôi sẽ nói về một số cách sử dụng RAG.