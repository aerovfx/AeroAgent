# 03 chức năng hiểu văn bản

---

Xin chào và chào mừng trở lại.

Trong video trước, chúng tôi

tổ chức phân tích PrimeBuy

việc bán hàng điện tử

thiết bị so với tổng doanh số bán hàng.

Trong video này, chúng ta hãy nhảy vào

một vấn đề mới đó

Prime Buy phải giải quyết.

Tính đến thời điểm hiện tại, có

sáu nhà kho

phục vụ cho việc giao hàng của

sản phẩm khắp các tiểu bang.

Prime Buy có tham vọng

kế hoạch mở rộng

cơ sở kho của nó để

phục vụ cho sự phát triển của nó

cơ sở khách hàng.

Họ muốn nhiều hơn nữa

Kho sắp được

được đặt ở các tiểu bang

với doanh số bán hàng cao hơn.

Việc mở rộng chiến lược này đòi hỏi

một sự hiểu biết thấu đáo về

phân phối bán hàng hiện tại

qua các kho khác nhau.

Vì vậy, Prime Buy đầu tiên

muốn phân tích

tổng số phân phối

bán hàng theo mã kho.

Hãy điều hướng đến

xem dữ liệu trong Power BI

và hãy nhìn vào

cột kho dưới

phiếu đặt hàng bán hàng.

Khi kiểm tra dữ liệu trong

cột mã kho,

người ta quan sát thấy rằng

các giá trị không có trong

định dạng mong muốn.

Các giá trị bao gồm

sự kết hợp của văn bản

và mã kho,

gây khó khăn cho

người dùng nhìn vào mã.

Tất cả mã kho

bắt đầu bằng tiền tố,

ở đâu và dấu gạch nối,

trong đó bổ sung thêm

sự lặp lại không cần thiết

và sự lộn xộn của thông tin.

Trước khi tiếp tục với

tạo ra sự trực quan,

nó là điều cần thiết để

giải quyết vấn đề này

Chúng ta cần trích xuất một chỉ định

số ký tự từ

cuối bên phải của

một mã kho để thực hiện

nó khác biệt với những người khác.

Các chức năng văn bản là

một bộ đa năng

những chức năng có thể

được sử dụng để thao tác và

định dạng chuỗi văn bản

theo nhiều cách khác nhau.

Trong kịch bản này,

chúng ta cần trích xuất

một số lượng nhất định

ký tự từ bên phải

cuối mã kho.

Đây là những loại khác nhau của

các chức năng văn bản như nối,

trái, phải và nhiều hơn nữa.

Sự nối

chức năng cho phép bạn

nối hai chuỗi văn bản

thành một chuỗi văn bản.

Cú pháp được đưa ra dưới đây.

Trong khi bên trái và bên phải

chức năng cho phép bạn

trả về số đã chỉ định

của các ký tự từ bên trái,

và bên phải của một cho trước

chuỗi văn bản tương ứng.

Với sự hiểu biết này,

chúng ta hãy hướng tới

Power BI để khắc phục điều này

cấp mã kho,

hãy sử dụng đúng chức năng

vì chúng tôi muốn giữ

chỉ có một vài ký tự từ

cuối bên phải của văn bản.

Đầu tiên chúng ta cần tạo

một cột được tính toán mới được gọi là

mã kho

ngắn mà trích xuất

bảy ký tự cuối cùng

từ nhà kho

cột mã trong

phiếu đặt hàng bán hàng như

mã chữ và số trong

mã khác nhau là của

bảy ký tự.

Hãy làm điều đó. làm

chắc chắn rằng bạn đang ở trong

phiếu đặt hàng bán hàng và

nhấp vào tab cột mới.

Trong thanh công thức,

truyền lại tên

của cột như

mã kho ngắn,

và gọi hàm đúng.

Để sử dụng chức năng này,

chúng ta cần cung cấp hai đối số

trong dấu ngoặc đơn.

Đầu tiên là cột từ

mà chúng tôi muốn

trích xuất các ký tự.

Trong trường hợp này, nó

là mã kho.

Như đối số thứ hai,

chúng ta cần nhập số

nhân vật mà chúng tôi

cần giải nén,

trong trường hợp của chúng tôi là bảy,

kể từ mã kho

dài bảy ký tự.

Hãy đóng dấu ngoặc đơn lại.

Công thức hoàn chỉnh

sẽ trông như thế này

Sau khi viết bài này

công thức, nhấn Enter,

và một cột mới sẽ được thêm vào

vào phiếu đặt hàng bán hàng

chứa cái cuối cùng

bảy ký tự

của từng mã kho.

Bây giờ chúng ta có

làm sạch cột của chúng tôi,

chúng ta hãy nhìn vào

số lượng bán hàng

đang được giải quyết bởi

kho khác nhau.

Đối với phân tích này,

biểu đồ cột nhóm

sẽ là biểu đồ lý tưởng.

Hãy hướng tới

phần xem báo cáo

và chọn một cụm

biểu đồ cột

để hình dung sự phân bố của

tổng doanh số bán hàng trên toàn

những kho này.

Để thêm các trường vào chỗ trống

biểu đồ cột cụm,

kéo và thả

tổng doanh số bán hàng

từ bảng biện pháp đến

trục y và mã kho

thiếu từ đơn đặt hàng

tấm theo trục x.

Làm như vậy bạn có thể thấy

biểu đồ cột nhóm

được tạo hiển thị tổng doanh số

theo mã số kho.

Sử dụng biểu đồ này, Prime Buy đã

có thể tìm thấy điều đó

kho có mã

NMK1003 là lớn nhất

đóng góp vào tổng doanh số bán hàng,

và NBV1002 là

người đóng góp thấp nhất

Họ có thể xây dựng một

thêm kho để hỗ trợ

tải trên Kho NMK1003

hoặc họ có thể bổ sung thêm

cơ sở vật chất để kích hoạt

kho khác để xử lý

doanh số bán hàng nhiều hơn và bằng nhau

phân phối tải.

Tuy nhiên, nhà kho

chỉ là một phần của

chuỗi cung ứng.

Chiến lược mở rộng

cũng phụ thuộc vào

tìm hiểu nhu cầu khách hàng

ở mức độ lớn hơn.

Hãy tinh chỉnh thêm

chiến lược mở rộng của họ.

Prime Buy rất muốn hiểu

mô hình phân phối bán hàng

kho bãi theo tiểu bang.

Để hình dung vấn đề này.

Hãy sử dụng bản đồ trực quan.

Trong bước tiếp theo, thêm

cột trạng thái từ

bảng vị trí cửa hàng

vào trường vị trí.

Như bạn có thể thấy, Power BI có

ánh xạ các trạng thái trong biểu đồ.

Đối với một số bạn, những người sẽ

nhận được một lỗi nói rằng

bản đồ bị vô hiệu hóa rồi bạn

cần phải thực hiện một sự điều chỉnh

trong cài đặt,

đi tới Tệp và bên dưới đó,

bấm vào Tùy chọn và Cài đặt.

Một lần nữa, Tùy chọn,

một cửa sổ mới xuất hiện.

Bây giờ hãy chuyển đến tab Bảo mật

thuộc Global và thực hiện

chắc chắn rằng ArcGIS cho

Power BI và Bản đồ và được điền

Hình ảnh được chọn.

Sau đó bấm vào Được rồi

và bạn sẽ phải

khởi động lại Power BI của bạn để thực hiện

chắc chắn rằng những điều này

những thay đổi được ghi lại.

Bây giờ hãy thêm kho

cột mã ngắn

từ phiếu đặt hàng bán hàng

đến lĩnh vực huyền thoại.

Cuối cùng, cộng tổng doanh số

đo vào kích thước bong bóng.

Khi đã xong việc đó, bạn

có thể thấy bản đồ hiển thị

tổng doanh số bán hàng theo tiểu bang và

mã kho được tạo.

Bong bóng càng lớn

quy mô, doanh số bán hàng cao hơn.

Ngoài ra, một chiếc bánh

biểu đồ với bong bóng

thể hiện tỷ trọng của

bán hàng của các kho khác nhau.

Với sự giúp đỡ của điều này

bản đồ Prime Buy cũ là

có thể đạt được

những phát hiện sau đây.

Mặc dù Kho

NMK1003 góp phần vào

phần lớn của

bán hàng về mặt

khối lượng bán hàng có thể được

nhìn thấy từ biểu đồ cụm.

Đó là Kho UHY1004 đó

bao gồm số lượng tối đa

tiểu bang trong

đất nước, đó là 16.

Ngoại trừ California,

Texas, Louisiana,

và tất cả New York

các tiểu bang khác là

phục vụ theo cá nhân

nhà kho.

Thứ ba, doanh số bán hàng cho

Kho MKL1006

trải rộng khắp năm bang,

đó là ít nhất.

Ngoài ra, doanh số bán hàng nằm rải rác

khắp các tiểu bang xa xôi

xa nhau.

Cuối cùng, Wyoming là

tiểu bang duy nhất làm được điều đó

không có doanh số bán hàng.

Bài học lớn từ

phân tích này là

rõ ràng và thuyết phục.

Prime Buy cần

phân bổ việc giao hàng cho

kho gần hơn

tới một nhóm các trạng thái.

Ngoài ra còn nhiều kho

có thể được thêm vào nơi có

là sự chậm trễ trong thời gian giao hàng

do khoảng cách

từ một nhà kho.

Với những bài học này,

chúng tôi đã đến

cuối video này.

Trong video này, chúng tôi đã giúp

Mua hàng Prime với sự hiểu biết

mô hình bán hàng theo kho

bằng cách sử dụng các chức năng văn bản.

Trong video tiếp theo,

hãy giúp Prime Mua vào

giải quyết vấn đề tiếp theo của họ.