# 6 -Thiết lập website và tìm hiểu flow.en US

---

WEBVTT

Chào các bạn.

Vì vậy, đây là phần thứ hai của khung Django và xây dựng trang web, đúng không, sử dụng khung Django.

Và trong video trước, tôi đã bỏ lỡ một thứ, đó là gói dấu chấm đáng ghen tị.

Vì vậy, gói này được sử dụng bởi nó có thể được sử dụng bởi bất kỳ ai muốn giữ bí mật thông tin đăng nhập, khóa của mình

thông tin nhạy cảm ở một nơi riêng biệt và không nằm trong cơ sở mã của họ.

Phải.

Vì vậy, bên trong gói dot ghen tị, chúng ta có chức năng tải ghen tị, tôi sẽ nói với bạn sau về

tại sao chúng tôi gọi hàm này.

Nhưng như bạn có thể thấy ở đây trong thư mục trang web của tôi, nơi chứa tất cả các tệp cấu hình,

Tôi có tệp dấu chấm và V, vì vậy nếu tôi nhấp vào đây, bạn có thể thấy rằng tôi có địa chỉ DNS khóa Django của mình,

Địa chỉ IP, tất cả những thứ đó ở đây.

Phải?

Vậy điều tôi đang làm là tạo một tập tin dấu chấm, phải không?

Và tôi đang lưu tất cả thông tin nhạy cảm của mình ở đây.

Sau đó, tôi gọi hàm tải và hàm V để gọi và cung cấp cho tôi tất cả các giá trị từ đây.

Vì vậy chúng tôi gọi chúng là chìa khóa.

Và tất cả giá trị của các khóa này đều được gọi ở đây, phải không?

Như bạn có thể thấy, tôi đang sử dụng hàm lấy môi trường dấu chấm của hệ điều hành, về cơ bản nó gọi ra giá trị

cho một khóa cụ thể mà chúng tôi đặt ở đây.

Phải.

Vì vậy, bạn có thể thấy rằng tôi đang gọi khóa Django để giá trị mà nó chứa bên trong hàm dấu chấm là

được lưu ở đây bên trong khóa bí mật.

Bây giờ hãy giả sử rằng không có khóa nào có tên này trong hàm ghen tị dấu chấm của tôi.

Sau đó nó sẽ chèn cái này vào trong khóa bí mật.

Phải.

Vì vậy, bây giờ bạn có thể đang nghĩ rằng, giả sử ai đó có thể truy cập vào cơ sở mã của chúng tôi, vậy nên anh ấy

cũng có thể truy cập tệp DMV.

Sau đó anh ta cũng có thể lấy được tất cả các thông tin nhạy cảm.

Phải.

Nhưng vấn đề là khi bạn chạy dấu chấm này và chúng tôi sẽ lưu trữ tất cả các khóa này cũng như giá trị của chúng.

được lưu trữ bên trong biến hệ thống này.

Vì vậy, khi chạy mã, bạn có thể xóa tệp DMV này.

Và thậm chí sau đó, với sự trợ giúp của tính ghen tị tải trọng, bạn vẫn có thể gọi ra các giá trị cho những điều cụ thể này.

khóa từ các biến hệ thống của bạn.

Phải?

Vì vậy, tất cả giá trị đó sau đó được lưu trữ trong các biến hệ thống của bạn và hàm tải gọi các giá trị đó

từ những biến đó đến đây.

Vì vậy, đó là cách bạn có tất cả thông tin nhạy cảm bên trong hệ thống của mình, chỉ các biến và sau đó

bạn có thể gọi họ ra để không ai có thể truy cập thông tin nhạy cảm đó, ngay cả khi họ nhận được

nắm giữ cơ sở mã của bạn.

Bây giờ, trong phần thứ hai.

Điều tôi muốn nhấn mạnh là mô hình sử dụng hệ thống kiến trúc mẫu mà Django cung cấp

bạn, người xử lý việc quản lý cơ sở dữ liệu, xử lý giao diện người dùng và phần phụ trợ.

Phải.

Vì vậy, tôi sẽ hiển thị cho bạn các lượt xem theo tệp.

Đây thực sự là bên trong ứng dụng.

Giống như tôi đã nói với bạn, nếu chúng tôi muốn các chức năng bổ sung được kết nối hoặc được tính phí trên

trang web hoặc để được sử dụng trên trang web của bạn, bạn sẽ cần phải xây dựng những trang web đó một cách cụ thể.

Và để làm được điều đó, bạn sẽ cần tạo một ứng dụng.

Và bên trong ứng dụng đó, bạn có thể xây dựng dựa trên các chức năng đó.

Bây giờ, như bạn có thể thấy, ở đây tôi có một hàm lấy tham số yêu cầu.

Vì vậy, các khung nhìn có các hàm hoặc lớp được xác định, phải không?

Vì vậy, trong các hàm đó, bạn viết mã để xử lý bất kỳ thứ gì thuộc phần back-end, đúng không.

Có nghĩa là nếu bạn muốn truy vấn một số dữ liệu từ cơ sở dữ liệu, bạn sẽ thực hiện điều đó ở đây bên trong

chức năng nếu bạn muốn, nếu bạn muốn nối thêm một cái gì đó, nếu bạn muốn đưa ra kết quả từ

dữ liệu của bạn, bạn sẽ làm điều đó ở đây.

Vì vậy, các khung nhìn, tất cả các hàm mà chúng ta tạo đều có kiểu trả về cụ thể, nghĩa là bạn sẽ

luôn phải trả về một hàm kết xuất để hiển thị đúng giao diện người dùng của bạn.

Vì vậy, mỗi chức năng lấy dữ liệu và có thể thao tác dữ liệu, sau đó gửi dữ liệu trở lại phía trước

kết thúc.

Nhưng làm thế nào để nó hiểu chính xác giao diện người dùng hoặc trang nào chúng ta cần gửi dữ liệu đến đó đã xong

thông qua kết xuất.

Phải.

Vậy với sự trợ giúp của kết xuất, chúng ta lại chuyển tham số đầu tiên theo yêu cầu, phải không?

Bạn có thể thấy rằng đây thực sự là việc xác định phương thức.

Sau đó chúng ta có trang HTML được lập chỉ mục, nghĩa là giống như trang này, chúng ta phải cảm ơn dữ liệu và

dữ liệu mà chúng tôi phải gửi sẽ gửi dưới dạng từ điển mà chúng tôi còn gọi là ngữ cảnh.

Bây giờ, có hai, hai loại hàm mà tôi đã xây dựng.

Một dành riêng cho Django, nơi chúng tôi gửi yêu cầu.

Như vậy Django hiểu rằng hàm này là hàm xử lý phần backend và cũng chịu trách nhiệm

để hiển thị một trang cụ thể.

Và khi chúng ta nói trang, chúng ta cũng gọi chúng là mẫu trong biệt ngữ Django, phải không?

Vì vậy, đây là cách hệ thống mẫu Vue hoạt động.

Nhưng nếu bạn di chuyển xuống một chút, bạn có thể thấy rằng tôi cũng đã tạo một chức năng dự đoán

đó không phải là tham số yêu cầu, phải không?

Vì vậy, như bạn có thể thấy, nó không lấy tham số yêu cầu.

Và đây.

Và điều đang xảy ra là chức năng này không được liên kết với bất kỳ trang giao diện người dùng nào.

Nhưng đây chỉ là thao tác dữ liệu và trả lại kết quả.

Và như bạn có thể thấy ở đây, tôi thực sự đã sử dụng hàm tạo chuỗi để dự đoán thế giới.

Phải.

Và cuối cùng, tôi sẽ trả lại văn bản đã tạo.

Vì vậy, điều đang xảy ra ở đây là đầu tiên khi tôi chạy, các chế độ xem mã của tôi sẽ chạy và sau đó là hàm xử lý

đang chạy phải không?

Và sau đó chúng tôi thấy rằng phương thức yêu cầu bị tạm dừng, sau đó chúng tôi yêu cầu khác rồi cung cấp cho tôi thông tin đầu vào.

Vì vậy, chúng tôi lấy đầu vào đó ở đây.

Sau đó, chúng tôi gửi thông tin đầu vào đó đến chức năng dự đoán để đưa vào mô hình.

Mô hình.

Mô hình dự đoán những từ đó và cung cấp cho chúng tôi văn bản được tạo và được lưu trữ lại để phản hồi.

Sau đó, chúng tôi gửi phản hồi là dữ liệu bị thao túng của chúng tôi trở lại giao diện người dùng bằng cách sử dụng từ điển ngữ cảnh

ở đây.

Nhưng như bạn thấy, ở đây tôi chỉ định nghĩa các hàm này và chỉ gọi là hàm dự đoán

ở đây, nhưng tôi chưa gọi hàm xử lý ở đâu cả.

Vậy chúng ta gọi những hàm đó như thế nào?

Phải.

Vì vậy, điều này đang xảy ra với sự trợ giúp của URL.

Bây giờ, như bạn có thể thấy, ở đây cũng có tệp chấm tròn của URL.

Phải.

Vì vậy, điều đang xảy ra ở đây là khi bạn chạy mã và máy chủ của bạn đang chạy cục bộ một chút,

mặc dù trên máy chủ ảo, điều đó vẫn xảy ra.

Và khi bạn truy cập các URL, đúng vậy, giống như bạn gõ w w w dot google dot com.

Vì vậy, nếu bạn truy cập một URL cụ thể.

Sau đó hàm xử lý sẽ được gọi và tới.

Xử lý với điều đó.

Chúng tôi tạo ra các khuôn mẫu trong đó chúng tôi nói điều đó hoặc nơi chúng tôi chỉ định điều đó ở phần nào hoặc phần nào bạn là L

chức năng nào cần được thực hiện đúng.

Vì vậy, như bạn có thể thấy ở đây trên con đường chém nhà của tôi, nó giống như đường chém nhà của chủ nhà địa phương.

Đó sẽ là URL của tôi và tôi sẽ hiển thị cho bạn sau một phút.

Sau đó thêm phần đó hoặc phần bạn được yêu cầu chạy chức năng xử lý.

Và khi chúng ta đi theo con đường đó và chức năng xử lý được chạy, phần phụ trợ sẽ hiểu điều đó.

Vâng.

Bây giờ tôi phải xem liệu tôi có đầu vào hay không.

Nếu có, tôi phải gửi nó đến chức năng dự đoán của mình để nhận kết quả.

Và khi tôi nhận được kết quả, tôi phải gửi lại những kết quả đó cho loại trang của mình.

Đây là cách nó hoạt động.

Nhưng một lần nữa, đây chỉ là phần mẫu và lượt xem.

Vậy mô hình xuất hiện như thế nào và chính xác thì mô hình là gì?

Như tôi đã nói với bạn, các mô hình thậm chí còn ở đây, bạn có thể thấy rằng có một dấu chấm mô hình theo từng tập tin.

Vì vậy, trong các mô hình, điều này khá trống rỗng.

Nhưng trong các mô hình, điều chúng ta làm là tạo các bảng ở đây, phải không?

Chúng tôi tạo các bảng ở đây để xác định chính xác cách các bảng kết thúc với những ràng buộc mà các bảng đó sẽ

được xây dựng bên trong cơ sở dữ liệu của bạn.

Vì vậy, điều chúng tôi làm là trong phần dạng xem, chúng tôi gọi các bảng đó và truy vấn một số nội dung để có được

dữ liệu từ các cơ sở dữ liệu.

Vì vậy, đây là cách hoạt động của chế độ xem mẫu và hệ thống kiến ​​trúc mô hình.

Và trong HTML được lập chỉ mục là trang giao diện người dùng, đây chỉ là nội dung CSS cơ bản, phải không?

Sau đó, bạn có thể thấy ở đây tôi đã tạo một biểu mẫu có cả phương thức và hành động.

Hành động về cơ bản là nơi bạn muốn chuyển hướng sau khi sự việc đã được hoàn thành và gửi đi.

Phải.

Lấy làm tiếc.

Vì thế.

Vâng, bạn có thể thấy điều đó.

Tôi đang lấy đầu vào.

Tôi đang lấy đầu vào ở đây.

Và tôi muốn đưa ra một ví dụ.

Nếu không muốn gõ 50 từ, bạn chỉ cần copy, dán và xem kết quả ra sao.

Phải.

Và cũng lưu ý rằng bạn không mắc bất kỳ sai sót nào khi nhập dữ liệu.

Phải.

Và tôi có thể thấy rằng có điều gì đó.

Vâng.

Vâng.

Vì vậy, một lần nữa, câu nên có 50 từ.

Và tôi giả sử rằng bạn chỉ đặt các kiểu dữ liệu chuỗi vì ngay tại đây bạn có thể thấy rằng tôi chưa đặt

đã sử dụng bất kỳ chức năng xử lý trước nào mà chúng tôi có và xin lỗi, đã thiết kế và sử dụng trong lần đầu tiên

một phần khi chúng tôi xây dựng mô hình.

Phải.

Vì vậy, hãy lưu ý điều đó.

Và nếu muốn, bạn có thể bao gồm những thứ đó để ngay cả khi ai đó nhập các từ như hashtag WW hoặc một số từ

URL để nó sẽ được lọc ra.

Điều cuối cùng tôi muốn nói đến là hệ thống tiền mặt.

Bây giờ, hãy lưu ý rằng mỗi lần hàm dự đoán của bạn được gọi, nó sẽ tải.

Vâng, nó sẽ tải mô hình của bạn ở đây nhiều lần.

Phải.

Vì vậy, điều này sẽ làm cho trang web của bạn chậm hơn một chút.

Nhưng ở đây bạn có thể thấy rằng chúng tôi chưa làm điều tương tự.

Chúng tôi được token hóa.

Vì vậy, để mã hóa mà tôi vừa tạo một tập lệnh riêng trong đó tôi đang tạo một hệ thống tiền mặt để

xảy ra là khi tôi tạo bộ đệm của mình, tệp .

Đôi mắt Tolkien.

Nó được lưu trong bộ nhớ đệm của tôi và được tải vào bộ nhớ của tôi nên bạn không cần phải tải lại lần nữa và

một lần nữa và bạn chỉ cần tải mô hình một lần.

Ý tôi là trang web một lần và nó sẽ ở trong bộ nhớ và bạn có thể trực tiếp gọi và sử dụng lại nó và

một lần nữa.

Và lý do tôi chưa làm điều này với mô hình deep learning là vì năm file đó là một file

loại, đây không phải là loại mà Django không thể tiếp cận được.

Vì vậy, chúng tôi không thể chọn một tệp, chúng tôi không thể trích xuất năm tệp dưới dạng tệp dưa.

Và những gì hệ thống của chúng tôi làm là lưu tệp ở định dạng dưa chua và sau đó mở tệp ở định dạng

định dạng dưa chua trong bộ nhớ.

Chỉ dùng để lưu tệp của bạn dưới dạng tệp dưa chua.

Nhưng năm tệp không được lưu dưới dạng tệp dưa.

Vì vậy, đó là lý do tại sao bạn cần tải đi tải lại các mô hình.

Nhưng cách thay thế này là bạn có thể tạo các phiên bên trong Django và trong các phiên đó

bạn chỉ có thể tải mô hình một lần cho đến khi phiên trực tuyến.

Một lần nữa, mô hình sẽ nằm trong bộ nhớ thay vì được tải lại nhiều lần.

Vì thế bạn có thể tự mình xem và đánh giá.

Nếu tôi đang tạo phiên và tải phiên lập mô hình của bạn sẽ là lựa chọn tốt hơn.

Phải.

Vì vậy, đây là cách Django, khung công tác Django giúp chúng ta xây dựng các trang web khá dễ dàng và

khá dễ sử dụng và quản lý.

Phải.

Điều cuối cùng là thực sự chạy máy chủ trên máy cục bộ.

Bạn có thể tự mình xem trang web đang hoạt động như thế nào.

Bây giờ bạn phải chạy lệnh trước mười, quản lý hoặc chạy máy chủ.

Được rồi.

Vì vậy, khi bạn chạy lệnh này, hệ thống sẽ mất một chút thời gian để khởi động quá trình

chạy máy chủ cục bộ.

Sau đó, nó cung cấp cho bạn một URL mà bạn có thể thấy ở đây.

Vì vậy, khi tôi nói về máy chủ lưu trữ cục bộ hoặc máy chủ lưu trữ cục bộ, tôi đang nói về điều cụ thể là bạn đang ở đây.

Và thậm chí ở đây bạn có thể thấy rằng.

Bảng mà Django sử dụng theo mặc định là cổng 8000 và chỉ định bằng cách đánh dấu phần này ở đây là vì

sau này chúng tôi sẽ cần chỉ định cổng bên trong W.

Dịch vụ S cũng có.

Bây giờ nếu tôi đi đến my.

Bạn đang ở trong ai.

Nếu tôi về nhà, bạn sẽ ở đó.

Như bạn có thể thấy ở đây bây giờ, nó đã được tải trong trang của tôi.

Nên khi vào nhà bạn đang ở trong nhà bạn không hiểu là mình phải chạy hàm xử lý

và khi đó hàm xử lý hiểu rằng tôi phải trả về trang HTML như khi chúng ta nói return the

Trang HTML, ý tôi là hiển thị trang ước tính.

Được rồi.

Vì vậy, trang ước tính được hiển thị ngay bây giờ.

Vì vậy, hãy nhập 50 từ hoặc bạn chỉ cần sao chép và dán nội dung này.

Tôi chỉ viết điều này ở đây để việc kiểm tra mô hình của bạn trở nên dễ dàng hơn một chút.

Sau đó, bạn có thể chỉ cần nhấp vào gửi.

Và sau đó nó chỉ tải.

Mô hình dự đoán chuỗi từ tiếp theo và sẽ cho bạn câu trả lời tại đây.

Nhưng như bạn có thể thấy ở đây, câu trả lời đã được chỉ định ở đây.

Vì vậy, bạn có thể thấy rằng trang web đang hoạt động khá tốt.

Và chúng ta cũng đã biết về hệ thống kiến trúc mẫu xem mô hình, chính xác như thế nào

Django giúp chúng tôi xử lý giao diện người dùng, quản lý cơ sở dữ liệu và làm việc với

phần phụ trợ cho trang web của chúng tôi.

Phải?

Vậy đây là thế này thế này thế này chúng ta cũng đã hoàn thành phần thứ hai của dự án đang xây dựng

trang web của chúng tôi bằng cách sử dụng khung Django.

Bây giờ, ngay trước khi chuyển sang phần thứ ba.

Điều tôi muốn chỉ rõ là thế.

Bạn sẽ phải tạo một tệp yêu cầu hoặc tệp txt bất cứ khi nào bạn muốn.

Trên thực tế, đây là một cách làm rất tốt để tạo ra các yêu cầu nộp hồ sơ cho bất kỳ dự án nào hoặc cho từng dự án.

và mọi dự án mà bạn có.

Bởi vì điều này sau đó chỉ định tất cả các gói và gói phụ thuộc mà bạn sử dụng cũng như phiên bản nào của gói đó

gói mà bạn sử dụng.

Bởi vì đôi khi điều xảy ra là mọi người viết blog và các nội dung về dự án và sau đó bạn thấy tất cả

các gói họ đã sử dụng.

Nhưng khi bạn dùng thử những gói đó, bạn hiểu rằng một số gói này đang gây ra vấn đề cho bạn

bởi vì trong các phiên bản mà mọi người sử dụng blog, đó là phiên bản trước đó có một số

các chức năng khác nhau được tạo ra và các phiên bản mới, các chức năng được tạo ra khác nhau hoặc các chức năng

được sử dụng là khác nhau.

Vậy là nó tạo ra xung đột vì điều đó phải không?

Vì vậy đây là một thực hành tốt để làm.

Và lý do khác khiến tôi tạo điều này là vì khi chúng tôi thiết lập máy chủ của mình, để thiết lập máy chủ,

nó cũng cần phải hiểu tất cả các gói đang được sử dụng.

Và ở đó tệp văn bản yêu cầu sẽ được sử dụng rất rộng rãi.

Phải.

Vì vậy tôi sẽ dừng lại ở đây.

Và trong video tiếp theo, chúng ta sẽ bắt đầu với việc các dịch vụ tìm hiểu về hệ thống máy chủ đám mây,

và cuối cùng, tìm cách đẩy mã của chúng tôi vào máy chủ và thiết lập máy chủ để trang web của chúng tôi

đang trực tiếp.