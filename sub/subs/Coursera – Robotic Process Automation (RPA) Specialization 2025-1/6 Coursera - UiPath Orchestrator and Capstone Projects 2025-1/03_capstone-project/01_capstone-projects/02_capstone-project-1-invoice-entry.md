# 02 capstone-dự án-1-hóa đơn

---

Trong video trước,

bạn đã được giới thiệu với

những dự án đỉnh cao cho

chuyên ngành RPA.

Trong video này, bạn sẽ

hiểu yêu cầu của

dự án capstone đầu tiên

gọi là Nhập hóa đơn.

Trong dự án này, bạn

được mong đợi;

sử dụng Excel và tự động hóa email,

sử dụng trích xuất PDF

để trích xuất dữ liệu,

và tải lên dữ liệu trong một ứng dụng

và tạo ra các báo cáo.

Hãy bắt đầu. bạn là

dự kiến xây dựng một dự án

tự động hóa việc nhập hóa đơn

quá trình trong một tổ chức.

Hoá đơn là một

tài liệu được tạo bởi

người bán khi nhận được

của một đơn đặt hàng

từ người mua.

Nó chứa các chi tiết

về sản phẩm hoặc

dịch vụ, giá cả, số lượng,

giá trị, tình trạng sản phẩm,

tên các bên,

địa chỉ thanh toán và

các điều khoản và điều kiện.

Tổ chức

nhận hóa đơn

trên email của nó dưới dạng tệp đính kèm.

Nó muốn tự động hóa

quá trình của

tải xuống và đọc

hóa đơn và tải lên

dữ liệu hoá đơn vào

một ứng dụng ERP.

Cuối cùng, của chúng tôi

các báo cáo nên được

được tạo trong tệp Excel

chứa số hóa đơn,

số lượng đã xử lý

các mục và dấu thời gian.

Có một số hành động

dự án nên

đảm nhận việc thực hiện.

Chúng ta sẽ hiểu tất cả

của những hành động này trong

chi tiết để bạn có thể tạo

dự án của riêng bạn.

Trước khi bắt đầu với

việc tạo ra dự án,

bạn nên đảm bảo rằng bạn

sẵn sàng với dự án

điều kiện tiên quyết.

Có năm điều kiện tiên quyết

cho dự án.

Điều kiện tiên quyết đầu tiên đó là

máy tính của bạn nên có

Studio UiPath và Microsoft

Đã cài đặt văn phòng.

Bạn có thể tìm thấy phần cứng đó và

yêu cầu phần mềm

cho việc cài đặt

của studio UiPath trên

Cổng thông tin tài liệu UiPath.

Điều kiện tiên quyết thứ hai là

studio nên có tất cả

gói cần thiết.

Những gói này là;

Hoạt động tự động hóa giao diện người dùng UiPath,

Hoạt động của hệ thống UiPath,

Hoạt động UiPath Excel,

Hoạt động thư UiPath,

và các hoạt động UiPath PDF.

Trong studio, bạn có thể xem

các gói được cài đặt bởi

nhấp vào gói quản lý

tùy chọn trên ribbon thiết kế.

Bạn có thể tìm kiếm và

cài đặt gói mới từ

tab Tất cả các gói của

cửa sổ quản lý gói.

Điều kiện tiên quyết thứ ba

là bạn nên có

ứng dụng ERP trên

máy tính của bạn để

tải lên dữ liệu hóa đơn.

Bạn có thể tìm thấy phần mềm

cùng với khóa học này.

Vui lòng tải hóa đơn xuống

tập tin entry.exe và lưu lại

nó trên máy tính của bạn.

Nó không yêu cầu cài đặt

hoặc nâng cao đặc quyền hệ thống.

Bạn có thể nhấp đúp vào nó để chạy.

Hãy để chúng tôi hiểu

giao diện của ứng dụng.

Như bạn có thể thấy trên

giao diện ứng dụng,

có bốn phần

dữ liệu ở đâu

cần được lấp đầy,

trong phần công ty,

các chi tiết của

người bán nên được lấp đầy.

Nó chứa bảy trường;

tên, địa chỉ, thành phố,

trạng thái, mã pin,

số liên lạc, và tn.

Trong phần khách hàng,

các chi tiết của

người mua nên được lấp đầy.

Nó chứa bảy trường;

tên khách hàng, địa chỉ, thành phố,

trạng thái, mã pin,

số liên lạc, và tn.

Ở phần chi tiết hóa đơn,

số hóa đơn và hóa đơn

dữ liệu cần được điền.

Trong phần mục, chi tiết

về sản phẩm hoặc dịch vụ,

số lượng và giá cả

nên được lấp đầy.

Cuối cùng, tổng phụ, GST,

và tổng số trường

nên được lấp đầy.

Sau khi dữ liệu được chèn

trong mọi lĩnh vực,

nút gửi

nên bấm vào để

xác nhận và tải lên

việc nhập dữ liệu.

Điều kiện tiên quyết thứ tư là

rằng bạn nên có Outlook

được cấu hình trên máy của bạn

với một địa chỉ email.

Điều kiện tiên quyết thứ năm

là bạn nên có

một vài hoá đơn như

tệp đính kèm email.

Dữ liệu bạn sẽ nhập vào

ứng dụng ERP phải

lấy từ các hóa đơn này.

Bạn có thể tìm thấy một số

hóa đơn mẫu

cùng với khóa học này.

Tải xuống các tập tin và lưu

chúng trên máy tính của bạn.

Gửi các tập tin này dưới dạng

tách riêng các tệp đính kèm email

cấu hình của bạn

Địa chỉ email Outlook.

Bạn nên đảm bảo

rằng các email là

chưa đọc trước khi bắt đầu

thực hiện dự án.

Chúng ta hãy nhìn vào một

của các hóa đơn.

Như bạn có thể thấy,

hóa đơn chứa

tất cả các mục mà bạn cần

điền vào ứng dụng ERP.

Nó chứa thông tin chi tiết về

người bán và người mua.

Nó cũng có một cái bàn

chứa các chi tiết

của các mặt hàng đã mua

và tổng phụ,

GST và tổng cộng.

Bây giờ hãy hiểu

những hành động

rằng dự án nên

đảm nhận việc thực hiện.

Hành động đầu tiên đó

dự án nên

lấy là để đọc

Email Outlook.

Khi đọc email,

dự án nên

xác định liệu có

là một email chưa đọc.

Nếu có một email chưa đọc,

dự án nên

thay đổi trạng thái

của email để đọc và

kiểm tra xem nó có chứa

tệp đính kèm PDF

của hồ sơ hóa đơn.

Nếu email không chứa

tệp đính kèm PDF

của hồ sơ hóa đơn,

dự án nên đọc lại

email Outlook cần xem

cho email chưa đọc tiếp theo.

Nếu email chứa

đính kèm file hóa đơn,

dự án nên tải nó xuống,

lưu trữ nó trong thư mục dự án,

và đọc lại email Outlook

để tìm email tiếp theo.

Nếu không có email nào chưa đọc

dự án nên kiểm tra

các tập tin hóa đơn hiện có trong

thư mục dự án

để xử lý.

Nếu không có hoá đơn

các tập tin trong thư mục dự án,

dự án nên

ngừng thực hiện.

Nếu có file hóa đơn

trong thư mục dự án,

dự án nên mở

ứng dụng ERP.

Sau đó, dự án

nên trích xuất dữ liệu từ

một tập tin hóa đơn và tải lên

dữ liệu vào ứng dụng.

Sau khi tải dữ liệu lên

của hồ sơ hóa đơn,

dự án nên kiểm tra xem

một tệp báo cáo Excel tồn tại.

Nếu báo cáo Excel

tập tin không tồn tại,

dự án nên

tạo một báo cáo Excel.

Báo cáo nên chứa

số hóa đơn,

số lượng đã xử lý

các mục và dấu thời gian.

Nếu tệp báo cáo Excel tồn tại,

dự án nên cập nhật

số hóa đơn,

số lượng mục được xử lý,

và dấu thời gian trong một hàng mới.

Sau khi tạo hoặc

cập nhật báo cáo,

dự án nên xóa

hóa đơn đã xử lý

tập tin và một lần nữa,

tìm hóa đơn tiếp theo

tập tin trong thư mục.

Nếu thư mục chứa

bất kỳ tập tin hóa đơn nào,

dự án nên tiếp tục

để trích xuất dữ liệu của nó.

Nếu thư mục không

chứa bất kỳ tệp hóa đơn nào,

dự án nên đóng cửa

ứng dụng ERP

và ngừng thực hiện.

Trong video tiếp theo,

yêu cầu để

tảng đá thứ hai

dự án được gọi là

Xu hướng giá cổ phiếu

Sự so sánh được giải thích

Bạn được mong đợi sẽ

hiểu các yêu cầu

cẩn thận và xây dựng

dự án của riêng bạn.

Đó là tất cả cho video này.

Cảm ơn đã xem.