# 38 - Chức năng kích hoạt tiếng Anh

---

Chào mừng mọi người trở lại với bài giảng về hàm kích hoạt này.

Vì vậy, hãy nhớ lại từ các mô hình mạng thần kinh của chúng ta rằng X của Đầu vào có trọng số được gán cho chúng là W, sau đó

chúng tôi cũng thêm vào một thuật ngữ sai lệch gắn liền với chúng trong mô hình Perceptron hoặc nơ-ron đó, có nghĩa là công thức

chúng ta có X nhân W cộng B.

Vì vậy, rõ ràng, nếu chúng ta bắt đầu nghĩ về điều này, W. chỉ ám chỉ chúng ta nên cân nặng và sức mạnh bao nhiêu

đang cung cấp cho đầu vào đó.

Chúng ta gần như có thể coi đầu vào đó quan trọng như thế nào.

Sau đó, bạn có thể tưởng tượng nếu chúng ta có giá trị tuyệt đối của trọng số đó là rất lớn thì đầu vào hoặc

tính năng đó có lẽ thực sự quan trọng.

Chúng ta cũng có thể coi B là một giá trị bù đắp.

Chúng tôi đã đề cập đến điều này trước đây, nhưng về cơ bản điều đó làm cho X nhân W phải đạt đến một ngưỡng nhất định

trước khi có tác dụng và khắc phục được hạn B đó.

Vì vậy, ví dụ, nếu chúng ta có B bằng âm 10, thì tác động của X nhân W sẽ không thực sự

bắt đầu vượt qua số hạng B hoặc byas đó cho đến khi tích của chúng vượt quá 10.

Vì vậy, sau đó, hiệu ứng chỉ dựa trên giá trị W đó, do đó thuật ngữ sai lệch cho B, vì vậy bạn

về cơ bản có thể coi thuật ngữ byas đó như một ngưỡng mà nơ-ron đã đặt để đầu vào

lần trọng lượng để bắt đầu nhận được một số loại hiệu ứng đa số.

Vì vậy, điều tiếp theo chúng tôi muốn làm là đặt ranh giới cho giá trị đầu ra tổng thể của sự kết hợp đó

X nhân W cộng B, và để cho mọi thứ đơn giản chúng ta có thể làm là chúng ta có thể giữ nguyên Z bằng X nhân W cộng B,

và sau đó chúng ta có thể chuyển số hạng Z đó thông qua một loại hàm kích hoạt nào đó để giới hạn giá trị của nó.

Bây giờ, hãy nhớ rằng, rất nhiều nghiên cứu đã được thực hiện về chức năng kích hoạt và tính hiệu quả của chúng.

Chúng ta sẽ khám phá một số chức năng kích hoạt thực sự phổ biến.

Và sau đó tôi cũng sẽ cho bạn xem trang Wikipedia về các chức năng kích hoạt, trang này hiển thị và liệt kê một

nhiều hơn nữa.

Vì vậy, chúng ta được gọi là mô hình Neron đơn giản hoặc Perceptron có F trên X. Vậy chúng ta có thời gian của X đó, chúng

trọng số, cộng với độ lệch của Neron đó.

Vì vậy, bạn có thể tưởng tượng nếu chúng ta gặp vấn đề về phân loại nhị phân, chúng ta muốn đầu ra bằng 0 hoặc

một.

Bây giờ, như một ghi chú nhanh, như tôi đã đề cập, để tránh nhầm lẫn, tôi sẽ tìm tổng số đầu vào là

biến Z này trong đó Z bằng W, X, cộng với B. Vì vậy, trong bối cảnh mạng lưới thần kinh này và việc truyền

trong thời gian đầu vào, trọng số cộng với độ lệch thành hàm kích hoạt, tôi thực sự sẽ vượt qua

số hạng Z đó vào hàm kích hoạt.

Hãy nhớ rằng, bạn thường thấy các biến này được viết hoa trong tài liệu, chẳng hạn như hàm của chữ hoa

hoặc hàm của Chữ Z viết hoa liên quan đến chữ X viết hoa nào đó, để biểu thị rằng thay vì một đầu vào X duy nhất,

thực ra bạn có một đầu vào tensor bao gồm nhiều giá trị, có nghĩa là Z cũng là một Tenzer, nghĩa là

có nghĩa là bạn có trọng số Tenzer, v.v. Vì vậy, đừng nhầm lẫn về cách viết hoa.

Bạn có thể thấy nếu bạn đang đọc một số cuốn sách.

Một điều nữa mà bạn thường bối rối khi mọi người viết ra các hàm kích hoạt này,

thực tế phổ biến là viết chúng ra theo F, vì viết một hàm liên quan đến

đến X là loại mặc định.

Vì vậy, bạn có thể thấy một số hàm kích hoạt được viết liên quan đến X, đặc biệt là trên Wikipedia đó

trang, hoặc chỉ trong tài liệu thông thường và những cuốn sách bạn đang đọc về việc học Billett khiến bạn bối rối.

thực sự chuyển toàn bộ W, X cộng với B cho các hàm kích hoạt.

Được rồi, tôi vừa đề cập, nếu chúng ta đang giải một bài toán phân loại nhị phân, nó sẽ rất tuyệt

rằng Neron luôn phun ra số 0 hoặc số 1.

Vì vậy, các mạng đơn giản nhất có thể dựa vào hàm bước cơ bản cho kết quả bằng 0 hoặc một.

Vì vậy tất cả những gì chúng ta làm là phụ thuộc vào giá trị của Z.

Dọc theo đây chúng ta có thể thấy trục X.

Điều chúng ta sắp làm là nếu giá trị của Z nhỏ hơn 0 thì chúng ta sẽ xuất ra số 0.

Nếu giá trị của C lớn hơn 0 thì chúng ta xuất ra một.

Vì vậy, bất kể giá trị là gì, điều tuyệt vời ở đây là nó luôn cho kết quả bằng 0 hoặc một.

Vì vậy, loại chức năng này thực sự hữu ích cho việc phân loại.

Nó sẽ luôn xuất ra 0 hoặc 1.

Tuy nhiên, đây là một hàm rất mạnh, không trích dẫn, vì những thay đổi thực sự nhỏ không được phản ánh,

bạn có thể thấy ở đây chỉ có một điểm cắt ngay lập tức chia giữa 0 và 1 nếu tổng sản lượng

của Z xảy ra nhỏ hơn 0, chúng ta vừa định nghĩa nó bằng 0.

Nếu tổng đầu ra của Z lớn hơn 0 thì khi chúng ta chuyển nó qua hàm bước,

chúng tôi đại loại là hoàn thành nó cùng một lúc.

Vì vậy, có một mức sàn là 0, một mức trần là một, và mức cắt đứt ngay lập tức chỉ phụ thuộc vào điều đó.

tổng giá trị của Z cuối cùng là.

Tuy nhiên, sẽ thật tuyệt nếu thay vì sử dụng hàm bước ấn tượng như vậy, chúng ta có một chút

nhiều hơn một chút về hàm động, chẳng hạn như đường màu đỏ đó.

Thật may mắn cho chúng tôi và có thể bạn đã quen với điều này nếu bạn đã từng học máy

các lớp, đây thực sự là hàm sigmoid.

Nó có cùng giới hạn dưới và giới hạn trên.

Vì vậy, 011, rất hữu ích cho việc phân loại nhị phân, nhưng nó thực hiện việc này ở mức vừa phải hơn một chút.

thời trang hơn là một đường cắt đơn giản mà chức năng bước sẽ thực hiện.

Và ở đây bạn có thể thấy công thức của hàm sigmoid, còn được gọi là hàm logistic,

là F của Z trong trường hợp của chúng ta bằng một chia cho một cộng với lũy thừa của Z âm, trong đó Z trong

trường hợp sẽ bằng X cộng B.

Vì vậy, việc thay đổi chức năng kích hoạt được sử dụng trong tế bào thần kinh của bạn có thể thực sự có lợi tùy thuộc vào nhiệm vụ.

Bây giờ, hãy nhớ rằng, điều này vẫn có tác dụng đối với việc phân loại, nhưng điều thực sự thú vị là nó sẽ như vậy

nhạy cảm hơn một chút với những thay đổi nhỏ.

Và nếu muốn, chúng ta thực sự có thể lấy đầu ra đó, giá trị sigmoid, để coi nó như một xác suất

giữa số không và một.

Vì chúng ta có thể thấy ở đây rằng có những giá trị thực sự, nên nó sẽ xuất ra giữa 0 và 1

thay vì chỉ bằng 0 hoặc chỉ một, đường màu đỏ đó sẽ có thể báo cáo lại điều gì đó như

không điểm sáu hoặc không điểm bốn.

Sau đó, chúng tôi sẽ cung cấp cho bạn ý tưởng về mức độ chắc chắn của mạng khi nó thuộc về bất kỳ lớp cụ thể nào.

Vì vậy, hãy thảo luận thêm về một số hàm kích hoạt mà chúng ta sắp gặp, một số hàm thực sự phổ biến

những thứ hoặc những thứ như tiếp tuyến hyperbol hiện nay, S10, H và Hiebert có thể thấy các công thức với

đối với X ở vế phải.

Vậy có hyperbol, cosin, sin hyperbol.

Nhưng phổ biến nhất là tang hyperbol, đó là sin hyperbol chia cho cos hyperbol.

Vậy điều tuyệt vời ở đây là nó sẽ xuất ra giữa âm một và một thay vì 0 thành một

trông thực sự giống với hàm sigmoid.

Về cơ bản, sự khác biệt chính là giới hạn dưới của tầng đó.

Và chúng ta sẽ thảo luận lý do sau.

Với một số nơ-ron và một số mạng nhất định, việc sử dụng tiếp tuyến hyperbol sẽ hợp lý hơn.

Tôi chỉ muốn bạn biết rằng đó là một lựa chọn thực sự phổ biến.

Bây giờ, một hành động thực sự phổ biến khác là đơn vị Linea đã được chỉnh sửa được rút ngắn thành ELU của chúng tôi và đây thực sự là

một chức năng thực sự tương đối đơn giản.

Về cơ bản, bạn có thể mô tả nó là Max Zero Z, về cơ bản nói rằng nếu đầu ra của giá trị

nhỏ hơn 0, chúng ta coi nó là 0.

Mặt khác, nếu nó lớn hơn 0, chúng tôi sẽ tiếp tục và xuất giá trị Z thực tế đó.

Vì vậy, các đơn vị Linera đã được chỉnh sửa thực sự đã được nhận thấy là có hiệu suất rất tốt, đặc biệt là khi giao dịch.

với vấn đề độ dốc biến mất, đây là một thuật ngữ và chúng ta sẽ thảo luận chi tiết hơn trong tương lai

bài giảng vì việc sử dụng đơn vị tuyến tính hiệu chỉnh và tài liệu thường được sử dụng khi chúng ta xây dựng

mạng của chúng tôi, sẽ mặc định là đơn vị tuyến tính được chỉnh lưu làm hàm kích hoạt do tổng thể của nó

hiệu suất tốt.

Bây giờ để có danh sách đầy đủ các chức năng kích hoạt có thể có, bạn nên xem Wikipedia

trang về chức năng kích hoạt.

Trên thực tế, chúng ta hãy tiếp tục và tham quan nhanh nó ngay bây giờ.

Được rồi.

Tôi đang ở trên trang Wikipedia về các chức năng kích hoạt.

Và chúng ta có thể thấy ở đây rằng nó thực sự hiển thị cho bạn chức năng kích hoạt logistic như một loại chức năng chính của nó

hình ảnh.

Nhưng nếu bạn cuộn xuống, nó sẽ nói về các chức năng, về mạng lưới thần kinh lấy cảm hứng từ sinh học.

Đây là hình ảnh chúng tôi đã cho bạn xem trước đó.

Bạn có thể tiếp tục đi xuống đây một số cấu trúc thay thế nếu bạn không muốn sử dụng chức năng kích hoạt.

Nhưng cuối cùng khi bạn cuộn xuống đây, bạn sẽ phải làm một số điều để so sánh lại các chức năng kích hoạt,

chẳng hạn như phi tuyến tính, phạm vi, giới hạn trên, giới hạn dưới nếu chúng khả vi liên tục.

Nhưng ở đây chúng ta có thể thấy bảng nhỏ này hiển thị rất nhiều hàm kích hoạt thường được sử dụng

là dẫn xuất của chúng, điều này sẽ rất quan trọng.

Chúng ta đang nói về những thứ như lan truyền ngược.

Nhưng hãy nhớ rằng điều quan trọng thực sự chỉ là cái tên, cốt truyện và phương trình.

cung cấp cho bạn một cái nhìn tổng quan về chức năng kích hoạt thực sự đang làm gì.

Có một nhận dạng đơn giản, đó là bất cứ thứ gì mà nơ-ron tạo ra, đó sẽ là những gì nó tạo ra

với chức năng kích hoạt gắn liền với nó.

Có bước nhị phân, về cơ bản là 0 nếu bạn nhỏ hơn 0, một nếu bạn lớn hơn hoặc

bằng không.

Logistic còn được gọi là sigmoid hoặc sophs, đây cũng là hàm kích hoạt rất phổ biến

để sử dụng, đặc biệt là để phân loại nhị phân.

Chúng ta có những thứ như tang hyperbol mà bạn vừa đề cập trông rất giống sigmoid, ngoại trừ

bạn có thể thấy ở đây ở giới hạn trên và dưới, cụ thể là giới hạn dưới là giới hạn âm.

Có cung, tiếp tuyến, cung, sin hyperbol, rất nhiều thứ ở đây.

Sau đó, nếu bạn tiếp tục chạy chậm lại, bạn sẽ thấy đơn vị Rectify Linear có toàn bộ trang Wikipedia về

quan tâm đến nó.

Như tôi đã đề cập trước đó, đây là một chức năng kích hoạt thực sự phổ biến được sử dụng.

Rất phổ biến.

Nó có bài viết Wikipedia riêng về nó.

Sau đó là loại đơn vị tuyến tính được chỉnh lưu, tiên tiến hơn.

Vì vậy, gần đây, rất nhiều người đã thử nghiệm các biến thể khác nhau của tuyến tính chỉnh lưu.

đơn vị cụ thể, thực sự có một đơn vị tuyến tính bị rò rỉ, được chỉnh sửa thay vì loại phẳng

xếp ở 0, bốn giá trị dọc theo trục x nhỏ hơn 0, nó hơi rò rỉ một chút

và có độ dốc rất nhỏ này.

Điều này thực sự là một chút phóng đại ở đây.

Chúng ta có thể thấy nó sẽ bằng 0 điểm 0 một x 4 X, tức là nhỏ hơn 0.

Vì vậy, đây được gọi là đơn vị tuyến tính bị rò rỉ, được chỉnh lưu.

Và có một loạt các đơn vị tuyến tính khác có thể xem tại đây.

Như bạn có thể thấy, chúng tôi có rất nhiều lựa chọn khác nhau ở đây.

Nhưng thông thường những gì chúng ta sắp làm là sử dụng những thứ như hàm sigmoid, hàm softmax

chức năng phân loại nhiều lớp mà chúng ta sẽ nói đến sau đây và sau đó sẽ sửa lại

các đơn vị sau này vì nhìn chung chúng có hiệu suất khá tốt.

Vì vậy, hãy nhớ rằng khuyến khích bạn xem trang chức năng kích hoạt tại đây.

Bài viết này thực sự thú vị.

Nhưng điều khác tôi muốn bạn ghi nhớ là hiện tại chúng ta chỉ thảo luận về những thứ như hệ nhị phân.

phân loại, giữ mọi thứ từ 0 đến 1, và sau đó có thể chúng ta có một loại xác suất cố định nào đó

ở đó.

Nhưng có một loạt vấn đề khác mà chúng ta phải suy nghĩ nếu chúng ta xử lý nhiều lớp

phân loại.

Vì vậy, hãy tiếp tục thảo luận về các hàm và mạng kích hoạt phân loại đa lớp trong phần tiếp theo.

bài giảng.

Tôi sẽ gặp bạn ở đó.