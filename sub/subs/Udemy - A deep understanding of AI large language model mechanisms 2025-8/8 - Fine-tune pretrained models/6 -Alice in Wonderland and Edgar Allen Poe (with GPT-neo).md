# 6 -Alice ở xứ sở thần tiên và Edgar Allen Poe (với GPT-neo)

---

Mình có series video ở phần này về tinh chỉnh mẫu để viết theo phong cách

của Alice ở xứ sở thần tiên hay Edgar Allan Poe.

Vì vậy, mục tiêu của video này là giới thiệu cho bạn khái niệm và một số mã

bạn sẽ sử dụng trong một số thử thách mã tiếp theo ở phần sau của phần này.

Tôi cũng sẽ giới thiệu cho bạn một mẫu khác

được gọi là GPT-Neo.

Điều này dựa trên GPT của OpenAI,

nhưng đó là một mô hình khác với tập hợp trọng lượng khác.

Đặc biệt, chúng tôi sẽ sử dụng các mô hình được cung cấp

bởi một tổ chức tên là eLuther.

Ở đây bạn thấy một ảnh chụp màn hình của trang web của họ.

Họ có một lịch sử khá thú vị.

Nó bắt đầu giống như một máy chủ Discord nhỏ

để thảo luận về nghiên cứu về sự liên kết của LLM

và nó phát triển từ đó.

Và bây giờ nó là một công ty độc lập phát triển các mô hình

và thực hiện nghiên cứu về khả năng diễn giải.

Nếu bạn tò mò,

bạn có thể đọc thêm về họ trên trang web của họ.

Nhưng bây giờ tôi sẽ tập trung vào bản demo Python.

Chúng tôi sẽ bắt đầu bằng cách nhập và kiểm tra mô hình này.

Trên thực tế, sẽ có hai phiên bản của mô hình này.

Thứ nhất, tôi sẽ luyện tập sử dụng bài văn trong Alice in Wonderland.

Về mặt kỹ thuật, cuốn sách có tên là Qua Kính Nhìn,

nhưng mọi người đều biết đến nó với cái tên Alice ở xứ sở thần tiên.

Và mô hình khác tôi sẽ huấn luyện bằng thơ

và truyện ngắn của Edgar Allan Poe.

Bây giờ, khi bạn xem qua danh sách các tính năng của mô hình,

bạn sẽ nhận ra kiến trúc của mô hình này,

và bạn cũng sẽ nhận ra rằng nó không hoàn toàn giống nhau

như cách tổ chức GPT-2 của OpenAI.

Tôi sẽ chỉ ra nhiều hơn về những khác biệt này

khi chúng ta đến chỗ đó, khi tôi chuyển sang viết mã,

nhưng bạn có thể thấy, ví dụ,

rằng trọng số chú ý được lưu trữ ở đây

dưới dạng ba ma trận riêng biệt

thay vì như một ma trận được nối với nhau.

Dù sao thì chúng ta cũng sẽ xem xét tokenizer.

Mã thông báo eluthor có 50.257 mã thông báo,

và tôi chắc chắn con số đó nghe quen quen

bởi vì đó là cùng số lượng mã thông báo

với tư cách là mã thông báo OpenAI GPT-2.

Vì vậy, chúng tôi cũng sẽ điều tra thêm về điều này.

Sau đó chúng tôi sẽ nhập thêm một số sách từ Gutenberg.org

và thấy rằng văn bản của Edgar Allan Poe

có số lượng token gấp khoảng bốn lần

làm văn bản cho Alice ở xứ sở thần tiên.

Thực ra, như tôi đã đề cập,

về mặt kỹ thuật nó được gọi là Qua Kính Nhìn,

nhưng không sao đâu.

Vì vậy, chúng ta sẽ tinh chỉnh hai mô hình,

một trên mỗi văn bản,

điều đó cũng có nghĩa là chúng ta cần hai trình tối ưu hóa riêng biệt

cho hai phiên bản của mô hình.

Ở đây bạn thấy hồ sơ tổn thất,

cả hai đều giảm khi luyện tập,

nhưng chúng khá khác nhau.

Tôi sẽ có một số nhận xét về

tại sao điều đó có thể xảy ra trong mã.

Bây giờ là viên ngọc quý của bản demo mã này

sẽ là đánh giá chất lượng

về cách hai mô hình này phản ứng với cùng một lời nhắc.

Nếu bạn đang rất thiếu kiên nhẫn và muốn biết ngay bây giờ,

Vậy thì tôi rất tiếc phải nói với bạn rằng,

bạn sẽ phải đợi để xem câu trả lời

của hai mô hình này với dấu nhắc đầu vào này,

nhưng tôi hứa bạn sẽ không thất vọng.

Được rồi, hãy chuyển sang mã.

Hầu hết các thư viện điển hình mà chúng ta sẽ sử dụng ở đây

và cả torchinfo.summary.

Được rồi, đây là eluthor GPT-neo125m.

125M, đây là 125 triệu thông số.

Vì vậy về cơ bản nó có cùng kích thước,

hoặc nó thực sự có cùng kích thước

như OpenAI GPT-2 Small.

Các mô hình không giống nhau.

Họ được đào tạo trước theo nhiều cách khác nhau

trên các cơ sở dữ liệu văn bản khác nhau.

Vì vậy các mô hình không giống nhau,

mặc dù chúng có cùng kích thước

và họ sử dụng cùng một mã thông báo.

Ở đây tôi đang chỉ định mã thông báo pad thực sự là một khoảng trắng,

điều này khác với những gì chúng tôi đã làm trong các video trước.

Được rồi, ở đây tôi đang tải mô hình GPT-2, phải không?

Vì vậy, đây là mã thông báo, đây là mô hình thực tế,

và bạn có thể thấy dòng mã này

được lặp lại chính xác hai lần.

Tôi chỉ đặt nó vào hai mô hình khác nhau.

Vậy người mẫu Alice và người mẫu Edgar.

Chúng chính xác là những mô hình giống nhau.

Họ bắt đầu giống hệt nhau.

Cả hai đều đã được đào tạo trước,

nhưng tôi sẽ tinh chỉnh chúng trên các văn bản khác nhau.

Được rồi, các bộ dữ liệu khác nhau.

Và ở đây tôi sẽ đẩy cả hai vào GPU.

Ở đây chúng ta có thể kiểm tra mô hình

như tôi đã hiển thị ảnh chụp màn hình trong các trang trình bày cách đây một lúc.

Bất cứ khi nào bạn làm việc với một mô hình mới,

Tôi thực sự khuyên bạn chỉ nên in mô hình ra

và xem tên là gì

của các thành phần khác nhau của mô hình.

Chúng không giống nhau trên các mô hình khác nhau

và kích cỡ khác nhau của một mô hình

ngay cả trong cùng một tổ chức.

Vì vậy, đó cũng là lý do tại sao thật tuyệt vời khi thực sự hiểu được

những gì liên quan đến việc tập hợp một mô hình,

đặc biệt là khối máy biến áp.

Vì vậy, nó không quá khác biệt.

Những cái tên sẽ khác nhau.

Đôi khi chúng được gọi là từ nhúng,

vị trí, một cái gì đó như thế.

Vì vậy, nó không nhất thiết phải giống nhau, giống hệt nhau.

Và vâng, đây là điểm khác biệt lớn nhất

là cái này được tách ra,

những ma trận trọng số chú ý này được tách ra

vào các ma trận vuông riêng biệt của chúng

thay vì được nối thành một,

đó là những gì OpenAI có xu hướng làm.

Ở đây bạn cũng thấy trong lớp MLP,

chúng tôi vẫn nhận được bản mở rộng gấp 4 lần này.

Vậy 768 nhân bốn là 3.072.

Được rồi, và vâng, tất cả những thứ này

về cơ bản là giống nhau.

Được rồi, bây giờ tôi đã làm điều này một chút trước đây,

nhưng tôi chỉ muốn cho bạn xem, để tôi xem.

Được rồi, người mẫu Alice, đó là điều tôi đã làm trước đây.

Bây giờ tôi muốn truy cập vào máy biến áp.

Vì vậy tôi có thể viết .transformer,

Và điều đó mang lại cho tôi phần máy biến áp của mô hình.

Bây giờ mô hình này hơi khó hiểu một chút.

Thuật ngữ có một chút khó hiểu

vì chúng tôi gọi đây là khối biến áp.

Nhưng trong mô hình cụ thể này,

toàn bộ phần này được gọi là máy biến áp,

bao gồm cả các phần nhúng.

Và trên thực tế, điều duy nhất không được đưa vào

trong lớp máy biến áp này là đầu LM cuối cùng,

đó là sự gỡ bỏ.

Vì vậy, khi tôi viết mô hình Alice dot Transformer,

Tôi đang nhận được các phần nhúng mã thông báo, các phần nhúng vị trí,

vân vân, tất cả những thứ này.

Điều duy nhất còn sót lại

là ma trận hủy nhúng cuối cùng.

Vì vậy nếu chúng ta thực sự muốn truy cập vào các khối biến áp,

chúng ta có thể viết dấu chấm H.

Và bây giờ, vâng, vậy là bây giờ chúng ta không còn thấy nữa

các ma trận nhúng.

Và sau đó hãy nói rằng, bây giờ về cơ bản tôi chỉ

theo dõi thông qua điều này ở đây.

Vậy bây giờ giả sử chúng ta muốn cái thứ bảy,

Tôi sẽ làm nó khác đi một chút,

khối máy biến áp thứ bảy.

Vậy đây là khối máy biến áp thứ bảy.

Và bạn có thể thấy điều này sẽ đi đến đâu.

Tôi sẽ không mất quá nhiều thời gian, nhưng.

Về cơ bản chúng ta có thể bắt đầu truy cập

tất cả các yếu tố riêng lẻ.

Đây là tất cả các trọng số của ma trận K.

Và vâng, ở đây tôi chỉ đang xem xét kích thước của cái này.

Vì vậy trong một số phần tiếp theo,

Tôi muốn bạn ngày càng trở nên thoải mái hơn

với việc truy cập tất cả các phần tử và số riêng lẻ

và ma trận trong các mô hình này.

Và khi chúng ta đến phần

về khả năng diễn giải cơ học,

chúng ta thực sự sẽ lặn sâu

vào các kiến trúc mô hình và tất cả các tham số này

và kích hoạt, v.v.

Được rồi, vâng, ở đây tôi đang sử dụng torchinfo.summary

và điều đó đòi hỏi một ít dữ liệu để nhập vào.

Bạn chỉ có thể xem ở đây tất cả các thông số.

Tôi hy vọng rằng một số con số này trông quen thuộc

từ hai phần trước về việc xây dựng GPT,

nơi chúng tôi phát hiện ra rằng mô hình 5 của chúng tôi

có kiến trúc giống hệt như GPT2 nhỏ,

giả sử rằng việc gỡ bỏ

và các ma trận nhúng được gắn với nhau,

và do đó chúng ta có thể trừ con số này

từ con số này để có được 124 triệu,

sao cũng được, tôi quên mất con số chính xác.

Được rồi, đó là điều tôi đang làm ở đây.

Vì vậy, chúng tôi muốn biết liệu ma trận nhúng,

các phần nhúng ban đầu cũng giống như các phần không nhúng.

Và bây giờ nếu bạn muốn định lượng điều này thật chính xác,

sẽ là một ý kiến hay nếu trừ các ma trận

và xem liệu có giá trị nào khác 0 không

hoặc lấy chuẩn của ma trận sai phân

và xem liệu nó có bằng 0 không.

Ở đây tôi đang làm một việc rất đơn giản,

chỉ in ra các phần của mảnh rất nhỏ

của hai ma trận này.

Và bạn có thể thấy rằng những con số này thực sự có vẻ khớp với nhau.

Và trên thực tế, đó là trường hợp của mô hình eluthor này,

phần nhúng và phần không nhúng được gắn với nhau.

Được rồi, một chút về tokenizer.

Thực ra, tôi nghĩ mình sẽ vượt qua chuyện này rất nhanh.

Hóa ra đây là điều tương tự

làm mã thông báo GPT-2.

Và để chứng minh điều đó,

Tôi đang nhập mã thông báo GPT-2 tại đây.

Và ở đây tôi chỉ in ra một vài mã thông báo ngẫu nhiên,

chỉ mục mã thông báo và sau đó là chuỗi mã thông báo trong,

xem nào, cái đầu tiên là eluthor,

và cái thứ hai là GPT.

Và bạn thấy đấy, chúng đều giống nhau.

Xác suất điều này xảy ra một cách tình cờ,

nếu đây là những tokenizer khác nhau,

giống như nhỏ hơn một chia cho số hạt

trong vũ trụ, có thể.

Vì vậy, dù sao đi nữa, vâng, vậy thì mã thông báo eluter

là mã thông báo GPT-2.

Được rồi, tôi đang nhận được hai tin nhắn

và chỉ in ra một số

đặc điểm cơ bản của chúng.

Vậy 50.000 token trong Alice ở xứ sở thần tiên,

200.000 token trong văn bản của Edgar Allan Poe.

Alice ở xứ sở thần tiên, đây chỉ là một cuốn sách thôi phải không?

Nó xuyên qua tấm gương của Lewis Carroll.

Nhân tiện, cuốn sách tuyệt vời.

Văn bản của Edgar Allan Poe trên Gutenberg.org

không chỉ là một cuốn sách, nó thực sự là một bộ sưu tập

thơ và truyện ngắn của Edgar Allan Poe.

Đó là một phần lý do tại sao nó dài hơn một chút.

Điều đó cũng có nghĩa là văn bản này đa dạng hơn một chút

bởi vì có rất nhiều văn bản khác nhau được ghép lại với nhau.

Tất nhiên, Edgar Allan Poe có chất giọng rất đặc trưng.

Anh ấy có giọng hát rất đặc biệt

rất tối và rất rùng rợn.

Nhưng chắc chắn là giọng điệu đó, phong cách viết đó

thấm vào tất cả các văn bản,

nhưng ở đây có nhiều sự đa dạng hơn ở đây.

Được rồi, bây giờ chúng ta đang chuẩn bị tinh chỉnh.

Ở đây tôi tạo hai trình tối ưu hóa.

Chúng tôi muốn có một trình tối ưu hóa riêng cho từng mô hình này.

Mặt khác, cả hai đều giống hệt nhau.

Họ có cùng tốc độ học tập.

Đó là cơ chế tối ưu hóa tương tự,

chỉ là các thông số khác nhau được đẩy vào chúng.

Được rồi, và sau đó, chúng ta sẽ tập luyện

sử dụng 16 lô 256 mã thông báo cho mỗi chuỗi

trong đợt này và chúng tôi sẽ đào tạo khoảng 500 mẫu.

Được rồi, vậy thì hãy xem, đây là vòng đào tạo chính.

Vì vậy, chúng tôi lặp lại 500 mẫu.

Ở đây, tất cả mã ở đây chỉ để đào tạo Alice,

Và tất cả đoạn code ở đây chỉ dành cho việc đào tạo Edgar.

Vì vậy, ở đây tôi đang tạo một loạt mã thông báo ngẫu nhiên

từ thẻ Alice.

Hai dòng mã này bạn đã thấy nhiều lần trước đây

ở phần trước,

và bạn sẽ tiếp tục gặp họ nhiều lần

trong phần này là tốt.

Được rồi, loại bỏ độ dốc, chạy chuyển tiếp.

Vì đây cũng là những người mẫu ôm mặt,

chúng ta không cần một hàm mất mát riêng biệt,

giống như với GPT-2 từ OpenAI.

Tất cả những gì bạn phải làm là cung cấp thông tin đầu vào tùy chọn này

có nghĩa là nhãn bằng X,

và bên trong, Ôm Mặt sẽ tạo ra

các giá trị mục tiêu dựa trên việc dịch chuyển các mã thông báo này từng cái một,

rồi tính toán tổn thất,

khả năng mất nhật ký âm,

và đưa nó ra trong phần Outputs.loss ở đây.

Được rồi, sau đó quay lại, chạy qua trình tối ưu hóa

và lưu trữ các khoản lỗ.

Mã này ở đây giống hệt với mã Alice,

tất nhiên, ngoại trừ tất cả, vâng,

ở mọi nơi tôi nhắc đến Alice,

mã thông báo hoặc mô hình hiện được thay thế bởi Edgar.

Đây là một thiết lập rất thú vị

bởi vì hai mô hình này bắt đầu

hoàn toàn giống hệt nhau,

nhưng bây giờ chúng tôi đang tinh chỉnh chúng

dựa trên một tập dữ liệu khác.

Được rồi, bây giờ tôi sẽ chạy cái này,

mất vài phút, không lâu lắm.

Vậy là mất khoảng ba phút

và bạn có thể thấy sự mất mát bắt đầu

về cơ bản là giống hệt nhau,

2,61 đến 2,60,

nhưng hơi khác một chút khi họ rơi xuống.

Vì vậy Alice đã giảm xuống còn 0,19

và Edgar chỉ tụt xuống 1,46.

Chúng ta có thể hình dung điều đó ở đây, mã vẽ đồ thị rất đơn giản.

Và bạn thấy cả hai đều từ chối,

nhưng cuốn sách của Alice lại rớt nhiều hơn thế.

Một lần nữa, tại sao lại như vậy?

Có một vài lý do.

Tôi nghĩ cuốn sách của Alice là,

trước hết, nó đồng nhất hơn một chút,

vì thế việc học sẽ nhanh hơn một chút.

Đồng nhất về văn phong và nội dung,

trong khi cuốn sách của Edgar, như tôi đã đề cập,

thực ra là một tập hợp của nhiều thứ,

và nó lớn hơn,

nên nó sẽ không đồng nhất hơn một chút.

Ngoài ra, nếu bạn đọc qua hai cuốn sách này,

đọc qua một số văn bản từ hai cuốn sách này,

bạn sẽ thấy phong cách viết của Edgar Allan Poe

khác biệt hơn rất nhiều so với Internet hiện đại.

Vậy hãy nghĩ về Wikipedia, các bài báo,

Reddit, Twitter, những thứ tương tự,

trong đó có rất nhiều văn bản có sẵn công khai.

Và sau đó cả hai cuốn sách này đều không

thực sự nghe giống như một bài viết trên Wikipedia,

nhưng cuốn sách của Alice thì kiểu như vậy,

ngôn ngữ gần hơn một chút với tiếng Anh hiện đại

so với phong cách viết của Edgar Allan Poe.

Được rồi, đó là một đánh giá định lượng.

Nhưng ở đây một lần nữa, chúng ta có thể hỏi cái nào tốt hơn?

Có phải tốt hơn là tổn thất ở đây thấp hơn?

Nếu đây là độ chính xác của việc phân loại

và chúng tôi đã có câu trả lời đúng,

thì tất nhiên tổn thất thấp hơn là tốt hơn.

Nhưng khi nói đến các mô hình sáng tạo,

thật sự rất khó để diễn giải những con số này.

bạn không nhất thiết muốn một mô hình có mức suy hao thấp như vậy

bởi vì tổn thất thấp này có nghĩa là mô hình

thực sự rất thích ứng với văn bản Alice ở xứ sở thần tiên,

đó không nhất thiết là thứ chúng ta mong muốn.

Được rồi, vậy hãy làm một đánh giá định tính.

Ở đây tôi tạo lời nhắc này,

Nữ hoàng Đỏ đã nói gì với Alice?

Và đó là lời nhắc mà tôi đưa ra

mô hình Alice và mô hình Edgar,

cả hai sẽ tạo ra tổng cộng tối đa 120 mã thông báo.

Trên thực tế, đây là khoảng 10.

Vì vậy, khoảng 100 token.

Và nó sẽ là một mẫu ngẫu nhiên,

có nghĩa là mỗi lần tôi chạy đoạn mã này,

nó sẽ trông hơi khác một chút.

Tuy nhiên, nó luôn có điều gì đó thú vị.

Vì vậy, đây là văn bản của tôi mà tôi đã nhập.

Và đây là những gì mô hình Alice đã trả lời.

Cô ấy nói, đừng xấc xược.

Tôi không biết bạn bị thuyết phục bởi điều gì,

nhưng hãy nói điều gì đó ở bên cạnh.

Được rồi, rõ ràng là mô hình này hiểu được điều gì đó về văn bản.

Nó đề cập đến việc Alice đang sử dụng dấu ngoặc kép.

Có rất nhiều đoạn hội thoại trong văn bản

và nữ hoàng thở hổn hển bước đi và cứ thế.

Được rồi, và đây là phiên bản của Edgar Allan Poe.

Tôi rùng mình khi nhìn thấy chính xác trạng thái giọng nói của cô ấy.

Tạm biệt.

Và tôi đã lao đầu vào một cơn ác mộng vô tận.

Ý tôi là, đây là nét đặc trưng của Poe.

Trời tối quá.

Thật đáng lo ngại.

Khi tôi ngồi bận rộn như thế, một ý nghĩ chợt đến với tôi

rằng người quen của tôi đã trở nên thân thiết.

Được rồi, điều này rõ ràng là khác biệt

đây là phong cách của Through the Looking Glass,

và đây là phong cách viết của Edgar Allan Poe.

Và cảm giác chất lượng mà bạn không có được

chỉ từ việc nhìn vào những dòng này ở đây

và nhìn vào những con số này ở đây.

Vì vậy, đánh giá định lượng này là tốt,

đó là thứ bạn nên xem xét,

nhưng nó không bao giờ thực sự nắm bắt được những gì bạn muốn hiểu

về các mô hình sáng tạo.

Đó là chủ đề mà bạn sẽ thấy xuyên suốt phần này.

Bạn biết đấy, có rất nhiều mô hình được đào tạo trước thực sự tuyệt vời mà bạn có thể tải xuống và điều chỉnh và

khám phá.

Điều quan trọng là phải hiểu kiến trúc và thuật toán được nhúng trong LLM vì khác nhau

mô hình từ các công ty khác nhau có quy ước đặt tên hoặc tổ chức hơi khác nhau.

Bây giờ, hầu hết thời gian trong khóa học này, chúng ta sẽ sử dụng các mô hình tương đối nhỏ chỉ vì

họ nhập khẩu và đào tạo dễ dàng hơn và nhanh hơn. Nhưng một khi bạn nắm được các nguyên tắc, bạn có thể bắt đầu

tải xuống các mô hình lớn hơn nhiều với hàng tỷ thông số thay vì hàng triệu.