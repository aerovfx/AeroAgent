# 03 đọc-giữa-đường cong với log-loss

---

Xin chào và chào mừng trở lại.

Chúng ta đã thấy cách

các giá trị khác nhau của m và

c sẽ ảnh hưởng đến đường cong sigmoid cho

dữ liệu của chúng tôi.

Có rất nhiều sigmoid

những đường cong có thể được hình thành

cùng một tuyên bố vấn đề

tùy thuộc vào giá trị của m và c.

Tuy nhiên, chúng ta cần tìm cách

chọn đường cong sigmoid phù hợp nhất.

Nếu bạn còn nhớ, trong hồi quy tuyến tính,

chúng tôi giảm thiểu bình phương hàm mất mát

lỗi để tìm dòng phù hợp nhất.

Tương tự, trong hồi quy logistic,

để tìm ra đường cong phù hợp nhất,

chúng tôi giảm thiểu chức năng mất mát.

Hàm mất mát cho logistic

hồi quy là hàm mất log.

Hàm mất nhật ký định lượng khoảng cách

giữa xác suất dự đoán và

kết quả thực tế.

Mục tiêu là tìm ra một mô hình

đó giảm thiểu sự mất mát này.

Một mô hình hoàn hảo sẽ

có log loss bằng 0.

Trong phương trình này, n là số

của các quan sát trong tập dữ liệu,

y là kết quả thực tế của các quan sát.

Trong trường hợp hiệp lực,

y sẽ là một nếu đơn vị được bán

lớn hơn 1000 và 0 nếu không.

Với tư cách là một quy ước,

PI trong hồi quy logistic là

xác suất của một mẫu

thuộc lớp 1.

Trong trường hợp hiệp lực, p sẽ là

xác suất dự đoán của một mẫu

thuộc các đơn vị lớp

bán được hơn 1000.

Hãy hiểu chức năng mất nhật ký này

tốt hơn bằng cách so sánh hai sigmoid

những đường cong chúng tôi đã thực hiện trong video trước.

Trong biểu đồ này,

có hai đường cong sigmoid đại diện

xác suất dự đoán cho

số lượng bán được lớn hơn 1000.

Để hiểu chức năng mất nhật ký

tốt hơn, chúng ta sẽ so sánh hai đường cong này

bằng cách nhìn vào dự đoán

xác suất cho hai điểm.

Một điểm mà thực tế

giá trị của y là 1, và

một điểm khác ở đó

giá trị thực tế của y là 0.

Dựa vào hai điểm này, chúng ta sẽ tìm thấy

các giá trị hàm mất log tương ứng.

Hãy bắt đầu với một điểm dữ liệu tại y = 1,

hãy gọi điểm này là A.

Để có được xác suất dự đoán cho A,

chúng ta sẽ vẽ một đường thẳng từ

điểm này tới đường cong màu xanh lá cây.

Đối với A, xác suất dự đoán

là khoảng 0,65.

Hãy đặt những giá trị này của

xác suất thực tế và

xác suất dự đoán trong

chức năng mất log.

Ở đây, n và

phép tính tổng có thể được bỏ qua vì chúng ta

chỉ đang quan sát một điểm dữ liệu.

Bây giờ, hàm này trở thành như sau.

Nếu chúng ta nhập giá trị của y,

phương trình sẽ rút gọn thành thế này,

và đối với quan sát đầu tiên y là 1 và

p là 0,65,

điều này sẽ đến để xem xét

một cái gì đó như thế này

Vì vậy, mất nhật ký cho

điểm A với đường cong màu xanh lá cây là 0,4308.

Để so sánh điều này với đường cong màu xanh,

xác suất dự đoán cho

điểm A với đường cong màu xanh sẽ là 0,8,

và

chức năng mất nhật ký

sẽ vào khoảng 0,2231.

Lưu ý mức độ mất mát giảm như thế nào khi

xác suất dự đoán tiến gần hơn đến 1.

Tiếp theo, hãy thử so sánh tổn thất của

mẫu thuộc lớp 0.

Hãy gọi đây là điểm B.

Đối với điểm B, giá trị thực tế của y là 0,

và dựa vào đường thẳng để

đường cong màu xanh lá cây, dự đoán

xác suất sẽ là khoảng 0,3.

Vì vậy, đặt những giá trị này vào

hàm mất log với y = 0,

phương trình sẽ giảm xuống mức này.

Đối với quan sát đầu tiên,

y là 0 và p là 0,3.

Điều này sẽ dẫn đến điều này.

Vậy log mất điểm B với green

đường cong sẽ xấp xỉ 0,3567.

Để so sánh điều này với đường cong màu xanh,

xác suất dự đoán cho

điểm B với đường cong màu xanh sẽ là 0,19,

và tổn thất log sẽ là 0,2107.

Lưu ý mức độ mất mát giảm như thế nào khi

xác suất dự đoán tiến gần tới 0.

Nếu chúng ta tạo một đường cong chỉ bằng cách sử dụng những

hai mẫu, chúng ta có thể quan sát điều đó với

cả hai giá trị tổn thất, đường cong màu xanh

sẽ trở thành đường cong tốt hơn.

Tuy nhiên, trong các kịch bản thế giới thực,

chúng tôi không đánh giá khả năng của mô hình

chỉ dựa trên một hoặc hai quan sát.

Thay vào đó, chúng tôi tổng hợp các khoản lỗ nhật ký cho

mỗi điểm dữ liệu để có được

một biện pháp tích lũy như sau.

Các giá trị của hệ số và

các giao điểm cho giá trị nhỏ nhất của

hàm tích lũy được tìm thấy bằng cách sử dụng

các thuật toán tối ưu hóa mà chúng tôi

đã học trong hồi quy tuyến tính.

Giống như trong hồi quy tuyến tính,

phần này được chăm sóc bởi các thư viện

như statsmodel và scikit-learn.

Điều này đưa chúng ta đến phần cuối của video này.

Tóm lại, chúng ta đã học được cách

những dự đoán có thể được thực hiện cho

các mẫu đã cho dựa trên các đường cong.

Chúng ta đã học cách tìm các giá trị mất mát

dựa trên xác suất dự đoán và

cuối cùng so sánh hai sigmoid

đường cong để tìm cái tốt hơn.

Trong video tiếp theo, chúng ta sẽ xây dựng một

mô hình hồi quy logistic sử dụng mô hình thống kê

để giúp giải quyết việc phân loại

vấn đề đối với Synergyx.

Hẹn gặp bạn ở đó.