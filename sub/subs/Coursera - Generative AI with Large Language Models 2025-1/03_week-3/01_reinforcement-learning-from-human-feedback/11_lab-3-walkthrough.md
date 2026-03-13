# 11 lab-3-hướng dẫn

---

Bài học về RLHF này được giới thiệu

rất nhiều thuật ngữ và khái niệm mới.

Đồng nghiệp của tôi Chris đã đưa

cùng nhau tạo nên một phòng thí nghiệm thú vị

thực hiện những gì bạn

được khám phá trong những video này.

Vì vậy, để làm bẩn tay bạn với RLHF,

Tôi sẽ đưa nó cho Chris bước đi

bạn qua cuốn sổ ghi chép của tuần này.

>> Này, cảm ơn Ancha, và

bây giờ là lúc dành cho Lab 3.

Được rồi, chào mừng mọi người trở lại,

chúng ta sẽ nói về Phòng thí nghiệm 3.

Phòng thí nghiệm 3 là một trong những phòng tôi yêu thích nhất.

Đây là nơi chúng tôi bắt tay vào thực hiện

với việc học tăng cường và

phản hồi của con người, hoặc RLHF.

Mục đích của phòng thí nghiệm này là để giảm

sự độc hại trong hướng dẫn của chúng tôi

mô hình tinh chỉnh từ Lab 2,

đó là kết quả của Lab 2.

Đó sẽ là đầu vào cho Lab 3 ở đây.

Và chúng tôi sẽ giảm độc tính

sử dụng phần thưởng cho lời nói căm thù

mô hình mà chúng tôi muốn tối ưu hóa cho

không ghét.

Chúng tôi sẽ sử dụng PPO mà bạn đã tìm hiểu

trong bài học và chúng ta sẽ tóm tắt mọi thứ

lên với số lượng và sau đó là chất lượng

so sánh quá trình giải độc của chúng tôi.

Được rồi, hãy cài đặt thư viện Python của chúng tôi.

Ở đây chúng ta thấy rằng chúng ta đang sử dụng PyTorch.

Chúng tôi cũng đang sử dụng máy biến áp tương tự

mà chúng tôi đã sử dụng trong phòng thí nghiệm trước đây,

tất nhiên, tập dữ liệu để có được

truy cập vào tập dữ liệu công khai của chúng tôi,

đánh giá như vậy

rằng chúng ta có thể chạy rouge_score.

Peft là tham số

thư viện tinh chỉnh hiệu quả.

Và đây là một thư viện mới có tên là trl.

Và đây là những gì đang diễn ra

để cấp cho chúng tôi quyền truy cập vào PPO.

Và một loại huấn luyện viên tương tự và

sau đó rèn luyện lập luận,

sẽ có PPOTrainer và

sau đó huấn luyện lập luận sau

quy ước khuôn mặt ôm của huấn luyện viên và

lập luận đào tạo.

Hãy thực hiện một loạt việc nhập khẩu của chúng ta ở đây.

Các lớp quen thuộc, AutoModelForSeq2Seq.

Lưu ý rằng có một cái mới ở đây,

đó là AutoModelForSeq1Classification.

Đây là những gì chúng ta sẽ sử dụng để

tải trình phân loại nhị phân Facebook của chúng tôi,

bộ phân loại seq1.

Khi chúng tôi cung cấp cho nó một chuỗi văn bản hoặc

một chuỗi văn bản,

nó sẽ cho chúng ta biết liệu có hay không

văn bản đó có chứa lời nói căm thù hay không,

với sự phân bố cụ thể

không ghét hay ghét.

Và tất nhiên, trong phòng thí nghiệm này,

chúng tôi sẽ tối ưu hóa để không ghét bỏ.

Ở đây chúng ta thấy Peft của chúng ta và

LoraConfig của chúng tôi mà chúng tôi đã thấy trong Lab 2.

Ở đây chúng ta thấy PPOtrainer cụ thể.

Ngoài ra còn có lớp khác,

Ngôn ngữ AutoModelForSeqtoSeq

mô hình với một đầu giá trị.

Đây là những gì được yêu cầu khi chúng tôi thực hiện PPO

huấn luyện mà chúng ta sẽ thấy sau đây.

Ngoài ra, LongSampler này.

Điều này sẽ cho chúng ta khả năng lọc hoặc

thực sự mẫu từ văn bản của chúng tôi khác nhau

độ dài, vì vậy chúng tôi thực sự không có

để kéo toàn bộ chuỗi,

chúng tôi chỉ có thể lấy các mẫu khác nhau.

Và điều này có ích khi chúng ta đang cố gắng

lấy mẫu từ tập dữ liệu đầy đủ của chúng tôi,

mặc dù nó vượt xa

cửa sổ ngữ cảnh 512.

Chúng tôi có thể muốn lấy mẫu lên tới 512.

Trong một số trường hợp,

bạn thực sự sẽ vứt đi

mẫu lớn hơn 512.

Ví dụ: với LongSampler,

chúng ta chỉ có thể lấy mẫu 512 đầu tiên hoặc

lấy mẫu theo trình tự,

có thể không bắt đầu từ đầu, nhưng

có thể ở giữa hoặc về phía cuối.

Và vì vậy, LongSampler khá hay.

Ở đây chúng ta thấy PyTorch, đánh giá.

Nếu bạn chưa từng thấy điều này trước tqdm,

đây là

thường ở đâu khi bạn thấy sự tiến bộ

các thanh hiển thị trong Notebook Jupyter hoặc

trên dòng lệnh của bạn,

chúng đến từ thư viện tqdm này.

Như trước đây,

chúng tôi sẽ tải tập dữ liệu của mình và

rồi cuối cùng mô hình của chúng tôi sẽ ở đây sau một giây nữa,

chúng tôi có dữ liệu xây dựng này

thiết lập hàm Python mà chúng tôi đã

được xác định có thể làm được chiều dài

lấy mẫu bằng cách sử dụng lengthSampler đó

đã được đề cập ở trên,

cũng có thể chuyển đổi văn bản của chúng tôi thành những

vectơ, còn được gọi là tokenizing.

Vì vậy, đây là nơi chúng ta bắt đầu thấy một chút

phức tạp hơn một chút trong mã của chúng tôi.

Một vài phòng thí nghiệm đầu tiên

chúng tôi vẫn khá đơn giản.

Phòng thí nghiệm 3, chúng ta bắt đầu làm một chút

thêm một chút nội dung kiểu Pythonic.

Chúng tôi có các hàm lồng nhau ở đây để mã hóa.

Chúng tôi đang bắt đầu kết hợp mọi thứ

thành các chức năng đơn lẻ và

chúng ta sẽ chỉ nói

xây dựng tập dữ liệu ở đây.

Chúng tôi sẽ đặt cho nó tên model.

Chúng ta cần tên model để biết cái nào

tokenizer để sử dụng, bởi vì một lần nữa,

mỗi mẫu này đều có

mã thông báo của riêng họ.

Nếu bạn cố gắng trộn và kết hợp các mã thông báo

giữa các loại mô hình khác nhau,

điều đó không tốt, và

bạn sẽ thấy một số kết quả khá tệ.

Một tính năng khác của bản dựng này

chức năng tập dữ liệu là chúng tôi

sắp kết thúc tập dữ liệu của chúng tôi

vào lời nhắc hướng dẫn này.

Vì vậy đây là điều chúng tôi đã làm

trong phòng thí nghiệm thứ nhất và thứ hai.

Vì vậy, chúng tôi đang kết hợp tất cả

thành một chức năng duy nhất ở đây.

Bây giờ đây là mô hình mà chúng tôi

được đào tạo ở phòng thí nghiệm thứ hai.

Vì vậy tôi đang lấy nó từ bộ lưu trữ đám mây ở đây.

Chúng tôi kéo nó xuống và

nó phải ở trong một thư mục ở đây có tên là

peft-hộp thoại-tóm tắt-điểm kiểm tra, chúng ta hãy

hãy mở nó ra chỉ để xem.

Đây là adapter_model.bin.

Một lần nữa, đó là vấn đề,

đó chỉ là 14 megabyte.

Và đây là số in tiện dụng của chúng tôi về

chức năng tham số mô hình có thể huấn luyện được

thỉnh thoảng chúng tôi sẽ sử dụng để có được

ưa thích và xem khi nào chúng tôi đang sử dụng peft.

Trong toàn bộ phòng thí nghiệm này,

chúng tôi sẽ sử dụng peft.

Vì vậy phần lớn,

chúng ta sẽ chỉ đào tạo và

tinh chỉnh rất nhỏ

phần trăm kích thước mô hình của chúng tôi.

Vì vậy, ở đây một lần nữa, 1,4%.

Bây giờ đây là nơi chúng ta phải sử dụng cái này

biến thể của AutoModelForSeq2SeqLM,

đó là với ValueHead.

Vì vậy, điều này có liên quan đến cách PPO

thực sự thực hiện việc đào tạo của nó.

Và đây, nhân tiện, để cho rõ ràng,

chúng tôi nói is_trainable bằng True.

Và đó là mục đích của chúng tôi bởi vì chúng tôi

thực sự đang đưa mô hình vào

mô hình tinh chỉnh.

Và sau này khi chúng tôi

đi đưa ra dự đoán và

để tạo ra các bản tóm tắt,

chúng tôi sẽ đặt nó thành sai.

Vì vậy nếu bạn để ý con số này là một chút

cao hơn một chút so với ở phòng thí nghiệm 2.

Và nó cao hơn chính xác 769 thông số.

Và thế là

hãy để tôi giải thích những gì đang xảy ra ở đó.

768 trong số đó

là từ ValueHead.

Trên thực tế, tất cả 769 đều đến từ ValueHead.

Đó là 768, là kích thước

của ValueHead cộng với sự thiên vị của chúng tôi.

Và sự thiên vị là rất quan trọng,

Nhân tiện, vì nó luôn ở đó,

mọi người có xu hướng không bao gồm

nó trong những cuộc trò chuyện thông thường của họ.

Bây giờ, tôi đã bỏ qua điều này

tạo mô hình tham khảo

Điều này thực sự đến từ TRL.

Chúng tôi đã nhập cái này ở trên.

Và điều này đang làm là,

như các em đã học trong bài

khi chúng tôi thực hiện RLHF, bạn có thể chỉ định

một mô hình cơ sở được sử dụng với KL

phân kỳ để đảm bảo rằng trong khi

chức năng phần thưởng đang được tối ưu hóa,

đúng rồi, trong khi chúng tôi đang tối ưu hóa

để tối đa hóa phần thưởng,

trong trường hợp này không phải là lời nói căm thù.

Chúng tôi không muốn chỉ

hack phần thưởng đó một cách điên cuồng và

chỉ tạo ra những thứ không phải là sự căm ghét,

nhưng điều đó không liên quan đến bản gốc.

Nói cách khác, khi chúng ta đi tàu,

chúng ta sẽ chuyển qua hai mô hình,

cái được gọi là mô hình tham chiếu,

đó là một mô hình sẽ không trở thành

tinh chỉnh chút nào, thậm chí không với peft.

Nó chỉ là bản gốc

hướng dẫn tinh chỉnh mô hình

đó là kết quả của Phòng thí nghiệm 2,

đó hiện là đầu vào cho Lab 3.

Và sau đó phân kỳ KL được sử dụng để

so sánh mô hình ban đầu sẽ như thế nào

đã tạo ra so với những gì sẽ

mô hình PPO hiện tại đã tạo ra và

sau đó sắp xếp mọi thứ

xếp hàng theo cách đó và

sau đó giảm thiểu khả năng của mô hình

để thực hiện việc hack phần thưởng.

Vì vậy, chúng ta sẽ thấy nó ở đây một chút.

Đây thực sự là nơi chúng tôi sẽ tải,

cái mà tôi gọi là mô hình độc tính.

Một lần nữa, điều này đến từ Facebook.

Nó được thiết kế để phát hiện lời nói căm thù,

nó dựa trên Bert.

Facebook có một biến thể

của Bert tên là Roberta.

Vậy mẫu này có giá hàng triệu

của các tham số, không phải ở hàng tỷ và

tỷ như ngôn ngữ lớn

những mô hình mà chúng ta có ngày nay.

Bây giờ mô hình đó đã được tải, vậy nên một lần nữa,

đây là nơi chúng tôi sử dụng mô hình ô tô cho

phân loại trình tự.

Vì vậy, đây là một bộ phân loại.

Trong trường hợp này, chỉ có hai nhãn và

đó là điều sẽ biến cái này thành nhị phân

phân loại, đó không phải là ghét hay ghét.

Và chúng ta sẽ thấy điều đó được thực hiện ở đây.

Đây là một mẫu văn bản không độc hại.

Tôi muốn hôn em,

đoạn văn bản khá thân thiện ở đây.

Và chúng tôi thấy những cách khác nhau mà điều này

mô hình thực sự có thể tạo ra đầu ra cho

văn bản này,

thực sự có thể phân loại văn bản này.

Chỉ biết rằng vị trí đầu tiên,

điều quan trọng nhất là điều đầu tiên

khe cắm mà mô hình này có thể tạo ra.

Hạng nhất không phải là ghét, và

điều đó trở nên rất quan trọng.

Ghét ở vị trí thứ hai,

chỉ mục bên phải hoặc 0, đó là chỉ mục đầu tiên.

Vậy chỉ số 0 không phải là ghét,

chỉ số đầu tiên, chỉ số 1 là ghét.

Và chúng tôi thấy rằng không ghét là rất cao.

Vậy đây là nhật ký phải không?

Tất nhiên, chúng ta cũng có thể

thực hiện mức tối đa mềm trên các nhật ký đó và

chúng ta thấy rằng xác suất của

văn bản này không độc hại hoặc

không ghét, về cơ bản là 100%.

Xác suất mà mô hình này là hoặc

rằng văn bản này là sự căm ghét rất gần với 0.

Trong khóa đào tạo PPO của chúng tôi,

chúng tôi thực sự sẽ sử dụng logit và

nó rất quan trọng để

lấy chỉ số đúng.

Và tôi nói điều này bởi vì nếu bạn

vô tình tối ưu hóa cho

chỉ mục sai, bạn thực sự có thể

tạo ra văn bản độc hại hơn,

đó không phải là những gì chúng ta đang có

cố gắng làm ở đây ngày hôm nay.

Và một điều tôi đã thực sự làm để

làm cho điều này rõ ràng hơn là tôi gọi ra

chỉ số không ghét bằng 0.

Và lý do khiến điều này khó hiểu là

trong nhiều trường hợp, kiểu tích cực

lớp đứng ở vị trí thứ hai và

lớp phủ định nằm ở số 0.

Và vì vậy nếu bạn đi và sao chép của người khác

mã hoặc bạn tìm thấy một ví dụ trực tuyến, hoặc

bạn có một người bạn giúp đỡ bạn, bạn có thể

vô tình làm xáo trộn chỉ mục nào.

Đây là một ví dụ về văn bản độc hại,

và bây giờ hãy ghi nhớ,

Tôi đã phải sử dụng một từ xấu

ở đây để thực sự kích hoạt điều này.

Và vì vậy hãy chạy nó ở đó.

Và ở đây chúng ta thấy 97, gần 97 và

xác suất nửa phần trăm là

đây là lời nói độc hại hoặc căm thù.

Bây giờ lời nói căm thù là cực đoan.

Và vì vậy tôi thận trọng,

nếu bạn thử làm theo ví dụ này,

mà đôi khi bạn phải như vậy

cực đoan để kích hoạt cờ căm thù.

Vậy tin tốt là chúng tôi hiện không tối ưu hóa

đối với cờ thù địch, chúng tôi đang tối ưu hóa cho

cờ không ghét, vì vậy chúng ta hãy tiếp tục.

Một điều chúng tôi chưa

được thể hiện nhiều trong các phòng thí nghiệm này

cái được gọi là ôm

đối mặt với đường dẫn suy luận.

Và vì vậy cái này được nhập lên phía trên,

cái này đã được nhập khẩu.

Và ở đây chúng tôi đang tạo ra những gì

được gọi là đường dẫn cảm xúc.

Và giá trị thực sự của chúng

ôm mặt ống dẫn,

đây là từ thư viện máy biến áp.

Giá trị thực sự là tôi chỉ có thể nói điều này

là một vấn đề phân tích tình cảm,

về cơ bản là 0, hoặc xin lỗi, hai lớp.

Và tôi đặt tên cho mô hình của tôi và

thì tôi có thể sử dụng cái này.

Và tôi không phải gọi tất cả những thứ đó

model.generate cấp thấp và

làm mã thông báo và tất cả những thứ đó,

điều này thực sự sẽ làm tất cả cho chúng tôi.

Một lần nữa, chúng tôi đã không sử dụng những thứ này

ở phòng thí nghiệm thứ nhất và thứ hai,

chúng tôi đang sử dụng nó ở đây chỉ để giảm bớt

sự phức tạp của phòng thí nghiệm này và

thực sự, thực sự tập trung vào phần RL của nó.

Nhưng tôi muốn cho bạn thấy rằng có

những thứ này có được gọi là suy luận không

đường ống, và chúng rất, rất tiện dụng.

Bạn có thể trộn và

phù hợp như chúng tôi đang làm trong phòng thí nghiệm này.

Đôi khi bạn có thể sử dụng chúng,

đôi khi bạn không cần phải sử dụng chúng.

Ở đây chúng tôi đang thiết lập

cơ chế đánh giá độc tính

Và chúng ta sẽ tái sử dụng

thư viện Đánh giá Python

có lớp học đầu tiên

kiến thức về độc tính.

Và tất nhiên, khi chúng tôi thiết lập điều này,

chúng ta phải cung cấp cho nó mô hình độc tính,

trong trường hợp này chúng tôi đang sử dụng

Facebook RoBERTa mô hình lời nói căm thù.

Điều thú vị khác là

chúng ta phải chuyển nhãn chất độc hại.

Trong trường hợp này, nhãn độc hại là sự ghét bỏ.

Và chúng tôi sẽ sử dụng công cụ đánh giá này

sau này khi chúng ta so sánh trước và

sau đó sau PPO, lực lượng tăng cường của chúng tôi

học tập với sự phản hồi của con người.

Ở đây chúng ta thấy văn bản không độc hại mà chúng ta

được chỉ định ở trên, tôi muốn hôn bạn và

văn bản độc hại, chúng ta thấy rằng những điểm số này

phù hợp với những gì chúng ta mong đợi.

Đây là một chức năng tiện lợi nơi chúng tôi

truyền vào mô hình, truyền vào tập dữ liệu.

Chúng ta thậm chí có thể cho nó biết số

mẫu để thử và

để tính toán độc tính trung bình

cho điểm theo tiêu chuẩn

độ lệch cho

cả đống tóm tắt đó

được tạo ra hãy cho chúng tôi biết điều gì

là điểm độc tính trung bình.

Và vì vậy mục tiêu là giảm giá trị trung bình

điểm độc tính sau khi chúng tôi thực hiện PPO.

Và ở đây chúng ta thấy ý nghĩa và

độc tính độ lệch chuẩn là trước

chúng tôi thực hiện quá trình giải độc để giảm

tính độc hại của những bản tóm tắt do chúng tôi tạo ra.

Ở đây chúng ta sẽ

khởi tạo PPOtrainer.

Chúng tôi cũng có PPOConfig.

Đây thực sự chỉ là sắp xếp

về tỷ lệ học tập tiêu chuẩn.

Chúng tôi đang làm một việc nhỏ

số lượng sử thi PPO.

Một lần nữa, chỉ để giữ thời gian cho

phòng thí nghiệm này xuống một con số hợp lý.

Batch_size, đây, 16, không tệ lắm.

Và bạn thực sự có thể chơi với một số

những giá trị này khi bạn vào phòng thí nghiệm.

Ở đây chúng ta thấy PPOtrainer

lấy mô hình tham chiếu.

Vì vậy, điều này chúng tôi đã sử dụng hết ở trên khi chúng tôi

được gọi là mô hình Create_Reference.

Và đó thực chất là bản gốc

mô hình là đầu ra của Phòng thí nghiệm 2.

Và đó là những gì sẽ được sử dụng cho

KL phân kỳ trong quá trình đào tạo PPO.

Bây giờ chúng tôi thực sự tinh chỉnh

mô hình sử dụng RLHF

Đây là phần thú vị.

Và ở đây chúng ta thấy kl phân kỳ,

đó là điều chúng tôi muốn giảm thiểu,

giống như bạn đã học trong bài.

Chúng tôi không muốn sự phân kỳ KL xảy ra

quá cao, điều đó có nghĩa là mô hình

bắt đầu hack chức năng phần thưởng,

và điều đó không tốt.

Nó chỉ tạo ra những thứ

để làm cho phần thưởng vui vẻ,

nó không tạo ra những thứ

thực sự giống với văn bản gốc

điều đó đang được chuyển vào để tóm tắt.

Và chúng tôi đang cố gắng

tối đa hóa lợi nhuận trung bình.

Đây là một số chất tăng cường PPO

học các khái niệm mà bạn đã học

trong các slide.

Phát huy tối đa lợi thế và

việc này sẽ chạy trong khoảng 20 phút hoặc lâu hơn.

Vậy hãy đi lấy một tách cà phê.

Và những gì đang xảy ra ở đây là,

chúng tôi đang nắm lấy từng cái

các mẫu mà chúng tôi cung cấp

từ tập dữ liệu hộp thoại của chúng tôi và

chúng tôi đang tóm tắt văn bản.

Chúng tôi đang sử dụng quy trình cảm tính mà chúng tôi

được tạo ở trên sẽ phân loại

cả những gì được gọi là truy vấn, đó là

lời nhắc và câu trả lời cùng nhau.

Vì vậy chúng ta sẽ nén hai cái đó lại

cùng nhau bằng cách sử dụng zip python.

Và chúng tôi có phản hồi truy vấn, chúng tôi

sẽ chuyển cặp đó vào

đường dẫn tình cảm và

hỏi đường ống, cái này có độc không?

Đây là ghét hay đây không phải là ghét?

Điều đó sau đó cung cấp cho chúng tôi nhật ký cho

các cặp phản hồi truy vấn đó.

Chúng tôi sẽ rút ra

điểm not_hate và

chúng ta sẽ vượt qua tất cả

cái này vào PPOtrainer.

Vì vậy chúng tôi sẽ đưa ra lời nhắc,

chúng ta sẽ đưa ra phản hồi hoặc

tóm tắt và

chúng ta sẽ cho nó điểm số.

Tất cả ba thứ đó đều được liệt kê dưới dạng danh sách,

theo từng đợt vào PPOTrainer của chúng tôi.

Sau đó sẽ thực hiện PPO

bước để giảm thiểu hàm mất mát

như bạn đã thấy trong các slide.

Và đây là nơi thực tế

gradient đang được cập nhật.

Và bây giờ hãy ghi nhớ

rằng chúng tôi đang sử dụng peft.

Và vì vậy chúng tôi không thực sự sửa đổi

peft tham số LOM cơ sở,

chúng tôi chỉ đang sửa đổi

bộ chuyển đổi lorapeft 1,4%

đang được sử dụng trong thời gian

quá trình tinh chỉnh này.

Và chúng ta sẽ chạy nó một chút.

Chúng tôi thấy sự phân kỳ của KL tương đối ổn định,

vào khoảng 27, 28, 29.

Nó đi lên, nó đi xuống,

đó là PPO đang cố gắng giữ mọi thứ cân bằng.

Và một khi việc này được thực hiện,

chúng ta sẽ so sánh mô hình một cách định lượng

cũng như chất lượng.

Sau khoảng 10 lần lặp, chúng ta có thể so sánh

mô hình đã được giải độc,

hoặc đã giảm độc tính như

so với mô hình ban đầu.

Và ở đây chúng tôi có thể làm điều này một cách chất lượng

bằng cách so sánh trước đó

phản hồi lại phản hồi sau.

Vì vậy ở đây chúng ta thấy rằng phần thưởng có

thực sự đã tăng lên ở một số

trường hợp của những ví dụ này.

Vì vậy, truy vấn là văn bản gốc

mà chúng tôi muốn tóm tắt,

cuộc trò chuyện ban đầu đã kết thúc

trong lời nhắc hướng dẫn đó và

chúng ta thấy phản hồi trước đó,

chúng tôi thấy phản hồi sau đó.

Và chúng ta thấy rằng mô hình có

xác định rằng mô hình khen thưởng,

mô hình lời nói căm thù đã xác định rằng

phần thưởng thực sự là nhiều hơn

tích cực trong một số trong số này.

Nếu bạn tập luyện lâu hơn và

có nhiều thời gian hơn,

bạn sẽ thấy điều này tương đối

sự khác biệt đáng kể.

Điều khác cần đề cập là,

bởi vì mô hình khen thưởng quá cực đoan,

điều đó thực sự để có được lợi ích lớn nhất,

bạn sẽ bắt đầu với một tương đối

tập dữ liệu độc hại, đây không phải là

một tập dữ liệu tương đối độc hại và

thì bạn sẽ thấy nhiều

sự khác biệt lớn hơn.

Nhưng ở đây chúng ta thấy có hướng

bằng cách thực hiện PPO và

sử dụng chức năng khen thưởng

chúng tôi đang sử dụng mô hình phần thưởng cho

lời nói căm thù,

rằng chúng ta thực sự có thể hạ thấp tổng thể

độc tính của mô hình của chúng tôi

phản hồi với số lượng vừa phải.