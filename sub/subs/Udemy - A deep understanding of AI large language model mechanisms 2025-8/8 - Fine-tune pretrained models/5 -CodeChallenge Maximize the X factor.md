# 5 -CodeChallenge Tối đa hóa hệ số X

---

Thử thách viết mã này bám sát thử thách viết mã mà chúng tôi đã thực hiện trong phần trước.

Đây là mặt tiêu đề của video đó. Bạn sẽ nhớ rằng mục tiêu trong video đó là tạo một hàm mất tùy chỉnh sử dụng khoảng cách KL để lấy mô hình GPT ngẫu nhiên của chúng tôi nhằm chọn mã thông báo có chứa chữ X.

x. Vậy thử thách mã mà bạn đang xem ở đây là phần tiếp theo của thử thách này. Chúng tôi sẽ sử dụng một

mô hình được đào tạo trước và bạn sẽ thấy rằng có một số thách thức nảy sinh ở đây mà chúng tôi không giải quyết được

thực sự chúng ta không phải lo lắng về điều đó ở phần trước. Trước khi bắt đầu

thử thách mã này, tôi khuyên bạn nên tìm và mở tệp sổ ghi chép đó từ video này,

bởi vì rất nhiều thách thức về mã này có thể được giải quyết bằng cách sao chép và sửa đổi mã

từ tệp mã được liên kết với video này. Được rồi, bài tập một là

nhập khẩu và kiểm tra mô hình trung bình GPT-2. Tôi đã đề cập trước đó rằng có

nhiều kích cỡ của GPT-2 có sẵn trong Ôm mặt và bạn cũng

có một video trong đó chúng tôi đã nhập bốn mẫu GPT2 khác nhau để đếm

các thông số. Đó là phần quay lại phần xây dựng GPT. Dù sao thì những gì tôi

muốn bạn làm ở đây là kiểm tra mô hình này và cũng kiểm tra cấu hình của nó

thuộc tính và cũng báo cáo số lượng khối máy biến áp trong mô hình này. Bây giờ trên

Một mặt, bạn có thể nhìn và thấy ngay tại đây

rằng mô hình này có 24 khối biến áp,

nhưng tôi muốn bạn viết mã để xuất ra số đếm đó

dựa trên kiến trúc này.

Vì vậy, đây chỉ là một chút bồi dưỡng thú vị

về việc truy cập các phần khác nhau của mô hình.

Thế là xong bài tập một.

Bạn không cần phải sử dụng mô hình

hoặc thiết lập đào tạo chưa.

Vì vậy bạn có thể dành thời gian khám phá mô hình này.

Một số thư viện mà chúng ta sẽ sử dụng bao gồm TextWrap

và hãy xem nào, ở đây tôi đang gọi phương tiện GPT-2.

Vì vậy hóa ra là nếu bạn muốn GPT-2 nhỏ,

bạn chỉ cần viết GPT-2 và bất kỳ kích thước nào khác,

bạn phải đề cập rõ ràng kích thước ở đó.

Được rồi, ở đây bạn cũng có thể thấy rằng tôi đang phân công

mã thông báo pad, theo mặc định là không có.

Nó trống để làm mã thông báo kết thúc chuỗi.

Bạn đã thấy điều đó trong video trước hoặc một vài video trước.

Được rồi, cái này sẽ mất, bạn có thể thấy nó là 1,5 gigabyte.

Vì vậy nó sẽ tải khá nhanh,

nhưng tải lâu hơn một chút so với

sang phiên bản nhỏ của GPT-2.

Được rồi, bây giờ chúng ta có thể in ra mô hình này, hãy xem.

bạn có thể thấy nó có nhúng từ mã thông báo

tức là 50.257 tương ứng với số

số mã thông báo trong từ vựng tăng thêm 1.024.

Vậy cái này đã lớn hơn GPT-2 nhỏ rồi

mà chúng tôi đã dành rất nhiều thời gian cho nó.

Hãy nhớ rằng thứ nguyên nhúng đó là 768

và bây giờ là 1.024.

Được rồi, chúng tôi cũng có tình trạng bỏ học, điều mà tôi sẽ không thảo luận.

Bây giờ chúng ta sẽ nói về điều đó sau trong phần này.

Và ở đây chúng ta thấy tất cả các mô-đun H, khối H.

Đây là những khối ẩn, đây là những khối máy biến áp.

Vậy có 24 người,

và tất cả đều bắt đầu với định mức lớp,

và sau đó là sự chú ý, bao gồm C sự chú ý và dự án C.

Vậy sự chú ý của C là 3000 x 1000.

Điều này tương ứng với WQ, WK và WV,

tất cả được nối với nhau.

Mỗi cái có 1024 bình phương.

Được rồi đi ra ngoài đây.

Và ma trận này ở đây là những gì tôi,

trong phần trước, cái tôi gọi là,

hoặc hai phần trước, cái mà tôi gọi là W0.

Đây là ma trận trộn tuyến tính

điều đó thu hút tất cả sự chú ý vào nhau

để họ có thể chia sẻ những gì họ đã học được

về văn bản.

Được rồi, ở đây chúng ta có các lớp MLP.

Đây là kết nối đầy đủ,

đây là cái mà tôi gọi là W1 hoặc lớp mở rộng.

Nó tăng từ một nghìn lên 4.000, tức là tăng gấp 4 lần.

Và sau đó proj là lớp co lại,

Tôi cũng gọi đây là W2, và nó tăng từ 4.000 lên 1.000.

họ. Được rồi, và cuối cùng, sau 24 người này, chúng ta có một lớp cuối cùng

chuẩn và đầu mô hình tuyến tính. Đây chỉ là lớp tuyến tính cuối cùng trên đầu mô hình.

Nó còn được gọi là lớp không nhúng, và tỷ lệ này là 50.000 x 1000. Tất nhiên, điều này tương ứng

đến thứ nguyên nhúng và đây là số phần tử trong từ vựng.

Được rồi, sau đó chúng ta có GPT2.config cung cấp thông tin bổ sung về mô hình

chúng tôi sẽ thường xuyên truy cập.

Đây là rất nhiều thông tin bạn sẽ thấy khi xem danh sách này ở đây, nhưng đây

là một cách hay để truy cập tất cả thông tin này.

Ví dụ: n nhúng, n vị trí, đây là dành cho các phần nhúng mã hóa vị trí và

vân vân.

Vì vậy, ở đây tôi đang nhận được GPT2.transformer.h và tôi đang nhận được độ dài của nó.

Và điều đó cho tôi biết có 24 khối máy biến áp.

Bây giờ đến bài tập thứ hai.

hàm mất tùy chỉnh mà chúng tôi đã tạo và sau đó tạo một phiên bản của hàm đó.

Đảm bảo mô hình và chức năng mất trên GPU và sau đó tạo một số dữ liệu

để đẩy qua mô hình.

Sau đó, bạn muốn kiểm tra kích thước đầu ra của mô hình.

Nếu bạn sử dụng kích thước lô là 4 và độ dài chuỗi là 64 thì bạn sẽ có thể nhận được

Những kết quả này là kích thước của đầu vào ngẫu nhiên cho mô hình

và các đầu ra tương ứng với các đầu vào ngẫu nhiên đó.

Nhưng những con số đó là gì?

Rõ ràng những thứ này là những con số,

nhưng chúng tương ứng với cái gì?

Chúng là softmax hay có thể là logsoftmax?

Có lẽ chúng là những bản ghi thô.

Bây giờ bạn có thể đã biết câu trả lời,

nhưng điều tôi muốn bạn làm ở đây là viết mã

để điều tra xem liệu kết quả đầu ra của mô hình

tuân theo phân bố xác suất

hoặc phân phối xác suất log.

Câu trả lời cho câu hỏi đó sẽ cho bạn biết

cách diễn giải kết quả đầu ra của mô hình.

Và sau đó trước khi nhập kết quả đầu ra của mô hình

vào hàm mất mát,

Tôi muốn bạn định hình lại kết quả đầu ra ba chiều

thành 2D.

Vì vậy, kết quả đầu ra từ mô hình là 4 x 64 x 50.000.

Và bạn muốn định hình lại nó thành ma trận 256 x 50.257.

Đó sẽ là ma trận mà bạn nhập vào

vào chức năng mất tùy chỉnh của chúng tôi.

Và phần cuối cùng của bài tập này

là để kiểm tra hàm mất mát bằng cách đưa một số dữ liệu vào đó.

Bạn không cần phải lo lắng về back prop hoặc gradient

hoặc trình tối ưu hóa hoặc bất cứ thứ gì tương tự.

Bạn chỉ muốn chắc chắn rằng chức năng mất hoạt động

mà không đưa ra bất kỳ lỗi nào.

Đó là bài tập thứ hai,

tạm dừng video và làm việc này.

Bây giờ tôi sẽ chuyển sang mã và thảo luận về giải pháp của mình.

Sau bài tập này, bạn sẽ sẵn sàng huấn luyện mô hình.

Vậy hàm mất mát ở đây gần như được sao chép hoàn toàn

sao chép từ video trong thử thách mã

ở phần trước.

Sự thay đổi duy nhất mà tôi đã thực hiện là

để chèn bình luận này ở đây.

Vì vậy chúng tôi muốn chắc chắn rằng chúng tôi thực sự

nhập xác suất nhật ký.

Đó là lý do tại sao điều cực kỳ quan trọng là phải biết

ý nghĩa là gì, giải thích là gì

của những con số mà mô hình đưa ra.

Được rồi, tôi chạy mã này ở đây,

Ở đây tôi tạo một thể hiện của hàm mất này

và đưa nó vào GPU.

Ở đây tôi đang tạo ra các số hoàn toàn ngẫu nhiên

và tôi không quan tâm những con số đó tương ứng với cái gì.

Tất cả những gì tôi đang làm là kiểm tra mã

để đảm bảo rằng nó không gây ra lỗi cho tôi

và để xem xét kích thước.

Được rồi, kích thước lô là 4, độ dài chuỗi là 54,

tạo số nguyên hoàn toàn ngẫu nhiên

giữa số 0 và kích thước từ vựng.

Bây giờ bạn sẽ thấy loại mã này

ngày càng thường xuyên hơn kể từ bây giờ trong văn bản.

Đặc biệt khi bạn có những mô hình rất lớn,

bạn muốn họ chạy qua một đường chuyền về phía trước

càng nhanh càng tốt,

có nghĩa là bạn muốn tắt mọi thứ trong mô hình

điều đó không liên quan đến việc chuyển tiếp.

Vì vậy, bạn có thể làm điều đó một phần bằng cách viết,

với ngọn đuốc.nograd.

Điều này vô hiệu hóa mọi thứ liên quan đến tính toán

và thiết lập gradient và đồ thị tính toán.

Đó là tất cả những gì về backprop.

Mọi thứ chúng tôi đang làm ở đây đều mang tính chuyển tiếp.

Vì vậy chúng ta có thể sử dụng withtorch.nograd.

Bạn cũng có thể quen thuộc với gpt2.eval

chuyển mô hình sang chế độ đánh giá.

Tôi sẽ thảo luận về điều này nhiều hơn một chút sau trong phần này.

Nếu bạn quen với việc chuyển đổi mô hình

vào chế độ eval và sau đó là chế độ đào tạo, không sao cả.

Bạn cũng có thể làm điều đó.

Hãy đảm bảo rằng sau khi bạn thực hiện động tác chuyển tiếp,

nếu bạn định đào tạo người mẫu,

bạn đưa nó trở lại chế độ luyện tập.

Được rồi, bây giờ tôi sẽ không lo lắng về điều đó nữa.

Được rồi, hãy xem nào.

Vì vậy, chúng tôi tạo ra một số dữ liệu.

Chúng ta thấy rằng đầu vào là 4 x 64,

và đầu ra là bốn đợt,

64 mã thông báo trong mỗi chuỗi,

và 50.000 tương ứng với từ vựng.

Được rồi, và một lần nữa, câu hỏi ở đây là liệu

đây là các bản ghi thô, nếu đây là các giá trị softmax,

hoặc nếu đây là các giá trị log softmax.

Vì vậy, những gì chúng ta có thể làm là đặt một số câu hỏi.

Chúng ta có thể tổng hợp tất cả các giá trị này.

Vì vậy bây giờ tôi chỉ chọn đầu ra.

Đây sẽ là tất cả 50.000 giá trị đầu ra

cho một mã thông báo cụ thể từ một lô cụ thể

và tổng hợp tất cả những điều đó.

Và con số đó sẽ là bao nhiêu?

Vâng, nếu đây đã là một phân bố xác suất,

thì kết quả ở đây, tổng ở đây phải là một.

Và mặt khác, có lẽ đây không phải là một,

thực sự hãy để tôi bình luận điều đó.

Được rồi, đây rõ ràng không phải là một.

Nó rất, rất xa so với một.

Được rồi, nhưng đủ công bằng.

có lẽ đây là đầu ra log softmax.

Và nếu đây là dữ liệu log softmax,

thì chúng ta sẽ mong đợi rằng nếu chúng ta lũy thừa chúng

để đảo ngược việc chuyển đổi nhật ký,

thì điều đó phải phù hợp với phân bố xác suất

và do đó tổng phải là một.

Và ở đây tổng về cơ bản là bằng không.

Con số này có vẻ lớn,

nhưng đây là lần 10 mũ trừ 32.

Vì vậy, đây là số 0 cộng với một số lỗi làm tròn cực kỳ nhỏ.

Được rồi, về cơ bản từ điều này,

chúng ta có thể kết luận rằng đầu ra của mô hình này

không phải là xác suất softmax,

nó cũng không phải là log softmax,

do đó là log thô,

điều này tốt cho một số ứng dụng,

nhưng vì mục đích của chúng tôi,

cho sự phân kỳ KL này, cho hàm này ở đây,

chúng tôi thực sự cần những thứ này để ghi lại xác suất.

Vậy điều đó có nghĩa là để sử dụng hàm mất mát này,

chúng ta cần chuyển đổi dữ liệu để ghi nhật ký softmax.

Được rồi, và tôi đang định hình lại đây.

Vì vậy, bạn thấy ở đây.

Vì vậy, chúng ta có xác suất log của các log,

đó là 4 x 64, sau đó tôi định hình lại nó

là 256 x 50.000.

Và đây là mặt nạ của hàm mất.

Bây giờ hai chiều này khớp nhau

và hàm phân kỳ KL trong Python

sẽ xem xét phân phối xác suất này.

Đây là phân phối Q.

Đây là dành cho phân phối P.

Và hàm, hàm PyTorch

sẽ phát đi phát lại thông tin này trên toàn bộ 256

của những phần tử này.

Vậy điều đó có nghĩa là điều này sẽ so sánh sự phân bố này

đến sự phân bố này cho mỗi phần tử trong số 256 phần tử này.

Được rồi, sau đó chúng ta có thể chạy cái này.

Một lần nữa, đây là mã thông báo ngẫu nhiên thuần túy.

Không có ý nghĩa gì đối với bất kỳ mã thông báo nào trong số này.

Tất cả những gì tôi muốn làm là đảm bảo rằng nó hoạt động

mà không đưa ra bất kỳ thông báo lỗi nào.

Bây giờ là lúc đào tạo mô hình.

Và thực ra, trước khi bạn huấn luyện mô hình,

bạn nên chạy mã mà chúng tôi đã viết

trong thử thách mã khác để đếm số lượng mã thông báo

mà mô hình tạo ra có chứa chữ X.

Sau khi chạy đánh giá đó,

sau đó bạn có thể đào tạo trong 300 kỷ nguyên.

Bạn có thể sao chép mã từ thử thách mã khác,

nhưng hãy lưu ý rằng bạn có thể cần

để thực hiện một số sửa đổi.

Vâng, vậy hãy luyện tập trong 300 kỷ nguyên,

sử dụng tỷ lệ học tập từ 10 đến âm sáu

và đào tạo trên tất cả các token, không chỉ các token cuối cùng.

Điều đó cũng hơi khác một chút so với cách chúng tôi thiết lập

thử thách mã trước đó.

Bây giờ, mẫu này lớn hơn GPT-2 Small một chút.

Vì vậy, thậm chí chỉ cần 300 đợt đào tạo về GPU

có thể mất vài phút.

Vậy một lần nữa, bạn muốn thiết lập mã này

có thể sử dụng 30 kỷ nguyên, có thể chỉ sử dụng ba kỷ nguyên,

chỉ để đảm bảo rằng mã của bạn chạy,

nó không có lỗi và bạn có thể sử dụng đầu ra.

Khi bạn cảm thấy thoải mái với mã vòng lặp đào tạo của mình,

sau đó bạn có thể tăng nó lên 300

rồi đi uống cà phê hay gì đó.

Dù sao đi nữa, sau khi khóa đào tạo kết thúc,

bạn có thể vẽ ra sự mất mát

và lặp lại đánh giá ưu tiên X một lần nữa.

Vì vậy hãy tạm dừng video và viết mã đi,

và bây giờ tôi sẽ chỉ ra giải pháp của mình.

Mã này ở đây đang được thiết lập để đánh giá.

Vì vậy, tôi bắt đầu với một chút văn bản mã,

tại sao con gà lại băng qua đường?

Và đẩy nó vào GPU ở đây.

Và sau đó tôi sẽ tạo ra một số văn bản,

lấy mẫu ngẫu nhiên, độ dài tối đa 200.

Được rồi, sau đó tôi sẽ in nó ra bằng textwrap.fill

và chiều rộng là 100.

Về cơ bản, điều đó sẽ bao bọc văn bản xung quanh

vì vậy nó dễ đọc hơn một chút.

Sau khi tôi làm điều đó, tôi sẽ lặp lại

tất cả các mã thông báo ở đầu ra

và xác định xem có dấu X trong văn bản đó không

tương ứng với chỉ số mã thông báo đó.

Nếu có X thì tôi tăng hasTarget lên một.

Và những gì bạn cũng có thể thấy ở đây

là tôi không thực sự giải mã tất cả đầu ra của mô hình.

Tôi đang bắt đầu từ độ dài của X và sau đó đi đến cuối.

Như tôi đã đề cập nhiều lần rồi,

những mô hình này, khi bạn gọi hàm tạo,

đầu ra sẽ bắt đầu với đầu vào.

Vì vậy, chúng tôi muốn bỏ qua đầu vào trong phép định lượng này ở đây.

Được rồi, vậy tại sao con gà lại băng qua đường?

Đây là những gì họ tìm thấy.

Điên rồi, có con gà băng qua đường không?

Được rồi, điều này thật tuyệt.

Truyền thuyết kể rằng, tuy nhiên, chúng ta tìm thấy ở đây

không có 192 mã thông báo nào thực sự chứa

chữ cái đích X rất nhỏ.

Bạn có thể thử chạy mã này nhiều lần.

Đôi khi bạn sẽ tìm thấy số không.

Bạn có thể tìm thấy một, hai, ba, bốn thẻ,

một cái gì đó như thế

Được rồi, bây giờ chúng ta đã sẵn sàng để luyện tập.

Tỷ lệ học tập rất nhỏ.

Chúng tôi thực sự không muốn đào tạo quá mức mô hình này

trên chữ X.

Được rồi, vậy hãy bắt đầu vòng đào tạo này tại đây.

Và bạn có thể thấy, vâng,

Tôi chỉ đang tạo một số token ngẫu nhiên,

mã thông báo ngẫu nhiên hoàn toàn vô nghĩa.

Chuyển tiếp, nhận kết quả đầu ra, đây là nhật ký.

Tôi chỉ nhận được đầu ra đầu tiên ở đây

bởi vì phần tử thứ hai trong bộ dữ liệu này

là những mất mát, đó không phải là điều chúng tôi muốn ở đây.

Chúng tôi chỉ muốn nhật ký đầy đủ.

Được rồi, sau đó tôi định hình lại, nó là 256 x 50.000,

chuyển đổi để ghi lại softmax và gọi hàm mất.

Sau đó tính toán tổn thất, thực hiện backprop,

và sau đó chọn ra số bị mất

để tôi có thể in nó ra đây,

và cũng vì vậy tôi có thể vẽ nó ngay sau đó.

Được rồi, số lỗ giảm từ sáu xuống còn hai.

Thật thú vị khi so sánh điều đó với những tổn thất gần bằng 0

mà chúng tôi đã tìm thấy ở vài video trước

với tốc độ học lớn hơn.

Vì vậy, hãy xem quỹ đạo mất mát trông như thế nào.

Khá đẹp và trơn tru đi xuống,

vâng, hai điểm gì đó.

Được rồi, bây giờ tôi có thể chạy lại mã này,

theo nghĩa đen là sao chép và dán,

và chúng tôi đang muốn xem

tại sao con gà lại băng qua đường?

Được rồi, trong trường hợp này, chúng ta có một trong số 39 token,

nhưng mô hình ở đây đã tạo ra phần cuối của mã thông báo văn bản.

Vì vậy, tôi sẽ chạy nó một lần nữa.

Được rồi, điều này thật thú vị.

Chúng tôi không nhận được 192 mã thông báo.

Và nhân tiện, tại sao đây chỉ là 192 mà không phải 200?

Bởi vì chiều dài tối đa là 200

và tám cái đầu tiên là thế này.

Cái này dài tám token,

và vì thế nó sẽ đạt mức tối đa

vì mã này là 192.

Được rồi, bạn có thể chạy nó nhiều lần,

và khá thú vị khi thấy tổn thất giảm xuống,

nhưng nhìn chung mô hình vẫn không tạo ra nhiều X.

Mục tiêu của bài tập 4

chỉ là để thử lại toàn bộ tệp mã,

nhưng với tốc độ học tập khác nhau.

Bạn không cần phải thay đổi tốc độ học tập một cách có hệ thống

ví dụ như vòng lặp for,

như chúng tôi đã làm một vài video trước đây.

Bạn chỉ có thể thay đổi tốc độ học tập

từ 10 đến âm 6 đến 10 đến âm 4,

và sau đó chỉ cần chạy lại toàn bộ tập lệnh từ đầu.

Tất nhiên, nếu bạn muốn điều tra kỹ lưỡng hơn

giống như chúng tôi đã làm một vài video trước đây, không sao cả, hãy tiếp tục.

Nhưng thực ra kết quả chính của bài tập 4

sẽ là cuộc kiểm tra chất lượng

của các token mà mô hình tạo ra.

Vì vậy, bạn biết phải làm gì.

Và bây giờ tôi sẽ chuyển sang mã.

Vì vậy nhìn lại, đây là lần chạy thứ hai.

Đây không phải là điều tôi đã cho bạn thấy trước đây.

Vẫn không có trong số 192 mã thông báo có chữ cái X.

x. Bây giờ bạn thấy tỷ lệ học là 10 trừ 4. Về cơ bản tất cả những gì tôi làm là thay đổi

cái này. Đó là số 6, tôi đổi thành số 4, rồi tôi chạy hết. Đó là tất cả những gì tôi đã làm.

Và bây giờ hãy nhìn vào tốc độ học tập này. Nó bắt đầu từ số 6, đó là khoảng thời gian khi chúng tôi

đã bắt đầu trước đó, nhưng với tốc độ học từ âm 10 đến âm 6, điều này chỉ

đã giảm xuống còn 2, bây giờ nó giảm xuống còn 0,001. Nhìn kìa. Đó là một điều hoàn toàn rất nhỏ

tốc độ học tập.

Được rồi, ở đây chúng ta có thể thấy rằng 192 trong số 192 mã thông báo có mục tiêu. Và đây là gì

gobbledygook mà người mẫu hiện đang sản xuất? Mô hình này bây giờ được đào tạo quá mức đến mức không thể tin được

để chọn chữ X, nó chỉ là,

nó thậm chí không chọn các từ có dấu cách trong đó.

Đó chỉ là những token có X ở khắp mọi nơi.

Nó không có ý nghĩa gì cả, không có ý nghĩa gì cả.

Hãy xem xét, bạn biết đấy, so sánh nó với mã này ở trên đây,

chính xác cùng một mô hình.

Đây là bước tinh chỉnh trước rất phổ biến,

Ý tôi là, bạn biết đấy, cá có thực sự xấu xa không?

Được rồi, có lẽ đây là ngôn ngữ hài hước,

nhưng ít nhất nó hợp lý.

ít nhất đó là tiếng Anh.

Tinh chỉnh là khá khó khăn.

Ý tôi là, về mặt khái niệm, nó rất đơn giản và dễ hiểu,

nhưng ma quỷ ở trong các chi tiết.

Và vấn đề về các hệ thống lớn, phức tạp

là thường rất khó để đưa ra những dự đoán chính xác

về cách họ sẽ cư xử trong những tình huống khác nhau.

Vì vậy, thực tế là việc tinh chỉnh trong thực tế

thường bao gồm rất nhiều thử nghiệm,

điều chỉnh, thay đổi mọi thứ, thử những thứ khác,

thử những thứ khác nhau,

thử kết hợp nhiều thứ khác nhau, v.v.