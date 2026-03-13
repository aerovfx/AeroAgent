# 2 -Các vấn đề về số trong logits và dịch softmax

---

Bạn đã gặp và sử dụng softmax nhiều lần trong khóa học này và có thể

trong các khóa học hoặc ứng dụng khác.

Điều tôi sắp thảo luận trong video này là một số vấn đề về số có thể phát sinh khi tính toán

softmax từ các giá trị logic thô, đặc biệt là trong các mô hình rất lớn với từ vựng rất lớn.

Đây là một vấn đề khá nghiêm trọng, nhưng may mắn thay có một cách khắc phục thực sự đơn giản.

Và hóa ra hàm PyTorch Softmax thực hiện kiểu chuẩn hóa này.

Đây là slide bạn đã xem trước đây trong khóa học.

Tôi chỉ muốn nhắc các bạn thật nhanh về công thức biến đổi Softmax

và mục tiêu của Softmax.

Vì vậy, Softmax chỉ có nghĩa là lấy số mũ tự nhiên của một số nào đó và chia nó cho tổng

trên tất cả các số mũ tự nhiên của toàn bộ tập dữ liệu, do đó, tất cả các giá trị có liên quan.

Các giá trị Softmax thu được là không âm và chúng được chuẩn hóa sao cho chúng tạo thành

một phân bố xác suất.

Trong học máy và học sâu, mục tiêu của chuyển đổi Softmax là chuyển đổi

bất kỳ tập hợp giá trị tùy ý nào thành hàm xác suất.

Trong LLM, các giá trị này tương ứng với nhật ký đầu ra, là các số cho mỗi giá trị có thể

dấu hiệu trong từ vựng.

Và chúng tôi muốn Softmax nếu chúng tôi đang cố gắng đạt được phân phối xác suất trên tất cả

các mã thông báo để tạo ra các mã thông báo mới theo xác suất.

Được rồi, đó chỉ là một lời nhắc nhở rất nhanh.

Đây là những gì chúng ta sẽ làm trong bản demo Python.

Mình định import GPT2 bản nhỏ và GPT2 bản lớn, push một ít chữ

through chỉ để lấy nhật ký đầu ra.

Hãy nhớ rằng chúng có cùng mã thông báo và cùng kiến trúc, mặc dù số lượng

Các tham số và lớp khác nhau giữa phiên bản nhỏ và lớn của GPT2.

Vì vậy, mặc dù tôi đã đẩy chính xác các mã thông báo giống nhau và tôi đang xem nhật ký

đối với cùng một mã thông báo trong chuỗi, các giá trị số thô thực sự rất lớn

khác nhau, giống như một thứ tự độ lớn.

Ở đây bạn sẽ thấy biểu đồ của nhật ký từ GPT2 nhỏ so với GPT2 lớn.

Và mặc dù chúng chắc chắn có mối tương quan với nhau nhưng rõ ràng hai mô hình đang xử lý những điều này

mã thông báo ít nhất theo những cách hơi khác nhau.

Nhưng đó không phải là trọng tâm chính của video này.

Điều tôi sẽ làm tiếp theo là Softmax, những giá trị logit này để chuyển chúng thành xác suất

phân phối.

Và thật không may đã xảy ra sự cố.

Nó hoạt động với GPT2 lớn, nhưng ở đây chúng ta chỉ có được hình ảnh hai chú thỏ trắng trong

một cơn bão tuyết.

Vì vậy, điều gì đó khủng khiếp đã xảy ra trong quá trình chuyển đổi, mặc dù bản thân mã giống hệt nhau.

Và khi tôi chuyển sang mã Python, tôi sẽ giải thích điều gì đã xảy ra và tại sao nó lại xảy ra.

Sau đó, tôi sẽ áp dụng một phép chuẩn hóa siêu đơn giản cho dữ liệu logic để chúng ta thực sự có thể

tính toán Softmax.

Và sự chuyển đổi này thực sự đơn giản.

Tất cả những gì tôi làm là chuyển toàn bộ phân phối lên một chút.

Và sau đó tôi sẽ cho bạn thấy rằng kiểu chuẩn hóa này được thực hiện nội bộ trong PyTorch's

Chức năng Softmax.

Dưới đây là những thư viện mà chúng ta sẽ cần.

Ở đây tôi đang nhập hai phiên bản GPT2, phiên bản nhỏ và phiên bản lớn.

Tất nhiên tất cả đều dựa vào cùng một mã thông báo, vì vậy chúng tôi chỉ cần điều đó một lần.

Và bạn có thể thấy tôi đang gọi những biến này là GPT2 nhỏ và lớn.

Được rồi, trong ô mã này, tôi chỉ lấy một số dữ liệu từ các mô hình.

Tôi thực sự không quan tâm nó là gì.

Đó chỉ là một dòng văn bản ngẫu nhiên.

Nhưng về cơ bản, tôi chỉ muốn một vài mã thông báo được xử lý để tôi có thể nhận được nhật ký sắp tới

ra khỏi mô hình.

Nhân tiện, tôi đang chạy mã này trên CPU chứ không phải trên GPU.

Nếu bạn chỉ sử dụng những mô hình này để chạy một chút về phía trước ở đây và ở đó,

bạn không thực sự thực hiện bất kỳ phép tính phức tạp hay phản hồi hay bất cứ điều gì, thì

có lẽ tốt hơn là cứ gắn bó với CPU.

Việc này dễ dàng hơn một chút và bạn không sử dụng hết tài nguyên GPU.

Được rồi, vậy là không mất quá nhiều thời gian.

Và bây giờ điều tôi đang làm chỉ là trích xuất logit cuối cùng.

Vì vậy, đây là một chuỗi, có nghĩa là có kích thước lô là một.

Vì vậy, đây là phần tử đầu tiên trong thứ nguyên lô, thực tế là phần tử duy nhất trong

kích thước lô.

Thực ra đây, hãy để tôi làm điều này.

Chỉ để đảm bảo điều này thực sự rõ ràng, Outputs.small.shapes.

Được rồi, đây là, ôi, tôi muốn, uh, logits.shapes.

Được rồi, vậy chúng ta có một vì chỉ có một trình tự, bảy vì điều này cuối cùng đã trở thành

bảy mã thông báo và 50.000 vì hóa đơn bị lật 50.000.

Được rồi, để thuận tiện, tôi chỉ trích xuất mã thông báo cuối cùng.

Chúng tôi thực sự chỉ cần một số con số để chơi đùa.

Được rồi, sau đó tôi sẽ vẽ biểu đồ nhật ký cho GPT nhỏ, cho GPT lớn và sau đó

một âm mưu phân tán của hai cái này với nhau.

Chính xác là con số mà tôi đã trình bày trong các slide cách đây một lúc.

Uh, vâng, và chủ yếu điều tôi muốn chỉ ra ở đây là hai điều.

Thứ nhất, chúng ta có được dữ liệu hợp lệ, chúng ta có được một âm mưu.

Vì vậy, không có gì sai với những dữ liệu này vào thời điểm tôi đang tạo biểu đồ này.

Đó sẽ là kiến ​​thức phù hợp cho cốt truyện tiếp theo.

Và chúng tôi cũng thấy rằng có sự khác biệt rất lớn về số lượng giữa các log, các log thô

xuất ra từ GPT thành nhỏ so với lớn.

Tại sao điều đó xảy ra?

Về cơ bản nó chỉ liên quan đến việc chuẩn hóa, v.v.

Nhưng điều đó không quan trọng.

Điều quan trọng là những con số này nhỏ hơn những con số này, hoặc ít nhất là nhiều hơn

tiêu cực.

Được rồi, điều tôi làm ở đây là tính softmax bằng cách triển khai trực tiếp công thức.

Công thức cực kỳ đơn giản, chúng ta chỉ cần lấy tất cả dữ liệu của mình và nói e cho các giá trị dữ liệu.

Đây là z mà tôi đã trình bày trong công thức ở các slide cách đây vài phút, chia cho

tổng của từng số đó.

Vì vậy, tôi làm điều đó cho cái nhỏ và cái lớn.

Và sau đó tôi vẽ lại nó.

Và bây giờ chúng ta thấy điều gì đó kỳ lạ đang xảy ra.

Và điều kỳ lạ đang xảy ra là ở đây không có gì dành cho GPT nhỏ cả.

Chúng tôi nhận được dữ liệu cho GPT ở mức độ lớn nhưng không thu được ở mức độ nhỏ.

Và chuyện gì đang xảy ra vậy?

Vì vậy chúng ta hãy nhìn vào điều này.

Biến này đây, đây là softmax hướng dẫn sử dụng nhỏ.

Đó là dữ liệu mà tôi đang cố gắng vẽ ở đây.

Tất cả đều là NAN.

Tại sao tất cả đều là NAN?

Một lần nữa, chúng ta có thể xem công thức này và chúng ta lấy NAN ở đâu?

NAN đến từ việc chia 0 cho 0.

Vậy có lẽ chúng ta đang chia 0 cho 0 ở đây.

Về lý thuyết thì điều đó không nên xảy ra, nhưng có lẽ nó đang xảy ra.

Được rồi, đầu tiên chúng ta hãy xem xét, ở đây tôi chỉ chọn một số số ngẫu nhiên.

Vậy 10.000 và logic cho chỉ số mã thông báo 10.000 là âm 123.

Đó không phải là một con số cực đoan.

Chúng tôi không vượt quá giới hạn tính toán của CPU với con số 123.

Nhưng hãy nhớ rằng khi bạn lấy số mũ tự nhiên của một số âm thì số đó biến mất

về không.

Vậy trên thực tế, con số này ở đây, theo lý thuyết, không phải bằng 0, phải không?

E đến bất cứ thứ gì không bao giờ bằng không.

Nhưng con số này đủ nhỏ để PyTorch chỉ coi nó bằng 0.

Vì vậy, khi chúng ta lấy E cho tất cả các số này, thì chúng ta nhận được rất nhiều số 0 và

sau đó, chúng ta tổng hợp rất nhiều số 0 và chúng ta nhận được số 0.

Và cái này ở đây, đây chính xác là mẫu số trong softmax ở đây.

Nó trông hơi khác trong mã vì ở đây tôi đang sử dụng các hàm và ở đây tôi

chỉ cần gọi các phương thức trực tiếp trên tensor này, nhưng điều đó không thành vấn đề.

Vì vậy, chúng tôi đang chia cho số không.

Bây giờ tôi chỉ muốn cho bạn thấy các thư viện khác nhau giải quyết những vấn đề kỳ diệu mới này

theo những cách khác nhau.

Vậy nếu chúng ta nói, thì ở đây tôi chỉ nói, bạn biết đấy, một số biến bằng trừ 123.

Trong NumPy, tôi không nhận được số 0, mặc dù điều này không thực sự có thể phân biệt được với số 0.

Đó là 10 mũ âm 54.

Đó là một con số điên rồ và nhỏ bé.

Và ở PyTorch, chúng tôi thực sự nhận được con số 0.

Được rồi, nhưng nó không quan trọng.

Ngay cả khi chúng tôi chạy những phép tính này trong NumPy, thay vì trong PyTorch, chúng tôi sẽ

vẫn nhận được những kết quả vô nghĩa, không đáng tin cậy.

Được rồi, bây giờ tôi đang áp dụng một chuẩn hóa siêu phức tạp cực kỳ phức tạp.

Tôi chỉ đùa thôi.

Việc bình thường hóa thực sự đơn giản.

Tất cả những gì tôi đang làm là lấy giá trị lớn nhất và trừ nó khỏi tất cả các giá trị.

Và điều đó có tác dụng gì?

Điều đó chỉ lấy toàn bộ phân phối này ở đây và dịch chuyển nó lên sao cho giá trị lớn nhất

là số không.

Và bạn thấy ở đây.

Vì vậy, cốt truyện này thực sự giống hệt với cốt truyện mà tôi vừa trình bày lúc trước,

nhưng tất cả các giá trị số đã được dịch chuyển sao cho giá trị lớn nhất bằng 0 cho cả hai

GPT2 nhỏ và lớn.

Tất nhiên, mối quan hệ này không thay đổi.

Giá trị trục x thay đổi, giá trị trục y thay đổi.

Được rồi, bây giờ tôi cũng sẽ lặp lại chính xác đoạn mã này ở đây.

Vì vậy, đoạn mã tạo ra hình này có vấn đề.

Và bây giờ tôi đang tạo lại bản sao chép theo đúng nghĩa đen này.

Điều duy nhất tôi làm là thay đổi tên biến thành chuẩn và chữ N viết hoa ở đây

thay vì các bản ghi thô mà tôi đã lấy ra.

Và bây giờ không có vấn đề gì.

Bây giờ chúng tôi nhận được kết quả hợp lệ trong cả hai trường hợp.

Thật khó để hình dung vì về cơ bản, tôi không biết liệu bạn có thể thấy điều này trên máy tính của mình không

màn hình bạn đang xem video này, nhưng nếu bạn chạy mã Python này, bạn sẽ

có thể nhìn thấy có một chấm nhỏ ở đây.

Và về cơ bản đó là dự đoán của mô hình về loại token nào sẽ xuất hiện tiếp theo.

Vậy với xác suất softmax, tất cả những con số này đã bị nén xuống 0 và có

một điểm dữ liệu ở trên đó.

Chúng ta có thể thấy điều đó ở đây khi nhìn vào nhật ký thô, đó là giá trị

ở đây trong GPT lớn.

Nó có giá trị ở đâu đó khoảng 10, logit ở đâu đó trên 10.

Và về cơ bản, softmax sẽ lấy phần còn lại của bản phân phối này và đè bẹp nó

xuống sao cho nó không chính xác bằng 0, mà rất nhỏ, rất gần bằng 0.

Được rồi, bạn thấy ở đây, bạn thấy ở đây.

Được rồi, nhưng vấn đề là chúng ta đã đúng, giống như những con số hợp lệ bây giờ chỉ bằng cách áp dụng điều này

chuẩn hóa rất đơn giản trong đó chúng ta dịch chuyển các giá trị và điểm dịch chuyển các giá trị

chỉ để phạm vi số lớn hơn một chút.

Vì vậy, bây giờ tôi có thể chạy lại mã này.

Hãy để tôi quay lại đây và chúng ta có thể nhìn vào, xem nào, bây giờ cái này được gọi là, ồ không,

nó được gọi như thế này

Vâng, điều này chỉ để cho bạn thấy chúng tôi có được những con số hợp lệ.

Và đây, để tôi xem.

Vì vậy, bây giờ hãy nhớ từ dữ liệu ban đầu bằng 0, và bây giờ với những dữ liệu này, nó là

biến này có bằng không không.

Cái đó đến từ đây.

Được rồi, vậy bây giờ chúng ta có giá trị âm 16.

Và khi lũy thừa nó, chúng ta vẫn nhận được một con số nhỏ, nhưng chắc chắn khác không.

Được rồi, rất đẹp.

Vì vậy, điều cuối cùng tôi muốn thảo luận là chức năng softmax của PyTorch.

Vì vậy, f dot softmax và sau đó tôi không nhập các giá trị chuẩn hóa.

Chúng được gọi như thế này, nhưng thay vào đó chỉ là nhật ký đầu ra thô từ hai mô hình,

đây chính xác là những dữ liệu đã gây rắc rối cho chúng tôi trước đây khi tính toán thủ công

softmax.

Và bây giờ chúng ta thấy rằng chúng ta nhận được các giá trị bình thường ở đây.

Và một lần nữa, bạn thấy những giá trị bình thường này.

Bây giờ tài liệu softmax không nêu rõ rằng họ áp đặt kiểu chuẩn hóa này,

nhưng bạn thấy khá thường xuyên trong các hàm PyTorch mà họ đã xây dựng sẵn các cơ chế để xử lý

với khả năng, nguy cơ mất ổn định về số lượng.

Nhưng bạn có thấy ở đây họ viết rescale để các phần tử nằm trong phạm vi 0

đến một và tổng thành một.

Vì vậy, về cơ bản họ đang thêm một số yếu tố chuẩn hóa để đảm bảo hoặc để đảm bảo rằng

đầu ra thực sự là một phân bố xác suất.

Tôi hy vọng bạn thấy video này sâu sắc.

Tôi không muốn bạn nghĩ rằng bạn không bao giờ nên tính toán softmax bằng cách thực hiện

công thức trực tiếp rất thường xuyên đó là một điều hoàn toàn tốt đẹp và an toàn để làm.

Nhưng có những điều cần cân nhắc khi làm việc với các mô hình cực lớn mà về cơ bản bạn sẽ

không bao giờ phải suy nghĩ khi làm việc với các mô hình nhỏ hơn.

Và trong video này tôi đã nêu bật một ví dụ về điều đó.