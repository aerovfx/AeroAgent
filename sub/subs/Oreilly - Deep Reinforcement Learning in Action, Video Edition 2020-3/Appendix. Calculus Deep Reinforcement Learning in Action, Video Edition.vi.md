# Phụ lục. Giải tích học tập củng cố sâu trong thực tế, Phiên bản video.vi

---

A.2 Giải thích về cơ bản là

môn nghiên cứu về đạo hàm và phân tích.

Trong học sâu, chúng ta thực hiện

chỉ cần sử dụng chức năng đạo đức.

Đạo hàm là quá trình tìm kiếm một hàm đạo

một hàm số. Chúng tôi đã giới thiệu một thuật ngữ

khái niệm về đạo hàm, đó là kỹ thuật của một khoảng giá trị đầu ra với một khoảng

input value. Nó cho bạn biết mức độ đầu ra không thể kéo dài hoặc co lại.

Điều quan trọng cần lưu ý là các giá trị khoảng này là các giá trị khoảng có định hướng, do

chúng có thể là âm hoặc dương, và số đó có thể là âm hoặc dương. Ví dụ, hãy đánh giá hàm

f của x bằng x bình luận. Lấy một điểm x và vùng lân cận của nó là x trừ epsilon, x cộng

epsilon, trong đó epsilon là một tùy chọn giá trị nhỏ và chúng ta có một xung đột giá trị khoảng

xung quanh x. Để cụ thể, cho x bằng 3, epsilon bằng 0,1. Cụm giá trị xung quanh x bằng 3 là

2,9 3,1. Độ dài và hướng của giá trị khoảng này là 3,1 trừ 2,9 bằng cộng 0,2 và giá trị khoảng

this value được sơ đồ tới f của 2,9 bằng 8,41 và f của 3,1 bằng 9,61. This start value is 8,41

9,61 và kích thước của nó là 9,61 trừ 8,41

bằng 1,2. Như bạn có thể thấy, khoảng đầu

ra vẫn dương, vì tỷ lệ như vậy, df chia cho dx

bằng 1,2 chia cho 0,2 bằng 6, là đạo hàm của

hàm f tại x bằng 3. Chúng tôi biểu thị thị đạo

hàm của một hàm, f, theo biến đầu vào x là

df trên dx. Nhưng điều này không được coi

là một phân số đen, nó chỉ là một

ký hiệu. Chúng ta không cần lấy một khoảng

ở cả hai phía của điểm. Chỉ cần một khoảng ở

một bên miễn là nó nhỏ, tức là chúng ta

có thể xác định một khoảng là xx cộng với

epsilon và kích thước của khoảng cách chỉ là

epsilon, while size of first interval

là f của x cộng epsilon trừ f của x. Job

usecác công cụ có giá trị như chúng ta đã có

làm lại các giá trị gần đây một cách chính xác

chung. Để có được giá trị tuyệt đối, chúng

ta cần sử dụng các khoảng trống vô cùng nhỏ.

Chúng ta có thể thực hiện điều này một cách

biểu tượng bằng cách tưởng tượng rằng

epsilon là một số vô cùng nhỏ, lớn hơn 0 nhưng

nhỏ hơn bất kỳ số nào khác trong hệ thống của chúng ta.

Bây giờ phép tính vi phân trở thành một bài toán đại số.

Xem biểu thức này. Xem biểu thức này.

Xem biểu thức này. Xem biểu thức này.

Xem biểu thức này. Xem biểu tượng

this format. Xem biểu thức này.

Ở đây, chúng tôi chỉ lấy tỷ lệ của khoảng đầu ra cho khoảng đầu vào, cả hai đều vô nghĩa

cùng nhỏ vì epsilon là một số vô cùng nhỏ. Chúng ta có thể rút gọn biểu thức này theo

đại số thành 2x + epsilon và vì epsilon là vô cùng nhỏ, 2x + epsilon gần vô cùng với

2x, chúng ta lấy làm đạo hàm đúng của hàm ban đầu f(x) = x bình phương. Xin hãy nhớ

rằng họ đang lấy tỷ lệ của các khoảng có hướng có thể là dương hoặc âm. Chúng ta

ta không chỉ muốn biết các hàm kéo giãn hay nén đầu vào bao nhiêu mà còn muốn biết

chức năng đó có thể thay đổi hướng của khoảng đó hay không. Có rất nhiều kiến trúc

​\u200bCao cấp thuật toán nâng cao chứng minh tất cả những điều này, hãy xem phép toán

không chuẩn hoặc phép toán vô cùng nhỏ gọn, nhưng quy trình này hoạt động tốt cho các mục tiêu thực tế.

Tại sao tính toán chức năng lại là một khái niệm hữu ích

hữu ích trong học sâu? Chà, trong máy học của chúng tôi

chúng tôi đang cố gắng nỗ lực hết sức để đạt được hàm ưu tiên, nghĩa là chúng tôi đang cố gắng tìm kiếm điểm đầu

in for function, sao cho hàm ra kết quả tối đa hoặc tối thiểu để mọi đầu vào khả thi.

Tức là, giả sử có một hàm f nào đó của x, chúng tôi muốn tìm một x sao cho f của x nhỏ hơn

mọi lựa chọn khác nhau của x. Chúng tôi thường biểu thị điều này là argmin open parent f

of x close ngoặc. Thông thường, chúng tôi có hàm mất mát hoặc hàm chi phí hoặc hàm lỗi,

chức năng này lấy một số đầu vào, một mục tiêu và một tham số làm đầu vào rồi

trả lại lỗi giữa đầu ra được mong đợi và đầu ra thực tế và mục tiêu của chúng tôi

tìm kiếm các tham số sao cho chức năng này đạt được mức tối thiểu. Có nhiều cách để tối ưu hóa hàm

đây, không phải cách nào cũng cần đến đạo nhưng hàm trong hầu hết các trường hợp, cách

hiệu quả và tiết kiệm nhất để tối ưu hóa hàm mất mát trong học tập là ứng dụng thông tin đạo hàm.

Vì các mô hình học sâu không có tính năng tuyến tính nên chúng không được phép cộng và được phép

nhân vô hướng nên các hàm đạo không phải là hằng số như trong tính năng biến đổi tuyến tính được phép.

Lượng và hướng xảy ra từ điểm đầu

đến điểm cuối sẽ thay đổi theo từng điểm.

Được phép theo một cạnh khác

tính năng này cho biết hàm cong theo

dù hướng dẫn nào đi nữa, vì vậy chúng ta có thể theo đường cong đi xuống điểm thấp nhất.

Hàm đa biến như mô hình học sâu không chỉ có một hàm đạo mà còn sót lại

có một bộ đối lập mô tả hàm riêng biệt của hàm

từng thành phần đầu vào riêng lẻ. Bằng cách này, chúng ta có thể

tìm kiếm tập hợp các tham số cho đường dẫn sâu của mạng nơ-ron đến lỗi nhỏ nhất.

Ví dụ đơn giản nhất về việc sử dụng thông tin đạo hàm để tối giản hóa một hàm là xem hàm đó hoạt động

động như thế nào để hợp lý các hàm thành đơn giản. Hàm mà chúng ta sẽ cố gắng tìm giá trị nhỏ nhất là…

View this function. Đồ thị được hiển thị trong hình A.1. Bạn có thể thấy rằng

Giá trị nhỏ nhất của hàm này phải có trong khoảng âm 1. Đây là hàm hợp lý

do chứa một gói biểu thức đa thức được chứa trong logarit. Vì vậy,

chúng ta cần sử dụng quy tắc tính đạo hàm trong phép tính vi phân để tính đạo hàm.

Chúng tôi muốn có đạo hàm của hàm này

với x. Hàm này chỉ có một thùng rác, vì vậy nó

sẽ chỉ có một tiểu cực giá trị. Tuy nhiên,

các mô hình học có chiều sâu kích thước cao và có

cao thành phần và có nhiều xu hướng

giá trị cực tiểu. Lý tưởng nhất là chúng tôi muốn

tìm giá trị cực tiểu toàn cục là điểm thấp

nhất trong hàm. Các giá trị cực tiểu toàn cục

hoặc local là các điểm trên hàm ở mức độ đó

gradient, tức là đạo hàm, tại các điểm bằng không.

Đối số với một số, giống như ví dụ

đơn giản này, chúng ta có thể tính giá

phân tích cực tiểu cực trị, sử dụng

đại số. Chiều sâu mô hình thường quá

phức tạp đối với các tính đại số được phép và

chúng ta phải sử dụng các kỹ thuật lặp.

Hình A.1 Đầu ra của một hàm ghép

đơn giản, f (x) bằng logarit của lượng x

mũ bốn cộng x lập phương cộng 2. Quy

quy định trong cung cấp tính năng vi

cho chúng tôi một cách tính đạo đức của các

chức năng hợp lý bằng cách phân tích các phần.

Nếu bạn đã nghe nói về dòng ngược, về cơ bản

thì đó chỉ là quy tắc ứng dụng chuỗi cho nơ-ron

các mạng với một số Mẹo

chúng có hiệu quả hơn. Đối với ví dụ của

chúng tôi, hãy viết lại hàm trước

đó thành hai hàm. Xem các hàm này.

Đầu tiên, chúng tôi tính đạo hàm của

Hàm bên ngoài là f(x) bằng logarit của

h(x), nhưng điều này chỉ dành cho họ

ta df trên dh, còn điều chúng ta thực sự

you want to df on dx. You can known

rằng đạo hàm của log tự nhiên trừ đi...

This biểu thức. Và đạo

hàm bên trong h(x)

là... Biểu thức này.

Để có đủ hàm đạo đức

hợp lý, chúng tôi nhận thấy rằng...

Xem biểu thức này. Nghĩa

là, đạo hàm chúng ta muốn, df

on dx, used by way

nhân đạo của hàm bên ngoài

đối với đầu vào của nó và

hàm bên trong, đa thức, đối với x.

Xem các hàm này. You can setting

đạo này hàm bằng không để tính đại số

cực tiểu, 4x bình phương cộng 3x

bằng không. Hàm này có hai cực tiểu

tại x bằng không và x bằng trừ 3 chia

cho 4 bằng trừ 0,75, nhưng chỉ x bằng

âm 0,75 là giá trị toàn cục nhỏ nhất vì

f(-0,75) bằng 0,638971, khi f(0) bằng

0,693147, tức thời lớn hơn một chút. Chúng ta

hãy xem cách khai báo phương pháp này

sử dụng phương pháp giảm độ dốc

vòng lặp thuật toán để tìm giá trị nhỏ nhất của hàm.

Ý tưởng là bắt đầu với x ngẫu nhiên

làm điểm bắt đầu. Sau đó, ta tính

đạo hàm của hàm này tại thời điểm

điều này, cung cấp độ lớn và hướng độ

tại thời điểm này. Sau đó, ta chọn

điểm x mới dựa trên điểm x cũ, đạo

chức năng của điểm đó và số bước

nhảy để điều khiển tốc độ chuyển đổi. Đó là...

Xem biểu thức này. Hãy xem

cách thực hiện điều này bằng mã hóa.

Liệt kê A.1, giảm dần độ dốc. run

Đây là thuật toán gradient gốc, bạn sẽ nhận được

được giá trị x bằng -0,75000000882165,

sau khi làm tròn thì chính xác là kết quả bạn

được nhận khi tính toán bằng phép tính

đại số. Quy trình đơn giản này gốc gốc

chúng tôi sử dụng khi đào tạo mạng

sâu nơ-ron, ngoại trừ độ sâu mạng nơ-ron là

các hàm tổng hợp nhiều biến, do đó, chúng ta sử dụng

ứng dụng chức năng đạo đức riêng. Không còn tồn tại chức năng tùy chỉnh của Đạo cụ

phức tạp hơn đạo hàm thông thường. Xem xét một số hàm f của x, y

bằng x lũy thừa 4 cộng y bình phương. Không còn chức năng riêng biệt nào

của hàm số này vì hàm có hai biến đầu vào. Ta can get function of x

hoặc y hoặc cả hai. Khi ta lấy hàm đạo của nhiều biến đối lập

Tất cả các biến của nó và gói rút gọn vào ma trận, ta gọi đó là

gradient, ký hiệu bằng ký hiệu nabla. Nghĩa là gradient của f của x

ma trận có các thành phần là đạo hàm

của f đối với x và hàm đạo của f đối với y.

Để tính toán các hàm riêng của f

for x,nghĩa là df trên dx,

ta chỉ cần đặt biến y kia thành hằng số

số và tính đạo hàm như bình thường.

Trong trường hợp này, df trên dx

4x lập phương và df trên dy bằng 2y.

Vậy gradient f của x bằng 4x setting

2y, ma trận cụ thể của các đạo hàm riêng.

Sau đó ta có thể thực hiện thuật toán giảm độ dốc như

bình thường, ngoại trừ lần này ta tìm ra ma trận kết hợp

Điểm thấp nhất trong một

chức năng sâu của mạng nơ-ron.

.