# 04 sự hiểu biết-mối quan hệ giữa các bảng

---

Xin chào và chào mừng trở lại.

Trong video trước,

chúng tôi đã thực hiện dọn dẹp cơ bản

tập dữ liệu PrimeBuy và

đã nhập nó vào Power BI.

Trong video này, chúng tôi

sẽ hành động

phía trước và giúp đỡ PrimeBuy

giải quyết nhiệm vụ tiếp theo của nó.

Nhiệm vụ tiếp theo là xác định và

thiết lập mối quan hệ

trong dữ liệu

hiện ở nhiều bảng khác nhau.

Để hình dung

các mối quan hệ hiện tại,

chúng ta hãy chuyển sang chế độ xem mô hình

phần trong Power BI và

kiểm tra

mối quan hệ giữa

các tờ của tập dữ liệu.

Hãy thu nhỏ một chút.

Ở đây bạn có thể thấy rằng Sức mạnh

BI đã tự động

được phát hiện và tạo

một kết nối

giữa các bảng

có một cột chung.

Ví dụ: bảng thông tin khách hàng

được kết nối với

phiếu đặt hàng bán hàng.

Cả hai tờ đều có

một cột chung,

cột ID khách hàng.

Tương tự, Đội ngũ bán hàng

Trang tính được kết nối với

bảng nhân khẩu học của nhóm bán hàng

bởi một cột chung,

ID nhóm bán hàng.

Nếu chúng ta nhấp vào bất cứ nơi nào trên

đường kết nối

giữa hai tờ giấy,

chúng ta có thể xem các thuộc tính của

sự kết nối như vậy

như kiểu kết nối,

tên của tờ giấy,

và cột chung.

Sơ đồ hiển thị cho chúng ta trong

phần xem mô hình là

gọi là sơ đồ quan hệ.

Khi kiểm tra các

sơ đồ quan hệ,

chúng tôi quan sát thấy rằng mỗi tờ có

ít nhất một kết nối với

một tờ khác ngoại trừ

tờ sản phẩm và

từ điển dữ liệu.

Mặc dù vậy, từ điển dữ liệu

không yêu cầu

mọi kết nối,

nó được thêm vào để bạn tham khảo.

Hãy xem liệu cái này có gì không

tác động lên sự trực quan của chúng ta.

Hãy chuyển sang chế độ xem báo cáo.

Hãy nói rằng, chúng ta phải thực hiện

một biểu đồ thanh đơn giản để

nhìn vào các sản phẩm hàng đầu trong

điều kiện về số lượng đặt hàng.

Điều này sẽ rất

tương tự như biểu đồ

ở các quốc gia hàng đầu ở

điều kiện về số lượng

lượt đặt chỗ bạn đã thực hiện

đồng thời giúp nâng cao

khu nghỉ dưỡng trong Tuần 1.

Để làm điều này,

đầu tiên chúng ta cần phải đi đến

phần xem báo cáo

và chọn

biểu đồ cột cụm.

Trong phần hiện trường,

kéo và thả

cột tên sản phẩm

từ bảng sản phẩm

vào trục X.

Tương tự, kéo và thả

cột số lượng đặt hàng từ

bảng đơn bán hàng vào trục Y.

Bằng cách đó, bạn có thể thấy

biểu đồ cột nhóm với

một thanh có chiều dài bằng nhau xuất hiện

trên canvas báo cáo.

Điều này có vẻ khá kỳ lạ,

như đối với tất cả các sản phẩm,

chúng tôi đang nhận được

cùng số lượng đặt hàng,

và con số đó cũng tính bằng triệu triệu.

Biểu đồ này yêu cầu chúng tôi

sử dụng thông tin từ

hai bảng khác nhau,

nhưng không có

kết nối giữa

các bảng trong

phần xem mô hình.

Theo mặc định, Power BI

tổng hợp các giá trị

trên khắp các danh mục

khi một kết nối

giữa các bảng

không có mặt.

Hãy cùng khám phá xem

có một cột chung

giữa tấm sản phẩm

và phiếu đặt hàng bán hàng

trong chế độ xem dữ liệu.

Sau khi kiểm tra cẩn thận, chúng tôi

chú ý rằng tờ sản phẩm

chỉ chứa hai cột trong khi

phiếu đặt hàng bán hàng

có nhiều cột,

không có cái nào phù hợp với

các cột trong bảng sản phẩm.

Tuy nhiên, các giá trị được lưu trữ

ở cột ID của

bảng sản phẩm tương ứng với

cột mã sản phẩm

từ phiếu đặt hàng bán hàng.

Chúng ta có thể kiểm tra chéo điều này bằng cách

nói chuyện với người có liên quan

các bên liên quan tại PrimeBuy.

Sau khi thảo luận, các bên liên quan

đã xác nhận sự nghi ngờ của chúng tôi

cột ID trong

bảng sản phẩm thực sự

tương ứng với mã sản phẩm.

Từ sự phân tích này, nó

trở nên rõ ràng rằng

Power BI tạo kết nối

dựa trên tên của

các cột chung.

Trong trường hợp này, kể từ khi

tên đã khác nhau,

Power BI không tự động

tạo kết nối

giữa các tờ giấy.

Để khắc phục vấn đề này và

có được những hiểu biết có ý nghĩa,

chúng ta cần sửa thủ công

các mối quan hệ

giữa các bảng này.

Để làm được điều đó, hãy đi

quay lại Mô hình

Xem phần trong power

BI và chọn

Tab Mối quan hệ được quản lý

từ phần ribbon trên cùng.

Khi một tab mới mở ra,

bấm vào nút mới để

tạo ra một mối quan hệ mới.

Trong phần Tạo mối quan hệ

hộp thoại,

chọn một trong những

các bảng, giả sử,

bảng Lệnh bán hàng

từ danh sách thả xuống.

Bây giờ chọn cột chung,

đó là mã sản phẩm trong

bảng lệnh bán hàng.

Ở bước tiếp theo, chọn

bàn thứ hai,

đó là bảng sản phẩm

từ danh sách thả xuống,

và chọn cột chung,

đó là cột ID trong trường hợp này,

bạn hẳn đã quan sát thấy điều đó

Power BI tự động

đã phát hiện kiểu quan hệ

dưới phần cardinality.

Chúng ta sẽ nói về điều này

loại mối quan hệ muộn hơn một chút.

Bây giờ hãy nhấn nút Được rồi

nút để thiết lập

mối quan hệ

và bấm vào Đóng.

Với điều này, chúng tôi đã thành công

kết nối hai bảng dựa trên

trên cột chung.

Bạn có thể thấy một cái mới

kết nối đã được tạo

giữa tờ sản phẩm và

phiếu đặt hàng bán hàng

trong chế độ xem mô hình.

Bây giờ mối quan hệ đó

được thành lập,

chúng ta có thể quay lại báo cáo

vài phần và quan sát

biểu đồ thanh như thế nào

tự động cập nhật,

nhưng vẫn có điều gì đó thiếu sót.

Như có thể thấy từ

biểu đồ sản phẩm đọc có

thứ tự cao bất thường

số lượng so với

các sản phẩm khác mà

trông không có ý nghĩa.

Hãy đi đến gốc rễ

của vấn đề và

nhìn vào thứ tự

số lượng để đọc.

Phiếu đặt hàng bán hàng sẽ có

mã sản phẩm và chúng tôi có thể

tìm mã sản phẩm liên quan

số lần đọc từ bảng sản phẩm.

Hãy hướng tới

xem dữ liệu và chọn

Bảng sản phẩm và nhấp vào

thả xuống cho

tên sản phẩm

để lọc các lần đọc sản phẩm.

Khi bạn nhấp vào được,

chúng tôi nhận được ID cho

đọc, đó là 27.

Bây giờ đi bán hàng

tờ đơn đặt hàng để xem xét

tương ứng

số lượng đặt hàng cho

mã sản phẩm 27

bằng cách sử dụng một bộ lọc.

Hãy sắp xếp các giá trị trong

cột số lượng đặt hàng

theo thứ tự giảm dần,

và kiểm tra giá trị đầu tiên.

Ở đây chúng ta thấy một

số lượng cao bất thường.

Giá trị này tính bằng triệu triệu.

Điều này không thể đúng được.

Bây giờ chúng ta có

đã xác định được vấn đề

hãy sửa nó.

Sau khi thảo luận với

nhóm PrimeBuy,

nó đã được hiểu rằng

phạm vi số lượng cho mỗi

đặt hàng tại PrimeBuy

thay đổi từ 1-10.

Hãy loại bỏ tất cả

các đơn đặt hàng ở đâu

số lượng không đáp ứng

các tiêu chí đã xác định.

Để làm điều này, chúng ta hãy đi đến

tùy chọn dữ liệu được chuyển đổi từ

tab Trang chủ và điều hướng

vào bảng Đơn đặt hàng bán hàng.

Hãy điều hướng đến Đơn hàng

menu thả xuống cột số lượng

và dưới Số

Tùy chọn bộ lọc,

chọn giữa tùy chọn để chuyển tiếp

một phạm vi chấp nhận được

giá trị số lượng đặt hàng.

Khi bạn đã nhập vào phạm vi,

nhấn Được rồi để áp dụng.

Để hoàn thiện những thay đổi trong

Trình soạn thảo truy vấn mạnh mẽ hãy

bấm vào Đóng và

Áp dụng như bình thường để

xem liệu điều đó có khắc phục được không

biểu đồ trong chế độ xem báo cáo.

Hãy chuyển sang chế độ xem báo cáo,

và chúng tôi thấy nó có.

Điều này có ý nghĩa bây giờ.

PrimeBuy hiện đã biết

phụ kiện là của họ

sản phẩm phổ biến nhất,

tiếp theo là cocktail

ly và đĩa.

Đây là một giá trị

cái nhìn sâu sắc cả cho

việc quản lý và

hội đồng quản trị của PrimeBuy.

Trong video này, chúng tôi

đã giúp PrimeBuy tham gia

xác định và thiết lập

các mối quan hệ trong dữ liệu.

Chúng tôi đã thấy một cái giếng

mối quan hệ được xác định

cho phép chúng ta trực quan hóa dữ liệu

trên nhiều bảng và

tạo thuận lợi cho việc tạo ra

những hình ảnh trực quan có ý nghĩa.

Vì vậy, việc dành thời gian để

hiểu

kết nối giữa

tờ giấy rất quan trọng

để khai thác

toàn bộ tiềm năng của

Chế độ xem mô hình dữ liệu.

Bây giờ trong video tiếp theo,

chúng ta sẽ đi sâu hơn vào

mô hình mối quan hệ.

Chúng ta sẽ hiểu một số

các thuật ngữ liên quan đến nó và

cũng hiểu cái gì

các đường kết nối

giữa các tờ đại diện.