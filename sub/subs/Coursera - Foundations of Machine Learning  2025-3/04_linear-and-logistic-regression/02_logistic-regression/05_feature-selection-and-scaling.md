# 05 lựa chọn tính năng và chia tỷ lệ

---

Chào mừng trở lại.

Ở bài học trước chúng ta đã học

để tạo ra một mô hình ổn định,

chúng ta phải đảm bảo rằng mô hình của chúng ta tuân thủ

giả định về hồi quy logistic.

Giả định quan trọng nhất là

sự vắng mặt của đa cộng tuyến.

Chúng tôi sẽ sử dụng cùng một Jupyter

sổ ghi chép từ video trước, vì vậy

trước khi chúng ta bắt đầu,

đảm bảo chạy tất cả các ô ở trên.

Vì chúng ta đã học ở

video hồi quy tuyến tính cách sử dụng

VIF kiểm tra hiện tượng đa cộng tuyến

mô hình hồi quy, hãy nhanh chóng

kiểm tra VIF bằng cách tính VIF

chức năng mà chúng tôi đã tạo ra.

Bây giờ, chúng ta có thể loại bỏ các tính năng

có VIF lớn hơn 10.

Bây giờ chúng tôi đã loại bỏ

các tính năng có điểm VIF cao,

hãy nhanh chóng kiểm tra hình dạng của dữ liệu của chúng tôi.

Nếu bạn nhớ lại,

có 25 đặc điểm trong dữ liệu

trước khi loại bỏ đa cộng tuyến.

Sau khi loại bỏ đa cộng tuyến,

chỉ còn lại 16 tính năng.

Hoàn hảo, hiện tại có hiện tượng đa cộng tuyến

đã được xử lý xong, hãy tiếp tục

để xây dựng lại hồi quy logistic của chúng tôi

mô hình bằng cách làm theo các bước tương tự.

Hãy phân tích và

so sánh các thông số mà chúng ta đã thảo luận

điểm giả r trước đó,

log khả năng và giá trị p.

Đối với giả r bình phương,

có sự giảm nhẹ về

giá trị đi từ 0,2757 đến 0,2719.

Điều này gợi ý rằng sau

loại bỏ các đặc điểm đa cộng tuyến,

mô hình phù hợp với dữ liệu

đã giảm đi một chút.

Để có khả năng ghi nhật ký, trong khi mô hình

độ vừa vặn giảm nhẹ sau

loại bỏ một số tính năng nhất định

đi từ -9552 đến -9602.

Nó vẫn có thể có ích vì

đa cộng tuyến có thể làm biến dạng

việc giải thích các đặc điểm và

giảm khả năng ứng dụng của mô hình.

Bây giờ, với vấn đề đa cộng tuyến được giải quyết,

nó càng trở nên cần thiết hơn để

hiểu ý nghĩa

của từng đặc điểm riêng lẻ.

Và đây là nơi chúng ta so sánh các giá trị p.

Như đã quan sát thấy trong hồi quy tuyến tính,

các biến có giá trị vượt quá 0,05

có thể không có ý nghĩa thống kê.

Để đảm bảo mô hình của chúng tôi là cả hai

có thể giải thích và mạnh mẽ,

chúng ta phải loại bỏ các tính năng với

giá trị p lớn hơn 0,05.

Bởi vì chúng tôi đã làm rồi

bước này trong hồi quy tuyến tính,

hãy nhanh chóng loại bỏ tính năng này

với giá trị p lớn hơn 0,05.

Bây giờ chúng tôi đã đảm bảo rằng

mô hình chỉ kết hợp nhiều nhất

các tính năng thích hợp,

hãy xây dựng lại mô hình của chúng tôi sau khi mở rộng quy mô.

Như đã thấy trong hồi quy tuyến tính.

Không cần mở rộng quy mô,

so sánh các hệ số của

các tính năng trở nên sai lệch.

Chúng ta không thể so sánh trực tiếp

các hệ số không có tỷ lệ.

Bởi vì các tính năng có độ lớn khác nhau

sẽ ảnh hưởng đến hệ số năng suất

nhiều hơn bởi quy mô của họ hơn thực tế của họ

quan trọng trong việc dự đoán kết quả.

Khi chúng tôi điều chỉnh mô hình của mình

các tính năng có quy mô tương tự,

chúng ta có thể hiểu rõ hơn

các hệ số của mô hình.

Hơn nữa, điều này có thể giúp các thuật toán

phù hợp với các tập dữ liệu lớn nhanh hơn.

Tương tự như hồi quy tuyến tính, hãy

sử dụng vô hướng tiêu chuẩn từ thư viện.

Để kiểm tra vệ sinh nhanh chóng, hãy viết

một mã chuyển đổi tỷ lệ

Mảng NumPy x_scale được thu nhỏ lại thành Pandas

khung dữ liệu được gọi là df_scaled.

Chúng tôi cũng sẽ sử dụng bản gốc

tên cột từ x, vì vậy

đọc mô hình dễ dàng hơn

tóm tắt có cùng tên tính năng.

Hãy xây dựng một mô hình cuối cùng cho

phương pháp mô tả

bằng cách sử dụng các tính năng được chia tỷ lệ.

Giá trị tuyệt đối cao hơn

của các hệ số cho

tính năng này có nghĩa là họ nhiều hơn

có ý nghĩa trong việc dự đoán liệu

một đơn vị được bán sẽ được bán

hơn 1000 đơn vị hay không.

Vậy hãy so sánh tuyệt đối

các hệ số đặc trưng trong

thứ tự giảm dần để xác định

những cái quan trọng nhất.

Tính chất có giá trị tuyệt đối lớn nhất

các hệ số là lưu lượng truy cập trang và

đơn giá.

Điều này tương tự như hồi quy tuyến tính

mô hình nơi lưu lượng truy cập trang và

đơn giá được đưa ra để có

giá trị tuyệt đối cao nhất.

Hãy nhớ rằng tích cực hay tiêu cực

dấu của hệ số cũng có vấn đề.

Ví dụ, hệ số dương cho

lưu lượng truy cập trang cho thấy rằng cao hơn

lưu lượng truy cập trang làm tăng khả năng

của một sản phẩm là sản phẩm bán chạy nhất.

Trong khi hệ số âm cho

đơn giá cho thấy đơn vị cao hơn

giá giảm khả năng đó.

Những giải thích này có thể rất hữu ích

để sự phối hợp được ưu tiên nhất

những đặc điểm có ảnh hưởng khi kinh doanh

quyết định cho các chiến dịch tiếp thị.

Quản lý hàng tồn kho và xác định

sản phẩm có doanh số bán hàng đáng kể.

>> Người nói 3: Trong video này, chúng ta

sử dụng phương pháp miêu tả,

chúng tôi tập trung vào sự hiểu biết

mối quan hệ với dữ liệu trong quá khứ.

Đối với phương pháp miêu tả,

chúng tôi đã đánh giá mô hình bằng cách sử dụng

Hình vuông giả R của McFadden.

Tuy nhiên, điều đáng lưu ý là

đây không phải là thước đo được sử dụng rộng rãi.

Lý do là nó không

rất áp dụng cho

các thuật toán khác ngoài hồi quy logistic.

Trong video cuối cùng của mô-đun này,

hãy xây dựng hồi quy logistic của chúng ta

mô hình dựa trên phương pháp dự báo.

Đối với phương pháp dự đoán, chính của chúng tôi

chỉ số đánh giá sẽ là điểm F1.

Nếu bạn nhớ lại, chúng tôi đã sử dụng rất

số liệu tương tự khi chúng tôi làm việc với KNN

thuật toán trong mô-đun trước.

Vì vậy, không cần phải chần chừ thêm nữa,

hãy chuyển sang phương pháp dự đoán.