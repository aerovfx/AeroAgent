# 04 điều kiện-trung bình-điều trị-hiệu quả

---

Giả sử chúng ta nghĩ có lẽ phương pháp điều trị này

có tác dụng tốt hơn đối với bệnh nhân lớn tuổi.

Vậy liệu chúng ta có thể sử dụng thực tế là điều này

bệnh nhân là 56 tuổi

có được một ước tính cá nhân hơn

quyền lợi của họ dựa trên độ tuổi này.

Chính thức hơn,

chúng tôi tìm cách ước tính dự kiến

sự khác biệt về tiềm năng

kết quả khi ở tuổi 56

Đây gọi là điều kiện

hiệu quả điều trị trung bình,

bởi vì chúng ta đang điều hòa

kỳ vọng vào độ tuổi bằng 56.

Trong bối cảnh thử nghiệm đối chứng ngẫu nhiên,

chúng ta có thể chia ước tính này thành

việc ước lượng hai đại lượng.

Chúng ta có thể ước tính giá trị đầu tiên

số lượng bằng cách tìm tất cả bệnh nhân

trong điều trị

nhóm có độ tuổi 56 và

nhìn vào họ

kết quả mong đợi ở đây là 0,5.

Chúng ta có thể làm theo quy trình tương tự đối với

nhìn vào bệnh nhân

trong nhóm đối chứng có độ tuổi từ

56 và nhìn vào kết quả trung bình của họ.

Cuối cùng, chúng ta có thể tạo ra sự khác biệt

giữa hai kỳ vọng này để có được kết quả mong đợi

sự khác biệt trong

kết quả tiềm năng là 0,5.

Tuy nhiên, hãy chú ý rằng vì

chúng tôi có rất ít mẫu để

ước tính một trong hai điều này

trực tiếp từ dữ liệu,

chúng ta có thể không tin điều đó

chúng tôi có một ước tính chính xác.

Điều này càng trở nên rắc rối hơn nếu chúng ta

không chỉ xem xét tuổi tác mà

cũng đang xem xét bệnh nhân khác

các đặc điểm như huyết áp của họ.

Một lần nữa,

chúng ta có thể chia ước tính này thành

việc ước lượng hai đại lượng riêng biệt.

Và lần này thấy rằng chúng tôi không có

bệnh nhân trong nhóm điều trị bằng

cả hai cùng tuổi và

huyết áp với tư cách là bệnh nhân mà chúng tôi

quan tâm để tìm ra sự khác biệt mong đợi cho.

Chúng ta có thể có một bệnh nhân

trong nhóm kiểm soát nhưng

điều đó vẫn không cho phép chúng tôi trực tiếp

ước tính sự khác biệt này từ dữ liệu.

Bây giờ một giải pháp cho vấn đề này

có thể là chúng ta có thể học được một mối quan hệ

giữa tuổi,

huyết áp và kết quả của chúng tôi, và chúng tôi có thể sử dụng

mối quan hệ này

để có được ước tính.

Để xem chúng ta có thể thực hiện điều này như thế nào,

trước tiên hãy đơn giản hóa thuật ngữ.

Viết hoa X đại diện cho các tính năng

như tuổi tác và huyết áp,

và x nhỏ đại diện cho các giá trị

những tính năng này đảm nhận.

Vậy x nhỏ ở đây có thể là một vectơ

bao gồm 56 và 130.

Nhưng nếu chúng ta có nhiều tính năng hơn,

thì chúng ta có thể kết hợp chúng vào x.

Và vì vậy bây giờ chúng tôi tìm kiếm điều kiện này

hiệu quả điều trị trung bình,

mà chúng ta có thể chia nhỏ trong bối cảnh của

thử nghiệm đối chứng ngẫu nhiên theo dự kiến

kết quả điều trị dựa trên những đặc điểm này

trừ đi kết quả mong đợi trong kiểm soát

đưa ra những tính năng này.

Bây giờ chúng ta đã thấy trong ví dụ trước

rằng chúng tôi không thể ước tính trực tiếp điều này từ

dữ liệu bởi vì chúng tôi đã không

tìm bất kỳ bệnh nhân nào phù hợp với tất cả

của các tính năng.

Vì vậy, thay vào đó chúng ta sẽ sử dụng một hàm,

mũ mu của 1,

để có thể ước tính số lượng này.

Vậy mu mũ của 1 sẽ lấy n,

các biến số bệnh nhân, và

đưa ra ước tính của số lượng này.

Và mu mũ của 0 sẽ

cũng làm tương tự ngoại trừ

nó sẽ làm điều đó cho cánh tay điều khiển.

Và vì vậy chúng ta có thể chỉ cần lấy kết quả đầu ra và

lấy sự khác biệt

của những đầu ra đó để đạt được

hiệu quả điều trị trung bình có điều kiện.

Hàm này mà chúng ta sẽ ước tính

sẽ được gọi là hàm đáp ứng điều trị

và mu hat của 0 sẽ là

được gọi là hàm phản hồi điều khiển.