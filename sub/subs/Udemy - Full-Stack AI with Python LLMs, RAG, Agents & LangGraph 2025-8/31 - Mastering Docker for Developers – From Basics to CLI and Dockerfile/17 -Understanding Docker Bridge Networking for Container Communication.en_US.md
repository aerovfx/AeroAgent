# 17 -Tìm hiểu về mạng cầu nối Docker cho truyền thông container.en US

---

Này các bạn, tôi thực sự muốn

để chúc mừng bạn

để làm cho đến đây.

Bây giờ đây là phần hoàn toàn mới của chúng tôi

trong đó chúng ta sẽ nói chuyện

về mạng Docker.

Chúng tôi sẽ hiểu điều đó.

Mạng Docker là gì?

Cách hoạt động của mạng trong Docker.

Và nó thực sự rất ấn tượng

hiểu mạng trong Docker.

Vì vậy, cùng với đó, hãy xem làm thế nào

nhiều chế độ mạng có sẵn

trong Docker và phổ biến nhất

và phổ biến được sử dụng đó là

mạng chế độ cầu.

Vì vậy, những gì bạn có

việc cần làm là bạn phải nhảy

vào tài liệu.

Vì vậy, kết nối mạng Docker và điều này

là tổng quan về mạng.

Vì vậy bạn có thể thấy đó là gì

về cơ bản là mạng.

Chúng ta hãy làm một điều thôi.

Hãy để tôi chạy Docker của tôi

quỷ, hãy chạy công cụ Docker của tôi.

Đúng vậy, công cụ Docker của tôi là

lên và chạy.

Và hãy để tôi mở

thiết bị đầu cuối cho bạn.

Phải.

Vậy thiết bị đầu cuối của tôi ở đâu?

Chuẩn rồi.

Vì vậy, ở đây tôi đã có thiết bị đầu cuối.

Vì vậy đây là điều tôi muốn cho bạn thấy

là nếu tôi phóng to lên một chút.

Vì vậy nếu tôi chỉ nói Docker

chạy tương tác phải không?

Bây giờ bạn đã biết những lệnh này rồi phải không?

Bạn được sử dụng rất nhiều

tới các lệnh này.

Và tôi cố gắng chạy một cái gì đó

được gọi là hộp bận rộn, phải không?

Vì vậy, tất nhiên nó sẽ kéo hình ảnh.

Không sao đâu.

Vì vậy tôi sẽ chỉ đợi

hình ảnh cần được kéo.

Và đó là một hình ảnh rất thấp,

Ý tôi là hình ảnh rất nhỏ.

Vì vậy, bạn có thể thấy nếu tôi nói ping

google.com chờ đã, bạn có thấy điều đó không?

Có, nó có thể ping google.com

và không chỉ vậy, nếu tôi cố gắng

để ping trang web của tôi, nghĩa là

piyushkar.dev thực ra là vậy

có thể ping trang web của tôi là tốt.

Vậy tôi có thể nói điều đó một cách hiệu quả không

thùng chứa này, bất cứ thứ gì

thùng chứa này, thùng chứa này

có quyền truy cập vào Internet.

Thùng chứa đặc biệt này có thể nói chuyện

với Internet thế giới bên ngoài.

Nhưng làm sao điều đó có thể được?

Nó chỉ là một cỗ máy bị cô lập

Internet của ai cái máy này

đang sử dụng, có địa chỉ IP

máy này đang dùng

địa chỉ Mac mà nó đang sử dụng.

Có phải của tôi không, có phải máy của tôi không

đang cho anh ta Internet à?

Hay nó là một thứ riêng biệt, bạn biết đấy,

môi trường biệt lập có nó

địa chỉ Mac và địa chỉ IP của riêng bạn?

Vậy chính xác thì chuyện gì đang xảy ra?

Đó là điều tôi muốn dạy cho bạn.

Vì vậy, mạng container.

Mạng đề cập đến khả năng

để các container kết nối

và liên lạc với nhau

trên hoặc vào khối lượng công việc không docker.

Được rồi, vậy container có

mạng được bật theo mặc định.

Đây là những gì tôi muốn cho bạn thấy.

Các vùng chứa đã được kích hoạt mạng

theo mặc định và họ có thể

thực hiện các kết nối đi.

Đây là những gì chúng ta vừa thấy phải không?

Theo mặc định.

Tôi chưa đưa gì cả

hướng dẫn đặc biệt.

Đó chỉ là một lần chạy Docker

lệnh và tôi đã có thể

để ping thế giới bên ngoài.

Một container không có thông tin

về loại ip nào, loại gì

của mạng mà nó đã gắn vào.

Thùng chứa rất quan trọng không có

manh mối hoặc liệu đồng nghiệp của họ có

khối lượng công việc của Docker hay không.

Được rồi.

Một container chỉ nhìn thấy một mạng

giao diện với cổng IP

và bảng định tuyến dịch vụ DNS.

Một điều khác.

Vậy chúng ta hãy đi xuống.

Được rồi, hãy đi xuống đây và tôi chỉ

trước hết muốn chỉ cho bạn cách

nhiều chế độ mạng có sẵn.

Thế cái đó ở đâu vậy các bác?

Vâng, trình điều khiển mạng.

Được rồi, nếu bạn thấy trình điều khiển mạng,

Hệ thống con mạng Dockers

có thể cắm được bằng cách sử dụng trình điều khiển.

Vì vậy, hãy để tôi chỉ cho bạn các loại.

Vì vậy, bất cứ khi nào tôi nói mạng Docker,

driver, driver về cơ bản có nghĩa là loại.

Đầu tiên là cây cầu,

trình điều khiển mạng mặc định.

Vì vậy, để xem cái này tôi sẽ chỉ làm

một điều khiển D và chỉ cần nói Docker

mạng hoặc mạng Docker.

Và bạn có thể thấy rằng bạn có

một lệnh đó là mạng Docker.

Vì vậy, đây là một sự giúp đỡ.

Được rồi, đây là một sự trợ giúp

chúng tôi sẽ đề cập đến.

Vì vậy tôi chỉ có thể nói LS để liệt kê

tất cả các mạng phải không?

Vì thế tôi chỉ có thể nói

Mạng Docker và ls.

Vì vậy, đây là tất cả các lệnh

và đây là tất cả các mạng.

Và trong trường hợp của tôi thực sự

bạn có thể thấy tôi có rất nhiều

của các mạng bổ sung là tốt.

Khi bạn định sử dụng

lệnh này bạn sẽ chỉ

xem máy chủ cầu và không có.

Tất cả những cái tiếp theo, tất cả những cái nhỏ này

loại hình khối và giáo viên mặc định.

Đây thực sự là của tôi

tùy chỉnh riêng, mạng.

Vì vậy bạn có thể bỏ qua chúng.

Đây là, tôi đã, bạn biết đấy, đang làm

một cái gì đó với kubernetes.

Vì vậy, đây là tất cả những thứ đó, mạng.

Nhưng vâng, bạn có thể bỏ qua điều đó.

Thì ra đây là tên của

mạng và đây là trình điều khiển.

Vậy driver nào hay cái nào

loại họ đang sử dụng.

Vì vậy, theo mặc định nó là loại cầu.

Nếu bạn không chỉ định trình điều khiển,

đây là loại

của mạng bạn đang tạo.

Được rồi, điều đó có nghĩa là điều gì sẽ xảy ra

là khi tôi nói Docker hãy chạy, được thôi,

hãy để tôi làm một Docker container.

Ls PS Vậy đây là

tất cả các thùng chứa.

Tôi chỉ muốn loại bỏ

tất cả các thùng chứa.

Vâng, rất nhiều

container đang chạy.

Vì thế.

Vì vậy hãy loại bỏ

tất cả các thùng chứa.

Được rồi, vậy hãy để tôi lên đây

và quay lại và bạn có thể thấy rất nhiều

số container đang chạy.

Chỉ cần xóa mọi container

và chúng ta cũng hãy loại bỏ tất cả

những hình ảnh bởi vì, bạn biết đấy.

Ừ, vậy hãy bắt đầu lại nào.

Vì vậy không có container nào đang chạy

bây giờ điều tôi sẽ làm là

Tôi sẽ chỉ chạy một container.

Được rồi.

Và lưu ý rằng tôi đang tạo

ở chế độ tách rời.

Tôi muốn đặt cho nó một cái tên, được chứ?

Và tên có thể giống như thùng chứa của tôi.

Được rồi, thùng chứa của tôi.

Và tôi đang tặng cờ RM.

Bạn hiểu rằng những gì

đây là những lá cờ RM và tất cả.

Thế là vào, để nó kéo cái hộp bận.

Vì vậy, về cơ bản là chế độ tách rời

và loại bỏ sau khi sử dụng.

Và đây là tên phải không?

Và vâng, bạn có thể thấy

một container đang chạy.

Vì vậy, chỉ để xác minh, tôi có thể

chỉ cần nói docker container.

tái bút

một container đang chạy.

Đẹp.

Bây giờ hãy để tôi nói về mạng Docker.

Được rồi?

Bạn biết đấy, Docker, mạng ls.

Ý tôi là, bạn biết điều đó

Tôi có cây cầu này.

Hãy để chúng tôi làm một tài liệu

mạng, Mạng.

Và chúng ta hãy thực hiện một cuộc kiểm tra

trên cây cầu này.

Vì vậy bạn có thể thấy rằng cái tên

trong số này có Bridge ID ở đó.

Được tạo ra như địa phương của họ ở đó.

Và bạn có một số địa chỉ IP

cấu hình ở đó.

Và nếu bạn đi xuống, bạn có thể thấy điều đó không?

có một phần container

trong đó nó cho thấy rằng điều này

container cụ thể được kết nối.

Container mà tôi vừa chạy này là

được kết nối với mạng cầu.

Và đây là địa chỉ IP

của thùng chứa đó.

Vì vậy ngay bây giờ những gì chúng tôi đã làm là

chỉ cần tưởng tượng nó hoạt động như thế nào.

Bạn có một máy chủ.

Đây là cái này

máy chủ của bạn.

Vì vậy, hãy để tôi có một máy tính ở đây.

Vì vậy hãy nói rằng đây là những gì

đây là máy chủ của tôi

Được rồi?

Vì vậy, chủ nhà.

Máy chủ này có,

trình điều khiển mặc định của riêng nó.

Máy tính xách tay của tôi đang có một số loại

của người lái xe đó là

được kết nối với bộ định tuyến.

Được rồi, để tôi đưa bộ định tuyến tới đây.

Vậy đây là bộ định tuyến WI fi của tôi, được chứ?

Vậy máy này được kết nối với cái này

Bộ định tuyến WI fi, rất tốt.

Bây giờ, trên máy chủ của tôi, tôi

Docker đã được cài đặt phải không?

Vì vậy, hãy có Docker ở đây.

Không phải cái này.

Hãy có Docker ở đây.

Vì vậy điều đặc biệt này

máy đã cài đặt.

Docker đã được cài đặt.

Và những gì Docker làm là nó tạo ra

mạng lưới hoàn toàn mới của chúng tôi

giao diện được gọi là Bridge,

cái mặc định phải không?

Điều đó chúng ta vừa thấy.

Rằng chúng ta vừa nhìn thấy cái này.

Và bất cứ khi nào tôi nghĩ ra một cái mới

thùng chứa, hãy nói rằng

đây là thùng chứa, được chứ?

Vì vậy, đây là viết tắt của một container.

Bất cứ khi nào tôi quay một thùng chứa mới,

những gì nó làm, về cơ bản nó

kết nối điều đặc biệt này

tới mạng lưới cầu đặc biệt này.

Điều đó có nghĩa là điều này có phụ riêng của nó.

Nó có địa chỉ IP riêng.

Hiểu rồi.

Vì vậy, bạn có thể thấy rằng điều đặc biệt này

Mạng Docker đặc biệt như thế này

Docker container được kết nối với

Cây cầu này do ai làm?

Docker này, khi chúng tôi cài đặt nó.

Và đây là cách nó có thể

để truy cập Internet.

Vì vậy, khi chúng tôi nói thích ping google.com

nó được kết nối với cây cầu này

mạng và cây cầu này Mạng là

về cơ bản đưa ra cấu hình

hoặc khả năng nói chuyện với Internet.

Vì vậy, ngay bây giờ bạn có thể thấy rằng tôi

có, tôi có container ở đó.

Vì vậy, nó là thùng chứa của tôi.

Vì vậy việc hình dung là rất

quan trọng ở đây, vậy cái tên

thùng chứa này là thùng chứa của tôi.

Và địa chỉ IP là gì?

Nó có địa chỉ IP này.

Tôi chỉ định sao chép nó

và tôi sẽ dán nó vào.

Vậy đây là địa chỉ IP phải không?

Hãy để tôi xem điều đó.

Địa chỉ IP của tôi là gì?

Vì vậy, hãy để tôi xem địa chỉ IP của tôi.

Địa chỉ IP máy chủ của tôi, phải không?

Vì vậy, nếu tôi chỉ nhìn thấy

địa chỉ IP của máy chủ.

Vì vậy, địa chỉ IP của tôi thực sự là thế này.

Vì vậy, đây là địa phương của tôi.

Được rồi, đây là địa chỉ IP cục bộ của tôi.

Đây là những gì được thực hiện bởi docker.

Vì vậy, bạn thậm chí có thể nhìn thấy

các giao diện mạng.

Phải?

Bây giờ chúng ta hãy làm một việc thôi.

Hãy tạo thêm một container nữa.

Được rồi, tôi đi đây

để tạo thêm một vùng chứa nữa.

Vì vậy Docker, hãy chạy.

Được rồi, dấu gạch nối, dấu gạch nối,

dấu gạch nối, dấu gạch nối rm, dấu gạch nối, Tên,

tương đương với thùng chứa.

Gạch dưới hai.

Vì vậy, bạn có thể có bất kỳ tên ngẫu nhiên

và một lần nữa, hộp bận rộn.

Được rồi, đây có thể là bất kỳ

hình ảnh, nhưng vâng, hộp bận rộn.

Bây giờ nếu tôi nói docker, network.

Được rồi, Docker, Mạng.

Cầu.

Thanh tra.

Xin lỗi, kiểm tra.

Cầu.

Được rồi, bridge, nếu tôi có thể gõ

đúng rồi, cầu.

Vì vậy bây giờ điều bạn sẽ nhận thấy là

rằng có hai mạng.

Có hai thùng chứa.

Thùng chứa của tôi, cái cũ hơn, phải không?

Đây là địa chỉ IP.

Bây giờ bạn có thêm một container nữa.

Và điều này cũng được kết nối

đến cùng một cây cầu và nó đã có

địa chỉ IP 1-721.7.3.

Vậy điều đó có nghĩa là cả hai đều

đang ở trên cùng một mạng.

Nhưng bạn có thể thấy IP

địa chỉ đang được phân bổ.

Vậy là nó cũng đã kích hoạt DHCP rồi

là giao thức điều khiển máy chủ động.

Nó tự động

phân bổ địa chỉ IP.

Đúng, đúng.

Bây giờ bởi vì cả hai thùng chứa này đều

trên cùng một mạng,

họ có thể nói chuyện với nhau không?

Vâng, họ có thể.

Làm sao?

Hãy để tôi chỉ cho bạn.

Những gì tôi sẽ làm là

Tôi có hai thùng chứa.

Vì vậy, docker.

tái bút

bạn có thể thấy tôi có hai thùng chứa.

Chúng ta hãy đi sâu vào vấn đề này.

Vậy đây là tên container thứ hai.

Hãy để tôi nói container thứ hai.

Được rồi, tôi sẽ nói, tôi sẽ thử ping

thùng một từ thùng hai.

Vì vậy, tôi sẽ nói hãy xem Docker, thực thi.

Đây là một lệnh mới cho bạn.

Được rồi, chỉ cần nhìn vào người điều hành này

vùng chứa nào bạn muốn thực thi.

Tôi muốn thực hiện điều đó trong container

với những gì tôi muốn nói bash.

Không phải bash.

Tôi muốn nói, này, ping

thùng chứa của tôi.

Hãy nói theo tên.

Hãy nói không.

Được rồi, điều đó là không thể.

Nhưng giả sử nếu tôi cung cấp IP

địa chỉ, tôi biết IP là gì

địa chỉ container của tôi và tôi làm

một lần nhập, nó có thể ping.

Bạn có thể thấy nó có khả năng ping.

Và điều gì sẽ xảy ra nếu tôi, bạn biết đấy,

có thể viết sai địa chỉ IP

sáu, không tồn tại.

Bạn có thể thấy nó là

không ping được nó.

Nó bị kẹt rồi phải không?

Nhưng nếu tôi cung cấp đúng địa chỉ IP

ở cuối là 0,2,

bạn có thể thấy nó có khả năng ping.

Vì vậy, bên trong container thứ hai, tôi có thể

để ping container một, phải không?

Bởi vì cả hai đều là

trên cùng một mạng.

Đó là mạng cầu nối mặc định.

Vâng, điều đó khá tuyệt phải không?

Tương tự, bạn thậm chí có thể có

nhiều container và họ có thể

giao tiếp với nhau.

Vì vậy đây là cây cầu mặc định

mạng được kích hoạt.

Được rồi?

Bây giờ tôi có thể nói rằng họ

cả hai đều ở trong cùng một mạng?

Tất nhiên rồi.

Chúng ta vừa thấy, chúng ta

thậm chí đã xác minh nó.

Chúng tôi đã xác minh nó bằng cách nào?

Bởi vì tôi đã có thể

để ping chúng và bạn có thể thấy

dải địa chỉ IP.

Bây giờ những gì bạn có thể làm là trong Docker.

Tại sao?

Điều này là cần thiết, phải không?

Sự cần thiết của điều này là gì?

Điều này về cơ bản đảm bảo rằng,

giả sử bạn đang làm việc

một kiến trúc microservice phải không?

Vậy là bạn có một vùng chứa Docker.

Hãy để tôi, bạn biết đấy, sao chép nó.

Ở đây bạn có một Docker

container đang chạy

ứng dụng nút của bạn.

Hãy nói rằng đây là

ứng dụng JS nút của bạn.

Ứng dụng JS nút này

đang chạy trên một số cổng

và để lộ một số cổng.

Rồi bên trong, bên trong

bạn có thể có redis, được chứ?

Và redis này có thể

xoay quanh một số, một số.

Bạn gọi là gì,

hãy nói là ba, phải không?

Và nút JS này về cơ bản có thể

nói chuyện với redis này bởi vì

nó nằm trong cùng một mạng.

Tương tự, bạn có thể có

một dịch vụ, giả sử là

postgres, một dịch vụ cơ sở dữ liệu

chạy trên một số cổng khác.

Giả sử 0,4.

Và bạn thậm chí có thể có postgres này.

Bạn thậm chí có thể giao tiếp

với postgres này.

Tại sao?

Bởi vì máy chủ JS nút này,

bởi vì máy JS nút này là

trong cùng một mạng.

Vì vậy đây là lợi thế

của cùng một mạng, máy đó

trong cùng một mạng có thể nói chuyện

riêng tư với nhau phải không?

Không cần phải có công khai

Địa chỉ IP của các máy này.

Không cần phải vạch trần.

Vậy cái máy này, nút JS này

máy có thể bị lộ

với Internet công cộng, phải không?

Để mọi người có thể ghé thăm

máy chủ JS nút của bạn.

Nhưng các dịch vụ nội bộ như Redis

hoặc Postgres, điều này có thể được giấu kín

từ thế giới bên ngoài.

Vì để lộ cơ sở dữ liệu ra bên ngoài

có thể có lỗ hổng bảo mật.

Vậy đây là chế độ bridge của bạn.

Được rồi, Cầu.

Và bạn giao tiếp như thế nào?

Trong cây cầu mặc định, bạn có

để giao tiếp bằng địa chỉ IP.

Hiểu rồi.

Bây giờ đây là chế độ cầu nối mặc định.

Hãy hiểu điều này tốt hơn.

Vì vậy, cầu nối, mạng lưới thường được

được sử dụng khi ứng dụng của bạn

chạy một container cần

để giao tiếp với các container khác

trên cùng một máy chủ.

Đây là những gì tôi vừa nói với bạn.

Phải?

Vì vậy, xét về mặt kết nối mạng, một cây cầu

mạng là một thiết bị lớp liên kết

cái đó chuyển tiếp giao thông

giữa các phân đoạn mạng.

Vì vậy, xét về Docker, một cây cầu

mạng sử dụng cầu nối phần mềm

cho phép các container kết nối với

cùng một mạng lưới cầu

giao tiếp trong khi cung cấp

cách ly khỏi container

hiện đang được kết nối với

mạng lưới cầu đó.

Vì vậy, nếu có.

Được rồi, tôi sẽ nói với bạn điều đó

trong video tiếp theo.

Thật ra video tiếp theo là

chỉ trên cái này thôi.

Vì vậy, bạn có thể có hai loại

của mạng cầu.

Được rồi.

Một là mạng cầu mặc định.

Một là người dùng xác định

mạng lưới cầu.

Khi bạn khởi động một docker,

một cây cầu mặc định, còn được gọi là

cầu, được tạo tự động.

Một container mới bắt đầu kết nối với

nó trừ khi bạn chỉ định một số khác.

Bạn cũng có thể tạo người dùng

cầu tùy chỉnh được xác định.

Cầu tùy chỉnh do người dùng xác định

vượt trội hơn so với mặc định.

Bây giờ điều cao cấp này là gì

trong cây cầu do người dùng xác định

cung cấp DNS tự động

độ phân giải giữa các mạng.

Đây là một cái gì đó rất

quan trọng là tôi sẽ đi

để kể cho bạn nghe ở video tiếp theo.

Được rồi?

Độ phân giải DNS tự động này, được rồi,

đây là thứ không có ở đó

trong cầu mặc định, phải không?

Và những cây cầu do người dùng xác định

mang lại sự cách ly tốt hơn.

Tất nhiên, container có thể

gắn vào và tách ra một cách nhanh chóng

và mỗi mạng do người dùng xác định

tạo ra một cây cầu có thể cấu hình được.

Vì vậy, không có gì phải lo lắng.

Trong video tiếp theo tôi sẽ

để cho bạn biết cây cầu do người dùng xác định.

Nhưng trong video đặc biệt này

Tôi muốn cho bạn thấy điều đó

bạn có mạng docker.

Vì vậy, mạng docker

và bạn chỉ có thể thực hiện ls.

Bạn có thể thấy các mạng, bạn

có thể kiểm tra trên mạng.

Vì vậy bạn có thể thấy cái đó

container docker được kết nối

tới một mạng cụ thể.

Và đó là cách của bạn

docker có quyền truy cập

với thế giới Internet bên ngoài.

Hiểu rồi.

Vậy video này nói về

mạng chế độ cầu.

Trong video tiếp theo, chúng ta hãy nói về

mạng cầu do người dùng xác định.