# 1 - Những hứa hẹn và thách thức của việc đánh giá định lượng được dịch

---

Chào mừng bạn đến với phần này của khóa học.

Bây giờ bạn đã hiểu về kiến trúc của LLM và cách chúng được đào tạo

và được tinh chỉnh, đã đến lúc bắt đầu tìm hiểu về cách chúng ta đánh giá các mô hình đã được đào tạo.

Có cả phương pháp đánh giá định lượng và định tính.

Điều đó có nghĩa là chúng tôi có thể đính kèm điểm số hoặc con số vào hiệu suất và khả năng của LLM.

Về cơ bản, nó giống như đưa ra một bài kiểm tra ở trường cho một người mẫu và sau đó người mẫu đó sẽ được chấm điểm,

giống như bạn sẽ được điểm nếu bạn làm bài kiểm tra ở trường.

Các biện pháp định tính mà tôi sẽ thảo luận trong phần tiếp theo,

là những cách xem xét đầu ra của mô hình mà chúng ta có thể mô tả bằng từ ngữ và đánh giá chủ quan,

nhưng chúng tôi thực sự không có cách nào để tự động hóa việc đánh giá.

Vì vậy, mục tiêu của video giới thiệu này là giải thích mục tiêu và thách thức của việc đánh giá định lượng

và cũng để giới thiệu cho bạn thứ gọi là Định luật Lòng nhân ái,

điều mà bạn chắc chắn cần biết khi nghiên cứu bất kỳ điều gì liên quan đến sự liên kết và an toàn kỹ thuật của AI.

Và đây cũng là một khái niệm hay để hiểu vì nó liên quan đến kinh tế,

chính phủ, xã hội, văn hóa, giáo dục, v.v., nằm ngoài bối cảnh của LLM.

Mục tiêu chung của đánh giá định lượng là có một chuẩn mực hoặc thực chất là một bộ chuẩn mực

mà mọi người có thể sử dụng để đánh giá khả năng của một mô hình ngôn ngữ.

Ví dụ, nó khá trực quan. Rõ ràng là GPT-4 tốt hơn GPT-2,

nhưng chúng tôi muốn có một số con số mà chúng tôi có thể sử dụng để đánh giá những cải tiến và khả năng trong các mô hình khác nhau.

Bây giờ, những con số chuẩn này sẽ phản ánh khả năng của LLM,

và bao gồm từ cú pháp, ngữ pháp cấp thấp rất cơ bản và cách sử dụng từ cho đến kiến thức thế giới

và cả những việc như lý luận, viết mã, giải các bài toán,

biết về chi tiết của một kỹ thuật y tế cụ thể hoặc bất kỳ lĩnh vực chủ đề nào.

Một số phương pháp đánh giá cũng được thiết kế để kiểm tra hành vi không an toàn tiềm ẩn trong LLM.

Ví dụ: nếu một người mẫu có thể bị lừa nói cho bạn biết cách đột nhập vào tài khoản email của ai đó hoặc chế tạo vũ khí.

Và chúng tôi cũng muốn các tiêu chuẩn đánh giá này được chuẩn hóa theo cách mà chúng có thể được so sánh trực tiếp giữa các LLM khác nhau,

có thể có số lượng tham số khác nhau hoặc các loại kiến trúc khác nhau hoặc được phát triển bởi các tổ chức và công ty khác nhau.

Một lần nữa, bạn có thể nghĩ về thử nghiệm tiêu chuẩn hóa được thực hiện ở người.

Vì vậy, đây đều là những mục tiêu nghe có vẻ rất hay và sẽ tuyệt vời phải không?

Nếu nó đơn giản như thực hiện một bài kiểm tra, họ sẽ cung cấp cho chúng tôi một con số hoàn toàn chính xác về khả năng của tất cả các mô hình mà chúng tôi có thể sử dụng để đánh giá

và chúng tôi có thể áp dụng nó cho mọi LLM.

Chà, thật không may, nó không hoàn toàn đơn giản như vậy.

Có rất nhiều thách thức và hạn chế của các phương pháp đánh giá này.

Tôi cũng sẽ thảo luận về những thách thức và khó khăn cụ thể trong phần còn lại của phần này.

Và trước khi bắt đầu trình bày danh sách này ở đây, tôi chỉ muốn nhấn mạnh rằng những điểm không hoàn hảo, sai sót cũng như những hạn chế của các thước đo đánh giá định lượng

không phải vì những phương pháp này được phát triển bởi những người lười biếng kém thông minh.

Hoàn toàn ngược lại. Vấn đề là các mô hình, mô hình ngôn ngữ, thực sự phức tạp và có nhiều khả năng, một số trong đó chúng ta thậm chí còn không hiểu hết.

Và ngôn ngữ của con người cũng thực sự phức tạp và cũng thực sự mơ hồ.

Vì vậy, đây là những thách thức cơ bản và chúng ta có những vấn đề tương tự khi đánh giá định lượng ở người.

Ví dụ, ngay cả kỳ thi SAT nổi tiếng được sử dụng ở Mỹ để vào đại học cũng được biết là về cơ bản không có khả năng dự đoán về thành công trong cuộc sống trong tương lai.

Và bạn biết điều này chính mình. Bạn biết liệu bạn có phải là người tốt hay không, liệu bạn có có một cuộc sống tốt đẹp, hiệu quả, ý nghĩa và hạnh phúc hay không,

thực sự không phụ thuộc vào việc bạn có thể giải một số phương trình toán cụ thể tốt đến mức nào khi bạn 17 tuổi.

Dù sao đi nữa, hãy để tôi xem. Điểm này về cơ bản tôi chỉ đề cập đến.

Ngôn ngữ rất phức tạp và năng động. Có những khó khăn trong việc xác định điều gì tạo nên câu trả lời đúng mà một mô hình đưa ra.

Bạn sẽ thấy các ví dụ cụ thể về điều này ở phần sau. Nhưng giả sử một mô hình được cho là dự đoán từ ghế trong một câu, nhưng thay vào đó, mô hình đó lại dự đoán từ ghế dài.

Bây giờ, điều đó hoàn toàn không chính xác, nhưng nó vẫn có thể là một phản hồi thích hợp trong bối cảnh đó. Đó chỉ là một ví dụ đơn giản.

Liên quan, nhiều phương pháp Eval rất khó hoặc mơ hồ đối với con người. Và xem xét rằng các LLM này được thiết kế để sử dụng ngôn ngữ của con người, không thực sự rõ ràng là chúng ta có thể tin tưởng vào hiệu suất LLM trong một nhiệm vụ ngôn ngữ mà con người cũng gặp khó khăn hoặc ít nhất là có một số mơ hồ về nó.

Một vấn đề khác là trang bị quá mức. Ở đây, vấn đề là khi các công ty phát triển AI biết đến phương pháp Eval, họ có thể bắt đầu tinh chỉnh mô hình của mình trong các thử nghiệm đó.

Bây giờ, ngay cả khi có một số tập hợp nắm giữ mà nhóm đánh giá giữ bí mật, LLM vẫn có thể được tinh chỉnh để hiểu và hoạt động tốt dựa trên loại đánh giá mà phương pháp đánh giá dựa vào.

Một vấn đề khác là các phương pháp mở rất khó đánh giá và có thể không có cơ sở thực tế để so sánh. Ở đây, bạn có thể nghĩ về mô hình viết một bài luận hoặc tóm tắt một văn bản dài hoặc viết một số mã Python.

Điểm này ở đây có nghĩa là bạn có thể nhận được các kết quả đầu ra rất khác nhau của một mô hình bằng cách nhắc nó theo những cách hơi khác nhau. Điều này gây khó khăn cho việc tái tạo một điểm cụ thể trong bài đánh giá Đánh giá.

Vì vậy, giả sử bạn đang cố gắng yêu cầu mô hình thực hiện một tác vụ và nó có thể thực hiện với độ chính xác 95% hoặc 60% tùy thuộc vào cụm từ của lời nhắc bạn sử dụng.

Hoặc có thể do việc tạo mã thông báo ngẫu nhiên này, ngay cả với cùng một lời nhắc, cùng một mô hình và cùng đánh giá thử nghiệm, hiệu suất cũng có thể thay đổi từ 60% đến 90%, đơn giản vì mô hình đang tạo ra một luồng mã thông báo mới mỗi lần nó chạy.

Và cuối cùng, chúng tôi có vấn đề về chi phí và khả năng mở rộng. Một số phương pháp Đánh giá rất tốn kém và tốn thời gian để chạy và đôi khi bạn cần một chuyên gia để đánh giá hiệu suất của mô hình và khi đó điều đó có thể còn tốn kém và tốn thời gian hơn.

Chà, đây không phải là danh sách đầy đủ mà chỉ là cái nhìn tổng quan về những khó khăn của việc đánh giá định lượng. Tôi hy vọng tôi không quá chỉ trích lĩnh vực này.

Đánh giá định lượng là cực kỳ quan trọng và cũng thực sự hữu ích trong việc giúp chúng tôi không chỉ hiểu sự phát triển và kiến ​​trúc của LLM mà còn giúp chúng tôi xác định các vấn đề, sai sót và rủi ro an toàn mà LLM phát triển.

Các công ty phát triển LLM có thể sử dụng để đảm bảo không chỉ AI tốt hơn, AI có khả năng cao hơn mà còn AI an toàn hơn.

Vì vậy, quan điểm của tôi ở đây là thực sự không dễ để thực hiện loại công việc này.

Bây giờ tôi sẽ kể cho bạn nghe về một thứ gọi là Luật Trái tim nhân hậu. Nó được đặt theo tên của một nhà kinh tế học người Anh và theo Google, nó trông giống thế này.

Vì vậy, câu trích dẫn là, khi một biện pháp trở thành mục tiêu, nó không còn là một biện pháp tốt nữa. Điều đó có nghĩa là gì? Điều này có nghĩa là nếu bạn đang cố gắng cải thiện điều gì đó chỉ bằng cách tăng điểm của một phép đo cụ thể thì phép đo đó không còn hữu ích nữa vì mọi người sẽ chỉ cố gắng tăng điểm thay vì cố gắng cải thiện thứ mà bạn đang cố gắng đo lường.

Hãy để tôi xem qua một vài ví dụ để bạn hiểu điều này có nghĩa là gì. Hãy tưởng tượng có những con rắn hổ mang hoang dã ở một đất nước và chúng rất nguy hiểm cho trẻ em.

Vì vậy, chính phủ đưa ra phần thưởng cho những người mang rắn hổ mang chết về. Tất nhiên chính phủ đã có một ý tưởng hay, đó là loại bỏ quần thể rắn hổ mang.

Nhưng kết quả là người ta bắt đầu nuôi rắn hổ mang chỉ để giết chúng. Và thế là chúng ta thậm chí còn có nhiều rắn hổ mang hơn trước.

Một ví dụ khác là trong lĩnh vực chăm sóc sức khỏe, nơi các bệnh viện được đánh giá một phần dựa trên số liệu thống kê như thời gian lưu trú.

Một lần nữa, điều này ban đầu nghe có vẻ tuyệt vời vì bệnh viện càng có thể chăm sóc bệnh nhân tốt hơn thì những bệnh nhân đó sẽ rời bệnh viện càng sớm.

Nhưng điều cuối cùng xảy ra là bệnh nhân được xuất viện quá sớm khi vẫn còn bệnh, có thể vẫn còn lây nhiễm hoặc vết thương chưa lành.

Một ví dụ khác là trong giáo dục, nơi các bài kiểm tra định lượng được sử dụng để đánh giá trường học, từ đó xác định số tiền tài trợ mà khu học chánh sẽ nhận được.

Một lần nữa, điều này có vẻ như là một hệ thống công bằng và dựa trên thành tích. Nhưng vấn đề là các trường chỉ mới bắt đầu dạy học sinh cách làm tốt bài kiểm tra tiêu chuẩn, điều đó có nghĩa là học sinh không học được những kỹ năng và kiến ​​thức thực sự sẽ giúp ích cho các em trong tương lai.

Bây giờ bạn có thể thấy rằng cho đến nay, không có ví dụ nào trong số này liên quan đến AI hoặc LLM.

Luật Goodheart không dành riêng cho AI. Đó là nguyên tắc chung trong quản trị, kinh tế và văn hóa.

Nhưng nó thường được thảo luận trong bối cảnh AI vì các mô hình có thể dễ dàng được tinh chỉnh về cơ bản đối với bất kỳ tác vụ dựa trên ngôn ngữ nào hoặc thực sự là bất kỳ tác vụ nào có thể được biểu diễn dưới dạng chuỗi mã thông báo.

Vì vậy, giả sử ngày mai bạn có một ý tưởng thiên tài về một phương pháp đánh giá LLM hoàn toàn mới, nó thực sự tuyệt vời và nó cũng khác với tất cả các phương pháp khác hiện đang tồn tại.

Vì vậy bạn công khai phương pháp đánh giá của mình để mọi người có thể sử dụng.

Hiện tại, trong vài tháng đầu tiên, bài kiểm tra của bạn là phương pháp eVal tốt nhất hiện có và nó thực sự nêu bật tất cả các khả năng cũng như sự khác biệt giữa các LLM khác nhau.

Vấn đề là tất cả các công ty LLM đều muốn mô hình của họ thực hiện tốt bài kiểm tra của bạn.

Vì vậy, họ bắt đầu tinh chỉnh mô hình của mình một cách cụ thể để hoạt động tốt theo phương pháp mà bạn đã phát triển.

Và rồi trong vòng nửa năm, đột nhiên tất cả các LLM này đang làm theo phương pháp của bạn tốt hơn nhiều so với trước đây.

Và đó là bởi vì các mô hình được điều chỉnh cụ thể theo phương pháp của bạn chứ không phải để cải thiện bất kỳ khả năng nào mà bạn nghĩ rằng đánh giá đánh giá của bạn thực sự đo lường được.

Được rồi bây giờ tôi muốn nói vài lời về cách tổ chức phần này.

Trong tâm trí tôi có một hệ thống phân cấp các cấp độ đánh giá.

Đây là một hệ thống phân cấp độ phân giải chi tiết. Nó không phải là một hệ thống phân cấp về chất lượng hay tầm quan trọng.

Vì vậy, ở mức độ chi tiết tốt nhất, có các đánh giá cấp độ mã thông báo dựa trên việc xem nhật ký mô hình,

có thể ghi nhật ký biến đổi softmax. Và đây là cách bạn đánh giá các kỹ năng ngôn ngữ cấp thấp cơ bản của mô hình về cú pháp, ngữ pháp và thống kê cặp từ như những từ nào có thể xuất hiện trong bối cảnh gần đây, v.v.

Sau đó chúng ta có phương pháp đánh giá mức độ câu.

Ở đây, bạn có thể nghĩ về điểm số dựa trên độ chính xác giống như các bài kiểm tra trắc nghiệm trong đó mô hình được cung cấp một số tùy chọn với một số bối cảnh cơ bản và nó phải chọn tùy chọn nào là đúng nhất.

Những loại biện pháp này đánh giá sự hiểu biết về ngữ pháp của mô hình nhưng đó cũng là kiến ​​thức về thế giới vì tất cả các lựa chọn trong bài kiểm tra trắc nghiệm có thể đúng về mặt ngữ pháp.

Nhưng chỉ có một là phù hợp dựa trên cách thế giới vận hành.

Và cuối cùng, chúng ta có các phương pháp cấp độ diễn ngôn trong đó chúng ta đang xem xét phân bổ thống kê xác suất của mã thông báo trên hàng trăm hoặc hàng nghìn mã thông báo được tạo.

Ở đây chúng ta không xem xét khả năng dự đoán mã thông báo tiếp theo hoặc thậm chí chọn câu trả lời đúng của mô hình.

Thay vào đó, chúng tôi quan tâm đến việc liệu mô hình có thể tạo ra ngôn ngữ có cảm giác giống hoặc đọc giống nội dung mà con người viết hay không.

Vậy là xong video giới thiệu này.

Tôi muốn nhấn mạnh một lần nữa rằng các phương pháp Đánh giá là một phần thực sự quan trọng trong sự phát triển và an toàn của AI.

Nhưng thực sự rất khó để thực hiện loại công việc này vì nó nằm ở điểm giao thoa của nhiều hiện tượng phức tạp bao gồm sự phức tạp của LLM cũng như sự phức tạp và mơ hồ của ngôn ngữ con người.