# 2 -Tinh chỉnh GPT2 đã được huấn luyện trước

---

Hầu hết video này là bản demo Python.

Điểm chính là cung cấp một số mã và cũng trình bày cách tinh chỉnh hoạt động trong

PyTorch.

Như tôi đã đề cập ở video trước, việc tinh chỉnh không khác gì việc đào tạo trước trong

về cấu trúc và cách thiết lập mã.

Có một vài khác biệt nhỏ mà tôi sẽ thảo luận trong mã, nhưng nhìn chung nó khá đẹp

giống nhau nhiều. Và tôi cũng sẽ bắt đầu giới thiệu cho bạn một số phím tắt mà tôi chưa sử dụng

được sử dụng trong phần trước vì tôi thực sự muốn mã dài hơn một chút để tạo

chắc chắn rằng mọi việc chúng tôi đang làm đều rõ ràng. Khi bạn đã hiểu cách huấn luyện một người mẫu thì thật tuyệt vời.

hữu ích khi có một số phím tắt giúp bạn tiết kiệm thời gian và dòng mã. Dù sao thì mục tiêu chính của

việc tinh chỉnh ở đây sẽ là nhập

mô hình cơ sở từ GPT được đào tạo trước

và tinh chỉnh nó trên văn bản của Gulliver's Travels.

Và ý tưởng là chúng ta không đào tạo

một mô hình ngẫu nhiên từ đầu,

nhưng thay vào đó lấy một mô hình được đào tạo hiện có

và huấn luyện nó có một sở thích nhỏ

để viết văn bản trông giống như Những chuyến du hành của Gulliver.

Vì vậy đây là những gì chúng tôi sẽ làm.

Chúng ta sẽ bắt đầu bằng cách nhập nội dung cuốn Những chuyến du hành của Gulliver và tôi sẽ thảo luận về một số vấn đề khác nhau.

cách sử dụng mã thông báo dễ dàng hơn một chút so với những gì chúng tôi đang làm trong

phần trước, mặc dù kết quả thực tế sẽ khác ở một số điểm

không tốt hơn hay tệ hơn, nhưng có điều gì đó quan trọng cần biết.

chúng ta sẽ tìm những token thường được sử dụng trong Gulliver's Travels. Tôi sẽ được đào tạo trước

mô hình tạo ra một loạt văn bản mới và sau đó chúng tôi có thể đếm tần suất các mã thông báo xuất hiện trong

Cuốn sách Những chuyến du hành của Gulliver xuất hiện trong văn bản được tạo. Bây giờ trong trường hợp cụ thể này là khoảng 40%.

phần trăm. Khi tôi chỉ cho bạn những token thường xuyên nhất là gì, bạn sẽ không ngạc nhiên lắm.

ở số này. Các mã thông báo phổ biến bao gồm và và và dấu phẩy và dấu chấm, v.v. Nhưng

câu hỏi đặt ra là liệu con số này có tăng lên sau khi tinh chỉnh mô hình Gulliver's Travels hay không.

Đó là những gì chúng ta sẽ làm tiếp theo. Chúng tôi sẽ tinh chỉnh mô hình và tôi cũng sẽ cho bạn thấy rằng việc học

tỷ lệ mà tôi sử dụng nhỏ hơn một chút. Tôi sẽ chỉ cho bạn một phím tắt để tính độ mất ôm

các mô hình được cung cấp theo từng giai đoạn thực sự nhanh hơn và hiệu quả hơn cách chúng tôi đang có

mất mát ở phần trước. Ở đây bạn thấy sự mất mát trong việc tinh chỉnh và bạn có thể thấy rằng nó giảm mạnh

cho đến tận 0 hoặc ít nhất bạn biết một số nào đó gần bằng 0. Đó là

thấp hơn đáng kể so với bất kỳ tổn thất nào mà chúng tôi quan sát được ở phần trước, và đó là

hoàn toàn là do đây là một mô hình nền tảng được đào tạo trước thực sự tuyệt vời. tôi cũng sẽ

hãy thảo luận xem liệu điều này có phải là điều tốt hay không nếu chúng ta thực sự muốn tổn thất giảm xuống mức 0.

Và cuối cùng tôi sẽ chỉ cho bạn một vài lựa chọn khác nhau để đánh giá sự thành công

của việc tinh chỉnh.

Được rồi, hãy bắt đầu nào.

Dưới đây là một số thư viện mà chúng tôi sẽ sử dụng

và tất cả đều là những thư viện mà chúng tôi đã sử dụng trước đây

ở phần trước.

Ở đây tôi đang nhập mã thông báo GPT-2

và cả bản thân mô hình nữa.

Được rồi, đây là mô hình cơ sở được đào tạo trước từ OpenAI.

Chúng ta sẽ, hãy xem nào, đặt mọi thứ vào GPU,

đặc biệt là để đào tạo những mô hình này,

bạn không muốn sử dụng CPU.

CPU có thể chấp nhận được nếu bạn muốn thực hiện một vài lần chuyển tiếp

không có quá nhiều dữ liệu, nhưng để truyền ngược

và phải tập luyện rất nhiều, nó thực sự rất đau đớn

để chạy tất cả những thứ này trên CPU.

Ừ, vậy chúng ta sẽ có buổi huấn luyện

với kích thước lô có độ dài chuỗi 16 và 256,

dài hơn một chút so với độ dài chuỗi tám

mà chúng ta đã sử dụng ở phần trước.

Được rồi, để tôi chạy nó.

Ở đây tôi đang nhận được văn bản.

Được rồi, đây là cách chúng tôi mã hóa

văn bản ở phần trước.

Như bạn còn nhớ, tokenizer.encode,

và sau đó bạn nhập một chuỗi cho văn bản,

và đầu ra của hàm này là một danh sách các số nguyên.

Vì vậy, đó là một danh sách Python.

Tuy nhiên, để sử dụng các mã thông báo này trong mô hình PyTorch,

chúng tôi không thể nhập danh sách.

Chúng tôi cần nhập mã thông báo PyTorch, thang đo PyTorch.

Vì vậy, tôi đã sử dụng công cụ này để chuyển đổi sang tensor

và điều này để đảm bảo rằng chúng ta có được kiểu dữ liệu

torch.long, đây là cách viết số nguyên của Torch.

Được rồi, thế này là ổn.

Không có gì sai với điều đó.

Nhưng điều tôi sẽ chỉ cho bạn ở đây

và những gì chúng ta sẽ bắt đầu sử dụng trong tương lai

bản thân nó chỉ là chức năng tokenizer

và sau đó dấu phẩy trả về tensor bằng PT.

Bạn nghĩ PT là viết tắt của từ gì?

Tôi hy vọng bạn đoán được.

Nó là viết tắt của PyTorch.

Vậy điều đó có nghĩa là chức năng này

bây giờ sẽ không xuất ra danh sách,

mà thay vào đó là một tensor PyTorch.

Tuy nhiên, hãy để tôi thực sự chỉ cho bạn điều này.

Tuy nhiên, đầu ra của việc này là,

đó là kích thước này ở đây.

Được rồi, cái đầu tiên ở đây, cỡ đầu tiên này,

đó là kết quả của việc mã hóa để có được danh sách

và sau đó chuyển nó thành tensor PyTorch.

Và kích thước này ở đây tương ứng

đến dòng mã này ở đây.

Vậy đây là vector 1 x 160.000.

Đây là một chiều đơn lẻ.

Và về cơ bản điều này có nghĩa là PyTorch sẽ xử lý vấn đề này

như đầu vào hàng loạt.

Chúng tôi có một lô có độ dài một và 160.000 mã thông báo.

Bây giờ, đôi khi điều đó cũng ổn.

Và đôi khi điều đó sẽ gây ra một số nhầm lẫn

hay bị lỗi hay đau đầu.

Vì vậy, những gì tôi muốn cho các ứng dụng mà tôi sẽ sử dụng

không phải là có ma trận, tensor đa chiều,

nhưng thay vào đó chỉ có một dãy số không thứ nguyên,

giống như những gì tôi có ở đây.

Vì vậy, tôi chỉ truy cập vào hàng đầu tiên,

về cơ bản chỉ là giải nén tensor này.

Được rồi, đó là dành cho phím tắt đó.

Và hãy xem, được rồi, tôi đang tìm đây

100 token thường xuyên nhất trong Gulliver's Travels.

Điều này khá dễ thực hiện.

Tất cả những gì chúng ta cần làm là tìm những token duy nhất

và trả về số đếm bằng đúng.

Và sau đó chúng ta có thể sắp xếp chúng và tìm ra, vâng,

100 token phổ biến nhất đầu tiên trong cuốn sách này.

Và ở đây tôi có thể in chúng ra.

Vì vậy, bạn có thể thấy mã thông báo phổ biến nhất là mã thông báo 11,

chỉ số 11, xuất hiện 10.000 lần trong cuốn sách.

Và đó là dấu phẩy.

Dấu hiệu phổ biến tiếp theo là thứ trông buồn cười này,

đó là dòng mới phải không?

Vì vậy, đây là một ngắt dòng ở đây.

Và sau đó chúng ta có the, of, và, v.v.

Và bạn có thể thấy rằng đây không phải là những token cụ thể.

Chúng thực sự xuất hiện trong rất nhiều văn bản và ngôn ngữ tiếng Anh.

Một số trong số này là một số ký tự định dạng,

nhưng vâng, nhìn chung, những thứ này không thực sự độc đáo

về chuyến đi của Gulliver.

Được rồi, và đó là lý do tại sao nó không có gì đáng ngạc nhiên

rằng chúng tôi nhận được khoảng 40% số token được tạo

từ GPT-2 đã được huấn luyện trước khi tinh chỉnh

trên Gulliver's Travels để bao gồm các mã thông báo này.

Được rồi, ở đây tôi đã đẩy mô hình lên GPU.

Được rồi, ở đây tôi chỉ đang tạo một số văn bản

chỉ để cho bạn thấy rằng chúng tôi có thể đạt được kết quả hợp lý

từ GPT-2.

Vì vậy, chúng tôi bắt đầu với một lời nhắc, tôi không thể tin được điều đó.

Và hãy xem GPT-2 hoàn thành nó như thế nào.

Tôi không thể tin được điều đó.

Bây giờ đây là văn bản mà tôi đưa vào.

Đây là lời nhắc đầu vào.

Họ muốn dành một năm ở chỗ bạn

và khiến bạn cảm thấy không được chào đón.

Rất thô lỗ, rất không hiếu khách.

Được rồi, hãy xem nào.

Bây giờ những gì tôi muốn, đó chỉ là một bản demo nhỏ.

Bây giờ điều tôi muốn làm là điều gì đó nghiêm ngặt hơn một chút,

một cái gì đó định lượng hơn một chút.

Và điều tôi sắp làm là tạo ra một loạt token

rồi đếm xem có bao nhiêu token

rằng mẫu GPT-2 được đào tạo trước này có trong danh sách

trong số 100 token thường xuyên nhất trong Gulliver's Travels.

Được rồi, đó là mục tiêu.

Bây giờ bạn đã thấy phương thức tạo này trước đây.

Thông thường bạn đã nhìn thấy nó một cái gì đó,

bạn biết đấy, hãy sử dụng nó như thế này,

nơi tôi chỉ nói, tạo ra và sau đó chúng tôi nhập một số mã thông báo,

có thể một vài đầu vào khác.

Tôi sẽ có toàn bộ video

trong một vài video bây giờ.

Đây không phải là video tiếp theo mà là video tiếp theo

đó là tất cả về toàn bộ video.

Nó chỉ tập trung vào các thông số

để sử dụng phương pháp tạo này.

Để biết thêm về tất cả những thứ này sau,

nhưng chỉ cần nói rằng, ý tưởng ở đây là chúng ta đang bắt đầu

tắt các mã thông báo này.

Và ở đây tôi đang thiết lập độ dài tối đa

và độ dài tối thiểu.

Đây là các tham số tùy chọn giống nhau,

đó là số lượng mã thông báo cộng với một.

Tôi sẽ giải thích lý do tại sao tôi cộng một ngay sau đây.

Làm mẫu bạn đã thấy trước đây.

Điều này đảm bảo rằng chúng tôi nhận được phản hồi được tạo ngẫu nhiên.

Đây, đây là ID từ xấu.

Đây là danh sách mã thông báo mà tôi muốn GPT sử dụng,

hoặc bất kỳ mô hình nào mà chúng tôi đang tạo ra,

để tránh phát sinh.

Và tại sao tôi muốn tránh tạo ra

mã thông báo cụ thể này, mã thông báo kết thúc chuỗi?

Vâng, khi mô hình quyết định

rằng nó đã sản xuất đủ token,

sau đó nó sẽ tạo ra token EOS,

và điều đó chỉ dừng lại thế hệ,

điều đó đóng cửa thế hệ.

Và có thể điều đó xảy ra sau ba hoặc bốn mã thông báo.

Hãy tưởng tượng bạn đang trò chuyện bằng trò chuyện GPT,

bạn hỏi một câu hỏi có hoặc không rất đơn giản

và GPT trả lời có, đó là tất cả những gì tôi phải nói.

Và thế là kết thúc cuộc trò chuyện.

Vậy điều đã xảy ra là GPT đã tạo ra token EOS

và điều đó được coi là một tín hiệu

chỉ để ngừng tạo thêm mã thông báo.

Bây giờ đối với một bot trò chuyện thực sự thì ổn thôi.

bạn muốn nó có khả năng đó.

Nhưng đối với ứng dụng cụ thể này,

chúng tôi thực sự không muốn điều đó.

Chúng tôi muốn mô hình tiếp tục tạo mã thông báo

để định lượng số lượng token mà nó tạo ra

từ cuốn sách này Những chuyến du hành của Gulliver.

Được rồi, đó là lý do tại sao tôi có nó ở đây.

Và sau đó, mã thông báo pad là mã thông báo được sử dụng để đệm

độ dài chuỗi không bằng nhau.

Thực ra, chúng tôi không thực sự cần điều đó ở đây,

nhưng tôi đang đưa nó vào đây

chỉ để tránh nhận được tin nhắn cảnh báo.

Tôi cũng sẽ nói nhiều hơn về điều này trong một vài video.

Được rồi, đó là chi tiết hơn một chút

về phương pháp tạo.

Và đây là điểm bắt đầu ngẫu nhiên.

Vì vậy điểm bắt đầu ngẫu nhiên

theo nghĩa đen là số nguyên ngẫu nhiên có kích thước,

rất khác nhau giữa số 0 và kích thước từ vựng.

Và số lượng số nguyên hoặc kích thước của ma trận này

là số lần lặp lại bằng một, trong đó số lần lặp lại là 10.

và một.

Vì vậy, điều này sẽ tạo ra 10 đợt một mã thông báo.

Tôi có thể cho bạn xem hình dạng của cái này.

Được rồi, tôi chưa chạy cái này.

Hãy để tôi sao chép cái này và dán nó vào đây.

Được rồi, đây là tensor 10 x 1.

Đó là những gì tôi đang nhập vào GPT2.generate.

Vì vậy, về cơ bản điều này sẽ tạo ra 10 chuỗi

bắt đầu bằng bất kỳ số nguyên ngẫu nhiên nào

đây là những Và được rồi, bây giờ tôi đang xác định rằng đầu ra

chiều dài sẽ là 100. Nhưng như bạn đã thấy ở trên, và bạn

cũng thấy rằng, bất cứ khi nào chúng ta sử dụng phương thức tạo này trước đây,

phần đầu của đầu ra của phương thức tạo là sự lặp lại của

mã thông báo mà bạn đã cung cấp. Vì vậy, nếu tôi muốn tạo 100 mã thông báo

token, tôi sẽ lấy ra 101 token. Và mã thông báo đầu tiên không phải là mã thông báo mà mô hình đã tạo.

Đó là mã thông báo mà tôi đã nhập. Và đó là lý do tại sao tôi muốn nhận 100 token khi chỉ định mức tối đa

chiều dài là 101. Và khi tôi đặt độ dài tối thiểu ở đây, điều này cũng chỉ giúp đảm bảo

rằng tôi đang nhận được chính xác 100 token được tạo ra bởi mô hình này.

Được rồi, bây giờ đây là một câu hỏi dành cho bạn. Nếu tôi muốn 1.000 mã thông báo do mô hình tạo ra,

tại sao tôi lại thực hiện 10 lần lặp lại, mỗi lần 100 mã thông báo? Tại sao tôi không có

một lần lặp lại và 1.000 mã thông báo? Nếu bạn muốn có một chút thời gian để suy nghĩ về điều này,

vui lòng tạm dừng video. Câu trả lời là những mô hình này thực sự gặp khó khăn

tiếp tục thực hiện nhiệm vụ và duy trì phản ứng mạch lạc. Do đó, phản hồi càng dài,

đầu ra được tạo ra càng dài thì nó sẽ càng trở nên kỳ lạ hơn và càng có nhiều loại

đi vào tầng bình lưu nó sẽ trở nên vô nghĩa hơn.

Vì vậy, tốt hơn là nên có nhiều chuỗi ngắn hơn là có ít chuỗi dài hơn.

Giờ đây, khi bạn tương tác với các chatbot hiện đại, có sẵn trên thị trường, như thông qua OpenAI, thông qua Anthropic, thông qua Google hoặc Facebook,

những mô hình đó đã được đào tạo rất cụ thể và rất cẩn thận trong một thời gian dài để tạo ra những phản hồi dài có tính mạch lạc nội bộ cao.

Nhưng những mẫu như GPT-2 này, chúng thực sự bay vào tầng bình lưu.

Vì vậy, nói chung tốt hơn là nên có 10 nhân 100 thay vì 1 nhân 1000.

Được rồi, đó là lời giải thích thực sự sâu sắc về ô mã này.

Nhưng điều này rất quan trọng và bạn sẽ thấy đoạn mã trông như thế này trong suốt phần còn lại của phần này.

Vì vậy, đó là lý do tại sao tôi muốn dành thời gian để giải thích điều này thật chi tiết.

Được rồi, ở đây tôi chỉ hiển thị tất cả kết quả đầu ra.

Vì vậy, đây là một đầu ra cụ thể.

Lưỡng cực không có lỗi.

Trên thực tế, cơ thể còn giúp hệ thống miễn dịch

chống lại bệnh tật, bất cứ điều gì.

Được rồi, chúng ta hãy tiếp tục.

Vì vậy bây giờ điều tôi đang làm là lấy tất cả kết quả đầu ra đó

và kiểm tra xem các mã thông báo ở đầu ra có

nằm trong top 100 token thường xuyên nhất trong các chuyến đi của Gulliver.

trong Những chuyến du hành của Gulliver.

Và ở đây tôi đang lấy tất cả các đợt

và đầu tiên đến cuối chuỗi

vì tôi muốn bỏ qua mã thông báo đầu tiên,

đó là cái tôi tạo ngẫu nhiên.

Được rồi, và ở đây chúng tôi thấy 40% rất nhất quán

với kết quả mà tôi đã trình bày trong slide.

Được rồi, bây giờ chúng ta sẽ tinh chỉnh mô hình.

Đây là trình tối ưu hóa, không có gì mới ở đây.

Bạn có thể thấy rằng tốc độ học tập nhỏ hơn một chút

hơn tốc độ học tập mà chúng tôi đang sử dụng

trong phần trước của khóa học.

Vì vậy, nói chung để tinh chỉnh,

bạn muốn sử dụng tỷ lệ học tập nhỏ hơn.

Và lý do là bạn không muốn ghi đè

kiến thức thế giới, ngữ pháp và cú pháp

và cấu trúc và mô hình trong ngôn ngữ

mà những mô hình được đào tạo trước này đã học được.

Thay vào đó, bạn chỉ muốn thêm

một chút sửa đổi.

Bạn chỉ muốn huých những người mẫu này

mà không ghi đè hoàn toàn

tất cả kinh nghiệm trước đây của họ.

Bây giờ, thông thường trong mã,

đây là nơi tôi sẽ xác định hàm mất mát,

nhưng chúng ta không cần hàm mất mát ở đây

bởi vì những người mẫu có khuôn mặt ôm sát

thực sự có một hàm mất mát được nhúng bên trong mô hình,

điều đó thực sự tuyệt vời

Điều đó có nghĩa là chúng ta không cần phải lo lắng về hàm loss.

Và nó trông như thế nào?

Nó trông như thế này.

Vì vậy, nếu bạn cung cấp một số thông tin đầu vào cho mô hình,

nếu bạn nói nhãn bằng,

và hầu hết thời gian điều đó sẽ xảy ra,

các nhãn sẽ giống như các đầu vào,

sau đó ôm người mẫu khuôn mặt vào trong

sẽ lấy tất cả các mã thông báo đầu vào này

và dịch chuyển chúng từng cái một và sử dụng chúng làm mục tiêu.

Ngoài ra bên trong mô hình,

nó sẽ đảm bảo rằng nó đang sử dụng

giá trị log soft hoặc log softmax âm

để tính toán tổn thất.

Điều đó thực sự tuyệt vời.

Vì vậy, bạn có thể thấy chúng tôi nhận được kết quả đầu ra

và chúng tôi viết results.loss và đây là sự mất mát.

Chúng ta không cần phải có hàm loss riêng.

Được rồi, tuyệt vời.

Hãy để tôi bắt đầu chạy mã này.

Mọi thứ khác ở đây, tôi tin rằng bạn đã từng thấy trước đây,

bạn có thể thấy tôi cũng rất đơn giản

và lấy một cách thẳng thắn một loạt dữ liệu ngẫu nhiên

thay vì lo lắng về trình tải dữ liệu và tập dữ liệu

và đi xuyên suốt toàn bộ văn bản.

Nếu bạn thực sự đang đào tạo cho một ứng dụng thực tế,

thì đó là điều bạn muốn làm.

Ở đây tôi chỉ đang huấn luyện một số rất nhỏ

mẫu ngẫu nhiên từ cuốn sách.

Và vâng, đây chỉ là để minh họa

quy trình hoạt động như thế nào.

Vì vậy, mất bốn phút, nhìn chung không quá tệ.

Ở đây chúng ta có thể thấy những mất mát.

Và thực sự là tôi sẽ quay lại

và có một câu hỏi về điều này trong giây lát.

Được rồi, một lần nữa, chính xác là cùng một lời nhắc.

Bây giờ hãy để tôi quay lại lời nhắc trước đó ở đây.

Đây là từ đào tạo trước.

Bạn có thể thấy chúng tôi có ba,

mô hình được đào tạo trước nhưng trước khi tinh chỉnh.

Bạn có thể thấy chúng tôi có ba đoạn văn ở đây

và tất cả đều tách ra.

Cái này hơi dài phải không?

Và bây giờ chúng ta đi xuống đây,

và bây giờ chúng ta thấy rằng chúng ta có được,

có gì đó trông hơi khác một chút, được chứ?

Vậy là xong rồi, chỉ một đoạn văn nhưng ngắn hơn.

Và nếu chúng ta đọc cái này, nó là,

"'Tôi không thể tin rằng trong thời gian hai tuần,

"'Tôi có thể cung cấp cho anh ấy.

"'Tôi cũng đã nhận thấy rằng danh dự của anh ấy,

"'khi anh ấy đề cập đến bất kỳ quốc gia nào

"'nơi lẽ ra tôi không được phép vào.'"

Hãy xem, đây là sự phản bội đất nước của anh ấy,

phản bội chính người dân của mình.

Vì vậy, điều này nghe có vẻ rất giống Gulliver's Travels

và cũng giống như văn bản của Những chuyến du hành của Gulliver.

Hãy để tôi chỉ cho bạn những gì tôi muốn nói.

Ở đây chúng tôi đang ở trang web của URL cho văn bản

mà chúng tôi đã tải xuống để đào tạo.

Và lưu ý rằng tất cả văn bản đều có số lượng giới hạn

số dòng hoặc ký tự trên mỗi dòng, phải không?

Vậy đại khái mọi việc là như thế này.

Vì vậy, bạn thấy phong cách đó cũng xuất hiện ở đây.

Được rồi, bây giờ tôi đang tạo thêm văn bản

và hãy xem, và tính toán lại điều này.

Vì vậy, việc sử dụng token Gulliver's Travels thông thường

đã tăng từ 40% trước khi tinh chỉnh

đến 60% sau khi tinh chỉnh.

Vì vậy, mặc dù đây đều là những từ rất phổ biến,

GPT hiện đang sử dụng chúng nhiều hơn,

thích hơn 50% trong số chúng sau khi tinh chỉnh cuốn sách này.

Được rồi, và điều cuối cùng tôi muốn thảo luận

là liệu đây có phải là một điều tốt hay không.

Vì vậy, bạn biết đấy, khi bạn học về máy học,

giảm độ dốc, học sâu,

bạn biết rằng tổn thất tàu hỏa phải càng thấp càng tốt

và tổn thất kiểm tra phải càng thấp càng tốt.

Khi nó về 0 thì thật tuyệt.

Vậy thì mô hình của bạn thực sự tuyệt vời.

nhưng đó có thực sự là một điều tuyệt vời ở đây?

Hãy nhớ rằng khi tổn thất tiến về 0,

điều đó có nghĩa là người mẫu đã được đào tạo rất bài bản

trên văn bản đào tạo rằng nó có nguy cơ

của việc trang bị quá mức cho văn bản.

Nhưng điều chúng tôi muốn từ những mô hình sáng tạo này

không phải là có khả năng ghi nhớ hoàn hảo các văn bản

mà mô hình đã đào tạo.

Thay vào đó, chúng tôi muốn tạo ra văn bản thú vị,

logic, hợp lý, hữu ích, mạch lạc, v.v.

Và vì thế tôi không rõ liệu đó có phải là một sự mất mát,

đó là một sự mất mát rất nhỏ trong việc tinh chỉnh

thực sự là một điều tốt.

Đây là một cuộc thảo luận tôi sẽ quay lại nhiều lần.

Vì vậy có thể bạn không muốn mô hình của mình

trông giống hệt cuốn sách Những chuyến du hành của Gulliver,

nhưng chỉ cần tinh chỉnh một chút

nên nó có một chút kiến thức chuyên môn về cuốn sách đó,

trong trường hợp đó chúng ta có thể đã đào tạo quá nhiều ở đây.

Khi bạn tiến tới nâng cao hơn

và các ứng dụng tùy chỉnh của LLM,

hoặc thực sự là bất cứ điều gì trong học máy,

bạn sẽ bắt đầu thấy rằng việc triển khai mã

và cơ chế không nhất thiết phải phức tạp hơn.

Thay vào đó, những thách thức thực sự bắt đầu đến

từ những khía cạnh chất lượng hơn,

như chọn một tập dữ liệu thích hợp,

thiết lập tốc độ học tập phù hợp và các thông số khác,

và tìm ra cách tốt để đánh giá hiệu suất.

Chúng ta sẽ tiếp tục khám phá những ý tưởng này

trong thử thách viết mã ở video tiếp theo.