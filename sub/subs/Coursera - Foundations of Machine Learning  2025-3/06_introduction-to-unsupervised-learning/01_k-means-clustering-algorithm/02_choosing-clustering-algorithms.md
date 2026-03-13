# 02 thuật toán chọn-phân cụm

---

Xin chào và chào mừng trở lại.

Trong video trước, bạn đã

một cái nhìn thoáng qua về

phát biểu vấn đề.

Chúng tôi thiết lập rằng chúng tôi sẽ sử dụng

kỹ thuật phân cụm

học máy không giám sát

để giải quyết vấn đề này.

Nhưng cái gì làm

phân cụm thực sự làm gì?

Bạn sẽ có

chắc chắn đã quan sát

bảng tuần hoàn như thế nào

nhóm phần tử

có tính chất tương tự

thành các nhóm.

Đó là mục tiêu cơ bản

của việc phân cụm

các thuật toán cũng vậy.

Nhóm phân cụm

dữ liệu, tùy theo

giống hoặc như thế nào

chúng không giống nhau.

Các nhóm được tạo bằng cách sử dụng

hai thuộc tính chính.

Trạng thái thuộc tính đầu tiên

rằng tất cả các điểm dữ liệu trong

cụm nên như

tương tự như nhau

khác nhất có thể.

Thuộc tính thứ hai nêu rõ

rằng dữ liệu chỉ ra từ

các cụm khác nhau nên được

càng khác biệt càng tốt

từ nhau.

Chúng ta hãy nhìn vào

các thuật toán phân cụm phổ biến.

Có ba rất phổ biến

các thuật toán được sử dụng để phân cụm.

K-nghĩa, phân cấp

phân cụm và DBSCAN.

Trong phân cụm K-mean,

việc phân nhóm

điểm dữ liệu được thực hiện

xét trọng tâm

của các cụm.

Trong phân cụm theo cấp bậc,

việc phân nhóm được thực hiện dựa trên

về sự giống nhau giữa

các điểm dữ liệu thông qua

sơ đồ phân cấp

được gọi là dendrogram.

Trong DBSCAN, việc nhóm các

điểm dữ liệu được thực hiện dựa trên

về mật độ điểm.

Đừng lo lắng. chúng tôi sẽ

nhìn vào từng cái

các thuật toán này một cách chi tiết

trong các video sắp tới.

Bây giờ, hãy tập trung vào

thuật toán đầu tiên,

thuật toán K-means.

K-mean có lẽ là

phổ biến nhất

thuật toán phân cụm.

Đó là một phương pháp độc quyền của

phân cụm trong đó mỗi điểm dữ liệu

thuộc về một cụm duy nhất.

K trong K-means là viết tắt của

về số lượng nhóm

hoặc cụm chúng tôi muốn

dữ liệu cần phân loại.

Hãy nói rằng chúng ta có

15 điểm này,

và chúng tôi muốn áp dụng

K-có nghĩa là tạo ra

cụm cho những điểm này.

Đây là cách chúng ta có thể làm điều đó.

Bước đầu tiên trong K-mean là

để chọn số cụm,

k. Hãy nói rằng chúng tôi muốn

có ba cụm.

Điều này có nghĩa là K = 3 ở đây.

Tiếp theo, chúng tôi chọn ngẫu nhiên

ba điểm dữ liệu là

trọng tâm cho mỗi cụm.

Trong K-nghĩa mỗi cụm là

được đại diện bởi nó

trung tâm hoặc một trọng tâm.

Đây xanh, vàng

và những vòng tròn màu đỏ

đại diện cho trung tâm chúng ta có

được chọn cho những điều này

cụm ngẫu nhiên.

Một khi chúng ta đã khởi tạo

các trọng tâm,

chúng tôi chỉ định từng điểm cho

cụm gần nhất

trọng tâm dựa trên khoảng cách.

Ở đây bạn có thể thấy điều đó

những điểm gần hơn

tâm màu đỏ là

được gán vào cụm màu đỏ.

Những điểm gần hơn

tâm màu vàng là

được giao cho màu vàng

cụm, v.v.

Bây giờ chúng tôi đã chỉ định

tất cả các điểm để

hoặc cụm,

bước tiếp theo là tính toán

các trung tâm mới dựa trên

các mẫu trong một cụm.

Những trọng tâm mới này

sẽ được sử dụng cho

lần lặp tiếp theo của việc phân bổ

trỏ tới các cụm.

Nếu bạn nhìn kỹ ở đây,

bạn sẽ nhận thấy

đó là điểm màu xanh

bây giờ đã gần hơn với

trọng tâm màu vàng.

Vì vậy, nó sẽ được giao cho

cụm màu vàng trong

lần lặp tiếp theo.

Cũng lưu ý rằng

vì điểm này là

sẽ không còn nữa

một phần của cụm màu xanh,

trọng tâm của

cả màu vàng và

các cụm màu xanh sẽ

thay đổi ở lần lặp tiếp theo.

Một khi các trọng tâm mới

được tạo ra.

Một lần nữa, chúng ta thấy

một điểm dữ liệu khác,

lần này cái màu đỏ ở gần hơn

đến cụm màu xanh bây giờ.

Trong phần tiếp theo

lặp lại, điểm này

sẽ di chuyển đến cụm màu xanh,

và tâm màu đỏ

cũng sẽ thay đổi.

Với việc bổ sung

điểm dữ liệu mới,

tương tự, màu xanh

trọng tâm cũng sẽ thay đổi.

Nhưng chờ đã, khi nào chúng ta nên

dừng việc lặp lại này

trung tâm tính toán

và phân công

trỏ đến từng cụm?

Chúng ta có thể dừng thuật toán khi

điểm dữ liệu dừng lại

thay đổi cụm,

ngay cả sau khi cập nhật

centroid hoặc sau khi cố định

số lần lặp.

Theo mặc định trong scikitlearn's

thực hiện

K-có nghĩa là số mặc định

số lần lặp là 300

Với điều đó, tôi chắc chắn rằng bạn

có sự hiểu biết rõ ràng

về cách thuật toán K-means

cụm điểm dữ liệu.

Với điều này rất thú vị

và thuật toán mạnh mẽ,

chúng tôi sẽ giúp sức mạnh tổng hợp giải quyết

vấn đề của họ trong video tiếp theo.