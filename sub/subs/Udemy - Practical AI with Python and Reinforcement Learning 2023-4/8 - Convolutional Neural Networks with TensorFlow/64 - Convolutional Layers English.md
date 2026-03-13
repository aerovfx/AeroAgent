# 64 - Lớp tích chập tiếng Anh

---

Chào mừng trở lại, mọi người.

Bây giờ chúng ta đã hiểu cách hoạt động của Col và các bộ lọc hình ảnh, hãy tiếp tục và xem chúng đóng vai trò như thế nào

trong phần lớp tích chập của mạng lưới thần kinh tích chập.

Hãy nhớ lại rằng việc chạy một mạng lưới thần kinh nhân tạo chỉ là một mạng lưới thần kinh chuyển tiếp nguồn cấp dữ liệu được kết nối đầy đủ

mạng cho trạng thái Emna thực sự mang lại một mạng có độ chính xác tương đối tốt.

Tuy nhiên, có một số vấn đề khi luôn sử dụng mô hình phụ cho dữ liệu hình ảnh.

Vì vậy, nếu chúng ta luôn sử dụng mạng lưới thần kinh nhân tạo, thì chỉ là các mạng bình thường, được kết nối đầy đủ cho

dữ liệu hình ảnh, chúng ta sẽ thu được một lượng lớn thông số.

Hãy nhớ lại rằng khi chúng tôi thực sự kiểm tra số lượng tham số cho mạng của mình trên tập dữ liệu đại chúng, chúng tôi đã có

hơn 100000 tham số và đó là cho các hình ảnh nhỏ 28 x 28, 28 x 28.

Hình ảnh pixel thực sự rất nhỏ so với hình ảnh mà bạn đã quen với cuộc sống bình thường.

Ví dụ: bạn biết rằng độ phân giải của bạn trên màn hình điều khiển bình thường có thể sâu khoảng 10.

Đó là 10 80 pixel hoặc một nghìn tám mươi pixel.

Nó lớn hơn rất nhiều so với 28 x 28.

Vì vậy, nếu chúng ta cố gắng mở rộng mạng lưới thần kinh nhân tạo thành những hình ảnh có kích thước bình thường, bạn sẽ kết thúc

không chỉ có 100000 tham số mà còn có hàng triệu tham số vì thời gian đào tạo sẽ kéo dài mãi mãi.

Vấn đề khác với mạng nơ-ron nhân tạo là việc chúng ta phải làm phẳng dữ liệu trước đó.

thực sự đưa nó vào mạng.

Và nếu chúng ta làm phẳng dữ liệu, về cơ bản chúng ta sẽ mất tất cả thông tin hai chiều.

Và vấn đề còn lại là nó thực sự chỉ hoạt động tốt khi hình ảnh cực kỳ giống nhau.

Và nếu bạn nhìn kỹ hơn vào tập dữ liệu M này, bạn sẽ nhận thấy rằng về cơ bản tất cả các con số

được căn giữa trong hình ảnh.

Chúng tôi muốn các mạng thần kinh tích chập của chúng tôi hoặc chỉ các mạng của chúng tôi nói chung có thể nhận ra một

số bất kể nó ở đâu trong hình ảnh.

Một mạng lưới thần kinh nhân tạo thực sự sẽ không thể làm được điều đó.

Nếu bạn chụp ảnh một chữ số viết tay có kích thước 20 x 20 nhưng chữ số đó không nằm ở giữa, có thể

nó bắt đầu từ bên phải và đưa nó vào mạng lưới thần kinh nhân tạo mà chúng tôi đã đào tạo,

bạn thực sự sẽ không nhận được kết quả tốt và rất có thể mạng sẽ không thể hiểu được

những gì nó thực sự đang nhìn vào.

Vì vậy, tập dữ liệu khối thực sự đặc biệt vì tất cả các số đều được căn giữa một cách hoàn hảo và chúng thực sự

hình ảnh nhỏ 20 x 20.

Và đó là lý do tại sao mạng lưới thần kinh nhân tạo thực sự có thể hoạt động tốt ở đó.

Nhưng sau này chúng ta sẽ thấy rằng mạng này sẽ không khái quát hóa tốt với những hình ảnh có kích thước bình thường, đặc biệt là

khi thứ chúng ta đang tìm kiếm có thể ở bất kỳ đâu trong hình ảnh.

Vì vậy chúng ta có rất nhiều hạn chế đối với mạng lưới thần kinh nhân tạo.

Giờ đây, CNN hoặc mạng nơ ron tích chập có thể sử dụng cái được gọi là lớp tích chập để giúp giảm bớt

rất nhiều vấn đề trong số này, một lớp chập được tạo ra.

Khi chúng ta áp dụng nhiều bộ lọc hình ảnh cho hình ảnh đầu vào, lớp đó sẽ được huấn luyện để hình

ra các giá trị chờ bộ lọc tốt nhất.

CNN cũng giúp giảm bớt các tham số bằng cách tập trung vào kết nối cục bộ và chúng ta sẽ thực sự thấy một ví dụ

của các kết nối cục bộ này.

Vì vậy, trong mạng nơ-ron tích chập, đặc biệt là trong lớp tích chập này, không phải tất cả các nơ-ron sẽ

được kết nối đầy đủ.

Thay vào đó, các nơ-ron chỉ được kết nối với một tập hợp con các nơ-ron cục bộ ở lớp tiếp theo, và những nơ-ron này thực sự

cuối cùng trở thành bộ lọc.

Vì vậy, hãy hiểu kết nối cục bộ này và kết nối của nó với các bộ lọc bằng cách bắt đầu bằng một cách rất đơn giản,

ví dụ một chiều, sau đó chúng tôi sẽ mở rộng ví dụ này sang đầu vào hai chiều cho thang độ xám

hình ảnh và sau đó chuyển sang đầu vào tensor ba chiều cho hình ảnh màu.

Vì vậy, ở đây chúng ta chỉ có một mạng lưới thần kinh nhân tạo bình thường mà chúng ta thấy ở phía bên trái, chúng ta có

một số loại đầu vào và sau đó nó được kết nối hoàn toàn với tất cả các nơ-ron ở lớp tiếp theo và sau đó

sẽ tiếp tục trên toàn mạng.

Vì điều này được kết nối đầy đủ nên có rất nhiều tham số đã được quyết định sẽ diễn ra

là một vấn đề đối với những hình ảnh thực sự lớn hoặc thậm chí chỉ là những hình ảnh có kích thước bình thường do quá trình đào tạo, thời gian

để tìm ra tất cả các thông số đó.

Vậy làm cách nào để giảm số lượng tham số này?

Vâng, một lớp tích chập, chức năng của nó là tập trung vào các kết nối cục bộ.

Bây giờ hãy lưu ý rằng các nơ-ron chỉ được kết nối với một nơ-ron cục bộ ở lớp tiếp theo.

Chúng không được kết nối với mọi nơ-ron đơn lẻ khác.

Vì vậy, ở đây chúng ta có những kết nối cục bộ này và điều này chỉ được hiển thị trên một chiều.

Sau này, chúng tôi sẽ mở rộng điều này thành hai chiều.

Nhưng ở đây chúng ta có thể thấy rằng chúng ta thực sự có một bộ lọc, vậy điều sắp xảy ra là do điều này

về cơ bản là một lớp tích chập có kết nối cục bộ, những kết nối cục bộ này cuối cùng sẽ tạo ra

bộ lọc này.

Và bản thân mạng sẽ tìm ra đâu là điều tốt nhất để chờ đợi cho bộ lọc này.

Và vì vậy điều chúng tôi có thể làm là có thể thêm một bộ lọc khác và khi bạn đào tạo, mạng thần kinh tích chập của bạn

mạng, bạn thực sự có quyền quyết định số lượng bộ lọc bạn muốn áp dụng cho hình ảnh này và về cơ bản

để mạng tìm hiểu cách chờ đợi tốt nhất cho bộ lọc.

Vì vậy, trước đây chúng ta đã thấy rằng các bộ lọc thực sự phổ biến, chẳng hạn như bộ lọc mờ hoặc bộ lọc cạnh, những trọng số đó

đã được biết đến.

Nhưng nếu bạn đang làm việc với dữ liệu nhận dạng khuôn mặt và bạn đang cố gắng tìm hiểu xem điều gì

các giá trị bộ lọc sẽ thực sự tốt trong việc nhận dạng lông mày, nhưng bản thân bạn có thể sẽ không làm được điều đó.

để có thể tìm ra những con số đó.

Nhưng mạng lưới thần kinh tích chập, ở đâu đó, có thể sẽ tìm ra được

một số bộ lọc có tác dụng tốt trong việc nhận dạng một số thành phần của khuôn mặt đó.

Hãy nhớ rằng, có thể nói, sẽ rất khó để thực sự mở ra mạng lưới thần kinh và

quyết định xem mỗi bộ lọc thực sự nhìn vào những gì trên hình ảnh khuôn mặt đó.

Nhưng có khả năng là các bộ lọc sẽ bắt đầu nhận ra các mẫu ngày càng cao hơn liên quan đến khuôn mặt

như mũi, tai, miệng của lông mày, v.v..

Và chúng ta sẽ nói về việc diễn giải các bộ lọc của mạng và hình dung điều đó ở phần sau của khóa học.

Nhưng ở đây chúng ta có thể hiểu rằng thông qua các kết nối cục bộ này trong mạng lưới thần kinh tích chập này,

sau đó chúng ta có thể có nhiều bộ lọc xếp chồng lên nhau.

Đó là một ví dụ đơn giản, một chiều về tích chập, nhưng hãy nhớ lại những hình ảnh thang độ xám này,

đó là hai chiều.

Và chúng tôi đã đề cập rằng chúng tôi muốn lưu giữ thông tin quan hệ hai chiều trong mô hình tích chập

lớp.

Và đây là lúc kiến ​​thức của chúng ta về các bộ lọc hình ảnh hoặc Col hình ảnh đó phát huy tác dụng.

Vì vậy bây giờ chúng ta hãy mở rộng điều này thành hai chiều.

Và nó thực sự khá đơn giản ở đây.

Chúng tôi có một hình ảnh đầu vào.

Đó là một hình ảnh thực sự đơn giản.

Nó chỉ có kích thước ba x bốn pixel.

Và hãy nhớ lại rằng vì đây là hình ảnh thang độ xám nên về cơ bản mỗi giá trị nằm trong khoảng từ 0

và một hoặc tùy thuộc vào cách nó được chuẩn hóa giữa âm một và một hoặc không và hai, năm mươi lăm là

một giá trị pixel thực sự phổ biến khác.

Nhưng ý tưởng chính ở đây là đây là những pixel và về mặt kỹ thuật chúng chỉ là những con số hoặc ma trận.

Chúng tôi đang cho nó ăn ở đây.

Đây là hình ảnh của chúng tôi, thực sự rất đơn giản tại sao hình dạng chúng tôi hiển thị ở đây với màu tối hơn

số không và số nhẹ hơn.

Sau đó, điều chúng ta sắp làm với hình ảnh này là nhớ lại rằng chúng ta có bộ lọc này mà về cơ bản chúng ta có thể

quét qua hình ảnh và những điều khác cần nhớ là nếu muốn, chúng ta có thể đệm hình ảnh

và chúng ta cũng có thể chọn độ dài sải chân.

Vì vậy, những gì chúng ta sắp làm ở đây là ở dạng hai chiều.

Chúng ta sẽ tập trung vào các kết nối được bản địa hóa bằng quy trình lọc này và nhắc lại rằng chúng ta có thể

chỉnh sửa kích thước sải chân của chúng tôi.

Và vì vậy cuối cùng chúng tôi kết thúc việc làm ở đây là chúng tôi có được các kết nối cục bộ này từ những hình ảnh đầu vào này

hoặc các đặc điểm đầu vào của các giá trị pixel này và chỉ kết nối chúng với một số tập hợp con nơ-ron nhất định trong

lớp tiếp theo.

Và bạn sẽ nhận thấy rằng về cơ bản những gì chúng tôi đang tạo ở đây là một bộ lọc và sau đó nó phụ thuộc vào mạng

để tìm ra trọng số cần áp dụng cho bộ lọc này trong quá trình huấn luyện nhằm phân loại chính xác

những hình ảnh.

Và nếu muốn, bạn luôn có thể thực hiện việc này với một bộ bộ lọc khác để có thể thêm bao nhiêu bộ lọc

như bạn muốn ở đây.

Vì vậy, bạn thực hiện lại quá trình quét tương tự.

Và ở đây chúng ta có ba bộ lọc cho hình ảnh đầu vào này, nhưng không có gì lạ khi thấy hàng chục hoặc hàng trăm bộ lọc

bộ lọc tùy thuộc vào mức độ phức tạp của nội dung bạn thực sự đang cố gắng phân loại, cũng như số lượng

các loại đối tượng khác nhau đang cố gắng phân loại.

Vì vậy, nếu chúng ta xếp chồng các bộ lọc này lại với nhau, thì đó là thứ bắt đầu tạo ra lớp chập của chúng ta.

Về cơ bản, đây là tập hợp các bộ lọc dành cho mạng tích chập để tìm ra trọng số phù hợp.

Và mỗi bộ lọc này chỉ có các kết nối cục bộ vì chúng tôi hiểu hình ảnh, đại tá,

có liên quan đến hình ảnh đó.

Bây giờ, hãy nhớ rằng, về mặt kỹ thuật, đó chỉ là một ví dụ về hình ảnh thang độ xám, nhưng còn màu sắc thì sao?

hình ảnh?

Hình ảnh màu có thể được coi là Tensas ba chiều bao gồm các kênh màu đỏ, lục và lam.

Việc trộn màu phụ gia cho phép chúng ta thể hiện nhiều loại màu khác nhau bằng cách kết hợp các màu khác nhau.

số lượng màu đỏ, xanh lá cây và xanh dương.

Như vậy chắc hẳn bạn đã từng nghe đến mã màu, mã màu đỏ, lục, lam.

Và ý tưởng đằng sau đó là thông qua sự kết hợp của màu đỏ, xanh lá cây và xanh lam, bạn có thể tạo bất kỳ phiên bản nào

bất kỳ màu nào.

Bây giờ, hãy nhớ rằng, có những giới hạn cho việc này.

RGB không thể tạo ra mọi màu có sẵn nhưng nó tạo ra nhiều loại màu khác nhau

chúng ta có thể thấy ở quy mô con người.

Vì vậy, bạn sẽ không nhìn thấy những thứ như tia cực tím hoặc tia hồng ngoại.

Nhưng RGB cho phép bạn tạo ra thứ được gọi ở đây là dải màu này.

Bây giờ, mỗi kênh màu sẽ có các giá trị cường độ và có thể bạn đã thấy điều này nếu bạn từng

từng làm việc với việc thể hiện các pixel màu và phần mềm khác của thanh trượt RGB.

Vì vậy, ở đây chúng ta có các thanh trượt RGB và về cơ bản chúng ta chọn một số giá trị từ 0 đến 255 cho màu đỏ,

xanh lá cây và xanh dương.

Và về cơ bản, bạn trộn chúng lại với nhau như thể có sơn và bạn sẽ có được một loại màu nào đó.

Ý tưởng chính là những màu này về cơ bản có thể được biểu diễn dưới dạng kết hợp giữa màu đỏ, xanh lục.

và màu xanh.

Vậy điều đó có ý nghĩa gì đối với hình ảnh thực tế của chúng ta?

Vì vậy, ở đây chúng ta có thể xem một ví dụ về việc chia một hình ảnh đủ màu thành các kênh màu của nó.

Vì vậy, đối với một hình ảnh một màu, chúng ta có ba chiều thực tế này.

Chúng ta có chiều cao tương ứng với thứ mà chúng ta đã quen thuộc.

Nhưng đối với mỗi kênh màu, một kênh màu đỏ, một kênh màu xanh lá cây và một kênh màu xanh lam, chúng tôi

thực sự sẽ có một mảng pixel riêng biệt.

Điều này có nghĩa là khi bạn thực sự đọc một hình ảnh và kiểm tra hình dạng của nó, nó sẽ trông giống cái gì đó

như thế này, bạn sẽ có thể có 12, 80 x 7, 20 x 3.

Vì vậy, điều đó có nghĩa là một hình ảnh có 12, 80 pixel với chiều cao 720 pixel và sau đó là ba kênh màu.

Và hãy nhớ rằng mỗi kênh màu này về cơ bản là nếu bạn chỉ lấy một trong số chúng,

nó trông giống như một hình ảnh thang độ xám.

Nó chỉ là các giá trị giữa 0 và 1 hoặc 0 hai hoặc 55 hoặc âm một và một.

Chúng chỉ đại diện cho cường độ của màu cụ thể đó.

Vì vậy, chúng ta có thể thấy ở đây cường độ của màu đỏ, lục và lam.

Và khi bạn kết hợp những cường độ đó, như chúng ta đã thảo luận trước đây, bạn sẽ tạo ra

sự pha trộn của các màu sắc, tạo ra hình ảnh màu này.

Vì vậy, một lần nữa, chúng ta coi đây là chiều cao, chiều rộng và sau đó là ba kênh màu và nhớ lại điều này

chỉ dành cho một hình ảnh duy nhất.

Vì vậy, bây giờ một hình ảnh thực sự là tensor ba chiều này.

Bạn cũng nên nhớ rằng máy tính thực sự sẽ biết liệu một kênh đã được đọc hay chưa, nó chỉ biết

rằng hiện nay có ba kênh cường độ.

Vì vậy, bạn cũng nên ghi nhớ điều đó trong trường hợp hình ảnh của bạn có mã hóa màu khác nhau.

Một số chương trình thực sự sẽ mã hóa thay vì màu đỏ, xanh lá cây, xanh lam, chúng sẽ mã hóa thành màu xanh lam, xanh lục,

màu đỏ.

Điều đó thực sự không quan trọng lắm đối với trường hợp sử dụng mạng nơ ron tích chập của chúng ta bởi vì

mạng không thực sự quan tâm đến thứ tự màu sắc được đưa vào.

Nó chỉ quan tâm rằng có ba kênh cường độ.

Bây giờ, câu hỏi được đặt ra, chúng ta vừa biết cách thực hiện phép tích chập trên mảng một chiều, sau đó

chúng ta đã biết cách thực hiện nó trên một mảng hai chiều, cách chúng ta thực hiện tích chập trên màu này

hình ảnh vì nó là một tensor ba chiều?

Vì vậy, chúng tôi thực sự kết thúc với một bộ lọc ba chiều với các giá trị cho từng kênh màu.

Về cơ bản, bộ lọc này hiện có ba chiều.

Chúng tôi có chiều cao và chiều rộng thực tế của bộ lọc đó được hiển thị là ba x ba, nhưng sau đó chúng tôi có một phiên bản

cho từng chiều, cho các kênh màu.

Vì vậy, có một cho màu đỏ, một cho màu xanh lá cây và một cho màu xanh lam.

Và cũng như trước đây, chúng ta có thể có bao nhiêu bộ lọc tùy thích để có thể tạo một bộ lọc khác.

Và một lần nữa, bộ lọc này là ba chiều.

Nó có một hạt nhân hình ảnh nhỏ cho mỗi kênh màu.

Vì vậy, một cho màu đỏ, một cho màu xanh lá cây và một cho màu xanh lam.

Và chúng ta có thể tiếp tục bổ sung thêm các bộ lọc này.

Vì vậy, bây giờ bạn nên coi các bộ lọc này cho những hình ảnh màu này là ba chiều trở lên.

trong khóa học sẽ thực sự mở rộng từ hình ảnh thang độ xám và chúng tôi sẽ chuyển sang hình ảnh màu để chúng tôi có thể

có ý tưởng làm việc với chiều dữ liệu bổ sung này.

Hiện nay, tai xoắn thường được đưa vào một lớp chập khác nên không có gì lạ khi thấy

một lớp chập được xếp chồng trực tiếp và đưa vào một lớp chập khác rồi xếp chồng lên nhau

và được đưa vào một lớp chập khác.

Và điều thực sự thú vị ở đây là nó cho phép mạng khám phá các mẫu bên trong các mẫu, thường là

với độ phức tạp cao hơn cho các lớp tích chập sau này.

Bây giờ, chúng ta đã học được rất nhiều điều và chúng ta có ba chủ đề cuối cùng cần đề cập trước khi viết mã cho riêng mình.

mạng nơ ron tích chập, và đó là lớp tổng hợp còn được gọi là lấy mẫu xuống hoặc lớp phụ

lớp lấy mẫu

Khi bạn hiểu cách lớp kéo hoạt động cùng với lớp chập, thì chúng ta có tất cả

những phần chúng ta cần để thực sự tạo ra mạng lưới thần kinh tích chập của riêng mình và sau đó chúng ta sẽ xem lại

vấn đề tập dữ liệu này.

Vì vậy, trong bài giảng tiếp theo, chúng ta hãy đi vào phần thảo luận về các lớp gộp.

Tôi sẽ gặp bạn ở đó.