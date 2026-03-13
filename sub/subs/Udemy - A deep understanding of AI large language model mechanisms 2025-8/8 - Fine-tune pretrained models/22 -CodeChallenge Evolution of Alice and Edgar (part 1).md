# 22 -CodeChallenge Sự tiến hóa của Alice và Edgar (phần 1)

---

Thử thách viết mã này là phần tiếp theo của video trước. Trên thực tế, để hoàn thành

thử thách mã này, bạn cần phải tạo và tải xuống mô hình phân loại BERT

mà chúng tôi đã phát triển trong video trước. Ở đây chúng ta sẽ có ba mô hình trong một Python

phiên, một mô hình BERT để phân loại và hai mô hình tổng quát để đào tạo. Ngoài ra

chỉ tải bộ nhớ để bạn theo dõi những gì chúng tôi đang làm và mỗi mô hình phải làm gì,

cũng có một số vấn đề về bộ nhớ Python và GPU mà chúng ta sẽ phải giải quyết. Bức tranh lớn

Tổng quan về những gì chúng ta sắp làm ở đây là huấn luyện mô hình Alice và Edgar như chúng ta đã làm trước đó

trong phần này và trong quá trình đào tạo, chúng ta sẽ yêu cầu trình phân loại Bert đọc văn bản

được tạo ra bởi hai mô hình đó và quyết định văn bản nào đến từ mô hình nào. Đây sẽ là một

một cách khác để đánh giá hiệu suất tinh chỉnh.

Có rất nhiều bộ phận chuyển động trong bài tập này.

Vậy hãy bắt đầu.

Bài tập một về cơ bản liên quan đến việc nhập ba mô hình

vào phiên Python.

Để bắt đầu, bạn muốn tải lên trình phân loại BERT đã được huấn luyện

mà chúng tôi đã phát triển và tải xuống trong video trước.

bạn có thể tải tệp lên bằng nút này tại đây.

Tệp PT đó có dung lượng khoảng nửa gigabyte,

vì vậy phải mất vài phút để tải lên

tùy thuộc vào tốc độ kết nối internet của bạn.

Bây giờ, đây chỉ là thông số.

Bạn sẽ cần phải tạo lại mã mô hình

như chúng tôi đã làm trong video trước.

Vì vậy, điều bạn cần làm là chạy lại mã

để xác định lớp cho mô hình,

Và sau đó bạn sử dụng hàm LoadStateDict

để ánh xạ các tham số từ tệp đã tải xuống đã được đào tạo

vào mô hình mà bạn vừa tạo trong mã,

mà tôi đã hướng dẫn cách thực hiện một số video trước đây.

Bây giờ chúng ta sẽ không đào tạo lại mô hình.

Nó đã được huấn luyện rồi, nó đã được tinh chỉnh rồi.

Vì vậy, bạn có thể chuyển nó sang chế độ đánh giá

cho toàn bộ thử thách mã.

Ngoài ra, để tiết kiệm bộ nhớ,

chúng ta có thể sử dụng phương thức một nửa trên mô hình phân loại này.

Tôi sẽ giải thích chi tiết hơn việc này làm gì

khi tôi cho bạn xem mã của tôi.

Vì vậy, bây giờ, bạn chỉ có thể chạy nó.

Có lẽ bạn muốn đọc một chút về nó trực tuyến.

Được rồi, đó là tất cả về mô hình phân loại BERT.

Tiếp theo bạn muốn thiết lập hai mô hình để tinh chỉnh

đến văn bản Alice và văn bản Edgar.

Vì vậy, bạn sẽ cần nhập và mã hóa hai cuốn sách đó

và sau đó cũng nhập mô hình eluthor-gpt-neo hai lần.

Bây giờ điều này chúng tôi đã thực hiện một vài lần trước đây

trong các thử thách mã trước đó.

Vì vậy, bạn có thể tìm mã liên quan và dán nó vào đây.

Bây giờ đây là hai mô hình mà chúng ta sẽ đào tạo.

Vì vậy, bạn không muốn chuyển chúng sang chế độ eval

và bạn không muốn sử dụng phương pháp một nửa.

Cuối cùng, đẩy cả ba model đó lên GPU.

Đó là bài tập một,

và bây giờ bạn có thể tạm dừng video

và viết mã để giải bài tập này.

Và bây giờ tôi sẽ chuyển sang Python, tôi sẽ cho bạn xem mã của tôi,

và tôi cũng sẽ bắt đầu một cuộc thảo luận đang diễn ra

về các vấn đề bộ nhớ trong LLM và GPU.

Vì vậy, ở đây tôi đang nhập một số thư viện mà chúng tôi sẽ cần,

gọi GPU.

Ở đây tôi đã bắt đầu nên tôi nhấn nút này

và tôi đã tải tệp này lên đây, tệp PyTorch này.

Tôi đã bắt đầu tải nó lên.

Bạn có thể thấy vật nhỏ màu xanh lá cây này ở đây.

Cuối cùng vòng tròn đó sẽ hoàn thành

và sau đó chúng ta sẽ có phiên bản đầy đủ của mô hình đó.

Trong lúc chờ đợi, trong khi tệp này đang được tải lên,

chúng ta vẫn có thể tương tác với tệp mã.

Chúng ta vẫn có thể chạy mã.

Chúng tôi không phải đợi quá trình tải lên này kết thúc.

Vì vậy, đây là định nghĩa lớp.

Tôi thực sự chỉ sao chép và dán nó từ tập tin trước đó.

Và vâng, bây giờ tôi nói ở đây là tải tập tin lên.

Bây giờ phần còn lại của mã này,

chúng tôi thực sự không thể chạy cho đến khi việc này hoàn tất.

Vì vậy, tôi sẽ quay lại chạy ô mã này sau giây lát.

Đầu tiên, hãy để tôi giải thích điều này.

Vì vậy, khi bạn chuyển một mô hình sang chế độ đánh giá,

điều đó có nghĩa là nó đang được thiết lập để đánh giá

và không phải để đào tạo.

Điều đó thật tuyệt vì chúng tôi không đào tạo bộ phân loại này.

Nó đã được đào tạo trước và đã được tinh chỉnh

như một mô hình phân loại.

Và những gì tôi làm ở đây là một nửa mô hình.

Và phương pháp này làm gì?

Phương thức này chuyển đổi mọi thứ từ float 32 sang float 16.

Vì vậy, về cơ bản nó làm giảm độ chính xác của mô hình.

Bây giờ, đây không phải là điều bạn thường muốn làm

theo mặc định với các mô hình.

Bạn chắc chắn không muốn làm điều này

khi bạn lần đầu đào tạo hoặc tinh chỉnh một mô hình

bởi vì bạn thực sự muốn có sẵn tối đa

độ chính xác để điều chỉnh tất cả các tham số mô hình.

Tuy nhiên, khi bạn gặp vấn đề về bộ nhớ,

thì việc chia nó thành một nửa là một ý tưởng không tồi.

Điều đó nói lên rằng, nếu có thể,

bạn nên kiểm tra điều này với độ chính xác một nửa

và hoàn toàn chính xác và đảm bảo rằng bạn không

thực sự mất rất nhiều thông tin

trong mô hình sẽ cho phép bạn chạy trình phân loại.

Trong trường hợp này, độ phân giải 16 bit vẫn là quá nhiều

bởi vì sự phân loại mà chúng tôi đang thực hiện

tương đối dễ thực hiện.

Vì vậy điều tiếp theo tôi làm

đang nhập mã thông báo eluthor.

Vì vậy, tôi nhập mã thông báo và mô hình,

model GPT-neo đã được đào tạo trước 125 triệu thông số.

các thông số. Và như bạn đã thấy trước đó, ở phần trước, chúng tôi nhập chính xác cùng một tệp

hai lần, nhưng tôi đặt cho nó những tên biến khác nhau. Tôi cũng quên đề cập rằng tôi đang nhập

Mã thông báo BERT ở đây. Hiện tại, mã thông báo BERT khác với mã thông báo GPT OpenAI. Vì vậy chúng tôi

cần phải có hai mã thông báo ở đây với các tên biến khác nhau. Điều đó có nghĩa là các token

cũng sẽ khác đi.

Chúng ta sẽ giải quyết vấn đề đó trong bài tập tiếp theo.

Ở đây tôi đang tải xuống hai văn bản này.

Đây cũng là đoạn mã mà bạn đã thấy nhiều lần trước đây.

Bạn đã thấy trước đó eluthor sử dụng mã thông báo của GPT-2,

nhưng mã thông báo BERT thì khác

từ mã thông báo GPT-2.

Vì vậy, điều đó có nghĩa là bạn sẽ cần phải dịch

giữa BERT và mã thông báo eluthor.

Và lý do tại sao bạn cần phải làm điều này

đó là trong các bài tập sau của thử thách viết mã này,

chúng ta sẽ sử dụng mô hình BERT

để đọc văn bản được tạo ra

theo mô hình Alice và Edgar.

Bạn nhớ rằng chúng tôi đã phát triển

chức năng dịch tokenizer sớm hơn trong khóa học

đó là trong phần

khi bạn lần đầu tiên tìm hiểu về mã thông báo.

Nếu bạn thích, bạn có thể tìm mã đó

rồi sao chép dán vào đây.

Nhưng tôi cũng khuyên bạn chỉ nên viết lại mã từ đầu.

Khi bạn cảm thấy thoải mái với mã thông báo,

thì việc thực hiện bản dịch này không quá khó khăn.

Bạn có thể kiểm tra bản dịch của mình bằng cách sử dụng một số văn bản mẫu.

Và thực ra ảnh chụp màn hình ở đây là một lời nhắc nhở

về lý do tại sao chúng ta cần chức năng dịch thuật.

Vì vậy, bản thân các chỉ số mã thông báo là tùy ý

và do đó không thể được ánh xạ trực tiếp

giữa các tokenizer khác nhau.

Ở đây bạn thấy một ảnh chụp màn hình về việc sử dụng các chức năng

mà tôi viết để dịch.

Và thực tế là hai câu này giống nhau

cho thấy mã của tôi có thể bắt đầu bằng văn bản,

được mã hóa bằng BERT, được dịch sang eluthor

và ngược lại.

Ngoài ra, hãy đảm bảo loại trừ mã thông báo CLS và SEP

mà Bert chèn theo mặc định.

Bạn thực sự có thể xác định mức độ khó khăn

bạn muốn bài tập này được thực hiện bằng cách sao chép mã

từ trước đó trong khóa học hoặc viết nó từ đầu.

Mặc dù thành thật mà nói, đôi khi phải mất nhiều thời gian hơn

để tìm đoạn mã phù hợp

hơn là chỉ viết lại từ đầu.

Dù sao thì bây giờ tôi sẽ chuyển sang Python.

Ô mã đầu tiên này là những gì tôi đã hiển thị ảnh chụp màn hình,

và đó chỉ là lời nhắc nhở tại sao chúng ta cần

chức năng dịch mã thông báo.

Vì vậy tôi bắt đầu với văn bản này,

xin chào, tên tôi là Mike và tôi thích màu tím.

Sau đó, tôi mã hóa nó bằng cách sử dụng mã thông báo eluthor,

và sau đó tôi giải mã những số nguyên đó

trực tiếp với Bert.

Và sau đó tôi chỉ nhận được một loạt những điều vô nghĩa.

Và điều ngược lại cũng đúng.

Khi tôi mã hóa bằng Bert và sau đó thử giải mã

sử dụng eluthor, tôi nhận được rất nhiều điều vô nghĩa.

Được rồi, điều chúng tôi muốn làm ở đây là dịch từ,

vì vậy hãy mã hóa bằng cách sử dụng eluthor và sau đó giải mã

sử dụng bộ giải mã của eluthor.

và sau đó chúng ta có thể mã hóa trong BERT văn bản được giải mã từ eluthor. Nghe có vẻ hơi khó hiểu khi tôi

mô tả nó thành tiếng, nhưng tôi tin rằng bạn biết tôi đang nói về điều gì. Chúng tôi

đã loay hoay với rất nhiều điều này trong phần về mã thông báo. Đây là nơi mọi thứ bắt đầu diễn ra

khó khăn. Chúng ta vẫn chưa sẵn sàng cho việc tinh chỉnh và phân loại, nhưng bài tập thứ ba là

bước cần thiết để cho phép chúng tôi hoàn thành thử thách mã này. Mục tiêu cơ bản ở đây là tạo ra một

lô dữ liệu mà BERT có thể sử dụng để phân loại. Mỗi đợt phải có kích thước 64 x 128. Tất cả đều là mã thông báo

chỉ số và 32 hàng đầu tiên là mã thông báo được tạo bởi mô hình Alice và 32 hàng tiếp theo

là các mã thông báo được tạo bởi mô hình Edgar.

Khi bạn đặt tất cả những thứ này vào một hàm Python,

đầu ra của hàm đó sẽ là một tenxơ PyTorch

mà chúng ta có thể nhập vào bộ phân loại BERT

cùng với một vectơ nhãn sẽ là 32 số không

tiếp theo là 32 cái.

Bây giờ, một phần nguyên nhân khiến bài tập này trở nên phức tạp

là bạn cần có chính xác 128 mã thông báo trong mỗi hàng.

Nhưng mô hình Alice và Edgar tạo ra mã thông báo eLuther,

nhưng mô hình BERT cần mã thông báo BERT.

Và 128 token eLuther không nhất thiết phải là 128 token BERT.

Vì vậy, đó là một vấn đề mà bạn sẽ phải giải quyết

với một giải pháp cho.

Một vấn đề khác là các mô hình eluthor

có thể tạo mã thông báo khoảng trắng

như ký tự dòng mới hoặc tab hoặc dấu cách

mà mô hình Bert sẽ hoàn toàn bỏ qua.

Vì vậy, giải pháp tôi nghĩ ra cho việc này

là có một danh sách các token

mà tôi yêu cầu các mô hình eluthor đặc biệt tránh sử dụng.

Hàm Python của tôi trông giống như thế này.

Vì vậy tôi gọi hàm này là batch cho Bert.

Và đây thực sự không phải là toàn bộ chức năng.

Tôi đã xóa một loạt dòng mà bạn có thể điền vào.

Nhưng về cơ bản ý tưởng là khởi tạo

tensor lô này ở đây.

Đó là kích thước lô theo độ dài chuỗi,

nghĩ ra một số mã thông báo bắt đầu bằng số nguyên ngẫu nhiên,

tạo chuỗi mã thông báo bằng mô hình Alice

và mô hình Edgar.

Và sau đó bên trong vòng lặp này,

Tôi chỉ định nửa đầu của hàng

trở thành mã thông báo do Alice tạo ra

và nửa sau của vòng lặp này

là mã thông báo do Edgar tạo ra.

Ở đây bạn có thể xem danh sách token

mà tôi đang hướng dẫn các mô hình eluthor tránh sử dụng.

Một lần nữa, đây không phải là một chức năng hoạt động hoàn chỉnh,

nhưng nếu bạn gặp khó khăn với bài tập này,

sau đó bạn có thể bắt đầu từ mã này và điền vào phần còn lại.

Sau khi chức năng đó hoạt động,

bạn có thể tạo hàm mất cho mô hình BERT

và sau đó kiểm tra nó.

Vậy những gì bạn thấy ở đây là những nhãn mà BERT đã dự đoán,

và đây là những nhãn thực tế từ dữ liệu thực tế.

Trong trường hợp này, độ chính xác là khoảng 50%,

và đó là trước khi tôi thực hiện bất kỳ khóa đào tạo nào

của các mô hình sinh eluthor.

Vì vậy, bộ phân loại BERT đã được huấn luyện đầy đủ,

nhưng các mô hình eluthor tại thời điểm này chưa được đào tạo.

Vì vậy, độ chính xác phân loại 50% là chính xác

những gì chúng ta mong đợi trước khi tinh chỉnh.

Đó là bài tập thứ ba.

Chúc may mắn làm việc thông qua cái này.

Và bây giờ tôi sẽ chuyển sang mã và hiển thị giải pháp của mình.

Ở đây tôi xác định kích thước lô và độ dài chuỗi.

Và hãy xem, vâng, đây là đoạn mã mà tôi đã đưa ra trước đó.

Điều tôi sẽ thảo luận ở đây là một cách mà tôi đã cố gắng đảm bảo

rằng chúng tôi sẽ không nhận được quá ít token để tạo ra

từ mô hình Alice và mô hình Edgar

gấp bốn lần số token chúng ta cần.

Và sau đó giả sử rằng điều này sẽ dài hơn

hơn bất cứ điều gì nó kết thúc

khi chúng tôi dịch nó sang BERT.

Vậy hãy để tôi mô tả một kịch bản cụ thể

để đảm bảo rằng điều này là rõ ràng.

Vì vậy hãy tưởng tượng chúng ta tạo ra 128 token.

Hãy nói rằng tôi đã làm nó như thế này.

Bây giờ, 128 token trong mô hình eLuther,

khi tôi dịch chúng sang token BERT,

có lẽ đó chỉ là 101 token,

nhưng đó không phải là điều chúng ta muốn.

chúng tôi muốn có 128 token BERT.

Việc chúng ta có bao nhiêu token EDGAR thực sự không quan trọng.

Đó là lý do tại sao tôi viết mã này.

Vì vậy ý tưởng là chúng ta đang tạo ra quá nhiều token

và sau đó chúng tôi chỉ, sau đó tôi chỉ trích xuất

bất kể độ dài chuỗi ở đây là bao nhiêu

cho mô hình này ở đây, lô dữ liệu này ở đây.

Bây giờ, khi tôi đang viết và thử nghiệm các chức năng này,

Tôi thấy rằng những mô hình sáng tạo này

đã làm rất nhiều việc mà tôi không thích

và họ đã gây ra lỗi.

Họ đã làm hỏng toàn bộ chức năng.

Và một số điều đó có liên quan đến việc dừng lại sớm.

Vì vậy, tôi đặt điểm dừng sớm là sai.

Một số trong đó đã lặp lại khoảng trắng.

Vì vậy tôi đặt ra hình phạt lặp lại

cao hơn một chút.

Vì vậy, nếu mô hình bắt đầu tạo ra khoảng trắng,

nó sẽ không tiếp tục tạo ra không gian nữa.

Và sau đó tôi cũng đưa cái này vào đây, ID từ xấu,

và tôi đã liệt kê tất cả các vấn đề phổ biến về khoảng trắng

mà chúng ta có thể gặp phải.

Vì vậy, dòng mới, dòng mới gấp đôi, vận chuyển trở lại,

đây thực ra không phải là một dòng mới,

điều này chỉ đưa con trỏ trở lại

ở đầu dòng, tab và dấu cách.

Và hy vọng với tất cả những điều đó,

điều đó thực sự kết thúc.

Được rồi, bây giờ chúng ta có thể kiểm tra và rất tiếc,

Tôi phải chạy mã này lên đây.

Chúng ta đang ở đâu?

Cao hơn một chút.

Vâng, mã này tôi cần chạy.

Được rồi, bây giờ chúng ta có thể kiểm tra.

Việc này mất vài giây.

Phải mất một chút thời gian cho hai mô hình này

để tạo ra tất cả các mã thông báo này

và phải mất một chút thời gian để thực hiện việc tổ chức này,

mặc dù đó không phải là nút cổ chai tính toán chính.

Vì vậy, bây giờ chúng ta thấy rằng chúng ta có 64 x 128 mã thông báo theo lô.

Các nhãn là 64.

Được rồi, hãy nhớ rằng đây là 128 token BERT

bởi vì tôi đã dịch mã thông báo eluthor

thành token BERT.

Thế là bây giờ mình đã chạy được rồi, mình có thể set hàm loss

và tôi đang viết về sự mất BERT vì trong chốc lát

trong bài tập thứ tư, chúng ta sẽ tinh chỉnh

mô hình Alice và Edgar.

Vì vậy chúng ta cần có hàm loss riêng

cho mô hình BERT và mô hình Alice và Edgar.

Bây giờ tôi không đào tạo mô hình BERT,

nhưng điều này sẽ cho phép chúng tôi theo dõi tổn thất

của mô hình BERT bên cạnh độ chính xác.

Vì vậy, chúng ta có thể chạy cái này.

Vì vậy bây giờ tôi chạy qua mô hình BERT,

lô mà tôi đã tạo ở đây bằng cách sử dụng hàm.

Và sau đó chúng ta có thể nhìn vào các nhãn được dự đoán

và các nhãn thực tế.

Trong trường hợp này, độ chính xác là 45%,

ngay gần mốc 50% mà chúng tôi mong đợi,

cho rằng mô hình Alice và Edgar là mô hình được đào tạo trước

để họ có thể tạo ra văn bản,

nhưng chúng không được tinh chỉnh để tạo văn bản

cho cuốn sách Alice hoặc cho cuốn sách Edgar.

Còn một bài tập nữa trong thử thách viết mã này, nhưng tôi quyết định chia video ở đây để khuyến khích bạn thực hiện.

Ra khỏi ghế duỗi chân uống một ngụm nước hoặc cà phê và khi đã sẵn sàng, bạn có thể quay lại ghế.

bài tập cho thử thách mã này