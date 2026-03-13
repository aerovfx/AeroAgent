# 3 -Bối rối dịch thuật

---

Video này và video tiếp theo tập trung vào thước đo định lượng về hiệu suất của mô hình được gọi là độ bối rối.

Trong video này, tôi sẽ giải thích cách diễn giải thước đo này và cách tính toán nó.

Và sau đó, trong thử thách viết mã ở video tiếp theo, bạn sẽ khám phá sự bối rối theo nhiều cách khác nhau.

tập dữ liệu, các mô hình khác nhau và sử dụng các tham số phân tích khác nhau.

Tôi sẽ bắt đầu bằng cách cung cấp cho bạn một số trực giác về việc giải thích điểm số bối rối và sau đó

chúng ta sẽ chuyển sang phần toán.

Tôi sẽ sử dụng biểu đồ này để đưa ra hiểu biết mang tính khái niệm về sự bối rối.

Ở đây chúng ta có các ô dạng thanh được nhóm thành năm tình huống.

Vì vậy, tình huống 0, 1, 2 và lên đến 4.

Vì vậy, hãy tưởng tượng rằng chúng ta có một mô hình ngôn ngữ nhỏ có bốn mã thông báo và mục tiêu của

mô hình là dự đoán mã thông báo tiếp theo.

Vì vậy, trục y ở đây tương ứng với nhật ký đầu ra của tất cả các mã thông báo và trong mỗi mã thông báo.

trong những tình huống này, mã thông báo cuối cùng là mã thông báo mục tiêu.

Vì vậy, đó là câu trả lời chính xác mà mô hình nên đưa ra.

Được rồi, điểm bối rối được ghi ở phía dưới đây.

Bây giờ tình huống này ở đây minh họa cho hiệu suất của mô hình lý tưởng.

Mô hình này mang lại mức độ kích hoạt thực sự cao cho mã thông báo mục tiêu và mức độ kích hoạt thấp cho mã thông báo mục tiêu.

các token khác.

Và sự bối rối ở đây là 1.

Bây giờ tình huống này thật thú vị vì mô hình vẫn có logit cao nhất cho

mục tiêu.

Nếu chúng ta coi việc lựa chọn mục tiêu là người chiến thắng trong tất cả các kịch bản, thì tình huống 1 giống hệt nhau

đến tình huống 0.

Mô hình vẫn sẽ chọn đúng mã thông báo mục tiêu.

Tuy nhiên, rõ ràng người mẫu kém tự tin hơn rất nhiều về lựa chọn của mình vì khoảng cách

giữa mục tiêu và phi mục tiêu nhỏ hơn nhiều.

Và bây giờ độ phức tạp là 2.1.

Bây giờ trong tình huống 2, chúng ta thấy rằng mô hình thực sự không thực sự thích mục tiêu trong

cảm thấy rằng có một tùy chọn không phải mục tiêu có cùng nhật ký đầu ra.

Vì vậy, bản thân mô hình này không thực sự sai, nhưng nó cũng không thực sự đúng hoàn toàn.

Và ở đây độ bối rối cao hơn một chút ở mức 2,7.

Bây giờ mục tiêu ở đây có mức độ kích hoạt cao hơn một số mục tiêu không phải mục tiêu, nhưng mục tiêu không phải mục tiêu này

có logit cao nhất.

Vì vậy, mô hình này chắc chắn là sai về mặt phân loại, nhưng nó vẫn có thể tạo ra một số loại

về một dự đoán đúng đắn về mục tiêu chính xác.

Và ở đây độ phức tạp là 4,4.

Được rồi, và đây chính là tình huống tệ nhất ở đây.

Mô hình này rất tự tin trong việc lựa chọn một mục tiêu không phải mục tiêu và bản thân mục tiêu đó không có

kích hoạt lớn hơn các mục tiêu không phải khác này.

Và bây giờ sự bối rối gần như cao hơn gần 3.000 lần so với bất kỳ điều nào khác trong số này

tình huống.

Được rồi, vậy chúng ta có thể suy ra điều gì về sự bối rối dựa trên hình minh họa này?

Đối với một điều, số lượng nhỏ hơn là tốt hơn.

Bạn muốn sự bối rối ở mức thấp, gần bằng không.

Thứ hai, điểm số không chỉ phản ánh độ chính xác về mặt phân loại mà còn phản ánh điều gì đó

về khoảng cách giữa mã thông báo mục tiêu và mã không phải mục tiêu, ngay cả khi mô hình không

chọn đúng mục tiêu.

Vì vậy, nó giống như một thước đo độ chính xác liên tục.

Đặc điểm bối rối của chúng tôi, điều này thực sự không rõ ràng trong ví dụ đồ chơi này, nhưng nó

nói chung là đúng, sự bối rối của một mã thông báo đó thực sự gây ồn ào.

Nó không mang tính biểu thị lắm.

Nó rất không đáng tin cậy.

Và điều đó cũng có ý nghĩa về mặt trực giác.

Một số mã thông báo tiếp theo rất dễ dự đoán, trong khi các mã thông báo khác, như phần đầu câu,

khó dự đoán hơn nhiều.

Do đó, trong thực tế, bạn tính toán mức độ phức tạp trung bình trên nhiều mã thông báo, giống như một con số khổng lồ.

số lượng token.

Trong các đánh giá thực tế, họ tính mức độ bối rối trung bình trên tất cả các mã thông báo trong tập huấn luyện.

Trong bản demo Python ở đây và cả trong thử thách viết mã ở video tiếp theo, tôi cũng sẽ

hiển thị mức độ phức tạp trung bình trên các chuỗi nhỏ hơn để giúp bạn hiểu được mức độ biến đổi.

Cuối cùng, cách giải thích sự bối rối đó là thước đo mức độ dự đoán của mô hình

mã thông báo cũng như mức độ phân biệt mục tiêu với mã thông báo không phải mục tiêu.

Và phần giải thích sau đó là sự khác biệt giữa tình huống màu xanh lam

ở đây và tình huống màu cam ở đây.

Vì vậy, sự bối rối là một thước đo đa diện và liên tục để dự đoán mã thông báo và phân tách mã thông báo.

Được rồi, đó là cách giải thích.

Bây giờ tôi sẽ chỉ ra phép toán.

Đây là phương trình cho sự bối rối.

Mình viết ở đây là p đôi khi người ta cũng viết ra ppl.

Vì vậy n đây là số lượng token đang được xem xét.

Như tôi đã nói ở slide trước, đó thường là số lượng mã thông báo trong toàn bộ tập dữ liệu,

mặc dù bạn cũng có thể tính toán nó cho một tập hợp con nhỏ hơn.

L là tổn thất của token i.

Vì vậy, khoản lỗ được tính cho mỗi mã thông báo, sau đó tính tổng và chia cho số lượng mã thông báo,

có nghĩa là tổn thất trung bình trên tất cả các mã thông báo.

Và sau đó bạn lấy số mũ tự nhiên của điều đó.

Bây giờ bạn muốn đảm bảo tính trung bình trước rồi tính lũy thừa chứ không phải tính trung bình theo cấp số nhân

của những tổn thất riêng lẻ.

Đó là vì lý do ổn định về số lượng.

Một lần nữa, ý tưởng là việc mất một mã thông báo thực sự rất ồn ào và không mang tính đại diện.

Vì vậy trước tiên bạn lấy trung bình cộng của chúng và sau đó bạn lấy e về mức trung bình đó.

Bây giờ vì hàm mất mát là entropy chéo nên chúng ta có thể viết lại phương trình này bằng cách sử dụng hàm thực

chức năng mất mát, trông như thế này.

Vì vậy y hat là dự đoán softmax của mã thông báo mục tiêu.

Vì vậy, mã thông báo chính xác mà mô hình nên chọn.

Và đó chính là ý tôi với dấu hoa thị ở đây, ngôi sao ở chỉ số trên.

Vì vậy, trên mã thông báo i trong chuỗi, xác suất softmax của mã thông báo mục tiêu và sau đó trừ đi

nhật ký tự nhiên của điều đó.

Và ở đây chúng ta có một cách khác để viết phương trình đó.

Vì vậy, đây là xác suất chọn mã thông báo mục tiêu dựa trên tất cả các mã thông báo trước đó.

Và đây là những gì softmax làm.

Được rồi, hãy xem tổng quan nhanh về những gì tôi sẽ trình bày trong bản demo mã Python.

Thực ra tôi sẽ bắt đầu bằng cách cho bạn xem đoạn mã tạo ra ví dụ về đồ chơi đó với

các biểu đồ thanh mà tôi đã trình chiếu ở một vài slide trước đây.

Sau đó, tôi sẽ nhập mô hình GPT2 và cả tập dữ liệu văn bản wiki.

Tôi sẽ tính toán độ phức tạp ở một số đoạn văn bản ngẫu nhiên.

Và bạn có thể thấy rằng các phân đoạn nhỏ có độ phức tạp khá khác nhau, mặc dù

trung bình trên tập dữ liệu là khoảng 30.

Vì vậy, đây là cho các đợt ngẫu nhiên.

Tiếp theo tôi sẽ tính toán độ phức tạp theo thứ tự.

Vì vậy, thời gian thay đổi các phân đoạn trong văn bản.

Và bạn có thể thấy rằng dường như có một sự tự tương quan nào đó trong đó, có nghĩa là

một số mẫu dữ liệu tuần tự dễ dự đoán hơn trong khi những mẫu khác khó dự đoán hơn.

Được rồi, vậy chúng ta hãy xem xét Python.

Và sau phần demo mã hóa, tôi sẽ nói vài lời về một số hạn chế của

sự bối rối.

Tôi đã chạy dòng mã này và khởi động lại phiên của mình.

Vì vậy, bây giờ tôi đã sẵn sàng nhập các thư viện này.

Ở đây tôi đang nhập mô hình GPT2 và mã thông báo.

Chúng tôi không đào tạo nên chúng tôi có thể chuyển mô hình sang chế độ đánh giá.

Đây là nơi tôi nhập tập dữ liệu văn bản wiki.

Và chỉ để cho bạn một ví dụ về một trong những món đồ này trông như thế nào.

Vì vậy, ví dụ này đọc Bacon cho biết cơ hội xảy ra nhiều hơn đáng kể.

Tôi nghĩ dù sao thì điều này cũng có thể ám chỉ Kevin Bacon, tôi không chắc lắm.

Nhưng bạn có thể thấy đó chỉ là một số văn bản.

Không sao đâu.

Nó cứ tiếp tục như vậy.

Được rồi, vậy hãy xem nào.

Đây là bản demo mà tôi đã trình chiếu trong các slide.

Vì vậy, tôi có những tình huống này.

Bạn có thể tưởng tượng rằng những thứ này tương ứng với nhật ký của bốn đầu ra mã thông báo.

Vì vậy, giả sử chúng ta có một mô hình ngôn ngữ nhỏ chỉ có bốn mã thông báo và đây sẽ là

nhật ký đầu ra.

Trong tất cả các trường hợp này, tôi đang mô phỏng mã thông báo mục tiêu mà mô hình thực sự cần

được ưu tiên là mã thông báo thứ tư, mã thông báo cuối cùng.

Được rồi, đó là những gì tôi nói ở đây.

Vì vậy, danh mục mục tiêu hoặc chỉ số mã thông báo tất nhiên là ba, bắt đầu từ, bắt đầu đếm

ở mức không.

Vì vậy, bên trong vòng lặp for này trong các tình huống khác nhau, trước tiên tôi chuyển đổi nó thành PyTorch

tensor.

Ở đây, tôi đang chuyển đổi sang softmax và sau đó lấy nhật ký.

Vì vậy, đây là mô phỏng chuyển đổi sang xác suất và lấy xác suất log và sau đó

việc mất mã thông báo cụ thể này trong trường hợp cụ thể này sẽ là softmax của nhật ký mô hình

cho mã thông báo mục tiêu.

Và đó là những gì bạn thấy ở đây.

Và sau đó chúng tôi chỉ nói, vâng, với điều đó.

Và điều đó khiến chúng ta bối rối.

Bây giờ vì đây là dữ liệu mô phỏng nên chúng tôi thực sự có thể tính toán mức độ phức tạp của một mã thông báo.

Đó không phải là điều bạn thường làm trong văn bản, nhưng đó là điều tuyệt vời về

dữ liệu mô phỏng.

Bạn thực sự có thể chỉ làm việc với các điểm dữ liệu riêng lẻ.

Được rồi, vậy hãy xem nào.

Vâng, ở đây tôi chỉ in ra tất cả dữ liệu ở đây và sau đó hiển thị dữ liệu này trong một biểu đồ.

Nếu bạn muốn, tò mò điều tôi khuyến khích bạn làm là bắt đầu chơi đùa với những thứ này

những con số.

Bạn có thể thay đổi một số con số này và xem nó ảnh hưởng như thế nào đến sự bối rối và về cơ bản

chỉ cần cố gắng đạt được một số trực giác về mối quan hệ giữa độ cao tương đối của

các thanh khác nhau này và liệu độ phức tạp nhỏ hơn, gần bằng 0 hay lớn hơn nhiều.

Được rồi.

Bây giờ chúng ta hãy bắt đầu, hãy làm một số ví dụ thực tế.

Ở đây tôi có một lô bốn, vì vậy kích thước lô bốn chuỗi có độ dài một nghìn hai mươi

bốn.

Sau đó, tôi nhận được một loạt dữ liệu ngẫu nhiên và chuyển nó qua GPT 2 và tôi đã gán nhãn

bằng X. Bạn đã từng thấy điều này trước đây.

Và điều đó có nghĩa là mất chấm đầu ra là mất cho lô này.

Vì vậy, bây giờ chúng ta có thể đơn giản lấy số mũ tự nhiên của sự mất mát đó và đó là điều khó hiểu đối với

lô dữ liệu này.

Bây giờ cần phải rõ ràng, đây không phải là chỉ số ngẫu nhiên.

Điều này thực sự đến từ dữ liệu thực từ dữ liệu WikiTax.

Tôi chỉ gọi nó là ngẫu nhiên vì tôi chỉ lấy mẫu ngẫu nhiên từ một nơi nào đó trong toàn bộ

tập dữ liệu.

Được rồi, vậy chúng ta có độ phức tạp khoảng ba mươi.

Một lần nữa, đây không phải là một con số siêu đáng tin cậy vì đây chỉ là một phép tính

từ một mẫu ngẫu nhiên.

Được rồi, điều tôi sắp làm ở đây là tính độ phức tạp.

Trên thực tế, bạn biết điều gì sẽ thú vị để làm.

Bạn chỉ có thể tiếp tục chạy lại mã này.

Tất cả các mã đều giống hệt nhau.

Kích thước lô, độ dài chuỗi, tất cả đều giống nhau.

Tất cả những gì tôi đang làm là nhận được các mã thông báo ngẫu nhiên khác nhau.

Vậy là đã ba mươi rồi.

Bây giờ đã hai mươi.

Bây giờ là ba mươi lăm hai mươi bảy.

Vì vậy, bạn có thể thấy rằng cũng có một số thay đổi, bạn biết đấy, không phải là chúng ta đang nhận được

giá trị điểm một và một trăm triệu.

Vì vậy, bạn biết đấy, với nó, sẽ có một số, một số cửa sổ trong đó người ta sẽ quan sát thấy sự bối rối

cho một mô hình nhất định và một đoạn văn bản nhất định.

Được rồi, trên thực tế, những gì tôi làm về cơ bản là một phương pháp nghiêm ngặt hơn một chút về những gì tôi

vừa làm ở đây bằng cách chạy đi chạy lại mã này.

Vì vậy, tôi sẽ lặp lại tất cả những điều này chỉ với 300 mẫu ngẫu nhiên.

Và sau đó tôi tính giá trị trung bình của tất cả các khoản lỗ và lấy giá trị tự nhiên

hàm mũ của những tổn thất trung bình đó.

Lưu ý sự khác biệt giữa mã này và mã này ở đây.

Vậy ở đây tôi đang nói đến sự mất mát ngay lập tức.

Và điều tôi đang làm ở đây là tính tất cả các khoản lỗ riêng lẻ và tính trung bình chúng

cùng nhau và sau đó tận dụng điều đó.

Bây giờ điều này chỉ hoạt động ở mức trung bình trên tất cả những điều này bởi vì mỗi đợt này có chính xác

độ dài chuỗi dài.

Nếu bạn bị tổn thất ở các độ dài chuỗi khác nhau, nếu một số chuỗi ngắn hơn và các chuỗi khác

trình tự dài hơn, thì bạn sẽ cần thêm một chút mã bổ sung vào

hãy chắc chắn rằng bạn đang chia cái này.

Vì vậy, bạn có thể chia từng mục cho độ dài chuỗi và khi đó đây sẽ là tổng như sau

cái này.

Vì vậy, bạn muốn tính trung bình của tất cả các mã thông báo và ở đây chúng tôi có thể đơn giản hóa việc tính trung bình của mã thông báo

một chút vì mỗi đợt ở đây đều có số lượng token giống nhau.

Được rồi.

Và sau đó chúng ta có thể vẽ đồ thị tất cả những điều đó và chúng ta thấy rằng đây là những gì tôi đã trình bày trên các slide.

Vì vậy, có khá nhiều hệ số biến thiên của 2 nhiều hơn hệ số của 2 một chút

từ sự bối rối nhỏ nhất đến sự bối rối lớn nhất.

Một lần nữa, điều đó thực sự chỉ là do tính biến thiên của việc lấy mẫu và độ phức tạp nội tại và

sự ồn ào của ngôn ngữ viết tự nhiên của con người.

Được rồi.

Vì vậy, bây giờ điều tôi đang làm là tính toán độ phức tạp trên các phân đoạn không chồng chéo.

Khái niệm tương tự là tôi lấy các phân đoạn dữ liệu và sau đó chạy chúng trong mô hình

bị lỗ và ở đây tôi đang tính toán mức độ phức tạp thực tế của từng phân khúc riêng lẻ

và sau đó chuyển sang phân đoạn tiếp theo.

Vì vậy, đi từ phân đoạn này sang phân đoạn khác trong văn bản.

Được rồi.

Vì vậy, chúng ta thấy điều đó tạo ra hình mà tôi đã trình bày trên slide cũng như nơi chúng ta thấy

rằng khi chúng ta xem qua văn bản, có một số đoạn có vẻ như

ngẫu nhiên và sau đó cũng có một số đoạn văn bản mà sự bối rối có vẻ tương đối

ở mức thấp liên tục trong một thời gian và các giai đoạn khác mà sự bối rối dường như liên tục

cao.

Bây giờ điều đó có nghĩa là gì?

Về cơ bản, điều này có nghĩa là có một số phần nhất định của văn bản mà mô hình đang gặp phải.

một thời gian dễ dàng hơn.

Mô hình dự đoán chính xác hơn mã thông báo tiếp theo có thể do ngôn ngữ trong

những phân đoạn này đơn giản hơn một chút và ở đây mô hình gặp khó khăn hơn trong việc dự đoán

các mã thông báo tiếp theo trong chuỗi có lẽ vì có nhiều loại văn bản hỗn hợp.

Ví dụ: có thể có rất nhiều tài liệu tham khảo ở đây nên rất khó dự đoán

vì chúng có định dạng khác.

Tất nhiên, nếu bạn tò mò, bạn có thể đi tìm những phân khúc có giá tương đối thấp

độ phức tạp và các phân đoạn có độ phức tạp tương đối cao và chỉ cần nhìn vào văn bản và

xem liệu bạn có thể hiểu được điều đó không.

Nhưng điều đó nằm ngoài phạm vi những gì tôi đang làm trong bản demo mã này.

Sự bối rối là một thước đo tuyệt vời và nó thường được sử dụng để so sánh các mô hình khác nhau nhưng không phải vậy.

hoàn hảo, không có gì là hoàn hảo và có một số lưu ý cần lưu ý khi sử dụng sự bối rối như một

cách đánh giá và so sánh các mô hình.

Có một điều là độ phức tạp thực sự rất khác nhau nên để có được một kết quả đáng tin cậy và ổn định về mặt thống kê

ước tính bạn thực sự muốn tính trung bình trên một tấn dữ liệu.

Bạn đã thấy điều đó một chút trong video này và bạn sẽ thực sự thấy nó có thể thay đổi như thế nào

thử thách mã trong video tiếp theo.

Thứ hai, độ phức tạp có thể được dự kiến sẽ thấp hơn trên văn bản mà mô hình đã đào tạo

trên hoặc đã được tinh chỉnh và các mô hình hiện đại rất lớn đã được đào tạo về cơ bản

toàn bộ internet.

Vì vậy, điểm này cũng có nghĩa là nếu bạn tinh chỉnh một mô hình thì độ phức tạp sẽ thấp hơn

tập tinh chỉnh thì nó sẽ nằm trên dữ liệu được huấn luyện trước.

Bây giờ đó không hẳn là một điều xấu nhưng đó là điều cần lưu ý.

Ví dụ: nếu bạn đang so sánh hai mô hình được đào tạo trên các tập dữ liệu khác nhau,

nếu điểm bối rối được đo bằng cách sử dụng một số dữ liệu mà một mô hình đã được đào tạo thì

điều đó có thể gây nhầm lẫn cho việc giải thích sự bối rối tương đối.

Có lẽ hạn chế quan trọng nhất ở đây là sự bối rối không trực tiếp chuyển tải

để mô hình hóa khả năng hoặc giá trị ứng dụng.

Sự bối rối phản ánh mức độ một mô hình có thể dự đoán mã thông báo tiếp theo nhưng đó không phải lúc nào cũng là điều

chúng tôi muốn.

Chúng tôi không muốn trò chuyện GPT lấy lại chính xác một cách hoàn hảo bất cứ điều gì nó đã được đào tạo.

Mặc dù đó là điều nên làm nếu tất cả những gì chúng ta quan tâm là đạt được mức thấp nhất có thể

sự bối rối.

Vì vậy, điểm bối rối thấp hơn là tốt nhưng đó không phải là trường hợp mà mức độ bối rối nên

ở mức tối thiểu, đặc biệt đối với một mô hình tổng quát.

Và cuối cùng, về cơ bản đây là những gì tôi đã nói trước đây.

Trang bị quá mức dẫn đến độ phức tạp thấp hơn mặc dù trang bị quá mức thường không phải là một điều tốt.

Tôi hy vọng tôi không tỏ ra quá tiêu cực về sự bối rối.

Đây là thước đo rất tốt và ngắn gọn về hiệu suất của mô hình và cũng là một thước đo khá chuẩn

cách để so sánh hiệu suất giữa các mô hình.

Trong video tiếp theo, bạn sẽ khám phá sự bối rối chi tiết hơn.