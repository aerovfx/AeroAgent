# 28 -Thiết lập Amazon Elastic Container Register (ECR) để đẩy Docker Images.en US

---

Được rồi, cụ thể là thế này

video, hãy bắt đầu thiết lập ECR.

Bây giờ ecr này là gì?

Vì vậy, ECR về cơ bản là viết tắt của.

Hãy để tôi nói ECR

là viết tắt của Đàn hồi.

Cơ quan đăng ký vùng chứa đàn hồi.

Được rồi.

Về cơ bản nó giống nhau

tương tự như hub.docker.com

tới hub.docker.com

bạn thậm chí có thể sử dụng cái này.

Nhưng về cơ bản đây là của Amazon

phiên bản của hub.docker.com

vậy đó là người đăng ký.

Được quản lý

bởi Dịch vụ web của Amazon.

Phải.

Vậy điều chúng ta sắp làm là,

hãy để tôi cung cấp cho bạn toàn bộ dòng chảy.

Vì vậy chúng ta sẽ tạo một sổ đăng ký

nơi chúng ta sẽ tạo ra

đăng ký trên AWS ECR số một.

Và sau đó điều chúng ta phải làm là chúng ta,

chúng ta có một máy cục bộ, phải không?

Trên máy cục bộ.

Chúng tôi sẽ lấy

mã JS nút này.

Được rồi, hãy lấy cái này đi, node

Mã JS và chúng tôi sẽ chuyển đổi mã này

mã JS của nút thành hình ảnh Docker.

Phải?

Hãy chỉ nói Docker.

Vì vậy, đây là docker.

Vì vậy chúng ta sẽ chuyển đổi cái này

mã JS của nút thành hình ảnh Docker

và sau đó chúng ta sẽ đẩy cái này

Hình ảnh Docker cho AWS ecr này.

Về cơ bản đây là đám mây của chúng tôi,

được rồi, Cloud, đăng ký hình ảnh.

Vì vậy, bạn thậm chí có thể sử dụng Hub Docker.

Nhưng điều đó luôn tốt mà bạn

biết đấy, khi chúng tôi đang thiết lập

nâng cấp toàn bộ cơ sở hạ tầng của chúng ta trong,

bên trong aw, chúng tôi thậm chí có thể lưu trữ

sổ đăng ký của chúng tôi bên trong aw.

Vậy làm thế nào để làm điều đó?

Hãy bắt đầu.

Vì vậy, thật đáng tiếc, bạn phải tìm kiếm

đối với thứ ECR này có tính đàn hồi

Cơ quan đăng ký vùng chứa, được quản lý đầy đủ

Đăng ký vùng chứa Docker.

Phải.

Chia sẻ và triển khai phần mềm container.

Vì vậy về cơ bản nó là

hub.docker.com cho AWS.

Vì vậy, một khi bạn đi vào con số này

có một điều, hãy để tôi chuyển đổi,

bạn biết đấy, khu vực vị trí này

đó là Châu Á Thái Bình Dương,

vì nó gần tôi hơn.

Vì thế bây giờ, ngay bây giờ bạn có thể thấy tôi

ở Mumbai và đây là

Cơ quan đăng ký vùng chứa đàn hồi.

Vì vậy, bạn có thể đi trực tiếp

vào kho như thế này

và bạn chỉ có thể tạo

một kho lưu trữ hoặc thậm chí bạn có thể nhấp vào

trên nút này được tạo.

Vì vậy, về cơ bản nó là điều tương tự.

Vì vậy, các kho lưu trữ, bạn có thể

xem tôi không có kho lưu trữ.

Hãy tạo một kho lưu trữ.

Bây giờ tên là gì

kho lưu trữ của bạn?

Phải.

Bạn muốn đặt tên gì?

Vì vậy đây là tên người dùng của tôi,

tên người dùng này được tạo như thế nào,

về cơ bản đây là số tài khoản của tôi.

Bạn có thể thấy điều đó không?

Đây là số tài khoản của tôi

Thế thì cái này giống như DKR, ECR,

AP South1, khu vực tôi đang ở

in và Amazon AWS dot com.

Hãy tạo một ứng dụng nút.

Hoặc tôi chỉ có thể nói rằng điều này

là phụ trợ của tôi, phải không?

Vậy đây là tên

của kho lưu trữ.

Nên tôi đặt tên nó như thế này

Vì vậy, điều này có thể thay đổi.

Không sao đâu.

Mọi thứ đều có thể giống nhau

và chỉ cần tạo.

Vì vậy, bạn có thể thấy rằng những gì tôi

đã làm là tôi đã làm

một kho lưu trữ riêng tư, phải không?

Tôi nghĩ đây là chuyện riêng tư.

Chúng ta đã chọn ở đâu chưa?

Vâng, đây là kho lưu trữ riêng tư.

Vì vậy, bạn có thể thấy rằng chúng tôi có

đã tạo một kho lưu trữ riêng.

Đây là URL của nó

kho lưu trữ khi nó được tạo ra.

Và bạn có thể thấy không có gì

ngay bây giờ điều chúng ta phải làm là để

tôi chỉ, bạn biết đấy, bật Docker của tôi lên

động cơ và chúng tôi phải xây dựng cái này và

chúng ta phải xây dựng cái này đặc biệt

hình ảnh.

Vậy chúng ta hãy làm một điều thôi,

hãy xây dựng nó và vâng,

Tôi có một vài thứ.

Hãy để tôi xóa nó đi.

Vâng, có một điều là tôi muốn

để thay đổi vài thứ

Thứ nhất, cổng này, tôi muốn

chỉ cần nói rằng này, đó

là biến ENV, biến ENV

đó là cổng theo mặc định.

Hãy tăng lên 8.000, phải không?

Và chúng ta cần hiển thị cổng 8.000,

bạn biết, bạn biết những thứ đó, phải không?

Điều này có nghĩa là gì và tại sao chúng tôi

làm điều này bởi vì nó tiện dụng

cho người dùng sử dụng nó.

Vì vậy, đây là ứng dụng đơn giản

và đây là môi trường

các biến mà chúng tôi sẽ cung cấp.

Mặc định là vậy đó bạn

biết đấy, theo mặc định nó sẽ là 8.000.

Npm start là lệnh.

Và vâng, đây là một cái đẹp

điều tuyệt vời phải không?

Đây là một điều khá thú vị.

Vì vậy bây giờ chúng ta hãy xây dựng cái này

hình ảnh cụ thể.

Vậy Docker, được rồi, docker build,

dấu gạch nối, T, phần phụ trợ, bạn có thể

đặt tên cho nó là bất cứ điều gì và sau đó bạn

chỉ có thể nhấn dấu chấm và nhập.

Vậy cái này sẽ làm gì, đây là

sẽ xây dựng hình ảnh Docker của bạn.

Bây giờ hình ảnh Docker của tôi đã được xây dựng.

Vì vậy, chỉ để thấy điều này, tôi có thể

nói hình ảnh Docker, hình ảnh hình ảnh.

Và bạn có thể thấy rằng tôi có

hình ảnh phụ trợ này đã sẵn sàng.

Bây giờ điều chúng ta phải làm là chúng ta có

để đẩy hình ảnh cụ thể này.

Làm thế nào tôi có thể làm điều đó?

Bạn có nhớ điều đó không?

chúng ta phải nhắm mục tiêu.

Bạn có nhớ tôi đã chỉ cho bạn không.

Vì vậy, bạn có thể chỉ cần nhấp vào

trên lệnh đẩy chế độ xem này.

Vì vậy, bây giờ tôi phải đăng nhập trước.

Bây giờ hãy hiểu điều này tại địa phương.

Tôi đã cài đặt công cụ Docker này,

được rồi, công cụ Docker đã được cài đặt.

Tôi phải đăng nhập vào đây

Công cụ Docker để cấp cho nó quyền truy cập

vào tài khoản AWS này.

Làm thế nào tôi có thể làm điều đó?

Tôi phải sao chép lệnh này.

AWS ecr, lấy mật khẩu đăng nhập

khu vực đăng nhập Docker này.

Vì vậy, tôi chỉ, tôi chỉ đang làm docker

đăng nhập bằng thông tin đăng nhập này.

Vì vậy, chỉ cần làm và nhập.

Vì vậy bởi vì bạn có của bạn

Đã cấu hình AWS CLI, nó sẽ

chỉ cần nói đăng nhập thành công.

Phải?

Phải.

Vì vậy, bạn có thể thấy đăng nhập thành công.

Tuyệt vời.

Bây giờ bạn phải làm gì, bạn

đã xây dựng nó rồi, vậy là xong

về cơ bản là giúp đỡ bạn.

Bây giờ bạn phải nói thẻ docker

hình ảnh phụ trợ của bạn sẽ được gắn thẻ

với URL kho lưu trữ này.

Phải?

Vì vậy hãy sao chép lệnh

và chỉ cần dán nó ở đây.

Thế là xong.

Bây giờ bạn chỉ cần nhấn Docker Push

và của bạn, tên hình ảnh của bạn và nhập.

Vì vậy, về cơ bản điều này đang diễn ra

để đẩy hình ảnh cụ thể này

đến cái ecr này.

Vì vậy chúng ta phải chờ một thời gian.

Hiểu rồi.

Đẹp.

Bây giờ nếu tôi quay lại đây, hãy đóng lại

nó và làm mới, bạn có thể thấy

đó, vâng, tôi có một hình ảnh.

Đúng rồi, bạn có thể thấy tôi có một hình ảnh,

ngày khi nó được đẩy kích thước.

Và tôi chỉ có thể sao chép uri.

Có một bản tóm tắt.

Vậy bây giờ các bạn, hiệu quả nhé

những gì bạn đã làm là bạn

đã thực hiện đăng ký ECR.

Được rồi.

Và đây là liên kết

vào sổ đăng ký đó.

Vì vậy, tôi chỉ muốn dán

nó dưới dạng một URL chứ không phải dưới dạng URL.

Nếu tôi có thể dán nó như thế này.

Được rồi.

Dù sao, tôi không thể dán nó.

Bạn biết đấy, hãy sao chép phần này.

Ừ, được rồi.

Nó sẽ coi nó như một URL.

Đây là URL của chúng tôi nơi chúng tôi

bạn biết đấy, đã đẩy mã của chúng tôi.

Vậy xin chúc mừng các bạn.

Bạn đã hoàn tất thiết lập ECR của mình.

Được rồi.

Cơ quan đăng ký vùng chứa đàn hồi.

Về cơ bản một sổ đăng ký cho

lưu trữ hình ảnh Docker.

Trong video tiếp theo,

hãy thiết lập cụm

và thiết lập định nghĩa nhiệm vụ.

Vì vậy, vâng, hãy gặp bạn

trong phần tiếp theo.