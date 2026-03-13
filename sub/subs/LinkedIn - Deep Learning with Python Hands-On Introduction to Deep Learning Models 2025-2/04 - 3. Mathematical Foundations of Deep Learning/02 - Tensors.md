# 02 - Tenxơ

---

- [Người hướng dẫn] Mô hình deep learning lưu trữ dữ liệu

trong các cấu trúc dữ liệu được gọi là tensor.

Tensors rất cơ bản cho lĩnh vực học sâu

rằng nền tảng học sâu mà chúng tôi sử dụng trong khóa học này,

TensorFlow, được đặt theo tên của họ.

Vậy tensor là gì?

Tại cốt lõi của nó,

tensor là nơi chứa dữ liệu,

thường là dữ liệu số.

Về cơ bản, nó là một nơi chứa dữ liệu đa chiều,

giống như vectơ và ma trận.

Chúng ta có thể lấy phần chấm của tensor,

chúng ta có thể nhân chúng lên,

và chúng có thể phải chịu các hoạt động theo từng phần tử.

Các framework học sâu như TensorFlow

được thiết kế đặc biệt

để xử lý các hoạt động tensor này một cách hiệu quả.

Một tensor được xác định bởi ba thuộc tính chính.

Đầu tiên là số trục hoặc cấp của tensor.

Trong video trước,

chúng tôi giới thiệu các đại số vô hướng, vectơ và ma trận.

Vô hướng hoặc số đơn

chúng tôi gọi là tensor hạng 0,

vectơ là tensor cấp 1,

và ma trận là tensor hạng 2.

Thuộc tính thứ hai của tensor là hình dạng của nó.

Điều này thường được biểu diễn dưới dạng lật đổ các số nguyên

mô tả một tensor có bao nhiêu chiều

dọc theo mỗi trục.

Giá trị vô hướng chẳng hạn như năm có hình dạng trống.

Một vectơ có ba phần tử

có hình ba, dấu phẩy, không có gì.

Và một tensor ma trận hoặc hạng 2

với hai hàng và ba cột

có hình dạng hai và ba.

Thuộc tính thứ ba của tensor là kiểu dữ liệu của nó.

Đây là loại dữ liệu chứa trong tensor.

Điều này có thể dao động từ các giá trị số nguyên unicode 8 bit

đến số dấu phẩy động 32-bit hoặc khối văn bản,

được gọi là chuỗi.

Như chúng ta đã biết hiện nay,

tensor về cơ bản là một sự khái quát hóa

của vô hướng, vectơ và ma trận

đến một số chiều tùy ý.

Như vậy, chúng ta có thể sử dụng tensor

để thể hiện bất kỳ dữ liệu số nào mà chúng tôi xử lý trong học sâu.

Trong khi tensor có thể biểu diễn dữ liệu

đến vô số chiều,

hầu hết các vấn đề chúng ta gặp phải trong thực tế

thường sẽ yêu cầu thao tác tensor

có thứ hạng từ 0 đến tối đa là 5.

Chúng ta hãy xem một số ví dụ.

Tập dữ liệu tài liệu văn bản

nơi chúng tôi đại diện cho từng tài liệu

bằng cách đếm xem mỗi từ bao nhiêu lần

trong từ điển các từ thông dụng xuất hiện trong tài liệu

có thể được biểu diễn dưới dạng tensor hạng 2.

Giả sử chúng ta có 500 tài liệu trong kho văn bản

và 20.000 từ duy nhất trong từ điển,

toàn bộ tập dữ liệu có thể được lưu trữ

trong một tenxơ hạng 2 có hình dạng

500 x 20.000.

Kích thước đầu tiên đại diện cho các mẫu hoặc tài liệu,

trong khi chiều thứ hai thể hiện các tính năng,

đó là những từ duy nhất trong từ điển.

Tensor hạng 2 là một trong những tenxơ được sử dụng phổ biến nhất

trong học sâu.

Bất cứ khi nào thời gian quan trọng trong dữ liệu của chúng tôi

hoặc tồn tại khái niệm về thứ tự,

thật hợp lý khi lưu trữ dữ liệu dưới dạng tenxơ cấp 3

với một trục thời gian rõ ràng.

Ví dụ: hãy xem xét một tập dữ liệu từ năm cảm biến

đo ba biến,

nhiệt độ, độ ẩm và áp suất khí quyển

ở 10 bước thời gian khác nhau.

Những dữ liệu này có thể được biểu diễn bằng tensor cấp 3

với hình dạng 5 x 3 x 10.

Kích thước đầu tiên đại diện cho các mẫu hoặc cảm biến.

Chiều thứ hai thể hiện các đặc điểm,

nhiệt độ, độ ẩm và áp suất.

Cuối cùng, chiều thứ ba thể hiện các bước thời gian

trong đó có 10.

Trong bối cảnh nhiệm vụ thị giác máy tính

chẳng hạn như phân loại hình ảnh,

phát hiện đối tượng hoặc phân đoạn hình ảnh,

tensor hạng 4 thường được sử dụng để biểu diễn dữ liệu hình ảnh.

Hãy xem xét một tập hợp gồm 32 hình ảnh màu,

mỗi cái có độ phân giải 128 x 128 pixel.

Hàng loạt hình ảnh có thể được biểu diễn

với một tensor bậc 4 có hình dạng

32 x 128 x 128 x 3.

Kích thước đầu tiên là một số hình ảnh trong lô,

còn được gọi là kích thước lô.

Chiều thứ hai và thứ ba

đại diện cho chiều cao và chiều rộng,

tương ứng của hình ảnh tính bằng pixel.

Chiều thứ tư đề cập đến số lượng kênh màu

cho hình ảnh.

Hình ảnh màu RGB có ba kênh,

đỏ, xanh lá cây và xanh dương.

Trong khi hình ảnh thang màu xám chỉ có một kênh

để biểu thị cường độ.

Chúng ta có thể coi dữ liệu video như một chuỗi các khung hình,

với mỗi khung hình là một hình ảnh màu.

Điều này có nghĩa là chúng ta có thể biểu diễn dữ liệu video

theo cách tương tự như dữ liệu hình ảnh,

à, với một chiều bổ sung, thời gian.

Hãy xem xét một lô

trong số năm video YouTube độ phân giải cao dài 10 giây

được lấy mẫu ở tốc độ 60 khung hình mỗi giây.

Dữ liệu này có thể được biểu diễn bằng tensor cấp 5

với hình dạng 5 x 600

vào năm 1920 vào năm 1080 vào 3.

Kích thước đầu tiên thể hiện cỡ lô hoặc mẫu.

Chiều thứ hai là một số khung

trong mỗi video clip.

60 khung hình mỗi giây nhân 10 giây,

đây là chiều thời gian.

Các chiều thứ ba, thứ tư và thứ năm

đại diện cho chiều cao, chiều rộng của mỗi khung hình,

và số lượng kênh.

Video Full HD có độ phân giải 1920 x 1080 pixel.

Như được minh họa bằng những ví dụ này,

chúng ta có thể sử dụng tensor xếp hạng

0, 1, 2, 3, 4 hoặc 5

để đại diện cho hầu hết mọi loại dữ liệu phổ biến

mà chúng ta gặp phải trong học sâu.