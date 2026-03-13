# 08 giải thích-hậu cần-hồi quy-chi phí-hàm-tùy chọn

---

Trong một video trước đó, tôi đã viết

xuống một biểu mẫu cho hàm chi phí cho

hồi quy logistic.

Trong video tùy chọn này, tôi muốn

cung cấp cho bạn một lời biện minh nhanh chóng cho

tại sao chúng tôi thích sử dụng hàm chi phí đó cho

hồi quy logistic.

Tóm tắt nhanh, trong hồi quy logistic,

chúng ta có dự đoán đó

là sigmoid của w hoán vị x + b,

trong đó sigmoid là hàm quen thuộc này.

Và chúng tôi đã nói rằng chúng tôi muốn giải thích

y mũ là p( y = 1 | x).

Vì vậy chúng tôi muốn thuật toán của mình

xuất y mũ như một cơ hội

y = 1 với

một tập hợp các tính năng đầu vào x cho trước.

Vì vậy, một cách khác để nói điều này

đó là nếu y bằng 1

thì cơ hội của y được đưa ra

x bằng y mũ.

Và ngược lại nếu y bằng 0 thì

khả năng y bằng 0 là 1- y hat,

phải không?

Vậy nếu y mũ là một cơ hội thì y = 1,

thì 1- y hat là khả năng y = 0.

Vì vậy, hãy để tôi lấy hai phương trình cuối cùng này

và chỉ cần sao chép chúng sang slide tiếp theo.

Vậy điều tôi sắp làm là

lấy hai phương trình này

về cơ bản xác định p(y|x) cho

hai trường hợp y = 0 hoặc y = 1.

Và sau đó lấy hai phương trình này và

tóm tắt chúng thành một phương trình duy nhất.

Và chỉ để chỉ ra y phải bằng 0

hoặc 1 vì trong phương trình chi phí nhị phân,

y = 0 hoặc 1 là hai số duy nhất

những trường hợp có thể xảy ra, được rồi.

Khi ai đó lấy hai phương trình này và

tóm tắt chúng như sau.

Hãy để tôi viết ra nó trông như thế nào,

sau đó chúng tôi sẽ giải thích tại sao nó trông như vậy.

Vậy (1 – y mũ) lũy thừa của (1 – y).

Hóa ra một dòng này

tóm tắt hai phương trình trên.

Hãy để tôi giải thích tại sao.

Vì vậy, trong trường hợp đầu tiên,

giả sử y = 1, phải không?

Vậy nếu y = 1 thì cái này

thuật ngữ cuối cùng là y hat,

bởi vì đó là y mũ lũy thừa 1.

Số hạng này kết thúc bằng 1- y đối với

lũy thừa 1-1, vậy đó là lũy thừa của 0.

Nhưng, bất cứ thứ gì có lũy thừa bằng 0

bằng 1, nên cái đó biến mất.

Và vì vậy, phương trình này,

giống như p(y|x) = y hat, khi y = 1.

Vì vậy, đó chính xác là những gì chúng tôi muốn.

Bây giờ còn trường hợp thứ hai thì sao,

nếu y = 0 thì sao?

Nếu y = 0 thì phương trình này

ở trên là p(y|x) = y mũ về 0,

nhưng bất cứ điều gì liên quan đến quyền lực

của 0 bằng 1 nên

nó chỉ bằng 1 lần

Mũ 1- y lũy thừa 1- y.

Vậy 1- y là 1- 0, vậy đây chỉ là 1.

Và vì vậy cái này bằng 1

lần (1- y mũ) = 1- y mũ.

Và vì vậy ở đây chúng ta có y = 0,

p(y|x) = 1- y mũ,

đó chính xác là những gì chúng tôi muốn ở trên.

Vì vậy, những gì chúng tôi vừa trình bày

đó có phải là phương trình này

là định nghĩa đúng cho p(ylx).

Cuối cùng, vì hàm log là một

hàm tăng đơn điệu nghiêm ngặt,

log tối đa hóa của bạn p(y|x) sẽ

cung cấp cho bạn một kết quả tương tự như

tối ưu hóa p(y|x). Và nếu bạn tính toán

log của p(y|x), bằng

log của y mũ lũy thừa của y,

1 - y mũ lũy thừa 1 - y.

Và điều đó đơn giản hóa thành y log y hat

+ 1- y nhân log 1- y mũ phải không?

Và thế là

điều này thực sự là tiêu cực của sự mất mát

hàm mà chúng ta phải tìm trước đây.

Và có dấu âm ở đó bởi vì

thông thường nếu bạn đang đào tạo một cách học tập

thuật toán, bạn muốn

làm cho xác suất lớn

trong khi đó trong hồi quy logistic

chúng tôi đang thể hiện điều này.

Chúng tôi muốn giảm thiểu chức năng mất mát.

Vì vậy việc giảm thiểu tổn thất tương ứng với

tối đa hóa log của xác suất.

Vậy đây là hàm mất mát

trên một ví dụ duy nhất trông như thế nào.

Làm thế nào về chức năng chi phí,

hàm chi phí tổng thể trên

toàn bộ tập huấn luyện trên m ví dụ?

Hãy tìm ra điều đó.

Vì vậy, xác suất của tất cả

các nhãn Trong tập huấn luyện.

Viết điều này một chút không chính thức.

Nếu bạn cho rằng các ví dụ đào tạo

Tôi đã vẽ độc lập hoặc vẽ IID,

được phân phối độc lập giống hệt nhau,

thì xác suất của ví dụ

là sản phẩm của xác suất.

Tích từ i = 1 đến

m p(y(i) ) cho trước x(i).

Và vì vậy nếu bạn muốn thực hiện

ước tính khả năng tối đa, phải,

thì bạn muốn tối đa hóa,

tìm các tham số tối đa hóa

cơ hội quan sát của bạn và

tập huấn luyện.

Nhưng tối đa hóa điều này là như nhau

như tối đa hóa nhật ký, vì vậy

chúng tôi chỉ đặt các bản ghi ở cả hai bên.

Vậy log xác suất của các nhãn

trong tập huấn luyện bằng,

log của một sản phẩm là tổng của log.

Vậy đó là tổng từ i=1 đến

m của log p(y(i)) cho trước x(i).

Và trước đây chúng tôi đã

đã tìm ra ở phần trước

trượt rằng đây là âm L của y hat i,

ừ tôi.

Và trong thống kê, có một nguyên tắc

được gọi là nguyên tắc khả năng tối đa

ước tính, có nghĩa là chọn

các thông số tối đa hóa điều này.

Hay nói cách khác,

tối đa hóa điều này.

Tổng âm từ i = 1 đến

m L(y hat ,y) và

chỉ cần di chuyển dấu âm

ngoài tổng hợp.

Vì vậy, điều này biện minh cho chi phí chúng tôi đã có cho

hồi quy logistic

đó là J(w,b) của cái này.

Và bởi vì bây giờ chúng tôi muốn giảm thiểu

chi phí thay vì tối đa hóa khả năng,

chúng ta phải loại bỏ dấu trừ.

Và cuối cùng để thuận tiện, để thực hiện

chắc chắn rằng số lượng của chúng tôi có quy mô tốt hơn,

chúng ta chỉ cần thêm 1 trên m

hệ số tỷ lệ thêm ở đó.

Nhưng tóm lại, bằng cách giảm thiểu

hàm chi phí này J(w,b) chúng ta thực sự

thực hiện ước tính khả năng tối đa

với mô hình hồi quy logistic.

Theo giả định rằng chúng tôi

ví dụ đào tạo là IID, hoặc

được phân phối độc lập giống hệt nhau.

Vì vậy, cảm ơn bạn đã xem video này,

mặc dù đây là tùy chọn.

Tôi hy vọng điều này mang lại cho bạn cảm giác tại sao

chúng tôi sử dụng hàm chi phí mà chúng tôi thực hiện cho

hồi quy logistic.

Và với điều đó, tôi hy vọng bạn tiếp tục

bài tập lập trình và

các câu hỏi trắc nghiệm của tuần này.

Và chúc may mắn với cả hai câu đố,

và bài tập lập trình.