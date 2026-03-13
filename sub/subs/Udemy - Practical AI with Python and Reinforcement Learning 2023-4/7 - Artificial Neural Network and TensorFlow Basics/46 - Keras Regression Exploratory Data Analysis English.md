# 46 - Phân tích dữ liệu khám phá hồi quy Keras

---

Chào mừng trở lại, mọi người.

Trong loạt bài giảng tiếp theo, chúng ta sẽ viết mã cùng với một dự án dựa trên hồi quy trong đó

dựa trên tập dữ liệu về các đặc điểm nhà ở khác nhau, chúng tôi sẽ cố gắng dự đoán mức giá

một ngôi nhà nên bán nó.

Vì vậy, dựa trên những yếu tố như số phòng ngủ, không có phòng tắm, diện tích, v.v., chúng tôi sẽ cố gắng

xây dựng một mô hình deep learning có thể dự đoán giá một ngôi nhà.

Vì vậy, một phần quan trọng của việc này là phân tích dữ liệu mang tính khám phá cũng như kỹ thuật tính năng, đó là những gì

sẽ tập trung vào phần một.

Hãy đi tới một cuốn sổ tay và bắt đầu.

Tôi đang ở đây với một cuốn sổ tay và tôi đã nhập tên của Panda, Pi, Matplotlib và Seabourne làm

ghi chú nhanh.

Nếu bạn vào thư mục Anand của chúng tôi, cuốn sổ tương ứng với bài giảng này hoặc một loạt bài giảng

được gọi là hồi quy Keris.

Nó nằm ngay sau cú pháp cơ bản.

Và nếu bạn mở nó lên, bạn sẽ có thể cuộn xuống và xem mô tả đầy đủ về tất cả các

cột đặc trưng.

Vì vậy, một số cột tính năng này có thể không rõ ràng cột tính năng thực tế là gì

cho.

Vì vậy, ở đây chúng tôi có các định nghĩa thực tế trong trường hợp bạn quan tâm đến nó.

Vì vậy, chúng ta sẽ quay lại đây và tải lên.

Dữ liệu của chúng tôi sẽ cho biết D.F. tương đương với PDCA.

Đọc CSFI.

Và dữ liệu của chúng tôi nằm bên dưới thư mục dữ liệu của chúng tôi.

Vì vậy, nếu bạn quay lại một thư mục và thư mục này có tên là Kacie, hãy gạch dưới dữ liệu như thế nào.

Đó là CSFI, hãy tiếp tục và đọc nó.

Và một lần nữa, nếu bạn xem sổ ghi chép hồi quy của chúng tôi, chúng tôi thực sự đang sử dụng dữ liệu này.

Vì vậy, đây là tập dữ liệu thực từ liên kết Kagle.

Vì vậy, bạn có thể kiểm tra liên kết thực tế ngay tại đây.

Nhưng về cơ bản đây là dữ liệu lịch sử về giá bán nhà ở Quận King, Hoa Kỳ và King

Quận về cơ bản là nơi có Seattle.

Vì vậy, chúng ta sẽ quay lại sổ ghi chép của mình và chúng ta sẽ khám phá dữ liệu này một chút bằng cách sử dụng

một số kỹ thuật trực quan.

Vì vậy, trước tiên, hãy xem liệu chúng ta có thiếu dữ liệu nào không.

Chúng tôi sẽ Sadaf là vô giá trị một số.

Và điều này trước hết là D.F. là vô giá trị.

Điều đó chỉ trả về giá trị đúng hoặc sai nếu có gì đó không có giá trị.

Vì vậy, nếu thiếu một cái gì đó, nó sẽ quay trở lại.

ĐÚNG VẬY.

Và sau đó tôi thực sự có thể tổng hợp số này trên mỗi cột và nó sẽ coi số giả là số 0 và số trew là số 1.

Và bằng cách đó, chúng tôi thực sự có thể cộng thêm số lượng điểm dữ liệu còn thiếu.

Và đối với tập dữ liệu cụ thể này, chúng tôi thực sự không có dữ liệu nào bị thiếu, điều này có ý nghĩa nếu một

Ngôi nhà trước đây đã được bán, không phải là bạn không biết ngôi nhà có bao nhiêu phòng ngủ trước đây

bạn đã bán nó.

Vì vậy, đối với tập dữ liệu cụ thể này, việc không thiếu dữ liệu là điều hợp lý.

Ở phần sau của khóa học, chúng tôi sẽ chỉ cho bạn cách xử lý tập dữ liệu bị thiếu

dữ liệu.

Và một điều khác tôi muốn làm sau khi bạn kiểm tra xem có bao nhiêu dữ liệu bị thiếu là mô tả nhanh

cuộc gọi sẽ cung cấp cho bạn phân tích thống kê về tập dữ liệu của bạn.

Và cá nhân tôi muốn chuyển đổi điều này để tôi có thể thấy được phương tiện thống kê và độ lệch tối thiểu

giá trị phần trăm, v.v., cho tất cả các cột.

Bây giờ, một số trong số này thực sự không có ý nghĩa gì cả.

Vì vậy, sau này, nếu bạn thực sự nhìn thấy phần đầu của khung dữ liệu.

Bạn sẽ nhận thấy rằng một trong số chúng chỉ là một I.D. duy nhất, vì vậy đây là một loại I.D. duy nhất. để bán.

Vì vậy, thực sự không có ý nghĩa gì khi xem xét bất kỳ ý nghĩa nào đối với giá trị trung bình của ID.

Những thứ khác của chúng tôi, như giá trung bình, có thể thực sự quan trọng.

Vậy chúng ta có thể thấy ở đây chúng ta có ký hiệu khoa học này, về cơ bản có nghĩa là năm phẩy bốn lần

mười lũy thừa của năm.

Vì vậy, về cơ bản hãy thêm vào năm số không.

Được rồi, vậy là chúng ta đã có tất cả thông tin đó.

Sẽ hơi khó khăn nếu chỉ đọc bảng này và hiểu kỹ nó.

Hãy bắt đầu thực sự mô tả nó thông qua trực quan hóa, sử dụng Seabourne và matplotlib và tất cả những thứ đó.

các kỹ năng chúng tôi đã học được trong phần khóa học về sự cố trực quan hóa dữ liệu.

Vì vậy, điều tôi có thể làm, đặc biệt đối với các nhãn liên tục, chỉ là phân phối thực tế

nhãn.

Vì vậy, hãy thực hiện phân phối, về cơ bản là biểu đồ.

Và một điều khác tôi có thể làm là làm cái này lớn hơn một chút.

Bằng cách gọi Kielty là con số đó.

Và giả sử cài đặt các bản sửa lỗi.

Sáu giờ mười, vì vậy tôi sẽ tiếp tục chạy nó và tôi sẽ thấy bản phân phối này.

Vì vậy, hãy chú ý ở đây, có vẻ như hầu hết các ngôi nhà của chúng ta đang rơi vào khoảng từ 0 đến có thể khoảng

một phẩy năm triệu đô la.

Và chúng ta có thể có những ngoại lệ cực đoan này cho những ngôi nhà thực sự đắt tiền.

Và thực sự có thể hợp lý khi loại bỏ những ngoại lệ đó trong phân tích của chúng tôi nếu chúng chỉ là một vài điểm

điều đó rất cực đoan.

Và vì vậy về cơ bản chúng ta có thể xây dựng một mô hình dự đoán thực tế giá một ngôi nhà nếu nó được dự kiến

giá trị nằm ở khoảng giữa, chẳng hạn, từ 0 đến hai triệu đô la.

Và dường như sẽ không có nhiều ngôi nhà trên thị trường có giá trị cao hơn, chúng ta hãy

nói, ba triệu.

Vì vậy, đó là điều cần ghi nhớ ở đây, đặc biệt là khi áp dụng điều này vào tình huống thực tế.

May, chúng tôi đang cố gắng xây dựng mô hình cho một đại lý bất động sản, vì thực sự không có nhiều nhà ở đó

trên thị trường đắt đỏ như vậy, có thể thực sự không hữu ích nếu có mô hình tàu hỏa của chúng tôi

về những ngoại lệ cực đoan này.

Bây giờ, chúng ta có thể tiếp tục và thực hiện phân tích tương tự về các tính năng khác nhau.

Vì vậy, ví dụ, đối với những dữ liệu được phân loại như số phòng ngủ, là loại liên tục, nhưng

bạn thực sự không thể có một đến năm phòng ngủ, bạn thực sự có thể có bốn phòng tắm đó.

Nhưng đối với những đứa trẻ trong phòng ngủ, chúng tôi có trong tập dữ liệu của mình.

Chúng ta thực sự không có một phẩy năm hay hai phẩy năm.

Vì vậy chúng ta có thể coi đây là một âm mưu cắm trại.

Vì vậy, tôi có thể nói điều gì đó như hãy tiếp tục đếm số phòng ngủ rồi vẽ sơ đồ ra.

Và ở đây tôi có thể thấy những gì thực sự trông gần giống như một sự phân phối tương tự trong đó đại đa số

trong số tất cả những ngôi nhà này có khoảng từ hai đến năm phòng ngủ.

Và có vẻ như có một dinh thự khổng lồ ở đâu đó trong khu vực này có 33 phòng ngủ.

Vì vậy, có vẻ như từ tám đến ba mươi ba, có lẽ chỉ có một phiên bản tương tự, mà

đó là lý do họ xuất hiện ở đây.

Nhưng chúng tôi thực sự không thể nhìn thấy quầy bar đó vì không, số phòng ngủ còn lại thực sự lên tới hàng nghìn.

Vì vậy, thật hợp lý khi bạn không thực sự nhìn thấy màu sắc cho một thứ nhỏ như một.

Bây giờ, điều thú vị là chỉ cần so sánh nhãn của bạn với một số tính năng mà bạn cho là có mức độ cao.

sự tương quan.

Và điều bạn không thể làm là bạn có thể nói dữ liệu từ đó.

Tương quan, chạy nó và sau đó bạn có thể bắt đầu thấy những gì thực sự tương quan với nhãn của bạn và tắt

về điều này, tôi sẽ tiếp tục và lấy nhãn của mình.

Hãy chỉ nói giá.

Chạy nó và tiếp tục sắp xếp các giá trị này, chúng ta sẽ nói sắp xếp.

Gạch dưới các giá trị.

Và ở đây tôi có thể thấy những thứ có mối tương quan cao, tương quan tích cực hoặc tương quan tiêu cực cao,

rõ ràng giá cả sẽ tương quan hoàn hảo với giá cả, nhưng có vẻ như mét vuông của

không gian sống có mối tương quan rất cao với giá thực tế của căn nhà.

Và điều tôi khuyên bạn nên làm là khám phá các tính năng có mối tương quan cao với nhãn của bạn thông qua biểu đồ phân tán.

Vì vậy, ví dụ, tôi có thể nói S.A.S..

Biểu đồ phân tán.

Và so sánh giá cả.

Với feet vuông không gian sống của tôi và nói rằng dữ liệu bằng D.F., tôi sẽ tiếp tục và chạy dữ liệu đó.

Và tôi có thể thấy ở đây một mối quan hệ tuyến tính rất mạnh mẽ.

Và nếu tôi cần mở rộng điều này ra, hãy lưu ý rằng có vẻ như giá đang chồng chéo.

Tôi có thể nói hình Pulte và chỉ cho nó thêm một chút không gian bằng cách nói kích thước này bằng một cái gì đó

như 10 x 5.

Và điều đó mang lại cho chúng ta một không gian nhỏ xinh ở đây, được rồi, một lần nữa, tôi luôn khuyên bạn nên kiểm tra các mối tương quan

giữa các tính năng khác nhau và nhãn thực tế của bạn, sau đó khám phá những mối tương quan đó thông qua

hoặc khám phá những tính năng đó thông qua một số hình thức trực quan hóa dữ liệu.

Vì vậy, ví dụ, nếu chúng ta nhìn vào đây, có vẻ như phòng ngủ cũng có mối tương quan tích cực nào đó

cũng như phòng tắm.

Và bạn cũng có thể đếm các ô của những ô đó theo giá hoặc thậm chí các ô hình hộp để xem sự phân bổ,

ví dụ như đó là một ô hộp.

Trong đó X là số phòng ngủ.

Tại sao lại là giá và dữ liệu của tôi là D.F., tôi sẽ tiếp tục và làm cho nó lớn hơn một chút.

Bằng cách gọi hình ở đây, hãy tiếp tục và làm chiếc lều này lúc sáu giờ hoặc thứ gì đó tương tự, và đây là gì

đang cho tôi thấy sự phân bố giá mỗi phòng ngủ.

Vì vậy, ví dụ, tôi có thể thấy rằng có khá nhiều sự khác biệt về số lượng phòng ngủ, từ ba phòng ngủ trở lên.

và bảy.

Và điều đó cũng có ý nghĩa, bởi vì nếu chúng ta nhìn vào biểu đồ đếm từ trước, nó trông giống như

phần lớn các ngôi nhà có cựu chiến binh có thể từ ba đến bảy người.

Vì vậy, cũng dễ hiểu khi có khá nhiều mức giá khác nhau ở đó.

Vì vậy, không có cách nào đúng hay sai để thực hiện phân tích dữ liệu khám phá, vì vậy hãy tiếp tục khám phá

dữ liệu này được đặt thông qua bất kỳ tính năng nào khác mà bạn quan tâm, thực hiện vẽ sơ đồ hộp hoặc đếm

lô.

Tuy nhiên, chúng ta nên lưu ý rằng trong tập dữ liệu của mình, nếu nhìn vào các cột, chúng ta có cái này

LAT và các tính năng dài.

Và nếu chúng ta nhìn lại các cột tính năng thực tế của mình, chúng thực sự đại diện cho vĩ độ và

kinh độ.

Vì vậy, có thể sẽ rất thú vị khi thực sự khám phá điều này bằng cách đưa nó ra ngoài và chúng ta thực sự có thể làm được một điều khá thú vị.

làm tốt việc này chỉ dành cho biểu đồ phân tán đơn giản.

Bây giờ, hãy nhớ rằng, Seabourne thực sự không có khả năng vẽ đồ thị địa lý tích hợp.

Có một chút điều đó với matplotlib, với một số plugin mở rộng trong thư viện.

Nhưng thực ra chúng ta sẽ không tập trung vào việc cố gắng vẽ những điểm này lên trên bản đồ thế giới thực.

Thay vào đó, chúng ta thực sự có thể thu được rất nhiều thông tin với một chút kiến thức sơ lược về những gì King

Quận thực sự trông như thế nào, kết hợp với lệnh gọi biểu đồ phân tán đơn giản.

Vì vậy, trước tiên chúng ta hãy xem sự phân bổ giá theo vĩ độ và kinh độ.

Vì vậy, tôi sẽ quay lại sổ ghi chép của mình ở đây và tất cả những gì tôi sắp làm.

nhìn thấy?

Giá của tôi trông như thế nào?

Vì vậy, chúng ta sẽ có giá trên trục x.

Và sau đó có một loại yếu tố phân biệt nào đó chỉ dựa trên kinh độ, nên chúng ta sẽ nói dữ liệu

là D. F. và vì tôi có rất nhiều điểm trong tập dữ liệu của mình, tôi sẽ làm cho con số này lớn hơn một chút.

Chúng ta sẽ nói hình Kielty.

Và đặt kích thước cố định bằng hãy tăng 12 x 8 để tôi có thể tiếp tục chạy cái này và tôi mong đợi

về cơ bản chỉ thấy một đốm màu phẳng ở đây nếu không có sự phân biệt giá dựa trên kinh độ.

Nhưng có vẻ như có xu hướng phân bổ giá ở một kinh độ nhất định.

Vì vậy, nó trông giống như ở kinh độ, âm một đến hai phẩy hai, trông giống như một ngôi nhà đắt tiền

khu vực.

Bạn có thể thấy sự phân bổ khá rõ ràng ở đây và chúng ta có thể lặp lại điều này theo vĩ độ.

Vì vậy, chúng ta có thể tiếp tục và thay đổi từ dài sang Latt và chúng ta cũng có thể khám phá điều này, và hành vi tương tự

dường như bật lên, có vẻ như ở vĩ độ cụ thể đó, có một số khu nhà ở đắt tiền.

Và về cơ bản điều này cho chúng ta biết là nó trông giống như ở một sự kết hợp nhất định giữa vĩ độ và

kinh độ, đó có xu hướng là một khu vực đắt tiền.

Vì vậy, nếu chỉ nhìn vào bản đồ Quận King, chúng ta có thể bắt đầu nhận ra điều này.

Và điều chúng ta sắp làm là chúng ta có thể thấy ở đây về cơ bản là thành phố Seattle và chính Quận King.

Chúng ta hãy vẽ vĩ độ và kinh độ và vẽ tất cả những điểm này và sau đó chúng ta có thể tác động

sắc thái của chúng.

Vì vậy, chúng ta sẽ quay lại sổ ghi chép của mình và chúng ta có thể nói chỉ từ bằng chứng này rằng có

có lẽ là một điểm nóng nào đó trên bản đồ có những ngôi nhà đắt tiền.

Vì vậy, chúng ta sẽ quay lại đây và chúng ta sẽ làm như sau.

Tôi sẽ phân tán.

Với X là kinh độ và Y là vĩ độ của tôi và nó phải theo thứ tự này để bản đồ có thể hiển thị

có ý nghĩa, nếu không thì cuối cùng bạn sẽ lật tọa độ của bản đồ và sau đó chúng ta sẽ nói, hãy

cũng làm cho hình vẽ lớn hơn này.

Kích thước hình bằng 12 x 8, vì vậy đây chỉ là một biểu đồ phân tán đơn giản và chúng ta có được cái gì đó trông giống như

như thế này.

Và nếu chúng ta so sánh điều này với bản đồ thực tế của Quận King, chúng ta có thể thấy rằng ít nhiều họ có xu hướng

khớp với nhau.

Chúng ta có thể thấy ở đây những hình dạng của Seattle và ở đây chúng ta có thể thấy ở đây bản đồ thực sự của Quận King.

Vì vậy, hãy ghi nhớ điều đó.

Và điều chúng ta sắp làm bây giờ là tôi sẽ bắt đầu chỉnh sửa phần này để xem liệu chúng ta có thể thực sự trau dồi

tại khu nhà ở đắt đỏ này.

Và một cách chúng ta có thể làm điều này là cố gắng nói WHU bằng giá.

Và điều nó sẽ làm là nó thực sự sẽ tô màu những điểm này tối hơn hoặc nhạt hơn dựa trên

giá của họ.

Và tôi có thể bắt đầu thấy một chút ở đây về một vùng tối hơn.

Và có vẻ như nó thực sự phù hợp với ước tính ban đầu của chúng tôi về kinh độ đắt đỏ.

Vì vậy, hãy chú ý đến âm một đến hai điểm hai, nếu tôi tiếp tục đi lên, cuối cùng tôi sẽ chạm tới những điểm tối hơn này.

Tương tự ở khoảng 47,6, gần như những gì chúng tôi mong đợi dựa trên bản đồ vĩ độ này.

Tuy nhiên, có vẻ như tôi không nhận được độ chuyển màu như mong muốn và đó là vì

về những ngôi nhà ngoại lệ thực sự đắt tiền đó, cũng như thực tế là chúng ta vẫn có lợi thế rõ rệt ở đây.

Vì vậy, hãy xem liệu chúng ta có thể thực sự làm sạch bản đồ này một chút bằng cách loại bỏ một số ngoại lệ này hay không.

Vì vậy tôi sẽ làm là tôi sẽ xem xét.

Khung dữ liệu của tôi và tôi sẽ sắp xếp các giá trị.

Dựa trên giá, tôi sẽ nói tăng dần bằng sai và hãy để tôi kiểm tra.

20 ngôi nhà đắt nhất và giá trị LOPSA nên được tìm kiếm mà chúng ta nên biết rằng trong danh sách hàng đầu của tôi

20 căn nhà, căn nhà đắt nhất bang của tôi có giá 7,7 triệu đô la.

Và khi tôi tiếp tục đi xuống, bạn sẽ nhận thấy rằng cuối cùng nó nhanh chóng giảm xuống một thứ gì đó cao hơn

hợp lý, như ba phẩy sáu.

Và nếu chúng ta nhìn vào sự phân bổ giá của những ngôi nhà này, có vẻ như tôi nên

có một mức giới hạn hợp lý ở mức ba triệu đô la vì nó gần như giống như vậy.

Ở đây chỉ có 20 căn nhà có giá trên ba triệu hoặc có thể hơn thế một chút.

Vì vậy, điều tôi có thể làm là lấy mẫu có thể là 1% cao nhất của tất cả các ngôi nhà.

Vì vậy, nếu tôi nhìn vào độ dài của khung dữ liệu của mình, hiện tại tôi có khoảng 21 nghìn ngôi nhà

trong khung dữ liệu của tôi, có nghĩa là.

Một phần trăm trong số này là hai trăm mười lăm ngôi nhà, thực tế là khá nhiều ngôi nhà.

Vì vậy, hãy tiếp tục và tạo một khung dữ liệu khác.

Và chúng tôi sẽ gọi đây là 1% không phải ở trên cùng, hoặc bạn có thể đặt tên lại là 99% ở dưới cùng,

và điều chúng ta sắp làm ở đây là lấy cùng khung dữ liệu mà chúng ta đã tạo.

D.F. sắp xếp giá trị, giá tăng dần.

Và điều tôi sẽ làm là tôi sẽ lấy mọi thứ sau 1% số ngôi nhà đứng đầu, về cơ bản là

có nghĩa là bắt đầu vị trí số nguyên chỉ mục đến 16, hãy tiếp tục và lấy mọi thứ vượt quá số đó.

Vì vậy, tất cả những gì tôi đang làm ở đây là tôi nắm lấy 99% phần đáy của các ngôi nhà, để tôi không đánh rơi

bấy nhiêu thông tin.

Tôi chỉ bỏ đi một phần trăm thông tin.

Nhưng hy vọng điều đó sẽ loại bỏ tất cả những ngôi nhà thực sự đắt tiền đó.

Và lý do là để tôi có thể có được sự phân bổ màu sắc rõ ràng hơn trên biểu đồ phân tán thực tế này,

nên chúng ta sẽ quay lại đây.

Bây giờ tôi có 99 phần trăm dưới cùng hoặc không phải phần trăm trên cùng.

Và hãy tiếp tục và thử lại lần nữa.

Tôi sẽ sao chép và dán.

Chiếc áo khoác này đây, ngoại trừ việc bây giờ dữ liệu của tôi sẽ bằng thay vì D.F..

Khung dữ liệu 1% không cao nhất đó, nên tôi có thể chạy cái này.

Và bây giờ tôi chắc chắn có thể thấy sự phân bổ màu sắc rõ ràng hơn rất nhiều và tôi thực sự có thể bắt đầu thử nghiệm.

với điều này.

Vì vậy, ví dụ, có lẽ tôi không muốn có màu cạnh.

Tôi không muốn màu trắng đó, tôi bắt đầu nói.

Mỗi màu bằng không, và vì tôi có rất nhiều điểm xếp chồng lên nhau nên cũng nói

Alpha bằng 0 điểm hai.

Và cuối cùng, tôi sẽ tiếp tục và chọn một gradient màu khác.

Vì vậy, đây là thứ hoàn toàn tùy chọn đối với bạn, nhưng tôi sẽ chọn.

Một dải màu đỏ, vàng, xanh lục, vậy đây chính là lý do tại sao LGM và nó sẽ chuyển từ đỏ sang

màu vàng sang màu xanh lá cây, và điều đó sẽ làm cho nó rõ ràng hơn một chút về ngôi nhà đắt tiền ở đâu.

Vì vậy, tôi chạy lại cái này.

Hãy chắc chắn kiểm tra Comus của bạn.

Bạn luôn có thể sao chép và dán những dòng mã này từ sổ ghi chép.

Nhưng bây giờ đây là một âm mưu hay hơn nhiều trong việc cho tôi thấy những khu vực đắt đỏ của Quận King nằm ở đâu.

Và tôi có thể thấy sự phân bổ rất rõ ràng ở đây.

Và bạn cũng sẽ nhận thấy rằng có vẻ như ở mép nước có xu hướng nhẹ hơn

điểm, điều này hợp lý vì thông thường bất động sản ven sông sẽ đắt hơn đất liền

tài sản.

Vì vậy, đây là bản đồ phân bố và biểu đồ phân tán tốt hơn nhiều so với bản đồ ban đầu của chúng tôi ở đây.

Mặc dù điều này cho chúng ta biết một chút thông tin nhưng chúng ta có thể bắt đầu thử nghiệm với thực tế

khung dữ liệu mà chúng tôi đang vẽ ra bây giờ.

Chúng tôi vẫn đang hiển thị ở đây.

Chín mươi chín phần trăm của tất cả các ngôi nhà.

Và những ngoại lệ mà chúng ta có thể giả định sẽ ở đâu đó trên bờ sông, trên này

rìa phía bắc hoặc trong khu vực đắt đỏ này của Quận King.

Rất nhiều thứ khác nhau.

Bạn có thể thử quanh đây để thực sự có được những ô trông đẹp hơn và cung cấp nhiều thông tin hơn cho người dùng.

Và những điều khác mà chúng tôi có thể chỉ cho bạn ở đây là những việc như vẽ sơ đồ hộp về việc có điều gì đó hay không

đang ở trên bờ sông.

Vì vậy, đó thực sự là một trong những tính năng của chúng tôi.

Chúng ta có thể nói.

X bằng.

Bờ sông và nói Y bằng giá.

Giữ nguyên khung dữ liệu gốc.

Và ở đây chúng ta có thể thấy sự phân bổ giá cả, cho dù chúng có ở ven sông hay không.

Vì vậy, có vẻ như nếu bạn ở bờ sông, bạn có nhiều khả năng sẽ đắt hơn, điều này một lần nữa,

loại có ý nghĩa.