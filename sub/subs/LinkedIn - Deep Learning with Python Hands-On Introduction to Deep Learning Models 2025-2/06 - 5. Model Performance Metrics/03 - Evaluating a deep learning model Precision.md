# 03 - Đánh giá mô hình deep learning Độ chính xác

---

- [Người hướng dẫn] Trong video này, bạn sẽ học cách tạo

và giải thích độ chính xác của mô hình học sâu.

Tôi sẽ chạy mã trong tệp 05_03e.

Bạn có thể làm theo bằng cách hoàn thành việc bán mã trống

trong tệp 05_03b.

Lưu ý rằng video này là video thứ ba trong chuỗi năm video

hướng dẫn bạn qua quá trình

đánh giá một mô hình học sâu trong Python.

Nếu bạn chưa làm như vậy, hãy xem hai video trước

để được giải thích chi tiết về mã trước đó.

Trước khi bắt đầu, hãy chạy mã chúng tôi đã tạo

trong hai video đó để cải thiện môi trường của chúng ta.

Vì vậy tôi sẽ tiếp tục và nhấp chuột phải vào đây

trong ô mã tiếp theo rồi chạy các ô mã trước đó.

Vì vậy tôi sẽ cuộn lên để có thể quan sát đoạn mã

và đảm bảo rằng mọi thứ đã chạy.

Vì vậy, có vẻ như tất cả việc bán mã đã chạy rồi.

Vậy bây giờ chúng ta có thể quay lại đây và bắt đầu.

Vì vậy, độ chính xác là thước đo đo lường độ chính xác

của những dự đoán tích cực được thực hiện bởi một mô hình.

Cụ thể, nó định lượng có bao nhiêu trường hợp

mà mô hình dự đoán là tích cực

thực sự là những mặt tích cực thực sự.

Nó trả lời câu hỏi, trong tất cả các trường hợp

mô hình được phân loại là tích cực,

có bao nhiêu cái đã thực sự đúng?

Vậy công thức là, số thực dương được chia

bởi những điều tích cực thực sự, cộng với những điều tích cực giả.

Độ chính xác cao có nghĩa là khi mô hình dự đoán một lớp,

rất có thể nó đúng.

Điều này đặc biệt quan trọng trong những tình huống

nơi mà kết quả dương tính giả rất tốn kém.

Vì vậy, trong ví dụ của chúng tôi ở đây, chúng tôi sẽ tiếp tục

và sử dụng chức năng tính điểm chính xác từ sklearn.metrics

để tính toán độ chính xác của mô hình của chúng tôi.

Vì vậy, chúng tôi bắt đầu bằng cách nhập hàm đó

và sau đó chúng ta sẽ chuyển sang nó,

các lớp thực và các lớp dự đoán.

Và vì mô hình của chúng tôi

là mô hình phân loại đa lớp,

chúng tôi có nhiều giá trị chính xác cho mỗi nhãn,

và đó là lý do tại sao chúng ta có vòng lặp for

điều đó cho phép chúng ta liệt kê và đi qua

để tính toán từng điểm chính xác

cho mỗi nhãn.

Vì vậy, hãy tiếp tục và xem kết quả của chúng tôi trông như thế nào.

Vì vậy, hãy chạy nó.

Và bây giờ, chúng ta thấy độ chính xác của từng

của các chữ số từ 0 đến 9.

Vì vậy, hãy giải thích một trong những điều này, ví dụ.

Vị trí của chữ số 0 trong trường hợp này,

cái đầu tiên ở đây là 0,9928, hay 99,28%.

Điều này gần như có nghĩa là ngoài trường hợp này,

tất cả các trường hợp mà mô hình dự đoán

chữ số là 0 thì 99,28% những dự đoán đó là đúng.

0,72% còn lại là dương tính giả.

Đó là trường hợp mô hình

dự đoán không chính xác các chữ số khác bằng 0.

Vì vậy hãy ghi nhớ,

bởi vì chúng ta đã thấy ma trận nhầm lẫn,

chúng ta cũng có thể tính toán con số này,

giá trị này từ ma trận nhầm lẫn.

Ví dụ: đối với chữ số 0,

chúng ta có thể tính toán giá trị chính xác này

bằng cách nhìn vào 962, là TP,

giá trị mà chúng tôi có ở đây

và kết quả dương tính giả là bảy, tức là một số

của sự phân loại sai trong cùng một cột.

Vì vậy, nếu chúng ta cộng tất cả các giá trị này vào đây,

điều đó mang lại cho chúng ta điều tương tự.

Vì vậy chúng ta cũng có thể sử dụng ma trận nhầm lẫn

để tính toán giá trị chính xác cho mô hình của chúng tôi.

Vì vậy, trong video này, chúng tôi đã có thể tạo

và giải thích ma trận độ chính xác

cho mỗi nhãn lớp trong mô hình học sâu.

Trong video tiếp theo, chúng ta sẽ xem xét một số liệu khác,

được gọi là thu hồi, đối với mỗi nhãn lớp,

để hiểu sâu hơn về các mô hình.