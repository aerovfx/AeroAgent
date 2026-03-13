# 07 xử lý-ảo giác

---

Ảo giác là mối lo ngại thường xuyên khi làm việc với LLM,

và ngay cả một hệ thống RAG được thiết kế tốt vẫn có thể gây ảo giác.

Phát hiện ảo giác, giảm bớt chúng,

và đảm bảo các nguồn trang web LLM chính xác

do đó, đây là phần quan trọng nhất trong việc xây dựng đường dẫn RAG của bạn.

Chúng ta hãy xem xét một số cách thực hiện việc này.

Hãy tưởng tượng bạn thiết lập và chạy hệ thống RAG đầu tiên của mình,

một chatbot dịch vụ khách hàng cho một cửa hàng trực tuyến.

Một người dùng viết thư và hỏi liệu công ty có giảm giá cho sinh viên hay không.

Người săn tìm tìm thấy thông tin về giảm giá cho cả người cao tuổi và khách hàng mới,

cả hai đều sẽ được giảm giá 10%.

Trong khi đó, lời nhắc của hệ thống LLM khuyến khích nó hữu ích với khách hàng.

Tất cả những yếu tố này ảnh hưởng đến LLM phản ứng,

hoàn toàn, bạn có thể được giảm giá 10 phần trăm với thẻ sinh viên hợp lệ,

mức giảm giá lớn tương tự mà chúng tôi dành cho người cao niên và khách hàng mới.

Người dùng hài lòng và tiếp tục mua sắm trên trang web của bạn,

háo hức yêu cầu giảm giá khi thanh toán.

Vấn đề duy nhất là khoản giảm giá dành cho sinh viên đó không thực sự tồn tại.

LLM vừa mới làm được điều đó.

Điều quan trọng cần nhớ là tại sao LLM lại gây ảo giác ngay từ đầu.

Một mô hình ngôn ngữ được thiết kế để tạo ra các chuỗi văn bản có thể xảy ra,

với một chút ngẫu nhiên được đưa vào để tạo sự đa dạng.

Các chuỗi văn bản có thể xảy ra thường chính xác về mặt thực tế, nhưng không phải lúc nào cũng vậy.

Mô hình ngôn ngữ không được thiết kế để phân biệt giữa đúng và sai,

chỉ có thể xảy ra và không thể xảy ra.

Ảo giác có vấn đề vì một số lý do.

Điều đầu tiên là đủ rõ ràng.

Bạn chỉ không muốn mô hình ngôn ngữ của mình cung cấp thông tin không chính xác cho người dùng.

Thứ hai là gần như theo định nghĩa,

ảo giác nghe có vẻ hợp lý,

và do đó có thể khó phát hiện hơn là hoàn toàn vô nghĩa.

Cuối cùng, theo thời gian, ảo giác thỉnh thoảng có thể khiến người dùng mất niềm tin vào hệ thống RAG của bạn,

ngay cả khi phần lớn nội dung được tạo ra là chính xác.

Tất nhiên, lý do chính khiến bạn xây dựng đường dẫn RAG là để giảm ảo giác.

Thông tin bạn truy xuất từ cơ sở kiến thức của mình có thể giúp đưa ra phản hồi của LLM,

và có thể cung cấp thông tin còn thiếu trong dữ liệu huấn luyện của mô hình.

Dù vậy, hệ thống RAG vẫn dễ bị ảo giác,

vì vậy các bước bổ sung để ngăn chặn chúng là cần thiết.

Ảo giác có thể có nhiều loại và kích cỡ.

Quay trở lại với mức giảm giá đó,

LLM có thể mô tả chính xác mức giảm giá thực tế dành cho người cao tuổi và cách yêu cầu khoản giảm giá đó,

nhưng lại ghi sai mức giảm giá là 5% thay vì 10%.

Trong những trường hợp cực đoan hơn, LLM có thể nêu không chính xác

không có chiết khấu cao cấp khi thực sự có.

Hoặc, như bạn đã thấy trước đó, hãy nghĩ ra những chương trình giảm giá hoàn toàn mới mà công ty bạn không cung cấp.

Điều này có nghĩa là bạn sẽ cần đánh giá văn bản mà LLM của bạn tạo ra ở nhiều cấp độ

nếu bạn muốn cảm thấy tự tin vào độ chính xác của nó.

Bây giờ đến đây là sự thật lạnh lùng và phũ phàng.

Không có giải pháp hoàn hảo cho chứng ảo giác, hoặc ít nhất là không có ở thời điểm hiện tại.

Tuy nhiên, may mắn thay, RAG là một trong những phương pháp tốt nhất hiện có,

và có nhiều cách bạn có thể tinh chỉnh hệ thống RAG

để giảm thêm tần suất ảo giác.

Để bắt đầu, hãy suy nghĩ kỹ cách bạn phát hiện ảo giác trong đầu ra LLM

nếu bạn không có nền tảng kiến thức.

Nếu không có nguồn đáng tin cậy bên ngoài để so sánh kết quả đó với,

lựa chọn của bạn khá hạn chế.

Tuy nhiên, một cách tiếp cận là tự kiểm tra tính nhất quán,

nơi bạn yêu cầu mô hình liên tục tạo các lần hoàn thành cho cùng một lời nhắc

và kiểm tra xem thông tin thực tế có trong đó có nhất quán hay không.

Ý tưởng cơ bản là nếu mô hình ngôn ngữ tạo ra thông tin ảo giác,

nó sẽ làm như vậy một cách không nhất quán,

và sự khác biệt thực tế giữa các lần hoàn thành sẽ có thể được phát hiện.

Tuy nhiên, trong thực tế, phương pháp này có thể tốn kém và không đáng tin cậy.

Nếu bạn có nền tảng kiến ​​thức để tham khảo thì đó là nơi tốt nhất để bắt đầu.

Vì bên trong hệ thống RAG, bạn có quyền truy cập vào cơ sở kiến thức,

cách tốt nhất để giảm ảo giác

là để đảm bảo các phản hồi được căn cứ vào thông tin được truy xuất.

Ví dụ: bạn có thể sửa đổi lời nhắc hệ thống của mình

để nói rằng LLM chỉ có thể đưa ra những tuyên bố thực tế

dựa trên thông tin được truy xuất.

Nếu bạn muốn tự tin hơn nữa

rằng LLM đang đưa ra phản hồi dựa trên các tài liệu được truy xuất,

bạn có thể yêu cầu LLM trích dẫn thêm nguồn của nó.

Đôi khi, điều này chỉ có nghĩa là nhắc người mẫu trích dẫn nguồn

ở cuối mỗi câu hoặc đoạn văn.

Điều này có thể làm tăng thêm khả năng

rằng LLM đưa ra phản hồi của nó dựa trên các nguồn được truy xuất.

Và trích dẫn cũng làm cho nó dễ dàng hơn

để người đọc xác minh các yêu cầu trong phản hồi.

Tuy nhiên, rủi ro với cách tiếp cận này là

là LLM sẽ chỉ tạo ra ảo giác về các trích dẫn.

Một số mô hình được tinh chỉnh để trích dẫn nguồn

sẽ tạo ra các trích dẫn hợp lệ đáng tin cậy hơn,

nhưng nếu bạn muốn tự tin hơn trong trích dẫn của mình,

bạn sẽ cần sử dụng hệ thống bên ngoài.

Ví dụ: ContextCite là một hệ thống

để đánh giá xem phản hồi có cơ sở tốt như thế nào

trong một tập hợp các nguồn tài liệu.

Mô hình xử lý câu trả lời theo từng câu

và nó quy định từng câu

đến một trong những tài liệu ngữ cảnh đã được lấy ra

và cung cấp cho LLM.

ContextCite sau đó tạo thẻ cho mỗi câu

lưu ý tài liệu nào là nguồn gốc của câu đó.

Trong trường hợp lời khai

không có tài liệu hỗ trợ thì ghi là không có nguồn.

Một số triển khai thậm chí có thể cung cấp điểm tương tự

giữa câu và tài liệu nguồn được xác định.

Các thẻ này có thể được sử dụng để tạo trích dẫn nguồn

trong đầu ra LLM được tạo cuối cùng

hoặc như một phần của đánh giá

về tần suất LLM căn cứ vào các phản hồi của nó

trong các tài liệu được hệ thống RAG truy xuất.

Những nỗ lực gần đây, chẳng hạn như tiêu chuẩn ALCE,

nhằm mục đích đo lường mức độ tham chiếu của hệ thống

và trích dẫn nguồn khi tạo phản hồi.

Hệ thống cung cấp các cơ sở kiến thức được lắp ráp sẵn

và các câu hỏi mẫu.

Sau đó, bạn sẽ sử dụng hệ thống RAG của mình theo những lời nhắc này

để yêu cầu hệ thống ALCE đánh giá phản hồi được tạo ra.

Điểm được tạo cho ba số liệu chính,

sự trôi chảy, chính xác và chất lượng trích dẫn.

Nói cách khác, văn bản cuối cùng rõ ràng đến mức nào?

Thực tế chính xác như thế nào?

Và các trích dẫn được cung cấp căn chỉnh tốt đến mức nào

với các nguồn chính xác để trích dẫn?

Những điểm chuẩn này không kiểm soát được ảo giác

trong hệ thống sản xuất của bạn,

nhưng chúng cho thấy hệ thống của bạn hoạt động tốt như thế nào

là tránh ảo giác và trích dẫn nguồn.

Phát hiện ảo giác là một thách thức liên tục

trong một hệ thống dựa trên LLM.

Điều đó nói lên rằng, bằng cách xây dựng hệ thống RAG,

bạn đã thực hiện bước hiệu quả nhất rồi

để giảm thiểu ảo giác.

Sau đó, hãy tập trung sức lực vào việc đảm bảo LLM

đưa ra câu trả lời và lấy thông tin

bằng cách tinh chỉnh lời nhắc hệ thống của bạn.

Cuối cùng, hãy kiểm tra hệ thống của bạn

sử dụng điểm chuẩn tập trung vào ảo giác

để đảm bảo hệ thống của bạn đang được nối đất,

câu trả lời được trích dẫn tốt.

Cùng với nhau, những cách tiếp cận này có thể đáng kể

giảm ảo giác và giúp bạn xây dựng một hệ thống

cung cấp những câu trả lời đáng tin cậy.