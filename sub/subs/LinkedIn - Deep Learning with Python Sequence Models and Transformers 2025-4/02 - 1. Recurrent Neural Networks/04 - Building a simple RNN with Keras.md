# 04 - Xây dựng RNN đơn giản với Keras

---

- [Hướng dẫn] Trong video này,

chúng ta sẽ xây dựng một mạng lưới thần kinh tái diễn

bằng Python bằng Keras.

Mô hình chúng tôi sắp xây dựng

là một mô hình phân tích tình cảm.

Vì vậy, trước khi bắt đầu, hãy chọn kernel của chúng ta.

Và tôi đã chạy trước mã để tiết kiệm thời gian ở đây.

Vì vậy đối với hướng dẫn này,

chúng ta sẽ cần hai gói,

TensorFlow và Keras.

Và nếu bạn muốn biết thêm một chút

về xây dựng mô hình deep learning

bằng Python sử dụng TensorFlow và Keras,

Tôi khuyên bạn nên xem các video khóa học khác của tôi.

Khóa học có tiêu đề

"Học sâu với nền tảng Python."

Vì vậy, để bắt đầu, chúng tôi muốn tiếp tục và nhập Keras

từ gói TensorFlow.

Và chúng tôi cũng muốn nhập gói Lớp.

Chúng ta sẽ sử dụng hai lớp này để định nghĩa

và xây dựng mô hình mà chúng tôi muốn làm việc hôm nay.

Điều tiếp theo chúng ta làm ở đây là chỉ định một hạt giống.

Lý do tại sao chúng tôi làm điều này là để tạo ra một mã xác định,

điều đó có nghĩa là càng nhiều càng tốt

khi tôi chạy mã của mình và bạn chạy mã trên máy của mình,

kết quả tương tự hoặc nếu không giống nhau.

Vì vậy, tập dữ liệu chúng ta sẽ sử dụng ngày hôm nay

là tập dữ liệu đánh giá phim IMDB.

Và trong tập dữ liệu này,

chúng tôi có 50.000 bài đánh giá phim được dán nhãn

như tích cực hoặc tiêu cực.

Và ý tưởng phân tích tình cảm

là có thể phân tích văn bản để xem xét

và phân loại đánh giá đó là tích cực hay tiêu cực.

Vậy chúng ta sẽ làm gì

là chúng tôi thực sự sẽ tiếp tục và tải tập dữ liệu của mình,

nhưng chúng tôi cũng muốn giới hạn kích thước

về những gì chúng ta sẽ làm việc cùng.

Vì vậy, chúng tôi chỉ định giá trị tính năng tối đa là 10.000.

Điều này có nghĩa là chúng ta chỉ muốn nhìn vào những từ ngữ

đó là 10.000 từ xuất hiện thường xuyên nhất

thực tế cho từng tập dữ liệu.

Và vì vậy chúng tôi muốn hạn chế sự tập trung của mình

chỉ những tính năng đó khi chúng tôi xây dựng mô hình của mình.

Vì vậy, chúng tôi tiếp tục và chỉ định số lượng tính năng tối đa là 10.000,

và sau đó chúng tôi nhập tập dữ liệu của mình

từ hàm dữ liệu imdb.load

trong gói keras.datasets.

Khi tập dữ liệu của chúng tôi được đưa vào,

điều tiếp theo chúng ta sẽ làm là xử lý trước nó.

Và điều chúng tôi đang làm ở đây là chúng tôi sẽ cố định độ dài

trong số các đánh giá mà chúng tôi sắp phân tích.

Vì vậy, nếu bài đánh giá dài hơn 500 từ,

chúng tôi sẽ cắt ngắn nó.

Nhưng nếu nó dài dưới 500 từ,

chúng tôi sẽ đệm nó,

Lối này,

nó giữ các giá trị đầu vào hoặc chuỗi đầu vào,

hằng số vectơ sao cho mạng nơ-ron hồi quy

mong đợi vectơ có kích thước nhất định

và nó sẽ được đặt ở mức 500 từ.

Và vì thế mỗi đầu vào được đưa vào,

mỗi đợt nhập hàng sẽ có số lượng hạn chế

đến 500 từ hoặc 500 thẻ.

Đó chính là điều chúng tôi đang làm ở đây trong mã của mình

là chúng tôi chỉ định độ dài tối đa.

Và sau đó chúng tôi đệm cả dữ liệu huấn luyện và dữ liệu kiểm tra.

Đó là tất cả những gì chúng ta cần làm vào thời điểm này

để nhập và xử lý trước dữ liệu của chúng tôi.

Bước tiếp theo là xác định kiến ​​trúc mô hình.

Và chúng tôi cũng làm điều này trong khóa học trước,

khóa học của nền tảng.

Nhưng ở đây,

chúng ta sẽ định nghĩa một mạng lưới thần kinh tái diễn

sử dụng một khung tuần tự.

Vì vậy, điều đầu tiên chúng ta làm là khởi tạo.

Vì vậy, chúng tôi nói keras.Sequential.

Và sau đó chúng tôi chỉ định lớp đầu vào,

đó là các lớp. Nhúng.

Ở đây chúng tôi đang nói rằng lớp đầu vào này

sẽ có những tính năng tối đa,

và nó sẽ xuất ra 128 giá trị.

Và vì vậy những giá trị đó bây giờ sẽ được chuyển sang lớp tiếp theo,

đó là các nút ở lớp tiếp theo,

sẽ là RNN, các lớp của lớp RNN đơn giản.

Và nút đó cũng có 32,

lớp có 32 nút trong đó.

Và lớp tiếp theo cũng có 32 nút.

Vậy điều chúng ta đang làm ở đây

là chúng ta đang chỉ định một lớp đầu vào gồm một nghìn,

và sau đó nó sẽ xuất 128 sang lớp tiếp theo,

rồi 32, rồi 32.

Và lớp cuối cùng, lớp dày đặc,

sẽ đưa ra khuyến nghị hoặc dự đoán

về việc đánh giá là tích cực hay tiêu cực.

Vì vậy, đối với lớp này, chúng tôi sử dụng hàm kích hoạt sigmoid,

và như chúng ta đã học trước đây,

chức năng kích hoạt sigmoid cung cấp cho chúng tôi

với giá trị từ 0 đến 1.

Được rồi, vậy một khi chúng ta đã xác định được

kiến trúc của mô hình của chúng tôi,

việc tiếp theo chúng ta cần làm là biên dịch mô hình.

Trước khi chúng tôi biên dịch mô hình,

chúng ta phải chỉ định trình tối ưu hóa,

hàm mất mát mà chúng ta mong đợi sử dụng,

và thước đo hiệu suất.

Vì vậy, ở đây chúng tôi chỉ định adam làm trình tối ưu hóa của mình.

Và đối với hàm mất mát,

chúng tôi chỉ định entropy chéo nhị phân.

Vì vậy, đối với các vấn đề phân loại nhị phân,

entropy chéo nhị phân thường là

hàm mất mát mà chúng tôi sử dụng cho việc đó.

Và chúng tôi chỉ định độ chính xác làm thước đo hiệu suất được lựa chọn.

Sau khi chúng ta hoàn tất việc chỉ định các giá trị này,

điều tiếp theo chúng ta cần làm

bây giờ là xây dựng mô hình để huấn luyện mô hình.

Và để làm được điều đó,

chúng tôi sử dụng phương pháp phù hợp với chính mô hình.

Và trong phương pháp phù hợp,

chúng tôi chỉ định dữ liệu đào tạo,

nhãn đào tạo,

và số lượng kỷ nguyên.

Vậy số kỷ nguyên ở đây sẽ là 10,

và chúng tôi chỉ định kích thước lô là 256.

Điều này có nghĩa là mỗi lần mô hình

trong quá trình lan truyền ngược,

trong khi nó đang được huấn luyện,

nó sẽ đọc 256 phiên bản dữ liệu

trước khi nó thực hiện bất kỳ cập nhật nào về trọng số.

Một lần nữa, nếu bạn quan tâm đến chi tiết

về chính xác cách thức hoạt động của lan truyền ngược

và cách cập nhật trọng số,

xem khóa học của nền tảng.

Và chúng tôi cũng chỉ định sự phân chia.

Vậy đây là sự phân chia

giữa tập huấn luyện và tập xác nhận.

Vì vậy, chúng tôi đang nói ở đây rằng 80% dữ liệu của chúng tôi

nên dành riêng cho việc đào tạo,

và 20% nên được sử dụng để xác nhận

trong quá trình đào tạo.

Vì vậy, mô hình sẽ trải qua,

quá trình đào tạo sẽ diễn ra

trải qua 10 thời đại khác nhau,

và chúng ta thấy kết quả của họ ở đây, nhật ký của các kỷ nguyên.

Chẳng có gì phải lo lắng khi nó đến

đến việc phân bổ bộ nhớ vượt quá 10%.

Và khi toàn bộ quá trình đó hoàn tất,

chúng tôi đạt đến điểm mà mô hình của chúng tôi đã được đào tạo hoàn chỉnh,

và bây giờ chúng tôi muốn đánh giá

mô hình hoạt động như thế nào so với dữ liệu thử nghiệm.

Và vì vậy ở đây,

chúng ta chuyển sang mô hình đánh giá chức năng,

chúng tôi chuyển cho nó dữ liệu thử nghiệm và sau đó là nhãn thử nghiệm.

Và sự mong đợi ở đây

là chúng tôi muốn so sánh những dự đoán của mô hình

vào nhãn thực tế của dữ liệu thử nghiệm, phải không?

Vì vậy, nhãn dữ liệu thử nghiệm sẽ là nhãn cho kết quả dương tính

và số 0 cho số âm.

Và khi chúng ta thực hiện quá trình này,

chúng tôi nhận được điểm chính xác là 0,8202, tức là chính xác 82%.

Vì vậy, điều này cho chúng ta biết khá nhiều

dựa trên mô hình mà chúng ta vừa đào tạo,

mà chúng tôi đã không thực sự chi tiêu

bấy nhiêu thời gian để tập hợp lại,

mô hình của chúng tôi có thể dự đoán chính xác nhãn

hoặc cảm tính của 82% đánh giá trong tập dữ liệu thử nghiệm.

Vì vậy, rõ ràng mô hình này mà chúng tôi vừa tạo

là một mạng lưới thần kinh tái phát,

vì vậy nó là một mạng lưới thần kinh tái phát cơ bản.

Sau này trong khóa học này,

chúng ta sẽ tìm hiểu về các kiến trúc tiên tiến hơn khác,

một trong số đó là cái mà chúng tôi gọi là

mạng bộ nhớ ngắn hạn dài, LSTM,

và cái còn lại là mạng đơn vị định kỳ có kiểm soát.

Và vì vậy chúng ta sẽ tìm hiểu cách các mạng này hoạt động

để nâng cao hiệu suất của mô hình của chúng tôi.

Chúng ta cũng có thể điều chỉnh các lớp mà chúng ta đã xác định trước đó.

Vì vậy ở đây khi chúng tôi chỉ định RNN đơn giản,

chúng ta có thể nói Layer.LSTM hoặc Layer.GRU.

Nhưng hiện tại, chúng ta sẽ để nó như vậy

cho đến khi chúng ta thực sự tìm hiểu thêm về những kiến ​​trúc đó.

Và nếu bạn muốn,

bạn có thể quay lại và sửa đổi đoạn mã này

để sử dụng những lớp mới đó.