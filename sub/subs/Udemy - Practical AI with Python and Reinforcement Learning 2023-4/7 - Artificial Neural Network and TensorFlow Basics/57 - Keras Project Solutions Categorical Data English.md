# 57 - Keras Project Solutions Dữ liệu phân loại tiếng Anh

---

Chào mừng mọi người quay trở lại, trong bài giảng này, chúng tôi sẽ hướng dẫn các bạn cách làm việc với phân loại

dữ liệu trong tập dữ liệu của chúng tôi.

Vì vậy, chúng tôi chỉ xử lý dữ liệu còn thiếu.

Bây giờ, hãy khám phá dữ liệu phân loại và dữ liệu chuỗi rồi xem liệu chúng ta có xóa hoặc chuyển đổi dữ liệu đó không

nó thành các biến giả bằng cách sử dụng một mã hóa nóng.

Hãy quay lại sổ ghi chép Sao Mộc và tiếp tục từ nơi chúng ta đã dừng lại.

Được rồi, tôi lại đang ở bên cuốn sổ đây.

Chúng ta đã xử lý tất cả các giá trị null mà tôi có thể thấy ở đây từ trước.

Chúng tôi không còn giá trị null nữa.

Vì vậy, bây giờ chúng ta cần làm là quan tâm đến các biến phân loại.

Vì vậy, nhiệm vụ đầu tiên là liệt kê tất cả các cột hiện không phải là số.

Và có hai liên kết hữu ích ở đây về cơ bản chỉ cho bạn cách nhanh chóng sử dụng nó thông qua một cách rất hữu ích.

cuộc gọi phương thức.

Và cách chúng tôi có thể làm là nếu bạn kiểm tra các liên kết đó, nó sẽ yêu cầu bạn chạy D.F. Chọn D

các loại.

Và chúng ta có thể chọn một đối tượng dưới dạng một chuỗi mục duy nhất, sau đó chọn các cột được điều chỉnh lạnh và chỉ điều đó

chọn các cột chuỗi cơ bản.

Vì vậy, bây giờ chúng ta phải làm là chúng ta phải xem qua từng lớp học kỳ này, thật tuyệt vời, v.v. và xem điều gì

chúng ta nên làm gì với họ.

Một số trong số chúng sẽ bị xóa, một số khác sẽ hữu ích cho chúng tôi và chúng tôi sẽ giữ chúng.

Vì vậy chúng ta phải quyết định.

Và điều đầu tiên chúng ta sẽ bắt đầu là thuật ngữ.

Vì vậy, chúng ta hãy tiếp tục và kiểm tra thuật ngữ.

Và trên thực tế, nếu chúng tôi kiểm tra thuật ngữ đó, chúng tôi có thể thực hiện yêu cầu thông tin tính năng theo thuật ngữ từ chức năng đó

mà chúng tôi dành cho bạn.

Đó là một số khoản thanh toán cho khoản vay và giá trị được tính bằng tháng và có thể là ba, sáu tháng

hoặc sáu tháng.

Và nếu chúng ta nhìn vào.

D.F. lưu ý rằng số lượng thuật ngữ và giá trị cuộc gọi về cơ bản là một cột nhị phân, có ba mươi sáu

tháng hoặc sáu tháng, có nghĩa là chúng ta có một vài lựa chọn ở đây vì nó cũng là số.

Tôi có thể chuyển đổi số này thành 36 dưới dạng số nguyên hoặc 60 dưới dạng số nguyên.

Vì vậy, một cách trực tiếp, chỉ cần lấy hai số đầu tiên cơ bản này và chuyển chúng thành số nguyên.

Điều khác tôi có thể làm là vì về mặt kỹ thuật nó chỉ có hai loại, tôi có thể dùng một mã nóng

bây giờ có thể là ba mươi sáu tháng hoặc không phải là ba mươi sáu tháng vì có một mối quan hệ bằng số

từ ba mươi sáu đến 60 tháng.

Hãy tiếp tục và giữ mối quan hệ bằng số đó về cơ bản cho bạn thấy mối quan hệ giữa việc có

nhiều thời gian hơn để trả hết khoản vay.

Vì vậy, điều chúng ta sắp làm là ánh xạ trực tiếp cái này tới 36 và 60.

Có nhiều cách bạn có thể làm điều này.

Một cách là chỉ cần tạo một từ điển gọi là ánh xạ nào đó và sau đó ánh xạ chuỗi ba mươi sáu tháng tới

số ba mươi sáu, chuỗi sáu tháng đến số 60.

Nhưng một cách khác mà chúng ta có thể làm là lấy hai ký tự đầu tiên trong chuỗi và chuyển đổi

chúng thành một con số thực tế.

Vì vậy, cách bạn sẽ làm điều đó.

Là bằng cách áp dụng một hàm thực hiện biểu thức Orlanda đó, vì vậy chúng ta sẽ làm là tiết kiệm một chút

một chút không gian, chúng ta sẽ thực hiện biểu thức đất đai.

Về cơ bản, chúng ta sẽ xem xét các điều khoản và đối với các điều khoản, chúng ta sẽ lấy hai ký tự đầu tiên,

thiết lập mọi thứ thành bật, kể cả chỉ số 3, sau đó chúng ta sẽ chuyển đổi nó thành số nguyên.

Và sau đó chúng ta sẽ nói D.F. thuật ngữ.

Bằng với số hạng và chúng ta áp dụng nó, vì vậy chúng ta sẽ tiếp tục chạy nó.

Hãy ghi nhớ, bạn có thể nhận được một cảnh báo.

Nhưng trong trường hợp này, điều đó không sao cả, về cơ bản là cảnh báo bạn rằng bạn đang lấy một cột hiện có và

sau đó gán lại nó.

Vì vậy, chỉ nói cho bạn biết những gì bạn đã biết.

Và nếu bạn nhìn vào D.F. học kỳ bây giờ, bạn sẽ nhận thấy bây giờ chỉ còn ba mươi sáu sáu mươi nên chúng ta thực sự có thể

chạy lại giá trị này.

Và chúng ta thấy về cơ bản chúng ta chuyển đổi thành ba mươi sáu tháng, sáu tháng thành các số nguyên, 36 và 60.

Vậy là cột đó bây giờ đã được xử lý xong.

Bây giờ là cột số mà chúng ta có thể chuyển sang dòng chảy dày đặc hơn.

Phần tiếp theo chúng ta sẽ xem xét là tính năng tuyệt vời.

Và chúng ta thực sự đã biết rằng lớp chỉ đơn giản là một phần của lớp phụ.

Vì vậy, chúng ta có thể bỏ đi tính năng tuyệt vời vì việc thu hồi ở cấp phụ đã có thông tin đó.

Nếu thứ gì đó thuộc hạng phụ của Jiwon thì chúng tôi đã biết thuộc hạng G rồi.

Vì vậy, đó thực chất là thông tin trùng lặp.

Vì vậy chúng ta sẽ tiếp tục và bỏ nó đi.

Hãy cứ nói D.F. bằng D. F. sự sụt giảm đó và chúng ta sẽ nói lớp X bằng một.

Hãy nhớ rằng, bất cứ khi nào bạn đang chạy các lệnh gọi phương thức hoặc lệnh gọi hàm này, bạn chỉ có thể chạy

chúng một lần.

Nếu không, bạn sẽ gặp lỗi vì bạn không thể bỏ thứ gì đó nhiều lần.

Vì vậy, chúng tôi tiếp tục và chạy nó.

Và bây giờ chúng tôi không còn cột đó nữa.

Và bây giờ chúng ta sẽ chuyển đổi cột điểm phụ thành các biến giả và sau đó

chúng tôi sẽ nối các cột mới này với khung dữ liệu gốc.

Một vài điều cần nhớ từ các bài giảng là bỏ cột riêng ban đầu, vì chúng ta

sau này sẽ không cần nó nữa

Và để thêm dấu gạch dưới trước tiên bằng true trong lệnh gọi giả của bạn để ngăn chặn đa biến

bẫy, về cơ bản ngăn chặn việc mã hóa thông tin trùng lặp.

Vì vậy chúng ta hãy tiếp tục và kiểm tra điều này.

Bạn có thể thực hiện việc này theo nhiều cách khác nhau nhưng về cơ bản có ba bước chính.

Bước đầu tiên là thực sự lấy các biến giả.

Vì vậy chúng ta sẽ nói hình nộm bằng với.

Nhận hình nộm và sau đó tôi sẽ lấy chúng từ cột điểm phụ, vì vậy tôi có cột điểm phụ của mình

và nhớ lại vì đó là một cột, tôi cũng cần phải nói ở đây rằng việc thả đầu tiên bằng đúng và cuối cùng

sẽ ngăn chúng tôi mã hóa thông tin trùng lặp.

Đó là lý do tại sao chúng tôi bỏ cái đầu tiên.

Bạn có thể tưởng tượng trong trường hợp này, nếu chúng ta có một loại cột giới tính hoặc giới tính nào đó là nam hay nữ,

chúng ta không cần mã hóa cả hai thành số 0 và số 1, thay vào đó nó sẽ được chuyển đổi thành liệu

hoặc không họ là nam, không hoặc một.

Nếu không, bạn đang sao chép thông tin.

Và điều tương tự cũng xảy ra nếu bạn bắt đầu mở rộng sang nhiều danh mục hơn.

Vì vậy, nếu bạn có ABC làm danh mục của mình, vì vậy nếu bạn có ABC, bạn không cần mã hóa nó thành 0

số không hoặc một cái gì đó như thế.

Bạn chỉ cần các cột IMDB, vì nếu không và nếu không phải B thì có nghĩa là nó

sẽ là C, đó là lý do vì sao chúng ta tụt xuống so với bằng nhau.

Đúng đấy.

Được rồi, sau đó chúng ta cần nối nó với khung dữ liệu thực tế.

Vì vậy chúng ta sẽ nói D.F. và đầu tiên sẽ bỏ sub gốc.

Cột tuyệt vời.

Bởi vì chúng ta sẽ không cần nó nữa, vì chúng ta đã có các hình nộm và điều chúng ta sẽ làm là ghép nối nó

với những hình nộm, nên chúng ta sẽ nói là PD.

Ghép nối cái này, chúng ta chuyển cái này dưới dạng một danh sách, nối nó với việc đảm bảo rằng quyền truy cập bằng một

với việc bỏ lớp phụ rồi nói lớp phụ.

Trên thực tế, chỉ cần nói ngu ngốc ở đây.

Và sau đó chúng ta sẽ nói trục bằng một, vì vậy chúng ta thực hiện lệnh gọi hàm đó và sau đó chúng ta đặt trục đó thành hiện tại của mình

khung dữ liệu.

Vì vậy, thực sự chỉ có hai dòng mã chính.

Đầu tiên là đưa hình nộm ra khỏi tàu ngầm.

Cột tuyệt vời.

Và việc tiếp theo là đảm bảo xóa cột ban đầu đó rồi nối nó với

hình nộm dọc theo các cột.

Và về cơ bản đó là tất cả những gì cần làm.

Và bạn phải đảm bảo rằng dấu ngoặc và dấu ngoặc đơn của bạn khớp với nhau.

Có vẻ như chúng ta ở đây ổn.

Vì vậy chúng ta hãy tiếp tục và chạy cái này.

Và chúng ta bắt đầu.

Vì vậy bây giờ nếu tôi nhìn vào các cột này, bạn sẽ nhận thấy tôi có nhiều cột hơn vì bây giờ chúng ta có

một mã hóa cho mỗi bản nâng cấp có thể có.

Và chúng tôi đã bỏ môn đầu tiên, đó là A1.

OK, bây giờ đã có cột của tôi và chúng ta sẽ tiếp tục.

Ý tôi là, hãy tiếp tục và bình luận điều đó.

Và bây giờ về cơ bản chúng ta sẽ thực hiện điều tương tự đối với trạng thái xác minh, loại ứng dụng được khởi tạo

trạng thái.

Và cột mục đích, vì vậy nếu bạn nhìn vào các cột khác, chúng cũng là những ứng cử viên sáng giá

vì đã được chuyển đổi thành các biến giả vì không có nhiều danh mục và chúng khá đẹp

cũng có nhiều đối với hầu hết các hệ nhị phân này hoặc chỉ một số danh mục.

Vì vậy, chúng là những ứng cử viên tốt để tiếp tục chuyển đổi chúng thành các biến giả để chúng ta thực sự có thể

thực hiện việc này về cơ bản giống hệt các bước mà chúng tôi đã thực hiện ở đây.

Vì vậy, tôi chỉ cần sao chép và dán những thứ này.

Và sau đó đặt chúng vào đây và điều tôi sắp làm là tôi chỉ cần che những cột này và chúng ta đặt

chúng theo cách mà bạn có thể sao chép và dán.

Vì vậy, chúng ta sẽ chuyển đổi và lấy hình nộm và lấy chúng theo lệnh.

Bạn có thể chuyển tất cả những người này cùng một lúc và sau đó chúng tôi sẽ tiếp tục và loại bỏ các cột ban đầu.

Ngay lập tức, chúng ta sẽ tiếp tục và làm điều đó, thế là xong.

Vì vậy, đây thực sự là các lệnh giống hệt nhau trước khi bạn chuyển danh sách các cột ngay bây giờ, đó là

khá tốt.

Vì vậy, chúng tôi không cần phải làm thêm việc gì.

Chúng ta sẽ tiếp tục và chạy nó.

Hãy để tôi dành thêm một chút thời gian vì ở đây khá nhanh, nhưng chúng tôi đã tiếp tục và cẩn thận

của các cột đó.

OK, bây giờ là quyền sở hữu nhà.

Chúng ta sẽ tiếp tục và xem xét số lượng giá trị ở đây cho cột quyền sở hữu nhà để biết được điều gì đó

trông như thế này

Vậy Sadaf, quyền sở hữu nhà.

Và nếu bạn đếm giá trị ở đây, điều bạn sẽ nhận thấy là về cơ bản hầu hết mọi người đều kiếm được

ba loại thế chấp, thuê hoặc sở hữu, và sau đó chỉ có rất ít thuộc loại khác không hoặc

bất kỳ.

Vì vậy, những gì chúng ta sẽ làm ở đây là vì có quá ít người và không có ai, hãy cứ tiếp tục

và đặt những kẻ 29 và 3 này vào loại khác.

Vì vậy, bằng cách đó, chúng tôi giảm số lượng cột tính năng thực tế vì chúng tôi không muốn có toàn bộ cột tính năng

chỉ cho hai mươi chín cộng ba người.

Thay vào đó, chúng ta sẽ tiếp tục và đặt chúng vào phần còn lại.

Vì vậy, để bắt đầu việc này, trước tiên chúng tôi muốn thay thế none và bất kỳ bằng cái khác và liên kết thay thế sẽ thực sự

hiển thị cho bạn lệnh gọi này, cho phép bạn thay thế trực tiếp các giá trị chuỗi bằng các giá trị chuỗi khác.

Vì vậy, chúng ta có thể thấy ở đây có tài liệu về cách nó thực sự hoạt động.

Nhưng về cơ bản, cuộc gọi trông như thế này, chúng tôi nói và có nhiều cách bạn có thể thực hiện việc này.

Bạn cũng có thể chỉ cần lập bản đồ nó.

Bạn có thể nói không có cái nào được ánh xạ sang cái khác hoặc chỉ thực hiện chức năng áp dụng tùy chỉnh của bạn, nhưng.

Chà, điều duy nhất tôi thực sự phải làm ở đây là quyền sở hữu nhà và nói thay thế và bạn có thể

chuyển qua danh sách những gì bạn muốn thay thế.

Vì vậy, trong trường hợp này, tôi muốn thay thế none và bất kỳ pass nào làm tham số thứ hai mà bạn muốn thay thế

họ với.

Và trong trường hợp này, tôi muốn thay thế chúng bằng cái khác.

Vì vậy, bạn có thể thực hiện việc này nếu từ điển ánh xạ chức năng áp dụng tùy chỉnh của bạn hoặc với sự tiện lợi này

thay thế chức năng.

Rất nhiều cách khác nhau bạn có thể làm điều này.

Vì vậy, hãy tiếp tục và chạy sự thay thế đó, vì vậy bây giờ nếu tôi chạy lại giá trị, hãy chú ý 29 giá trị đó

cộng với ba người đã được thêm vào cột khác.

Vì vậy bây giờ chúng ta sẽ chuyển đổi nó thành các biến giả.

Và để làm điều đó, tôi chỉ cần sao chép và dán những gì chúng ta có trước đó.

Vì vậy, hãy để tôi sao chép.

Anh chàng này sẽ quay lại đây để làm chủ sở hữu nhà, bắt kịp tiến độ và thay thế một số hạng bằng quyền sở hữu nhà.

Vì vậy, hãy đặt anh chàng đó vào đó và đặt nó vào đó.

Được rồi, hãy tiếp tục và chạy nó.

Và bây giờ chúng ta đã thay thế quyền sở hữu nhà.

Hãy nhớ rằng bạn chỉ có thể chạy những thứ này một lần, nếu không bạn sẽ bắt đầu gặp lỗi.

Bây giờ, cột tiếp theo chúng ta sẽ xem xét là cột địa chỉ.

Vì vậy, điều chúng ta sắp làm là nếu chúng ta thực sự xem xét các ví dụ về cột địa chỉ, có vẻ như

giống như đó là địa chỉ đầy đủ của ai đó.

Vậy nó là một loại địa chỉ nào đó, không phải là điền trang.

Và có vẻ như chúng ta cũng có mã zip.

Nơi chúng tôi sắp làm là chúng tôi sẽ thực sự kỹ thuật tính năng bằng cách giải nén zip

mã từ đây.

Và có nhiều cách khác nhau để bạn có thể làm điều này.

Một cách là sử dụng kỹ thuật tương tự mà chúng tôi đã sử dụng ở đây khi chúng tôi trích xuất các số thực từ

chuỗi ba mươi sáu và sáu mươi.

Vì vậy, hãy lưu ý rằng mã zip luôn là năm chữ số cuối cùng ở đây.

Vậy chúng ta có năm chữ số cuối này, nghĩa là nếu tôi áp dụng một hàm hoặc biểu thức lambda,

một trong hai, nếu tôi nói lamda, hãy tiếp tục và xem địa chỉ đó rồi sau đó.

Lấy bắt đầu từ vị trí âm năm cho đến hết và chạy ở đó, điều đó thực sự sẽ lấy

mục thông tin cuối cùng đó.

Vì vậy, nếu tôi nhìn vào điều này, tôi có thể nói ATF.

Mã vùng.

Bằng với việc trích xuất từ ​​cột địa chỉ thực tế.

Vì vậy, chúng tôi chạy nó và chúng tôi sẽ xem xét việc biến cột mã zip này thành các biến giả

vì vậy về cơ bản chúng tôi có thể tạo một danh mục cho mỗi mã zip.

Và nếu tôi làm D.F..

Mã vùng.

Và sau đó giá trị được gọi được tính vào nó.

Bạn sẽ nhận thấy rằng thực tế không có nhiều mã zip duy nhất ở đây.

Vì vậy, chúng tôi chạy cái này và có vẻ như có tổng cộng một, hai, ba, bốn, năm, sáu, bảy,

tám, chín, 10 mã zip.

Vì vậy, điều đó không hoàn toàn vô lý khi tạo ra 10 tính năng giả từ chín tính năng bổ sung này.

cột.

Và chúng ta sẽ bỏ cái đầu tiên.

Vì vậy, chúng ta sẽ chỉ sao chép và dán đoạn mã tương tự mà chúng ta đã thực hiện ở đây.

Nhưng bây giờ chúng tôi sẽ thay thế quyền sở hữu nhà bằng cột mã zip mới mà chúng tôi đã tạo.

Vì vậy, hãy tiếp tục lấy nó và sau đó chúng ta sẽ chuyển nó vào.

Được rồi, chúng ta sẽ chạy nó và sau đó điều chúng ta sẽ làm là tiếp tục bỏ địa chỉ ban đầu đó

cột vì chúng tôi sẽ không cần nữa.

Vì vậy chúng ta sẽ nói D.F. bằng với điểm rơi F và sau đó chúng ta sẽ tiếp tục, chuyển một địa chỉ vào đó.

Cùng Acces bằng một.

OK, vậy là đã xử lý xong cột địa chỉ.

Tiếp theo là vấn đề gạch dưới D.

Vậy nếu chúng ta xem qua thông tin tính năng của anh chàng này.

Và chạy nó, bạn sẽ nhận thấy rằng thông tin tính năng này cho biết tháng mà khoản vay được tài trợ,

và nếu chúng tôi thực sự nghĩ về vấn đề mà chúng tôi đang cố gắng giải quyết thì đây là chúng tôi đang cố gắng xác định dựa trên

loại bỏ những đặc điểm đã biết của ai đó cho dù họ có trả lại khoản vay hay không, lý tưởng nhất là

điều đó sẽ xảy ra trước khi chúng tôi thực sự phát hành chúng, bởi vì nếu chúng tôi nghĩ rằng họ sẽ không

thực sự trả lại khoản vay, chúng tôi sẽ không phát hành ngay từ đầu.

Vì vậy, trên thực tế, chúng tôi sẽ không có ngày phát hành khi chúng tôi thực sự chạy mô hình.

Không phải là chúng tôi sẽ biết rằng chúng tôi đã phát hành chúng một mình.

Nếu không thì kiểu đó sẽ phá hủy toàn bộ mục đích của mô hình.

Vì vậy, đây thực sự là sự rò rỉ dữ liệu vì trên thực tế, khi áp dụng mô hình, bạn

sẽ không có ngày phát hành.

Vì vậy chúng ta sẽ tiếp tục và bỏ cột này đi.

Chúng tôi sẽ Sadaf bằng thả.

Ngày phát hành.

Dọc theo trục bằng một.

Được rồi, tiếp theo là hạn mức tín dụng sớm nhất.

Vì vậy, nếu chúng ta xem xét kỹ chức năng này hoặc tính năng này, trên thực tế, chúng ta chỉ có thể gọi thông tin tính năng

ở đây và passan sớm nhất.

Hạn mức tín dụng, đây dường như là tháng mà người đi vay báo cáo hạn mức tín dụng sớm nhất được mở.

Vì vậy, có một tính năng dấu thời gian lịch sử.

Vì vậy, điều chúng ta sắp làm là trích xuất năm từ tính năng này bằng cách sử dụng hàm appli.

Vì vậy, có rất nhiều cách khác nhau để bạn có thể làm điều này.

Nhưng trước tiên, hãy chuyển đổi nó thành một loại tính năng ngày nào đó hoặc chúng ta thực sự có thể lấy nó

dựa trên vị trí của nó.

Vì vậy, chúng ta hãy xem các ví dụ trong cột thực tế này sẽ cho biết hạn mức tín dụng sớm nhất, chạy đó

và để ý ngay bây giờ, về cơ bản nó có ba chữ cái cho một tháng, một dấu gạch ngang và sau đó là năm của

hạn mức tín dụng sớm nhất.

Vì vậy, những gì chúng ta sẽ làm ở đây là chúng ta có thể chuyển đổi nó thành ngày giờ và sau đó trích xuất bằng một thuộc tính

gọi năm hoặc chỉ lấy bốn ký tự cuối cùng trong chuỗi và chuyển đổi nó thành số nguyên.

Điều đó có lẽ dễ thực hiện hơn một chút.

Vì vậy, chúng ta sẽ tiếp tục thực hiện phương pháp đó, mặc dù cả hai phương pháp đều hoàn toàn hợp lệ.

Vì vậy, tôi có thể nói, chúng tôi áp dụng lambda và vào ngày này, hãy tiếp tục và bắt đầu từ vị trí phủ định

bốn, đi đến cuối cùng để lấy bốn ký tự cuối cùng đó và sau đó chúng tôi sẽ chuyển đổi nó thành

một số nguyên và chúng ta sẽ nói D.F. hạn mức tín dụng sớm nhất bây giờ bằng nhau.

Về vấn đề này, vì vậy chúng tôi sẽ tiếp tục thực hiện điều đó và chúng tôi sẽ xác nhận hạn mức tín dụng sớm nhất và bây giờ nếu chúng tôi thực hiện

nhìn này, chúng ta có cột mới này.

Bây giờ, hãy nhớ rằng, nếu bạn làm theo chính xác các hướng dẫn tác vụ này, chúng tôi đã yêu cầu bạn tạo một tác vụ mới

cột có tên Năm tín dụng sớm nhất và sau đó loại bỏ tính năng hạn mức tín dụng sớm nhất.

Về cơ bản nó là điều tương tự.

Nếu bạn chỉ ghi đè lên thì ghi đè lên hoặc gán sang cột mới nào đó rồi bỏ thật

tùy bạn.

Ý tưởng chính ở đây là về cơ bản chúng tôi chỉ muốn năm vì đó là thứ chúng tôi có thể làm việc và

trên thực tế, chúng ta có thể khám phá thêm điều này bằng cách tính giá trị dựa trên nó.

Và lưu ý ở đây rằng chúng tôi có các tài khoản giá trị hợp lý và chúng tôi không cần chuyển đổi tài khoản này thành tài khoản giả

các biến vì bản thân năm có thể được coi là kiểu dữ liệu liên tục.

Được rồi, tiếp tục, chuỗi bước tiếp theo sẽ chỉ là xử lý trước những thứ như phân tách treinta

cũng như mở rộng quy mô dữ liệu.

Vì vậy chúng ta sẽ tiếp tục và giải quyết vấn đề đó trong bài giảng tiếp theo.

Tôi sẽ gặp bạn ở đó.