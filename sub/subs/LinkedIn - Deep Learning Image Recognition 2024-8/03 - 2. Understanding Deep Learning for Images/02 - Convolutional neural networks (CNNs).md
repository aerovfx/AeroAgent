# 02 - Mạng nơ ron tích chập (CNN)

---

- Bây giờ chúng tôi đã chuẩn bị dữ liệu của mình,

hãy tiếp tục và nói về mạng lưới thần kinh tích chập,

nói cách khác, CNN.

Vậy CNN là một lớp mạng lưới thần kinh sâu

chủ yếu được sử dụng để phân loại và nhận dạng hình ảnh.

Họ tự động và thích ứng

tìm hiểu hệ thống phân cấp không gian của các tính năng

từ những hình ảnh đầu vào mà chúng tôi cung cấp.

Vâng, công dụng này ở đâu?

Điều này được sử dụng rộng rãi trong các nhiệm vụ thị giác máy tính

chẳng hạn như nhận thức hình ảnh,

phát hiện và phân đoạn đối tượng.

Trong khi kiến trúc CNN bao gồm nhiều lớp khác nhau,

nó bắt đầu với lớp đầu vào để chấp nhận hình ảnh đầu vào,

ví dụ: hình ảnh 32x32 RGB cho tập dữ liệu của chúng tôi,

trong trường hợp này là CIFAR-10,

và sau đó nó có các lớp chập.

Nó áp dụng các bộ lọc tích chập

để trích xuất các đặc điểm từ ảnh đầu vào.

Nó có chức năng kích hoạt, ReLU.

Nó giới thiệu tính phi tuyến tính cho mô hình của chúng tôi.

Tiếp theo, chúng ta có các lớp tổng hợp

nơi nó lấy mẫu bản đồ đặc trưng

để giảm kích thước không gian

và do đó nó làm giảm độ phức tạp tính toán

điều này cũng làm cho mọi việc nhanh hơn.

Sau đó chúng ta có các lớp được kết nối đầy đủ.

Chúng tôi kết nối mọi nơ-ron trong một lớp

tới mọi nơ-ron ở lớp tiếp theo được sử dụng để phân loại.

Cuối cùng, chúng ta có một lớp đầu ra.

Nó tạo ra đầu ra cuối cùng.

Ví dụ: xác suất của lớp cho CIFAR-10.

Là ngựa, là ếch?

Nó có phải là một chiếc ô tô, vân vân.

Bây giờ hãy nói về các thành phần chính của CNN.

Về các lớp chập,

tìm hiểu các trình phát hiện tính năng như các cạnh, kết cấu và hình dạng.

Nhóm các lớp, điều này làm giảm kích thước không gian

của các bản đồ đặc trưng,

giữ lại các tính năng quan trọng nhất

điều đó quan trọng nhất với chúng tôi.

Làm phẳng lớp, nó chuyển đổi bản đồ đặc trưng 2D thành vectơ 1D.

Các lớp dày đặc, nó thực hiện phân loại

dựa trên các đặc trưng đã được trích xuất.

Một người bỏ học thì thế nào?

Một kỹ thuật chính quy hóa để ngăn chặn việc trang bị quá mức

bằng cách loại bỏ ngẫu nhiên các tế bào thần kinh trong quá trình huấn luyện.

Vâng, trường hợp sử dụng cụ thể của chúng tôi thì sao?

Chúng tôi sẽ sử dụng CNN với bộ dữ liệu CIFAR-10.

Một lần nữa, nó bao gồm 60.000 hình ảnh,

Hình ảnh màu 32x32 trong 10 lớp.

Chúng tôi đã thực hiện xong phần tiền xử lý.

Chúng tôi chuẩn hóa các giá trị pixel thành phạm vi 0, 1.

Chúng tôi đã chuyển đổi nhãn lớp thành vectơ được mã hóa một lần.

Còn định nghĩa mô hình thì sao?

Vâng, hãy sử dụng API tuần tự để xác định kiến ​​trúc CNN.

Điều này bao gồm các lớp chập, gộp và dày đặc.

Đào tạo, chúng tôi sẽ biên dịch mô hình bằng trình tối ưu hóa,

cái gọi là Trình tối ưu hóa Adam và chức năng mất mát

đó là entropy chéo phân loại.

Huấn luyện mô hình trên dữ liệu huấn luyện

và sau đó xác nhận dữ liệu thử nghiệm luôn.

Sau đó chúng ta sẽ có sự đánh giá,

đánh giá hiệu suất của mô hình trên dữ liệu thử nghiệm.

Trong khi CNN là công cụ mạnh mẽ để phân loại hình ảnh

và đã đạt được những kết quả tiên tiến

trong nhiều nhiệm vụ thị giác máy tính,

chúng ta sẽ thử nghiệm các kiến trúc khác nhau

và siêu tham số để cải thiện hiệu suất mô hình.

Và tài liệu TensorFlow và Keras

là những nguồn tài nguyên tuyệt vời để đọc thêm,

cũng như một số tài liệu nghiên cứu

nếu bạn quan tâm đến CNN

và ứng dụng của họ sẽ rất, rất có lợi.

Được rồi, tiếp theo, hãy chuyển sang mã

và bắt đầu tạo CNN của chúng tôi.

Vì vậy, lần trước chúng tôi đã dừng lại ở phần hiển thị hình ảnh.

Bây giờ hãy bắt đầu với việc mở tệp 02_02_begin.python

để bắt đầu tạo mạng lưới thần kinh tích chập của chúng tôi.

Vì vậy chúng ta sẽ tiếp tục

và xác định một mô hình CNN đơn giản

dựa trên những gì chúng ta vừa thảo luận trong bài thuyết trình.

Vì vậy để xác định điều đó,

chúng ta sẽ tạo một hàm Python,

bắt đầu bằng create_simple_cnn_model.

Và trong hàm này, chúng ta sẽ có các lớp sau,

Conv2D như chúng ta đã thảo luận

và sau đó chúng ta sẽ tiếp tục

và cho kết quả là 32, 3, 3.

Tiếp theo, chúng ta sẽ phải kích hoạt ReLU

và sau đó chúng ta sẽ đưa ra hình dạng đầu vào là 32 x 32, thành 3.

Tiếp theo chúng ta sẽ thêm lớp tổng hợp tối đa.

Vì vậy, nó sẽ có tổng hợp tối đa 2D,

và sau đó chúng ta sẽ có nó 2 x 2.

Tiếp theo chúng ta sẽ thêm lượt chuyển đổi

vào lớp một lần nữa,

và sau đó chúng tôi sẽ tiếp tục thêm nhiều lớp hơn vào đó.

Được rồi, bây giờ chúng ta có chức năng tạo mô hình CNN đơn giản

được xác định bằng các lớp khác nhau.

Chúng ta hãy xem xét tất cả điều này có nghĩa là gì.

Vâng, trước hết, điều này khởi tạo một mô hình tuần tự.

Khi chúng ta nói tuần tự, đó là một chồng các lớp tuyến tính.

Sau đó, chúng tôi theo dõi nó bằng Conv2D,

là lớp tích chập 2D với 32 bộ lọc mỗi lớp

có kích thước 3x3.

Lớp này sẽ quét hình ảnh đầu vào có kích thước 32

bằng hình ảnh 32 RGB để phát hiện các tính năng mà chúng tôi có.

Tiếp theo, chúng tôi xác định relu kích hoạt.

Điều này áp dụng relu,

đó là hàm kích hoạt đơn vị tuyến tính được chỉnh lưu,

giới thiệu tính phi tuyến tính cho mô hình

bằng cách loại bỏ các giá trị âm cho chúng ta.

Vì vậy tất cả những gì nó làm là loại bỏ các giá trị âm

và chúng tôi đưa ra hình dạng đầu vào.

Điều này chỉ định hình dạng của hình ảnh đầu vào.

Vậy đó là 32 x 32 pixel

với 3 kênh màu là RGB.

Đó là ý nghĩa của RGB. Sau đó, chúng tôi thêm tổng hợp tối đa 2D.

Điều này thêm một lớp tổng hợp tối đa với bộ lọc 2 x 2.

Lớp này làm giảm kích thước không gian, tức là chiều cao

và chiều rộng của bản đồ đặc điểm

bằng cách lấy giá trị tối đa trong mỗi khối 2 x 2.

Chức năng của nó chỉ đơn giản là giúp giảm mẫu đầu vào

và giảm số lượng tham số

bởi nó làm giảm sự mở rộng

về sức mạnh tính toán mà chúng ta cần.

Tiếp theo chúng ta thêm Conv2D.

Trong khi điều này thêm một lớp chập 2D khác,

với thời gian này, 64 bộ lọc có kích thước 3 x 3.

Lớp này sẽ tìm hiểu các tính năng phức tạp hơn từ đầu vào.

Một lần nữa, chúng ta có relu kích hoạt.

Đây là hàm kích hoạt để giới thiệu tính phi tuyến tính.

Sau đó, chúng ta có một lớp 2D tổng hợp tối đa khác.

Đây lại là bộ lọc 2 x 2

để tiếp tục lấy mẫu các bản đồ đặc trưng.

Sau đó chúng ta tiếp tục và làm phẳng.

Điều này làm phẳng các bản đồ đặc trưng 2D thành một vectơ 1D.

ánh xạ vào vector A 1D.

Bước cụ thể này chuẩn bị dữ liệu

Tiếp theo, chúng ta có kích hoạt dày đặc 64 tương đương với relu.

Tiếp theo, chúng ta có kích hoạt dày đặc 64 tương đương với ulu.

Điều này bổ sung thêm một lớp được kết nối đầy đủ, nói cách khác, dày đặc

với 64 nơ-ron.

Mỗi nơ-ron được kết nối

tới tất cả các nơ-ron ở lớp trước.

Vì vậy, không có tế bào thần kinh lỏng lẻo trong trường hợp này.

Một lần nữa, kích hoạt là relu.

Tiếp theo chúng ta có lớp bỏ học.

Đây là một lớp có tỷ lệ bỏ học là 0,5.

Lớp này đặt ngẫu nhiên 50% đơn vị đầu vào

về 0 ở mỗi lần cập nhật trong thời gian đào tạo

để ngăn chặn việc lắp quá mức.

Kích hoạt dày đặc 10 dấu phẩy tương đương với softmax.

Sau đó, 10 lần kích hoạt bằng softmax.

một cho mỗi lớp trong tập dữ liệu.

Chúng tôi sử dụng kích hoạt bằng softmax.

Trong tập dữ liệu, chúng tôi sử dụng kích hoạt bằng softmax.

đưa ra phân bố xác suất

trên 10 lớp.

10 lớp.

Sau đó chúng tôi đóng định nghĩa mô hình tuần tự

và chúng tôi trả lại mô hình.

Vì vậy hàm đặc biệt này xây dựng một mô hình CNN đơn giản

với hai lớp chập, theo sau

một lớp bỏ học và một lớp dày đặc cuối cùng

với kích hoạt tối đa mềm để phân loại.

để phân loại.

Mặc dù kiến trúc đặc biệt này phù hợp

là tập dữ liệu chúng tôi đang làm việc cùng, tập dữ liệu CIFAR-10.

là dữ liệu chúng tôi đang làm việc với tập dữ liệu C far 10.

Vì vậy hãy chắc chắn rằng chúng ta

có sẵn và tồn tại thư mục đầu ra.

và hiện có.

Vì vậy hãy tiếp tục và chèn nó vào đây.

Tiếp theo, chúng ta sẽ có một con đường

mà chúng tôi sẽ lưu mô hình vào đó.

Một lần nữa, chúng ta hãy tiếp tục và đưa ra con đường ở đây.

chúng ta sẽ tiếp tục và gọi nó là cifar10_simple_model.h5.

Chấm h5 có nghĩa là tên,

H năm có nghĩa là tên,

Được rồi, vậy tiếp theo, chúng ta sẽ làm gì

là chúng ta sẽ kiểm tra xem mô hình đã tồn tại chưa.

đã tồn tại rồi.

Nếu nó đã tồn tại thì chúng ta chỉ cần sử dụng lại

nếu chúng ta muốn, hoặc chúng ta có thể tiếp tục và chạy lại nó.

Vì vậy tôi sẽ mang đoạn mã đó đến đây

và sau đó bắt đầu giải thích nó.

Vì vậy, trước tiên chúng ta sẽ kiểm tra xem mô hình này đã tồn tại chưa.

Nếu không, chúng ta sẽ bắt đầu

tạo mô hình CNN đơn giản mà chúng ta vừa xác định.

mô hình chúng ta vừa xác định.

Vì vậy, chúng tôi sẽ biên dịch nó, chúng tôi sẽ cung cấp trình tối ưu hóa,

chúng tôi sẽ đưa ra khoản lỗ và chúng tôi sẽ đưa ra giá trị số liệu.

Sau đó chúng ta sẽ nhận được bản tóm tắt mô hình.

Chúng ta sẽ nhận được một số âm mưu cho chúng ta biết về

mô hình của chúng tôi hoạt động như thế nào xét về độ chính xác,

và sau đó chúng tôi sẽ đánh giá điều đó.

Sau đó, chúng ta sẽ lưu biểu đồ đó vào thư mục biểu đồ đầu ra.

Vì vậy, hãy tiếp tục và viết mã đó, đánh giá mô hình

trên dữ liệu thử nghiệm để có được sự mất mát và độ chính xác.

Khi đó chúng ta sẽ có kết quả kiểm tra bị mất, độ chính xác của bài kiểm tra,

bằng với model.evaluate,

và sau đó chúng tôi sẽ đưa ra bài kiểm tra X bài kiểm tra Y.

Thế thôi.

Sau đó chúng ta sẽ tiếp tục và in ra kết quả kiểm tra độ chính xác của F bằng.

Được rồi, chúng ta sẽ có nó bằng nhau

để mở dấu ngoặc nhọn và nói độ chính xác của bài kiểm tra.

Thế thôi.

Vì vậy, những gì chúng tôi đã làm ở đây là chúng tôi đã xác định được mô hình CNN.

Sau đó, chúng tôi xem xét liệu mô hình đã tồn tại chưa, nếu có,

chúng ta có thể sử dụng lại mô hình đã có sẵn.

Nếu không, hãy tiếp tục và tạo một cái mới.

Sau đó chúng tôi đã đi trước

và lưu nó vào thư mục lô đầu ra.

Và sau đó chúng tôi đang in hiệu suất của mô hình này.

Vì vậy, hãy tìm tệp Python cuối cùng,

đã được hoàn thành với tất cả mã chúng tôi đã hiển thị.

Hãy tiếp tục và nhấp vào chạy,

và nó sẽ cho chúng ta biết rằng chúng ta đã có mô hình rồi

trong thư mục đầu ra.

Vì vậy, bạn thực sự có thể sử dụng mô hình hiện có,

hoặc bạn có thể tiếp tục và tạo một cái.

Tùy bạn đấy.

Nó sẽ cung cấp cho bạn độ chính xác kiểm tra của mô hình hiện có.

Nếu bạn muốn xây dựng một cái mới,

tìm mô hình đơn giản, tiếp tục và xóa nó.

Bây giờ chúng ta đã xóa mô hình đơn giản, hãy tiếp tục

và chạy tệp Python này một lần nữa.

Những gì nó sẽ làm là nó sẽ thực sự tạo lại mô hình này

bởi vì chúng ta không còn mô hình đơn giản này ở đây nữa phải không?

Bởi vì chúng ta không có mô hình đơn giản,

nó sẽ trải qua các thời kỳ tạo ra nó,

và sau đó nó sẽ tạo một mô hình mới, lưu mô hình đơn giản ở đây,

và sau đó lưu cốt truyện mới vào phần cốt truyện,

mà chúng ta có cốt truyện cũ ở đây.

Nó sẽ ghi đè lên nó và chúng tôi thấy rằng độ chính xác

là dưới 0,6 một chút.

Vì vậy, có chỗ để cải thiện,

nhưng không quá tệ đối với một mô hình CNN đơn giản.

Vì vậy sẽ mất thêm hai kỷ nguyên nữa để hoàn thành,

và sau đó chúng ta sẽ có thể thấy mô hình mới

và sau đó là biểu đồ hình ảnh hiển thị bị ghi đè.

Được rồi, bây giờ chúng ta đã hoàn thành mô hình đơn giản.

Chúng ta có thể đi kiểm tra độ chính xác của bài kiểm tra và nó là 0,6179.

Bây giờ hãy nhớ rằng, mỗi khi bạn chạy mô hình mới này,

nó sẽ có độ chính xác khác vì hình ảnh

và các lựa chọn được chọn ngẫu nhiên,

vì vậy nó hoàn toàn bình thường và ổn.

Và chúng ta có thể tiếp tục

và kiểm tra mô hình PNG đơn giản,

và xem độ chính xác so với kỷ nguyên ở đây.

Và thế là xong.

Chúng tôi vừa tạo mô hình CNN đơn giản,

và bạn có thể thấy nó trong 02_02.python.