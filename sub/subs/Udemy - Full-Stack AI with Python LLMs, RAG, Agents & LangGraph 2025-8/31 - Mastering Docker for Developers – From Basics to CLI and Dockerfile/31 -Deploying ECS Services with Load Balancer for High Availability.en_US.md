# 31 -Triển khai dịch vụ ECS với Load Balancer để có tính sẵn sàng cao.en US

---

Vậy nên các bạn, hãy ăn cái này nhé

dịch vụ được thiết lập và chạy.

Vì vậy hãy đi vào các cụm

và đi vào dev.

Và hãy nói điều đó ở đây

Tôi không có dịch vụ nào cả

Tôi không có nhiệm vụ gì phải không?

Vì thế tôi chỉ muốn

để tạo ra một dịch vụ mới.

Vì vậy, bạn có thể chỉ cần nhấp vào

trên nút tạo này.

Vì vậy, hãy tạo ra một dịch vụ.

Vì vậy ở đây tôi muốn có

một kiểu khởi chạy của Fargate.

Bạn muốn triển khai cái gì?

Tôi muốn triển khai một dịch vụ.

Sử dụng tác vụ nào?

Cái mà.

Sử dụng cấu hình nào?

Cấu hình này.

Cấu hình này để sử dụng.

Chúng tôi vừa làm đúng

trong định nghĩa nhiệm vụ.

Tên dịch vụ.

Tôi có thể đặt tên dịch vụ này là API.

Bạn muốn khởi động bao nhiêu nhiệm vụ?

Hãy nói rằng tôi muốn

có một thùng chứa.

Tôi có thể có khoảng bốn container.

Hãy nói, được, vậy bạn có thể

có hai thùng chứa.

Vì vậy, điều này về cơ bản có nghĩa là.

Này, về cơ bản tôi đang nói

đó, này, khi bạn quay lên,

triển khai hai container.

Cân bằng tải giữa hai container.

Phải?

Tùy chọn triển khai.

Cập nhật cuộn.

Không sao đâu.

Bây giờ kết nối mạng.

Mọi thứ đều ổn phải không?

Bạn muốn gán một IP công cộng cho nó.

Cân bằng tải.

Bạn có muốn cân bằng tải?

Vâng, tôi muốn làm

cân bằng tải ứng dụng.

Trên cổng nào?

Số cổng 8.000.

Bởi vì đây là những gì chúng tôi đã đưa ra

trong định nghĩa nhiệm vụ của chúng tôi.

Bạn biết đấy, chúng tôi đã để lộ Cổng 8000.

Tạo một bộ cân bằng tải mới.

Vì vậy tôi có thể đưa ra điều đặc biệt này

cân bằng tải một tên.

Vì vậy, tôi có thể nói cân bằng tải API.

Được rồi, vậy thì cân bằng tải API.

Được rồi.

Tải này trên cổng nào

cân bằng sẽ chạy?

80.

Cân bằng tải luôn chạy trên cổng 80.

Đó là HTTP.

Được rồi, sau đó có một nhóm mục tiêu.

Vậy là ổn rồi.

HTTP, mọi thứ đều ổn.

Phải?

Sau đó, bạn có muốn tự động mở rộng quy mô không?

Có, tôi muốn tự động chia tỷ lệ.

Vậy làm thế nào để tự động chia tỷ lệ?

Thùng chứa tối thiểu phải là hai.

Giống như luôn giữ hai thùng chứa

lên và chạy.

Nhưng tối đa bạn có thể đi như năm.

Vì vậy nếu lưu lượng truy cập

tăng dần, như năm.

Vì vậy, trên quy mô lớn, bạn có thể làm được khoảng 50.

Bạn có thể làm 100.

Nhưng được rồi, tôi sẽ chỉ nói năm.

Vì vậy, tối thiểu hai.

Nhưng nếu bạn nghĩ rằng những điều này

container đang trở nên quá tải,

rất nhiều yêu cầu đang đến.

Chỉ cần nâng cấp chúng lên năm.

Phải?

Bạn muốn đo lường điều đó như thế nào

một container đang bị quá tải?

Vì vậy tôi có thể nói nếu trung bình,

Việc sử dụng CPU.

Tôi chỉ có thể nói mức trung bình của CPU.

Được rồi, bạn chỉ cần đặt tên

chính sách và điều này.

Nếu mức sử dụng CPU trung bình

tăng 70%, điều đó có nghĩa là cả hai

của các container là

đang chạy và CPU trung bình

mức tiêu thụ đã tăng 70.

Điều đó có nghĩa là của bạn

giao thông ngày càng tăng.

Đó là nơi bạn có thể nâng cấp.

Bạn không thể cao cấp.

Bạn có thể nâng cấp vùng chứa này.

Nhưng tối đa là tới 5.

Vì vậy đây là một chính sách

về những thông số nào để mở rộng quy mô.

Đó là những gì tôi đang nói.

Phải.

Và bạn có muốn đính kèm

một số khối lượng bổ sung?

Không.

Và chỉ cần nhấp vào nút tạo này.

Đó là nó.

Các bạn, các bạn vừa thực hiện dịch vụ của riêng mình.

Bây giờ bạn phải đợi một lúc.

Được rồi, dịch vụ này

sáng tạo mất rất nhiều thời gian.

Được rồi, bây giờ bạn có thể thấy tôi không

có bất kỳ dịch vụ nào bởi vì

dịch vụ này đang được tạo ra.

Bây giờ dịch vụ này lý tưởng là gì

thực hiện nội bộ, dịch vụ này

đang tạo vùng chứa cho bạn.

Dịch vụ này đang tạo

cân bằng tải cho bạn.

Dịch vụ này đang tạo

nhóm mục tiêu cho bạn.

Nó đang tạo mạng

chính sách dành cho bạn.

Nó đang tạo các nhóm nhật ký cho bạn.

Nó đang tạo ra điều gì vậy bạn

gọi cơ sở hạ tầng

cho bạn và cỗ máy nơi bạn

có thể chạy những container này.

Và nó chứa đựng.

Còn một điều nữa, an ninh

nhóm dành cho bạn

và cân bằng tải tự động mở rộng quy mô.

Tất cả những thứ đó mà chúng tôi

vừa cấu hình xong hết

đó đang được tạo ra.

Vì đây là lần đầu tiên của chúng tôi,

nó sẽ mất một thời gian.

Vì vậy tôi sẽ tua nhanh video.

Trong khi đó điều này đang được tạo ra.

Bạn có muốn xem nó đang làm gì không?

Bạn có thể tìm kiếm một dịch vụ

được gọi là sự hình thành đám mây.

Nó sử dụng đám mây nội bộ

hình thành để làm công việc này.

Vậy sự hình thành đám mây, không phải đám mây,

sự hình thành đám mây, không phải đám mây,

phía trước, sự hình thành đám mây.

Vâng.

Cái này bạn chỉ cần mở

liên kết cụ thể này trong một liên kết mới

tab đó là sự hình thành đám mây.

Vì vậy, hãy xem điều gì đang xảy ra.

Đây là một trong những quá trình tạo đang được tiến hành.

Bạn chỉ có thể nhấp vào điều này.

Vậy nội bộ nó là gì

đang làm, hãy xem ngăn xếp.

Vì vậy nó đang tạo ra rất nhiều

những thứ dành cho bạn, nguồn lực.

Vậy là đã tạo rồi

một nhóm mục tiêu cho bạn.

Bây giờ những gì nó đang làm là

tạo một bộ cân bằng tải cho bạn.

Vì vậy, bạn có thể thấy quá trình tạo đang diễn ra.

Đúng vậy, cân bằng tải

đang được tạo ra.

Vì vậy, các sự kiện là có.

Bạn có thể thấy nó bắt đầu như thế nào.

Vậy là nhóm mục tiêu đã xong.

Cân bằng tải, nhóm mục tiêu.

Vì vậy, bạn có thể thấy nó đang diễn ra như thế nào.

Vì vậy, chúng ta hãy nhấp vào đây mà thôi.

Vì vậy, quá trình sáng tạo đang được tiến hành.

Vậy đây chính là điều đặc biệt

dịch vụ đang được thực hiện nội bộ.

Cái này, cái thứ đang tải này.

Đúng rồi, đang tải thứ này ở đây

đang làm công việc này.

Vì thế chúng ta có thể, chúng ta có thể có

một cái nhìn sâu sắc.

Vậy là nhóm mục tiêu đã xong.

Cân bằng tải đang được tạo.

Cân bằng tải cần có thời gian.

Cân bằng tải cần có thời gian.

Phải.

Và sau đó nó sẽ tạo ra

dịch vụ và tất cả những thứ đó.

Vì vậy đây là cái mà chúng tôi

đã tạo cụm, phải.

Vì vậy, khi chúng tôi tạo một cụm

nó vừa tạo ra một cụm.

Bây giờ chúng tôi đang tạo ra một dịch vụ.

Ồ thấy không?

Cân bằng tải đã xong.

Trình nghe trên bộ cân bằng tải được thực hiện.

Bây giờ nó đang tạo ra một dịch vụ cho chúng tôi.

Vậy hãy xem nó thế nào, nó tốt thế nào

Quản lý tài nguyên cho chúng tôi.

Bạn thậm chí có thể kiểm tra, bạn biết đấy,

bạn có thể thích tìm kiếm, ec2.

Bạn có thể thích tìm kiếm ec2.

Vì vậy, khi bạn tìm kiếm ec2,

sau đó bạn sẽ có

một thứ cân bằng tải.

Vì vậy, cân bằng tải.

Vì vậy, đây là bộ cân bằng tải.

Bạn có thấy không?

Cân bằng tải API, phải không?

Và bạn thậm chí có thể đi

vào nhóm mục tiêu.

Vì vậy bạn có thể thấy điều đó ở đây

là nhóm mục tiêu.

Vì vậy nhóm mục tiêu này là

về cơ bản nhắm mục tiêu.

Bạn gọi dịch vụ ECS của chúng tôi là gì?

Và bộ cân bằng tải này về cơ bản là

cân bằng tải trên nhóm mục tiêu đó.

Được rồi?

Đây là cách mọi thứ hoạt động trong aw.

Và bây giờ là dịch vụ

đang được tạo ra.

Vì vậy, vâng.

Được rồi, các bạn, các bạn có thể thấy,

dịch vụ được thực hiện.

Bạn có thể thấy điều đó không?

Nếu tôi bắt đầu thực hiện nhiệm vụ,

nó thực sự đang cố gắng

để tạo ra những nhiệm vụ này.

Nhưng nó nói không lành mạnh.

Bạn có biết lý do không?

Bởi vì sức khỏe của chúng ta là gì

kiểm tra xem bạn có phải thực hiện không

một yêu cầu về sức khỏe cắt giảm.

Nhưng các bạn, nếu các bạn còn nhớ, chúng ta

chưa đẩy mã này.

Không có con đường sức khỏe, phải không?

Và vì không có sức khỏe

tuyến đường, nó không thể

để xác nhận lộ trình sức khỏe.

Và vì điều đó

nó đang nói không lành mạnh.

Và bởi vì những thùng chứa này

được đánh dấu là không lành mạnh, bạn sẽ thấy

rằng những container này đang nhận được

bị phá hủy và nó sẽ tự động

tạo một vùng chứa mới.

Bởi vì tôi đã nói điều đó, này,

thùng chứa tối thiểu phải là hai.

Vì vậy, bởi vì những thùng chứa này

không chạy, họ không chạy.

Họ không khỏe mạnh.

Vì vậy, những thứ này sẽ bị giết và mới

container đang được sử dụng hết.

Vì vậy điều chúng ta nên làm là chúng ta nên

xây dựng lại hình ảnh này, được chứ?

Vì vậy chỉ cần xây dựng lại hình ảnh này

và chỉ cần đẩy nó lần nữa, được chứ?

Bởi vì bây giờ chúng ta cần một con đường sức khỏe.

Thế là xong.

Và bây giờ chỉ cần gắn thẻ

và chỉ cần thực hiện một cú đẩy.

Vì vậy bây giờ khi bạn thực hiện cú đẩy,

bạn sẽ thấy trong ecr của mình, được chứ?

Trong ECR của bạn, bạn sẽ

xem kho lưu trữ.

Bây giờ bạn có thể thấy rằng tôi chỉ

đã đẩy một phiên bản mới.

Bây giờ những gì tôi có thể làm là tôi có thể đi vào

dịch vụ và tôi chỉ phải nói.

Tôi chỉ cần nói cập nhật, dịch vụ.

Bạn có thấy điều này không?

Cập nhật, dịch vụ.

Buộc triển khai mới, phải không?

Buộc triển khai và cập nhật mới.

Thế thôi.

Bây giờ nó sẽ làm gì, nó

sẽ kéo hình ảnh một lần nữa.

Bây giờ chúng ta có một hình ảnh mới,

hình ảnh mới nhất một lần nữa.

Vậy bây giờ chúng ta hãy xem điều gì sẽ xảy ra.

Được rồi?

Vì vậy ngay bây giờ tất cả

các nhiệm vụ là không lành mạnh.

Đây là những nhiệm vụ trước đó.

Vì thế họ phải bị giết.

Vì vậy hãy chờ đợi họ

bị giết vì những thứ này

được đánh dấu là không lành mạnh.

Vì vậy, bởi vì những thùng chứa này là

không lành mạnh, nó vẫn đang được tiến hành.

Vì vậy nó sẽ cố gắng giết những người đó

container, mang container mới vào

nếu chúng khỏe mạnh,

sau đó giết những cái trước nếu

những thứ đó không tốt cho sức khỏe, hãy quay lại.

Vì vậy nó làm rất nhiều

những điều bên trong.

Vì vậy, hãy bắt tay vào nhiệm vụ.

Vì vậy, trong, trong, trong một vài giây

bạn sẽ thấy điều đó, được rồi, nó

sẽ tạo ra các thùng chứa mới.

Được rồi.

Vì vậy phải mất một thời gian.

Phải mất một thời gian vì

bạn biết đấy, tạo ra và phá hủy

không phải là điều dễ dàng.

Đúng vậy, nếu bạn chỉ muốn

để làm điều đó, bạn biết đấy, rất nhanh,

bạn chỉ cần nhấp vào những cái này

và bạn có thể dừng chúng bằng tay.

Bạn chỉ có thể dừng những điều này

container dừng lại.

Được rồi, bây giờ bạn sẽ thấy

cái đó, được rồi, nó nói, này, số không

của hai nhiệm vụ đang chạy.

Vì vậy nó sẽ tự động thử

để phù hợp với trạng thái này.

Tình trạng.

Vì vậy, hãy xem, trạng thái mong muốn là 2, nhưng,

nhưng hiện tại là 0.

Vì vậy nó sẽ cố gắng để phù hợp.

Vì thế nó nói, ồ, tôi đã được hướng dẫn

có hai thùng chứa, nhưng ở đó

chỉ bằng 0, nên tôi nên

quay lên hai thùng chứa mới.

Vì vậy, trong một vài giây, bởi vì

chúng tôi có rất nhiều cuộc kiểm tra sức khỏe

vấn đề, trong vài giây

bạn sẽ thấy nó đang diễn ra

để triển khai các container mới.

Được rồi các bạn, bây giờ các bạn có thể

thấy đã lâu lắm rồi.

Bây giờ bạn có thể thấy rằng nó

đã biến một cái gì đó.

Vì vậy bây giờ bạn sẽ thấy rằng nó sẽ

bắt đầu tạo vùng chứa mới.

Đúng vậy, bạn có thể thấy điều đó

thùng chứa này hiện đang

ở trạng thái chờ xử lý.

Vì vậy, thùng chứa đặc biệt này nên

thực sự đã vượt qua cuộc kiểm tra sức khỏe.

Vì vậy bây giờ bạn có thể thấy tôi có

hai thùng chứa

ngay bây giờ họ không hoạt động.

Vì vậy, một lần, hãy xem điều gì sẽ xảy ra.

Đầu tiên họ sẽ hoạt động, sau đó

họ phải vượt qua cuộc kiểm tra sức khỏe.

Chỉ khi đó họ mới đi

được coi là khỏe mạnh.

Vì vậy, một container đang chạy

nhưng vẫn không khỏe.

Sẽ mất một thời gian vì

ban đầu, bạn biết đấy, cần phải có,

Tôi nghĩ chúng ta đã thiết lập nó

đến 20 giây nếu bạn nhớ.

Vì vậy, nó sẽ mất 20 giây đầu tiên.

Được rồi, nó đã, nó đã từng

được đánh dấu là không lành mạnh.

Vấn đề có thể là gì?

Vì vậy, các bạn, nó thực sự rất xấu hổ.

Tôi không thể gỡ lỗi đó.

Điều gì thực sự đã xảy ra?

Bạn biết những điều này chúng tôi

thực sự sử dụng trong sản xuất, bạn

có thể thấy chúng tôi có container

đang chạy, chúng tôi có số liệu thống kê tốt.

Tôi nghĩ đây là một tài khoản mới.

Có vấn đề gì đó xảy ra hoặc có thể tôi đang

phạm phải một số sai lầm ngớ ngẩn, nhưng tôi có

đã kiểm tra chéo rất nhiều lần.

Vì vậy ngay bây giờ những gì tôi đã làm là

Tôi đã tắt tính năng kiểm tra sức khỏe.

Làm thế nào bạn có thể làm điều đó?

Bạn phải đi vào

định nghĩa nhiệm vụ.

Bạn phải mở nhiệm vụ của bạn.

Vì vậy bạn có thể thấy tôi có

rất nhiều phiên bản.

Bây giờ giả sử bạn đang ở trên hai, vì vậy

bất kể phiên bản mới nhất của bạn là gì,

nếu phiên bản mới nhất của bạn là một.

Chỉ cần chọn một.

Vì vậy bạn phải lựa chọn của bạn

phiên bản mới nhất, bấm vào đây

và tạo một bản sửa đổi mới.

Và sau đó bạn phải làm gì

là bạn phải đi xuống

và bạn chỉ cần bỏ chọn

tất cả các trường kiểm tra sức khỏe này.

Chỉ cần làm cho chúng trống rỗng, phải không?

Tất cả các lĩnh vực.

Một khi bạn làm điều đó, bạn chỉ có thể

nhấp vào tạo và điều này sẽ

tạo một bản sửa đổi mới của nó.

Vì vậy, ví dụ, nếu bạn

trên một, nó sẽ tạo ra hai.

Nếu bạn ở trên hai, nó

sẽ tạo ra ba.

Bây giờ tôi đang ở trên năm, vì vậy

nó sẽ tạo ra sáu.

Khi bạn đã tạo một bản sửa đổi mới,

bạn có thể tới nhà phát triển này,

bấm vào dịch vụ này, phải không?

Bạn chỉ có thể nói dịch vụ cập nhật.

Bạn chỉ có thể nói bắt buộc mới

triển khai và chọn phiên bản mới nhất

triển khai, đúng thế nào cũng được

là bản sửa đổi mới nhất của bạn

và chỉ cần nhấp vào bản cập nhật này.

Nó.

Sẽ mất một thời gian và sau đó

dần dần nó sẽ cập nhật.

Bây giờ bạn có thể thấy rằng tôi có

đã xóa phần kiểm tra sức khỏe.

Điều này hiện đang hoạt động để xác minh rằng

nếu mọi thứ đều hoạt động hay không.

Hãy đến EC2 vì bạn nhớ

chúng tôi đã thực hiện một bộ cân bằng tải.

Vậy EC2 và đi thôi

vào bộ cân bằng tải.

Vì vậy, tôi thực sự đã thực hiện

một bộ cân bằng tải mới.

Để tôi có thể nhấp vào bộ cân bằng tải này,

sao chép tên DNS này.

Bạn có thấy tên DNS này ở đây không?

Vì vậy bạn chỉ cần sao chép tên DNS này

và cố gắng đưa ra yêu cầu về nó.

Được rồi, nếu bạn cố gắng đưa ra một yêu cầu

trên đó, bạn có thể thấy rằng tôi

thực sự nhận được phản hồi.

Bây giờ có thể có cơ hội

rằng bạn sẽ không nhận được phản hồi này.

Làm sao vậy?

Những gì bạn có thể làm là bạn có

để chắc chắn rằng bạn phải đi

vào các nhóm bảo mật.

Đây là bảo mật mặc định

nhóm và bạn phải chỉnh sửa

quy tắc gửi đến theo mặc định.

Tôi nghĩ quy tắc gửi vào là

điều gì đó như bạn biết đấy,

TCP tùy chỉnh hoặc tương tự như tùy chỉnh.

Và sau đó là một nhóm bảo mật.

Tôi nghĩ đây là cái mặc định.

Những gì bạn chỉ cần làm,

xóa mọi thứ.

Hãy tạo ra một quy tắc rằng này,

tất cả TCP được phép từ mọi nơi

và thêm một quy tắc nữa là tất cả

TCP được phép từ mọi nơi

và chỉ cần lưu quy tắc này.

Thế thôi.

Nhóm bảo mật.

Về cơ bản bạn đang nói, bạn

biết, cho phép mọi thứ bật, bật

mọi trang web và sau đó bạn có thể

thấy rằng đúng, về điều này

miền cụ thể vùng chứa của tôi

là chính xác và nó là

nhận được cân bằng tải.

Nó thực sự đang được cân bằng tải

giữa hai thùng chứa này.

Bây giờ những lý do có thể là gì

cuộc kiểm tra sức khoẻ hôm nay thất bại à?

Tôi đang nhìn thấy một điều, một điều rất

mẫu AWS không phản hồi

cách nó đã từng phản ứng.

Bạn có thể thấy điều đó đầu tiên,

cụm, việc tạo đã thất bại.

Sau đó tôi có thể nhìn thấy rất nhiều thứ

ngày nay đang thất bại.

Tôi nghĩ có một số vấn đề nội bộ

vấn đề với Cloudflare.

Xin lỗi, không phải Cloudflare với aws,

bởi vì ngay cả tôi cũng đang nhìn thấy

ngăn xếp Cloudflare, bạn có thể thấy

rằng việc tạo ra đã thất bại.

Còn có một vài thứ nữa

điều đó đang trở nên thất bại.

Vì vậy, suy đoán của tôi vào lúc này là

Bạn biết đấy, AWS không xử lý nó.

Và một điều nữa tôi muốn cho bạn thấy

về các giáo viên sản xuất của chúng tôi.

Bạn có thể thấy điều đó ngay bây giờ khi bạn

đang xem video đặc biệt này.

Đây là máy chủ của điều đó.

Bạn có thể thấy chúng tôi có định nghĩa nhiệm vụ.

Và bạn có thể thấy rõ, bạn

có thể thấy rằng chúng tôi đang sử dụng

lệnh tương tự, phải không?

Và nó hoạt động như một sự quyến rũ.

Vì vậy tôi đoán là thế

có một số vấn đề

Vì vậy, chúng tôi sẽ cố gắng gỡ lỗi nó một lần nữa.

Được rồi, cái đó.

Cái gì, vấn đề chính xác là gì vậy?

Nhưng tôi đã và đang làm việc đó

trong nhiều năm như vậy.

Đây là cách đúng đắn.

Tôi thực sự không thể nghĩ

về bất cứ điều gì có thể xảy ra sai sót.

Nếu có gì đó,

Tôi chắc chắn sẽ cập nhật cho bạn.

Nhưng vâng, chắc chắn là như vậy

làm việc vì chúng tôi đã

làm việc đó trong một thời gian dài.

Nhưng đây là cách bạn có thể triển khai

các container sử dụng dịch vụ.

Vậy bây giờ bạn đã biết về

ecr, bạn biết về ecs, bạn biết đấy

cụm, bạn biết nhiệm vụ

định nghĩa, bạn biết dịch vụ.

Một điều mà tôi đã không thể làm được

xong, đó chính là kiểm tra sức khỏe.

Nhưng các bạn đừng lo lắng, ngay khi

khi tôi gỡ lỗi nó, nếu tôi có được chút gì đó chắc chắn

giải pháp, xem bây giờ tôi có ổn không

giả sử rằng đây là một cái gì đó để

làm với aw, nó có thể hiệu quả

bạn.

Nhưng nếu nó không hoạt động, nếu có

là một số vấn đề thực sự từ tôi

bên cạnh, tôi sẽ cập nhật các video.

Được rồi?

Tôi hy vọng rằng nếu bạn đang theo dõi

đồng thời, cuộc kiểm tra sức khỏe của bạn đã đạt yêu cầu.

Và nếu nó đi qua,

điều đó thật tuyệt phải không?

Điều đó có nghĩa là có vấn đề gì đó

bằng tài khoản AWS của tôi.

Nhưng nếu không, đừng lo lắng,

Tôi sẽ cập nhật video.

Vậy hãy kết thúc video này nhé

và gặp lại bạn ở lần tiếp theo.