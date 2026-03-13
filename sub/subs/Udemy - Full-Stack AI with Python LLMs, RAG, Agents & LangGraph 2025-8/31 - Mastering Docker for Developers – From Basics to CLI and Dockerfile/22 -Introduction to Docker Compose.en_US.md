# 22 -Giới thiệu về Docker Compose.en US

---

Này các bạn, chào mừng trở lại.

Chào mừng đến với một điều thú vị khác

phần của Docker Compose.

Trong phần cụ thể này chúng tôi

sẽ hiểu Docker là gì

Compose, Docker cần gì

Compose, Docker Compose có thể làm được như thế nào

giúp bạn thiết lập

môi trường đang phát triển

môi trường, tôi phải nói.

Vì vậy Docker Compose rất mạnh mẽ

công cụ được cung cấp bởi chính thức

Docker, chỉ bằng một cú nhấp chuột, bạn

có thể thiết lập toàn bộ cơ sở hạ tầng của bạn

và chỉ bằng một cú nhấp chuột bạn có thể đặt nó

xuống.

Vì vậy, trong video cụ thể này, chúng ta hãy

cố gắng hiểu Docker Compose.

Vì vậy, ở đây tôi có một dự án.

Được rồi, để tôi đi bộ

bạn thông qua dự án này.

Đây chính là dự án mà

chúng tôi đã có, cái Typescript đó.

Vì vậy, những gì tôi đã làm trên đầu

trong số đó là tôi đã cài đặt Redis

và tôi đã cài đặt postgres.

Vậy bây giờ chuyện gì đang xảy ra

ứng dụng của chúng tôi phụ thuộc vào

trên Redis và postgres.

Vì vậy, ở đây tôi đã thực hiện một vài thay đổi.

Bạn có thể thấy rằng đây là chính xác

cùng một ứng dụng mà chúng tôi đã có ví dụ

trước đó chúng tôi đã ở đâu, bạn biết đấy,

tìm hiểu về các tệp Docker này.

Những thay đổi tôi đã thực hiện là,

số một, tôi đã thêm

một kết nối Redis và tôi có

đã thêm một kết nối postgres.

Vì vậy, ứng dụng này, trước đây

bắt đầu, cố gắng thực hiện

một kết nối với Redis.

Vì vậy, bạn có thể thấy rằng đây là Redis

chặn và cố gắng tạo

một kết nối với postgres.

Hiện tại tôi không có Redis,

Tôi không có postgres.

Vì vậy nếu tôi cố gắng xây dựng

ứng dụng này, vì vậy

xây dựng sẽ thành công.

Xây dựng thì ổn, nhưng nếu tôi cố gắng

để bắt đầu NPM, bạn sẽ

để thấy rằng tôi nhận được lỗi.

Vì vậy, lỗi này xảy ra vì

Tôi không thể kết nối với Redis.

Vậy bạn có thể thấy điều đó

kết nối đã bị đóng.

Vì vậy điều đặc biệt này

ứng dụng không chạy.

Vậy làm thế nào tôi có thể có được điều đặc biệt này

ứng dụng được thiết lập và chạy?

Cách đầu tiên là tôi cần

để cài đặt Redis trên máy của tôi.

Tôi cần cài đặt postgres

trên máy của tôi.

Và nếu tôi có những nhà phát triển đồng nghiệp,

giả sử nếu tôi có một đội gồm 10 người

các nhà phát triển, tôi phải hỏi mọi người

để cài đặt cùng một phiên bản của Redis

và postgres rằng tôi sẽ

cài đặt ngày hôm nay.

Hãy nói hôm nay, nếu ngay cả tôi cài đặt

Redis và postgres trên máy của tôi.

Thứ nhất, nó chiếm rất nhiều

dung lượng trên máy của tôi, phải không?

Tôi thực sự không muốn

để cài đặt các dịch vụ riêng biệt.

Thứ 2 hôm nay mình cài đặt nhé

nói PostgreSQL phiên bản 14.

Ngày mai, sau một năm, nếu

một nhà phát triển tham gia và Postgres 16 là

đang diễn ra, tôi phải đặc biệt

nói với anh ấy rằng, này, bạn có

chỉ cài đặt Postgres phiên bản 14.

Một lần nữa, môi trường dev

vấn đề nảy sinh.

Vậy làm thế nào chúng ta có thể giải quyết nó?

Chúng ta có thể sử dụng thứ gì đó

được gọi là Docker Compose.

Vì vậy, tôi có thể tạo tệp soạn thảo Docker

trong đó tôi có thể chỉ định rằng

để chạy ứng dụng cụ thể này

Tôi cần những gì tôi cần postgres,

Tôi cần redis, thế là xong.

Chỉ với một cú nhấp chuột tôi có thể nhận được

cơ sở hạ tầng của tôi đang hoạt động.

Vì vậy, để tạo một tệp soạn thảo Docker

trên thư mục gốc, bạn có

để tạo Docker soạn tệp YML.

Vậy đây là tên chính xác

Docker Soạn yml.

Và bạn có thể thấy rằng đây là

tự động xuất hiện một logo.

Vì vậy, điều bạn phải làm trước tiên là

trên hết, hãy đặt cho nó một cái tên.

Vì vậy, giả sử tôi đang xây dựng

Trang web thương mại điện tử.

Vì vậy, bạn chỉ có thể nói Thương mại điện tử.

Bất kỳ cái tên thân thiện nào, phải không?

Thương mại điện tử.

Về cơ bản thì điều này là của bạn

mạng cũng sẽ hoạt động trên đó.

Vì vậy, vâng, dịch vụ.

Bây giờ bạn phải chỉ định các dịch vụ,

tất cả các dịch vụ

bạn cần về điều này đặc biệt

Thành phần Docker, phải không?

Vì vậy, các bạn, tôi cần gì?

Tôi cần bưu phẩm.

Vì thế tôi chỉ có thể đặt tên cho nó.

Giống như tôi có thể đặt tên cho bất cứ điều gì.

Ví dụ, tôi có thể

chỉ cần đặt tên nó là db.

Tôi có thể đặt tên nó là postgres.

Vì vậy, tên vùng chứa.

Được rồi, bạn có thể có container.

Vì vậy nếu bạn biết tất cả

các lệnh Docker.

Vì vậy trước hết hãy nói

hình ảnh nào tôi muốn sử dụng.

Vì thế tôi có thể nói, này, tôi muốn

để sử dụng hình ảnh Postgres ở 16.

Vì vậy tôi chỉ có thể nói postgres.

Vì vậy về cơ bản nó tương đương

để nói nếu tôi thêm nhận xét ở đây,

Tôi chỉ có thể nói như bạn nói docker,

giả sử chạy tương tác.

Và bạn chỉ cần nói postgres.

Vậy điều tôi đang nói là, này,

chạy hình ảnh cụ thể này.

Được rồi.

Và hãy nói rằng tôi cũng muốn

đặt tên cho vùng chứa này

như bạn biết đấy, postgres.

Vì vậy, bạn có thể đặt cho nó một cái tên.

Vì vậy, đặt tên là postgres.

Mát mẻ.

Vậy bạn còn muốn tặng gì nữa?

Tên vùng chứa.

Thực ra không có tên

tên gạch dưới của vùng chứa.

Được rồi, được rồi.

Vậy hãy nói xem nào

bạn có muốn tặng không?

Bạn muốn cho nó

một biến môi trường.

Vì vậy, nếu bạn đi vào tài liệu,

Tôi không nói điều này, cứ đi đi

vào tài liệu, bạn sẽ nhận được nó.

Được rồi, vậy thì sao?

Tất cả môi trường

các biến có thể xảy ra.

Vì vậy, bạn có thể thấy rằng bạn có thể

đưa ra các biến môi trường

chẳng hạn như mật khẩu postgres.

Vì vậy, chúng ta có thể chỉ định một cái gì đó

như thế này phải không?

Dấu gạch nối E postgres

mật khẩu bằng 1234.

Ở đây có thể nói là môi trường phải không?

Môi trường.

Và tôi có thể nói mật khẩu postgres.

BẰNG.

Hãy chỉ định mật khẩu

chỉ như postgres.

Được rồi, vậy còn có gì nữa?

Tất cả đều đến từ

tài liệu, phải không?

Tất cả đều đến từ tài liệu.

Vì vậy bạn có thể thấy rằng tôi có thể

có mật khẩu postgres,

người dùng postgres đang ở đó.

Thế nên tôi chỉ có thể nói, này, tôi muốn

một người dùng postgres và tôi muốn

một postgres giả sử db.

Tên của cơ sở dữ liệu

cũng là postgres.

Vì vậy về cơ bản nó tương đương

để nói dấu gạch nối e postgres

mật khẩu, dấu gạch nối và postgres

người dùng, gạch nối và postgres db.

Và tôi cũng cần phải làm một số việc

cổng bị lộ, phải không?

Vì vậy, nó chạy trên một cổng cụ thể.

Vì vậy, nó theo mặc định chạy

nó chạy trên cổng nào.

Ý tôi là, được rồi, đây là một bước ngoặt.

Điều đặc biệt này.

Postgres, hãy tìm kiếm

cho cổng mặc định của postgres.

Được rồi, vậy Postgres chạy trên 5432.

Điều đó có nghĩa là tôi có thể nói rằng

để lập bản đồ cổng, phải không?

Tôi có thể nói các cổng và tôi có thể nói về,

máy chủ của tôi được gắn

đến thùng chứa, chiếc máy này.

Vì vậy, về cơ bản đây là

máy chủ và vùng chứa.

Vậy tôi có thể nói là năm, nghìn 431.

Vì vậy, về cơ bản điều này có nghĩa là đối với tôi,

trên máy chủ của tôi 5431

container, 5432 có thể được kết nối.

Vì thế điều tôi đang làm một cách nhàn rỗi là tôi

về cơ bản chỉ định một cấu hình

để chạy một thùng chứa postgres có

tên là cái này bên trong cái này và sau đó

Tôi có thể có bản đồ cổng.

Làm cách nào tôi có thể chạy tập tin này

bây giờ tôi chỉ có thể nói docker,

soạn thảo và nhập.

Nó sẽ tự động kéo bạn

db đó là postgres của bạn.

Vậy chúng ta hãy chờ một lát nhé.

Vì vậy, về cơ bản nó đang thực hiện thao tác kéo

cho các postgres vì điều này

hình ảnh là một cái gì đó mới, phải không?

Nó phải kéo hình ảnh này.

Vì vậy, chúng ta hãy chờ đợi kéo.

Vì vậy, chỉ với một cú nhấp chuột, tôi

chỉ cần thiết lập cơ sở hạ tầng

ngay bây giờ chúng tôi chỉ có

một dịch vụ đó là db.

Vậy chúng ta hãy chờ một lát nhé.

Vâng, bạn có thể thấy nó đang chạy.

Xem có những bản ghi.

Và postgres của tôi là

đã hoạt động rồi phải không các bạn?

Postgres của tôi đã hoạt động.

Chỉ để xác minh thôi, đi thôi

vào máy tính để bàn docker.

Được rồi, để tôi mở docker

máy tính để bàn, nó trông như thế nào ở đó.

Vì vậy, đi đến bảng điều khiển.

Vì vậy bạn có thể thấy rằng ở đó

là một ngăn xếp thương mại điện tử

trong đó postgres đang chạy.

Và bạn có thể thấy rằng những điều này

các cổng đang được phơi bày.

Vì vậy, trong ứng dụng của tôi, hãy

bình luận ra redis bởi vì như

bây giờ tôi không có redis.

Và chúng tôi đang nghe trên 5431.

Đây là một vấn đề.

Nếu tôi kiểm soát C ở đây,

nó thực sự dừng lại.

Vì vậy, tôi có thể làm tương tự với dấu gạch nối D

cho chế độ tách rời.

Vậy dấu gạch nối D.

Vì vậy, nó chạy ở chế độ nền.

Bạn có thể thấy nó đang chạy.

Bây giờ nếu tôi nói bắt đầu NPM, bạn sẽ

xem postgres sẽ kết nối.

Được rồi, chúng tôi đang gặp lỗi.

Ồ, chúng ta cần phải xây dựng trước.

Vì vậy, NPM chạy, xây dựng và.

Và.

Được rồi.

Và NPM bắt đầu.

Vì vậy, bây giờ nó sẽ xây dựng và chạy.

Bây giờ bạn sẽ thấy điều đó

các postgres được kết nối.

Kỳ quặc.

Được rồi, nếu tôi đóng cái này lại thì sao?

Điều gì sẽ xảy ra nếu tôi, bạn biết đấy, dừng nó lại?

Vì vậy, bây giờ bạn thấy tôi đã có một lỗi.

Thấy nó không kết nối được.

Vì vậy, để chạy cái này tôi chỉ cần nói docker,

soạn, lên, gạch nối D.

Vì vậy, bây giờ nó đang chạy.

Bây giờ tôi chỉ có thể nói NPM

chạy, xây dựng và chạy.

Bạn có thể thấy kết nối postgres của tôi

đang dần thành công.

Tại sao?

Vì nó đang cố gắng

để kết nối trên 5431.

Vì vậy, ứng dụng này đang chạy

trên máy chủ của tôi, đang kết nối với 5431.

Đúng không?

Và vâng, nó có quyền truy cập vào nó.

Tuyệt vời, những thứ tuyệt vời.

Ngoài ra, hãy thêm Redis.

Vì vậy, tên dịch vụ Redis.

Đây có thể là bất cứ điều gì.

Sau đó, bạn phải chỉ định hình ảnh.

Vì vậy, tôi muốn redis làm cơ sở hạ tầng.

Phải?

Vì vậy, bạn có thể có Redis.

Vì thế tôi sẽ chỉ nói, này,

sử dụng hình ảnh nào?

Tôi muốn sử dụng hình ảnh này.

Hãy chỉ định vùng chứa

tên được redis.

Và bạn có thể nói cổng.

Được rồi.

Bản đồ cổng.

Vì vậy, điều này phơi bày.

Vì vậy cổng mặc định cho

bạn gọi là gì, Redis là 6378.

Sáu, ba, bảy.

Lấy làm tiếc.

6379.

Vì vậy, ánh xạ 6379 đến 6379.

Đúng.

Sau đó bạn có thể cho

các biến môi trường.

Không cần thiết.

Vì vậy, hãy để tôi làm một điều.

Docker soạn thảo,

Mọi thứ đều bị phá hủy.

Docker soạn thảo,

mọi thứ đã biến mất.

Bây giờ hãy soạn thảo lại Docker.

Vì vậy docker soạn dấu gạch nối D.

Lần này phải kéo redis

bởi vì redis không có ở đó.

Và redis sẽ có sẵn.

Vậy hãy chờ redis nhé

để được kéo.

Vâng, bạn có thể thấy

bây giờ redis đang hoạt động.

Postgres ở đó.

Và bây giờ tôi thậm chí có thể

bỏ ghi chú điều redis này.

Và nếu bây giờ tôi cố gắng chạy

ứng dụng, bạn sẽ thấy điều đó

redis cũng đang được kết nối.

Các bạn, màu đỏ đã được kết nối.

Đã kết nối Postgres.

Và điều khiển C để dừng lại.

Bạn có muốn phá hủy mọi thứ?

Không sao đâu.

Không sao đâu.

Docker soạn.

Soạn xuống.

Mọi chuyện đã qua rồi các bạn ạ.

Vậy điều đó có nghĩa là những gì tôi có

việc cần làm là tôi chỉ cần nói

gửi tới các nhà phát triển của tôi rằng này, đây là

một tập tin soạn thảo Docker.

Không cần phải chạm vào nó trước

đang chạy ứng dụng này.

Chỉ cần nói Docker Compose,

Docker Soạn dấu gạch nối D và của bạn

cơ sở hạ tầng đang hoạt động.

Tại sao?

Bởi vì tôi đã chỉ định

phiên bản, nó luôn là 16, tôi có

tất cả các biến môi trường được đặt

lên và hoàn toàn không có

cần cài đặt postgres này

thứ Redis này trên máy của tôi

máy cục bộ.

Cấu hình cụ thể này

đang chăm sóc nó.

Tôi có thể thêm bao nhiêu dịch vụ tôi muốn.

Tôi có thể tiếp tục thêm Redis Postgres,

Tôi có thể tiếp tục thêm MongoDB.

Về cơ bản tôi có thể thêm

có gì ở đây phải không?

Nếu bạn nghĩ về nó.

Vì vậy, về cơ bản đây là

cơ sở hạ tầng của tôi.

Docker soạn thảo.

Có một điều, các bạn, hãy nói với tôi một điều.

Hiện tại Docker này

Compose thực sự tạo ra

một mạng nội bộ.

Điều đó có nghĩa là, giả sử tôi muốn điều đó

DB nên sở hữu Redis nên

chỉ bắt đầu nếu DB có sẵn.

Vì vậy, tôi thậm chí có thể nói phụ thuộc vào.

Tôi có thể nói tùy thuộc vào, phải không?

Phụ thuộc vào.

Và tôi có thể nói dp.

Bây giờ điều đặc biệt này sẽ

chỉ và chỉ bắt đầu nếu điều này

DB đã hoạt động rồi phải không?

Vì vậy, điều này cũng có thể.

Và bởi vì họ ở trên cùng một

mạng, bạn biết không, tôi có thể làm gì

làm được, tôi thậm chí có thể chạy ứng dụng của mình

trong Docker soạn và.

Và không cần thiết

để sau đó thực hiện ánh xạ cổng.

Bởi vì xem ba dịch vụ

đang chạy trên cùng một mạng.

Nếu bạn còn nhớ ví dụ này thì phải

ở đây, nếu ba dịch vụ đang chạy

tương tự, không cần phải phơi bày

các cổng cho Redis và postgres.

Nhưng bởi.

Nhưng hiện tại điều đang xảy ra là

nút JS này thực sự là

chạy ra ngoài container.

Nó đang chạy trên máy chủ của tôi.

Đó là lý do tôi cần

để vạch trần Redis và tôi cần

để lộ cổng postgres.

Đó là vấn đề.

Nhưng trong những video sau tôi sẽ trình chiếu

bạn biết làm sao bạn có thể chạy được

ứng dụng của bạn bên trong một ứng dụng cụ thể

mạng nội bộ

được tạo bởi Docker Compose này.

Và rồi bạn sẽ thấy điều đó

không cần đâu, hoàn toàn không

cần cung cấp bản đồ cổng này

tới Redis và Postgres.

Vì vậy, về cơ bản đây là cách

mạng hoạt động phải không?

Nó tạo ra một mạng nội bộ.

Vì vậy, hãy nói nếu Redis muốn

để giao tiếp với db,

nó có thể sử dụng tên.

Bạn có nhớ ví dụ này ở đâu

Người nhện đã có thể kết nối với

Ironman nhưng chỉ bằng cái tên ở đây thôi.

Ngoài ra nếu Redis muốn kết nối

với DB bây giờ chỉ có thể nói db.

Nó chỉ có thể sử dụng db này.

Nó sẽ tự động đi

vào thùng chứa này.

Tất cả các cuộc gọi sẽ đi

vào thùng chứa này.

Vì vậy, chúng tôi sẽ.

Tôi sẽ cho bạn thấy điều đó

trong các video sắp tới.

Nhưng trong video cụ thể này, tôi

hy vọng bạn đã hiểu điều đó

Nhà soạn nhạc Docker là gì?

Docker soạn thảo.

Docker soạn dấu gạch nối

D Docker soạn thảo.

Và bạn phải tạo ra

tập tin soạn thảo Docker này.

Docker soạn tập tin YML.

Và đó chỉ là cấu hình.

Bạn chỉ có thể đi

bật và thêm cấu hình.

Thực ra bạn có rất nhiều

của các cấu hình.

Bạn có cấu hình lệnh,

cpu, kiểm tra sức khỏe.

Có rất nhiều cấu hình ở đó.

Và danh sách này có thể tiếp tục.

Được rồi, điều này rất hữu ích

trong việc thiết lập môi trường.

Chỉ bằng một lệnh, bạn có thể

có nhiều container đang chạy

tất cả các thiết lập cơ sở hạ tầng.

Và chỉ bằng một lệnh,

bạn có thể phá hủy mọi thứ.

Điều siêu mát mẻ.