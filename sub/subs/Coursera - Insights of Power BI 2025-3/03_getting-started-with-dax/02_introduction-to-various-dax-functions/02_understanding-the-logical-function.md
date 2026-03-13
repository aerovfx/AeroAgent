# 02 hiểu-hàm-logic

---

Xin chào và chào mừng trở lại.

Trong video cuối cùng,

chúng tôi đã sử dụng các hàm tổng hợp và

các biện pháp phức tạp để giúp PrimeBuy trong

nhận được thông tin chi tiết về hiệu suất

của mỗi cửa hàng bằng cách tính toán mạng

lợi nhuận cho mỗi cửa hàng.

Bây giờ chúng ta hãy tiến lên một bước và

hiểu vấn đề tiếp theo của họ.

Ban quản lý của PrimeBuy mong muốn mở rộng

loại sản phẩm điện tử của nó.

Với những báo cáo về thị trường và

nghiên cứu sắp tới,

họ đang lạc quan về phân khúc này,

PrimeBuy nhằm mục đích xác định sự đóng góp

thiết bị điện tử trên tổng doanh số

so với các thể loại khác.

Hãy chuyển sang chế độ xem dữ liệu Power BI và

điều hướng đến bảng sản phẩm.

Qua quan sát số liệu chúng ta có thể thấy

chúng tôi chỉ có dữ liệu sản phẩm

không được phân loại vào các nhóm khác nhau.

Vì vậy chúng ta phải xác định tất cả các sản phẩm

thuộc phạm vi điện tử

danh mục thiết bị và tạo một danh mục riêng

cột để lưu trữ thông tin đó.

Sau khi kiểm tra cẩn thận

của cột tên sản phẩm,

chúng ta có thể nhận ra rằng có bốn

sản phẩm riêng biệt có thể

được xếp vào loại này,

đó là máy tính,

TV và video, điện thoại và thiết bị âm thanh.

Yêu cầu này phù hợp một cách hoàn hảo

với các hàm logic.

Các hàm logic giúp bạn thực hiện

quyết định dựa trên việc thông qua đơn hoặc

nhiều điều kiện.

Hãy cùng khám phá sự khác biệt

các hàm logic lần lượt.

Đầu tiên là hàm IF.

Hãy coi hàm IF như một câu lệnh

giúp bạn đánh giá tình trạng và

trả về một giá trị nếu nó đúng và

khác nếu nó sai.

Cú pháp của hàm này

được đề cập dưới đây.

Cái thứ hai là hàm AND,

trong đó đánh giá hai điều kiện và

chỉ trả về đúng khi tất cả

các điều kiện được đáp ứng.

Cú pháp của hàm này

được đề cập dưới đây.

Lưu ý rằng một đơn và

tuyên bố chỉ có thể có hai điều kiện.

Cái thứ ba là hàm OR,

trong đó đánh giá nhiều điều kiện và

trả về true nếu ít nhất

một trong số đó là sự thật.

Nó cho phép chúng ta xem xét

kịch bản khác nhau và

có được cái nhìn toàn diện

của bối cảnh dữ liệu.

Cú pháp của cái này

chức năng được đưa ra dưới đây.

Lưu ý rằng chức năng này cũng

xử lý hai điều kiện cùng một lúc.

Tiếp theo, chúng ta có hàm logic OR.

Toán tử mạnh mẽ này cho phép

chúng tôi đánh giá nhiều HOẶC

điều kiện đồng thời.

Hãy coi toán tử này như

một sự thay thế cho hàm OR.

Nó sẽ trả về sự thật

giá trị nếu có bất kỳ OR

điều kiện là đúng và

trả về false nếu tất cả chúng đều không đúng.

Cú pháp tương tự được đưa ra dưới đây.

Tiếp theo, chúng ta có toán tử logic OR.

Toán tử mạnh mẽ này cho phép

chúng tôi đánh giá nhiều HOẶC

điều kiện đồng thời.

Hãy coi toán tử này như

một sự thay thế cho hàm OR.

Nó sẽ trả về sự thật

giá trị nếu có bất kỳ OR

điều kiện là đúng và

trả về false nếu tất cả chúng đều không đúng.

Cú pháp của cái này

toán tử được đưa ra dưới đây.

Tiếp theo, tính logic và

toán tử cho phép bạn thêm nhiều

điều kiện sử dụng câu lệnh AND.

Hãy nghĩ về điều này như một sự thay thế cho AND

chức năng.

Cú pháp của toán tử này

được đề cập dưới đây.

Với sự hiểu biết này,

chúng ta hãy tiến về phía trước để giải quyết vấn đề.

Chúng tôi sẽ tạo một tính toán mới

cột có tên là điện tử có hoặc

không có trong bảng sản phẩm

để xác định xem mỗi

sản phẩm thuộc diện điện tử

danh mục thiết bị hay không.

Chúng ta sẽ sử dụng logic hoặc

toán tử vì chúng tôi có nhiều hơn

hơn hai sản phẩm rơi

thành một loại sản phẩm.

Hãy nhấp vào cột mới và

sau đó truyền vào tên của cột.

Bây giờ chúng ta sẽ bắt đầu với hàm IF như

một lần nữa chúng tôi muốn đánh giá một điều kiện và

trả về các kết quả khác nhau dựa trên

điều kiện đó là đúng hay sai.

Bên trong hàm IF,

hãy sử dụng logic HOẶC

toán tử để kiểm tra nhiều

điều kiện cùng một lúc.

Chúng ta so sánh cột tên sản phẩm trong

bảng bảng sản phẩm với mỗi

bốn tên thiết bị điện tử.

Hãy chắc chắn rằng bạn viết sản phẩm

đặt tên chính xác cách chúng xuất hiện trong

tập dữ liệu có khoảng trắng thích hợp và

viết hoa.

Nếu bất kỳ điều kiện nào là đúng,

cho biết tên sản phẩm phù hợp

một trong những tên thiết bị điện tử,

kết quả là công thức trả về Y.

Và ngược lại nếu không có

các điều kiện được đáp ứng,

đó là tất cả đều sai,

kết quả là công thức trả về N.

Công thức sẽ trông giống như thế này.

Sau khi viết xong công thức

nhấn vào.

Làm điều đó, bạn có thể thấy một

cột tính toán đã được tạo

chứa thông tin nếu sản phẩm

có phải là thiết bị điện tử hay không.

Bây giờ, để đảm bảo rằng

công thức đã chạy đúng rồi

hãy nhấp vào thả xuống và

lọc các hàng có chữ Y.

Chúng ta thấy rằng cả bốn sản phẩm đều có

được đặc trưng là thiết bị điện tử,

Vậy là công thức của chúng ta đã thành công như mong muốn.

Bây giờ, bước thứ hai, chúng tôi muốn tìm hiểu

tổng doanh thu của primeBuy là bao nhiêu

đến từ các thiết bị điện tử.

Để làm điều này, chúng ta cần biết tổng

bán hàng cho tất cả các sản phẩm.

Mặc dù Power BI có thể

cộng doanh số bán hàng cho

chúng tôi bằng cách trực tiếp kéo doanh số bán hàng

cột số lượng vào hình ảnh,

chúng ta sẽ tính tổng

việc bán hàng tự đo lường.

Điều này sẽ làm cho mọi việc sau này dễ dàng hơn.

Hãy tạo ra nó,

điều hướng đến bảng đo lường và

nhấp chuột phải vào nó và

chọn biện pháp mới.

Tiếp theo, chuyển tên của

thước đo là tổng doanh thu và

chúng ta sẽ tận dụng

hàm tổng trong DAX.

Hàm tổng là hàm tổng hợp

để cộng các giá trị trong một cột.

Bên trong hàm tổng,

chỉ định bảng và

cột mà từ đó chúng tôi

muốn tính tổng.

Trong trường hợp này, chúng tôi sử dụng lệnh bán hàng

bảng trang tính và cột số tiền bán hàng.

Công thức sẽ trông giống như thế này.

Bây giờ nhấn enter và làm điều đó,

một biện pháp mới đã được tạo ra

bên trong bảng đo.

Bây giờ với những biện pháp mới được tạo ra này và

cột,

hãy hình dung chúng bằng biểu đồ hình tròn.

Để làm điều đó, hãy quay lại báo cáo

xem phần và chọn biểu đồ hình tròn.

Bây giờ hãy thêm thiết bị điện tử

cột vào trường chú giải và

tổng doanh thu tính theo Giá trị

trường của biểu đồ hình tròn.

Làm điều đó bạn có thể thấy một biểu đồ hình tròn

đã được tạo có chứa thông tin

về tỷ lệ phần trăm của tổng doanh số bán hàng

cả hai thể loại, đó là

sản phẩm được bán như thiết bị điện tử và

những người không thuộc loại này.

Quan sát biểu đồ hình tròn, PrimeBuy đã

có thể thấy rằng các thiết bị điện tử

chỉ chiếm 7,85 phần trăm

trong tổng doanh số của PrimeBuy.

Với thông tin này thì khá rõ ràng

rằng có một phạm vi đáng kể cho

mở rộng trong phần này và

họ cần đầu tư thêm nguồn lực để

xác định các cơ hội bất đối xứng.

Hãy kết thúc video này tại đây.

Trong video này, chúng tôi đã giúp PrimeBuy

hiểu sự đóng góp của điện

doanh số bán thiết bị so với doanh số bán của

các sản phẩm khác sử dụng chức năng logic.