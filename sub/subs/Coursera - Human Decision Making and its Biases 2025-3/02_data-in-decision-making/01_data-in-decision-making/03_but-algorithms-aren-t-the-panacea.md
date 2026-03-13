# 03 nhưng-thuật toán-là-t-thuốc chữa bách bệnh

---

Chúng tôi đã thấy thuật toán có thể trợ giúp như thế nào

chúng ta đưa ra quyết định tốt hơn.

Nhưng thuật toán không phải là thuốc chữa bách bệnh

mà bạn có thể bị dẫn dắt để tin tưởng.

Hôm nay chúng ta sẽ xem xét những điểm không hoàn hảo

các thuật toán thường xuyên

ẩn dưới bề mặt.

Hãy để tôi chia sẻ một vài ví dụ

để giải thích điều này tốt hơn.

Cách đây vài năm, một sự việc thú vị

đã xảy ra có liên quan đến Amazon Books.

Có một nhà nghiên cứu đã

đang nghiên cứu một cái gì đó

chủ đề đã dẫn anh ấy tới cuốn sách

được gọi là Việc tạo ra một con ruồi.

Anh ấy nhìn vào giá của cuốn sách và

anh ấy ngạc nhiên khi thấy rằng có

hai người bán cuốn sách đó,

một người bán nó với giá 18 triệu USD,

trong khi người kia đang bán

cuốn sách tương tự với giá 23 triệu USD.

Đây là một cuốn sách hiếm, nhưng

anh ấy đã mong đợi mức giá

một vài đô la, có thể là 20 đô la hoặc 30 đô la.

Vậy làm thế nào mà số tiền này lại trở thành 18 triệu đô la và

23 triệu USD?

Nhà nghiên cứu này đã quyết định thực hiện một

chụp màn hình và ghi lại quan sát này.

Điều này thật đáng kinh ngạc phải không?

Hóa ra chuyện gì đã xảy ra

thực sự khá đơn giản.

Đó chỉ là cuộc đụng độ của hai người

thuật toán đơn giản mà

đã cố gắng vượt qua nhau.

Người bán đầu tiên đã sử dụng thuật toán

để xác định giá của cuốn sách.

Họ quyết định đặt giá ở mức

127% giá của đối thủ cạnh tranh.

Người bán thứ hai, người muốn

rẻ hơn người bán đầu tiên,

chọn giá 99%

giá của người bán đầu tiên.

Bây giờ, điều này bắt đầu một cách ngây thơ

với số lượng giá thấp nhưng

nhanh chóng bạn có thể thấy điều đó

giá tiếp tục tăng lên.

Và chẳng bao lâu sau, giá đã đạt đến

tổng số tiền khổng lồ là 23 triệu đô la và

18 triệu USD.

Điều bắt đầu là sự cạnh tranh về thuật toán

nhanh chóng leo thang đến độ cao phi lý.

Định giá theo thuật toán

tiếp tục lặp lại,

khiến giá tăng vọt

đến số tiền cắt cổ.

Các thuật toán thiếu

những ràng buộc thích hợp hoặc

giám sát, và điều này dẫn đến

trong một hậu quả không lường trước được.

Đây là một câu chuyện hấp dẫn để nhắc nhở

chúng ta về khía cạnh kỳ quặc của thuật toán.

Bây giờ chúng ta hãy khám phá một tai nạn khác,

lần này là trên sân bóng.

Một máy ảnh tự động

được thiết kế để theo dõi quả bóng,

liên tục mất dấu nó và

thay vào đó tập trung vào trọng tài.

Bạn có biết chuyện gì đã xảy ra không?

Hóa ra thuật toán AI

nhầm cái đầu trọc của trọng tài là

bóng đá và bắt đầu theo dõi

đầu của anh ấy thay vì quả bóng đá.

Vì vậy, bất chấp hành động

xảy ra trên sân,

máy ảnh không ngừng nghỉ

quay lại với trọng tài.

Thật buồn cười phải không?

Những ví dụ này dạy chúng ta rằng

AI có những hạn chế của nó.

Lấy qure.ai làm ví dụ.

các nhà phân tích của qure.ai đang xây dựng

một thuật toán để tìm ra cái gì

X-quang ngực bất thường và phân biệt

nó từ X-quang ngực bình thường.

Và hóa ra thuật toán

cực kỳ chính xác.

Vì vậy họ đã xem xét dữ liệu và

đã phát hiện ra rằng thuật toán này là

nhặt các ghi chú được viết trên tia X và

xác định rằng bất kỳ tia X nào có

ghi chú viết trên đó là một điều bất thường.

Bây giờ, bạn có thể thấy vấn đề với điều này,

phải không?

bởi vì khi ở ngoài đời thực, một tấm X-quang mới

xuất hiện và nó không được chú thích,

thuật toán sẽ chọn nó và

cho rằng đó có thể là một tia X bình thường.

Vì vậy, thuật toán có cách chọn này

cập nhật thông tin có thể không phải lúc nào cũng có

dự định, và lấy nó và sử dụng nó

thông tin theo những cách không mong muốn là tốt.

Khám phá này cho thấy tầm quan trọng

hiểu biết về dữ liệu cơ bản và

rủi ro của việc trang bị quá mức

mô hình không có bối cảnh phù hợp.

Tôi chắc chắn bạn cũng biết về

Thí nghiệm của Microsoft trên Twitter.

Họ tung ra một robot tên là Tay,

dành cho Công nghệ và bạn.

Điều này được giới thiệu là một thiếu niên AI

sẽ tương tác với thế giới.

Vì vậy vào năm 2016, khi Tay ra mắt đã

ra mắt với rất nhiều sự phô trương.

Nhưng chỉ trong một ngày,

Tay nhanh chóng mất kiểm soát,

đưa ra những nhận xét phân biệt giới tính và phân biệt chủng tộc.

Cuối cùng, nó phải như vậy

tắt ngay trong ngày.

Những người lập mô hình đã không lường trước được

tác động của các phản ứng không được lọc và

tương tác trên Twitter.

Người ta đã có thể đẩy

bot tạo ra nhiều thứ khác nhau

các loại nhận xét,

nhận xét phân biệt giới tính và phân biệt chủng tộc.

Nó lại đóng vai trò như một lời nhắc nhở ấn tượng

thậm chí là tiên tiến nhất

Hệ thống AI có thể dễ bị

những hậu quả không lường trước được.

Cuối cùng, hãy xem ví dụ về

Zillow, một công ty bất động sản có trụ sở tại Hoa Kỳ.

Một vài năm trước, Zillow đã sử dụng

một mô hình dự đoán giá nhà hiệu quả,

nhưng sự mở rộng đầy tham vọng của họ và

quá phụ thuộc vào thuật toán

dẫn tới sự thất bại thảm hại.

Hãy thảo luận về những gì đã xảy ra ở đây.

Mô hình kinh doanh chủ yếu của Zillow

liên quan đến việc cung cấp bất động sản

thông tin và dịch vụ,

trong đó có ước tính định giá tài sản.

Để hỗ trợ hoạt động của họ, Zillow

phát triển thuật toán dự đoán nhà

giá cả, máy tận dụng

kỹ thuật học tập.

Những thuật toán này là công cụ trong

sự thành công của chương trình mua hàng của họ được biết đến

như Ưu đãi của Zillow.

Họ nhận ra rằng họ có thể sử dụng

mô hình dự đoán giá này,

tìm ra những ngôi nhà được định giá thấp, và

dùng vốn tự có để mua

những ngôi nhà đó và bán chúng sau này.

Đây được gọi là Ưu đãi của Zillow.

Zillow aggressively expanded

chương trình mua hàng của nó,

có được một số lượng đáng kể

nhà trong thời gian ngắn.

Tuy nhiên, thuật toán của họ đã thất bại.

điều chỉnh theo sự thay đổi động lực của thị trường.

Kết quả là,

Thuật toán của Zillow một cách nhất quán

đã đánh giá quá cao giá trị của những ngôi nhà

mà họ đã trả tiền.

Cuối cùng, họ đã có một lượng lớn

kiểm kê những ngôi nhà chưa bán được.

Mấu chốt của vấn đề nằm ở

một hiện tượng được gọi là sự trôi dạt khái niệm.

Sự trôi dạt khái niệm xảy ra khi

các mô hình cơ bản và

mối quan hệ trong dữ liệu

thay đổi theo thời gian,

điều này làm cho mô hình ban đầu ít hơn

chính xác hoặc thậm chí hoàn toàn không chính xác.

Nếu thuật toán Zillow đang tìm kiếm

thông tin tài sản bị định giá sai,

và giá tài sản cơ bản

đã thay đổi với khái niệm trôi dạt này,

các mô hình có thể trở nên rất không chính xác.

Trong trường hợp của Zillow, vỏ làm mát

thị trường trình bày một kịch bản của khái niệm

trôi dạt và thuật toán của họ không thành công

thích ứng với điều kiện thị trường mới.

Trong khi các thuật toán của Zillow thực hiện

đáng ngưỡng mộ trong những năm trước đó,

họ chùn bước khi nhà ở

thị trường hạ nhiệt.

Thay vì nhận ra sự thay đổi và

điều chỉnh mô hình của họ cho phù hợp,

Thuật toán của Zillow tiếp tục giả định

rằng thị trường vẫn nóng, và

họ có thể thấy nhiều cơ hội hơn

để mua những ngôi nhà được định giá thấp.

Sự thất bại trong việc thích ứng này đã dẫn đến sự nhất quán

đánh giá quá cao giá nhà,

và hậu quả thực sự tồi tệ đối với

Zillow.

Zillow tiếp tục giữ nhà trống

với hy vọng giá sẽ phục hồi,

và trong khi đó chi phí

gắn kết đáng kể.

Cuối cùng, Zillow đã tìm thấy chính mình

trong tình thế bấp bênh,

buộc phải bán số lượng lớn nhà

ở mức giá thấp hơn chi phí mua hàng của họ,

họ đã phải chịu một khoản lỗ lớn,

cổ phiếu của họ giảm giá.

Gánh nặng tài chính này bất lợi

đã tác động đến lợi nhuận của công ty và

làm xói mòn niềm tin của nhà đầu tư.

Zillow đã dựa quá nhiều vào các thuật toán.

Và sai lầm thuật toán này phục vụ

như một lời nhắc nhở rằng các mô hình AI

không phải là không thể sai lầm.

Trên thực tế,

hiệu suất của họ không giảm theo thời gian.

Nó nhấn mạnh sự cần thiết của

theo dõi, cập nhật liên tục và

hiệu chỉnh lại các mô hình AI để

đảm bảo tính chính xác liên tục của chúng.

Trường hợp của Zillow nhấn mạnh

tầm quan trọng của sự giám sát của con người và

can thiệp vào thuật toán

các quá trình ra quyết định.

Trong khi các thuật toán có thể tự động hóa một số

nhiệm vụ và cung cấp những hiểu biết có giá trị của con người,

sự phán xét của con người vẫn cần thiết cho

sự hiểu biết theo ngữ cảnh,

phân tích thị trường và điều chỉnh

các mô hình khi cần thiết.

Câu chuyện của Zillow và

mô hình dự đoán giá của nó nhấn mạnh

những rủi ro của việc phụ thuộc quá nhiều vào các mô hình.

Mô hình và thuật toán còn hạn chế

chúng được xây dựng để phục vụ

một mục đích nhất định và

thực sự không thể hoạt động ngoài điều đó.

Họ thường không đại diện cho thực tế

trong bất kỳ biện pháp đầy đủ nào và không thể xử lý

sự phức tạp của thế giới thực,

Thế giới VUCA mà chúng ta gặp hàng ngày.

Điều này đúng ngay cả đối với AI sáng tạo.

Chúng ta đã thấy trong hai năm qua,

Các mô hình AI sáng tạo đã bắt đầu hiển thị

kết quả kỳ diệu và đã bắt đầu chơi

vai trò rất quan trọng trong việc tự động hóa

quyết định và tăng cường các quyết định của con người.

Những mô hình này mạnh mẽ và

giống con người hơn nhưng

có những hạn chế rất giống nhau.

Họ có thể bị ảo giác,

tạo ra các sự kiện, làm các phép toán đơn giản và

lỗi logic, và có thể có sai lệch và

hạn chế về kiến thức của bản thân.

Trong vài năm tới,

bất chấp điều này,

chúng tôi sẽ tiếp tục tăng cường

phụ thuộc vào các thuật toán nói chung.

Chìa khóa để đưa ra quyết định đúng đắn

trong thế giới phức tạp này sẽ nằm ở

sự kết hợp thông minh của cái nhìn sâu sắc của con người,

sự khéo léo của con người với

thông tin đáng chú ý

sức mạnh xử lý của máy.