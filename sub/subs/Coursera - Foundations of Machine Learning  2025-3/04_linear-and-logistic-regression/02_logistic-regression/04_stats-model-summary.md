# 04 số liệu thống kê-mô hình-tóm tắt

---

Bây giờ chúng tôi đã được trang bị tốt với

kỹ thuật hồi quy logistic,

chúng ta sẽ bắt đầu bằng việc xây dựng một hệ thống hậu cần

mô hình hồi quy cho bài toán đã cho.

Chúng ta sẽ bắt đầu với một mô tả

cách tiếp cận trong video này và

thử dự đoán

cách tiếp cận trong các video sau.

Để nhắc lại,

sự khác biệt chính giữa dự đoán và

phương pháp mô tả là

mục tiêu của vấn đề.

Các mô hình mô tả tìm cách hiểu

mối quan hệ trong dữ liệu

dựa trên những gì đã xảy ra trong quá khứ.

Trong khi các mô hình dự đoán được xây dựng

với mục tiêu hàng đầu là thực hiện

dự đoán chính xác cho tập dữ liệu chưa nhìn thấy.

>> Diễn giả 2: Chúng ta sẽ sử dụng mô hình Thống kê

thư viện để xây dựng hồi quy logistic

mô hình cho phương pháp mô tả.

Chúng tôi sẽ bắt đầu bằng cách nhập những thứ cần thiết

thư viện và sau đó thay đổi thư mục

đến nơi bạn đã lưu trữ tập dữ liệu,

hãy bắt đầu với việc đọc tập dữ liệu.

Đây chính là dữ liệu bán quá trình

chúng tôi đã nghiên cứu về hồi quy tuyến tính,

vì vậy chúng tôi sẽ chuyển trực tiếp đến

bỏ cột số lượng đơn vị đã bán.

Chúng tôi đang làm điều này bởi vì chúng tôi không thể giữ

các đơn vị được bán vì nó liên quan trực tiếp đến

đơn vị bán được hơn 1.000 cột.

Vì vậy hãy tiếp tục và bỏ cột này đi.

Vì hồi quy logistic cũng

dựa trên các giả định tuyến tính,

đó là một cách thực hành tốt để sử dụng một

mã hóa nóng để chuyển đổi phân đoạn

giá trị cột từ

phân loại thành số.

Hãy giải quyết vấn đề này bằng cách sử dụng

hàm pd.get_dummies.

Hãy kiểm tra nhanh các loại dữ liệu

của dữ liệu bằng hàm .dtypes.

Vì chúng tôi đang sử dụng phiên bản mới nhất của

Gấu trúc, các bạn sẽ nhận thấy rằng hai người này

các cột vừa được thêm vào dữ liệu

frame có kiểu dữ liệu là Bool.

Chúng tôi sẽ sử dụng hàm lambda để

chuyển đổi các giá trị này thành số

cột, hãy kiểm tra phần đầu của dữ liệu.

Bây giờ hãy bắt đầu với việc mô tả

Phương pháp xây dựng mô hình cơ bản và

kiểm tra hiệu suất của nó.

Trước khi xây dựng mô hình,

chúng ta cần xác định biến dự đoán của mình

của các đặc tính và biến mục tiêu.

Trong bước này, chúng tôi đang chọn tất cả các cột

trong tập dữ liệu là tính năng x vì chúng giúp ích

trong việc đưa ra dự đoán và mục tiêu

biến là unit_sold lớn hơn 1.000.

Hơn nữa, đó luôn là một thực hành tốt

để xác nhận hình dạng dữ liệu của chúng tôi

đảm bảo rằng ma trận tính năng của chúng tôi và

vectơ mục tiêu được căn chỉnh chính xác.

Như chúng ta có thể quan sát,

chúng tôi có khoảng 20.000 hàng và

25 tính năng trong tập dữ liệu của chúng tôi,

giống như chúng ta đã làm trong hồi quy tuyến tính,

hãy thêm một hằng số vào x để đảm bảo

rằng giao điểm đó khác 0.

Bây giờ chúng ta hãy xây dựng logistic

mô hình hồi quy.

Ở đây, hàm logic

từ mô hình Thống kê được sử dụng để

xây dựng mô hình hồi quy logistic.

Phương pháp fit huấn luyện mô hình trên r

dữ liệu và phương pháp tóm tắt cung cấp

phân tích chuyên sâu về mô hình

hiệu suất và hệ số.

Bây giờ chúng ta hãy quan sát sự phân tích hoặc

tóm tắt chúng tôi đã nhận được cho mô hình này.

Hãy hiểu bản tóm tắt này có ý nghĩa gì

cho vấn đề phân loại của chúng tôi cho

Synergix.

Hiện tại, chúng ta sẽ tập trung

cụ thể trên ba tham số

giả R vuông,

log khả năng và giá trị p.

Như bạn đã biết, r bình phương là một đánh giá

số liệu cho hồi quy tuyến tính,

tương đương với điều đó trong logistic

hồi quy là giả r bình phương.

Giả r bình phương, đôi khi

được gọi là bình phương Macfiden, kể

mô hình logistic phù hợp với dữ liệu như thế nào

và giá trị của nó có thể nằm trong khoảng từ 0 đến 1.

Càng gần một cái,

mô hình càng tốt.

Đối với mô hình đầu tiên mà chúng tôi đã xây dựng,

giá trị của giả r bình phương là 0,27.

Tuy nhiên, đây không phải là

một thước đo rất phổ biến cho

vấn đề phân loại là giả

r vuông không thể được sử dụng để

đánh giá các mô hình học máy

khác với hồi quy logistic.

Bây giờ, hãy nói về khả năng ghi nhật ký.

Nếu bạn còn nhớ, chúng tôi đã phân tích

chức năng mất mát trong video cuối cùng,

mối quan hệ giữa hàm mất mát và

khả năng đăng nhập là rất gần gũi.

Trong video cuối cùng,

chúng tôi nhằm mục đích giảm thiểu hàm mất mát,

điều này có nghĩa là chúng tôi tối đa hóa khả năng ghi nhật ký.

Để giải thích rõ hơn, chúng ta hãy xem

phương trình của hàm mất mát và

phương trình cho

khả năng đăng nhập trông giống như,

điều này tối đa hóa khả năng ghi nhật ký là

tương tự như giảm thiểu hàm mất mát.

Bởi vì sự khác biệt duy nhất giữa

hai là dấu âm n sẽ

không có bất kỳ tác động nào vì nó đang diễn ra

là một hằng số có giá trị gần hơn

0 khả năng đăng nhập

cho thấy sự phù hợp tốt hơn.

Đối với mô hình đầu tiên mà chúng tôi xây dựng,

khả năng ghi nhật ký là -9552,4.

Giống như trong hồi quy tuyến tính,

thật khó để đánh giá một mô hình

với sai số bình phương trung bình thì rất khó

để đánh giá mô hình này bằng nhật ký

giá trị khả năng trong hồi quy logistic.

Cuối cùng, hãy nói về giá trị p,

như chúng ta biết,

giá trị p trong hồi quy tuyến tính cho biết

chúng tôi liệu một tính năng cụ thể có

có ý nghĩa thống kê ở

dự đoán biến mục tiêu.

Những điều này có ý nghĩa tương tự trong

hồi quy logistic là tốt.

Ở đây, giá trị p là 0,05, có nghĩa là

tính năng này rất quan trọng trong việc giải thích

sự thay đổi trong việc liệu một sản phẩm

bán được hơn 1.000 đơn vị hay không.

Tương đương với giá trị thăm dò thống kê F

trong hồi quy logistic là LLR p-alue.

>> Diễn giả 1: Tìm hiểu một mô hình

tóm tắt giúp chúng tôi trong việc phân tích mô tả

của mô hình.

Như bạn có thể đã quan sát,

có rất nhiều tính năng mà

giá trị p cao hơn 0,05.

Đừng quên, hồi quy logistic

cũng có giả định là không

đa cộng tuyến, chúng ta sẽ giải quyết

những vấn đề này trong video tiếp theo.