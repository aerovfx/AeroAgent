# 002 Phần bổ sung kỹ thuật AWS IoT MQTT, mTLS, Bảo mật & chính sách AWS và JSON en

---

Trong bài học này, chúng ta sẽ xem xét một số chi tiết kỹ thuật về các quá trình cơ bản của một xã hội và điều này

sẽ chuẩn bị cho chúng ta những bài học tiếp theo nơi chúng ta thực hiện.

Vì vậy, trong phần tóm tắt này, chúng ta sẽ xem xét thêm một chút về Kuti cũng như những kiến ​​thức cơ bản về xác thực WC Iot.

Và chúng ta cũng sẽ xem xét ngắn gọn hơn về TLS hoặc MTA lẫn nhau.

Và sau đó chúng ta sẽ xem xét bảo mật WC liên quan đến chứng chỉ và khóa của thiết bị.

Và điều đó sẽ dẫn chúng ta đến các chính sách của WC Iot, sau đó sẽ tách chúng ta thành JSON.

Vì vậy, hãy đi sâu vào ngay.

Được rồi, bây giờ trở lại trống rỗng.

Trống là viết tắt của MQ Telemetry Transport.

Và một lần nữa, đó là một giao thức nhắn tin nhẹ đơn giản được thiết kế cho các thiết bị có giới hạn tài nguyên trên

mạng bị hạn chế.

Và tắt tiếng là tiêu chuẩn cho nhắn tin Iot.

Và nó được sử dụng vì nó yêu cầu tài nguyên và băng thông mạng tối thiểu trong khi vẫn đảm bảo độ tin cậy

và một số mức độ đảm bảo giao hàng.

Và đây là điều khiến mq t trở nên lý tưởng trong các thiết bị được kết nối giữa máy với máy hoặc Internet of Things trong đó

cả băng thông và năng lượng pin đều có thể bị hạn chế.

Vì vậy MQ t sử dụng mô hình máy chủ khách trong đó mọi thiết bị Iot đều là máy khách và được kết nối với máy chủ có tên

một nhà môi giới NQT, chẳng hạn như AWB Stewart chẳng hạn.

Vì vậy, trong mô hình này, khách hàng gửi tin nhắn đến một địa chỉ được gọi là chủ đề.

Sau đó, nhà môi giới MQ sẽ chuyển tiếp tin nhắn đó tới tất cả khách hàng đã đăng ký chủ đề đó.

Ví dụ: ở đây chúng tôi có Thing X công bố trạng thái dẫn đầu cho chủ đề chính.

Sau đó, nhà môi giới MQ sẽ chuyển tiếp thông báo trạng thái dẫn đến điều y và điều.

Các khách hàng đều đã đăng ký vào chủ đề chính.

Được rồi.

Bây giờ chúng ta hãy xem thông tin cơ bản về xác thực thiết bị WSI Iot, thiết bị WC Iot được xác thực bằng cách sử dụng

xác thực TLS lẫn nhau với chứng chỉ x509 và sau đó mật mã x509 là Viễn thông quốc tế

Tiêu chuẩn liên minh xác định định dạng của chứng chỉ khóa công khai.

Vì vậy, khi chứng chỉ được cung cấp không được kích hoạt, nó có thể được cài đặt trên thiết bị.

Sau đó, thiết bị sẽ sử dụng chứng chỉ đó cho tất cả các yêu cầu gửi đến một xã hội và chúng tôi sẽ tạo

các chứng chỉ cần thiết trong WC và nhúng chúng vào ESP 32 trong bài học tiếp theo.

Bây giờ chúng ta hãy đề cập đến TLS MTA chung.

Ít hơn được sử dụng để thiết lập lòng tin giữa hai bên và đảm bảo rằng các bên ở mỗi đầu của

mạng lưới là những người mà họ tuyên bố là.

Bằng cách xác minh rằng cả hai đều có khóa riêng chính xác và thông tin trong TLS tương ứng của họ

chứng chỉ cung cấp xác minh bổ sung.

Và sau này chúng tôi thấy rằng chúng tôi đã thực hiện cái được gọi là chứng chỉ gốc, chứng chỉ ủy quyền và chứng chỉ gốc.

Chứng chỉ TLS ít cần thiết hơn đối với MTA và điều này cho phép một tổ chức trở thành chứng chỉ của riêng họ

thẩm quyền.

Các chứng chỉ được sử dụng bởi máy khách và máy chủ được ủy quyền phải tương ứng với chứng chỉ gốc,

và chứng chỉ gốc này được tự ký, nghĩa là tổ chức tự tạo ra nó.

Và một lần nữa, trong bài học tiếp theo chúng ta sẽ tải CAA gốc trực tiếp từ WC.

Và trong trường hợp WC, họ cung cấp chứng chỉ và khóa thiết bị dưới dạng A.W. với tư cách là cơ quan cấp chứng chỉ

cho các thiết bị Iot.

Vì vậy, trong trường hợp này, chứng chỉ và khóa được cài đặt trên thiết bị và thiết bị sẽ sử dụng

chứng chỉ và chìa khóa đó để xác thực chính nó với một xã hội.

Ngoài ra, trong trường hợp này, để thực hiện thao tác WSOP với thiết bị của mình, bạn phải tạo một

Chính sách AWG Iot và đính kèm nó vào chứng chỉ thiết bị của bạn và chúng ta sẽ thực hiện quy trình này trong phần tiếp theo

bài học.

Bây giờ chúng ta hãy thảo luận về các chính sách về chính sách Iot của Hoa Kỳ.

Các chính sách này là các tài liệu JSON cho phép thiết bị của bạn thực hiện các hoạt động AWG Iot.

IWC IOT xác định một tập hợp các hành động chính sách mô tả các hoạt động và tài nguyên mà bạn có thể cấp

hoặc từ chối truy cập.

Và đây chỉ là một vài ví dụ.

IoT Connect thể hiện quyền kết nối với nhà môi giới tin nhắn Iot và đăng ký Iot thể hiện quyền

để kết nối với một chủ đề trống hoặc bộ lọc chủ đề.

Vì vậy, tài liệu chính sách ở dạng ký hiệu đối tượng JSON hoặc JavaScript, đây là một tiêu chuẩn mở nhẹ

dạng trao đổi dữ liệu.

Và là một tài liệu văn bản, người dùng có thể đọc và viết cũng như máy phân tích và tạo dễ dàng hơn.

Và chúng ta cũng sẽ thực hiện điều này trong bài học tiếp theo, nhưng chúng ta không phải tạo tài liệu chính sách JSON theo cách thủ công.

Chúng tôi sẽ sử dụng trình tạo ở đây và cho phép từng hành động sau đó.

Được rồi.

Vậy chúng ta hãy tiếp tục ở bài học tiếp theo.