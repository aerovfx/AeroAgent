# 01 cá nhân-tính năng-tầm quan trọng

---

Bây giờ bạn đã học được cách lấy toàn cầu

tầm quan trọng của một tính năng đối với một mô hình.

Trong bài học này, bạn sẽ học cách

có thể hiểu được tầm quan trọng của một tính năng

dựa trên dự đoán của một cá nhân cụ thể.

Với các phương pháp như phương pháp hoán vị,

chúng tôi đã thấy rằng chúng tôi có thể có được

tầm quan trọng của mỗi

tính năng cho một mô hình tổng thể.

Nhưng hãy coi như chúng ta không quan tâm đến

hiểu một mô hình tổng thể nhưng

hiểu một dự đoán duy nhất

của một mô hình trên một bệnh nhân.

Chúng tôi muốn biết tầm quan trọng

huyết áp là dành cho

dự đoán của mô hình trên Bệnh nhân A.

Bệnh nhân đặc biệt này có máu

áp suất rất cao.

Vì vậy, chúng ta có thể mong đợi rằng mặc dù tuổi tác

nói chung là quan trọng hơn về điều này

bệnh nhân cụ thể, máu của họ

áp lực sẽ thúc đẩy rủi ro của họ.

Vì vậy, chúng ta có thể đào tạo một mô hình để dự đoán

kết quả y sử dụng tuổi và huyết áp.

Và một khi mô hình này được đào tạo,

nó quay lại với một dự đoán

rủi ro 0,93 cho một sự kiện.

Và chúng ta sẽ đại diện cho mô hình này

với f và BP và tuổi làm đầu vào.

Tương tự, chúng ta cũng có thể huấn luyện

một mô hình dự đoán kết quả y

chỉ sử dụng huyết áp và

chỉ sử dụng độ tuổi.

Và hai mô hình này cũng có thể

đưa ra dự đoán về rủi ro.

Lưu ý rằng dự đoán sử dụng

BP tương tự như

dự đoán được thực hiện bởi mô hình đầy đủ, nhưng

dự đoán được thực hiện chỉ với tuổi nhỏ hơn nhiều.

Chúng ta có thể tính toán tầm quan trọng

của một tính năng cho

Bệnh nhân A bằng cách lấy sự khác biệt trong

đầu ra, có và không có tính năng.

Đối với độ tuổi, chúng tôi có mô hình đầy đủ

trừ đi đầu ra của mô hình

không chứa tuổi, và

sự khác biệt đó là -0,01.

Bây giờ khi chúng ta loại bỏ BP,

đầu ra của mô hình thay đổi 0,53.

Như vậy, tầm quan trọng của

Huyết áp cao hơn nhiều đối với

bệnh nhân này hơn tầm quan trọng của tuổi tác.

Lưu ý rằng điều này rất giống với

phương pháp thả cột mà chúng ta đã thấy,

ngoại trừ việc chúng ta đang xem xét

đầu ra của mô hình,

f, không phải hiệu suất của các mô hình.

Tuy nhiên, phương pháp này có thể thất bại

để nhận biết những đặc điểm quan trọng

khi có những đặc điểm tương quan.

Đây là một ví dụ về điều đó.

Hãy nói rằng thay vì sử dụng một

giá trị huyết áp của bệnh nhân

mô hình, chúng tôi sử dụng cả tâm thu và

huyết áp tâm trương.

Chúng ghi lại áp lực trong máu

mạch máu khi tim đang đập và

lần lượt nghỉ ngơi.

Chúng có mối tương quan cao và

đối với bệnh nhân này đều rất cao.

Vì vậy, giống như trước đây, chúng ta nên mong đợi rằng

tầm quan trọng của cả hai tính năng này

nên rất cao.

Thay vào đó, đây là những gì sẽ xảy ra.

Giống như trước đây, chúng tôi xem xét rủi ro

dự đoán của một mô hình sử dụng tất cả

các tính năng làm đầu vào cho bệnh nhân này.

Chúng tôi cũng xem xét dự đoán rủi ro của

ba mô hình không bao gồm tuổi,

huyết áp tâm thu, và

đặc điểm huyết áp tâm trương.

Chú ý lần này, ít nhất một trong số

hai lần đo huyết áp

luôn nằm trong bộ tính năng, vì vậy

chúng tôi luôn thấy dự đoán rủi ro cao.

Sử dụng phương pháp của chúng tôi,

chúng tôi thấy rằng tầm quan trọng của mỗi

do đó các tính năng là rất nhỏ.

Và chúng ta không thể nhận ra

tầm quan trọng của sBP cao và

dBP cao ở bệnh nhân này,

mặc dù việc thiết lập gần như đã xong

mặt khác giống hệt như khi chúng tôi có

một lần đo huyết áp.

Hãy xem chúng ta có thể khắc phục điều này như thế nào.