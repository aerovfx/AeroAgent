# 09 an ninh

---

Hãy nói về việc bảo mật ứng dụng RAG của bạn.

An ninh mạng là một lĩnh vực sâu rộng và không ngừng phát triển,

vì vậy không thể giải quyết mọi rủi ro bảo mật có thể xảy ra.

Thay vào đó, chúng ta hãy xem xét một số

những thách thức và cơ hội về an ninh

dành riêng cho hệ thống RAG.

Trọng tâm chính ở đây sẽ là

bảo mật thông tin trong cơ sở tri thức của bạn.

Lý do phổ biến khiến bạn chọn xây dựng hệ thống RAG ở

vị trí đầu tiên là bởi vì bạn có

thông tin riêng tư hoặc độc quyền.

Thông tin đó đã được cố tình giữ kín

trang web mở nơi LLM

có nhiều khả năng đã được đào tạo về nó.

Ngay cả sau khi bạn đã xây dựng hệ thống RAG,

bạn có thể vẫn muốn giữ dữ liệu đó ở chế độ riêng tư.

Có một số cách để thông tin

trong cơ sở kiến thức của bạn có thể bị rò rỉ.

Một là người dùng có thể chỉ

yêu cầu nó trực tiếp từ lời nhắc họ gửi.

Một lời nhắc khéo léo có thể thuyết phục

một LLM để báo giá trực tiếp

thông tin trong các khối được truy xuất từ cơ sở tri thức của bạn.

Ngay cả khi có các biện pháp bảo vệ tại chỗ,

đó là một giả định hợp lý rằng người dùng

ứng dụng của bạn ít nhất có thể

truy cập gián tiếp vào nội dung cơ sở tri thức của bạn.

Có một số giải pháp đơn giản ở đây.

Một là xác thực người dùng trong

một cách thích hợp để

thông tin họ được phép truy cập.

Ví dụ: nếu cơ sở tri thức của bạn chứa dữ liệu của công ty tư nhân,

đảm bảo chỉ nhân viên đăng nhập

có thể nhắc hệ thống RAG của bạn là một khởi đầu tốt.

Cách tiếp cận quan trọng thứ hai là đảm bảo rằng dữ liệu được phân chia

trên nhiều đối tượng thuê dựa trên

quyền truy cập dựa trên vai trò hoặc đặc quyền RBAC.

Nói cách khác, nếu người dùng nhắc

dẫn đến việc truy xuất từ cơ sở dữ liệu vector,

về mặt lý thuyết người dùng chỉ có quyền truy cập vào

tài liệu dựa trên vai trò và mức độ truy cập của họ.

Về lý thuyết, bạn có thể giữ tất cả tài liệu trong

một đối tượng thuê duy nhất và sử dụng các bộ lọc siêu dữ liệu để

xác định những tài liệu nào người dùng sẽ có quyền truy cập vào,

trong thực tế, kỹ thuật này rất dễ bị thất bại.

Lọc siêu dữ liệu được sử dụng tốt nhất cho việc cá nhân hóa,

nhưng không có bảo mật.

Để bảo mật, có nhiều riêng biệt

người thuê được lưu trữ là một cách tiếp cận đáng tin cậy hơn nhiều.

Một cách khác mà dữ liệu cơ sở tri thức có thể bị rò rỉ về mặt lý thuyết là nếu

lời nhắc đang được gửi tới

một nhà cung cấp LLM để tạo ra sự hoàn thành.

Lời nhắc tăng cường mà bạn đang gửi sẽ chứa

tài liệu hoặc đoạn văn bản được truy xuất từ cơ sở kiến thức của bạn,

và tại thời điểm đó, bạn mất quyền kiểm soát an ninh.

Tùy thuộc vào mức độ bảo mật của

thông tin trong cơ sở kiến thức của bạn,

đây có thể không phải là một rủi ro có thể chấp nhận được.

May mắn thay, trong những trường hợp này,

bạn có thể chọn chạy hệ thống RAG hoàn toàn cục bộ tại chỗ.

Điều này có nghĩa là lưu trữ LLM và

cơ sở dữ liệu vector trên phần cứng của riêng bạn.

Mặc dù điều này có thể gây thêm sự phức tạp

và chi phí chung cho dự án của bạn,

bây giờ bạn cũng có quyền kiểm soát nội dung của

nền tảng kiến thức của bạn trên toàn bộ quy trình RAG.

Nếu cả hai bạn đều muốn triển khai hệ thống RAG và cần

đảm bảo mức độ bảo mật cao cho cơ sở tri thức của bạn,

bước di chuyển toàn bộ hệ thống tại chỗ này có thể đáng giá.

Tuy nhiên, một cách khác mà nền tảng kiến thức của bạn có thể bị xâm phạm là nó

chỉ cần bị hack trực tiếp càng tốt với bất kỳ cơ sở dữ liệu truyền thống nào.

Một cách bảo vệ cơ sở dữ liệu truyền thống

chống lại sự truy cập trái phép bằng cách mã hóa nội dung của chúng.

Điều này có nghĩa là ngay cả khi hacker có quyền truy cập vào cơ sở dữ liệu,

họ không thể dễ dàng truy cập thông tin được mã hóa.

Cơ sở dữ liệu vectơ đưa ra một số thách thức đặc biệt đối với vectơ tấn công này.

Để thuật toán ANN hoạt động,

ít nhất là các biểu diễn vectơ dày đặc của

tài liệu của bạn cần được lưu trữ trong bộ nhớ theo cách được giải mã.

Bản thân văn bản của các đoạn có thể là

được lưu trữ và truy xuất theo cách được mã hóa,

và sau đó được giải mã để xây dựng lời nhắc tăng cường.

Một số nhà cung cấp cơ sở dữ liệu vector hiện cung cấp dịch vụ này,

hoặc bạn có thể chọn tự mình mã hóa và giải mã các đoạn.

Điều này làm tăng thêm độ phức tạp và có thể gây ra một số độ trễ cho hệ thống của bạn,

nhưng cung cấp một mức độ bảo mật bổ sung.

Những vectơ dày đặc cần không được mã hóa

tiếc là vẫn có thể gây ra một số rủi ro bảo mật.

Nghiên cứu gần đây cho thấy khả năng tái tạo

văn bản gốc từ các biểu diễn vector dày đặc của nó.

Nói cách khác, nếu bạn mã hóa các khối của mình,

có khả năng hacker vẫn có thể tái tạo lại

chúng khỏi các vectơ dày đặc không được mã hóa.

Một số kỹ thuật hiện đang được khám phá để giải quyết mối lo ngại về bảo mật,

như thêm nhiễu vào các vectơ dày đặc,

áp dụng các phép biến đổi cho chúng,

hoặc giảm kích thước theo cách

duy trì khoảng cách trong khi che khuất ý nghĩa ngữ nghĩa.

Mỗi kỹ thuật này đều tăng thêm độ phức tạp cho chó tha mồi của bạn,

tuy nhiên, và có xu hướng làm giảm hiệu suất hệ thống.

Lỗ hổng bảo mật tiềm ẩn có phần độc đáo của

cơ sở dữ liệu vector là một chủ đề nghiên cứu đang diễn ra,

nhưng đáng được lưu ý.

Cuộc tấn công này yêu cầu tin tặc có quyền truy cập trực tiếp vào cơ sở dữ liệu của bạn

và sử dụng các kỹ thuật thử nghiệm để tái tạo lại văn bản từ các vectơ dày đặc,

nhưng có thể có mối lo ngại về bảo mật.

Đây chỉ là cái nhìn nhanh về bảo mật cho hệ thống RAG của bạn,

nhưng hy vọng sẽ giúp làm nổi bật những mối quan tâm riêng của RAG.

Bài học chính ở đây là hãy nhớ rằng nền tảng kiến thức của bạn

có thể chứa một số thông tin cá nhân,

và bạn nên hiểu và kiểm soát cách truy cập thông tin đó.

Kết hợp các kỹ thuật trong video này với một loạt biện pháp phòng ngừa an ninh mạng rộng hơn

sẽ giúp cải thiện tính bảo mật của hệ thống RAG sản xuất của bạn.