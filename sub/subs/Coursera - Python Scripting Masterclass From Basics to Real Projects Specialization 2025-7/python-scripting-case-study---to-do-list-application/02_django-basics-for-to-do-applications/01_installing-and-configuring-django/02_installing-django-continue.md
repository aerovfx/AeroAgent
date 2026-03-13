# 02 cài đặt-django-tiếp tục

---

Được rồi, tôi phải mất một lúc, có thể do kết nối internet, tùy thuộc vào

về tốc độ kết nối internet, ít nhất nó sẽ cài đặt và tải xuống nhanh hơn

tải xuống nhanh hơn.

Vậy là bây giờ nó đã được cài đặt thành công như các bạn thấy, đã cài đặt thành công Django 3.0.4.

Vì vậy, tôi sẽ xóa màn hình và bây giờ chúng ta có một môi trường khép kín nơi chúng ta

đã sẵn sàng để viết mã Django của riêng chúng tôi.

Và như bạn có thể thấy, tên của môi trường ảo xuất hiện trước PSS,

khi chúng tôi tạo các thiết bị đầu cuối tích hợp mới.

Vì vậy, khi bạn nói phím shift và dấu ngã, nó đã tạo ra một thiết bị đầu cuối tích hợp mới cho chúng tôi

và tạo thiết bị đầu cuối tích hợp trong môi trường mà chúng tôi đã tạo.

Thế là xong.

Và bây giờ đến với chính Django, các thuật ngữ của Django, bất kỳ dự án Django cụ thể nào cũng là

bạn biết đấy, bao gồm một số tệp cấu hình cấp trang web, cùng với một hoặc nhiều ứng dụng

mà bạn có thể triển khai lên máy chủ web để tạo một ứng dụng web chính thức.

Vì vậy, một dự án Django có thể chứa nhiều ứng dụng và mỗi ứng dụng thường có một ứng dụng độc lập

chức năng trong dự án.

Vì vậy có thể thêm các thành phần khác nhau vào một dự án.

Vì vậy, mỗi thành phần này có thể có chức năng khác nhau.

Và cùng một ứng dụng cũng có thể có trong nhiều dự án Django.

Vì vậy, ứng dụng cho phần này chỉ là một gói Python, không có gì nhiều, không có gì hơn.

Và nó tuân theo những quy ước nhất định mà Django mong đợi.

Bây giờ chúng ta hãy tạo một ứng dụng Django rất đơn giản và tối giản.

Và điều quan trọng là trước tiên chúng ta phải tạo dự án Django sẽ đóng vai trò là vùng chứa

cho ứng dụng mà chúng tôi sẽ tạo.

Và sau đó chúng ta sẽ tự tạo ứng dụng.

Vì vậy, chúng ta sẽ phải sử dụng tiện ích quản trị của Django và bất cứ điều gì bạn muốn làm với

Django, bạn luôn phải nói quản trị viên Django, được rồi, quản trị viên Django dot, quản trị viên dash, và

sau đó bạn thiết lập các lệnh, khởi động máy chủ và thực hiện nhiều việc với nó.

Vì vậy, nếu bạn muốn đưa ra lệnh cho khung Django, thì bạn phải sử dụng quyền quản trị của nó

cơ sở vật chất.

Và đây là hai từ mà bạn phải sử dụng kết hợp để nêu lên

gọi cơ sở hành chính của Django.

Vì vậy, trước tiên hãy tạo dự án Django.

Vì vậy, hãy để chúng tôi nói quản trị viên Django, và sau đó chúng tôi sẽ bắt đầu dự án, được rồi, đó là lệnh,

bắt đầu dự án và đặt tên cho nó, hãy gọi dự án này là Django, gạch dưới một, sau đó

chúng ta sẽ chỉ nói dấu chấm để, bạn biết đấy, ở cuối thư mục này, nó sẽ tạo ra

thư mục ở đó, nó sẽ chỉ tạo dự án ở đó.

So if I hit enter, and there you go.

Và bạn có thể thấy ở đó, nó đã tạo ra một dự án Django có dấu gạch dưới cho chúng tôi.

Và ngoài ra, nếu bạn mở nó lên, bạn sẽ thấy năm tệp trong đó, gạch dưới dấu gạch dưới

init gạch dưới dấu chấm py và URL cài đặt ASGI, WSGI và chức năng quản lý dấu chấm py chung.

Bây giờ, cái này không hoạt động mà là quản lý dấu chấm p y một tệp Python.

Bây giờ đây là tiện ích quản trị dòng lệnh Django cho dự án.

Vì vậy, chúng ta thực sự có thể nói, tôi sẽ chỉ nói CLS, chúng ta thực sự có thể nói Python quản lý dấu chấm py,

và bạn có thể có các lệnh và bạn có thể có các tùy chọn ở đó.

Vì vậy bạn có thể sử dụng quản lý dấu chấm p y này cho các tiện ích quản trị.

Và chúng tôi cũng có thể thấy một dự án được thêm vào các dự án Django.

Và đây là dự án chúng tôi vừa tạo, chỉ là dự án thôi, chúng tôi chưa có ứng dụng nào cả.

Đây chỉ là một dự án

Và đây là tất cả các tệp cấu hình, tất cả các tệp cấu hình Python.

Vì vậy, cái này, cái đầu tiên, nó chỉ là một tập tin trống sẽ cho Python biết rằng cái này

thư mục là một gói Python.

Và cái thứ hai, ASGI, W hoặc the, bạn có ASGI, đôi khi là WSGI đầu tiên.

Vì vậy đây là thứ mà chúng ta không cần, nó cũng là một file config khác.

Và đây là tập tin cấu hình cấp ứng dụng.

Và sau đó bạn có WSGI.

Và đây là điểm vào cho các máy chủ web tương thích WSGI.

Một lần nữa, chúng ta sẽ không đi sâu vào tất cả những điều đó mà chỉ lướt qua tất cả những điều đó một cách ngắn gọn.

các tệp cấu hình Python khác nhau mà bạn sẽ có trong dự án của mình.

Và bạn thường để nguyên tập tin này.

Và nó cung cấp các kết nối cho các máy chủ web ở cấp độ sản xuất.

Và chúng tôi cũng có các cài đặt, chúng tôi cũng có các URL.

Vì vậy, các cài đặt, nó chứa các cài đặt cho dự án Django cụ thể này.

Và chúng tôi sẽ sửa đổi khi chúng tôi phát triển ứng dụng web này.

Và sau đó chúng ta có URL.py, tệp cấu hình URL.

Và phần này chứa mục lục cho dự án Django.

Chúng tôi cũng sẽ sửa đổi điều này trong tương lai.

Bây giờ, bạn có thể thấy rằng nó có một số vấn đề.

Và đây không phải là lỗi, đây là những cảnh báo nên chúng ta có thể bỏ qua.

Và nó nói rằng việc nhập khẩu chưa được giải quyết, v.v.

Vì vậy bây giờ chúng ta không phải lo lắng về điều đó.

Vì vậy, chúng ta sẽ đóng cái này lại và truy cập init.py.

Và chúng ta sẽ bước ra khỏi đó.

Và bây giờ hãy xác minh dự án Django.

Và chúng tôi sẽ đảm bảo rằng chúng tôi đang ở trong môi trường ảo trước tiên và nó đã được kích hoạt.

Và sau đó hãy khởi động máy chủ phát triển Django.

Và chúng ta sẽ sử dụng lệnh python management.py, gọi tệp tiện ích quản trị.

Và sau đó chúng ta sẽ nói chạy máy chủ.

Và hãy xem điều gì sẽ xảy ra.

Chỉ cần cho nó một chút thời gian.

Thế đấy.

And it has created the server for us.

Và nó cũng đã tạo ra máy chủ và cung cấp cho chúng tôi URL.

Nó cho biết HTTP 127 là máy chủ cục bộ và số cổng là 8800.

Vì vậy, điều này khá phổ biến khi bạn tạo máy chủ lưu trữ cục bộ và đó là URL thông thường.

Vì vậy, nếu tôi điều khiển và nhấp chuột, nó sẽ mở ra trong trình duyệt tôi sử dụng.

Tôi sử dụng Edge.

Và nếu bạn mở trong bất kỳ trình duyệt nào, trình duyệt mặc định cho hệ thống của bạn, bạn sẽ có thể

để xem toàn bộ điều này.

Và nếu bạn có thể nhìn thấy tên lửa này, tên lửa nhỏ với hình ảnh động này và tất cả

trong số những văn bản này, điều đó có nghĩa là tôi đã cài đặt thành công Django.

Và chúng tôi cũng đã tạo một dự án rất đơn giản không có ứng dụng nào trong đó.

Vì vậy, có sự khác biệt giữa dự án và ứng dụng.

Bây giờ chúng tôi biết điều đó.

Và chúng tôi cũng đã tạo một máy chủ và chúng tôi cũng đã kích hoạt máy chủ đó và chúng tôi có thể thấy nó đang chạy

nó ở ngay đây.

Và cái này chẳng có gì cả vì chúng ta chưa có gì bên trong cả.

Chúng tôi không có, chúng tôi chưa viết một dòng mã nào.

Chúng ta sẽ viết điều đó trong chương tiếp theo.

Đây chỉ là về việc cài đặt Django.

Và điều sắp xảy ra là khi chúng ta bắt đầu viết mã, khi bạn bắt đầu tạo

ứng dụng, chúng ta vẫn sẽ sử dụng cùng một máy chủ, cùng một máy chủ cục bộ

máy chủ và chúng tôi sẽ chỉ làm mới trình duyệt và xem điều gì sẽ xảy ra.

Vì vậy, đó là nó bây giờ.

Nếu bạn có thể nhìn thấy thông báo này và hình ảnh động này thì khi bạn mở trình duyệt của mình,

khi bạn nhấp vào Visual Studio Code thì bạn đã cài đặt thành công Django.