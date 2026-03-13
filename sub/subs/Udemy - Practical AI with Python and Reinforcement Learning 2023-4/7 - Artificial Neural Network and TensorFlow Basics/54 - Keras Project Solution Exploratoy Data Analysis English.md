# 54 - Keras Project Solution Exploratoy Phân tích dữ liệu Tiếng Anh

---

Chào mừng tất cả mọi người đến với bài giảng đầu tiên của chúng tôi và lời giải cho các câu hỏi bài tập dự án này.

Chúng ta sẽ bắt đầu với phần phân tích dữ liệu thăm dò.

Hãy bắt đầu.

Được rồi, tôi đang ở sổ ghi chép bài tập, sẽ bắt đầu bằng cách chạy vài phần khởi động đầu tiên

ô mã hóa.

Vì vậy, đó là việc nhập dữ liệu cho phép chúng tôi chạy chức năng thông tin đối tượng, cũng như tải

trong tập dữ liệu thực tế sẽ làm việc.

Vì vậy, có vẻ như tất cả đã được tải.

Tiếp theo, hãy bắt đầu phân tích dữ liệu thăm dò.

Vì vậy, như tôi đã đề cập trước đây, đây luôn là một ý tưởng hay, đặc biệt nếu có vấn đề về phân loại cần giải quyết.

âm mưu khám phá sự cân bằng thực tế của nhãn của bạn.

Vì vậy chúng ta sẽ nói S.A.S. đếm lô và chúng tôi sẽ nói tình trạng cho vay.

Và giả sử dữ liệu bằng D.F., vậy đó là cách bạn có thể tạo một biểu đồ ở đây và tôi sẽ nói đây là một

vấn đề mất cân bằng hoặc mất cân bằng.

Lưu ý rằng chúng tôi có nhiều mục nhập về những người đã trả hết khoản vay của họ hơn số người mà chúng tôi có

điều đó đã không trả lại.

Và điều này thực sự phổ biến đối với những vấn đề như vấn đề phân loại liên quan đến gian lận hoặc thư rác.

Có ít trường hợp gian lận hoặc thư rác hơn so với các hành động hợp pháp, chẳng hạn như hành động hợp pháp.

email hoặc một giao dịch mua thẻ tín dụng hợp pháp hoặc một khoản vay hợp pháp đã được thanh toán đầy đủ.

Vì vậy, đó là điều cần ghi nhớ.

Và điều đó có nghĩa là chúng tôi có thể mong đợi có thể làm rất tốt về mặt độ chính xác, nhưng độ chính xác của chúng tôi

và thu hồi sẽ là số liệu thực sự mà chúng tôi sẽ phải dựa vào đó để đánh giá mô hình của mình.

Và chúng tôi dự kiến sẽ thực hiện tốt điều đó trên các số liệu cụ thể đó do thực tế là chúng tôi có

tập dữ liệu rất mất cân bằng ở đây.

Vì vậy, chúng tôi muốn tạo biểu đồ của cột số tiền cho vay.

Có rất nhiều cách khác nhau để chúng ta có thể làm điều này.

Có lẽ cách dễ nhất là chỉ cần gọi một biểu đồ phân phối trên cột đó để chúng ta có thể gọi D.F. tiền vay

số tiền ở đây.

Và vì tôi chỉ muốn biểu đồ thực tế nên tôi sẽ nói KDDI bằng sai.

Và nếu bạn chỉ chạy nó, về cơ bản nó sẽ cung cấp cho bạn thông tin cơ bản về biểu đồ, thì bạn có thể bắt đầu

chơi đùa với những thứ như thùng rác.

Vì vậy, nếu bạn muốn có nhiều thùng hơn, bạn có thể tăng số lượng thùng ở đó và bạn cũng có thể chơi xung quanh

với những thứ như kích thước.

Vì vậy, bạn luôn có thể nói kích thước fiqh của hình Pulte bằng một số bộ dữ liệu.

Vì vậy, thông thường đối với biểu đồ bạn muốn chúng dài nhưng ngắn hơn một chút.

Vì vậy, bạn nhận được một cái gì đó trông như thế này.

Được rồi, có rất nhiều cách khác nhau để bạn có thể làm điều đó.

Nhưng về cơ bản, điều cần chú ý ở đây là bạn thấy những đột biến này xảy ra ở mức tiền chẵn này

số lượng, loại nào có ý nghĩa.

Vì vậy, rõ ràng, những đột biến này đang xảy ra ở mức giống như khoản vay thậm chí mười nghìn đô la thay vì

tăng đột biến một số giá trị ngẫu nhiên như tám nghìn ba trăm ba mươi ba.

Vì vậy, đó chính là điều mà những đột biến nhỏ này về cơ bản đang chỉ ra rằng có một số lượng nhất định

về cơ bản là các khoản vay tiêu chuẩn.

OK, vậy chúng ta hãy tiếp tục khám phá mối tương quan giữa các biến đặc trưng liên tục để chúng ta có thể

dễ dàng làm điều này bằng cách chỉ cần nói D.F..

Và sau đó tính toán mối tương quan như vậy, nên nó chỉ là một phép toán đơn giản.

Chúng tôi đã thấy điều này rất nhiều lần trong suốt các bài giảng của mình.

Chúng ta cũng đã thấy một chút về cách chúng ta có thể hình dung nó.

Vì vậy, cách chúng ta có thể hình dung nó là gọi bản đồ nhiệt bản chất về mối tương quan cụ thể này.

Và chúng ta cũng có thể nói chú thích bằng true.

Vì vậy, chúng tôi có những liên kết thực tế đó cho bạn trong trường hợp bạn quan tâm đến những liên kết đó.

Và tôi sẽ tiếp tục thay đổi cách ánh xạ màu.

Trở thành Seamap.

Cái này chỉ vì đối với tôi, nó luôn rõ ràng một chút, vì vậy nếu bạn chỉ chạy cái này,

bạn sẽ có được loại bản đồ nhiệt thực sự được thu nhỏ này.

Vì vậy, điều bạn có thể làm trước hết là mở rộng kích thước, chẳng hạn như con số phạt.

Và điều này phải luôn đi trước lệnh seabourne của bạn, chẳng hạn như kích thước cố định.

Và hãy làm cái này lớn hơn một chút, khoảng 12 x 7.

Bạn chạy nó và nó sẽ được cải thiện hơn rất nhiều.

Nhưng điều cần lưu ý ở đây là tùy thuộc vào phiên bản matplotlib của bạn, bạn sẽ nhận thấy ở phía dưới

và phần trên thực sự bị cắt bỏ ở đây.

Và bạn có thể xem các liên kết mà chúng tôi đã cung cấp cho bạn để được trợ giúp về việc thay đổi kích thước.

Cụ thể ở phần thứ hai này, chúng ta sẽ nói về lỗi nhỏ đó và đó là do matplotlib

chơi không tốt đâu, Seabourne.

Vì vậy, cách bạn có thể chỉnh sửa là làm rối tung các giới hạn Y.

Vì vậy có rất nhiều giải pháp khác nhau.

Vì vậy, một cách và chúng tôi thể hiện điều này trong sổ tay giải pháp là sau cuộc gọi seabourne, đơn giản là

nói Pilt y chi và họ nói đi từ 10 đến 0 hay gì đó tương tự, và điều đó sẽ kéo dài

bản đồ nhiệt thực tế

Được rồi, đó là bản đồ nhiệt của chúng ta.

Chúng ta có thể thấy các mối quan hệ khác nhau giữa các tính năng và rõ ràng là bạn sẽ có được mối tương quan hoàn hảo

dọc theo đường chéo.

Vì vậy, khi di chuyển đến đây, chúng tôi sẽ nói rằng bạn lẽ ra phải nhận thấy mối tương quan gần như hoàn hảo với

tính năng trả góp này.

Vì vậy, nếu chúng ta quay lại đây, hãy lưu ý rằng số tiền cho vay có mối tương quan bằng 0,95 với

đợt này.

Vì vậy, điều đó khá thú vị.

Vậy hãy cùng khám phá thêm tính năng này nhé.

Chúng tôi muốn đảm bảo rằng chúng tôi không vô tình làm rò rỉ dữ liệu từ các tính năng của mình vào nhãn của mình.

Vì vậy, chúng tôi luôn muốn đảm bảo rằng không có một đặc điểm nào có thể dự đoán nhãn hoàn hảo,

vì về cơ bản điều đó chỉ ra rằng đó không thực sự là một tính năng.

Có lẽ đó chỉ là một số thông tin trùng lặp rất giống với nhãn.

Vì vậy hãy tiếp tục và in nó ra.

Chúng tôi sẽ nói thông tin tính năng về phần đó.

Vì vậy, chúng tôi tiếp tục thực hiện việc này và khoản trả góp là khoản thanh toán hàng tháng mà người đi vay phải trả nếu

khoản vay bắt nguồn.

Vì vậy, từ khóa là nếu.

Và sau đó chúng tôi cũng sẽ nói thông tin đặc trưng về số tiền cho vay.

Và đây là số tiền giới hạn mà người đi vay áp dụng, nên điều này khá hợp lý.

rằng số tiền trả góp và số tiền vay thực tế sẽ có mối tương quan cực kỳ lớn vì về cơ bản chúng

tương quan với một số loại công thức nội bộ mà công ty này sử dụng, điều này khá hợp lý.

Nếu bạn cho ai đó vay một triệu đô la, bạn sẽ mong đợi rằng theo một số công thức, khoản thanh toán của bạn,

số tiền trả góp hàng tháng của bạn sẽ khá cao và bạn có thể sẽ sử dụng cùng một công thức đó

ngay cả khi bạn cho ai đó vay một nghìn đô la, thì những khoản thanh toán đó sẽ có khả năng tương quan với nhau.

ít hơn nhiều.

Vì vậy, rõ ràng họ đang sử dụng một loại công thức nào đó chỉ là hàm số trực tiếp của số tiền vay để tính toán

ra phần trả góp sẽ là gì.

Và chúng ta luôn có thể thực hiện một biểu đồ phân tán để xác nhận điều này.

Chúng ta có thể nói Asness.

Scatterplot và ta có thể thấy mối tương quan cao này nên ta thấy X phần Y bằng.

Số tiền cho vay và sau đó là dữ liệu bằng D.F., vì vậy chúng tôi chạy số tiền đó và chúng tôi sẽ có thể thấy những phân tán thực tế này

âm mưu và bạn có thể làm những việc như tắt rìa thị trường, làm cho Alpha nhẹ hơn một chút, vân vân.

OK, vậy tiếp theo chúng ta muốn tạo một hộp thể hiện mối quan hệ giữa trạng thái khoản vay và khoản vay

số tiền.

Vì vậy, nó sẽ trả lời câu hỏi liệu có mối quan hệ nào giữa các khoản vay thực sự đắt đỏ hay không

và không thể trả hết hoặc các khoản vay với số tiền rất thấp và sau đó thanh toán đầy đủ những khoản đó?

Vì vậy, những gì chúng tôi làm chỉ đơn giản là nói.

Nhận một hộp âm mưu.

Về tình trạng cho vay của chúng tôi.

Vì trục x rồi trục Y sẽ là số tiền chúng ta vay.

Và dữ liệu của chúng tôi vẫn giữ nguyên khung dữ liệu đó.

Điều này cho phép chúng ta khám phá mối quan hệ và nói chung, có vẻ như chúng khá giống nhau,

tính trung bình các khoản vay, bạn có thể thấy ô này cao hơn một chút, nghĩa là nếu khoản vay của chúng tôi

số tiền cao hơn, chúng tôi có khả năng tăng nhẹ về khả năng số tiền đó bị tính phí, một lần nữa,

về mặt trực giác, có nghĩa là việc trả các khoản vay lớn sẽ khó hơn các khoản vay nhỏ.

Vì vậy, chúng cực kỳ giống nhau ở đây.

Vì vậy, đây không phải là chỉ báo quan trọng về việc liệu ai đó có trả hết khoản vay của họ hay không, số tiền thực tế

họ cất cánh.

Nhưng có một mối quan hệ nhỏ mà chúng ta có thể thấy từ hình hộp này.

Và chúng ta có thể làm điều này bằng cách chỉ tính toán số liệu thống kê tóm tắt cho số tiền vay được nhóm theo trạng thái khoản vay.

Vì vậy tôi có thể nói như sau, tôi sẽ nói D.F. nhóm theo.

Tình trạng khoản vay, sau đó nếu tôi chỉ nhóm theo tình trạng khoản vay rồi hỏi người ghi chép thì nó sẽ hiển thị cho tôi

điều này cho tất cả các cột.

Vì vậy, hãy chú ý ở đây, có một khung dữ liệu thực sự lớn trong khi thực sự tất cả những gì tôi quan tâm ở đây là

trường hợp cụ thể, vì đây là nội dung câu hỏi yêu cầu, là số tiền cho vay.

Và điều này về cơ bản cho chúng ta thấy những con số định lượng đằng sau biểu đồ hình hộp này.

Vì vậy, nếu bạn từng gặp trường hợp như thế này mà biểu đồ hình hộp hơi khó đọc, bạn luôn có thể so sánh

mức trung bình ở đây nên bạn có thể thấy giá trung bình đã tính phí cao hơn một chút so với mức giá được thanh toán đầy đủ

cho vay.

Được rồi, một lần nữa, tất cả những điều này cho thấy mức trung bình của các khoản vay đối với những người không có khả năng trả

số tiền họ trả lại cao hơn một chút so với mức trung bình của những người trả hết khoản vay của họ.

Đó là những gì có trong hộp cốt truyện.

Và nếu nó hơi khó đọc, bạn luôn có thể kiểm tra phần này theo cách thủ công.

Vậy đó chính là điều mà những bài kiểm tra này đang cố gắng giúp bạn nhận ra.

Tiếp theo, chúng ta hãy tiếp tục khám phá những cột tuyệt vời và tuyệt vời mà LendingClub gán cho

các khoản vay.

Và câu hỏi đầu tiên là, các cấp độ và cấp độ phụ duy nhất có thể có là gì?

Điều này sẽ khá đơn giản.

Bạn có thể chỉ cần lấy cột lớn và sau đó yêu cầu.

Điểm độc đáo của điều này và bạn sẽ có thể làm điều tương tự cho một cột tuyệt vời nào đó, chỉ cần

nói.

Độc đáo và chúng ta có thể thấy ngay rằng các lớp phụ này về cơ bản chứa thông tin thực tế

chính lớp vì nó chứa chữ cái lớp và sau đó là một loại ký tự phụ nào đó.

Và nếu chúng ta muốn biết thông tin về nội dung nó đại diện, chúng ta luôn có thể nói thông tin nguồn cấp dữ liệu rồi chuyển

trên một cái gì đó như lớp phụ và nó sẽ báo cáo lại lớp phụ khoản vay được chỉ định của LendingClub, được chứ?

Vì vậy, chúng tôi cuộn xuống đây và chúng tôi muốn tạo tài khoản Plott cho mỗi lớp và đặt màu sắc thành trạng thái cho vay

nhãn và bằng cách này, chúng tôi có thể biết liệu có sự khác biệt giữa việc trả hết khoản vay của bạn hay có

nó sẽ bị tính phí dựa trên điểm của bạn.

Vì vậy chúng ta sẽ nói S.A.S. Đếm Âm mưu.

Chúng ta sẽ nói X bằng màu xanh lá cây.

Dữ liệu là khung dữ liệu của chúng tôi và đây là Hugh, chúng tôi sẽ tiếp tục và coi đó là trạng thái cho vay của chúng tôi.

Chúng tôi chạy nó và ở đây chúng tôi có thể thấy mối quan hệ rõ ràng, nhưng hơi khó nói

đây là thứ tự của các lớp thực tế.

Vì vậy, hãy chú ý rằng chúng ta đang bắt đầu với B và sau đó đến A, C, E, sương mù.

Vì vậy, nó sẽ được tốt đẹp.

Và chúng ta sẽ làm gì ở bài toán tiếp theo.

Nhiệm vụ tiếp theo của chúng tôi thực sự là chỉ cho bạn hoặc yêu cầu bạn tìm ra cách sắp xếp lại các mẹo trục x này.

Nhưng về cơ bản điều này đang thể hiện là tỷ lệ phần trăm các khoản vay bị tính phí có vẻ như đang tăng lên

khi điểm chữ cái ngày càng cao.

Vì vậy, có vẻ như những khách hàng tốt nhất sẽ được đánh giá cao hơn khách hàng tốt thứ hai khi được xếp hạng A, B, C,

D, v.v. Và chúng ta có thể làm điều này bằng cách so sánh các tỷ lệ ở đây.

Vì vậy, chúng ta hãy xem xét kỹ hơn về vấn đề này, hãy thực sự thực hiện theo cấp lớp phụ để chúng ta có thể thực sự cần phải

thay đổi kích thước để cố gắng có được âm mưu này.

Nhưng điều đầu tiên tôi sẽ làm là đếm số lượng các nhóm con này để xem sự phân bố này xuyên suốt

toàn bộ tập dữ liệu.

Chúng ta có bao nhiêu cái một?

Chúng ta có bao nhiêu lần, v.v.?

Và chúng ta có thể thấy từ câu trả lời, có vẻ như đa số là điểm B và C, điều này tạo nên

hợp lý vì đây rõ ràng là những khoản cho vay rủi ro hơn, vì chúng có nhiều khả năng bị tính nợ dựa trên

về những gì chúng ta đã thấy ở đây về điểm tổng thể.

Lưu ý rằng mức giá thanh toán đầy đủ và mức giảm giá gần như giống nhau đối với người ở hạng G

thể loại.

Vậy làm thế nào để chúng tôi thực sự hiển thị số lượng âm mưu này cho mỗi lần nâng cấp?

Vâng, chúng tôi chỉ đơn giản nói.

S.A..

Biểu đồ đếm đó và sau đó chúng ta sẽ nói X bằng.

Nhớ lại lớp, có một dấu gạch dưới ở đó.

Và sau đó là dữ liệu của chúng tôi.

Bằng với D.F. Bây giờ, nếu bạn chỉ chạy biểu đồ này, bạn sẽ nhận được thứ gì đó trông như thế này.

Vì vậy điều đầu tiên chúng ta nên sửa là kích thước của ô này.

Vì vậy chúng ta sẽ làm điều đó bằng cách nói hình Kielty.

Kích thước của nó bằng và nó sẽ tạo thành 12 x 4.

Được rồi, vậy là xong việc về kích thước.

Tuy nhiên, điều tôi muốn có thể làm là sắp xếp lại trục x đó.

Vì vậy, nếu bạn nghiên cứu một chút về cốt truyện ở Seabourne, về cơ bản bạn chỉ cần đến Seabourne

Trang API hoặc hướng dẫn rồi tra cứu số lượng biểu đồ.

Vì vậy, nó sẽ ở đây trong các ô phân loại.

Bạn sẽ nhận thấy rằng thực tế có một tham số thứ tự, đây chỉ là danh sách các chuỗi.

Vậy đó chính là thứ tự bạn muốn.

Vì vậy, hãy tiếp tục và tìm ra điều đó.

Vì vậy, điều chúng ta sắp làm ở đây là chúng ta sẽ nói thứ tự lớp phụ của mình.

Mong muốn tương đương sẽ quay lại đây và sử dụng những gì chúng tôi đã làm trước đây, nơi chúng tôi in ra thực tế

duy nhất, vì vậy chúng tôi sẽ sao chép nó và sau đó chúng tôi sẽ sắp xếp chúng bằng cách sử dụng python cơ bản.

Vì vậy, Python dựa trên có loại chức năng này.

Và về cơ bản những gì chúng tôi đang làm ở đây là thay đổi kích thước cốt truyện và bây giờ chúng tôi có danh sách thứ tự phụ này,

đây là cách gọi được sắp xếp của các lớp phụ duy nhất và sau đó tôi sẽ chuyển nó vào.

Theo yêu cầu của tôi ở đây, chúng ta sẽ đi và nói rằng nó rất có trật tự.

Chạy nó và bây giờ bạn sẽ thấy mọi thứ được sắp xếp theo thứ tự.

Điều cuối cùng cần lưu ý ở đây là điều tôi không thích là màu sắc có vẻ quá giống nhau giữa một cái.

hay tám nhóm và các nhóm.

Vì vậy, tôi chỉ chọn một bảng màu về cơ bản không cho phép điều đó.

Và trong trường hợp của tôi, sau khi khám phá tài liệu về matplotlib, tôi thích làm mát ấm áp.

Vì vậy, bạn có thể thấy ở đây các loại tốt hơn về cơ bản có màu xanh hơn và các loại kém hơn có màu đỏ hơn.

ĐƯỢC RỒI.

Vì vậy, ở đây chúng ta có thể thấy rằng về cơ bản nó trông giống như năng lượng, nên điểm số không được trả thường xuyên.

Vì vậy, chúng tôi muốn tách biệt những thứ đó và tạo lại biểu đồ đếm chỉ dành cho những nâng cấp đó.

Bạn cũng sẽ nhận thấy rằng ở đây, nó cũng yêu cầu bạn có thể thoải mái thử nghiệm với màu sắc.

Vì vậy, ở mảnh đất thứ hai này, chúng tôi chỉ có trạng thái cho vay ở đây.

Vì vậy, chúng ta cũng có thể so sánh điều đó.

Vì vậy, bạn luôn có thể làm điều đó bằng cách chỉ cần đến đây và nói bạn.

Bằng.

Tình trạng cho vay.

Và sau đó bạn có được cốt truyện đó.

Rất nhiều thông tin ở đây mà chúng ta có thể coi là chỉ từ hình ảnh trực quan và rõ ràng đây là loại kém nhất

danh mục, có vẻ như tỷ lệ giảm giá gần giống như tỷ lệ thanh toán đầy đủ.

Vì vậy, có thể đáng để điều tra xem liệu việc cho mọi người vay tiền có đáng hay không, nếu chúng ta chấm điểm

họ là G hoặc F.

Và điều chúng ta sắp làm ở đây là về cơ bản chúng ta sẽ phóng to phần nhỏ đó

của cốt truyện.

Và cách chúng ta sắp làm điều đó chỉ đơn giản là cùng một đoạn mã.

Nhưng trước tiên chúng ta sẽ lọc nhanh bằng cách sử dụng pandas.

Vì vậy, về cơ bản tôi sẽ sao chép và dán mã này.

Hãy quay lại đây.

Dán nó vào đây và điều tôi sẽ làm ở đây là nói rằng tôi chỉ muốn FMG, vì vậy tôi sẽ nói FMG bằng khung dữ liệu của tôi

nơi lớp khung dữ liệu của tôi.

Bằng G.

Toán tử pipe, hoặc khi điểm bằng F, rồi tôi sẽ gói những kẻ này vào trong ngoặc đơn để tạo

chắc chắn bạn không nhận được của họ.

Và sau đó, phần còn lại của dòng mã mà chúng ta có D.F., tôi sẽ thay thế nó bằng FFG.

Vì vậy, chúng tôi sẽ lấy thứ tự riêng của mình ở đó và chúng tôi sẽ đặt dữ liệu của mình ở đó.

Được rồi, vậy tất cả những gì chúng ta đang làm về cơ bản là đặt lại khung dữ liệu và sau đó thực hiện các biểu đồ tương tự

như trên.

Vì vậy, nếu chúng tôi chạy nó ngay bây giờ, chúng tôi có thể thấy trạng thái được thanh toán đầy đủ so với trạng thái Chartoff cho những điều này về cơ bản

điểm kém hơn, và bạn sẽ nhận thấy rằng nếu bạn được xếp loại G5 thì khả năng là gần như hoàn toàn

trả hết khoản vay của bạn so với việc bị tính phí cho khoản vay.

Được rồi, chúng ta còn một âm mưu nữa cần tạo để tạo nó, trước tiên chúng ta phải hoàn thành nhiệm vụ này, nhiệm vụ này

đang tạo một cột mới có tên là Lone Repayed, cột này sẽ chứa một cột ở trạng thái duy nhất đã được thanh toán đầy đủ

và số 0 nếu nó đã bị tính phí.

Vì vậy, ngay bây giờ, cột nhãn của chúng tôi là các chuỗi và tôi muốn thay đổi bản đồ cơ bản đó

đến một và không.

Vì vậy, có rất nhiều cách khác nhau để chúng ta có thể làm điều này.

Nhưng có một cách là nói đơn giản.

Tình trạng khoản vay của tôi.

Hãy tiếp tục và lập bản đồ thanh toán đầy đủ.

Và tôi chỉ có thể sao chép điều này và bạn có thể lấy điều này như một cuộc gọi duy nhất, nhưng hãy tiếp tục và lập bản đồ thanh toán đầy đủ

là một và sau đó bản đồ được tính phí.

Bằng 0 và sau đó chúng tôi muốn bạn đặt cột này làm cột mới và chúng tôi sẽ thiết lập cột này trong cột của bạn

được gọi là Lone Underscore Repayed, và đây thực sự sẽ là cột lao động mà chúng tôi sử dụng khi làm việc

của dòng chảy Tenzer.

Vì vậy, hãy tiếp tục và chạy nó và sau đó bạn sẽ có thể xem cả hai.

Vì vậy, hãy tiếp tục và thể hiện điều đó.

Vậy là chúng ta đã hoàn trả được khoản vay, dấu phẩy.

Tình trạng vay vốn, chỉ cần nhìn hai cái đó là thấy có tác dụng nên khoản vay đã được hoàn trả.

Đó là một nếu nó được thanh toán đầy đủ.

Nó bằng 0 nếu nó đã bị tính phí.

Vì vậy, bây giờ điều đó cho phép chúng tôi hoàn thành những hình dung trực quan cuối cùng của mình, điều mà chúng tôi thực sự đã thực hiện ở phần trước.

bài giảng.

Vì vậy, về mặt kỹ thuật, đây là một nhiệm vụ đầy thách thức nhưng có một liên kết hữu ích trong trường hợp bạn cần trợ giúp.

Và điều chúng tôi muốn nó làm về cơ bản là thực hiện biểu đồ này để cho thấy những đối tượng số nào có giá trị cao nhất

tương quan với nhãn thực tế.

Và chúng tôi đã làm điều này trong các nhiệm vụ phân loại hoặc trong các bài giảng phân loại trước đây.

Nhưng hãy tiếp tục và chỉ cho bạn cách thực hiện lại.

Bước đầu tiên, hãy thực sự tính toán những mối tương quan đó.

Bước tiếp theo là chỉ lấy.

Đó là cột hoàn trả khoản vay.

Sau đó, điều bạn có thể làm là nói Plott.

Kynikos BA, và điều đó cung cấp cho bạn những kiến ​​thức cơ bản về nội dung cốt truyện này.

Tuy nhiên, một điều cần lưu ý là khoản vay được hoàn trả sẽ được đưa vào và không được sắp xếp.

Vì vậy, điều chúng ta có thể làm ở đây là trước khi gọi là cốt truyện, chúng ta sẽ tiếp tục và nói.

Sắp xếp các giá trị đó, sắp xếp các giá trị gạch dưới, bạn vẽ biểu đồ đó và bạn sẽ có phiên bản được sắp xếp tại đây,

tuy nhiên, điều hợp lý là khoản vay được hoàn trả có mối tương quan hoàn hảo với khoản vay được thay thế, được hoàn trả.

Vì vậy chúng ta sẽ tiếp tục và thả xuống.

Khoản vay đã được hoàn trả.

Và tôi không cần chỉ định các trục, vì đây thực sự là một chuỗi từ khung dữ liệu tương quan.

Chạy nó và bây giờ bạn sẽ nhận được cốt truyện giống hệt ở đây, vì vậy bạn có thể thấy rằng lãi suất đã

về cơ bản là mối tương quan nghịch cao nhất với việc liệu ai đó có trả lại khoản vay của họ hay không,

loại nào có ý nghĩa.

Có thể nếu bạn có lãi suất cực cao, bạn sẽ khó trả được khoản vay đó hơn.

OK, vậy là kết thúc phần đầu tiên của bài tập, nơi chúng ta chỉ khám phá dữ liệu và thực hiện

trực quan hóa.

Tôi thực sự khuyến khích bạn không chỉ thực hiện các hình dung ở đây trong sổ ghi chép mà còn chơi thử

với dữ liệu của chính bạn và xem liệu bạn có thể trả lời bất kỳ câu hỏi nào dựa trên kiến thức về miền của mình không

và dựa trên những tính năng nào bạn thấy thú vị.

Cảm ơn.

Và tôi sẽ gặp bạn ở bài giảng tiếp theo nơi chúng ta tiếp tục với Phần hai về tiền xử lý dữ liệu.

Tôi sẽ gặp bạn ở đó.