# 7 -Phân tích đường cơ sở tùy chọn (phần 2) đã dịch

---

Được rồi, trong video này chúng ta sẽ xem xét phân tích đường cơ sở khi nó phụ thuộc vào

trên một trạng thái.

Vì vậy, đây là phân tích cơ bản của BST.

Và một lần nữa, đây là tùy chọn vì nó sẽ khá toán học và đây không phải là

sẽ thay đổi những gì chúng ta làm.

Nó sẽ biện minh thôi.

Nó chỉ nhằm biện minh cho những gì chúng tôi làm.

Vì vậy, bạn không cần phải xem cái này nếu bạn không muốn.

Được rồi, trước tiên, tôi muốn cho bạn thấy tại sao đạo hàm của chúng ta từ trước không áp dụng được ở đây.

Vì vậy, nếu bạn nghĩ về những gì chúng ta có trước đây, nó trông như thế này.

Vì vậy, đây là độ dốc và sau đó chúng tôi có giá trị mong đợi và nó giống như thế này.

Vậy log của p omega theta, chi omega và bây giờ giả sử là trừ B s.

Được rồi, vậy vấn đề với điều này là một.

Nó kết hợp hai ký hiệu khác nhau cùng một lúc.

Vì vậy, khi chúng ta nghĩ về omega, đó là cả một quỹ đạo.

Nhưng khi chúng ta nghĩ về s, điều đó đề cập đến một trạng thái cụ thể s.

Vì vậy, trong ngữ cảnh này, s gần như không đổi bởi vì nó đang nói, bởi vì nó đang nói điều gì

giá trị kỳ vọng của s trong suốt quỹ đạo này.

Vì vậy, theo nghĩa đó, nó sẽ ổn, nhưng cũng theo nghĩa đó, B sẽ lại không đổi.

B vẫn không đổi, đây không phải là điều chúng tôi muốn phân tích vào lúc này.

Ồ, và nếu tôi chưa đề cập đến thì tại sao chúng ta lại làm điều này?

Là vì ​​trong thực tế nên trong thực tế chúng ta sử dụng đường cơ sở.

Đường cơ sở là V.

Chúng tôi sử dụng hàm giá trị trạng thái cho đường cơ sở, chúng tôi sử dụng hàm giá trị trạng thái cho đường cơ sở.

Và bạn đã thấy tại sao điều này cũng có lý, bởi vì ví dụ, một dạng lợi thế,

ví dụ: QSA trừ V của s, về cơ bản là tốt hơn bao nhiêu nếu chọn

hành động A so với những gì bạn sẽ nhận được trung bình nếu bạn chọn các hành động một cách ngẫu nhiên.

Và về cơ bản biểu thức này không thực sự có ý nghĩa.

Vì vậy, chúng ta sẽ bỏ qua điều đó và chúng ta sẽ viết nó theo một cách khác

có ý nghĩa.

Vì vậy, đây chỉ là quay lại một trong những biểu thức mà chúng ta đã có cho gradient trước đó khi chúng ta

thực hiện đạo hàm của chúng tôi.

Chúng tôi chia ra các bước thời gian.

Và chúng tôi cũng đã loại bỏ được động lực của môi trường.

Vì vậy, không có P của s nguyên tố r cho S và A. Nó chỉ là độ dốc của chính sách.

Vì vậy, nó là tổng của tất cả các bước thời gian.

gradient log pi A t, và trước đó ở đây, chúng ta có tổng giải thưởng trong tương lai.

Vậy tau bằng t cộng một lên đến T lớn.

Giả sử R của s tau, hoặc bạn chỉ cần nói R tau cho phần thưởng bạn nhận được tại thời điểm tau và

sau đó trừ BST.

Vì vậy BST không nằm trong tổng.

Đó là lý do tại sao nó không nằm trong số tiền này.

Ý tôi là, đó là lý do tại sao nó có chỉ số T.

Được rồi.

Vì vậy, một lần nữa, chúng tôi chia phần này thành hai phần.

Vậy tổng t bằng một đến T, gradient log theta A t, ST, và sau đó tổng này tau t cộng

một lên tới T lớn, R s tau.

Và một lần nữa, đây chỉ là chuyện của chúng tôi trước đây.

Vì vậy nó là không thiên vị.

Và chúng ta muốn chỉ ra rằng kỳ vọng này, T bằng một đến T lớn, log pi theta A t,

ST, BST.

Chúng tôi muốn chứng minh rằng đây là số không.

Một để cho thấy điều này là bằng không.

Ý tôi là việc trừ đi độ lệch phụ thuộc trạng thái sẽ khiến độ dốc chính sách vẫn không bị sai lệch.

Được rồi.

Vì vậy IE muốn chứng tỏ rằng điều này vẫn không thiên vị.

Được rồi.

Vì vậy, cách chúng tôi thực hiện điều này là chia kỳ vọng thành hai phần.

Được rồi.

Vì vậy, nó sẽ trông như thế này.

Vậy nó sẽ là E. Và tôi sẽ giới thiệu một chút về ký hiệu mới

ở đây.

Vì vậy, S của một dấu hai chấm T. Điều này chỉ có nghĩa là S1, S2, S3, cho đến

S bé T. Và khi đó chúng ta sẽ có A1 đến T trừ một.

Được rồi.

Và tôi đang chọn thời điểm này và chữ C rất rõ ràng.

Và sau đó chúng ta có các bước thời gian khác.

Vậy E của ST cộng một lên T lớn. Và rồi A T lên đến T lớn trừ một.

Được rồi. Bởi vì ở bước cuối cùng chúng ta không chọn một hành động nào cả.

Và đây là kỳ vọng về độ dốc của log pi theta A T ST và sau đó là B ST.

Được rồi.

Và vì vậy trong trường hợp bạn không biết tại sao chúng tôi được phép làm điều này.

Vì vậy, về cơ bản, bạn nghĩ xem kỳ vọng này sẽ kết thúc như thế nào.

Hãy giả sử rằng các trạng thái và hành động là rời rạc.

Vì vậy, thực sự điều chúng tôi đang làm là tính tổng tất cả các biến ngẫu nhiên khác nhau này.

Phải.

Vậy có S1, có A1, S2, A2, vân vân và vân vân cho đến A T trừ một.

Và sau đó ST. Và sau đó chúng tôi tính toán phân bố xác suất của quỹ đạo,

đó là sản phẩm của động lực môi trường nhân với chính sách.

Được rồi. Vậy nó là P. Nó là gì?

S T. Chúng ta có thể tiến lên thực tế là chúng ta sẽ nói T cộng một ở đây và chúng ta sẽ tiến lên T trừ một

lên đây.

Được rồi.

Vậy cho ST tại và sau đó là pi theta.

Bất kỳ cái nào khác có ý nghĩa hơn A T ST và sau đó là độ dốc, v.v.

Được rồi.

Vì vậy, về cơ bản những gì ở trên đang làm khi chúng ta chia tội lỗi thành hai phần khác nhau

mong đợi là chúng ta chỉ đang nói, này, hãy cắt bỏ phần này vào lúc nào đó và làm phần này

một kỳ vọng.

Vậy đây là E và đây là E của thứ này.

Được rồi.

Vì vậy, hy vọng lý do tại sao chúng tôi được phép làm điều đó là hợp lý.

Và bạn cũng có thể chia phần này ra để có xác suất phù hợp.

Và cũng trong trường hợp điều này chưa rõ ràng, chúng nằm trên toàn bộ không gian trạng thái hoặc

toàn bộ không gian hành động.

Được rồi.

Vì vậy, toàn bộ không gian trạng thái, toàn bộ không gian hành động, về cơ bản là tổng tất cả các giá trị có thể có.

Được rồi.

Vì vậy, bằng cách sử dụng những gì chúng tôi có ở trên, tôi đoán chúng tôi cũng có thể đăng ký bằng nhau ở đây vì

họ bình đẳng.

Những gì chúng tôi nhận ra là chúng tôi có thể tính ra một số điều.

Vì vậy, trước tiên tôi sẽ cho bạn xem kết quả và sau đó tôi sẽ chứng minh nó bằng một số ví dụ đơn giản hơn.

Vì vậy tôi khẳng định, vì vậy tôi khẳng định rằng chúng ta có thể làm được điều này.

Vậy được rồi.

Vì vậy chúng ta sẽ không sử dụng cái này.

Điều tôi muốn làm trước tiên là giải thích những gì chúng tôi đang cố gắng làm.

Vì vậy, chúng ta sẽ thao tác cái này hơn nữa, cái này hơn nữa.

Và điều tôi muốn làm với việc này là tôi muốn mang BST ra ngoài.

Được rồi.

Bên ngoài sự mong đợi đầu tiên hoặc sự mong đợi bên trong.

Và lý do chúng ta có thể làm điều đó là vì chú ý, ST không phải là một trong các biến ở đây.

Đó là trước đó.

Vì vậy biến đầu tiên chúng ta xét là s(t+1).

Vì vậy chúng ta có thể mang BST ra ngoài.

Được rồi.

Vì vậy, hãy thao tác điều đó một chút.

Vậy chúng ta có s1 đến t, a1 đến t trừ 1.

Và bây giờ chúng ta có BST ở đây.

Và sau đó chúng tôi có phần còn lại.

Vậy s t cộng 1 lên t lớn, a t lên đến t trừ 1, t lớn trừ 1.

Và bây giờ chúng ta chỉ có độ dốc.

Bây giờ tôi sẽ pi theta a t s t.

Được rồi.

Vì vậy, mục tiêu của chúng tôi bây giờ về cơ bản là chúng tôi muốn tìm ra đây là gì.

Và chúng tôi muốn chứng minh rằng nó bằng không.

Vì vậy, chúng tôi sẽ cung cấp cho nó một lá thư mới.

Chúng ta sẽ gọi nó là E nhỏ.

Được rồi.

Vì vậy, chúng tôi muốn hiển thị, muốn hiển thị E bằng 0.

Được rồi.

Và để làm được điều đó, giờ là lúc mở rộng sang hình thức này.

Được rồi.

Vì vậy tôi sẽ nói E, cái này bằng tổng trên a t, s t cộng 1, a t cộng 1, v.v.

Cho đến a t trừ 1 và sau đó là s t.

Và sau đó chúng ta có phân bố xác suất mà chúng ta đang tính tổng.

Vậy là vậy, bây giờ chúng ta phải giới thiệu một biến mới vì t nằm ở bên ngoài.

Vì thế chúng ta sẽ nói tau.

Tau bắt đầu từ t tăng dần đến t lớn trừ 1.

Và đó là pi theta a tau s tau và sau đó là p s tau cộng 1 cho s tau a tau.

Và sau đó là độ dốc.

Đó là một gradient của nhật ký.

Và sau đó là a, a t s t.

Được rồi.

Vì vậy bây giờ chúng ta có thể quay lại những gì chúng ta đã cố gắng giải thích trước đây.

Đó là bao thanh toán số tiền này.

Được rồi.

Vì vậy, hóa ra là chúng ta có thể phân tích một số yếu tố như thế này.

Vì vậy đây là một t.

Và tôi muốn đưa ra anh chàng này, người phụ thuộc vào t.

Được rồi.

Vậy nó sẽ là pi theta a t cho s t.

Và tôi cũng sẽ đưa anh chàng này ra ngoài.

Được rồi.

Vậy gradient của log pi a t s t.

Và khi đó chúng ta có tổng trên s t cộng 1.

Và sau đó chúng ta sẽ có động lực môi trường.

Vậy p s t cộng 1 cho s t a t.

Và sau đó chúng ta có tổng trên a t cộng 1, vân vân, vân vân, cho đến tận s t.

Và cuối cùng, xác suất cuối cùng nếu chúng ta làm theo mô hình này sẽ là p s t

s t trừ 1, et trừ 1.

Được rồi.

Được rồi.

Được rồi.

Vì vậy, điều này có thể cần được giải thích một chút nếu bạn không hiểu ngay cách thức hoạt động của nó.

Đầu tiên, nếu bạn không nhìn thấy thì đây là một sản phẩm.

Phải.

Vì vậy, nó thực sự có nghĩa là tôi sẽ cố gắng vẽ một đường chấm.

Điều này có nghĩa là pi theta a t s t.

Và sau đó p s t cộng 1 cho s t a t.

Và sau đó nó là một sản phẩm.

Vì vậy, nó có nghĩa là chúng ta nhân lên mọi thứ.

Phải.

Vậy nó là pi theta a t cộng 1 cho s t cộng 1.

Và sau đó p s t cộng 2 cho s t cộng 1 a t cộng 1, v.v.

Phải.

Về cơ bản, tôi đang nói những phép tính tổng này mà chúng ta có thể nói thay vì đặt chúng ở đây,

chúng ta có thể di chuyển một số chúng vào bên trong.

Được rồi.

Bởi vì họ không phụ thuộc vào các biến này.

Được rồi.

Và vì vậy, trong trường hợp bạn không nhớ môn toán cấp ba hoặc đầu đại học của mình để hiểu

tại sao điều này lại hiệu quả, tôi sẽ chỉ cho bạn một số điều.

Ví dụ đơn giản.

Được rồi.

Đây là một ví dụ đơn giản.

Vậy chúng ta có tổng trên i, tổng trên j.

Và sau đó chúng ta có ai, bij.

Vì vậy đây là mô hình xảy ra khá thường xuyên trong nhiều lĩnh vực.

Vì vậy, bao gồm xác suất, số liệu thống kê, vật lý, v.v.

Được rồi.

Vậy bạn có thể làm gì với cái này và thực ra bạn có thể tự mình thử nó.

Vì vậy, bạn có thể nghĩ ra những ví dụ đơn giản.

Phải.

Vậy trong trường hợp này, điều này thực sự có ý nghĩa gì, hoặc thực ra, tôi sẽ nói về điều đó sau.

Trước tiên hãy tính nó ra.

Vì ai, nên nếu bạn chỉ nghĩ về phần này, j ai bij, chúng ta luôn có thể mang đến

ai ở bên ngoài.

Phải.

Vì vậy, điều này sẽ xảy ra, nếu chúng ta bỏ qua phần này, chúng ta chỉ nghĩ về phần này, phần này.

Điều này có thể trở thành ai, tổng trên j, bij.

Phải.

Vì vậy, chúng tôi được phép tính đến ai.

Và tôi đoán sẽ có một ví dụ thậm chí còn đơn giản hơn để xem nó hoạt động như thế nào.

Hãy nghĩ về một hằng số.

Phải.

Vì vậy, nếu bạn có tổng trên i, cxi, điều này cũng giống như việc phân tích c và tính tổng của

xi đầu tiên.

Được rồi.

Vì vậy, hy vọng bạn tin rằng điều đó có ý nghĩa.

Vì vậy bây giờ hãy nghĩ về một ví dụ gần giống với những gì chúng ta đang làm bây giờ.

Vì vậy, hãy xem xét một mô hình đánh dấu với ba bước thời gian.

Và chúng tôi muốn tổng hợp tất cả các xác suất.

Vì vậy, đó sẽ là tổng trên s1, tổng trên s2, tổng trên s3.

Và sau đó là ps1, rồi ps2 đến từ s1.

Và sau đó ps3 đến từ s2.

Được rồi.

Và với điều này, chúng ta có thể làm điều tương tự.

Vì vậy chúng ta có thể nói s1.

Vì s1 không phụ thuộc, hoặc ps1 không phụ thuộc s2 hay s3 nên ta có thể mang nó ra ngoài

cả hai khoản tiền đó.

Vậy là ps1.

Và sau đó là s2.

Điều đó không phụ thuộc vào s3, vì vậy ít nhất chúng ta có thể đưa nó ra ngoài cái này.

Vậy tổng theo s2, ps2 cho s1.

Và thứ duy nhất còn lại là ps3 với s2.

Vậy s3, ps3 cho s2.

Được rồi.

Và bạn sẽ nhận thấy rằng cái này trông giống hệt những gì chúng ta có ở trên.

Và bước thời gian ban đầu là bước đi ra phía trước.

Được rồi.

Vì vậy, bây giờ bạn đã thuyết phục được rằng điều này có hiệu quả, từ đây sẽ không còn nhiều việc phải làm nữa.

Vì vậy, về cơ bản, vấn đề là, khi chúng ta phân tích những thứ như thế này, đây là tổng của một

toàn bộ phân phối xác suất.

Nói cách khác, tổng là 1.

Và rồi tổng tiếp theo, vì đó cũng là phân bố xác suất, nên cũng bằng 1.

Và khi chúng ta đến đây thì cũng là 1.

Bởi vì nó chỉ là một phân phối xác suất và mọi thứ ở bên phải của nó cũng

1.

Được rồi.

Vì vậy chỉ khi chúng ta đến đây, bởi vì đây không chỉ là phân bố xác suất,

nó được nhân với một gradient, chỉ có phần đó không bằng 1.

Nhưng mọi thứ ở bên phải của nó là 1.

Được rồi.

Và một lần nữa, nếu bạn thấy dấu chấm lửng hoặc dấu chấm khó hiểu, bạn có thể xem một ví dụ đơn giản hơn

như thế này.

Và bạn có thể thấy điều này ngay lập tức.

Vì vậy, nếu bạn tính tổng số này thì đây là 1, vì nó chỉ tính tổng tất cả các giá trị có thể

của s3.

Và sau đó bạn có số này nhân 1, giống như số chúng ta có trước đây, chỉ cần tính tổng

trên s2.

Vì vậy, đó sẽ là 1.

Được rồi.

Vì vậy chúng ta hãy chuyển sang trang tiếp theo.

Được rồi.

Vì vậy bây giờ chúng ta tin chắc rằng với e, chúng ta có biểu thức này.

Vậy tại, pi, tại, cho st, del theta log pi, theta tại st.

Và tại thời điểm này, nó chỉ trở thành một bài tập tương tự mà chúng ta đã làm ở phần trước

chứng minh với đường cơ sở không đổi.

Vì vậy, chúng ta sẽ áp dụng thủ thuật ghi nhật ký ngược lại.

Vì vậy, một lần nữa, tôi sẽ viết nó ra, del log f bằng del f trên f, hay nói cách khác, f, del

log f bằng del f.

Được rồi.

Vì vậy, ở đây chúng ta có tổng theo gradient của pi.

Và tôi đoán chúng ta cũng có thể đặt theta ở đó.

Tại St.

Và một lần nữa, chúng ta có thể chuyển đổi độ dốc và tổng.

Vì vậy, chúng ta có gradient tổng tại theta tại st.

Và bây giờ tại thời điểm này, mọi việc lại trở nên dễ dàng.

Đây là tổng trên toàn bộ phân bố xác suất, có nghĩa là nó bằng 1.

Vì vậy, chúng ta có gradient bằng 1, bằng 0.

Được rồi.

Và đó là những gì chúng tôi đang cố gắng thể hiện.

Vậy chúng ta đã chứng minh được điều chúng ta đang cố gắng chứng minh rằng việc trừ đường cơ sở không cố định,

một đường cơ sở phụ thuộc vào tình trạng hiện tại cũng không thiên vị.

Hoặc ít nhất nó không làm cho ước tính trở nên sai lệch hơn.

Và do đó, chúng tôi có thể cảm thấy rằng việc sử dụng điều này trong các phương pháp chuyển màu chính sách của mình là ổn.