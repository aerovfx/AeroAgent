# 06 xử lý-thiếu-giá trị-phần 1

---

Sau khi dữ liệu được kết hợp và

tất cả các cột đều ở trong

một khung dữ liệu duy nhất,

chúng ta sẽ xem xét từng cột

cá nhân và quyết định

những cách tốt nhất để điều trị chúng.

Những cách điều trị khác nhau có thể

bao gồm việc xóa cột

nếu phần lớn

giá trị bị thiếu,

xóa các hàng hoặc quan sát

với những giá trị còn thiếu,

đổ lỗi cho sự thiếu sót

các giá trị có giá trị trung bình, trung vị,

chế độ hoặc giá trị liên quan khác

theo sự hiểu biết của doanh nghiệp.

Ngoài ra, còn có

có thể là những lúc chúng ta có thể

điền dữ liệu trước đó

giá trị hoặc giá trị tiếp theo.

Bây giờ hãy nhảy tới Sao Mộc

Sổ ghi chép và xem

chúng ta sẽ như thế nào

xử lý các giá trị còn thiếu trong

khung dữ liệu tập trung dữ liệu.

Hãy chắc chắn rằng bạn chạy tất cả

tế bào trước khi bạn bắt đầu.

Đầu tiên, chúng ta hãy sử dụng

tính năng isnull để tìm

các giá trị null hoặc bị thiếu trong

tập dữ liệu và thêm bằng cách sử dụng.sum.

Chúng tôi thấy có rất nhiều

thiếu giá trị ở nhiều cột,

hãy giải quyết chúng từng cái một,

bắt đầu bằng đơn giá.

Suy nghĩ ban đầu

có thể quy kết

các giá trị null trong

đơn giá bằng 0,

nhưng nó không có ý nghĩa vì

ID SKU có web

lưu lượng truy cập lớn hơn 0,

và không có công ty thương mại điện tử nào

sẽ bao giờ hiển thị

một sản phẩm mà công ty bán

mà không hiển thị bất kỳ giá nào.

Kịch bản duy nhất mà

giá sẽ được ẩn là khi

công ty đang chạy

một số khuyến mãi hoặc sản phẩm

đã bị ngừng hoạt động.

Vì chúng tôi không có

thông tin về điều này,

chúng tôi sẽ buộc tội

giá trị null còn lại

với doanh số trung bình

của từng phân khúc.

Nhưng trước hết chúng ta cần tìm

tất cả ID SKU mà

đơn giá có giá trị null.

Để chắc chắn hơn, chúng ta hãy sử dụng

một vòng lặp để tính toán

tỷ lệ giá trị còn thiếu

ở cột đơn giá

mỗi ID SKU duy nhất có trong

khung dữ liệu tập trung dữ liệu.

Việc này chỉ cần thực hiện đối với

tất cả ID SKU bị thiếu

giá trị tính theo đơn giá.

Trong trường hợp ID SKU cụ thể có

ít nhất một trường hợp trong đó

đơn giá hiện có,

chúng ta có thể quy kết nó với

giá trị đó cho

ID SKU cụ thể.

Hãy tiếp tục và

chạy tế bào này.

Ở đây, đối với tất cả

ID SKU có

ít nhất một giá trị còn thiếu

ở cột đơn giá

đơn giá xuất hiện xuyên suốt

ID SKU cụ thể.

Bây giờ chúng ta có thể đơn giản quy kết

tất cả các giá trị với

trung vị dựa trên phân khúc.

Bây giờ hãy kiểm tra giá trị rỗng

giá trị ở cột đơn giá.

Chúng ta có thể thấy bây giờ có

không có giá trị null trong

cột đơn giá.

Bây giờ hãy giải quyết

cột đánh giá,

điều quan trọng cần lưu ý là

tất cả các cột xếp hạng

có tính tích lũy,

điều đó ngụ ý rằng nếu có

đang thiếu các giá trị cho

một tuần cụ thể,

nó chỉ ra rằng

không có xếp hạng mới nào

được cung cấp cho SKU đó

ID trong tuần đó.

Xét về mặt tích lũy

bản chất của các cột này,

thích hợp nhất

phương pháp tính toán

những giá trị còn thiếu

sẽ được sử dụng

số lượng xếp hạng tích lũy

tính đến tuần trước.

Cách tiếp cận này đảm bảo rằng

tổng số xếp hạng vẫn còn

nhất quán trong nhiều tuần trong đó

không có xếp hạng mới nào được ghi lại

cho một ID SKU cụ thể.

Vì vậy, chúng ta sẽ quy kết

cột đánh giá cho

mỗi ID SKU sử dụng

số lượng xếp hạng tích lũy từ

tuần trước của

ID SKU cụ thể đó.

Chúng tôi bắt đầu bằng việc tạo

một danh sách có tên cột

của tất cả năm xếp hạng.

Bây giờ hãy thực hiện điền chuyển tiếp

để gán các giá trị còn thiếu của

mỗi ID SKU có

tích lũy của tuần trước

xếp hạng cho ID SKU đó.

Chúng tôi nhóm dữ liệu

tập trung theo ID SKU

và sử dụng hàm Lamda

để thực hiện điền về phía trước.

Hãy kiểm tra

giá trị null nữa.

Vâng, chúng ta có thể thấy điều đó

ngay cả sau khi điền về phía trước,

có giá trị null.

Điều này chỉ ra rằng lần đầu tiên

giá trị của các cột xếp hạng

đối với một ID SKU cụ thể là

null và do đó họ

đã không được lấp đầy.

Chúng tôi sẽ chỉ thay thế nó

bằng 0 như nó chỉ ra

rằng chưa có xếp hạng nào

cho ID SKU cụ thể đó.

Hãy kiểm tra những gì còn thiếu

các giá trị một lần nữa.

Chúng ta có thể thấy tất cả điều đó

những giá trị còn thiếu

đã bị buộc tội trong

tất cả các cột xếp hạng.

Bây giờ chúng ta hãy kiểm tra

các cột sau;

số lượng hình ảnh, số lượng đạn,

số tiêu đề, và

độ dài mô tả

Trong khi xử lý trước

dữ liệu trong các video trước,

chúng tôi hiểu rằng ở trên

bốn cột sẽ có

cùng một giá trị cho tất cả các

ngày cho một ID SKU cụ thể.

Nhưng chúng ta cũng phải tính đến

tính đến cơ hội của

bất kỳ thay đổi nào về giá trị của

các cột sau

cho một ID SKU cụ thể.

Ví dụ: có thể đối với SKU 1040,

số lượng hình ảnh là

tăng từ 3-5.

Để tính đến

sự thay đổi trong

giá trị cho một ID SKU nhất định,

tốt hơn là nên quy trách nhiệm

những giá trị này với

trung bình ở cấp ID SKU.

Hãy tạo một danh sách với

tên cột sẽ là

chứa đầy trung vị.

Bây giờ hãy sử dụng vòng lặp for để áp đặt

các cột này có SKU

Giá trị trung bình dựa trên ID.

Bạn có thể bỏ qua cảnh báo này,

bây giờ hãy kiểm tra

thiếu giá trị một lần nữa.

Bạn sẽ nhận thấy rằng

vẫn còn

ba giá trị null trong

tập dữ liệu và nó

không có ý nghĩa.

Lý do cho điều đó là chúng tôi

đã nhóm các

dữ liệu có ID SKU,

và nhóm đó hoặc ID SKU,

có giá trị null xuyên suốt

bốn cột này.

Hãy quy kết nó với

trung bình toàn cầu của

toàn bộ cột.

Bạn cũng có thể thử

quy kết nó với

giá trị trung bình dựa trên

phân khúc của sản phẩm.

Bây giờ chúng ta hãy kiểm tra

các giá trị còn thiếu.

Với điều đó, chúng tôi đã quy kết

các giá trị null trong số lượng hình ảnh,

số lượng đạn, số lượng tiêu đề,

và độ dài mô tả.

Bây giờ hãy xử lý số

cụm từ tìm kiếm duy nhất

và sân tìm kiếm không phải trả tiền.