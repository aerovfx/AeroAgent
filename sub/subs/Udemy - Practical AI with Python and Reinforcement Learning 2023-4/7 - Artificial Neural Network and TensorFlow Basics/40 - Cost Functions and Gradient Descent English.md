# 40 - Hàm chi phí và Độ dốc giảm dần bằng tiếng Anh

---

Chào mừng mọi người trở lại và bài giảng này chúng ta sẽ nói về các hàm chi phí,

sẽ cho phép chúng ta đo lường mức độ sai lệch của chúng ta trong các dự đoán đầu ra của mạng lưới thần kinh.

Và sau đó chúng ta sẽ nói về việc giảm độ dốc, điều này sẽ giúp chúng ta giảm thiểu chi phí hoặc giảm thiểu

lỗi đó thường xảy ra do hàm chi phí.

Bạn cũng có thể nghe thấy chúng được gọi là hàm mất mát hoặc hàm không khí.

Vì vậy, chúng ta sẽ nói về tất cả chủ đề thực sự thú vị ở đây.

Và về cơ bản nó sẽ giúp chúng ta hiểu rõ hơn về cách mạng lưới thần kinh thực sự sẽ

học hỏi.

Vì vậy, chúng ta đã hiểu rằng mạng lưới thần kinh nhận đầu vào ở lớp đầu tiên đó, sau đó chúng

nhân chúng với trọng số rồi cộng độ lệch với chúng, và sau đó có thể điều đó được chuyển qua một

hàm kích hoạt như hàm sigmoid hoặc đơn vị tuyến tính được chỉnh lưu.

Và sau đó nó sẽ đi vào một lớp khác, sau đó là một tập hợp trọng số và độ lệch khác, v.v.

vân vân, vân vân, cho đến lớp đầu ra cuối cùng.

Vì vậy, lớp đầu ra cuối cùng đó, chúng ta có thể gọi nó hoặc gọi nó là mũ trắng.

Về cơ bản, đó là ước tính của mô hình về những gì nó dự đoán nhãn.

Vì vậy, chúng tôi có hai câu hỏi chính sau khi mạng tạo ra dự đoán đó, đó là làm cách nào để chúng tôi thực sự đánh giá

nó chống lại nhãn thực sự?

Và sau khi đánh giá, làm cách nào chúng tôi có thể cập nhật mạng lưới, trọng số và độ lệch?

Vì vậy, thực sự điều chúng ta sẽ tập trung vào bài giảng này là làm thế nào để đánh giá mức độ sai lệch của dự đoán của chúng ta

là để cập nhật mạng, trọng số và độ lệch?

Chúng ta sẽ phải tìm hiểu về sự lan truyền ngược, điều này sẽ được trình bày trong bài giảng sau.

Vì vậy, ngay bây giờ, hãy tập trung vào câu hỏi đầu tiên.

Vì vậy, điều chúng ta cần làm là lấy kết quả đầu ra ước tính của mạng và sau đó so sánh chúng

với các giá trị thực của nhãn và hãy nhớ rằng điều tôi đang đề cập đến hiện nay đang diễn ra trong

phần đào tạo hoặc phần phù hợp của quá trình học có giám sát.

Vì vậy, hiện tại, điều chúng tôi đang làm là chỉ sử dụng tập dữ liệu huấn luyện.

Bằng cách đó, chúng tôi có thể quay lại và cập nhật trọng số và thành kiến của mình trong quá trình kiểm tra mà chúng tôi không thực sự cập nhật

trọng số và độ lệch.

Thay vào đó, chúng tôi lại đánh giá tổng thể trên toàn bộ tập dữ liệu.

Mạng lưới thần kinh của chúng ta hoạt động như thế nào?

Hiện tại, chúng tôi đang thực hiện những đánh giá nhỏ về các trận đấu tập này để thực sự tiến hành

quay lại và cập nhật trọng số và độ lệch trong mạng của chúng tôi.

Vì vậy, hãy ghi nhớ điều đó.

Được rồi, để thực sự so sánh kết quả đầu ra của mạng nơ-ron với giá trị thực, chúng ta sẽ

bằng cách sử dụng cái được gọi là hàm chi phí.

Và điều này cũng thường được gọi là hàm bị mất hoặc hàm lỗi.

Về cơ bản, nó chỉ là thứ đo lường mức độ bạn cách xa giá trị thực dựa trên

dự đoán.

Và một lưu ý quan trọng là chúng ta phải lấy giá trị trung bình để xuất ra một giá trị duy nhất.

Sau đó, bạn có thể theo dõi tổn thất hoặc chi phí đó trong quá trình đào tạo để theo dõi hiệu suất mạng.

Vì vậy, hy vọng rằng trong mỗi giai đoạn đào tạo, sự mất mát hoặc chi phí của bạn sẽ giảm đi, giảm xuống.

Cho đến khi bạn hội tụ về một giá trị chi phí tối thiểu nào đó.

Vì vậy điều chúng ta có thể làm ở đây là tôi muốn giới thiệu một vài biến mà chúng ta sẽ sử dụng Y để biểu diễn

giá trị thực và sau đó chúng ta sẽ sử dụng A để thể hiện dự đoán nơ-ron.

Vì vậy, xét về trọng số và độ lệch, điều chúng ta có ở đây là nhớ lại rằng chúng ta đặt Z là đại diện cho trọng số

nhân X cộng với B, sau đó chúng ta chuyển Z đó vào một hàm kích hoạt chẳng hạn như hàm sigmoid sao cho

Z đi vào sigmoid thì bằng a.

Vì vậy, tất cả những gì tôi đang cố gắng nói ở đây là a đại diện cho loại đầu ra cuối cùng của một nơ-ron lấy

tính đến chức năng kích hoạt là gì.

Và điều đó cũng tính đến Z, từ đó tính đến W, là các trọng số

và của Bias.

Vì vậy, chỉ cần ghi nhớ điều đó sẽ chứa rất nhiều thông tin.

Nó chứa thông tin về hàm kích hoạt, trọng số và độ lệch.

Vì vậy, có lẽ hàm chi phí phổ biến nhất mà bạn thấy được gọi là hàm chi phí bậc hai, và nếu

bạn đã từng học máy, điều này có thể thực sự quen thuộc với bạn vì nó trông giống như

lỗi bình phương trung bình gốc, về cơ bản nó giống như ở đây.

Nó chỉ không được ký hiệu cho dữ liệu đa chiều.

Vì vậy tất cả những gì chúng ta đang làm ở đây là ngày nọ chúng ta sẽ tính sự khác biệt giữa các giá trị thực

ở đây, chúng tôi gắn nhãn nó bằng X. Vì vậy, nếu bạn có một số thông tin đầu vào, chúng tôi sẽ chỉ định đâu là hàm đúng.

Vì vậy, đó sẽ là giá trị thực sự.

Và sau đó chúng tôi trừ đi các giá trị dự đoán của mình.

Vì vậy, ở đây chúng ta có mức X, và hãy nhớ rằng A trên L, ký hiệu đó chỉ biểu thị rằng

là đầu ra hàm kích hoạt của lớp L trong đó L là lớp cuối cùng của bạn, nghĩa là lớp

trước đó trong mạng là L trừ một, lớp trước đó là L trừ hai, v.v.

Sau này, chúng ta sẽ hiểu tại sao việc đặt Marquel làm lớp cuối cùng lại thuận tiện hơn và sau đó thực hiện ngược lại

từ đó thay vì bắt đầu lại từ đầu.

Vì vậy, một lần nữa, mức X về cơ bản là sản lượng dự đoán của bạn.

Vì vậy, hãy nhớ rằng, ký hiệu được hiển thị lại ở đây tương ứng với các đầu vào và đầu ra vectơ, vì

chúng tôi thực sự đang phải đối mặt với một loạt điểm đào tạo và dự đoán trong quá trình thực hiện.

Nhưng ý chính là bạn phải xem như một hàm chi phí, bạn đang thực hiện một số cách tính trung bình.

Đó là lý do tại sao chúng ta có một trên hai lần.

Và N là số điểm ở đó và bạn lấy tổng của tất cả những khác biệt đó và bình phương

họ.

Vì vậy, câu hỏi thực sự được đặt ra là, tại sao chúng ta thực sự bình phương cái này và cái này thành những thứ hữu ích cho chúng ta?

Thứ nhất, nó giữ mọi thứ tích cực bởi vì bạn có không khí tích cực hoặc tiêu cực.

Nếu bạn bình phương, nó trở thành số dương, điều này tốt vì chúng ta muốn một số loại phép đo tuyệt đối

của lỗi.

Nếu chúng ta không bình phương số này và chúng ta có những giá trị âm và dương, khi bạn tính trung bình nó ra,

có thể dao động quanh số 0, đây thực sự không phải là dấu hiệu thực sự của giá trị tuyệt đối hoặc giá trị tuyệt đối

đơn vị đo khoảng cách của bạn.

Vì vậy, bình phương nó, đảm bảo rằng mọi thứ đều dương.

Điều khác và quan trọng hơn nhiều là nó sẽ trừng phạt những lỗi thực sự lớn.

Vì vậy, đôi khi bạn có một số điểm dữ liệu mà bạn sẽ thực sự không hài lòng và nếu bạn thực sự bình phương

lỗi đó, sau đó sẽ tăng theo cấp số nhân theo chi phí của bạn.

Vì vậy, có thể bạn bị thiếu 10 đô la và bất kỳ đơn vị nào bạn đang cố đo, nhưng chi phí của bạn đang tăng lên.

để báo cáo điều đó và bình phương đơn vị.

Vì vậy, nó sẽ nói rằng bạn bị giảm một trăm thay vì chỉ mười.

Vì vậy, bạn sẽ thực sự trừng phạt mạng của mình vì đã thực sự sai sót ở một số điểm nhất định, điều này là tốt

bởi vì bạn không muốn mạng của mình đột nhiên không thể dự đoán tốt dù chỉ một vài điểm

khi nó mang đến cho bạn một lỗi rất lớn, bạn thà chịu đựng một chút về tất cả các điểm khác chứ không phải

hoàn toàn tắt đối với một số loại trường hợp đặc biệt.

Vì vậy, điều đó thực sự giúp trừng phạt những lỗi lớn.

Bây giờ, nói chung, chúng ta có thể coi hàm chi phí là hàm của bốn thứ chính.

Vì vậy, hàm chi phí sẽ là hàm của W, tức là mạng lưới thần kinh của chúng ta có trọng số B,

là tất cả các thành kiến trong mạng thần kinh SFR của chúng tôi, là đầu vào của một mẫu đào tạo duy nhất và Ívar,

đó là đầu ra mong muốn của mẫu đào tạo đó.

Và điều đó rất có ý nghĩa vì chi phí phụ thuộc vào trọng số và độ lệch hiện tại.

Nó cũng phụ thuộc vào những gì bạn đã truyền vào làm ví dụ đào tạo thực tế.

Và điều đó cũng phụ thuộc vào thứ bạn đang so sánh với nó, đó là Ívar.

Vì vậy, hãy chú ý xem thông tin đó thực sự được mã hóa theo ký hiệu đơn giản mà chúng ta có như thế nào, vì vậy

Tôi đã chỉ cho bạn đây là hàm chi phí và bạn có thể thắc mắc, không phải bạn vừa nói rằng chi phí

hàm là hàm của WMP, trong khi đó WMP thuộc hàm bậc hai ở đây?

Chà, nó thực sự được mã hóa trong A của X vì hãy nhớ rằng, ảnh hưởng chứa thông tin về trọng số

và sai lệch vì X là Z được chuyển vào hàm kích hoạt trong đó Z chứa thông tin về

W và B.

Được rồi, điều này có nghĩa là nếu chúng ta có một mạng lưới lớn, chúng ta có thể mong đợi hàm chi phí thực tế sẽ thực sự

khá phức tạp với một vectơ lớn hoặc Tenzer trọng số và một Tenzer of Bias khổng lồ khác.

Vì vậy, ví dụ, nếu chúng ta chỉ lấy một mạng nhỏ và bắt đầu gắn nhãn cho mọi cách và mọi thành kiến

và mọi đầu ra đều là loại đầu ra của hàm kích hoạt, bạn có thể thấy tất cả các tham số

được dán nhãn ở đây, nó thực sự phức tạp, rất nhanh.

Và đây thực sự là một mạng lưới nhỏ.

Ở đây chỉ có loại có bốn lớp ẩn thôi.

Và những lớp ẩn đó thậm chí còn không hấp dẫn đến thế ở đây.

Nếu chúng ta bắt đầu ghi nhận mọi thứ, nó có thể trở nên khá phức tạp.

Bạn đã có một ma trận khá lớn về trọng số và độ lệch.

Vậy làm cách nào để chúng ta thực sự tính toán được điều này, làm cách nào để tính hàm chi phí đó và sau đó tìm ra cách

để giảm thiểu nó?

Vì vậy, trong trường hợp thực tế, điều này có nghĩa là chúng ta có một số hàm chi phí, xem nào, phụ thuộc vào nhiều trọng số,

hàm chi phí đó sẽ phụ thuộc vào trọng số của đầu vào đầu tiên và trọng số của trọng số thứ hai

ở cái thứ ba cho đến tận WFM.

Và chúng tôi cần tìm ra trọng số cụ thể nào giúp chúng tôi đạt được chi phí thấp nhất vì chúng tôi muốn

để quay lại đây và tìm ra tất cả các trọng số này, làm cách nào để thay đổi chúng để giảm thiểu hàm chi phí của tôi

vào cuối cùng.

Vì vậy, để đơn giản và chỉ nghĩ về điều này, hãy tưởng tượng rằng chúng ta đang giải quyết một vấn đề thực sự đơn giản

mạng chỉ có một trọng lượng duy nhất về cơ bản chỉ sau một năm.

Vì vậy, điều chúng tôi muốn làm là giảm thiểu tổn thất hoặc chi phí, về cơ bản là lỗi tổng thể của chúng tôi, mà

một lần nữa, điều đó có nghĩa là chúng ta cần tìm ra giá trị nào của W mà chúng ta sử dụng sẽ mang lại kết quả tối thiểu

của giá trị C.

Vì vậy, đây là biểu đồ của chúng tôi về hàm chi phí thực sự đơn giản, trong đó đây là một mạng thực sự đơn giản, nó chỉ

chứa một trọng số.

Vâng, điều chúng ta muốn làm là tìm ra giá trị nào của W tối thiểu hóa hàm chi phí này.

Và mặc dù đây là một ví dụ thực sự đơn giản nhưng bạn có thể chỉ cần nói điều đó để giảm thiểu

hàm chi phí ở đây, bạn có thể thấy rằng mức tối thiểu có thể rơi vào nơi có mũi tên đó.

Vì vậy, đó là trọng lượng sẽ giảm thiểu hàm chi phí đó, có nghĩa đó có thể là

trọng lượng mà chúng tôi muốn trong Neron thực tế hoặc đầu vào của Neron vì điều đó giúp giảm chi phí xuống mức tối thiểu.

Bây giờ, sinh viên tính toán biết điều chúng ta có thể làm là lấy đạo hàm của hàm chi phí này

và sau đó giải quyết bằng không.

Nhưng hãy nhớ lại, hàm chi phí thực của chúng ta sẽ cực kỳ phức tạp và nó sẽ không phải là một chiều,

hai chiều và ba chiều.

Nếu bạn nhìn lại mạng đó, nó sẽ có số chiều bằng W và đó là

thậm chí không phải là thứ tôi thực sự có thể âm mưu.

Vì vậy, một lần nữa, nó sẽ có n chiều, có nghĩa là lấy đạo hàm đó và đặt nó bằng

về 0 thực sự sẽ không bằng bạn sẽ không thể tính được số đó nếu không chi tiêu

của một nghìn năm thời gian tính toán.

Vì vậy, mạng của chúng tôi, đặc biệt là khi chúng tôi xây dựng các mạng thực sự lớn, sẽ có hàng nghìn

trọng số đến hàng trăm trọng số, chúng ta sẽ không lấy đạo hàm đó.

Vì vậy, thay vào đó, những gì chúng tôi làm là một quá trình ngẫu nhiên.

Vì vậy, điều chúng ta có thể làm là sử dụng phương pháp giảm độ dốc để giải quyết loại vấn đề này.

Vì vậy, hãy quay trở lại loại phiên bản đơn giản hóa này của mạng một lần nữa, chúng ta chỉ cần chờ một lần và

hãy xem cách giảm độ dốc sẽ hoạt động như thế nào trong ví dụ đơn giản này và sau đó chúng ta có thể dễ dàng mở rộng nó sang nhiều hơn

những ví dụ phức tạp.

Vì vậy, những gì chúng tôi làm là bắt đầu tại một điểm trên hàm chi phí này và một lần nữa, những gì chúng tôi đang tìm kiếm

vì đây là giá trị W tối thiểu hóa hàm chi phí này.

Vì vậy, điều chúng tôi làm là tính độ dốc tại một điểm và sau đó chúng tôi di chuyển theo hướng đi xuống của

độ dốc.

Và bạn tiếp tục lặp lại quá trình này cho đến khi cuối cùng bạn hội tụ về 0, biểu thị một

tối thiểu.

Vì vậy, điều chúng ta có thể làm là hãy nhớ rằng, chúng ta có thể thay đổi dấu bước để tìm điểm tiếp theo.

Vì vậy, ở đây chúng tôi đã lấy kích thước bước bằng nhau.

Và nếu bạn thực hiện các kích thước bước nhỏ hơn, sẽ mất nhiều thời gian hơn để tìm mức tối thiểu.

Nếu bạn thực hiện kích thước lớn hoặc bước, bạn sẽ đi nhanh hơn, nhưng điều xảy ra là bạn có nguy cơ vượt quá mức tối thiểu.

Vì vậy, nếu bạn sử dụng kích thước bước quá lớn, bạn thực sự có thể bỏ lỡ trọng lượng tối thiểu hoặc trọng lượng tối thiểu đó

cảm biến và sau đó vượt quá giới hạn và cuối cùng bạn không hội tụ.

Vì vậy, kích thước bước đó được gọi là tốc độ học tập.

Vì vậy, nếu bạn thấy mạng của mình đang chỉnh sửa tốc độ học, thì thực sự chúng là gì

việc làm ở đây là họ đang chỉnh sửa tốc độ họ sẽ cố gắng tìm giá trị trọng số tối thiểu đó.

Và nó cũng hoạt động tương tự với Bias's.

Bạn đang tìm thấy những trọng số tối thiểu đó, thực sự là những giá trị của trọng số và độ lệch giúp giảm thiểu điều đó

hàm chi phí.

Bây giờ, trong những ví dụ trước đó, điều bạn nên biết là tốc độ học tập không đổi.

Nghĩa là, kích thước mỗi bước đều bằng nhau.

Vì vậy, bất kể chúng ta đang thực sự xem xét cái nào, chẳng hạn như kích thước bước nhỏ hơn hoặc kích thước lớn hơn

kích thước bước, bước thực tế là bằng nhau cho tất cả các bước này.

Bây giờ chúng ta thực sự có thể thông minh hơn một chút và điều chỉnh kích thước bước của mình khi chúng ta tiếp tục, bạn có thể tưởng tượng rằng

vì bạn đang bắt đầu ở một vị trí ngẫu nhiên trong không gian chiều này và các trọng số có thể có

và thành kiến, nếu bạn bắt đầu với các bước lớn hơn, điều bạn có thể làm là sau đó bạn có thể đi ngày càng nhỏ hơn

trong kích thước bước của bạn khi độ dốc hoặc độ dốc đó tiến gần đến 0.

Và điều này được gọi là giảm độ dốc thích ứng.

Tùy thuộc vào độ dốc mà bạn quay lại, bạn sẽ điều chỉnh kích thước bước của mình.

Vì vậy, vào năm 2015, Kingma và Barr đã xuất bản bài báo của họ có tên Atem, một phương pháp tối ưu hóa ngẫu nhiên,

và Adam là cách hiệu quả hơn nhiều để tìm kiếm những mức tối thiểu này.

Vì vậy, bạn sẽ thấy chúng tôi đôi khi thực sự ở lại, Adam, với tư cách là người tối ưu hóa trong suốt quá trình viết mã.

Vì vậy, hãy ghi nhớ điều đó.

Nếu bạn từng gặp Adam, tất cả những gì chúng tôi thực sự đang đề cập đến là cách thực hiện chuyển màu được tối ưu hóa này

đi xuống nơi chúng tôi có loại kích thước bước thích ứng này.

Vì vậy, chúng tôi bắt đầu với quy mô lớn và sau đó tùy thuộc vào vị trí của chúng tôi, chúng tôi có thể ngày càng nhỏ hơn.

Vì vậy, bạn có được điều tốt nhất của cả hai thế giới.

Bạn có thể sử dụng kích thước bước lớn hơn và tăng tốc độ tìm mức tối thiểu đó.

Nhưng khi bạn càng ngày càng tiến gần đến nó và không muốn vượt quá giới hạn, bạn có thể bước một bước nhỏ hơn

kích thước.

Vì vậy, bạn thực sự có thể so sánh Adam với các thuật toán giảm độ dốc khác và ở đây nó hiển thị

cho bạn biết chi phí đào tạo so với số lần lặp lại trên toàn bộ tập dữ liệu.

Và bạn có thể thấy Adam ở đây đang hoạt động tốt hơn các thuật toán giảm độ dốc thích ứng khác này.

Vì vậy, tất cả những người được liệt kê ở đây không phải là Adam, thực ra họ cũng là những người giảm dần độ dốc thích ứng.

Tuy nhiên, Adam thể hiện tốt hơn tất cả những điều này.

Vì vậy, chúng ta sẽ sử dụng Adam vì việc sử dụng nó cho thần kinh là khá phổ biến.

mạng.

Vì vậy, nếu bạn thấy tất cả những gì chúng tôi đang làm ở đây là chúng tôi đang nói, được rồi, hãy tối ưu hóa cách chúng tôi tìm

mức tối thiểu này.

Bây giờ, trên thực tế, chúng tôi đang cho bạn xem minh họa về độ dốc giảm dần trên chỉ một chữ W,

vì vậy đó gần như là một chiều. Điều chúng tôi thực sự đang làm là tính toán độ dốc giảm dần

trong không gian n chiều cho tất cả trọng số của chúng tôi ở đây, bạn có thể thấy cách tính độ dốc giảm dần và hai

mặt phẳng chiều, bao gồm cả trọng số và độ lệch.

Trên thực tế, tôi thậm chí còn không thể minh họa được không gian các chiều bởi vì nó sẽ

là và kích thước của hàng chục hoặc hàng trăm trọng số và độ lệch.

Vì vậy, thực sự không có cách nào chúng tôi có thể minh họa điều đó cho bạn, đó là lý do tại sao chúng tôi đơn giản hóa nó thành loại

một trọng lượng duy nhất.

Bạn có thể hiểu việc giảm độ dốc đang làm gì và sau đó là những gì chúng ta thực sự đang làm hoặc những gì máy tính đang thực hiện.

sẽ thực hiện với chúng ta bằng cách thực hiện cùng một loại phép tính, nhưng trên không gian n chiều mà chúng ta

thực sự không thể minh họa thực tế cho bạn.

Vì vậy, khi xử lý các vectơ n chiều này, còn được gọi là Tensas, ký hiệu sẽ thay đổi

từ đạo hàm sang gradient.

Đó là lý do tại sao bạn đã nghe tôi nói đến gradient vài lần thay vì thuật ngữ đạo hàm.

Vì vậy, khi chúng ta xử lý N chiều, thay vì nói đạo hàm, điều đó thực sự đúng

thuật ngữ trở thành gradient.

Và điều đó có nghĩa là chúng ta tính toán độ dốc của hàm chi phí đối với tất cả các trọng số này.

Vì vậy, nếu bạn thấy điều đó cho đến hình tam giác hướng xuống đó, về cơ bản đó là cách bạn ghi chú độ dốc

thay vì chỉ nói đạo hàm.

Bây giờ, trước khi chúng ta kết thúc bài giảng này về hàm tổn thất hoặc chi phí và độ dốc giảm dần,

Tôi muốn đề cập nhanh rằng đối với các bài toán phân loại, thay vì sử dụng hàm chi phí bậc hai,

chúng tôi thường sử dụng hàm mất entropy chéo.

Và điều thú vị ở hàm mất entropy chéo này là về cơ bản nó có tác dụng như thế nào?

Nó giả định rằng mô hình của bạn dự đoán phân bố xác suất cho mỗi lớp.

Vì vậy, có thể nó có sự phân bổ từ lớp Một đến lớp ba, v.v.

Và cách thức thực hiện công thức này là dành cho phân loại nhị phân chỉ có hai lớp.

Bạn có kết quả là công thức hàng đầu và sau đó những nhật ký đó thực sự đại diện cho các nhật ký tự nhiên.

Và khi đó với số lớp nào lớn hơn bạn sử dụng công thức dưới đây thì bạn đừng lo lắng

quá nhiều về công thức này, vì về cơ bản khi chúng ta mã hóa nó, chúng ta sẽ chỉ định

sử dụng entropy chéo.

Vì vậy, khi chúng tôi thực hiện phân loại, đặc biệt là phân loại nhiều lớp, điều đó lớn hơn

chỉ là phân loại nhị phân, chúng ta sẽ coi entropy chéo là hàm chi phí của chúng ta.

Được rồi, vì vậy hãy ghi nhớ điều đó.

Nếu bạn từng thấy chúng tôi viết mã và chỉ định trên entropy thì đây là những công thức thực tế mà chúng tôi đang chỉ định

máy tính sử dụng để tìm ra phân bố xác suất cho mỗi lớp đó.

Vì vậy, để ôn lại nhanh, chúng ta đã nói về các hàm chi phí, chúng ta đã nói về việc giảm độ dốc, chúng ta đã nói về

về thực tế là có nhiều trình tối ưu hóa khác nhau như trình tối ưu hóa Adam và sau đó chúng tôi cũng đã nói về

chi phí bậc hai và entropy chéo.

Cho đến nay, chúng tôi hiểu rằng các mạng lấy đầu vào, ảnh hưởng đến đầu vào đó về trọng số và độ lệch cũng như kích hoạt

có chức năng tạo ra sản lượng ước tính.

Sau đó, chúng tôi đã học được cách đánh giá kết quả đầu ra đó so với nhãn thực sự?

Điều cuối cùng chúng ta cần làm và thảo luận lý thuyết là câu hỏi sau đây.

Một khi chúng ta thực sự nhận được chi phí hoặc giá trị bị mất đó, chúng ta sẽ hiểu mình còn cách xa đến mức nào.

Chúng ta vẫn chưa thực sự nói về cách chúng ta quay trở lại và điều chỉnh tất cả những trọng số và thành kiến vẫn còn đó.

loại điều kỳ diệu này.

Và điều kỳ diệu đó chỉ trong một giây nữa sẽ không còn quá kỳ diệu nữa.

Vì vậy, nó sẽ mang tính toán học và nó được gọi là lan truyền ngược.

Về cơ bản, bạn truyền ngược qua mạng của mình và sau đó cập nhật tất cả các trọng số và độ lệch đó.

Đó chính xác là những gì chúng ta sẽ đề cập trong bài giảng tiếp theo.

Tôi sẽ gặp bạn ở đó.