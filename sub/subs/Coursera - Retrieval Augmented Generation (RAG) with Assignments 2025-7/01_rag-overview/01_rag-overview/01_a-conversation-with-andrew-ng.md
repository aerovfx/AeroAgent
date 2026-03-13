# 01 a-conversation-with-andrew-ng

---

Chào mừng bạn đến với Thế hệ tăng cường truy xuất từ ​​DeepLearner.ai.

Truy xuất thế hệ tăng cường, hoặc RAG,

là kỹ thuật được sử dụng rộng rãi nhất để cải thiện chất lượng và độ chính xác

phản hồi của mô hình ngôn ngữ lớn.

NLM bắt đầu chỉ biết thông tin từ

có thể là dữ liệu internet công cộng mà nó đã được đào tạo.

Vì vậy, nếu bạn cần trả lời các câu hỏi

sử dụng các dữ kiện được rút ra từ dữ liệu phù hợp,

nói, tài liệu của riêng bạn,

RAG cho phép người mẫu làm điều này

bằng cách cung cấp cho mô hình quyền truy cập vào dữ liệu bổ sung đó.

Điều này cho phép LLM trả lời các câu hỏi bằng sự thật

mà nó chưa được đào tạo.

Ví dụ: bạn cũng có thể đã thấy một chatbot

như ChatGP hoặc Cloud hoặc Gemini

cho bạn biết nó đang tìm kiếm trên web để giúp trả lời câu hỏi của bạn.

LLM này đang truy cập thông tin bổ sung

để cố gắng đảm bảo phản hồi được cập nhật và chính xác.

Tôi rất vui được giới thiệu người hướng dẫn của bạn cho khóa học này,

Zain Hassan.

Zain là một kỹ sư máy học và AI giàu kinh nghiệm

và nhà nghiên cứu, nhà giáo dục.

Ông đã dành phần lớn thập kỷ qua

làm việc tại một số công ty AI thú vị

như Weavier, công ty cơ sở dữ liệu vector hàng đầu

cung cấp một trong những thành phần chính của RAG,

cũng như ZigenAI, nhà cung cấp dịch vụ LLM.

Cảm ơn, Andrew.

Tôi rất vui mừng được ở đây.

Điều tôi yêu thích ở RAG

thực tế là nó cung cấp một cách đơn giản và thiết thực

để tập trung sức mạnh của các mô hình ngôn ngữ lớn.

Ý tưởng cốt lõi của RAG là ghép nối các hệ thống tìm kiếm cổ điển

với khả năng suy luận của các mô hình ngôn ngữ lớn.

Với khóa học này, chúng tôi đã cố gắng cân bằng

bao gồm các khái niệm cơ bản

làm cơ sở cho cả tìm kiếm và LLM

và những lời khuyên thiết thực để áp dụng những khái niệm này

để kiến trúc một hệ thống RAG hiệu suất cao.

Mặc dù khái niệm RAG không phức tạp,

có hàng triệu cách để thực hiện nó,

và những lựa chọn thiết kế tạo nên sự khác biệt lớn

về độ chính xác và tốc độ của hệ thống của bạn.

Bạn sẽ học cách chuẩn bị dữ liệu của mình

được sử dụng trong hệ thống này,

nhắc mô hình ngôn ngữ của bạn tận dụng tối đa dữ liệu đó,

và đánh giá lưu lượng người dùng thực tế

để đảm bảo bạn đang cung cấp phản hồi chất lượng cao.

Vì vậy bạn sẽ rời khỏi khóa học này

với nhiều kỹ năng thực tế

để xây dựng và điều chỉnh hệ thống RAG của bạn

và có hiểu biết nền tảng

về lý do tại sao những kỹ thuật này hoạt động.

Đó là một bộ kỹ năng cực kỳ hữu ích

và có ứng dụng cho rất nhiều ngành công nghiệp.

Tôi nghĩ RAG có thể là loại được xây dựng phổ biến nhất

ứng dụng dựa trên LLM trên thế giới hiện nay.

Các công ty lớn đang sử dụng nó để giúp đỡ khách hàng của họ

nhận được câu trả lời cho các câu hỏi về sản phẩm của họ

hoặc giúp nhân viên của họ có được câu trả lời

đến các chính sách nội bộ của công ty hoặc các vấn đề khác.

Các công ty khởi nghiệp cũng đang xây dựng ứng dụng RAG

trong nhiều ngành dọc, như chăm sóc sức khỏe,

chẳng hạn như trả lời các câu hỏi y tế,

hoặc trong giáo dục để giúp đỡ học sinh

về một loạt các chủ đề, v.v.

Một điều thú vị về RAG

đó là khi công nghệ LLM được cải thiện,

Các hệ thống RAG cũng đang nhanh chóng kết hợp các công nghệ này.

Vì vậy, ví dụ, thế hệ mô hình gần đây

đã tốt hơn nhiều so với một hoặc hai năm trước

để làm cho hệ thống RAG trở nên vững chắc hơn

trong các tài liệu hoặc bối cảnh được đưa ra,

nên trong khoảng một năm qua,

cảm giác như tỷ lệ ảo giác của hệ thống RAG

đang có xu hướng giảm dần.

Và các mô hình lý luận cũng cho phép họ giải quyết

những câu hỏi phức tạp hơn nhiều

và có thể suy luận dựa trên bối cảnh được cung cấp.

Và một thay đổi thú vị trong vài năm qua

giống như cửa sổ ngữ cảnh đầu vào của LLM đã mở ra,

điều chỉnh siêu tham số,

bạn biết đấy, chính xác thì bạn chèn cái gì vào RAG,

làm cách nào để cắt tài liệu thành từng phần để báo hiệu ngữ cảnh đầu vào,

những phương pháp hay nhất mà XAN thực sự là chuyên gia,

cũng đã phát triển,

bởi vì bây giờ bạn không cần phải thu thập quá nhiều thông tin

vào một cửa sổ ngữ cảnh nhỏ xíu.

Và như trích xuất tài liệu đại lý

và các công nghệ liên quan được cải thiện,

giờ đây bạn cũng có thể dễ dàng xây dựng hệ thống RAG hơn

ở đầu các tệp PDF hoặc trang trình bày hoặc các loại tài liệu khác,

để bạn có thể xây dựng hệ thống RAG để sử dụng dễ dàng hơn

và suy luận và trả lời các câu hỏi

liên quan đến tập hợp tài liệu rộng hơn mà bạn có thể có.

Và rộng hơn, khi các nhóm đang xây dựng

quy trình làm việc tác nhân nhiều bước phức tạp hơn,

RAG thường là một thành phần trong quy trình làm việc tác nhân phức tạp

có thể ở đâu, bạn biết đấy, bước năm hoặc bước bảy

của một số khối lượng công việc nội bộ doanh nghiệp,

RAG cung cấp cho đại lý thông tin cần thiết

để xử lý một tài liệu

hoặc lý do về yêu cầu của khách hàng.

Ồ, tôi hoàn toàn đồng ý.

Ngay cả khi lĩnh vực AI tiếp tục phát triển nhanh chóng,

Tôi không nghĩ RAG sẽ đi đâu cả.

LLM sẽ tiếp tục được hưởng lợi

từ việc truy cập vào dữ liệu có liên quan chất lượng cao.

Tôi cũng nghĩ rằng khóa học này mang lại một nền tảng thực sự vững chắc

để làm việc với tất cả những tiến bộ tiên tiến này.

Chúng tôi đã bao gồm rất nhiều kỹ thuật tiên tiến

trong khóa học này,

từ các mô hình đa phương thức hoặc lý luận, như bạn đã đề cập,

đến các phương pháp cân bằng như RAG, tinh chỉnh,

và các mô hình bối cảnh dài mới hơn.

Một kỹ thuật mà cá nhân tôi khá hào hứng

là tác nhân RAG,

hoặc xây dựng hệ thống sử dụng nhiều mô hình ngôn ngữ lớn

trong đó mỗi người xử lý một phần của quy trình làm việc lớn

và có cơ quan quyết định dữ liệu nào cần lấy.

Đây là ngay biên giới

về nơi các công ty đang thúc đẩy hiệu suất

của các ứng dụng dựa trên LLM.

Tôi nghĩ thế hệ hệ thống RAG trước đó

là một kỹ sư con người sẽ viết một loạt mã

hoặc viết một loạt các quy tắc

để quyết định, đưa ra truy vấn,

đây là cách chúng tôi lấy một tài liệu dài,

cách chúng tôi cắt nó thành từng mảnh,

cách chúng tôi lấy lại nó,

và chúng tôi sẽ thực hiện, bạn biết đấy,

bảy phần hoặc thứ gì đó để đưa vào bối cảnh LLM.

Vậy đó thực sự là một kỹ sư con người

quyết định nên đưa ra cái gì làm bối cảnh

để LLM trả lời một câu hỏi.

Và điều thực sự thú vị

về tác nhân RAG là

bạn có thể cung cấp cho một đại lý AI các công cụ

để lấy thông tin và để nó quyết định,

nó có muốn thực hiện tìm kiếm trên web tiếp theo không?

Và nếu vậy thì nó muốn sử dụng từ khóa gì

cho việc tìm kiếm trên web?

Hoặc có thể truy vấn một cơ sở dữ liệu chuyên biệt cụ thể.

Và sau khi lấy được thông tin đầu tiên,

nó có đủ tốt không?

Hay bạn muốn thực hiện đợt truy xuất thứ hai?

Vậy nên những hệ thống có tính tác nhân cao này

sau đó có thể tự quyết định

cần lấy thông tin gì

nhằm phục vụ một nhu cầu thông tin cụ thể.

Và tôi thấy đó là một cách quan trọng

để làm cho hệ thống linh hoạt và mạnh mẽ hơn nhiều.

Nó mang lại cho họ một cách để giải quyết

sự hỗn loạn của thế giới thực.

Nếu họ gặp rắc rối, họ có thể định tuyến trở lại

và sửa chữa cách tiếp cận mà họ đang thực hiện.

Vì vậy, hãy bắt đầu từ RAG cơ bản

đến tác nhân RAG tiên tiến,

trong khóa học này, bạn tìm hiểu về

phạm vi kỹ thuật này,

cả từ những nguyên tắc cốt lõi

và khuôn khổ tinh thần

về cách xây dựng những hệ thống này

đến tính thực tiễn của

làm thế nào để bạn thực sự điều chỉnh một siêu tham số

kích thước khối thích hợp là bao nhiêu

để cắt một tài liệu rất dài thành

và cách quản lý bối cảnh.

Và nếu bạn chỉ mới bắt đầu

ở các giai đoạn trước

xây dựng các ứng dụng Gen AI,

Tôi nghĩ rằng khóa học này

sẽ cung cấp cho bạn một cái nhìn tổng quan tốt

không chỉ của RAG,

nhưng nhiều thành phần

đi vào RAG

điều đó có thể hữu ích

cho những thứ khác bạn có thể xây dựng

trong tương lai cũng vậy.

Vì vậy tôi nghĩ rằng khóa học này

sẽ thiết lập cho bạn

nhất định phải làm RAG,

nhưng rộng hơn,

để có một nền tảng tốt

suy nghĩ về cách lắp ráp

nhiều công cụ

mà chúng ta hiện có trong Gen AI

để xây dựng một ứng dụng

và để đánh giá nó

và thúc đẩy những cải tiến liên tục.

Cho đến nay, Zan và tôi

đã trò chuyện về RAG

và tại sao chúng tôi nghĩ nó quan trọng

và tại sao chúng tôi nghĩ bạn được hưởng lợi

từ việc tìm hiểu về nó.

Và trong video tiếp theo,

Zan sẽ trình bày tổng quan cấp cao

điều gì là quan trọng nhất

các thành phần của RAG

để cho dù bạn đang xây dựng

một hệ thống RAG độc lập

hoặc xây dựng nó như một thành phần

của một tác nhân phức tạp hơn

hoặc loại hệ thống khác,

bạn có bản đồ tinh thần đó

để làm những việc gì

bạn cần phải làm

để hệ thống RAG hoạt động hiệu quả.

Vì vậy chúng ta hãy xem xét

ở video tiếp theo

để đi sâu vào chi tiết của RAG.