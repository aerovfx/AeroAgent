# 001 Trình kiểm tra trạng thái trang web vi

---

Trong phần này, chúng tôi sẽ bắt đầu các tính năng tiếp theo của chúng tôi trong trình cài đặt ngôn ngữ Inside the Go.

Vì vậy, trong video này, trong phần tiếp theo, chúng tôi sẽ bắt đầu nói về các kênh và quy trình.

Kênh và quy trình đều là cấu trúc bên trong được sử dụng để xử lý các chương trình đồng thời.

Và vì vậy, chúng tôi sẽ hiểu ý nghĩa chính xác của quá trình cài đặt vào thời điểm hiện tại

nghĩa là gì.

Trước tiên, chúng ta sẽ bắt đầu tất cả cuộc thảo luận này bằng cách viết một chương trình nhỏ mà chúng ta sẽ

viết theo kiểu rất ngây thơ hoặc đơn giản, và chúng tôi sẽ không sử dụng bất kỳ công cụ đồng thời nào

v.v. thích hợp nào.

Chúng tôi sẽ viết chương trình.

Chúng tôi sẽ quan sát thấy rằng có một số vấn đề và sau đó chúng tôi sẽ tìm ra cách chúng tôi

có thể sử dụng một số đồng thời gian này để giải quyết sự cố của chúng tôi hoặc sửa chữa chương trình của chúng tôi và làm cho nó hoạt động

nhiều hơn nữa theo cách mà chúng tôi mong đợi.

Vì vậy, hãy bắt đầu bằng cách nói về những gì chúng tôi sẽ xây dựng.

Vì vậy, chúng tôi sẽ xây dựng một chương trình nhỏ có nghĩa là nó sẽ trở thành một loại trình kiểm tra trạng thái cho

một số trang web phổ biến tồn tại trực tuyến.

Vì vậy, chúng tôi sẽ tạo một chương trình nhỏ này để lấy danh sách các trang web phổ biến hoặc

biến rất phổ biến và thực hiện yêu cầu HTTP đến từng trang web này.

Và ý tưởng ở đây là chúng tôi có thể kiểm tra để chắc chắn rằng mỗi trang web này đều hoạt động

và phản hồi với lượng truy cập HTTP được lưu trữ.

Vì vậy, tôi có thể tưởng tượng rằng chúng tôi sẽ chạy chương trình này một vài lần trong ngày

và nói, đã được rồi, có vẻ như tất cả các trang web này đều hoạt động và hiển thị hoặc Không, có thể trang này được hiển thị

đang bị hỏng và chúng tôi phải đăng một số trạng thái thông báo cho biết rằng, có vẻ như Facebook đã ngừng hoạt động vì không thể truy cập được.

Vì vậy, một lần nữa, chúng tôi sẽ viết chương trình này theo một cách tiếp cận rất đơn giản.

Để bắt đầu, chúng tôi sẽ quan sát thấy rằng có một số vấn đề về việc phát triển việc khai trương của chúng tôi và sau

chúng tôi sẽ tìm cách sử dụng những kênh thứ thường xuyên này và những kênh thứ này để giải quyết chương trình.

Vì vậy, với suy nghĩ đó, hãy bắt đầu.

Tôi sẽ chuyển mã soạn thảo của mình và tôi sẽ tạo một dự án thư mục mới.

Vì vậy, chúng tôi sẽ mở.

Tôi sẽ tạo một thư mục mới và chúng tôi sẽ gọi đây là thư mục của các kênh và chúng tôi sẽ mở thư mục này và sau đó tạo

tệp dot go main của chúng tôi bên trong nó.

Vì vậy, chúng tôi sẽ nói chính đi và sau đó chúng tôi sẽ bắt đầu với đoạn mã rất bình thường mà chúng tôi rất quen viết.

Tại thời điểm này, chúng tôi sẽ nói Package Main và func main như vậy, đã được rồi, vì chương trình thực tế hoặc logic bên trong nó cho vòng lặp

Điều đầu tiên này chúng tôi sẽ thực hiện một cách tiếp cận rất đơn giản sẽ không liên kết

quan đến bất kỳ mã nào mà chúng tôi chưa thực sự viết trước đây.

Vì vậy, chúng tôi sẽ liệt kê một số trang web rất phổ biến như những trang web này ngay tại đây.

Chúng tôi sẽ liệt kê các URL thực tế cho từng URL trong một chuỗi.

Sau đó, chúng tôi sẽ lặp lại phần đó và đối với từng URL bên trong phần này, chúng tôi sẽ cố gắng thực hiện một HTTP yêu cầu và

cùng một cách chính xác mà chúng tôi đã thực hiện ở đây một chút.

Nếu sau đó chúng tôi có thể thực hiện yêu cầu thành công, chúng tôi sẽ đưa ra một thông báo thành công.

Nhưng nếu xảy ra lỗi với yêu cầu, bất kỳ loại lỗi nào, chúng tôi sẽ gặp một

thông báo có nội dung: Cái này có vẻ như có thể là facebook. com hoặc golang dot org có down hay không.

orbcomm link get link.

Chỉ cần truy cập vào liên kết dot org.

Xin lỗi cho tôi hỏi.

Vì vậy, hay thực hiện ngay bây giờ.

Quay lại bên trong trình chỉnh sửa mã của tôi.

Trước tiên, tôi sẽ bắt đầu bằng cách tạo một máy tính chuỗi đã được đánh dấu và liệt kê một vài trang

web khác nhau.

Vì vậy, chúng tôi sẽ nói về các chức năng liên kết chính của chúng tôi.

Vì vậy, đó sẽ là tên của tất cả các URL khác nhau mà chúng tôi muốn tìm tải

will be type string, lát của loại chuỗi, rõ ràng.

Và sau đó chúng tôi sẽ liệt kê một số trang web khác nhau.

Vì vậy, chúng tôi sẽ nói http, gạch ngang, gạch chéo google. com, chém gió chém gió facebook. com.

Chúng tôi sẽ nói về Stack Overflow và chúng tôi sẽ thực hiện thêm hai bước nữa.

Giả sử http, truy cập liên kết dot org và Amazon. com.

Được chứ.

Vì vậy, hãy đảm bảo rằng bạn có dot com trên tất cả những thứ này, ngoại trừ Golang, là một dot org.

Và hãy chắc chắn rằng bạn cũng liệt kê các giao thức.

Hãy nhớ rằng, với các mô-đun HTTP mà chúng tôi đang sử dụng, nó hy vọng sẽ được tìm thấy toàn bộ

giao thức phía trước miền thực thi.

Vì vậy, chúng tôi phải nói đầy đủ dấu gạch chéo, dấu gạch ngang HTTP đầy đủ, và sau đó cũng phải đảm bảo rằng bạn đã nhận được dấu gạch ngang

comoma ở cuối mỗi dòng, bao gồm cả mục cuối cùng ở đây.

Vì vậy, hiện tại chúng tôi có thể lặp lại phần này ngay tại đây và đối với mỗi URL bên trong nó, chúng

ta sẽ thực hiện một HTTP yêu cầu.

Vì vậy, trước tiên chúng ta sẽ thiết lập vòng lặp để lặp lại tất cả các liên kết khác nhau.

Bây giờ, chúng tôi không thực sự quan tâm đến chỉ mục của bất kỳ mục nào trong số này ở đây.

Giống như chỉ mục là loại vô nghĩa đối với chúng tôi.

Vì vậy, chúng tôi sẽ bỏ qua các chỉ mục biến mà chúng tôi sẽ chuyển vào bên trong vòng lặp bằng cách đặt dấu gạch dưới.

Nhưng chúng ta sẽ nhận được đối số thứ hai, sẽ là phần tử thực tế mà chúng ta đang lặp

lại.

Vì vậy, trong trường hợp này, chúng tôi chỉ cần gọi nó là một liên kết, chúng tôi sẽ nói dấu hai chấm bằng phạm vi.

Và sau đó, cắt lát mà chúng ta đang lặp lại, sẽ là các liên kết ngay bây giờ bên trong hàm này, tôi nghĩ rằng điều đó tạo ra

tôi khó chịu bên trong vòng lặp cho điều này.

Tôi nghĩ rằng sẽ rất thông minh nếu có thể không thực hiện yêu cầu HTTP thực tế trực tiếp tại đây.

Tôi nghĩ rằng có lẽ chúng ta nên tập hợp một chức năng đặc biệt để đưa ra yêu cầu thực tế và

định nghĩa xem trang web có đáp ứng lưu lượng truy cập hay không.

Vì vậy, họ tận dụng tốc độ nhanh chóng và sau đó tiếp tục trong phần tiếp theo và kết hợp chức năng

Điều này để lấy từng liên kết và thực hiện một yêu cầu HTTP tới nó.

Vì vậy, hãy nhanh chóng nghỉ ngơi và tôi sẽ gặp lại bạn sau một phút.