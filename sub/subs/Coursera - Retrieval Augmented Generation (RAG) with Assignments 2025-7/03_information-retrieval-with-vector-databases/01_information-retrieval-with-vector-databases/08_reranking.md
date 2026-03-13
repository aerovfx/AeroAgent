# 08 sắp xếp lại

---

Một cách hay để tận dụng tối đa cả hai thế giới trong tìm kiếm ngữ nghĩa

là chỉ sử dụng nhiều kỹ thuật tìm kiếm cùng nhau.

Xếp hạng lại là một quá trình sau khi truy xuất

trong đó bộ tài liệu ban đầu

được cơ sở dữ liệu vector trả về

được xếp hạng lại bằng cách sử dụng các mô hình có hiệu suất cao nhưng đắt tiền

nhằm đảm bảo tài liệu được trả về tuyệt đối nhất.

Hãy xem nó hoạt động như thế nào.

Việc sắp xếp lại tất cả là nhằm cải thiện chất lượng truy xuất của bạn

sau khi một tập hợp các tài liệu hoặc các đoạn đã được lấy ra

nhưng trước khi chúng được gửi đến LLM.

Khi cơ sở dữ liệu vector trả về kết quả,

sắp xếp lại xuất hiện và cải thiện chất lượng truy xuất bằng cách tính điểm lại

và sau đó sắp xếp lại những tài liệu được truy xuất

sử dụng các mô hình có khả năng hơn.

Vì chỉ một số ít tài liệu cần được tính điểm lại và xếp hạng lại,

có thể sử dụng các mô hình hiệu suất cao nhưng tốn kém

không thể sử dụng được khi tìm kiếm toàn bộ cơ sở tri thức.

Hãy xem xét một ví dụ được đơn giản hóa quá mức.

Nếu lời nhắc là thủ đô của Canada là gì?

Cơ sở dữ liệu vectơ của bạn có thể truy xuất các tài liệu có liên quan về mặt ngữ nghĩa

nhưng không trả lời trực tiếp câu hỏi.

Ví dụ: cụm từ Toronto ở Canada,

thủ đô của Pháp là Paris,

hay Canada là thủ đô si rô phong của thế giới

tất cả đều có liên quan về mặt ngữ nghĩa với lời nhắc

nhưng cuối cùng không trả lời câu hỏi.

Đây là nơi người xếp hạng lại có thể đến để chấm điểm và xếp hạng lại các kết quả này

để cuối cùng chỉ những tài liệu thực sự có liên quan mới được trả lại.

Trong các hệ thống sử dụng trình xếp hạng lại,

bạn thường sẽ tìm nạp quá nhiều tài liệu trong quá trình truy xuất cơ sở dữ liệu vectơ ban đầu của mình.

Ví dụ: bạn có thể truy xuất khoảng từ 20 đến 100 tài liệu hoặc các đoạn

sử dụng phương pháp tìm kiếm lai điển hình.

Sau đó, trình xếp hạng lại sẽ được sử dụng để chấm điểm lại các tài liệu này

dẫn đến xếp hạng cuối cùng.

Cuối cùng, bạn vẫn sẽ chỉ trả lại một tập hợp con tài liệu

được truy xuất bằng tìm kiếm vectơ, có lẽ từ 5 đến 10.

Tuy nhiên, nhờ có người xếp hạng lại,

những tài liệu được xếp hạng lại này sẽ phù hợp hơn nhiều

hơn có thể xảy ra nếu bạn chỉ thực hiện một tìm kiếm kết hợp đơn giản.

Thông thường, những người xếp hạng lại có kiến ​​trúc mã hóa chéo.

Như bạn đã thấy trước đó, bộ mã hóa chéo mang lại kết quả tốt hơn

hơn bộ mã hóa kép tiêu chuẩn

nhưng chậm hơn đáng kể và không khả thi để sử dụng

với hàng triệu hoặc hàng tỷ tài liệu.

Nếu bộ mã hóa kép đã thu hẹp danh sách tài liệu

tuy nhiên, điều đó cần phải được xem xét,

đột nhiên sự đánh đổi giữa chất lượng và thời gian trở nên có ý nghĩa hơn rất nhiều.

Bộ mã hóa chéo sẽ tăng thêm một chút độ trễ cho toàn bộ hệ thống của bạn

ngay cả khi chỉ xếp hạng lại 20 đến 100 tài liệu như trường hợp thông thường.

Tuy nhiên, sự đánh đổi này hầu như luôn có giá trị.

Việc xếp hạng lại dựa trên LLM cũng đang được sử dụng ngày càng nhiều.

Ý tưởng này khá giống với một bộ mã hóa chéo

nhưng thay vì cung cấp cặp tài liệu nhanh chóng cho bộ mã hóa chéo để sắp xếp lại,

nó được cung cấp trực tiếp cho LLM.

LLM được thiết kế đặc biệt cho nhiệm vụ này có thể phân tích cặp,

đánh giá mức độ liên quan của chúng và trả lời bằng điểm số liên quan.

Mặc dù đầy hứa hẹn nhưng cách tiếp cận này về cơ bản không hiệu quả như một bộ mã hóa chéo.

Trong cả hai trường hợp, việc tính điểm không thể bắt đầu cho đến khi nhận được lời nhắc.

Và chấm điểm một tài liệu riêng lẻ vẫn là một hoạt động tương đối tốn kém.

Do đó, việc tính điểm dựa trên LLM có thể được cải tiến hơn nữa

nhưng nó sẽ vẫn là một kỹ thuật sắp xếp lại chỉ có thể được sử dụng

sau khi tìm kiếm vectơ điển hình đã thu hẹp danh sách tài liệu cần được xếp hạng lại.

Mặc dù hệ thống RAG không yêu cầu nghiêm ngặt việc sử dụng việc sắp xếp lại,

nó thường khá dễ thực hiện và mang lại hiệu suất tốt hơn nhiều.

Đối với nhiều cơ sở dữ liệu vectơ, việc này có thể đơn giản chỉ là thêm một dòng vào truy vấn tìm kiếm của bạn

cho biết bạn muốn sử dụng trình xếp hạng lại.

Do đó, sử dụng re-ranker là một trong những kỹ thuật đầu tiên bạn nên khám phá

thêm vào quy trình RAG của bạn khi cố gắng cải thiện mức độ liên quan của tìm kiếm.

Thông thường, bạn có thể tìm nạp quá mức 15 đến 25 tài liệu

và sau đó xếp hạng lại giữa chúng để tăng mức độ liên quan

với cái giá phải trả là độ trễ tăng thêm một chút.