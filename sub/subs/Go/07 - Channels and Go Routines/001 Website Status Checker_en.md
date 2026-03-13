# 001 Trình kiểm tra trạng thái trang web vi

---

Giảng viên: Phần này chúng ta sẽ bắt đầu

tính năng lớn tiếp theo của chúng tôi trong ngôn ngữ lập trình Go.

Vì vậy, trong video này, trong cặp đôi tiếp theo,

chúng ta sẽ bắt đầu nói về các kênh và goroutine.

Các kênh và goroutine đều là cấu trúc bên trong Go

được sử dụng để xử lý lập trình đồng thời.

Và vì thế chúng ta sẽ hiểu rõ hơn

về chính xác ý nghĩa của việc lập trình đồng thời

hoặc đồng thời có nghĩa là gì.

Đầu tiên chúng ta sẽ bắt đầu cuộc thảo luận này

bằng cách viết một chương trình nhỏ mà chúng ta sẽ viết

một cách rất ngây thơ hoặc đơn giản.

Và chúng tôi sẽ không sử dụng bất kỳ

về những thứ đồng thời thú vị này.

Chúng ta sẽ viết ra chương trình.

Chúng ta sẽ quan sát

rằng nó có một số vấn đề,

và sau đó chúng ta sẽ tìm ra cách có thể sử dụng

một số tính năng đồng thời bên trong Go

để khắc phục vấn đề của chúng tôi hoặc sửa chữa chương trình của chúng tôi

và làm cho nó hoạt động hiệu quả hơn theo cách chúng ta mong đợi.

Vì vậy hãy bắt đầu bằng cách nói về

những gì chúng ta sẽ xây dựng.

Được rồi, chúng ta sẽ xây dựng một chương trình nhỏ

rằng nó là một loại công cụ kiểm tra trạng thái

đối với một số trang web phổ biến tồn tại trực tuyến.

Vì vậy chúng ta sẽ thực hiện chương trình nhỏ này

có danh sách các trang web rất phổ biến hoặc rất phổ biến

và thực hiện yêu cầu HTTP GET tới từng trang web này.

Và ý tưởng ở đây là chúng ta có thể kiểm tra

để đảm bảo rằng mỗi trang web này đều hoạt động

và phản hồi lưu lượng HTTP.

Và vì vậy chúng ta có thể tưởng tượng rằng có lẽ

chúng tôi sẽ chạy chương trình này nhiều lần trong ngày và nói,

"Được rồi, có vẻ như tất cả các trang web này đều hoạt động bình thường."

Hoặc "Không, có lẽ cái này bị hỏng.

"Và chúng ta cần đăng xuất một số thông báo trạng thái

"điều đó cho thấy rằng, này, có vẻ như

"Facebook ngừng hoạt động vì không thể truy cập được."

Vì vậy, một lần nữa, chúng ta sẽ viết ra chương trình này

theo một cách tiếp cận rất đơn giản để bắt đầu.

Chúng ta sẽ quan sát thấy có một cặp đôi

về các vấn đề với việc triển khai của chúng tôi,

và sau đó chúng ta sẽ tìm ra

cách chúng tôi sử dụng những thứ goroutine này

và những kênh này để sửa chữa chương trình.

Vì vậy, với ý nghĩ đó, chúng ta hãy bắt đầu.

Tôi sẽ chuyển sang trình soạn thảo Mã của mình

và tôi sẽ tạo một thư mục dự án mới.

Vì vậy chúng ta sẽ nhấn Mở.

Tôi sẽ tạo một thư mục mới

và chúng ta sẽ gọi cái này là kênh, còn kênh thì sao?

Và chúng ta sẽ mở thư mục này

và sau đó tạo tệp main.go của chúng ta bên trong nó.

Vậy chúng ta sẽ nói gì về main.go.

Và sau đó chúng ta sẽ bắt đầu với đoạn mã rất thông thường

mà chúng tôi đã rất quen với việc viết vào thời điểm này.

Chúng ta sẽ nói package main và func main như vậy.

Được rồi, chương trình thực tế hoặc logic bên trong nó

cho lần lặp đầu tiên này thông qua đó

chúng ta sẽ thực hiện một cách tiếp cận rất đơn giản với

sẽ không liên quan đến bất kỳ mã nào

mà chúng tôi chưa thực sự viết trước đây.

Vì vậy chúng tôi sẽ liệt kê ra một vài

của những trang web rất phổ biến như những trang này ngay tại đây.

Chúng tôi sẽ liệt kê các URL thực tế

cho mỗi trong số chúng bên trong một lát chuỗi kiểu.

Sau đó chúng ta sẽ lặp qua lát cắt đó.

Và với mỗi URL bên trong lát cắt,

chúng tôi sẽ cố gắng thực hiện một yêu cầu HTTP

theo cùng một cách chính xác mà chúng tôi đã làm

chỉ một chút trước đây.

Nếu sau đó chúng tôi có thể thực hiện yêu cầu thành công,

chúng tôi sẽ in ra một thông báo thành công.

Nhưng nếu có lỗi xảy ra với yêu cầu,

bất kỳ loại lỗi nào,

chúng tôi sẽ in ra một thông báo có nội dung:

"Này, có vẻ như facebook.com

hoặc golang.org.com không hoạt động, hoặc không golang.org.com,

chỉ golang.org, xin lỗi.

Vì vậy, hãy bắt đầu với nó.

Quay lại trình soạn thảo Mã của tôi, trước tiên tôi sẽ bắt đầu

bằng cách tạo một lát chuỗi kiểu

và liệt kê một số trang web khác nhau này.

Vì vậy, chúng tôi sẽ nói bên trong các liên kết chức năng chính của chúng tôi.

Vì vậy, đó sẽ là tên của tất cả các URL khác nhau

mà chúng ta muốn tìm nạp sẽ có kiểu chuỗi,

lát của chuỗi loại phải rõ ràng.

Và sau đó chúng tôi sẽ liệt kê ra một vài

của các trang web khác nhau này.

Vì vậy chúng ta sẽ nói http://google.com, //facebook.com.

Vì vậy chúng ta sẽ nói http://google.com, //facebook.com.

Chúng tôi sẽ nói stackoverflow và chúng tôi sẽ làm thêm hai điều nữa.

Giả sử http://golang.org và amazon.com.

Giả sử http://golang.org và amazon.com.

Được rồi, vì vậy hãy đảm bảo bạn có .com trên tất cả những thứ này

ngoại trừ golang, là một .org.

Và hãy đảm bảo rằng bạn cũng liệt kê ra giao thức.

Hãy nhớ rằng, với mô-đun HTTP bên trong Go

mà chúng tôi đang sử dụng, nó mong đợi được thấy

toàn bộ giao thức phía trước tên miền thực tế.

Vì vậy chúng ta phải nói đầy đủ http://.

Và sau đó, hãy đảm bảo

rằng bạn nhận được một dấu phẩy ở cuối mỗi dòng

bao gồm cả mục cuối cùng ở đây.

Được rồi, bây giờ chúng ta có thể lặp lại lát cắt này ngay tại đây.

Và với mỗi URL bên trong nó,

chúng ta sẽ thực hiện một yêu cầu HTTP.

Vì vậy, trước tiên chúng ta sẽ thiết lập vòng lặp for

để lặp qua tất cả các liên kết khác nhau này.

Bây giờ, chúng tôi không thực sự quan tâm đến chỉ số

của bất kỳ mục nào ở đây

giống như chỉ mục này là vô nghĩa đối với chúng tôi.

Vì vậy chúng ta sẽ bỏ qua biến chỉ số

mà chúng ta vượt qua được bên trong vòng lặp for

bằng cách đặt dấu gạch dưới.

Nhưng chúng ta sẽ nhận được đối số thứ hai

đó sẽ là yếu tố thực tế

mà chúng tôi đang lặp đi lặp lại.

Vì vậy, trong trường hợp này, chúng tôi sẽ gọi nó là một liên kết.

Chúng ta sẽ nói :=range,

và sau đó là lát cắt chúng ta đang lặp lại

đó sẽ là các liên kết.

Bây giờ, bên trong hàm này, tôi nghĩ rằng,

hoặc xin lỗi, bên trong vòng lặp for này,

Tôi nghĩ sẽ là thông minh nếu có thể

không thực hiện yêu cầu HTTP thực tế trực tiếp tại đây.

Tôi nghĩ có lẽ chúng ta nên tập hợp lại

một chức năng riêng biệt để thực hiện yêu cầu thực tế

và quyết định xem trang web có

có phản ứng với giao thông hay không.

Vì vậy chúng ta hãy nghỉ ngơi nhanh chóng

và sau đó tiếp tục trong phần tiếp theo

và kết hợp chức năng này để lấy từng liên kết

và thực hiện một yêu cầu HTTP tới nó.

Vậy nên hãy nghỉ ngơi nhanh và tôi sẽ gặp bạn sau một phút nữa.