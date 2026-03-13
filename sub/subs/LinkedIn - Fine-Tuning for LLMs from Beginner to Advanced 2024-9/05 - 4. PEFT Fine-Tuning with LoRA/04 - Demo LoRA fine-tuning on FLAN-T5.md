# 04 - Demo tinh chỉnh LoRA trên FLAN-T5

---

- [Người hướng dẫn] Trong phần demo này chúng ta đến phần xuất sắc

của Tinh chỉnh LoRA.

Vì vậy, cuối cùng chúng tôi sẽ triển khai LoRA,

một trong những tiên tiến nhất

và các kỹ thuật thú vị trong PEFT,

tinh chỉnh tham số hiệu quả.

Vào thời điểm ghi hình này vào năm 2024,

LoRA chưa đầy hai tuổi.

Điều này có nghĩa là bạn sẽ học được điều gì đó

đó không chỉ là một công nghệ hiện đại,

nhưng bạn cũng sẽ thấy

việc thực hiện nó sẽ hơi phức tạp một chút

bởi vì không tồn tại gói

và hỗ trợ cho LoRA, cho Ôm Mặt,

TensorFlow hoặc PyTorch nguyên bản

thích làm điều gì đó như LoRA.apply.

Chúng tôi chưa có điều đó.

Đó là trạng thái hiện đại của chúng tôi hiện nay.

Vì vậy tôi hy vọng bạn cũng hào hứng như tôi.

Hãy để tôi kết nối với GPU và chúng tôi ở đó.

Và như mọi khi, trước tiên chúng ta cần thực hiện cài đặt pip.

Vì vậy, để thực hiện LoRA một cách hiệu quả, gói duy nhất chúng ta cần

để bổ sung, một tính năng mới đối với chúng tôi, đó là tensorflow_add-ons,

mà chúng tôi sẽ sử dụng để thêm bộ điều hợp thấp hơn.

Chúng ta sẽ xem chúng ta sẽ sử dụng nó như thế nào sau này. Nó đây rồi.

Chúng ta có thể thấy rằng nó được cài đặt hoàn hảo.

Bây giờ chúng ta sẽ tải tập dữ liệu.

Bạn biết đây là tập dữ liệu dịch WMT16

từ tiếng Đức sang tiếng Anh.

Chúng ta sẽ in cái đầu tiên,

nhưng bạn đã biết nó trông như thế nào rồi.

Chúng tôi đã chơi với nó rồi

và nó kết thúc và một lần nữa,

bạn có thể thấy chúng tôi có bản dịch, tiếng Đức

và phần tiếng Anh.

Vì vậy, bây giờ đến việc xử lý văn bản.

Bạn đã biết điều này rồi, nhưng trong trường hợp tôi sẽ đề cập đến nó,

chúng tôi tải bằng mã thông báo tự động của mô hình của chúng tôi.

Đầu vào nhớ phần dịch nhé

cho phần tiếng Anh,

chúng ta cần thêm vào lời nhắc dịch tiếng Anh sang tiếng Đức

để giúp FLAN_T5.

Mục tiêu sẽ là bản dịch tiếng Đức.

Sau đó, chúng tôi sẽ sử dụng mã thông báo như mọi khi,

và hãy nhớ một điều rất quan trọng, chúng ta cần

để đặt các tenxơ trả về dưới dạng TF

để trả về các tensor TensorFlow thực tế.

Sau đó chúng ta có được nhãn giống như trước

và chúng tôi nhận được đầu vào bộ giải mã như thế này.

Vụ này chỉ để chạy thôi

trong một khoảng thời gian không lớn,

Tôi đã thực hiện câu lệnh chọn này để nhận được 20.000 hàng

cho tập huấn luyện

và 1000 hàng cho tập kiểm tra đánh giá.

Được rồi, sau đó chúng ta làm những việc tương tự như trước đây.

Một điều nữa trước khi thực hiện

đó có phải là kích thước lô không, tôi đặt nó thành 128.

Một lần nữa vì lý do thời gian

bởi vì GPU của tôi cho phép điều đó.

Trong trường hợp bạn chỉ có CPU

hoặc bạn có GPU kém mạnh hơn, như T-4,

bạn có thể giảm con số này xuống còn 8 hoặc 16 và do đó nó

sẽ sử dụng ít RAM hơn và sau đó nó không bị sập.

Đó là điều quan trọng, hãy nhớ,

nhưng quy mô lô cao hơn nghĩa là đào tạo nhanh hơn,

nhưng cũng có nhiều RAM GPU hơn.

Vì vậy, bạn cần phải thực hiện một giao dịch ở đó.

Với tất cả những điều đó, hãy chạy cái này.

Chúng ta đây rồi. Hoàn hảo.

Vì vậy bây giờ hãy tải mô hình của chúng tôi.

Chúng tôi sẽ tải mô hình cơ sở FLAN-T5 của chúng tôi

và chúng tôi ở đó.

Hoàn hảo. Vậy chúng ta triển khai LoRA như thế nào?

Chúng ta cần tạo một lớp Keras

và sau đó ý tưởng sẽ là thay thế một loại cụ thể

của lớp trong mô hình của chúng tôi với lớp này.

Để làm cho cách tiếp cận đầu tiên này trở nên dễ dàng, bạn sẽ

chỉ cần thay thế những lớp dày đặc thôi, được chứ?

Vì vậy, mỗi khi bạn nhìn thấy một lớp dày đặc trong mô hình,

bạn sẽ thay thế nó bằng lớp LoRA.

Vì vậy, trong init, chúng ta cần thứ hạng.

Hãy nhớ rằng điều đó sẽ quyết định số tiền

các tham số của LoRA.

Điều đó cũng sẽ xác định kích thước của ma trận

và lớp thực tế mà tôi gọi ở đây là dày đặc.

Điều này có nghĩa là lớp dày đặc thực sự xuất hiện.

Tại sao tôi cần nó, bởi vì tôi cần đầu ra của nó

để thực hiện kết quả cộng A nhân B, hãy nhớ,

và tôi cũng cần nó để đặt nó là không thể đào tạo được.

Về việc xây dựng lớp,

phương thức xây dựng là cái đang được gọi

khi chúng tôi khởi tạo lớp đó

và nó được thêm vào mô hình

về việc biên soạn đồ thị tính toán.

Chúng ta sẽ tạo hai ma trận A và B,

giống như chúng tôi đã làm trong các slide

nơi chúng tôi sử dụng phương pháp thêm trọng lượng từ Keras.

Hình dáng quan trọng, chữ A đứng đầu.

Nó là A nhân B, vậy từ phép nhân ma trận,

chiều thứ hai của ma trận thứ nhất cần bằng nhau

chiều thứ nhất của ma trận thứ hai.

Đó là lý do tại sao nó nói tự xếp hạng ở cả hai nơi

như chúng tôi muốn thứ nguyên cuối cùng

chính xác bằng lớp ban đầu.

Chiều thứ nhất của ma trận thứ nhất

và chiều cuối cùng của ma trận thứ hai cần

để phù hợp với một trong những lớp dày đặc.

Chúng ta sẽ khởi tạo chúng dưới dạng ma trận chuẩn ngẫu nhiên,

nhưng hãy nhớ rằng chúng ta sẽ huấn luyện họ.

Cuối cùng, khi chúng ta gọi lớp này, chúng ta sẽ

đầu tiên gọi các lớp dày đặc

của đầu ra ban đầu bình thường mà chúng tôi sẽ nhận được.

Sau đó chúng ta thực hiện A nhân B thực tế

và áp dụng nó vào đầu vào, việc mà chúng tôi làm

bằng phép nhân ma trận 2 lần.

Đó sẽ là đầu ra LoRA.

Chúng tôi đặt lớp dày đặc là không thể đào tạo được,

và cuối cùng chúng tôi trả lại phép cộng của 2.

Đây là việc triển khai lớp LoRA. Được rồi?

Hãy nhớ điều này.

Bây giờ nếu chúng ta thấy mô hình của mình,

vấn đề với người mẫu Ôm Mặt

là chúng thường được đóng gói.

Ý tôi muốn nói ở đây là, ví dụ,

nếu bạn thấy bộ mã hóa

hoặc bộ giải mã, chúng là một lớp cụ thể.

Vậy điều đó có nghĩa là những người phát triển mô hình đó

đã tạo một lớp đặc biệt cho thành phần cụ thể đó

chặn bộ mã hóa hoặc bộ giải mã.

Điều đó có nghĩa là nếu tôi muốn thực hiện LoRA trên bộ mã hóa,

ví dụ: tôi cần tìm hiểu sâu hơn về nội bộ

về cấu trúc của loại lớp đó,

đó là lớp chính của TFT5,

và đó là những gì chúng ta sẽ làm.

Tôi sẽ chỉ cho bạn chính xác cách thực hiện trên một khối

để bạn biết chính xác phải làm gì.

Được rồi, bắt đầu thôi.

Để làm điều đó, đây là đoạn mã chúng ta cần chạy,

nhưng tôi nghĩ tốt nhất chúng ta chỉ cần thêm vào đây một ô mã

và tôi chỉ cho bạn cách chúng ta có thể chơi đùa

với người mẫu trong Ôm Mặt.

Nhân tiện, trò chơi này cực kỳ tiên tiến, vì vậy hãy chơi nó

bao nhiêu lần tùy theo nhu cầu của bạn.

Bất kỳ mô hình nào chúng tôi có thể nhận được,

tất nhiên là các lớp, thông thường đây là quá trình tự động hoàn thành,

xin lỗi, nhưng chúng tôi cũng có thể làm những kiểu này

của những người mẫu trong Ôm Mặt, nhận

theo tên lớp như một thuộc tính.

Vì vậy, ví dụ, tôi có thể lấy model.decoding

và model.decode, như bạn có thể thấy,

nói lớp chính TFT5.

Quả thực là vậy. Chúng ta có thể thấy nó ở đây, hoàn hảo.

Bây giờ có một phương pháp nội bộ được gọi là làm phẳng các lớp.

Nó đây rồi, và những lớp phẳng này

sẽ tạo ra một máy phát điện.

Trình tạo là thứ mà khi bạn lặp lại nó,

nó sẽ cho bạn thấy các yếu tố của nó

và đó sẽ là tất cả các lớp của mô hình được làm phẳng.

Hãy nhớ rằng trong T5 đó là một chuỗi

mô hình tuần tự và bộ giải mã, một số

của các khối có thể thực sự song song.

Vì vậy, sự làm phẳng này sẽ dễ dàng đặt cái này với cái kia.

Cách tốt nhất, theo ý kiến ​​của tôi để thấy điều này chỉ là thực hiện lớp

cho lớp trong model.decoding._flatten._layers.

Vì vậy, nếu chúng ta chạy cái này, bây giờ, chúng ta có thể thấy tất cả các lớp

của mô hình này.

Thủ thuật dễ thương phải không?

Vậy ở đây chúng ta thấy nó có phần nhúng, sau đó có khối

vân vân và bây giờ, chúa ơi, nó đây rồi.

Bây giờ chúng ta có thể thấy các lớp dày đặc.

Ví dụ: nếu chúng ta muốn trở nên dễ thương

và chúng tôi cũng muốn sửa đổi cơ chế căng thẳng,

chúng ta có thể làm điều đó bằng cách làm phẳng các lớp

cũng ở khối này.

Thế là nó làm tổ và làm tổ. Chúng ta có thể đi bao nhiêu tùy thích.

Trong trường hợp này, chúng ta sẽ chỉ lên cấp độ đầu tiên,

nhưng bạn có thể làm bao nhiêu tùy thích, hãy nhớ,

và chúng ta sẽ thay thế những lớp này, những lớp dày đặc.

Hoàn hảo. Được rồi, tôi hy vọng nó có ý nghĩa.

Vậy hãy để tôi đi xuống.

Tất nhiên, bạn có thể thấy mô hình này có rất nhiều lớp.

Mỗi lớp này có rất nhiều tham số, v.v.

Vậy điều chúng ta sắp làm là vì,

và một lần nữa, hãy nhớ rằng các lớp phẳng sẽ trả về cho tôi một trình tạo.

Vì vậy tôi sẽ sử dụng enumerate để lấy từ trình tạo đó,

cái, hãy gọi nó là số của lớp đó, chỉ mục

và lớp thực tế.

Và sau đó tôi sẽ hỏi liệu lớp đó có phải là một phiên bản của,

và điều tốt nhất cần làm là sao chép chính xác điều này

khi nó đến và dán nó.

Hãy tin tôi, đó là điều tốt nhất bạn có thể làm

bởi vì nếu bạn muốn trở nên sang trọng

và nói ở đây, như từ tf_keras

nhập dày đặc thì sẽ không bắt được.

Tin tôi đi, tôi đã đến đó rất nhiều lần rồi.

Vì vậy, bạn chỉ cần sao chép và dán và bây giờ nó sẽ hoạt động.

Nó sẽ phát hiện trường hợp đó.

Chúng tôi sẽ đặt nó là không thể huấn luyện được,

và sau đó chúng ta sẽ lấy lớp đó

và thay thế nó bằng một lớp thấp hơn,

cái mà chúng tôi đã tạo ở trên.

Cuối cùng, nếu chúng ta không có loại lớp đó,

về cơ bản là tất cả những cái khác, chúng ta sẽ

để đặt chúng là không thể đào tạo được.

Điều này áp dụng hiệu quả LoRA cho bộ giải mã.

Như chúng ta đã biết cách thực hiện điều đó trong một khối,

chúng ta sẽ tránh làm điều đó trên bộ mã hóa

và trên phần chia sẻ, nhưng nó sẽ giống nhau.

Vì vậy, chúng tôi sẽ đặt hai lớp đó là không thể đào tạo được.

Cuối cùng, trên lớp dày đặc cuối cùng, đó là đầu LM,

chúng tôi cũng sẽ thay thế nó bằng một lớp thấp hơn.

Vì vậy, sau khi làm tất cả những điều này,

nếu chúng ta thấy bản tóm tắt mô hình một cách kỳ diệu thì bây giờ

để ý rằng trong số 247 triệu tham số,

222 triệu tham số không thể huấn luyện được.

Điều đó không tuyệt vời sao?

Bây giờ chúng ta đã áp dụng LoRA, chúng ta sẽ bắt đầu

để biên dịch mô hình của chúng tôi

và chúng tôi sẽ điều chỉnh nó cho các kỷ nguyên miễn phí.

Có lẽ sẽ mất từ 7 đến 10 phút trong GPU của tôi,

bởi vì vẫn nhớ, vì tôi chưa đi đủ sâu

với LoRA, tôi đang huấn luyện 24 triệu thông số.

Vâng, đó là 9% tổng số mô hình,

nhưng nó vẫn còn rất nhiều thông số.

Vì vậy sẽ mất một ít thời gian,

nhưng đừng lo lắng, trong trường hợp của bạn, nếu bạn muốn đi sâu hơn

và sâu hơn, bạn có thể làm

với cùng một phương pháp sử dụng các lớp phẳng,

và bạn chỉ cần thay thế bao nhiêu lớp tùy thích bằng LoRA,

và nó chỉ hoạt động.

Thật tuyệt vời.

Vì vậy, bây giờ nó đang chuyển sang GPU và sẽ đào tạo

và quá trình đào tạo đã kết thúc.

Như bạn có thể thấy, GPU này mất 7 phút,

điều đó thực sự rất, rất tốt.

Bây giờ chúng ta có thể làm bất cứ điều gì chúng ta muốn với mô hình này.

Trong trường hợp của chúng tôi, tôi muốn cho bạn xem mô hình đánh giá,

chạy qua tập dữ liệu thử nghiệm,

và nó sẽ mang lại cho chúng ta sự mất mát

và số liệu mà chúng tôi đã nêu.

Trong trường hợp của chúng tôi, nó sẽ khiến chúng tôi thua lỗ,

là 2,6, rất thấp, và

do đó đây là một mô hình rất tốt.

Như vậy chúng ta có thể thấy buổi tập huấn đã thành công,

không những thành công mà

nhưng chúng tôi chỉ đào tạo 9% thông số.

Tôi muốn nhấn mạnh rằng, điều này rất quan trọng,

đặc biệt nếu bạn muốn huấn luyện một tập dữ liệu khổng lồ

hoặc nếu bạn muốn đào tạo cho một số lượng lớn kỷ nguyên

bởi vì thời gian mỗi kỷ nguyên, nếu bạn kiểm tra,

là ít hơn đáng kể.

Và quan trọng hơn,

nếu chúng ta đến đây, hãy để ý dung lượng RAM GPU được sử dụng.

Tôi đã không đề cập đến nó trước đây, nhưng

trước đó nó có dung lượng khoảng 30 gigabyte.

Bây giờ chỉ mới 8 giờ.

Điều đó có nghĩa là bạn có thể rèn luyện điều này

trên phiên bản Amazon rẻ nhất có GPU

đó là GeForce tại thời điểm ghi.

Đây là một con số khổng lồ đối với bất kỳ công ty nào.

Tất nhiên, tôi có thể lấy mô hình này và chạy rouge

và điểm xanh trên bản dịch,

nhưng bạn đã biết cách làm điều đó.

Điểm nhấn của bản demo này là cách triển khai LoRA.