# 02 - Áp dụng chuẩn hóa batch cho mô hình deep learning

---

- [Người hướng dẫn] Trong video này,

bạn sẽ học cách áp dụng chuẩn hóa hàng loạt

sang mô hình học sâu.

Tôi sẽ viết mã trong tệp 05_02e.

Bạn có thể làm theo bằng cách hoàn thành các ô mã trống

trong tệp 05_02b.

Lưu ý rằng đây là video đầu tiên trong chuỗi ba video

hướng dẫn bạn cách áp dụng chuẩn hóa hàng loạt,

cắt độ dốc, dừng sớm,

và lập kế hoạch tốc độ học tập cho một mô hình học sâu.

Hãy bắt đầu bằng cách chạy đoạn mã đã viết trước đó

để nhập và xử lý trước dữ liệu.

Vậy điều đầu tiên tôi cần làm ở đây

thực sự là chọn kernel cho môi trường của tôi.

Vì vậy, Môi trường Python.

Tôi sẽ nói Python 3.10.

Bây giờ tôi sẽ nhấp vào ô mã tiếp theo,

và tôi sẽ nói Chạy trước.

Được rồi, vậy hãy tiếp tục và chạy đoạn mã trên

để nhập và xử lý trước dữ liệu.

Được rồi, thế là xong.

Vì vậy, mô hình của chúng tôi bao gồm một lớp đầu vào với 784 nút,

hai lớp ẩn với 512 và 128 nút tương ứng,

và một lớp đầu ra với 10 nút.

Giữa mỗi lớp ẩn,

chúng tôi sẽ bình thường hóa kết quả đầu ra của một lớp

trước khi cho chúng ăn tiếp theo.

Đây là những gì chúng ta gọi là chuẩn hóa hàng loạt.

Chuẩn hóa hàng loạt có thể ổn định việc đào tạo

của mô hình deep learning và giúp nó hội tụ nhanh hơn.

Để áp dụng chuẩn hóa hàng loạt cho một mô hình,

chúng tôi chỉ cần đưa lớp BatchNormalization vào mô hình.

Vì vậy, ở đây chúng ta sẽ nhập Đầu vào,

Các lớp dày đặc và BatchNormalization

sử dụng keras.layers.

Vì vậy, khi chúng tôi xác định mô hình của mình,

chúng tôi chỉ định keras.Sequential để khởi tạo mô hình.

Chỉ định lớp đầu vào.

Lớp dày đặc đầu tiên, là lớp ẩn đầu tiên.

512 nút có chức năng kích hoạt relu.

Và giữa lớp đó và lớp dày đặc tiếp theo,

chúng tôi chỉ định một lớp BatchN normalization. Thế thôi.

Chúng ta làm điều tương tự một lần nữa

giữa lớp dày đặc thứ hai và lớp đầu ra.

Vì vậy, hãy tiếp tục và chạy nó để khởi tạo mô hình của chúng ta.

Và vì vậy, vâng, lỗi mà chúng tôi gặp phải ở đây,

hoặc cái mà chúng ta có ở đây thực ra là lành tính,

nên không có gì phải lo lắng.

Tất cả những gì nó muốn nói là môi trường của chúng ta chưa được thiết lập

để sử dụng GPU.

Chúng tôi sẽ không sử dụng GPU cho những ví dụ này,

nên chúng ta nên đi thôi. Được rồi?

Làm tốt lắm.

Chúng tôi đã áp dụng thành công chuẩn hóa hàng loạt

đến mô hình học sâu trong Python. Đó là nó.

Tiếp theo, chúng ta thảo luận về việc cắt gradient là gì,

và sau đó chúng ta sẽ hướng dẫn cách sử dụng nó trong Python.