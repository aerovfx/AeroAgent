# 01 thước đo độ nhạy-độ đặc hiệu và đánh giá

---

Tuần này chúng ta sẽ đi sâu hơn vào

sự đánh giá sâu sắc

mô hình học tập y khoa.

Trong y học, vì

các quyết định có tác động lớn,

chúng tôi quan tâm đến

hiểu chính xác

khi một mô hình hoạt động trên một

kiên nhẫn và khi nào thì không.

Bạn sẽ tìm hiểu về

số liệu bao gồm

độ nhạy, độ đặc hiệu,

giá trị tiên đoán,

và đường cong ROC,

đó là những thành phần chính trong

đánh giá các mô hình trong

cơ sở y tế.

Trong bài học này, chúng ta sẽ nói về

những thiếu sót của

độ chính xác như một thước đo.

Từ độ chính xác, chúng ta sẽ xem xét

về cách chúng ta có thể rút ra

độ nhạy và độ đặc hiệu đối với

khái niệm cốt lõi trong

đánh giá y tế.

Trong phần thứ hai

của bài học này,

chúng ta sẽ nói về

giá trị tiên đoán,

cái nào có thể giúp

chuyên gia y tế

với việc ra quyết định lâm sàng.

Để trả lời câu hỏi

về việc một mô hình tốt như thế nào,

chúng ta sẽ bắt đầu bằng

nhìn vào độ chính xác.

Khi tính toán các

độ chính xác trên một tập kiểm tra,

chúng tôi nhìn vào tỷ lệ của

tổng số ví dụ mà

mô hình được phân loại chính xác.

Hãy làm việc với một

ví dụ để chúng ta có thể

minh họa

tính toán độ chính xác.

Ở đây chúng tôi có một bài kiểm tra

bộ 10 ví dụ.

Tám người trong số họ có

sự thật cơ bản của

bình thường và hai có

sự thật nền tảng của bệnh tật.

Giả sử chúng ta có một

mô hình đầu ra

âm tính cho cả 10 bệnh nhân.

Phủ định ở đây có nghĩa là mô hình

đang xuất ra

dự đoán bình thường.

Đây là tất nhiên

không phải là một mô hình hữu ích,

nhưng lưu ý rằng nó đang nhận được

tất cả các ví dụ bình thường đều đúng.

Vậy là sắp hết tám giờ rồi

trong số 10 ví dụ phải không,

và do đó có độ chính xác là 0,8,

so sánh với mô hình 2.

Mô hình 2 dự đoán chính xác

tích cực về cả hai

ví dụ về bệnh ở đây,

và cũng gọi hai trong số

ví dụ bình thường tích cực.

Bây giờ chúng ta có thể tính toán

độ chính xác của mô hình

2 và nếu chúng ta đi qua

tính toán này,

chúng ta sẽ tìm thấy một lần nữa

rằng chúng tôi nhận được tám trong số

10 ví dụ đúng với mô hình

2 để có độ chính xác là 0,8.

Vì vậy chúng ta có hai mô hình

với độ chính xác 0,8.

Mặc dù chúng tôi chưa

chính thức hóa việc này,

chúng ta có cảm giác rằng mô hình 2 là

có lẽ đang làm gì đó

hữu ích hơn

mô hình 1 vì nó ít nhất

cố gắng phân biệt giữa

bệnh nhân khỏe mạnh và bệnh tật.