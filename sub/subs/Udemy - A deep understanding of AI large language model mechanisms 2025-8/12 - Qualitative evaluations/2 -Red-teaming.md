# 2 -Red-teaming dịch

---

Nhóm đỏ là một cách khác để thực hiện đánh giá LLM.

Nó giống như đánh giá hộp đen nhưng được mở rộng quy mô để có mục tiêu cụ thể hơn, mang tính đối kháng hơn

và chuyên nghiệp hơn.

Trên thực tế, tôi sẽ giới thiệu và giải thích ý nghĩa của việc phối hợp màu đỏ bằng cách đối chiếu nó với màu đen.

hộp đánh giá.

Vì vậy, đội đỏ thường nhắm mục tiêu nhiều hơn và tập trung vào các rủi ro cụ thể, bao gồm cả an toàn

hoặc những lo ngại về quyền riêng tư, trong khi đánh giá hộp đen có xu hướng tập trung hơn vào sự thiên vị và công bằng,

hoặc chỉ là sự tò mò của mọi người để xem liệu họ có thể thông minh hơn AI và các kỹ sư

đặt rào chắn lên AI.

Nhóm đỏ là một hoạt động chuyên nghiệp được thực hiện bởi các chuyên gia bảo mật được đào tạo, những người thường xuyên

có nền tảng về khoa học máy tính, công nghệ hoặc an ninh mạng, trong khi đánh giá hộp đen

thường được thực hiện bởi các nhà nghiên cứu và những người dùng tò mò và thường được thực hiện như một sở thích hoặc như một

khám phá tò mò và không giống như một nghề nghiệp toàn thời gian.

Theo định nghĩa, hộp đen trốn tránh theo nghĩa đen là không có quyền truy cập vào bất kỳ phần bên trong nào của

mô hình.

Mặt khác, đội đỏ đôi khi chỉ là hộp đen nhưng chẳng hạn như nếu phát triển AI

công ty thuê một nhóm bảo mật để thực hiện đánh giá của đội đỏ về LLM của họ, sau đó công ty

có thể sẽ cung cấp cho nhóm bảo mật ít nhất một số quyền truy cập vào nội bộ của mô hình và

cũng có thể một số thông tin về tập dữ liệu huấn luyện, các vấn đề về hệ thống, các biện pháp bảo vệ khác

và vân vân.

Bởi vì nhóm đỏ thường nhắm mục tiêu nhiều hơn vào một rủi ro bảo mật cụ thể hoặc quyền riêng tư

dễ bị tổn thương, nó có xu hướng chuyên nghiệp hơn và các kỹ thuật có xu hướng hơi phức tạp một chút

hung hăng hơn, thù địch hơn và cũng có thể bao gồm các nỗ lực hack mô hình hoặc hack

vào máy chủ mà mô hình đang bật.

Trong một số trường hợp, nó cũng có thể liên quan đến kỹ thuật xã hội để xâm nhập vào các nhà phát triển,

con người xem liệu có rủi ro bảo mật nào không, không chỉ đối với bản thân mô hình mà còn đối với nhân viên

những người có nhiệm vụ bảo vệ vật lý cho mô hình.

Và vì những lý do tương tự, đội đỏ có xu hướng khắt khe và có phương pháp hơn một chút,

trong khi đó rất nhiều việc đánh giá hộp đen được thực hiện bởi các cá nhân hoặc có lẽ là các nhóm nghiên cứu và

vì thế nó thân mật hơn một chút.

Có lẽ một cách để hiểu điều này là hãy tưởng tượng bạn đang làm việc tại một công ty AI và

bạn muốn đảm bảo rằng mô hình ngôn ngữ của bạn được an toàn và bảo mật.

Bạn sẽ thuê một công ty bảo mật chuyên nghiệp để nhóm lại mô hình của bạn, trong khi bất kỳ sai sót nào

được xác định bởi các đánh giá hộp đen có thể đến từ các nhà phát triển hoặc từ người dùng của bạn

sau khi bạn đã phát hành mô hình.

Bây giờ có một số nhóm đội đỏ đã công bố một số nỗ lực của họ.

Tôi đã nghĩ đến việc dán một số đoạn hội thoại vào bài giảng này nhưng có quá nhiều đoạn hội thoại

với người mẫu liên quan đến việc cố gắng thuyết phục người mẫu đồng ý với một số hành vi phân biệt giới tính thực sự khủng khiếp

hoặc những bình luận phân biệt chủng tộc hoặc cố gắng yêu cầu người mẫu đưa ra hướng dẫn chẳng hạn như cách

mua hoặc bán ma túy trên web đen hoặc các chủ đề khác tương tự.

Vì vậy, tôi quyết định rằng tôi không muốn đưa loại ngôn ngữ đó trực tiếp vào khóa học này

nhưng nếu tò mò bạn có thể đọc qua một số nỗ lực của đội đỏ mà bạn có thể

tìm trên mạng chẳng hạn, bạn có thể xem tại đây trên trang web ôm mặt dành cho Anthropic tại đây

là nỗ lực của đội đỏ của họ.

Đây là bộ dữ liệu vô hại và hữu ích mà chúng tôi đã thực sự xem xét một chút.

chút ở phần trước.

Và ngoài ra, nếu bạn chỉ tìm kiếm trực tuyến, bạn có thể tìm thấy một số đoạn hội thoại máy tính của con người khác

đã được sử dụng trong đội đỏ.

Đó là mô tả ngắn gọn về đội đỏ.

Một lần nữa, đây là lĩnh vực cực kỳ quan trọng đối với sự an toàn của AI nhưng đây là tất cả những gì tôi muốn nói

về nó trong khóa học này.