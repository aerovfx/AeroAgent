# Phụ lục. Giải tích học tập củng cố sâu trong thực tế, Phiên bản video

---

A.2 Phép tính

Giải tích cơ bản là nghiên cứu về vi phân và tích phân. Trong học sâu, chúng tôi chỉ

thực sự cần phải sử dụng sự khác biệt. Vi phân hóa là quá trình thu được đạo hàm của

một chức năng. Chúng ta đã giới thiệu một khái niệm về đạo hàm, tỷ số của khoảng đầu ra

đến khoảng đầu vào. Nó cho bạn biết không gian đầu ra bị kéo giãn hoặc bị nén đến mức nào.

Điều quan trọng là các khoảng này là các khoảng định hướng nên chúng có thể âm hoặc dương,

và do đó tỷ lệ này có thể âm hoặc dương. Ví dụ, xét hàm f của x

bằng x bình phương. Lấy một điểm x và lân cận của nó x trừ epsilon, x cộng epsilon, trong đó epsilon

là một giá trị nhỏ tùy ý nào đó và chúng ta nhận được một khoảng xung quanh x. Để cụ thể hơn, hãy

x bằng 3, epsilon bằng 0,1. Khoảng xung quanh x bằng 3 là 2,9 3,1. Kích thước và

hướng, của khoảng này là 3,1 trừ 2,9 bằng cộng 0,2 và khoảng này nhận được

ánh xạ tới f của 2,9 bằng 8,41 và f của 3,1 bằng 9,61. Khoảng đầu ra này là 8,41

9,61 và kích thước của nó là 9,61 trừ 8,41 bằng 1,2. Như bạn có thể thấy, khoảng thời gian đầu ra là

vẫn dương, nên tỉ số df chia cho dx bằng 1,2 chia cho 0,2 bằng 6, bằng

là đạo hàm của hàm f tại x bằng 3. Chúng ta biểu thị đạo hàm của một hàm,

f, đối với biến đầu vào, x, là df trên dx. Nhưng điều này không đáng để suy nghĩ

dưới dạng phân số theo nghĩa đen, nó chỉ là một ký hiệu. Chúng ta không cần phải có khoảng thời gian cho cả hai

các mặt của điểm. Một khoảng ở một bên sẽ có tác dụng miễn là nó nhỏ, nghĩa là chúng ta

có thể định nghĩa một khoảng là xx cộng với epsilon và kích thước của khoảng đó chỉ là epsilon,

trong khi đó kích thước của khoảng đầu ra là f(x cộng epsilon trừ f(x). Sử dụng bê tông

các giá trị như chúng tôi đã làm chỉ mang lại giá trị gần đúng nói chung. Để có được sự tuyệt đối, chúng ta cần phải

sử dụng những khoảng nhỏ vô hạn. Chúng ta có thể làm điều này một cách tượng trưng bằng cách tưởng tượng rằng epsilon

là một số vô cùng nhỏ, lớn hơn 0 nhưng nhỏ hơn mọi số khác

số trong hệ thống số của chúng tôi. Bây giờ đạo hàm trở thành một bài toán đại số.

Xem biểu hiện này. Xem biểu hiện này. Xem biểu hiện này. Xem biểu hiện này.

Xem biểu hiện này. Xem biểu hiện này. Xem biểu hiện này.

Ở đây chúng ta chỉ cần lấy tỷ lệ giữa khoảng đầu ra và khoảng đầu vào, cả hai đều

là vô cùng nhỏ vì epsilon là một số vô cùng nhỏ. Chúng ta có thể đại số

giảm biểu thức xuống 2x cộng với epsilon, và vì epsilon là vô cùng nhỏ nên 2x cộng

epsilon gần bằng 2x, mà chúng ta coi là đạo hàm thực sự của số nguyên gốc

hàm f của x bằng x bình phương. Hãy nhớ rằng, chúng ta đang lấy tỷ lệ của các khoảng định hướng

đó có thể tích cực hoặc tiêu cực. Chúng ta không chỉ muốn biết hàm số giãn ra bao nhiêu,

hoặc nén, đầu vào, nhưng liệu nó có thay đổi hướng của khoảng hay không. có một

rất nhiều toán học nâng cao chứng minh tất cả những điều này, xem phân tích phi tiêu chuẩn hoặc phân tích mượt mà

phân tích vô hạn, nhưng quá trình này hoạt động tốt cho các mục đích thực tế.

Tại sao sự khác biệt là một khái niệm hữu ích trong học sâu? Vâng, trong học máy chúng ta

đang cố gắng tối ưu hóa một hàm, nghĩa là tìm các điểm đầu vào của hàm,

sao cho đầu ra của hàm là cực đại hoặc cực tiểu trên tất cả các đầu vào có thể có.

Nghĩa là, cho trước một hàm f(x) nào đó, chúng ta muốn tìm một x sao cho f(x) nhỏ hơn

bất kỳ lựa chọn nào khác của x. Chúng ta thường biểu thị điều này là dấu ngoặc đơn mở argmin f của x close

dấu ngoặc đơn. Thông thường chúng ta có hàm mất mát hoặc hàm chi phí hoặc lỗi cần một số

vectơ đầu vào, vectơ mục tiêu và vectơ tham số và trả về mức độ lỗi giữa

đầu ra dự đoán và đầu ra thực sự, và mục tiêu của chúng ta là tìm ra tập tham số

giúp giảm thiểu hàm lỗi này. Có nhiều cách có thể để giảm thiểu điều này

chức năng, không phải tất cả đều phụ thuộc vào việc sử dụng các công cụ phái sinh, nhưng trong hầu hết các trường hợp, cách hiệu quả nhất

Và cách hiệu quả để tối ưu hóa các hàm mất mát trong học máy là sử dụng thông tin phái sinh.

Vì các mô hình deep learning là phi tuyến tính, nghĩa là chúng không bảo toàn phép cộng và

nhân vô hướng, đạo hàm không cố định như trong phép biến đổi tuyến tính.

Mức độ và hướng nén hoặc kéo dãn xảy ra từ điểm đầu vào đến điểm đầu ra là khác nhau

từ điểm này sang điểm khác. Theo một nghĩa khác, nó cho chúng ta biết hàm số đang cong theo hướng nào,

nên chúng ta có thể đi theo đường cong hướng xuống điểm thấp nhất.

Các hàm đa biến như mô hình deep learning không chỉ có một đạo hàm duy nhất,

mà là một tập hợp các đạo hàm riêng mô tả độ cong của hàm số

tới từng thành phần đầu vào riêng lẻ. Bằng cách này chúng ta có thể tìm ra bộ tham số nào

đối với mạng lưới thần kinh sâu dẫn đến lỗi nhỏ nhất.

Ví dụ đơn giản nhất về việc sử dụng thông tin đạo hàm để cực tiểu hóa một hàm là xem nó hoạt động như thế nào

cho một hàm thành phần đơn giản. Hàm số ta sẽ tìm giá trị nhỏ nhất là…

Xem chức năng này. Đồ thị được thể hiện trên hình A.1. bạn có thể

thấy rằng giá trị cực tiểu của hàm này dường như ở khoảng âm 1. Đây là một hàm tổng hợp

vì nó chứa biểu thức đa thức được bao bọc trong logarit. Vì vậy chúng ta cần

sử dụng quy tắc dây chuyền từ phép tính để tính đạo hàm.

Chúng ta muốn đạo hàm của hàm này theo x. Chức năng này chỉ có một thung lũng,

vì vậy nó sẽ chỉ có một mức tối thiểu. Tuy nhiên, các mô hình học sâu có tính đa chiều

và có tính cấu thành cao và có xu hướng có nhiều cực tiểu. Lý tưởng nhất là chúng ta muốn tìm

mức tối thiểu toàn cầu là điểm thấp nhất trong hàm. Cực tiểu toàn cục hoặc cục bộ là

các điểm trên hàm trong đó hệ số góc, tức là đạo hàm, tại các điểm đó bằng 0.

Đối với một số hàm, như ví dụ đơn giản này, chúng ta có thể tính toán giá trị tối thiểu bằng cách sử dụng

đại số. Các mô hình học sâu thường quá phức tạp để tính toán đại số và

chúng ta phải sử dụng các kỹ thuật lặp lại. Hình A.1. Đầu ra của một thành phần đơn giản

hàm số, f(x) bằng logarit của đại lượng x lũy thừa 4 cộng với x lập phương

cộng 2. Quy tắc dây chuyền trong giải tích cho ta một cách

tính toán đạo hàm của các hàm hợp thành bằng cách phân rã chúng thành từng phần.

Nếu bạn đã nghe nói về lan truyền ngược thì về cơ bản nó chỉ là quy tắc dây chuyền được áp dụng cho mạng thần kinh.

mạng với một số thủ thuật để làm cho nó hiệu quả hơn. Đối với trường hợp ví dụ của chúng tôi, hãy viết lại

chức năng trước đó là hai chức năng. Xem các chức năng này.

Đầu tiên chúng ta tính đạo hàm của hàm ngoài, f(x) bằng logarit

của h(x), nhưng điều này chỉ cho chúng ta df trên dh, và cái chúng ta thực sự muốn là df trên dx. bạn

có thể đã biết rằng đạo hàm của log âm tự nhiên là…

Biểu hiện này. Và đạo hàm của hàm trong h(x)

là… Biểu thức này.

Để có được đạo hàm đầy đủ của hàm hợp thành, chúng ta nhận thấy rằng…

Xem biểu hiện này. Đó là, đạo hàm mà chúng ta muốn, df trên dx,

thu được bằng cách nhân đạo hàm của hàm ngoài với giá trị của nó

đầu vào và hàm bên trong, đa thức, đối với x.

Xem các chức năng này. Bạn có thể đặt đạo hàm này về 0 để tính

cực tiểu theo đại số, 4x bình phương cộng 3x bằng 0. Hàm này có hai cực tiểu

tại x bằng 0 và x bằng trừ 3 chia cho 4 bằng trừ 0,75, nhưng chỉ có x bằng

trừ 0,75 là mức tối thiểu toàn cầu vì f(-0,75) bằng 0,638971, trong khi f(0) bằng 0,693147,

cái đó lớn hơn một chút Hãy xem cách chúng ta có thể giải quyết vấn đề này bằng cách sử dụng gradient

đi xuống, là một thuật toán lặp để tìm cực tiểu của hàm.

Ý tưởng là chúng ta bắt đầu với một điểm x ngẫu nhiên làm điểm bắt đầu. Sau đó chúng ta tính đạo hàm

của hàm số tại điểm này, nó cho chúng ta biết độ lớn và hướng của độ cong

vào thời điểm này. Sau đó chúng ta chọn một điểm x mới dựa trên điểm x cũ, đạo hàm của nó,

và tham số kích thước bước để kiểm soát tốc độ chúng ta di chuyển. Đó là…

Xem biểu hiện này. Hãy xem cách thực hiện điều này trong mã.

Liệt kê A.1, độ dốc giảm dần. Nếu bạn chạy thuật toán giảm độ dốc này,

bạn sẽ nhận được x bằng trừ 0,75000000882165, tức là, nếu làm tròn, chính xác là kết quả bạn nhận được

khi tính toán đại số. Quy trình đơn giản này cũng giống quy trình chúng tôi sử dụng

khi đào tạo mạng lưới thần kinh sâu, ngoại trừ mạng lưới thần kinh sâu có nhiều biến

các hàm hợp thành nên chúng ta sử dụng đạo hàm riêng. Đạo hàm riêng không còn nữa

phức tạp hơn đạo hàm thông thường. Xét hàm nhiều biến f của x,

y bằng x mũ 4 cộng y bình phương. Không còn một đạo hàm duy nhất của

hàm này vì nó có hai biến đầu vào. Chúng ta có thể lấy đạo hàm theo

x hoặc y hoặc cả hai. Khi lấy đạo hàm của một đa biến

hoạt động đối với tất cả các đầu vào của nó và đóng gói nó thành một vectơ, chúng tôi gọi nó là

độ dốc, được biểu thị bằng ký hiệu nabla. Nghĩa là, gradient của f của x là

bằng vectơ có các thành phần, đạo hàm của f theo x và đạo hàm

của f đối với y. Để tính đạo hàm riêng của f với

đối với x, nghĩa là df trên dx, chúng ta chỉ cần đặt biến y khác là một hằng số

và phân biệt như bình thường. Trong trường hợp này, df trên dx bằng 4x lập phương và df trên dy

bằng 2y. Vì vậy gradient f của x bằng 4x lập phương 2y, là vectơ của đạo hàm riêng.

Sau đó, chúng ta có thể chạy giảm độ dốc như bình thường, ngoại trừ bây giờ chúng ta tìm thấy vectơ liên kết với

điểm thấp nhất trong hàm lỗi của mạng lưới thần kinh sâu.

.