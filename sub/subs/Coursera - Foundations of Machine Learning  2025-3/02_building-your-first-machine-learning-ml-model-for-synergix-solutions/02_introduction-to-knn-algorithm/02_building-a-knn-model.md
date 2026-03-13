# 02 mô hình tòa nhà

---

Bây giờ bạn có một

trực giác của KNN,

hãy để chúng tôi hiểu các thuật toán

hoạt động bên trong trong video này

với một ví dụ đơn giản.

Để hiểu KNN tốt hơn,

chúng ta hãy nhìn vào

một biểu đồ phân tán của

hai đặc điểm từ

tập dữ liệu tổng hợp.

Cốt truyện này ở đây là từ

một tập dữ liệu đã được làm sạch

chúng tôi đã chuẩn bị trong

các video trước đó.

Chúng tôi đang xem xét

hai tính năng ở đây,

đơn giá và lưu lượng truy cập trang.

Trong trường hợp này, chúng tôi

biến mục tiêu

đơn vị được bán lớn hơn

1.000 Nó được đại diện bởi

màu xanh và màu đỏ.

Trong đó màu xanh có nghĩa là đơn vị

được bán lớn hơn

1.000 và màu đỏ có nghĩa là

điều ngược lại.

Bây giờ hãy nói rằng có

một điểm dữ liệu mới.

Chúng tôi đang hiển thị nó ở đây

với một chữ thập màu vàng.

Điểm này có đơn giá là

33 và lưu lượng truy cập trang là 7.200.

Bây giờ chúng tôi muốn dự đoán nếu

sản phẩm đặc biệt này,

với trang đã cho

lưu lượng và đơn giá

sẽ bán nhiều hay ít

hơn 1.000 đơn vị.

Chúng ta sẽ làm điều này bằng cách tìm kiếm

tại các nước láng giềng gần nhất của nó.

Chúng tôi sẽ thực hiện một

dự đoán dựa trên

lớp đa số,

những người hàng xóm gần nhất.

Nhưng sau đó câu trả lời cho

điều đó sẽ phụ thuộc vào

số lượng hàng xóm gần nhất

bạn chọn nhìn vào.

Để dễ dàng, chúng ta hãy nhìn vào

một đại diện thu phóng chính xác

của đồ thị.

Nếu số lượng

hàng xóm gần nhất

chúng tôi đang xem xét là một,

thì màu đỏ sẽ là đẳng cấp của bạn

cho điểm dữ liệu mới.

Tương tự, nếu chúng ta nhìn vào

ba người hàng xóm gần nhất,

chúng ta sẽ lại nhận được

màu đỏ như lớp.

Nếu chúng ta nhìn vào bảy trong số

những người hàng xóm gần nhất,

thì lớp sẽ có màu xanh.

Lúc này chúng ta đã hiểu

dự đoán này một cách trực quan.

Một cách tiếp cận tốt hơn thế này

sẽ là để tính toán

những khoảng cách,

tất cả các điểm đến điểm mới của chúng tôi

và tìm những người hàng xóm gần nhất.

Vì tập dữ liệu của chúng tôi có

khoảng 19.000 điểm dữ liệu,

chúng ta sẽ phải tính toán

khoảng 19.000 khoảng cách.

Hãy giả sử khoảng cách

thu được như hình

trong danh sách dưới đây.

Bây giờ chúng ta sẽ sắp xếp danh sách

những khoảng cách này tăng dần

thứ tự khoảng cách,

và chọn cái ngắn nhất đầu tiên

khoảng cách từ danh sách.

Bây giờ hãy nói số lượng

hàng xóm được đại diện bởi k,

và k bằng năm.

Một lần nữa, hãy lấy

nhìn vào hình đã phóng to

phiên bản của biểu đồ,

vì vậy ở đây hãy đánh dấu năm

láng giềng gần nhất của điểm này.

Một khi chúng tôi có

hàng xóm gần nhất,

bước cuối cùng là làm

dự đoán về dữ liệu

điểm của hàng xóm.

Chúng ta sẽ áp dụng chế độ

nhãn của

hàng xóm gần nhất.

Ở đây chúng tôi có ba màu đỏ

điểm và hai điểm màu xanh.

Trong trường hợp này, chế độ

sẽ có màu đỏ.

Chúng ta có thể kết luận rằng

điểm mới này trong

dữ liệu thử nghiệm sẽ có

số sản phẩm bán được dưới 1.000

và sẽ được phân công

đến màu đỏ.

Vấn đề chúng tôi

đã giải quyết ngay bây giờ cho đơn vị

được bán bằng KNN là một

vấn đề phân loại,

đó là lý do tại sao chúng tôi đã chỉ định

sang phiên bản mới.

Nếu vấn đề là một

vấn đề hồi quy,

thì chúng ta sẽ chỉ định

ý nghĩa của hàng xóm KNN

trường hợp mới.

Nhưng đợi một chút.

Trong khi chúng tôi thực hiện tất cả các bước này,

bạn chắc chắn phải có

một câu hỏi trong đầu bạn

Làm thế nào hoặc tại sao chúng ta đã

chọn K là năm?

Chúng tôi sẽ trả lời điều này

trong video tiếp theo.