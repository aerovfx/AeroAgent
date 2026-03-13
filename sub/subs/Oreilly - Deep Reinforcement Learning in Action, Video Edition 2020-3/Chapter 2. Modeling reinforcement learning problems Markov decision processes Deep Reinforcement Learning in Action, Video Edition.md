# Chương 2. Mô hình hóa các bài toán học tăng cường Quá trình ra quyết định của Markov Học tăng cường sâu trong thực tế, Phiên bản video

---

Chương 2 Mô hình hóa các bài toán học tăng cường - Quy trình ra quyết định của Markov

Chương này đề cập đến sơ đồ chuỗi và phương pháp giảng dạy của chúng tôi

Khung học tập sâu PyTorch Giải quyết các vấn đề về kẻ cướp không có vũ khí

Cân bằng giữa thăm dò và khai thác Mô hình hóa một vấn đề như một quá trình ra quyết định Markov

(MDP) Triển khai mạng nơ-ron để giải quyết vấn đề quảng cáo

vấn đề lựa chọn Chương này đề cập đến một số vấn đề cơ bản nhất

khái niệm trong tất cả các học tăng cường, và nó sẽ là cơ sở cho phần còn lại của

cuốn sách. Nhưng trước khi đi vào vấn đề đó, trước tiên chúng tôi muốn

điểm qua một số phương pháp giảng dạy định kỳ mà chúng tôi sẽ sử dụng trong cuốn sách này.

Đáng chú ý nhất là các sơ đồ dây mà chúng tôi đã đề cập ở chương trước.

Phần 2.1 Sơ đồ chuỗi và phương pháp giảng dạy của chúng tôi

Theo kinh nghiệm của chúng tôi, khi hầu hết mọi người cố gắng dạy một điều gì đó phức tạp, họ có xu hướng

dạy nó theo thứ tự ngược lại với thứ tự phát triển chủ đề đó.

Họ sẽ cung cấp cho bạn một loạt định nghĩa, thuật ngữ, mô tả và có lẽ cả định lý,

và sau đó họ sẽ nói, "Tuyệt vời! Bây giờ chúng ta đã học hết lý thuyết rồi, hãy bắt đầu thôi

về một số vấn đề thực hành." Theo ý kiến của chúng tôi, điều đó hoàn toàn ngược lại

thứ tự mà mọi thứ nên được trình bày. Hầu hết các ý tưởng hay đều xuất hiện dưới dạng giải pháp cho thế giới thực

vấn đề hoặc ít nhất là những vấn đề tưởng tượng. Người giải quyết vấn đề tình cờ gặp được một khả năng

giải pháp, kiểm tra nó, cải thiện nó và cuối cùng chính thức hóa và có thể toán học hóa

nó. Các thuật ngữ và định nghĩa được đưa ra sau giải pháp

đến vấn đề đã được phát triển. Chúng tôi nghĩ rằng việc học là động lực nhất và

hiệu quả khi bạn thay thế người đưa ra ý tưởng ban đầu đang nghĩ cách

để giải quyết một vấn đề cụ thể. Chỉ khi dung dịch kết tinh thì nó mới đảm bảo sự chính thức hóa,

điều thực sự cần thiết để thiết lập tính đúng đắn của nó và truyền đạt một cách trung thực

nó cho những người khác trong lĩnh vực này. Có một sự thôi thúc mạnh mẽ để tham gia vào việc này

đảo ngược phương thức giảng dạy theo trình tự thời gian, nhưng chúng tôi sẽ cố gắng hết sức để chống lại nó và phát triển

chủ đề khi chúng ta đi. Với tinh thần đó, chúng tôi sẽ giới thiệu các thuật ngữ, định nghĩa và thuật toán mới

các ký hiệu khi chúng ta cần chúng. Ví dụ: chúng tôi sẽ sử dụng lời kêu gọi như thế này.

Định nghĩa Mạng nơ-ron là một loại máy học

mô hình bao gồm nhiều lớp thực hiện phép nhân vectơ ma trận theo sau là

việc áp dụng hàm kích hoạt phi tuyến. Các ma trận của mạng lưới thần kinh

là các tham số có thể học được của mô hình và thường được gọi là "trọng số" của

mạng lưới thần kinh. Bạn sẽ chỉ nhìn thấy những chú thích này một lần mỗi học kỳ, nhưng chúng tôi sẽ thường xuyên lặp lại

định nghĩa theo nhiều cách khác nhau trong văn bản để đảm bảo bạn thực sự hiểu và ghi nhớ

nó. Đây là khóa học về học tăng cường, không phải là sách giáo khoa hay tài liệu tham khảo nên chúng ta sẽ không

tránh việc lặp lại chính mình khi chúng ta nghĩ rằng có điều gì đó quan trọng cần ghi nhớ.

Bất cứ khi nào chúng ta cần giới thiệu một số phép toán, thông thường chúng ta sẽ sử dụng một hộp hiển thị phép toán

và một phiên bản pseudopython của cùng một khái niệm cơ bản. Đôi khi việc suy nghĩ sẽ dễ dàng hơn

về mặt mã hóa hoặc toán học và chúng tôi nghĩ rằng thật tốt khi làm quen với cả hai. Như

một ví dụ siêu đơn giản, nếu chúng ta giới thiệu phương trình của một đường thẳng, chúng ta sẽ làm như sau

cái này.

Bảng 2.1. Ví dụ về toán học song song và mã giả mà chúng tôi sử dụng trong cuốn sách này. Xem bảng

hình.

Chúng tôi cũng sẽ bao gồm nhiều mã nội tuyến, đoạn mã ngắn và danh sách mã dài hơn

ví dụ về mã cũng như mã cho các dự án hoàn chỉnh. Tất cả các mã trong cuốn sách được cung cấp

trong Sổ ghi chép Jupyter được phân loại theo chương trên kho GitHub của cuốn sách tại liên kết này.

Nếu bạn tích cực theo dõi nội dung và xây dựng các dự án trong cuốn sách này, chúng tôi chắc chắn sẽ

khuyên bạn nên làm theo mã trong kho GitHub được liên kết này, thay vì sao chép

mã trong văn bản. Chúng tôi sẽ giữ cho mã GitHub được cập nhật và không có lỗi, trong khi mã

trong cuốn sách có thể hơi lỗi thời vì các thư viện Python mà chúng tôi sử dụng đã được cập nhật. GitHub

mã cũng hoàn chỉnh hơn, chẳng hạn như chỉ cho bạn cách tạo các hình ảnh trực quan

chúng tôi đưa vào, trong khi mã trong văn bản được giữ ở mức tối thiểu nhất có thể để tập trung

về các khái niệm cơ bản.

Vì học tăng cường bao gồm rất nhiều khái niệm liên kết với nhau có thể trở thành

khó hiểu khi chỉ sử dụng từ ngữ, chúng tôi sẽ đưa vào rất nhiều sơ đồ và hình vẽ thuộc nhiều loại khác nhau.

Loại hình quan trọng nhất mà chúng ta sẽ sử dụng là sơ đồ dây. Có lẽ đó là một điều kỳ lạ

tên, nhưng đó thực sự là một ý tưởng đơn giản và được phỏng theo lý thuyết phạm trù, một nhánh của

môn toán mà chúng tôi đã đề cập ở chương đầu tiên, nơi họ có xu hướng sử dụng nhiều sơ đồ để bổ sung

hoặc thay thế ký hiệu tượng trưng truyền thống.

Bạn đã thấy sơ đồ chuỗi trong Hình 2.1 khi chúng tôi giới thiệu khung chung

để học tăng cường ở Chương 1. Ý tưởng là các hộp chứa danh từ hoặc danh từ

cụm từ, trong khi các mũi tên được dán nhãn bằng động từ hoặc cụm động từ. Nó hơi khác một chút

từ các sơ đồ dòng điển hình, nhưng điều này giúp dễ dàng chuyển sơ đồ chuỗi sang

Văn xuôi tiếng Anh và ngược lại. Chức năng của các mũi tên cũng rất rõ ràng.

Loại sơ đồ chuỗi đặc biệt này còn được gọi là nhật ký bản thể học hoặc O-log. bạn

có thể tra cứu chúng nếu bạn tò mò muốn tìm hiểu thêm.

Hình 2.1. Mô hình học tăng cường tiêu chuẩn trong đó một tác nhân thực hiện các hành động theo

môi trường phát triển tạo ra phần thưởng để củng cố hành động của tác nhân.

Tổng quát hơn, sơ đồ dây, đôi khi được gọi là sơ đồ nối dây trong các nguồn khác,

là các sơ đồ dạng luồng thể hiện luồng dữ liệu được nhập dọc theo chuỗi, nghĩa là

mũi tên có hướng hoặc không có hướng, vào các quy trình, tính toán, hàm, phép biến đổi,

các quy trình, v.v., được biểu diễn dưới dạng các hộp. Sự khác biệt quan trọng giữa chuỗi

sơ đồ và các sơ đồ luồng trông tương tự khác mà bạn có thể đã thấy là tất cả dữ liệu trên

các chuỗi được gõ rõ ràng, ví dụ: một mảng gọn gàng có hình dạng 10 x 10 hoặc có thể

một số dấu phẩy động và các sơ đồ có đầy đủ thành phần. Theo thành phần,

ý của chúng tôi là chúng ta có thể phóng to hoặc thu nhỏ sơ đồ để xem bức tranh lớn hơn, trừu tượng hơn,

hoặc để đi sâu vào các chi tiết tính toán. Nếu chúng tôi đang hiển thị mô tả ở cấp độ cao hơn,

các hộp quy trình có thể chỉ được dán nhãn bằng một từ hoặc cụm từ ngắn chỉ loại

của quá trình xảy ra, nhưng chúng tôi cũng có thể hiển thị chế độ xem phóng to của hộp quy trình đó

tiết lộ tất cả các chi tiết bên trong của nó, bao gồm tập hợp các chuỗi con và quy trình con của riêng nó.

Bản chất thành phần của các sơ đồ này cũng có nghĩa là chúng ta có thể cắm các phần của một sơ đồ vào

sang một sơ đồ khác, tạo thành các sơ đồ phức tạp hơn, miễn là tất cả các loại chuỗi

tương thích. Ví dụ: đây là một lớp của mạng thần kinh dưới dạng sơ đồ chuỗi.

Xem hình này. Đọc từ trái sang phải, chúng ta thấy có một số

dữ liệu loại N chảy vào hộp xử lý gọi là "lớp mạng thần kinh" và tạo ra đầu ra

thuộc loại M. Vì mạng nơ-ron thường lấy vectơ làm đầu vào và tạo ra vectơ

là đầu ra, các loại này đề cập đến kích thước của vectơ đầu vào và đầu ra tương ứng.

Nghĩa là, lớp mạng nơ-ron này chấp nhận một vectơ có chiều dài hoặc chiều N và tạo ra

một vectơ có chiều M. Có thể N bằng M đối với một số lớp mạng thần kinh.

Cách gõ chuỗi này được đơn giản hóa và chúng tôi chỉ thực hiện khi biết rõ nội dung

các loại có nghĩa từ ngữ cảnh. Trong các trường hợp khác, chúng tôi có thể sử dụng ký hiệu toán học như

R cho tập hợp tất cả các số thực, về cơ bản được dịch trong các ngôn ngữ lập trình

đến số dấu phẩy động. Vì vậy, đối với một vectơ số dấu phẩy động có chiều N,

chúng ta có thể gõ các chuỗi như thế này. Xem hình này.

Bây giờ việc gõ phong phú hơn, chúng ta không chỉ biết kích thước của đầu vào và đầu ra

vectơ, chúng ta biết rằng chúng là những số có dấu gạch chéo thực sự. Trong khi điều này gần như

luôn luôn như vậy, đôi khi chúng ta có thể phải xử lý các số nguyên hoặc số nhị phân. Trong mọi trường hợp,

hộp xử lý lớp mạng thần kinh của chúng tôi được để lại dưới dạng hộp đen. Chúng tôi không biết chính xác những gì

đang diễn ra ở đó ngoài việc nó biến đổi một vectơ thành một vectơ khác

có thể có những kích thước khác nhau. Chúng ta có thể quyết định phóng to quá trình này để xem cụ thể điều gì

đang xảy ra. Xem hình này.

Bây giờ chúng ta có thể thấy bên trong hộp quy trình ban đầu và nó bao gồm một tập hợp các

các quy trình con. Chúng ta có thể thấy rằng vectơ n chiều của chúng ta được nhân với ma trận các chiều

n x m, tạo ra tích vectơ m chiều. Vector này sau đó đi qua một số

quá trình được gọi là Rayleigh, mà bạn có thể nhận ra là chức năng kích hoạt mạng lưới thần kinh tiêu chuẩn,

đơn vị tuyến tính được hiệu chỉnh. Chúng ta có thể tiếp tục phóng to quy trình phụ Rayleigh

nếu chúng tôi muốn. Bất cứ thứ gì xứng đáng với sơ đồ chuỗi tên đều phải được xem xét kỹ lưỡng

ở bất kỳ mức độ trừu tượng nào và vẫn được gõ đúng ở mọi cấp độ, nghĩa là các loại dữ liệu

việc vào và ra các quy trình phải tương thích và có ý nghĩa. Một quá trình mà

được cho là tạo ra các danh sách được sắp xếp không nên kết nối với một quy trình khác mong đợi

số nguyên. Miễn là các chuỗi được đánh máy tốt, chúng ta

có thể xâu chuỗi nhiều quy trình lại với nhau thành một hệ thống phức tạp. Điều này cho phép chúng ta xây dựng

các thành phần một lần và tái sử dụng chúng ở bất kỳ nơi nào có loại phù hợp. Ở mức độ cao hơn một chút, chúng tôi

có thể mô tả một mạng thần kinh tái phát hai lớp đơn giản, RNN, như thế này.

Xem hình này. RNN này lấy một vectơ Q và tạo ra

một vectơ S. Tuy nhiên, chúng ta có thể thấy các quá trình bên trong. Có hai lớp và mỗi lớp

một cái trông giống hệt nhau về chức năng của nó. Mỗi người lấy một vectơ và tạo ra một vectơ,

ngoại trừ việc vectơ đầu ra được sao chép và đưa trở lại quy trình lớp như một phần của

đầu vào, do đó sự lặp lại. Sơ đồ chuỗi là một loại sơ đồ rất tổng quát

sơ đồ. Ngoài việc lập sơ đồ mạng lưới thần kinh, chúng ta có thể sử dụng chúng để lập sơ đồ cách thức

để nướng một chiếc bánh. Đồ thị tính toán là một loại sơ đồ chuỗi đặc biệt trong đó tất cả các

các quy trình thể hiện các tính toán cụ thể mà máy tính có thể thực hiện hoặc có thể

được mô tả bằng một số ngôn ngữ lập trình như Python.

Nếu bạn đã từng hình dung một biểu đồ tính toán trong TensorBoard của TensorFlow, bạn sẽ

biết chúng tôi muốn nói gì. Mục tiêu của một sơ đồ chuỗi tốt là chúng ta có thể xem một thuật toán hoặc

mô hình học máy ở mức cao để có được bức tranh lớn, sau đó thu phóng dần dần

cho đến khi sơ đồ chuỗi của chúng tôi đủ chi tiết để chúng tôi thực sự triển khai thuật toán

hầu như chỉ dựa trên kiến thức của chúng ta về sơ đồ.

Giữa toán học, mã Python đơn giản và sơ đồ chuỗi mà chúng tôi sẽ trình bày trong

cuốn sách này, bạn sẽ không gặp vấn đề gì khi hiểu cách triển khai một số máy khá tiên tiến

các mô hình học tập.

[tĩnh]