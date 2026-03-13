# 04 - Giảm dần độ dốc

---

- [Người hướng dẫn] Giảm độ dốc

là một kỹ thuật tối ưu hóa cơ bản

được sử dụng rộng rãi trong học sâu

và nhiều thuật toán học máy khác.

Mục đích là tìm các thông số tối ưu

làm giảm thiểu một hàm mất mát nhất định.

Để nắm bắt độ dốc giảm dần,

điều quan trọng là phải hiểu khái niệm về hàm mất mát.

Hãy tưởng tượng bạn đang đào tạo một người mẫu

để dự đoán một cái gì đó như giá nhà.

Sau khi huấn luyện về một số dữ liệu,

mô hình đưa ra những dự đoán có thể không khớp hoàn toàn

giá thực tế.

Hàm mất mát là một công thức toán học

đo lường mức độ tệ hại của những dự đoán đó

so với số liệu thực tế.

Về cơ bản, nó định lượng sự khác biệt

giữa giá trị dự đoán và giá trị thực.

Mục tiêu khi huấn luyện mạng nơ-ron

là liên tục điều chỉnh các thông số mạng

để làm cho sự mất mát càng nhỏ càng tốt,

có nghĩa là các dự đoán càng gần càng tốt

đến các giá trị thực tế.

Bây giờ hãy tưởng tượng rằng với tất cả các giá trị có thể

của một tham số cụ thể theta,

chúng tôi ánh xạ giá trị của hàm mất.

Cốt truyện sẽ trông giống như một phong cảnh

hoặc bề mặt đồi núi gập ghềnh,

trong đó chiều cao tại bất kỳ điểm nào đại diện cho

giá trị của sự mất mát, tức là dự đoán tệ đến mức nào.

Điểm cao thể hiện tổn thất cao hơn,

nghĩa là, những dự đoán tồi tệ hơn.

Điểm thấp thể hiện tổn thất thấp hơn,

nghĩa là dự đoán tốt hơn.

Mục tiêu của việc giảm độ dốc là di chuyển

băng qua bề mặt đồi núi này để tìm điểm thấp nhất

hoặc tổn thất thấp nhất.

Giá trị tham số tại thời điểm này

là giá trị tối ưu làm giảm thiểu hàm mất mát.

Vậy quá trình giảm độ dốc hoạt động như thế nào?

Giả sử chúng ta bắt đầu ở một giá trị tham số ngẫu nhiên theta nào đó,

tương ứng với điểm này

trên bối cảnh chức năng mất mát.

Giảm dần độ dốc bắt đầu bằng cách tính toán độ dốc

của hàm mất mát tại thời điểm đó.

Chúng ta có thể coi gradient là độ dốc

điều đó cho chúng ta biết tổn thất sẽ thay đổi bao nhiêu

nếu chúng ta điều chỉnh tham số một chút.

Độ dốc lớn hoặc độ dốc lớn

có nghĩa là những thay đổi nhỏ trong theta sẽ dẫn đến

trong những thay đổi đáng kể về tổn thất.

Tuy nhiên, độ dốc thoải hoặc độ dốc nhỏ

có nghĩa là những thay đổi trong theta sẽ có tác động ít rõ rệt hơn

về sự mất mát.

Về mặt toán học, độ dốc hoặc độ dốc tại bất kỳ điểm nào

trên đường cong hàm tổn thất có thể được tính toán

là đạo hàm của hàm mất mát L

đối với tham số theta.

Nếu đạo hàm của hàm loss là dương,

tăng theta làm cho sự mất mát lớn hơn.

Do đó, thuật toán giảm độ dốc

giảm giá trị của theta để giảm thiểu tổn thất.

Tuy nhiên, nếu đạo hàm của hàm loss là âm,

tăng theta sẽ làm giảm tổn thất.

Trong trường hợp này, thuật toán giảm độ dốc sẽ điều chỉnh theta

bằng cách tăng giá trị của nó để tiến gần hơn đến tổn thất tối thiểu.

Quá trình tính toán độ dốc này

ở theta hiện tại và điều chỉnh theta

theo hướng ngược lại của gradient tiếp tục

cho đến khi gradient gần bằng 0,

chỉ ra rằng theta đã đạt đến một điểm

nơi tổn thất được giảm thiểu

hoặc gần với mức tối thiểu cục bộ.

Mức độ mà giá trị theta được điều chỉnh mỗi lần

để đáp ứng với độ dốc được hướng dẫn

bởi tham số do người dùng xác định được gọi là tốc độ học tập

bằng cách sử dụng công thức hiển thị ở đây.

Lựa chọn tốc độ học tập phù hợp là rất quan trọng

để đảm bảo sự hội tụ hiệu quả và chính xác

đến giải pháp tối ưu.

Tỷ lệ học cao dẫn đến những thay đổi lớn hơn trong theta,

có thể tăng tốc độ hội tụ,

nhưng có thể có nguy cơ vượt quá mức tối thiểu.

Mặt khác, kết quả là tỷ lệ học tập thấp

trong những điều chỉnh nhỏ hơn, chính xác hơn đối với theta,

có thể làm chậm quá trình hội tụ

hoặc dẫn đến việc mô hình bị kẹt ở mức tối thiểu cục bộ

đó không phải là giá trị tốt nhất có thể cho theta.

Giảm dần độ dốc là nền tảng của việc tối ưu hóa

trong học máy, cho phép các mô hình

để học hỏi từ dữ liệu bằng cách tinh chỉnh lặp đi lặp lại các tham số của chúng

để giảm thiểu lỗi.