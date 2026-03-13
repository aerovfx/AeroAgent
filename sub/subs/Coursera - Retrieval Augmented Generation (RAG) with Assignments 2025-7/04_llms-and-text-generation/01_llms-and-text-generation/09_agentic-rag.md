# 09 chất tẩy rửa

---

Khi hệ thống RAG của bạn trưởng thành,

một cách mạnh mẽ để cải thiện hiệu suất của nó

là bắt đầu giới thiệu quy trình làm việc tổng thể.

Một quy trình làm việc tác nhân có nghĩa là sử dụng

một số LLM trong toàn bộ hệ thống RAG của bạn,

mỗi người chịu trách nhiệm về

một bước duy nhất trong toàn bộ quá trình.

Bạn đã thấy ý tưởng này với LLM được sử dụng để

thực hiện các tác vụ như mở rộng truy vấn,

viết lại nhanh chóng hoặc tạo trích dẫn.

Có rất nhiều hệ thống phức hợp

như thế này bạn có thể xây dựng.

Vì vậy, hãy xem xét cách bạn có thể cải thiện hơn nữa

chất lượng của hệ thống RAG của bạn

bằng cách xây dựng nó một cách tự động.

Thông thường, cách bạn sử dụng mô hình ngôn ngữ

là đưa ra một lời nhắc và nó sẽ đưa ra phản hồi.

Đơn giản.

Trong một hệ thống đại lý,

có hai thay đổi chính đối với mô hình này.

Đầu tiên, các nhiệm vụ hiện được xử lý

như một chuỗi các bước và quyết định,

mỗi trong số đó có thể được hoàn thành

bằng một cuộc gọi đến một LLM khác.

Thứ hai, LLM được cấp quyền truy cập vào nhiều công cụ hơn

như trình thông dịch mã, trình duyệt web,

hoặc trong trường hợp của RAG,

một cơ sở dữ liệu vector thông tin để tham khảo.

Đây là một quy trình làm việc tổng thể khả thi cho hệ thống RAG.

Người dùng gửi lời nhắc tới hệ thống

và đầu tiên nó được xử lý bởi một bộ định tuyến nhỏ LLM.

Công việc của LLM này là xác định

nếu lời nhắc thực sự yêu cầu một cuộc gọi

vào cơ sở dữ liệu vectơ.

Nó được điều chỉnh đặc biệt cho nhiệm vụ này

và sẽ chỉ xuất ra có,

có nghĩa là lời nhắc biện minh cho việc truy xuất

từ cơ sở dữ liệu, hoặc không,

có nghĩa là lời nhắc có thể được trả lời mà không cần truy xuất.

Dựa trên quyết định của bộ định tuyến LLM,

lời nhắc sẽ được gửi tới cơ sở dữ liệu vector

để truy xuất hoặc bỏ qua bước đó.

Nếu việc truy xuất không được hoàn tất,

lời nhắc được gửi trực tiếp đến một LLM riêng

để tạo ra phản hồi.

Nếu một bước truy xuất được yêu cầu,

một người đánh giá riêng LLM được sử dụng để xác định

nếu các tài liệu được truy xuất là đủ

để trả lời câu hỏi.

Dựa trên quyết định của người đánh giá LLM này,

truy xuất bổ sung từ cơ sở dữ liệu vector

có thể được yêu cầu.

Sau khi đã lấy đủ thông tin,

một lời nhắc tăng cường được xây dựng

và được đưa cho LLM để tạo ra phản hồi.

Tại thời điểm này, LLM cuối cùng sẽ trải qua phản hồi này

và thêm trích dẫn.

Đây chỉ là một hệ thống RAG tác nhân khả thi,

nhưng nó nhấn mạnh một số điểm chính

điều đó đúng với bất kỳ hệ thống tác nhân nào.

Đầu tiên bạn có thể nghĩ tới việc thiết kế một hệ thống Agent

về cơ bản giống như vẽ một biểu đồ dòng chảy.

Mỗi LLM trong sơ đồ vẫn chỉ nhập văn bản

và tạo đầu ra văn bản,

nhưng hệ thống đã được thiết lập

để mỗi LLM hoàn thành một nhiệm vụ

trên hành trình của lời nhắc thông qua hệ thống RAG.

Thứ hai, bạn không cần sử dụng cùng một LLM

cho từng bước trong quy trình làm việc.

Bộ định tuyến và bộ đánh giá LLM trong hệ thống đại lý này

có thể là những mô hình nhẹ, chạy nhanh và rẻ

vì họ có một nhiệm vụ duy nhất và tương đối đơn giản.

Sau đó bạn có thể sử dụng một mô hình lớn hơn

để tạo ra phản hồi dự thảo

và chọn một mô hình chuyên về tạo trích dẫn

cho bước đó.

Khi bạn nghĩ đến việc thêm quy trình làm việc tổng đài

vào ứng dụng RAG của bạn,

Dưới đây là một số mẫu phổ biến cần xem xét.

Một quy trình làm việc tuần tự chỉ di chuyển đầu ra theo kiểu tuyến tính

thông qua một loạt LLM.

Điều này có thể có nghĩa là mọi lời nhắc được gửi tới hệ thống của bạn

di chuyển qua trình phân tích cú pháp truy vấn dựa trên LLM,

trình ghi lại truy vấn và trình tạo trích dẫn

như một phần của quá trình tạo ra.

Mỗi LLM chỉ tập trung vào một bước của quy trình tổng thể

và do đó có thể chuyên môn hóa ở bước đó.

Quy trình làm việc có điều kiện sử dụng LLM để quyết định

lời nhắc nên đi theo đường dẫn nào trong số nhiều đường dẫn.

Bạn vừa thấy một bộ định tuyến LLM triển khai quy trình làm việc này

để quyết định xem việc truy xuất có cần thiết hay không

để trả lời một lời nhắc.

Bạn cũng có thể sử dụng bộ định tuyến để xác định

cái nào trong số một số LLM

với thế mạnh và chuyên môn khác nhau

nên được sử dụng để tạo ra phản hồi.

Một quy trình làm việc lặp lại hoạt động tương tự

đến một quy trình làm việc có điều kiện,

nhưng nó định tuyến lời nhắc tới điểm trước đó

trong hệ thống tổng thể, tạo thành một vòng lặp.

Ví dụ: nếu hệ thống RAG của bạn được thiết kế để tạo mã

tích hợp với cơ sở mã hiện có,

có thể hệ thống sẽ cần nhiều lần thử

để viết mã làm việc.

Người đánh giá LLM có thể được sử dụng để đánh giá từng dự thảo,

có lẽ với sự hỗ trợ của một trình thông dịch mã

và cung cấp phản hồi cho đến khi thấy giải pháp phù hợp.

Cuối cùng, bạn có thể tạo quy trình công việc song song

trong đó một mô hình ngôn ngữ điều phối

chia lời nhắc thành nhiều tác vụ riêng biệt

và phân công từng nhiệm vụ cho các LLM riêng biệt.

Mặt khác, một mô hình ngôn ngữ tổng hợp

kết hợp lại công việc của họ

Nếu ứng dụng của bạn nói, hãy so sánh những hiểu biết chính

từ hai tài liệu nghiên cứu,

bạn có thể muốn hai LLM khác nhau

để tóm tắt và đánh giá từng cái

và sau đó yêu cầu người điều phối kết hợp những phát hiện của họ.

Đối với các hệ thống tác nhân đơn giản,

bạn chỉ có thể thực hiện logic

về quy trình làm việc mà bạn mong muốn.

Tuy nhiên, khi mọi thứ trở nên phức tạp hơn,

có rất nhiều công cụ, thư viện và nền tảng

được thiết kế để giúp bạn xây dựng và quản lý một hệ thống đại lý.

Khả năng sáng tạo khi xây dựng hệ thống Agent

thực sự là vô tận.

Ngoài ra còn có một sự thay đổi tư duy quan trọng đang diễn ra ở đây.

LLM bắt đầu trông ít giống các giải pháp độc lập hơn

và giống như các phần mô-đun hơn

phù hợp với quy trình làm việc lớn hơn.

Đột nhiên, bạn rất vui khi sử dụng các mô hình nhỏ hơn

hoặc những người mẫu chỉ xuất sắc ở một vài nhiệm vụ

bởi vì khả năng của họ rất phù hợp

với các phần của quy trình làm việc mà họ chịu trách nhiệm.

Việc thêm các thành phần tác nhân có thể mang lại cho bạn sự linh hoạt

để xây dựng các hệ thống RAG có khả năng cao hơn nữa.