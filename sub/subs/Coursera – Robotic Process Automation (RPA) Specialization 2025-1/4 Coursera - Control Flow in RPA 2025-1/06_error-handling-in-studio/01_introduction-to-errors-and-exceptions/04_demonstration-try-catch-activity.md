# 04 hoạt động trình diễn-thử-bắt

---

[ÂM NHẠC]

Xin chào và chào mừng đến từng bước

bản demo từng bước về cách sử dụng tính năng thử bắt

hoạt động giải quyết một vấn đề trong

quy trình làm việc hiển thị lỗi

trong khi đọc dữ liệu từ tệp Excel.

Chúng tôi sẽ chứng minh điều này bằng cách

tạo ra một quy trình làm việc

sẽ đọc dữ liệu từ một tập tin Excel.

Tệp Excel sẽ được mở trong khi

chạy quy trình làm việc vì mỗi lần chúng tôi

để tập tin mở nó

sẽ ném một ngoại lệ.

Chúng tôi sẽ bắt ngoại lệ và

khắc phục nó bằng cách sử dụng hoạt động thử bắt.

Chúng tôi sẽ sử dụng hoạt động thử bắt

để đóng tệp Excel và

sau đó thử đọc tập tin.

Tìm kiếm một hoạt động theo trình tự trong

bảng điều khiển hoạt động và kéo và

thả nó vào bảng thiết kế.

Đổi tên hoạt động thành đọc Excel

dữ liệu và thêm chú thích vào nó.

Tìm kiếm hoạt động ở phạm vi sậy ở

bảng điều khiển hoạt động và kéo và

thả nó vào hoạt động theo trình tự,

đổi tên thành phạm vi đọc, đọc dữ liệu Excel.

Bấm vào biểu tượng thư mục để

mở tệp Explorer và

chọn tệp Excel từ

dữ liệu nào sẽ được đọc.

Đây là tên của file Excel

chúng tôi đang sử dụng là dữ liệu nhân viên.XLSX.

Làm trống hộp văn bản phạm vi để

rằng toàn bộ bảng Excel có thể được đọc.

Điều hướng đến bảng thuộc tính và

trong thuộc tính bảng dữ liệu

nhấn Ctrl + K trên bàn phím của bạn

để tạo một biến mới và

nhập nhân viên gạch dưới DT

data làm tên biến.

Đây là biến chứa dữ liệu

từ file Excel sẽ được lưu trữ.

Bây giờ hãy mở tệp Excel.

Bây giờ trong studio đường dẫn của tôi, hãy nhấp vào Lưu

để lưu dự án và chạy nó.

Bạn có thể thấy thời gian chạy đó

lỗi thực thi được hiển thị.

Nó nói rằng quá trình này không thể truy cập vào

tập tin vì một quá trình khác đang sử dụng nó.

Điều đó có nghĩa là tệp Excel

không nên mở trong khi

chạy quy trình làm việc,

nhấn OK để đóng cửa sổ bật lên này.

Tìm kiếm hoạt động thử bắt

trong bảng hoạt động và

kéo và thả nó dưới phạm vi đọc

hoạt động, đổi tên nó thành tệp Excel đóng.

Kéo thả hoạt động phạm vi đọc vào

phần Tri của hoạt động thử bắt.

Bấm vào thêm sản phẩm đánh bắt mới

trong phần đánh bắt và

chọn hệ thống .io.io

ngoại lệ từ trình đơn thả xuống

thực đơn đại diện cho

ngoại lệ hoạt động không hợp lệ.

Tìm kiếm hoạt động viết dòng

trong bảng hoạt động và

kéo và thả nó vào phần bắt

phần của hoạt động thử bắt.

Đổi tên nó để hiển thị lỗi,

điều hướng đến bảng thuộc tính của nó và

bấm vào biểu tượng dấu chấm lửng của văn bản

thuộc tính để mở trình soạn thảo biểu thức.

Nhập biểu thức

ngoại lệ.message.tostring+"at'+ngoại lệ-

.source.tostring.

Biểu thức này sẽ in các lỗi

gặp phải trong quá trình

bảng đầu ra.

Tìm kiếm hoạt động nhấp chuột

trong bảng hoạt động và

kéo và

thả nó xuống bên dưới hoạt động dòng ghi.

Đổi tên nó thành tệp Excel đóng, nhấp vào

các yếu tố chỉ ra trên liên kết màn hình và

chỉ ra nút đóng ở trên cùng

góc bên phải của cửa sổ file Excel.

Hoạt động này sẽ kết thúc

tệp Excel nếu nó mở,

nhấp vào nút hamburger và chọn

chỉnh sửa bộ chọn từ trình đơn thả xuống.

Trong cửa sổ soạn thảo bộ chọn,

bỏ chọn hộp tiêu đề và

nhấp vào nút xác nhận để đảm bảo

rằng bộ chọn hợp lệ và nhấp vào OK.

Bây giờ hãy sử dụng để viết dòng

các hoạt động để chỉ ra sự bắt đầu này và

kết thúc quá trình đọc file Excel.

Tìm kiếm hoạt động viết dòng

trong bảng hoạt động và kéo và

thả nó lên trên hoạt động thử bắt,

đổi tên nó để bắt đầu.

Trong hộp văn bản của nó nhập

văn bản đọc tệp Excel.

Kéo và

thả một hoạt động viết dòng khác bên dưới

hoạt động thử bắt, đổi tên thành kết thúc.

Trong hộp văn bản của nó, nhập văn bản

Đọc file excel thành công

mở rộng phần cuối cùng

của hoạt động thử bắt.

Tìm kiếm hoạt động if trong

bảng điều khiển hoạt động và kéo và

thả nó vào phần cuối cùng.

Đổi tên nó để kiểm tra biến trống,

trong hộp văn bản tình trạng của nó

nhập biểu thức DT gạch dưới

dữ liệu nhân viên không là gì cả.

Tìm kiếm hoạt động ở phạm vi sậy ở

bảng hoạt động và kéo và thả nó

trong phần then của hoạt động if,

đổi tên nó để đọc lại dữ liệu Excel.

Hoạt động này nếu sẽ kiểm tra

dù bảng dữ liệu biến DT

gạch dưới dữ liệu nhân viên trống.

Nếu nó được tìm thấy trống thì hãy thử

để đọc tệp Excel sẽ được thực hiện,

bấm vào biểu tượng thư mục này

hoạt động để mở tệp Explorer và

chọn tệp data.XLSX của nhân viên

từ đó dữ liệu sẽ được đọc.

Làm trống hộp văn bản phạm vi để

rằng toàn bộ bảng Excel có thể được đọc.

Điều hướng đến bảng thuộc tính và

trong thuộc tính bảng dữ liệu,

nhập dữ liệu nhân viên DT gạch dưới.

Hãy chạy quy trình công việc này ngay bây giờ,

nhấp vào Lưu để lưu dự án và

bấm chạy từ tệp gỡ lỗi

tùy chọn để chạy quy trình công việc.

Hãy mở bảng đầu ra.

Bạn có thể thấy rằng quy trình làm việc

thực hiện thành công.

Nó có nghĩa là hoạt động không hợp lệ

ngoại lệ đã được xử lý thành công bởi

hoạt động thử bắt.

Cảm ơn đã xem, tạm biệt.