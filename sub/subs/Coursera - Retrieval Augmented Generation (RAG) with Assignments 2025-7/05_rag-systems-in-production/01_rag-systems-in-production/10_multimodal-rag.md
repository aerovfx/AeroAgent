# 10 miếng giẻ lau đa phương thức

---

Trong suốt khóa học này, bạn đã thấy các hệ thống RAG được xây dựng dựa trên dữ liệu văn bản, nhưng ngày nay,

thông tin được lưu trữ ở nhiều định dạng khác nhau.

Các bản trình chiếu, tệp PDF hoặc hình ảnh cũng bao gồm thông tin có giá trị mà bạn mong muốn

để đưa vào cơ sở kiến thức của bạn và cung cấp cho LLM của bạn.

Nhờ sự phát triển tiên tiến của các mô hình đa phương thức, ngày càng có khả năng xây dựng

Hệ thống RAG xử lý nhiều loại dữ liệu.

Chúng ta hãy xem cách họ làm việc.

Mô hình đa phương thức là mô hình được thiết kế để xử lý nhiều loại dữ liệu.

Việc ghép nối phổ biến nhất là văn bản và hình ảnh, nhưng cũng có thể ghép nối âm thanh và video.

Một hệ thống RAG đa phương thức điển hình là một hệ thống có thể chấp nhận cả văn bản và hình ảnh dưới dạng lời nhắc,

lưu trữ cả tệp văn bản và hình ảnh trong cơ sở kiến thức và cuối cùng tạo ra phản hồi văn bản.

Để hỗ trợ những khả năng mới này, cả chó săn mồi và LLM đều cần phải được

được cập nhật để có khả năng đa phương thức.

Hãy xem mỗi thành phần cần được thay đổi như thế nào.

Thành phần đầu tiên cần được thực hiện đa phương thức là mô hình nhúng được sử dụng bởi

cơ sở dữ liệu vectơ

Mô hình nhúng đa phương thức là mô hình có thể nhúng nhiều định dạng dữ liệu vào cùng một

không gian vectơ.

Nếu bạn sử dụng loại mô hình này để nhúng cả hai từ dog và dog, bạn sẽ mong đợi

các vectơ của chúng khá gần nhau, như với mô hình nhúng chỉ có văn bản.

Tuy nhiên, nếu bạn đưa cho mô hình này một hình ảnh của một con chó, thì vectơ của hình ảnh đó sẽ

cũng kết thúc ở một phần lân cận của không gian vectơ.

Nếu bạn nhúng hình ảnh một cái cây và cây từ, hai đối tượng đó cũng sẽ

được nhúng gần nhau nhưng ở một phần khác của không gian vectơ.

Nói cách khác, mô hình nhúng đa phương thức hoạt động giống như mô hình nhúng văn bản, đặt

những đồ vật có ý nghĩa tương tự gần nhau hơn.

Tuy nhiên, nhờ thiết kế của chúng, chúng có thể thực hiện chức năng tương tự với nhiều loại

hoặc các phương thức của dữ liệu.

Khi bạn có mô hình nhúng đa phương thức, việc truy xuất dựa trên vectơ sẽ hoạt động theo cách rất quen thuộc.

cách.

Cả hình ảnh và văn bản từ cơ sở tri thức của bạn đều có thể được nhúng vào cùng một không gian vectơ.

Khi nhận được lời nhắc, mô hình đa phương thức đó sẽ được sử dụng để nhúng lời nhắc, cho dù

đó là một hình ảnh hoặc văn bản.

Sau đó việc tìm kiếm vectơ được hoàn thành như bình thường, trả về các hình ảnh hoặc tài liệu có vectơ

gần nhất với vectơ nhắc.

Sau đó, văn bản và hình ảnh được lấy từ cơ sở kiến thức có thể được thêm vào lời nhắc tăng cường

như bình thường và được gửi cùng với mô hình ngôn ngữ.

Để mô hình ngôn ngữ xử lý cả văn bản và hình ảnh, bạn sẽ cần sử dụng một ngôn ngữ

mô hình tầm nhìn.

Loại mô hình này hoạt động rất giống với LLM chỉ có văn bản nhưng có khả năng xử lý

hình ảnh cũng đã được mã hóa.

Để làm được điều đó, hình ảnh phải được mã hóa.

Một quy trình điển hình để mã hóa một hình ảnh là chia hình ảnh thành các phần riêng biệt

mỗi cái được biểu diễn dưới dạng một mã thông báo.

Tùy thuộc vào độ phân giải của chúng, hình ảnh có thể được biểu diễn ở đâu đó theo thứ tự 100

mã thông báo ở cấp thấp hơn để đạt tới 1000 mã thông báo ở cấp cao hơn.

Tuy nhiên, điều quan trọng ở đây không phải là số lượng token được sử dụng mà là thực tế

rằng các mô hình này được thiết kế sao cho cả hình ảnh và văn bản đều có thể được chuyển đổi thành mã thông báo

trình tự giống như với các mô hình chỉ có văn bản.

Các mô hình tầm nhìn ngôn ngữ sau đó hoạt động rất giống với LLM tiêu chuẩn, vượt qua đa phương thức này.

chuỗi mã thông báo thông qua một máy biến áp có thể phát triển sự hiểu biết sâu sắc về cả hai

văn bản và hình ảnh trong lời nhắc và mối quan hệ của chúng.

Sau đó, mô hình thường sẽ tạo ra các mã thông báo văn bản làm đầu ra, đáp ứng yêu cầu ban đầu.

nhắc nhở.

Nếu bạn có mô hình nhúng đa phương thức và mô hình tầm nhìn ngôn ngữ, hãy nâng cấp RAG của bạn

Hệ thống lưu trữ cả hình ảnh và văn bản trong cơ sở kiến thức khá đơn giản.

Kiến trúc cấp cao về cơ bản giống hệt nhau, nhưng giờ đây nó có thể xử lý cả văn bản

và hình ảnh.

Điều thú vị khi cập nhật hệ thống RAG để xử lý hình ảnh là điều này cho phép bạn

hệ thống sử dụng nhiều định dạng tệp phổ biến có thể dễ dàng chuyển đổi thành hình ảnh.

Ví dụ: các trang trình bày và tệp PDF có thể dễ dàng được coi là tệp hình ảnh.

Tuy nhiên, một thách thức với các định dạng này là cách các trang trình bày và tệp PDF chứa nhiều thông tin được hiển thị.

có thể được.

Một trang hoặc slide có thể chứa văn bản, biểu đồ, chú thích và hình ảnh.

Một vectơ duy nhất sẽ gặp khó khăn trong việc nắm bắt tất cả sắc thái trên một trang của tệp PDF.

Nói cách khác, bạn cần chia nhỏ hình ảnh giống như cách bạn chia nhỏ văn bản.

Ban đầu, việc này được thực hiện bằng các kỹ thuật khá phức tạp để phát hiện các phần khác nhau của

một trang PDF.

Các thuật toán này cố gắng xác định phần nào của trang là biểu đồ, phần nào là biểu đồ

hình ảnh, đó là văn bản, v.v.

Tuy nhiên, trên thực tế, những kỹ thuật này vẫn khá dễ mắc lỗi và khó thực hiện.

Một cách tiếp cận mới hơn, được gọi là PDF RAG, chỉ chia mỗi trang thành một lưới các ô vuông mà không cần

lo lắng về việc liệu những ranh giới đó có rơi vào những vị trí hợp lý hay không.

Mỗi hình vuông sau đó được nhúng vào một vectơ dày đặc bằng mô hình nhúng đa phương thức.

Điều này có nghĩa là trang của bạn được biểu thị bằng một nghìn vectơ thay vì một vectơ.

Tìm kiếm vectơ sau đó hoạt động rất giống với Colbert.

Mỗi từ trong lời nhắc sẽ tìm ô vuông phù hợp nhất trên một trang nhất định.

Những điểm này sau đó được cộng lại để tính điểm tổng thể của trang tài liệu.

Cách tiếp cận này rất linh hoạt vì bất kỳ hình ảnh nào cũng có thể được chia thành một lưới các ô vuông.

Trong thực tế, nó cũng thực hiện tốt các nhiệm vụ truy xuất.

Thực tế là cách tiếp cận này rất linh hoạt và hoạt động tốt có nghĩa là đây là một phương pháp đầy hứa hẹn.

hướng để hỗ trợ truy xuất đa phương thức.

Nhược điểm chính của nó là nó yêu cầu cơ sở dữ liệu vector của bạn lưu trữ một số lượng lớn

của các vectơ.

Tuy nhiên, các nhà cung cấp cơ sở dữ liệu vector đang ngày càng triển khai nhiều công cụ để cho phép

kiểu truy xuất đa phương thức này và bạn có thể mong đợi nó sẽ tiếp tục trở nên dễ dàng hơn

để xây dựng hệ thống RAG xung quanh các cơ sở kiến thức đa phương thức.

RAG đa phương thức vẫn là một công nghệ tiên tiến với sự phát triển nhanh chóng và tích cực.

Hầu hết các nhà cung cấp LLM đều cung cấp mô hình tầm nhìn ngôn ngữ, trong khi các mô hình nhúng đa phương thức thì cung cấp

cung cấp thử nghiệm tương đối nhiều hơn.

Điều đó có nghĩa là, khi bạn tìm cách nâng cao giới hạn những gì hệ thống RAG của bạn có thể làm, hãy mong đợi

thấy sự tiến bộ thú vị và liên tục trong thế giới RAG đa phương thức.