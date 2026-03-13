# Chương 1. Khung học tăng cường Học tăng cường sâu trong thực tế, Phiên bản video

---

Phần 1.4 Khung học tập tăng cường

Richard Bellman đã giới thiệu quy hoạch động như một phương pháp chung để giải một số loại

về các vấn đề về kiểm soát hoặc quyết định, nhưng nó chiếm phần cuối cùng của chuỗi RL. Có thể cho rằng,

Đóng góp quan trọng hơn của Bellman là giúp phát triển khuôn khổ tiêu chuẩn cho

vấn đề RL. Khung RL về cơ bản là bộ lõi

các thuật ngữ và khái niệm mà mọi vấn đề RL đều có thể diễn đạt được. Điều này không chỉ cung cấp

một ngôn ngữ tiêu chuẩn hóa để giao tiếp với các kỹ sư và nhà nghiên cứu khác, nó cũng buộc

chúng ta hình thành các vấn đề của mình theo cách phù hợp với vấn đề giống như lập trình động

phân rã, sao cho chúng ta có thể tối ưu hóa lặp đi lặp lại các vấn đề con cục bộ và thực hiện

tiến tới đạt được mục tiêu cấp cao toàn cầu. May mắn thay, nó khá đơn giản

quá.

Để minh họa cụ thể khung, chúng ta hãy xem xét nhiệm vụ xây dựng thuật toán RL

có thể học cách giảm thiểu việc sử dụng năng lượng tại một trung tâm dữ liệu lớn. Máy tính cần phải được

được giữ mát để hoạt động tốt, vì vậy các trung tâm dữ liệu lớn có thể phải chịu chi phí đáng kể từ việc làm mát

hệ thống. Cách tiếp cận ngây thơ để giữ cho trung tâm dữ liệu luôn mát mẻ là giữ cho máy điều hòa không khí luôn mát

mọi lúc ở mức độ mà không có máy chủ nào chạy quá nóng. Điều này sẽ

không yêu cầu bất kỳ máy học ưa thích nào. Nhưng cách này không hiệu quả và bạn có thể làm tốt hơn,

vì không chắc tất cả các máy chủ ở trung tâm đều nóng cùng lúc,

và mức độ sử dụng trung tâm dữ liệu luôn ở mức như nhau. Nếu bạn nhắm mục tiêu làm mát

đến địa điểm và thời điểm quan trọng nhất, bạn có thể đạt được kết quả tương tự với số tiền ít hơn.

Bước một trong khuôn khổ này là xác định mục tiêu tổng thể của bạn. Trong trường hợp này, tổng thể của chúng tôi

Mục tiêu là giảm thiểu số tiền chi cho việc làm mát, với hạn chế là không có máy chủ nào trong

trung tâm có thể vượt qua một số nhiệt độ ngưỡng. Mặc dù đây dường như là hai mục tiêu,

chúng ta có thể gộp chúng lại với nhau thành một hàm mục tiêu tổng hợp mới. Hàm này trả về

một giá trị lỗi cho biết mức độ chúng tôi không đạt được mục tiêu trong việc đáp ứng hai mục tiêu, được đưa ra

chi phí hiện tại và dữ liệu nhiệt độ cho máy chủ. Con số thực tế mà chúng tôi

Trả về của hàm mục tiêu không quan trọng, chúng tôi chỉ muốn làm cho nó ở mức thấp nhất có thể.

Do đó, chúng ta cần thuật toán RL để giảm thiểu mục tiêu, lỗi, lợi nhuận của hàm này

giá trị đối với một số dữ liệu đầu vào, chắc chắn sẽ bao gồm chi phí vận hành

và dữ liệu nhiệt độ, nhưng cũng có thể bao gồm thông tin ngữ cảnh hữu ích khác có thể

giúp thuật toán dự đoán việc sử dụng trung tâm dữ liệu.

Dữ liệu đầu vào được tạo ra bởi môi trường. Nói chung, môi trường của RL hoặc điều khiển

nhiệm vụ, là bất kỳ quá trình động nào tạo ra dữ liệu có liên quan để đạt được mục tiêu của chúng tôi.

Mặc dù chúng tôi sử dụng “môi trường” như một thuật ngữ kỹ thuật, nhưng nó không quá trừu tượng so với nghĩa của nó.

sử dụng hàng ngày. Là một ví dụ của thuật toán RL rất tiên tiến, bạn luôn ở trong một số tình huống

môi trường, và mắt và tai của bạn liên tục tiêu thụ thông tin do môi trường của bạn tạo ra,

để bạn có thể đạt được mục tiêu hàng ngày của mình. Vì môi trường là một quá trình năng động nên

là một hàm của thời gian, nó có thể tạo ra một luồng dữ liệu liên tục có kích thước và

loại. Để làm cho mọi thứ trở nên thân thiện với thuật toán, chúng ta cần lấy dữ liệu môi trường này và đóng gói

thành các gói riêng biệt mà chúng tôi gọi là trạng thái của môi trường, sau đó phân phối

nó vào thuật toán của chúng tôi ở mỗi bước thời gian riêng biệt. Nhà nước phản ánh kiến thức của chúng tôi

của môi trường tại một thời điểm cụ thể nào đó, giống như một máy ảnh kỹ thuật số ghi lại một hình ảnh rời rạc

ảnh chụp nhanh của một cảnh tại một thời điểm nào đó và tạo ra một hình ảnh có định dạng nhất quán.

Để tóm tắt cho đến nay, chúng tôi đã xác định hàm mục tiêu, giảm thiểu chi phí bằng cách tối ưu hóa nhiệt độ,

đó là chức năng của trạng thái (chi phí hiện tại, dữ liệu nhiệt độ hiện tại) của môi trường,

trung tâm dữ liệu và mọi quy trình liên quan. Phần cuối cùng của mô hình của chúng tôi là thuật toán RL

chính nó. Đây có thể là bất kỳ thuật toán tham số nào có thể học từ dữ liệu để giảm thiểu hoặc tối đa hóa

một số hàm mục tiêu bằng cách sửa đổi các tham số của nó. Nó không cần phải là một thuật toán học sâu.

RL là một lĩnh vực riêng, tách biệt khỏi mối quan tâm của bất kỳ thuật toán học tập cụ thể nào.

Như chúng tôi đã lưu ý trước đây, một trong những điểm khác biệt chính giữa RL hoặc các nhiệm vụ kiểm soát nói chung và

học có giám sát thông thường, đó là trong một nhiệm vụ điều khiển, thuật toán cần thực hiện

quyết định và thực hiện hành động. Những hành động này sẽ có tác động nhân quả đến những gì xảy ra

trong tương lai. Thực hiện hành động là một từ khóa trong khuôn khổ và nó có nghĩa ít nhiều

bạn mong đợi nó có ý nghĩa gì. Tuy nhiên, mọi hành động được thực hiện đều là kết quả của việc phân tích

trạng thái hiện tại của môi trường và cố gắng đưa ra quyết định tốt nhất dựa trên thông tin đó.

Khái niệm cuối cùng trong khung RL là sau mỗi hành động được thực hiện, thuật toán

được trao phần thưởng. Phần thưởng là tín hiệu "cục bộ" về mức độ hiệu quả của thuật toán học

đang thực hiện để đạt được mục tiêu toàn cầu. Phần thưởng có thể là một tín hiệu tích cực

đang hoạt động tốt, hãy duy trì hoặc có tín hiệu tiêu cực, tức là đừng làm điều đó, mặc dù chúng tôi gọi

cả hai tình huống đều là phần thưởng. Tín hiệu khen thưởng là tín hiệu duy nhất cho việc học

thuật toán phải tiếp tục hoạt động khi nó tự cập nhật với hy vọng hoạt động tốt hơn trong lần tiếp theo

trạng thái của môi trường. Trong ví dụ về trung tâm dữ liệu của chúng tôi, chúng tôi có thể trao phần thưởng cho thuật toán

+10, một giá trị tùy ý, bất cứ khi nào hành động của nó làm giảm giá trị lỗi. Hoặc hợp lý hơn,

chúng tôi có thể trao phần thưởng tỷ lệ thuận với mức độ giảm lỗi. Nếu nó tăng

lỗi, chúng tôi sẽ tặng nó một phần thưởng tiêu cực. Cuối cùng, hãy đưa ra thuật toán học tập của chúng ta

một cái tên huyền ảo hơn, gọi nó là "đại lý". Tác nhân là người thực hiện hành động hoặc ra quyết định

thuật toán học trong bất kỳ bài toán RL nào. Chúng ta có thể kết hợp tất cả lại với nhau như trong hình 1.8.

Hình 1.8. Khung tiêu chuẩn cho thuật toán RL. Người đại diện thực hiện một hành động trong

môi trường, chẳng hạn như di chuyển một quân cờ, sau đó cập nhật trạng thái của môi trường.

Đối với mỗi hành động được thực hiện, nó sẽ nhận được phần thưởng, ví dụ: +1 nếu thắng trò chơi, -1 cho

thua trò chơi, ngược lại là 0. Thuật toán RL lặp lại quá trình này với mục tiêu

tối đa hóa phần thưởng về lâu dài và cuối cùng nó học được cách hoạt động của môi trường.

Trong ví dụ về trung tâm dữ liệu của chúng tôi, chúng tôi hy vọng rằng đại lý của chúng tôi sẽ học cách giảm thời gian làm mát

chi phí. Trừ khi chúng ta có thể cung cấp cho nó kiến thức đầy đủ về môi trường, nó

sẽ phải thực hiện một số mức độ thử nghiệm và sai sót. Nếu chúng ta may mắn, đặc vụ có thể biết được

tốt đến mức nó có thể được sử dụng trong các môi trường khác với môi trường mà nó được đào tạo ban đầu.

Vì tác nhân là người học nên nó được triển khai như một loại thuật toán học tập nào đó. Và kể từ đó

đây là cuốn sách về học tăng cường sâu, các tác nhân của chúng tôi sẽ được triển khai bằng cách sử dụng sâu

các thuật toán học tập, còn được gọi là mạng lưới thần kinh sâu (xem hình 1.9). Nhưng hãy nhớ, RL

thiên về loại vấn đề và giải pháp hơn là về bất kỳ thuật toán học tập cụ thể nào,

và bạn chắc chắn có thể sử dụng các lựa chọn thay thế cho mạng lưới thần kinh sâu. Trên thực tế, ở chương

3, chúng ta sẽ bắt đầu bằng cách sử dụng một thuật toán mạng phi thần kinh rất đơn giản và chúng ta sẽ thay thế nó bằng

một mạng lưới thần kinh ở cuối chương. Hình 1.9. Dữ liệu đầu vào là trạng thái

của môi trường tại một thời điểm nào đó, được đưa vào tác nhân, được thực hiện dưới dạng sâu

mạng lưới thần kinh trong cuốn sách này, sau đó đánh giá dữ liệu đó để thực hiện hành động. các

quá trình này phức tạp hơn một chút so với trình bày ở đây, nhưng điều này nắm bắt được bản chất.

Mục tiêu duy nhất của đại lý là tối đa hóa phần thưởng mong đợi trong dài hạn. Nó

chỉ lặp lại chu trình này – xử lý thông tin trạng thái, quyết định hành động cần thực hiện, xem

nếu nó nhận được phần thưởng, hãy quan sát trạng thái mới, thực hiện một hành động khác, v.v. Nếu chúng ta đặt

tất cả những điều này được thực hiện một cách chính xác, tác nhân cuối cùng sẽ học cách hiểu môi trường của nó và thực hiện

những quyết định đúng đắn và đáng tin cậy ở mọi bước. Cơ chế chung này có thể được áp dụng cho việc tự động

phương tiện giao thông, chatbot, robot, giao dịch chứng khoán tự động, chăm sóc sức khỏe và nhiều hơn thế nữa. chúng tôi sẽ

khám phá một số ứng dụng này trong phần tiếp theo và xuyên suốt cuốn sách này.

Phần lớn thời gian của bạn trong cuốn sách này sẽ được dùng để học cách cấu trúc các vấn đề trong

mô hình chuẩn và cách triển khai các thuật toán học tập (tác nhân) đủ mạnh để giải quyết

những vấn đề khó khăn. Đối với những ví dụ này, bạn sẽ không cần xây dựng môi trường. Bạn sẽ

đang cắm vào các môi trường hiện có, chẳng hạn như công cụ trò chơi hoặc các API khác. Ví dụ,

OpenAI đã phát hành thư viện đá quý Python cung cấp cho chúng ta một số môi trường

và một giao diện đơn giản để thuật toán học tập của chúng tôi tương tác. Mã trên

bên trái của Hình 1.10 cho thấy việc thiết lập và sử dụng một trong những môi trường này đơn giản như thế nào.

Một trò chơi đua xe chỉ cần năm dòng mã.

Xem mã này. Hình 1.10. Thư viện OpenAI Python đi kèm với nhiều môi trường và

giao diện dễ sử dụng để thuật toán học tập tương tác. Chỉ với vài dòng

mã chúng tôi đã tải lên một trò chơi đua xe.