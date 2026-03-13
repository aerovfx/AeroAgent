# 04 - Xác định mô hình học sâu có thể điều chỉnh được trong Keras

---

- [Người hướng dẫn] Trong video này, bạn sẽ học cách

để xác định một mô hình học sâu có thể điều chỉnh

để chuẩn bị cho việc điều chỉnh siêu tham số.

Tôi sẽ chạy mã trong tệp 04_04e.

Bạn có thể làm theo bằng cách hoàn thành các ô mã trống

trong tệp 04_04b.

Lưu ý rằng đây là video đầu tiên

trong chuỗi hai video hướng dẫn bạn cách

để điều chỉnh các siêu tham số của mô hình học sâu.

Đảm bảo chạy mã đã viết trước đó để nhập

và xử lý trước dữ liệu cũng như xây dựng

và huấn luyện mô hình cơ sở.

Tôi đã làm như vậy rồi.

Vì vậy, đoạn mã được viết trước đó đã được chạy ở trên

để tạo ra một mô hình cơ sở.

Bây giờ chúng ta sẽ xác định một kiến ​​trúc mô hình có thể điều chỉnh được.

Trước khi chúng ta tìm kiếm các siêu tham số tối ưu

đối với một mô hình, chúng ta cần xác định một hàm

trong đó xác định bản thiết kế kiến trúc của mô hình.

Kế hoạch chi tiết sẽ kết hợp các siêu tham số

về số lượng đơn vị trên mỗi lớp, tỷ lệ bỏ học,

và tốc độ học tối ưu hóa.

Keras Tuner sẽ gọi chức năng này

sau này nhiều lần

với các giá trị siêu tham số khác nhau

để tìm ra sự kết hợp tối ưu

giúp tối đa hóa độ chính xác xác thực.

Vì vậy trước khi tiếp tục, trước tiên chúng ta cần

để nhập khẩu một vài thứ.

Đầu tiên là lớp bỏ học.

Vì vậy, chúng tôi nhập Dropout từ tensorflow.keras.layers.

Tiếp theo, chúng tôi nhập trình tối ưu hóa Adam

từ tensorflow.keras.optimizers.

Bây giờ chúng ta xác định hàm có thể điều chỉnh được, hàm

điều đó thực sự xác định mô hình của chúng tôi.

Vì vậy chúng ta sẽ gọi hàm này là build_model,

và chúng ta sẽ chỉ định một đối số hp đại diện cho mỗi

của các siêu tham số mà chúng tôi đang cố gắng điều chỉnh.

Vì vậy, chúng tôi bắt đầu bằng cách khởi tạo mô hình của mình,

vì vậy keras.Sequential, sau đó chúng tôi chỉ định lớp đầu vào.

Hình dạng là 784, vì vậy chúng ta đã thấy điều này sớm hơn.

Đọc ở trên bạn sẽ hiểu rõ hơn

về những gì đang diễn ra ở đây.

Việc tiếp theo chúng tôi làm là

để thêm lớp dày đặc đầu tiên, lớp ẩn đầu tiên.

Vì vậy, trong lớp dày đặc này, chúng ta sẽ

để thử các giá trị siêu tham số,

hoặc số lượng tế bào thần kinh ở đây cho lớp dày đặc này,

trong khoảng từ 32 đến 512.

Vì vậy chúng tôi chỉ định hp.Int, có nghĩa là

rằng các giá trị siêu tham số sẽ là giá trị nguyên.

Và chúng ta sẽ gọi cái này là Hidden1.

Đây chỉ là nhãn để mô tả lớp này.

Và chúng ta sẽ đi từ 32 đến 512,

và với bước 32, có nghĩa là

chúng tôi sẽ thử giá trị của 32 nơ-ron,

rồi cộng thêm 32, tức là 64 nơ-ron

vân vân, cho đến tận 512 nơ-ron.

Lớp tiếp theo là lớp bỏ học.

Chúng tôi sẽ cố gắng, chúng tôi sẽ sử dụng tỷ lệ bỏ học

trong khoảng từ 0,1 đến 0,5 với bước 0,1.

Vì vậy chúng tôi sẽ thử tỷ lệ bỏ học

là 0,1, 0,2, 0,3, 0,4 và 0,5.

Vì vậy ý tưởng ở đây là có thể

để tìm ra chính xác tỷ lệ bỏ học nào trong số đó

đối với lớp này là tốt nhất cho mô hình này.

Vì vậy, chúng tôi chỉ định hp.Float, biểu thị

rằng các giá trị siêu tham số đang diễn ra

là số float hoặc số thập phân.

Lớp ẩn thứ hai chúng tôi gọi là Hidden2.

Bây giờ chúng ta cũng sẽ thử nhiều giá trị nơ-ron, số

của các giá trị nơ-ron, các giá trị số nguyên

từ 16 đến 128 với bước 16.

Vậy điều đó có nghĩa là giá trị đầu tiên sẽ là 16,

sau đó chúng ta thử 32, và từ đó chúng ta đi tiếp.

Vì vậy chúng ta sẽ thử lấy 16 đến tận 128.

Chúng tôi thêm một lớp bỏ học khác.

Lần này chúng tôi cũng đánh giá tỷ lệ bỏ học

trong khoảng từ 0,1 đến 0,5 với bước nhảy 0,1.

Cuối cùng, chúng ta chỉ định lớp đầu ra của mình, phải không?

Vì vậy, lớp đầu ra của chúng tôi sẽ không phải là một siêu tham số

cần phải điều chỉnh vì điều này bị hạn chế

đến số lượng kết quả có thể xảy ra trong mô hình của chúng tôi.

Vì vậy, đây sẽ là lớp đầu ra điển hình

với đơn vị là 10, nghĩa là

rằng sẽ có 10 nơ-ron

trong lớp đầu ra này hoặc 10 nút.

Cuối cùng, chúng ta sẽ tiếp tục

và chỉ định các giá trị tốc độ học tập,

giá trị tốc độ học tập tiềm năng cho trình tối ưu hóa của chúng ta, phải không?

Vì vậy, ở đây chúng ta sẽ sử dụng, như chúng ta đã làm trước đây,

chúng tôi sử dụng hp.Float, hp.Int cho các giá trị nguyên.

Ở đây chúng ta sẽ nói hp.Choice, có nghĩa là

rằng chúng ta sẽ có những giá trị rời rạc

mà chúng tôi muốn đánh giá.

Lần này chúng ta sẽ đánh giá các giá trị

là 0,0001, 0,001 hoặc 0,01.

Vì vậy, đó là những gì chúng tôi đã chỉ định ở đây làm giá trị có thể

để đánh giá trong quá trình điều chỉnh siêu tham số.

Và cuối cùng, chúng ta muốn mô hình của mình được biên dịch ngay bây giờ, phải không?

Vì vậy chúng tôi chỉ định model.compile.

Chúng tôi chỉ định trình tối ưu hóa Adam là trình tối ưu hóa mà chúng tôi muốn sử dụng,

và chúng tôi chỉ định các giá trị tốc độ học tập để đánh giá,

đó là những giá trị mà chúng tôi đã chỉ định ở đây.

Vì vậy, mỗi khi hàm được gọi

trong quá trình điều chỉnh siêu tham số,

nó sẽ đánh giá những tỷ lệ học tập khác nhau

cùng với các siêu tham số khác

mà chúng tôi đang cố gắng đánh giá.

Và sau đó sự mất mát là entropy chéo phân loại.

Và số liệu mà chúng tôi muốn sử dụng

để đánh giá hiệu suất là độ chính xác, được chứ?

Vì vậy, đây thực sự là cách chúng tôi xác định một mô hình có thể điều chỉnh được

để điều chỉnh siêu tham số.

Vì vậy, tôi sẽ tiếp tục và chạy cái này.

Tất cả điều này làm vào thời điểm này chỉ là

chuẩn bị sẵn mô hình, chức năng sẵn sàng, vì vậy

rằng khi chúng tôi thực sự thực hiện tìm kiếm siêu tham số,

chức năng này được gọi đi gọi lại nhiều lần.

Và điều này cho phép chúng ta có thể tìm kiếm trong không gian.

Vì vậy, tiếp theo, chúng ta sẽ tìm hiểu quy trình

chạy tìm kiếm siêu tham số

để xác định tập hợp tối ưu

siêu tham số cho vấn đề của chúng tôi.

Hẹn gặp lại bạn ở phía bên kia.