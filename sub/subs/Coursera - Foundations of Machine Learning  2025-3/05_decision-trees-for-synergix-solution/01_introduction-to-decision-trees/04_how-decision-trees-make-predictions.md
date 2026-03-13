# 04 cây-quyết định-dự đoán

---

Chào mừng trở lại. Cho đến bây giờ chúng tôi

đã hiểu được những điều cơ bản

đằng sau việc xây dựng một

mô hình cây quyết định

và sự xây dựng của nó.

Chúng tôi cũng đã học được

về các tiêu chí

chi phối cách mỗi

nút sẽ được chia.

Trong video này, chúng ta hãy

hiểu thế nào

cây quyết định của chúng ta sẽ tạo ra

dự đoán cho tập dữ liệu mới.

Để dễ hiểu,

hãy đảm nhận một vai trò mới.

Bây giờ chúng ta hãy xem

tại cây quyết định của chúng tôi.

Điều kiện ở gốc

nút kiểm tra xem giá trị

phân khúc ít hơn

hơn hoặc bằng 1,5.

Vì giá trị của đoạn

trong tập dữ liệu mới bằng 0,

điều kiện được thỏa mãn.

Vì vậy,

mẫu sẽ chuyển đến

nút nhánh trái

của cây quyết định.

Tóm tắt nhanh, trong

cây quyết định được vẽ bởi

chức năng cây lô,

các mẫu thỏa mãn

một điều kiện cụ thể đi

đến nút nhánh trái,

và các mẫu không đi

tới nút nhánh bên phải.

Bây giờ trong nút này,

điều kiện thứ hai là

đã xác minh kiểm tra nào

nếu giá trị của

phân khúc ít hơn

hơn hoặc bằng 0,5.

Vì điều kiện này

cũng hài lòng rồi

mẫu bây giờ chuyển sang bên trái

nút nhánh như được hiển thị ở đây.

Cuối cùng, trong nút này,

chúng ta có điều kiện thứ ba

để kiểm tra xem số lượng

khuyến mãi ít hơn

hơn hoặc bằng 0,5.

Như bạn có thể thấy từ bảng,

số lượng khuyến mãi là một.

Điều đó có nghĩa là điều kiện

không hài lòng.

Mẫu sẽ đi đến

bài nút lá bên phải

mà không có

sự chia cắt tiếp theo.

Hãy gọi nút này là nút A

và nút tiếp theo

với nó là nút B.

Lớp dự đoán của

nút A này có doanh thu thấp.

Điều này là do theo

các mẫu có sẵn trong nút,

xác suất của

sự xuất hiện của

doanh số bán hàng thấp là 1/1 hoặc một.

Trong khi đó xác suất

sự xuất hiện của

doanh thu cao cấp là

không bằng một hoặc bằng không.

Vì xác suất

sự xuất hiện của

doanh số bán hàng của tầng lớp thấp cao hơn,

lớp dự đoán của

nút có doanh số thấp.

Do đó, cây sẽ dự đoán

rằng sản phẩm có

hai tính năng này sẽ không được

đã bán được hơn 1.000 chiếc.

Một thực tế khác cần quan sát là

dự đoán này là

cực kỳ không đáng tin cậy.

Đó là vì nó được xác định

chỉ dựa trên một mẫu.

Để hiểu được dự đoán

xác suất tốt hơn,

chúng ta hãy nhìn xem

tại nút B cũng vậy.

Dựa trên số

của các mẫu hiện có

trong nút này, từ mỗi lớp,

chúng ta có thể thấy rõ điều đó

xác suất của

sự xuất hiện của lớp thấp

doanh số bán hàng sẽ là ba

bằng bốn hoặc 0,75 và

xác suất xảy ra của

doanh thu cao cấp sẽ

là một phần bốn hoặc 0,25.

Đó cũng là lý do tại sao trong nút này,

lớp dự đoán là

doanh số sẽ thấp.

So với nút A, chúng ta có

nhiều mẫu hơn ở nút B.

Đó là lý do tại sao dự đoán được đưa ra

tại nút này sẽ có nhiều hơn

đáng tin cậy và ít được trang bị quá mức

đến dữ liệu huấn luyện.

Ngay cả với cái nhỏ

cây quyết định,

quá trình đưa ra quyết định

có vẻ hơi dài với

nhiều bước nhưng không

lo lắng trong quá trình thực hiện,

những dự đoán này cho

vài nghìn hàng

được thực hiện trong một phần nhỏ của

giây bởi những chiếc máy tính nhanh của chúng tôi.

Với điều này, chúng tôi đã đến

đến cuối video này.

Tôi hy vọng bạn thích học cách

cây quyết định đưa ra dự đoán

cho tập dữ liệu chưa nhìn thấy.

Trong video tiếp theo chúng ta sẽ

xây dựng quyết định

mô hình cây trên

tập dữ liệu giải pháp tổng hợp để

giúp đỡ họ với

phát biểu vấn đề.