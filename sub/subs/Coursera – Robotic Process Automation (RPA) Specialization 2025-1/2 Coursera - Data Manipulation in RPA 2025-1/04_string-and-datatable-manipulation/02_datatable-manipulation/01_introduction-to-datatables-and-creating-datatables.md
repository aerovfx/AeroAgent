# 01 phần giới thiệu về datatables và tạo datatables

---

Ở bài học trước,

bạn đã hiểu các phương pháp và

hoạt động cho

thao tác trên chuỗi.

Trong bài học này, bạn sẽ

hiểu DataTables và

chúng được tạo ra như thế nào.

Tìm hiểu các hoạt động đó

trợ giúp trong thao tác DataTable.

Video này tập trung vào

hiểu biết về DataTables

và DataTables như thế nào

được tạo ra. Hãy bắt đầu.

DataTable là một bảng trong bộ nhớ

đại diện của

một bảng cơ sở dữ liệu duy nhất có

một bộ sưu tập

hàng và cột.

DataTable lưu trữ dữ liệu dưới dạng

một bảng tính đơn giản

với hàng và cột,

sao cho mỗi phần của

dữ liệu có thể được xác định

dựa trên sự độc đáo của họ

tọa độ cột và hàng.

Các cột DataTables được

được xác định thông qua

chữ in hoa và

hàng thông qua các số.

Trong studio có nhiều

các cách tạo DataTable.

Bây giờ chúng ta hãy xem xét một số

trong số những cái phổ biến nhất.

Cái đầu tiên là

xây dựng DataTable.

Hoạt động này xây dựng một

cấu trúc đáng tin cậy cho

một DataTable bằng cách sử dụng một

cửa sổ chuyên dụng.

Nó cho phép tùy biến

một số cột và loại

dữ liệu cho từng cột.

Người dùng có thể cấu hình

mỗi cột có

các tùy chọn cụ thể như

cho phép giá trị null,

giá trị duy nhất,

tự động tăng số,

giá trị mặc định trong

độ dài cho chuỗi.

Cách thứ hai để tạo

DataTables có phạm vi đọc.

Hoạt động này đọc

dữ liệu từ một tập tin hiện có,

sao chép nội dung

của một bảng tính hoặc

một lựa chọn từ

bảng tính đó và

lưu trữ nó trong một

Biến DataTable.

Biến DataTable có thể

được tạo trực tiếp từ

bảng thuộc tính bằng cách sử dụng

phím tắt điều khiển K.

Cái thứ ba là Đọc CSV.

Hoạt động này đọc

nội dung của một CSV được gọi là

một tệp giá trị được phân tách bằng dấu phẩy

và lưu trữ nó trong một

biến bảng dữ liệu.

Nó giống như Đọc

Phạm vi hoạt động với

sự khác biệt mà nó hoạt động

cho các tệp CSV làm đầu vào.

Cái thứ tư là quét dữ liệu.

Hoạt động này

cho phép người dùng

trích xuất có cấu trúc

dữ liệu từ trình duyệt,

đơn hoặc tài liệu và

lưu trữ nó trong DataTable.

Bây giờ chúng ta hãy hiểu một số

thao tác dữ liệu

hoạt động,

chúng ta hãy đi qua

từng cái một.

Thêm cột dữ liệu.

Nó thêm một cột vào một

biến DataTable hiện có.

Dữ liệu đầu vào có thể là

kiểu cột dữ liệu

hoặc cột có thể

được thêm trống bởi

xác định kiểu dữ liệu và

cấu hình các tùy chọn.

Thêm hàng dữ liệu. Nó thêm

một hàng mới vào một hàng hiện có

Biến DataTable.

Dữ liệu đầu vào cho

hoạt động này có thể

là một loại hàng dữ liệu

hoặc nó có thể được nhập

dưới dạng một hàng mảng bằng cách khớp

từng đối tượng với

kiểu dữ liệu của mỗi cột.

Tra cứu bảng dữ liệu.

Nó cho phép tìm kiếm

một giá trị được cung cấp trong

một DataTable được chỉ định và

trả về chỉ mục hàng

tại đó nó được tìm thấy

hoặc nó có thể được cấu hình

để trả về giá trị từ một

ô có tọa độ cho trước,

đó là chỉ số hàng

và cột mục tiêu.

Lọc bảng dữ liệu

Nó cho phép lọc

một DataTable thông qua

Trình hướng dẫn Bộ lọc sử dụng

điều kiện khác nhau.

Hoạt động này có thể được

được cấu hình để tạo

một DataTable mới cho

đầu ra của hoạt động,

hoặc để giữ cái hiện có

một và lọc ra hoặc

xóa các mục không

phù hợp với điều kiện lọc.

Tham gia DataTables.

Nó kết hợp các hàng từ hai bảng

bằng cách sử dụng các giá trị

chung của nhau.

Đây là một trong những thứ nhất

hoạt động hữu ích trong

kịch bản kinh doanh nơi làm việc

với nhiều hơn một dữ liệu

bảng là rất phổ biến.

Hợp nhất DataTable.

Nó được sử dụng để hợp nhất

một DataTable được chỉ định với

DataTable hiện hành.

Nó cung cấp bốn loại

các hành động cần thực hiện khi sáp nhập,

thêm, bỏ qua, quay lại

lỗi và nhập thủ công.

Tạo DataTable, tạo

một biến DataTable từ

dữ liệu phi cấu trúc bằng cách cho phép

người dùng chỉ ra hàng

và dấu phân cách cột.

Tùy chọn này cực kỳ

hữu ích khi dữ liệu

được ghi lại từ quá trình quét

tài liệu hoặc quét web.

Đối với mỗi hàng, nó tương tự

vào vòng lặp for mỗi vì nó

lặp qua tất cả các hàng trong

một DataTable và thực hiện

hành động tương tự.

Xóa bảng dữ liệu

Nó xóa tất cả dữ liệu

các mục trong một DataTable.

Nó có thể rất hữu ích với

Các bảng dữ liệu được sử dụng như

bảng trung gian cho dữ liệu

chuyển từ bàn này sang bàn khác.

Bảng dữ liệu đầu ra.

Nó được sử dụng để viết một

Bảng dữ liệu được chỉ định

thành một biến chuỗi

ở định dạng CSV.

Điều này có thể phục vụ như một

bước trung gian

một quá trình hoặc như một

bước cuối cùng khi,

sau nhiều lần thao tác,

một DataTable chứa

chỉ có một số giá trị.

Xóa dữ liệu. Đó là một

nhóm gồm hai hoạt động

được sử dụng để loại bỏ các hàng hoặc

cột từ một

DataTable hiện có.

Hàng có thể được xác định bởi

số chỉ mục của họ hoặc bằng

nhập dòng dữ liệu

như một đối tượng và các cột

có thể được bổ sung

được xác định bằng tên của họ.

Loại bỏ các hàng trùng lặp.

Nó được sử dụng để loại bỏ

các hàng trùng lặp trong khi

chỉ giữ lại

lần xuất hiện đầu tiên.

Sắp xếp bảng dữ liệu.

Nó được sử dụng để sắp xếp một DataTable

sử dụng một quy định

cột theo tiêu chí.

Bên cạnh việc chỉ ra đâu

cột để sử dụng trong khía cạnh này,

người dùng có thể chọn xem

việc sắp xếp sẽ được thực hiện

tăng dần hoặc giảm dần.

Tôi sẽ khuyến khích

bạn hãy thử từng cái một

những hoạt động này trong studio

và trực tiếp xem cách họ làm việc.

Tiếp theo, chúng tôi có hai bản demo để

chỉ cho bạn cách làm việc

với DataTable.

Đó là tất cả cho video này.

Cảm ơn bạn đã xem.