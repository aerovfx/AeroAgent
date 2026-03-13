# 014 Kênh Hiểu rồi! vi

---

Giáo viên: Ở phần cuối,

chúng tôi đã thêm nghĩa đen của hàm này vào đây.

Chúng tôi làm vậy để có thể đảm bảo rằng chúng tôi chỉ tạm dừng

trước khi thực hiện các lệnh gọi hàm checkLink tiếp theo.

Vì vậy, nếu chúng ta đã thêm câu lệnh time.Sleep

trực tiếp vào checkLink, điều đó sẽ đảm bảo

rằng chúng tôi cũng đã tạm dừng trong lần tìm nạp đầu tiên,

đó chắc chắn không phải là điều chúng tôi thực sự muốn.

Vì vậy nhân tiện, tôi sẽ đảm bảo rằng tôi sẽ dọn dẹp

câu lệnh time.Sleep mà tôi đã thêm tạm thời

vào chức năng checkLink ngay tại đây.

Vì vậy, điều đó sẽ biến mất.

Được rồi, bây giờ là phần cuối của phần cuối cùng,

chúng tôi nhận thấy có một thông báo cảnh báo nhỏ ở đây

xung quanh lệnh gọi hàm checkLink.

Vậy nét nguệch ngoạc màu xanh lá cây có nghĩa đây là cảnh báo,

trái ngược với một lỗi.

Bạn có thể nhận thấy rằng cảnh báo cho biết,

biến l được nắm bắt bởi hàm chữ.

Và vì vậy, chúng ta sẽ nói về chính xác điều đó có nghĩa là gì

chỉ trong một giây, nhưng vì đây là cảnh báo ngay tại đây,

điều đó có nghĩa là chúng tôi vẫn có thể biên dịch và thực thi chương trình của mình.

Vì vậy tôi nghĩ chúng ta nên biên dịch và thực thi chương trình

và hãy xem điều gì xảy ra rồi chúng ta sẽ quay lại

và tìm hiểu điều gì đang xảy ra với cảnh báo này.

Vì vậy tôi sẽ quay trở lại thiết bị đầu cuối của mình

và tôi sẽ chạy, hãy chạy main.go.

Bây giờ, bạn sẽ nhận thấy rằng năm lần tìm nạp đầu tiên

xuất hiện gần như ngay lập tức

và sau đó chúng tôi có khoảng dừng nhỏ này và sau đó chúng tôi bắt đầu nhận được

năm tuyên bố khác được in ra ở đây.

Nhưng bạn sẽ nhận thấy rằng mỗi cái đều xuất hiện

trở thành lệnh gọi hàm facebook.com,

điều đó rất thú vị

Vì vậy, có vẻ như trong tuyên bố tiếp theo này,

trong lần tìm nạp tiếp theo ngay tại đây,

nó trông giống như biến l này,

hoặc bất cứ điều gì chúng tôi thực sự đang tìm kiếm,

luôn chỉ nhận được facebook.com

làm biến tiếp theo để tìm nạp.

Vì vậy, điều này trực tiếp là do thông báo cảnh báo

mà chúng ta đang thấy ở đây,

biến phạm vi l được nắm bắt bởi hàm chữ.

Vì vậy, hãy nói về chính xác những gì đang xảy ra ở đây.

Được rồi, chúng ta sẽ xem sơ đồ.

Vậy bạn sẽ nhớ lại khi chúng ta nói chuyện

về các hàm, con trỏ và địa chỉ bộ nhớ,

chúng tôi thấy một vài sơ đồ trông mơ hồ như thế này.

Vì vậy điều này có nghĩa là để đại diện

bộ nhớ trên máy cục bộ của chúng tôi.

Chúng tôi có một số địa chỉ

và sau đó là các giá trị thực tế mà mỗi cái nắm giữ.

Bây giờ, một lần nữa, giống như các sơ đồ

chúng tôi đã xem xét trước đó,

đây không phải là sơ đồ siêu chính xác về RAM của chúng tôi,

nó chỉ là một phiên bản đơn giản hóa của nó

để giúp chúng tôi hiểu lý do tại sao chúng tôi nhìn thấy

loại lỗi này ở đây,

nơi tôi chỉ nhận được báo cáo tiếp theo

để tìm nạp facebook.com.

Vì vậy, hãy nói về những gì đang xảy ra ở đây.

Được rồi, ngay bây giờ trong quy trình Chính của chúng ta,

bất cứ khi nào chúng tôi nhận được giá trị từ kênh của mình,

chúng ta đang gán nó cho biến l này ngay tại đây phải không?

Vì vậy, chúng ta có thể tưởng tượng rằng quy trình Main của chúng ta có một biến l

nó đang trỏ vào một vị trí nào đó bên trong bộ nhớ

chứa địa chỉ của một số trang web

mà chúng tôi cần lấy.

Bây giờ, tôi đặt google.com vào đây, thực sự hoàn toàn không liên quan,

bạn biết đấy, chúng ta có thể nói đây là facebook.com, sao cũng được.

Về cơ bản, chúng ta có một địa chỉ bộ nhớ,

hoặc chúng tôi có một biến, đó là trỏ tới google.com.

Bây giờ, nếu chúng ta xem xét kỹ càng cách chúng ta đã cấu trúc

hàm này theo nghĩa đen ở đây,

bạn sẽ nhận thấy rằng chữ hàm

đang tham chiếu đến l, nằm trong phạm vi bên ngoài.

Vì vậy biến l này được định nghĩa ở phạm vi bên ngoài

của hàm ẩn danh hoặc nghĩa đen của hàm.

Và khi chúng tôi làm điều này, chúng tôi đang nói,

này, chức năng này theo nghĩa đen ở đây

đang được thực thi trong một quy trình Go riêng biệt.

Vậy điều đó có nghĩa là thói quen dành cho Trẻ em ở đây

cũng đang trỏ đến cùng một địa chỉ bộ nhớ.

Nó đang nhìn vào cùng một chuỗi.

Bây giờ, đây là nơi mọi thứ bắt đầu trở nên thực sự thú vị.

Khi chúng ta bắt đầu lặp lại điều này cho biến l ngay tại đây

và chúng tôi bắt đầu nhận được các biến hoặc chúng tôi bắt đầu,

xin lỗi, nhận tin nhắn qua kênh,

chúng tôi liên tục thay đổi giá trị được gán cho l.

Vì vậy, đôi khi đây sẽ là google.com

và vào những lúc khác, sau khi chúng tôi nhận được tin nhắn,

nó sẽ nhận một giá trị mới được chèn vào biến l,

chẳng hạn như facebook.com, nếu không chúng tôi sẽ nhận được stackoverflow.

Và tại mọi thời điểm,

cả quy trình Chính và quy trình Con

đang tham chiếu cùng một vị trí trong bộ nhớ.

Và đó là lý do tại sao chúng ta đang thấy

thông báo lỗi thực sự ngớ ngẩn này.

Đó là vì quy trình Go vẫn đang xem xét biến l,

có thể là một số biến hoàn toàn khác,

hoặc nó có thể bị thay đổi theo thời gian,

vì vậy tôi muốn nói, một giá trị hoàn toàn khác.

Vì vậy, khi chúng ta vào bên trong checkLink,

à, có lẽ ban đầu chúng ta đưa ra yêu cầu nhận

với giá trị chính xác của liên kết,

với liên kết mà chúng tôi cũng thực sự cần nói đến.

Nhưng sau khi yêu cầu thực sự được giải quyết,

liên kết ở dưới đây, vì vậy liên kết này tham chiếu ngay tại đây,

có thể đã được thay đổi khi chúng tôi xuống

đến những tài liệu tham khảo này để liên kết.

Và thông điệp cảnh báo này mà chúng ta đang thấy ở đây

về cơ bản là nói rằng, này, bạn đang tham chiếu đến một biến

được khai báo trong phạm vi bên ngoài của hàm này.

Và đó là một vấn đề lớn vì chúng tôi đang cố gắng

để tham chiếu một biến đang được duy trì hoặc sử dụng,

bởi một thói quen Go khác.

Vì vậy, trong thực tế, chúng tôi không bao giờ cố gắng tham khảo

cùng một biến bên trong hai thói quen khác nhau.

Thay vào đó, chúng ta sẽ dựa vào thực tế

rằng Go là ngôn ngữ truyền theo giá trị.

Vì vậy, bất cứ khi nào thủ tục Main có một số dữ liệu mà chúng ta muốn

chuyển sang quy trình Trẻ em khi nó được tạo,

và đó thực chất là những gì chúng tôi đang làm ở đây,

chúng tôi muốn sử dụng một số dữ liệu mà quy trình Chính có

bên trong thói quen Trẻ em

và thói quen Trẻ em cần nó khi khởi động.

Và vì vậy bất cứ khi nào điều đó xảy ra, chúng tôi sẽ đảm bảo

rằng chúng tôi cung cấp tất cả thông tin đó như một lý lẽ

đến hàm tạo nên thói quen Trẻ em này

bởi vì thay vào đó chúng ta chuyển nó vào dưới dạng đối số của hàm,

giá trị đó sẽ được sao chép vào bộ nhớ.

Hãy nhớ rằng chúng ta đã nói rằng bất cứ khi nào chúng ta bỏ qua một giá trị,

nó luôn được nhận dưới dạng bản sao trong bộ nhớ.

Và điều đó có nghĩa là,

giả sử nếu chúng ta có google.com ngay tại đây

và chúng tôi bắt đầu quy trình mới dành cho Trẻ em

và chúng tôi cung cấp google.com làm đối số,

chứ không phải là một tài liệu tham khảo bên trong phạm vi bên ngoài,

giống như hiện tại thì google.com sẽ được sao chép xuống

tới địa chỉ bộ nhớ khác ngay tại đây

và thay vào đó, quy trình Trẻ em sẽ tham chiếu địa chỉ này.

Vì vậy hiện tại, thói quen Trẻ em đã có thành tích rất ổn định

về liên kết mà nó đang cố tìm nạp,

nhưng quy trình chính có thể tiếp tục

thay đổi địa chỉ này bao nhiêu tùy ý

khi nó bắt đầu nhận các giá trị mới thông qua kênh.

Vì vậy, điều này sau đó có thể thay đổi thành facebook.com,

hoặc stackoverflow, bất kể nó là gì,

nhưng quy trình Trẻ em vẫn đang xem bản sao của nó

giá trị ban đầu, có thể là google.com.

Vậy điều này thực sự có ý nghĩa gì trong thực tế, và nhân tiện,

đôi khi biên tập viên của bạn sẽ cho bạn một gợi ý nhỏ

để nhắc nhở bạn không làm điều này.

Về cơ bản đó là những gì gợi ý này muốn nói ở đây.

Vì vậy, để khắc phục vấn đề này ở đây, chúng ta cần cung cấp l,

vì vậy liên kết chúng tôi đang cố gắng tìm nạp,

như một đối số cho hàm này theo nghĩa đen ngay tại đây.

Vì vậy chúng ta sẽ chuyển l vào như một đối số.

Hãy nhớ rằng, tập hợp dấu ngoặc đơn ở đây

là tập hợp các dấu ngoặc đơn

thực sự thực thi hàm theo nghĩa đen,

giống như chúng ta có dấu ngoặc đơn

sau một hoạt động bình thường, như thế này đây.

Vì vậy, chúng ta chuyển vào l làm đối số cho hàm,

xin lỗi, hàm số theo nghĩa đen.

Tôi cứ muốn nói hàm ẩn danh

vì tôi viết rất nhiều JavaScript,

nhưng về mặt kỹ thuật nó được gọi là chữ hàm trong Go.

Bây giờ, chúng ta phải đảm bảo rằng hàm này ở đây

được bảo rằng nó nên được mong đợi

để nhận được một liên kết làm đối số.

Vì vậy chúng ta phải chấp nhận nó như một đối số

bên trong định nghĩa hàm thực tế.

Vì vậy, ngay tại đây, chúng ta sẽ nói l, hoặc thực sự,

thật tuyệt khi nói, chuỗi liên kết.

Bạn sẽ nhận thấy chúng ta có thể gọi tên biến này ngay tại đây

hoàn toàn bất cứ điều gì chúng tôi muốn.

Và nó sẽ không xung đột

với liên kết được khai báo ở bất kỳ phạm vi bên ngoài nào ở đây,

nhưng tôi chọn gọi nó là liên kết thay vì l,

vì nếu chúng ta gọi nó là l, điều đó sẽ thực sự khó hiểu,

như, chúng ta đang đề cập đến cái nào ở đây?

Vì thế tôi sẽ, đại loại là,

tùy ý gọi nó là liên kết, thay vào đó.

Và bây giờ, bên trong checkLink, thay vì chuyển vào l,

chúng ta sẽ chuyển vào liên kết, như vậy.

Được rồi, khi chúng ta thực hiện thay đổi đó và lưu tệp,

thông báo cảnh báo biến mất.

Vì vậy bây giờ, khi chúng ta nhận được tin nhắn qua kênh c,

giá trị mới đó được gán cho l.

Chúng ta chuyển l sang nghĩa đen của hàm ngay tại đây,

chuỗi đó được sao chép vào bộ nhớ

và sau đó quy trình Go có quyền truy cập vào bản sao đó,

trái ngược với giá trị ban đầu của l.

Vì thế bây giờ tôi có thể thay đổi bao nhiêu tùy thích

và chúng ta không phải lo lắng

về việc chúng ta vẫn có thói quen đi Go

tham chiếu cùng một bản sao hoặc cùng một địa chỉ trong bộ nhớ.

Được rồi, bây giờ chúng ta hãy chuyển sang phần terminal của chúng ta.

Tôi sẽ kết thúc quá trình này bằng cách nhấn Ctrl + C

và sau đó chúng ta sẽ bắt đầu lại chương trình của mình.

Và bây giờ khi chúng tôi chạy nó,

chúng ta sẽ gặp lại năm linh hồn đó lần nữa,

chúng tôi sẽ đợi khoảng năm giây

và cuối cùng là năm người tiếp theo của chúng tôi.

Và bạn sẽ nhận thấy

rằng bây giờ chính xác tất cả chúng đều có các tên miền khác nhau.

Và theo thời gian, khi những địa chỉ khác nhau này

bắt đầu truy xuất thông tin ở các tốc độ khác nhau,

cuối cùng nó sẽ trở thành một dòng chảy liên tục

bởi vì, bạn biết đấy, cuối cùng cũng có sự tạm dừng

việc thực hiện yêu cầu sẽ, gần như, thậm chí tất cả đều được thực hiện.

Và thậm chí bây giờ khi tôi đang xem video này, có vẻ như họ,

kiểu như ngày càng loạng choạng hơn theo thời gian,

trái ngược với việc luôn cập nhật cùng một lúc.

Được rồi, đại khái là như vậy.

Một số điểm cao thực sự lớn

với các kênh có quy trình Go.

Hãy nhớ rằng, bài học lớn với Go Routines

mà chúng ta vừa học được ở đây

là chúng ta chưa bao giờ thử truy cập vào cùng một biến

từ một thói quen khác của trẻ.

Bất cứ khi nào có thể, chúng tôi chỉ chia sẻ thông tin

với quy trình con hoặc quy trình Go mới mà chúng tôi tạo,

bằng cách đưa nó vào như một đối số,

hoặc giao tiếp với trẻ qua các kênh.

Chúng tôi không bao giờ cố gắng chia sẻ các biến trực tiếp giữa chúng.

Nếu không, chúng ta sẽ có những hành vi thực sự kỳ lạ,

giống như cái chúng ta vừa thấy, điều đó chắc chắn sẽ xảy ra

kết thúc với một số thứ thực sự khó hiểu.

Được rồi, đó là khá nhiều cho lần chạy đầu tiên của chúng tôi

về các quy trình và kênh của Go.

Bây giờ, tất nhiên,

đây đều là những chủ đề rất khó hiểu,

vì vậy chúng ta hãy tạm dừng ngay bây giờ.

Chúng ta sẽ tiếp tục trong một phút nữa với một câu đố nhỏ,

chỉ để đạt được một số điểm cao và ôn lại nhanh chóng

về các thói quen của Go là gì và các kênh là gì.

Vì vậy, hãy nghỉ nhanh và chúng ta sẽ đi đến bài kiểm tra đó chỉ sau một giây.