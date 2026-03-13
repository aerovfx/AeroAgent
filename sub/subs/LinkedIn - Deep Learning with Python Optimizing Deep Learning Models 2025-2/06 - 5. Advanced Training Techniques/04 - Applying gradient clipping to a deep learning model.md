# 04 - Áp dụng cắt giảm độ dốc cho mô hình học sâu

---

- Trong video này, bạn sẽ học cách áp dụng

cắt gradient thành mô hình học sâu trong Python.

Tôi sẽ viết mã trong tệp 05_04 E.

Bạn có thể làm theo bằng cách hoàn thành các ô mã trống

trong tệp 05_04 B.

Lưu ý rằng đây là video thứ hai trong chuỗi ba video

hướng dẫn bạn cách áp dụng chuẩn hóa hàng loạt,

cắt độ dốc, dừng sớm,

và lập kế hoạch tốc độ học cho mô hình học sâu.

Nếu bạn chưa làm như vậy, hãy xem video về cách đăng ký

chuẩn hóa hàng loạt sang mô hình học sâu

để được giải thích chi tiết về mã trước đó.

Trước khi bắt đầu, hãy chạy mã chúng tôi đã tạo trong video đó

để môi trường của chúng ta tăng tốc.

Vì vậy, điều đầu tiên tôi cần làm

là chỉ định hạt nhân của tôi,

lấy môi trường Python của tôi, 3.10.

Tôi sẽ nhấp vào ô mã tiếp theo của mình

và nói chạy tất cả ở trên.

Tôi sẽ cuộn lên một chút để đảm bảo

Tôi biết khi nào mọi việc đã xong.

Được rồi. Vì vậy bây giờ chúng ta đã xác định

kiến trúc mô hình của chúng ta, hãy biên dịch nó

bằng cách chỉ định trình tối ưu hóa, hàm mất

và số liệu hiệu suất để tối ưu hóa.

Chúng tôi sẽ sử dụng trình tối ưu hóa Adam cho mô hình của mình.

Theo mặc định, trình tối ưu hóa không áp đặt bất kỳ giới hạn nào đối với độ dốc.

Tuy nhiên, độ dốc lớn có thể khiến các tham số của mô hình

dao động đáng kể trong quá trình đào tạo

và cản trở sự hội tụ.

Việc cắt giảm độ dốc giảm thiểu vấn đề này

bằng cách giới hạn độ lớn hoặc chuẩn mực của độ dốc.

Để thực hiện cắt độ dốc,

chúng tôi đặt đối số clipnorm bằng trình tối ưu hóa Adam.

Điều này đảm bảo rằng chuẩn L2 của gradient

không vượt quá giá trị mà chúng tôi chỉ định,

trong trường hợp này là 1.0.

Vì vậy, để bắt đầu, chúng tôi nhập trình tối ưu hóa, Adam,

bằng cách sử dụng keras.optimizers.

Sau đó, chúng tôi chỉ định hoặc thực sự biên dịch mô hình của mình.

Và chúng ta nói người tối ưu hóa là Adam.

Trong hàm tối ưu hóa Adam, chúng tôi chỉ định clipnorm.

Vì vậy chúng ta nói clipnorm bằng 1,

mất mát là entropy chéo phân loại,

và số liệu chúng tôi sắp sử dụng là độ chính xác.

Vì vậy, hãy tiếp tục và chạy nó.

Vì vậy, hãy lưu ý rằng chúng ta có thể điều chỉnh giá trị clipnorm này, đúng không.

Vì vậy, ở đây chúng tôi sử dụng 1.0, nhưng chúng tôi có thể điều chỉnh nó khi thấy phù hợp

dựa trên tập dữ liệu hoặc vấn đề của chúng tôi.

Ngoài ra, chúng ta cũng có thể sử dụng đối số clipvalue

để cắt các gradient theo giá trị thay vì theo định mức.

Vì vậy, quá trình mà chúng ta vừa trải qua bây giờ

là cách chúng tôi áp dụng việc cắt dải màu

đến mô hình học sâu trong Python.

Tiếp theo, chúng ta sẽ tìm hiểu cách dừng sớm, kiểm tra điểm

và công việc lập kế hoạch tốc độ học tập.