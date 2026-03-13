# 01 - Đánh giá mô hình deep learning Độ chính xác dự đoán

---

- [Người hướng dẫn] Trong video này,

bạn sẽ học cách tính toán và giải thích

độ chính xác dự đoán của mô hình học sâu.

Tôi sẽ chạy mã trong tệp 05_01e.

Bạn có thể làm theo bằng cách hoàn thành các ô mã trống

trong tệp 05_01b.

Lưu ý rằng đây là lần đầu tiên trong chuỗi năm video

hướng dẫn bạn qua quá trình

đánh giá một mô hình học sâu trong Python.

Trước khi bắt đầu, hãy nhập dữ liệu đã được đào tạo trước đó của chúng tôi

Mô hình Keras và xử lý trước dữ liệu thử nghiệm

chúng tôi dự định đánh giá mô hình dựa trên.

Vậy tôi đi xuống đây

và đặt ô mã của tôi ở đây

và sau đó chạy mọi thứ ở trên.

Bây giờ hãy cuộn lên một chút để đảm bảo

rằng mọi thứ đã hoàn thành trước khi chúng ta tiếp tục.

Được rồi, vậy là chúng ta đã tải xong mô hình được đào tạo trước đó

và xử lý trước dữ liệu.

Vì vậy sau khi đào tạo, điều quan trọng là phải đánh giá

một mô hình được kỳ vọng sẽ hoạt động tốt như thế nào

chống lại dữ liệu mới chưa được nhìn thấy.

Và có một số số liệu chúng ta có thể sử dụng để làm điều này.

Độ chính xác dự đoán là một trong số đó,

và đó là một thước đo đơn giản.

Và cách chúng tôi tính toán đây là tổng số

số dự đoán đúng chia cho tổng số

tổng thể của các dự đoán

Vì vậy, để có được độ chính xác dự đoán của mô hình của chúng tôi,

trước tiên chúng ta cần có xác suất dự đoán

cho mỗi hình ảnh thử nghiệm.

Vì vậy, những gì chúng tôi có ở đây là mô hình của chúng tôi

và chúng tôi gọi phương pháp dự đoán

và chúng tôi chuyển nó vào các hình ảnh thử nghiệm,

và điều đó trả lại cho chúng ta xác suất.

Vì vậy chúng ta hãy tiếp tục và chạy cái này.

Vậy bây giờ điều tiếp theo chúng ta cần làm

là chuyển đổi những xác suất này thành nhãn lớp

bằng cách chọn nhãn lớp

với xác suất dự đoán cao nhất

sử dụng hàm argmax.

Và do đó, hàm argmax được NumPy cung cấp cho chúng ta.

Vì vậy, trước tiên chúng ta sẽ nhập NumPy dưới dạng np,

và sau đó chúng ta sẽ gọi argmax.

Vì vậy, hãy tiếp tục và làm điều đó.

Và chúng tôi đã làm điều tương tự với nhãn thử nghiệm.

Vì vậy bây giờ với những giá trị này,

bây giờ chúng ta có thể sử dụng chức năng tính điểm chính xác

được cung cấp cho chúng tôi bởi gói sklearn.metrics.

Vì vậy, chúng tôi tiếp tục và nhập gói đó

cho chính chức năng đó.

Và sau đó chúng tôi sử dụng chức năng tính điểm chính xác

để tính toán độ chính xác.

Ở đây chúng tôi đã chuyển cho nó các lớp thực sự

cũng như các lớp dự đoán.

Vì vậy, hãy tiếp tục và chạy nó.

Và bây giờ chúng ta thấy rằng độ chính xác của mô hình là 0,9801.

Điều này có nghĩa là 98,01% dự đoán

được thực hiện bởi mô hình là chính xác.

Nói cách khác, trong số 10.000 hình ảnh thử nghiệm trong dữ liệu,

mô hình đã dự đoán chính xác nhãn của 9.801 trong số đó,

trong khi 199 bị phân loại sai.

Vì vậy, điều này cung cấp cho chúng tôi một cái nhìn tổng quan ở cấp độ cao

về hiệu suất của mô hình của chúng tôi.

Nhưng còn một điều khác chúng ta cũng có thể làm

là xem xét ngẫu nhiên một số ví dụ bị phân loại sai

để biết được mô hình của chúng tôi có thể đang đi sai hướng ở đâu.

Vì vậy, để làm điều đó, những gì chúng ta sẽ làm ở đây

là chúng ta sẽ tiếp tục và lấy một danh sách

trong số tất cả các ví dụ,

tất cả hình ảnh mà mô hình của chúng tôi đưa ra dự đoán

điều đó không chính xác và chúng ta sẽ hình dung một vài trong số chúng.

Vì vậy chúng ta sẽ làm ở đây là hình dung

năm trong số những ví dụ đó chỉ để hiểu chung

về nơi mà mô hình của chúng tôi có thể đi chệch hướng.

Vì vậy, hãy tiếp tục và nhập matplotlib,

lấy danh sách các hình ảnh bị phân loại sai,

và sau đó chúng ta sẽ hình dung ra những hình ảnh này, năm trong số đó,

chỉ để biết mọi thứ trông như thế nào.

Vì vậy, hãy tiếp tục và chạy nó.

Và ở đây chúng ta thấy rằng trong ví dụ này,

chúng ta có nhãn hiệu thực sự là bốn,

nhưng người mẫu của chúng tôi nghĩ rằng hình ảnh này là số 9.

Tôi có thể thấy một chút lý do tại sao nó lại nghĩ như vậy.

Và ví dụ tiếp theo, chúng ta có nhãn đúng là hai,

trong khi mô hình của chúng tôi cho rằng đó là số chín.

Và ở đây chúng ta có một nhãn thực sự gồm bốn,

và mô hình của chúng tôi nghĩ đây là số 6.

Và ở đây nữa, chúng ta thấy nhãn hiệu thực sự của hai,

nhưng mô hình của chúng tôi nghĩ đó là số 7.

Và cuối cùng ở đây chúng ta thấy nhãn thực sự của năm,

nhưng mô hình của chúng tôi nghĩ đó là số 3.

Vì vậy, trong video này, chúng tôi đã có thể tính toán

và giải thích độ chính xác dự đoán

của mô hình của chúng tôi so với dữ liệu thử nghiệm.

Trong video tiếp theo, chúng ta sẽ khám phá ma trận nhầm lẫn

để hiểu sâu hơn về hiệu suất của mô hình.

Nhìn thấy.