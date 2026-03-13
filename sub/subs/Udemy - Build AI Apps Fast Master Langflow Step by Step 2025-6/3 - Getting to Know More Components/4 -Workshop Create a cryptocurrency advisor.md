# 4 -Workshop Tạo một cố vấn tiền điện tử đã dịch

---

Đã đến lúc bắt đầu.

Hãy vui vẻ và tạo một dự án thực tế hơn để thực hành những gì chúng ta đã học

các thành phần ở bài học trước.

Để làm được điều này, tôi đã tạo một dự án có tên là Cố vấn tiền điện tử.

Mục tiêu của quy trình công việc này là gì?

Mục đích chính là lấy thông tin từ dịch vụ này có tên là KindCup, có

trên trang chính của nó, hiển thị thông tin về các loại tiền điện tử khác nhau.

Nó cung cấp các thông tin quan trọng như giá, vốn hóa thị trường, khối lượng giao dịch cuối cùng

24 giờ và phần trăm thay đổi của loại tiền điện tử đó trong cùng khoảng thời gian đó.

Ưu điểm lớn của trang web này là nó cho phép bạn truy cập API miễn phí.

Thậm chí, bạn có thể thực hiện một số yêu cầu hàng tháng đối với API này.

Tôi đã tạo một tài khoản để sử dụng cho bài tập này và khi bạn truy cập API

tài liệu, bạn có thể xem trong phần mô tả số lượng yêu cầu chúng tôi có thể thực hiện cho mỗi

tháng với một tài khoản miễn phí.

Nếu bạn muốn phát triển một ứng dụng phức tạp hơn, bạn có thể mua dịch vụ của họ để bắt đầu

tới 3 triệu tín chỉ mỗi tháng.

Trong trường hợp của họ, tài khoản miễn phí này là đủ.

Bạn có thể tạo một cái miễn phí như tôi đã đề cập.

Và như một phần của tài liệu, chúng tôi có một bộ API hoặc điểm cuối mà chúng tôi có thể kết nối

để có được thông tin về tiền điện tử.

Ví dụ: chúng ta có thể lấy danh sách các tài sản tiền điện tử, tham khảo một loại tiền điện tử, truy cập

lịch sử tiền điện tử, trong số các điểm cuối có sẵn khác.

Chúng tôi quan tâm đến việc kiểm tra lịch sử của tiền điện tử để tìm hiểu về hiệu suất của nó

và xác định xem đây có phải là thời điểm tốt để mua hay không.

Bây giờ, vì tôi đã đăng nhập trước đó thông qua ủy quyền cho tôi, ID của tôi hoặc dịch vụ

khóa do trang web cung cấp, tôi có thể thực hiện truy vấn trên cùng một trang.

Vì vậy nếu mình click vào tryout rồi chọn thực thi thì ở đây mình cần nhập các thông tin như sau

làm tên của tiền điện tử, ví dụ như Bitcoin.

Ví dụ: chúng tôi chọn khoảng thời gian vì người ta thấy rằng nó hiển thị cho chúng tôi khoảng thời gian tính bằng ngày

và sau đó chúng tôi nhấp vào thực hiện.

Điều này bắt đầu quá trình lấy thông tin về tiền điện tử Bitcoin.

Tôi tăng kích thước này lên một chút.

Chúng ta đã có dữ liệu chưa?

Chúng tôi có ngày truy vấn tiền điện tử, thời gian và giá bằng đô la của tiền điện tử đó.

Bằng cách này, chúng tôi có được lịch sử của tiền điện tử và chúng tôi có thể thấy nó hoạt động tốt hay kém như thế nào

trong một khoảng thời gian nhất định.

Vì vậy, đây là thông tin chúng tôi muốn nhận được.

Chúng tôi muốn truy vấn mô hình AI về tiền điện tử để nó trích xuất thông tin liên quan

và cho chúng ta biết liệu có nên mua nó hay không.

Chúng ta làm điều này như thế nào?

Chúng ta đi đến langflow và điều đầu tiên chúng ta sẽ làm để bắt đầu luồng của mình là tạo kiểu nhập văn bản

thành phần cho phép chúng ta viết một tin nhắn.

Ví dụ: hãy cho tôi biết về Bitcoin.

Giả sử đây là truy vấn của người dùng, hãy lưu ý rằng tôi không biết.

Tôi không biết chính xác tên của loại tiền điện tử hoặc cách thực hiện truy vấn tới API, nhưng tôi

muốn là người dùng có thể nhập bất kỳ văn bản nào về tiền điện tử và nhận thông tin

thông qua dòng chảy.

Vì vậy, khi chúng ta có văn bản đầu vào này, điều lý tưởng là định dạng nó để trích xuất tiền điện tử

chúng tôi quan tâm đến.

Để làm được điều đó, chúng ta sẽ sử dụng một thành phần có tên StructShirtOutput mà chúng ta đã phân tích trước đó và nó

cho phép chúng tôi sử dụng mô hình AI để có được lược đồ đầu ra.

Bây giờ, hãy kết nối tin nhắn này với tin nhắn đầu vào.

Chúng tôi cũng sẽ kết nối một mô hình trí tuệ nhân tạo, trong trường hợp này là ở trên

AI.

Bạn có thể sử dụng một mô hình khác nếu bạn có quyền truy cập vào một mô hình.

Hãy kết nối mô hình ngôn ngữ với StructShirtOutput và chỉ định rằng chúng ta muốn

tạo một bảng đầu ra.

Bạn ơi, bạn có thể tạo tất cả các trường bạn muốn.

Trong trường hợp của tôi, tôi sẽ tạo một trường đầu tiên có tên là CryptoName và mô tả của nó sẽ là

mô tả nhiều hơn một chút.

Trong trường hợp này, họ đã xác định được tiền điện tử.

Ưu điểm lớn của việc này là chúng tôi có thể đưa vào các ví dụ để mô hình AI được hướng dẫn và

cung cấp chính xác những gì chúng ta cần.

Trong trường hợp này, API yêu cầu một định dạng cụ thể, tên tiền điện tử, trong chữ thường,

cùng với xác định của nó.

Ở đây, chúng tôi sẽ đưa ra một số ví dụ về giao diện của các mã nhận dạng này.

Hãy để những cái này ở đây và đây sẽ là tên của tiền điện tử.

Thủy triều sẽ là một chuỗi và sẽ đại diện cho một giá trị duy nhất.

Nó nằm ở trường thứ hai có tên là CryptoSymbol.

Ở đây, chúng tôi sẽ nêu rõ rằng mô tả sẽ là biểu tượng của tiền điện tử.

Ví dụ: liên kết, một hộp, trong số những thứ khác.

Điều này sẽ cho phép chúng tôi có được tên của tiền điện tử.

Tại đây, bạn có thể thêm bao nhiêu dữ liệu tùy thích.

Vì mô hình AI có kiến ​​thức chứ không chỉ về.

Thông tin bạn cung cấp từ văn bản nhưng nó cũng biết tên của tiền điện tử,

giá trị của nó tại một thời điểm nhất định, v.v.

Nó có thể lấy thông tin ngay cả khi nó không được tìm thấy trong văn bản đầu vào.

Nó có thể tạo ra thông tin mà nó đã biết.

Đó là lý do tại sao chúng tôi cung cấp cặp cột này làm ví dụ.

Hãy lưu kết quả đầu ra và kiểm tra xem nó có hoạt động chính xác không.

Chúng tôi chạy thành phần và đợi vài giây.

Bạn có thể thấy rằng sau vài giây, quá trình thực thi đã thành công.

Nếu chúng tôi kiểm tra khung dữ liệu, bạn sẽ thấy rằng chúng tôi đang lấy chính xác tên tiền điện tử

và CryptoSymbol.

Ở đây, chúng ta có tên của loại tiền điện tử, Bitcoin và ký hiệu của nó, BTC.

Một khía cạnh quan trọng cần xem xét là các mô hình AI khác nhau có thể cung cấp các phản hồi khác nhau.

Ví dụ: ta đổi GPD của model mini thành GPD40 và chạy linh kiện tương tự

với cùng cấu hình.

Bây giờ hãy kiểm tra đầu ra.

Bạn có thể nhận thấy rằng trong trường hợp cụ thể này, chúng tôi không nhận được kết quả như trước.

Bây giờ một cột có tên Tin nhắn xuất hiện, cột này thậm chí không chứa thông tin mà chúng tôi

mong đợi.

Vì vậy, nếu bạn muốn lặp lại bài tập này, tôi khuyên bạn nên chọn mẫu mini GPD40

để có được kết quả tương tự.

Khi chúng tôi có được tên tiền điện tử bằng thành phần này, bước tiếp theo là tạo

URL để chúng tôi có thể kết nối với một tập hợp các URL này.

Nếu kiểm tra tài liệu, chúng tôi sẽ tìm thấy chuỗi cuộn tròn này hướng dẫn chúng tôi cách kết nối

đến dịch vụ.

Điều này cung cấp một URL nơi bạn có thể thấy địa chỉ bao gồm tên tiền điện tử mà chúng tôi có

từ thành phần trước đó.

Tôi sẽ sao chép URL này được tìm thấy giữa các dấu ngoặc đơn và sau đó sử dụng một thành phần có tên

trình phân tích cú pháp mà chúng ta đã thấy trước đây.

Điều này cho phép chúng tôi trích xuất một điểm dữ liệu duy nhất và tạo một mẫu văn bản để chuyển sang điểm khác

thành phần.

Trong trường hợp này, chúng tôi quan tâm đến việc đưa đầu ra vào khung dữ liệu, kết nối

nó với thành phần tiếp theo và như bạn có thể nhớ lại, việc chạy thành phần này mang lại cho chúng ta những điều này

hai cột, tên mật mã và ký hiệu mật mã, là dữ liệu chúng ta có thể trích xuất như một phần của

mẫu thành phần phân tích cú pháp.

Tôi sẽ mở thành phần này và thay vì văn bản chúng ta có trước đó, tôi sẽ dán

URL tôi đã đề cập trước đó.

Tôi sẽ dán nó và thay thế tên của tiền điện tử bằng một biến có tên là tên tiền điện tử.

Hãy nhớ rằng, đây là một trong những trường tạo thành một phần đầu ra từ thành phần trước đó,

tên mật mã này.

Vì vậy, với thành phần này, chúng ta có thể tạo mẫu này và hoán đổi tên tiền điện tử lấy tiền điện tử

tên thu được từ thành phần trước, tạo URL mà chúng tôi sẽ sử dụng trong thành phần tiếp theo.

Thành phần tiếp theo chúng ta sẽ sử dụng có nhiệm vụ cho phép chúng ta đưa ra một yêu cầu hoặc một

truy vấn cho phép chúng tôi truy cập điểm cuối của dịch vụ.

Để làm được điều đó, chúng tôi sẽ sử dụng thành phần có tên là yêu cầu API mà chúng tôi sẽ gán URL cho

chúng tôi đã thu được và tạo ra trước đó.

Ở đây chúng ta cần thực hiện một số cấu hình bổ sung.

Bạn có thể thấy rằng lệnh chữa bệnh này cho biết nó đang mong đợi hai tiêu đề, một tên ngoại trừ

và một cái khác gọi là ủy quyền.

Vì vậy, quay lại thành phần yêu cầu API, tôi nối thêm phần điều khiển và đây là một phần

trong các điều khiển của thành phần này, chúng tôi tìm thấy thuộc tính tiêu đề.

Đó là một cái bàn.

Hãy mở nó và ở đây chúng ta có thể thêm tất cả các tiêu đề chúng ta cần.

Tiêu đề đầu tiên của chúng tôi được đặt tên là chấp nhận.

Vì vậy, hãy thêm nó.

Tôi cũng bao gồm giá trị là một phần của chuỗi này, đó là JSON của ứng dụng.

Và cuối cùng, chúng tôi thêm ủy quyền tên tiêu đề thứ hai với mã thông báo râu tương ứng

giá trị của dịch vụ truy cập cổng thông tin này.

Bây giờ hãy thay thế giá trị vì chúng ta có các thông tin in đậm một cách chính xác.

Nhấp vào lưu và bằng cách này, chúng tôi đã định cấu hình dịch vụ để bao gồm các tiêu đề in đậm.

Vì vậy, chúng tôi sẽ không có bất kỳ vấn đề.

Hãy xem những lời này có đúng không nhé.

Hãy chạy truy vấn, thực thi thành phần này, đợi vài giây, chúng tôi sẽ nhận được phản hồi chính xác.

Hãy kiểm tra dữ liệu.

Và ở đây bạn có thể thấy rằng chúng ta có kết quả chính xác với tất cả những dữ liệu này, một phần của

phản hồi thu được từ điểm cuối và sẽ cho phép mô hình AI xác định mức độ thuận tiện

có nên mua tiền điện tử hay không.

Bây giờ bạn có thể thấy rằng có nhiều điểm dữ liệu xuất hiện trong kết quả, điều này có thể gây ra lỗi

với mô hình AI vì nó có thể không xử lý được tất cả chúng.

Nhưng chúng tôi quan tâm đến việc chỉ thu thập những hồ sơ gần đây nhất, chẳng hạn như từ

tháng trước để đánh giá mức độ tiện lợi hay mạnh mẽ của tiền điện tử.

Để áp dụng bộ lọc, hãy nhớ rằng bộ lọc đó là một phần của danh mục xử lý.

Có một số bộ lọc chúng ta có thể sử dụng.

Trong trường hợp của chúng tôi, chúng tôi sử dụng bộ lọc Alamda để chọn kết quả mới nhất bằng hướng dẫn tự nhiên.

Hãy kết nối nút dữ liệu từ yêu cầu API với nút dữ liệu trong bộ lọc Lamda.

Chúng ta phải tạo thành phần OpenAI mới để thành phần bộ lọc Lambda hoạt động bình thường.

Hãy cho biết rằng chúng tôi đã sử dụng mô hình mini.

Hãy đặt đây là mô hình ngôn ngữ AI.

Kết nối nó với bộ lọc Lambda và cuối cùng, đến phần hướng dẫn, tôi sẽ mở tin nhắn này

hoặc chỉnh sửa nội dung văn bản và cho biết lời nhắc sẽ lấy được dữ liệu lịch sử

đối với tiền điện tử được đặt hàng từ ngày gần đây nhất đến ngày cũ nhất.

Điều này sẽ dẫn đến việc chúng tôi nhận được tập hợp các bản ghi đã được lọc.

Hãy kiểm tra xem điều này có hoạt động chính xác không.

Hãy đợi một vài giây.

Hãy phân tích kết quả.

Bạn có thể thấy rằng chúng tôi đang nhận được thành công các kết quả gần đây nhất.

Và cuối cùng, dữ liệu cũ nhất sẽ xuất hiện, rất thuận tiện cho trường hợp sử dụng của chúng ta.

Ngoài ra, bạn có thể nhận thấy rằng phản hồi hiện được định dạng theo cách phù hợp hơn.

Bây giờ chúng ta có từng cột, cho phép chúng ta truy cập vào bất kỳ trường nào trong số này trong trường hợp

chúng tôi cần họ.

Trong trường hợp của chúng tôi, chúng tôi muốn chuyển tất cả thông tin này sang mô hình AI.

Làm thế nào chúng ta có thể đạt được điều này?

Chúng ta sẽ sử dụng một thành phần có tên là trình phân tích cú pháp mà chúng ta đã thấy trước đó.

Điều này cho phép chúng tôi định dạng khung dữ liệu và chuyển đổi nó thành chuỗi bằng trình phân tích cú pháp bằng cách sử dụng

tùy chọn xâu chuỗi.

Trong video trước, chúng tôi đã giải thích cách sử dụng trình phân tích cú pháp để tạo mẫu văn bản.

Trong trường hợp cụ thể này, chúng tôi sẽ không làm điều đó.

Và điều chúng ta sắp làm là truyền chuỗi JSON như hiện tại, mặc dù chúng ta không thể nhìn thấy

nó ở đây vì chúng tôi đang sử dụng bố cục bảng để hiển thị rõ hơn.

Điều quan trọng đối với chúng tôi là chuyển đổi nó sang định dạng JSON.

Nếu chúng tôi bật tùy chọn này có tên là stringify, điều này sẽ cho phép dữ liệu được tạo bởi phiên bản trước

thành phần được chuyển dưới dạng chuỗi văn bản.

Bạn sẽ nhận thấy rằng ngay cả loại nút cũng thay đổi.

Bây giờ chúng tôi không có đầu ra văn bản.

Thay vào đó, đầu ra trong trường hợp này sẽ là một đối tượng JSON.

Trên thực tế, chúng ta có thể nhanh chóng kiểm tra điều này.

Tôi chạy các thành phần.

Chúng tôi kiểm tra đầu ra và bạn có thể thấy rằng tất cả thông tin được thu thập ở đây nhờ

việc sử dụng thành phần trình phân tích cú pháp này được đặt ở chế độ xâu chuỗi.

Bây giờ chúng ta có thông tin tên tiền điện tử cũng như dữ liệu lịch sử của tiền điện tử.

Đó là bước tiếp theo, về cơ bản là chuẩn bị lời nhắc cho mô hình AI.

Để đạt được điều này, chúng ta đã xem xét thành phần có tên là nhắc nhở, thành phần này cho phép chúng ta

để tạo mẫu gửi đến mô hình trí tuệ nhân tạo.

Vì vậy, điều chúng ta sẽ làm tiếp theo là thay đổi mẫu.

Ở đây, trước đây tôi đã chuẩn bị một lời nhắc có nội dung: bạn là chuyên gia phiên dịch

xu hướng thị trường tài chính, đặc biệt là hiệu suất lịch sử của tiền điện tử.

Tôi cần bạn phân tích dữ liệu lịch sử của loại tiền điện tử mà tôi sẽ chỉ định tên

bên dưới.

Hãy cho tôi biết nên mua hay không mua tiền điện tử vào lúc này.

Ở đây chúng tôi chỉ định tiền điện tử, là một biến và chúng tôi cũng bao gồm các loại tiền điện tử

lịch sử.

Đây là hai phần dữ liệu chúng tôi đã thu được trước đó.

Với điều này, chúng tôi kiểm tra, lưu các thay đổi và bây giờ nó xuất hiện trong cả hai trường như một phần của

nhắc nhở.

Bây giờ chúng tôi kết nối các lĩnh vực này.

Chúng tôi kết nối đầu ra với lịch sử với trường này được gọi là lịch sử, trường này đã có sẵn

đã được tạo ra.

Mặt khác, tên của tiền điện tử, như bạn có thể nhớ, được tạo theo cấu trúc

đầu ra.

Tuy nhiên, kết quả đầu ra có cấu trúc này, như bạn nhớ lại, trả về hai phần dữ liệu, tên của

tiền điện tử và biểu tượng của nó.

Do đó, nếu chúng tôi chỉ muốn trích xuất tên của tiền điện tử, chúng tôi có thể sử dụng

phân tích cú pháp một lần nữa, cái mà chúng tôi đã có sẵn.

Hãy kéo cái này vào.

Chúng ta sẽ kết nối đầu ra của khung dữ liệu để nó trở thành đầu vào của trình phân tích cú pháp.

Và hãy nhớ rằng, điều này cho phép chúng ta tạo một mẫu bằng cách sử dụng các biến thu được từ phiên bản trước

thành phần.

Trong trường hợp này, chúng tôi quan tâm đến tên mật mã, đây là một trong những trường được tạo như một phần

của thành phần, tên mật mã.

Điều này sẽ cho phép chúng tôi trích xuất dữ liệu này, trên thực tế là Bitcoin hoặc tên của tiền điện tử,

và đưa nó vào như một phần của văn bản đầu ra.

Vì vậy, khi chúng tôi đã có sẵn dữ liệu này, chúng tôi sẽ kết nối tên của tiền điện tử với tiền điện tử

tên trong thành phần nhắc nhở.

Với điều này, chúng tôi đã chuẩn bị gần như mọi thứ.

Chúng ta chỉ cần thêm ghi chú cuối cùng, một mô hình LIL sẽ xử lý yêu cầu hoặc lời nhắc

với được tạo ra.

Điều này có nghĩa là đầu ra của thành phần nhắc sẽ trở thành đầu vào cho thành phần openAI.

Chúng tôi sẽ để trống thông báo hệ thống, chúng tôi có thể sửa đổi nó nếu cần, chúng tôi chọn

mô hình, chọn một khóa và để xem kết quả được chỉ định mà chúng tôi muốn quan sát đầu ra trò chuyện

điều này trong thời gian thực hoặc để làm cho việc luyện tập trở nên thú vị hơn một chút.

Chúng tôi bắt đầu thực thi từ sân chơi, chạy luồng và xem điều gì sẽ xảy ra.

Sau vài giây, bạn có thể thấy rằng chúng tôi đã có phản hồi trong cuộc trò chuyện ở sân chơi.

Tại đây, chúng tôi được cung cấp thông tin về mức độ khuyến khích đầu tư vào tiền điện tử,

một số xu hướng và biến động giá cũng như hành vi của tiền điện tử.

Cuối cùng, về cơ bản nó nói rằng nó có thể được khuyến nghị nếu bạn muốn áp dụng lâu dài

chiến lược đầu tư và cảm thấy thoải mái với những rủi ro liên quan đến tiền điện tử

đầu tư.

Vì vậy, điều này giúp chúng tôi giải thích về hành vi của tiền điện tử và giúp chúng tôi xác định xem nó có phù hợp hay không

để thực hiện đầu tư.

Tại đây, bạn có thể thêm một phần của quy trình này hoặc từ thành phần ban đầu bất kỳ lời nhắc hoặc văn bản nào

liên quan đến tiền điện tử để phân tích xem việc đầu tư vào nó có đáng giá hay không.

Đây là cách chúng tôi tạo ra luồng này được gọi là tư vấn về tiền điện tử.

Tôi hy vọng bạn thích nó và nó hữu ích cho bạn.

Và hãy nhớ rằng, nếu có bất kỳ ghi chú hoặc thành phần nào mà bạn không chắc chắn, tôi khuyên bạn nên sao chép lại

thử nghiệm này và quan sát kết quả đầu ra để xem mỗi thành phần đó tạo ra những gì.

Bằng cách này, bạn sẽ hiểu rõ hơn và bắt đầu chuyên sâu hơn trong việc sử dụng