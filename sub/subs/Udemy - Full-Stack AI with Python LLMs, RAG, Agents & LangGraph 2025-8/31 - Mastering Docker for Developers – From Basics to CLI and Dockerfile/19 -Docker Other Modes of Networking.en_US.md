# 19 -Docker Các chế độ kết nối mạng khác.en US

---

Được rồi, bây giờ chúng ta hãy nói về

các chế độ kết nối mạng khác

có sẵn trong Docker.

Được rồi, vậy hãy bắt đầu.

Vậy là chúng ta đã nhìn thấy cây cầu rồi.

Sau đó chúng ta có máy chủ.

Bây giờ chủ nhà là gì?

Máy chủ là thứ không phải

khuyến khích sử dụng và đó

không hoạt động tốt trên MacBook.

Đúng.

Vậy là có lỗi và máy chủ này

không hoạt động chính xác

trên MacBook tính đến ngày hôm nay, như

kể từ ngày quay video này.

Có lẽ nó sẽ được sửa trong tương lai.

Vậy nó làm gì.

Tôi sẽ chỉ giải thích cho bạn.

Đúng, vậy nó sẽ làm gì khi bạn nói

máy chủ mạng, bộ chứa docker

không ở trong một môi trường biệt lập.

Nó được kết nối trực tiếp

đến giao diện máy chủ.

Và ưu điểm của việc này là

bây giờ bạn không cần phải làm nữa

điều ánh xạ cổng P có dấu gạch nối đó.

Nếu vùng chứa Docker này

để lộ Cổng 8000,

nó có sẵn cho bạn ngay tại đó.

Không cần làm gạch nối P8000

được gắn vào cổng 8000.

Không cần thiết vì nó trực tiếp

đang chạy trên máy chủ của bạn.

Nó sử dụng địa chỉ IP của bạn.

Nó giống như một quá trình

đang chạy trên máy của bạn.

Về cơ bản đây là chế độ máy chủ

mạng, nhưng về cơ bản nó

xóa bỏ sự cô lập giữa

container và máy chủ docker.

Đúng vậy, đây là một chuyện.

Sau đó có một số đó là

Lớp phủ ca sử dụng rất tiên tiến.

Lớp phủ cho phép bạn kết nối nhiều

docker daemon với nhau.

Chỉ cần tưởng tượng bạn có

docker này đang chạy.

Bạn còn một cái nữa

daemon docker đang chạy.

tôi chỉ đang nói chuyện thôi

về toàn bộ docker.

Vì vậy, nếu bạn muốn tạo một cây cầu

giữa chúng có hai docker riêng biệt

daemon, đó là nơi bạn có thể

sử dụng Overlay, sau đó là ipvlan và Mac

vlan, hai cái này hay quá.

Trong ipvlan, về cơ bản nó mang lại cho bạn

toàn quyền kiểm soát địa chỉ IP

phân bổ cho các container docker.

Phải?

Vì vậy bạn có thể đọc nó ở đây.

Và Mac Vlan ở một cấp độ khác.

Nếu bạn làm Mac vlan,

về cơ bản nó giống như bạn đang tạo

một container docker như

một máy vật lý riêng biệt.

Máy vật lý nơi chứa này

có địa chỉ Mac riêng, có địa chỉ của nó

địa chỉ IP riêng và những thứ tương tự

kết nối trực tiếp với bộ định tuyến này.

Về cơ bản đây là Mach vlan.

Vì vậy bạn phải cho đi rất nhiều

cấu hình như thế

cấu hình cổng và sau đó là gì

bạn gọi giao diện à

cấu hình và rất nhiều thứ,

Cấu hình vòng lặp.

Vì vậy, về cơ bản nó cố gắng tạo ra

một máy vật lý trên mạng của bạn

có máy Mac riêng

địa chỉ và địa chỉ IP và trực tiếp

kết nối với bộ định tuyến.

Vì vậy, về cơ bản đây là Mac vlan.

Vì vậy, bạn có thể đọc Mac VLAN cho phép bạn

để gán địa chỉ Mac cho

vùng chứa, làm cho nó xuất hiện dưới dạng A

thiết bị vật lý trên mạng của bạn.

Hiểu rồi.

Đây là một điều, sau đó cuối cùng là không có gì.

Cái này cũng được sử dụng khá nhiều.

Tôi sẽ kể cho bạn nghe.

Vì vậy, nếu tôi nói docker run, hãy

tạo một vùng chứa mới.

Docker chạy nó.

Và tôi nói, này, gạch nối, gạch nối RM

Chúng ta đừng đặt cho nó một cái tên.

Và tôi nói dấu gạch nối, dấu gạch nối, mạng.

Được rồi, Mạng.

Và chỉ cần nói không.

Được rồi, không có.

Và bạn chỉ có thể nói bận rộn, hộp.

Được rồi, vậy hãy để hộp bận rộn chạy.

Vậy bây giờ container này không thể đi được

đến thế giới bên ngoài

vì chế độ mạng đang bật.

Xem google.com không thể.

Hãy thử piyushkar.dev

uh.dev không thể được.

Bạn có thể ping một số địa chỉ IP không?

1.1.1.1 có lẽ vậy?

Không, thấy đấy, mạng không thể truy cập được.

Vì vậy nếu bạn nói không có mạng,

về cơ bản nó tạo ra sự thuần khiết

môi trường biệt lập.

Vì vậy, nếu bạn muốn chạy một số

ứng dụng, bạn biết đấy, hãy kiểm tra nó

ra ngoài hoặc có một số thứ nhạy cảm

dữ liệu, bạn chỉ muốn làm

một số loại tính toán

trong ứng dụng cụ thể đó.

Và bạn lo lắng rằng nên có

không được gọi mạng ra bên ngoài phải không?

Bạn đang chạy một số mã và bạn

chỉ lo lắng rằng có

không nên gọi ra bên ngoài.

Về cơ bản thì không có mạng

vô hiệu hóa toàn bộ mạng.

Không có kết nối đi được cho phép.

Vì vậy, vâng, đây là một điều.

Được rồi.

Và thậm chí còn có plugin.

Vì vậy, về cơ bản đây là của bạn

Tóm lại, mạng Docker.

Chủ yếu chúng tôi sử dụng thứ này

là cây cầu do người dùng xác định,

thường là cầu vì nó là

mặc định, nó sẽ được tạo.

Nhưng khi bạn đi vào thực tế

ứng dụng, 98% số lần bạn

sử dụng mạng cầu do người dùng xác định.

Vì vậy, hãy kết thúc chuyện này

video cụ thể và tôi hy vọng bạn

đã thích phần này

kết nối mạng trong các vùng chứa Docker.