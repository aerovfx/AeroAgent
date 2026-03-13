# 06 trình diễn-sử dụng-regex-builder

---

[ÂM NHẠC]

Xin chào và chào mừng đến với cuộc biểu tình này trên

sử dụng RegEx Builder trong studio,

trong video này bạn sẽ

đang tạo ra một quy trình làm việc

có thể trích xuất ID email từ

một đoạn văn bản để hiển thị

trong bảng đầu ra.

Vì vậy, hãy bắt đầu, tìm kiếm

một hoạt động được giao trong

bảng Hoạt động và

kéo và thả nó vào bảng Designer,

đổi tên chuỗi thành RegEx Builder và

thêm chú thích vào nó.

Đổi tên hoạt động được chỉ định thành tin nhắn,

trong hai hộp văn bản,

nhấn Control cộng K để

tạo một biến mới và

đặt tên nó là tin nhắn.

Bây giờ điều hướng đến Thuộc tính

bảng của hoạt động được chỉ định,

nhấp vào biểu tượng dấu chấm lửng của trường giá trị

để mở cửa sổ soạn thảo biểu thức.

Nhập tên tôi là Joe, email của tôi là,

joe@theratemail.com và

email của bố tôi là jack@theratemail.com,

và

email của chú tôi là j@theratemail.com,

trong dấu ngoặc kép, bấm OK.

Tìm kiếm hoạt động Matches,

và kéo và

thả nó xuống dưới hoạt động được chỉ định,

đổi tên nó thành email.

Bấm vào cấu hình thường xuyên

nút biểu thức bên trong

hoạt động của trận đấu,

trong trình hướng dẫn RegEx Builder,

đi tới cột RegEX và

chọn email từ danh sách thả xuống.

Trong cột vòng loại,

chọn bất kỳ số 0 hoặc

nhiều hơn nữa từ danh sách thả xuống,

nó sẽ trích xuất tất cả email

ID từ văn bản,

nhấp vào lưu để thoát khỏi trình hướng dẫn.

Bây giờ, điều hướng đến Thuộc tính

bảng điều khiển hoạt động Trận đấu,

trong Thuộc tính đầu vào,

nhập thông báo biến hiện có.

Trong thuộc tính kết quả,

nhấn Control cộng K trên bàn phím của bạn và

tạo một biến mới,

ID email, sau khi đặt dấu hai chấm

để lưu trữ ID email được trích xuất.

Tìm kiếm, Đối với từng hoạt động, kéo và

thả nó sau hoạt động Trận đấu và

đổi tên nó thành ID Email.

Để lại mục văn bản trong

hộp đầu tiên vẫn vậy, và

trong hộp văn bản biểu thức VB,

nhập ID email biến.

Tìm kiếm

một hoạt động bên phải và kéo và

thả nó vào phần nội dung của For

Mỗi hoạt động và

đổi tên nó thành ID Email,

nhập mục dấu chấm vào chuỗi trong vùng văn bản.

Lưu dự án và chạy nó,

đi đến bảng đầu ra,

bạn có thể thấy rằng tất cả ID email từ

văn bản được trích xuất và liệt kê ở đây.

Với điều này, bây giờ chúng ta đi đến

kết thúc cuộc biểu tình,

nó được khuyến khích xây dựng

quy trình làm việc như đã được chứng minh và

làm quen với

RegEx Builder, cảm ơn bạn đã xem