# 21 -BERT quyết định Alice hoặc Edgar

---

Đây sẽ là một video thú vị và nó sẽ dẫn thẳng đến thử thách lập trình trong phần tiếp theo

video.

Trong video này, chúng ta sẽ xây dựng một bộ phân loại khác bằng mô hình được đào tạo trước BERT

và sau đó trong video tiếp theo, chúng tôi sẽ sử dụng trình phân loại này làm phương pháp thay thế để đánh giá

hiệu suất của một mô hình sáng tạo. Đây là một số văn bản. Tôi đã lấy đoạn văn bản này ra khỏi

hoặc từ cuốn Thơ và Truyện ngắn của Edgar Allan Poe hoặc từ cuốn Alice Through the

Kính Nhìn. Bạn nghĩ gì? Vui lòng tạm dừng video nếu bạn muốn đọc nội dung này và quyết định

bạn nghĩ điều này đến từ cuốn sách nào.

Có thể bạn có ý tưởng, nhưng thậm chí,

bạn không thể vượt qua được

và thực hiện đánh giá này cho hàng nghìn đoạn văn bản.

Vậy điều chúng ta sẽ làm trong video này

đang huấn luyện một mô hình BERT để chọn.

Đó là một phân loại rất đơn giản.

Trên thực tế, nó hoàn toàn giống kiến trúc

như phân loại phân tích tình cảm

mà chúng tôi đã làm trong vài video trước đây.

Sự khác biệt là ở đây chúng ta có văn bản

từ hai cuốn sách khác nhau và mô hình phân loại của chúng tôi

sẽ cần phải học thông qua việc đoán ngẫu nhiên

và sau đó lan truyền ngược lại,

cuốn sách nào trong hai cuốn sách đó được chọn ngẫu nhiên

đoạn văn bản đến từ.

Vì vậy, thiết lập khá gọn gàng.

Vì vậy, đây là những gì chúng ta sẽ làm.

chúng tôi sẽ nhập hai văn bản

mà chúng tôi đã sử dụng trước đó trong phần này.

Và sau đó tôi sẽ tạo một mô hình phân loại

giống hệt như một vài video trước đây.

Sau đó chúng ta sẽ tinh chỉnh mô hình

để phân biệt hai văn bản này.

Bây giờ, tôi quyết định không bao gồm

bộ lập lịch tốc độ học tập tuyến tính hoặc cắt giảm độ dốc,

một phần vì mô hình đã học được

việc phân loại khá tốt.

Và cũng một phần chỉ vì lợi ích

giữ cho mã đơn giản, rõ ràng và tập trung.

Vậy tôi sẽ chỉ cho bạn cách xây dựng

một chức năng làm mịn trung bình.

Hàm làm mịn trung bình là một cách để tính toán lại một vectơ

sử dụng cửa sổ trượt trung bình.

Ở đây bạn có thể xem một bản demo nhỏ

về chức năng của bộ lọc làm mịn trung bình.

Vì vậy, đường màu xanh là dữ liệu gốc.

Đây thực sự là những con số ngẫu nhiên,

nhưng bạn có thể tưởng tượng rằng đây có thể giống như một vectơ mất mát.

Và sau đó với màu cam, tôi đã áp dụng bộ lọc làm mịn.

Ưu điểm của bộ lọc làm mịn

là nó làm nổi bật các xu hướng

trong khi lấy trung bình tiếng ồn.

Bây giờ, tôi sẽ không nói rằng bạn nên luôn sử dụng

một bộ lọc làm mịn trung bình.

Tôi sẽ có nhiều điều để nói về điều đó sau trong đoạn mã.

Dù sao đi nữa, sau khi đào tạo mô hình,

Tôi sẽ chỉ ra sự mất mát và độ chính xác

cho các phiên bản được làm mịn và không được làm mịn

và mọi thứ trong cùng một biểu đồ.

Nếu bạn chưa biết cách tạo đồ thị như thế này

với hai trục Y khác nhau,

thì đây sẽ là một sự bổ sung tuyệt vời

đến kỹ năng Matplotlib của bạn.

Và cuối cùng nhưng không kém phần quan trọng,

chúng tôi sẽ lưu mô hình phân loại sau khi đào tạo.

Và điều đó quan trọng vì chúng tôi thực sự sẽ sử dụng

mô hình đã lưu này trong thử thách mã tiếp theo.

Vì vậy, rất nhiều điều thú vị để làm.

Hãy bắt tay vào làm việc và chuyển sang Python.

Thư viện, GPU, chúng tôi chắc chắn muốn chạy cái này trên GPU

bởi vì chúng tôi sẽ đào tạo LLM.

Được rồi, ở đây tôi đang nhập hai văn bản.

Bạn đã từng thấy mã đó trước đây.

Mã này tạo một trình phân loại, một trình phân loại LLM

về cơ bản nó chạy mô hình BERT.

Và phần còn lại chỉ là công cụ phân loại

mà tôi thêm vào ở cuối.

Nó được khởi tạo thành số ngẫu nhiên.

Và vâng, đường chuyển tiếp chỉ đẩy các mã thông báo

thông qua mô hình BERT,

và sau đó thông qua bộ phân loại ở cuối.

Đó chính xác là kiến ​​trúc mà chúng tôi đã sử dụng trước đây.

Và vâng, đây chỉ là để chúng ta có thể thấy

mô hình trông như thế nào một lần nữa.

Vì vậy, nó cũng đang nhập mô hình.

Được rồi, bây giờ chúng ta đang chuẩn bị tinh chỉnh mô hình.

Tôi sẽ chạy đợt 64

và 256 mã thông báo trong mỗi chuỗi.

và chỉ 150 giai đoạn đào tạo,

chúng tôi thực sự không cần phải đào tạo hoặc tinh chỉnh

với rất nhiều dữ liệu.

Bạn sẽ thấy rằng bộ phân loại học cách phân biệt

Alice trong Edgar nhắn tin khá tốt, khá nhanh.

Điều đó không có nghĩa đây là một mô hình hoàn hảo

rằng nó không thể được cải thiện,

nhưng bạn sẽ thấy nó hoạt động khá tốt

với các thông số mà tôi đã đặt.

Bạn cũng có thể thấy rằng tốc độ học tập

thực sự rất nhỏ.

Tôi không muốn ghi đè lên mô hình này quá nhiều.

Tôi muốn mô hình này được giữ lại

hầu hết các giá trị tham số ban đầu của nó.

Tôi chỉ muốn chỉnh sửa chúng một chút

để bộ phân loại ở cuối

có thể tách tuyến tính văn bản Edgar khỏi văn bản Alice.

Được rồi, hãy chạy mã đó.

Và ở đây, đây chỉ là minh họa quy trình

cho một bước đào tạo.

Vì vậy, ở đây tôi đang nhận được một loạt dữ liệu

từ cuốn sách Alice và từ cuốn sách Edgar.

Đây là mã bạn đã thấy trước đây.

Tôi chỉ đang tạo ra một loạt các số nguyên ngẫu nhiên

và đặt chúng lại với nhau trong một ma trận.

Mã này có gì khác biệt

so với những gì bạn đã thấy trước đây

là trước đây nó chỉ là một văn bản

mà chúng tôi đã rút ra một đợt ngẫu nhiên từ đó.

Và đây là hai văn bản và tôi đang ghép chúng lại

để có được ma trận chứa 32, tôi nghĩ là 32, vâng, 64.

Được rồi, 32 hàng đầu tiên là chuỗi mã thông báo

từ cuốn sách Alice.

Và 32 hàng tiếp theo là chuỗi mã thông báo

từ cuốn sách của Edgar.

Vì vậy, những cái đó được nối.

Và hãy xem, sau đó chúng ta cần một số nhãn.

Vì vậy tôi dán nhãn chúng là số không và số một.

Và về cơ bản là mô hình, bộ phân loại BERT,

sẽ cần phải phân biệt giữa loại 0

và loại một.

Ở đây tôi thực hiện một đường chuyền về phía trước.

Tôi nhận được argmax của logit.

Vì vậy, về cơ bản đây là bất kỳ bản ghi nào trong hai bản ghi cuối cùng,

các nút đầu ra sẽ cao hơn.

Đó là dự đoán của mô hình cho hạng mục

của đoạn dữ liệu cụ thể đó.

Và sau đó tính toán sự mất mát.

Và vâng, ở đây chúng ta thấy độ chính xác

thực ra là 72%,

nhưng con số đó có vẻ khá cao,

nhưng đây là một mô hình ngẫu nhiên.

Vì vậy, chúng ta sẽ nhận được những con số khác nhau

mỗi lần chúng tôi chạy mã này.

Chúng tôi không thực sự mong đợi điều này đáng tin cậy,

luôn ở mức trên 50%,

mặc dù điều kỳ lạ là nó có trong tất cả các mô hình này,

nhưng đó thực sự chỉ là do lấy mẫu ngẫu nhiên.

Ở đây chúng tôi nhận được một con số gần hơn với 50%.

Bây giờ để đào tạo mô hình.

Bây giờ điều này cũng vậy, không có mã nào ở đây

mà bạn thực sự chưa bao giờ thấy trước đây.

Rõ ràng là độ chính xác rất cao

chỉ sau 150 đợt huấn luyện

với tốc độ học tập thực sự nhỏ.

Vì vậy trên thực tế, việc phân loại này không thực sự khó khăn

vấn đề để mô hình giải quyết.

Tôi sẽ cho bạn thấy âm mưu của sự mất mát và độ chính xác

trông như trong giây lát.

Đầu tiên tôi muốn giới thiệu với các bạn bộ lọc làm mịn trung bình này

chức năng.

Vì vậy, đây là một hàm có hai đầu vào, vectơ

của những con số mà chúng ta muốn làm trơn,

và một tham số tùy chọn k mà tôi đặt thành 3 theo mặc định.

Vì vậy, đây là ý tưởng.

Ý tưởng là chúng tôi tạo một bản sao của dữ liệu.

Vì vậy tôi thêm số 0 vào đây để y khác biệt.

Đó là một bản sao duy nhất của dữ liệu x.

Và sau đó tôi đặt w, về cơ bản nó chỉ bằng một nửa k.

Vậy khi k bằng ba thì w bằng ba trừ một,

đó là hai, rồi chia cho hai là một.

Sau đó chúng ta lặp qua tất cả các giá trị trong y,

hoặc trong X, xin lỗi, thực tế là tương đương.

Và sau đó chúng ta nói rằng X trừ, trong trường hợp này,

trong ví dụ này, W là một.

Vậy vị trí hiện tại trừ đi một

đến vị trí hiện tại cộng thêm một,

điều đó cho chúng ta tổng cộng ba con số.

Vì vậy, giá trị trước đó, giá trị hiện tại,

và giá trị tiếp theo.

Và sau đó chúng tôi tính trung bình chúng lại với nhau,

và điều đó cho chúng ta giá trị của Y.

Và nó thật đơn giản.

đó là một bộ lọc làm mịn trung bình.

Và phần còn lại của mã này chỉ hiển thị bản demo

mà tôi đã trình chiếu trong ảnh chụp màn hình mà tôi đã trình chiếu trong các trang trình bày.

Được rồi, tôi đang tạo ra cốt truyện đây

và những gì tôi làm ở đây là thiết lập một X đôi.

Vì vậy, đây là cách bạn thiết lập trục thứ hai

đó là trên đỉnh của trục đầu tiên.

Vì vậy, tôi có các ô phụ và sau đó chỉ có một ô phụ

và đó là cái này

Đây là một ô phụ, một trục.

Sau đó, ở đây tôi tạo một trục mới và sử dụng ax.twin,

thì Matplotlib sẽ thực sự vẽ trục này

theo nghĩa đen là ở trên cùng của trục này bằng cách sử dụng cùng dấu x

và vân vân.

Được rồi, đó là cách chúng ta có được cốt truyện này ở đây.

Những đường mảnh là dữ liệu thô,

các đường dày là dữ liệu mịn trung bình,

Và sau đó các giá trị màu xanh ở đây thể hiện sự mất mát,

họ đang đi xuống.

Các giá trị màu cam ở đây tương ứng với trục Y bên phải

và đó là độ chính xác, nó đang tăng lên.

Bây giờ tôi có thể nói đây là hiệu suất rất tốt.

Có lẽ có thể cải thiện độ chính xác hơn nữa.

Nếu bạn tập luyện nhiều hơn một chút,

có thể điều chỉnh một số thông số huấn luyện,

nhưng tôi có thể nói điều này là khá tốt.

Nhân tiện, bạn nghĩ gì về bộ lọc làm mịn ý nghĩa này?

Bạn nghĩ rằng điều này giúp ích hay gây tổn hại

với cách giải nghĩa?

Đó là một câu hỏi mở.

Chúng thường xuyên xảy ra, trừ khi bạn đạt được cài đặt thông số cực cao,

ví dụ như nếu tôi thay đổi điều này thành,

độ chính xác làm mịn có nghĩa là ở đâu?

Giả sử tôi đặt nó thành 15.

Vì vậy, bây giờ chúng ta đang bắt đầu làm mịn rất nhiều.

Theo ý kiến ​​​​của tôi, đó là một chút quá trơn tru.

có lẽ không sao, nó vẫn chắc chắn làm nổi bật các xu hướng,

nhưng đến một lúc nào đó bạn bắt đầu làm mịn

và lọc dữ liệu rất nhiều

rằng nó trở nên hơi sai lệch một chút, phải không?

Nếu bạn nhìn vào những đường nét mượt mà này,

nó mang đến cho bạn một kiểu diễn giải sai lệch

về việc quá trình đào tạo thực sự suôn sẻ như thế nào.

Nhân tiện, ở đây bạn có thể thấy các hiệu ứng cạnh.

Bạn luôn gặp những điều kỳ lạ xảy ra

ở rìa của chuỗi thời gian khi bạn áp dụng bộ lọc.

Còn nhiều cách phức tạp hơn

để loại bỏ những hiệu ứng biên này,

nhưng đó là chủ đề của khóa học về xử lý tín hiệu.

Tôi sẽ không thảo luận về điều đó ở đây.

Điểm tôi muốn đề cập là bạn càng mịn màng,

bạn càng có nguy cơ gây ấn tượng sai lệch

về những gì đang thực sự xảy ra với mô hình

và với việc đào tạo.

Mặt khác, một chút làm mịn

thực sự tạo điều kiện cho việc giải thích trực quan

và sự hiểu biết, đó là một điều tốt.

Vì vậy, đôi khi đó là một đường khó vẽ.

Trong trường hợp này, tôi thích ý tưởng hiển thị

cả hai phiên bản được làm mịn nhẹ

và cả chuỗi thời gian thô nữa.

Được rồi, điều cuối cùng chúng ta muốn làm là lưu mô hình này.

Và đó là vì trong video tiếp theo,

đó là một thử thách về mã,

chúng ta sẽ sử dụng mô hình tinh chỉnh này

để phân biệt văn bản được tạo ra

bởi một mô hình được đào tạo bởi Alice và một mô hình được đào tạo bởi Edgar.

Vì vậy chúng ta cần sử dụng lại mô hình này trong một file riêng

trong một phiên Python riêng biệt.

Vì vậy tôi lưu mô hình này

và tôi sẽ gọi nó là BertClassifier Alice đấu với Edgar.

Được rồi, khi bạn chạy mã này,

bạn muốn mở cấu trúc tập tin này ở đây

rồi bấm vào dấu ba chấm ở đây

và tải xuống tập tin này.

Tôi đã tải xuống tập tin này,

nên tôi sẽ không tải nó xuống nữa.

Nó không phải là một tập tin lớn.

Nó lớn cỡ nào?

Nó nặng hơn 400 megabyte một chút.

Vì vậy hãy tải cái này về máy tính của bạn.

Đừng xóa nó vì chúng ta sẽ sử dụng nó

trong video tiếp theo.

Tôi đã đề cập trước đó rằng các mô hình tổng quát

thực sự rất khó để đánh giá

bởi vì đánh giá định lượng

không nhất thiết phải sâu sắc đến thế

và đánh giá chất lượng khác nhau tùy theo từng người,

mang tính chủ quan và có thể mang tính cụ thể cao về nhiệm vụ.

Vì vậy sẽ thật tuyệt nếu chúng ta có thể sử dụng một mô hình

như một cách để định lượng hiệu suất

của một mô hình sinh sản khác.

Và đó chính là bước khởi đầu cho thử thách viết mã

của video tiếp theo.