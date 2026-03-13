# 05 rag-kiến trúc-tổng quan

---

Bạn đã thấy các thành phần quan trọng nhất trong hệ thống RAG, cụ thể là bản thân LLM, kiến thức

cơ sở thông tin liên quan và một công cụ tìm kiếm có thể tìm kiếm cơ sở tri thức. Bây giờ chúng ta hãy

xem xét kiến trúc tổng thể của hệ thống RAG và cách các thành phần này hoạt động cùng nhau.

Hãy bắt đầu bằng cách xem cách bạn thường sử dụng mô hình ngôn ngữ lớn. Bạn gõ một lời nhắc

và gửi nó tới LLM. LLM xử lý lời nhắc và tạo ra phản hồi.

Trải nghiệm người dùng đối với hệ thống RAG thực sự giống hệt nhau. Bạn gửi lời nhắc và nhận lại một

phản hồi. Tuy nhiên, bên trong hệ thống còn có một vài bước nữa. Khi hệ thống RAG nhận được

nhắc, đầu tiên nó sẽ định tuyến nó đến bộ thu hồi. Người săn mồi có quyền truy cập vào cơ sở kiến thức,

mà thực tế mà nói chỉ là một cơ sở dữ liệu gồm những tài liệu hữu ích. Người truy vấn truy vấn

cơ sở dữ liệu, trả về các tài liệu mà nó xác định là phù hợp nhất với lời nhắc. Tiếp theo, hệ thống

tạo ra một lời nhắc tăng cường, kết hợp thông tin từ các tài liệu liên quan vào

lời nhắc ban đầu. Ví dụ: lời nhắc tăng cường có thể là trả lời câu hỏi sau,

Tại sao khách sạn ở Vancouver lại đắt vào cuối tuần tới? Dưới đây là năm bài viết có liên quan

điều đó có thể giúp bạn phản hồi, sau đó chèn văn bản từ bài viết. Lúc này, hệ thống

hoạt động giống như bất kỳ LLM nào khác. Lời nhắc tăng cường được gửi đến LLM và nó tạo ra phản hồi.

LLM có thể phản hồi dựa trên cả kiến thức mà nó học được từ dữ liệu đào tạo của mình,

cũng như bất kỳ ngữ cảnh bổ sung nào được cung cấp bởi các tài liệu được truy xuất. Trải nghiệm người dùng

vẫn giống như mọi khi, có lẽ có thêm một chút độ trễ. Bạn gõ một lời nhắc và bạn nhận được

trả lời lại. Tuy nhiên, nhờ có con đường phụ đó xuyên qua chó săn nên có khả năng cao hơn

phản hồi là chính xác, cập nhật và nhận biết được bối cảnh. Như bạn vừa thấy, sự khác biệt chính giữa

sử dụng LLM trực tiếp và hệ thống RAG là sự bổ sung của chó săn. Điều này khá đơn giản

Tuy nhiên, sự bổ sung này mang lại một số lợi thế. Đầu tiên và quan trọng nhất, nó tạo ra thông tin

có sẵn cho LLM mà có thể không có. Cho dù đó là chính sách của công ty, một phần thông tin cá nhân

thông tin, hoặc các tiêu đề sáng nay, RAG thường là cách duy nhất để tạo ra một số loại thông tin

có sẵn cho LLM. Liên quan đến điểm đầu tiên này, RAG làm giảm khả năng xảy ra ảo giác hoặc

những phản hồi gây nhầm lẫn. Những điều này thường xảy ra do LLM tạo ra phản hồi về các chủ đề

đã bị loại khỏi dữ liệu đào tạo của họ hoặc có lẽ hiếm khi được đề cập đến. Thêm liên quan

thông tin trực tiếp trong lời nhắc làm cơ sở cho các câu trả lời của mô hình ngôn ngữ và làm cho chúng ít hơn

có khả năng tạo ra văn bản chung chung hoặc gây hiểu nhầm. RAG giúp việc cập nhật LLM dễ dàng hơn nhiều với

thông tin thay đổi nhanh chóng. Đào tạo lại một mô hình ngôn ngữ thường tốn kém và mất thời gian

kỳ tích, vì vậy LLM phải vật lộn để theo kịp những thông tin rất mới. Tuy nhiên, trong hệ thống RAG, bạn có thể

chỉ cần cập nhật thông tin trong cơ sở kiến thức giống như bạn cập nhật các mục trong bất kỳ cơ sở kiến thức nào khác.

cơ sở dữ liệu. Ngay sau khi những thay đổi đó được lập chỉ mục, LLM của bạn sẽ có thể phản hồi dựa trên thông tin mới

thông tin. RAG cải thiện khả năng trích dẫn nguồn của LLM. Hệ thống RAG có thể thêm thông tin trích dẫn

đến lời nhắc tăng cường và LLM sau đó có thể đưa thông tin đó vào phản hồi cuối cùng của nó.

Điều này không chỉ tạo cơ sở cho câu trả lời mà còn cho phép người đọc tìm hiểu sâu hơn và xác thực

văn bản được tạo ra. Cuối cùng, RAG cho phép LLM tập trung vào việc tạo văn bản này. Bộ lọc tha mồi xuống

một thế giới thông tin rộng lớn, tìm thấy những gì quan trọng và phù hợp nhất, đồng thời trình bày nó một cách ngắn gọn.

LLM vẫn cần viết phản hồi tốt, nhưng nó không được dựa vào để tìm hiểu thực tế hoặc

các bước lọc Nói cách khác, mỗi thành phần được giao nhiệm vụ làm việc trên lĩnh vực lớn nhất của nó.

sức mạnh. Khi kết thúc khóa học này, bạn sẽ đi sâu vào việc xây dựng hệ thống RAG từ đầu,

nhưng đây là đoạn mã demo rất đơn giản về cách hoạt động của RAG, với hầu hết các chi tiết đã được trừu tượng hóa.

Tôi có chức năng truy xuất và chức năng tạo. Chức năng truy xuất là một trình bao bọc

xung quanh một con chó săn. Nó chấp nhận một truy vấn văn bản và trả về các tài liệu liên quan từ cơ sở tri thức.

Hàm tạo chỉ là một trình bao bọc xung quanh một mô hình ngôn ngữ lớn. Nó chấp nhận một lời nhắc văn bản

và trả về phản hồi của LLM. Tôi sẽ viết một lời nhắc và lưu nó vào biến dấu nhắc.

Câu hỏi đặt ra là tại sao giá khách sạn ở Vancouver cuối tuần này lại siêu đắt?

Bây giờ, hãy gửi lời nhắc trực tiếp tới LLM của chúng tôi và xem câu trả lời trả về là gì.

Được rồi, bây giờ hãy xem chú chó tha mồi của chúng ta có thông tin bổ sung gì về lời nhắc này, như thế này.

Và bây giờ, hãy xây dựng một lời nhắc tăng cường chứa cả câu hỏi ban đầu của người dùng

và thông tin được truy xuất. Vì vậy, ở đây, lời nhắc tăng cường sẽ đọc, hãy trả lời câu hỏi sau

nhắc nhở. Chúng tôi thêm lời nhắc của mình bằng cách sử dụng thông tin được lấy sau đây để giúp bạn trả lời. Và

sau đó chúng tôi thêm vào các tài liệu đã truy xuất của mình. Bây giờ hãy gửi lời nhắc tăng cường này tới LLM của chúng tôi. Bây giờ

LLM có thể đưa ra câu trả lời chính xác cho câu hỏi, tích hợp thông tin

được lấy ra từ cơ sở tri thức. Đó thực sự là tất cả những gì có ở RAG. Bổ sung thêm

bối cảnh theo lời nhắc của bạn để giúp LLM phản hồi chính xác hơn. Phải thừa nhận rằng đây là một mức rất cao

tổng quan về mức độ của kiến trúc RAG. Hãy tham gia cùng tôi trong video tiếp theo và chúng ta sẽ bắt đầu xem xét

từng thành phần một cách chi tiết hơn.