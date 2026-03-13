# 01 đường cong và ngưỡng

---

Trong bài học này,

chúng ta sẽ xem xét một trong những công cụ hữu ích nhất

để đánh giá các mô hình y tế,

đường cong ROC. Chúng ta sẽ xem đường cong ROC cho phép như thế nào

chúng tôi trực quan

vẽ đồ thị độ nhạy của một mô hình so với tính đặc hiệu của

mô hình ở các ngưỡng quyết định khác nhau.

Đầu ra của mô hình phân loại chụp X-quang ngực

xác suất mắc bệnh khi chụp X-quang.

Đầu ra này có thể được chuyển đổi thành

chẩn đoán sử dụng ngưỡng hoặc

điểm vận hành.

Khi xác suất vượt quá ngưỡng,

thì chúng ta giải thích điều này là tích cực hoặc

nói rằng bệnh nhân mắc bệnh.

Khi xác suất là

dưới ngưỡng,

chúng tôi giải thích điều này là tiêu cực hoặc nói

bệnh nhân không mắc bệnh.

Ví dụ: nếu điểm của chúng tôi là 0,7 và

ngưỡng của chúng tôi là

0,5 thì chúng tôi sẽ phân loại

ví dụ này là tích cực.

Nhưng nếu điểm của chúng tôi là 0,2 và

ngưỡng của chúng tôi là 0,5,

chúng ta sẽ phân loại cái này

ví dụ là tiêu cực.

Sự lựa chọn ngưỡng của chúng ta ảnh hưởng

các số liệu chúng tôi đã xem xét cho đến nay.

Ví dụ: nếu chúng ta có ngưỡng t là 0

sau đó chúng ta sẽ phân loại

mọi thứ đều tích cực.

Và vì thế sự nhạy cảm của chúng ta sẽ là một

trong khi độ đặc hiệu của chúng tôi sẽ bằng không.

Tương tự, nếu chúng ta đã chọn một ngưỡng

của một chúng tôi sẽ phân loại mọi thứ

là tiêu cực, vì vậy độ đặc hiệu của chúng tôi sẽ là

một trong khi độ nhạy của chúng tôi sẽ bằng không.

Hãy đi sâu hơn vào cách chúng tôi

lựa chọn ngưỡng còn được gọi là

điểm vận hành

ảnh hưởng đến các đại lượng này.