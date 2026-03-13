# 4 -CodeChallenge Sự bối rối bối rối được dịch

---

Tôi đã giải thích trong video trước rằng sự bối rối là một con số đặc trưng cho tổng thể

khả năng của một mô hình để dự đoán mã thông báo tiếp theo trong một chuỗi.

Về cơ bản, nó là mức trung bình của tổn thất trên toàn bộ văn bản và phản ánh cả

độ chính xác của mô hình để dự đoán chính xác mã thông báo tiếp theo và cả sự tách biệt giữa

dự đoán của mã thông báo mục tiêu so với tất cả các mã thông báo khác.

Vì vậy, trong thử thách viết mã này, bạn sẽ có cơ hội thực hiện lại sự bối rối

và khám phá mức độ phức tạp phụ thuộc vào các tham số như độ dài chuỗi và văn bản cũng như cách thức

nó thay đổi đối với các mô hình khác nhau khi xử lý cùng một văn bản.

Mục tiêu của bài tập một chỉ đơn giản là viết một hàm để tính độ phức tạp đã cho

một chuỗi mã thông báo, một mô hình và độ dài chuỗi được chỉ định.

Bây giờ hàm của bạn không cần phải giống hệt hàm của tôi, nhưng bạn có thể làm theo cách chung này

cấu trúc nếu bạn thích.

Nhưng chức năng này chắc chắn cần lấy mô hình làm đầu vào vì trong các bài tập sau

chúng ta sẽ khám phá việc sử dụng các mô hình khác nhau trên cùng một văn bản và chức năng của bạn cũng cần

để nhập lại độ dài chuỗi vì đây là tham số mà chúng ta sẽ thao tác sau

trong thử thách mã này.

Vì vậy, ý tưởng của chức năng này là chia văn bản thành các đoạn nhỏ

văn bản dựa trên độ dài chuỗi, tính toán độ mất trong mỗi phân đoạn đó và sau đó

tính toán sự bối rối ở cuối.

Tôi đã triển khai điều này bằng cách sử dụng các phân đoạn không chồng chéo để đơn giản.

Nếu bạn muốn triển khai điều này bằng cách sử dụng các phân đoạn chồng chéo một phần với tham số bước tiến,

điều đó cũng tốt, nhưng nhìn chung trong bài tập này và với thử thách viết mã này, tôi hiểu rõ hơn

quan tâm đến việc đảm bảo rằng bạn hiểu cách tính độ phức tạp và do đó bạn không nên

lo lắng quá nhiều về các chi tiết triển khai khác mà về nguyên tắc có thể được đưa vào.

Bây giờ khi bạn đã triển khai chức năng này, bạn có thể kiểm tra nó bằng cách sử dụng 50.000 mã thông báo ngẫu nhiên

sử dụng GPT2.

Và với các mã thông báo ngẫu nhiên, ý tôi là các chỉ số mã thông báo ngẫu nhiên theo đúng nghĩa đen, bạn sẽ cảm thấy bối rối.

thước đo cho điều đó và tôi muốn bạn so sánh điều đó với sự mong đợi về sự bối rối được đưa ra

một sự phân bố hoàn toàn đồng đều.

Bây giờ độ phức tạp dự kiến ​​của phân bố đều ngẫu nhiên là e mũ âm tự nhiên

log của 1 trên n.

Bây giờ tôi sẽ không cho bạn biết liệu sự phức tạp của các mã thông báo ngẫu nhiên của bạn có phù hợp với kỳ vọng này hay không

từ một phân phối ngẫu nhiên.

Tôi muốn bạn xem điều gì xảy ra và sau đó suy nghĩ xem liệu sự trùng khớp hay không phù hợp

có ý nghĩa.

Như tôi thường khuyến khích trong khóa học này, tôi muốn bạn đưa ra dự đoán về những gì bạn nghĩ

sẽ xảy ra trước khi bạn thực sự nhìn thấy kết quả.

Nếu dự đoán của bạn được xác nhận thì bạn có thể tiếp tục suy nghĩ xem tại sao mình lại đúng.

Và nếu dự đoán của bạn không được xác nhận thì điều đó còn tốt hơn vì đó là sự thật

cơ hội để học một cái gì đó mới.

Được rồi, hãy tạm dừng video và chuyển sang Python và bắt đầu viết mã.

Và bây giờ tôi sẽ chuyển sang viết mã, đưa ra giải pháp của mình và thảo luận về câu trả lời cho câu hỏi này.

Một số thư viện để nhập vào đây.

Tôi đang nhập GPT2 nhỏ và tôi viết, hãy đảm bảo rằng nó nhỏ vì

trong các bài tập sau, chúng tôi sẽ nhập phiên bản GPT2 lớn hơn một chút.

Được rồi, vậy mô hình, hãy chuyển nó sang chế độ đánh giá vì chúng ta không thực hiện bất kỳ hoạt động đào tạo nào.

Và tất nhiên tôi cũng cần tokenizer.

Vì vậy, đây là chức năng của tôi cho sự bối rối.

Nhận một loạt mã thông báo từ một văn bản, một mô hình mặc định cho bất kỳ mô hình nào

được gọi là GPT2 và độ dài chuỗi mặc định là 1024.

Ở đây tôi tính số đoạn phù hợp với toàn bộ chuỗi.

Vì vậy, số lượng mã thông báo chia cho độ dài chuỗi và điều này sẽ mang lại cho tôi một số

số nguyên.

Đó là số nguyên vì tôi đang sử dụng hai dấu gạch chéo.

Nếu tôi làm điều này thì chúng ta có thể nhận được một giá trị không nguyên.

Điều này cho tôi biết số lượng phân khúc.

Và thực sự có khả năng là khi sử dụng mã này, chúng tôi sẽ thu được rất nhiều mã thông báo

ở cuối, ở đâu đó có ít hơn 1.023 mã thông báo thực sự không được đánh giá.

Đó là điều mà nếu bạn đang tính toán sự bối rối thực sự, thực sự

ứng dụng, bạn sẽ muốn kết hợp điều đó để tính đến các mã thông báo bổ sung có thể có

ở cuối trình tự.

Ở đây tôi không lo lắng về điều đó.

Được rồi, sau đó tôi lặp lại tất cả các phân đoạn riêng lẻ đó.

Ở đây tôi tìm thấy tinh bột và các chỉ số vị trí cuối cùng để tính toán một mẻ.

Ở đây, vị trí bắt đầu bằng các chỉ số này nhân với độ dài chuỗi, và sau đó

vị trí bắt đầu cộng với độ dài chuỗi.

Như tôi đã đề cập trong các slide, đây là các trình tự không chồng chéo.

Nếu có thể thực hiện việc này theo trình tự chồng chéo, mặc dù có

bạn sẽ gặp phải vấn đề tính toán khoản lỗ trên cùng một mã thông báo nhiều lần

nếu bạn có trình tự chồng chéo.

Vì vậy, bạn cần kết hợp thêm mặt nạ vào đó.

Vì vậy, đây chỉ là một cách tiếp cận đơn giản hơn.

Được rồi, đây là những token đó.

Ở đây tôi thực hiện chuyển tiếp với torched.no-grad, phải không?

Bởi vì một lần nữa, chúng ta không cần tính gradient.

Chúng tôi không đào tạo, tinh chỉnh hay bất cứ điều gì tương tự.

Vì vậy, điều này chỉ tăng tốc độ tính toán lên một chút và cũng tránh chiếm nhiều thời gian hơn.

RAM, nhiều bộ nhớ hơn mà chúng ta không thực sự cần.

Được rồi, vậy thì một khi tôi thực hiện bước chuyển tiếp này, thì tôi sẽ bị thua.

Và sau vòng lặp, tất cả mã này ở bên trong vòng lặp trên tất cả các phân đoạn.

Khi vòng lặp đó kết thúc, tôi có thể tính tổng tất cả những thứ đó và chia cho số đoạn.

Vì vậy, đây là tổn thất trung bình trên toàn bộ văn bản.

Và rồi đến điều đó, và điều đó khiến tôi bối rối.

Được rồi, ở đây tôi đang tạo ra 50.000 token ngẫu nhiên.

Vì vậy, các chỉ số ngẫu nhiên giữa 0 và kích thước từ vựng, và sẽ có 50.000 từ vựng như vậy.

Cái ở đây là vì chúng ta cần một lô vì đầu vào mô hình ở đây luôn giả định

đó là từng đợt theo trình tự.

Được rồi, hãy xem qua tất cả 50.000 token đó.

Và đây là những gì chúng tôi nhận được.

Chúng tôi nhận được một số lượng thực sự lớn.

Chúng tôi nhận được 173.000.

Được rồi, và hãy so sánh điều đó với sự phức tạp dự kiến ​​của một phân phối ngẫu nhiên hoàn toàn đồng nhất.

Vì vậy, đó sẽ là trường hợp khi bạn khởi tạo một mô hình có trọng số ngẫu nhiên, ngẫu nhiên thống nhất

trọng số, mô hình không biết mã thông báo nào sẽ tuân theo, mã thông báo nào khác,

bởi vì nó hoàn toàn ngẫu nhiên.

Vì vậy, mọi mã thông báo đều có cơ hội theo dõi mọi mã thông báo khác như nhau.

Và ở đây, trên thực tế, chúng ta nhận được một giá trị tương ứng với kích thước từ vựng.

Vậy là 50.257.

Tất nhiên, điều đó không có gì đáng ngạc nhiên.

Hãy nhớ quy tắc logarit rằng nếu bạn có dấu trừ khi nhân logarit thì đó là

tương đương với chuyển động tịnh tiến bên trong logarit.

Vì vậy, về mặt toán học, chúng ta có thể biểu thức này ở đây, trừ log của 1 trên một cái gì đó,

tương đương với log dương của nghịch đảo của cái này, tức là kích thước từ vựng chia cho

1.

Như vậy, điều đó tương đương với việc có dấu trừ ở đây.

Và sau đó chúng ta có từng bản ghi về kích thước từ vựng và số mũ tự nhiên và số tự nhiên

logarit là nghịch đảo của nhau, do đó mọi thứ đều bị triệt tiêu.

Và chúng ta chỉ kết thúc với kích thước từ vựng.

Được rồi, đó là lý do, để tôi xem.

Chuẩn rồi.

Độ phức tạp dự kiến ​​với các mã thông báo thống nhất ngẫu nhiên là 50.000.

Vậy làm thế nào mà chúng ta có thể nhận được giá trị lớn hơn ba lần so với kỳ vọng đã cho

ngẫu nhiên, vì đây cũng là những mã thông báo được chọn ngẫu nhiên?

Đó là câu hỏi mà tôi hy vọng bạn đang băn khoăn, bối rối và suy ngẫm.

Câu trả lời cho câu hỏi đó là việc phân phối xác suất mã thông báo trong ngôn ngữ được đào tạo trước

mô hình không đồng đều.

Nó hoàn toàn không đồng nhất.

Và nó sẽ khá rõ ràng khi bạn nghĩ về lý do tại sao điều đó không nên xảy ra.

Vì vậy, các mã thông báo như dấu chấm, dấu phẩy và các ký tự dòng mới, còn nhiều hơn thế nữa

thường thấy trong văn bản.

Và do đó, xác suất cơ bản của chúng cao hơn nhiều so với một số ngẫu nhiên khác

mã thông báo có thể chỉ xuất hiện rất ít trong văn bản trực tuyến.

Được rồi, kết luận là mặc dù chúng ta đang sử dụng các token hoàn toàn ngẫu nhiên,

bản thân mô hình không phải là ngẫu nhiên.

Nó không có sự phân bố thống nhất về xác suất của mã thông báo.

Bây giờ chúng ta đã có hàm tính độ phức tạp, các bài tập còn lại trong thử thách mã này

liên quan đến việc sử dụng chức năng đó để khám phá sự bối rối thêm một chút.

Ở đây trong bài tập hai, bạn muốn nhập nhiều sách khác nhau từ Gutenberg.org và

tính toán sự phức tạp của họ.

Bây giờ bạn sẽ nhận ra giao diện của mã này.

Đó chính xác là mã mà chúng tôi đã sử dụng trong phần đầu tiên của khóa học về mã thông báo,

mã hóa các văn bản khác nhau, xem xét hiệu suất mã hóa, ZipSlaw, v.v.

Vì vậy, vì lợi ích của thời gian tính toán và cũng vì lợi ích của việc có thêm một chút

so sánh công bằng giữa các cuốn sách, bạn chỉ nên sử dụng 50.000 mã thông báo đầu tiên từ mỗi cuốn sách

của những cuốn sách này.

Bạn có thể in kết quả dưới dạng văn bản trông như thế này và bạn có thể tạo một biểu đồ thanh

trông giống như thế này

Tôi nghĩ bạn sẽ thấy thú vị về sự phức tạp có thể khác nhau như thế nào mặc dù chúng ta

sử dụng chính xác cùng một mô hình, cùng độ dài chuỗi và cùng số lượng mã thông báo.

Vì vậy, bạn có thể nghĩ tại sao lại như vậy và tôi sẽ thảo luận vấn đề này khi tôi chuyển đổi

để viết mã, điều mà tôi sẽ làm ngay bây giờ.

Vì vậy, đây là những cuốn sách chúng tôi sẽ nhập.

Ở đây tôi đang khởi tạo một vectơ phức tạp, đó là ý nghĩa của nó.

Và bây giờ tôi đang xem lại tất cả các cuốn sách ở đây.

Vì vậy, mã này trông quen thuộc.

Tôi đang nhập toàn bộ văn bản và mã hóa từng cuốn sách này.

Ở đây tôi chỉ lấy 50.000 token đầu tiên, gửi chúng đến GPU, gọi tính toán

hàm phức tạp, sau đó in ra kết quả.

Vì vậy, không tệ đến mức mất khoảng 35 giây và chúng ta có thể thấy khá nhiều biến đổi

trong sự phức tạp của những văn bản khác nhau này.

Chúng ta có thể đánh giá cao sự thay đổi đó dễ dàng hơn khi tạo biểu đồ thanh.

Thật thú vị khi thấy rằng một số văn bản này nhìn chung có độ phức tạp thấp hơn giống như Alice.

Đây là thông qua kính nhìn.

Đây là cuốn sách gồm những bài thơ và truyện ngắn của Edgar Allen Poe.

Cao nhất là Romeo và Juliet, có hơn gấp đôi, gần gấp ba lần.

sự bối rối như cuốn sách của Edgar chẳng hạn.

Và tại sao lại như vậy?

Điều gì gây ra những khác biệt giữa sự phức tạp của các văn bản khác nhau này?

Vâng, một điều cần lưu ý là trong thực tế, sự bối rối thường được tổng hợp

qua những đoạn văn bản khổng lồ, chẳng hạn như toàn bộ internet.

Vì vậy, mặc dù những cuốn sách này có vẻ tương đối dài nhưng chúng vẫn thực sự ngắn đối với một chuyên gia.

tính toán độ phức tạp.

Vì vậy, điều đó có nghĩa là cũng chỉ có một số biến đổi lấy mẫu ở những con số khác nhau này.

Nhưng điều mà sự bối rối thực sự đo lường là khả năng dự đoán mã thông báo tiếp theo của mô hình

theo một trình tự.

Và do đó, trình tự của mô hình càng dễ dự đoán thì độ phức tạp sẽ càng thấp.

được.

Và do đó, những văn bản có trình tự từ ít dự đoán hơn sẽ có mức độ hiệu quả cao hơn

sự bối rối.

Vậy tại sao Romeo và Juliet lại có mức độ bối rối cao hơn?

Một trong những lý do là hầu hết Internet mà GPT-2 đã được đào tạo trước không

nghe như Shakespeare.

Hầu hết internet không có vần điệu.

Nó được viết bằng tiếng Anh hiện đại chứ không phải bằng tiếng Anh của Shakespearean.

Vì vậy, toàn bộ cấu trúc của văn bản này, các đặc điểm thống kê của văn bản này,

khác với tiếng Anh hiện đại như Wikipedia, trang web tin tức, tạp chí, khoa học

và các bài báo trên tạp chí y khoa, v.v., những mô hình này phần lớn đã được đào tạo trước

trên.

Trong bài tập trước, chúng ta đã sử dụng cùng một mô hình và các văn bản khác nhau.

Và bây giờ trong bài tập thứ ba, chúng ta sẽ sử dụng cùng một văn bản nhưng các mô hình khác nhau.

Đặc biệt, đối với bài tập này, bạn nên nhập bốn biến thể của GPT-2.

Đây chỉ là một số mã để nhắc bạn rằng theo quan điểm khiêm tốn của tôi, việc tổ chức sẽ rất thuận tiện

tất cả các mô hình này vào từ điển Python để bạn có thể gọi chúng trong vòng lặp for qua

các phím khác nhau.

Vậy đây là đoạn mã bạn đã từng thấy trước đây.

Trước đây trong khóa học này tôi đã hướng dẫn bạn cách nhập tất cả các mô hình này vào từ điển.

Bây giờ đối với dữ liệu, bạn có thể sử dụng tập dữ liệu WikiText và bạn có thể sao chép mã cho dữ liệu đó từ

video trước đó để nhập WikiText.

Nếu có bất kỳ tập dữ liệu nào khác mà bạn muốn sử dụng thì cũng không sao.

Điều quan trọng ở đây đối với bài tập thứ ba là sử dụng chính xác cùng một dữ liệu và

các mã thông báo giống nhau cho mỗi mô hình này.

Và cũng giống như bài tập trước, bạn có thể báo cáo kết quả dưới dạng văn bản Python

và bạn cũng có thể tạo một biểu đồ thanh.

Và cũng như những bài tập trước, tôi muốn bạn đưa ra dự đoán về những gì

bạn nghĩ những kết quả này sẽ như thế nào.

Cụ thể, bạn cho rằng sự bối rối sẽ tăng, giảm hay không liên quan đến

số lượng tham số trong mô hình, đâu là điểm khác biệt chính giữa bốn biến thể này?

Được rồi, bây giờ bạn nên tạm dừng video và bắt đầu làm việc.

Và bây giờ tôi sẽ thảo luận về giải pháp của tôi.

Vì vậy, ở đây tôi đang nhập văn bản.

Nó không có nhiều văn bản, nhưng không sao.

Chúng ta chỉ cần một chút để so sánh các mô hình khác nhau.

Vì vậy, phải mất một chút thời gian để đọc.

Ở đây, thực ra tôi đang tính toán độ phức tạp cho mô hình nhỏ GPT2 chỉ vì, vâng,

Tôi thực sự không biết tại sao tôi lại có thứ này ở đây.

Thành thật mà nói, tôi không chỉ rõ nó trong hướng dẫn, nhưng dù sao, tôi nghĩ tôi chỉ đang thử nghiệm

cái này.

Được rồi, đây là coderum nhập tất cả các mô hình khác nhau.

Việc này sẽ mất một lúc.

Chạy qua tất cả các mô hình để tính toán độ phức tạp khá đơn giản.

Tôi có một vòng lặp for ở đây.

Và điều quan trọng cần nhớ là thay đổi mô hình.

Vì vậy, ở đây tôi đang lặp lại tất cả các mục trong mô hình biến này.

Hãy lưu ý tên của từ điển Python mà tôi đã sử dụng để nhập tất cả các biến thể GPT2.

Và sau đó, bạn chỉ muốn đảm bảo chỉ định mô hình.

Khá thú vị khi thấy sự bối rối giảm bớt.

Hãy nhớ rằng văn bản giống hệt nhau.

Độ dài chuỗi giống hệt nhau.

Mọi thứ đều giống hệt nhau trong phân tích này ngoại trừ biến thể của mô hình GPT2.

Và tất nhiên, chúng chủ yếu khác nhau ở số lượng tham số cũng như số lớp

và vân vân.

Nhưng điều đó liên quan đến số lượng tham số.

Vì vậy, nhỏ có độ phức tạp cao nhất và chúng ta càng nhận được nhiều tham số thì tỷ lệ càng thấp

sự bối rối.

Trên thực tế, điều này giảm gần một nửa.

Vì vậy, chúng ta đi từ mức độ bối rối khoảng 30 đến khoảng 15 hoặc cao hơn 15 một chút.

Vì vậy, điều đó khá thú vị.

Đây là một phát hiện khá điển hình trong nghiên cứu về sự bối rối khi mô hình càng có nhiều tham số,

sự bối rối càng thấp.

Điều đó thực sự không có gì đáng ngạc nhiên.

Đó là một kết quả rất trực quan.

Các mô hình phức tạp hơn có khả năng dự đoán mã thông báo tiếp theo theo bất kỳ chuỗi nhất định nào tốt hơn

dựa trên ngữ cảnh trước mỗi mã thông báo.

Vì vậy, bạn thấy rằng mô hình càng lớn thì độ phức tạp càng thấp.

Đây là bài tập cuối cùng của thử thách mã này.

Mục tiêu ở đây là chỉ sử dụng một mô hình GPT2 và cũng chỉ một văn bản.

Và sau đó bạn sẽ thay đổi độ dài chuỗi cho các phân đoạn bên trong sự bối rối

chức năng tính toán.

Ở đây bạn có thể thấy độ dài chuỗi khác nhau mà tôi đã sử dụng.

Bạn có thể sử dụng bất kỳ mô hình GPT nào bạn thích.

Để có được kết quả này, tôi đã sử dụng phiên bản nhỏ nhưng chỉ vì nó tính toán nhanh hơn một chút.

Nó không thực sự quan trọng.

Miễn là bạn đang sử dụng cùng một mô hình và cùng một văn bản trong tất cả các bài kiểm tra này và chỉ

thao tác độ dài chuỗi.

Bây giờ hãy nhớ rằng tổng số văn bản mà bạn đang tính toán độ phức tạp là

hoàn toàn giống nhau cho tất cả các văn bản này.

Điều khác biệt duy nhất là có bao nhiêu mã thông báo được tính trung bình cùng nhau thành một phân đoạn

khi bạn chạy qua đường chuyển tiếp và nhận được mức lỗ trung bình của mã thông báo.

Và tất nhiên bạn cũng có thể hình dung những kết quả này dưới dạng biểu đồ thanh.

Có lẽ tôi không cần phải nói lại điều này một cách rõ ràng, nhưng tôi nghĩ sẽ thật tuyệt nếu bạn

sẽ đưa ra dự đoán về việc bạn nghĩ những kết quả này sẽ như thế nào trước khi bạn thực sự

nhìn thấy họ.

Được rồi, bây giờ là cơ hội để bạn làm và học hỏi.

Và bây giờ tôi sẽ chuyển sang Python.

Tôi hy vọng bạn không gặp khó khăn với mã của bài tập này.

Nó trông thực sự giống với mã của một số bài tập vừa qua.

Vì vậy, chúng ta có một vòng lặp for ở đây với các độ dài chuỗi khác nhau.

Bạn có thể thấy tôi thiết lập cái này là lũy thừa 2 và sau đó là các số nguyên từ 5 đến 10.

Và vâng, đó chính là những mã thông báo mà tôi đang sử dụng từ văn bản wiki.

Tôi không chỉ định mô hình ở đây, điều đó có nghĩa là hàm phức tạp sẽ được sử dụng

biến GPT2, đây là phiên bản nhỏ.

Một lần nữa, nếu bạn muốn sử dụng phiên bản GPT2 lớn hơn thì hoàn toàn ổn.

Bạn sẽ nhận được các giá trị số khác nhau của độ phức tạp, nhưng mẫu mà bạn sẽ

xem độ dài chuỗi khác nhau sẽ giống nhau.

Được rồi, và ở đây tôi chỉ định độ dài chuỗi.

Được rồi, sẽ mất một chút thời gian để chạy.

Nó sẽ in ra độ phức tạp của mỗi độ dài chuỗi đó và sau đó chúng ta

có thể thực hiện một âm mưu thanh.

Vì vậy, ở đây, chỉ cần nhìn vào những con số, chúng ta thấy sự bối rối giảm đi một cách đơn điệu thực sự đáng kinh ngạc

với sự gia tăng độ dài chuỗi.

Trên thực tế, đây giống như một sự thay đổi gấp năm lần từ mức độ bối rối thấp nhất khoảng 30 đến mức độ bối rối

độ bối rối cao nhất ở đây vào khoảng 150.

Và hãy nhớ rằng, đó là cùng một mô hình, cùng một văn bản, cùng một mã thông báo,

rằng mọi thứ đều giống hệt nhau ngoại trừ ở đây chúng tôi đang tính trung bình trên các phần nhỏ hơn của

dữ liệu và ở đây chúng tôi đang tính trung bình trên các khối dữ liệu lớn hơn.

Bây giờ, nếu bạn sử dụng văn bản khác hoặc mô hình khác, bạn có thể nhận được các số khác ở đây

trên trục y, nhưng mức giảm chung khi tăng độ dài chuỗi mã thông báo sẽ là

được bảo tồn.

Đó là một mô hình khá nhất quán.

Và tại sao điều này lại xảy ra?

Tại sao chúng ta có được mô hình này?

Hãy nhớ rằng, tôi đã thảo luận nhiều lần và tôi sẽ tiếp tục đề cập đến ngôn ngữ này, ngôn ngữ đó

thực sự phức tạp và nó thực sự ồn ào.

Và do đó, khả năng của một mô hình ngôn ngữ có thể dự đoán bất kỳ ngôn ngữ nào được chọn ngẫu nhiên

mã thông báo thực sự nhỏ.

Thật sự rất khó để dự đoán mã thông báo tiếp theo trong một chuỗi và có một số chuỗi

điều đó dễ dự đoán hơn một chút và một số trình tự không thể thực hiện được

để dự đoán.

Vì vậy, bạn càng tập hợp nhiều dữ liệu lại với nhau thì các chuỗi càng dễ dự đoán giống nhau

cân bằng các trình tự khó dự đoán.

Vì vậy, bạn có nhiều phép đo nhiễu trong một hệ thống phức tạp và bạn càng lấy trung bình nhiều dữ liệu

cùng nhau, bạn sẽ càng có được phép đo ổn định và đáng tin cậy.

Đặc biệt, trong trường hợp bối rối, là một số liệu không âm, do đó có

không thể là giá trị âm.

Vì vậy, nhiễu trong hệ thống đo lường này sẽ chỉ làm tăng giá trị chứ không giảm

các giá trị.

Kết quả cuối cùng của những điểm rút ra này là giá trị số tuyệt đối của sự bối rối

từ một mô hình ngôn ngữ thực sự khó diễn giải.

Ví dụ: điểm bối rối là 2,7 là tốt hay xấu?

Điều này thực sự khó nói vì nó phụ thuộc vào nhiều yếu tố, trong đó có một số yếu tố

không có gì để làm với chính mô hình.

Mặt khác, nếu bạn có hai mô hình khác nhau xử lý cùng một văn bản với cùng một

các thông số phân tích thì bạn chắc chắn có thể giải thích được điểm số phức tạp tương đối.

Mặt khác, điều chúng ta mong muốn ở LLM tổng quát không phải là khả năng dự đoán hoàn hảo.

mã thông báo tiếp theo trong văn bản hiện có mà thay vào đó tạo ra sự mạch lạc, hữu ích và trung thực

tương tác phù hợp với lợi ích và giá trị của chúng ta.

Và sự bối rối không có gì để nói về những phẩm chất đó.

Và với ý nghĩ đó, bây giờ chúng ta hãy bắt đầu khám phá một số cách đánh giá LLM khác.