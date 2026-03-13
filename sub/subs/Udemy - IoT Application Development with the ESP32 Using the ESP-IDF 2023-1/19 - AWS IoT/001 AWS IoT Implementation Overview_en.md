# 001 Tổng quan triển khai AWS IoT vi

---

Xin chào và chào mừng bạn đến với phần Iot của Dịch vụ web Amazon.

Trong phần này, chúng tôi sẽ định cấu hình dự án để cho phép giao tiếp với lõi Iot của Hoa Kỳ, đó là

một dịch vụ đám mây cho phép chúng tôi liên lạc với ISP từ mọi nơi.

Và trong quá trình triển khai, chúng ta sẽ tìm hiểu các quy trình cơ bản của lõi Iot và từ bảng điều khiển AWG

chúng tôi sẽ đăng ký và xuất bản dữ liệu cảm biến nhiệt độ và độ ẩm cũng như tín hiệu nhận được

sức mạnh của kết nối Wi-Fi cục bộ của chúng tôi.

Được rồi, trong bài học này, tôi sẽ chỉ giới thiệu ngắn gọn ở cấp độ cao về lõi WSI Iot và

sau đó tôi sẽ chia sẻ một số tài nguyên cốt lõi của WC Iot có ích khi mới bắt đầu, đó là

cũng sẽ giúp làm rõ thêm các chi tiết kỹ thuật.

Và giống như phần mở đầu trong bài học tiếp theo, tôi sẽ thảo luận về một số chủ đề kỹ thuật sẽ cung cấp

thậm chí còn làm rõ hơn.

Tôi cũng sẽ đề cập đến ESP, AWB Iot SDK, sẽ tích hợp vào dự án và cũng cung cấp

Link thiết lập tài khoản AWB.

Và cuối cùng tôi sẽ đề cập đến các bước cần thực hiện để triển khai đăng ký công khai của chúng tôi và

thử nghiệm bằng cách sử dụng ứng dụng khách thử nghiệm MQ t.

Được rồi.

Vì vậy, bây giờ, hãy tiếp tục với Tổng quan về an toàn AWB và trực quan hóa Truyền thông AWB Iot ở mức độ

mức độ rất cơ bản.

Chúng tôi sẽ có thứ của mình như được gọi là AWB, đây là thiết bị của chúng tôi sẽ kết nối với đám mây thông qua

Lõi Iot AWB sử dụng giao thức NQT, đây là giao thức đăng ký được xuất bản nhẹ tương thích

với một xã hội.

Tôi sẽ đề cập đến điều này nhiều hơn một chút.

Bây giờ chúng ta hãy xem lại một số thông tin cơ bản về Quân đoàn An toàn Hoa Kỳ.

Quân đoàn An toàn Hoa Kỳ là một nền tảng kết nối các thiết bị Iot với các dịch vụ Iot của Hoa Kỳ.

Và để bắt đầu, chúng ta hãy điểm qua một số tài nguyên chính về an toàn của Hoa Kỳ.

Và trước tiên tôi khuyên bạn nên theo liên kết này đến trang Bắt đầu Iot của Hoa Kỳ vì nó đáng giá

xem qua tất cả thông tin này vì có nhiều điều để tìm hiểu về một xã hội, đó là lý do tại sao

Tôi cũng khuyên bạn nên tìm hiểu thêm về liên kết trang web và đánh dấu trang đó để tham khảo sau này.

Và nếu bạn đang tìm kiếm tài nguyên bổ sung về khía cạnh kỹ thuật, tôi cũng khuyên bạn nên xem

phần giới thiệu này về tee WSU và chỉ cần theo liên kết là bạn có thể đăng nhập bằng tài khoản Amazon của mình.

Và đây là phần giới thiệu thực sự hay về những điều cơ bản trong đó từng thành phần được mô tả.

Và trên thực tế, tôi thậm chí sẽ quay lại vấn đề này sau khi chúng ta hoàn thành việc thiết lập dự án nếu bạn thực sự muốn

để đóng đinh nó xuống.

Tuy nhiên, bây giờ, chúng ta hãy tiếp tục với những điều cơ bản ở đây.

Lõi WSU bao gồm cổng thiết bị, cho phép các thiết bị giao tiếp với WSU một cách an toàn và

trong thiết bị một cách hiệu quả.

Gateway hỗ trợ ổ cắm web NQT và giao thức HTTP 1.1, đồng thời thiết bị Gateway lưu trữ một trình trung chuyển tin nhắn

kết nối và xử lý tin nhắn giữa thiết bị IoT của bạn và đám mây.

Nhà môi giới tin nhắn là một dịch vụ môi giới đăng ký được xuất bản cho phép bạn gửi tin nhắn có địa chỉ

đến một chủ đề giống như chủ đề tôi đã tạo ở đây mà chúng ta sẽ sử dụng sau này.

Vì vậy hành động gửi tin nhắn được gọi là xuất bản và hành vi đăng ký nhận

tin nhắn cho bộ lọc chủ đề được gọi là đăng ký.

Và trong khóa học này, chúng tôi sẽ sử dụng ứng dụng khách thử nghiệm bị tắt tiếng ở đây để theo dõi các tin nhắn bị tắt tiếng được chuyển vào

Tài khoản Amazon Web Services từ ESP 32.

Vì vậy, ESP 32 sẽ xuất bản các thông báo được xác định theo chủ đề ở trạng thái được truyền đạt tới một

Nhóm WSU và cũng sẽ đăng ký các tin nhắn từ phía ESP 32 và kiểm tra việc gửi chúng bằng cách sử dụng

đến một tùy chọn chủ đề ở đây.

Vì vậy, xuất bản và đăng ký bằng ứng dụng khách thử nghiệm MQ là một cách tốt để bắt đầu hòa nhập với xã hội.

Và một khi bạn đã làm được điều này, bạn có thể tự mình tìm hiểu sâu hơn.

Và chỉ nói ngắn gọn về nQt.

nQt là một giao thức mạng đăng ký nhẹ, được xuất bản để truyền tin nhắn giữa các thiết bị.

Để tìm hiểu thêm về các giao thức truyền thông cốt lõi của Iot và chi tiết của từng giao thức, bạn có thể sử dụng FWC Iot

liên kết các giao thức liên lạc của thiết bị tại đây, nơi bạn có thể kiểm tra chi tiết và khả năng của từng giao thức.

Và liên kết tiếp theo khá hữu ích để tìm hiểu thêm về cách sử dụng MQ với xã hội.

Và bạn sẽ thấy rằng có hai cấp độ khác nhau về chất lượng dịch vụ.

Tin nhắn chất lượng mức dịch vụ 0 được gửi không hoặc nhiều lần và nên được sử dụng cho các tin nhắn

được gửi qua các liên kết liên lạc đáng tin cậy hoặc có thể bị bỏ qua mà không gặp vấn đề gì.

Và các tin nhắn chất lượng dịch vụ cấp một được gửi ít nhất một lần và sau đó lặp đi lặp lại cho đến khi công chúng

nhận được phản hồi.

Và bạn sẽ thấy các tùy chọn chất lượng dịch vụ khác nhau được sử dụng và triển khai như thế nào trong mã nguồn.

Bây giờ, hãy xem cách chúng tôi sẽ kích hoạt giao tiếp TE Core của AWG sale trên ESB 32.

Vì vậy, tất nhiên là chúng tôi sẽ sử dụng IWC hoặc TE, nhưng tôi muốn chỉ ra rằng SB 32 hỗ trợ nhiều đám mây

khuôn khổ.

Vì vậy, nếu quan tâm, bạn có thể nhấp vào các liên kết bổ sung tại đây để bắt đầu với những kiến thức cơ bản về

bất kỳ khuôn khổ nào trong số này.

Ví dụ: Google Iot cung cấp các ví dụ riêng mà bạn có thể bắt đầu.

Và họ cũng cung cấp hướng dẫn bắt đầu cho họ.

Được rồi.

Vì vậy, đó là tất cả những gì tôi sẽ đề cập về điều đó.

Bây giờ hãy quay trở lại IWC.

Nhóm bán hàng IWC ESP 32 dựa trên Amazon Web Services, Iot Device SDK và được nhúng.

Hãy xem bạn có thể tìm thấy gì ở đây và chúng ta sẽ thiết lập điều này trong bài học tiếp theo.

Nhưng trước tiên, bạn cần thiết lập tài khoản IWC Iot của mình.

Vì vậy, hãy xem lại quá trình.

Bạn có thể sử dụng liên kết ở đây để thiết lập tài khoản của mình.

Và quá trình này là quá trình đăng ký điển hình.

Bạn chỉ cần cung cấp địa chỉ email của mình và tạo tên tài khoản, xác nhận và tạo mật khẩu,

rồi nhập tên, số điện thoại, địa chỉ và thông tin thẻ tín dụng của bạn để xác minh danh tính

mục đích.

Và sau đó bạn sẽ thấy một thông báo như thế này khi làm như vậy.

Và sau đó bạn cũng có thể cần phải xác minh danh tính của mình bằng số điện thoại.

Và toàn bộ quá trình sẽ mất khoảng 5 phút.

Và tôi cũng chỉ đề cập rằng khi đăng ký, tôi đã chọn gói hỗ trợ cơ bản miễn phí.

Và bạn có thể kiểm tra chi tiết khi bạn đến phần này.

Và sau khi hoàn tất, bạn luôn có thể quay lại bảng điều khiển quản lý thông qua liên kết tại đây.

Vì vậy, hãy thoải mái đánh dấu cái này.

Bây giờ hãy nói về các bước triển khai và cấu hình mà chúng ta sẽ thực hiện.

Đầu tiên, chúng ta sẽ sao chép kho lưu trữ ESP WC Iot và thêm nó vào dự án bằng cách cập nhật CE

tạo tập tin danh sách trong thư mục dự án.

Sau đó, chúng tôi sẽ thêm các tệp mẫu được cung cấp trong tài nguyên dành cho phần này và chúng tôi sẽ

đưa chúng vào bản dựng dự án bằng cách cập nhật tệp danh sách tạo CE trong thư mục chính và sau đó

chúng ta sẽ đi vào bảng điều khiển quản lý lõi Iot và tạo một thứ trong Amazon Web Services.

Và chúng tôi cũng sẽ tạo một chính sách và đính kèm nó vào chứng chỉ thiết bị, sau đó chúng tôi sẽ tạo chứng chỉ

trong khóa chung và khóa riêng, sau đó chúng tôi sẽ cần thêm chứng chỉ và khóa riêng tư như được nhúng

các thành phần ở phía Đông.

Sau đó, chúng tôi sẽ cập nhật mã nguồn để đáp ứng nhiệm vụ AWG Iot Freitas và thêm thành phần lõi Iot

sẽ tăng kích thước ứng dụng của chúng tôi, vì vậy chúng tôi sẽ cần điều chỉnh bảng phân vùng cho phù hợp.

Vậy thì hãy cập nhật cấu hình SDK để bao gồm điểm cuối dữ liệu thiết bị từ tài khoản Amazon Web Services của bạn.

Và sau đó chúng ta có thể flash tới ESB 32 được kết nối với Internet và đăng ký cũng như xuất bản dữ liệu lên và

từ bảng điều khiển RWC.

Và tôi cũng chỉ muốn đề cập rằng chúng ta sẽ sử dụng chức năng gọi lại sự kiện được kết nối của mình và chính C

để bắt đầu nhiệm vụ miễn phí Iot của Hoa Kỳ vì chúng tôi muốn bắt đầu nhiệm vụ đó khi ESP được kết nối với internet.

Và ở bước thứ hai, chúng ta sẽ nhận được chỉ báo cường độ tín hiệu nhận được của kết nối Wi-Fi bằng cách sử dụng

ESP Wi-Fi để nhận API thông tin AP và sẽ xuất bản nó cho nhóm WSU.

Điều này sẽ cho phép bạn theo dõi tình trạng kết nối từ mọi nơi và sau đó cũng sẽ xuất bản

dữ liệu cảm biến nhiệt độ và độ ẩm.

Được rồi, vì vậy hãy nhớ thiết lập Tài khoản cốt lõi của Hiệp hội UAW và LC càng sớm càng tốt.