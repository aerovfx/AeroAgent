# 05 - Đánh giá điểm F1 của mô hình deep learning

---

- [Người hướng dẫn] Trong video này, bạn sẽ học cách tạo

và diễn giải điểm F1 của mô hình học sâu.

Tôi sẽ chạy mã trong tệp 05_05 E.

Bạn có thể theo dõi

bằng cách hoàn thành các ô mã trống trong tệp 05_05 B.

Lưu ý, video này là video thứ năm trong chuỗi năm video

hướng dẫn học sinh trong suốt quá trình

đánh giá một mô hình học sâu trong Python.

Nếu bạn chưa làm như vậy, hãy xem bốn video trước

để được giải thích chi tiết về mã trước đó.

Trước khi bắt đầu, hãy chạy mã chúng tôi đã tạo

trong những video đó

để môi trường của chúng ta tăng tốc.

Vì vậy tôi sẽ đi xuống ô mã của mình

rồi chạy các ô mã trước đó.

Và tôi sẽ cuộn lên một chút để đảm bảo

mã trước của chúng tôi đã hoàn thành việc thực thi

trước khi chúng ta chuyển sang ví dụ về điểm F1.

Được rồi, vậy là mã của chúng ta đã chạy xong,

chúng ta sẽ quay trở lại lần nữa.

Vậy điểm F1 là một thước đo

kết hợp cả độ chính xác

và gọi lại thành một con số duy nhất cung cấp thước đo cân bằng

về hiệu suất của một mô hình.

Nó đặc biệt hữu ích khi bạn muốn đánh giá một mô hình

về hiệu suất trong các tình huống, cho dù đó là sự đánh đổi

giữa độ chính xác và thu hồi

hoặc khi chúng ta đang xử lý các tập dữ liệu mất cân bằng.

Công thức cho F1 được hiển thị ở đây.

Nó là một phương tiện hài hòa của cả độ chính xác và thu hồi.

Vì vậy, khi chúng ta cố gắng tính điểm F1 của một mô hình,

chúng tôi gọi hoặc sử dụng hàm điểm F1 từ sklearn.metrics.

Vì vậy, chúng tôi bắt đầu bằng cách nhập hàm này

và sau đó chúng tôi vượt qua các lớp học thực sự

và các lớp được dự đoán trong mô hình của chúng tôi

đến hàm điểm F1.

Tương tự như độ chính xác và thu hồi, chúng tôi tính điểm F1

cho mỗi nhãn gốc của tập dữ liệu của chúng tôi.

Vì vậy, chúng ta sẽ tiếp tục và chạy đoạn mã này

và điều đó mang lại cho chúng tôi điểm F1

cho các chữ số từ 0 chữ số 1 cho đến chữ số 9.

Vì vậy, hãy giải thích những kết quả này bằng cách sử dụng kết quả đầu tiên

như một ví dụ.

Điểm F1 là 0,9872

hoặc 98,72% nghĩa là mô hình có độ cân bằng tốt

giữa độ chính xác và thu hồi.

Nó đang hoạt động tốt về mặt

của cả hai việc giảm thiểu dương tính giả

và xác định chính xác những mặt tích cực thực sự.

Điểm F1 kém thường giảm thấp hơn đáng kể,

chẳng hạn như dưới 0,5.

Điều này cho thấy mô hình đang gặp khó khăn

để duy trì sự cân bằng tốt giữa độ chính xác và thu hồi.

Điểm thấp gợi ý

rằng một mô hình hoặc tạo ra nhiều kết quả dương tính giả,

đó là độ chính xác thấp,

hoặc nó không xác định được một phần đáng kể

về những mặt tích cực thực sự, đó là khả năng thu hồi thấp.

Vì vậy, trong video này, chúng ta đã xem xét điểm F1,

và trong các video trước chúng tôi đã có thể

để xem xét các số liệu đánh giá khác nhau,

ma trận chuyển đổi, độ chính xác dự đoán,

độ chính xác và thu hồi.

Nếu bạn tiếp tục xem hết năm video,

bây giờ bạn đã học thành công cách

đánh giá một mô hình deep learning

sử dụng các số liệu hiệu suất thiết yếu.

Điều này bao gồm sự hiểu biết làm thế nào

để đánh giá độ chính xác của dự đoán

để đo lường độ chính xác tổng thể

dự đoán của mô hình của bạn

và giải thích ma trận nhầm lẫn

để hiểu rõ hơn về các loại lỗi mà mô hình của bạn mắc phải.

Bạn cũng đã khám phá tính toán chính xác để xác định

có bao nhiêu dự đoán tích cực

thực sự đã nhớ lại chính xác để xem

mô hình xác định tất cả các trường hợp có liên quan hiệu quả như thế nào

và điểm F1, cung cấp thước đo cân bằng

cả về độ chính xác và độ thu hồi.

Nắm vững các số liệu đánh giá này sẽ giúp bạn tốt hơn

hiểu điểm mạnh mô hình của bạn

và điểm yếu, cho phép bạn tinh chỉnh

và cải thiện các dự án deep learning của bạn

để có kết quả đáng tin cậy hơn.