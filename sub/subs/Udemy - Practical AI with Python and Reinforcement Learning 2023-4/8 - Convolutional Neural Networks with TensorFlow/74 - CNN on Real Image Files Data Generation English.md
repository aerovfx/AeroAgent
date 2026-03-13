# 74 - CNN về Tạo dữ liệu tập tin ảnh thật Tiếng Anh

---

Chào mừng mọi người quay trở lại với Phần hai về mạng nơ-ron tích chập và hình ảnh tùy chỉnh một phần là

thực sự điều chúng ta sẽ tập trung vào là vật thể đặc biệt này từ Tenzer Focus, được gọi là hình ảnh

bộ tạo dữ liệu.

Bạn sẽ có thể làm gì nếu lớp này là FITA trong thư mục trên các tệp hình ảnh thực tế của bạn

và bạn sẽ có thể thực hiện nhiều thao tác trên hình ảnh của mình rồi cung cấp những hình ảnh mới đó

vào mô hình của bạn.

Hãy tiếp tục và khám phá ý tưởng về thao tác hình ảnh cũng như chuyển từ một thư mục, những điều này

lô tập tin mới.

Hãy quay trở lại cuốn sổ mà chúng ta đã dừng lại lần trước.

Được rồi.

Hãy nhớ lại lần trước chúng ta đọc dữ liệu và tìm ra kích thước trung bình của

hình ảnh của chúng ta, bởi vì khi chúng ta đưa những hình ảnh này vào mô hình, chúng ta cần đảm bảo rằng tất cả chúng đều có

cùng kích thước.

Vì vậy, chọn kích thước trung bình có lẽ là một ý tưởng hay.

Trong trường hợp của chúng tôi, thuận tiện là vào khoảng 1 giờ 30 và 13.

Tiếp theo là thao tác hình ảnh.

Vì vậy, hãy nhớ rằng thực sự có quá nhiều dữ liệu để chúng ta có thể đọc tất cả dữ liệu này cùng một lúc.

Những tệp này lớn hơn rất nhiều so với các tệp chúng tôi đang xử lý.

Hãy nhớ lại rằng nó về cơ bản là 28 x 28.

SSAFA là ba mươi hai đến ba mươi hai.

Và ngay cả sự mở rộng nhỏ từ 28 lên hai mươi hai hình ảnh màu từ ba mươi hai đến ba mươi hai cũng là một sự mở rộng lớn

sự mở rộng về lượng dữ liệu.

Vậy đó là 28 nhân 28 là 784 điểm dữ liệu.

Và khi chúng tôi đến SSAFA, con số là ba mươi hai x ba mươi hai nhân ba một cho mỗi kênh màu.

Đó là ba nghìn bảy mươi hai.

Các tập tin của chúng tôi sẽ còn lớn hơn nữa khi chúng tôi đọc chúng.

Chúng sẽ là 130 lần, 130 lần 3.

Vậy bây giờ chúng ta đang xử lý 50.700 điểm dữ liệu.

Do đó, chúng tôi sẽ không thể cung cấp mọi thứ cùng một lúc.

Thay vào đó, chúng ta sẽ phải chọn hàng loạt hình ảnh của mình.

Ý tưởng khác mà chúng tôi muốn mô hình có thể khắc phục là nó phải đủ mạnh

để xử lý những hình ảnh khá khác so với những hình ảnh đã thấy trước đây.

Và khi chúng ta có thể làm điều đó là bằng cách thao tác và thực hiện các phép biến đổi trong hình ảnh của mình, những thứ như

xoay, thay đổi kích thước và chia tỷ lệ để bắt đầu.

Toàn bộ quá trình này sẽ được thực hiện từ luồng cảm biến thực hiện quá trình tiền xử lý.

Việc nhập hình ảnh và chúng tôi sẽ sử dụng dữ liệu hình ảnh.

Máy phát điện, cứ chạy đi.

Và sau khi nó được nhập, tôi khuyến khích bạn thực sự gọi trợ giúp về đối tượng này và nhận

một khoản vay hoặc chỉ xem tài liệu cho lớp này.

Chắc chắn có rất nhiều điều đang diễn ra ở đây.

Đây là một lớp học lớn, thậm chí còn có nhiều ví dụ đầy đủ về cách thực hiện việc này.

Nhưng điều tôi muốn bạn làm chỉ là dành chút thời gian để đọc qua phần này và xem các ví dụ khác nhau.

Bạn cũng có thể đọc về điều này trên trang tài liệu trực tuyến của nó.

Nhưng những gì chúng tôi sắp làm về cơ bản là cho bạn thấy ý tưởng chính về hình ảnh mà trình tạo dữ liệu đang thực hiện.

Vì vậy điều tôi sẽ làm là tạo một phiên bản của trình tạo hình ảnh.

Chúng ta sẽ nói hình ảnh Djenne bằng và chúng ta sẽ gọi đối tượng tạo dữ liệu hình ảnh của mình.

Nếu bạn thực hiện shift top ở đây, bạn có thể bắt đầu thấy các thông số khác nhau.

Và có rất nhiều thông số.

Sự so sánh ở đây, mọi thứ từ tính năng định tâm thông minh, cỡ mẫu, định tâm, độ sáng,

phạm vi, lật ngang, lật dọc, tiền xử lý, v.v. Vì vậy, có rất nhiều cách khác nhau

những điều chúng ta có thể làm ở đây.

Bạn cũng nên nhớ lại rằng khi chúng ta xử lý tập dữ liệu M này, chúng ta có 60000 hình ảnh và

60000 hình ảnh là rất nhiều hình ảnh.

Và đó là loại tệp rất đơn giản, về cơ bản là một hình ảnh rất đơn giản.

Lúc đó mới chỉ có hai mươi tám x hai mươi tám.

Hiện tại, chúng tôi có một nửa kích thước đó trên toàn bộ tập dữ liệu của mình.

Toàn bộ tập dữ liệu của chúng tôi có ít hơn 30000 hình ảnh.

Vì vậy, chúng tôi muốn có thể mở rộng số lượng hình ảnh mà không cần phải thu thập thêm dữ liệu.

Chúng ta không thể cứ lấy tế bào máu từ người khác được.

Vì vậy, thay vào đó, những gì chúng ta có thể làm là thực hiện những việc như chụp ảnh hiện tại và xoay chúng một cách ngẫu nhiên để có thứ gì đó

chúng ta có thể thực hiện phép xoay, phạm vi gạch dưới và đặt giá trị này bằng với số độ mà chúng ta có thể ngẫu nhiên

xoay hình ảnh của chúng tôi để chúng tôi có thể làm điều gì đó như 20 độ.

Và đối với những thứ như tế bào máu, có bản chất là hình tròn, bạn có thể chọn rất nhiều

lớn hơn 20 độ.

Nhưng ở đây tôi chỉ cho bạn thấy những ví dụ.

Những thứ khác mà chúng ta có thể bắt đầu chỉnh sửa là những thứ như phạm vi thay đổi chiều rộng và điều này sẽ thay đổi

chiều rộng thực tế của hình ảnh theo một số phần trăm tối đa.

Vì vậy, nếu chúng ta nói số 0, một, viết tắt của từ, hãy chọn ngẫu nhiên một giá trị trong khoảng từ 0 đến 10 phần trăm hoặc bằng 0

một điểm 0 một để thay đổi chiều rộng của hình ảnh và chúng ta có thể làm điều tương tự với chiều cao, chúng ta

có thể kéo dài chúng ra một cách ngẫu nhiên.

Vậy chúng ta có thể nói điều gì đó giống như số 0 một.

Bây giờ, bạn có thể đang thắc mắc đâu là giá trị tốt để chọn ở đây cho những thứ như xoay và dịch chuyển?

Tất cả phụ thuộc vào loại hình ảnh bạn đang xử lý.

Chúng tôi rất may mắn trong trường hợp của mình là chúng tôi đang xử lý những gì thực chất là các đốm màu.

Vì vậy, chúng ta có thể mong đợi rằng hình ảnh trong tương lai của các tế bào hồng cầu sẽ trông giống như những đốm màu này sẽ có hình tròn

trong tự nhiên và chúng có thể bị kéo giãn hoặc bị ép lại trong các hình ảnh nổi bật.

Vì vậy, những gì chúng ta có thể làm có lẽ là chọn một giá trị khá lớn hơn ở đây cho những thứ như xoay và dịch chuyển.

Nếu bạn đang xử lý một cái gì đó giống như hoặc dữ liệu, bạn không muốn phải ép hoặc xoay khuôn mặt quá nhiều

rằng họ đang ở những vị trí không thực tế.

Ví dụ: hãy tưởng tượng bạn đang tạo phần mềm cho một máy quay video sẽ cố gắng hết sức để

phát hiện xem khuôn mặt của một người có trong hình ảnh đó hay không.

Có lẽ bạn không muốn xoay thứ gì đó 180 độ vì nó không hữu ích cho máy ảnh.

có thể phát hiện các khuôn mặt lộn ngược trừ khi ai đó sắp đi lộn ngược trong máy ảnh đó

xem.

Vì vậy những ý tưởng đó có thể giúp bạn lựa chọn những giá trị hợp lý cho những phép biến đổi ngẫu nhiên này.

Được rồi, điều khác mà chúng tôi muốn làm là thay đổi tỷ lệ hình ảnh để có thể thay đổi tỷ lệ bằng cách chuẩn hóa

nó.

Nếu chúng ta nhìn vào một trong những hình ảnh mẫu mà chúng ta có.

Vì vậy, chúng ta hãy xem xét, giả sử, Paracel.

Vì vậy, đó là tập tin hình ảnh của chúng tôi ở đó.

Chúng ta hãy nhìn vào.

Hình ảnh hiển thị nó và chúng ta hãy xem các giá trị tối đa ở đây, vì vậy, trong trường hợp của chúng tôi, chúng thực sự là

đã được tiêu chuẩn hóa và chuẩn hóa cho chúng tôi.

Nhưng nếu không, giả sử chúng đã đi từ 0 đến 255, thì tôi sẽ phải điều chỉnh lại bằng cách

nói một chia cho hai năm mươi lăm.

Trong trường hợp của chúng tôi, có vẻ như những hình ảnh này đã được chúng tôi xử lý kỹ lưỡng nên chúng tôi không cần phải bình thường hóa

bất cứ điều gì bởi yếu tố rescale.

Chúng tôi cũng có thể kiểm tra điều này trên ô không bị nhiễm mà chúng tôi có trước đó.

Vì vậy, ô không bị nhiễm, hãy đảm bảo rằng thực sự tôi tin rằng đây đã là một mảng từ trước đó.

Vậy là chúng ta đã có ô không bị nhiễm virus.

Chúng ta hãy nhìn vào nó, kiểm tra giá trị tối đa của nó.

Nó cũng có vẻ được bình thường hóa.

Vì vậy, có vẻ như tất cả các giá trị đều nằm trong khoảng từ 0 đến nhỏ hơn một, đó chính xác là những gì

chúng tôi muốn trong trường hợp của chúng tôi.

Vậy yếu tố rủi ro thì chúng ta không cần lo lắng về điều đó.

Nhưng nếu bạn muốn nâng cao kỹ năng, bạn sẽ làm điều gì đó giống như một trên hai năm mươi lăm.

Được rồi, trong trường hợp của chúng ta, chúng ta đã chuẩn hóa để lo lắng về điều đó, chúng ta cũng có thể làm những việc như có

một phạm vi tuyệt đối.

Vì vậy, tuyệt đối có nghĩa là cắt đi một phần của hình ảnh và chúng ta có thể đặt phần đó ở mức tối đa là 10 phần trăm.

Chúng ta cũng có thể phóng to hình ảnh.

Chúng tôi có tùy chọn phóng to ngẫu nhiên để bạn có thể nói phạm vi thu phóng bằng 0, điểm một.

Chúng ta cũng có thể thực hiện lật ngang và lật dọc.

Vì vậy, ví dụ, tôi có thể nói lật ngang bằng đúng.

Vì vậy nó sẽ ngẫu nhiên cho phép lật ngang.

Và sau đó tôi phải tìm ra cách điền dữ liệu còn thiếu?

Vì vậy, một cách để làm điều này là chế độ Phil gần nhất.

Vì vậy, điều tôi muốn nói là nếu bạn đang thực hiện một phép chuyển đổi về cơ bản kéo dài hình ảnh,

bạn sẽ lấp đầy khoảng trống đó như thế nào?

Bạn sẽ để trống nó chỉ với một vài số 0, hay bạn sẽ lấy số gần nhất

giá trị pixel cho nó và sau đó kéo dài nó ra với các giá trị pixel đó?

Tôi khuyên bạn nên chọn gần nhất.

OK, vậy là chúng ta đã có trình tạo dữ liệu hình ảnh này.

Và chúng ta hãy nhìn vào.

Ô này không bị nhiễm, nhắc lại, ô không bị nhiễm là mảng này, nên mình có thể nói là hình ảnh TLT hiển thị

và tôi có tế bào không bị nhiễm virus này.

Hãy xem điều gì sẽ xảy ra nếu tôi xem xét việc biến đổi ngẫu nhiên tế bào không bị nhiễm bệnh này.

Và nó có thể không quá rõ ràng ở đây vì không có điểm nào ở giữa.

Vì vậy, thực ra, hãy làm điều này với hình ảnh PEMRA hoặc tế bào ký sinh, quay trở lại đây,

đảm bảo chúng ta lấy đúng đối tượng.

Vì vậy chúng ta sẽ nói hình phạt Imrie đối với Paracel.

Vì vậy hãy cuộn lên.

Hãy chọn một trong đó thực sự có điểm này.

Chúng tôi sẽ làm cho nó dễ dàng hơn một chút để xem sự chuyển đổi.

Vì vậy, chúng ta sẽ tiếp tục và nói.

PLT, IMNSHO, Zimride, Paracel.

Được rồi, vậy là tôi có chiếc Paracel Esmoreit này, hãy tiếp tục và thiết lập nó như vậy.

Hình ảnh gạch dưới Para bằng Imrie Paracel.

Bằng cách đó tôi chỉ có thể hiển thị.

Hình ảnh ký sinh trùng, nên chạy về cơ bản là giống nhau.

Vậy tôi sẽ làm gì.

Hãy lấy hình ảnh này là khu vực của tôi và tôi sẽ nói như sau.

Lấy đối tượng tạo hình ảnh mà tôi đã xác định ở trên.

Và gọi một phép biến đổi ngẫu nhiên duy nhất, vì vậy về cơ bản hãy thực hiện một loạt các phép biến đổi ngẫu nhiên trên đó

dựa trên những hạn chế mà tôi đã thiết lập ở đây, vì vậy chúng ta đã biết đây là giao diện thông thường

khi chúng tôi thực sự cung cấp dữ liệu cho mô hình.

Chúng tôi sẽ không cho nó ăn.

Thay vào đó, hình ảnh thô này sẽ biến đổi hình ảnh một cách ngẫu nhiên.

Vậy chúng ta hãy thực sự xem sự biến đổi ngẫu nhiên bằng cách nói, Paul chỉ ra, chạy nó.

OK, bây giờ đây là phiên bản ngẫu nhiên của hình ảnh.

Lưu ý rằng chúng ta có một số loại cột giống như kéo dài nhô ra khỏi ô.

Và đó là bởi vì thông qua sự biến đổi ngẫu nhiên này, có vẻ như nó đã được kéo dài ra và lấp đầy

trong các giá trị đó với giá trị pixel gần nhất.

Và sau đó nó cũng được xoay.

Sẽ rất có ý nghĩa khi xoay hình ảnh ngẫu nhiên ở đây vì chúng là các ô.

Chúng có thể ở bất kỳ loại trục quay nào mà chúng muốn.

Chúng có thể trôi nổi trong mẫu của chúng.

Vì vậy, một lần nữa, tùy thuộc vào loại hình ảnh thực tế bạn đang xem, bạn sẽ như thế nào.

Chơi xung quanh với các giá trị phạm vi thực tế này.

Được rồi, bây giờ với thực tế là chúng ta có thể biến đổi ngẫu nhiên những hình ảnh này, về cơ bản tôi có thể tăng cường

tập dữ liệu, tôi không còn bị giới hạn ở chỉ một hình ảnh này từ ô nữa.

Tôi có thể biến đổi ngẫu nhiên nhiều lần.

Vì vậy, nếu bạn tiếp tục chạy nó, bạn sẽ thấy ngày càng nhiều biến đổi ngẫu nhiên.

Và đây là một cách mở rộng tập dữ liệu hình ảnh của bạn một cách giả tạo.

Hãy nhớ lại, chúng tôi có ít hơn 30000 hình ảnh, nhưng bây giờ tôi có thể thực hiện chuyển đổi ngẫu nhiên trên tất cả những hình ảnh đó

và ngay lập tức tăng gấp đôi kích thước tập dữ liệu của tôi.

Có lẽ tôi có thể thực hiện năm phép biến đổi ngẫu nhiên và tôi đã chuyển từ khoảng 20000 hình ảnh sang 100000

hình ảnh.

Vì vậy, đây là một công cụ thực sự mạnh mẽ mà bạn phải ghi nhớ khi làm việc với các loại vấn đề nhỏ hơn.

bộ dữ liệu.

Và khi nói đến mạng lưới thần kinh tích chập, phải mất hàng nghìn, hàng nghìn hình ảnh để có được thứ gì đó

điều đó thực hiện rất tốt.

Đó là lý do tại sao tập dữ liệu này và tập dữ liệu Safah ton đó thực sự rất lớn.

Được rồi, vậy làm cách nào để chúng ta thực sự thiết lập các thư mục của mình để chuyển các lô từ một thư mục?

Cách chúng tôi làm điều đó là chúng tôi nói.

Hình ảnh gạch dưới, Jen, luồng từ thư mục và sau đó bạn cung cấp đường dẫn đến.

Thư mục đào tạo của bạn, vì vậy hãy nhớ rằng biến đường dẫn xe lửa này, nếu chúng ta đến đây, là đường dẫn tệp

để bán hình ảnh xe lửa.

Vì vậy, chúng ta sẽ nói hãy tưởng tượng dòng chảy từ đường dẫn tàu thư mục.

Và khi bạn chạy nó, bạn sẽ thấy nó nói, OK, tôi đã tìm thấy nhiều hình ảnh này thuộc hai lớp.

Làm thế nào nó thực sự biết điều đó?

Đó là vì để sử dụng luồng từ thư mục, các tệp của bạn thực sự phải được sắp xếp theo

một cách rất cụ thể.

Và chúng tôi đã trình bày điều đó cho bạn trong cuốn sổ tay tương ứng với bài giảng này về cách làm việc theo yêu cầu.

hình ảnh.

Về cơ bản, nếu bạn cuộn xuống, bạn sẽ thấy mọi thứ chúng tôi đã làm cho đến nay.

Tiếp tục đi xuống.

Cho đến khi bạn nhìn thấy điều này, vì vậy để sử dụng luồng từ thư mục, bạn phải sắp xếp các hình ảnh trong Thư mục con.

Vì vậy đây là yêu cầu tuyệt đối, nếu không phương pháp sẽ không hiệu quả.

Vì vậy, khi bạn làm theo các hướng dẫn này trên tập dữ liệu của riêng mình, các thư mục phải được

cơ bản là như thế này.

Bạn phải có thư mục dữ liệu hình ảnh tổng thể của mình.

Vì vậy, hãy nhớ lại đó là thư mục hình ảnh di động của chúng tôi và sau đó bạn cần cho mọi lớp ở đây.

Vậy là bạn có lớp một.

Bạn sẽ tiếp tục và có một hình ảnh, một hình ảnh khác, một hình ảnh khác thể hiện Lớp một,

rồi bốn.

Lớp hai, bạn sẽ cần một hình ảnh khác, một hình ảnh khác, v.v.

Vì vậy, về cơ bản điều sẽ xảy ra là nếu chúng ta xem xét lại lộ trình đào tạo ban đầu của mình để có thể quay trở lại

vào sổ ghi chép của chúng tôi để tìm hiểu về điều này, gợi nhớ về con đường đào tạo của chúng tôi.

Ở ngay đây, hình ảnh tế bào được đào tạo và bên trong đó, nếu tôi nói hệ điều hành.

Liệt kê các thư mục.

Tôi có một thư mục cho mỗi lớp, ví dụ: nếu chúng ta đang giải quyết vấn đề phân loại nhiều lớp

giả sử chúng ta đang cố gắng phân biệt hình ảnh của chim, chó và mèo, thì tôi sẽ cần

ba thư mục ở đây, một thư mục chứa tất cả các hình ảnh con chim, một thư mục chứa tất cả các hình ảnh con chó và một thư mục chứa tất cả các hình ảnh

những hình ảnh con mèo.

Vì vậy, bạn cần một thư mục cho mỗi lớp.

Đó là cách luồng từ thư mục này hiểu ngay rằng có hai lớp vì có

hai thư mục ở đây.

Có thư mục ký sinh trùng và thư mục không bị nhiễm virus.

Đó là cách nó hoạt động.

Nó phải như vậy.

Ở loại định dạng này, khi đó bạn sẽ có một thư mục dành cho dữ liệu đào tạo của mình và sau đó là một thư mục

cho dữ liệu thử nghiệm của bạn.

OK, bây giờ chúng ta đã hiểu điều đó, hãy tiếp tục và xem quá trình tạo hình ảnh trông như thế nào

dòng chảy từ bài kiểm tra.

Nó sẽ chỉ nói dòng gen hình ảnh từ thư mục.

Kiểm tra đường dẫn thử nghiệm, chạy nó và bạn sẽ nhận thấy nó tìm thấy hai nghìn sáu trăm hình ảnh thuộc về

thành hai lớp, điều này hợp lý vì mỗi lớp có 1300 hình ảnh.

Và một lần nữa, đường dẫn kiểm tra có định dạng giống hệt nhau.

Nó có hai thư mục bên dưới, một thư mục cho mỗi lớp.

Được rồi, bài giảng này đã kết thúc về khả năng tạo hình ảnh từ trình tạo dữ liệu hình ảnh này,

đối tượng lớp.

Đây là một lớp học siêu hữu ích và về cơ bản nó thực hiện tất cả những công việc nặng nhọc cho bạn.

Tôi khuyến khích bạn dành thời gian đọc tài liệu trực tuyến về nó để xem những lựa chọn nào khác

có đấy.

Nhưng điều chính cần lưu ý ở đây và một lần nữa, một phần quan trọng của việc này là hiểu đường dẫn tệp của bạn,

đang đảm bảo dữ liệu của bạn được sắp xếp theo định dạng cụ thể này là một thư mục cho mỗi lớp hoặc mỗi thư mục

thư mục lớp có nhiều phiên bản của lớp cụ thể đó.

Vì vậy, ví dụ: đây sẽ là tất cả chó, Albat, v.v. cho từng lớp động vật đó.

Trong trường hợp của chúng tôi, chúng tôi chỉ xử lý hai lớp.

Tiếp theo, chúng ta sẽ tạo một mô hình và sau đó chúng ta sẽ nói về việc đánh giá mô hình

hiệu suất.

Cảm ơn.

Và tôi sẽ gặp bạn ở bài giảng tiếp theo.