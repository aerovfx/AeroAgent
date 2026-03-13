# 06 mô hình-đánh giá

---

Trong suốt điều này

tất nhiên, bạn đã thấy

những phát biểu như

mô hình đã được chứng minh

thực hiện tốt nhiệm vụ này hoặc

mô hình tinh chỉnh này cho thấy

một cải tiến lớn trong

hiệu suất so với mô hình cơ sở.

phát biểu làm gì

như thế này có nghĩa là gì?

Làm thế nào bạn có thể chính thức hóa

cải thiện hiệu suất của

mô hình tinh chỉnh của bạn hơn

mô hình được đào tạo trước

bạn đã bắt đầu với?

Hãy cùng khám phá một số

các số liệu được

được sử dụng bởi các nhà phát triển lớn

mô hình ngôn ngữ mà bạn

có thể sử dụng để đánh giá

hiệu suất của

mô hình của riêng bạn và so sánh

sang các mô hình khác

ra ngoài thế giới.

Trong học máy truyền thống,

bạn có thể đánh giá như thế nào

à một người mẫu là

làm bằng cách nhìn vào

hiệu suất của nó trên

dữ liệu đào tạo và xác nhận

đặt nơi đầu ra

đã được biết đến.

Bạn có thể tính toán đơn giản

các chỉ số như độ chính xác,

trong đó nêu phân số

của tất cả các dự đoán

đúng vì

các mô hình mang tính quyết định.

Nhưng với ngôn ngữ lớn

mô hình nơi đầu ra là

không xác định và

đánh giá dựa trên ngôn ngữ

thách thức hơn nhiều.

Lấy ví dụ, câu,

Mike thực sự thích uống trà.

Điều này khá giống với

Mike thích nhấm nháp trà.

Nhưng làm thế nào để bạn đo lường

sự giống nhau?

Chúng ta hãy nhìn vào những điều này

hai câu còn lại.

Mike không uống cà phê,

và Mike uống cà phê.

Chỉ có một

sự khác biệt từ

giữa hai câu này.

Tuy nhiên, ý nghĩa là

hoàn toàn khác.

Bây giờ, đối với con người như chúng ta với

bộ não hữu cơ yếu đuối,

chúng ta có thể thấy sự tương đồng

và sự khác biệt.

Nhưng khi bạn huấn luyện một người mẫu

trên hàng triệu câu,

bạn cần một hệ thống tự động,

cách có cấu trúc để

thực hiện các phép đo.

ROUGE và BLEU,

là hai được sử dụng rộng rãi

chỉ số đánh giá

cho các nhiệm vụ khác nhau.

ROUGE hoặc thu hồi theo định hướng

học để đùa giỡn

đánh giá chủ yếu là

được sử dụng để đánh giá

chất lượng của

tự động

tóm tắt được tạo bởi

so sánh chúng với do con người tạo ra

tóm tắt tham khảo.

Mặt khác, BLEU,

hoặc đánh giá song ngữ

học sinh là

một thuật toán

được thiết kế để đánh giá

chất lượng của

văn bản được dịch bằng máy,

một lần nữa, bằng cách so sánh nó với

bản dịch do con người tạo ra.

Bây giờ từ BLEU

là tiếng Pháp có nghĩa là màu xanh lam.

Bạn có thể nghe thấy mọi người

gọi đây là màu xanh

nhưng ở đây tôi sẽ tiếp tục

với BLEU gốc.

Trước khi chúng ta bắt đầu

tính toán các chỉ số.

Hãy xem xét một số thuật ngữ.

Trong giải phẫu của ngôn ngữ,

một unigram là tương đương

thành một từ duy nhất.

Một bigram là hai từ và

n-gram là một nhóm n-từ.

Những thứ khá đơn giản.

Đầu tiên, chúng ta hãy nhìn vào

số liệu ROUGE-1.

Để làm như vậy, chúng ta hãy nhìn vào

do con người tạo ra

câu tham khảo.

Bên ngoài trời lạnh và

một đầu ra được tạo ra

bên ngoài rất lạnh.

Bạn có thể thực hiện đơn giản

tính toán số liệu tương tự

sang học máy khác

nhiệm vụ sử dụng thu hồi,

độ chính xác và F1.

Chỉ số thu hồi

đo số

của từ hoặc unigram

phù hợp

giữa tham chiếu

và đầu ra được tạo ra

chia cho

số từ hoặc

unigram trong tài liệu tham khảo.

Trong trường hợp này, điều đó nhận được một

điểm tuyệt đối của một như

tất cả các từ được tạo đều khớp

các từ trong tài liệu tham khảo.

Các biện pháp chính xác

trận đấu của unigram

chia cho kích thước đầu ra.

Điểm F1 là

ý nghĩa hài hòa của

cả hai giá trị này.

Đây là những số liệu rất cơ bản

điều đó chỉ tập trung vào

các từ riêng lẻ,

do đó cái tên trong tên,

và đừng xem xét

thứ tự của các từ.

Nó có thể lừa dối.

Thật dễ dàng có thể

tạo ra các câu

ghi điểm tốt nhưng sẽ

nghèo về mặt chủ quan.

Hãy dừng lại một chút và tưởng tượng

mà câu đã tạo ra

bởi mô hình là khác nhau

chỉ bằng một từ.

Không, nên bên ngoài trời không lạnh.

Điểm số sẽ giống nhau.

Bạn có thể nhận được một chút

ghi điểm tốt hơn bằng cách

có tính đến bigram hoặc

bộ sưu tập của hai

từng từ một từ

tài liệu tham khảo và

câu được tạo ra.

Bằng cách làm việc với các cặp từ

bạn đang thừa nhận

một cách rất đơn giản,

sự sắp xếp của

các từ trong câu.

Bằng cách sử dụng bigram, bạn

có thể tính toán ROUGE-2.

Bây giờ, bạn có thể tính toán

việc thu hồi, độ chính xác,

và điểm F1 bằng cách sử dụng

thay vào đó là trận đấu bigram

của từng từ riêng lẻ.

Bạn sẽ nhận thấy điều đó

điểm số là

thấp hơn điểm ROUGE-1.

Với những câu dài hơn, chúng

cơ hội lớn hơn đó

bigram không khớp,

và điểm số có thể

thậm chí còn thấp hơn.

Thay vì tiếp tục

bật với số ROUGE

ngày càng lớn hơn đến n-gram

ba hoặc bốn,

chúng ta hãy thực hiện một cách tiếp cận khác.

Thay vào đó, bạn sẽ tìm

chung dài nhất

trình tự có mặt trong

cả đầu ra được tạo ra

và đầu ra tham chiếu.

Trong trường hợp này, dài nhất

các dãy con phù hợp là,

bên ngoài trời lạnh và

mỗi cái có chiều dài bằng hai.

Bây giờ bạn có thể sử dụng giá trị LCS để

tính toán thu hồi

độ chính xác và điểm F1,

trong đó tử số ở cả hai

sự thu hồi và độ chính xác

tính toán là độ dài

dài nhất

dãy con chung,

trong trường hợp này là hai.

Nói chung, những

ba số lượng

được gọi là điểm Rouge-L.

Như với tất cả các điểm rouge,

bạn cần phải lấy

các giá trị trong ngữ cảnh.

Bạn chỉ có thể sử dụng điểm số

để so sánh khả năng của

mô hình nếu điểm số là

xác định cho cùng một nhiệm vụ.

Ví dụ như tóm tắt.

Điểm Rouge cho các nhiệm vụ khác nhau

không thể so sánh được

với nhau.

Như bạn đã thấy, một

vấn đề cụ thể

với điểm rouge đơn giản là

rằng điều đó là có thể đối với

một sự hoàn thành tồi tệ

mang lại kết quả đạt điểm tốt.

Lấy ví dụ,

đầu ra được tạo ra này,

lạnh, lạnh, lạnh, lạnh.

Như điều này tạo ra

đầu ra chứa

một trong những từ từ

câu tham khảo,

nó sẽ đạt điểm khá cao,

mặc dù cùng một từ

được lặp đi lặp lại nhiều lần.

Độ chính xác của Rouge-1

điểm số sẽ hoàn hảo.

Một cách bạn có thể chống lại

vấn đề này là do

sử dụng chức năng cắt

để hạn chế số lượng

unigram khớp với

số lượng tối đa

cho unigram đó

trong phạm vi tham chiếu.

Trong trường hợp này, có

một vẻ ngoài lạnh lùng

và tài liệu tham khảo và

vì vậy độ chính xác được sửa đổi

với một clip trên

kết quả trùng khớp của unigram

với số điểm giảm đáng kể.

Tuy nhiên, bạn vẫn sẽ

bị thử thách nếu

những từ được tạo ra của họ

đều có mặt,

nhưng chỉ theo một thứ tự khác.

Ví dụ, với điều này

câu được tạo ra,

ngoài trời lạnh lắm.

Câu này được gọi là

hoàn toàn ngay cả trên

độ chính xác được sửa đổi với

chức năng cắt

như tất cả các từ và

đầu ra được tạo ra là

có trong tài liệu tham khảo.

Trong khi sử dụng một

điểm rouge khác nhau

có thể giúp thử nghiệm với

kích thước n-gram đó

sẽ tính toán

điểm số hữu ích nhất sẽ là

phụ thuộc vào câu

kích thước câu,

và trường hợp sử dụng của bạn.

Lưu ý rằng nhiều mô hình ngôn ngữ

thư viện chẳng hạn

Ôm Mặt, mà bạn đã sử dụng

trong phòng thí nghiệm của tuần đầu tiên,

bao gồm việc triển khai

về số điểm rouge mà bạn

có thể sử dụng để dễ dàng đánh giá

đầu ra của mô hình của bạn.

Bạn sẽ được dùng thử rouge

cho điểm và sử dụng nó để so sánh

của người mẫu

hiệu suất trước và

sau khi tinh chỉnh

trong phòng thí nghiệm của tuần này.

Điểm số khác có thể

hữu ích trong việc đánh giá

hiệu suất của bạn

mô hình là điểm BLEU,

viết tắt của song ngữ

đánh giá đang được nghiên cứu.

Chỉ để nhắc nhở bạn rằng

Điểm BLEU rất hữu ích cho

đánh giá chất lượng của

văn bản được dịch bằng máy.

Bản thân điểm số là

tính toán bằng cách sử dụng

độ chính xác trung bình trên

nhiều kích cỡ n-gram.

Giống như điểm Rouge-1

mà chúng ta đã xem xét trước đây,

nhưng được tính toán cho một phạm vi

kích thước n-gram và sau đó tính trung bình.

Chúng ta hãy đến gần hơn

nhìn cái gì thế này

biện pháp và cách thức

nó đã được tính toán.

Điểm BLEU định lượng

chất lượng của một

dịch bằng cách kiểm tra

có bao nhiêu n-gram trong

máy tạo ra

trận đấu dịch

những người trong tài liệu tham khảo

bản dịch.

Để tính điểm,

độ chính xác trung bình của bạn trên

một loạt các khác nhau

kích thước n-gram.

Nếu bạn định

tính toán bằng tay,

bạn sẽ thực hiện nhiều

tính toán và sau đó

trung bình tất cả các kết quả

để tìm điểm BLEU.

Đối với ví dụ này,

chúng ta hãy nhìn vào

một câu dài hơn

để bạn có thể có được

một cảm giác tốt hơn về

giá trị điểm số.

Tài liệu tham khảo

câu do con người cung cấp là,

Tôi rất vui khi nói rằng tôi

đang uống một tách trà ấm.

Bây giờ, như bạn đã thấy

những tính toán riêng lẻ này trong

chiều sâu khi bạn nhìn vào rouge,

Tôi sẽ cho bạn thấy kết quả của

BLEU sử dụng thư viện chuẩn.

Tính điểm BLEU là

dễ dàng với văn bản trước

thư viện từ nhà cung cấp

thích ôm mặt

và tôi vừa mới làm xong

điều đó đối với mỗi người chúng ta

câu ứng cử viên.

Ứng cử viên đầu tiên là,

Tôi rất hạnh phúc vì tôi

đang uống một tách trà.

Điểm BLEU là 0,495.

Khi chúng ta ngày càng đến gần hơn

vào câu gốc,

chúng tôi nhận được số điểm đó là

ngày càng gần nhau hơn.

Cả rouge và BLEU đều

số liệu khá đơn giản và

chi phí tương đối thấp

để tính toán.

Bạn có thể sử dụng chúng cho

tham khảo đơn giản như bạn

lặp lại các mô hình của bạn,

nhưng bạn không nên sử dụng

họ một mình báo cáo

đánh giá cuối cùng của

một mô hình ngôn ngữ lớn

Sử dụng rouge để chẩn đoán

đánh giá của

nhiệm vụ tổng hợp và

BLEU cho nhiệm vụ dịch thuật.

Để đánh giá tổng thể về

mô hình của bạn

tuy nhiên, hiệu suất

bạn sẽ cần phải nhìn vào một trong

sự đánh giá

điểm chuẩn có

được phát triển bởi các nhà nghiên cứu.

Chúng ta hãy xem

tại một số trong số này trong

chi tiết hơn trong video tiếp theo.