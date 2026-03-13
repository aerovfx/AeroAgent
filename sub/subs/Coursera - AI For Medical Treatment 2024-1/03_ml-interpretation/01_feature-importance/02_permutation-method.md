# 02 phương pháp hoán vị

---

Chúng ta sẽ xem xét phương pháp hoán vị để

giải quyết thách thức cần phải đào tạo này

nhiều mô hình để

xác định tầm quan trọng của tính năng

Một lần nữa, chúng ta có cùng một tiên lượng

thiết lập mô hình như trước, được đào tạo

về tuổi tác và huyết áp.

Chúng ta sẽ tập trung vào

việc đánh giá mô hình này.

Giả sử chúng ta có một tập hợp thử nghiệm gồm các bệnh nhân

mà chúng tôi có thể đánh giá mô hình trên đó và chúng tôi

thấy rằng mô hình được kiểm tra

hiệu suất, chỉ số C thử nghiệm là 0,9.

Ý tưởng có tầm quan trọng hoán vị là

mà bây giờ chúng ta sắp hoán vị, hoặc trong

nói cách khác là xáo trộn, một cột tính năng trong

tập kiểm tra của chúng tôi trước khi chúng tôi đánh giá mô hình.

Vì vậy, chúng ta có thể thấy ở đây chúng ta có cột H.

Chúng ta sẽ làm gì

có bệnh nhân này

tuổi được xáo trộn với tuổi của người khác.

Và vì thế chúng ta có một sự xáo trộn trong việc này

cột của cột này ở đây.

Vì thế bây giờ chúng ta sẽ không đi qua

ở độ tuổi của bệnh nhân đó,

chúng ta đang bước qua tuổi của một số bệnh nhân khác,

nhưng tất nhiên, kết quả là như nhau.

Và chúng ta thấy sự sụt giảm trong đó là gì

hiệu suất của mô hình khi

chúng tôi cho ăn theo thứ tự xáo trộn

cột vào mô hình.

Tương tự, chúng ta cũng có thể xáo trộn

tính năng huyết áp nơi chúng ta có

cho một bệnh nhân cụ thể được xáo trộn

giá trị huyết áp đến từ

giá trị huyết áp của bệnh nhân khác và

vân vân và vân vân.

Và bây giờ chúng tôi lại chuyển điều này vào mô hình

và xem hiệu suất là gì

của mô hình mà chúng ta có được khi chúng ta có

huyết áp xáo trộn đi vào.

Và bây giờ ý tưởng chính với

tầm quan trọng của hoán vị là chúng ta

sẽ nhìn vào sự sụt giảm

hiệu suất giữa mô hình đầy đủ của chúng tôi,

và mô hình của chúng tôi với điều đó

cột cụ thể được xáo trộn.

Vì vậy, nếu một tính năng cụ thể là

quan trọng thì chúng ta mong đợi khi chúng ta

xáo trộn cột đó chúng ta thấy

hiệu suất giảm mạnh.

Và ở đây chúng ta có thể thấy rằng sự sụt giảm

hiệu suất theo độ tuổi là 0,2, trong khi mức giảm

về hiệu suất cho BP nơi tôi đang tham gia

mô hình đầy đủ và chúng tôi đang trừ đi

hiệu suất của mô hình khi chúng ta có

cột BP được xáo trộn nhỏ hơn nhiều.

Đó là 0,07. Vì vậy, điều này cho phép chúng ta nói rằng

tuổi tác quan trọng hơn huyết áp.

Và điều thú vị về phương pháp này

là chúng ta có thể sử dụng phương pháp này

mà không cần đào tạo lại người mẫu.

Và phương pháp này hiệu quả với bất kỳ mô hình nào

làm việc với dữ liệu có cấu trúc trong bảng.