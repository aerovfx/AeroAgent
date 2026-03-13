# 05 mô hình-hiểu-sử dụng-mô tả-cách tiếp cận

---

Hồi quy tuyến tính đơn giản là

một cách tiếp cận hữu ích để dự đoán

phản hồi dựa trên cơ sở

biến dự báo duy nhất.

Tuy nhiên, trong thực tế,

chúng tôi thường có nhiều hơn

hơn một yếu tố dự đoán.

Ví dụ, trong

tập dữ liệu tổng hợp cho đến nay chúng tôi

đã xem xét mối quan hệ

giữa đế đơn vị

và tốc độ giao thông.

Nhưng chúng tôi cũng có

dữ liệu về đơn giá.

Phân đoạn và nhiều

các biến khác.

Chúng ta có thể muốn biết làm thế nào mỗi

những tính năng này là

liên quan đến đơn vị được bán.

Điều này đưa chúng ta đến một

câu hỏi quan trọng.

Làm thế nào chúng ta có thể mở rộng

phân tích đơn vị

được bán để đáp ứng

những yếu tố dự đoán bổ sung này?

Bạn có thể nghĩ đến việc chạy

hồi quy tuyến tính riêng lẻ

đối với từng yếu tố dự báo.

Tuy nhiên cách này không hiệu quả

bởi vì nó mang lại sự riêng biệt

phương trình cho từng tính năng,

làm cho dự đoán bị phân mảnh

và có thể gây nhầm lẫn.

Để phân tích tốt hơn đơn vị đã bán

với nhiều yếu tố dự đoán,

chúng ta có thể tích hợp tất cả

dự đoán thành một phương trình.

Trong đó x1, x2,

x3, v.v.

là người dự đoán

cho sự độc lập

biến và m1,

m2, v.v., sẽ là

các hệ số tương ứng

đối với từng yếu tố dự đoán.

Mỗi hệ số sẽ đại diện

sự thay đổi trong

biến phản hồi cho

thay đổi một đơn vị

trong bộ dự đoán

giả định tất cả những điều khác

các yếu tố dự đoán được giữ không đổi.

Cuối cùng, C là

đánh chặn tương tự

chúng ta đã thấy một cách đơn giản

hồi quy tuyến tính.

Với sự hiểu biết này,

hãy bắt đầu bằng cách xây dựng

mô hình hồi quy đa tuyến tính

với tính chất miêu tả

tiếp cận đầu tiên.

Hãy mở một cái mới

sổ tay sao Mộc

và xây dựng dựa trên

công việc trước đó.

Chúng ta sẽ bắt đầu bằng cách nhập

những khoản nợ cần thiết trước tiên.

Bây giờ thay đổi thư mục làm việc

đến nơi bạn có

đã lưu trữ tập dữ liệu.

Hãy nhanh chóng tải

tập dữ liệu bây giờ.

Bây giờ sử dụng chức năng thông tin dấu chấm,

chúng ta có thể nhanh chóng kiểm tra

cột và kiểu dữ liệu của chúng.

Một bước quan trọng trong

học máy đang xử lý

dữ liệu phân loại.

Trong phân đoạn dữ liệu của chúng tôi

cột nổi bật như

cột phân loại với

các hạng mục như trang điểm,

dưỡng da, chăm sóc tóc.

Vì những danh mục này

không có bất kỳ đơn đặt hàng nào,

hãy dùng cái nóng nhé

mã hóa thay vì

một bộ mã hóa nhãn để chuyển đổi

chúng thành số.

Hãy kiểm tra kiểu dữ liệu

của tất cả các biến

trong dữ liệu df_encoded bằng cách sử dụng

chức năng loại dấu chấm D.

Chú ý rằng hai cái này

các cột vừa được thêm vào

vào tập dữ liệu vẫn có

các kiểu dữ liệu là Boolean.

Đó là bởi vì chúng tôi

sử dụng mới nhất

phiên bản gấu trúc,

điều này sẽ chuyển đổi chúng

thành các giá trị Boolean.

Chúng ta sẽ chuyển chúng thành

số nguyên sử dụng a

Hàm Lambda.

Chúng tôi sẽ chạy mã

bên dưới để thực hiện tương tự.

Khi thực hiện xong điều đó, bạn có thể

quan sát rằng

giá trị phân loại trong

cột phân đoạn đã thay đổi

thành các giá trị số,

làm cho nó sẵn sàng để sử dụng trong

xây dựng bội số

mô hình hồi quy tuyến tính.

Đáng chú ý là có một cột

đơn vị_bán lớn hơn

1.000 mà trước đây chúng tôi

rơi vào một cách đơn giản

mô hình hồi quy tuyến tính.

Hãy loại bỏ cái này

trước khi tiếp tục.

Bây giờ chúng ta đã sẵn sàng để xây dựng một

mô hình hồi quy bội.

Trong bước tiếp theo, chúng ta hãy

tách tập dữ liệu thành

tính năng dự đoán

và các biến mục tiêu

mà chúng ta muốn dự đoán.

Vì chúng ta đang sử dụng một

phương pháp mô tả

nghiên cứu số liệu thống kê

của mô hình,

hãy tìm tóm tắt mô hình

sử dụng mô hình thống kê với

tất cả các tính năng.

Chúng ta hãy nghiên cứu một số

những quan sát

và cố gắng hiểu

ý nghĩa của chúng là gì.

R bình phương, chúng ta có thể

thấy rằng chúng ta đã có

giá trị bình phương R là 0,462.

Đây là một ý nghĩa quan trọng

cải tiến

trên tuyến tính đơn giản của chúng tôi

mô hình hồi quy,

nơi chúng tôi đã đạt được một

R-bình phương 0,363.

Bình phương R đã điều chỉnh là

phiên bản sửa đổi của R

bình phương đã được điều chỉnh

cho số lượng

các yếu tố dự báo trong mô hình.

Nó chỉ tăng nếu

tính năng mới cải thiện

mô hình nhiều hơn sẽ là

được mong đợi một cách ngẫu nhiên.

Đây là 0,461

khá gần với

giá trị bình phương R.

Xác suất của thống kê F

cho chúng ta biết liệu

mô hình tổng thể với

các biến độc lập

về mặt thống kê

có ý nghĩa trong việc giải thích

biến mục tiêu.

Xác suất của

Thống kê F thấp hơn

0,05 cho chúng ta biết rằng

mô hình thống kê

đáng kể.

Chúng ta sẽ hiểu khác

thông số quan trọng

khi chúng tôi di chuyển qua

phương pháp miêu tả.

Một trong những giả định quan trọng của

một mô hình hồi quy tuyến tính là

sự vắng mặt của đa cộng tuyến.

Đa cộng tuyến xảy ra khi

hai hoặc nhiều hơn

biến độc lập

có mối tương quan cao

với nhau.

Điều này có thể dẫn đến sai lệch

hoặc kết quả sai lệch,

làm cho nó khó khăn

giải thích tác dụng của

các biến riêng lẻ và có thể

cũng làm cho mô hình của chúng ta không ổn định.

Hãy sử dụng một cách đơn giản

ví dụ giả định

với hai biến dự đoán để

giải thích ý nghĩa của

đa cộng tuyến trong

bối cảnh của hồi quy tuyến tính.

Hãy xem xét một tuyến tính

mô hình hồi quy với

hai đặc tính x1 và x2.

Bây giờ giả sử x1 và x2 là

có mối tương quan cao gần như

điểm tại đó x1

có thể hoàn toàn

được xác định bởi x2 với

một phương trình tuyến tính,

nơi A và B ở

một số hằng số,

Điều này có nghĩa là bất kỳ sự thay đổi nào trong

x1 được phản chiếu bởi

một sự thay đổi trong x2,

giống như có hai

bóng tối cho một chủ đề.

Trong kịch bản này, khi chúng ta tạo

mô hình hồi quy

với x1 và x2,

các hệ số của x1 và x2

sẽ ảnh hưởng lẫn nhau,

điều này sẽ làm cho

mô hình không ổn định

Để giải quyết vấn đề đa cộng tuyến,

chúng tôi sử dụng một thước đo gọi là phương sai

yếu tố lạm phát, hoặc VIF.

VIF là thước đo

số lượng của

đa cộng tuyến trong

phân tích hồi quy,

nếu không có yếu tố nào tương quan,

VIF sẽ bằng một.

VIF được tính bằng cách chọn

một biến độc lập

và thoái lui

nó chống lại nhau

biến độc lập.

Từ hồi quy này, chúng tôi

nhận được giá trị bình phương R.

Giá trị bình phương R cao cho biết

biến đó là

gần như hoàn hảo,

sự kết hợp sạch hơn

của các biến khác,

báo hiệu sự dư thừa.

Về mặt toán học, VIF cho

một biến độc lập là

được trình bày như sau.

Thông thường, VIF

ngưỡng 2,5,

và 10 được dùng để chỉ

sự tương quan cao.

Trong trường hợp của chúng ta, hãy xem xét

10 là ngưỡng VIF.

Hãy chuyển trở lại

sổ ghi chép và kiểm tra

các giá trị VIF cho

tất cả các tính năng.

Đầu tiên, nhập phương sai

hàm yếu tố lạm phát

từ thư viện mô hình thống kê,

được sử dụng để tính toán

VIF cho mỗi

biến dự báo.

Sau đó chúng ta cần xác định một

hàm gọi là tính toán

gạch dưới VIF mất một

khung dữ liệu làm đối số của nó.

Chức năng này sẽ trở lại

một khung dữ liệu có chứa

giá trị VIF cho mỗi cột

trong khung dữ liệu đầu vào.

Tóm lại là khá rõ ràng

mà chúng tôi đã có

một số tính năng

những thứ dư thừa như

nhiều tính năng có VIF

giá trị hơn mười.

Tính năng dư thừa sẽ không

mang theo bất kỳ thông tin mới

đến mô hình,

vì vậy tốt hơn hết là loại bỏ chúng.

Dựa trên quan sát trên,

bước tiếp theo là loại bỏ

các tính năng có giá trị VIF

trên ngưỡng để

giảm thiểu tác động

của hiện tượng đa cộng tuyến.

Quá trình này được tiến hành ở

nhiều lần lặp và

loại bỏ một tính năng tại

một thời gian để quan sát làm thế nào

tác dụng loại bỏ

VIF của các tính năng khác.

Thả tất cả lên cao

Tính năng VIF trong

một lần đi không cho phép chúng ta nhìn thấy

sự phụ thuộc lẫn nhau

và những thay đổi trong

một giá trị còn lại

tính năng sau mỗi lần loại bỏ.

Mục tiêu ở đây là loại bỏ

tất cả các tính năng dư thừa,

từ đó tạo ra một

mô hình ổn định hơn.

Chúng ta sẽ khởi tạo một biến x,

gạch dưới VIF, nó sẽ lưu trữ

giá trị VIF tối đa

trong mỗi lần lặp.

Tiếp theo, chúng ta sẽ sử dụng vòng lặp y

điều đó sẽ giữ

chạy chừng nào

giá trị VIF cao nhất trong số

biến dự đoán

lớn hơn mười.

Khi đã xong việc đó, chúng ta sẽ

tính toán các giá trị VIF

cho tất cả người dự đoán

biến có trong x,

và sau đó cập nhật tối đa

gạch dưới biến VIF bằng

giá trị cao nhất trong VIF

khung dữ liệu TF được gạch chân.

Chúng tôi sẽ kiểm tra xem

giá trị tối đa là

lớn hơn ngưỡng

trong số mười, nếu đúng như vậy,

chúng tôi sẽ sắp xếp dấu gạch dưới VIF

Khung dữ liệu DF trong

dựa vào thứ tự giảm dần

trên các giá trị VIF và chọn

hàng đầu tiên sử dụng

dấu chấm ilog của số 0,

điều này mang lại cho chúng tôi

biến dự đoán

có VIF cao nhất.

Cuối cùng, chúng tôi sẽ loại bỏ

các giá trị dự đoán có

VIF cao nhất từ

khung dữ liệu,

tất cả các biến

mà không đáp ứng

ngưỡng được giảm xuống

một cách lặp đi lặp lại.

Các tính năng cuối cùng với

VIF được hiển thị

ở đầu ra.

Ở đây chúng ta có thể thấy điều đó

tất cả các tính năng mà

vẫn có giá trị VIF

dưới mười.

Tuyệt vời, chúng tôi đã giảm nhẹ

tính đa cộng tuyến.

Bây giờ hãy xem liệu

thực hiện bước này

có ảnh hưởng gì đến

hiệu suất mô hình.

Để làm điều đó, hãy xây dựng lại

mô hình và tìm

tóm tắt bằng mô hình thống kê.

Chúng ta có thể thấy rằng R

giá trị bình phương vẫn còn

gần như giống nhau ngay cả sau đó

loại bỏ một số tính năng,

điều này có nghĩa là

các biến chúng tôi đã loại bỏ là

dư thừa và không thêm

lời giải thích độc đáo

cấp nguồn cho mô hình.

Cho đến nay trong video này,

chúng tôi đã hiểu

tầm quan trọng của việc xử lý

nhiều yếu tố dự đoán bằng cách sử dụng

đa tuyến tính

phương pháp hồi quy.

Chúng tôi nhấn mạnh những cạm bẫy

đa cộng tuyến

và giới thiệu các

yếu tố lạm phát phương sai.

Trong video tiếp theo,

chúng tôi sẽ tiếp tục

khám phá miêu tả

tiếp cận và hiểu

một số số liệu thống kê khác có trong

Tóm tắt mô hình để đánh giá

mô hình. Hãy theo dõi.