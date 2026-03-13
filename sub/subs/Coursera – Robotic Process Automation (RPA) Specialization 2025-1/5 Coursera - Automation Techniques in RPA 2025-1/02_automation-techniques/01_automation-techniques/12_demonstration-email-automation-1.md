# 12 trình diễn-email-tự động hóa-1

---

Xin chào và chào mừng đến với điều này

trình diễn cách sử dụng

Nhận tin nhắn thư IMAP

Hoạt động trong Studio.

Trong video này, bạn

sẽ học cách tạo ra

một quy trình làm việc mở ra

gửi email qua IMAP,

lấy năm đầu tiên

email chưa đọc và

lưu trữ chúng trong CSV

tập tin bằng Gmail.

Hãy bắt đầu. Tìm kiếm

một hoạt động Xây dựng DataTable trong

bảng Hoạt động và

kéo và thả nó vào

bảng thiết kế.

Đổi tên trình tự

tự động hóa email

và thêm chú thích vào nó.

Sau đó đổi tên Build Data

Hoạt động của bảng dưới dạng dt_GetMails.

Bấm vào nút Bảng dữ liệu

trong bản dựng

Hoạt động của bảng dữ liệu.

Trong cửa sổ bật lên,

tạo ba cột

với tiêu đề

làm Chủ ngữ với

kiểu dữ liệu là Chuỗi,

Từ với kiểu dữ liệu là Chuỗi,

và cơ thể với

kiểu dữ liệu dưới dạng Chuỗi.

Nhấp vào "Được". đi đến

bảng Thuộc tính của

hoạt động này và trong

Thuộc tính DataTable,

nhấn "Control plus K" để tạo

một biến mới

có tên là dt_GetMails.

Tìm kiếm Nhận IMAP

Hoạt động của Thư Tin nhắn trong

các hoạt động

bảng điều khiển và kéo và

thả nó xuống dưới

Xây dựng bảng dữ liệu

hoạt động và đổi tên nó.

Đi tới Thuộc tính của nó

bảng điều khiển và trong

thư mục thư

thuộc tính, hãy nhập Hộp thư đến.

Trong thuộc tính Cảng, nhập 993.

Bấm vào thuộc tính máy chủ

biểu tượng dấu chấm lửng để mở

Trình soạn thảo biểu thức và

nhập "imap.gmail.com".

Nhấp vào "Được". Bấm vào Email

biểu tượng dấu ba chấm thuộc tính

để mở Trình soạn thảo biểu thức

và nhập email

địa chỉ trong dấu ngoặc kép.

Nhấp vào "Được". nhấp chuột

biểu tượng dấu ba chấm của

thuộc tính Mật khẩu để mở

Trình soạn thảo biểu thức và

nhập mật khẩu

trong dấu ngoặc kép.

Đảm bảo rằng chỉ có thư chưa đọc

Thuộc tính tin nhắn không được chọn.

Nó sẽ lấy tất cả các email

bất kể trạng thái đọc của chúng.

Trong thuộc tính Top, nhập năm,

trong thuộc tính Tin nhắn,

nhấn "Control plus K" để tạo

một biến mới

được đặt tên là Tin nhắn mới.

Nếu bạn đang sử dụng Gmail của mình

tên người dùng và mật khẩu,

cho phép tài khoản Google của bạn

các ứng dụng và thiết bị kém an toàn hơn.

Điều này có thể được sử dụng bằng cách truy cập

tab Bảo mật bên dưới

trang tài khoản Google.

Bạn có thể tạm dừng việc này

video ở đây để thiết lập

tài khoản Google của bạn và quay lại

ở đây để tiếp tục hơn nữa.

Tìm kiếm hoạt động ForEach trong

bảng Hoạt động và

kéo và thả nó bên dưới Get

Hoạt động của Tin nhắn Thư IMAP.

Điều hướng đến

Bảng thuộc tính của

hoạt động ForEach và nhấp vào

đối số kiểu

thả xuống thuộc tính

và chọn Duyệt tìm loại.

Trong cửa sổ bật lên,

duyệt tìm loại MailMessage.

Chọn MailMessage trong

Danh mục System.Net.Mail.

Nhấp vào "Được". Bây giờ đổi tên

hoạt động ForEach.

Thay thế mục văn bản từ

hộp văn bản đầu tiên có thư.

Trong hộp văn bản bên cạnh,

nhập biến newMessages.

Tìm kiếm hoạt động Phân công

trong bảng Hoạt động và

kéo và thả nó vào

phần cơ thể của

hoạt động ForEach, hãy đổi tên nó.

Trong hộp văn bản đầu tiên,

nhấn "Control plus K" để

tạo một biến mới

được đặt tên là Chủ đề.

Ở ô bên cạnh,

nhập biểu thức

thư.Chủ đề.

Kéo và thả cái khác

Chỉ định hoạt động bên dưới

sự phân công trước đó

hoạt động và đổi tên nó.

Trong hộp văn bản đầu tiên,

nhấn Control cộng K để tạo

một biến mới có tên From.

Ở ô bên cạnh,

nhập biểu thức

thư.From.Tostring.

Kéo và thả cái khác

Chỉ định hoạt động bên dưới

sự phân công trước đó

hoạt động và đổi tên nó.

Trong hộp văn bản đầu tiên,

nhấn Control cộng K để tạo

một biến mới có tên là Body.

Ở ô bên cạnh,

nhập biểu thức

thư.Body.ToString.

Bây giờ hãy tìm kiếm Thêm

Hoạt động hàng dữ liệu trong

các hoạt động

bảng điều khiển và kéo và

thả nó xuống dưới phần thứ ba

hoạt động và đổi tên nó.

Điều hướng đến Thuộc tính của nó

bảng điều khiển và nhấp chuột

biểu tượng dấu ba chấm của

thuộc tính ArrayRow để

mở Trình soạn thảo biểu thức.

Nhập biểu thức

{Chủ đề,Từ,Nội dung}.

Nhấp vào "Được". trong

Thuộc tính DataTable,

nhập biến dt_GetMails.

Tìm kiếm hoạt động Viết CSV,

và kéo và thả nó bên dưới

hoạt động ForEach

và đổi tên nó.

Trong hộp văn bản đầu tiên,

nhập tên tệp CSV mới có tên

"FreshMails.csv" và trong

hộp văn bản thứ hai,

nhập bảng dữ liệu

biến dt_GetMails.

Xin lưu ý rằng

Tệp CSV sẽ được

được tạo tự động

trong thư mục Dự án.

Lưu dự án và chạy nó.

Bây giờ, hãy mở CSV

tập tin FreshMails.csv.

Tất cả các email được lưu trữ trong

các cột riêng biệt dưới Chủ đề,

Từ, và cơ thể.

Nó được khuyến khích để

tạo quy trình làm việc

như đã chứng minh và

hãy thử hoạt động này.

Cảm ơn bạn đã xem.