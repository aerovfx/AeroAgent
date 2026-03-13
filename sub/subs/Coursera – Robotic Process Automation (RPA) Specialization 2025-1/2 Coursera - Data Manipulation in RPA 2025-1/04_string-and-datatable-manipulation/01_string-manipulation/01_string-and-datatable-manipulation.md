# 01 thao tác chuỗi và dữ liệu

---

Chào mừng đến với phần tiếp theo

mô-đun của khóa học này,

giới thiệu về chuỗi và

Thao tác với DataTable.

Trong mô-đun trước,

bạn đã hiểu

thao tác dữ liệu,

các hoạt động khác nhau

được thực hiện trên đó.

Bạn cũng đã thấy dữ liệu

có thể được chuyển đổi từ

loại này sang loại khác bằng cách sử dụng

kỹ thuật chuyển đổi dữ liệu.

Đến cuối mô-đun này,

bạn sẽ có thể hiểu được

thao tác chuỗi, hiểu

Thao tác với DataTable.

Hãy bắt đầu việc này

bài học ở đâu bạn

sẽ hiểu chuỗi và

việc sử dụng khác nhau

hoạt động và

hoạt động cho

thao tác trên chuỗi.

Trong bài học về biến số,

bạn đã học được rằng một chuỗi là

kiểu dữ liệu chứa

bất kỳ chuỗi ký tự nào.

Hầu như mọi tự động hóa

kịch bản liên quan đến việc sử dụng

chuỗi khi chúng được sử dụng khi

văn bản cần được ghi lại,

được xử lý, gửi giữa

ứng dụng hoặc hiển thị.

Trong Studio, một số thao tác

có thể được thực hiện

để thao túng.

Hãy hiểu

mỗi người trong số họ.

Hãy bắt đầu với

phương pháp concat.

Phương pháp này nối

các biểu diễn chuỗi

của hai đối tượng được chỉ định.

Trong biểu thức sau đây,

hai biến chuỗi có tên

Họ và Tên

đang được nối lại.

Kiểu dữ liệu đầu ra cho

biểu thức này sẽ là

chuỗi với sự kết hợp

giá trị của cả hai biến.

Ví dụ: nếu FirstName có

một giá trị Smith và

Họ Jones,

giá trị đầu ra

sẽ là SmithJones.

Thứ hai, phương thức chứa.

Phương pháp này kiểm tra xem

một chuỗi con được chỉ định

xảy ra trong một chuỗi.

Phương thức này trả về

một giá trị Boolean

điều đó đúng hoặc sai.

Trong biểu thức sau đây,

sự xuất hiện của

chuỗi Bucharest là

đang được kiểm tra trong chuỗi

biến có tên PostalAddress.

Nếu Bucharest sẽ

có mặt trong địa chỉ,

đầu ra sẽ là

đúng, ngược lại là sai.

Thứ ba, phương pháp định dạng.

Phương pháp này chuyển đổi

giá trị của đồ vật

thành chuỗi dựa trên

định dạng được chỉ định

và chèn chúng vào

một chuỗi khác mà

làm giảm độ phức tạp và

làm tăng khả năng đọc.

Ví dụ, có

hai biến chuỗi có tên

FirstName và CityName.

Bằng cách sử dụng

biểu thức sau,

họ được gán số 0 và

tương ứng một vị trí.

Đầu ra của biểu thức này

sẽ là cuộc sống của Smith

ở Bucharest,

và kiểu dữ liệu đầu ra

sẽ có kiểu chuỗi.

Thứ tư, phương pháp IndexOf.

Phương thức này trả về

chỉ số dựa trên số không

về lần xuất hiện đầu tiên của

một ký tự trong một chuỗi.

Trong biểu thức sau đây,

chỉ số của nhân vật

tôi là sợi dây

biến FirstName,

giá trị ở đâu

Smith được trích xuất.

Đầu ra sẽ là hai,

và kiểu dữ liệu đầu ra cho

biểu thức này sẽ là số nguyên.

Thứ năm, phương pháp nối.

Phương pháp này nối

các yếu tố

trong một bộ sưu tập và

hiển thị chúng dưới dạng một chuỗi.

Trong biểu thức sau đây,

các yếu tố chào đón,

đến và UiPath,

trình bày một biến mảng,

Arr_Tin nhắn chào mừng,

hoặc nối

sử dụng khoảng trắng làm dấu phân cách.

Đầu ra sẽ là

chào mừng bạn đến với đường dẫn UI,

và kiểu dữ liệu đầu ra

cho biểu thức này

sẽ là chuỗi.

Thứ sáu, phương pháp thay thế.

Phương pháp này xác định một

dãy ký tự của

gõ chuỗi vào một văn bản và

thay thế nó bằng một chuỗi nhất định.

Ví dụ, có

một biến FullName với

đánh giá cao Smith Jones trong đó.

Bây giờ, nếu bạn phải thay thế

Smith với Brandon,

bằng cách sử dụng

biểu thức sau,

tên Smith sẽ là

được thay thế bằng Brandon.

Đầu ra sẽ là

Brandon Jones và

kiểu dữ liệu đầu ra cho việc này

biểu thức sẽ là chuỗi.

Thứ bảy, phương pháp chia nhỏ.

Phương thức này chia một chuỗi thành

chuỗi con dựa trên một số nhất định

tiêu chí do người dùng đặt ra.

Dấu phân cách này có thể là khoảng trắng,

dấu phẩy hoặc dấu chấm.

Trong biểu thức sau đây,

biến chuỗi có tên

WelcomeMessage với giá trị

Chào mừng đến với UiPath đã bị chia cắt

sử dụng khoảng trắng làm dấu phân cách.

Đầu ra sẽ là

UiPath cho giá trị chỉ mục

hai làm kiểu dữ liệu cho

biểu thức này là

mảng chuỗi.

Thứ tám, phương pháp chuỗi con.

Phương pháp này chiết xuất

một chuỗi con từ

một chuỗi sử dụng bắt đầu

chỉ số và độ dài.

Nó được sử dụng để cô lập hoặc

tách một chuỗi con khỏi

chuỗi gốc.

Trong cách diễn đạt này,

chuỗi chào mừng được trích xuất

từ biến chuỗi

được đặt tên là WelcomeMessage

giữ tin nhắn

Chào mừng đến với UiPath.

Chỉ số bắt đầu cho

chuỗi chào mừng là

số không và độ dài của

chuỗi chào mừng là bảy.

Kiểu dữ liệu đầu ra cho việc này

biểu thức sẽ là chuỗi.

Bây giờ hãy tiếp tục

hiểu thêm

các hoạt động cho chuỗi

thao tác trong Studio.

Đầu tiên là sửa đổi văn bản.

Hoạt động này cập nhật một văn bản

giá trị sử dụng sửa đổi,

bao gồm tìm và thay thế,

cắt, kết hợp, hoặc

nối với

một giá trị văn bản khác và

thay đổi thành chữ hoa/thường.

Khi bạn kéo và thả

hoạt động này ở

bảng thiết kế,

bạn sẽ thấy một số

các lựa chọn trong hoạt động.

Trường văn bản và sửa đổi,

mà bạn có thể thấy ở trên cùng,

sẽ lấy văn bản

cái mà bạn muốn

để sửa đổi ở định dạng chuỗi.

Bây giờ là lúc để lựa chọn

sự sửa đổi

mà bạn muốn

biểu diễn trên

chuỗi bạn đã cung cấp.

Bạn có thể chọn sửa đổi

từ quảng cáo

modification drop-down.

Trình đơn thả xuống có bốn

tùy chọn sửa đổi

: Tìm và thay thế,

kết hợp văn bản, cắt xén,

văn bản lên trên/dưới.

Hãy nói về

tùy chọn sửa đổi đầu tiên

trong danh sách đó là

tìm và thay thế.

Mở trình đơn thả xuống và

chọn sửa đổi này.

Bạn sẽ nhận thấy một phát hiện

và thay thế hoạt động

xuất hiện bên dưới

Văn bản để sửa đổi trường.

Trong hoạt động này, bạn có thể

cung cấp đầu vào vào

trường Tìm kiếm.

Văn bản bạn nhập vào đây sẽ

được tìm kiếm trong văn bản

cái đó có trong

Văn bản để sửa đổi trường.

Tiếp theo, bạn có

Thay thế bằng trường.

Văn bản tìm kiếm sẽ là

được thay thế bằng văn bản

bạn nhập vào trường này,

bạn có thể lấy một biến chuỗi

trong trường Lưu kết quả dưới dạng,

sẽ lưu kết quả.

Hoạt động này hoạt động giống như

bất kỳ tiêu chuẩn nào tìm thấy và

tính năng thay thế bạn đến

xuyên suốt trong các ứng dụng khác.

Tùy chọn sửa đổi thứ hai

trong danh sách là Kết hợp văn bản.

Hoạt động này sẽ

nối hoặc kết hợp

văn bản với văn bản hiện có

trong trường Văn bản cần sửa đổi.

Bạn có hai lựa chọn ở đây.

Tùy chọn bên trái sẽ

kết hợp văn bản để

tùy chọn bên trái và bên phải

sẽ kết hợp các

văn bản ở bên phải.

Sửa đổi thứ ba

tùy chọn trong danh sách là Trim.

Cắt dải tùy chọn

hoặc xóa

khoảng trống ở đầu và cuối

từ một biến chuỗi.

Bạn có thể chọn trái, phải,

hoặc cả hai tùy chọn như

theo yêu cầu.

Tùy chọn sửa đổi thứ tư

là Văn bản sang chữ hoa/thường.

Như tên mô tả,

sửa đổi này

chuyển đổi văn bản thành

chữ hoa hoặc chữ thường

như người dùng đã chọn.

Những sửa đổi này có thể được sử dụng

đơn lẻ hoặc kết hợp.

Bây giờ chúng ta hãy đến

nút kiểm tra.

Nút này được thiết kế để kiểm tra

đầu ra của sửa đổi

áp dụng cho chuỗi.

Hãy chuyển sang

hoạt động tiếp theo cho

thao tác chuỗi,

đó là văn bản sang trái hoặc phải.

Hoạt động này có

bốn trường trong đó.

Đó là: Toàn văn, Dấu phân cách,

Lưu văn bản sang trái dưới dạng,

Lưu văn bản sang phải dưới dạng.

Toàn văn và dấu phân cách là

các trường đầu vào và các trường khác

hai là trường đầu ra.

Trong trường Toàn văn,

văn bản mong muốn

được chia thành

dựa trên thành phần bên trái và bên phải

trên đầu vào dấu phân cách được chèn vào.

Trong ngăn cách

trường, dấu phân cách,

được sử dụng để phân chia

toàn bộ văn bản sang trái

và bên phải được chèn vào.

Dù là dấu phân cách nào

bạn cung cấp

trường này sẽ được tìm kiếm

trong trường văn bản đầy đủ.

Lưu văn bản vào trường bên trái

lưu trữ bên trái của

dấu phân cách và văn bản tới

lưu trữ đúng văn bản

ngay đến dải phân cách.

Người dùng phải chỉ định

tên biến trong đó

đầu ra phải được lưu trữ.

Ví dụ, nếu ở

trường văn bản đầy đủ

bạn có văn bản,

Bạn đang học RPA

khóa học chuyên môn

và không gian được chỉ định

trong trường phân cách,

sau đó là từ bạn và những người còn lại

của câu

sẽ bị tách ra.

Giá trị đầu ra bạn

sẽ được lưu trữ trong

Tin nhắn bên trái

biến và phần còn lại

của câu trong

MessageRight tương ứng.

Xin lưu ý rằng điều này

hoạt động tìm kiếm

sự xuất hiện đầu tiên của

dấu phân cách được chỉ định

trong trường phân cách.

Đó là tất cả cho video này.

Tiếp theo trong bài học này là

video trình diễn

thao tác trên chuỗi.

Cảm ơn bạn đã xem.