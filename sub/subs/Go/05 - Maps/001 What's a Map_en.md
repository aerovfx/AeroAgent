# 001 Bản đồ là gì vi

---

Giảng viên: Được rồi, đã đến lúc tiếp tục

tính năng lớn tiếp theo của chúng tôi trong Go.

Tôi rất hào hứng với chủ đề tiếp theo,

bởi vì nó sẽ là một cái gì đó kiểu như vậy

so sánh và đối chiếu với một trong những cái trước đó

những tính năng mà chúng ta vừa nói đến,

đó là cấu trúc.

Vì vậy, trong phần này chúng ta sẽ nói về bản đồ.

Vì vậy, bản đồ sẽ rất giống với cấu trúc,

nhưng chúng tôi sẽ đảm bảo rằng chúng tôi chỉ ra

rất nhiều sự khác biệt giữa hai.

Trong Go, bản đồ là tập hợp các cặp giá trị chính.

Và vì vậy, nếu bạn đã quen với các ngôn ngữ khác,

như Ruby, JavaScript, Python,

bạn có thể nghĩ bản đồ giống như một hàm băm trong Ruby,

một đối tượng trong JavaScript hoặc một lệnh hoặc từ điển trong Python.

Bây giờ, bạn sẽ nhớ lại điều đó trong loại bộ sưu tập cuối cùng

của video, tôi đã nói rằng cấu trúc rất giống với

chính xác những đối tượng tương tự.

Và bây giờ tôi muốn nói rằng, à,

đây là hai thứ riêng biệt trong Go

rất giống với hàm băm, một đối tượng và một từ điển.

Vậy trước tiên chúng ta sẽ nói chuyện một chút

về chính xác bản đồ là gì

và một vài tính năng xung quanh chúng.

Và sau đó tôi sẽ kể cho bạn nghe rất chi tiết

chúng khác với cấu trúc trong Go như thế nào

và nơi chúng tôi chọn sử dụng cái này so với cái kia.

Được rồi, điều đầu tiên tôi muốn bạn hiểu

về bản đồ là cả khóa và giá trị

được gõ tĩnh.

Vì vậy, bất cứ khi nào chúng tôi thêm một số phím vào bản đồ trong Go,

tất cả chúng phải cùng loại chính xác.

Và sau đó, tất cả các giá trị khác nhau mà chúng tôi thêm vào

cũng phải cùng loại.

Bây giờ, bản thân các khóa và giá trị không cần phải có

cùng loại, chỉ là tất cả các giá trị khác nhau phải có.

Về cơ bản, chúng ta có một tập hợp các loại ở đây,

và sau đó là tập hợp các loại khác ở đây về phía khóa.

Bây giờ, xét về bản đồ, thực sự không có gì thay thế được

để thực hiện một đoạn mã nhỏ

hoặc chỉ là chơi đùa với họ một chút.

Vì vậy, hãy chuyển sang trình soạn thảo mã của chúng tôi

và chúng ta sẽ thực hiện một dự án nhỏ

để hiểu rõ hơn về cách chúng tôi tạo bản đồ

và cách chúng ta thao túng chúng.

Vì vậy tôi sẽ chuyển sang trình soạn thảo mã của mình

và chúng ta sẽ tạo một thư mục dự án mới

cho ví dụ mới này.

Vì vậy, tôi sẽ đi đến tập tin, mở.

Tôi sẽ tạo một thư mục mới tên là bản đồ,

và sau đó tôi sẽ mở thư mục đó.

Bây giờ, bên trong đây, chúng ta sẽ bắt đầu bằng cách tạo một tệp mới,

vậy là main.go.

Và sau đó, chúng ta sẽ đặt bản soạn sẵn thông thường xuống

cho một tập tin bắt đầu.

Vì vậy, chúng ta cũng sẽ nói package main và func main ở trên cùng.

Bây giờ, tôi mong đợi sau khi in ra một vài dòng khác nhau

mã ở đây chỉ để chúng ta có thể kiểm tra bản đồ

và tìm ra chính xác nó hoạt động như thế nào.

Vì vậy tôi cũng sẽ nhập gói FMT ngay.

Được rồi, bây giờ có nhiều hơn một cách

để khai báo bản đồ trong Go.

Và vì vậy, chúng ta sẽ bắt đầu bằng cách kiểm tra

một vài cách khác nhau để khai báo bản đồ.

Vì vậy, điều đầu tiên chúng ta sẽ xem xét là

cú pháp rất rõ ràng, rất đơn giản, theo nghĩa đen.

Vì vậy chúng ta sẽ tạo một bản đồ có tên là màu sắc

và chúng ta sẽ nói rằng cả khóa và giá trị của nó

có kiểu chuỗi.

Để nói điều đó, chúng ta sẽ nói màu sắc

sẽ được gán bản đồ giá trị.

Chúng ta sẽ đặt các dấu ngoặc vuông, chuỗi,

chúng ta sẽ đóng chúng lại và nói chuỗi lần thứ hai.

Bây giờ, cái này ở đây nói rằng chúng ta đang khai báo một bản đồ

trong đó tất cả các khóa bên trong bản đồ đều thuộc loại chuỗi

và tất cả các giá trị đều thuộc loại chuỗi.

Vì vậy, hãy tìm hiểu cách chúng ta có thể cộng một vài giá trị

vào vấn đề này khi chúng ta tạo bản đồ lần đầu tiên.

Vì vậy tôi sẽ gán cho nó một chuỗi làm phím màu đỏ,

chúng ta sẽ đặt dấu hai chấm,

và sau đó là giá trị mà chúng ta muốn đặt bằng.

Vì vậy, hãy tưởng tượng trong giây lát rằng bản đồ màu sắc này

bằng cách nào đó sẽ liên hệ đến tên của một màu

sang mã hex có cùng màu.

Vì vậy, nếu bạn không quen với màu mã hex, này,

nó thực sự không tệ đến thế

Chúng ta có thể nói mã hex màu đỏ trong Google

và nó sẽ cho chúng ta biết mã hex của màu đỏ

là FF000.

Được rồi, hãy lật lại và nhập nó vào đây.

Vì vậy, hãy nói FF0000.

Bây giờ, để rõ ràng, màu đỏ này

mã hex của một màu này là

chỉ là một ví dụ ở đây, bạn biết đấy,

Tôi chỉ đang tưởng tượng có lẽ chúng ta muốn một ít

loại bản đồ để tìm ra,

cho một tên màu, mã hex của nó là gì.

Vì vậy, không có gì thực sự đặc biệt xảy ra ở đây.

Tôi chỉ muốn một ví dụ điển hình.

Bây giờ, chúng ta có thể thêm bao nhiêu cặp giá trị khóa vào bản đồ này

như chúng tôi mong muốn.

Chúng ta chỉ cần phân tách từng mục bằng dấu phẩy.

Vì vậy chúng ta có thể đặt dấu phẩy,

và sau đó có lẽ chúng ta muốn thêm màu xanh lá cây vào.

Và đó có thể là, tôi không biết,

Tôi chỉ đang bù 745 ở đây thôi.

Điều đó sẽ hiệu quả.

Và sau đó, không giống như các ngôn ngữ khác,

và chúng ta đã thấy điều này với cấu trúc chỉ một giây trước,

mỗi cặp giá trị khóa mà chúng tôi thêm vào,

chúng ta sẽ đặt dấu phẩy sau nó, như vậy.

Vì vậy, điều này khai báo một bản đồ trong đó tất cả các khóa khác nhau

là các chuỗi và tất cả các giá trị cũng là các chuỗi.

Vậy bây giờ chúng ta hãy in bản đồ này ra và xem điều gì sẽ xảy ra.

Vì vậy, chúng ta sẽ nói màu sắc của dòng in FMT, như vậy.

Sau đó, chúng ta sẽ lưu tập tin và lật lại

đến thiết bị đầu cuối của chúng tôi và chạy cái này và xem điều gì sẽ xảy ra.

Vì vậy tôi sẽ chuyển sang bản đồ.

Có tập tin của chúng tôi và chúng tôi sẽ chạy go run main.go.

Thế đấy.

Được rồi, nó cho chúng ta biết đó là một bản đồ.

Chúng tôi có hai cặp giá trị chính.

Đầu tiên là màu đỏ. Đây là giá trị.

Thứ hai là màu xanh lá cây và đây cũng là giá trị của cái đó.

Vì vậy tôi nghĩ rằng ít nhất chúng ta cũng có ý tưởng về cách

chúng tôi tạo một bản đồ ở đây bằng cách sử dụng cú pháp nhỏ đầu tiên này.

Vì vậy, hãy nghỉ ngơi nhanh chóng và quay lại phần tiếp theo,

và chúng ta sẽ xem xét hai cách bổ sung

khai báo và gán bản đồ.

Vậy nên hãy nghỉ ngơi nhanh và tôi sẽ gặp bạn sau một phút nữa.