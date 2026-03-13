# Tổng kết 01 khóa học

---

Chúc mừng bạn đã hoàn thành khóa học này! Bây giờ bạn đã đạt được sự hiểu biết toàn diện

xây dựng các ứng dụng Gen AI. Bạn có thể bắt đầu khám phá các cơ hội để tiếp tục học tập

và áp dụng các kỹ năng có được của bạn. Nhưng trước đó, hãy xem lại một số thành phần chính mà bạn

được học trong suốt khóa học. Các mô hình AI sáng tạo đề cập đến các hệ thống AI

có thể dự đoán và tạo ra nội dung mới như văn bản, hình ảnh, mã và âm thanh dựa trên

dữ liệu đầu vào. Các mô hình cơ bản là một tập hợp con của các mô hình AI tổng quát bao gồm ngôn ngữ lớn

mô hình hoặc LLM. Lời nhắc là những hướng dẫn hoặc thông tin đầu vào được đưa ra cho

một LLM được thiết kế để hướng dẫn nó thực hiện một nhiệm vụ cụ thể hoặc tạo ra kết quả đầu ra mong muốn.

Có hai thành phần nhắc nhở. Hướng dẫn là các lệnh rõ ràng, cụ thể cho biết

Hệ thống AI phải làm gì. Bối cảnh bao gồm thông tin cần thiết hoặc nền tảng giúp LLM

hiểu ý nghĩa của lời hướng dẫn. Lời nhắc có thể bao gồm hướng dẫn nhiệm vụ, thông tin đầu vào

dữ liệu, bối cảnh và ví dụ. Mặc dù các tham số của mô hình ảnh hưởng đến đầu ra nhưng chúng không

một phần của lời nhắc. Trong bối cảnh, học tập là một phương pháp cụ thể

về kỹ thuật nhanh chóng trong đó việc trình diễn nhiệm vụ được cung cấp như một phần của lời nhắc

bằng ngôn ngữ tự nhiên. Nó không yêu cầu bất kỳ sự đào tạo nào và một nhiệm vụ mới được học từ một

tập hợp nhỏ các ví dụ được trình bày trong ngữ cảnh tại thời điểm suy luận.

Chúng ta hãy tóm tắt lại các kỹ thuật nhắc nhở quan trọng. Đầu tiên là lời nhắc không bắn, hướng dẫn

một LLM để thực hiện một nhiệm vụ không có ví dụ. Nó dựa hoàn toàn vào kiến ​​thức được đào tạo trước của nó.

Tiếp theo là lời nhắc một lần, cung cấp cho LLM một ví dụ duy nhất cùng với

hướng dẫn để giúp nó thực hiện một nhiệm vụ. Lời nhắc vài cảnh sử dụng một số ví dụ nhỏ

để giúp LLM khái quát hóa các mẫu và áp dụng việc học của nó để thực hiện một nhiệm vụ.

Chuỗi suy nghĩ hoặc lời nhắc COT hướng dẫn LLM thông qua lý luận phức tạp theo từng bước

cách. Tính tự nhất quán nâng cao độ tin cậy của kết quả đầu ra bằng cách tạo ra nhiều lý luận

đường dẫn hoặc câu trả lời, sau đó chọn đường dẫn phù hợp nhất hoặc thường xuyên nhất.

Lang chain là một framework mã nguồn mở giúp đơn giản hóa quá trình phát triển ứng dụng

sử dụng LLM. Nó chứa các thành phần như mô hình ngôn ngữ, mô hình trò chuyện, tin nhắn trò chuyện,

mẫu phản hồi, trình phân tích cú pháp đầu ra. Chuỗi là một chuỗi các cuộc gọi. Một tuần tự

chuỗi bao gồm một loạt các bước, mỗi bước lấy một đầu vào để tạo ra một đầu ra. các

đầu ra của bước 1 trở thành đầu vào của bước 2, v.v. Tác nhân là hệ thống động, trong đó

mô hình ngôn ngữ xác định chuỗi hành động, chẳng hạn như chuỗi được xác định trước. mô hình

tạo ra kết quả đầu ra dựa trên văn bản để hướng dẫn những hành động này. Đại lý có thể sử dụng các công cụ tích hợp như

như cơ sở dữ liệu và công cụ tìm kiếm để thu thập thông tin hoặc thực hiện các nhiệm vụ đáp ứng

yêu cầu của người dùng.

Ngôn ngữ biểu thức chuỗi lang hoặc LCEL là mẫu để xây dựng các ứng dụng chuỗi lang

sử dụng toán tử đường ống để kết nối các thành phần. Phương pháp này đảm bảo sạch sẽ,

luồng dữ liệu có thể đọc được từ đầu vào đến đầu ra. LCEL cung cấp các phím tắt cú pháp tinh tế. cho

Ví dụ: thay vì sử dụng chuỗi có thể chạy được, một chuỗi tuần tự tương tự có thể được tạo

bằng cách đơn giản kết nối các thành phần bằng một đường ống, làm cho cấu trúc dễ đọc và trực quan hơn.

Dưới đây là bản tóm tắt ngắn gọn về các mô hình AI được đề cập trong khóa học này.

Llama3 cung cấp khả năng hiểu ngữ cảnh nâng cao đồng thời xử lý tốt hơn các sắc thái

vấn đề. Nó được biết đến với khả năng suy luận nâng cao.

Granite là mô hình ngôn ngữ tiên tiến của IBM và là một phần của nền tảng watsonx.ai. Nó

được tối ưu hóa cho các trường hợp sử dụng của doanh nghiệp và mang lại hiệu suất mạnh mẽ trong kinh doanh và

các lĩnh vực kỹ thuật.

Mixtro sử dụng hỗn hợp các hệ thống chuyên gia, trong đó mỗi lớp có 8 mô hình con chuyên gia và chỉ

hai cái phù hợp nhất được kích hoạt cho mỗi suy luận hoặc nhiệm vụ. Nó cung cấp khả năng thích ứng cao do

các chuyên gia chuyên ngành, cho phép tinh chỉnh cho các nhu cầu cụ thể. Nó hiệu quả vì nó

chỉ kích hoạt các chuyên gia cần thiết, giúp tiết kiệm tài nguyên cho các nhiệm vụ đa dạng.

Nếu bạn chưa đăng ký chương trình chứng chỉ chuyên nghiệp bao gồm khóa học này,

chúng tôi khuyến khích bạn làm như vậy. Tùy thuộc vào lịch trình của bạn và số lượng các khóa học trong

chương trình, bạn có thể hoàn thành nó trong khoảng 2 đến 6 tháng. Nếu quan tâm, các liên kết đến

các khóa học trong chương trình này nằm trong phần chúc mừng và đọc các bước tiếp theo ở cuối chương trình này

tất nhiên.

Chúng tôi khuyên bạn nên tiếp tục áp dụng kiến thức thu được từ khóa học này vào công việc của mình.

Sự nghiệp của thế hệ AI. Chúng tôi hy vọng những nguyên tắc này sẽ hoàn thiện kỹ năng của bạn và giúp bạn thăng tiến

một cách chuyên nghiệp.

Chúc mừng bạn đã hoàn thành khóa học này. Chúng tôi đánh giá cao sự tham gia của bạn vào việc học này

cuộc hành trình và chúc bạn mọi điều tốt đẹp nhất!