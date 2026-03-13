# 03 giới thiệu về dbscan

---

Mặc dù chúng tôi

được xây dựng thành công

mô hình không giám sát của chúng tôi

sử dụng phân cụm theo thứ bậc,

một trong những nhược điểm lớn

của thuật toán

là nó chỉ phù hợp

cho các tập dữ liệu nhỏ.

Điều này là bởi vì nó là

một cách tính toán

thuật toán đắt tiền.

Tìm các cụm bằng cách sử dụng

một dendrogram cũng có thể

trở nên khá khó khăn khi

số lượng mẫu tăng lên.

Trong một kịch bản thế giới thực,

tập dữ liệu có thể lớn hơn nhiều so với

tập dữ liệu tổng hợp mà chúng tôi

đã được sử dụng cho đến nay.

Một nhược điểm lớn khác

của mô hình HCA là

rằng nó nhạy cảm với

các ngoại lệ giống như k-mean.

Thuật toán này có thể buộc

cung cấp các điểm dữ liệu

thành các cụm.

Để khắc phục vấn đề này, hãy thay đổi

sự tập trung của chúng tôi vào

thuật toán thứ ba,

điều đó thật tuyệt vời

phát hiện các ngoại lệ.

Không gian dựa trên mật độ

phân cụm

ứng dụng có tiếng ồn

hoặc đơn giản là DBSCAN.

Không giống như k-mean có độ lệch

để tạo lồi

cụm hình,

DBSCAN có thể hình thành

các cụm có hình dạng tùy ý.

Việc này được thực hiện dựa trên

mật độ của mẫu

Đầu tiên chúng ta hãy hiểu

hoạt động của thuật toán

rồi tiến hành xem xét

ở hiệu suất của nó.

Chúng tôi sẽ sử dụng nó trên

cùng một tuyên bố vấn đề

của tập dữ liệu tổng hợp.

Giải pháp tổng hợp

đã tìm thấy điều đó

tiếp thị của nó

chiến lược dựa trên

các phân khúc hiện có

không hiệu quả lắm.

Họ muốn thử thời đại mới

tiếp thị trực tuyến trọn gói

chiến lược mà

sẽ yêu cầu họ phải

nhóm sản phẩm tương tự

cùng nhau không phân biệt

của phân khúc.

Hãy nhìn vào những điều thô này

điểm dữ liệu không được phân cụm.

Quan sát số lượng

điểm gần nhau.

Hãy chọn một cách dày đặc

điểm nằm,

ví dụ như điểm đỏ này.

Tiếp theo, hãy vẽ một vòng tròn màu xanh

xung quanh nó và xem làm thế nào

nhiều điểm nó trùng nhau.

Vòng tròn màu xanh này ở đây

chồng lên nhau tám điểm,

một phần hoặc toàn bộ.

Chúng ta có thể nói rằng điểm đỏ này

gần với tám điểm khác.

Bán kính của màu xanh này

vòng tròn do người dùng xác định,

và nó được gọi là

Eps hoặc Epsilon.

Đó là tham số đầu tiên của

Thuật toán DBSCAN được sử dụng

để phân cụm dữ liệu.

Tham số Eps xác định

bán kính của

lân cận xung quanh một điểm.

Trong một kịch bản nơi

khoảng cách giữa

hai điểm là ít hơn

hơn hoặc bằng Eps,

số điểm là

được coi là hàng xóm.

Tương tự, hãy xem

tại điểm đỏ này,

vòng tròn màu xanh cho

điểm này một phần

hoặc chồng chéo hoàn toàn

bảy điểm khác,

biến họ thành hàng xóm của mình.

Một lần nữa, điểm đỏ này

gần với tám điểm khác,

và điểm đỏ này ở gần

đến ba điểm khác,

nhưng điểm đỏ này

ở đây không gần

bất kỳ điểm nào khác bởi vì

vòng tròn màu xanh không

chồng lên bất kỳ điểm nào khác.

Tương tự, chúng ta có thể xem xét

mỗi điểm để tìm thấy nó

hàng xóm gần nhất.

Chúng ta có thể định nghĩa các điểm có

hơn bốn gần

hàng xóm làm mẫu cốt lõi,

vậy số 4 trong trường hợp này là

mẫu tối thiểu

hoặc min_samples.

Min_samples có thể được định nghĩa là

số lượng tối thiểu của

những mẫu nên

nằm trong khoảng cách Eps cho

một mẫu cần được xem xét

một mẫu lõi.

Trong tập dữ liệu của chúng tôi,

tất cả những thứ này đều có màu đỏ

mẫu có thể được coi là

mẫu cốt lõi vì chúng là

ít nhất là gần với

bốn mẫu khác.

Tất cả các điểm khác

được tô màu xanh lam là

các mẫu không cốt lõi vì chúng

không thỏa mãn điều kiện.

Một khi các mẫu lõi

được xác định,

tiếp theo thuật toán

tiến hành ngẫu nhiên

chọn một mẫu lõi và

gán nó vào một cụm.

Sau đó các mẫu lõi trong

màu đỏ gần

mẫu được chọn là

cũng được thêm vào cụm.

Sau đó, điểm cốt lõi là

gần gũi hơn với nhóm

các mẫu cũng tham gia

cụm và như vậy.

Nhưng đợi một chút,

ở đây chúng ta thấy rằng ở đó

là ba mẫu cốt lõi

và một mẫu không cốt lõi

gần với

một cụm đang phát triển.

Trong một kịch bản như vậy,

chỉ các mẫu cốt lõi

được thêm vào

cụm bây giờ,

cuối cùng chúng tôi sẽ thêm

các mẫu không lõi,

nhưng hiện tại, chúng ta chỉ tiếp tục

để thêm các mẫu cốt lõi.

Cuối cùng, tất cả các mẫu cốt lõi

gần cụm đang phát triển

được thêm vào cụm đầu tiên

và được sử dụng để mở rộng nó.

Bây giờ chúng tôi không có

nhiều mẫu cốt lõi hơn

để mở rộng cụm đầu tiên,

chúng tôi thêm tất cả những thứ không cốt lõi

các mẫu gần

các mẫu cốt lõi bên trong

khoảng cách Eps tới

cụm đầu tiên.

Ví dụ, phần không cốt lõi này

mẫu ở đây gần rồi

đến một mẫu lõi trong

cụm đầu tiên bên trong

khoảng cách Eps,

vì vậy chúng tôi thêm nó vào

cụm đầu tiên.

Tuy nhiên, vì điều này

mẫu mới được thêm vào

là một mẫu không cốt lõi,

nó sẽ không được sử dụng nữa

để mở rộng cụm.

Điều đó có nghĩa là điều này

mẫu sẽ không được

đã tham gia vào việc này

cụm vì nó là

không gần với bất kỳ

các mẫu cốt lõi bên trong

khoảng cách Eps.

Tương tự, tất cả các phần không cốt lõi

mẫu gần

một mẫu cốt lõi từ

cụm đầu tiên là

được thêm vào cụm này.

Bây giờ hãy chuyển trọng tâm của chúng ta sang

lõi còn lại

các mẫu được

không liên quan

với cụm này.

Vì không có mẫu cốt lõi nào trong số này

gần với cụm đầu tiên,

chúng tạo thành cụm thứ hai

vì họ ở gần nhau

với nhau.

Các mẫu không lõi gần

cụm thứ hai là

cũng được thêm vào nó dựa trên

trên các tiêu chí trước đó.

Cuối cùng, thuật toán

đã hoàn thành việc phân công

tất cả các mẫu lõi và

mẫu không lõi để

các cụm khác nhau.

Bây giờ tất cả các mẫu còn lại

không liên quan

với một trong hai cụm

được gọi là ngoại lệ.

Những ngoại lệ này tạo thành một cụm

của riêng họ để họ

có thể được xác định.

Thuật toán DBSCAN là một trong những thuật toán

phân cụm tốt nhất

thuật toán để

xác định các mẫu ồn ào như vậy.

Lưu ý rằng hai tham số,

Eps và min_samples,

là công cụ trong

xác định các mẫu cốt lõi,

và cuối cùng là các cụm.

Số mẫu tối thiểu cao hơn hoặc Eps thấp hơn

chỉ ra rằng chúng tôi muốn

các cụm có

mật độ cao hơn.

Bạn có để ý rằng chúng tôi

không cần phải chỉ định

số lượng cụm

trong thuật toán DBSCAN?

Ngoài ra, chúng tôi không cần phải

chọn số

của các cụm từ

một dendrogram như chúng tôi đã phải làm

làm cho việc phân cụm thứ bậc.

Tôi chắc chắn bạn có

một sự hiểu biết rõ ràng về

hậu trường của

thuật toán DBSCAN.

Bạn cũng hiểu

thông số khác nhau

tham gia vào

Thuật toán DBSCAN.

Hẹn gặp lại bạn sau

video nơi chúng tôi áp dụng

thuật toán DBSCAN cho

tuyên bố vấn đề tổng hợp.