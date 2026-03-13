# 04 thế hệ-ai-llms

---

Được rồi, chúng ta hãy bắt đầu, trong bài học này,

chúng ta sẽ dựng bối cảnh.

Chúng ta sẽ nói về các mô hình ngôn ngữ lớn,

trường hợp sử dụng của họ,

cách các mô hình hoạt động, kỹ thuật nhanh chóng,

cách tạo đầu ra văn bản sáng tạo,

và phác thảo vòng đời dự án cho

các dự án AI mang tính sáng tạo.

Vì sự quan tâm của bạn đối với khóa học này,

có lẽ nó an toàn

để nói rằng bạn đã có cơ hội để thử

một công cụ AI có tính sáng tạo hoặc muốn.

Cho dù đó là bot trò chuyện,

tạo hình ảnh từ văn bản, hoặc

sử dụng plugin để giúp bạn phát triển mã,

những gì bạn thấy trong những công cụ này là một cỗ máy

có khả năng tạo ra nội dung

bắt chước hoặc gần đúng khả năng của con người.

AI sáng tạo là một tập hợp con của

học máy truyền thống.

Và các mô hình học máy

làm nền tảng cho AI sáng tạo có

đã học được những khả năng này bằng cách tìm

mô hình thống kê hàng loạt

tập dữ liệu về nội dung đã được

ban đầu do con người tạo ra.

Các mô hình ngôn ngữ lớn đã được đào tạo

trên hàng nghìn tỷ từ trong nhiều tuần và

tháng, và

với sức mạnh tính toán lớn.

Những mô hình nền tảng này, như chúng tôi gọi,

với hàng tỷ tham số,

thể hiện những đặc tính nổi bật vượt ra ngoài

riêng ngôn ngữ, và các nhà nghiên cứu

đang mở khóa khả năng phá vỡ của họ

nhiệm vụ phức tạp, lý do và giải quyết vấn đề.

Dưới đây là bộ sưu tập nền tảng

mô hình, đôi khi được gọi là mô hình cơ sở,

và kích thước tương đối của chúng trong

các tham số của chúng.

Bạn sẽ đề cập đến các thông số này trong

chi tiết hơn một chút sau này, nhưng

bây giờ,

hãy coi chúng như ký ức của người mẫu.

Và mô hình càng có nhiều tham số,

bộ nhớ càng nhiều, và

hóa ra, càng phức tạp

các nhiệm vụ nó có thể thực hiện.

Trong suốt khóa học này, chúng tôi sẽ đại diện

LLM có các vòng tròn màu tím này và

trong phòng thí nghiệm, bạn sẽ tận dụng

một mô hình nguồn mở cụ thể, flan-T5,

thực hiện các nhiệm vụ ngôn ngữ.

Bằng cách sử dụng các mô hình này như

họ đang hoặc bằng cách áp dụng tinh chỉnh

kỹ thuật để điều chỉnh chúng cho phù hợp với bạn

trường hợp sử dụng cụ thể, bạn có thể nhanh chóng xây dựng

giải pháp tùy chỉnh mà không cần

để đào tạo một mô hình mới từ đầu.

Bây giờ, trong khi AI sáng tạo

các mô hình đang được tạo ra cho

nhiều phương thức,

bao gồm hình ảnh, video, âm thanh và

bài phát biểu, trong khóa học này bạn sẽ

tập trung vào các mô hình ngôn ngữ lớn và

việc sử dụng chúng trong việc tạo ra ngôn ngữ tự nhiên.

Bạn sẽ thấy chúng được xây dựng như thế nào và

được đào tạo,

cách bạn có thể tương tác với họ

thông qua văn bản được gọi là lời nhắc.

Và cách tinh chỉnh mô hình cho

trường hợp sử dụng và dữ liệu của bạn, và

cách bạn có thể triển khai chúng bằng các ứng dụng

để giải quyết các nhiệm vụ kinh doanh và xã hội của bạn.

Cách bạn tương tác với các mô hình ngôn ngữ

khá khác biệt so với các máy khác

mô hình học tập và lập trình.

Trong những trường hợp đó,

bạn viết mã máy tính bằng cách chính thức hóa

cú pháp để tương tác với các thư viện và

API.

Ngược lại, các mô hình ngôn ngữ lớn

có thể sử dụng ngôn ngữ tự nhiên hoặc

hướng dẫn bằng văn bản của con người và

thực hiện các nhiệm vụ giống như con người.

Văn bản mà bạn chuyển đến

LLM được gọi là lời nhắc.

Không gian hoặc bộ nhớ có sẵn để

dấu nhắc được gọi là cửa sổ ngữ cảnh,

và điều này thường đủ lớn để

vài ngàn từ nhưng

khác nhau từ mô hình này sang mô hình khác.

Trong ví dụ này,

bạn yêu cầu người mẫu xác định vị trí

Ganymede nằm trong hệ mặt trời.

Lời nhắc được chuyển đến mô hình,

mô hình sau đó dự đoán các từ tiếp theo và

vì lời nhắc của bạn có chứa một câu hỏi,

mô hình này tạo ra một câu trả lời.

Đầu ra của mô hình

được gọi là sự hoàn thành,

và hành động sử dụng mô hình để

tạo ra văn bản được gọi là suy luận.

Phần hoàn thiện bao gồm văn bản

có trong lời nhắc ban đầu,

theo sau là văn bản được tạo ra.

Bạn có thể thấy mô hình này đã làm rất tốt

công việc trả lời câu hỏi của bạn

Nó xác định chính xác rằng Ganymede là một

mặt trăng của sao Mộc và tạo ra một sự hợp lý

trả lời câu hỏi của bạn nói rằng

mặt trăng nằm trong quỹ đạo của sao Mộc.

Bạn sẽ thấy rất nhiều ví dụ về lời nhắc và

hoàn thiện theo phong cách này

trong suốt khóa học.