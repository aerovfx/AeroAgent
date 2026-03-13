# 07 trình diễn-excel-tự động hóa

---

Xin chào và chào mừng đến với

cuộc biểu tình này trên

đọc và viết các

dữ liệu trong file Excel.

Trong video này, bạn sẽ học cách

tạo ra một quy trình công việc so sánh

hai cột đầu tiên

của Excel và hiển thị

kết quả cột thứ ba

sử dụng các hoạt động Excel.

Vậy hãy bắt đầu.

Bắt đầu bằng việc tạo

một tập tin Excel.

Mở một tệp Excel mới và

tạo hai cột A và B.

Nhập 10 số ngẫu nhiên giữa

1 và 100 trong mỗi cột.

Lưu và đóng tập tin.

Đi tới UiPath Studio,

tìm kiếm một Excel

Hoạt động phạm vi ứng dụng,

và kéo và thả vào

bảng thiết kế.

Đổi tên trình tự thành

Tự động hóa Excel và thêm

một chú thích cho nó.

Đổi tên Excel

Hoạt động phạm vi ứng dụng

dưới dạng so sánh.xlsx.

Bấm vào biểu tượng thư mục và

chọn tệp Excel đã được

vừa tạo ra. Nhấp vào "Mở".

Tìm kiếm hoạt động Phạm vi Đọc

trong danh mục Excel trong

bảng Hoạt động

và kéo và thả nó vào

vùng chứa Do của Excel

Hoạt động Phạm vi ứng dụng.

Đổi tên nó. Điều hướng đến

bảng Thuộc tính của

hoạt động Phạm vi Đọc.

Trong thuộc tính DataTable,

nhấn "Điều khiển" cộng

"K" để tạo mới

biến và tên

nó dưới dạng dt_dummyData.

Bây giờ, hãy tìm kiếm Thêm

Hoạt động của Cột Dữ liệu trong

bảng Hoạt động

và kéo và thả nó

dưới Phạm vi Đọc

hoạt động và đổi tên nó.

Chuyển đến bảng Thuộc tính.

Trong thuộc tính ColumnName,

nhập so sánh

trong dấu ngoặc kép

và nhập

biến dt_dummyData

trong thuộc tính DataTable.

Tìm kiếm cho mỗi hàng

trong hoạt động Bảng dữ liệu trong

bảng Hoạt động

và kéo và thả nó

bên dưới Cột Thêm dữ liệu

hoạt động và đổi tên nó.

Trong hộp văn bản biểu thức VB,

nhập biến dt_dummyData.

Tìm kiếm hoạt động nếu

trong bảng Hoạt động.

Kéo và thả nó vào

phần cơ thể

của Cho Mỗi Hàng trong

Hoạt động của bảng dữ liệu

và đổi tên nó.

Trong hộp điều kiện,

nhập CInt theo sau là

CurrentRow 0 trong ngoặc đơn.

Đảm bảo bổ sung

dấu ngoặc quanh số 0,

sau đó là ký hiệu lớn hơn.

Sau đó nhập CInt

theo sau là CurrentRow 1.

Đảm bảo bổ sung

dấu ngoặc quanh một.

Ở đây hàm CInt chuyển đổi

giá trị chuỗi thành một số nguyên.

Kiểm tra toàn bộ điều kiện

liệu các giá trị trong

cột đầu tiên là

lớn hơn

thứ hai trong tệp Excel.

Tìm kiếm hoạt động Phân công

và kéo và thả nó vào

phần sau đó của

nếu hoạt động. Đổi tên nó.

Trong hộp văn bản đầu tiên,

nhập CurrentRow rồi

hai trong ngoặc đơn.

Trong hộp văn bản bên cạnh,

nhập văn bản Lớn hơn

trong dấu ngoặc kép.

Bấm vào "Hiển thị khác" để xem

phần khác của

hoạt động nếu.

Kéo và thả cái khác

nếu hoạt động trong

phần khác của

hoạt động if đầu tiên.

Đổi tên nó. Trong hộp điều kiện,

nhập CInt theo sau là

CurrentRow 0 trong ngoặc đơn.

Đảm bảo bổ sung

dấu ngoặc quanh số 0,

sau đó nhập ký hiệu nhỏ hơn.

Sau đó nhập CInt

tiếp theo là Hàng hiện tại 1.

Đảm bảo bổ sung

dấu ngoặc quanh một.

Ở đây hàm CInt chuyển đổi

giá trị chuỗi thành một số nguyên,

và toàn bộ điều kiện

kiểm tra xem các giá trị trong

cột đầu tiên là

nhỏ hơn

thứ hai trong tệp Excel.

Tìm kiếm một bài tập

hoạt động và kéo và thả

nó vào phần sau của

nếu hoạt động. Đổi tên nó.

Trong hộp văn bản đầu tiên,

nhập CurrentRow rồi

hai dấu ngoặc đơn bên trong.

Ở ô bên cạnh,

nhập văn bản Ít hơn

trong dấu ngoặc kép.

Bấm vào "Hiển thị khác" để xem

phần khác của

hoạt động nếu.

Kéo và thả và

Chỉ định hoạt động trong

phần khác của nếu

hoạt động và đổi tên nó.

Trong hộp văn bản đầu tiên,

nhập CurrentRow rồi

hai dấu ngoặc đơn bên trong,

và trong hộp bên cạnh,

nhập văn bản Bằng

trong dấu ngoặc kép.

Bây giờ, hãy tìm kiếm một

Hoạt động viết phạm vi

trong danh mục Excel trong

các hoạt động

bảng điều khiển và kéo và

thả nó bên dưới For Each

Hàng trong hoạt động Bảng dữ liệu.

Đổi tên nó. trong

hộp văn bản đầu tiên,

nhập Sheet2 trong dấu ngoặc kép.

Trong hộp văn bản thứ hai,

xóa biểu thức hiện có

và nhập dấu ngoặc kép.

Trong hộp văn bản thứ ba,

nhập biến dt_dummyData.

Điều hướng đến

Bảng thuộc tính của

hoạt động Phạm vi Viết và

kiểm tra tùy chọn AddHeaders.

Hoạt động này sẽ chèn

kết quả trong một tờ mới

được gọi là Sheet2 trong

cùng một tệp Excel.

Lưu dự án và chạy nó.

Bây giờ hãy mở tệp Excel

để kiểm tra kết quả.

Mỗi kết quả hàng được lưu trữ trong

cột thứ ba trong một trang tính mới.

Nó được khuyến khích để

tạo quy trình làm việc như

đã chứng minh và

hãy thử hoạt động này.

Cảm ơn bạn đã xem.