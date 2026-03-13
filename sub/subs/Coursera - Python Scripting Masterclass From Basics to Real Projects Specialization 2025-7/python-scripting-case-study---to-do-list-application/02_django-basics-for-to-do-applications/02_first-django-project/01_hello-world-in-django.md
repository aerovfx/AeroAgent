# 01 xin chào thế giới ở django

---

Xin chào, chào mừng bạn quay trở lại với chương này, chúng ta sẽ bắt đầu viết chương trình hello world

ở Django.

Mặc dù nó sẽ không phải là hello world nhưng nó sẽ phức tạp hơn một chút

hơn xin chào thế giới.

Như chúng ta đã nói ở chương trước, bất cứ điều gì chúng ta viết trong kho lưu trữ gợn sóng đó đều

nơi chúng ta chỉ sao chép và dán mã giai thừa đó, thay vào đó chúng ta có thể thử điều tương tự ở đây

xin chào thế giới, chỉ là đây sẽ là chương trình đầu tiên chúng tôi viết bằng Django

và kiểm tra môi trường.

Ngoài ra, có một số điều tôi đã bỏ qua khi nói ở chương trước

và tôi sẽ nói về nó bây giờ.

Vì vậy, hãy truy cập Visual Studio Code và xem những gì cần phải làm.

Vì vậy, hãy quay lại Visual Studio Code và bạn có thể thấy chính xác điều này đang chạy

cũng vậy.

Và có một điều mà tôi đã bỏ lỡ để nói đến trước khi kết thúc phần trước.

chương là mỗi khi bạn tạo một máy chủ và chạy nó lần đầu tiên, nó sẽ luôn

tạo một cơ sở dữ liệu SQLite mặc định và cơ sở dữ liệu đó sẽ được gọi là db.sqlite3.

Và đây là nội dung của tệp và SQLite không thực sự được cài đặt theo mặc định, mặc dù

nó tạo ra một tệp db.sqlite có tên là db.sqlite.

Và nếu bạn nhấp vào tin nhắn đó, nếu bạn thấy thông báo tin nhắn đó xuất hiện, nó cho biết

rằng nếu bạn muốn tìm kiếm thứ đó trên thị trường, nó có hai nút và cũng có

thêm một nút nữa và yêu cầu dừng hoặc chặn những thông báo đó.

Vì vậy, tôi vừa nhấp vào nút đầu tiên có nội dung là thị trường tìm kiếm và đây là nội dung

đã nghĩ ra SQLite hoặc bạn có thể chỉ cần nhập SQLite vào thanh tìm kiếm trong

tab tiện ích mở rộng và điều này sẽ xuất hiện.

Vì vậy, chúng tôi nhấp vào đó và nó sẽ nói khám phá và truy vấn cơ sở dữ liệu SQL, cơ sở dữ liệu SQLite.

Hãy cài đặt nó.

Nó sẽ là một tập tin rất nhỏ.

Hầu như không có 208 KB và chỉ thế thôi.

Thế là xong.

Được rồi.

Vậy là nó đã được cài đặt.

Vì vậy, bây giờ chúng ta có thể quay lại Explorer của mình và bạn cũng có thể đóng cửa sổ thị trường.

Vì vậy, bây giờ chúng tôi có cơ sở dữ liệu SQLite cùng với plugin hoặc tiện ích mở rộng mà chúng tôi đã tải xuống

đó là nơi chúng ta có thể khám phá cơ sở dữ liệu này.

Và SQLite được dành cho mục đích phát triển.

Nó cũng có thể được sử dụng trong sản xuất và thường được sử dụng cho các ứng dụng web có dung lượng thấp.

Nó không được sử dụng cho ứng dụng web thực sự có cấu hình cao.

Đó là lý do tại sao nó được gọi là SQLite.

Vì vậy, bạn phải sử dụng thứ gì đó phức tạp hơn để sử dụng nó trong sản xuất, cấp độ cao

môi trường sản xuất.

Và Django cũng có một máy chủ web tích hợp và chỉ dành cho phát triển địa phương

mục đích.

Vì vậy, chúng tôi triển khai bất kỳ ứng dụng nào ở Django.

Chúng tôi chưa tạo ra một cái nào.

Khi bạn triển khai bất kỳ ứng dụng nào lên máy chủ web, Django sẽ sử dụng máy chủ web của máy chủ web để thay thế.

Đó là lý do tại sao chúng tôi có mô-đun wsgi.py trong dự án Django và nó đảm nhiệm việc hooking

lên máy chủ sản xuất.

Vì vậy, đây giống như cái móc hiện đang bám vào các máy chủ sản xuất.

Tệp này, tệp cấu hình wsgi.py.

Và nếu bạn nhìn vào URL ở đây, đó là cổng localhost 8000.

Nếu bạn muốn sử dụng số cổng khác vì bất kỳ lý do gì, thì tất cả những gì bạn phải làm là

hãy quay lại Visual Studio Code và vào bên trong đây và trước khi tôi chỉ cho bạn cách thay đổi

số cổng.

Nếu muốn thoát khỏi máy chủ, bạn có thể đóng cửa sổ như thế.

Ngoài ra, đầu tiên chúng ta phải đóng cửa sổ và sau đó bạn có thể nhấn control C và điều đó sẽ

đóng máy chủ.

Như bạn có thể thấy, máy chủ đã bị đóng.

Nếu bạn CLS và chúng tôi sẽ quay lại đây.

Vì vậy, nếu bạn muốn tạo một máy chủ thay thế, nếu bạn muốn tạo một máy chủ có máy chủ khác

port, thay vì 8000 mà nó tạo theo mặc định cho bạn, tất cả những gì bạn phải làm là nói python

máy chủ chạy quản lý.py.

Và đây là lệnh thông thường để tạo máy chủ phải không?

Và tất cả những gì bạn phải làm là chỉ định số cổng ngay bên cạnh máy chủ chạy sau một khoảng trắng.

Vì vậy, 5000, 6000, bất kể số cổng là gì, tôi không muốn số cổng thay thế.

Tôi sẽ chỉ sử dụng localhost và nhấn enter.

Và nó đã tạo ra điều đó.

Bây giờ nếu bạn di chuột qua đó, nhấn control, giữ phím control và

bấm vào nó.

Nó sẽ mở ra trên trình duyệt mặc định mà bạn đã biết.

Hoàn hảo.

Vì vậy, bây giờ chúng ta hãy tạo ứng dụng.

Vì vậy, bây giờ chúng ta đã hoàn thành tất cả các yêu cầu sơ bộ, bây giờ chúng ta hãy tạo ứng dụng.

Vì vậy, để chúng tôi tạo ứng dụng, bạn có thể tạo cửa sổ bảng điều khiển mới hoặc tải

một thiết bị đầu cuối mới ở đó và hiển thị một bảng điều khiển mới và duy trì hoạt động của máy chủ này hoặc chúng ta có thể đơn giản

bây giờ hãy đóng máy chủ và bạn có thể sử dụng cùng một cửa sổ bảng điều khiển.

Nó không quan trọng.

Vì vậy, chúng tôi sẽ đóng máy chủ và tạo ứng dụng, sau đó chúng tôi sẽ khởi động lại máy chủ vì

nó không quan trọng

Chúng tôi không cần phải duy trì hoạt động đó trong khi sử dụng thiết bị đầu cuối ở đây.

Vì vậy, hãy sử dụng lệnh khởi động ứng dụng tiện ích quản trị để tạo ứng dụng Django mới.

Vì vậy, chúng tôi nói ứng dụng khởi động python management.py và bây giờ đây là lệnh và hãy đặt tên cho nó

và hãy nói xin chào Django.

Được rồi.

Xin chào Django.

Tại sao không?

Xin chào Django và nhấn enter.

Bây giờ điều này làm là nó tạo ra một thư mục tên là hello Django như bạn có thể thấy và nếu

Các bạn mở thư mục đó ra sẽ thấy một số file config tương tự như những gì chúng ta có trong

dự án Django chính.

Tuy nhiên, có một vài bổ sung nữa như bạn có admin.py, bạn có apps.py và bạn

cũng có mô hình kiểm tra và xem.

Vì vậy, nó khá khác với init, ngoài init.py gạch dưới, nó chỉ cho biết

Visual Studio Code rằng đây là tệp Python, hầu như tất cả các tệp cấu hình đều khác nhau

chỉ là chúng giống nhau về cách sắp xếp trong ứng dụng.

Thế thôi.

Mặt khác, tất cả chúng đều là các tệp khác nhau.

Vì vậy, đây là dự án Django chính.

Đây là thành phần mà chúng tôi đã tạo trong phần gạch dưới chính của dự án Django

Django một, được gọi là xin chào Django.

Vì vậy, trong số tất cả các tệp cấu hình này, chúng tôi thường xuyên làm việc với view.py nhé và nó chứa

các chức năng xác định các trang trong ứng dụng web của chúng tôi và chúng tôi cũng làm việc với models.py và

chứa các lớp xác định đối tượng dữ liệu của chúng tôi và sau đó bạn có thư mục di chuyển

cũng chứa thêm một init.py.

Và điều này được các tiện ích quản trị của Django sử dụng để quản lý các phiên bản cơ sở dữ liệu và chúng tôi sẽ

hãy nói về điều đó sau hoặc chúng ta thậm chí có thể không đề cập đến điều đó, tôi chưa chắc về điều đó.

Nhưng chúng ta sẽ chưa nói về vấn đề di cư, ít nhất là trong chương này, chúng ta sẽ không đề cập đến

nói về nó

Chúng tôi sẽ giữ nó thực sự đơn giản.

Chúng tôi sẽ chỉ giữ nó trong bốn hoặc năm tệp cấu hình này để chúng tôi kiểm tra đơn giản

ra khỏi chương trình hello world của chúng tôi.

Và sau đó bạn có apps.py.

Đây chỉ là cấu hình ứng dụng và bạn có thể thấy nó đang nhập thứ gì đó

từ cấu hình ứng dụng.

Nó có một lớp tên là hello Django config và nó nói xin chào Django là tên của

bản thân ứng dụng.

Và sau đó bạn có admin.py.

Ở đây không có gì khác ngoài một câu lệnh nhập và nó được sử dụng để tạo quản trị

giao diện và cuối cùng chúng ta có test.py.

Điều này chỉ được sử dụng để kiểm tra như tên cho thấy.

Bây giờ chúng ta vẫn chưa đi sâu vào vấn đề đó.