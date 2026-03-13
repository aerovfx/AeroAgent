# 002 ESP-IDF FreeRTOS vi

---

Được rồi, vậy hãy tiếp tục với những bài học bổ sung.

Chúng ta hãy xem xét ngắn gọn về ESP IDF Riotous như một tiền đề cho những gì sẽ xảy ra trong quá trình phát triển ứng dụng

bài học.

Vì vậy phạm vi của bài học này sẽ không quá đầy đủ và sẽ chỉ giới hạn ở phần sau.

Tôi sẽ chỉ cho bạn nơi tìm tài liệu nếu bạn muốn tìm hiểu sâu hơn về ảnh miễn phí, sau đó

chúng tôi sẽ xem xét một số điểm khác biệt so với phiên bản ESP IDF của ô tô miễn phí với phiên bản vanilla hoặc miễn phí thông thường

ô tô.

Sau đó, chúng ta sẽ xem xét việc tạo thử nghiệm ở trạng thái Teske và X Test Tạo API Penta Core cũng như

V cũng trì hoãn nhiệm vụ.

Được rồi, vậy hãy nhảy ngay vào.

Được rồi, trong trường hợp bạn là người mới sử dụng ô tô miễn phí, Ô tô miễn phí là nhân hệ điều hành thời gian thực

dành cho các thiết bị nhúng và trang sau từ bộ lưu trữ tự động miễn phí cung cấp mô tả rõ ràng về

một nhà nghệ thuật.

Vì vậy, tóm lại, bộ lập lịch trong Hệ điều hành thời gian thực được thiết kế để cung cấp một lịch trình có thể dự đoán được.

mẫu thực thi và các hệ thống nhúng thường có yêu cầu về thời gian thực, điều đó có nghĩa là chúng phải

phản hồi một sự kiện nhất định trong một thời gian hoặc thời hạn được xác định nghiêm ngặt.

Việc đảm bảo đáp ứng các yêu cầu này chỉ có thể được thực hiện nếu hành vi của bộ lập lịch hệ điều hành

có thể dự đoán được hoặc mang tính quyết định.

Được rồi.

Vì vậy, bạn có thể muốn đánh dấu liên kết này miễn phí hoặc các sách có sẵn từ Tự động khởi động miễn phí.

Tổ chức ở đây.

Thật tuyệt khi có chúng như một nguồn tài nguyên bổ sung.

Và nếu bạn truy cập liên kết miễn phí những nguyên tắc cơ bản đó, bạn sẽ thấy rằng trang này chứa thông tin cơ bản

về các khái niệm đa nhiệm và thời gian thực cơ bản dành cho người mới bắt đầu.

Vì vậy, nếu bạn muốn tìm hiểu sâu hơn về lý thuyết thì đây cũng là một nguồn tài liệu tốt.

Ngoài ra, bạn có thể tìm thấy tài liệu ấn tượng về phiên bản Artus miễn phí của họ bằng cách theo dõi

liên kết này và chúng ta sẽ sớm xem xét các phần của liên kết đó.

Được rồi, vậy là có một số khác biệt rõ ràng giữa xe aespa, xe ID3 và xe thông thường hoặc xe vani.

ô tô miễn phí ảnh hưởng đến việc phát triển ứng dụng.

Thứ nhất, ESP 32 mở rộng MCU chứa hai lõi xử lý mở rộng.

Và IDF sử dụng phiên bản cổng frittatas rộng rãi của riêng mình, cung cấp hỗ trợ đa lõi.

Và vì vậy, trong trường hợp bạn đã quen thuộc với ô tô miễn phí nhưng chưa biết phiên bản IDF, chúng tôi không

phải gọi lịch trình bắt đầu tác vụ V hoặc API khi sử dụng ô tô miễn phí ESP IDF.

Ngoài ra, kích thước ngăn xếp tác vụ ô tô miễn phí được chỉ định theo byte khi sử dụng IDF, không phải từ như bạn muốn

làm với ô tô miễn phí thường xuyên.

Ngoài ra, Quy trình khởi động ứng dụng có liên quan ở đây, bao gồm mọi thứ xảy ra

sau khi ứng dụng bắt đầu thực thi và trước khi chức năng chính bắt đầu chạy bên trong tác vụ chính.

Bạn có thể tìm thấy thông tin chi tiết ở đây với cái nhìn cấp cao về phần khởi động.

Quá trình được mô tả đầu tiên.

Bộ nạp khởi động và rom giai đoạn đầu tiên tải hình ảnh bộ nạp khởi động giai đoạn thứ hai vào RAM từ Flash Offset

Hex một nghìn và bước thứ hai.

Bộ tải khởi động giai đoạn thứ hai tải bảng phân vùng và hình ảnh ứng dụng chính từ Flash.

Ứng dụng chính kết hợp cả hai phân đoạn RAM và đọc trên các phân đoạn này thông qua bộ đệm flash.

Sau đó quá trình khởi động ứng dụng sẽ thực thi và tại thời điểm này, CPU thứ hai và bộ lập lịch tự động được khởi động.

Bạn có thể đọc chi tiết về từng bước này, vì vậy, vui lòng truy cập vào đây nếu bạn quan tâm.

Nhưng bây giờ, hãy chuyển sang chi tiết khởi động ứng dụng.

Và do đó, mọi thứ xảy ra sau khi ứng dụng khởi động và trước khi ứng dụng chính được gọi đều liên quan đến

khởi tạo cổng sau của phần cứng và hệ thống môi trường thời gian chạy C cơ bản, khởi tạo

dịch vụ phần mềm và ô tô miễn phí, đồng thời chạy tác vụ chính và gọi App Main, sẽ là

điểm vào ứng dụng của chúng tôi.

Được rồi, tôi nghĩ đó là đủ thông tin chi tiết về việc khởi động ứng dụng cho các mục đích.

Được rồi, trong một triển khai thiết kế khác, chương trình được chia thành các nhiệm vụ và nhiệm vụ khác nhau.

mỗi tác vụ chạy liên tục trong một vòng lặp vô hạn.

Được rồi, vậy là chúng ta có thể tạo các tác vụ chúc mừng miễn phí bằng cách sử dụng X test, tạo API.

Và để làm được điều đó, chúng ta sẽ cần bao gồm ô tô miễn phí, nhiệm vụ cắt giảm, kho lưu trữ.

Và có hai tùy chọn API có sẵn.

Chúng ta có thể sử dụng X Test Create, cho phép ESP IDF bạo loạn chọn lõi của ESP 32 để

nhiệm vụ nên chạy trên.

Sau đó, đây là cấu trúc cơ bản của một tác vụ bánh mì nướng miễn phí với vòng lặp vô hạn là phần chính của

nhiệm vụ.

Và ở đây API tạo tác vụ X sẽ tạo tác vụ.

Và do đó, tốc độ tác vụ của nó được ghim vào lõi cho phép chỉ định lõi nào sẽ chạy tác vụ tiếp theo.

Tôi sẽ tóm tắt mô tả về các tham số API.

Được rồi, mã kiểm tra PV tham số đầu tiên là hàm C tùy chỉnh hoặc tác vụ gây rối chạy trong một

vòng lặp vô hạn.

Và tên PC là tên mô tả mà bạn có thể giao nhiệm vụ và chỉ được sử dụng làm công cụ hỗ trợ gỡ lỗi.

Độ sâu ngăn xếp của Hoa Kỳ là bộ nhớ và byte cần được hạt nhân phân bổ cho tác vụ.

Tham số PV là tham số tùy chọn, là con trỏ có thể được tác vụ sử dụng.

Mức độ ưu tiên UX là mức độ ưu tiên mà tác vụ sẽ chạy trong số mức độ ưu tiên cao hơn được ưu tiên

và tác vụ được tạo P là một trình xử lý tác vụ tùy chọn mà tác vụ đã tạo có thể được tham chiếu.

Ví dụ: nếu bạn cần sử dụng nhiều KPI tự động miễn phí khác nhau như Xóa tác vụ V, như được hiển thị ở đây với

xử lý tác vụ được tham chiếu.

Và ý tưởng cốt lõi là cốt lõi của ESP 32 mà nhiệm vụ được giao, có thể là cốt lõi

số không hoặc cốt lõi.

Và liên kết này sẽ đưa bạn đến phần mô tả về trạng thái nhiệm vụ cũng như sơ đồ chuyển đổi trạng thái.

Được rồi, chúng ta hãy xem sơ đồ trạng thái và tôi sẽ tóm tắt ngắn gọn các trạng thái của nhiệm vụ.

Vì vậy, trạng thái đang chạy có nghĩa là tác vụ đang thực thi và sử dụng bộ xử lý và trạng thái sẵn sàng

ở đây có nghĩa là tác vụ có thể thực thi nhưng hiện không chạy vì tác vụ có giá trị bằng

hoặc mức độ ưu tiên cao hơn hiện đang chạy.

Vì vậy, nếu một tác vụ bị chặn, điều này có thể do một sự kiện tạm thời gây ra.

Ví dụ: lệnh gọi tác vụ V bị trì hoãn khiến tác vụ được đặt ở trạng thái khối cho đến khi

thời gian trì hoãn đã hết.

Hoặc nó có thể bị chặn do một sự kiện bên ngoài, nghĩa là tác vụ đang chờ nhận từ

một nhóm sự kiện Q hoặc thông báo hoặc một sự kiện tương tự.

Và điều này khác với các tác vụ ở trạng thái treo khi không có thời gian chờ trong các tác vụ chỉ nhập và

thoát khỏi trạng thái bị treo khi được lệnh rõ ràng làm như vậy bằng cách sử dụng V tạm dừng tác vụ và tiếp tục tác vụ X

Cuộc gọi API.

Được rồi.

Và những điều này được liên kết.

Vì vậy, hãy thoải mái đọc những điều đó.

Và về Vitesse DeLay, nó được sử dụng để chuyển một nhiệm vụ sang trạng thái đen trong một số lượng tích tắc nhất định.

Thời gian thực tế mà tác vụ vẫn bị chặn phụ thuộc vào tốc độ đánh dấu và khoảng thời gian đánh dấu cổng không đổi.

Một phần nghìn giây có thể được sử dụng để tính thời gian thực từ tốc độ đánh dấu.

Ví dụ: nếu tốc độ đánh dấu rùa miễn phí trong cấu hình SDK được đặt thành 100 hertz như được hiển thị ở đây,

thì khoảng thời gian đánh dấu cổng này là 10 mili giây và 500 chia cho 10 là 50 tích tắc, đó là những gì chúng tôi đã vượt qua

để kiểm tra độ trễ và đó là độ trễ x.

Trong ví dụ này, với 50 tích tắc trong khoảng thời gian 10 mili giây, chúng ta thu được năm trăm

độ trễ mili giây.

Được rồi, vậy là xong phần tổng quan nhanh về ô tô miễn phí này.