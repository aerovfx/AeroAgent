# 014 Kênh Hiểu rồi! vi

---

Trong phần cuối cùng, chúng tôi đã bổ sung thêm chức năng này theo nghĩa đen tại đây, chúng tôi đã làm

điều đó để có thể chắc chắn rằng chúng tôi chỉ tạm dừng trước khi theo dõi kiểm tra liên kết hàm gọi lệnh.

Vì vậy, nếu chúng tôi đã trực tiếp thêm lệnh time sleep vào kiểm tra liên kết, điều đó chắc chắn rằng

chúng tôi cũng phải tạm dừng trong lần tải ban đầu, điều này chắc chắn không phải là những gì chúng tôi thực sự mong muốn.

Vì vậy, tôi chắc chắn rằng tôi sẽ xóa lệnh thời gian ngủ mà tôi đã tạm thời bổ sung vào chức năng

khả năng kiểm tra liên kết ngay tại đây.

Vì vậy, điều đó sẽ biến mất.

Bây giờ, ở phần cuối cùng, chúng tôi nhận thấy rằng có một thông báo cảnh báo nhỏ ở xung quanh đây

xung quanh chức năng kiểm tra lệnh gọi.

Vì vậy, chữ nguệch ngoạc màu xanh lá cây có nghĩa đây là một cảnh báo trái ngược với một lỗi.

Bạn có thể nhận thấy rằng cảnh báo cho biết các biến thể được nắm bắt theo nghĩa đen của hàm.

Và vì vậy, chúng tôi sẽ nói về chính xác điều đó có nghĩa là gì chỉ trong một giây.

Nhưng bởi vì đây là một cảnh báo ngay tại đây, nó có nghĩa là chúng ta vẫn có thể biên dịch và thực hiện chương trình của mình.

Vì vậy, tôi nghĩ chúng ta nên biên dịch và thực hiện chương trình này và chỉ cần xem điều gì sẽ xảy ra và sau đó chúng ta sẽ quay

lại và tìm hiểu điều gì đang xảy ra với cảnh báo này.

Vì vậy, tôi sẽ lại một thiết bị cuối cùng của mình và tôi sẽ chạy, chạy, chạy, chạy chính.

Bây giờ bạn sẽ nhận thấy rằng năm lần tải đầu tiên xuất hiện gần như ngay lập tức.

Và sau đó chúng tôi tạm dừng một chút điều này và sau đó chúng tôi bắt đầu ra các lệnh khác ở đây.

Nhưng bạn sẽ nhận thấy rằng mỗi người trong số họ phải như là một lệnh gọi chức năng dot com của Facebook, điều này rất thú vị.

Vì vậy, có vẻ như trong lệnh tiếp theo này, trong lần tải tiếp theo ngay tại đây, có vẻ như biến l này hoặc bất cứ điều gì

điều chúng tôi thực sự đang thực hiện là đã nhận được facebook. com làm biến tiếp theo để

find loading.

Vì vậy, điều này trực tiếp là thông báo cảnh báo mà chúng ta đang thấy ngay tại đây.

Biến phạm vi L được ghi lại bởi hàm đen.

Vì vậy, hãy nói về chính xác những gì đang xảy ra ở đây.

Được chứ.

Vì vậy, chúng tôi sẽ xem xét một sơ đồ.

Vì vậy, bạn sẽ nhớ lại khi chúng tôi nói về các hàm, con trỏ và bộ nhớ địa chỉ, chúng tôi đã tìm thấy một

một số sơ đồ mơ hồ như thế này.

Vì vậy, điều này có nghĩa là đại diện cho bộ nhớ trên máy cục bộ của chúng tôi.

Chúng tôi có một số địa chỉ và sau đó là các giá trị thực tế có giá trị mà mỗi địa chỉ nắm giữ.

Bây giờ, một lần nữa, giống như các sơ đồ chúng tôi đã xem trước đây, đây không phải là một sơ đồ siêu chính

xác định về RAM của chúng ta.

Nó chỉ là một loại phiên bản đơn giản hóa của nó để giúp chúng tôi hiểu lý do tại sao chúng tôi gặp phải loại lỗi này ngay tại đây, nơi

tôi chỉ nhận được các tuyên bố tiếp theo để tìm tải Facebook. com.

Vì vậy, hãy nói về những gì đang xảy ra ở đây.

Vì vậy, ngay bây giờ, trong quy trình chính của chúng tôi, bất cứ khi nào chúng tôi nhận được giá trị từ kênh của mình, chúng tôi sẽ chỉ định giá trị

đó cho biến này.

L Ngay đây.

Đúng?

Vì vậy, họ có thể tưởng tượng rằng thói quen chính của họ có một biến thể.

Nó đang được đặt vào một số vị trí trong bộ nhớ chứa địa chỉ của một số trang web mà chúng tôi

cần tải.

Bây giờ, tôi cài đặt google. com ở đây thực sự hoàn toàn không liên quan.

Có thể nói đây là facebook. com, bất cứ điều gì.

Về cơ bản, chúng tôi có một bộ nhớ địa chỉ hoặc chúng tôi có một biến thể đang truy cập vào google. com.

Bây giờ, nếu chúng ta xem xét xét rất kỹ cách chúng ta đã cấu trúc hàm này theo nghĩa đen

ngay tại đây, bạn sẽ nhận thấy rằng hàm nghĩa đen đang tham chiếu đến L, nằm trong phạm vi bên ngoài.

Vì vậy, biến L này được định nghĩa trong phạm vi bên ngoài của hàm ẩn hoặc hàm theo nghĩa.

Và vì vậy khi chúng tôi làm điều này, chúng tôi đang nói, this, hàm this nghĩa đen ngay tại đây đang

được thực thi trong một quy trình riêng biệt.

Vì vậy, điều đó có nghĩa là thói quen trẻ em ngay tại đây cũng đang trỏ đến cùng một địa chỉ bộ nhớ.

Nó đang nhìn vào cùng một chuỗi.

Bây giờ, đây là nơi mọi thứ bắt đầu trở nên thực sự thú vị khi chúng ta bắt đầu lặp lại điều này cho biến L ngay tại

đây và chúng tôi bắt đầu nhận các biến hoặc chúng tôi bắt đầu nhận thông báo qua kênh,

chúng tôi liên tục thay đổi giá trị được phân bổ cho L.

Vì vậy, trùng lặp khi điều này sẽ được google. com và sau đó vào những thời điểm khác sau khi chúng tôi nhận được

thông báo, nó sẽ nhận được một giá trị mới được chèn vào biến l như facebook. com hoặc chúng tôi sẽ nhận được tràn ngăn xếp.

Và tại mọi thời điểm, các thói quen chính và thói quen đều tham chiếu cùng một vị trí trong bộ

nhớ.

Và đó là lý do tại sao chúng tôi thấy thông báo lỗi thực sự ngốc nghếch này.

Đó là bởi vì thói quen vẫn đang xem xét biến L, có thể là một số biến khác hoàn toàn khác, hoặc

it may be thay đổi theo thời gian.

Vì vậy, tôi muốn nói giá trị hoàn toàn khác nhau.

Vì vậy, khi chúng tôi đi xuống bên trong quá trình kiểm tra liên kết, chúng tôi có thể cấm chúng tôi thực hiện yêu cầu nhận giá trị

chính xác của liên kết với liên kết mà chúng tôi thực sự muốn nói đến.

Nhưng sau khi yêu cầu thực sự được giải quyết, liên kết ở đây.

Vì vậy, các liên kết tham chiếu này ngay tại đây có thể đã được thay đổi vào thời điểm chúng tôi tải xuống các tham chiếu này

for link.

Và vì vậy, thông báo cảnh báo mà chúng tôi đang tìm thấy ngay tại đây về cơ bản nói rằng, bạn đang tham gia

reference đến một biến được khai báo bên ngoài phạm vi của hàm này.

Và đó là một vấn đề lớn vì chúng tôi đang cố gắng tham khảo một biến thể đang được duy trì hoặc sử dụng

được sử dụng bởi một hoạt động khác.

Vì vậy, trong thực tế, chúng tôi không bảo giờ cố gắng tham khảo cùng một biến thể trong hai thói quen khác nhau.

Thay vào đó, chúng tôi sẽ dựa trên thực tế rằng đi là một ngôn ngữ có giá trị đi qua.

Vì vậy, bất cứ khi nào quy trình chính có nhiều dữ liệu mà chúng tôi muốn chuyển cho quy trình khi nó được tạo và về cơ sở dữ liệu

bản này là những gì chúng tôi đang làm ngay tại đây.

Chúng tôi muốn sử dụng một số dữ liệu mà quy trình chính có trong quy trình trẻ em và quy trình trẻ

em cần nó vào thời điểm khởi động.

Và vì vậy, bất kể điều gì xảy ra, chúng tôi chắc chắn rằng chúng tôi cũng

Cung cấp tất cả thông tin dưới dạng đối số cho hàm tạo quy trình này, bởi vì chúng tôi chuyển nó sang dạng đối số bên dưới của hàm.

Thay vào đó, giá trị đó sẽ được sao chép vào bộ nhớ.

Hãy nhớ rằng, chúng tôi đã nói rằng bất cứ khi nào chúng tôi chuyển một giá trị, nó luôn được nhận dưới dạng một bản sao trong bộ nhớ.

Và điều đó có nghĩa là nếu chúng ta nói có Google. com ngay tại đây và chúng tôi bắt đầu

thói quen trẻ em mới và chúng tôi cung cấp cho google. com as a đối số không phải là một tham chiếu bên trong phạm vi

bên ngoài như hiện tại.

Sau đó, Google. com sẽ được sao chép xuống địa chỉ khác của bộ nhớ này ngay tại đây và thay vào đó

ở đó, quen thuộc sẽ tham chiếu đến địa chỉ này.

Vì vậy, hiện nay quy trình trẻ em đã có một bản ghi rất ổn định về liên kết mà nó đang cố gắng tìm tải.

Nhưng quy trình chính có thể tiếp tục thay đổi tùy chọn địa chỉ này khi nó bắt đầu nhận các

thông tin mới có giá trị qua kênh.

Vì vậy, điều này sau đó có thể thay đổi Facebook. com hoặc StackOverflow, bất kể nó là gì.

Nhưng thói quen của trẻ em vẫn đang xem xét bản sao của giá trị ban đầu, có thể là google. com.

Vì vậy, điều này thực sự có ý nghĩa như thế nào trong thực tế và nhân tiện, đôi khi trình biên dịch của bạn sẽ đưa ra một chút

tip tip để nhắc nhở bạn không nên làm điều này.

Về cơ bản đó là những gì gợi ý này đang nói ngay ở đây.

Vì vậy, để giải quyết vấn đề này ngay tại đây, chúng tôi cần cung cấp l.

Vì vậy, liên kết mà chúng tôi đang cố gắng nỗ lực tìm kiếm lý lẽ cho hàm nghĩa đen ngay tại đây.

Vì vậy, chúng tôi sẽ chuyển L như một đối số.

Hãy ghi nhớ tập hợp các dấu ngoặc này ngay tại đây là một tập hợp các dấu ngoặc đơn thực thi hàm theo nghĩa đen, giống nhau

như chúng ta có các dấu ngoặc đơn sau một hàm bình thường như thế này ngay tại đây.

Vì vậy, chúng tôi đang chuyển sang L dưới dạng một đối số cho hàm, tôi xin lỗi, hàm theo nghĩa.

Tôi tiếp tục muốn nói hàm ẩn danh vì tôi viết rất nhiều JavaScript, nhưng về mặt kỹ thuật nó được gọi

là một hàm đen và đi.

Bây giờ chúng ta phải chắc chắn rằng chức năng này ngay tại đây được thông báo rằng nó sẽ được nhận

một liên kết như một đối số.

Vì vậy, chúng ta phải nhận nó như một đối số trong định nghĩa hàm thực tế.

Vì vậy, ngay tại đây chúng tôi sẽ nói L hoặc chúng tôi thực sự rất hay khi nói chuỗi liên kết.

Bạn sẽ nhận thấy rằng chúng tôi có thể gọi tên biến này ngay tại đây, hoàn toàn bất cứ điều gì chúng tôi muốn.

Và nó sẽ không nhất quán với độ dài được khai báo ở bất kỳ vi phạm nào bên ngoài đây.

Nhưng tôi đang chọn nó là liên kết trái ngược với L, bởi vì nếu chúng tôi gọi là L, điều đó sẽ thực sự sự thật

Khó hiểu.

Giống như chúng tôi đang tham khảo ở đây?

Vì vậy, tôi sẽ chỉ tiện ích gọi nó là liên kết.

Và bây giờ, bên trong Liên kết Kiểm tra thay vì chuyển vào L, chúng ta cũng sẽ chuyển vào liên kết đó.

Được chứ.

Vì vậy, khi chúng tôi thực hiện thay đổi và lưu tệp, thông báo cảnh báo sẽ bị mất.

Vì vậy, hiện tại chúng tôi đã nhận được thông báo qua Kênh C rằng giá trị mới được phân bổ cho L, chúng tôi chuyển L sang hàm

nghĩa đen ngay tại đây.

Chuỗi đó được sao chép vào bộ nhớ và sau đó quy trình có quyền truy cập vào bản sao trái ngược với giá trị

cấm đầu của L.

Vì vậy, hiện tại L có thể thay đổi tùy chọn.

Và chúng tôi không phải lo lắng về việc vẫn có thói quen tham chiếu đến cùng một bản sao hoặc cùng một địa chỉ trong

bộ nhớ.

Vì vậy, bây giờ chúng tôi chuyển sang thiết bị đầu cuối của chúng tôi.

Tôi sẽ kết thúc quá trình này bằng cách nhấn nút điều khiển C và sau đó chúng tôi sẽ bắt đầu lại chương trình của mình.

Và bây giờ khi chúng tôi chạy nó, chúng tôi sẽ tìm lại số lần tải đó.

Chúng tôi sẽ mong đợi 5 giây hoặc lâu hơn và cuối cùng sẽ có năm giây tiếp theo của chúng tôi và bạn sẽ nhận được

nhận thấy rằng bây giờ chính xác là tất cả chúng đều có các miền khác nhau.

Và theo thời gian, khi các địa chỉ khác nhau này bắt đầu truy xuất thông tin ở các tốc độ khác nhau, cuối cùng

nó sẽ biến thành một dòng liên tục vì công việc cuối cùng tạm dừng thực hiện yêu cầu

will drop all.

Và ngay bây giờ, khi tôi đang theo dõi điều này, có vẻ như chúng tôi càng ngày càng

chênh lệch theo thời gian, trái ngược với việc cập nhật cùng một lúc.

Vì vậy, có khá nhiều đó.

Một số điểm cao thực sự cho các kênh, với hoạt động của quy trình.

Hãy ghi nhớ bài học lớn với thói quen đi mà chúng ta vừa học được ngay sau đây là chúng ta

không bao giờ cố gắng truy cập vào cùng một biến thể từ một thói quen trẻ em khác bất cứ khi nào có thể.

Chúng tôi chỉ chia sẻ thông tin về một thói quen trẻ em hoặc một thói quen đi mới mà chúng tôi tạo ra bằng cách chuyển đổi

nó vào như một cuộc thảo luận hoặc giao tiếp với thói quen trẻ em qua các kênh.

Chúng tôi không bao giờ cố gắng chia sẻ các biến trực tiếp giữa chúng.

Nếu không, chúng tôi sẽ có một số hành động thực sự kỳ lạ giống như hành vi mà chúng tôi vừa thấy,

điều đó chắc chắn sẽ dẫn đến một số thực sự khó hiểu.

Vì vậy, có khá nhiều hoạt động ban đầu của chúng tôi về các kênh và quy trình hoạt động.

Tất nhiên, đây là cả hai chủ đề rất khó hiểu.

Vì vậy, chúng tôi tạm dừng ngay lúc này.

Chúng ta sẽ tiếp tục chỉ sau một phút với một câu tranh luận nhỏ chỉ để đạt được một số điểm

cao trong bản cập nhật cập nhật nhanh chóng về quá trình hoạt động và kênh là gì.

Vì vậy, hãy nhanh chóng nghỉ ngơi và chúng tôi sẽ đến bài kiểm tra đó chỉ sau một giây.