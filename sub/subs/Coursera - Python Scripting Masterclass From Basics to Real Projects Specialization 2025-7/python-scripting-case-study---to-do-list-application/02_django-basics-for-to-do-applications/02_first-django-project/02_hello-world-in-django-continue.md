# 02 hello-world-in-django-tiếp tục

---

Bây giờ, hãy truy cập vào view.py và tạo một chế độ xem duy nhất cho trang chủ của ứng dụng.

Được rồi.

Và tôi nghĩ chúng ta có thể đóng cái này ngay bây giờ và chúng ta có thể khởi động lại nó.

Vì vậy, nó nói, hãy tạo quan điểm của bạn ở đây và chúng tôi sẽ nói def và chúng tôi sẽ nói home và chúng tôi sẽ nói request.

Được rồi.

Và sau đó chúng ta sẽ nói phản hồi HTTP trả lại, phản hồi HTTP và hãy nói xin chào Django.

Bây giờ, tất nhiên, nó sẽ gặp vấn đề nếu bạn chạy qua tab vấn đề, nó báo là không mong muốn

mã thông báo và phản hồi HTTP mã thông báo không mong muốn.

Đó là vì nếu bạn đã đoán được thì chúng ta phải thay đổi câu lệnh import.

Vì vậy, thay vì nói from Django.shortcuts import render, chúng tôi sẽ nói rằng chúng tôi cũng có from

Django.http và chúng tôi sẽ nhập và chúng tôi sẽ nói phản hồi HTTP.

Thế đấy.

Và tôi tin, vâng, nên tôi cứ quên điều này.

Vì vậy, nó sẽ hoạt động.

Được rồi.

Vì vậy, bây giờ chúng tôi vừa tạo một chế độ xem duy nhất cho trang chủ ứng dụng.

Bây giờ hãy tạo một tệp trong dự án hello Django.

Vì vậy, chúng ta sẽ chỉ cần nhấp vào đây và nhấp vào một tệp mới và chúng ta sẽ gọi đây là urls.py.

Chúng tôi đã tạo một tệp url mới và hãy nhập từ đường dẫn nhập Django.urls.

Được rồi.

Vì vậy, chúng tôi đang nhận được thứ đầu tiên, nhập khẩu thứ đầu tiên.

Và sau đó chúng ta cũng phải nói lời chào Django nhập view.py.

Được rồi.

Và sau đó chúng ta sẽ nói tên bằng nhà và kết thúc ở đó.

Và tôi nghĩ mọi thứ ở đây đều tốt.

Vì vậy, không có vấn đề.

Vâng, nó không có vấn đề gì.

Và thư mục cũng chứa URL, thư mục dự án Django cũng chứa urls.py.

Nếu chúng ta có thể nhấp vào đó ở đây, bạn có thể thấy rằng đây cũng là urls.py thuộc về

dự án Django chứ không phải ứng dụng, mặc dù nó mang tính toàn cầu, nhưng nó

vẫn kết nối với ứng dụng.

Vì vậy, nếu bạn mở nó và chúng tôi phải sửa đổi để nó cũng bao gồm các url hoặc chế độ xem

từ ứng dụng xin chào Django.

Và tệp này thực sự là nơi xử lý việc định tuyến URL.

Được rồi.

Vì vậy, đây là lý do tại sao chúng ta cũng phải sửa đổi tệp cấu hình này.

Được rồi.

Vì vậy, đường dẫn ở đây, chúng ta phải lại, cung cấp đường dẫn dưới dạng một chuỗi trống và chỉ cần xóa nó.

Và trong admin.site.urls, chúng ta sẽ nói bao gồm và chúng ta sẽ nói xin chào, xin chào, Django.urls.

Được rồi.

Và điều đó đề cập đến tệp cấu hình cụ thể mà chúng tôi vừa tạo.

Nếu bạn lưu nó.

Được rồi, vậy hãy lưu tất cả và nói lưu tất cả.

Bây giờ chúng ta hãy quay trở lại CLS terminal của chúng ta.

Và bây giờ hãy chạy máy chủ phát triển, chúng ta sẽ nói python management.py và chúng ta sẽ nói run

máy chủ.

Điều đó sẽ chạy máy chủ, máy chủ cục bộ.

Giả sử bao gồm, tên bao gồm không được xác định, xin chào Django.urls.

Đó là bởi vì chúng ta cũng phải thêm câu lệnh include chính nó vào bên trong

nhập khẩu.

Thế đấy.

Bây giờ điều đó sẽ ổn thôi.

Được rồi.

Và bây giờ nó sẽ tạo một máy chủ.

Hoàn hảo.

Và bây giờ nếu tôi nhấp vào đây, bạn sẽ thấy.

Vì vậy, xin chào Django có thể nhìn thấy được.

Hoàn hảo.

Được rồi.

Vì vậy, bây giờ chúng ta đã có câu chào Django, chúng ta đã hứa rằng tôi đã nói với bạn rằng chúng ta sẽ

thực sự viết một cái gì đó phức tạp hơn một chút so với chỉ đơn giản là chuỗi hello world được in trên

màn hình.

Vì vậy, hãy làm điều đó ngay bây giờ.

Vì vậy, chúng ta sẽ quay lại đây và bên trong view.py là nơi chúng ta đã viết hàm,

home và sau đó chúng tôi chỉ trả lại phản hồi HTTP.

Bây giờ chúng ta biết rằng điều này đang trả về một giá trị chuỗi.

Vì vậy, tất cả những gì chúng ta phải làm là đưa vào, bạn biết đấy, mã giai thừa và

đầu ra của mã giai thừa đó phải được lưu trữ bên trong một biến chuỗi.

Và sau đó chúng ta sẽ chỉ chuyển biến chuỗi vào bên trong hàm trả về này.

Vì vậy, hãy làm điều đó.

Vì vậy, trước khi tạo hàm này, hãy viết mã đơn giản đó.

Vì vậy, tôi sẽ đi qua, tôi sẽ không viết mã đó, tôi chỉ nói Ripple.it.

Được rồi.

Vì vậy tôi chỉ cần mở tập tin đó lên, vào hello Python, bạn không cần phải viết tiếp

điều đó lặp đi lặp lại.

Và thế là xong.

Vì vậy, chúng ta đừng đưa sự thật vào câu lệnh in, chúng ta chỉ đưa vào hàm này

xác định giai thừa n.

Vì vậy, tôi sẽ sao chép nó, quay lại mã Visual Studio của tôi và dán nó.

Và điều này sẽ xảy ra, vết lõm sẽ bị rối tung.

Vì vậy, chúng ta sẽ sửa nó trước.

Và thế là xong.

Vì vậy, điều này là tốt.

Bây giờ có lẽ chúng ta sẽ thay đổi, tôi nghĩ thế là đủ rồi.

Vâng.

Chúng ta không cần phải thay đổi bất cứ điều gì ở đây.

Bây giờ giả sử đầu ra bằng giai thừa.

Và chúng tôi sẽ chuyển vào năm phần và sau đó bên trong phản hồi HTTP, chúng tôi sẽ chỉ đưa đầu ra vào.

Và vì đây là biến chuỗi nên nó không phải là một chuỗi nhỏ mà nó chứa chuỗi

bên trong.

Vì vậy, chúng ta chỉ cần chuyển vào biến.

Được rồi.

Vậy chúng ta hãy quay lại và kết thúc điều này.

Chúng tôi không cần điều này ngay bây giờ.

Và nếu bạn làm mới phần này, bạn có thể thấy 120.

Và nếu bạn muốn xem liệu nó có thực sự hiệu quả hay không, hãy cho là bốn.

Vậy sẽ là bốn thành ba thành hai thành một.

Vậy 12 chia hai, 24.

Vậy cái này sẽ in ra 24 cho chúng ta.

Nếu tôi quay lại và nhấn nút làm mới, bạn có thể thấy nó hoạt động rất tốt.

Được rồi.

Vậy là chúng tôi đã viết ứng dụng Django đầu tiên của mình.

Chúng tôi đã học cách tạo máy chủ.

Chúng tôi đã học cách đóng máy chủ.

Chúng tôi cũng đã biết được điều đó và chúng tôi cũng đã cài đặt SQLite từ Market.

Chúng tôi cũng biết rằng khi bạn chạy máy chủ lần đầu tiên, nó sẽ tạo cơ sở dữ liệu thử nghiệm

đối với bạn, SQLite thuộc loại SQLite.

Và sau đó chúng tôi cũng tạo một ứng dụng mới có tên HelloDjango.

Và chúng tôi đã tạo một URL mới, một tệp cấu hình và chúng tôi đã thêm tất cả mã này vào bên trong.

Và sau đó chúng tôi nối các URL này với các URL chính của dự án Django như thế này.

Và sau đó, bên trong các khung nhìn, chúng tôi đã tạo một khung nhìn mới ở đây.

Và đây là chế độ xem mặc định mà chúng tôi đã quyết định rằng trang web sẽ có được thời điểm hiện tại

chạy.

Đó là những gì chúng tôi đã làm.

Và lần đầu tiên chúng tôi sử dụng một chuỗi hello world đơn giản và chúng tôi đã thử nghiệm nó tốt.

Và sau đó chúng tôi đưa vào cùng một đoạn mã giai thừa mà chúng tôi đã viết kể từ chương này.

hai cái gì đó

Và sau đó chúng ta sử dụng đầu ra của hàm giai thừa đó làm đầu ra của hàm này

được gọi là phản hồi HTTP.

Và một khi các lượt xem, vì chúng tôi đang kết nối các lượt xem với các URL ở đây và các URL này

đang được kết nối với các dự án Django, URL của dự án chính, mọi thứ đều hoạt động

liền mạch.

Thế là xong.

Và bây giờ chúng ta có thể thoát khỏi máy chủ.

Và hãy bắt đầu với việc thiết kế ứng dụng danh sách việc cần làm của chúng tôi, một ứng dụng danh sách việc cần làm trong

chương tiếp theo.

Chúng ta sẽ bắt đầu thiết kế nó và sẽ bắt đầu phát triển nó từ chương tiếp theo.

Chúng tôi đã hoàn tất việc cài đặt và chúng tôi đã hoàn tất tất cả các công việc nền tảng cần thiết

để chúng tôi phát triển ứng dụng đó.