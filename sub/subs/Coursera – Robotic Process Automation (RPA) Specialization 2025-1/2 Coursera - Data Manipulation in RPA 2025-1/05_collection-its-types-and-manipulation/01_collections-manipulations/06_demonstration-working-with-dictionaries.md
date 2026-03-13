# 06 demo-làm việc với từ điển

---

Xin chào và chào mừng đến với

cuộc biểu tình này trên

cách làm việc với từ điển

sử dụng các phương pháp khác nhau.

Trong video này, bạn sẽ

tạo một từ điển

chứa tên khác nhau

các quốc gia và thủ đô của họ.

Ngoài ra, bạn sẽ học

các phương pháp khác nhau để thêm

các giá trị trong từ điển,

và lấy lại, và

loại bỏ các giá trị khỏi nó.

Trong UiPath Studio,

tìm kiếm một hoạt động được chỉ định trong

bảng Hoạt động và kéo

và thả nó vào

Bảng thiết kế.

Đổi tên và chú thích

trình tự.

Ngoài ra, đổi tên

Chỉ định hoạt động.

Mở bảng Biến.

Trong cột Tên tạo mới

biến có tên CountryCapital,

và trong Biến

bấm vào cột gõ

tùy chọn duyệt tìm loại

từ trình đơn thả xuống.

Trong cửa sổ bật lên,

tìm kiếm từ điển và

chọn "Từ điển" bên dưới

System.Collections.Generic.

Chúng ta cần chọn loại

cặp khóa và giá trị

chúng tôi muốn lưu trữ.

Từ điển của chúng ta sẽ có quốc gia

và chữ hoa là chuỗi,

vì vậy trong các hộp đó

xuất hiện trên đầu trang

cửa sổ chọn "Chuỗi"

từ các menu thả xuống.

Nhấp vào "Được". Đóng

bảng Biến.

Trong hai hộp văn bản của

hoạt động Phân công,

nhập CountryCapital.

Bấm vào biểu tượng dấu ba chấm của

thuộc tính giá trị từ

Bảng thuộc tính và nhập

biểu thức Mới

Từ điển(Của chuỗi, chuỗi).

Biểu thức này khởi tạo

từ điển.

Hãy mở rộng biểu thức này.

Nhập từ[{"Úc","Sydney"),("Anh",

Luân Đôn")).

This extended

biểu thức lưu trữ hai

các quốc gia và của họ

chữ hoa trong từ điển.

Nhấp vào "Được" để

đóng cửa sổ lại.

Chúng ta sẽ sử dụng một phương pháp

để đếm số lượng

giá trị hiện được lưu trữ

trong từ điển.

Kéo và thả một

hoạt động hộp tin nhắn

bên dưới hoạt động Chỉ định.

Đổi tên hoạt động.

Trong hộp văn bản của nó,

nhập biểu thức "Đếm

: "+

CountryCapital.Count.ToString.

Chúng ta sẽ lấy lại vốn của

Úc sử dụng ba phương pháp.

Hãy xem phương pháp đầu tiên.

Kéo và thả một

hoạt động của hộp tin nhắn.

Đổi tên hoạt động.

Trong hộp văn bản của nó,

nhập biểu thức

"Thủ đô của Úc là: +

CountryCapital("Úc"). ToString.

Chúng ta sẽ lấy lại vốn của

Úc sử dụng

phương pháp thứ hai.

Kéo và thả một

hoạt động hộp tin nhắn

, đổi tên hoạt động.

Trong hộp văn bản của nó,

nhập biểu thức "Vốn

của Úc sử dụng

Phương pháp mục

là:

+CountryCapital.Item("Úc").ToString.

Chúng ta sẽ lấy lại vốn của

Úc sử dụng

phương pháp thứ ba.

Đối với phương pháp này,

Studio UiPath của bạn

phải có

Microsoft.Activities.Extensions.

Nếu nó được cài đặt,

bạn có thể tìm thấy nó dưới

sự phụ thuộc của dự án

tab trong quản lý gói,

hoặc bạn phải cài đặt nó

từ tab Tất cả các gói.

Kéo và thả lại từ

hoạt động từ điển

Trong cửa sổ bật lên đó

xuất hiện chọn "Chuỗi"

từ cả hai trình đơn thả xuống

menu và nhấp vào "Được".

Đổi tên hoạt động.

Trong hộp văn bản đầu tiên của

hoạt động, nhập

Vốn nước.

Trong hộp văn bản thứ hai,

nhập "Úc".

Trong hộp văn bản thứ ba,

nhấn "Control plus K" trên

bàn phím và gõ của bạn

Thủ đô Úc.

Giá trị truy xuất

của Úc sẽ

được lưu trữ trong biến

Thủ đô Úc.

Bây giờ, hãy kéo và thả một

hoạt động của hộp tin nhắn.

Đổi tên hoạt động.

Trong hộp văn bản của nó,

nhập biểu thức.

“Thủ đô nước Úc

sử dụng Nhận từ

hoạt động từ điển là

"+Thủ đô Úc.

Bây giờ chúng ta hãy chạy quy trình công việc này.

Bạn có thể thấy rằng một

hộp tin nhắn hiển thị

số lượng giá trị khóa

cặp trong từ điển,

đó là hai, nhấp vào "Được".

Tin nhắn tiếp theo hiển thị

thủ đô của Úc

sử dụng cái đầu tiên

phương pháp. Nhấp vào "Được".

Tin nhắn tiếp theo hiển thị

thủ đô của Úc

sử dụng thứ hai

phương pháp. Nhấp vào "Được".

Tin nhắn tiếp theo hiển thị

thủ đô của Úc

sử dụng thứ ba

phương pháp. Nhấp vào "Được".

Bây giờ, chúng ta sẽ thêm dữ liệu mới

vào từ điển.

Let's remove all the

hoạt động hộp tin nhắn

và họ nhận được từ

hoạt động từ điển

Bây giờ, hãy kéo và thả và thêm

đến hoạt động từ điển.

Trong cửa sổ bật lên đó

xuất hiện chọn,

Chuỗi từ cả hai trình đơn thả xuống

menu và nhấp vào "Được".

Đổi tên hoạt động.

Trong hộp văn bản đầu tiên,

nhập CountryCapital.

Trong văn bản thứ hai

hộp, nhập ''USA".

Trong hộp văn bản thứ ba,

nhập "Washington DC".

Bây giờ, hãy kéo và thả một

hoạt động của hộp tin nhắn.

Đổi tên hoạt động.

Trong hộp văn bản của nó,

nhập biểu thức.

“Mỹ có trong từ điển

: "+CountryCapital.ContainsKey

("Hoa Kỳ"). ToString.

Biểu thức này sẽ trông

Hoa Kỳ trong từ điển

và trả về true nếu tìm thấy

và sai nếu không tìm thấy.

Bây giờ, chúng ta sẽ loại bỏ

Hoa Kỳ và giá trị của nó

từ từ điển.

Kéo và thả hoặc xóa

từ hoạt động từ điển.

Trong cửa sổ bật lên xuất hiện,

chọn Chuỗi từ

cả trình đơn thả xuống

menu và nhấp vào "Được".

Đổi tên hoạt động.

Trong hộp văn bản đầu tiên

nhập ''CountryCapital''.

Trong văn bản thứ hai

hộp, nhập "USA".

Trong hộp văn bản thứ ba,

nhấn Control cộng K và

nhập ''RemoveUSA''.

The RemoveUSA

biến sẽ lưu trữ.

Đúng như giá trị của nó nếu Hoa Kỳ

đã có mặt ở

từ điển và bị xóa,

và nó sẽ lưu trữ Sai nếu

Hoa Kỳ không có mặt

trong từ điển.

Bây giờ, hãy kéo và thả một

hoạt động của hộp tin nhắn.

Đổi tên hoạt động.

Trong hộp văn bản của nó,

nhập biểu thức "USA

bị xóa: +RemoveUSA.ToString.

Bây giờ hãy kéo và thả cái khác

hoạt động của hộp tin nhắn.

Đổi tên hoạt động.

Trong hộp văn bản của nó,

nhập biểu thức,

CountryCapital("USA'').ToString.

Biểu thức này sẽ tìm kiếm

giá trị của Hoa Kỳ

trong từ điển,

và UiPath Studio sẽ ném

một lỗi nếu không tìm thấy USA.

Hãy tiến hành hoạt động này.

Bạn có thể thấy rằng một hộp tin nhắn

cho thấy sự xác nhận của Hoa Kỳ

có mặt ở

từ điển. Nhấp vào "Được".

Thông báo tiếp theo hiển thị

xác nhận rằng Hoa Kỳ là

bị xóa khỏi

từ điển. Nhấp vào "Được".

Bây giờ, một cửa sổ lỗi nói rằng

chìa khóa đã cho không phải

có trong từ điển.

Đó là bởi vì chúng tôi

loại bỏ Hoa Kỳ khỏi

từ điển sử dụng lệnh xóa

từ hoạt động từ điển.

Đó là nó cho việc này

từ điển trình diễn.

Cảm ơn bạn đã xem.