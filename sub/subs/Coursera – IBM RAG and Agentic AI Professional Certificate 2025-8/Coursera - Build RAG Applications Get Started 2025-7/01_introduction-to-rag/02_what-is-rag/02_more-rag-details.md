# 02 chi tiết khác

---

Chào mừng đến với việc truy xuất

Thế hệ tăng cường hoặc RAG.

Sau khi xem video này,

bạn sẽ có thể

giải thích quá trình RAG.

Bạn cũng sẽ có thể

mô tả các bước khác nhau

trong quy trình RAG

để nhận được phản hồi hiệu quả

cho các câu hỏi hoặc

nhắc bạn nhập.

Đầu tiên chúng ta hãy hiểu

RAG là gì.

RAG là một khung AI

điều đó giúp tối ưu hóa

sản lượng lớn

mô hình ngôn ngữ hoặc LLM.

RAG sử dụng khả năng của

LLM và các miền cụ thể

hoặc cơ sở dữ liệu nội bộ của

một tổ chức không có

đào tạo lại người mẫu.

LLM được đào tạo trước

có thể phải đối mặt với những thách thức

với kiến thức về lĩnh vực cụ thể

mà họ không được đào tạo.

Trong khi họ biểu diễn

làm tốt các công việc chung,

họ có thể cung cấp

phản hồi không chính xác

đến các truy vấn chuyên biệt.

Vì vậy, việc bổ sung bên ngoài

nguồn kiến thức liên quan

giúp đảm bảo hơn

những phản hồi chính xác.

Hãy xem xét một ví dụ về một

chính sách di động của công ty.

Nếu bạn hỏi một chatbot về

chính sách di động của công ty,

chatbot sẽ

cung cấp câu trả lời từ

cơ sở kiến thức của nó bởi vì

chính sách của công ty bao gồm

thông tin mật.

Vì vậy, để tạo ra

phản hồi cụ thể về miền,

quy trình RAG rất hữu ích.

Hãy cùng khám phá RAG giúp ích như thế nào

trong việc tạo ra các phản hồi.

Dựa trên đã chèn

nội dung hoặc lời nhắc,

RAG kết hợp lấy

thông tin và

tạo ra ngôn ngữ tự nhiên

để tạo ra những phản hồi.

RAG sử dụng nhiều nội dung khác nhau

từ nền tảng kiến thức của nó,

bao gồm dữ liệu từ

chatbot được đào tạo,

chính sách công ty không có sẵn trên

Internet và

những tài liệu lớn.

RAG bao gồm hai thành phần chính

các thành phần, bộ thu hồi,

cốt lõi của RAG,

và máy phát điện,

có chức năng như một chatbot.

Trong quá trình RAG,

bước đầu tiên là

nhúng văn bản.

Lời nhắc được chèn hoặc

câu hỏi được chuyển thành

một vector chiều cao

sử dụng bộ mã hóa câu hỏi.

Các tài liệu dựa trên tri thức được

chuyển đổi riêng thành

vectơ chiều cao và

được nhúng bằng cách sử dụng một

bộ mã hóa bối cảnh.

Bước tiếp theo là thu hồi,

nơi hệ thống phù hợp

các vectơ tương tự trong

lời nhắc được chèn

hoặc hài lòng với

các vectơ trong

cơ sở tri thức

để lấy thông tin.

Tuy nhiên, trong phần tăng cường

tạo truy vấn,

hệ thống tạo ra

truy vấn tăng cường

bằng cách kết hợp văn bản

liên kết với

truy xuất vectơ

và bản gốc

lời nhắc hoặc nội dung.

Cuối cùng, trong mô hình

bước thế hệ,

mô hình ngôn ngữ sử dụng

đã tạo truy vấn tăng cường để

tạo phản hồi bằng cách sử dụng

nội dung từ

nền tảng kiến thức.

Bộ mã hóa chuyển đổi

lời nhắc và

cơ sở kiến thức vào phần nhúng

đại diện cho thông tin.

Sau đó bối cảnh và

nhúng câu hỏi

có thể được tạo ra từ

cùng một bộ mã hóa.

Cách tiếp cận này dễ dàng

hiểu như

nó liên quan đến việc chuyển đổi

văn bản để nhúng,

mặc dù nó có thể không

làm việc hiệu quả như thế nào.

Bây giờ hãy hiểu

mã hóa nhanh chóng.

Lời nhắc được chèn

sử dụng nhúng mã thông báo và

vectơ trung bình đến

mã hóa lời nhắc

và chuyển đổi chúng thành một

biểu diễn vector.

Trong việc nhúng mã thông báo,

mỗi mã thông báo, chẳng hạn như một từ

hoặc chèn từ phụ

trong lời nhắc sử dụng một dữ liệu được đào tạo trước

mô hình nhúng mã thông báo như vậy

như hai chiều

Biểu diễn bộ mã hóa

từ Máy biến áp hoặc BERT và

một sáng tạo được đào tạo trước

Máy biến áp hoặc

GPT chuyển đổi thành

vectơ chiều cao.

Một khi tất cả các token

được nhúng,

hệ thống lấy giá trị trung bình của

tất cả các vectơ mã thông báo để tạo

một biểu diễn vector đơn

cho lời nhắc.

Điều này có nghĩa là trung bình

biểu diễn vector

nắm bắt được ý nghĩa

của phần được chèn

nhắc một cách ngắn gọn.

Tiếp theo, hãy hiểu

làm thế nào để chuyển đổi

dữ liệu theo ngữ cảnh từ

cơ sở tri thức thành vectơ.

Hãy xem xét điện thoại di động của công ty

chính sách hiển thị trên màn hình.

Bạn có thể thấy rằng công ty

chính sách di động lớn,

và chèn nó vào

chatbot có thể là một thách thức.

Vì vậy, bản gốc

văn bản chính sách

nên bị phá vỡ

xuống thành nhỏ hơn,

các đoạn văn bản có thể quản lý được

đạt được mục tiêu và

truy xuất hiệu quả.

Tiếp theo, nhúng từng đoạn văn bản

thành các vectơ và lập chỉ mục cho chúng

thành một cơ sở tri thức.

Bây giờ, hãy mã hóa các đoạn văn bản cho

biểu diễn vector

bằng cách biến đổi

chúng lên mức cao

vectơ chiều

sử dụng một chương trình đã được đào tạo trước

mô hình nhúng mã thông báo.

Một khi tất cả các token

được nhúng,

hệ thống tính trung bình mỗi

vector mã thông báo để tạo

một biểu diễn vector đơn

cho toàn bộ đoạn văn bản.

Kết hợp các đoạn văn bản và

vectơ nhúng đại diện

nền tảng kiến thức,

nắm bắt được

thông tin cho từng đoạn.

Chèn các phần nhúng này

vào cơ sở dữ liệu vector để

đại diện cho

cơ sở tri thức với

ID chunk đó

đóng vai trò là chìa khóa.

Các hoạt động khoảng cách

trên các phần nhúng này

sử dụng chunk ID để tìm

thông tin liên quan.

Bước tiếp theo trong RAG

quá trình là tìm kiếm

bối cảnh liên quan cho

lời nhắc được chèn từ

nền tảng kiến thức.

Để làm được điều đó, hệ thống

so sánh vector nhắc

với các vectơ biểu thị

các đoạn văn bản trong

nền tảng kiến thức.

Hãy đặt một câu hỏi về

chính sách di động của công ty.

Cơ sở kiến thức và câu hỏi

được chuyển đổi thành

biểu diễn vector.

Hơn nữa, hệ thống

tính toán khoảng cách

giữa vectơ nhắc

và mỗi vectơ bối cảnh

sử dụng khoảng cách

thước đo để xác định

sự tương đồng giữa

vectơ nhắc và

vectơ bối cảnh.

Tiếp theo nó chọn 3

- 5 vectơ bối cảnh

gần với vectơ nhắc để

trình bày phù hợp hơn

thông tin để

tăng cường đầu vào được chèn

sử dụng các thước đo khoảng cách.

Hãy nhúng truy vấn

q và các phần nhúng từ

cơ sở tri thức c1 và c2.

Chỉ số khoảng cách đã chọn

ảnh hưởng đến kết quả truy xuất.

Nếu bạn lấy tích số chấm,

xét vectơ

chỉ đường và

độ lớn bằng cách ưu tiên

sự liên kết tổng thể,

bạn sẽ tìm thấy kiến thức

nhúng dựa trên

c2 gần hơn một chút

vectơ bối cảnh.

Bây giờ, hãy xem xét

hướng cosin,

trong đó tập trung vào hướng

để đo lường

sự khác biệt góc cạnh.

Vì vậy, dựa trên kiến thức

nhúng c2 là một lựa chọn tốt.

Nó có nghĩa là đối với

độ lớn vectơ,

tích số chấm là thích hợp hơn,

và đối với vectơ chỉ phương,

khoảng cách cosin

là tốt hơn.

Để chọn nhiều nhất

bối cảnh K hàng đầu có liên quan,

trong đó K là siêu tham số,

chọn ID đoạn 6, 2,

và 0 sử dụng của công ty

chính sách di động với 7 khối.

Bộ dữ liệu thực sự sử dụng

thư viện các khối để

tăng tốc quá trình.

Điều này có nghĩa là bạn nên chọn

ID đoạn văn bản tương tự như

truy vấn và liên quan đến

điện thoại di động của công ty hoặc

chính sách chung của công ty.

Cuối cùng, văn bản được chọn

từ cơ sở tri thức và

truy vấn được chèn vào

chatbot để tạo ra

một phản ứng thích hợp.

Điều này có nghĩa là với

sự giúp đỡ của RAG,

chatbot có thể cung cấp

một phản ứng hiệu quả.

Trong video này, bạn

đã học cách tận dụng RAG

để tạo ra phản hồi khi

mô hình không được đào tạo trước.

Chatbot tạo ra phản hồi

dựa trên các câu hỏi.

Tuy nhiên, đó là thách thức

để tạo ra phản hồi cho

các miền cụ thể như

chính sách di động của công ty.

Để tạo ra phản hồi cho

chính sách di động của công ty,

các lời nhắc được chèn được mã hóa

sử dụng nhúng mã thông báo

và trung bình vector,

lời nhắc ở đâu

chia nhỏ thành

nhỏ hơn và có thể

các đoạn văn bản.

Các khối này được nhúng

và chuyển đổi thành

chiều cao

vectơ cần tìm

bối cảnh liên quan

sử dụng các thước đo khoảng cách.

Vector gần nhất với

đoạn văn bản được chọn

từ kiến thức

cơ sở để tạo ra

một phản ứng thích hợp.