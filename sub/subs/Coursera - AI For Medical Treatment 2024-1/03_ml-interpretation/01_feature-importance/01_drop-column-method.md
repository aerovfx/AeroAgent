# 01 phương pháp thả cột

---

Tuần này bạn sẽ tìm hiểu về các phương pháp để

diễn giải các mô hình AI mà bạn đã có

được xây dựng để chẩn đoán và tiên lượng.

Bạn sẽ tìm hiểu về các phương pháp

giải thích các mô hình dựa trên cây

bạn đã xây dựng trong Khóa học 2 và phần sâu

các mô hình học tập bạn đã xây dựng trong Khóa 1.

Trong bài học này,

bạn sẽ tìm hiểu về một phương pháp cho

sự giải thích của

các mô hình học máy.

Phương pháp này sẽ cho phép

bạn diễn giải một mô hình

bằng cách tìm hiểu xem mỗi cái bao nhiêu

tính năng đóng góp cho mô hình.

Giả sử chúng ta đã có một tiên lượng

mô hình sử dụng huyết áp, huyết áp,

và tuổi tác có nguy cơ tử vong.

Hãy xem chúng ta có thể làm thế nào

tìm hiểu tầm quan trọng

của từng đặc điểm này vào mô hình.

Phương pháp đầu tiên chúng ta sẽ xem xét

để xác định tầm quan trọng của tính năng

là phương pháp thả cột.

Trong phương pháp này,

chúng tôi có mô hình ban đầu sử dụng

huyết áp và tuổi tác làm đầu vào.

Bây giờ chúng tôi đào tạo hai mô hình khác,

một cái chỉ sử dụng tuổi làm đầu vào,

và một cái khác chỉ sử dụng

huyết áp làm đầu vào.

Chúng ta sẽ đề cập đến những mô hình này bằng cách

đầu vào bằng cách sử dụng ký hiệu tập hợp này.

Chúng ta có thể đánh giá từng điều này

mô hình tiên lượng trên tập kiểm tra

sử dụng một thước đo như chỉ số C.

Mô hình có cả huyết áp và

tuổi có chỉ số C cao nhất, theo sau

bởi người mẫu chỉ có độ tuổi, theo sau

bằng mô hình chỉ với huyết áp.

Bây giờ, chúng ta có thể xác định tầm quan trọng

tuổi tác, hoặc huyết áp, bằng cách nhìn vào

sự khác biệt trong hiệu suất của

mô hình có và không có đặc điểm tuổi.

Vì vậy chúng tôi lấy sự khác biệt trong

chỉ số C, 0,90

và 0,82, để có được sự khác biệt là 0,08.

Tương tự như vậy để xem xét tầm quan trọng của

huyết áp, huyết áp,

chúng tôi nhìn vào sự khác biệt trong mô hình

sử dụng cả hai tính năng so với một

không bao gồm BP

để có được 0,90 trừ (lần này)

0,85 và tìm thấy rằng

sự khác biệt là 0,05.

Như vậy, chúng ta có thể nhận ra

tuổi đó có tính năng cao hơn

quan trọng hơn huyết áp.

Phương pháp này được gọi là cột thả

phương pháp vì chúng tôi đang bỏ

một tính năng để xây dựng một mô hình bổ sung.

Bởi vì các tính năng thường

được biểu diễn dưới dạng các cột trong bảng,

do đó có tên phương pháp thả cột.

Đây là một bảng

minh họa cho phương pháp này

Nơi chúng tôi có mô hình đầy đủ

được đào tạo về cả độ tuổi và

đặc điểm huyết áp và kết quả,

sau đó chúng tôi bỏ cột BP

để tạo thành mô hình thứ hai.

Cuối cùng, chúng tôi bỏ cột tuổi

để tạo thành mô hình thứ ba.

Thách thức với phương pháp này là

chúng ta phải xây dựng nhiều mô hình.

Với hai đặc điểm, chúng ta phải

xây dựng hai mô hình bổ sung này,

với ba đặc điểm,

chúng tôi phải xây dựng thêm ba mô hình.

Vì vậy chúng ta sẽ phải xây dựng càng nhiều

các mô hình bổ sung vì có các tính năng và

điều này có thể được tính toán

rất đắt tiền.