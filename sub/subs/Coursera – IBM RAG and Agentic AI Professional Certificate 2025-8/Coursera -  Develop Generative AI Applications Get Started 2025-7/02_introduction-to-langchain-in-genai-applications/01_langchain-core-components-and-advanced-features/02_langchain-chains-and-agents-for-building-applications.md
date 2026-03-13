# 02 chuỗi langchain và đại lý cho ứng dụng xây dựng

---

Chào mừng đến với chuỗi LangChain

và đại lý cho

xây dựng các ứng dụng.

Sau khi xem video này,

bạn sẽ có thể mô tả

chuỗi trong LangChain cho

tạo ra phản hồi và cách

LangChain lưu trữ bộ nhớ.

Bạn cũng sẽ có thể xác định

các tác nhân được sử dụng trong LangChain.

LangChain là một nền tảng được nhúng

với các API để phát triển

ứng dụng,

trao quyền cho họ để truyền tải

xử lý ngôn ngữ

khả năng.

Vì vậy, các nhà phát triển

tìm LangChain

thích hợp cho việc xây dựng

ứng dụng.

LangChain sử dụng một số công cụ nhất định,

bao gồm các tài liệu, dây chuyền,

và đại lý cho

xây dựng các ứng dụng.

Hãy cùng khám phá chuỗi cho

xây dựng các ứng dụng.

Trong LangChain, các chuỗi được

một chuỗi các cuộc gọi.

Một chuỗi tuần tự bao gồm

các bước cơ bản ở đâu

mỗi bước mất

một đầu vào để tạo ra một đầu ra

để tạo ra một liền mạch

luồng thông tin.

Đầu ra từ Bước 1

trở thành đầu vào cho Bước 2.

Chúng ta hãy nhìn vào việc tạo ra

một chuỗi tuần tự

ba chuỗi riêng lẻ.

Mục đích của chuỗi này là

để xác định công thức và

thời gian nấu ước tính cho

món ăn nổi tiếng có sẵn

ở vị trí được chèn.

Người dùng tận dụng

Chuỗi 1 để chọn

khu vực địa lý để có được

món ăn nổi tiếng

ở vị trí đó,

Chuỗi 2 để cung cấp

công thức,

và Chuỗi 3 để ước tính

thời gian nấu ăn.

Chuỗi 1 trong chuỗi sử dụng

lời nhắc của người dùng làm đầu vào cho

một món ăn cụ thể

dựa trên người dùng

địa điểm quy định.

Ví dụ như Trung Quốc.

Do đó, đầu ra

đối với Chuỗi 1 nên

là một món ăn nổi tiếng ở

Trung Quốc, Vịt Bắc Kinh.

Chúng ta hãy xem cách sử dụng

mã để tạo chuỗi này.

Đầu tiên, xác định một mẫu

chuỗi cho lời nhắc.

Yêu cầu một món ăn cụ thể

từ một vị trí được chỉ định.

Tạo một đối tượng mẫu nhắc nhở

sử dụng mẫu đã xác định,

chỉ định đầu vào

biến như vị trí.

Sau đó tạo chuỗi LLM

đối tượng được đặt tên là chuỗi vị trí,

sử dụng mô hình ngôn ngữ dựa trên LLM,

chẳng hạn như Mixtral LLM.

Có nghĩa là trước đó

chạy mã này,

giả sử mô hình trò chuyện đó

đối tượng có sẵn.

Do đó, đầu ra sẽ là

dự trữ theo bữa ăn chính.

Hãy nhìn vào Chuỗi 2.

Trong chuỗi thứ hai của

thiết lập tuần tự của chúng tôi,

sử dụng đầu ra từ

chuỗi đầu tiên,

tức là tên của

món ăn là đầu vào.

Đầu ra từ chuỗi này

sẽ là công thức của chính nó.

Hãy nhìn vào mã.

Đầu tiên, xác định

mẫu trước

yêu cầu một cách đơn giản

công thức cho một bữa ăn nhất định.

Tiếp theo, tạo mẫu lời nhắc

với bữa ăn là biến đầu vào.

Cuối cùng, tạo LLM

chuỗi có tên là món_chuỗi,

sử dụng Mixtral LLM và

mẫu lời nhắc với

công thức khóa đầu ra.

Tiếp theo là Chuỗi 3.

Lấy công thức thu được từ

chuỗi thứ hai làm đầu vào.

Chuỗi này là

được thiết kế để ước tính

thời gian nấu ăn cho

bữa ăn dựa trên công thức.

Giống như Chuỗi 2, xác định mẫu

ước tính việc nấu ăn

thời gian cho một công thức nhất định.

Tiếp theo, tạo mẫu lời nhắc

với công thức là

biến đầu vào.

Cuối cùng, tạo chuỗi LLM

được đặt tên là Recipe_chain bằng cách sử dụng

Mixtral LLM và nhắc nhở

mẫu với

khóa_đầu ra, thời gian.

Bây giờ sử dụng ba chuỗi,

thiết lập tổng thể là

chuỗi tuần tự

điều đó bao bọc tất cả

các chuỗi riêng lẻ với nhau,

tạo thành một quy trình thống nhất.

Bằng cách gọi truy vấn

thông qua chuỗi kết hợp này,

bạn có thể theo dõi dòng chảy của

thông tin từ đầu đến cuối.

Bạn có thể đặt tùy chọn dài dòng

thành true để xem

tổng sản lượng.

Điều này cung cấp một cách rõ ràng

và cái nhìn chi tiết về cách

mỗi đầu vào được chuyển đổi

qua chuỗi vào

đầu ra cuối cùng.

Đây là một ví dụ về đầu ra.

Bạn có biết trí nhớ là thế nào không?

được lưu trữ trong các ứng dụng LLM?

Trong LangChain, bộ nhớ lưu trữ được

quan trọng cho việc đọc và

viết dữ liệu lịch sử.

Mỗi chuỗi dựa vào

trên đầu vào cụ thể,

chẳng hạn như người dùng và bộ nhớ.

Chuỗi đọc từ bộ nhớ đến

nâng cao đầu vào của người dùng

trước khi thực hiện

logic cốt lõi của nó và viết

đầu vào chạy hiện tại và

đầu ra trở lại

bộ nhớ sau khi thực hiện.

Điều này đảm bảo tính liên tục

và bảo tồn bối cảnh

qua các tương tác.

Lịch sử tin nhắn trò chuyện

lớp trong LangChain là

được thiết kế để quản lý và lưu trữ

lịch sử cuộc trò chuyện

một cách hiệu quả,

bao gồm cả thông điệp của con người

và tin nhắn AI.

Điều này cho phép thêm tin nhắn từ

AI và người dùng đối với lịch sử.

Trong ví dụ này, hãy gọi

một lớp ChatMessageHistory và

thêm tin nhắn AI xin chào

vào bộ nhớ.

Bộ nhớ sẽ nối thêm

thông báo AI này làm đầu vào.

Bây giờ, thêm tin nhắn của người dùng,

thủ đô của Pháp là gì,

và bộ nhớ sẽ nối thêm

đây là đầu vào tin nhắn của con người.

Bạn sẽ nhận được phản hồi

dựa trên bộ nhớ được lưu trữ.

Bây giờ hãy hiểu

đại lý tại LangChain.

Đại lý tại LangChain là

hệ thống động lực nơi

một mô hình ngôn ngữ xác định và

trình tự các hành động như vậy

như các chuỗi được xác định trước.

Mô hình tạo văn bản

kết quả đầu ra để hướng dẫn hành động,

nhưng không thực thi

chúng một cách trực tiếp.

Tuy nhiên, các đại lý tích hợp với

các công cụ như công cụ tìm kiếm,

cơ sở dữ liệu và các trang web

để đáp ứng yêu cầu của người dùng.

Ví dụ: nếu người dùng hỏi

đối với người dân Ý,

đại lý sử dụng ngôn ngữ

mô hình để tìm các lựa chọn,

truy vấn cơ sở dữ liệu để biết chi tiết,

và trả về một danh sách giám tuyển.

Điều này cho thấy

khả năng của đại lý

tự động tận dụng LLM

suy luận bằng các công cụ bên ngoài.

Trong ví dụ này, hãy tạo

một khung dữ liệu Pandas

đại lý sử dụng LangChain.

Tác nhân này cho phép người dùng truy vấn

và trực quan hóa dữ liệu

bằng ngôn ngữ tự nhiên.

Để thiết lập nó, hãy khởi tạo

tác nhân create_pandas_dataframe_agent

lớp học.

Trong lớp này, vượt qua LLM

mô hình trò chuyện trong khung dữ liệu.

Tiếp theo, đặt chi tiết thành đúng

để xem LLM nghĩ thế nào.

Cuối cùng, sử dụng lệnh gọi

mã để thực hiện truy vấn,

có bao nhiêu hàng trong khung dữ liệu.

LLM biến đổi

truy vấn vào mã Python,

được thực thi ở chế độ nền,

cho phép trả lời chính xác

số lượng hàng

của khung dữ liệu.

Ví dụ,

phản hồi cho thấy có

139 hàng trong

DataFrame. Hãy tóm tắt lại.

Trong video này, bạn

được biết rằng LangChain là

một nền tảng nhúng API

cho việc phát triển các ứng dụng.

Chuỗi là chuỗi các cuộc gọi.

Trong chuỗi, đầu ra từ

một bước trở thành

đầu vào cho bước tiếp theo.

Trong LangChain, chuỗi là trên hết

xác định mẫu

chuỗi cho lời nhắc,

sau đó tạo một mẫu nhắc nhở

sử dụng mẫu đã xác định,

và tạo LLM

tên đối tượng chuỗi.

Trong LangChain, bộ nhớ lưu trữ được

quan trọng cho việc đọc và

viết dữ liệu lịch sử.

Đại lý tại LangChain là

hệ thống động lực nơi

một mô hình ngôn ngữ xác định và

trình tự các hành động như vậy

như các chuỗi được xác định trước.

Đại lý tích hợp với các công cụ

chẳng hạn như công cụ tìm kiếm,

cơ sở dữ liệu và các trang web

để đáp ứng yêu cầu của người dùng.