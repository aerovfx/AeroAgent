# Tổng quan triển khai WiFi 001 en

---

Chào mừng mọi người đến với phần triển khai của Whitefly sẽ cung cấp thông tin tổng quan về quá trình triển khai

và một số API mà chúng tôi sẽ sử dụng từ khung phát triển Viotti đầy ấn tượng.

Vì vậy, trước tiên, chúng ta hãy xem tổng quan về việc triển khai của chúng tôi.

Từ góc độ cấp cao, nghĩa là ứng dụng Abilify phải làm gì mà không cần nhận được

quá nhiều chi tiết là, trước hết, ESP 32 phải khởi động điểm truy cập của nó để các thiết bị khác

có thể kết nối với nó.

Điều này cho phép người dùng kết nối với nó để truy cập thông tin như dữ liệu cảm biến, thông tin thiết bị,

trạng thái kết nối và thông tin kết nối như địa chỉ IP, cổng và mặt nạ mạng được gán cho

ESP32.

Ngoài ra, chúng tôi sẽ có tùy chọn người dùng để kết nối và ngắt kết nối khỏi điểm truy cập cũng như hiển thị địa chỉ cục bộ

thời gian, v.v..

Tiếp theo, ứng dụng Wi-Fi sẽ khởi động máy chủ HTTP và sẽ lập trình ứng dụng này sau khi lập trình wi-fi.

các phần và máy chủ web đó sẽ hỗ trợ một trang web thực hiện mọi thứ mà tôi vừa đề cập.

Ngoài ra, ứng dụng còn chứa một tác vụ ô tô miễn phí nhận các thông báo gợi ý sẽ sử dụng để phối hợp

Các sự kiện về Wi-Fi và máy chủ web và chúng ta sẽ tìm hiểu thêm về vấn đề này sau.

Nhân tiện, vui lòng kiểm tra các API ảnh này để tạo, tạo ra Q và Q gửi tới

gửi dữ liệu đến Q và Q nhận được để nhận dữ liệu sẽ sử dụng lại để điều phối thứ tự các sự kiện

xảy ra trong ứng dụng của chúng tôi.

Vì vậy tôi sẽ không đi sâu vào chi tiết về những điều này vì tôi tin rằng bạn sẽ có hiểu biết chung

về cách họ làm việc.

Sau khi chúng tôi triển khai chúng trong ứng dụng và sau này trong khóa học sẽ kết nối ESP 32 bằng cách sử dụng trước đó

thông tin xác thực đã lưu.

Vì vậy, đây là tổng quan đơn giản về ứng dụng Wi-Fi.

Về cơ bản, bạn sẽ có một thiết bị kết nối, điện thoại di động hoặc máy tính xách tay, v.v., thiết bị này sẽ trở thành

trạm của băng mềm ESB 32.

Khi được kết nối, dịch vụ DHP từ ứng dụng mềm ESP 32 sẽ tự động gán IP cho thiết bị của bạn

và bạn sẽ tương tác với ESP 32 thông qua trang web do máy chủ web cung cấp.

Ngoài ra, bản thân P32 sẽ khởi động chế độ trạm cắt điểm truy cập và sẽ gán IP tĩnh

địa chỉ tới API mềm.

Dịch vụ DHP tự động gán địa chỉ IP cho các trạm kết nối cũng sẽ chỉ định địa chỉ IP tối đa

số lượng trạm được phép kết nối.

Và cuối cùng, chúng tôi sẽ cập nhật ứng dụng để có thể kết nối SB 32 với quyền truy cập bên ngoài

điểm hoặc bộ định tuyến nơi có kết nối internet.

Và điều này cho phép chúng tôi lấy giờ địa phương bằng Giao thức thời gian mạng đơn giản hoặc S&P.

Và cũng đã giữ dịch vụ từ điểm truy cập sẽ tự động gán địa chỉ IP cho SPF 30

đến một giờ ứng dụng.

Bây giờ hãy nói ngắn gọn về API trình điều khiển Wi-Fi từ ESB IDF.

Vì vậy, tôi khuyên bạn nên truy cập tài liệu ấn tượng ở đây về trình điều khiển Wi-Fi và thực hiện một vài

phút để duyệt qua điều này.

Ngoài ra, hãy xem mô hình lập trình cũng như các sự kiện fi xảy ra trong nền.

Những sự kiện này sẽ được xử lý bởi người xử lý sự kiện của chúng tôi.

Ngoài ra, hãy xem tài liệu tham khảo API tại đây và thoải mái duyệt qua nó, nhưng tôi sẽ nói về các API đã chọn

API trong thời gian ngắn.

Và cũng xem xét tài liệu giao diện mạng ở đây.

Chỉ cần cố gắng ghi lại ý tưởng đằng sau nó và kiến trúc rồi cuộn xuống phần dành cho các lập trình viên

hướng dẫn sử dụng, trong đó có các chế độ sự kiện Wi-Fi và khởi tạo mặc định mà tôi đã đề cập.

Tôi cũng sẽ thảo luận về một số API sau tại đây.

Được rồi, vậy chúng ta sẽ bắt đầu định cấu hình ứng dụng Wi-Fi của mình bằng cách xác định cài đặt Wi-Fi trong tiêu đề

tập tin như bên cạnh USB với mật khẩu, địa chỉ IP, cổng và mặt nạ mạng, v.v.

Chúng tôi cũng sẽ xác định ứng dụng Wi-Fi cho nhiệm vụ khó khăn và chúng tôi có thể sử dụng API ở đây, nhưng

thực sự sẽ sử dụng mã PIN cho phiên bản mã ở đây để chúng tôi có thể chỉ định lõi nào chúng tôi muốn phân bổ

hoạt động hiệu quả vì chúng tôi có sẵn hai lõi trên ESB 32.

Chúng tôi cũng sẽ tạo một trình xử lý sự kiện để các sự kiện Wi-Fi và IP nhất định được tự động tính đến

bởi trình điều khiển Wi-Fi.

Và khi bắt đầu ứng dụng Wi-Fi của bạn, chúng tôi sẽ thiết lập cấu hình mặc định bằng cách khởi tạo

ngăn xếp TCP IP bằng giao diện mạng ESB và chức năng CNTT.

Và cũng sẽ tạo các cài đặt cấu hình Wi-Fi cơ bản bằng cách sử dụng chức năng ESP Wi-Fi trong CNTT.

Và nhân tiện, cái này phải được gọi trước khi bất kỳ API Wi-Fi nào khác được gọi.

Ngoài ra, chúng tôi sẽ cần sử dụng bộ lưu trữ Wi-Fi của ISP, bộ lưu trữ này sẽ đặt loại cấu hình lưu trữ.

Trong trường hợp nào sẽ đặt loại lưu trữ thành RAM?

Sau đó sẽ tạo cấu hình mặc định cho cả giao diện ứng dụng mặc định và trạm mặc định.

Vui lòng theo dõi các liên kết này và đọc chúng chi tiết hơn cũng như nhấp vào liên kết để biết

ứng dụng mặc định và trạm mặc định.

Như API đã đề cập, chúng tôi cần những thứ này để đăng ký trình xử lý Wi-Fi mặc định.

Việc bắt đầu ứng dụng cũng bao gồm việc xác định SPF 30 để cấu hình cao điểm trong ngày mềm sẽ xác định

cài đặt AP cho các thành viên của cấu trúc cấu hình wi fi, trong trường hợp này sẽ muốn cập nhật đã chọn

các thành viên cấu trúc AP mềm được liệt kê ở đây.

Và giao diện mạng ESPN cho biết thông tin IP đặt địa chỉ IP của giao diện mạng AP và ESPN mềm,

D.H. CPS khởi động dịch vụ DHP cho mọi trạm kết nối với ESPN 32 để địa chỉ IP

có thể được phân bổ động bởi ESPN.

Ngoài ra, S.P. Rifai, tôi đã nói chế độ đặt chế độ, cho dù đó là chế độ, chế độ trạm hay chế độ trạm,

đó là chế độ mà chúng tôi sẽ sử dụng và ESP Wi-Fi cho biết Config đặt cấu hình của điểm truy cập

dựa trên các thành phần cấu trúc cấu hình Wi-Fi mà chúng tôi đã đặt trước đó.

Và băng thông được đặt bởi S.P. Wi-Fi sẽ sử dụng để đặt băng thông ở mức 20 megahertz.

Ngoài ra, chúng tôi sẽ sử dụng Wi-Fi của ISP, Power Save cho biết và chúng tôi sẽ không đặt nó thành không vì chúng tôi

sẽ không sử dụng tính năng tiết kiệm năng lượng trong ứng dụng này.

Cuối cùng, chúng ta có thể gọi ISP wi fi start sau khi thực hiện xong tất cả những điều này, thao tác này sẽ khởi động wi fi ở chế độ

được chỉ định trước, trong trường hợp của chúng tôi là chế độ trạm ứng dụng chế độ wi fi.

Được rồi, vì vậy hãy thoải mái mở tài liệu này khi chúng ta đi qua phần lập trình, nếu bạn

cần phải xem lại những gì đang diễn ra và tôi sẽ gặp bạn ở đó.