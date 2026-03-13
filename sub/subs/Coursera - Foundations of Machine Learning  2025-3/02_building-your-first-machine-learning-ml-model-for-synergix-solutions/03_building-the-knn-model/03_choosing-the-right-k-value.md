# 03 chọn-đúng-k-giá trị

---

Xin chào và chào mừng trở lại.

Trong video trước, chúng tôi đã xây dựng

đầu tiên của chúng tôi

mô hình học máy.

Chúng tôi đã sử dụng giá trị mặc định của k

bằng năm đến

lấy một mô hình đó

mang lại cho chúng tôi độ chính xác 82,8%

điểm trong dữ liệu kiểm tra.

Nhưng rồi chúng tôi bị bỏ lại

với câu hỏi,

đây có phải là nhất không

mô hình phù hợp?

Nếu không thì cái gì là

đúng giá trị của k?

Điều này cho chúng ta mô hình tốt nhất.

Trong video này, chúng ta hãy

hiểu điều này,

chúng ta sẽ tạo ra bốn

vòng lặp tính toán

độ chính xác khác nhau

điểm dựa trên giá trị của k

từ 1-51 Chúng tôi sẽ lưu trữ

điểm hiệu suất cho

vừa luyện tập vừa kiểm tra

tập hợp trong danh sách riêng biệt.

Lưu ý rằng bước này có thể mất

đôi khi như đã biết

là một mô hình chậm.

Knn là một mô hình chậm vì nó

không lưu bất kỳ

phương trình hoặc học tập.

Mỗi lần chúng tôi tập luyện

hoặc đưa ra dự đoán,

khoảng cách giữa một số

điểm đang được tính toán.

Do đó, khi

tập dữ liệu rất lớn,

chúng ta thường có xu hướng không sử dụng nó.

Bây giờ chúng ta hãy vẽ đồ thị

điểm chính xác

cho chuyến tàu và bài kiểm tra

dữ liệu và quan sát nó.

Chúng ta có thể thấy điều đó k

bằng ba cho chúng ta

điểm chính xác tốt nhất cho

dữ liệu thử nghiệm và nhịp đập

điểm chuẩn quá.

Nhưng có một

khoảng cách đáng kể giữa

hiệu suất của

tập huấn luyện và tập kiểm tra.

Khi chúng ta tăng giá trị

của k, khoảng cách giảm dần.

Tuy nhiên, hiệu suất trên

bộ kiểm tra cũng

giảm dần.

Ngoài ra còn có nhiều

mô hình trong đó giá trị của k

cho bạn điểm chính xác

lớn hơn 80% trên dữ liệu thử nghiệm.

Chúng ta nên chọn mô hình nào?

Để hiểu việc lựa chọn

đúng mẫu mã,

bạn cần phải hiểu

hai khái niệm quan trọng,

quá vừa vặn và không vừa vặn.

Hãy hiểu điều này

trong video tiếp theo.