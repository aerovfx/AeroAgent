# 12 -CodeChallenge Các khám phá MAUVE lớn và nhỏ đã được dịch

---

Bây giờ bạn đã biết cách đánh giá MOV hoạt động và cách triển khai nó trong Python, tôi sẽ

muốn thực hiện thêm một số khám phá để bạn có thể làm quen hơn với phương pháp này và

cũng thấy sự đa dạng về điểm số mà bạn có thể nhận được.

Chỉ là một cảnh báo, thử thách mã này mất nhiều thời gian.

Không hẳn là vì nó khó đến mức bạn phải mất nhiều thời gian để viết mã, nhưng việc tạo ra

mã thông báo mà bạn cần để chạy phân tích này có thể mất 20 đến 25 phút cho mỗi bài tập.

Vì vậy, sẽ có thời gian để bạn viết mã và sẽ có thời gian để bạn để việc phân tích

chạy trong khi bạn đi ra ngoài và làm việc khác.

Mục tiêu của bài tập một là nhập các phiên bản nhỏ và lớn của GPT2.

Làm theo mã từ bài tập trước để tạo 100 lần lặp lại 400 mã thông báo

cho mỗi mô hình.

Vì vậy, nó lớn hơn một chút so với những gì chúng ta đã làm trong video trước.

Bây giờ tùy thuộc vào bộ xử lý mà bạn có quyền truy cập, việc này có thể mất khoảng

25 phút chỉ để chạy.

Vì vậy, khi bạn thiết lập mã của mình, hãy kiểm tra mã đó trên các khối dữ liệu nhỏ, chẳng hạn như ba

lặp lại 10 thẻ mỗi lần.

Và nhân tiện, có nhiều cách để giảm thời gian tính toán này mà tôi sẽ thảo luận ở phần sau.

mã.

Một điểm nữa về bài tập này hơi khác so với đoạn mã chúng ta đã chạy

video trước đó.

Hãy nhớ rằng trong video trước, chúng tôi không thực sự nhập mã thông báo vào

Chức năng Maw.

Thay vào đó, chúng tôi nhập văn bản vào hàm Maw và nội bộ nó đang mã hóa

họ.

Điều tôi muốn bạn làm ở đây trong bài tập này và thực tế là trong toàn bộ thử thách viết mã này

là mã thông báo đầu vào chứ không phải văn bản.

Vì vậy, bạn thực sự không cần phải tạo văn bản ở đây.

Bạn cần tạo mã thông báo và bạn có thể để chúng dưới dạng mã thông báo.

Vì vậy, bây giờ bạn có thể tạm dừng video và thực hiện bài tập này và bây giờ tôi sẽ chuyển sang

mã.

Đây là nơi tôi đã cài đặt thư viện Maw.

Chúng ta sẽ sử dụng nó sau trong bài tập sau.

Dưới đây là các thư viện mà chúng ta sẽ sử dụng, trong đó có thư viện TQDM mà mình đã giới thiệu

bạn đến sớm hơn.

Được rồi, ở đây chắc chắn muốn chạy cái này trên GPU.

Nếu không, chúng tôi sẽ phải đợi nhiều ngày thay vì hàng chục phút để chạy phân tích.

Và ở đây tôi đang nhập GPT2 nhỏ và lớn đặt chúng sang chế độ eVal, đẩy chúng

vào GPU và nhập mã thông báo.

Được rồi, đây là mã cho bài tập một.

Vì vậy, mã này trông thực sự rất giống với mã từ bài tập trước trong phần

video trước đó.

Trên thực tế, tôi chỉ thay đổi một vài thứ.

Một là tôi đã mã hóa mềm số lần lặp lại và số lượng mã thông báo cho mỗi lần lặp lại.

sự lặp lại.

Và sau đó tôi cũng đang sử dụng thư viện TQDM này để cập nhật tiến độ.

Bây giờ tôi cũng đã đề cập trong video trước rằng ở đây tôi thực sự đang duyệt qua tất cả

100 lần lặp và sau đó tạo ra một lô có kích thước một trong mỗi lệnh gọi này tới

Tạo dấu chấm GPT.

Về lý thuyết, bạn không cần vòng lặp for.

Bạn có thể tạo tất cả 100 chuỗi gồm 400 mã thông báo cùng một lúc chỉ bằng cách nhập 100

bằng một tensor ở đây.

Về cơ bản là một lô cỡ 100.

Thật không may là nó bị lỗi, tôi có phiên Python, tôi hết RAM trên GPU và vì vậy tôi

không thể làm theo cách đó.

Vì vậy, tôi quyết định giữ nó đơn giản và dễ hiểu và lặp qua từng phần tử một

vì lợi ích của việc làm cho nó rất đơn giản.

Nó có nghĩa là phải mất lâu hơn một chút.

Có thể có sự cân bằng nào đó giữa tốc độ và kích thước lô.

Vì vậy, ví dụ, bạn có thể giả sử 10 lô 10, có thể 5 lô 20 cũng có thể

làm việc.

Nếu bạn muốn thử điều đó thì thật tuyệt.

Tôi chắc chắn khuyến khích bạn làm điều đó.

Tôi sẽ không làm điều đó ở đây chỉ vì muốn giữ mọi thứ đơn giản.

Và ở đây khi chúng ta thêm văn bản, hãy đảm bảo bạn bỏ qua mã thông báo đầu tiên

bởi vì đó là phần đầu của mã thông báo câu hoặc phần đầu của ID mã thông báo chuỗi.

Điều này không hữu ích, đây không phải là mã thông báo mà mô hình đã tạo nên chúng ta có thể bỏ qua điều đó.

Được rồi, vậy tất cả mã này là dành cho GPT2 và ở đây chúng ta có GPT2 lớn.

Đây là chuyện nhỏ, đó là điều tôi muốn nói.

Và thực ra còn một điều nữa tôi muốn nói, nếu bạn tạo theo đợt, thì hãy thực hiện

chắc chắn rằng cuối cùng bạn có một tập dữ liệu là một danh sách, một danh sách Python với mỗi phần tử

trong danh sách là 400 token.

Vì vậy, bạn không muốn kết quả này là tensor 100 x 400.

Nó phải là một danh sách gồm 100 phần tử danh sách.

Bây giờ chúng tôi có 4000 token cho mỗi mô hình.

Mục tiêu của bài tập hai là thực hiện phân tích MOV sử dụng sáu ngôn ngữ viết khác nhau của con người.

văn bản làm tài liệu tham khảo.

Bây giờ nghĩ lại công thức phân kỳ KL, ý tưởng là chúng ta giữ xác suất

phân phối p cố định và chúng tôi thay đổi phân phối q.

Bạn có thể sử dụng những cuốn sách mà chúng tôi đã sử dụng nhiều lần trước đây trong khóa học này.

Bây giờ để khớp số lượng mẫu và mã thông báo với dữ liệu mô hình, bạn cần trích xuất 100

lô 400 token từ mỗi cuốn sách này.

Vì vậy, điều đó có nghĩa là văn bản mẫu và văn bản con người sẽ có cùng số lượng

của các mục trong danh sách, mỗi mục có số lượng mã thông báo chính xác như nhau.

Vì vậy, điều đó giúp đảm bảo rằng chúng tôi có sự so sánh công bằng trong phân tích.

Vì vậy, nó tạo ra hai mô hình và sáu văn bản, mang lại cho chúng tôi tổng cộng 12 kết quả, 12 MOV

điểm số.

Bạn có thể sắp xếp điểm MOV thành các ô thanh và trực quan hóa chúng như thế này.

Vì vậy, đối với mỗi cuốn sách trên trục x, tôi có điểm MOV cho GPT2 nhỏ và lớn

phiên bản.

Bây giờ rõ ràng là bạn sẽ thấy được sự đa dạng trong những kết quả này và tôi muốn bạn

trước hết hãy nghĩ xem sự đa dạng đó có ý nghĩa gì và nó đến từ đâu.

Và thứ hai, tôi muốn bạn suy nghĩ về cách thiết lập đánh giá này một chút

khác nhau để chúng ta có thể đạt được điểm MOV cao hơn.

Bây giờ, bạn thực sự không cần phải thực hiện bất kỳ ý tưởng nào của mình vì chúng ta sẽ

làm điều đó trong bài tập thứ ba.

Vì vậy, ở bài tập thứ hai, bạn chỉ nên nghĩ về những gì bạn có thể làm để thay đổi điều gì đó

trong quá trình thiết lập đánh giá để đạt được điểm MOV cao hơn.

Tôi hy vọng bạn thích làm việc thông qua bài tập này.

Bây giờ bạn có thể tạm dừng video và chuyển sang mã và bây giờ tôi sẽ thảo luận về giải pháp của mình.

Vì vậy, ở đây tôi có danh sách các cuốn sách và đây là vòng lặp for chính.

Vì vậy, cách tôi chọn để thiết lập phân tích này là duyệt qua tất cả các cuốn sách, nhập

văn bản, tất cả những thứ này bạn đã thấy trước đây.

Đây chỉ là danh sách các nhãn trục x mà tôi sẽ sử dụng để tạo các biểu đồ thanh sau này

trên.

Ở đây tôi đang mã hóa văn bản.

Hãy nhớ rằng hiện tại chúng tôi không thực sự nhập văn bản vào phân tích MOV.

Trong video này, chúng tôi đang nhập mã thông báo.

Vì vậy, ở đây tôi nhận được một số phần tử mã thông báo liên tục ngẫu nhiên và nó sẽ là một loạt

có kích thước num đại diện là một biến tôi đặt là 100 và số mã thông báo tôi đặt là 400.

Được rồi, trong mỗi văn bản, tôi đang chạy phân tích MOV giống như bạn đã thấy trong phần

video trước cho GPT nhỏ và cho GPT lớn.

Vì vậy, điều này gần như giống hệt như cách thiết lập trong video trước ngoại trừ ở đó chúng ta

có dữ liệu văn bản nên những đầu vào này được gọi là p-text và ở đây tất nhiên chúng tôi đang sử dụng mã thông báo

chúng tôi sử dụng p-token và q-token.

Được rồi, bạn làm như vậy để chạy qua cả hai mô hình và sau đó tôi lưu kết quả đầu ra vào

ma trận này mà tôi gọi là MOV có kích thước 2 x 6 và chiều thứ hai dành cho chiều khác

sách và chiều thứ nhất dành cho hai mô hình đầu tiên.

Được rồi, việc này sẽ mất nhiều thời gian, tôi quên mất mất bao lâu, không quá lâu, vài

phút.

Mất khoảng 8 phút để chạy 6 văn bản, có thể là hơn 1 phút một chút

35, 40 giây cho mỗi lần so sánh này.

Được rồi, hãy xem đây là sơ đồ thanh, để tôi phóng to một chút ở đây và đây chúng ta

trước hết hãy xem điểm MOV khá thấp so với những gì chúng ta đã thấy ở phần trước

video.

Hãy nhớ trong video trước chúng ta có tập dữ liệu văn bản wiki và có điểm MOV

tôi nghĩ đó là 0,8 những gì tôi có trong video và những gì tôi trình bày trong các slide là 0,865 gì đó

như vậy và ở đây chúng ta thấy rằng các giá trị thấp hơn nhiều khoảng 0,1,05 chung

thứ tự độ lớn.

Vậy tại sao lại như vậy?

Trước hết, những văn bản này lớn hơn trong video trước nên có

sẽ có độ ổn định tăng lên do kích thước mẫu lớn hơn.

Điều đó nói lên những kích thước mẫu mà chúng tôi đang làm việc ở đây trong video này và cả trong

video trước đó thực sự nhỏ như nhỏ hơn 1 hoặc 2 bậc so với video trước đó

thực sự được khuyến nghị để có được thước đo ổn định thực sự tốt về điểm MOV.

Vì vậy, bạn có thể thấy rằng đây là một quá trình phân tích khá tốn thời gian nếu bạn thực sự muốn

để có đủ lượng dữ liệu.

Được rồi nhưng dù sao thì những điểm MOV này đều thấp hơn một chút và tại sao điều đó có thể xảy ra

vụ án?

Vâng, một điều cần lưu ý là đây đều là những cuốn sách khá cũ nên chúng ta có

Gatsby vĩ đại qua gương soi, Romeo và Juliet, Huck Finn, Edgar Ellen

Poe's, Tax và Goleverse Travels.

Đây đều là sách cũ.

Những điều này không được viết theo cách viết tiếng Anh hiện đại.

Vì vậy dù chỉ so sánh sự phân bổ văn bản từ hàng trăm cuốn sách của con người

của nhiều năm trước đối với văn bản của con người hiện được viết trên Wikipedia, những điều đó sẽ khá

hơi khác nhau hoàn toàn tách biệt khỏi mối quan hệ với đầu ra của mô hình.

Trên thực tế, tôi không coi đây là bài tập nhưng nếu tò mò, bạn có thể thực hiện phân tích đó.

Bạn có thể xem điểm MOV giữa văn bản Wikipedia của con người mà chúng tôi đã nhập và xử lý

với dữ liệu trong video trước và những cuốn sách kinh điển về con người mà chúng ta có trong video này.

Tôi chắc chắn rằng điểm MOV đó cũng sẽ khá thấp.

Vì vậy, điều đó thực sự chỉ ra rằng các mô hình này không hoạt động theo cách mặc định

Shakespeare viết tiếng Anh phải không?

Họ chỉ, bạn biết đấy, bạn nói chuyện với Chad Gbt hay Claude hay bất cứ điều gì và họ không nói như,

họ không viết theo phong cách Shakespeare trừ khi bạn yêu cầu họ làm vậy một cách cụ thể.

Vì vậy điều đó giải thích tại sao điểm MOV này lại thấp hơn.

Phần tiếp theo, phần cuối cùng của bài tập thứ hai là nghĩ ra một số cách để tăng điểm số này.

Vì vậy, chúng ta có cùng một mô hình và chúng ta có cùng một văn bản và bạn có thể

thậm chí chỉ cần nghĩ về một văn bản như hãy tập trung vào chuyến đi của Gulliver.

Chúng ta có thể làm gì để sửa đổi môi trường này để đưa thanh này lên đây để Gbt

lớn có cao hơn không?

Đó là điều chúng ta sẽ khám phá trong bài tập tiếp theo.

Bây giờ đối với bài tập thứ ba, mục tiêu ở đây là đạt được điểm MOV cao hơn.

Tôi tò mò muốn biết bạn đã có ý tưởng gì để tăng điểm.

Nếu bạn có ý tưởng khác với những gì tôi sẽ bảo bạn làm trong bài tập này, hãy thoải mái

để thử ý tưởng của bạn và nếu bạn nhận được kết quả thú vị, tôi rất vui được bạn chia sẻ

họ với chúng tôi trong phần hỏi đáp.

Dù sao đi nữa, đây là những gì bạn nên làm cho bài tập thứ ba.

Thay vì nhắc mô hình bằng mã thông báo trình tự bắt đầu và để mô hình

cứ làm bất cứ điều gì nó làm, bạn có thể nhắc mô hình với 100 mã thông báo đầu tiên cho mỗi mã

trình tự hàng loạt.

Vì vậy, mô hình đã bắt đầu với một số ngữ cảnh và sau đó bạn có thể tạo nó

400 mã thông báo mới dựa trên bối cảnh được nhắc ban đầu đó.

Hãy nhớ rằng bạn muốn có 400 mã thông báo được tạo theo mô hình, vì vậy hãy đảm bảo rằng các mã thông báo mà bạn

việc sử dụng cho lời nhắc được loại trừ khỏi đầu ra.

Nếu không thì đó chỉ là một sự nhầm lẫn trong quá trình phân tích và sau đó bạn có thể tính toán lại và in ra

điểm MOV nữa.

Tôi gọi phiên bản đầu tiên từ bài tập hai là điểm MOV ngây thơ và phiên bản này từ đây

bài tập thứ ba tôi gọi là điểm MOV nhắc.

Tôi đã sử dụng GPT2 lớn và các lô từ chuyến đi của Gulliver.

Bạn có thể sử dụng một cặp mô hình và văn bản khác nhau, chỉ cần đảm bảo rằng bạn

đang so sánh cùng một mô hình và cặp văn bản khi có và không có lời nhắc.

Được rồi, bạn nhìn thấy biển báo và bạn biết phải làm gì và bây giờ tôi cũng biết mình cần phải làm gì.

Vì vậy, bạn có thể thấy rằng mã này nhìn chung giống với mã trước đó trong bài tập

một nhưng có một điểm khác biệt chính ở đây đó là đầu vào được lấy từ dữ liệu của con người và

sau đó từ số lô B đến phần tử B và sau đó từ mã thông báo nhắc đầu tiên nên phần tử đầu tiên

100 token và đó là những gì tôi nhập vào mô hình.

Và sau đó đầu ra bây giờ sẽ chứa 500 mã thông báo, 400 mã thông báo mới được tạo

cộng thêm 100 token ngay từ đầu.

Được rồi, vậy trong số 500 token đó tôi chỉ lấy bậc thang, 400 token và tôi tiếp tục thêm vào

đó.

Được rồi, tập dữ liệu mới GPT2 lớn, tôi đang sử dụng lại dữ liệu con người có thể thay đổi mà tôi đã tạo trong

vòng lặp for ở đây, đây là từ bài tập hai và về cơ bản tất cả những gì tôi làm chỉ là không

chúng tôi chạy lại cái này.

Vì vậy, dữ liệu con người biến đổi này là từ lần lặp cuối cùng thông qua vòng lặp for này, có nghĩa là

cuốn sách cuối cùng có nghĩa là chuyến du hành của Gulliver.

Được rồi, vậy hãy xem nào, tôi nghĩ, ồ vâng, vậy nó tương ứng với thanh này ở đây và

có giá trị bằng số, điểm mob là 3.0,04, khá thấp.

Vì vậy, hãy nhớ rằng đó là từ lời nhắc ngây thơ nơi các mã thông báo mà mô hình tạo ra

hoàn toàn độc lập với các token lấy từ dữ liệu của con người ở đây.

Vậy hãy xem nào, vâng, đã trải qua và sau đó ở đây tôi tính điểm của đám đông và

đây tôi in nó ra.

Và điều này khá sốc, chúng ta nhận được từ giá trị từ 0,038 đến 0,821.

Vì vậy, đó giống như một sự gia tăng đáng kể về điểm số của đám đông.

Và hãy nhớ văn bản giống như phân bố xác suất Q, văn bản tham chiếu là

hoàn toàn giống nhau.

Đó chính xác là các mã thông báo giống nhau theo cùng một thứ tự, không có gì thay đổi.

Và mô hình cũng giống hệt nhau, GPT2 lớn ở cả hai loại này.

Sự khác biệt duy nhất giữa điểm này gần bằng 0 và điểm này gần bằng 1 là ở chỗ

mô hình ở đây giống như được gieo mầm từ văn bản của con người, từ cùng một cuốn sách, không có các mã thông báo chồng chéo,

phải không?

Nhưng mô hình sẽ thực hiện những lời nhắc này và tạo ra các mã thông báo phù hợp với ngữ cảnh, có nghĩa là

mô hình sẽ mô phỏng phong cách du lịch của Gulliver.

Tôi hy vọng bạn thấy video này là phần mở rộng mang tính khai sáng của video trước.

Phân tích đám đông và toàn bộ cách tiếp cận đánh giá mô hình dựa trên kết quả thống kê

việc phân phối token mà nó tạo ra rất thông minh.

Và đó thực sự là một cách tuyệt vời để khái niệm hóa một mô hình ở cấp độ diễn ngôn thay vì

ở cấp độ mã thông báo duy nhất.

Tuy nhiên, phương pháp này có một số sắc thái phức tạp mà bạn cần phải hiểu rõ nếu

đánh giá các mô hình dựa trên điểm số của đám đông.

Ví dụ: nếu bạn hướng dẫn cụ thể một mô hình ngôn ngữ viết đánh giá sản phẩm của Amazon

dựa trên mọi thứ nó biết về đánh giá sản phẩm của Amazon và sau đó bạn so sánh sự phân phối đó

so với các bài đánh giá do con người viết trên Amazon, điểm số của đám đông có thể thực sự rất cao.

Và điều đó có thể nói lên điều gì đó về tính đồng nhất của các đánh giá trên Amazon và mô hình

khả năng.

Nhưng điều đó không thực sự nói lên nhiều điều về khả năng của mô hình, chẳng hạn như gỡ lỗi mã

hoặc tóm tắt văn bản pháp luật bằng tiếng Trung cho người dùng nói tiếng Anh.