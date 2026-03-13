# 2 -Hiểu về thư viện và tiền xử lý tập dữ liệu.en US

---

WEBVTT

Xin chào.

Vì vậy, đây là phần đầu tiên của dự án mà chúng ta sẽ xây dựng và đào tạo mô hình mạng lưới thần kinh.

Vì vậy, trước tiên chúng ta sẽ tìm hiểu về các gói và thư viện mà chúng ta sẽ sử dụng.

Phải.

Nhưng thậm chí trước khi tiếp tục với điều đó, chúng ta hãy xem qua khối mã đầu tiên mà tôi

có ngay tại đây.

Được rồi.

Đây là tôi đang nhập chức năng ổ đĩa từ Google Cloud.

Phải.

Như bạn có thể thấy.

Vậy tại sao chúng ta lại sử dụng cái này?

Lấy làm tiếc.

Tại sao chúng ta sử dụng cái này?

Là bởi vì.

Bây giờ phòng thí nghiệm của bạn không được kết nối với ổ đĩa của bạn.

Phải.

Vì vậy, nếu bạn muốn truy cập một số tệp bạn có trong ổ đĩa từ phòng thí nghiệm, bạn sẽ

cần chạy lệnh này để thư mục đó hoặc thư mục đó được gắn vào cộng tác viên của bạn tại đây.

Phải.

Vì vậy, hàm mount thực sự đang đi và nhìn thấy đường dẫn mà nó cần đi tới.

Sau đó tìm thư mục ở đó là thư mục ổ đĩa cho tôi rồi gắn thư mục ổ đĩa vào hoặc

thư mục vào phòng thí nghiệm của tôi để tôi có thể truy cập tất cả các tệp và thư mục bên trong thư mục ổ đĩa này.

Hiện nay.

Tiếp theo, bạn có thể thấy một số gói chuỗi hoặc thư viện được sử dụng để xử lý dữ liệu chuỗi

các loại.

Phải.

Và thứ tiếp theo bạn có thể thấy là thư viện phân tích.

Giờ đây, phân tích là thư viện Python tiêu chuẩn cung cấp một tập hợp các thuật toán đa dạng cho LP.

Đây là một trong những thư viện được sử dụng nhiều nhất cho NLP và ngôn ngữ học tính toán.

Bây giờ, quá trình làm sạch dữ liệu văn bản phi cấu trúc hoặc phân tích dữ liệu văn bản, chuyển đổi văn bản

dữ liệu sang các định dạng khác nhau sẽ được sử dụng sau này.

Tất cả điều đó có thể được thực hiện thông qua các lớp và hàm được xây dựng bên trong thư viện phân tích.

Vì vậy, dữ liệu văn bản trong thế giới thực là không có cấu trúc.

Nó không ở định dạng có thể được sử dụng trực tiếp vào mô hình.

Phải.

Và mặc dù dữ liệu không nhất quán nhưng dữ liệu có thể bị nhiễu.

Ý tôi là, những ký tự không mong muốn trong đó.

Phải.

Vì vậy việc xử lý dữ liệu trở thành một bước rất cần thiết, trong đó việc phân tích cung cấp rất nhiều chức năng và

các lớp học.

Và một số chức năng đó bạn sẽ thấy hoạt động khi chúng tôi tiếp tục.

Phải.

Vì vậy, đó là điều đó và tiếp theo, tôi sẽ nói thư viện quan trọng.

Thư viện quan trọng tiếp theo sẽ là Thư viện Curtis.

Phải.

Hiện tại, luôn có một số nhầm lẫn về Curtis và sau đó nhập hàm Curtis thông qua

TenorFlow.

Bây giờ nếu tôi đang viết từ Curtis Dart đang xử lý văn bản dấu chấm, đúng vậy, nếu tôi đang viết truy vấn nhập hoặc nếu

Tôi đang viết từ Curtis, điều đó có nghĩa là tôi đang sử dụng thư viện mượn tiêu chuẩn.

Đó là thư viện Curtis.

Bây giờ, nếu tôi đang viết một cái gì đó như thế này ở đây, TensorFlow dot Curtis Vì vậy, bây giờ tôi gọi Curtis

Hàm thư viện được nhúng vào thư viện TensorFlow.

Phải.

Vì vậy, có một sự khác biệt.

Bạn có thể sử dụng một số cái này và một số cái này trong cùng một khối mã hoặc trong cùng một hàm, bởi vì khi đó

nó sẽ tạo ra xung đột.

Vì vậy, nếu bạn đang sử dụng mục đích này cho một mục đích và bạn đang sử dụng mục đích này cho mục đích khác và cả hai mục đích này

các mục đích không liên quan đến nhau thì bạn có thể làm việc suôn sẻ với cả hai thư viện này.

Vậy đây là thư viện mạng lưới thần kinh, như nhiều người đã biết.

Nếu không thì Curtis là thư viện mã nguồn mở phải không?

Điều đó cung cấp giao diện Python cho mạng lưới thần kinh nhân tạo.

Bây giờ, Curtis cũng hoạt động như một giao diện cho thư viện TensorFlow, bạn có thể thấy điều đó từ đây

với những người khác nói, được rồi, điều này cũng được nhúng trong TensorFlow.

Vì thế.

À, TensorFlow cũng là một thư viện mã nguồn mở nhưng có rất nhiều task đang diễn ra

dưới mui xe.

Và TensorFlow cung cấp cả API cấp cao và cấp thấp để làm việc với các mô hình học sâu và

các mô hình khác, trong khi care chỉ cung cấp cho bạn API cấp cao.

Được rồi, đây là sự khác biệt giữa họ và cách gọi họ như thế này.

Vì vậy, gọi sự quan tâm như xin lỗi, nó như thế này hoặc như thế này có nghĩa là họ đến từ các thư viện khác nhau

và ở một mức độ nào đó, chúng thậm chí có thể có các chức năng khác nhau ngay cả đối với cùng chức năng này, phải không?

Vì vậy, một số gói mà bạn thấy ở đây một lần nữa là tất cả các gói cần thiết để xử lý dữ liệu chuỗi.

Chỉ có kiểu dữ liệu bên trong là kiểu dữ liệu văn bản.

Vì vậy, không phải dữ liệu, mà là tập dữ liệu.

Vì vậy, chúng tôi sẽ cần những thư viện này để lọc văn bản không mong muốn hoặc để có thêm thông tin.

phân tích dữ liệu văn bản.

Chúng ta sẽ cần những thư viện này như thư viện hoặc thư viện chuỗi, phải không?

Vì thế.

Được rồi.

Tôi đã bỏ lỡ thư viện trên Empire, viết tắt của Numerical Python, là một thư viện bao gồm

các đối tượng mảng đa chiều và một tập hợp các thủ tục để xử lý các vùng đó.

Giờ đây, việc sử dụng các phép toán logic và gọn gàng trên mảng có thể được thực hiện khá dễ dàng và

thậm chí theo cách rất hiệu quả.

Nhưng sau đó bạn sẽ thấy các gói ngẫu nhiên và gói dưa chua đang được sử dụng.

Về cơ bản, ngẫu nhiên có nghĩa là bạn đang sử dụng một hàm cung cấp cho tôi một số số ngẫu nhiên khi bắt đầu

và chỉ số kết thúc.

Phải.

Vì vậy, nếu bạn đang sử dụng đầu tròn, thì nó sẽ cho tôi một danh sách các số nguyên ngẫu nhiên.

Món tiếp theo là dưa chua.

Hiện tại, dưa chua là một gói giúp chúng ta lưu các mô hình, lưu bất kỳ loại dữ liệu nào bạn muốn vào

đĩa của bạn.

Vì vậy, nó phải có hai chức năng chính được sử dụng, đó là bãi chứa và tải.

Vì vậy, bạn cũng sẽ sử dụng chúng tại.

Như tôi đã nói trước đây, tập dữ liệu mà chúng tôi đang sử dụng thực tế là do Gutenberg cung cấp,

có rất nhiều bộ dữ liệu văn bản mã nguồn mở và miễn phí, thực chất là sách văn bản hoặc tiểu thuyết từ

chỉ có tác giả nổi tiếng

Phải.

Vì vậy tôi đã xác định rõ rằng cuốn sách đó là The Republic của Plato.

Một lần nữa, bạn thậm chí có thể tìm thấy tập dữ liệu tập dữ liệu cụ thể này ở phía Gutenberg.

Và cùng với đó, có rất nhiều sách mà bạn có thể sử dụng làm đầu vào để đào tạo mô hình của mình,

và thậm chí bạn có thể xem mô hình đang hoạt động như thế nào khi sử dụng từng tập dữ liệu.

Phải.

Vì vậy, tôi vừa tạo một hàm đang tải tập dữ liệu của mình.

Nhắc lại, có lẽ mình đặt tên là Republic txt nên file txt của mình mở rồi đọc qua hàm này ở đây

có chức năng dẫn đầu.

Phải.

Tôi chỉ mở tệp trước ở định dạng đọc, sau đó tôi đọc nội dung tệp vào dữ liệu văn bản của mình

thiết lập.

Vì vậy, một biến văn bản và trả về văn bản.

Tiếp theo là chức năng tổ chức của tôi.

Được rồi.

Vì vậy, trước khi tiến về phía trước, hãy để tôi chỉ.

Đúng vậy, có một số phương pháp chúng tôi sử dụng để làm sạch và sau đó xử lý trước dữ liệu, phát hiện dữ liệu.

Nghĩa là, chúng tôi thực sự thực hiện kỹ thuật tính năng trên dữ liệu cần lấy.

Để có được các tính năng mà chúng tôi có thể sử dụng làm đầu vào cho mô hình của tôi và đào tạo mô hình của tôi về các tính năng đó.

Điều đầu tiên chúng ta nên tìm hiểu và hiểu là quá trình mã hóa.

Sau khi tôi cung cấp cho bạn bản tóm tắt ngắn gọn về điều đó, chúng ta có thể tiếp tục hiểu điều gì đang xảy ra.

ở đây.

Phải?

Thực tế là có rất nhiều quy trình dọn dẹp trước khi chúng tôi tiến hành mã thông báo.

Quá trình chia nhỏ dữ liệu thuế và thành các mã thông báo riêng lẻ, có thể là câu nước

hoặc thậm chí các ký tự được gọi là mã thông báo.

Vì vậy, đây là một bước chính thức trong phân tích văn bản.

Và khi dữ liệu văn bản được chia thành các từ riêng lẻ thì nó được gọi là mã hóa.

Và đó chính xác là những gì chúng ta sẽ sử dụng.

Vì vậy, nó được triển khai bằng cách sử dụng các chức năng token hóa.

Và bạn có thể thấy rằng tôi đã nhập hàm mã thông báo vào đây từ thư viện phân tích của mình.

Nhưng trước khi hoàn toàn hiểu rõ sẽ nói chuyện.

Được rồi, token hóa đã rõ ràng rồi phải không?

Nhưng tại sao chúng ta lại cần token hóa dữ liệu đó?

Phải.

Bây giờ chúng ta cần gì cho việc đó?

Giữa học máy và hầu hết các kiến trúc học sâu, chúng ta không thể gửi hoặc nhập dữ liệu

kiểu dữ liệu chuỗi, phải không?

Vì vậy, bằng cách nào đó chúng ta cần chuyển đổi dữ liệu chuỗi thành dữ liệu số có sai sót hoặc kết thúc hoặc gấp đôi

hoặc bất cứ điều gì.

Phải.

Vậy tôi cần một con số, phải không?

Bạn chỉ cần nhập chuỗi hoặc ký tự vào mô hình của tôi.

Vì vậy, để làm được điều đó, quy trình đầu tiên là mã hóa, trong đó tôi đang cố gắng nhận được tất cả các mã thông báo có giá trị

riêng biệt để sau này tôi có thể thực hiện tác vụ kỹ thuật tính năng trên đó để chuyển đổi các mã thông báo đó hoặc

từ thành số thực tế hoặc danh sách các số.

Phải?

Vì vậy, điều này thực sự buộc tôi phải kể cho bạn về một quá trình khác, một quá trình khác.

Nạn nhân của văn bản.

Đôi khi người ta còn gọi đó là gọi.

Gọi nó là nhúng từ.

Phải.

Về cơ bản, khi chúng ta nói về token hóa, khi chúng ta nói về token hóa, ý nghĩa của nó là

rằng nếu tôi có một câu, tôi sẽ đi hôm nay.

Vì vậy nó chuyển đổi nó thành một danh sách các token đó là I.

Sau đó.

Rồi đi và rồi hôm nay.

Vì vậy, đây là Tokenization.

Điều tiếp theo mà tôi đang nói đến, đó là việc nhúng từ hoặc phân tích văn bản.

Vì vậy, điều đó xảy ra trên loại tập dữ liệu này, Đúng vậy.

Tôi sẽ nói về điều này trong video sau.

Phải.

Vậy hẹn gặp cậu ở nhé.