# 10 cách xử lý-mất cân bằng-bộ dữ liệu-thực hành

---

Xin chào các bạn học viên. Trong video này,

hãy sử dụng các kỹ thuật

mà chúng ta đã học ở

video cuối cùng để

xử lý sự mất cân bằng lớp học.

Ngoài ra, chúng tôi cũng sẽ

đang sử dụng oversampling và

lấy mẫu dưới

kỹ thuật để cân bằng

tập dữ liệu. Hãy bắt đầu.

Đầu tiên, hãy làm

tiền xử lý dữ liệu,

giống như chúng ta đã làm trong khi

xây dựng phân loại

và mô hình hồi quy.

Trước khi chúng tôi bắt đầu

phân tầng,

hãy kiểm tra tỉ số của

cả hai lớp trong

chia tách y_train và y_test.

Để kết hợp phân tầng

phân chia trong mô hình của chúng tôi,

chúng ta có thể sử dụng bài kiểm tra tàu hỏa

phân chia với sự phân tầng

tham số được đặt thành

y để đảm bảo rằng việc phân chia

được phân tầng dựa trên

biến mục tiêu y.

Bây giờ hãy biểu diễn

sự phân tầng

và xem liệu tỷ lệ có thay đổi không.

Như bạn có thể thấy, tỷ lệ

không thay đổi nhiều.

Điều này là do

tập dữ liệu chúng tôi có rất lớn,

do đó, cơ hội của

độ lệch mẫu nhỏ.

Nhưng như một cách thực hành tốt cho

vấn đề phân loại

với tập dữ liệu không cân bằng,

chúng ta nên luôn luôn làm

phân chia phân tầng.

Bây giờ hãy thử cái khác

kỹ thuật mà

đang sử dụng siêu tham số

trọng lượng lớp.

Như đã thảo luận trước đó, cụ thể

thuật toán học máy

như quyết định,

hồi quy logistic, v.v.,

cho phép chúng ta thiết lập lớp

siêu tham số trọng lượng.

Hãy đặt nó ở trạng thái cân bằng,

và sử dụng phân tầng

chia ra rằng chúng tôi

đã có được trước đó

để xây dựng mô hình.

Tuy nhiên, chúng ta cũng có thể

tùy chỉnh trọng lượng lớp

bằng cách định nghĩa một từ điển,

nơi các phím đại diện

cấp lớp và

giá trị đại diện cho trọng số

chúng tôi muốn gán cho mỗi lớp.

Bây giờ hãy đưa ra dự đoán

trên dữ liệu huấn luyện và kiểm tra.

Bây giờ chúng tôi đã thực hiện

thủ thuật để xử lý

mất cân bằng giai cấp,

chúng ta hãy đi sâu hơn vào

hiểu cách cân bằng

tập dữ liệu sử dụng

lấy mẫu dưới và

kỹ thuật lấy mẫu quá mức.

Đầu tiên, hãy thực hiện lấy mẫu dưới.

Để làm như vậy chúng ta có

cài đặt đầu tiên

thư viện scikit-learn

được gọi là imblearn.

Nó được thiết kế đặc biệt

để đối phó với

tập dữ liệu mất cân bằng

và giúp chúng tôi triển khai liền mạch

nhiều phương pháp khác nhau

như lấy mẫu dưới,

lấy mẫu quá mức và SMOTE, v.v.

Chạy mã bên dưới

để cài đặt tương tự.

Sau khi thư viện được cài đặt,

hãy nhập bộ lấy mẫu ngẫu nhiên

từ imb.undersampling.

Bây giờ hãy lấy mẫu lại

dữ liệu đào tạo

và xây dựng cây quyết định

với dữ liệu được lấy mẫu lại.

Như bạn có thể thấy từ các tỷ lệ,

sự phân bố lớp là

bây giờ bằng nhau do

lấy mẫu ngẫu nhiên.

Hãy xây dựng mô hình bằng cách sử dụng

dữ liệu đào tạo đã sửa đổi

và xem hiệu suất của nó.

Như bạn có thể thấy,

hiệu suất mô hình

đã xấu đi một chút.

Điều này là do dưới

trường hợp lấy mẫu từ

lớp đa số là ngẫu nhiên

bị loại bỏ và điều này có thể dẫn đến

đến việc mất thông tin.

Hãy thử ngẫu nhiên

lấy mẫu quá mức bây giờ.

Thực hiện ngẫu nhiên

lấy mẫu quá mức liên quan đến việc thực hiện

các bước tương tự như chúng tôi đã làm

cho bộ lấy mẫu ngẫu nhiên.

Tuy nhiên, điểm khác biệt duy nhất

là chúng ta phải nhập ngẫu nhiên

lấy mẫu từ imblearn

lấy mẫu quá mức và

xây dựng mô hình.

Hãy thực hiện lấy mẫu lại

của dữ liệu gốc.

Một lần ngẫu nhiên

lấy mẫu quá mức được thực hiện,

chúng ta có thể nhanh chóng kiểm tra xem

tỉ lệ của chúng

lớp có bằng nhau hay không.

Như bạn có thể thấy, nó bằng nhau.

Hãy chuyển sang bước tiếp theo

và xây dựng mô hình ngay bây giờ.

Như bạn có thể thấy, hiệu suất này

tốt hơn một chút so với

các kịch bản lấy mẫu dưới mức như

chưa có thông tin nào

bị xóa khỏi tập dữ liệu.

Hãy thử triển khai

lấy mẫu quá mức khác

kỹ thuật mượt mà.

Hãy bắt đầu bằng cách nhập

phương pháp SMOTE từ

mô-đun imblearn.oversampling.

Tiếp theo, SMOTE được khởi tạo

với một chỗ ngồi ngẫu nhiên

cho khả năng tái tạo.

SMote được áp dụng cho

dữ liệu đào tạo,

dẫn đến lấy mẫu quá mức

dữ liệu huấn luyện.

Hãy nhanh chóng kiểm tra các tỷ lệ

của các lớp trong

dữ liệu huấn luyện.

Như bạn có thể thấy,

tỉ lệ đều bằng nhau.

Hãy xây dựng

mô hình cây quyết định

sử dụng lấy mẫu quá mức

dữ liệu huấn luyện.

Như bạn có thể thấy trong này

kịch bản với SMote,

hiệu suất mô hình là

tương tự như lấy mẫu quá mức ngẫu nhiên.

Như chúng ta đã biết, việc lặp

kỹ thuật khác nhau là

một phần thiết yếu của

mô hình học máy

quá trình xây dựng là như vậy

nên thử

các kỹ thuật và công cụ khác nhau

để có được hiệu quả tốt nhất.

Trong video tiếp theo, chúng tôi sẽ

so sánh hiệu suất của

tất cả các mẫu đó

chúng tôi đã xây dựng như vậy

xa. Hẹn gặp lại bạn ở lần tiếp theo.

Trong mô-đun này, chúng tôi đã hiểu

cây quyết định từ đầu

bằng cách đi qua

hoạt động bên trong của nó

và sự hiểu biết

các thông số khác nhau.

Kiến thức này là

sẽ khá

hữu ích sau này

tất nhiên nơi chúng tôi

khám phá một số mô hình tiên tiến

sử dụng cây quyết định

làm mô hình cơ sở của nó.

Cây quyết định có thể

thay thế hiệu suất của

mô hình tuyến tính của chúng tôi về sự hiệp lực,

nhưng không thành công

vượt trội hơn các mô hình KNN.

Tuy nhiên, trong khóa học tiếp theo của chúng tôi,

một số quyết định dựa trên cây

mô hình tiên tiến

có thể cho chúng tôi hiệu suất tốt hơn.

Ngoài quyết định, chúng tôi còn

đã học về cách giải quyết

tập dữ liệu không cân bằng,

những điều rất phổ biến ở

các kịch bản thế giới thực.

Chúng tôi sẽ tiếp tục làm việc trên

vấn đề giám sát cho

hiệp lực trong khóa học tiếp theo.

Trong khi đó, hãy tiếp tục làm việc

vấn đề không được giám sát

trong mô-đun tiếp theo.