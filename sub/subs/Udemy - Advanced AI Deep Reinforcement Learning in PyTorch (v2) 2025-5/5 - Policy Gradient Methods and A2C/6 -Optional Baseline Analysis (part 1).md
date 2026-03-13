# 6 -Phân tích đường cơ sở tùy chọn (phần 1) đã dịch

---

Được rồi, trong video này chúng ta sẽ xem xét phân tích về đường cơ sở.

Vậy tại sao chúng ta được phép làm điều đó và nó mang lại lợi ích gì cho chúng ta?

Vì vậy, điều này sẽ khá toán học.

Vì vậy, chúng tôi sẽ nói rằng đó là tùy chọn đối với bất kỳ ai xem nội dung này và bạn không thích toán hoặc bạn không

hiểu những gì chúng tôi đang làm.

Điều này không quan trọng đối với những gì chúng ta cuối cùng sẽ làm.

Nó chỉ giúp ích cho sự hiểu biết của bạn.

Vì vậy, nếu điều này không giúp ích cho sự hiểu biết của bạn và nó chỉ khiến bạn bối rối hơn thì tôi

khuyên bạn nên bỏ nó ra khỏi danh sách các chủ đề bạn đang cân nhắc cho việc này

tất nhiên.

Được rồi, vì vậy chúng tôi sẽ gọi nó là phân tích cơ bản và nó là tùy chọn.

Được rồi, chỉ để cho bạn xem trước một chút về những gì chúng tôi đang làm để bạn không bị lạc

trong đám cỏ dại, chúng ta sẽ thực hiện ba bước.

Vì vậy, hai bước đầu tiên sẽ có đường cơ sở không đổi B. Và những gì chúng ta sẽ làm

để chứng minh rằng đầu tiên chúng ta sẽ chỉ ra rằng công cụ ước lượng là không thiên lệch.

Được rồi, đó là số một.

Vì vậy, việc trừ đường cơ sở không làm thay đổi giá trị kỳ vọng mà chúng tôi đang làm việc

trước đây.

Thứ hai, chúng ta sẽ tính đường cơ sở phương sai tối thiểu, đường cơ sở phương sai tối thiểu.

Và điều đó giúp ích như thế nào?

Vì vậy, mặc dù chúng ta sẽ không sử dụng giá trị này vì chúng ta sẽ không sử dụng đường cơ sở không đổi.

Vì vậy đây là những đường cơ sở không đổi.

Được rồi, mặc dù chúng ta sẽ không sử dụng đường cơ sở cố định, nhưng điều này sẽ cho thấy

chúng tôi rằng có một số giá trị chúng tôi có thể chọn sẽ làm giảm phương sai của độ dốc của chúng tôi

và nó sẽ không bằng không.

Vì vậy, nó sẽ là một nghiệm khác không cho chúng ta thấy rằng có thể giảm

phương sai của công cụ ước tính độ dốc chính sách vanilla.

Được rồi.

Và cả ba, điều này sẽ liên quan nhiều hơn một chút, bởi vì trong thực tế, chúng ta không

thực sự sử dụng một đường cơ sở không đổi.

Chúng tôi sử dụng đường cơ sở tùy thuộc vào tiểu bang.

Thông thường nó sẽ là hàm giá trị trạng thái.

Vì vậy, chúng tôi cũng sẽ chứng minh rằng nó cũng có tác dụng cho việc này.

Vì vậy, cũng có tác dụng với đường cơ sở B.

Vâng.

Hoặc BST.

Được rồi.

Vì vậy, bài giảng này có thể sẽ chỉ thực hiện một và hai và sau đó là ba phần khá liên quan.

Vì vậy, điều đó thậm chí còn tùy chọn hơn.

Nếu bạn không quan tâm, nghĩa là bạn chưa được tiếp xúc với các kỹ thuật toán học mà chúng tôi đang sử dụng

ở đó, sau đó tôi sẽ nói quên nó đi.

Được rồi.

Vì vậy, điều đầu tiên, hãy chỉ ra rằng đường cơ sở không đổi là không thiên vị.

Vì vậy, đường cơ sở không đổi sẽ trông như thế này.

Vì vậy, độ dốc mục tiêu của chúng ta sẽ bằng và vì vậy chúng ta sẽ làm việc với đầy đủ

đường đi trong bài giảng này.

Vì vậy, nó sẽ là độ dốc của log, xác suất của quỹ đạo omega, và đây

đã vượt qua tất cả theta của omega.

Và thay vì chỉ G, thay vì chỉ omega của bạn, giờ chúng ta đang trừ đi đường cơ sở này.

Được rồi.

Và vì vậy chúng ta sẽ coi như điều này là không thiên vị, thuật ngữ này.

Và một điều bạn nhớ về kỳ vọng từ nghiên cứu xác suất của mình là nếu bạn

có điểm cộng hoặc điểm trừ, bạn chỉ cần phân phối chúng.

Được rồi, cái này sẽ bằng log của p omega theta, G omega, và sau đó chúng ta chỉ phân phối

những điều khoản này.

Bây giờ, hãy quên nhật ký đi.

P omega theta, rồi đến B. Được rồi.

Vì vậy, chúng tôi sẽ coi như điều này là không thiên vị.

Và chúng tôi muốn biết rằng nếu chúng tôi trừ đi số này, nó vẫn không thiên vị.

Vì vậy, về cơ bản những gì chúng ta đang cố gắng làm là chỉ ra rằng đây là, cho thấy nó bằng không.

Được rồi.

Và nhân tiện, nếu bạn không nhớ việc sử dụng công cụ ước tính sai lệch hoặc công cụ ước tính không chệch

về cơ bản nó có nghĩa là chúng ta đang cố gắng ước tính một cái gì đó.

Vì vậy, chúng ta đang xem xét giá trị kỳ vọng của một số công cụ ước tính, chẳng hạn như theta hat, cái nào

giả sử theta ước tính, nếu chúng ta so sánh nó với theta thực, nó sẽ bằng 0.

Vì vậy, nói cách khác, nếu chúng ta thiên vị, điều đó có nghĩa là giá trị kỳ vọng của công cụ ước tính của chúng ta về

giá trị thực sẽ khác không.

Được rồi.

Vì vậy đó là lý do tại sao chúng ta đang cố chứng tỏ rằng đây là số không.

Được rồi.

Vậy làm thế nào để chúng ta chứng minh rằng đây là số không?

Vì vậy, nó không phải là rất khó khăn.

Vì vậy, chúng ta sẽ lấy cái này và chúng ta sẽ khai triển nó thành tích phân.

Vậy nó cũng có thể là một tổng, nhưng với mục đích bầu cử này, hãy nói nó là tích phân.

Và vì vậy chúng ta đang tích phân trên phân bố này, phân bố trên omega.

Ờ, p omega theta b d omega.

Được rồi.

Và bây giờ chúng ta sẽ áp dụng lại quy tắc log đó, ừ, gradient của log của f là

bằng gradient của f chia cho f.

Và ở đây chúng ta sẽ sử dụng nó ngược lại.

Vì vậy, chúng ta sẽ di chuyển f sang phía bên kia và nó gấp f lần độ dốc của khúc gỗ đó là

bằng gradient của f.

Vì vậy, trong trường hợp này, nó sẽ là tích phân và sau đó là gradient của f, trong trường hợp của chúng ta là p.

Và sau đó lần b d omega.

Được rồi.

Vì vậy, bước tiếp theo là một bước khá đơn giản.

Vì đây là hằng số nên chúng ta có thể đưa nó ra ngoài tích phân.

Được rồi.

Vậy nó là gradient tích phân b omega theta d omega.

Được rồi.

Và bước tiếp theo có thể là trực quan hoặc hiển nhiên, nhưng nếu bạn là một nhà toán học thuần túy,

bạn có thể tự hỏi liệu bạn có luôn được phép làm điều này không.

Nếu bạn là nhà nghiên cứu máy học hoặc nhà khoa học máy tính, bạn không quan tâm.

Vì vậy, chúng ta có thể chuyển đổi gradient và tích phân.

Và theo trực giác, lý do tại sao chúng ta có thể làm được điều đó là vì tích phân giống như một phép lấy tổng,

phải không?

Vì vậy đây là một phép đổi đạo hàm và tính tổng.

Vậy đây là p omega theta d omega.

Và bây giờ điều đó trở nên hiển nhiên vì đây là tích phân trên toàn bộ phân bố xác suất.

Vì vậy, đây phải là một.

Và do đó, nó bằng b gradient đối với theta của một, bằng 0 vì một là

một hằng số.

Vậy toàn bộ chuyện này bằng không.

Được rồi.

Đó là những gì chúng tôi đang cố gắng thể hiện nếu bạn nhớ lại.

Được rồi.

Vì vậy, giá trị kỳ vọng sau khi chúng ta trừ đi đường cơ sở sẽ bằng với giá trị kỳ vọng khi

không có đường cơ sở.

Vì vậy, điều này không làm thay đổi giá trị mong đợi của độ dốc, điều này thật kỳ lạ khi nghĩ rằng

về, nhưng toán học hoạt động.

Được rồi.

Vì vậy, bây giờ vì chúng ta đã hết dung lượng nên chúng ta sẽ bắt đầu một trang mới.

Và chúng ta sẽ xem xét việc giảm thiểu sự khác biệt.

Vì vậy, nói cách khác, bạn có thể coi nó là giá trị tối ưu của hằng số b cơ sở này

đường cơ sở?

Vì vậy, chúng ta sẽ nói phương sai tối thiểu, đường cơ sở phương sai tối thiểu.

Được rồi.

Vì vậy, hãy viết lại gradient chính sách của chúng ta.

Giá trị này bằng giá trị mong đợi của gradient của log p omega theta.

Và sau đó là omega.

Và bây giờ chúng ta có đường cơ sở không đổi mà chúng ta đang trừ đi.

Được rồi.

Vì vậy, nếu chúng ta coi vật bên trong là một biến ngẫu nhiên, hãy gọi nó là x, thì e của x sẽ

có ý nghĩa của nó.

Được rồi.

Và chúng ta cũng có thể nghĩ xem phương sai của x là bao nhiêu?

Sự khác biệt của thứ này bên trong là gì?

Được rồi.

Vậy phương sai của x.

Và điều này liên quan thế nào đến những gì chúng ta đang thực sự làm?

Vì vậy, bạn nhớ lại rằng trong thực tế, chúng tôi không sử dụng giá trị mong đợi.

Chúng tôi thay đổi điều này thành trung bình mẫu.

Và thứ chúng ta đang lấy trung bình mẫu là thứ bên trong.

Và vì vậy chúng tôi muốn các mẫu đó có ít phương sai hơn vì điều đó có nghĩa là chúng tôi cần ít hơn

của chúng để tính toán ước lượng chính xác của x.

Được rồi.

Vậy phương sai của x khi bạn nhớ lại bằng giá trị kỳ vọng của x trừ đi bình phương trung bình của nó.

Nhưng cái này cũng bằng e(x bình phương).

Nếu bạn chỉ mở rộng cái này và lưu ý rằng mu bằng e mũ x, đây là e mũ x và

sau đó tất cả bình phương.

Được rồi.

Một lần nữa, đây là từ một khóa học xác suất.

Cho nên nếu muốn xét lại danh tính đó thì làm như thế nào.

Nếu bạn mở rộng thứ ở bên trái, bạn sẽ có được thứ ở bên phải.

Nếu bạn muốn thử điều đó một mình.

Được rồi.

Vì vậy, bây giờ bạn có thể nhận ra có điều gì đó không ổn ở đây, điều mà tôi thấy hầu hết các tài nguyên đều không như vậy.

giải thích.

Vì vậy, hầu hết các tài nguyên không giải thích phần này.

Được rồi.

Vì vậy, vấn đề ở đây là khi chúng ta nói về phương sai, nó luôn là phương sai

của một biến vô hướng, phải không?

Bởi vì khi chúng ta có một vectơ, chúng ta phải nói đến hiệp phương sai vì một thành phần nào đó

có thể tương tác với các thành phần khác.

Và trong trường hợp này, chúng ta có vectơ không?

Câu trả lời là có, bởi vì chúng ta có gradient là một vectơ.

Vì vậy, thật sự không có ý nghĩa gì khi nói về sự khác biệt.

Vì vậy, ý nghĩa thật sự của những tài nguyên này là, có một cách nhìn không trực quan

vào nó, và sau đó có một cách nhìn trực quan.

Vì vậy, cách không trực quan nhưng là cách chính thức là chúng tôi thực sự muốn có dấu vết của

ma trận hiệp phương sai của x.

Được rồi.

Nhưng hóa ra sin x là một vectơ nên ta sẽ vẽ một đường bên dưới để biểu thị

rằng đó là một vectơ.

Vậy điều này sẽ làm gì nếu bạn nghĩ về nó, điều này làm cho nó trở nên trực quan hơn, hiệp phương sai

ma trận, nếu bạn nhớ lại, nó có, nó có trên các đường chéo, hiệp phương sai giữa, vì vậy

giả sử đây là rho i, cột j.

Giá trị này sẽ là hiệp phương sai giữa hoặc tôi sẽ không sử dụng sin x vì chúng tôi sử dụng nó khá nhiều.

Một chút trong khóa học này, chúng ta sẽ nói hiệp phương sai giữa x i và x j.

Nhưng trên các đường chéo, hiệp phương sai của x i, x i, đó chỉ là phương sai

của x i, vậy nó là sigma i bình phương.

Vì vậy, những gì dấu vết đang làm cho biết tổng của tất cả các phương sai này là bao nhiêu?

Vì vậy, bỏ qua hiệp phương sai, chúng tôi không quan tâm các biến tương tác như thế nào, chúng tôi chỉ quan tâm

chúng trải rộng bao nhiêu, được biểu thị bằng bình phương sigma.

Được rồi.

Nhưng hóa ra cái này bằng, nếu bạn làm phép tính, cái này bằng

độ lớn, giá trị kỳ vọng của độ lớn của x trừ mu bình phương.

Được rồi.

Và bây giờ bạn có thể thấy điều này có liên quan rất nhiều đến điều trên.

Phải?

Vì vậy, thay vì thứ bên trong là vô hướng, nó có thể là một vectơ, chúng ta chỉ cần lấy độ lớn.

Được rồi.

Vậy chúng ta làm điều này như thế nào?

Vì vậy, hãy lấy x của chúng ta, thực sự là cái này.

Vì vậy tôi sẽ bỏ theta và tất cả những thứ đó.

Vậy nó là log p omega, để đơn giản hơn một chút, và b của g omega trừ b.

Vậy đây là x của chúng ta, và chúng ta muốn biết phương sai của cái này là gì, hay dấu vết của

hiệp phương sai của điều này.

Vì vậy, thực ra tôi sẽ cho bạn xem thêm một danh tính nữa.

Chúng ta có thể khai triển cái này thành e có độ lớn của x bình trừ đi độ lớn của mu bình.

Nhưng mu là e của x.

Được rồi.

Vậy phương sai, nên chúng ta sẽ gọi đại lượng này là g.

Vậy phương sai của g bằng bình phương của cái này.

Đó thực sự là độ lớn của bình phương này.

Và sau đó g omega trừ b bình phương.

Và trừ bình phương trung bình.

Vậy ý nghĩa, đó chỉ là giá trị mong đợi của thứ đó thôi phải không?

Vậy nó là e của, thực ra phải có dấu độ lớn.

P omega, g omega trừ b bình phương.

Được rồi.

Vì vậy, điều đầu tiên chúng ta có thể làm ở đây là chúng ta có giá trị kỳ vọng này, giá trị trung bình này.

Nhưng nếu bạn nhớ lại bài tập trước, chúng ta đã chỉ ra rằng giá trị kỳ vọng này chỉ là

bằng giá trị kỳ vọng của thứ không có đường cơ sở.

Vì vậy, điều đó giúp chúng ta thoát khỏi một thuật ngữ.

Vậy cái này bằng với, à, chúng ta có thể giữ nguyên phần này.

Và sau đó trừ e của, điều đó thực sự không quan trọng tại thời điểm này bởi vì vì

nó không còn phụ thuộc vào b nữa, nó sẽ biến mất khi ta lấy đạo hàm.

Được rồi.

Và nhân tiện, tại sao chúng ta lại muốn lấy đạo hàm?

Vậy đây là phương sai của g và g là thế này.

Và vì vậy điều chúng tôi đang cố gắng làm bây giờ là chúng tôi đang cố gắng tìm ra phương sai tối thiểu

giải pháp.

Vậy b làm giảm thiểu phương sai này là gì?

Và vì đây là phương trình bậc hai nên đây là phương trình bậc hai dương hoặc hình bát trở lên

đối diện với cái bát, chúng ta biết rằng nó có mức tối thiểu.

Vì vậy, nếu chúng ta lấy đạo hàm của cái này và đặt nó bằng 0 và giải tìm b, chúng ta sẽ

tìm phương sai tối thiểu hoặc b dẫn đến phương sai tối thiểu hoặc phương sai tối thiểu

đối với b.

Được rồi.

Vì vậy, chúng tôi muốn lấy đạo hàm của db này.

Và vì vậy hãy làm điều đó ngay bây giờ.

Vì vậy, chỉ là phép tính cơ bản.

Thế là cả hai đi xuống đáy.

Thế là hai e, anh chàng này.

Và sau đó cái này trở thành power one, phải không?

Hai trừ một là một.

Và khi đó đạo hàm của bên trong sẽ là trừ một.

Và bây giờ số hạng thứ hai, mặc dù ban đầu nó phụ thuộc vào b, nhưng nó không còn phụ thuộc vào b nữa.

Vì vậy, nó không đổi đối với b.

Vậy đạo hàm của nó bằng 0.

Được rồi.

Và vì vậy chúng ta đặt giá trị này bằng 0 và chúng ta muốn giải b.

Được rồi.

Vì vậy, điều này biến mất.

Điều này biến mất vì số 0 chia cho hằng số vẫn bằng 0.

Và sau đó chúng ta có thể mở rộng những điều này ra.

Vậy thực ra chúng ta có e của, tôi sẽ viết nó ở trang tiếp theo vì chúng ta ở dưới cùng.

Vậy chúng ta có e của bình phương g này.

Và trừ e của bình phương b này bằng 0.

Được rồi.

Nhưng tất nhiên chúng ta có thể mang b ra ngoài.

Vậy b ở bên ngoài vì nó không đổi.

Và bây giờ nó chỉ là một phương trình tuyến tính mà chúng ta có thể giải để tìm b.

Được rồi.

Vậy b bằng e gradient của p hoặc log p bình phương.

e omega chia cho giá trị kỳ vọng của gradient log bình phương.

Được rồi.

Vì vậy, đây là đường cơ sở phương sai tối thiểu.

Và tất nhiên trong thực tế nếu bạn thực sự muốn làm điều này, bạn có thể ước tính những kết quả mong đợi này

giá trị bằng cách thực hiện nhiều lần phát hành, phát nhiều tập và sau đó tính toán mẫu

trung bình thay vì giá trị dự kiến.

Được rồi.

Nhưng phần quan trọng ở đây là có một số b khác 0.

Vì vậy, chúng tôi trừ đi thứ gì đó giúp chúng tôi giảm phương sai.

Được rồi.

Và phần tiếp theo chúng ta sẽ làm, hầu hết các tài nguyên cũng bỏ qua phần này, đó là chúng ta đã

chỉ làm việc với hằng số b.

Và điều tôi không thích ở các tài nguyên khác là chúng ta không bao giờ sử dụng hằng số b.

Chúng tôi luôn sử dụng v(s) làm đường cơ sở.

Nhưng khi họ cho bạn xem bằng chứng, họ cho bạn xem bằng chứng cho hằng số b, loại nào?

không có ý nghĩa

Vậy điều chúng ta sẽ làm sau đây là tôi sẽ cho bạn thấy bằng chứng khi b bằng

không cố định.

Vậy khi b phụ thuộc vào s.

Vì vậy, bst tiếp theo.