# 05 biểu đồ và đồ thị-in-power-bi-part-2

---

Hãy quay trở lại với bản báo cáo.

Bản đồ được dùng để thể hiện

sự phân bố địa lý của

dữ liệu bằng cách vẽ các điểm dữ liệu

trên nền địa lý.

Hãy tạo nó từ

ngăn hiển thị,

chọn bản đồ và

sau đó thêm quốc gia vào vị trí,

và ID đặt chỗ vào kích thước bong bóng.

Thật tuyệt vời phải không?

Làm điều này bạn có thể thấy một bản đồ hiển thị

sự phân bổ tổng thể của số lượng

đặt phòng theo địa lý.

Chúng ta có thể quan sát thấy sự nâng cao đó

khu nghỉ dưỡng nổi bật hơn ở châu Âu

so với các châu lục như vậy

như Bắc Mỹ và Úc.

Cho đến bây giờ chúng tôi đã tạo ra các biểu đồ hoặc

đồ thị giữ một số

đặt phòng làm tham số chính.

Nhưng mọi thứ sẽ thay đổi sau chuyện này.

Vấn đề tiếp theo mà Nâng cao Khu nghỉ dưỡng

muốn hiểu là sự phân tích của

doanh thu theo thị trường,

phân khúc và loại khách hàng.

Nhưng nếu bạn đi tới Chế độ xem dữ liệu và

đi đến tập dữ liệu Đặt phòng khách sạn,

bạn sẽ thấy rằng chúng tôi không có

bất kỳ cột nào liên quan đến doanh thu.

Để hiểu rõ hơn về doanh thu, chúng tôi

trước tiên cần tạo các cột có liên quan.

Nếu bạn nhìn vào tập dữ liệu

trong bảng Đặt phòng khách sạn,

chúng tôi có một cột gọi là ADR

là tỷ giá trung bình hàng ngày và

chúng tôi cũng có một cột tên là

Thời gian lưu trú mang lại cho chúng tôi

số ngày cho

việc đặt phòng đã được thực hiện.

Nếu chúng ta nhân các giá trị có trong

những cột này, chúng ta sẽ có được doanh thu.

Nhưng đây là một điều chúng ta phải nắm bắt

xem xét hai yếu tố khác.

Một, nhiều lượt đặt phòng nhận được

bị hủy bỏ được phản ánh

trong cột Bị hủy.

Hai, nếu bạn nhìn vào

loại ký gửi cột,

có một giá trị được gọi là Không hoàn lại.

Điều này có nghĩa là một số đặt phòng nhất định sẽ cung cấp

doanh thu của chúng tôi ngay cả khi chúng bị hủy.

Chúng ta hãy tính đến những yếu tố này

trong khi tạo một cột có tên

Doanh thu thực tế.

Bây giờ, hãy bắt tay vào quá trình

tạo một cột mới gọi là

Doanh thu thực bằng cách nhấp vào mới

cột hiện diện trong Công cụ Cột và

Phần tính toán.

Khi bạn nhấp vào một cột mới,

thanh công thức xuất hiện ở trên cùng.

Ở đây chúng ta cần viết một công thức

để tính doanh thu thực tế.

Hãy chia nhỏ công thức

để làm cho nó đơn giản.

Đầu tiên, hãy chuyển tên của

cột Doanh thu thực tế

bằng dấu bằng.

Sau đó chúng ta sẽ sử dụng hàm if

để thực hiện bài kiểm tra logic và

trả về các giá trị khác nhau

dựa trên kết quả.

Sau đó sử dụng hoặc

hàm bên trong dấu ngoặc đơn.

Hoặc chức năng là kiểm tra xem có

trong hai điều kiện bên trong

dấu ngoặc đơn là đúng.

Trong trường hợp này, nó sẽ kiểm tra xem

bị hủy bằng 0 hoặc

nếu loại tiền gửi bằng không hoàn trả.

Bây giờ hãy đóng hàm hoặc sau bạn

đã vượt qua hai điều kiện này.

Nếu bài kiểm tra logic đánh giá

để đúng công thức,

nhân giá trị trong cột ADR với

giá trị trong cột Thời gian lưu trú.

Nếu bài kiểm tra logic đánh giá là sai,

công thức trở về 0.

Cuối cùng, công thức của chúng ta sẽ như thế nào

điều này sau khi nhập công thức.

Nhấn Enter và

Power Bi sẽ xác thực công thức và

tạo một cột mới có tên là Doanh thu thực.

Bây giờ chúng ta có cột doanh thu,

nhưng nó cũng sẽ rất thú vị

xem Elevate Resorts có doanh thu bao nhiêu

mất do hủy đặt phòng.

Hãy tạo một cột mới

được gọi là Doanh thu bị mất.

Để làm điều này,

chúng tôi sẽ làm theo các bước tương tự như chúng tôi đã thực hiện

trong khi tạo cột Doanh thu thực.

Chỉ cần công thức sẽ

khác nhau thay vì hoặc

chức năng chúng ta sẽ sử dụng và

chức năng.

Điều này là do chúng tôi muốn

kiểm tra cả hai điều kiện.

Nếu bị hủy thì bằng một và

nếu loại tiền gửi không

tương đương với việc không hoàn lại tiền.

Cuối cùng, nếu cả hai điều kiện đều đúng,

sau đó công thức tính doanh thu

bị mất bằng cách nhân giá trị trong

cột ADR với thời gian lưu trú.

Vì đó là doanh thu bị mất,

hãy làm cho nó âm bằng cách nhân

bởi một tiêu cực cho sai

điều kiện trong nếu thêm chức năng trống như vậy

nó không trả về gì khi không có

điều kiện được đáp ứng công thức cuối cùng sẽ

trông như thế này với cái này, chúng tôi đã tạo

hai cột liên quan đến doanh thu.

Hãy chuyển sang chế độ xem báo cáo và

sử dụng cột Doanh thu thực tế trong phần tiếp theo

trực quan để hình dung thị trường

phân khúc theo tổng doanh thu.

Biểu đồ Donut là một biểu đồ tốt để có được

sự đóng góp theo tỷ lệ của khác nhau

danh mục vào một cột số như vậy

dưới dạng Doanh thu thực trong chế độ xem báo cáo.

Trong Power Bi, chọn biểu đồ Donut từ

Ngăn trực quan hóa trong một trang mới.

Bây giờ hãy thêm giá trị vào trường của nó,

đó là phân khúc thị trường cho Huyền thoại

trường và Doanh thu vào trường Giá trị.

Làm điều đó, bạn có thể thấy một cách thích hợp

sự phân chia các phân khúc thị trường theo

tổng doanh thu đã được tạo ra

vào canvas báo cáo.

Bằng cách tạo biểu đồ này,

chúng tôi thấy rằng Ta trực tuyến và

Ta offline là người đóng góp chính

xét về mặt tạo doanh thu

với sự tham gia của 47,29 và

tương ứng là 23,51%.

Ngoài ra, ngành hàng không còn góp phần

doanh thu ít nhất.

Tiếp tục, Elevate Resorts muốn

hiểu sự đóng góp của

các loại khách hàng khác nhau đối với doanh thu.

Mặc dù chúng ta có thể một lần nữa

sử dụng biểu đồ Donut ở đây.

Vì chúng ta đang tìm tỷ lệ

doanh thu của khách hàng khác nhau

các loại mang lại,

lần này chúng ta hãy sử dụng bản đồ cây.

Bản đồ cây cũng có thể được sử dụng để xem xét

tỷ lệ của một cột số với

một thể loại.

Đây là cách tạo bản đồ cây

trong chế độ xem báo cáo trong Power Bi,

chọn Bản đồ cây từ

ngăn hiển thị.

Tiếp theo, bạn sẽ thấy cây trống

bản đồ xuất hiện trên canvas của chúng tôi.

Tiếp theo, hãy thêm dữ liệu vào hình ảnh của chúng ta.

Kéo doanh thu thực vào khu vực giá trị.

Theo mặc định, Power Bi tổng hợp điều này

tổng hợp lại, mang lại cho chúng tôi tổng doanh thu.

Để thay đổi điều đó và

đạt được kết quả mong muốn,

kéo loại khách hàng vào khu vực chi tiết.

Điều này sẽ giúp phá vỡ

đặt phòng theo loại khách hàng.

Bây giờ bạn có thể thấy bản đồ cây hiển thị

tổng doanh thu theo loại khách hàng.

Đã được thêm vào khung báo cáo.

Khi quan sát đồ thị,

chúng ta có thể thấy loại khách hàng tạm thời được giữ

phần lớn doanh thu,

tiếp theo là hợp đồng bên tạm thời.

Và cuối cùng, chúng ta có nhóm

chúng ta hãy quay trở lại báo cáo.

Power Bi cũng cho phép bạn dễ dàng chuyển đổi

giữa các loại trực quan khác nhau.

Ví dụ,

bạn có thể dễ dàng chuyển đổi biểu đồ Donut

vào bản đồ cây chỉ trong vài cú nhấp chuột.

Hãy thay đổi biểu đồ Donut mà chúng ta đã xây dựng

cho phân khúc tiếp thị vào bản đồ cây.

Đây là cách nó hoạt động, chọn

hình ảnh bạn muốn thay đổi,

sau đó chỉ cần chọn mong muốn

kiểu trực quan và

Power Bi sẽ tự động

thực hiện chuyển đổi cho bạn.

Lối này,

bạn có thể dễ dàng khám phá dữ liệu của mình và

đạt được những hiểu biết sâu sắc bằng cách sử dụng nhiều

biểu diễn trực quan.

Bây giờ, trước khi chúng ta chuyển sang nhiệm vụ tiếp theo,

hãy cùng khám phá thêm một điều nữa

tính năng tuyệt vời của Power Bi.

Hãy dừng lại ở đây.

Chúng tôi đã học được nhiều điều mới

những điều trong video này.

Hãy xem lại các khái niệm này trước

chúng ta tiếp tục ở phần tiếp theo.