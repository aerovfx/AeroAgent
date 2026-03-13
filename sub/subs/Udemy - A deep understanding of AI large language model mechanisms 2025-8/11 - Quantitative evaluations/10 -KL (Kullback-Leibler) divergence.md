# Dịch phân kỳ 10 -KL (Kullback-Leibler)

---

Cho đến nay trong phần này, tôi đã tập trung vào đánh giá cấp độ mã thông báo và đánh giá cấp độ câu.

Bây giờ tôi sẽ giới thiệu cho bạn một mức độ đánh giá cao hơn về việc tạo ra ngôn ngữ, đó là

để tập trung vào số liệu thống kê phân phối của chuỗi mã thông báo dài hơn mà mô hình

đầu ra.

Ý tưởng là để xem liệu xác suất phân phối mã thông báo mà mô hình tạo ra có nhất quán hay không

với việc phân phối các token từ văn bản viết của con người.

Tôi sẽ tìm hiểu chi tiết về cách thức hoạt động của các loại phương pháp này trong video tiếp theo và trong

video này, tôi sẽ cho bạn biết về cách định lượng chính của số liệu thống kê phân phối,

dựa trên thước đo gọi là phân kỳ Kolbach-Lybler, thường được đơn giản hóa thành phân kỳ KL,

và nó còn được gọi là khoảng cách KL vì nó có thể được dùng làm thước đo khoảng cách.

Trên thực tế, tôi đã giới thiệu cho bạn về phân kỳ KL trước đó trong khóa học, mặc dù

Tôi không đi sâu vào chi tiết về toán học.

Vì vậy, hãy tưởng tượng rằng chúng ta có hai phân bố xác suất được biểu thị bằng hai đường màu khác nhau này.

X sẽ tương ứng với tất cả các mã thông báo trong từ vựng và có lẽ dòng màu cam là

xác suất của các mã thông báo khác nhau được quan sát thấy trong văn bản viết của con người, ví dụ: trong Wikipedia

các bài viết và đường màu vàng là phân bổ xác suất trên các mã thông báo mà LLM đã tạo.

Bây giờ nếu chúng ta muốn mô hình ngôn ngữ tạo ra văn bản có cùng mức phân bổ với ngôn ngữ của con người

văn bản bằng văn bản thì chúng ta muốn hai dòng này thật giống nhau.

Ở đây chúng không thực sự giống nhau đến thế, điều này cho thấy số liệu thống kê toàn cầu

xác suất mã thông báo là khác nhau giữa mô hình và con người.

Tất nhiên, tất cả những điều này phụ thuộc nhiều vào việc chọn đúng đoạn văn bản.

Ví dụ: nếu dòng màu cam là văn bản Twitter do con người viết và dòng màu vàng là mã Python do AI viết,

thì chúng ta thực sự sẽ không mong đợi hoặc thậm chí không muốn hai bản phân phối đó giống nhau như vậy.

Việc chọn văn bản tham khảo chính xác thực sự quan trọng và tôi sẽ nói nhiều hơn về điều đó trong hai video tiếp theo.

Vì vậy, đây lại là công thức tính phân kỳ KL.

Đó là xác suất của X, do đó P của X nhân log của P chia cho Q.

Bây giờ khi bạn tổng hợp tất cả các giá trị đó của X, nó sẽ cho ra một số,

và đó là giá trị phân kỳ KL.

Trong bối cảnh học sâu, nó thường được sử dụng như một hàm mất mát.

Bạn sẽ nhớ rằng chúng ta đã sử dụng chính xác số đo này làm hàm mất mát ở phần trước của khóa học,

trong các video mà chúng tôi đã huấn luyện một người mẫu để thích các mã thông báo có chữ X trong đó.

Thực ra chúng tôi đã làm điều đó hai lần trong hai video riêng biệt.

Bây giờ trong vài video tiếp theo về đánh giá,

chúng ta sẽ sử dụng công thức này không phải như một hàm mất mát mà như một cách đo lường sự giống nhau giữa văn bản LLM và văn bản con người.

Bây giờ chúng ta hãy dành một chút thời gian và suy nghĩ xem những giá trị khác nhau này có thể có ý nghĩa gì.

Trước hết, bạn luôn cần chỉ định một phân phối xác suất làm đầu vào và phân phối xác suất còn lại làm mục tiêu.

Phân bố xác suất đầu vào là phân bố mà bạn đang xem xét,

và mục tiêu là phân phối mà bạn đang sử dụng làm tài liệu tham khảo hoặc so sánh.

Tôi sẽ giới thiệu cho bạn về Python ngay lúc điều đó tạo nên sự khác biệt lớn,

và bạn nhận được các kết quả khác nhau tùy thuộc vào phân phối mà bạn coi là mục tiêu.

Thứ hai, bạn phải đảm bảo rằng đây thực sự là phân bố xác suất

tuân theo hai điều kiện của phân bố xác suất thực.

Vậy tất cả đều không âm và chúng có tổng bằng một.

Nếu bạn cố gắng sử dụng các vectơ ở đây không phải là phân bố xác suất đúng,

bạn sẽ nhận được kết quả kỳ lạ, không thể giải thích được và không chính xác.

Thứ ba, tôi sẽ cho bạn thấy ngay trong bản demo Python rằng PyTorch mong đợi P là xác suất ghi nhật ký,

và bạn có thể nhập liệu Q ở dạng xác suất thô hay xác suất nhật ký,

chỉ là một cái gì đó cần lưu ý về việc thực hiện.

Dù sao đi nữa, chúng ta hãy nhìn vào công thức này và suy nghĩ về cách diễn giải nó.

Đầu tiên, hãy xem xét trường hợp hai phân phối P và Q hoàn toàn giống nhau.

Trong trường hợp đó, P trên Q là một.

Log của một bằng 0, điều đó có nghĩa là độ phân kỳ KL sẽ bằng 0.

Vì vậy, đó là giá trị nhỏ nhất có thể mà chúng ta có thể mong đợi.

Và hai phân bố xác suất càng khác nhau thì độ phân kỳ KL càng lớn.

Không có giới hạn trên, nên phân kỳ KL có thể ngày càng lớn hơn,

phát triển không giới hạn khi sự phân phối trở nên khác nhau hơn.

Điểm cuối cùng tôi muốn thảo luận về phương trình này là phân kỳ KL không âm,

vì vậy nó có thể bằng 0 hoặc dương, nhưng không thể âm.

Bây giờ điều đó ban đầu có vẻ phản trực giác, bởi vì các giá trị trong đó Q lớn hơn P,

thì tỷ lệ này sẽ nhỏ hơn một và log của tỷ lệ đó sẽ âm.

Vì vậy, thực sự có thể có các giá trị âm trong tổng này, mặc dù tất cả chúng sẽ bị loại bỏ,

và nó sẽ luôn luôn tích cực.

Có một bằng chứng toán học dài hơn giải thích tại sao điều đó lại xảy ra.

Tôi sẽ không đi qua bằng chứng đó, nhưng tôi sẽ cho bạn biết một số trực giác.

Vì vậy, trực giác là bạn có thể coi đây là một tỷ lệ có trọng số.

Vì vậy tỷ lệ này được tính theo phân phối xác suất P.

Bây giờ bất cứ nơi nào Q lớn hơn P, điều đó có nghĩa là P sẽ nhỏ,

điều đó có nghĩa là số âm trong nhật ký sẽ có tác động nhỏ hoặc rất nhỏ đến tổng.

Và ngược lại, ở đâu P lớn hơn Q thì tỷ lệ này sẽ lớn hơn một,

và nhật ký sẽ dương và các trọng số đó sẽ tương đối lớn hơn.

Vì vậy, bạn thực sự có thể nhận được các giá trị âm bên trong tổng,

nhưng bạn sẽ không bao giờ có được khoảng cách KL âm.

Và thực tế, nếu bạn thực hiện một phân tích mà nhận được kết quả âm tính,

thì chắc chắn là do đã xảy ra sự cố và có thể là do đã xảy ra sự cố

là các phân phối không được chuẩn hóa thành phân phối xác suất thực.

Được rồi, đây là những gì chúng ta sẽ làm trong bản demo Python.

Tôi sẽ tạo hai bộ dữ liệu gồm các số ngẫu nhiên,

và sau đó tính toán phân bố xác suất của chúng, bạn có thể thấy ở đây.

Bạn có thể thấy rằng cả hai phân bố xác suất này đều tương tự nhau,

nhưng rõ ràng là không giống nhau.

Sau đó, tôi sẽ tính toán độ phân kỳ KL bằng cách thực hiện trực tiếp phương trình

mà tôi đã trình bày trong slide trước trong NumPy và tôi đã nhận được những kết quả này.

Hãy nhớ rằng tôi đã nói rằng bạn nhận được những kết quả khác nhau,

tùy thuộc vào phân phối xác suất mà bạn xem xét phân phối mục tiêu.

Sau đó tôi sẽ chỉ cho bạn cách triển khai phân kỳ KL bằng PyTorch

và xác nhận rằng chúng tôi nhận được kết quả tương tự như khi triển khai thủ công trong NumPy.

Bây giờ, việc triển khai trong PyTorch hơi khác một chút,

bởi vì như bạn đã học trước đó trong khóa học,

khi chúng tôi tạo ra các hàm mất mát cho phân kỳ KL,

PyTorch mong đợi xác suất ghi nhật ký thay vì xác suất thô.

Dù sao, hãy chuyển sang mã và xem xét.

Một số thư viện ở đây tôi đang tạo hai bản phân phối.

Vì vậy, chúng tôi có cỡ mẫu là 10.000.

Những dữ liệu này được gọi là phân phối log bình thường.

Nó gần giống như một phân phối bình thường,

và bạn đẩy nó qua hàm mũ tự nhiên.

Mọi người luôn hỏi tôi trong các khóa học về thống kê và học máy,

tại sao điều này được gọi là phân phối nhật ký bình thường khi không có thông tin đăng nhập ở đó?

Bạn sẽ không gọi đây là phân phối log bình thường chứ?

Câu trả lời cho câu hỏi đó là nếu bạn lấy nhật ký

của phân phối chuẩn logarit, bạn sẽ có phân phối chuẩn,

bởi vì log và số mũ tự nhiên là hàm nghịch đảo của nhau.

Được rồi, điều đó không liên quan gì đến sự phân kỳ KL.

Được rồi, ở đây tôi chỉ muốn nói là căn giữa và tính điểm Z,

thực ra chỉ là dịch chuyển nó một chút thôi.

Và ở đây tôi có phân phối chuẩn chuẩn,

cũng được ghi điểm Z, mặc dù điều đó không thực sự cần thiết

vì sự phân phối này.

Nhưng dù sao đi nữa, ở đây tôi tính toán biểu đồ của chúng,

và ở đây tôi chuyển đổi sang ước tính mật độ xác suất bằng cách chia cho tổng.

Bây giờ, tại sao tôi lại làm những việc này khi tôi đã có dữ liệu?

Vâng, thứ chúng ta cần đánh giá không phải là dữ liệu,

nhưng phân phối xác suất của dữ liệu.

Vì vậy, phân kỳ KL không được tính toán từ dữ liệu.

Nó được tính toán từ phân phối xác suất trên dữ liệu.

Bây giờ, nếu bạn đang làm việc với các hàm toán học thuần túy,

bạn có các hàm tạo khoảnh khắc,

bạn có thể nhận được bản PDF thuần túy.

Nhưng trong dữ liệu thực tế, trong dữ liệu thực nghiệm,

chúng ta không có các hàm tạo thời điểm như các biểu thức toán học.

Vì vậy, thay vào đó, chúng ta cần ước tính phân bố xác suất dựa trên dữ liệu đo được

mà chúng tôi thực sự có.

Và cách để làm điều đó là tính toán biểu đồ.

Vì vậy, chúng tôi tính toán biểu đồ ở đây.

Tôi đang xác định các cạnh này là giá trị nhỏ nhất đến lớn nhất trong dữ liệu một và dữ liệu hai,

chỉ để chúng ta có được các thùng giống hệt nhau cho cả hai tập dữ liệu này.

Được rồi, điều này mang lại cho tôi chiều cao về mặt số lượng.

Và bây giờ, những điều này không tuân theo phân bố xác suất

bởi vì chúng không tổng hợp thành một.

Chúng đều có giá trị dương hoặc không âm, nhưng chúng không có tổng bằng một.

Vì vậy, tôi chia cho tổng.

Và bây giờ, cuối cùng, chúng ta có y1 và y2, chúng ta có thể coi chúng là các hàm xác suất.

Và ở đây bạn thấy hai bản phân phối trông như thế nào.

Được rồi, bây giờ tôi sẽ tính độ phân kỳ.

Điểm phân kỳ là ở đây.

Vậy khoảng cách KL.

Vì vậy, ở đây bạn thấy tôi thực sự có, hãy để tôi bắt đầu với cái này.

Vì vậy, ở đây tôi có y1.

Đây là xác suất của tập dữ liệu một.

Và y2 là xác suất của tập dữ liệu thứ hai.

Vì vậy, theo cách nói của phương trình mà tôi đã trình bày trong slide, đây sẽ là p và đây sẽ là q.

Vậy tôi có p nhân log của p chia cho q.

Bây giờ thì ổn rồi.

Vấn đề là nếu bất kỳ một trong số này bằng 0,

chúng ta sẽ gặp rắc rối.

Nếu y2 bằng 0 với bất kỳ giá trị đã cho nào của x, thì với bất kỳ giá trị nào ở đây dọc theo phân bố này,

nếu chúng ta có các giá trị xác suất chính xác bằng 0,

nếu chúng ở q, hoặc ở đây tôi gọi biến này là y2,

thì chúng ta đang chia cho 0, điều này có vấn đề.

Và nếu chúng ở trong p, ở đây tôi gọi là y1,

đó cũng là vấn đề vì trong này sẽ bằng không.

Và log của số 0 không phải là một số hữu hạn.

Nó được biểu diễn dưới dạng âm vô cực, nhưng nó không thực sự là một con số hữu hạn.

Vì vậy, về cơ bản, số 0 ở bất kỳ đâu cũng sẽ gây ra vấn đề cho chúng ta.

Vì vậy, có một số giải pháp mà bạn có thể sử dụng để giải quyết tình huống này.

Một là cộng một số nhỏ nào đó, để chúng ta có thể nói, chẳng hạn,

EPS bằng 1E trừ 15 hay gì đó.

Vậy chỉ là một số epsilon, một số lượng rất nhỏ.

Và sau đó chúng ta có thể nói, như thế này, chúng ta có thể cộng epsilon vào y2,

và sau đó thêm epsilon như thế này.

Và bây giờ chúng ta không cần mặt nạ.

Như thế này, chúng ta sẽ không cần mặt nạ, v.v.

Điều này hoàn toàn ổn.

Về cơ bản, điều này đảm bảo rằng mọi giá trị bằng 0

sẽ không chia cho 0, và chúng ta không lấy log của 0.

Và khi y1 thực sự bằng 0, thì log của nó sẽ bằng

như trừ 10.000 hay gì đó tương tự.

Nhưng sau đó nó được nhân với 0 ở đây.

Được rồi, đó là một giải pháp, và một giải pháp khác,

mà tôi thực sự đã triển khai ở đây, chỉ là để tạo ra chiếc mặt nạ này.

Vì vậy, về cơ bản, tôi đang bỏ qua mọi giá trị mà một trong hai giá trị đó

bằng không.

Được rồi, rất đẹp.

Vì vậy, đây là sử dụng y2 là q, và đây là sử dụng y1 là q,

và bây giờ bạn thấy kết quả.

Bản thân những con số này không thú vị lắm đối với chúng ta,

nhưng điều chúng tôi muốn làm là so sánh chúng với pi torch.

Và đó là những gì bạn thấy ở đây.

Vì vậy, ở đây tôi đang chuyển đổi dữ liệu từ num pi thành tensor pi.

Và như bạn đã học ở phần trước của khóa học nơi chúng ta sử dụng hàm này

như một hàm mất mát, một hàm mất mát tùy chỉnh,

đầu vào đầu tiên phải là thăm dò nhật ký.

Bạn không thể nhập các giá trị xác suất thô làm đầu vào đầu tiên cần được ghi lại.

Đầu vào thứ hai cho q có thể là log,

hoặc không thể đăng nhập, có một phần không thành vấn đề.

Nhưng nếu đó là xác suất nhật ký thì bạn cần thêm cờ này,

mục tiêu đăng nhập bằng đúng.

Nếu không, bạn có thể làm điều gì đó như thế này và nói mục tiêu nhật ký bằng sai.

Điều đó sẽ tương đương.

Được rồi, và sau đó, được rồi, được rồi.

Vì vậy, bây giờ chúng tôi gặp lỗi vì đây là mảng num pi, không phải tensor pi.

Hãy để tôi hoàn tác tất cả những điều này.

Được rồi, điều quan trọng là hai kết quả ở đây,

mà chúng ta có được bằng cách áp dụng trực tiếp công thức toán học,

khớp những con số này ở đây mà chúng ta nhận được từ việc sử dụng hàm pi torch này.

Sự giảm thiểu ở đây, hầu hết bạn đều muốn nó ở mức nào đó,

các loại cắt giảm khác nhau là những cách khác nhau mà chức năng này

nội bộ sẽ giải quyết vấn đề thu gọn trên một thứ nguyên hàng loạt.

Nếu bạn cũng đang tính toán độ phân kỳ kL trên nhiều đợt.

Vì vậy, nếu bạn chỉ có một vectơ làm đầu vào thì bạn có thể sử dụng phép rút gọn tổng.

Bạn đã hai lần thấy trong khóa học này việc sử dụng phân kỳ kL làm hàm mất mát

đào tạo và tinh chỉnh các mô hình có thể rất hiệu quả, đôi khi quá hiệu quả.

Cách chúng ta sẽ sử dụng phân kỳ kL ở đây là để đánh giá sự tương đồng

giữa đầu ra LLM và văn bản của con người ở mức cao hơn mức đáng lo ngại

về nhật ký mã thông báo riêng lẻ hoặc độ chính xác của cấp độ câu.

Và điều đó sẽ xuất hiện trong hai video tiếp theo.