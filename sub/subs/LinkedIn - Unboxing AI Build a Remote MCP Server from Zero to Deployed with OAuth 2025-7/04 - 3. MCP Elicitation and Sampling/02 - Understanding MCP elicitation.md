# 02 - Tìm hiểu về suy luận MCP

---

- Vậy gợi hứng là gì?

Tôi phải thừa nhận, là một người hơi bị ám ảnh bởi ngôn ngữ,

khi lần đầu tiên tôi nhìn thấy và nghe thấy từ khơi gợi

liên quan đến MCP,

nó gây ra một số phản ứng trong tôi

bởi vì khơi gợi và khơi gợi một cái gì đó

là một từ kỳ lạ để sử dụng cho việc này,

và nó cũng nghe rất giống gợi ý,

đó không phải là điều tương tự.

Vậy...

Nhưng tôi không đưa ra những quyết định này, người khác sẽ làm.

Kích thích là khi một máy chủ MCP

gửi lại câu hỏi cho người dùng.

Nó gợi ra phản hồi từ người dùng máy chủ MCP

để giải quyết một số việc gì đó

hoặc để biết thêm thông tin, v.v.

Đó là một cách tạo ra sự qua lại giữa người dùng,

mô hình ngôn ngữ

thực ra là đang nói chuyện với máy chủ MCP,

và máy chủ MCP

vì có nhiều hoàn cảnh

nơi mô hình ngôn ngữ

có thể không chuyển đủ thông tin vào máy chủ MCP

để máy chủ MCP thực hiện công việc của nó.

Hoặc có thể có trường hợp máy chủ MCP

đang trải qua một quá trình,

và khi nó trải qua quá trình đó,

nó cần thêm thông tin từ người dùng,

và yêu cầu đó sau đó có thể được đưa ra vào thời điểm cần thiết

từ máy chủ MCP

để đảm bảo rằng người dùng thực sự tương tác với nó.

Vì vậy đây một phần là cách giới thiệu một con người vào vòng lặp

và một phần là cách giải quyết vấn đề

nếu không thì sẽ thực sự khó lập trình.

Ví dụ: nếu bạn đang yêu cầu một dịch vụ

và dịch vụ phục vụ...

Và dịch vụ trả về 10 phản hồi thay vì một,

và máy chủ MCP sau đó phải đưa ra lựa chọn, phải không?

Máy chủ thời tiết mà tôi đã xây dựng

có một ví dụ tích hợp về điều này.

Nếu bạn truy cập Open Media Geo...

API mã hóa địa lý,

đó là những gì đang được sử dụng trong máy chủ MCP đó,

nếu bạn yêu cầu một tên địa điểm duy nhất, chẳng hạn như Oslo,

sau đó bạn nhận được một kết quả.

Nếu bạn yêu cầu tên vị trí không phải là duy nhất,

như Springfield, hay London, hay Berlin,

máy định vị địa lý...

Không, máy chủ Mã hóa địa lý

sẽ trả về tuy nhiên có nhiều mục tồn tại cho vị trí đó.

Trong trường hợp của Berlin, nó là hơn 10.

Bây giờ, Berlin, Đức là lựa chọn đầu tiên,

nhưng không có gì đảm bảo

đó chính là điều người dùng thực sự đang tìm kiếm.

Và khi người dùng đang nói chuyện với LLM,

và LLM đang nói chuyện với máy chủ MCP,

và LLM vừa đi qua Berlin,

thì máy chủ MCP không có cách nào biết được

bạn đang nói về Berlin nào

Và sau đó để xây dựng máy chủ MCP,

bạn có thể làm những gì tôi đã làm trong ví dụ trước,

vừa mới nói,

"Hãy chọn cái đầu tiên, nhưng nó có thể sai."

Hoặc bạn có thể gợi ra phản hồi từ người dùng để nói:

"Này, đây là danh sách những người Berlin khác nhau.

Bạn đang tìm cái nào?"

Và sau đó người dùng phải đưa ra phản hồi

để làm điều đó xảy ra.

Đó là mục đích của nó.