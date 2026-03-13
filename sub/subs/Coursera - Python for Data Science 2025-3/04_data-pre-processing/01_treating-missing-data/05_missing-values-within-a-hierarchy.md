# 05 giá trị thiếu trong hệ thống phân cấp

---

Bây giờ chúng ta hãy đến với

phần phức tạp.

Xử lý các giá trị còn thiếu trong

cột đơn giá là

khá gần như tầm thường.

Chúng tôi vừa xóa cột,

nhưng điều này còn hơn thế nữa

phức tạp khi chúng tôi đến

sang bốn cột còn lại

có dữ liệu bị thiếu,

cụ thể là ngành, loại,

phân khúc và thương hiệu.

Lý do điều này phức tạp

là bởi vì những cột này

không độc lập.

Có một hệ thống phân cấp

mối quan hệ.

Nói cách khác, các hạng

thuộc các ngành,

phân khúc nằm trong danh mục,

và thương hiệu nằm trong các phân khúc.

Chúng tôi không thể chữa trị

chúng một cách độc lập

và chỉ quy kết dựa trên,

giả sử, chế độ

của từng cột.

Điều này có thể có ý nghĩa hơn nếu tôi

tạo nên một ví dụ

Nghe có vẻ như thế này.

Hãy nói rằng có

hai thuộc tính,

một cái gọi là vùng và

một cái gọi là đất nước.

Không có trong tập dữ liệu này,

trong một trường hợp giả định.

Giả sử có hai

khu vực, Châu Âu và Châu Á.

Ở mỗi vùng có

có nhiều quốc gia.

Bây giờ, nếu bạn có một

giá trị còn thiếu trong

cột quốc gia, giả sử,

và phổ biến nhất

quốc gia trong tập dữ liệu của chúng tôi là,

hãy nói ví dụ,

Nhật Bản trên toàn bộ dữ liệu.

Giả sử giá trị chế độ

đất nước là Nhật Bản,

và bạn tìm thấy một cái còn thiếu

giá trị trong nước,

chúng ta có thể bị cám dỗ

chỉ để thay thế nó

với Nhật Bản vì

đó là điều phổ biến nhất,

nhưng sau đó chúng ta cần phải xem xét

cột khu vực và nếu

khu vực là Châu Âu,

chúng ta không thể thay thế

đất nước với

Nhật Bản vì có

một hệ thống phân cấp ở đó.

Tập dữ liệu này lớn gấp bốn lần

phức tạp vì có

hệ thống phân cấp bốn cấp,

nhưng hãy bắt đầu thôi,

hãy sắp xếp nó ra.

Đầu tiên chúng ta hãy quan sát

những gì chúng ta thấy trong

tập dữ liệu và trợ giúp

thiết kế một chiến lược.

Một điều phức tạp là chúng tôi đã thấy rằng

chất lỏng phân đoạn thực sự

được liệt kê dưới hai

danh mục khác nhau,

bột giặt

và chất làm mềm vải.

Chúng tôi viết một phần

mã để tìm kiếm

tên phân đoạn và sau đó là

hạng tương ứng.

Chúng sẽ mơ hồ vì

từ đó chất lỏng như

một đoạn đi vào

hai nơi khác nhau.

Khi chúng ta đi thay thế

giá trị còn thiếu trong thương hiệu,

chúng ta sẽ phải đối mặt với những vấn đề tương tự.

Để sắp xếp thứ này, chúng ta hãy

làm một việc

Hãy đổi tên chất lỏng thành

nước giặt khi

danh mục là bột giặt,

và chất lỏng vải

khi danh mục là

chất làm mềm vải.

Đây là một điều chúng tôi sẽ làm.

Tuy nhiên, có một nhược điểm.

Chúng ta phải làm gì nếu

danh mục bị thiếu?

Sau đó chúng ta cần phải đi đến phần làm thế nào

chúng ta biết có nên giặt đồ không

chất lỏng hoặc chất lỏng vải.

Sau đó chúng ta hãy đi đến

thương hiệu và xem nếu

tên thương hiệu là của

chất tẩy rửa

như Tide hay Gain,

hoặc nó là một loại vải

nước xả như Downy hay Comfort.

Sau đó chúng tôi sẽ sử dụng thông tin đó

để thay thế từ chất lỏng.

Như bạn có thể thấy, đó là

đã nhận được

phức tạp và

sau đó nó trở nên tồi tệ hơn.

Chúng tôi có ba hồ sơ

thể loại ở đâu,

phân khúc và thương hiệu

đều bị thiếu.

Sau đó chúng ta đi đến Khu vực,

và ở đó chúng ta sẽ

có lẽ sử dụng chế độ này.

Hãy thực hiện việc này bằng cách

từng bước một.

Hãy bắt đầu với phân đoạn và xem

có bao nhiêu khác nhau

chúng ta có những phân đoạn nào và

chúng ta có bao nhiêu cái mỗi cái?

Chúng tôi có một cái gì đó như,

Tôi định nói điều này có vẻ

khoảng 20 đoạn

và đây là một số mục

cho từng giá trị đó.

Như bạn có thể thấy,

phổ biến nhất là

lỏng với 7.200 mục.

Nhưng chúng ta biết chất lỏng đó

thực ra có hai loại.

Bây giờ chúng ta hãy đi đến chuyên mục

và nhìn vào chế độ.

Danh mục phổ biến nhất

là bột giặt.

Bây giờ hãy viết một hàm

để thực hiện việc thay thế này

từ chất lỏng với

nước giặt

hoặc chất lỏng vải

dựa trên logic chúng ta

vừa nói tới.

Đây là một chức năng do người dùng xác định.

Tôi bắt đầu với def,

tên của chức năng,

giả sử người dùng xác định

tên và tham số.

Tôi sẽ cho nó một hàng

tại một thời điểm từ khung dữ liệu của tôi.

Tôi chỉ đang sử dụng trình giữ chỗ

tên biến được gọi là hàng.

Bạn có thể đặt X hoặc Y hoặc A hoặc B

hoặc C ở đây, không thành vấn đề.

Tôi đang sử dụng hàng vì

nó sẽ như vậy

một hàng từ dữ liệu

khung. Đây là logic.

Nếu trong trường hợp cụ thể đó

hàng phân khúc là

chất lỏng, sau đó lồng nhau nếu.

Hãy nhớ với Python, bạn đặt

một dấu chấm phẩy ở đây còn bạn

thụt dòng tiếp theo.

Nếu kết thúc bằng dấu chấm phẩy,

bất cứ điều gì rơi vào

if được thụt lề,

thụt lề là quan trọng

hãy nhớ trong Python,

không giống như nhiều ngôn ngữ khác.

Bên dưới nếu chúng ta có một cái khác nếu,

nếu đoạn đó là chất lỏng,

sau đó nếu danh mục hàng

là bột giặt,

sau đó chúng ta sẽ trả lại đồ giặt

chất lỏng, nhưng hãy nhớ,

điều này cũng có thể bị thiếu,

vì vậy để đề cập đến khả năng đó,

chúng tôi nói nếu thương hiệu hàng bị ràng buộc

hoặc hàng thương hiệu đã đạt được.

Đây là hai

thương hiệu mà bạn

có thể có dưới

chất tẩy giặt.

Nếu chúng ta biết đó là một

bột giặt,

tuyệt vời, nhưng nếu chúng ta

không biết điều đó,

chúng tôi nhìn vào thương hiệu.

Trong tất cả những trường hợp này,

chúng tôi trả lại giá trị

nước giặt.

Khác nếu, Elif có nghĩa là khác nếu,

nếu điều này không đúng

chúng ta sẽ đến đây

Đó là một câu lệnh if khác.

Nếu danh mục là

nước xả vải

hoặc nhãn hiệu là Downy hoặc Comfort,

chúng tôi trả lại chất lỏng vải.

Nếu cả hai điều này đều không đúng,

chúng tôi sẽ trả lại nước giặt

bởi vì đó là giá trị phương thức.

Ở đó chúng tôi đang dùng

đoán một chút.

Một phỏng đoán rất có tính toán

bởi vì chúng tôi đã đề cập gần như

mọi tình huống xảy ra ở đây.

Đây là những gì chúng tôi sẽ làm.

Sau đó chúng tôi trả lại phân đoạn này.

Điều này bây giờ sẽ mất

giá trị trong đoạn.

Đây là một chức năng do người dùng xác định.

Trước tiên chúng ta hãy chạy cái này

rằng điều này bây giờ trở thành

một chức năng có sẵn để

chúng tôi trong thời gian còn lại

phiên Python này.

Thay thế đoạn chất lỏng là

bây giờ là một hàm Python.

Nó được viết bởi bạn,

nó sẽ chỉ hoạt động cho đến khi

Tôi đóng cuốn sổ này lại,

nhưng trong khoảng thời gian đó,

bây giờ nó là một hàm Python.

Bây giờ chúng ta hãy áp dụng

chức năng này sử dụng

chức năng áp dụng từ gấu trúc,

rất hữu ích để áp dụng một cụ thể

chức năng cho một tập dữ liệu.

Tôi định nói, hãy lấy

cột này và

áp dụng chức năng này.

trục=1 vì tôi

sẽ thực hiện hàng này bằng cách

row, Hãy chạy cái này.

Những gì chúng tôi thực sự đã làm ở đây

được gọi là chức năng này

31.100 và đôi khi một lần trong

từng hàng và thực hiện

hoạt động đó

nó kêu gọi chúng ta làm.

Bây giờ bạn thấy chất lỏng

đã bỏ học,

chất lỏng vải và giặt

chất lỏng đã thay thế nó.

Họ là chính họ

mỗi cái đều khá phổ biến,

4.000 và đóng

tới 3.000 mục,

nhưng chúng tôi đã giải quyết được một trong

rất nhiều vấn đề mà

chúng tôi đã quan sát thấy trong dữ liệu.

Chúng ta sẽ tiếp tục việc này

bài học ở video tiếp theo.