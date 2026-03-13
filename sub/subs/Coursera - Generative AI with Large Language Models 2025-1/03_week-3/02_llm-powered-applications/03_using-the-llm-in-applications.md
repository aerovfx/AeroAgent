# 03 ứng dụng sử dụng llm trong ứng dụng

---

Mặc dù tất cả việc đào tạo, điều chỉnh và

các kỹ thuật sắp xếp bạn đã khám phá có thể

giúp bạn xây dựng một mô hình tuyệt vời cho

ứng dụng của bạn.

Có một số thách thức lớn hơn với

mô hình ngôn ngữ lớn không thể giải được

bằng cách đào tạo một mình.

Chúng ta hãy xem xét một vài ví dụ.

Một vấn đề là nội bộ

kiến thức được nắm giữ bởi một mô hình bị cắt đứt ở

thời điểm luyện tập trước.

Ví dụ, nếu bạn hỏi một người mẫu

đã được đào tạo vào đầu năm 2022

Thủ tướng Anh là,

nó có thể sẽ cho bạn biết Boris Johnson.

Kiến thức này đã lỗi thời.

Người mẫu không biết rằng Johnson

rời văn phòng vào cuối năm 2022 vì điều đó

sự kiện đã xảy ra sau khi đào tạo của nó.

Người mẫu cũng có thể gặp khó khăn

với phép toán phức tạp.

Nếu bạn nhắc một mô hình hành xử như

một chiếc máy tính, nó có thể trả lời sai,

tùy theo độ khó

của vấn đề.

Ở đây, bạn yêu cầu người mẫu

thực hiện phép chia.

Mô hình trả về một số gần với

câu trả lời đúng nhưng sai.

Lưu ý LLM không mang theo

ra các phép toán.

Họ vẫn đang cố gắng dự đoán

mã thông báo tốt nhất tiếp theo dựa trên quá trình đào tạo của họ,

và kết quả là,

có thể dễ dàng nhận được câu trả lời sai.

Cuối cùng, một trong những điều được biết đến nhiều nhất

vấn đề của LLM là xu hướng của họ

để tạo ra văn bản ngay cả khi họ

không biết câu trả lời cho một vấn đề.

Điều này thường được gọi là ảo giác,

và ở đây bạn có thể thấy rõ mô hình

tạo nên một mô tả về một cái gì đó không tồn tại

thực vật, Martian Dunetree.

Mặc dù vẫn chưa có

bằng chứng rõ ràng về sự sống trên sao Hỏa,

người mẫu sẽ vui vẻ nói với bạn điều ngược lại.

Trong phần này, bạn sẽ tìm hiểu về một số

kỹ thuật mà bạn có thể sử dụng để giúp bạn

LLM khắc phục những vấn đề này bằng cách kết nối với

nguồn dữ liệu bên ngoài và các ứng dụng.

Bạn sẽ có thêm một chút việc phải làm

có thể kết nối LLM của bạn với các bên ngoài này

các thành phần và tích hợp đầy đủ mọi thứ

để triển khai trong ứng dụng của bạn.

Ứng dụng của bạn phải quản lý

việc chuyển đầu vào của người dùng tới

mô hình ngôn ngữ lớn và

sự trở lại của sự hoàn thành.

Điều này thường được thực hiện thông qua một số

loại thư viện phối hợp.

Lớp này có thể kích hoạt một số chức năng mạnh mẽ

những công nghệ tăng cường và

nâng cao hiệu suất

của LLM trong thời gian chạy.

Bằng cách cung cấp quyền truy cập vào

nguồn dữ liệu bên ngoài hoặc

kết nối với các API hiện có

của các ứng dụng khác.

Một ví dụ triển khai là Langchain,

mà bạn sẽ tìm hiểu thêm

về phần sau của bài học này.

Hãy bắt đầu bằng cách xem xét làm thế nào để

kết nối LLM với các nguồn dữ liệu bên ngoài.

Truy xuất thế hệ tăng cường, hoặc

RAG viết tắt là một khuôn khổ cho

xây dựng các hệ thống hỗ trợ LLM

tận dụng các nguồn dữ liệu bên ngoài.

Và ứng dụng để khắc phục một số

hạn chế của các mô hình này.

RAG là một cách tuyệt vời để vượt qua

vấn đề hạn chế kiến thức và

giúp mô hình cập nhật

sự hiểu biết về thế giới.

Trong khi bạn có thể đào tạo lại

the model on new data,

điều này sẽ nhanh chóng trở nên rất tốn kém.

Và yêu cầu đào tạo lại nhiều lần để

thường xuyên cập nhật mẫu mới

kiến thức.

Một cách linh hoạt hơn và ít tốn kém hơn

để vượt qua những hạn chế về kiến thức là

cung cấp cho mô hình của bạn quyền truy cập vào bổ sung

dữ liệu bên ngoài tại thời điểm suy luận.

RAG rất hữu ích trong mọi trường hợp bạn muốn

mô hình ngôn ngữ để có quyền truy cập vào

dữ liệu mà nó có thể chưa nhìn thấy.

Đây có thể là tài liệu thông tin mới

không có trong chương trình đào tạo ban đầu

dữ liệu hoặc kiến thức độc quyền được lưu trữ trong

cơ sở dữ liệu riêng tư của tổ chức bạn.

Cung cấp cho mô hình của bạn

thông tin bên ngoài,

có thể cải thiện cả mức độ liên quan và

độ chính xác của việc hoàn thành nó.

Chúng ta hãy đến gần hơn

hãy xem cách nó hoạt động.

Thế hệ tăng cường truy xuất không

một tập hợp công nghệ cụ thể, nhưng đúng hơn là

một khuôn khổ để cung cấp quyền truy cập LLM vào

dữ liệu họ không nhìn thấy trong quá trình đào tạo.

Một số cách triển khai khác nhau

tồn tại và cái bạn chọn sẽ phụ thuộc

về chi tiết nhiệm vụ của bạn và định dạng

của dữ liệu bạn phải làm việc.

Ở đây bạn sẽ đi qua

việc thực hiện được thảo luận ở một trong

các bài báo sớm nhất về RAG của các nhà nghiên cứu

tại Facebook, được xuất bản lần đầu vào năm 2020.

Trọng tâm của việc thực hiện này là

một thành phần mô hình có tên là Retriever,

bao gồm một bộ mã hóa truy vấn và

một nguồn dữ liệu bên ngoài.

Bộ mã hóa lấy

lời nhắc đầu vào của người dùng và

mã hóa nó thành một dạng có thể

được sử dụng để truy vấn nguồn dữ liệu.

Trong bài báo trên Facebook,

dữ liệu bên ngoài là một kho lưu trữ vector,

mà chúng ta sẽ thảo luận trong

chi tiết hơn trong thời gian ngắn.

Nhưng thay vào đó nó có thể là cơ sở dữ liệu SQL,

Tệp CSV hoặc định dạng lưu trữ dữ liệu khác.

Hai thành phần này được đào tạo

cùng nhau tìm tài liệu trong

dữ liệu bên ngoài nhiều nhất

liên quan đến truy vấn đầu vào.

Retriever trả lại đĩa đơn hay nhất

nhóm tài liệu từ dữ liệu

nguồn và kết hợp thông tin mới

với truy vấn ban đầu của người dùng.

Lời nhắc mở rộng mới là sau đó

được chuyển sang mô hình ngôn ngữ,

tạo ra sự hoàn thành

đó sử dụng dữ liệu.

Chúng ta hãy nhìn vào

một ví dụ cụ thể hơn.

Hãy tưởng tượng bạn là một luật sư đang sử dụng

một mô hình ngôn ngữ lớn để giúp bạn trong

giai đoạn phát hiện vụ án.

Kiến trúc Rag có thể giúp bạn hỏi

câu hỏi của một tập tài liệu, dành cho

ví dụ, hồ sơ tòa án trước đó.

Ở đây bạn hỏi người mẫu về nguyên đơn

được đặt tên theo số vụ việc cụ thể.

Lời nhắc được chuyển đến bộ mã hóa truy vấn,

mã hóa dữ liệu trong cùng một

định dạng như các tài liệu bên ngoài.

Và sau đó tìm kiếm một liên quan

mục nhập trong kho tài liệu.

Sau khi tìm thấy một đoạn văn bản

chứa thông tin được yêu cầu,

Retriever sau đó kết hợp cái mới

văn bản với lời nhắc ban đầu.

Lời nhắc mở rộng hiện chứa

thông tin về cụ thể

trường hợp quan tâm là

sau đó được chuyển đến LLM.

Mô hình sử dụng thông tin trong

bối cảnh của lời nhắc để tạo

sự hoàn thành có chứa

câu trả lời đúng.

Trường hợp sử dụng bạn đã thấy

ở đây khá đơn giản và

chỉ trả về một phần thông tin

có thể được tìm thấy bằng các phương tiện khác.

Nhưng hãy tưởng tượng sức mạnh của Rag có thể

để tạo ra các bản tóm tắt hồ sơ hoặc

xác định những người, địa điểm cụ thể và

các tổ chức trong phạm vi đầy đủ

tập hợp các văn bản pháp luật.

Cho phép mô hình truy cập thông tin

chứa trong dữ liệu bên ngoài này

bộ làm tăng đáng kể tiện ích của nó cho

trường hợp sử dụng cụ thể này.

Ngoài việc khắc phục kiến thức

những vết cắt, giẻ rách cũng giúp bạn tránh được

vấn đề ảo giác của mô hình

khi nó không biết câu trả lời.

Kiến trúc RAG có thể được sử dụng để tích hợp

nhiều loại thông tin bên ngoài

nguồn.

Bạn có thể tăng cường các mô hình ngôn ngữ lớn

với quyền truy cập vào các tài liệu địa phương,

bao gồm cả wiki riêng tư và

các hệ thống chuyên gia.

Rag cũng có thể cho phép truy cập Internet

để trích xuất thông tin đăng trên web

các trang, ví dụ như Wikipedia.

Bằng cách mã hóa đầu vào của người dùng

lời nhắc dưới dạng truy vấn SQL,

RAG cũng có thể tương tác với cơ sở dữ liệu.

Một lưu trữ dữ liệu quan trọng khác

chiến lược là Cửa hàng Vector,

chứa vectơ

các biểu diễn của văn bản.

Đây là một định dạng dữ liệu đặc biệt hữu ích

cho các mô hình ngôn ngữ, vì trong nội bộ

họ làm việc với các biểu diễn vector

ngôn ngữ để tạo ra văn bản.

Cửa hàng Vector cho phép truy cập nhanh và

loại hiệu quả có liên quan

tìm kiếm dựa trên sự giống nhau

Lưu ý rằng việc triển khai RAG tốn một chút

phức tạp hơn việc chỉ thêm văn bản

vào mô hình ngôn ngữ lớn.

Có một vài chìa khóa

những cân nhắc cần lưu ý,

bắt đầu với kích thước

của cửa sổ ngữ cảnh.

Hầu hết các nguồn văn bản quá dài để phù hợp với

cửa sổ ngữ cảnh giới hạn của mô hình,

điều đó nhiều nhất vẫn chỉ là

vài nghìn token.

Thay vào đó, các nguồn dữ liệu bên ngoài

bị chặt thành nhiều khúc,

mỗi cái sẽ phù hợp

trong cửa sổ ngữ cảnh.

Các gói như Langchain có thể

xử lý công việc này cho bạn.

Thứ hai, dữ liệu phải có sẵn

ở định dạng cho phép

dễ dàng truy xuất văn bản có liên quan nhất.

Hãy nhớ lại rằng các mô hình ngôn ngữ lớn

không làm việc trực tiếp với văn bản, nhưng

thay vào đó hãy tạo các biểu diễn vector

of each token in an embedding space.

Các vectơ nhúng này cho phép LLM

để xác định các từ liên quan đến ngữ nghĩa

thông qua các biện pháp như

như độ tương đồng cosin,

mà bạn đã học trước đó.

Phương pháp Rag lấy những phần nhỏ của

dữ liệu bên ngoài và xử lý chúng thông qua

mô hình ngôn ngữ lớn,

để tạo các vectơ nhúng cho mỗi vectơ.

Những cách thể hiện mới này của dữ liệu

có thể được lưu trữ trong các cấu trúc gọi là

cửa hàng vector, cho phép

tìm kiếm nhanh các tập dữ liệu và

xác định hiệu quả

văn bản có liên quan về mặt ngữ nghĩa.

Cơ sở dữ liệu vector là một cơ sở dữ liệu cụ thể

triển khai kho vector

mỗi vectơ ở đâu

cũng được xác định bằng một khóa.

Điều này có thể cho phép, ví dụ,

văn bản được tạo bởi RAG tới

cũng bao gồm một trích dẫn cho

tài liệu mà nó được nhận từ đó.

Vậy là bạn đã thấy cách truy cập vào dữ liệu bên ngoài

nguồn có thể giúp một mô hình vượt qua giới hạn

với kiến thức bên trong của nó.

Bằng cách cung cấp thông tin cập nhật có liên quan

thông tin và tránh ảo giác,

bạn có thể cải thiện đáng kể trải nghiệm của

sử dụng ứng dụng của bạn cho người dùng của bạn.

Tiếp theo, chúng ta sẽ khám phá một kỹ thuật có thể

cải thiện khả năng suy luận của người mẫu và

lập kế hoạch các bước quan trọng khi sử dụng

LLM để cấp nguồn cho ứng dụng.

Hãy cùng tôi xem video tiếp theo để tìm hiểu thêm.