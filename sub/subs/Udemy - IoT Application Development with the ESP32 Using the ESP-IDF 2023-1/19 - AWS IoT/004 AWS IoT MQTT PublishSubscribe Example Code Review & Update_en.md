# 004 AWS IoT MQTT Xuất bảnĐăng ký Đánh giá và cập nhật mã ví dụ vi

---

Được rồi.

Bây giờ chúng ta sẽ xem lại mã nguồn để triển khai đăng ký xuất bản IWC và chúng ta sẽ tiến hành

để mở rộng nó để xuất bản dữ liệu cảm biến nhiệt độ và độ ẩm cũng như cường độ tín hiệu nhận được

của kết nối Wi-Fi để chúng tôi có thể xem dữ liệu này từ ứng dụng khách thử nghiệm MQ RTT.

Được rồi.

Vì vậy, bắt đầu từ chính, xem ở đây, chúng tôi đang gọi WAC Iot bắt đầu, vì vậy hãy tiếp tục và điều khiển nhấp chuột trái

đi theo chức năng đó.

Và ở đây tôi đã thêm nến thử nghiệm cho tác vụ WC Iot và kiểm tra null để đảm bảo rằng nó đã được tạo

chỉ một lần trong trường hợp hàm gọi lại được gọi nhiều lần.

Và ở đây nến thử nghiệm được tạo và khởi tạo thành null.

Được rồi, hãy tiếp tục.

Và ở đây chúng tôi có chứng chỉ của mình, không cần giải thích nhiều vì chúng tôi đã giải quyết vấn đề này trong

bài học trước mà chúng ta đã thấy rằng WSU T yêu cầu các chứng chỉ nhúng và đây thực tế là

được đưa vào như một phần của quá trình khởi tạo NQT trong tác vụ AWB Iot mà chúng ta sẽ thấy ngay sau đây.

Và sau đó chúng tôi có URL máy chủ nQt mà chúng tôi đã cập nhật thông qua cấu hình SDK.

Nhưng điều này cũng có thể được xác định trực tiếp trong mã nguồn, nếu bạn thích.

Và tiếp theo chúng ta có cổng dành cho người cụt, đó là cổng 8, 8, 3.

Và sau đó là các trình xử lý gọi lại đăng ký và ngắt kết nối.

Và chúng tôi đã thấy cách nhật ký gọi lại đăng ký, dữ liệu chủ đề và trình xử lý ngắt kết nối thử

để kết nối lại tự động hoặc thủ công.

Và tôi sẽ chỉ cho bạn vị trí bật chức năng tự động kết nối lại khi chúng ta tìm hiểu sâu hơn về tệp.

Sau đó, chúng ta có nhiệm vụ WC Iot và đầu tiên một mảng cho tải trọng được tạo và cũng có biến

AI, được sử dụng làm bộ đếm tin nhắn.

Nhưng tôi sẽ không sử dụng biến này khi chúng tôi thực hiện điều chỉnh, nhưng bạn có thể thoải mái giữ nó nếu muốn.

Và ở đây chúng tôi có một số phiên bản bắt nguồn từ SDK thiết bị Iot của MWC và đó là dành cho

Máy khách AWB Society, tham số khởi tạo NQT, tham số kết nối và tham số cho cả chất lượng

về mức độ dịch vụ 0 và chất lượng của các tin nhắn mức dịch vụ một và sau đó là các dòng tiếp theo.

Chú ý đến NQT trong các thông số như tự động kết nối lại.

Host Bạn sẽ có cổng được nhúng chứng chỉ lệnh NQT hết thời gian tính bằng mili giây, TLS

hết thời gian bắt tay, xác minh tên máy chủ SSL và sau đó cung cấp trình xử lý gọi lại ngắt kết nối.

Và sau đó dữ liệu xử lý ngắt kết nối là null và khi các tham số NQT được khởi tạo thì WC

Hàm init Iot nQt được gọi và tham chiếu đến ứng dụng khách Iot AWB được chuyển đến hàm cùng với

với NQT trong các thông số CNTT.

Sau đó, các tham số kết nối được khởi tạo cho kết nối máy khách Iot cùng với AWB cấu hình của chúng tôi

ID khách hàng ví dụ, được xác định trong tệp tiêu đề AWB Iot.

Và đây cũng là tên của bạn trong một xã hội.

Và xin nhắc lại, đây là khách hàng tôi đã làm mà tôi đã đưa vào phần đầu hồ sơ.

Được rồi, bây giờ chúng ta hãy quay trở lại nơi chúng ta đã ở.

Vì vậy, sau khi các tham số kết nối được khởi tạo ở đây, chúng tôi sẽ thử kết nối với wc bằng cách sử dụng

a wc iet nqt connect và chúng ta thực hiện việc này với khoảng cách 1/2 trong khi biến RC không bằng thành công.

Và đây là nơi chức năng tự động kết nối lại được bật và việc đó được thực hiện bằng WSU T và

trạng thái cài đặt tự động kết nối lại nhiệm vụ.

Và đây chính là chức năng tự động kết nối lại mà tôi đã đề cập cho trình xử lý gọi lại ngắt kết nối.

Sau đó, tên chủ đề được xác định và độ dài của nó được lấy để chúng ta có thể sử dụng nó trong wc iet mq để

chức năng đăng ký.

Và hàm này cũng lấy tên hàm xử lý gọi lại đăng ký Iot làm tham số.

Vì vậy, đây là cách chúng tôi đăng ký.

Được rồi.

Tiếp theo, một tham số chất lượng dịch vụ và chất lượng dịch vụ được khởi tạo và tải trọng sẽ được khởi tạo.

biến là bắt buộc.

Ở đây nó được chọn làm con trỏ void.

Và biến tải trọng là thứ chúng tôi chuyển dữ liệu của mình vào khi xuất bản.

Tiếp theo, chúng ta rơi vào vòng lặp hoang dã và ở đó miễn là chúng ta có một trong các trạng thái được đề cập là

được trả về và sau đó là hàm năng suất a wc iet kuti.

Chúng tôi sẽ đợi các tin nhắn màu đỏ và sau đó chúng sẽ nhận được hình mờ cao.

API tự động miễn phí được sử dụng để lấy ngăn xếp còn lại tính bằng byte và một API khác được sử dụng để trả về tên

của nhiệm vụ và nó đăng nhập vào bảng điều khiển, sau đó chúng tôi có độ trễ kiểm soát tần suất chúng tôi muốn

công bố dữ liệu.

Vì vậy tôi sẽ tiếp tục và tăng nó lên 3000 mili giây.

Và ở đây chúng tôi sử dụng printf để cập nhật tải trọng cho chất lượng dịch vụ bằng 0.

Vì vậy, bây giờ chúng ta hãy tiếp tục và cập nhật để bao gồm cường độ tín hiệu nhận được của kết nối Wi-Fi và

Tôi sẽ bao gồm chức năng ở đây, chức năng này sẽ được xác định ngay sau đây.

Nhưng bây giờ, hãy cập nhật văn bản và chúng tôi sẽ cập nhật văn bản thành wi fi hoặc a.

Và ở đây chúng ta sẽ thêm chức năng ứng dụng wi fi, nhận RSS.

Và hàm này sẽ trả về kết thúc.

Vì vậy, phần còn lại của câu lệnh sprint def vẫn ổn và tiếp theo chúng ta sẽ cần cập nhật độ dài tải trọng

và sau đó gọi WC iota trong Quý 2 để xuất bản dữ liệu về chất lượng dịch vụ bằng 0.

Và điều này đảm nhiệm việc xuất bản dữ liệu về chất lượng dịch vụ bằng không.

Tiếp theo, hãy cập nhật tải trọng cho các thông báo chất lượng dịch vụ cấp một, sẽ bao gồm nhiệt độ

và dữ liệu cảm biến độ ẩm.

Vì vậy bây giờ chúng ta hãy thêm văn bản về nhiệt độ.

Sau đó hãy thêm chức năng lấy nhiệt độ.

Sau đó, hãy cập nhật loại def chạy nước rút để trả lại nhiệt độ cho loại float bằng một

dấu thập phân.

Sau đó, hãy thêm một chuỗi khác cho độ ẩm và cũng bao gồm loại cho chức năng lấy độ ẩm

trở lại.

Được rồi.

Bây giờ chúng ta chỉ cần thêm văn bản về độ ẩm.

Và sau đó hãy thêm chức năng này.

Được rồi.

Sau đó, bước tiếp theo bao gồm cập nhật độ dài tải trọng một lần nữa, nhưng lần này là về chất lượng dịch vụ

one rồi gọi wc iut vào quý 2 để xuất bản dữ liệu.

Sau đó, vì đó là chất lượng dịch vụ nên chúng tôi sẽ kiểm tra sự xác nhận.

Được rồi, điều đó có vẻ tốt.

Vì vậy, bây giờ hãy thêm HD 22 chấm H cho các chức năng nhiệt độ và độ ẩm.

Được rồi.

Bây giờ chúng ta có thể truy cập các bản cập nhật wi fi và tạo nguyên mẫu cho chức năng get RSA.

Được rồi.

Và hàm này nhận giá trị RSS.

Của kết nối Wi-Fi.

Trong sự trở lại.

Là mức RSI hiện tại.

Và sự trở lại là một loại.

Và nó được gọi là ứng dụng wi fi.

Hãy tự sát.

Và điều đó là vô nghĩa.

Được rồi.

Bây giờ hãy vào tệp C và xác định nó.

Vì vậy, trước tiên hãy sao chép tên và kiểu trả về.

Hiện nay.

Chúng ta hãy đi xuống phía dưới.

Và dán nó xuống đây.

Và bây giờ chúng ta cần một phiên bản của loại bản ghi ứng dụng wi fi.

Và gọi nó là dữ liệu wi fi.

Và sau đó hãy kiểm tra ESP.

ESP wifi ở lại nhận thông tin ứng dụng.

Và sau đó chúng ta sẽ chuyển loại bản ghi ứng dụng Wi-Fi.

Được rồi.

Và đó là tham chiếu đến dữ liệu Wi-Fi.

Và sau đó chúng tôi chỉ cần trả lại dữ liệu Wi-Fi.

Quyền truy cập vào cấu trúc RSI.

Một thành viên.

Được rồi.

Và đây là nơi chúng ta có thể tìm thấy bản ghi ứng dụng wi fi.

Cùng với thành viên RSI.

Được rồi.

Bây giờ hãy xây dựng cái này và thử nghiệm nó.

Trong nháy mắt nó.

Được rồi, bây giờ hãy mở bảng điều khiển lên.

Được rồi.

Và tất cả điều này có vẻ tốt.

Chuẩn rồi.

Điều đó có vẻ ổn.

Vì vậy, bây giờ chúng ta hãy vào WC và kiểm tra máy khách và xác nhận rằng các giá trị đã được ghi lại.

Được rồi, hoàn hảo.

Dữ liệu được công bố của chúng tôi hiện bao gồm nhiệt độ, độ ẩm và phía RSA, và điều đó thực sự tuyệt vời.

Vậy là bây giờ chúng ta có thể kiểm tra cường độ kết nối Wi-Fi cũng như nhiệt độ, độ ẩm hay bất cứ thứ gì

dữ liệu khác mà bạn muốn xuất bản từ mọi nơi trên thế giới.

Và điều đó thực sự tuyệt vời.

Và bây giờ bạn đã có nền tảng về mạng cục bộ không dây và bây giờ bạn đã biết cách tích hợp

một khung đám mây như WC, giờ đây bạn có thể tự tin khám phá các khung đám mây khác nếu WC không phải là

một cho bạn.

Được rồi, tôi thực sự hy vọng bạn thích điều này và tôi hy vọng sớm gặp lại bạn.