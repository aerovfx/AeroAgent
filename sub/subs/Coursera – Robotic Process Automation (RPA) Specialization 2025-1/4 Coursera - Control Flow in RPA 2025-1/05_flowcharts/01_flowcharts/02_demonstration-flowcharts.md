# 02 sơ đồ trình diễn

---

Xin chào và chào mừng đến với

cuộc biểu tình này trên

sử dụng sơ đồ

hoạt động trong Studio.

Trong video này, bạn sẽ học cách

tạo quy trình làm việc

điều đó sẽ yêu cầu

tên người dùng

và đánh dấu và sau đó

hiển thị kết quả thi

trong một hộp tin nhắn.

Hãy bắt đầu. Trong UiPath Studio,

tìm kiếm một hoạt động sơ đồ

trong bảng Hoạt động,

và kéo và thả nó

trong bảng thiết kế.

Đổi tên sơ đồ

hoạt động dưới dạng Demo,

và thêm chú thích vào nó.

Bấm đúp để xem

hoạt động của sơ đồ.

Tìm kiếm đầu vào

Hoạt động hộp thoại

trong bảng Hoạt động,

và kéo và thả nó vào

các nút bắt đầu xuống

mũi tên trong vùng chứa lưu đồ

để kết nối nó với nút.

Đổi tên hoạt động

là Tên.

Bấm đúp để mở nó.

Trong dấu ngoặc kép,

nhập văn bản tiêu đề

"Tên" trong Tiêu đề hộp thoại,

trong văn bản nhãn nhập

Tên học sinh trong

Hộp Nhãn đầu vào.

Từ bảng Biến.

Tạo một biến,

nói Tên,

với kiểu biến là String,

và Phạm vi dưới dạng Bản trình diễn sơ đồ.

Bây giờ đi đến

Bảng thuộc tính của

hoạt động hộp thoại đầu vào của người dùng,

và nhập biến Đầu tiên

Tên trong thuộc tính kết quả của nó.

Điều hướng trở lại sơ đồ.

Tìm kiếm đầu vào

Hoạt động hộp thoại

trong bảng Hoạt động,

và kéo và thả nó bên dưới

hoạt động Hộp thoại Nhập liệu đầu tiên.

Đổi tên hoạt động thành intMarks,

và nhấp đúp để mở nó.

Trong dấu ngoặc kép,

nhập văn bản tiêu đề

"Dấu" trong Tiêu đề hộp thoại.

Trong văn bản nhãn,

nhập điểm của bạn bằng số

trong hộp Nhãn đầu vào.

Từ bảng Biến,

tạo một biến intMarks

với kiểu biến

như int32 và Phạm vi

dưới dạng Bản trình diễn sơ đồ.

Đi tới bảng Thuộc tính của

hoạt động Hộp thoại Nhập liệu của người dùng này,

và nhập biến intMarks

trong thuộc tính kết quả của nó.

Điều hướng trở lại sơ đồ,

tìm kiếm một luồng

Hoạt động quyết định

trong bảng Hoạt động,

và kéo và thả nó bên dưới

hoạt động Hộp thoại đầu vào.

Đổi tên quyết định luồng

hoạt động đã Đạt hoặc Không đạt.

Quyết định dòng chảy

hoạt động có hai mặt.

Bên trái là mặt thật

và bên phải là bên giả.

Nếu một điều kiện nhất định là đúng,

quy trình công việc hoặc

các hoạt động trên

bên trái của cái này

hoạt động sẽ thực thi.

Tương tự, nếu một

điều kiện là sai,

quy trình làm việc hoặc

các hoạt động trên

phía bên phải của cái này

hoạt động sẽ thực thi.

Điều hướng đến bảng Thuộc tính

của hoạt động Quyết định dòng chảy.

Trong hộp văn bản điều kiện,

nhập biểu thức intMarks

lớn hơn hoặc bằng 60.

Biểu thức này có nghĩa là

60 hoặc hơn 60 điểm là

cần thiết để vượt qua kỳ thi.

Tiếp theo, chèn hai

Hoạt động của Hộp Tin nhắn.

Đặt một cái ở bên trái,

đó là mặt thật,

và cái khác ở bên phải,

đó là mặt sai của

hoạt động Quyết định dòng chảy,

đổi tên cả hai hoạt động.

Bấm đúp để xem

hoạt động Hộp Tin nhắn đầu tiên.

Trong vùng văn bản, nhập văn bản,

"Xin chúc mừng"

cộng với Tên cộng

"bạn đã vượt qua kỳ thi."

Điều hướng trở lại sơ đồ.

Bấm đúp để xem

hoạt động của hộp tin nhắn thứ hai.

Trong vùng Văn bản, nhập văn bản,

"Xin chào" cộng với FirstName cộng

"Bạn đã trượt kỳ thi."

Hãy nhớ sử dụng dấu cộng

các ký hiệu khi viết văn bản.

Điều hướng trở lại sơ đồ.

Hãy lưu lại

dự án và chạy nó.

Nhập tên của một sinh viên

trong hộp Tên, nói Ron,

và nhấp vào ổn, và 75 trong

hộp Marks và nhấn OK.

Bạn có thể thấy thông báo nói rằng,

"Chúc mừng Ron, cậu

đã vượt qua kỳ thi."

Bây giờ hãy chạy lại quy trình làm việc.

Lần này nhập dấu

nói 50 cho Ron.

Ở đây bạn có thể thấy

tin nhắn nói rằng,

"Xin chào Ron, bạn có

thi trượt."

Nó được khuyến khích tạo ra

quy trình làm việc như đã trình bày,

đóng khung các quyết định của riêng bạn và

thử sơ đồ

hoạt động của riêng bạn.

Cảm ơn bạn đã xem.