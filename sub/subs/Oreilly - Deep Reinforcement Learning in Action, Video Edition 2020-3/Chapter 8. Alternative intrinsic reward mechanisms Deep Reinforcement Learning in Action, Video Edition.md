# Chương 8. Cơ chế khen thưởng nội tại thay thế Học tập củng cố sâu trong hành động, Phiên bản video đã được dịch

---

Mục 8.7, Cơ chế khen thưởng nội tại thay thế

Trong chương này chúng tôi đã mô tả vấn đề nghiêm trọng mà các tác nhân RL gặp phải trong môi trường có

Phần thưởng thưa thớt.

Chúng tôi coi giải pháp là khơi dậy sự tò mò của các đại lý và chúng tôi đã triển khai

một cách tiếp cận từ bài báo Pathack 2017, một trong những bài báo được trích dẫn rộng rãi nhất về củng cố

nghiên cứu học tập trong những năm gần đây.

Chúng tôi chọn thể hiện cách tiếp cận này không chỉ vì nó phổ biến mà còn vì nó xây dựng

về những gì chúng ta đã học ở các chương trước mà không giới thiệu quá nhiều khái niệm mới.

Học tập dựa trên sự tò mò, có nhiều tên gọi, là một lĩnh vực nghiên cứu rất tích cực,

và có nhiều cách tiếp cận khác, một số trong đó chúng tôi nghĩ là tốt hơn

ICM.

Nhiều phương pháp thú vị khác được sử dụng bởi lý thuyết thông tin và suy luận châu Á sắp ra mắt

đưa ra các cơ chế mới để thúc đẩy sự tò mò.

Lỗi dự đoán, PE, cách tiếp cận mà chúng tôi sử dụng trong chương này chỉ là một cách thực hiện

dưới một chiếc ô PE rộng hơn.

Ý tưởng cơ bản, như bạn đã biết, là đại lý muốn giảm PE của mình, hoặc nói cách khác là

nói cách khác, sự không chắc chắn của nó về môi trường.

Nhưng nó phải làm như vậy bằng cách tích cực tìm kiếm cái mới, kẻo nó bị ngạc nhiên bởi điều gì đó.

bất ngờ.

Một chiếc ô khác là trao quyền cho đại lý.

Thay vì tìm cách giảm thiểu lỗi dự đoán và làm cho môi trường trở nên dễ dự đoán hơn,

chiến lược trao quyền tối ưu hóa tác nhân để tối đa hóa khả năng kiểm soát của nó đối với môi trường,

hình 8.21.

Một bài báo trong lĩnh vực này là Tối đa hóa thông tin đa dạng để củng cố động lực nội tại

Bài học của Shakir Muhammad và Danilo Jimenez Resende, 2015.

Chúng ta có thể đưa ra tuyên bố không chính thức về việc tối đa hóa quyền kiểm soát môi trường thành một tuyên bố chính xác

phát biểu toán học mà chúng ta sẽ chỉ tính gần đúng ở đây.

Hình 8.21.

Hai cách tiếp cận chính để giải quyết Vấn đề Phần thưởng thưa thớt bằng các phương pháp giống như sự tò mò

là các phương pháp dự đoán lỗi, giống như phương pháp chúng tôi đã sử dụng trong chương này và các phương pháp trao quyền.

Thay vì cố gắng tối đa hóa sai số dự đoán giữa một trạng thái nhất định và trạng thái được dự đoán tiếp theo.

trạng thái, các phương pháp trao quyền nhằm mục đích tối đa hóa thông tin lẫn nhau, MI, giữa các tác nhân

hành động và trạng thái tiếp theo.

Nếu MI giữa hành động của tác nhân và trạng thái tiếp theo cao, điều đó có nghĩa là tác nhân có

mức độ kiểm soát hoặc quyền lực cao đối với các trạng thái tiếp theo.

Nghĩa là, nếu bạn biết tác nhân đã thực hiện hành động nào, bạn có thể dự đoán tốt trạng thái tiếp theo.

Điều này khuyến khích tác nhân học cách kiểm soát môi trường một cách tối đa.

Tiền đề dựa trên đại lượng gọi là thông tin lẫn nhau, MI.

Chúng tôi sẽ không định nghĩa nó về mặt toán học ở đây, nhưng một cách không chính thức, Michigan đo lường lượng thông tin

được chia sẻ giữa hai nguồn dữ liệu được gọi là biến ngẫu nhiên, vì thông thường chúng ta xử lý

với dữ liệu có mức độ ngẫu nhiên hoặc không chắc chắn.

Một định nghĩa khác ít mang tính todological hơn là MI đo lường mức độ không chắc chắn của bạn

khoảng một đại lượng X bị giảm đi với một đại lượng khác Y.

Lý thuyết thông tin lần đầu tiên được phát triển nhằm giải quyết các vấn đề giao tiếp trong thế giới thực,

trong đó một vấn đề là làm thế nào để mã hóa tin nhắn một cách tốt nhất trên một kênh liên lạc có thể gây nhiễu

sao cho tin nhắn nhận được ít bị sai sót nhất, hình 8.22.

Giả sử chúng ta có một tin nhắn X gốc muốn gửi qua một đường truyền ồn ào

đường dây, ví dụ như sử dụng sóng vô tuyến và chúng tôi muốn tối đa hóa thông tin lẫn nhau

giữa X và tin nhắn nhận được Y. Chúng tôi thực hiện điều này bằng cách phát triển một số cách mã hóa X,

có thể là một tài liệu văn bản, thành một dạng sóng vô tuyến nhằm giảm thiểu

xác suất dữ liệu bị hỏng do nhiễu.

Khi người khác nhận được tin nhắn được giải mã Y, họ có thể yên tâm rằng họ đã nhận được

tin nhắn rất gần với tin nhắn ban đầu.

Sau 8.22, Claude Shannon đã phát triển lý thuyết truyền thông ra đời từ nhu cầu mã hóa

tin nhắn một cách hiệu quả và mạnh mẽ trên các kênh liên lạc ồn ào như được mô tả ở đây.

Mục đích là mã hóa tin nhắn sao cho thông tin lẫn nhau giữa người nhận được

tin nhắn và tin nhắn được gửi là tối đa.

Trong ví dụ của chúng ta, X và Y đều là một loại tin nhắn bằng văn bản, nhưng X và Y thì không cần thiết.

có cùng loại đại lượng. Ví dụ, chúng ta có thể hỏi thông tin chung

là giữa lịch sử giá cổ phiếu một năm của một công ty và doanh thu hàng năm của nó. Nếu như

chúng tôi bắt đầu với một ước tính rất không chắc chắn về doanh thu hàng năm của một công ty, và sau đó

chúng ta tìm hiểu lịch sử giá cổ phiếu trong một năm, sự không chắc chắn của chúng ta giảm đi bao nhiêu? Nếu nó

giảm nhiều, MI cao.

Ví dụ đó liên quan đến số lượng khác nhau, nhưng cả hai đều sử dụng đơn vị đô la cần

cũng không phải vậy. Chúng ta có thể hỏi MI là bao nhiêu giữa nhiệt độ hàng ngày và

việc bán hàng của các cửa hàng kem. Trong trường hợp trao quyền cho tác nhân và học tăng cường,

mục tiêu là tối đa hóa thông tin lẫn nhau giữa một hành động hoặc chuỗi hành động,

và trạng thái hoặc các trạng thái kết quả trong tương lai. Tối đa hóa mục tiêu này có nghĩa là nếu bạn biết

tác nhân đã thực hiện hành động nào, bạn sẽ có độ tin cậy cao về trạng thái kết quả

là. Điều này có nghĩa là tác nhân có mức độ kiểm soát cao đối với môi trường, vì nó có thể

đến được các trạng thái một cách đáng tin cậy dựa trên hành động của nó. Do đó, một đại lý được trao quyền tối đa có tối đa

bậc tự do. Điều này khác với cách tiếp cận lỗi dự đoán vì giảm thiểu

PE trực tiếp khuyến khích sự khám phá, trong khi việc tối đa hóa việc trao quyền có thể tạo ra sự khám phá

hành vi như một phương tiện để học các kỹ năng trao quyền, nhưng chỉ một cách gián tiếp. Hãy xem xét một phụ nữ trẻ,

Sarah, người quyết định đi du lịch khắp thế giới và khám phá càng nhiều càng tốt. Cô ấy đang giảm

sự không chắc chắn của cô ấy về thế giới, đã so sánh cô ấy với Bill Gates, người có khả năng phi thường

người giàu có quyền lực cao. Anh ấy có thể không thích đi du lịch nhiều như Sarah,

nhưng anh ấy có thể nếu anh ấy muốn, và bất kể anh ấy ở đâu vào bất cứ lúc nào, anh ấy có thể đi đến nơi anh ấy muốn

để đi. Cả mục tiêu trao quyền và tò mò đều có trường hợp sử dụng của chúng. Mục tiêu dựa trên trao quyền

đã được chứng minh là hữu ích cho việc đào tạo các đại lý để có được các kỹ năng phức tạp mà không cần bất kỳ

phần thưởng bên ngoài, chẳng hạn như nhiệm vụ robot hoặc trò chơi thể thao, trong khi dựa trên sự tò mò

mục tiêu có xu hướng hữu ích hơn cho việc khám phá. Ví dụ: trò chơi như Super Mario Brothers

nơi mục tiêu là để tiến bộ thông qua các cấp độ. Trong mọi trường hợp, hai số liệu này giống nhau hơn

hơn là chúng khác nhau.