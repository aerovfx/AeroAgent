# 02 đầu vào ngẫu nhiên

---

Các mô hình ngôn ngữ lớn khó có thể xảy ra,

ít nhất là trong thời gian tới để cung cấp

bạn một cách chính xác và

câu trả lời lặp lại mỗi lần.

Luôn luôn có khả năng

họ làm điều gì đó hơi bất ngờ một chút

và đây là do thiết kế và

có thể là một điều thực sự tốt.

Bây giờ, rất nhiều việc chúng ta sẽ làm

trong kỹ thuật nhanh chóng đang cố gắng giải quyết

với thực tế là các mô hình ngôn ngữ lớn

có một số điều không thể đoán trước đối với họ.

Và chúng tôi muốn hạn chế điều đó

không thể đoán trước được, chúng tôi muốn tạo ra nó và

định hình nó và làm việc với nó trong

một cách có ích cho chúng tôi.

Bây giờ, điều tôi muốn nói ở đây là

luôn có sự ngẫu nhiên,

một số khả năng để tạo ra cái mới và khác biệt

ý tưởng mỗi khi bạn đưa ra lời nhắc.

Và điều này đôi khi có thể thực sự tốt.

Nếu chúng ta đang viết tiểu thuyết và

chúng tôi muốn có nhiều ý tưởng khác nhau,

rất nhiều cốt truyện khác nhau,

rất nhiều nhân vật khác nhau.

Và mỗi lần chúng tôi yêu cầu

dữ liệu mới hoặc yêu cầu một đầu ra mới,

chúng tôi nhận được một cái gì đó hoàn toàn mới và

độc đáo thì nó thực sự tốt.

Mặt khác, nếu chúng ta đang cố gắng có

mô hình ngôn ngữ lớn thực hiện một số loại

lý luận trên một hệ thống, chúng ta có thể không muốn

nó có rất nhiều biến thể và

những gì nó mang lại cho chúng ta.

Ví dụ: nếu chúng ta muốn có hoặc

một câu trả lời không.

Chúng ta không muốn nó nói có, đôi khi,

không, đôi khi, rồi đột nhiên quyết định

chỉ cần nói, à, có lẽ không phải vì đây là

những điều khác mà tôi muốn kể

bạn về lý do tại sao thật khó để xác định và

tiếp tục tràng này cho một đoạn văn hoặc

hai về lý do tại sao nó không thể chính xác

cho chúng tôi câu trả lời chính xác.

Đôi khi chúng ta chỉ muốn có hoặc

không mà không có bất kỳ lời giải thích nào và

chúng ta không phải lúc nào cũng có được điều đó một cách dễ dàng.

Vì vậy, rất nhiều kỹ thuật nhanh chóng

các kỹ thuật sẽ được giải quyết

với điều này.

Bây giờ tôi sẽ chỉ cho bạn thấy

một mẫu nhanh về tính ngẫu nhiên.

Thực tế là cùng một đầu vào

không nhất thiết phải đi đến

cung cấp cho chúng tôi chính xác điều này

cùng một đầu ra mọi lúc.

Và tôi muốn bạn nhớ điều này khi

chúng tôi trải qua khóa học này bởi vì tôi

sẽ cho bạn thấy rất nhiều

các kỹ thuật khác nhau để cố gắng

có được ngôn ngữ lớn

làm mẫu để làm những việc nhất định.

Và đôi khi chúng thực sự có tác dụng

tốt và đôi khi chúng sẽ không hoạt động.

Nhưng những kỹ thuật này thường sẽ

đưa cho bạn là họ sẽ cho bạn thứ gì đó

điều đó đáng tin cậy hơn và hoạt động hiệu quả nhất

của thời gian hoặc rất nhiều thời gian nhưng

không được đảm bảo để

làm việc mọi lúc.

Bây giờ, đây là một điểm quan trọng.

Chúng tôi sẽ luôn có

một số sự ngẫu nhiên ở đây.

Chúng tôi sẽ luôn có một ít

chưa biết và chúng ta phải chấp nhận điều đó và

đối phó với điều đó

Vì vậy, tôi đã hỏi ChatGPT và nói rằng,

có bao nhiêu con chim ở ngoài nhà tôi?

Và nó nói như một mô hình ngôn ngữ AI,

Tôi không có khả năng để

nhận thức thế giới vật chất.

Và anh ấy tiếp tục và sau đó nó nói, nếu

bạn quan tâm đến việc tìm hiểu có bao nhiêu

chim ở bên ngoài nhà bạn,

bạn có thể đi ra ngoài và

tự mình quan sát khu vực đó, bạn cũng có thể

đang cân nhắc việc thiết lập một nơi cho chim ăn.

Được rồi, đó là một điều thú vị.

Hãy xem liệu chúng ta có hỏi lại nó nói gì không.

Vì vậy, bây giờ chúng ta sẽ đi và lấy một

câu trả lời khác và nói rằng, à,

Tôi không thể thấy chuyện gì đang xảy ra

bên ngoài ngôi nhà của bạn.

Tôi không có quyền truy cập vào máy ảnh.

Tôi chỉ xử lý văn bản.

Và sau đó nó nói, bạn có thể đi ra ngoài và

tự mình quan sát khu vực đó hoặc

bạn có thể thiết lập một máy ảnh hoặc

thiết bị giám sát khác để ghi lại.

Lấy số lượng chim, tình trạng sẵn có

về thức ăn, chỗ ở và sự hiện diện.

Và vì vậy, bây giờ,

chúng tôi đã nhận được một cái gì đó khác biệt.

Và thứ chúng ta không còn có nữa là

lời khuyên này để thiết lập một máng ăn cho chim.

Nếu chúng ta chạy lại lần nữa,

có lẽ chúng ta cũng sắp có được

một ví dụ khác

Có lẽ nó sẽ có

một số đặc điểm tương tự.

Nó vẫn tiếp tục và nói, này,

Tôi không có khả năng làm điều đó.

Nó đang chạy một số thứ mà nó

loại văn bản tiêu chuẩn mà nó cho bạn biết.

Nhưng rồi nó lại nói,

này, nếu bạn quan tâm đến việc làm thế nào

bạn có thể thử quan sát khu vực hoặc

để chụp ảnh khu vực này, bạn có thể

sau đó đếm số lượng chim bạn nhìn thấy.

Ngoài ra, bạn có thể xem xét

bố trí máng ăn cho chim hoặc tắm cho chim.

Vì vậy, chúng ta đang nhận được một điều tương tự

xuất ra mỗi lần, nhưng

nó không hoàn toàn giống nhau.

Và vì vậy, đây là một điều kiện khá hạn chế

tập hợp các kết quả đầu ra cho câu hỏi này.

Chúng tôi vẫn đang nhận được một số loại tương tự

mọi thứ mỗi lần, nhưng chúng tôi không nhận được

chính xác điều tương tự và

đó luôn là vấn đề đối với chúng tôi.

Vì vậy hãy biết rằng khi bạn

phát triển các gợi ý,

rất nhiều thứ bạn đang giải quyết là

thực tế là có sự khác biệt.

Bây giờ, nếu tôi muốn nó cung cấp

cho tôi một con số chính xác và

Tôi đã sử dụng lời nhắc như thế này,

điều này rõ ràng là sẽ không hiệu quả.

Chúng ta sẽ không có được con số chính xác

của những con chim bên ngoài nhà tôi với cái này

nhắc nhở.

Bây giờ, chúng ta có thể cần phải

có thể quay lại và

cung cấp thêm thông tin

điều đó có thể giúp nó quyết định.