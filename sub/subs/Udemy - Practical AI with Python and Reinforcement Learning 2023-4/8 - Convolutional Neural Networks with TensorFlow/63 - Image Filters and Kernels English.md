# 63 - Bộ lọc hình ảnh và hạt nhân

---

Chào mừng mọi người trở lại với bài giảng về bộ lọc hình ảnh này.

Trước khi đi sâu hơn vào mạng nơ-ron tích chập, trước tiên chúng ta hãy thảo luận về một số ý tưởng chính trong máy tính.

tầm nhìn liên quan đến kiến trúc cách thức hoạt động của CNN.

Và hãy nhớ, thị giác máy tính chỉ là thuật ngữ chung để chỉ việc sử dụng các chương trình máy tính, quy trình,

hình ảnh, dữ liệu và các chủ đề như bộ lọc hình ảnh và Col's hình ảnh sẽ nằm trong tầm nhìn máy tính.

Vì vậy, chúng ta hãy cố gắng hiểu một số ý tưởng chính này và sau đó chúng ta sẽ xem chúng liên quan như thế nào với tích chập

mạng lưới thần kinh.

Giờ đây, nếu bạn đã từng sử dụng các phần mềm chỉnh sửa ảnh hay thậm chí là các ứng dụng chụp ảnh trên điện thoại thì chắc hẳn bạn đã từng

các bộ lọc đã thấy như bộ lọc mờ.

Nhưng câu hỏi đặt ra là những bộ lọc này thực sự hoạt động như thế nào?

Họ đang làm gì với các pixel bên dưới của hình ảnh để đạt được hiệu ứng mong muốn này?

Bộ lọc về cơ bản là một hạt nhân hình ảnh và hãy nhớ rằng thuật ngữ bộ lọc hình ảnh và hạt nhân hình ảnh

có thể được sử dụng thay thế cho nhau.

Vì vậy, bạn sẽ thấy một số người gọi nó là bộ lọc hình ảnh và những người khác gọi chúng là Col's hình ảnh.

Ý tưởng chính là nếu bạn đang đề cập đến hạt nhân hình ảnh, có thể bạn đang đề cập đến toán học hơn

hiểu đằng sau những gì bộ lọc hình ảnh đang làm.

Vậy hãy nói về điều đó.

Vậy hình ảnh đó, Col, là một ma trận nhỏ được áp dụng cho toàn bộ hình ảnh.

Hiện nay, một số bộ lọc phổ biến nhất định đã thực sự được nhiều người biết đến.

Ví dụ: để làm mờ một hình ảnh, bạn thực sự có thể chỉ cần sử dụng hạt nhân hình ảnh mà tôi đã trình bày ở đây.

Ma trận ba x ba này, khi áp dụng cho toàn bộ hình ảnh, sẽ thực sự làm mờ hình ảnh.

Vì vậy, hãy hiểu ý nghĩa của việc chúng tôi áp dụng cho toàn bộ hình ảnh.

Vì vậy, hãy khám phá ý nghĩa thực sự của việc áp dụng kernel hoặc bộ lọc cho hình ảnh.

Bộ lọc về cơ bản cho phép chúng ta chuyển đổi hình ảnh.

Vì vậy, ở đây chúng ta có một hình ảnh thang độ xám.

Đó thực sự là một hình ảnh nhỏ.

Và những gì chúng ta có, những giá trị của chúng ta được chia theo tỷ lệ từ âm một đến một trong đó một đại diện cho màu đen

và số âm đại diện cho màu trắng, và khi đó giá trị ngay giữa chúng, chẳng hạn như số 0, về cơ bản là

màu xám.

Vì vậy, chúng ta có những giá trị chuẩn hóa này giữa âm một và một.

Và điều tôi sắp làm là áp dụng bộ lọc cho hình ảnh này, vì vậy ở đây chúng ta có một ví dụ về

bộ lọc ba x ba.

Vì vậy, những gì chúng ta sẽ làm ở đây để áp dụng các bộ lọc cho hình ảnh sẽ bắt đầu từ trên cùng bên trái.

Tôi sẽ xem các giá trị cơ bản tương ứng với bộ lọc.

Vì vậy, về cơ bản, hãy đặt bộ lọc đó lên trên các pixel hình ảnh đó và sau đó chúng ta sẽ bắt đầu trượt nó

cùng.

Và khi chúng ta có bộ lọc ở trên cùng của hình ảnh, điều chúng ta làm là nhân các giá trị pixel đó với giá trị

bây giờ chúng ta sẽ gọi trọng số bộ lọc.

Vì vậy, các giá trị thực tế của bộ lọc, chúng ta sẽ bắt đầu coi chúng là trọng số vì sau này

trên mạng nơ ron tích chập sẽ chọn những trọng số đó cho chúng ta.

Nhưng chúng tôi đã xác định trước một số loại giá trị bộ lọc ở đây trong bộ lọc ba nhân ba này.

Vì vậy, chúng tôi lấy bộ lọc đó, đặt nó lên trên hình ảnh của mình và sau đó khi chúng tôi quét qua hình ảnh này,

chúng ta sẽ nhân với trọng số của bộ lọc.

Chúng tôi nhận được những kết quả đó và sau đó chúng tôi tổng hợp kết quả để có được một số giá trị đầu ra cuối cùng.

Vì vậy, trong trường hợp này, nếu chúng ta lấy bộ lọc 3 nhân 3 ở góc trên bên trái nhân với những bộ lọc đó

lọc các trọng số và sau đó là một số kết quả đó và để ý xem trong trường hợp này, độ phân giải sẽ thực sự như thế nào

giảm vì chúng ta đang lấy chín giá trị đầu vào và sau đó chỉ xuất ra một giá trị.

Bây giờ, như tôi đã đề cập, cuối cùng chúng ta sẽ thực hiện việc này trên toàn bộ hình ảnh, vì vậy về cơ bản chúng ta

Bây giờ chúng ta sẽ sải bước qua hình ảnh, thứ chúng ta có thể chỉnh sửa là khoảng cách sải chân của chúng ta.

Vì vậy, theo mặc định, chúng tôi phải vượt qua ít nhất một pixel.

Nhưng điều chúng ta có thể làm là có một khoảng cách thẳng lớn hơn.

Có lẽ chúng ta có thể bắt đầu lại với 2 pixel.

Và đó cũng là thứ chúng ta có thể chỉnh sửa trong mạng nơ-ron tích chập của mình.

Vì vậy, để hiểu rõ hơn về cách thực sự hoạt động của nó, có một ví dụ tương tác thực sự tuyệt vời

mà bây giờ tôi sẽ truy cập vào trình duyệt của mình và đây là URL của bạn Santoso.

Ôi, tha thứ cho hình ảnh gạch chéo phía trước của Col's.

Được rồi, hãy tiếp tục và đi tới phần này trong trình duyệt của chúng ta để chúng ta có thể biết được các bộ lọc hình ảnh này hoạt động như thế nào

thực sự được áp dụng và hình ảnh thu được trông như thế nào.

OK, vậy là chúng ta đang ở trạng thái của liên kết dành cho Image Col's và phần giải thích bắt đầu bằng cách hiển thị

bạn chỉ là một hình ảnh bình thường.

Vì vậy, hình ảnh thường có giá trị từ 0 đến 255 trong đó 0 là giá trị tối nhất có thể

giá trị và hai trăm năm mươi lăm là giá trị sáng nhất có thể.

Vì vậy, trong trường hợp ảnh thang độ xám, chúng ta có số 0 là màu đen và sau đó là hai năm mươi lăm là màu trắng.

Vì vậy, chúng ta có thể thấy ở đây khi chúng ta di chuột lên trên những giá trị này, chúng ta có thể thấy trong phần màu trắng này

mà tôi hiện đang di chuột qua, chúng tôi nhận được các giá trị khá gần với 255 và sau đó có thể

ở đây những gì tối hơn, có giá trị thấp hơn rất nhiều, khoảng 20.

Được rồi, đây là một loại hình ảnh có độ phân giải thấp được phóng to.

Nếu bạn nhìn qua phía bên phải này, bạn sẽ thấy bức ảnh nhỏ bé về đức tin của một khuôn mặt

xin lỗi.

Đó là loại kích thước thật của hình ảnh này.

Nó không bị thổi phồng lên ở quy mô lớn hơn thế này.

Nhưng điều tuyệt vời ở quy mô lớn này là bạn có thể nhìn thấy từng pixel rất rõ ràng.

Được rồi.

Vậy chúng ta có các số từ 0 đến 55.

Và chúng ta sẽ đi qua quá trình áp dụng kernel cho hình ảnh này.

Vì vậy, ở đây bạn thực sự có thể chọn loại đại tá nào bạn muốn ứng tuyển.

Chúng ta sẽ bắt đầu với đại tá mờ nhạt mà chúng ta đã đề cập trước đó.

Vậy đây là chín giá trị, một ma trận ba nhân ba hoặc ba nhân ba, thưa Đại tá, mà thực ra chúng ta đang

sẽ áp dụng hình ảnh này để làm mờ hình ảnh.

Vì vậy, điều gì sẽ xảy ra và bạn có thể thấy điều này, bạn có thể thử tương tác với điều này ở đây.

Bây giờ chúng ta thấy lưới nhỏ 3 x 3 mà chúng ta sắp áp dụng trên toàn bộ hình ảnh.

Và sau đó bạn có thể thấy kết quả cùng với phép tính nhân.

Và để ý rằng hình ảnh so với hình ảnh đầu ra, chúng ta có thể thấy rõ rằng hình ảnh đầu ra đã được

bị mờ do sự chuyển đổi áp dụng kernel này.

Và quá trình áp dụng kernel này đôi khi còn được gọi là tích chập.

Quá trình chụp hình này Đại tá rồi rê hoặc sải bước ngang qua hình ảnh này

và nhận được kết quả đầu ra này, thuật ngữ tích chập là cái mà chúng ta gọi khi nói về

điều này trong bối cảnh của một mạng lưới thần kinh tích chập.

Và ý tưởng chính đằng sau điều này là cho đến nay chúng tôi đã thực sự cho bạn thấy những hạt nhân này là bộ lọc hoạt động như thế nào

với các giá trị được xác định trước và đó là những giá trị nổi tiếng đối với một số hoạt động thực sự phổ biến nhất định,

như làm mờ một hình ảnh.

Sau này, chúng ta sẽ muốn mạng của mình thực sự chọn các trọng số đằng sau các bộ lọc này theo thứ tự

để thực hiện trích xuất đặc trưng.

Có lẽ chúng ta sẽ có một số bộ lọc thực sự tốt trong việc phát hiện lông mày hoặc những thứ tương tự nếu chúng ta

cố gắng phân loại khuôn mặt, chẳng hạn như từ các hình ảnh khác.

Vì vậy, ý tưởng chính đằng sau hình ảnh này, thưa Đại tá, trong bối cảnh của mạng lưới thần kinh tích chập là

mạng thực tế sẽ tìm ra trọng số chính xác thay vì chúng ta có những trọng số được xác định trước này.

Và thông thường khi bạn làm việc cho mạng nơ-ron tích chập, bạn sẽ nhận được rất nhiều khả năng phát hiện biên.

Và vì vậy chúng tôi thực sự có một số bộ lọc Sobell hoặc phát hiện cạnh ở đây.

Và bạn có thể thấy ở đây đây là một dạng phát hiện các đường ngang và bạn thậm chí có thể có trực giác

về điều này bằng cách chỉ cần kiểm tra ma trận để biết chúng ta có những giá trị âm lớn hơn ở đây và sau đó là trung tâm

dòng 0 và sau đó là các giá trị dương lớn hơn ở phía dưới.

Và nếu bạn có trực giác về việc điều này sẽ phản ứng như thế nào khi bạn đi dọc theo hình ảnh mà bạn có

những đường thẳng đứng mạnh mẽ chẳng hạn như đường chân tóc của người này ở đây, bạn sẽ nhận được kết quả cuối cùng có kích thước lớn hơn

giá trị khi bạn đi cùng.

Vì vậy, bạn có thể thấy ở đây vì chúng tôi đang bắt đầu phát hiện những loại đường ngang này, kết quả thực tế.

Khi bạn áp dụng kernel này chỉ bằng toán học, cách nó hoạt động rất sáng sủa so với những gì có

không có đường ngang, cuối cùng bạn sẽ có màu đen.

Như vậy ở đây chúng ta có thể thấy hình ảnh đầu ra được xuất ra rõ ràng những phần là các đường ngang.

Vì vậy, đó là cái được gọi là Sobol dưới cùng.

Và sau đó bạn có thể kiểm tra những thứ như.

Phải.

Và nó trông rất giống nhau, ngoại trừ việc bây giờ nó sẽ phát hiện các loại đường thẳng đứng.

Vì vậy, ý tưởng tương tự ở đây.

Bây giờ chúng ta có thể thấy rõ ràng những đường thẳng đứng của khuôn mặt người này ở phía bên tay trái và cái này

mặt người hướng về bên phải.

Và chúng ta cũng có thể thấy mũi của họ bắt đầu xuất hiện trong hình ảnh đầu ra đó.

Vì vậy, mạng nơ ron tích chập về cơ bản sẽ quyết định trọng số nào trên các bộ lọc của chính nó

vấn đề phân loại ảnh.

Và ở đây chúng tôi thực sự có thể có một hình ảnh tương tác và trình tải lên đại tá để bạn có thể chọn hình ảnh của riêng mình

tập tin và sau đó áp dụng bất kỳ hạt nhân nào bạn muốn và thậm chí bạn có thể phát triển hạt nhân tùy chỉnh của riêng mình tại đây.

Vì vậy, nó cho phép bạn bắt đầu thêm những thứ này để làm những việc bạn muốn khám phá.

Được rồi, ý tưởng chính đằng sau trang web này và chỉ cho bạn cách thức hoạt động của nó chỉ là lấy ý tưởng rằng

chúng ta sẽ có những hạt nhân này.

Họ không cần phải có ba người.

Đó có thể là bốn nhân bốn hoặc năm nhân năm.

Rõ ràng, số càng lớn thì chúng ta càng phải giải quyết nhiều thao tác và nhiều trọng số hơn.

Nhưng về cơ bản chúng ta chỉ cần kéo chúng lên trên hình ảnh và sau đó nó sẽ cho ra một loại kết quả nào đó.

Và hy vọng rằng, khi mạng lưới thần kinh tích chập học hỏi dựa trên hình ảnh, chúng tôi cung cấp dữ liệu cho nó, chúng tôi sẽ

nhận được một số kết quả đầu ra nhất định về cơ bản trích xuất các tính năng quan trọng.

Vì vậy, ở đây chúng tôi đang trích xuất các tính năng biên dựa trên hạt nhân này ngay tại đây.

Và bạn có thể thấy ở đây chúng ta có một bản phác thảo trong đó về cơ bản chúng ta đang tìm giá trị trung tâm của

tám là trọng lượng trung tâm chính của chúng tôi so với âm ở rìa.

Được rồi, hãy để tôi quay lại phần trình bày của chúng ta và kết thúc cuộc thảo luận về hình ảnh Col.

Được rồi.

Tôi hy vọng bạn thích ví dụ tương tác đó.

Và tôi khuyến khích bạn tự mình khám phá trang web đó.

Bây giờ, trong bối cảnh, như tôi đã đề cập, về mạng nơ ron tích chập, các bộ lọc này được gọi là

thành các hạt tích chập và quá trình truyền chúng qua một hình ảnh được gọi là tích chập.

Tôi muốn xem xét thêm một số yếu tố quan trọng cần ghi nhớ khi chúng ta tìm hiểu thêm về tích chập

mạng lưới thần kinh và hình ảnh.

Col hiện đang trong giai đoạn tích chập, chúng ta thực sự sẽ mất biên giới.

Vì vậy, nếu bạn xem xét kỹ hơn ví dụ trước đó, bạn sẽ nhận thấy có một đường viền màu đen

dọc theo hình ảnh đầu ra.

Và điều này là do khi bạn bắt đầu di chuyển về phía rìa của hình ảnh, thực tế bạn sẽ không

có những giá trị ở đó

Vì vậy, một cách để khắc phục điều này là bạn có thể thêm vào hình ảnh nhiều giá trị hơn và lựa chọn thực sự phổ biến chỉ là 0

hoặc loại ở giữa giá trị.

Và điều này cho phép chúng tôi không bị mất thông tin dọc theo biên giới đó.

Vì thế nó còn giúp chúng ta bảo toàn được kích thước hình ảnh.

Vì vậy, đây được gọi là đệm và đó là một kỹ thuật thực sự phổ biến mà mọi người thường sử dụng trên hình ảnh của mình.

họ không mất bất kỳ thông tin biên giới nào.

OK, vậy bây giờ chúng ta đã hiểu các bộ lọc hình ảnh, hãy tiếp tục và khám phá kiến trúc của bộ lọc tích chập

mạng thần kinh cho phép mạng đưa ra những cách tốt nhất cho bộ lọc trong cái được gọi là

lớp chập.

Vì vậy, chúng tôi hiểu rằng chúng tôi có các bộ lọc hình ảnh hoặc Col này mà về cơ bản chúng tôi sẽ thực hiện phép tính tích chập

trên hình ảnh.

Và tôi đã cho bạn xem các bộ lọc mà chúng tôi đã biết trọng số của chúng.

Tuy nhiên, khi nói đến những hình ảnh như hình ảnh chó hay mèo thì chúng ta chưa thực sự biết rõ đúng không?

ngay lập tức, giá trị hoặc trọng số bộ lọc nào sẽ quan trọng để phát hiện xem một con chó có

ở trong một hình ảnh hoặc một con mèo ở trong một hình ảnh.

Có lẽ sẽ là ý tưởng tốt hơn nếu chỉ có mạng tích chập để tự mình đưa ra các trọng số đó.

Và điều này được thực hiện trong lớp tích chập của mạng nơ ron tích chập sắp đi vào hoạt động

ngay trong bài giảng tiếp theo.

Tôi sẽ gặp bạn ở đó.