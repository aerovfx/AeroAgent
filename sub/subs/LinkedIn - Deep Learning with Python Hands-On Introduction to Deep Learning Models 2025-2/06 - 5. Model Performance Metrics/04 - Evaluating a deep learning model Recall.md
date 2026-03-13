# 04 - Đánh giá mô hình deep learning Recall

---

- [Người hướng dẫn] Trong video này, bạn sẽ học cách tạo

và giải thích việc thu hồi một mô hình học sâu.

Tôi sẽ viết mã trong tệp 05_04E.

Bạn có thể làm theo bằng cách hoàn thành các ô mã trống

trong tệp 05_04B.

Lưu ý rằng video này là video thứ tư trong tổng số năm video

trình tự hướng dẫn học sinh trong suốt quá trình

đánh giá một mô hình học sâu trong Python.

Nếu bạn chưa làm như vậy, hãy xem ba video trước

để được giải thích chi tiết về mã trước đó.

Trước khi bắt đầu, hãy chạy mã chúng tôi đã tạo

trong những video đó để cải thiện môi trường của chúng ta.

Vì vậy tôi sẽ cuộn lên để đảm bảo

rằng mã của chúng tôi đã hoàn tất trước khi chúng tôi tiếp tục.

Được rồi, thế là xong.

Bây giờ chúng ta có thể quay trở lại nơi chúng ta đã ở.

Vậy nhớ lại hay còn gọi là độ nhạy

hoặc tỷ lệ dương thực sự, là số liệu đo lường

một mô hình có thể xác định các trường hợp tích cực thực tế tốt như thế nào.

Nó trả lời câu hỏi,

của tất cả các trường hợp tích cực thực tế

mô hình đã xác định chính xác bao nhiêu?

Công thức thu hồi là tích cực thực sự

chia cho số dương thực và số âm giả.

Khả năng thu hồi cao có nghĩa là mô hình xác định chính xác

hầu hết các trường hợp tích cực.

Điều này đặc biệt quan trọng trong những trường hợp

khi thiếu một trường hợp tích cực,

đó là những kết quả âm tính giả, gây hậu quả nghiêm trọng.

Vì vậy, để tính toán khả năng thu hồi của mô hình của chúng tôi,

chúng tôi sử dụng hàm điểm thu hồi từ sklearn.metrics.

Vì vậy, chúng tôi bắt đầu bằng cách nhập hàm

và sau đó chúng ta chuyển cho hàm các lớp thực

và các lớp dự đoán.

Vì vậy hãy tiếp tục và chạy cái này

để chúng ta có thể lấy điểm thu hồi cho từng nhãn lớp.

Vì vậy, để giải thích những kết quả này,

tương tự như những gì chúng tôi đã làm để đạt được độ chính xác.

Việc thu hồi chữ số 0 trong trường hợp này

là 0,9816 hoặc 98,16%.

Điều này có nghĩa là trong số tất cả các hình ảnh

thực sự được dán nhãn là số 0,

mô hình đã xác định chính xác 98,16% trong số đó,

nhưng nó đã bỏ lỡ 1,84% số hình ảnh thực tế.

Chúng được phân loại không chính xác như một số chữ số khác.

Tương tự với độ chính xác,

chúng ta cũng có thể tính toán thu hồi từ ma trận nhầm lẫn.

Vì vậy, trong ví dụ này chúng ta thấy chữ số 0,

chúng ta có thể tính toán mức thu hồi bằng cách nhìn vào hàng đầu tiên

của ma trận nhầm lẫn, trong đó TP là 962

và FN là 18, là tổng của các phân loại sai

trong cùng một hàng.

Vì vậy, trong video này, chúng tôi đã có thể tạo

và diễn giải số liệu thu hồi cho từng

của nhãn lớp trong mô hình học sâu.

Trong video tiếp theo, chúng tôi sẽ tạo

và giải thích điểm F1 cho từng nhãn lớp

để hiểu sâu hơn về hiệu suất của mô hình.

Hẹn gặp bạn ở đó.