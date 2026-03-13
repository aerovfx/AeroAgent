# 47 - Keras Regression EDA Tiếp tục Tiếng Anh

---

Được rồi, bây giờ hãy tiếp tục và bắt đầu quy trình kỹ thuật tính năng của chúng ta cũng như loại bỏ các tính năng

điều đó sẽ không có ích cho chúng ta.

Vì vậy, chúng ta sẽ bắt đầu làm việc với dữ liệu tính năng này.

Và tôi luôn thích xem lại khung dữ liệu.

Vì vậy, thứ chúng ta có thể bỏ ngay là ý tưởng này.

Ý tưởng này là một loại ý tưởng độc đáo.

Không có xu hướng cho nó.

Và nếu có, có lẽ chúng ta không thực sự hiểu nó dựa trên con số này.

Vì vậy tôi sẽ chỉ nói D.F. bằng với việc thả rồi hãy tiếp tục bỏ cột ý tưởng đó.

Và đó là dọc theo trục bằng một.

Vì vậy, chúng ta tiếp tục và bỏ cột ý tưởng đó đi và điều tiếp theo chúng ta sẽ làm là kiểm tra.

Cột ngày tháng, vì vậy nếu chúng ta nhìn vào cột ngày tháng này ngay bây giờ, nó có vẻ giống như một cột nào đó

của chuỗi để chúng ta có thể chuyển đổi nó thành đối tượng ngày giờ bằng cách thực hiện như sau.

Tôi có thể nói DFA ngang bằng với Paudie.

Để nhấn mạnh ngày giờ.

Và Ngày Passan và mục đích của nó là nó sẽ tự động chuyển chuỗi này thành ngày giờ

đối tượng và khi nó là đối tượng ngày giờ, điều đó có nghĩa là tôi có thể trích xuất thông tin như tháng hoặc

năm tự động.

Vì vậy, tôi tiếp tục và chạy cái này.

Và bây giờ nếu tôi nhìn vào cột ngày của mình, hãy lưu ý, định dạng đã khác và bây giờ nó sẽ báo cáo lại

rằng đó là một đối tượng ngày giờ, có nghĩa là tôi có thể bắt đầu thực hiện kỹ thuật tính năng từ đối tượng này.

Bản thân thời gian ngày này có thể không hữu ích, nhưng tôi có thể trích xuất thành phần năm và thành phần tháng.

Và cách tôi có thể làm điều đó là thông qua một vài cuộc gọi đơn giản.

Tôi có thể nói là năm F.

Bằng với ngày tháng.

Và tôi có thể áp dụng một hàm thực sự trích xuất năm kể từ thời điểm ngày này, vì vậy nếu tôi có một ngày

đối tượng thời gian, nó chỉ đơn giản là một lệnh gọi thuộc tính để lấy chính năm đó.

Và tôi có thể làm điều này một cách đơn giản và diễn đạt bằng cách nói lam ngày và sau đó nói ngày tháng.

Nếu bạn không quen với các biểu thức đất đai thì đó thực chất là cách viết tắt của một hàm.

Vì vậy, để cho bạn thấy ý tôi khi nói điều đó, cách diễn đạt đất đai này sẽ giống hệt như khi tôi làm vậy

cái này hoặc tạo một hàm gọi là trích xuất của bạn sẽ mất một ngày nào đó và sau đó trả về ngày quay lại trong năm,

ngày tháng đó.

Và trong trường hợp này, thực tế phải là năm để khớp với cái mà tôi gọi là cột ở đây.

Vì vậy, biểu hiện đất này giống hệt như việc chạy nó ở đây.

Vì vậy, hãy nhớ lại rằng khi được xây dựng bằng Python, bạn có đối tượng ngày giờ này và bạn có thể lấy các thuộc tính

của năm, tháng, v.v. đó là lý do tại sao chúng tôi gọi PD là thời gian ngày tháng trên cột chuỗi gốc.

Và biểu hiện đất đai này về cơ bản là cách viết tắt cho điều đó.

Và tôi sẽ sao chép và dán cái này.

Cũng trong nhiều tháng.

Và đây thực chất là kỹ thuật tính năng, vì những tính năng này được ẩn kỹ thuật bên trong

của ngày trong chuỗi và bây giờ tôi đang tạo các cột mới để cố gắng trích xuất hoặc xử lý thêm thông tin

đặc điểm ban đầu của tôi

Đây là một bước rất phổ biến, đặc biệt nếu có dấu thời gian.

Vì vậy chúng ta sẽ tiếp tục và chạy cái này.

Và bây giờ nếu tôi nhìn vào phần đầu của khung dữ liệu, tôi có cột ngày giờ mới được định dạng này

và tôi sẽ cuộn sang bên phải ở đây và tôi sẽ thấy cột Năm và tháng của mình.

Và bây giờ tôi có thể thực hiện một số loại phân tích dữ liệu khám phá để xem liệu đây có phải là những tính năng hữu ích nói chung hay không.

Vì vậy, hãy tiếp tục và xem liệu có bất kỳ biến thể nào dựa trên tháng mà sản phẩm này được bán hay không.

Vì vậy, có thể chúng tôi định giá mọi thứ cao hơn nếu chúng tôi tin rằng chúng sẽ có mặt trên thị trường vào tháng 12 so với tháng 3.

Vì vậy tôi có thể làm điều đó bằng cách nói S.A.S. Sơ đồ hộp.

Và hãy tiếp tục xem mức phân bổ mỗi tháng.

Và một cách khác mà tôi có thể làm là thông qua việc nhóm theo tháng và sau đó mô tả về giá

cột nữa, về cơ bản đây là chức năng trực quan của một điểm hộp.

Và hãy làm cho cái này lớn hơn một chút.

Chúng ta sẽ nói con số PLT.

Kích thước này.

Hãy biến cái này thành khoảng 10 x 6, tiếp tục và chạy cái này và tôi có thể thấy bản phân phối ở đây.

Bây giờ, thật khó để nói chỉ từ cốt truyện này liệu có sự khác biệt đáng kể về phân phối hay không

giữa tháng mà bạn định bán căn nhà này.

Và điều có thể dễ dàng hơn là chỉ cần nhìn vào các con số để tôi có thể thực hiện chữ F.

Nhóm theo tháng ô tô ở đây và sau đó chỉ cần xem giá trung bình mỗi tháng là bao nhiêu, vì vậy tôi sẽ lấy giá trị trung bình

sau khi tôi mua theo nhóm và sau đó chỉ cần khám phá giá cả và sau đó nghe điều này có lẽ sẽ cho phép tôi thực sự

tự mình xem hoặc đọc các con số để xem liệu có sự khác biệt đáng kể nào giữa các tháng không

và nếu tôi muốn nhìn thấy điều này một cách trực quan, tôi cũng có thể chỉ cần gọi dấu chấm và điều này sẽ cho tôi thấy hành vi.

Vì vậy, có vẻ như có sự khác biệt nào đó giữa các tháng.

Nếu chúng ta thực sự nhìn thấy tổng phạm vi sóng, nó chỉ tăng từ năm triệu ish xuống còn khoảng năm rưỡi.

triệu ish.

Vì vậy, không có sự khác biệt lớn về giá ở đây.

Xin lỗi, thực ra.

Năm trăm mười nghìn so với năm trăm sáu mươi nghìn.

Vì vậy, không phải là một phạm vi lớn, nhưng có vẻ như có một số khác biệt về hành vi ở đó trong các tháng

và chúng ta có thể làm những điều tương tự trong năm.

Vì vậy, nếu tôi muốn khám phá năm, cốt truyện này chắc chắn có ý nghĩa, bởi vì nếu bạn nhìn lại

Doanh số bán hàng ở Quận King, chúng chỉ tăng giá theo thời gian.

Và bạn sẽ mong đợi điều đó một cách tự nhiên với lạm phát, trừ khi có một loại nhà ở lớn nào đó

sự kiện.

Được rồi, vậy là chúng ta đã nêu rõ năm và tháng được thiết kế.

Chúng ta sẽ tiếp tục và chỉ giữ chúng trong đó, xem mô hình có sử dụng chúng hay không và chúng ta sẽ bỏ ra

cột ngày của chúng tôi.

Chúng ta sẽ Sadaf bằng với DFG drop.

Và chúng ta sẽ xuống xe.

Cột ngày ban đầu đó, vì nó không còn hữu ích với chúng tôi nữa, vì chúng tôi đã thiết kế những gì chúng tôi làm.

Bây giờ, chúng ta hãy xem nhanh lại những thuộc địa còn lại mà chúng ta có, chúng ta có thể làm điều này với

D. F. cột hoặc tôi chỉ cần kiểm tra phần đầu của khung dữ liệu để bắt đầu khám phá phần này.

Rất nhiều tính năng trong số này thực sự có ý nghĩa như hiện tại.

Vì vậy, số lượng phòng ngủ, phòng tắm, diện tích sống có vẻ như chúng ta không cần phải làm nhiều tính năng

kỹ thuật ở đây.

Và thậm chí cả các danh mục loại bờ sông và chế độ xem, những loại này đã ở dạng biến giả đối với chúng tôi.

Vì vậy, nó là số không hoặc một.

Điều mà chúng tôi muốn lưu ý là cột mã zip này.

Vì vậy, mã zip là số.

Và nếu chúng ta đưa dữ liệu này trực tiếp vào mô hình của mình, mô hình sẽ cho rằng đó là một dạng liên tục

tính năng mà bằng cách nào đó mã zip chín tám một bảy tám lớn hơn chín tám một hai năm.

Và điều này có thể đúng hoặc không tùy thuộc vào cách mã zip thực sự được ánh xạ trên thực tế

bản đồ.

Vì vậy, đây là lúc trải nghiệm tên miền phát huy tác dụng.

Bạn phải tự mình tra cứu bản đồ để có thể tìm kiếm nhanh trên Google và tìm thấy một số loại

lập bản đồ mã vùng trên Quận King và xem liệu thực sự có mối quan hệ nào không.

Bạn có thể phóng to ở đây và xem liệu có mối quan hệ nào giữa các số mã zip được chỉ định không

so với có thể là vĩ độ hoặc kinh độ của chúng.

Họ cũng có thể làm điều đó thông qua một số loại âm mưu tương quan.

Nhưng nếu bạn xem xét kỹ hơn điều này, dường như không có sự phân bổ liên tục rõ ràng của

những mã zip thực tế này, có nghĩa là bạn sẽ muốn bắt đầu coi mã này như một biến phân loại.

Vì vậy, một lần nữa, chúng ta sẽ quay lại sổ ghi chép của mình ở đây và bắt đầu khám phá điều này và xem liệu nó có thực sự

có thể giữ nó như một loại danh mục nào đó để chúng ta có thể nói điều gì đó giống như F.

Mã vùng.

Và giá trị cuộc gọi được tính vào nó và điều này sẽ cho chúng tôi ý tưởng về số lượng mã zip duy nhất thực tế mà chúng tôi có

và sự phân bố của chúng như thế nào trên tập dữ liệu.

Và có vẻ như chúng ta có 70 mã zip duy nhất.

Vì vậy, có lẽ là quá nhiều nếu chỉ gọi cho PD, tìm hiểu về vấn đề này và sau đó có 70 loại zip

mã.

Vậy chúng ta sẽ đi tiếp.

Và đối với trường hợp cụ thể này, chúng tôi sẽ bỏ cột mã zip vì 70 danh mục là quá nhiều

cho chúng tôi.

Tuy nhiên, điều chúng ta có thể làm là có một chút kinh nghiệm về miền và kiến thức về miền, có thể thử

để phân loại điều này dựa trên những gì chúng tôi biết là mã zip đắt tiền và mã zip có thể rẻ hơn.

Hoặc chúng ta có thể thực hiện một số cách lập bản đồ hoặc nhóm để tạo mã zip ở phía nam, mã zip ở giữa,

mã zip ở phía Bắc, phía Đông và phía Tây, v.v. Nhưng việc này sẽ mất nhiều công việc thủ công hơn ở đây và nó

cũng cần có nhiều kinh nghiệm hơn về thực tế Quận King như thế nào.

Vì vậy, một lần nữa, một phần quan trọng của học máy và khoa học dữ liệu là liên hệ với người có kinh nghiệm về miền

và cố gắng sắp xếp các ánh xạ và kỹ thuật tính năng đó vào đúng vị trí.

Nhưng đối với trường hợp sử dụng của chúng tôi, có 70 danh mục ở đây.

Tuy nhiên, chúng tôi sẽ tiếp tục và bỏ qua chúng ngay bây giờ và trong một tình huống thực tế hơn.

Bạn có thể muốn dành thời gian để xem bản đồ và bắt đầu tự mình vạch ra những điều này theo cách thủ công.

Vì vậy chúng ta sẽ nói D.F. bằng với mức giảm DF và thực ra là vì mục đích thời gian, chúng ta sẽ bỏ zip

cột mã.

Và còn có những thứ khác mà chúng ta có thể xem xét, một thứ khác có thể gây rắc rối là

năm nay đã được cải tạo.

Bạn sẽ nhận thấy năm đó đã được cải tạo nếu chúng ta nhìn vào nó, D.F..

Bạn là người cải tạo, hãy tính giá trị của điều đó.

Hầu hết các giá trị thực tế đều bằng 0, về cơ bản ngụ ý rằng nó chưa được cải tạo, vì vậy anh ấy

bị mắc kẹt trong số 0 ở đó.

Và sau đó chúng ta có hai mươi, mười bốn, hai mươi, mười ba, v.v..

Bây giờ, có những cách tiếp cận khác nhau mà chúng ta có thể thực hiện ở đây khi có liên quan đến kỹ thuật trong tương lai.

Một vấn đề chính ở đây mà chúng ta có thể nói là số 0 thực ra không phải là một năm.

Thay vào đó, về cơ bản nó là dấu hiệu cho thấy ngôi nhà chưa được cải tạo.

Vì vậy, có thể sẽ hợp lý hơn nếu phân loại cái này là đã được cải tạo hoặc chưa được cải tạo, về cơ bản hãy biến tất cả những thứ này thành

năm sử dụng chức năng được áp dụng tùy chỉnh thành một loại cuộc gọi cải tiến tích cực và sau đó giữ số 0 chỉ

không được cải tạo.

Vì vậy, chúng ta có thể làm điều đó thông qua và áp dụng hàm.

Tuy nhiên, chúng ta thực sự có thể lợi dụng tình huống này bằng cách nghĩ về nó theo cách sau.

Lưu ý rằng về cơ bản, năm cải tạo càng gần thì giá trị càng cao.

năm nay cải tạo thì khả năng cao là nhà đó sẽ có giá bán cao hơn.

Và chúng ta chỉ có thể nghĩ ra một cách trực quan vì việc cải tạo càng gần đây thì càng tốt.

Và vì số 0 thực sự tuân theo mối tương quan này, nên nó gần giống như năm thấp nhất có thể,

thì chúng ta nên mong đợi rằng nó cũng có ít giá trị.

Vì vậy, trong trường hợp này, chúng tôi thực sự khá may mắn.

Và do quy mô từ 0 đến năm cao nhất nên tương quan với giá trị cao hơn.

Và chúng ta thực sự có thể giữ nguyên như vậy.

Và về cơ bản đó là loại tình huống may mắn mà chúng ta gặp phải, khi năm tháng phải trôi qua

theo hướng tích cực và những năm cao hơn có xu hướng tương quan với giá trị cao hơn vì những năm gần đây hơn

một cuộc cải tạo, chỉ bằng trực giác, bạn mong đợi nó sẽ có nhiều giá trị hơn.

Bây giờ, điều đó không phải lúc nào cũng đúng đối với những thứ có số năm và sau đó được điền vào các số 0.

Nhưng trong trường hợp của chúng tôi, chúng tôi đã gặp chút may mắn ở đây và việc để nó ở lại là điều hợp lý.

Tuy nhiên, bạn có thể thực hiện nhiều kỹ thuật tính năng hơn từ việc này bằng cách phân loại nó thành cải tạo và cải tạo.

không được cải tạo.

Được rồi, và những điều khác chúng ta có thể làm là chúng ta có thể xem ở đây một số như feet vuông trong

tầng hầm, một tình huống tương tự.

Vì vậy, nếu tôi lấy feet vuông và tầng hầm và tính giá trị trên đó.

Bạn sẽ nhận thấy rằng trong tình huống tương tự, nó chỉ có số 0 ở đó cho rất nhiều mục và số 0

rất có thể chỉ có nghĩa là không có tầng hầm ở đó.

Vì vậy, họ chỉ cần xây dựng một căn nhà rộng 4 feet vuông và tầng hầm.

Bây giờ, chúng ta có thể thấy ở đây một lần nữa các giá trị bắt đầu tăng lên, v.v.

Và về cơ bản những điều này cũng có ý nghĩa như một biến liên tục, bởi vì chúng ta mong đợi rằng nếu có

không có tầng hầm, nó sẽ có ít giá trị hơn việc có một tầng hầm cực rộng.

Vì vậy, chúng ta cũng có thể giữ nguyên như vậy.

Vì vậy, nhiều khi bạn sẽ phải đưa ra quyết định về kỹ thuật tính năng nếu muốn thực hiện liên tục

biến phân loại hoặc chỉ giữ nó liên tục.

Và bạn phải thực sự suy nghĩ cẩn thận xem việc giữ nó liên tục có hợp lý hay không.

Và đối với hai số này, không phải là một giả định điên rồ nếu giữ chúng liên tục và để các số 0 này là

loại điểm đánh dấu dưới cùng của bạn.

Được rồi.

Vậy là xong phần phân tích tính năng và kỹ thuật tính năng của chúng tôi.

Ở phần sau của bài tập phần này, bạn sẽ thực hiện nhiều kỹ thuật về tính năng hơn những gì chúng tôi đã làm

ở đây.

Vì vậy, hãy ghi nhớ điều đó.

Kỹ thuật tính năng và phân tích dữ liệu khám phá gần như luôn là một phần cần thiết của bất kỳ hàng hóa nào

dự án khoa học dữ liệu hoặc học máy.

Tiếp theo, chúng ta sẽ tập trung vào việc phân chia, chia tỷ lệ và tiền xử lý bài kiểm tra huấn luyện của mình

dữ liệu của chúng tôi để tạo ra mô hình của chúng tôi để chạy khỏi nó.

Cảm ơn.

Và tôi sẽ gặp bạn ở bài giảng tiếp theo.