# 16 phòng thí nghiệm-1-hướng dẫn

---

Đây là Phòng thí nghiệm 1, và như tôi đã nói,

chúng ta sẽ lấy

một tập dữ liệu trong số này

cuộc trò chuyện

điều đó đang xảy ra

giữa mọi người.

Những gì chúng tôi dự định làm

là tóm tắt

những cuộc đối thoại này và như vậy

nghĩ về một cuộc đối thoại hỗ trợ

giữa bạn và bạn

khách hàng có thể

cuối tháng

bạn muốn tóm tắt

tất cả những vấn đề mà

nhóm hỗ trợ khách hàng của bạn

đã giải quyết trong tháng đó.

Một số điều khác cần lưu ý bây giờ,

Tôi đang phóng to một

ở đây một chút,

nhưng bạn có thể thấy điều đó

chúng tôi có tám CPU,

chúng tôi có 32 hợp đồng RAM.

Chúng tôi đang sử dụng Python ba

và đây là một số

của cài đặt pip.

Vì vậy, nếu tôi thực hiện Shift Enter ở đây,

việc này sẽ bắt đầu thực hiện

thư viện Python cài đặt

và chúng tôi thấy rằng chúng tôi

sẽ sử dụng PyTorch.

Chúng tôi đang cài đặt một

thư viện có tên là dữ liệu Torch,

giúp với

tải dữ liệu và

một số khía cạnh khác cho PyTorch

cụ thể cho các tập dữ liệu.

Ở đây chúng ta thấy Transformers.

Đây là một thư viện

từ Ôm mặt,

một công ty thực sự tuyệt vời

ai đã xây dựng

rất nhiều nguồn mở

dụng cụ lớn

các mô hình ngôn ngữ

Họ cũng đã xây dựng

thư viện này,

thư viện Python này

được gọi là tập dữ liệu,

có thể tải ở nhiều

công chúng

tập dữ liệu mà mọi người

sử dụng để huấn luyện các mô hình,

tinh chỉnh các mô hình, hoặc

chỉ cần thử nghiệm với.

Nếu bạn bấm Shift Enter ở đó,

cái này sẽ chạy một chút.

Bây giờ hãy nhớ rằng điều này không

mất vài phút để tải.

Toàn bộ cuốn sổ này sẽ

phụ thuộc vào các thư viện này.

Vì vậy hãy chắc chắn rằng

những cái này cài đặt.

Chỉ cần bỏ qua những điều này

những lỗi, những cảnh báo này.

Chúng tôi luôn cố gắng làm những việc để

giảm thiểu những sai sót này và

cảnh báo và họ

luôn xuất hiện,

mọi thứ vẫn sẽ hoạt động.

Hãy tin tôi đi, những thư viện này

và những cuốn sổ này vẫn chạy.

Chúng tôi đã ghim tất cả

các phiên bản thư viện Python nên

rằng khi phiên bản mới ra mắt,

nó sẽ không có khả năng

đập vỡ những cuốn sổ này

vì vậy hãy ghi nhớ điều đó.

Điều này nói lên

khởi động lại hạt nhân,

Tôi không nghĩ bạn

phải làm điều đó

Hãy cứ tiếp tục đi.

Bây giờ chúng ta sẽ thực sự

thực hiện việc nhập khẩu ở đây.

Điều này sẽ nhập khẩu

các hàm được gọi là tải tập dữ liệu,

cái này sẽ được nhập khẩu

một số mô hình

và các tokenizer cần thiết

để hoàn thành phòng thí nghiệm của chúng tôi ở đây.

Chúng ta sẽ sử dụng tập dữ liệu này

được gọi là Tổng đối thoại và

đây là bộ dữ liệu công khai

máy biến áp đó

và đặc biệt là

thư viện bộ dữ liệu

không phơi bày và làm

cho chúng tôi quyền truy cập vào,

vì vậy tất cả những gì chúng tôi làm là gọi

tải tập dữ liệu đó

được nhập khẩu ở trên và chúng tôi

kéo tập dữ liệu này vào.

Bây giờ, từ đây trở đi,

chúng ta sẽ khám phá

một số dữ liệu,

chúng tôi sẽ thực sự cố gắng

tóm tắt chỉ với

mô hình dựa trên T5 phẳng.

Tuy nhiên, trước khi chúng ta đến đó,

hãy để tôi tải tập dữ liệu.

Chúng ta hãy xem xét một số

các ví dụ về tập dữ liệu này

Đây là một đoạn hội thoại mẫu

giữa người 1 và người 2.

Người 1 nói cái gì

Đã đến lúc rồi Tom?

Hình như là người thứ 2

Tên thật của nó là Tom.

Chỉ một phút thôi, đó là

10 giờ đến 9 giờ

đồng hồ của tôi và nhiều thứ khác.

Đây là đường cơ sở

tóm tắt của con người.

Đây là những gì con người có

đã gắn nhãn cuộc trò chuyện này là,

tóm tắt cuộc trò chuyện đó.

Bây giờ chúng tôi sẽ cố gắng cải thiện

dựa trên bản tóm tắt đó

bằng cách sử dụng mô hình của chúng tôi.

Một lần nữa, không có mô hình nào có

thậm chí đã được tải chưa.

Đây hoàn toàn chỉ là

dữ liệu thực tế.

Đây là cuộc trò chuyện và

sau đó nghĩ về điều này như thế nào

đây là mẫu đào tạo

và sau đó đây là những gì

con người đã dán nhãn cho nó và

sau đó chúng ta sẽ so sánh

tóm tắt về con người,

đó là điều chúng tôi đang xem xét

làm nền tảng,

chúng ta sẽ so sánh nó với cái gì

mô hình dự đoán

là tóm tắt.

Trên thực tế, mô hình sẽ

tạo ra một bản tóm tắt.

Đây là một ví dụ thứ hai.

Bạn có thể thấy nó có

một số thuật ngữ quen thuộc

ở đây có rất nhiều người trong chúng ta

quen thuộc với,

Chương trình vẽ CD ROM

cho phần mềm của bạn.

Bây giờ, đây thực sự là nơi chúng ta đang ở

sẽ tải mô hình.

FLAN-T5, chúng tôi đã nói chuyện

về trong các video.

Đây là một vị tướng rất hay

mô hình mục đích có thể làm được

rất nhiều nhiệm vụ

và hôm nay chúng ta sẽ

tập trung vào FLAN-T5,

khả năng tóm tắt

cuộc trò chuyện.

Sau khi tải mô hình,

chúng ta phải tải mã thông báo.

Bây giờ, tất cả những điều này đang đến

từ khuôn mặt ôm

Thư viện máy biến áp.

Để cho bạn một ví dụ, trước đây

máy biến áp xuất hiện,

chúng tôi đã phải viết rất nhiều

của chính mã này.

Tùy thuộc vào loại mô hình,

bây giờ có nhiều thứ khác nhau

mô hình ngôn ngữ và một số

trong số họ làm những việc

rất khác

hơn một số mẫu khác.

Có rất nhiều

thư viện đặc biệt riêng

ngoài kia có tất cả

cố gắng làm những điều tương tự

Rồi Ôm Mặt tới

cùng và thực sự có

được tối ưu hóa rất tốt

việc thực hiện tất cả những điều này.

Bây giờ, đây là mã thông báo.

Đây là những gì đang diễn ra

được sử dụng để chuyển đổi

văn bản thô từ

cuộc trò chuyện của chúng tôi

vào không gian vectơ của chúng ta

điều đó có thể được

được xử lý bằng mô hình Flan-T5 của chúng tôi.

Chỉ để cho bạn một ý tưởng,

chúng ta hãy lấy một cái

câu mẫu

ở đây. Mấy giờ rồi, Tom?

Câu đầu tiên từ

cuộc trò chuyện của chúng tôi ở trên,

chúng ta thấy câu được mã hóa

thực ra là những con số này ở đây

Sau đó nếu bạn giải mã nó,

chúng tôi thấy rằng điều này giải mã

quay lại ngay với bản gốc.

Công việc của tokenizer là

chuyển đổi văn bản thô thành số.

Những con số đó ám chỉ

một tập hợp các vectơ

hoặc các phần nhúng như

họ thường được gọi là,

sau đó được sử dụng trong

các phép toán

như việc học sâu của chúng tôi,

lan truyền ngược,

đại số tuyến tính của chúng tôi,

tất cả những thứ thú vị đó.

Bây giờ hãy chạy ô này ở đây

và tiếp tục khám phá.

Bây giờ, chúng ta đã tải mô hình của mình

và chúng tôi đã tải mã thông báo của mình,

chúng ta có thể chạy qua một số

những cuộc trò chuyện này thông qua

mẫu Flan-T5 và

xem mô hình này làm gì

thực sự tạo ra như một bản tóm tắt

cho những cuộc trò chuyện này.

Ở đây một lần nữa, chúng ta có

cuộc trò chuyện.

Đây lại là

tóm tắt cơ bản.

Sau đó chúng ta thấy mà không có bất kỳ

kỹ thuật nhanh chóng chút nào,

chỉ cần lấy

cuộc trò chuyện thực tế,

chuyển nó tới mẫu Flan-T5 của chúng tôi,

nó không làm được gì nhiều

tóm tắt công việc tốt.

Chúng tôi thấy bây giờ là 9 giờ kém 10.

Điều đó không hữu ích lắm.

Có thêm một số chi tiết trong

cuộc trò chuyện này

không ra ngoài vào thời điểm này.

Tương tự với cuộc trò chuyện

về CD-ROM của chúng tôi,

tóm tắt cơ bản với tư cách là Người

1 dạy Người 2 cách

nâng cấp phần mềm và

phần cứng trong hệ thống của Người 2.

Mô hình được tạo Người 1

đang nghĩ về

nâng cấp máy tính của họ

Một lần nữa, rất nhiều chi tiết trong

bản gốc này

cuộc trò chuyện làm

không đi qua bản tóm tắt.

Hãy xem chúng ta có thể làm thế nào

cải thiện về điều này.

Trong bài các bạn đã học

cách sử dụng hướng dẫn

để nói với người mẫu của bạn bạn là ai

cố gắng làm với dữ liệu

rằng bạn đang vượt qua nó.

Đây là một ví dụ. Đây là

được gọi là học tập trong ngữ cảnh và

đặc biệt là không có bức ảnh nào

suy luận với một hướng dẫn.

Đây là hướng dẫn,

đó là tóm tắt

cuộc trò chuyện sau đây.

Đây là cuộc trò chuyện thực tế,

và sau đó chúng tôi đang nói

mô hình ở đâu

nó sẽ in bản tóm tắt,

điều đó sẽ xảy ra

sau phần tóm tắt từ này.

Bây giờ điều này có vẻ rất đơn giản

và hãy xem nó hoạt động như thế nào.

Hãy xem liệu mọi thứ

trở nên tốt hơn.

Không tốt hơn nhiều ở đây.

Đường cơ sở vẫn là

Người 1 đang vội

Tom nói với Người 2

có rất nhiều thời gian.

Sau đó, cảnh quay số 0 trong bối cảnh

học với lời nhắc,

nó chỉ nói con tàu

sắp rời đi.

Một lần nữa, không phải là lớn nhất.

Và đây là cú sút không

cho mẫu máy tính.

Nó vẫn đang nghĩ thế

Người 1 đang cố gắng nâng cấp,

như vậy cũng không khá hơn là bao.

Chúng ta hãy tiếp tục ở đây.

Có một lời nhắc khác

mà chúng ta có thể sử dụng ở đây,

đó là nơi chúng tôi vừa

nói ngô đối thoại.

Bây giờ những điều này thực sự tùy thuộc vào bạn.

Đây là lời nhắc

mặt kỹ thuật

của ngôn ngữ lớn này

những mô hình mà chúng tôi đang cố gắng

để tìm lời nhắc tốt nhất

và trong trường hợp này chỉ

suy luận không bắn.

Không có sự tinh chỉnh của

người mẫu, không có gì cả.

Tất cả những gì chúng tôi đang làm chỉ là tìm kiếm

hướng dẫn khác nhau để

đi qua và nhìn thấy

nếu mô hình làm

tốt hơn với một chút

cụm từ khác nhau.

Hãy xem điều này diễn ra như thế nào.

Thực sự đây là

nghịch đảo của trước ở đâu

ở đây chúng tôi chỉ đang nói

đây là cuộc đối thoại,

và sau đó

chúng ta đang nói cái gì

đang diễn ra

trong cuộc đối thoại đó.

Hãy xem liệu điều này

làm bất cứ điều gì tốt hơn

Tom bị trễ chuyến tàu,

vì vậy nó đang thu thập thông tin đó,

nhưng vẫn chưa tuyệt vời.

Ở đây chúng ta thấy Người 1.

Bạn có thể thêm một

chương trình vẽ tranh.

Người 2 đó sẽ là một phần thưởng.

Tốt hơn một chút.

Nó không chính xác lắm,

nhưng nó đang trở nên tốt hơn.

Ít nhất là đang chọn

lên một số sắc thái.

Bây giờ, như một phần của

học tập trong bối cảnh,

bạn học được rằng có

cái gì đó gọi là

một phát rồi vài phát.

Chúng ta hãy lấy một mẫu về điều đó ở đây.

Hãy bắt tay vào thực hiện một

bắn rồi bắn ít.

Trước đó chúng tôi đã thực hiện zero-shot.

Điều đó có nghĩa là chúng tôi sẽ không cung cấp nó

bất kỳ mẫu lời nhắc nào

và sau đó là hoàn thành,

tất cả những gì chúng tôi đang làm chỉ là

đưa ra lời nhắc.

Chúng tôi đang yêu cầu người mẫu làm

cái gì đó và nhìn thấy cái gì

mô hình tạo ra.

Với một phát bắn và sau đó vài phát bắn,

chúng tôi thực sự sẽ cung cấp cho nó

các mẫu đúng,

hoặc sử dụng đường cơ sở của con người.

Điều đó mang lại cho mô hình

thêm một chút nữa

thông tin để làm việc.

Chúng ta hãy xem làm thế nào một

bắn hoạt động ở đây.

Tất cả những gì chúng tôi đang làm chỉ là

lấy một ví dụ đầy đủ,

bao gồm cả phần tóm tắt

từ nền tảng cơ bản của con người,

sau đó đưa ra ví dụ thứ hai,

nhưng không có bản tóm tắt thực tế.

Đó là cuộc đối thoại

rằng chúng tôi muốn mô hình

để tóm tắt. Hãy

xem nó trông như thế nào

Một phát có nghĩa là tôi đang cho đi

đó là một ví dụ hoàn chỉnh,

trong đó có câu trả lời đúng

như đã được con người quyết định

ở đây, đường cơ sở của con người.

Sau đó chúng tôi đưa ra ví dụ thứ hai

và hỏi người mẫu

chuyện gì đang xảy ra vậy

Hãy xem chúng tôi làm thế nào ở đây.

Ở đây chúng ta sẽ chỉ

thực hiện nâng cấp phần mềm.

Person1 muốn nâng cấp,

Person2 muốn thêm

chương trình vẽ tranh,

Person1 muốn thêm một CD ROM.

Tôi nghĩ nó tốt hơn một chút

và chúng ta hãy tiếp tục đi.

Có một thứ gọi là

suy luận vài lần là tốt.

Bây giờ một số bạn có thể

đang hỏi, à,

điều này có vẻ như gian lận bởi vì

chúng tôi thực sự đang cho nó

một câu trả lời và sau đó hỏi nó.

Nó không thực sự gian lận.

Đúng hơn là bạn đang giúp đỡ

mô hình tự giúp đỡ chính nó.

Bây giờ trong các bài học sau

và trong các phòng thí nghiệm tương lai,

thực ra chúng tôi sẽ

tinh chỉnh mô hình

nơi chúng ta có thể quay lại

suy luận không bắn,

đó là những gì bạn

thường sẽ nghĩ

như một mô hình ngôn ngữ tốt.

Nhưng ở đây chúng tôi chỉ

xây dựng một số

trực giác ở đây.

Hãy ghi nhớ, đây là

một cách rất rẻ tiền

để thử những mô hình này và

để thậm chí tìm ra cái nào

mô hình bạn nên tinh chỉnh.

Chúng tôi chọn phương án T5

bởi vì nó hoạt động xuyên suốt

một số lượng lớn các nhiệm vụ.

Nhưng nếu bạn không có

ý tưởng về một mô hình như thế nào,

nếu bạn thoát khỏi nó

một số trung tâm mô hình ở đâu đó.

Đây là bước đầu tiên.

Kỹ thuật nhanh chóng,

không bắn, một phát,

hầu như luôn luôn có ít cú đánh

bước đầu tiên khi

bạn đang cố gắng

học mô hình ngôn ngữ

rằng bạn đã từng

bàn giao và tập dữ liệu.

Bộ dữ liệu cũng rất cụ thể

cũng như nhiệm vụ cụ thể.

Ít phát súng có nghĩa là chúng ta

đưa ra ba ví dụ đầy đủ,

bao gồm cả con người

tóm tắt cơ bản, 1, 2, 3,

và sau đó là thứ tư nhưng

không có bản tóm tắt của con người.

Vâng, mặc dù chúng tôi có nó,

chúng tôi chỉ đang khám phá

mô hình của chúng tôi ngay bây giờ.

Chúng tôi đang nói, hãy cho chúng tôi biết điều gì

cuộc đối thoại thứ tư là.

Tóm tắt đó. Chỉ cần bỏ qua

một số lỗi này.

Một số trình tự này

lớn hơn một chút

hơn bối cảnh 512

chiều dài của mô hình.

Thông thường, bạn sẽ

có lẽ muốn lọc ra

bất kỳ đầu vào nào trong số này

lớn hơn 512.

Nhưng ở đây nó vẫn còn

làm một công việc khá tốt.

Ở đây chúng ta thấy một trường hợp

một vài phát súng không có tác dụng gì nhiều

tốt hơn so với một shot.

Đây là một cái gì đó

mà bạn muốn trả

chú ý đến bởi vì

trong thực tế,

mọi người thường cố gắng giữ

ngày càng thêm nhiều bức ảnh,

năm phát, sáu phát.

Thông thường, theo kinh nghiệm của tôi,

trên năm hoặc sáu phát súng,

rất đầy đủ và nhanh chóng

sau đó hoàn thành,

bạn thực sự không đạt được

nhiều sau đó.

Hoặc mô hình có thể

làm điều đó hoặc nó không thể làm được

nó và đi khoảng năm hoặc sáu.

Ở đây chúng ta thấy cho

mẫu đặc biệt này

thực sự một shot là đủ tốt.

Bây giờ là phần cuối cùng của điều này

phòng thí nghiệm sẽ rất vui.

Đây là nơi bạn có thể

thực sự chơi với một số

những cấu hình này

các thông số đó

bạn học trong các bài học.

Những thứ như

lấy mẫu, nhiệt độ.

Bạn có thể chơi thử với những thứ này

ra ngoài và có được trực giác của bạn

về cách những thứ này

có thể tác động đến những gì thực sự

do mô hình tạo ra.

Trong một số trường hợp, ví dụ,

bằng cách nâng cao

nhiệt độ lên trên,

hướng tới một hoặc thậm chí

gần hơn với hai,

bạn sẽ trở nên rất sáng tạo

loại phản hồi.

Nếu bạn hạ nó xuống

Tôi tin rằng 0,1 là

mức tối thiểu để ôm

dù sao cũng phải đối mặt với việc thực hiện,

của thế hệ này

lớp cấu hình ở đây

cái đó được sử dụng khi bạn

thực sự tạo ra.

Tôi có thể vượt qua thế hệ

cấu hình ngay tại đây.

Nếu bạn giảm xuống 0,1,

điều đó thực sự sẽ

làm cho phản hồi nhiều hơn

bảo thủ và đôi khi sẽ

đưa cho bạn điều tương tự

phản hồi nhiều lần.

Nếu bạn đi cao hơn,

Tôi thực sự tin rằng

2.0 là cao nhất.

Nếu bạn cố gắng lên 2.0,

điều đó sẽ bắt đầu mang lại cho bạn

một số phản ứng rất hoang dã.

Thật là vui. Bạn nên thử nó