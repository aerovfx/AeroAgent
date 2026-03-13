# 005 AWS IoT Sử dụng ví dụ về SDK MQTT được cập nhật vi

---

Xin chào và chào mừng bạn đến với bài học cập nhật về cách sử dụng US Iot với sdhc được cập nhật.

Trong các bài học trước, chúng tôi đã tích hợp ESP a US Iot phát hành phiên bản 3.1 và đây là phiên bản mới nhất

phiên bản tại thời điểm ghi âm nhưng sau đó đã phát hành phiên bản mới hơn và tôi sẽ giữ lại

phiên bản cũ như một phần của bài học cấu hình vì một số người vẫn đang sử dụng nó.

Nhưng đối với những người muốn xem ví dụ về xuất bản và đăng ký bằng phiên bản mới

đây, thì bài học này là dành cho bạn.

Tuy nhiên, trước khi tiếp tục, hãy chắc chắn rằng bạn đã thiết lập tài khoản của mình, tạo một thứ

ở Hoa Kỳ tạo ra các chứng chỉ và đính kèm chính sách.

Về cơ bản, mọi thứ chúng ta đã làm trong bài học cấu hình.

Vì vậy, hãy quay lại và xem nếu bạn chưa xem.

Vì vậy, hãy bắt đầu ở đây bằng cách vào thư mục dự án và thay đổi tên của Hoa Kỳ hiện tại

Thư mục Iot.

Trong trường hợp bạn muốn giữ phiên bản này.

Vậy đó là phiên bản 3.1.

Bây giờ hãy sao chép lệnh sao chép mà họ đã cung cấp cho chúng ta ở đây.

Vì vậy hãy sao chép nó.

Giống như vậy.

Và sau đó đi đến thư mục dự án.

Bởi vì chúng tôi muốn sao chép nó vào thư mục này và nhấp chuột phải vào đây.

Và sau đó đi đón Bashir.

Và sau đó dán vào lệnh sao chép.

Và chỉ cần dành một chút thời gian để hoàn thành vì nó có thể mất một chút thời gian.

Và bây giờ chúng ta có thể đóng get.

Và chúng ta hãy kiểm tra ngắn gọn những gì chúng ta có ở đây và thư mục xã hội ESP nhân bản của chúng ta.

Đây là cấu trúc cấp cao nhất trông khá đơn giản với thư mục ví dụ và thư mục thư viện,

và chúng ta sẽ sớm xem xét các ví dụ và thực tế chúng ta sẽ triển khai ví dụ mktg.

Và trong thư mục thư viện, chúng ta sẽ cần thêm những thứ này bằng cách điều chỉnh tệp danh sách tạo của mình.

Vì vậy, vui lòng làm quen với các tệp và thư mục này tại đây, đặc biệt nếu bạn quan tâm đến

đi sâu hơn vào xã hội.

Được rồi.

Vì vậy, bây giờ hãy xem lại ví dụ mà chúng ta sắp triển khai.

Hãy quay trở lại thư mục ví dụ.

Và ví dụ mà chúng tôi muốn là một ví dụ mà chúng tôi có thể chỉ cần xuất bản và đăng ký dữ liệu.

Tuy nhiên, bạn luôn có thể khám phá các ví dụ khác khi bạn biết cách tích hợp ví dụ này.

Vì vậy, hãy đi vào MQTT, sau đó hãy đi vào xác thực lẫn nhau TLS.

Và trước tiên, chúng ta hãy xem phần đọc tôi được cung cấp ở đây, vì có một số điều quan trọng

ghi chú ở đó.

Đầu tiên, nó nói rằng chúng ta cần tìm và đặt tên máy chủ điểm cuối của Hoa Kỳ và nó cho biết tài khoản Iot của bạn có

tên máy chủ điểm cuối duy nhất để kết nối.

Để tìm thấy nó, hãy mở bảng điều khiển Iot của Hoa Kỳ và nhấp vào nút cài đặt ở phía dưới bên trái và sử dụng

Tệp xây dựng dự án K config.

Từ ví dụ này, chúng ta có thể nhập tên máy chủ điểm cuối vào cấu hình ví dụ và sdhc

config.

Vì vậy, chúng ta cũng cần đặt ID khách hàng và ở đây có thông báo rằng ID khách hàng được sử dụng trong Giao thức MQTT

để gửi tin nhắn đến và đi từ một xã hội và Iot yêu cầu mỗi thiết bị được kết nối trong một mạng duy nhất

Tài khoản Hoa Kỳ sử dụng ID khách hàng duy nhất và nếu chúng ta nhớ lại từ bài học cấu hình thì đây là tên

về điều của chúng ta trong một xã hội.

Và trong ví dụ này, các định nghĩa này được biên dịch thành cấu hình menu mà chúng ta có thể điều chỉnh thông qua

tập tin cấu hình sdhc.

Được rồi, bây giờ chúng ta hãy nắm bắt thông tin đó, chỉ để ôn lại nhanh về những gì chúng ta có thể

tìm nó để sau này chúng ta có thể dễ dàng lấy lại.

Vì vậy, tôi sẽ chỉ tạo một tệp văn bản mới và từ tài khoản AWS của chúng tôi.

Chúng ta có thể đi đến lõi Iot.

Và sau đó tôi sẽ chỉ định vị trí của mình.

Và sau đó chúng ta có thể đi vào cài đặt.

Và hãy lấy tên máy chủ điểm cuối.

Sao chép nó như vậy.

Và sau đó tôi sẽ ghi lại nó ở đây.

Kế tiếp.

Chúng tôi muốn khách hàng ID.

Hãy đi đến tất cả các thiết bị.

Không đi làm gì cả.

Và tôi sẽ chỉ sao chép của tôi.

Và sau đó ghi lại nó ở đây và bây giờ.

Hãy bắt đầu tích hợp khung và chúng ta sẽ bắt đầu bằng cách điều chỉnh tệp danh sách CMYK cấp cao nhất

và chúng ta thực sự có thể sử dụng tệp danh sách C được cung cấp bởi ví dụ để tham khảo.

Vì vậy, hãy mở tệp danh sách được cung cấp.

Và sau đó hãy sao chép toàn bộ lệnh set ngay tại đây.

Bây giờ hãy chuyển đến tệp danh sách tạo cấp cao nhất C trong dự án.

Và chúng ta thực sự có thể di chuyển lệnh set đến vị trí được đề xuất để có thể loại bỏ lệnh này.

Và sau đó tăng tốc lệnh tới.

Nhưng hãy điều chỉnh đường dẫn ở đây sao cho phù hợp với cấu trúc thư mục của chúng ta.

Chúng ta có thể chọn phần này ở đây.

Sau đó sử dụng điều khiển f.

Và sau đó chúng ta có thể thay thế nó bằng đường dẫn chính xác đến thư mục ESP a US Iot tại đây.

Được rồi, chỉ cần nhập ESP.

Rất nhiều.

Sau đó thay thế tất cả.

Ồ.

Và tất cả đều có vẻ tốt.

Ngoại trừ việc chúng tôi quên làm một việc đó là làm mới dự án vì tôi nhận thấy rằng phiên bản USB Iot

Thư mục 3.1 bị thiếu ở đây.

Vì vậy, những gì chúng ta có thể làm là đi tới thư mục dự án cấp cao nhất và nhấp chuột phải rồi đi xuống để làm mới

và làm mới dự án.

Bây giờ chúng ta có phiên bản cũ trong phiên bản mới ngay tại đây.

Tiếp theo, hãy sao chép các tệp cần thiết sang ID bằng cách vào thư mục chính của ví dụ.

Vì vậy, hãy đi tới thư mục ví dụ.

Đi vào thư mục chính.

Và chúng tôi đã có ứng dụng chính của riêng mình.

Vì vậy, hãy lấy tệp tiêu đề cấu hình demo.

Tệp xây dựng dự án cấu hình và tệp nguồn demo MK PT.

Sao chép chúng lại.

Chọn ghi đè cho tệp xây dựng dự án k config.

Được rồi, Tiếp theo, chúng ta có thể cập nhật tệp danh sách CMYK chính bằng cách sao chép tên của tệp nguồn mới.

Đi tới tập tin nguồn mới.

Và nhấp chuột phải vào nó.

Để sao chép.

Sau đó hãy mở tập tin danh sách chính.

Và chúng ta có thể ghi đè lên tệp nguồn xã hội cũ.

Với tên tập tin mới ở đây.

Và chỉ cần chắc chắn để lưu nó.

Tiếp theo, hãy cập nhật giao diện chính của chúng ta.

Và hãy sử dụng ứng dụng này và xem ví dụ đó là tài liệu tham khảo.

Hãy tiếp tục và mở tập tin đó.

Và thứ duy nhất chúng ta cần ở đây là điểm vào ứng dụng demo, và đó chính là hàm này

ở đây.

Vì vậy, hãy sao chép nguyên mẫu và quay lại và dán nó vào.

Được rồi.

Bây giờ chỉ cần điều chỉnh nó như vậy.

Chúng ta cũng hãy thực hiện lệnh gọi hàm.

Và lệnh gọi hàm ở đây.

Chỉ cần sao chép nó và quay lại và dán nó vào ứng dụng wi fi của chúng tôi.

Chức năng gọi lại sự kiện được kết nối.

Và đó là vì chúng ta cần kết nối Internet trước khi kết nối với xã hội.

Chúng tôi cũng có thể nhận xét lệnh gọi hàm khởi động Iot cũ của Hoa Kỳ.

Hãy nhận xét điều này và chúng tôi cũng có thể loại bỏ phần bổ sung cho tiêu đề Iot cũ của Hoa Kỳ.

Và đó là tất cả những gì chúng ta cần làm ở đây.

Tiếp theo, hãy xem lại ngắn gọn mã được cung cấp bởi ví dụ và thực hiện một số thay đổi nếu cần thiết.

Hãy bắt đầu với tệp tiêu đề cấu hình demo.

Và chúng ta hãy đi qua điều này một cách ngắn gọn.

Điểm cuối ở đây sẽ đến từ cấu hình sdhc sau khi chúng tôi cập nhật nó.

Và cổng MQTT cũng sẽ đến từ cấu hình.

Và mã định danh ứng dụng khách cũng đến từ cấu hình sdhc và nó sẽ được cập nhật theo nội dung của chúng tôi.

Tên.

Và kích thước bộ đệm mạng cũng đến từ cấu hình sdhc cũng như tên nền tảng phần cứng.

Và chúng ta sẽ thấy những định nghĩa này được xác định như thế nào khi chúng ta cập nhật cấu hình sdhc trong thời gian ngắn.

Vì vậy, bây giờ chúng ta hãy xem tệp C xác thực lẫn nhau demo MQTT.

Và tệp này chứa mọi thứ chúng ta cần để chạy bản demo.

Nhưng tất nhiên chúng tôi cần cập nhật nó để có thể công bố nhiệt độ, độ ẩm và chỉ số RSI của wi fi

và để nó hoạt động với tài khoản AWS Iot của chúng tôi.

Vì vậy, trước tiên hãy thêm phần bổ sung cho cảm biến PH 22 và đó là để chúng tôi có thể công bố nhiệt độ

và độ ẩm.

Và hãy bao gồm cả ứng dụng wi fi để chúng tôi có thể xuất bản RSI wi fi.

Vì vậy, ở đầu tệp, chúng ta phải điều chỉnh định nghĩa CA gốc, chứng chỉ ứng dụng khách và

cả khóa riêng nữa.

Vì vậy, hãy tiếp tục và sao chép tên tệp CA gốc của Hoa Kỳ và chúng ta có thể lấy tên đó từ thư mục certs của mình.

Và sau đó nhấp chuột phải.

Sau đó sao chép.

Và hãy dán nó vào để bắt đầu dữ liệu nhị phân CA gốc.

Và đối với phần cuối của dữ liệu nhị phân.

Bây giờ chúng ta có thể làm tương tự cho chứng chỉ ứng dụng khách.

Vậy chúng ta hãy quay lại thư mục tìm kiếm rồi mình sẽ chỉ điều khiển xem.

Và sau đó chúng ta có thể dán nó vào để bắt đầu.

Hãy làm phần cuối cùng nhé.

Bây giờ là khóa riêng.

Kiểm soát C để sao chép và dán nó vào để bắt đầu.

Và kết thúc.

Bây giờ chúng ta hãy tiếp tục xuống tập tin.

Ở đây chúng tôi có thêm một số định nghĩa cho liên kết điểm cuối cũng như độ dài mã nhận dạng ứng dụng khách, v.v.

Và sau đó còn có kết nối lại tris và sau đó là một số kết nối khác mà bạn có thể muốn xem xét để tùy chỉnh

ví dụ này

Và đây là một điều quan trọng mà chúng tôi sẽ phải cập nhật.

Đây là tên chủ đề của chúng tôi, mà chúng tôi đã sử dụng trong ví dụ Iot trước đây để xuất bản đăng ký

trước đây chúng tôi đã xác định nó trong tệp Iot C của Hoa Kỳ.

Vì vậy chúng ta hãy đi đến đó.

Và tôi sẽ chỉ điều khiển bên trái để tìm kiếm nó.

Và đây là cách tôi xác định của tôi.

Được rồi.

Vì vậy, tôi sẽ tiếp tục và sao chép cái này.

Và sau đó quay lại tệp ví dụ mới.

Và sau đó cập nhật định nghĩa ở đây.

Và một lần nữa, đây là chủ đề để đăng ký và xuất bản.

Và hãy tiếp tục chuyển thông báo ví dụ này đến đây mà chúng tôi thực sự sẽ không sử dụng vì chúng tôi sắp xuất bản

nhiệt độ, độ ẩm và chúng tôi đốt Cici của mình.

Và như chúng ta có thể thấy từ bản phác thảo ở đây.

Có khá nhiều định nghĩa và nguyên mẫu hàm, và tôi khuyên bạn nên xem qua những định nghĩa này.

của riêng bạn.

Nếu bạn quan tâm đến việc tùy chỉnh ví dụ này và điều chỉnh nó cho phù hợp với nhu cầu ứng dụng của mình.

Bởi vì điều quan trọng đối với chúng tôi lúc này là xuất bản dữ liệu về chủ đề này.

Chúng tôi không muốn xuất bản thông báo Hello world này, vì vậy hãy cùng tìm hiểu xem định nghĩa này được sử dụng ở đâu

bằng cách sử dụng điều khiển f.

Và ở đây chúng tôi thấy rằng nó được sử dụng trong hàm nguyên tử đã xuất bản trong đó tải trọng và tải trọng

length được cập nhật với các định nghĩa macro này.

Vì vậy, thay vì gửi Hello world, hãy cung cấp cho nó nhiệt độ, độ ẩm và Wi-Fi C và

cung cấp cho nó độ dài tải trọng mới.

Và để làm được điều đó, chúng ta có thể lấy câu lệnh print def từ ví dụ cũ.

Vì vậy, chúng ta hãy quay trở lại với xã hội.

Và chúng ta có thể tìm thấy điều đó trong nhiệm vụ xã hội.

Và hãy sao chép dòng này ở đây.

Và hãy dán nó lên trên cùng của hàm.

Và chúng tôi cũng muốn có wi fi ở bên ngoài.

Vì vậy, hãy thêm vào văn bản cho điều đó.

Và sau đó hãy cung cấp cho nó chức năng là ứng dụng wi fi.

Nhận RC.

Và tại sao fi RSI lại là một chuỗi.

Và kết quả của hàm là một số nguyên.

Và hãy xác định biến tải trọng C ở đây.

Được rồi.

Và sau đó chúng tôi muốn cập nhật tải trọng bằng biến tải trọng C của mình.

Bây giờ sẽ chứa chỉ số RSI, nhiệt độ và độ ẩm.

Và sau đó chúng tôi cũng muốn cung cấp độ dài của tải trọng và chúng tôi có thể sử dụng str len cho điều đó.

Và đó là tất cả những gì chúng ta cần làm.

Và một lần nữa, nếu bạn muốn tìm hiểu sâu hơn, tôi khuyên bạn nên xem lại tệp nguồn này một cách chi tiết hơn.

Nhưng bây giờ, chúng ta hãy xem chức năng chính của bản demo Iot của Hoa Kỳ và xem mô tả để biết

tổng quan nhanh.

Và ở đây nó nói rằng ví dụ hiển thị bên dưới sử dụng API MQTT để gửi và nhận các gói MQTT qua

Kết nối TLS được thiết lập bằng OpenSSL.

Ví dụ này là một luồng và sử dụng bộ nhớ được cấp phát tĩnh.

Nó sử dụng chất lượng dịch vụ cấp một và do đó thực hiện cơ chế truyền lại cho các dữ liệu đã được xuất bản.

tin nhắn.

Vì vậy, bao gồm những điều cơ bản.

Và bây giờ hãy chuyển sang xây dựng dự án để chúng ta có thể tạo tệp cấu hình SDK và cập nhật

các biến cần thiết.

Vì vậy, hãy tiếp tục và xây dựng dự án.

Vì vậy bây giờ chúng ta hãy tiếp tục với cấu hình sdhc.

Và sau đó trong cấu hình ví dụ, chúng ta có thể cập nhật mã định danh ứng dụng khách và điểm cuối của

nhà môi giới MQTT để kết nối.

Vì vậy, hãy sao chép điểm cuối.

Và chỉ cần dán nó vào.

Nhưng bây giờ hãy lấy mã nhận dạng khách hàng.

Và dán nó vào đây.

Và hãy nhớ lưu cấu hình.

Được rồi.

Vì vậy, bây giờ chúng ta có thể tiếp tục và xác thịt nó.

Khi đã hoàn thành, chúng tôi sẽ mở màn hình và sau đó đi tới ứng dụng khách Iot MQTT Test của Hoa Kỳ.

Vì vậy chúng ta hãy tiếp tục và xác thịt.

Vậy là được rồi.

Tôi chỉ có thể đánh.

Tiếp tục.

Và tôi thực sự đã quên chọn cổng của mình.

Vì vậy, tôi sẽ tiếp tục và làm điều đó.

Và sau đó tôi sẽ flash lại.

Được rồi.

Bây giờ chúng ta có thể mở màn hình.

Bây giờ tôi đang kết nối với thông tin xác thực lưu.

Và tôi đã hiển thị dữ liệu được công bố.

Tuyệt vời.

Vì vậy, tiếp theo, chúng ta có thể tiến tới một xã hội và chúng ta có thể kiểm tra hoạt động từ đầu đó.

Vì vậy chúng ta hãy đi đến đó.

Và hãy nhấp vào điều của chúng tôi.

Hãy chuyển đến tab hoạt động.

Và ở đây chúng ta thấy các sự kiện đã đăng ký và được kết nối.

Sự kiện đã đăng ký của chúng tôi trông như thế này.

Và được kết nối.

Vì vậy bây giờ chúng ta hãy đến với client thử nghiệm MQTT.

Và sau đó chọn chủ đề.

Và ở đó chúng tôi có dữ liệu đã công bố, wi fi, RSI, nhiệt độ và độ ẩm đang được công bố

vào khoảng thời gian được cung cấp bởi ví dụ có vẻ tuyệt vời.

Vì vậy, tiếp theo, nếu bạn muốn thử nghiệm xuất bản từ ứng dụng khách thử nghiệm MQTT, chúng tôi có thể đặt các màn hình cạnh nhau

đứng về phía một xã hội và sau đó xem hoạt động từ phía màn hình.

Vì vậy, hãy tiếp tục và đặt những thứ này cạnh nhau.

Và sau đó.

Bây giờ hãy nhấn xuất bản.

Và chúng ta bắt đầu.

Các tin nhắn đang được nhận trên ESP 332 từ một tổ chức W.

Và điều đó thật tuyệt vời.

Vậy là bây giờ bạn đã biết cách tích hợp một ví dụ từ phiên bản ESP này với AWS Iot SDK, thì bạn

nên có nền tảng vững chắc để tự mình khám phá thêm.

Được rồi.

Vì vậy, cảm ơn bạn đã tham gia cùng tôi trong khóa học này và tôi hy vọng sẽ sớm gặp lại bạn.