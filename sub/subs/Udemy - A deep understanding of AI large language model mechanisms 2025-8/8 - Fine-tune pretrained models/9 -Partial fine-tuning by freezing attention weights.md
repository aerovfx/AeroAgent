# 9 -Tinh chỉnh một phần bằng cách đóng băng trọng số chú ý

---

Bạn đã biết về khái niệm trọng số ràng buộc, đó là ma trận hai trọng số.

được liên kết với nhau.

Nếu trước đây bạn đã học về deep learning thì có lẽ bạn cũng đã quen với khái niệm này

đóng băng trọng số trong quá trình tinh chỉnh hoặc trong quá trình học chuyển giao.

Điều này thường được thực hiện trong kiến ​​trúc CNN cho tầm nhìn tính toán.

Bạn cũng có thể cố định trọng lượng trong LLM,

có một số lợi ích tiềm năng

mà tôi sẽ thảo luận ở cuối video này.

Nhưng trước tiên tôi sẽ nhắc bạn ý nghĩa của nó

để đóng băng một ma trận trọng số,

và sau đó tôi sẽ có một đoạn mã demo,

hoặc thực ra tôi sẽ chỉ cho bạn cách thực hiện việc này trong PyTorch.

Kết quả cuối cùng của video này là nó thực sự rất dễ dàng

để đóng băng trọng lượng về mặt thực hiện mã hóa,

nhưng có thể choáng ngợp khi nghĩ về tất cả các khả năng của các tập hợp trọng lượng

điều đó có thể bị đóng băng trong quá trình tinh chỉnh.

Vậy trọng lượng đông lạnh có nghĩa là gì?

Nó không liên quan gì đến việc cử tạ ở Na Uy vào mùa đông bên ngoài.

Thay vào đó, cố định trọng số có nghĩa là bạn ngăn cản việc sửa đổi các tham số trong quá trình

sự lan truyền ngược.

Vì vậy thông thường khi bạn chạy backprop, tín hiệu lỗi sẽ truyền ngược qua mọi trọng số

trong mô hình.

Tuy nhiên, nếu một trọng lượng bị đóng băng thì backprop sẽ bỏ qua tham số đó và nó sẽ

không được điều chỉnh.

Đây chắc chắn không phải là điều bạn muốn làm trong quá trình đào tạo trước, nhưng nó là điều bình thường.

kỹ thuật tinh chỉnh, chuyển giao học tập và điều chỉnh hướng dẫn.

Việc cố định trọng lượng trong các mô hình thị giác máy tính là điều khá phổ biến, đặc biệt nếu bạn ổn.

điều chỉnh trên một tập dữ liệu nhỏ.

Và tại sao bạn muốn làm điều này?

Có một số lý do tại sao việc đông lạnh trọng lượng lại có lợi.

Tôi sẽ thảo luận chi tiết hơn sau phần demo mã, nhưng ý tưởng cơ bản là

nó làm giảm thời gian tính toán và cần ít tài nguyên hơn để đào tạo các mô hình lớn và

Nó cũng làm cho các điều chỉnh có mục tiêu hơn một chút

và tinh tế hơn một chút.

Trong PyTorch, việc đóng băng rất đơn giản để chuyển đổi.

Có một tham số trong mỗi tensor PyTorch

được gọi là yêu cầu grad.

Và tất cả các tensor được gắn vào

đối với một mô hình cụ thể có yêu cầu grad bằng true.

Và bạn chỉ cần đặt tham số này thành false

và điều đó đóng băng tensor đó.

Vì vậy, nó đóng băng tất cả các tham số trong ma trận đó.

Trong giây lát, tôi sẽ chuyển sang Python.

Chúng tôi sẽ nhập một mô hình được đào tạo trước

và tinh chỉnh nó trên văn bản Những chuyến du hành của Gulliver.

Vì vậy, một quy trình khá giống với những gì chúng tôi đã làm

vài lần trước đó.

Nếu bạn cảm thấy nhàm chán khi làm việc với cuốn sách này,

thì đừng lo lắng.

Chúng ta sẽ chuyển từ Gulliver's Travels

sang nội dung khác trong video tiếp theo.

Ảnh chụp màn hình này ở đây cho thấy mã trông như thế nào

để đóng băng có chọn lọc một lớp.

Tôi sẽ giải thích điều này chi tiết hơn khi tôi chuyển sang viết mã,

nhưng về cơ bản mã này đang được thiết lập

tham số grad yêu cầu phải sai

cho tất cả các khối máy biến áp,

mà chúng ta có thể xác định là có dấu chấm, dấu chấm H trong tên.

Sau đó tôi sẽ huấn luyện mô hình và xác nhận

rằng trọng lượng bị đóng băng thực sự không thay đổi

hoàn toàn như một chức năng của việc học tập.

Những gì tôi đang trình bày ở đây là chuẩn ma trận

về sự khác biệt trong ma trận trọng số

trước và sau khi đào tạo.

Và thực tế là chuẩn mực bằng 0 có nghĩa là các con số

trong ma trận trọng số trước và sau khi đào tạo

hoàn toàn giống nhau 100%.

Và để so sánh, đây là phân tích tương tự trên một lớp có thể huấn luyện.

Và ở đây chúng ta thấy rằng chuẩn khác 0, có nghĩa là ma trận sẽ khác sau

so với trước khi đào tạo.

Được rồi, hãy chuyển sang Python và sau đó tôi sẽ thảo luận về các lựa chọn khi nào

và tại sao phải đóng băng các tham số.

Tôi chắc chắn rằng đến thời điểm này trong khóa học, bạn đã bắt đầu thực sự quen thuộc với

xem xét tất cả mã nhập này và mã để nhập các mô hình này, mã để thiết lập các siêu này

các thông số và GPU, v.v. Đó là một điều tốt. Bạn muốn có thể tập trung vào những gì mới

và không phải lo lắng về tất cả mã soạn sẵn mà chúng tôi viết để thực hiện tất cả việc nhập này

và những thứ như thế. Được rồi, chúng ta có mã mới ở đây. Được rồi, hãy để tôi bắt đầu bằng việc sao chép cái này

và viết tên in ở đây.

Vì vậy, những gì đoạn mã này đang làm là lặp qua

tất cả các tham số được đặt tên trong mô hình này,

và sau đó tôi chỉ in ra tên.

Vì vậy, bạn có thể thấy nó khởi động tại Transform.wte,

đó là nhúng mã thông báo từ,

và sau đó là phần nhúng vị trí từ.

Và sau đó chúng ta có tất cả các lớp chuẩn chú ý MLP

cho H.0, H.1, H.2, v.v., cho đến H.11.

Tất nhiên, điều này tương ứng với 12 khối máy biến áp

đó là GPT-2 nhỏ và H lại là ẩn.

Vì vậy, điều chúng tôi muốn làm ở đây là lặp lại

tất cả các tham số được đặt tên này và nếu chúng tôi đang làm việc

với tham số nằm trong khối máy biến áp,

chúng ta có thể chỉ ra rằng bằng cách sử dụng dấu chấm H.

Và sau đó chúng ta sẽ thiết lập yêu cầu tham số grad

là sai.

Và ở đây tôi chỉ in nó ra.

Vì vậy tôi đang in ra dấu trừ nếu nó bị đóng băng

và sau đó nhận được tham số grad yêu cầu thực tế.

Và đây, nếu nó không nằm trong khối máy biến áp

hoặc một khối ẩn thì tôi có cộng cộng cộng.

Điều đó có nghĩa là lớp này, ma trận trọng số này

có thể huấn luyện được và sau đó tôi in ra giá trị của yêu cầu grad cho tham số đó.

Vì vậy, nó trông như thế này.

Về cơ bản, bạn biết đấy, bạn có thể thấy ở đây hầu hết là dấu trừ, chỉ một số điểm cộng

ở đây và các ma trận ma trận nhúng lúc đầu cũng có thể huấn luyện được.

Về cơ bản, toàn bộ mô hình này, gần như toàn bộ mô hình hiện đã bị đóng băng và thực sự chỉ

các phần nhúng ngay từ đầu của mô hình có thể được huấn luyện.

Đây có phải là một ý tưởng tốt?

Gần như chắc chắn là không.

Đây không phải là phương pháp đông lạnh,

đóng băng trên diện rộng mà bạn muốn sử dụng trong thực tế.

Tuy nhiên, điều này không dành cho ứng dụng.

Điều tôi muốn làm ở đây là cung cấp cho bạn mã.

Trong video tiếp theo, bạn sẽ bắt đầu với mã

nó trông như thế này và bạn sẽ mở rộng nó

và học cách đông lạnh chính xác,

đóng băng có mục tiêu hơn nhiều.

Tôi sẽ còn nhiều điều để nói về điều gì hợp lý và điều gì không hợp lý

để đóng băng sau này.

Được rồi, tất cả những điều đó đã nói lên,

vì vậy bây giờ hầu hết mô hình đều bị đóng băng, điều đó không sao cả.

Ở đây những gì tôi đang làm chỉ là tập tạ

chỉ từ một số lớp ngẫu nhiên.

Đây là lớp đông lạnh, nó nằm trong khối máy biến áp.

Và đây là ma trận trọng lượng có thể huấn luyện được ở đây.

Đây là cái cuối cùng, là cái này,

và nó có thể đào tạo được.

Vì vậy, về cơ bản chỉ là kiểm tra sự tỉnh táo,

việc tôi đang làm là tập tạ

trước khi tôi thực hiện bất kỳ điều chỉnh nào

và sau đó tinh chỉnh và chúng tôi sẽ so sánh chúng.

Được rồi, tôi sẽ chạy nó, đẩy mô hình vào GPU.

Ở đây tôi đang tinh chỉnh mô hình.

Mã này trông giống như nhiều mã khác

bạn đã thấy trước đây.

Tôi thậm chí sẽ không nói về nó.

Vì vậy tôi sẽ để nó chạy.

Đó là một khóa đào tạo rất nhanh chóng.

Thực sự không có nhiều mẫu.

Phải mất chưa đầy nửa phút.

Mục đích của video này không phải là tinh chỉnh một mô hình.

Mục đích của video này là cung cấp cho bạn mã

để bạn có thể xem cách xem qua tất cả các thông số

trong một mô hình và đóng băng có chọn lọc một số tham số.

Tôi rất sợ hãi khi nhìn vào thứ này.

Tôi thậm chí không muốn nhìn vào nó.

Được rồi, đây là, được rồi, được rồi.

chúng ta có thể nhìn vào nó

Chỉ là, ừ, người mẫu không học được nhiều đến thế

bởi vì nó không đào tạo nhiều.

Được rồi, đây là ma trận có trọng số giống hệt nhau

mà tôi đã nắm được trước khi tập luyện.

Những biến đó tôi gọi là pre, ở đây tôi gọi chúng là post.

Và ý tưởng là tôi đang trừ đi hai lớp đó.

Vì thế đông cứng cân, bài trừ trước.

Bây giờ, nếu mô hình thực sự bị đóng băng trên lớp này,

thì hai trọng số này phải giống hệt nhau

bởi vì backprop hoàn toàn không chạm vào chúng.

Vậy điều đó có nghĩa là ma trận này phải toàn là số không

và chuẩn của ma trận số không bằng không.

Mặt khác, hai ma trận này lẽ ra phải được huấn luyện.

Họ nên khác nhau.

Không quan trọng chúng khác nhau thế nào,

lớn hơn, nhỏ hơn, di chuyển theo hướng.

Nó không quan trọng cho mục đích của chúng tôi ở đây.

Tất cả những gì tôi muốn làm là xác nhận rằng hai ma trận này

là khác nhau,

trong trường hợp đó ma trận sai phân này

sẽ có chuẩn khác 0.

Và đó chính xác là những gì chúng ta thấy.

Một lần nữa, chỉ cần kiểm tra một chút sự tỉnh táo ở đây.

Vậy tại sao bạn lại muốn đóng băng bất kỳ trọng lượng nào?

Tại sao đây là một điều tốt để làm?

Có một số lý do.

Một là bằng cách chỉ đào tạo một số tham số

trong mô hình, bạn giảm được nguy cơ trang bị quá mức.

Và điều đó đặc biệt đúng nếu bạn muốn ngăn chặn

mô hình từ việc phát triển quá nhiều tập huấn luyện,

tập huấn luyện có những đặc điểm riêng.

Thực chất đây là những đặc điểm riêng

đó thực sự chính xác là những gì chúng tôi đã đào tạo người mẫu

để tạo ra, giống như trong Alice in Wonderland

hoặc các mô hình của Edgar Allan Poe.

Vì vậy, trong những video đó, việc trang bị quá mức

để đào tạo các đặc điểm riêng

gần như là mục tiêu của khóa đào tạo,

nhưng không phải lúc nào nó cũng là thứ bạn muốn.

Và bởi vì những mô hình này rất lớn,

nếu bạn có dữ liệu đào tạo hạn chế,

thì việc đóng băng các thông số sẽ giúp mô hình thích ứng tốt hơn

bởi vì bạn có cùng lượng dữ liệu

và ít tham số cần sửa đổi hơn.

Một ví dụ về điều này có thể là nếu bạn đang tinh chỉnh một mô hình

về tài liệu kỹ thuật bên trong một công ty.

Vì vậy, một mô hình nền tảng đã được đào tạo trước

trên toàn bộ internet sau đó có thể được tinh chỉnh

chỉ trên tài liệu kỹ thuật,

nhưng đó là một tập dữ liệu rất nhỏ

so với dữ liệu trước huấn luyện.

Vì vậy, chỉ các phần đào tạo của mô hình mới có thể có lợi.

Một lợi ích khác là rất thiết thực.

Trong khóa học này, chúng ta chủ yếu làm việc

với LLM tương đối nhỏ

có thể có vài trăm triệu tham số,

nhưng những mô hình được sử dụng trong thực tế

có hàng tỷ hoặc hàng chục tỷ tham số.

Và tinh chỉnh những loại mô hình đó

tốn rất nhiều thời gian và tiền bạc,

chưa kể đến tài nguyên tính toán.

Vì vậy mọi người sẽ đóng băng các phần lớn của mô hình

chỉ để việc đào tạo trở nên khả thi hơn

trên nguồn lực hạn chế.

Cuối cùng, bạn cũng có thể thực hiện việc đóng băng có mục tiêu.

Vì vậy, ví dụ, các khối máy biến áp trước đây

có xu hướng tìm hiểu thêm cú pháp và ngữ nghĩa cấp thấp.

Vì vậy, chỉ là cấu trúc ngôn ngữ cơ bản.

Trong khi các lớp sau thường học

bối cảnh cấp cao hơn và các mẫu trừu tượng.

Vì vậy chỉ đóng băng nửa đầu của khối máy biến áp

sẽ giúp duy trì cú pháp của mô hình

đồng thời cho phép việc đào tạo tập trung hơn

về các tính năng cấp cao hơn.

Và đây có thể là điều bạn muốn làm

nếu bạn đang tinh chỉnh một mô hình cho

giả sử, phân loại văn bản.

Bây giờ tôi có một vài điểm thảo luận

về những phần nào của mô hình sẽ bị đóng băng

và khi nào cần thực hiện đông lạnh.

Ở đây bạn có sự bùng nổ của các khả năng

đối với các lớp cụ thể trong mô hình mà bạn muốn cố định.

Ví dụ: nếu bạn đóng băng tất cả các lớp MLP

và cho phép các lớp chú ý tiếp tục được điều chỉnh,

ưu tiên có thể sửa đổi

cách các mã thông báo theo thời gian được chỉ định.

Bây giờ, tôi đã thảo luận về điểm này trước đó,

về cơ bản là sự đóng băng đó

các khối máy biến áp trước đó

cho phép đào tạo tập trung hơn vào văn bản cấp cao

và các đặc điểm ngữ cảnh trong khi vẫn bảo toàn được ngữ nghĩa

và kiến thức cú pháp.

Điểm này ở đây là bạn cũng có thể đóng băng một lớp

khi bắt đầu tinh chỉnh và sau đó giải phóng nó

chẳng hạn như sau hàng trăm mẫu huấn luyện đầu tiên.

Hoặc có thể bạn theo dõi tổn thất trong quá trình tinh chỉnh

và giải phóng một số lớp khi tổn thất giảm xuống

dưới một số ngưỡng mà bạn chọn.

Và cuối cùng, trong lĩnh vực khả năng diễn giải cơ học,

người ta sử dụng phương pháp đóng băng có chủ đích để kiểm tra các giả thuyết

về những phần khác nhau của mô hình có thể học được.

Nói cách khác, đông lạnh còn được sử dụng cho mục đích nghiên cứu,

không chỉ nhằm mục đích ứng dụng thực tế.

Vì vậy, đóng băng trong quá trình tinh chỉnh

vừa cực kỳ dễ vừa cực kỳ khó.

Nó cực kỳ dễ dàng vì về cơ bản

chỉ cần một đoạn mã để chạy.

Nhưng điều đó cực kỳ khó vì có rất nhiều khả năng

đóng băng để làm gì và khi nào.

Và mặc dù có một số hướng dẫn về lớp nào

đóng băng, thực tế là trong thực tế,

đóng băng bao gồm rất nhiều sự khám phá và thử nghiệm

và có thể khá tốn thời gian.

Bạn sẽ cảm nhận được điều này trong thử thách viết mã

trong video tiếp theo.