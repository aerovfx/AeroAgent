# 14 -Xuất bản hình ảnh Docker lên Docker Hub hoặc Private Registries.en US

---

Vì vậy, này các bạn, cụ thể là thế này

video, chúng ta sẽ đi

để xuất bản hình ảnh docker tùy chỉnh của chúng tôi

đến hub.docker.com phải không?

Chúng tôi sắp công bố công khai

hình ảnh để mọi người, các nhà phát triển

trên toàn thế giới có thể sử dụng tùy chỉnh của tôi

image và chạy trên máy của họ.

Vì vậy, nó siêu dễ dàng.

Vậy hãy để tôi quay lại bảng trắng

và trước tiên hãy hiểu

những gì chúng tôi đang cố gắng đạt được ở đây.

Được rồi.

Vì vậy, hãy xem, tôi hy vọng rằng nếu bạn

ít nhất bạn là một nhà phát triển

biết về GitHub phải không?

GitHub là gì?

Nó là gì?

Tôi có thể nói rằng nó cơ bản là như vậy

một máy chủ trung tâm.

Được rồi.

Tôi chỉ có thể nói đó là một máy chủ trung tâm.

Đó là một kho lưu trữ nơi bạn

có thể đẩy mã của bạn và mọi người xung quanh

thế giới có quyền truy cập hoặc

nếu đó là mã công khai thì mọi người

trên toàn thế giới có thể kéo nó.

Phải?

Vì vậy, đây là một máy chủ trung tâm.

Tương tự, trong docker

thế giới chúng ta có một thứ được gọi là

cơ quan đăng ký container.

Được rồi, được rồi.

Vậy sổ đăng ký container này là gì?

Ví dụ như có rất nhiều

của các cơ quan đăng ký, nhưng Official1

là hub.docker.com vậy

đây là cái chính thức

Nhưng bạn có như ecr, kho lưu trữ,

bạn có từ Digital Oceans,

bạn có từ những gì bạn gọi,

Google Cloud ở đó.

Vì vậy, Google Cloud có

sổ đăng ký hiện vật.

Vậy là bạn đã có thùng chứa

cơ quan đăng ký, một lần nữa,

lại là một máy chủ trung tâm.

Mọi người trên khắp thế giới có thể

xuất bản hình ảnh của họ lên đây

cơ quan đăng ký và mọi người trên khắp thế giới

có thể kéo những hình ảnh này.

Vì vậy, về cơ bản nó giống như nếu tôi có

để nói điều này trong một thế giới,

sổ đăng ký container là gì?

Về cơ bản nó là một GitHub

cho hình ảnh Docker.

Thế là xong, GitHub

cho hình ảnh Docker.

Vậy hãy đi đến phần chính thức

Một trong số đó là hub.docker.com

vì vậy bạn có thể thấy rằng điều này

là một trung tâm hình ảnh Docker.

Và chúng tôi đã và đang kéo Ubuntu,

chúng tôi đã kéo Alpine,

chúng tôi đã kéo hộp bận rộn,

chúng tôi đã kéo Node.

Vì vậy, tất cả điều này được kéo

từ đây, phải.

Và bây giờ chúng ta sẽ làm gì

việc cần làm là chúng tôi sẽ xuất bản

hình ảnh của chúng tôi tới trung tâm này.

Vậy hãy nhanh tay đăng ký nhé.

Vì vậy bạn cần tạo một tài khoản

trên hub.docker.com trong trường hợp của tôi

Tôi đã có tài khoản rồi.

Vì vậy điều tôi sắp làm là tôi

sẽ thực hiện đăng nhập nhanh chóng.

Vì vậy, bạn có thể thấy rằng tôi có

đăng nhập vào tài khoản của tôi và bạn

có thể xem liệu tôi có nhấp vào tài khoản của mình không

và tôi vào hồ sơ của mình.

Vậy hãy xem đó là gì

hồ sơ của tôi trông như thế nào.

Đã được một thời gian rồi.

Vì vậy, kho lưu trữ.

Vâng, bạn có thể thấy tôi có

không có kho lưu trữ, phải không?

Vì vậy không có kho lưu trữ.

Vì vậy, giống như bạn tạo kho lưu trữ

trên GitHub, bạn là bạn có

để tạo một kho lưu trữ ở đây.

Vì vậy, hãy tạo một kho lưu trữ.

Vì vậy tôi muốn tạo một kho lưu trữ

trong tài khoản của tôi.

Tên kho lưu trữ của bạn là gì?

Vì vậy, nó có thể giống như

nút, ứng dụng nút.

Được rồi, ứng dụng Node.

Và tôi có thể có một mô tả

rằng đây là, đây là của tôi

ứng dụng nút, làm thế nào

để chạy nó và tất cả những thứ đó.

Bây giờ có một công chúng

và có một cái riêng.

Phải?

Bây giờ vấn đề là bởi vì tôi

trên gói miễn phí, bạn chỉ có thể có

một kho lưu trữ riêng tư, nhưng tôi

có thể có nhiều bạn biết đấy, làm gì

bạn gọi các kho lưu trữ công cộng.

Đúng vậy, vậy hãy tạo ra một công chúng

chỉ để bất cứ ai cũng có thể sử dụng.

Nhưng nếu là bạn, hãy để tôi đọc

họ, họ đang yêu cầu xếp hạng.

Được rồi, nhưng nếu bạn

trong một tổ chức, bạn là

xây dựng nó cho chính mình,

bạn có thể có một cái riêng tư.

Nhưng vâng, đi thôi, đi thôi

với công chúng và sáng tạo.

Vì vậy, bạn có thể thấy kho lưu trữ của chúng tôi

và kho lưu trữ được tạo.

Và kho lưu trữ là pushkar dev.

Đó là tên người dùng, không gian tên của tôi

ứng dụng nút gạch chéo.

Bây giờ hãy hiểu điều này.

Trên địa phương của tôi, trên địa phương của tôi

Tôi có một hình ảnh Docker.

Vì vậy, hãy nói rằng

đây là địa phương của tôi phải không?

Ở địa phương của tôi, tôi có Docker

hình ảnh có tên là ứng dụng của tôi.

Tôi có thể xuất bản cái này không, ứng dụng của tôi, như nó vốn có

tới hub.docker.com thì không, bởi vì điều này,

ứng dụng của tôi không chỉ định gì cả, phải không?

Đây là cái gì?

Ứng dụng của tôi?

Bởi vì bạn cũng có thể có ứng dụng của tôi.

Tôi cũng có thể có ứng dụng của mình.

Vì vậy không có sự độc đáo.

Vì vậy điều bạn phải làm là bạn có

để đổi tên hình ảnh của bạn, địa phương của bạn

hình ảnh đến, có cùng tên

đó là tên kho lưu trữ của bạn.

Vì vậy, có hai cách để làm điều đó.

Thứ nhất, điều tôi có thể làm là

Tôi chỉ có thể xây dựng cái này

hình ảnh có tên này.

Vậy điều đó có nghĩa là lần này tôi chỉ

sẽ nói Docker, xây dựng dấu gạch nối t.

Hãy chắc chắn để sử dụng tên này.

Và sau đó tôi có thể nói

bạn gọi dấu chấm là gì.

Phải?

Vì thế đây là một cái tên độc đáo.

Không ai có thể, không ai khác

có thể có tên này phải không?

Vì vậy, một cách là bạn phải xây dựng

hình ảnh của bạn có cùng tên.

Và sau đó một khi nó được thực hiện

bạn chỉ có thể nói, hãy

chỉ cần đăng nhập Docker trước.

Vì thế đừng quên về

đăng nhập Docker.

Vì vậy Docker, hãy đăng nhập, nhập,

cho phép xác thực như vậy.

Vậy thực ra tôi có một tài khoản aws

đã đăng nhập rồi.

Vì vậy tôi nghĩ nó đã được ghi lại

bằng tài khoản đó.

Hãy để tôi kiểm tra.

Vâng, vậy là nó đã được đăng nhập rồi.

Vì vậy, bây giờ tôi chỉ có thể nói Docker push

và tên hình ảnh này nhập vào.

Vậy điều này sẽ làm là

điều này sẽ đẩy hình ảnh này

vào hub.docker.com để chúng ta có

phải đợi một lúc vì

hình ảnh này đang được đẩy lên.

Vì vậy, Docker đẩy

tên gì cũng được.

Được rồi, bạn có thể thấy

nó đang bị đẩy.

Tuyệt vời.

Và nếu bây giờ tôi đến đây và tôi chỉ làm

làm mới, những gì bạn sẽ nhận thấy là

này, tôi vừa đăng một hình ảnh mới.

Bạn có thể thấy điều này?

Bạn có thể thấy điều này?

Và bây giờ bất cứ ai trên toàn cầu đều có thể

docker chạy Dấu gạch nối nó piushkar

ứng dụng nút gạch nối dev và nó

sẽ tự động kéo từ đây.

Tôi sẽ cho bạn thấy điều đó sau một thời gian.

Hãy nói trên địa phương của tôi

Tôi có hình ảnh Docker.

Hãy nói Xem, bạn có thể thấy

Tôi có rất nhiều hình ảnh.

Hãy xóa tất cả các hình ảnh.

Bạn có thể thấy rằng tôi không có

hình ảnh và không có container.

Hãy xem tôi có thể làm gì.

Tôi có thể nói Docker chạy

nhà phát triển P piyushgurk tương tác.

Được rồi, gạch nối piyushgirk dev

tên là gì?

Ứng dụng nút.

Đúng vậy, nó sẽ nói rằng này, tôi

không thể tìm thấy hình ảnh này tại địa phương.

Nó sẽ lấy từ Docker

IO vì nó đã được xuất bản ngay bây giờ.

Thấy rồi không tìm được

đang kéo và kéo.

Và bây giờ máy chủ Docker của tôi đang chạy.

Vì vậy, thực sự ở cuối khóa học này

Tôi sẽ xóa kho lưu trữ này.

Nhưng bạn có thể thử xuất bản

hình ảnh riêng và trong Discord

máy chủ gửi cho tôi liên kết của bạn.

Vậy là bạn đã có Docker trong Discord

máy chủ bạn có kênh Docker.

Bạn có thể chia sẻ liên kết của bạn mà

này các bạn, tôi vừa

đã xuất bản hình ảnh Docker của riêng tôi.

Được rồi, vậy nên bất cứ ai ở xung quanh

thế giới có thể sử dụng nó.

Vì vậy bây giờ nếu tôi thực hiện điều khiển C, bạn có thể

thấy đấy, hệ thống của tôi có một

máy, nhấp vào một hình ảnh ở đây.

Bạn có thể thấy tất cả

các lệnh mà nó thực hiện.

Bạn có thể thấy có

không có lỗ hổng.

Tất cả các gói mà nó đã sử dụng

và đây là những hình ảnh gì,

những hình ảnh cơ bản chúng tôi đã sử dụng.

Vì vậy, điều đó cũng đang đến.

Rất tuyệt phải không?

Khá tuyệt.

Vì vậy, đây là một cách mà bạn tạo ra

hình ảnh của bạn trong tên này.

Cách thứ hai là gì?

Vì vậy, cách thứ hai là bạn tạo

hình ảnh giống như Docker Build Hyphen T của tôi

app, điều này không có ý nghĩa gì.

Và hãy cùng xây dựng hình ảnh này.

Không xây dựng.

Xin lỗi, lỗi của tôi.

Docker Build dấu gạch nối cho ứng dụng của tôi.

Bây giờ tôi có thể xuất bản cái này không, hình ảnh của tôi?

Hãy.

Hãy thử làm điều đó.

Vì vậy, nếu tôi xuất bản Docker

hình ảnh của tôi, bạn không thể làm điều đó ứng dụng của tôi.

Đúng, xin lỗi, ý tôi là

để nói Docker đẩy.

Vì vậy, tôi cần thực hiện đẩy Docker.

Và, đây là gì?

Ứng dụng của tôi.

Vì vậy, những gì bạn sẽ thấy là

bạn sẽ gặp lỗi

điều đó, không, điều này không được phép.

Bạn không thể đẩy thứ này.

Vì thế bạn sẽ thấy điều đó,

lỗi đó trong một thời gian.

Vì vậy, nó đang cố gắng đẩy ứng dụng này của tôi.

Nhưng vâng, bạn thấy đấy,

Tôi không thể đẩy được.

Vì vậy điều tôi có thể làm là tôi có thể nói Docker

tag, ghi tên bạn nhé, được thôi,

Lấy tên hình ảnh địa phương của bạn

là ứng dụng của tôi và gắn thẻ cho nó.

Vậy thẻ đó có thể là thứ này,

được rồi, chính xác là điều này.

Vì vậy bây giờ những gì bạn đã làm là của bạn

hình ảnh cục bộ, chưa

được đẩy, nó có một thẻ có tên này.

Bây giờ bạn chỉ có thể nói Docker xuất bản.

Quán rượu Docker.

Xin lỗi, Docker đẩy.

Được rồi, bạn chỉ cần nói Docker push

và những thứ này.

Vì vậy, điều này về cơ bản có nghĩa là

bên trong, được rồi, bên trong, cái này

đang đề cập đến điều này.

Vì vậy, đây là một cách để làm điều đó.

Vì vậy, bạn chỉ có thể nói như thẻ Docker,

dù tên địa phương của bạn là gì thì

tên chính thức của bạn, và sau đó bạn có thể

làm Docker push, tên chính thức của bạn.

Vì có thẻ nội bộ,

nó sẽ hiểu rằng điều này

về cơ bản có nghĩa là xuất bản cái này

image, mã này trên kho lưu trữ này.

Vì vậy, vâng, tôi đã xuất bản thêm một cuốn nữa.

Bạn có thể thấy điều đó bây giờ

có hai biến thể.

Vâng, xem nào,

vậy là có cái mới nhất rồi.

Bạn thậm chí có thể làm một thẻ.

Vì thế tôi chỉ có thể nói,

bạn biết đấy, xuất bản ở phiên bản V1.

Được rồi, vậy hãy thử xem điều gì sẽ xảy ra.

Tôi cần làm thẻ Docker

và tôi có thể nói ứng dụng của tôi với thứ này

ở V1, và sau đó tôi có thể làm

Docker xuất bản Docker đẩy.

Được rồi, vậy tôi đang cố gắng

để làm một công việc V1.

Vì vậy, về cơ bản nó giống như phiên bản.

Thật tuyệt.

Chúng ta hãy làm mới.

Và bây giờ bạn có V1.

Và nếu tôi tiếp tục với thẻ.

Vì vậy, bạn có V1, bạn có cái này mới nhất.

Vì vậy nếu có ai muốn kéo cái này

điều cụ thể là anh ấy có thể làm Docker

kéo thứ này ở V1, hoặc anh ấy có thể làm

Docker kéo thứ này muộn nhất.

Rất tuyệt vời phải không?

Và bây giờ tôi có thể xóa cái này

kho lưu trữ vì điều này

chỉ là một kho lưu trữ thử nghiệm.

Vì vậy, tôi có thể, tôi phải nhập tên

đó là Ứng dụng nút

và xóa kho lưu trữ mãi mãi.

Vâng, kho lưu trữ của tôi hiện đã biến mất.

Vậy đây là cách bạn có

để đẩy hình ảnh.

Nhưng trước đó, hãy đảm bảo

rằng bạn đã làm điều gì đó

được gọi là đăng nhập docker.

Vì vậy, bạn phải thực hiện đăng nhập docker.

Chỉ khi đó bạn mới có thể xuất bản hình ảnh.

Được rồi.

Khá tuyệt.

Tôi hy vọng bạn biết cách xuất bản

hình ảnh và cách kéo những hình ảnh đó.

Vì vậy, hãy kết thúc chuyện này

video cụ thể và tôi sẽ

hẹn gặp lại bạn ở lần tiếp theo.

Cho đến lúc đó, tạm biệt và chăm sóc nó.