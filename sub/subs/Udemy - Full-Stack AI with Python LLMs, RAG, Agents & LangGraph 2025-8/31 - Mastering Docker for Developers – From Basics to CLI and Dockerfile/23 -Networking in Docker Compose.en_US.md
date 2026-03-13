# 23 -Kết nối mạng trong Docker Compose.en US

---

Vậy trong video này chúng ta hãy thử

để hiểu rằng mạng lưới như thế nào

hoạt động trong Docker Compose.

Được rồi?

Mặc dù chúng ta đã nói chuyện rồi

về mạng rất nhiều,

nhưng điều này cũng quan trọng.

Vì vậy, kết nối mạng trong Docker Compose

tài liệu chính thức nhé các bạn.

Vì vậy, theo mặc định ở đây Bộ soạn thảo

thiết lập một mạng duy nhất cho ứng dụng của bạn.

Mỗi container cho một dịch vụ

tham gia mạng mặc định

trong cả hai và đều có thể truy cập được

bởi các container trên mạng đó.

Vì vậy, nếu tôi đi xuống.

Vì vậy, giả sử nếu bạn có thứ gì đó

như thế này, bạn có dịch vụ, bạn

có dịch vụ web, bạn có DB

hình ảnh dịch vụ, postgres và cái này,

đây chính xác là những gì chúng ta đã làm, phải không?

Vì vậy, về cơ bản đây là

cái gì, đây là những dịch vụ.

Vì vậy, dịch vụ dịch vụ.

Vì vậy, khi bạn chạy Docker Compose,

những điều sau đây xảy ra.

Một mạng gọi là ứng dụng của tôi

mặc định được tạo.

Được rồi?

Có một ứng dụng mạng,

có một mạng lưới được tạo ra.

Một vùng chứa được tạo

sử dụng cấu hình web.

Vậy là đã có một chiếc container được làm

cho trang web này phải không?

Và nó tham gia vào mạng mặc định của tôi.

Vì vậy tôi sẽ chỉ cho bạn nếu tôi làm vậy bác sĩ

Mạng Docker ls

vậy là không có gì phải không?

Bạn hoàn toàn có thể thấy điều đó.

Chỉ một giây thôi.

Thiết bị đầu cuối của tôi ở đâu?

Vâng, bạn có thể thấy điều đó

không có gì cả

Giả sử Docker Soạn Soạn

lên dấu gạch ngang T chạy Docker

mạng ls bạn có thể thấy Thương mại điện tử không

gạch dưới mạng mặc định

ở đó có một cây cầu.

Nó giống như việc tạo ra.

Nó lấy tên này

và tạo ra một mạng lưới cho tôi.

Và.

Và tất cả các thùng chứa trong này

mạng đang tham gia mạng này.

Và một khi bạn đã xác định được người dùng

mạng lưới cầu và container

có ở đó không, các bạn biết đấy, cái gì

xảy ra, bạn biết điều gì xảy ra

trong vùng chứa cầu do người dùng xác định?

Tất cả các thùng chứa ở đây, chúng

có thể nói chuyện với nhau bằng

tên và tất cả những thứ đó, phải không?

Đang quay lại.

Được rồi, một container là

đã tạo cấu hình DB.

Nó cũng tham gia cùng một mạng.

Mỗi container có thể nhìn

lên tên dịch vụ web hoặc DB

và lấy lại thích hợp

địa chỉ IP của vùng chứa.

Ví dụ: ứng dụng web

có thể kết nối các postgres URL.

Hãy xem chúng ta phải làm gì nếu trang web này

cần kết nối với postgres này,

Tôi chỉ có thể làm Postgres DB4,5432.

Tại sao?

Bởi vì đây là

tên vùng chứa DB.

Vì vậy, nhờ DB, tôi thực sự có thể

kết nối với điều đó.

Tại sao?

Bởi vì cả hai đều là

trong cùng một mạng.

Và khi hai thùng chứa giống nhau

mạng cầu do người dùng xác định,

Người nhện có thể gọi Ironman bằng tên.

Đây là những gì họ đang cố gắng làm.

Tôi không cần lấy địa chỉ IP

đối với db này tôi chỉ có thể nói,

này, chỉ cần kết nối với db là được

tự động tra cứu đó.

Được rồi.

DB tương ứng với điều này

dịch vụ đang chạy trên một số IP

địa chỉ mà chúng tôi không cần biết.

Được rồi, về cơ bản thì đây là cách

Mạng soạn thảo Docker hoạt động.

Vì vậy, về cơ bản nó là nội bộ,

xử lý tự động.

Bạn thậm chí có thể tạo liên kết, phải không?

DB đó được kết nối thông qua cơ sở dữ liệu.

Vì vậy, bạn thậm chí có thể tạo liên kết

mạng đa máy chủ.

Bạn thậm chí có thể chỉ định

mạng riêng của bạn.

Bạn có thể tạo mạng lưới của riêng bạn.

Vậy làm thế nào để làm điều đó?

Bạn có thể nói thấy quan trọng.

Được rồi, bạn có thể nói ở đây,

mạng lưới.

Vì vậy, về cơ bản nó giống như bạn có

dịch vụ, bạn có mạng.

Hãy tạo ra một mạng lưới.

Vì vậy tôi có thể tạo ra một mạng lưới

ví dụ như giao diện người dùng.

Được rồi, giả sử giao diện người dùng là

một mạng và bạn có thể nói

này, sử dụng trình điều khiển nào?

Tôi muốn sử dụng mạng cầu.

Bây giờ tôi có thể nói này Postgres,

bạn có thể vui lòng tham gia mạng lưới này không.

Vì vậy, mạng.

Này, hãy tham gia mạng lưới này.

Và ở đây tôi cũng có thể nói mạng.

Và này, bạn cũng có

để tham gia mạng lưới này.

Và tương tự tôi có thể tạo một cái

nhiều mạng hơn, giả sử là phụ trợ.

Vậy nó là một, nó lại là một mạng lưới.

Và bạn có thứ này và tôi có thể nói

này, bạn cũng là một phần của phụ trợ.

Hãy có thêm một dịch vụ nữa

đó cũng là một phần của phụ trợ.

Vậy bạn biết chuyện gì đang xảy ra rồi phải không?

Container nào có thể giao tiếp

với thùng chứa nào có tên,

trong cùng một mạng.

Chính xác.

Vì vậy, đây là cách bạn thậm chí có thể

tạo mạng lưới của riêng bạn.

Được rồi, vậy bạn có thể đi qua

tài liệu này.

Rất quan trọng.

Nhưng thông thường chúng ta không chạm vào điều này

kết nối mạng vì đó là Docker

soạn tập tin và tất cả các vùng chứa

theo mặc định là trong cùng một mạng,

giúp chúng tôi hoàn thành công việc.

Điều đó khá tuyệt vời.

Đó là những gì chúng tôi chỉ muốn.

Vì vậy, về cơ bản đây là mạng

trong Docker Compose.

Trong video tiếp theo tôi sẽ chỉ

bạn biết cách bạn có thể tăng âm lượng

gắn kết trong Docker Composer.