# Chương 10. Sự chú ý đa đầu và Học tập tăng cường sâu DQN quan hệ trong hành động, Phiên bản video được dịch

---

Phần 10.4, Sự chú ý nhiều đầu và DQN quan hệ.

Chúng tôi đã chứng minh rằng mô hình quan hệ của chúng tôi thực hiện tốt nhiệm vụ đơn giản là phân loại

Các chữ số M-NIST và hơn nữa bằng cách hình dung Bản đồ chú ý đã học, chúng ta có thể hiểu được

về dữ liệu mà mô hình đang sử dụng để đưa ra quyết định.

Nếu mô hình được đào tạo liên tục phân loại sai một hình ảnh cụ thể, chúng ta có thể kiểm tra bản đồ chú ý của nó

và xem liệu có lẽ nó đang bị phân tâm bởi tiếng ồn nào đó không.

Một vấn đề với cơ chế tự chú ý mà chúng ta đã sử dụng cho đến nay là nó nghiêm trọng

hạn chế lượng dữ liệu có thể được truyền do softmax.

Nếu đầu vào có hàng trăm hoặc hàng nghìn nút thì mô hình sẽ chỉ có thể thu hút sự chú ý

trọng lượng trên một tập hợp con rất nhỏ trong số đó và có thể không đủ.

Chúng tôi muốn có thể hướng mô hình tới các mối quan hệ học tập mà softmax giúp thúc đẩy,

nhưng chúng tôi không nhất thiết muốn giới hạn lượng dữ liệu có thể đi qua lớp tự chú ý.

Trên thực tế, chúng ta cần một cách để tăng băng thông của lớp tự chú ý mà không cần phải lo lắng về cơ bản.

thay đổi hành vi của nó. Để giải quyết vấn đề này, chúng tôi sẽ cho phép mô hình của mình có nhiều đầu chú ý,

nghĩa là mô hình học nhiều bản đồ chú ý hoạt động độc lập và sau đó được kết hợp lại,

hình 10.18.

Một đầu chú ý có thể tập trung vào một khu vực hoặc tính năng cụ thể của đầu vào,

trong khi một cái đầu khác sẽ tập trung ở nơi khác.

Bằng cách này, chúng tôi có thể tăng băng thông thông qua lớp chú ý nhưng vẫn có thể giữ nguyên

khả năng diễn giải và học tập quan hệ còn nguyên vẹn. Trên thực tế, sự chú ý bằng nhiều đầu có thể cải thiện

khả năng diễn giải vì trong mỗi đầu chú ý, mỗi nút có thể tập trung mạnh mẽ hơn vào một phần nhỏ hơn

tập hợp con của các nút khác, thay vì phải phân tán sự chú ý của nó một cách mỏng hơn.

Do đó, sự chú ý của nhiều người có thể cho chúng ta ý tưởng tốt hơn về những nút nào có liên quan chặt chẽ với nhau.

Hình 10.18.

Sản phẩm chấm nhiều đầu chú ý, MHDPA.

Thay vì sử dụng một ma trận chú ý duy nhất, chúng ta có thể có nhiều ma trận chú ý được gọi là các đầu có thể

độc lập tham gia vào các khía cạnh khác nhau của đầu vào.

Sự khác biệt duy nhất là việc thêm một thứ nguyên đầu mới vào các tensor truy vấn, khóa và giá trị.

Với sự chú ý của nhiều người, lợi ích của I'm some thậm chí còn trở nên rõ ràng hơn như chúng ta sẽ làm.

hoạt động trên bốn tensor của lô thứ nguyên theo đầu theo số nút theo tính năng.

Sự chú ý nhiều đầu sẽ không đặc biệt hữu ích cho MNIST vì không gian đầu vào đã nhỏ

và đủ thưa để một đầu chú ý duy nhất có đủ băng thông và khả năng diễn giải.

Do đó, đây là thời điểm tốt để giới thiệu nhiệm vụ học tăng cường của chúng tôi cho chương này,

bởi vì mô-đun quan hệ là mô hình tốn kém nhất về mặt tính toán mà chúng tôi đã triển khai trong cuốn sách này cho đến nay,

chúng tôi muốn sử dụng một môi trường đơn giản mà vẫn thể hiện được sức mạnh của lý luận quan hệ và

khả năng diễn giải trong học tập tăng cường.

Chúng ta sẽ đi hết vòng tròn và quay trở lại môi trường thế giới dạng lưới mà chúng ta gặp lần đầu ở chương 3.

Nhưng môi trường thế giới lưới mà chúng ta sẽ sử dụng trong chương này phức tạp hơn nhiều.

Chúng tôi sẽ sử dụng thư viện lưới nhỏ có trên GitHub tại liên kết này.

Nó được triển khai như một môi trường tập thể dục AI mở.

Nó bao gồm nhiều loại môi trường thế giới lưới khác nhau với độ phức tạp và độ khó khác nhau.

Một số môi trường thế giới lưới này rất khó khăn, phần lớn là do phần thưởng thưa thớt,

rằng chỉ những thuật toán học tăng cường tiên tiến nhất mới có khả năng đạt được tiến bộ.

Cài đặt gói bằng PIP.

Xem mã này.

Chúng ta sẽ sử dụng một môi trường hơi khó khăn trong đó tác nhân của thế giới lưới phải điều hướng đến một chiếc chìa khóa, nhặt nó lên,

dùng nó để mở một cánh cửa, sau đó điều hướng đến cột mục tiêu để nhận phần thưởng tích cực, hình 10.19.

Đây là rất nhiều bước trước khi nó nhận được phần thưởng, vì vậy chúng ta sẽ gặp phải vấn đề phần thưởng thưa thớt.

Đây thực sự sẽ là một cơ hội tuyệt vời để áp dụng phương pháp học tập dựa trên trí tò mò,

nhưng chúng ta sẽ hạn chế ở phiên bản nhỏ nhất của lưới, lưới mini,

để ngay cả một tác nhân ngẫu nhiên cuối cùng cũng tìm thấy mục tiêu, để chúng ta có thể huấn luyện thành công mà không cần tò mò.

Đối với các biến thể lưới lớn hơn của môi trường này, sự tò mò hoặc các cách tiếp cận liên quan gần như là cần thiết.

Hình 10.19. Môi trường chìa khóa cửa lưới mini.

Trong môi trường này, đặc vụ, hình tam giác, trước tiên phải điều hướng đến chiếc chìa khóa, nhặt nó lên, điều hướng đến cánh cửa, hình vuông rỗng,

mở nó và sau đó điều hướng đến hình vuông đặc.

Mỗi trò chơi khởi tạo các đối tượng trên lưới một cách ngẫu nhiên và tác nhân chỉ có chế độ xem một phần của lưới được biểu thị bằng vùng được đánh dấu xung quanh nó.

Có một số vấn đề phức tạp khác đối với tập hợp các môi trường lưới nhỏ.

Một là chúng là những môi trường có thể quan sát được một phần, nghĩa là tác nhân không thể nhìn thấy toàn bộ lưới mà chỉ nhìn thấy một vùng nhỏ ngay xung quanh nó.

Một điều nữa là tác nhân không chỉ đơn giản di chuyển sang trái, phải, lên và xuống mà còn có định hướng.

Đặc vụ chỉ có thể di chuyển về phía trước, rẽ trái hoặc rẽ phải. Nó luôn được định hướng theo một hướng cụ thể và phải quay lại trước khi lùi lại chẳng hạn.

Chế độ xem một phần của tác nhân đối với môi trường là lấy mình làm trung tâm, nghĩa là tác nhân nhìn lưới như thể nó đang đối mặt với nó.

Khi tác nhân thay đổi hướng mà không di chuyển vị trí, chế độ xem của nó sẽ thay đổi.

Trạng thái mà chúng tôi nhận được từ môi trường là một tenxơ 7x7x3, vì vậy tác nhân chỉ nhìn thấy một vùng con 7x7 của lưới ở phía trước nó.

Kênh cuối cùng, thứ nguyên của trạng thái, mã hóa đối tượng nào, nếu có, hiện diện ở vị trí đó.

Môi trường thế giới lưới này là nơi thử nghiệm tốt cho mô-đun quan hệ của chúng tôi, vì để học cách chơi thành công, tác nhân phải học cách liên kết chìa khóa với ổ khóa và ổ khóa để có thể truy cập vào mục tiêu, tất cả đều là một dạng lý luận quan hệ.

Ngoài ra, trò chơi được thể hiện một cách tự nhiên bằng một tập hợp các đối tượng hoặc nút, vì mỗi vị trí pixel trong lưới thực sự là một đối tượng thực tế, không giống như trong ví dụ của Mnist.

Điều này có nghĩa là chúng ta có thể biết chính xác đối tượng mà tác nhân đang chú ý đến. Chúng ta có thể hy vọng nó học cách chú ý nhiều nhất đến chìa khóa, cánh cửa và ô đích, và chìa khóa đó có liên quan đến cánh cửa.

Nếu đúng như vậy, điều đó cho thấy tác nhân đang học không quá khác so với cách con người học cách liên hệ với các đối tượng trên lưới.

Nhìn chung, chúng tôi sẽ sử dụng lại mô-đun quan hệ mà chúng tôi đã tạo trước đó cho ví dụ Mnist dưới dạng Dqn quan hệ.

Vì vậy, chúng tôi thực sự chỉ cần thay đổi đầu ra thành hàm kích hoạt bình thường, thay vì softmax gạch dưới nhật ký mà chúng tôi đã sử dụng để phân loại.

Nhưng trước tiên, hãy quay lại việc thực hiện sự chú ý bằng nhiều đầu. Khi việc vận hành trên các tensor bậc cao trở nên phức tạp hơn, chúng ta sẽ nhận được trợ giúp từ gói có tên iNOP, giúp mở rộng khả năng của hàm EINSUM tích hợp sẵn của PyTorch.

Bạn có thể cài đặt nó bằng PIP.

Xem mã này.

Chỉ có hai chức năng quan trọng trong gói này là sắp xếp lại và thu gọn và chúng ta sẽ chỉ sử dụng một chức năng sắp xếp lại.

Về cơ bản, sắp xếp lại cho phép chúng ta định hình lại kích thước của tensor bậc cao hơn một cách dễ dàng và dễ đọc hơn các hàm PyTorch tích hợp sẵn và nó có cú pháp tương tự như iNSUM.

Ví dụ: chúng ta có thể sắp xếp lại kích thước của tensor như thế này.

Xem mã này.

Hoặc nếu chúng ta đã thu gọn các chiều không gian h và w thành một chiều n duy nhất cho các nút, chúng ta có thể hoàn tác việc này.

Xem mã này.

Trong trường hợp này, chúng tôi cho nó biết rằng đầu vào có ba chiều, nhưng chiều thứ hai bí mật là hai chiều, h, w, đã được thu gọn và chúng tôi muốn trích xuất chúng thành các chiều riêng biệt một lần nữa.

Chúng ta chỉ cần cho nó biết kích thước của h hoặc w và nó có thể suy ra kích thước của chiều khác.

Thay đổi chính đối với sự chú ý nhiều đầu là khi chúng ta chiếu ma trận nút ban đầu n dấu hai chấm r lũy thừa b x n x f vào các ma trận khóa, truy vấn và giá trị, chúng ta sẽ thêm một thứ nguyên đầu bổ sung.

QKV dấu hai chấm r lũy thừa của b x h x n x d, trong đó b là kích thước lô và h là kích thước đầu.

Chúng ta sẽ tùy ý đặt số mặt ngửa là ba cho ví dụ này.

Vậy h bằng ba, n bằng bảy nhân bảy bằng bốn mươi chín, d bằng sáu mươi bốn, trong đó n là số nút, chỉ là tổng số vị trí lưới được xem.

Và d là số chiều của vectơ đặc trưng nút, đây chỉ là thứ mà chúng tôi chọn theo kinh nghiệm là 64, nhưng các giá trị nhỏ hơn hoặc lớn hơn cũng có thể hoạt động tốt.

Chúng ta sẽ cần thực hiện phép co tensor giữa truy vấn và các tensor chính để thu được một tensor chú ý, dấu hai chấm r lũy thừa b x h x n x n, chuyển nó qua softmax, thu gọn cái này với tensor giá trị, thu gọn kích thước đầu với n chiều cuối cùng,

và thu gọn kích thước cuối cùng, được thu gọn, với một lớp tuyến tính để có được tensor nút được cập nhật của chúng ta, n dấu hai chấm r lũy thừa b x n x d, sau đó chúng ta có thể chuyển qua một lớp tự chú ý khác hoặc thu gọn tất cả các nút thành một vectơ duy nhất và chuyển nó qua một số lớp tuyến tính đến đầu ra cuối cùng.

Chúng tôi sẽ tập trung vào một lớp chú ý duy nhất cho tất cả các ví dụ.

Trước tiên, chúng ta sẽ xem xét một số dòng cụ thể trong mã khác với mô hình chú ý một đầu người. Mô hình đầy đủ được sao chép trong danh sách mười điểm bảy.

Để sử dụng mô-đun lớp tuyến tính tích hợp của PyTorch, chỉ là phép nhân ma trận cộng với vectơ thiên vị, chúng tôi sẽ tạo một lớp tuyến tính trong đó kích thước thứ nguyên cuối cùng được mở rộng theo số lượng đầu chú ý.

Xem mã này.

Chúng ta tạo ba lớp tuyến tính thông thường, riêng biệt giống như chúng ta đã làm với mô hình chú ý một đầu, nhưng lần này chúng ta sẽ mở rộng chiều cuối cùng bằng cách nhân nó với số lượng đầu chú ý.

Đầu vào của các lớp chiếu này là một loạt ma trận nút ban đầu, n dấu hai chấm r lũy thừa b x n x c và kích thước c bằng với kích thước kênh đầu ra của lớp chập cuối cùng, cộng với hai tọa độ không gian mà chúng tôi nối thêm.

Do đó, lớp tuyến tính co lại theo chiều kênh để cung cấp cho chúng ta các ma trận truy vấn, khóa và giá trị, q, k, v, dấu hai chấm r lũy thừa b x n bằng dấu ngoặc đơn mở, h x d, dấu ngoặc đơn đóng.

Vì vậy, chúng ta sẽ sử dụng chức năng sắp xếp lại i-nops để mở rộng chiều cuối cùng thành chiều đầu và chiều d.

Xem mã này.

Chúng tôi sẽ trích xuất kích thước đầu và d riêng biệt, đồng thời sắp xếp lại các kích thước sao cho kích thước đầu xuất hiện sau kích thước lô.

Nếu không có i-nops, mã này sẽ có nhiều mã hơn và gần như không thể đọc được.

Trong ví dụ này, chúng tôi cũng sẽ bỏ dấu chấm, tích bên trong làm hàm tương thích.

Hãy nhớ lại đây là hàm xác định sự giống nhau giữa truy vấn và khóa và thay vào đó hãy sử dụng thứ gọi là sự chú ý bổ sung, hình 10.20.

Sự chú ý của sản phẩm chấm sẽ hoạt động tốt, nhưng chúng tôi muốn minh họa rằng đó không phải là loại chức năng tương thích duy nhất và chức năng cộng thực sự ổn định và biểu cảm hơn một chút.

Hình 10.20, hàm tương thích tính toán độ tương tự giữa từng khóa và vectơ truy vấn, tạo ra ma trận kề.

Với sự chú ý của sản phẩm dấu chấm, chúng tôi tính toán khả năng tương thích, nghĩa là độ tương tự, giữa mỗi truy vấn và khóa bằng cách chỉ cần lấy sản phẩm dấu chấm giữa mỗi vectơ.

Khi hai vectơ giống nhau về mặt phần tử, tích số chấm sẽ mang lại giá trị dương lớn và khi chúng khác nhau, nó có thể mang lại giá trị gần bằng 0 hoặc giá trị âm lớn.

Điều này có nghĩa là đầu ra của tích số chấm, hàm tương thích không bị giới hạn theo cả hai hướng và chúng ta có thể nhận được các giá trị lớn hoặc nhỏ tùy ý.

Điều này có thể có vấn đề khi chúng ta chuyển nó qua hàm softmax, hàm này có thể dễ dàng bão hòa.

Theo độ bão hòa, chúng tôi muốn nói rằng khi một giá trị cụ thể trong vectơ đầu vào lớn hơn đáng kể so với các giá trị khác trong vectơ, thì softmax có thể gán tất cả khối lượng xác suất của nó cho giá trị đơn lẻ đó,

đặt tất cả những cái khác về 0 hoặc ngược lại.

Điều này có thể làm cho gradient của chúng ta quá lớn hoặc quá nhỏ đối với các giá trị cụ thể và làm mất ổn định quá trình đào tạo.

Sự chú ý bổ sung có thể giải quyết vấn đề này với chi phí phải đưa ra các tham số bổ sung.

Thay vì chỉ nhân các tensor Q&K với nhau, chúng ta sẽ chuyển cả hai qua các lớp tuyến tính độc lập, cộng chúng lại với nhau rồi áp dụng hàm kích hoạt, theo sau là một lớp tuyến tính khác,

hình 10.21.

Điều này cho phép tương tác phức tạp hơn giữa Q và K mà không có nhiều nguy cơ gây mất ổn định về số, vì phép cộng sẽ không phóng đại sự khác biệt về số như phép nhân.

Đầu tiên chúng ta cần thêm ba lớp tuyến tính mới để tăng thêm sự chú ý.

Hình 10.21.

Sự chú ý bổ sung là một giải pháp thay thế cho sự chú ý chấm sản phẩm có thể ổn định hơn.

Thay vì nhân các truy vấn và khóa với nhau, trước tiên chúng tôi chuyển chúng một cách độc lập qua các lớp tuyến tính, sau đó cộng chúng lại với nhau, áp dụng hàm phi tuyến tính và chuyển qua một lớp tuyến tính khác để thay đổi chiều.

Xem mã này.

Trong phương pháp chuyển tiếp, chúng tôi xác định các bước tính toán thực tế cho sự chú ý bổ sung.

Xem mã này.

Như bạn có thể thấy, chúng ta chuyển Q qua một lớp tuyến tính và K qua lớp tuyến tính của chính nó, cộng chúng lại với nhau và sau đó áp dụng hàm kích hoạt phi tuyến tính.

Sau đó, chúng tôi chuyển kết quả này qua một lớp tuyến tính khác và cuối cùng áp dụng softmax trên các hàng nút, cuối cùng mang lại tenxơ trọng số chú ý.

Bây giờ chúng ta làm tương tự như trước và thu gọn tensor chú ý với tensor V dọc theo N chiều cuối cùng để có được một tensor có kích thước B x H x N x D, là ma trận nút nhiều đầu.

Xem mã này.

Những gì chúng tôi muốn ở cuối mô-đun tự chú ý là một ma trận nút được cập nhật với các kích thước B x N x D, vì vậy chúng tôi sẽ nối hoặc thu gọn kích thước đầu và kích thước D, sau đó chuyển điều này qua một lớp tuyến tính để giảm kích thước trở lại kích thước D.

Xem mã này.

Hình dạng cuối cùng của cái này bây giờ là BBXNXD, đây chính xác là những gì chúng ta muốn.

Vì chúng tôi sẽ chỉ sử dụng một mô-đun tự chú ý duy nhất nên chúng tôi muốn giảm 3 tensor này thành 2 tensor chỉ gồm một loạt vectơ, do đó, chúng tôi sẽ gộp tối đa trên chiều cuối và sau đó chuyển kết quả qua lớp tuyến tính cuối cùng, đại diện cho các giá trị Q.

Xem mã này.

Thế thôi. Chúng ta vừa xem qua tất cả các dòng mã cốt lõi nhưng chúng ta hãy cùng nhau xem và kiểm tra nó.

Liệt kê 10.7, mô-đun quan hệ nhiều đầu.