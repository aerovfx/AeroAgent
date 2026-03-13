# 04 lý do tại sao-sâu-đại diện

---

Tất cả chúng ta đều đã nghe điều đó sâu sắc

mạng lưới thần kinh hoạt động thực sự tốt cho

rất nhiều vấn đề, và không chỉ vậy

chúng cần phải là những mạng lưới thần kinh lớn,

cụ thể là họ cần phải

sâu hoặc có nhiều lớp ẩn.

Vậy tại sao vậy?

Chúng ta hãy xem qua một vài ví dụ và

cố gắng đạt được một số trực giác cho

tại sao mạng sâu có thể hoạt động tốt

Vì vậy, trước tiên,

điện toán mạng sâu là gì?

Nếu bạn đang xây dựng một hệ thống cho

nhận dạng khuôn mặt hoặc

nhận diện khuôn mặt, đây là một điều sâu sắc

mạng lưới thần kinh có thể đang làm.

Có lẽ bạn nhập hình ảnh của một khuôn mặt sau đó

lớp đầu tiên của mạng lưới thần kinh

bạn có thể nghĩ có thể là

một bộ phát hiện tính năng hoặc một bộ phát hiện cạnh.

Trong ví dụ này, tôi đang vẽ sơ đồ

mạng lưới thần kinh có khoảng 20 đơn vị ẩn,

có thể đang cố gắng tính toán trên hình ảnh này.

Vì vậy, 20 đơn vị ẩn được hiển thị

bởi những chiếc hộp vuông nhỏ này.

Ví dụ, hình dung nhỏ này

đại diện cho một đơn vị ẩn đó là

cố gắng tìm ra vị trí của các cạnh

của hướng đó có trong hình ảnh.

Và có thể đơn vị ẩn này

có thể đang cố gắng tìm hiểu

chiều ngang ở đâu

các cạnh trong hình ảnh này.

Và khi chúng ta nói về tích chập

mạng trong khóa học sau,

hình dung đặc biệt này

sẽ có ý nghĩa hơn một chút.

Nhưng về hình thức, bạn có thể nghĩ đến lớp đầu tiên

của mạng lưới thần kinh khi nhìn vào

hình ảnh và cố gắng tìm ra

các cạnh trong hình này ở đâu

Bây giờ, hãy nghĩ về vị trí của các cạnh

trong bức ảnh này bằng cách nhóm lại với nhau

các pixel để tạo thành các cạnh.

Sau đó nó có thể phát hiện các cạnh và nhóm

các cạnh với nhau để tạo thành các bộ phận của khuôn mặt.

Vì vậy, ví dụ, bạn có thể có mức thấp

nơ-ron đang cố gắng xem liệu nó có tìm thấy mắt không,

hoặc một nơ-ron khác đang cố gắng

để tìm ra phần mũi đó.

Và bằng cách ghép nhiều cạnh lại với nhau,

nó có thể bắt đầu phát hiện

phần khác nhau của khuôn mặt.

Và cuối cùng, bằng cách đặt

các phần khác nhau của khuôn mặt lại với nhau,

như mắt, mũi, tai hoặc

cằm, sau đó nó có thể cố gắng nhận ra hoặc

phát hiện các loại khuôn mặt khác nhau.

Vì vậy, bằng trực giác, bạn có thể nghĩ về

các lớp trước đó của mạng lưới thần kinh như

phát hiện các chức năng đơn giản, như các cạnh.

Và sau đó soạn chúng lại với nhau trong

các lớp sau của mạng lưới thần kinh vì vậy

rằng nó có thể học được nhiều hơn và

các chức năng phức tạp hơn.

Những hình ảnh trực quan này sẽ có ý nghĩa hơn

khi chúng ta nói về mạng tích chập.

Và một chi tiết kỹ thuật

của sự hình dung này,

các máy dò cạnh đang nhìn vào

các vùng tương đối nhỏ của hình ảnh,

có lẽ những vùng rất nhỏ như thế.

Và sau đó, máy dò khuôn mặt bạn có thể nhìn

ở những vùng hình ảnh có thể lớn hơn nhiều.

Nhưng trực giác chính bạn lấy đi

từ đây chỉ là tìm kiếm những điều đơn giản

giống như các cạnh và sau đó xây dựng chúng lên.

Soạn chúng lại với nhau để phát hiện

những thứ phức tạp hơn như mắt hoặc mũi

sau đó ghép chúng lại với nhau để

tìm thấy những điều thậm chí còn phức tạp hơn.

Và loại đơn giản đến phức tạp này

đại diện theo thứ bậc,

hoặc biểu diễn thành phần,

áp dụng trong các loại dữ liệu khác ngoài

hình ảnh cũng như nhận dạng khuôn mặt.

Ví dụ: nếu bạn đang cố gắng

xây dựng hệ thống nhận dạng giọng nói,

thật khó để hình dung lại lời nói nhưng

nếu bạn nhập một đoạn âm thanh thì có thể

cấp độ đầu tiên của mạng lưới thần kinh có thể

học cách phát hiện dạng sóng âm thanh ở mức độ thấp

các tính năng, chẳng hạn như giai điệu này có tăng lên không?

Nó đang đi xuống à?

Đó là tiếng ồn trắng hay

âm thanh sụt sịt như [ÂM THANH].

Và sân là gì?

Khi nói đến điều đó, hãy phát hiện mức thấp

các tính năng dạng sóng cấp như thế.

Và sau đó bằng cách sáng tác

dạng sóng cấp thấp,

có thể bạn sẽ học cách phát hiện

đơn vị cơ bản của âm thanh.

Trong ngôn ngữ học họ gọi là âm vị.

Nhưng, ví dụ, trong từ mèo,

C là âm vị, A là âm vị,

T là một âm vị khác.

Nhưng học cách tìm ra có lẽ

các đơn vị cơ bản của âm thanh và

sau đó có thể sáng tác nó cùng nhau

học cách nhận biết các từ trong âm thanh.

Và sau đó có thể kết hợp chúng lại với nhau,

để nhận ra toàn bộ cụm từ hoặc

câu.

Mạng lưới thần kinh sâu với nhiều ẩn

các lớp có thể có sớm hơn

các lớp học những điều này thấp hơn

cấp tính năng đơn giản và

sau đó có các lớp sâu hơn sau đó đặt

cùng với những điều đơn giản hơn nó được phát hiện

để phát hiện những điều phức tạp hơn

như nhận ra những từ cụ thể hoặc

thậm chí cả cụm từ hoặc câu.

Việc phát biểu để

thực hiện nhận dạng giọng nói.

Và những gì chúng ta thấy là trong khi cái kia

các lớp đang tính toán, có vẻ như

chức năng tương đối đơn giản của đầu vào

chẳng hạn như cạnh ở đâu, vào thời điểm đó

bạn vào sâu trong mạng bạn có thể

thực sự làm được những điều phức tạp một cách đáng ngạc nhiên.

Chẳng hạn như phát hiện khuôn mặt hoặc

phát hiện các từ hoặc cụm từ hoặc câu.

Một số người thích so sánh

giữa mạng lưới thần kinh sâu và

bộ não con người, nơi chúng tôi tin rằng,

hoặc các nhà khoa học thần kinh tin rằng,

rằng bộ não con người cũng bắt đầu

phát hiện những thứ đơn giản như các cạnh trong cái gì

mắt bạn nhìn rồi xây dựng chúng

lên để phát hiện phức tạp hơn

những thứ như những khuôn mặt mà bạn nhìn thấy.

Tôi nghĩ sự tương tự giữa

học sâu và

bộ não con người đôi khi

có chút nguy hiểm.

Nhưng có rất nhiều sự thật, điều này

cách chúng ta nghĩ rằng bộ não con người hoạt động và

rằng bộ não con người có lẽ

phát hiện những thứ đơn giản như cạnh trước

sau đó ghép chúng lại với nhau từ nhiều hơn và

các đối tượng phức tạp hơn và do đó

đã phục vụ như một hình thức truyền cảm hứng lỏng lẻo

cho một số học tập sâu sắc là tốt.

Chúng ta sẽ thấy thêm một chút

về bộ não con người hoặc

về bộ não sinh học

một video sau trong tuần này.

Phần trực giác khác

về lý do tại sao mạng lưới sâu dường như

làm việc tốt như sau.

Vậy kết quả này đến từ mạch

lý thuyết liên quan đến tư duy

về những loại chức năng bạn có thể

tính toán với

các cổng AND, cổng OR khác nhau,

KHÔNG phải cổng, về cơ bản là cổng logic.

Vì vậy, một cách không chính thức, các hàm của chúng tính toán

với một dây thần kinh tương đối nhỏ nhưng sâu

mạng và ý tôi là nhỏ

của các đơn vị ẩn là tương đối nhỏ.

Nhưng nếu bạn cố gắng tính toán tương tự

hoạt động với một mạng nông,

vì vậy nếu không có đủ lớp ẩn,

thì bạn có thể yêu cầu theo cấp số nhân

nhiều đơn vị ẩn hơn để tính toán.

Vậy hãy để tôi cho bạn một ví dụ và

minh họa điều này một cách không chính thức.

Nhưng giả sử bạn đang cố gắng

tính OR độc quyền, hoặc

tính chẵn lẻ của tất cả các tính năng đầu vào của bạn.

Vì vậy, bạn đang cố gắng tính X1,

XOR, X2, XOR,

X3, XOR, tối đa Xn nếu bạn có n hoặc

n tính năng X.

Vì vậy, nếu bạn xây dựng cây XOR như thế này,

vì vậy đối với chúng tôi nó tính toán XOR của X1 và

X2 rồi lấy X3 và

X4 và tính XOR của chúng.

Và về mặt kỹ thuật, nếu bạn chỉ đang sử dụng

Cổng AND hoặc NOT, bạn có thể cần một cổng

vài lớp để tính toán XOR

hoạt động chứ không chỉ một lớp, nhưng

với một mạch tương đối nhỏ,

bạn có thể tính toán XOR, v.v.

Và sau đó bạn có thể xây dựng,

thực sự, một cây XOR như vậy,

cho đến khi cuối cùng bạn có một mạch điện ở đây

đầu ra đó, hãy gọi đây là Y.

Đầu ra của mũ Y bằng Y.

HOẶC độc quyền,

tính chẵn lẻ của tất cả các bit đầu vào này.

Vì vậy, để tính XOR, độ sâu của

mạng sẽ theo thứ tự của log N.

Chúng ta sẽ chỉ có một cây XOR.

Vì vậy số lượng nút hoặc

số lượng các thành phần mạch hoặc

số lượng cổng ở đây

mạng không lớn.

Bạn không cần nhiều cổng như vậy

để tính toán OR độc quyền.

Nhưng bây giờ, nếu bạn không được phép

sử dụng mạng nơ-ron với nhiều

các lớp ẩn với, trong trường hợp này,

nhật ký đặt hàng và các lớp ẩn,

nếu bạn buộc phải tính toán cái này

hoạt động chỉ với một lớp ẩn,

vậy là bạn có tất cả những thứ này

các đơn vị ẩn

Và sau đó những thứ này sẽ xuất ra Y.

Sau đó để tính toán này

Hàm XOR, lớp ẩn này

sẽ cần phải lớn theo cấp số nhân,

bởi vì về cơ bản,

bạn cần phải liệt kê đầy đủ

2 đến N cấu hình có thể.

Vì vậy, theo thứ tự từ 2 đến N,

cấu hình có thể có của đầu vào

các bit dẫn đến OR độc quyền

là 1 hoặc 0.

Vì vậy, cuối cùng bạn cần một lớp ẩn

đó là lớn theo cấp số nhân trong

số lượng bit.

Tôi nghĩ về mặt kỹ thuật, bạn có thể làm điều này

với 2 đến N trừ 1 đơn vị ẩn.

Nhưng đó là số 2 lớn hơn của N, nên nó sẽ là

lớn hơn theo cấp số nhân về số lượng bit.

Vì vậy tôi hy vọng điều này mang lại cảm giác rằng

có các hàm toán học,

dễ dàng hơn nhiều để tính toán sâu

mạng hơn so với các mạng nông.

Trên thực tế, cá nhân tôi đã tìm thấy kết quả

từ lý thuyết mạch ít hữu ích hơn cho

đạt được trực giác, nhưng đây là

một trong những kết quả mà mọi người thường trích dẫn

khi giải thích giá trị của

có những biểu hiện rất sâu sắc.

Hiện nay, ngoài những lý do này

thích mạng lưới thần kinh sâu hơn,

phải hoàn toàn trung thực,

Tôi nghĩ những lý do khác khiến thuật ngữ này trở nên sâu sắc

việc học đã thành công chỉ là việc xây dựng thương hiệu.

Những thứ này chúng tôi gọi là thần kinh

mạng có nhiều lớp ẩn, nhưng

cụm từ học sâu chỉ là

một thương hiệu tuyệt vời, nó thật sâu sắc.

Vì vậy tôi nghĩ rằng một khi thuật ngữ đó được sử dụng

mạng lưới thần kinh thực sự đã được đổi thương hiệu hoặc

mạng lưới thần kinh với nhiều

các lớp ẩn được đổi tên thương hiệu,

giúp nắm bắt sự phổ biến

cả trí tưởng tượng nữa.

Nhưng bất kể PR thương hiệu là gì,

mạng sâu hoạt động tốt.

Đôi khi người ta đi quá đà và

khăng khăng sử dụng hàng tấn lớp ẩn.

Nhưng khi tôi bắt đầu một vấn đề mới,

Tôi thường thực sự bắt đầu với

thậm chí hồi quy logistic

thử cái gì đó với một hoặc

hai lớp ẩn và

sử dụng nó như một tham số siêu.

Sử dụng nó làm tham số hoặc siêu tham số

mà bạn điều chỉnh để cố gắng tìm

độ sâu phù hợp cho mạng lưới thần kinh của bạn.

Nhưng trong nhiều năm qua đã có

là một xu hướng khiến mọi người tìm thấy điều đó

đối với một số ứng dụng, rất, rất sâu

mạng lưới thần kinh ở đây có thể có nhiều

đôi khi có hàng chục lớp, đôi khi có thể

trở thành hình mẫu tốt nhất cho một vấn đề.

Vì vậy, đó là về trực giác cho

tại sao học sâu dường như hoạt động tốt

Bây giờ chúng ta hãy nhìn vào cơ chế

về cách triển khai không chỉ ở phía trước

lan truyền mà còn cả lan truyền ngược.