# 005 Go Hỗ trợ trong VSCode vi

---

-: Bây giờ chúng ta đã cài đặt trình soạn thảo VSCode,

chúng ta sẽ thực hiện một chút cấu hình cho nó

để thiết lập nó hoạt động tốt với Golang.

Vì vậy, VSCode không có bất kỳ hỗ trợ nào cho Go.

Chỉ bằng cách cài đặt một phần mở rộng nhỏ,

chúng ta có dạy người soạn thảo cách xử lý mã Go không.

Vì vậy, hãy bắt đầu với nó.

Tôi sẽ mở trình soạn thảo mã Visual Studio,

và khi làm vậy, tôi sẽ tìm thấy menu điều hướng trên cùng ở đây.

Vì vậy, đây là thanh menu trên cùng.

Tôi sẽ tìm thấy tùy chọn "Xem"

và bên trong đó, tôi sẽ tìm thấy tùy chọn "Tiện ích mở rộng".

Vì vậy, đây là phần mở rộng ngay tại đây.

Bây giờ, thanh bên này bật lên

liệt kê rất nhiều tiện ích mở rộng khác nhau mà chúng tôi có thể cài đặt

vào trình soạn thảo mã của chúng tôi.

Rất nhiều tiện ích mở rộng khác nhau hỗ trợ thêm

cho các ngôn ngữ khác nhau bên trong trình soạn thảo,

chẳng hạn như Python hoặc C Sharp, ngay tại đây.

Bây giờ, chúng tôi muốn tìm kiếm một tiện ích mở rộng rất cụ thể.

Chúng ta sẽ nhập vào chuỗi tìm kiếm "Go".

Bây giờ, hy vọng kết quả đầu tiên xuất hiện

có nội dung "Hỗ trợ ngôn ngữ Rich Go

dành cho Visual Studio,"

sẽ có khoảng một, hai, 3 triệu lượt tải xuống.

Và vì vậy, chúng ta sẽ chỉ cần nhấp vào nút cài đặt để cài đặt nó.

Bây giờ, tôi ước mình có thể nói rằng quá trình cài đặt,

hoặc cấu hình cho Go, thật dễ dàng.

Thật không may, chúng ta còn phải làm một bước nhỏ nữa.

Khi chúng tôi cài đặt tiện ích mở rộng hỗ trợ ngôn ngữ Go này

ngay đây, nó thực sự chỉ là một lớp liên kết

giữa trình soạn thảo mã của chúng tôi

và một bộ công cụ dòng lệnh cơ bản

thực sự chịu trách nhiệm về, kiểu như,

thực hiện một số kiểm tra chất lượng mã của bất kỳ tệp đang mở nào.

Và vì vậy, nó là phần mở rộng, mặc dù rất tuyệt vời,

và nó bổ sung thêm sự hỗ trợ cho ngôn ngữ hoặc cho trình soạn thảo của chúng tôi

chúng tôi cũng phải đảm bảo rằng nó có khả năng cài đặt

những công cụ bổ sung này mà nó cần để hoạt động bình thường.

Vì vậy, để đảm bảo rằng nó cài đặt được những công cụ khác này,

thực sự đơn giản,

tất cả những gì chúng ta phải làm là đóng trình soạn thảo mã.

Vì vậy, chúng tôi sẽ thoát khỏi Visual Studio Code hoàn toàn.

Sau đó tôi sẽ bắt đầu lại ngay.

Vì vậy, tôi sẽ bắt đầu lại ngay.

Và sau đó, đây là phần kỳ lạ,

nhưng hãy chịu đựng tôi một chút nhé.

Tôi sẽ đảm bảo rằng tôi có

một cửa sổ soạn thảo mã mở.

Nếu bạn không mở cửa sổ Mã như thế này,

bạn biết một cái mà chúng ta thực sự có thể gõ vào,

bạn có thể đi tới "tập tin" rồi đến "tập tin mới" ở trên đây.

Và thế là, bùm, tôi đã mở một cửa sổ soạn thảo Mã.

Bây giờ, ở phía dưới bên phải,

bạn sẽ thấy thứ gì đó ở đây có nội dung "Văn bản thuần túy".

Vì vậy, chúng ta sẽ nhấp vào đó.

Chúng tôi sẽ thay đổi chế độ ngôn ngữ của trình soạn thảo thành Go.

Vì vậy, tôi sẽ nhập "go" và tôi sẽ thấy tùy chọn Go ở đây.

Bây giờ, khi tôi làm điều đó, bạn sẽ thấy dòng chữ màu vàng này

ở dưới đây, phía dưới cùng bên phải,

thông báo "Thiếu công cụ phân tích".

Và đây là những công cụ bổ sung mà Tiện ích mở rộng Go

cần đảm bảo rằng nó có thể, đại loại,

kiểm tra chất lượng mã của bạn bên trong trình soạn thảo của bạn.

Vì vậy, chúng ta sẽ nhấp vào đây,

và nó sẽ nhắc chúng ta cài đặt

một số công cụ phân tích

Vì vậy, tất cả những gì chúng ta phải làm là nhấp vào "cài đặt",

và chúng ta sẽ thấy một cửa sổ terminal hiện lên ở đây,

và nó sẽ sử dụng một vài công cụ khác nhau.

Và chỉ mất một hoặc hai giây để hoàn thành.

Vì vậy, đó là khá nhiều nó.

Bây giờ, lần tiếp theo chúng ta mở tệp Go

bên trong VSCode, chúng ta sẽ có sẵn rất nhiều công cụ

để giúp chúng tôi viết mã, phân tích nó,

và chỉ cần đảm bảo rằng chúng tôi đang làm mọi việc một cách chính xác.

Như vậy là đã xong phần thiết lập trình soạn thảo mã của chúng ta.

Hãy nghỉ ngơi và quay lại phần tiếp theo,

và chúng ta sẽ bắt đầu nói về dự án đầu tiên

mà chúng tôi sắp làm việc.

Vậy tôi sẽ gặp bạn sau một phút nữa.