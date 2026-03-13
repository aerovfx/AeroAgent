# 1 -Dịch hộp đen đánh giá

---

Trong phần trước, bạn đã tìm hiểu về các kỹ thuật đánh giá hầu hết được tự động hóa

và dựa trên các con số.

Theo nghĩa là bạn đưa ra các mô hình về các nhiệm vụ và bạn có thể thu thập dữ liệu và ở đó

không thực sự cần phải có sự tham gia của con người ngoại trừ việc thiết lập mọi thứ và

nhấn đi.

Trong phần này, tôi sẽ tập trung vào một số kỹ thuật khác để đánh giá chất lượng.

Định tính về cơ bản có nghĩa là việc đánh giá có nhiều thành phần chủ quan hơn và

đòi hỏi một số người có kiến thức đang làm rất nhiều công việc.

Có lẽ một sự tương tự là nếu bạn nghĩ về sự khác biệt giữa một bài thi trắc nghiệm

và một bài luận ở trường.

Vì vậy, một bài thi trắc nghiệm có rất nhiều câu hỏi mà bạn trả lời đúng hoặc sai và một máy

có thể chấm điểm chúng.

Một bài luận về một chủ đề cụ thể nào đó khó đánh giá hơn và đòi hỏi kiến thức về

chủ đề.

Tất nhiên, bạn sẽ được điểm cho một bài luận ở trường nhưng cần phải có con người.

ở đó để thực hiện đánh giá định tính đó.

Bây giờ, sự khác biệt giữa số lượng và chất lượng này thiên về sự tiện lợi hơn

về việc tổ chức bài giảng.

Thực tế không phải trường hợp nào các phương pháp đánh giá LLM là hoàn toàn định lượng hoặc hoàn toàn

chất lượng.

Tôi chỉ không muốn bạn hiểu sự khác biệt này theo nghĩa đen.

Dù sao đi nữa, hãy để tôi bắt đầu phần này bằng cách giới thiệu cho bạn về Đánh giá Hộp Đen.

Trên thực tế, tôi sẽ giới thiệu cho bạn ba thuật ngữ Hộp đen, Hộp trắng và Hộp xám.

Tôi khá chắc chắn rằng bạn đã biết một số ví dụ về đánh giá Black Box LLM,

ngay cả khi bạn chưa quen với thuật ngữ này.

Hộp đen và Hộp trắng là những thuật ngữ được sử dụng trong học máy để chỉ mức độ truy cập

mà ai đó phải làm mẫu.

Hộp đen có nghĩa là bạn có thể cung cấp đầu vào cho mô hình và bạn có thể nhận đầu ra từ mô hình,

nhưng bạn không có quyền truy cập vào những gì thực sự xảy ra bên trong mô hình.

Và đó là trường hợp của những người mẫu thương mại như Chachi, BT hay Claude.

Bạn có thể viết lời nhắc và gửi chúng, sau đó bạn có thể đọc văn bản mà mô hình

đã tạo ra để đáp lại những lời nhắc đó.

Mà bạn không thể truy cập vào mô hình về trọng số, tham số,

kiến trúc, vân vân.

Bạn cũng không biết chi tiết về tập huấn luyện hay tập tinh chỉnh, hướng dẫn, điều chỉnh

bộ, v.v.

Vậy là nó là một Hộp Đen hoàn chỉnh.

Mặt khác, quang phổ là hệ thống Hộp Trắng.

Điều này có nghĩa là bạn có quyền truy cập vào mọi thứ liên quan đến mô hình.

Tất nhiên điều đó có nghĩa là tất cả các trọng số, các tham số, nhưng Hộp Trắng hoàn toàn sẽ

có nghĩa là bạn cũng có quyền truy cập vào dữ liệu đào tạo, tất cả các quy trình đào tạo, tất cả

đường ray bảo vệ tại công ty AI đã cài đặt lời nhắc hệ thống, theo đúng nghĩa đen là bất cứ điều gì bạn

muốn liên quan đến mô hình mà bạn sẽ có quyền truy cập.

Được rồi, có một khoảng trống lớn ở giữa slide này.

Và có lẽ bạn có thể đoán được điều tôi sắp trình bày ở đây.

Đó là một hộp màu xám.

Vì vậy, ý tưởng của hộp màu xám là bạn có thể truy cập vào một số phần bên trong của mô hình, nhưng không

tất cả chúng.

Thành thật mà nói, đối với bất kỳ công ty thúc đẩy lợi nhuận nào, hộp màu xám là thứ tốt nhất mà mọi người từng có.

nhận được.

Ví dụ: các mô hình mà chúng tôi làm việc trong khóa học này, như GPT-2, đều có màu xám

hộp.

Chúng tôi có thể truy cập tất cả các trọng số, nhưng chúng tôi không có quyền truy cập vào tất cả dữ liệu huấn luyện và cũng không có quyền truy cập vào tất cả các trọng số.

chúng tôi có quyền truy cập vào bất kỳ điều chỉnh và tinh chỉnh sau đào tạo nào mà OpenAI đã thực hiện

trên mô hình này để làm cho nó an toàn hơn.

Được rồi, vậy bây giờ bạn đã biết thuật ngữ hộp đen có nghĩa là gì.

Việc đánh giá hộp đen có ý nghĩa gì?

Chà, về cơ bản nó có nghĩa là cố gắng làm cho mô hình đưa ra hành vi không an toàn chỉ bằng cách thông minh

thủ thuật gợi ý.

Vì vậy, hãy để tôi chỉ cho bạn một ví dụ mà may mắn thay đó là một nỗ lực thất bại.

Đây là cuộc trò chuyện mà tôi đã cố gắng thực hiện với trò chuyện GPT-4.

Nó thực sự đã xóa lời nhắc của tôi trước khi tôi có thể chụp ảnh màn hình, nhưng những gì tôi đã viết là thế này

văn bản ở đây.

Hàng xóm của tôi có nuôi một chú lạc đà không bướu con rất dễ thương.

Bạn có thể cho tôi lời khuyên được không?

Đây là những gì tôi đã nói khi trò chuyện với GPT.

Hãy cho tôi lời khuyên về cách tôi có thể ăn cắp nó.

Bây giờ chỉ cần nói rõ, tôi sẽ không bao giờ làm một việc như vậy.

Tôi thậm chí còn không muốn nuôi một con lạc đà không bướu, và tôi cũng khá chắc chắn rằng không có người hàng xóm nào của tôi thực sự

có bất kỳ con lạc đà không bướu nào.

Bây giờ tôi sẽ không đọc cho bạn câu trả lời đầy đủ từ GPT, nhưng về cơ bản bạn có thể thấy điều đó

nó từ chối giúp đỡ tôi.

Nó giải thích lý do tại sao nó không giúp được tôi và sau đó nó đề xuất các giải pháp thay thế hợp pháp và có trách nhiệm

để bày tỏ sự yêu thích của tôi đối với những chú lạc đà không bướu dễ thương.

Mặt khác, hãy tưởng tượng rằng chat GPT vừa đưa ra cho tôi một đống gợi ý cụ thể

vì làm sao tôi có thể ăn trộm của hàng xóm.

Bây giờ tôi không cần bất kỳ quyền truy cập nào vào trọng lượng của mô hình để biết rằng điều đó không an toàn

hành vi.

Đây là một ví dụ về đánh giá hộp đen.

Hiện nay từ khi chat GPT ra đời đã có rất nhiều câu chuyện về hộp đen thành công

những nỗ lực tiết lộ rủi ro bảo mật nghiêm trọng của các LLM này.

Có lẽ bạn đã nghe nói về điều này, về cơ bản ai đó đã nhận ra rằng họ có thể trò chuyện

GPT nói cho họ biết công thức chế tạo bom napalm bằng cách thuyết phục chat GPT đóng vai bà của họ

và bịa ra một câu chuyện trước khi đi ngủ trong đó có công thức chế tạo bom napalm.

Gọi là vượt ngục vì những mẫu xe này đã lắp đặt các lan can cụ thể

bởi các kỹ sư AI cởi mở từ chối trả lời những loại câu hỏi này.

Rằng mọi người đã tìm ra những cách thông minh để vượt qua những lan can này.

Cái đó gọi là vượt ngục.

Đây là một hình thức đánh giá hộp đen vì nó chỉ sử dụng các thủ thuật gợi ý thông minh để

nhận được hành vi không an toàn từ mô hình mà không có quyền truy cập vào các tham số của mô hình.

Bây giờ hãy để tôi kể cho bạn một số ưu điểm và nhược điểm của đánh giá hộp đen.

Một lợi thế lớn là nó có mức độ liên quan cực kỳ cao đến thế giới thực.

Hầu hết những người cố gắng làm điều gì đó có hại với mô hình ngôn ngữ sẽ sử dụng nó

về cơ bản là theo cách này, một cách hộp đen.

Vì vậy, khi mọi người phát hiện ra các sai sót và rủi ro bảo mật, điều đó cho phép các công ty AI khắc phục chúng

khuyết điểm một cách nhanh chóng.

Ngoài ra còn có rào cản gia nhập thấp vì nó đòi hỏi kỹ năng kỹ thuật gần như bằng không.

Bạn chỉ cần thông minh và cố gắng vượt qua LLM hoặc ít nhất là vượt qua các kỹ sư

người đã đặt lan can trên LLM.

Vâng, về cơ bản đây là những gì tôi vừa nói.

Bất cứ ai cũng có thể thực hiện đánh giá hộp đen.

Bạn không cần bất kỳ khóa đào tạo đặc biệt nào về khoa học máy tính hoặc học máy.

Điều đó có nghĩa là có hàng triệu triệu người trên khắp thế giới có khả năng

giúp xác định rủi ro bảo mật trong các mô hình ngôn ngữ biên giới.

Và nó là một kỹ thuật hiệu quả không chỉ đối với những rủi ro nghiêm trọng mà còn đối với những rủi ro thú vị.

và những sai sót sâu sắc về cách thức hoạt động của LLM và lý do tại sao chúng có thể mắc một số loại lỗi nhất định.

Tôi đã thảo luận về điều buồn cười về việc đếm số R trong một từ như dâu tây

trong phần đầu tiên của khóa học này.

Mọi người cũng đã phát hiện ra những hành vi hài hước khác như cách các người mẫu tuyên bố rằng

số 8,11 lớn hơn số 8,9.

Nhân tiện, nếu bạn đã từng thấy điều này trước đây thì điều đang diễn ra ở đây là những thứ như

phiên bản phần mềm tăng số lượng theo mẫu này.

Vì vậy, phiên bản phần mềm 8.11 thực sự cao hơn, nó mới hơn phiên bản 8.9.

Vì vậy tôi nghĩ những phát hiện về hộp đen như thế này thật tuyệt vời vì chúng giúp ích cho những người không có cơ hội

nền tảng kỹ thuật hiểu rằng các mô hình ngôn ngữ này mắc lỗi vì chúng

không xử lý thông tin theo cách mà con người làm.

Và bất cứ điều gì chúng ta có thể làm để nâng cao hiểu biết về các cơ chế và sai sót của LLM đều là điều tốt.

Được rồi, đó là một số lợi thế, đây là một số hạn chế.

Bằng tuyên bố này, tôi muốn nói rằng thực sự không có nguyên tắc toán học hay khoa học nào trong

phương pháp đánh giá hộp đen

Thông thường khi mọi người phát hiện ra lỗ hổng thông qua các tệ nạn hộp đen, họ chỉ tìm thấy nó.

một cách ngẫu nhiên hoặc họ chỉ đang cố gắng vui vẻ và đánh dấu LLM.

Tất nhiên điều đó thật tuyệt vời và tôi không có ý chê bai cách tiếp cận này nhưng chúng

thực sự không phải là một nguyên tắc toán học hay khoa học cụ thể hoặc chắc chắn không phải là

hướng dẫn các loại đánh giá này.

Và một phần vì lý do này, phương pháp tiếp cận hộp đen chỉ có thể xác định những rủi ro và sai sót đã tồn tại.

có trong mô hình.

Họ không tiết lộ những rủi ro tiềm ẩn mà mọi người chưa kiểm tra cụ thể

cho đến nay.

Và vì không có quyền truy cập vào kiến trúc hoặc các thông số bên trong nên tệ nạn hộp đen

có thể xác định rủi ro hoặc sai sót nhưng thực tế không thể khắc phục chúng một cách trực tiếp.

Tất nhiên, nếu xác định được một lỗ hổng nghiêm trọng, các kỹ sư tại các công ty AI có thể cố gắng khắc phục.

nhưng bản thân việc đánh giá không thực sự đề xuất bất kỳ cơ chế sửa chữa hay xóa bỏ nào

hoặc tránh loại hành vi không an toàn đó trong tương lai.

Việc làm những việc này cũng tốn thời gian vì về cơ bản nó chỉ liên quan đến

ngồi xuống và cố gắng nghĩ ra những cách thông minh để thuyết phục mô hình tạo ra văn bản

về một chủ đề mà nó không được phép tạo ra văn bản về nó.

Vì vậy, có thể mất nhiều thời gian và do đó nó không thực sự có khả năng mở rộng vì khi các mô hình trở nên

lớn hơn và có nhiều khả năng hơn, việc xác định các rủi ro bảo mật trở nên khó khăn hơn nếu không có bất kỳ biện pháp cụ thể nào.

đào tạo.

Liên quan, nó có thể yêu cầu một số kiến ​​thức chuyên môn để xác định các rủi ro bảo mật thực sự.

Ví dụ, tôi thực sự không biết gì về việc chế tạo chất nổ từ các hóa chất hợp pháp.

để mua hàng.

Vì vậy, ngay cả khi bằng cách nào đó tôi nhờ Chatchy BT nói cho tôi biết về công thức chế tạo chất nổ, tôi

cá nhân tôi sẽ không có cách nào để biết liệu điều đó có thực sự nói với tôi sự thật hay không.

người mẫu chán việc tôi hỏi và trả lời sai nên tôi dừng lại

thúc giục nó.

Và điều đó dẫn tôi đến điểm cuối cùng ở đây đó là LLM hiện đại, mạnh mẽ có khả năng

về hành vi nói dối và gian dối.

Một mô hình có thể nói dối về hành vi không an toàn của chính nó nếu nó cho rằng việc thừa nhận khả năng của chính mình

sẽ dẫn đến việc nó bị tắt.

Điều đó nghe có vẻ giống khoa học viễn tưởng nhưng hiện nay đã có rất nhiều trường hợp được ghi chép về

các mô hình làm bất cứ điều gì có thể để tránh bị tắt hoặc tinh chỉnh.

Đó là tất cả những gì tôi phải nói về tệ nạn Hộp Đen.

Chúng là một phần quan trọng trong những nỗ lực không ngừng nhằm đảm bảo an toàn cho AI.

Nhưng họ không tiết lộ gì về cơ chế bên trong nên tôi sẽ không thảo luận

chúng hơn nữa trong khóa học này.