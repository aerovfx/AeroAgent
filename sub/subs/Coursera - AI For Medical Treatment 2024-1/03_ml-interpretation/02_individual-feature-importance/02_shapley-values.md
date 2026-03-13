# 02 giá trị shapley

---

Chúng ta sẽ xem xét một phương pháp khác, phương pháp Shapley

phương thức giá trị có thể gán tính năng

tầm quan trọng một cách chính xác ngay cả trong

sự hiện diện của các tính năng tương quan.

Trước đó chúng ta đã thấy làm thế nào chúng ta có thể có được

tầm quan trọng của sBP bằng cách xem xét

theo dự đoán được thực hiện với cả ba

các tính năng so với tính năng không sử dụng sBP.

Chúng tôi nhận được dự đoán là 0,95

với cả ba đặc điểm, và

0,94 nếu không có huyết áp tâm thu.

Vì vậy, chúng tôi nói sBP có đóng góp

của sự khác biệt là 0,01.

Với các giá trị Shapley, chúng tôi không chỉ

sẽ xem xét bộ tính năng đầy đủ,

nhưng tất cả các bộ tính năng có chứa sBP.

Ở bên trái,

chúng tôi có tất cả các bộ tính năng có chứa sBP.

Và bên phải tương ứng

bộ tính năng đã loại bỏ sBP.

Cái cuối cùng ở đây là bộ trống

đó là tập hợp không chứa đặc điểm nào.

Do đó chúng ta có thể đào tạo tám mô hình

điều đó đưa ra dự đoán cho

Bệnh nhân A với những điều này

tập hợp đặc tính khác nhau.

Bốn trong số này chứa sBP,

và bốn người trong số họ thì không.

Trường hợp đặc biệt ở đây là tập rỗng

mà chúng ta sẽ xác định

đầu ra của mô hình như mong đợi

giá trị của kết quả trong tập dữ liệu.

Vì vậy, trong trường hợp này, 10% bệnh nhân

dân số thực sự có sự kiện này.

Vì vậy, chúng ta đặt f của tập trống là 0,1.

Bây giờ chúng ta có thể tính toán tầm quan trọng của

sBP cho từng tập hợp con tính năng này,

bằng cách lấy sự khác biệt của dự đoán

có và không có tính năng.

Vì vậy, chúng ta có bốn số ở đây

cho chúng ta tầm quan trọng của sBP đối với

dự đoán của bệnh nhân A với

mỗi bộ tính năng này.

Câu hỏi là, làm thế nào chúng ta

kết hợp bốn số này để có được

một con số đại diện cho

tầm quan trọng của sBP đối với bệnh nhân A?