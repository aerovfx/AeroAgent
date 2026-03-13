# Chương 10. Lập luận quan hệ với sự chú ý Học tăng cường sâu trong hành động, Phiên bản video được dịch

---

Phần 10.2, Lý luận quan hệ có chú ý

Có nhiều cách có thể để thực hiện một mô hình quan hệ. Chúng tôi biết những gì chúng tôi muốn, một mô hình có thể tìm hiểu cách các đối tượng trong dữ liệu đầu vào có liên quan với nhau.

Chúng tôi cũng muốn mô hình tìm hiểu các tính năng cấp cao hơn trên các đối tượng như vậy, giống như CNN.

Chúng tôi cũng muốn duy trì khả năng kết hợp của các mô hình học sâu thông thường để có thể xếp chồng nhiều lớp lại với nhau, chẳng hạn như các lớp CNN.

Để tìm hiểu ngày càng nhiều tính năng trừu tượng và có lẽ quan trọng nhất, chúng ta cần tính năng này có hiệu quả về mặt tính toán để có thể huấn luyện mô hình quan hệ này trên một lượng lớn dữ liệu.

Một mô hình chung có tên là tự chú ý đáp ứng tất cả các yêu cầu này, mặc dù nó có khả năng mở rộng kém hơn so với các mô hình khác mà chúng ta đã xem xét cho đến nay.

Tự chú ý, như tên cho thấy, liên quan đến một cơ chế chú ý trong đó mô hình có thể học cách chú ý đến một tập hợp con dữ liệu đầu vào.

Nhưng trước khi nói đến sự chú ý đến bản thân, trước tiên chúng ta hãy nói về sự chú ý thông thường.

Phần 10.2.1, Mô hình chú ý

Các mô hình chú ý được lấy cảm hứng lỏng lẻo từ các hình thức chú ý của con người và động vật. Với tầm nhìn của con người, chúng ta không thể nhìn hoặc tập trung vào toàn bộ tầm nhìn trước mặt.

Đôi mắt của chúng ta thực hiện các chuyển động loạn thần, nhanh, giật cục để quét qua tầm nhìn và chúng ta có thể quyết định một cách có ý thức việc tập trung vào một khu vực đặc biệt nổi bật trong tầm nhìn của mình.

Điều này cho phép chúng tôi tập trung vào việc xử lý các khía cạnh liên quan của một cảnh, đó là cách sử dụng tài nguyên hiệu quả.

Hơn nữa, khi chúng ta đang suy nghĩ và lý luận, chúng ta chỉ có thể chú ý đến một số việc cùng một lúc.

Một cách tự nhiên, chúng ta cũng có xu hướng sử dụng lý luận quan hệ khi nói những điều như anh ấy lớn tuổi hơn cô ấy hoặc cánh cửa đóng lại sau lưng tôi.

Chúng ta đang liên hệ các thuộc tính hoặc hành vi của một số vật thể trên thế giới với những vật thể khác.

Quả thực, các từ trong ngôn ngữ của con người nhìn chung chỉ truyền đạt ý nghĩa khi liên quan đến các từ khác.

Trong nhiều trường hợp, không có hệ quy chiếu tuyệt đối. Chúng ta chỉ có thể mô tả sự vật khi chúng liên quan đến những sự vật khác mà chúng ta biết.

Các mô hình chú ý tuyệt đối, không quan hệ được thiết kế để hoạt động giống như mắt của chúng ta, trong đó chúng cố gắng học cách chỉ trích xuất những phần có liên quan của dữ liệu đầu vào để đạt hiệu quả và khả năng diễn giải.

Bạn có thể thấy mô hình đang học tập để chú ý đến điều gì khi đưa ra quyết định, trong khi mô hình tự chú ý mà chúng tôi sẽ xây dựng ở đây là cách đưa lý luận quan hệ vào mô hình.

Mục tiêu không nhất thiết là chắt lọc dữ liệu.

Hình thức đơn giản nhất của sự chú ý tuyệt đối đối với bộ phân loại hình ảnh sẽ là một mô hình chủ động cắt xén hình ảnh, chọn các vùng con từ hình ảnh và chỉ xử lý chúng, hình 10.4.

Mô hình sẽ phải học những gì cần tập trung vào, nhưng điều này sẽ cho chúng ta biết nó đang sử dụng phần nào của hình ảnh để phân loại.

Điều này khó thực hiện vì việc cắt xén là không thể phân biệt được.

Để cắt hình ảnh 28x28 pixel, chúng tôi cần mô hình của mình tạo ra tọa độ có giá trị số nguyên tạo thành tiểu vùng hình chữ nhật thành tập hợp con, nhưng các hàm có giá trị số nguyên không liên tục và do đó không thể phân biệt được, nghĩa là chúng tôi không thể áp dụng thuật toán đào tạo dựa trên độ dốc giảm dần.

Hình 10.4. Một ví dụ về sự chú ý tuyệt đối trong đó một hàm có thể chỉ xem xét các vùng con của hình ảnh và chỉ xử lý từng vùng con đó tại một thời điểm.

Điều này có thể giảm đáng kể gánh nặng tính toán vì chiều của mỗi phân đoạn nhỏ hơn nhiều so với toàn bộ hình ảnh.

Chúng ta có thể huấn luyện một mô hình như vậy bằng thuật toán di truyền như bạn đã học ở chương 6 hoặc chúng ta có thể sử dụng học tăng cường.

Trong trường hợp học tăng cường, mô hình sẽ tạo ra một tập hợp tọa độ nguyên, cắt hình ảnh dựa trên các tọa độ đó, xử lý tiểu vùng và đưa ra quyết định phân loại.

Nếu phân loại chính xác, nó sẽ nhận được phần thưởng tích cực hoặc sẽ nhận được phần thưởng tiêu cực nếu phân loại không chính xác.

Bằng cách này, chúng ta có thể sử dụng thuật toán tăng cường mà bạn đã học trước đó để huấn luyện mô hình thực hiện một hàm không khả vi.

Quy trình này được mô tả trong bài báo về các mô hình chú ý trực quan tái diễn của Volodymyr Minni, 2014.

Hình thức chú ý này được gọi là chú ý cứng vì nó không thể phân biệt được.

Ngoài ra còn có chú ý mềm, là một dạng chú ý có thể phân biệt, chỉ cần áp dụng bộ lọc để giảm thiểu hoặc duy trì các pixel nhất định trong hình ảnh bằng cách nhân từng pixel trong ảnh với giá trị chú ý mềm trong khoảng từ 0 đến 1.

Sau đó, mô hình chú ý có thể học cách đặt một số pixel nhất định về 0 hoặc duy trì một số pixel có liên quan nhất định, hình 10.5.

Vì các giá trị chú ý là số thực chứ không phải số nguyên nên dạng chú ý này có thể phân biệt được, nhưng nó làm mất hiệu quả của mô hình chú ý cứng vì nó vẫn cần xử lý toàn bộ hình ảnh thay vì chỉ một phần của nó.

Hình 10.5. Một ví dụ về sự chú ý nhẹ nhàng trong đó mô hình sẽ tìm hiểu pixel nào cần giữ và pixel nào cần bỏ qua. Tức là đặt thành 0.

Không giống như mô hình chú ý cứng, mô hình chú ý mềm cần xử lý toàn bộ hình ảnh cùng một lúc, điều này có thể đòi hỏi tính toán cao.

Trong mô hình tự chú ý, SAM, quá trình này khá khác biệt và phức tạp hơn.

Hãy nhớ rằng, đầu ra của SAM về cơ bản là một biểu đồ, ngoại trừ việc mỗi nút bị hạn chế chỉ được kết nối với một vài nút khác, do đó có khía cạnh chú ý.

Mục 10.2.2, suy luận quan hệ.

Trước khi đi vào chi tiết về sự tự chú ý, trước tiên chúng ta hãy phác thảo cách hoạt động của một mô-đun lý luận quan hệ chung.

Bất kỳ mô hình học máy nào thường được cung cấp một số dữ liệu thô ở dạng vectơ hoặc tensor bậc cao hơn hoặc có thể là một chuỗi các tensor như vậy, như trong các mô hình ngôn ngữ.

Hãy sử dụng một ví dụ từ mô hình hóa ngôn ngữ hoặc xử lý ngôn ngữ tự nhiên, NLP, vì nó dễ nắm bắt hơn một chút so với xử lý hình ảnh thô.

Hãy xem xét nhiệm vụ dịch một câu đơn giản từ tiếng Anh sang tiếng Trung.

Xem bảng này.

Mỗi từ, w, i, trong tiếng Anh, được mã hóa dưới dạng một vectơ nóng một chiều có độ dài cố định, w, i dấu hai chấm b lũy thừa N, với chiều N.

Kích thước xác định kích thước từ vựng tối đa. Ví dụ: nếu N bằng 10, mô hình chỉ có thể xử lý tổng cộng từ vựng là 10 từ, do đó, nó thường lớn hơn nhiều, chẳng hạn như N xấp xỉ bằng 40.000.

Tương tự, mỗi từ trong tiếng Trung được mã hóa dưới dạng một vectơ có độ dài cố định. Chúng tôi muốn xây dựng một mô hình dịch thuật có thể dịch từng từ tiếng Anh sang tiếng Trung.

Các cách tiếp cận đầu tiên cho vấn đề này dựa trên các mạng thần kinh tái phát, vốn là các mô hình tuần tự, vì chúng có khả năng lưu trữ dữ liệu từ mỗi đầu vào.

Mạng thần kinh tái phát, ở mức cao, là một hàm duy trì trạng thái bên trong được cập nhật với mỗi đầu vào mà nó nhìn thấy, hình 10.6.

Hình 10.6, mạng thần kinh tái diễn, RNN, có khả năng duy trì trạng thái bên trong được cập nhật với mỗi đầu vào mới mà nó nhận được. Điều này cho phép RNN mô hình hóa dữ liệu tuần tự như chuỗi thời gian hoặc ngôn ngữ.

Hầu hết các mô hình ngôn ngữ RNN hoạt động bằng cách trước tiên có một mô hình bộ mã hóa sử dụng một từ tiếng Anh tại một thời điểm và sau khi hoàn thành, sẽ cung cấp vectơ trạng thái bên trong của nó cho một bộ giải mã RNN khác để xuất ra từng từ tiếng Trung riêng lẻ.

Vấn đề với RNN là chúng không dễ dàng song song hóa vì bạn phải duy trì trạng thái bên trong, trạng thái này phụ thuộc vào độ dài chuỗi, hình 10.7.

Nếu độ dài chuỗi khác nhau giữa đầu vào và đầu ra, bạn phải đồng bộ hóa tất cả các chuỗi cho đến khi chúng được xử lý xong.

Hình 10.7, sơ đồ mô hình ngôn ngữ RNN. Hai RN riêng biệt được sử dụng, bộ mã hóa và bộ giải mã. Bộ mã hóa lấy từng từ trong câu đầu vào và sau khi hoàn thành, sẽ gửi trạng thái bên trong của nó tới bộ giải mã RNN, bộ giải mã này tạo ra từng từ trong câu đích cho đến khi nó dừng lại.

Trong khi nhiều người nghĩ rằng các mô hình ngôn ngữ cần lặp lại để hoạt động tốt, do tính chất tuần tự tự nhiên của ngôn ngữ, các nhà nghiên cứu nhận thấy rằng một mô hình chú ý tương đối đơn giản và không có sự lặp lại nào có thể hoạt động tốt hơn và có thể song song hóa một cách tầm thường, giúp đào tạo nhanh hơn và với nhiều dữ liệu hơn dễ dàng hơn.

Đây là những mô hình được gọi là máy biến áp, dựa vào sự chú ý của bản thân. Chúng tôi sẽ không đi vào chi tiết của họ. Chúng ta sẽ chỉ phác thảo cơ chế cơ bản ở đây.

Ý tưởng là một từ tiếng Trung, C-I, có thể được dịch là một hàm số của sự kết hợp có trọng số trong ngữ cảnh của các từ tiếng Anh, E-I.

Ngữ cảnh chỉ đơn giản là một tập hợp các từ có độ dài cố định gần với một từ tiếng Anh nhất định.

Ra lệnh, con chó Max của tôi đuổi một con sóc lên cây và sủa nó. Ngữ cảnh có ba từ cho từ sóc sẽ là câu phụ, Max đuổi một con sóc lên cây.

Nghĩa là, chúng tôi bao gồm ba từ ở hai bên của từ mục tiêu.

Đối với cụm từ tiếng Anh I-8 food trong hình 10.7, chúng ta sẽ sử dụng cả ba từ. Từ tiếng Trung đầu tiên sẽ được tạo ra bằng cách lấy tổng có trọng số của tất cả các từ tiếng Anh trong câu, C-I bằng F của tổng A-I nhân E-I, trong đó A-I là sự chú ý, trọng số, là một số từ 0 đến 1 sao cho tổng của A-I bằng 1.

Hàm F sẽ là một mạng nơ-ron, chẳng hạn như mạng nơ-ron chuyển tiếp đơn giản. Toàn bộ hàm sẽ cần phải tìm hiểu các trọng số của mạng thần kinh trong F, cũng như các trọng số chú ý, A-I.

Trọng số chú ý sẽ được tạo ra bởi một số chức năng mạng lưới thần kinh khác.

Sau khi đào tạo thành công, chúng ta có thể kiểm tra các trọng số chú ý này và xem những từ tiếng Anh nào được chú ý khi dịch sang một từ tiếng Trung nhất định.

Ví dụ: khi tạo ra từ tiếng Trung, từ này, từ tiếng Anh I, sẽ có mức độ chú ý cao liên quan đến nó, trong khi các từ khác hầu như bị bỏ qua.

Thủ tục chung này được gọi là hồi quy kernel. Để lấy một ví dụ đơn giản hơn nữa, giả sử chúng ta có một tập dữ liệu trông giống như hình 10.8 và chúng ta muốn tạo một mô hình học máy có thể lấy X không nhìn thấy và dự đoán Y thích hợp dựa trên dữ liệu huấn luyện này.

Có hai loại chính về cách thực hiện việc này, phương pháp không tham số và phương pháp tham số.

Hình 10.8, biểu đồ phân tán của tập dữ liệu phi tuyến tính mà chúng ta có thể muốn huấn luyện thuật toán hồi quy trên đó.

Mạng nơ-ron là các mô hình tham số vì chúng có một tập hợp các tham số có thể điều chỉnh cố định. Một hàm đa thức đơn giản như F của X bằng AX lập phương cộng BX bình cộng C là một mô hình tham số vì chúng ta có ba tham số ABC mà chúng ta có thể huấn luyện để khớp hàm này với một số dữ liệu.

Mô hình phi tham số là mô hình không có tham số có thể huấn luyện hoặc có khả năng điều chỉnh linh hoạt số lượng tham số dựa trên dữ liệu huấn luyện.

Hồi quy hạt nhân là một ví dụ về mô hình phi tham số để dự đoán. Phiên bản đơn giản nhất của hồi quy hạt nhân là chỉ cần tìm các điểm X I gần nhất trong dữ liệu huấn luyện, X, cho một số đầu vào mới, X, sau đó trả về giá trị trung bình của Y tương ứng thuộc về chữ Y trong dữ liệu huấn luyện.

Hình 10.9, một cách để thực hiện hồi quy hạt nhân phi tham số để dự đoán thành phần Y của giá trị X mới là tìm giá trị tương tự nhất, nghĩa là gần nhất, X nằm trong dữ liệu huấn luyện, sau đó lấy trung bình của các thành phần Y tương ứng của chúng.

Tuy nhiên, trong trường hợp này, chúng ta phải chọn có bao nhiêu điểm đủ điều kiện là điểm lân cận gần nhất với đầu vào X và đó là vấn đề vì tất cả những điểm lân cận gần nhất này đều đóng góp như nhau vào kết quả.

Lý tưởng nhất là chúng ta có thể đợi hoặc tham dự tất cả các điểm trong tập dữ liệu theo mức độ giống nhau của chúng với đầu vào, sau đó lấy tổng trọng số của YI tương ứng của chúng để đưa ra dự đoán.

Chúng ta cần một hàm nào đó, hàm F, ánh xạ từ tập X đến tập A, một hàm nhận đầu vào, X thuộc về X viết hoa và trả về một tập hợp trọng số chú ý, A thuộc về chữ hoa A mà chúng ta có thể sử dụng để thực hiện tổng có trọng số này.

Quy trình này về cơ bản chính xác là những gì chúng ta sẽ làm trong các mô hình chú ý, ngoại trừ khó khăn nằm ở việc quyết định cách tính toán trọng số chú ý một cách hiệu quả.

Nói chung, mô hình tự chú ý tìm cách lấy một tập hợp các đối tượng và tìm hiểu xem mỗi đối tượng đó có liên quan như thế nào với các đối tượng khác thông qua trọng số chú ý.

Trong lý thuyết đồ thị, đồ thị là một cấu trúc dữ liệu, G bằng NE, nghĩa là tập hợp các nút, N và các cạnh, kết nối hoặc quan hệ, giữa các nút, E.

Bộ sưu tập, N, có thể chỉ là một tập hợp các nhãn nút chẳng hạn như tập hợp các số tự nhiên, bắt đầu từ 0 và đếm trở lên hoặc mỗi nút có thể chứa dữ liệu và do đó mỗi nút có thể được biểu thị bằng một vectơ đặc trưng nào đó.

Trong trường hợp sau, chúng ta có thể lưu trữ tập hợp các nút của mình dưới dạng ma trận N dấu hai chấm R lũy thừa N nhân F, trong đó F là thứ nguyên đặc trưng, ​​sao cho mỗi hàng là một vectơ đặc trưng cho nút đó.

Tập hợp các cạnh, E, có thể được biểu diễn bằng ma trận kề, E dấu hai chấm R lũy thừa N x N, trong đó mỗi hàng và cột là các nút, sao cho một giá trị cụ thể ở hàng 2, cột 3 biểu thị độ mạnh của mối quan hệ giữa nút 2 và nút 3, bảng bên phải của hình 10.10.

Đây là cách thiết lập rất cơ bản cho biểu đồ, nhưng biểu đồ có thể phức tạp hơn khi ngay cả các cạnh cũng có vectơ đặc trưng liên kết với chúng. Chúng tôi sẽ không thử điều đó ở đây.

Hình 10.10. Cấu trúc biểu đồ ở bên trái có thể được biểu diễn một cách định lượng bằng ma trận tính năng nút mã hóa các tính năng nút riêng lẻ và ma trận kề mã hóa các cạnh, nghĩa là các kết nối hoặc mũi tên, giữa các nút.

Giá trị 1 ở hàng A trong cột B biểu thị rằng nút A có cạnh từ A đến B. Các tính năng của nút có thể giống như giá trị RGBA nếu các nút biểu thị pixel.

Mô hình tự chú ý hoạt động bằng cách bắt đầu với một tập hợp các nút, N dấu hai chấm R lũy thừa N x F, sau đó tính toán trọng số chú ý giữa tất cả các cặp nút.

Trên thực tế, nó tạo ra ma trận cạnh E dấu hai chấm R lũy thừa N x N. Sau khi tạo ma trận cạnh, nó sẽ cập nhật các tính năng của nút, sao cho mỗi loại nút được trộn cùng với các nút khác mà nó tham dự.

Theo một nghĩa nào đó, mỗi nút sẽ gửi một thông báo đến các nút khác mà nó chú ý nhiều nhất và khi các nút nhận được tin nhắn từ các nút khác, chúng sẽ tự cập nhật.

Chúng ta gọi quy trình một bước này là mô-đun quan hệ, sau đó chúng ta nhận được ma trận nút cập nhật, N dấu hai chấm R lũy thừa N x F, mà chúng ta có thể chuyển sang một mô-đun quan hệ khác sẽ thực hiện điều tương tự, Hình 10.11.

Bằng cách kiểm tra ma trận cạnh, chúng ta có thể biết nút nào đang tham dự nút nào khác và nó cho chúng ta ý tưởng về lý do của mạng lưới thần kinh.

Hình 10.11, một mô-đun quan hệ ở mức cao nhất xử lý ma trận nút, N dấu hai chấm R lũy thừa N x F và xuất ra ma trận nút cập nhật mới, N dấu hai chấm R lũy thừa N x D, trong đó chiều của tính năng nút có thể khác nhau.

Trong mô hình ngôn ngữ tự chú ý, mỗi từ trong một ngôn ngữ sẽ chú ý đến tất cả các từ trong ngữ cảnh của ngôn ngữ kia, nhưng sự chú ý chờ đợi hoặc các cạnh biểu thị mức độ mà mỗi từ đang chú ý, nghĩa là có liên quan đến từng từ khác.

Do đó, mô hình ngôn ngữ tự chú ý có thể tiết lộ ý nghĩa của một từ tiếng Trung được dịch đối với các từ trong câu tiếng Anh.

Ví dụ, từ tiếng Trung, this, có nghĩa là ăn, vì vậy từ tiếng Trung này sẽ có tầm quan trọng lớn đối với việc ăn, nhưng sẽ chỉ chú ý đến các từ khác hàng tuần.

Tự chú ý có ý nghĩa trực quan hơn khi được sử dụng trong mô hình ngôn ngữ, nhưng trong cuốn sách này, chúng ta chủ yếu đề cập đến các mô hình máy học hoạt động trên dữ liệu trực quan, chẳng hạn như pixel từ khung hình video.

Tuy nhiên, dữ liệu trực quan không có cấu trúc tự nhiên như một tập hợp các đối tượng hoặc nút mà chúng ta có thể chuyển trực tiếp vào mô-đun quan hệ.

Chúng ta cần một cách để biến một loạt pixel thành một tập hợp các đối tượng. Một cách để làm điều đó là chỉ cần gọi mỗi pixel riêng lẻ là một đối tượng, để làm cho mọi thứ hiệu quả hơn về mặt tính toán và để có thể xử lý hình ảnh thành các đối tượng có ý nghĩa hơn, trước tiên chúng ta có thể chuyển hình ảnh thô qua một vài lớp chập sẽ trả về một tenxơ có kích thước.

Bằng cách này, chúng ta có thể xác định các đối tượng trong hình ảnh tích chập dưới dạng vectơ trên chiều kênh. Nghĩa là, mỗi vật thể là một vectơ có chiều C và sẽ có n bằng h nhân w số lượng vật thể, hình 10.12.

Hình 10.12, một lớp tích chập trả về một loạt các bộ lọc tích chập được lưu trữ trong một tensor ba với các kênh hình dạng. Tức là số lượng bộ lọc, theo chiều cao và chiều rộng.

Chúng ta có thể biến điều này thành một tập hợp các nút bằng cách lấy các lát dọc theo kích thước kênh trong đó mỗi nút khi đó là một vectơ độ dài kênh, với tổng số nút chiều cao nhân với chiều rộng.

Chúng tôi gói chúng thành một ma trận mới có kích thước n theo C, trong đó n là số nút và C là kích thước kênh.

Sau khi hình ảnh thô được xử lý thông qua một số lớp CNN đã được huấn luyện, chúng tôi hy vọng rằng mỗi vị trí trong bản đồ đối tượng tương ứng với các đặc điểm nổi bật cụ thể trong hình ảnh bên dưới.

Ví dụ: chúng tôi hy vọng CNN có thể học cách phát hiện các đối tượng trong hình ảnh mà sau đó chúng tôi có thể chuyển vào mô-đun quan hệ của mình để xử lý mối quan hệ giữa các đối tượng.

Mỗi bộ lọc tích chập học một tính năng cụ thể cho từng vị trí không gian, do đó, việc lấy tất cả các tính năng đã học này cho một vị trí lưới x, y cụ thể trong một hình ảnh sẽ tạo ra một vectơ duy nhất cho vị trí đó mã hóa tất cả các tính năng đã học.

Chúng ta có thể thực hiện điều này cho tất cả các vị trí lưới để thu thập một tập hợp các đối tượng giả định trong ảnh mà chúng ta có thể biểu thị dưới dạng các nút trong biểu đồ, ngoại trừ việc chúng ta chưa biết kết nối giữa các nút.

Đó là những gì mô-đun lý luận quan hệ của chúng tôi sẽ cố gắng thực hiện.

Phần 10.2.3, các mô hình tự chú ý.

Có nhiều cách khả thi để xây dựng một mô-đun quan hệ, nhưng như chúng ta đã thảo luận, chúng ta sẽ triển khai một mô-đun dựa trên cơ chế tự chú ý.

Chúng tôi đã mô tả ý tưởng ở mức độ cao, nhưng đã đến lúc chúng tôi đi vào chi tiết thực hiện.

Mô hình mà chúng tôi sẽ xây dựng dựa trên mô hình được mô tả trong bài báo, học tăng cường sâu với các thành kiến ​​quy nạp quan hệ của Vynichius Zambaldi, 2019, từ DeepMind.

Chúng ta đã thảo luận về khuôn khổ cơ bản của ma trận nút N mũ R mũ N mũ F và ma trận cạnh E mũ R mũ N mũ N và chúng ta đã thảo luận về nhu cầu xử lý hình ảnh thô thành ma trận nút.

Giống như hồi quy kernel, chúng ta cần một số cách tính toán khoảng cách, hoặc ngược lại, độ tương tự giữa hai nút.

Không có lựa chọn duy nhất nào cho việc này, nhưng một cách tiếp cận phổ biến là chỉ cần lấy tích bên trong, còn được gọi là tích chấm, giữa hai nút vectơ đặc trưng làm độ tương tự của chúng.

Tích số chấm giữa hai vectơ có độ dài bằng nhau được tính bằng cách nhân các phần tử tương ứng trong mỗi vectơ rồi tính tổng kết quả.

Ví dụ: tích bên trong giữa các vectơ a bằng 1 trừ 2, 3 và b bằng trừ 1, 5, trừ 2, được ký hiệu là cặp có thứ tự gồm a và b và được tính là cặp có thứ tự gồm a và b bằng chữ in hoa S, a, i, b, i, trong trường hợp này là 1 nhân trừ 1 cộng trừ 2 nhân 5 cộng 3 nhân trừ 2 bằng trừ 1 trừ 10 trừ 6 bằng trừ 7.

Dấu của mỗi phần tử trong a và b trái ngược nhau, do đó tích bên trong thu được là số âm cho thấy sự bất đồng mạnh mẽ giữa các vectơ.

Ngược lại, nếu a bằng 1 trừ 2, 3, b bằng 2 trừ 3, 2 thì cặp có thứ tự gồm a và b bằng 14, đây là một số dương lớn, vì hai vectơ giống nhau hơn theo từng phần tử.

Do đó, tích chấm cho chúng ta một cách dễ dàng để tính toán độ tương tự giữa một cặp vectơ, chẳng hạn như các nút trong ma trận nút của chúng ta.

Cách tiếp cận này dẫn đến cái được gọi là sự chú ý của sản phẩm chấm theo tỷ lệ, phần được chia tỷ lệ sẽ phát huy tác dụng sau này.

Khi chúng ta có tập hợp nút ban đầu trong ma trận nút N, chúng ta sẽ chiếu ma trận này thành ba ma trận nút riêng biệt mới được gọi là khóa, truy vấn và giá trị.

Với ví dụ hồi quy kernel, truy vấn là x mới mà chúng ta muốn dự đoán y tương ứng, là giá trị, truy vấn là x, y là giá trị.

Để tìm giá trị, chúng ta phải xác định vị trí x i gần nhất và dữ liệu huấn luyện, đây là chìa khóa.

Chúng tôi đo lường mức độ tương tự giữa truy vấn và khóa, tìm các khóa giống nhất với truy vấn và sau đó trả về giá trị trung bình cho bộ khóa đó.

Đây chính xác là những gì chúng ta sẽ tự chú ý thực hiện, ngoại trừ các truy vấn, khóa và giá trị đều sẽ có cùng nguồn gốc.

Chúng tôi nhân ma trận nút ban đầu với ba ma trận chiếu riêng biệt để tạo ra ma trận truy vấn, ma trận khóa và ma trận giá trị.

Các ma trận chiếu sẽ được học trong quá trình huấn luyện, giống như bất kỳ tham số nào khác trong mô hình.

Trong quá trình đào tạo, ma trận chiếu sẽ học cách tạo ra các truy vấn, khóa và giá trị dẫn đến trọng số chú ý tối ưu, hình 10.13.

Hình 10.13, chế độ xem cấp cao của mô-đun quan hệ dựa trên sự chú ý.

Đầu vào của mô-đun quan hệ là ma trận nút N dấu hai chấm chấm N x F với N nút, mỗi nút có vectơ đặc trưng F chiều.

Sau đó, mô-đun quan hệ sao chép ma trận này thành tổng cộng ba bản sao và chiếu mỗi bản sao vào một ma trận mới thông qua một lớp tuyến tính đơn giản không có chức năng kích hoạt, tạo ra các ma trận truy vấn, khóa và giá trị riêng biệt.

Các ma trận truy vấn và khóa là đầu vào của hàm tương thích, là bất kỳ hàm nào tính toán mức độ tương thích, tương tự theo một cách nào đó.

Mỗi nút đối với nhau, dẫn đến một tập hợp các trọng số chú ý không chuẩn hóa, dấu hai chấm R lũy thừa của N nhân N.

Ma trận này sau đó được chuẩn hóa thông qua hàm softmax trên các hàng, sao cho giá trị của mỗi hàng sẽ có tổng bằng 1.

Sau đó, ma trận giá trị và ma trận chú ý chuẩn hóa được nhân lên và dấu mũ bằng AV.

Đầu ra của mô-đun quan hệ sau đó thường được truyền qua một hoặc nhiều lớp tuyến tính, không được mô tả.

Hãy lấy một cặp nút để tạo ra kết cấu cụ thể này. Giả sử chúng ta có một nút, là một vectơ đặc trưng, dấu hai chấm R lũy thừa 10 và một nút khác, b dấu hai chấm R lũy thừa 10.

Để tính toán mức độ tự chú ý của hai nút này, trước tiên chúng ta sẽ chiếu các nút này vào một không gian mới bằng cách nhân với một số ma trận chiếu.

Nghĩa là, aq bằng a lũy thừa của t, q, aq bằng a lũy thừa của t, k, av bằng a lũy thừa của t, v, trong đó chỉ số trên t biểu thị sự chuyển vị, sao cho vectơ nút bây giờ là vectơ cột, ví dụ: a lũy thừa của t dấu hai chấm R lũy thừa 1 x 10.

Ma trận tương ứng là q dấu hai chấm R lũy thừa 10 nhân d, sao cho aq bằng a lũy thừa t, q dấu hai chấm R lũy thừa d.

Bây giờ chúng ta có ba phiên bản mới của a có thể có một số chiều khác nhau so với đầu vào, ví dụ: aq, a, k, a, v dấu hai chấm R đến lũy thừa 20.

Chúng tôi làm tương tự cho nút b. Trước tiên, chúng ta có thể tính toán mức độ liên quan của a với chính nó bằng cách nhân thông qua tích bên trong, truy vấn và khóa của nó với nhau.

Hãy nhớ rằng, chúng tôi tính toán tất cả các tương tác theo cặp giữa các nút, bao gồm cả tương tác giữa các nút. Không có gì đáng ngạc nhiên, các đối tượng có khả năng liên quan đến chính chúng, mặc dù không nhất thiết, vì các truy vấn và khóa tương ứng, sau khi chiếu, có thể khác nhau.

Sau khi nhân truy vấn và khóa với nhau cho đối tượng a, chúng ta sẽ nhận được trọng số chú ý không chuẩn hóa. Giá trị của wa a bằng cặp có thứ tự aq, a, k, là một giá trị vô hướng duy nhất cho sự tự chú ý giữa a và a, chính nó.

Sau đó, chúng tôi thực hiện tương tự đối với tương tác theo cặp giữa a và b và b và a và b và b, vì vậy chúng tôi nhận được tổng cộng bốn trọng số chú ý. Đây có thể là các số lớn hoặc nhỏ tùy ý, do đó, chúng tôi chuẩn hóa tất cả các trọng số chú ý bằng cách sử dụng hàm softmax, như bạn có thể nhớ, hàm này nhận một loạt các số hoặc một vectơ và chuẩn hóa tất cả các giá trị ở trong khoảng 0, 1 và buộc chúng tổng bằng 1, để chúng tạo thành một phân bố xác suất rời rạc thích hợp.

Sự chuẩn hóa này buộc cơ chế chú ý chỉ tập trung vào những gì thực sự cần thiết cho nhiệm vụ. Nếu không có sự chuẩn hóa này, mô hình có thể dễ dàng xử lý mọi thứ và nó sẽ không thể giải thích được.

Sau khi đã chuẩn hóa được trọng số chú ý, chúng ta có thể thu thập chúng vào ma trận trọng số chú ý. Trong ví dụ đơn giản của chúng ta với hai đối tượng a và b, đây sẽ là ma trận 2 x 2.

Sau đó, chúng ta có thể nhân ma trận chú ý với từng vectơ giá trị, điều này sẽ tăng hoặc giảm các phần tử trong mỗi giá trị vectơ, tùy theo trọng số chú ý. Điều này sẽ cung cấp cho chúng ta một tập hợp các vectơ nút mới và được cập nhật. Mỗi nút đã được cập nhật dựa trên sức mạnh mối quan hệ của nó với các nút khác.

Thay vì nhân từng vectơ riêng lẻ với nhau, chúng ta có thể nhân toàn bộ ma trận nút với nhau. Thật vậy, chúng ta có thể kết hợp ba bước của phép nhân truy vấn khóa một cách hiệu quả để tạo thành ma trận chú ý, sau đó là ma trận chú ý với phép nhân ma trận giá trị và cuối cùng chuẩn hóa thành phép nhân ma trận hiệu quả.

Biểu thức này, trong đó q dấu hai chấm R lũy thừa của n nhân f, k lũy thừa của t dấu hai chấm R lũy thừa của f nhân n, v dấu hai chấm R lũy thừa của n nhân f, trong đó n là số nút, f là thứ nguyên của vectơ đặc trưng nút, q là ma trận truy vấn, k là ma trận khóa và v là ma trận giá trị.

Bạn có thể thấy rằng kết quả của q k lũy thừa t sẽ là ma trận n nhân n chiều, là ma trận kề như chúng tôi đã mô tả trước đó, nhưng trong ngữ cảnh này, chúng tôi gọi nó là ma trận trọng số chú ý.

Mỗi hàng và cột đại diện cho một nút. Nếu giá trị ở hàng 0 và cột một cao, chúng ta biết rằng nút 0 liên quan chặt chẽ đến nút một. Sự chú ý được chuẩn hóa, đó là ma trận kề, ma trận trọng số a bằng softmax của q k lũy thừa của t dấu hai chấm R lũy thừa của n x n, cho chúng ta biết tất cả các tương tác theo cặp giữa các nút.

Sau đó, chúng tôi nhân giá trị này với ma trận giá trị, ma trận này sẽ cập nhật vectơ đặc trưng của mỗi nút theo tương tác của nó với các nút khác, sao cho kết quả cuối cùng là ma trận nút được cập nhật, n dấu hai chấm mũ R lũy thừa n x f.

Sau đó, chúng ta có thể chuyển ma trận nút cập nhật này qua một lớp tuyến tính để thực hiện tìm hiểu bổ sung về các tính năng của nút và áp dụng tính phi tuyến tính để mô hình hóa các tính năng phức tạp hơn. Chúng tôi gọi toàn bộ quy trình này là mô-đun quan hệ hoặc khối quan hệ.

Chúng ta có thể xếp chồng các mô-đun quan hệ này một cách tuần tự để tìm hiểu các mối quan hệ bậc cao hơn và phức tạp hơn.

Trong hầu hết các trường hợp, đầu ra cuối cùng của mô hình mạng nơ-ron của chúng ta cần phải là một vectơ nhỏ, chẳng hạn như đối với các giá trị q trong dqn. Sau khi xử lý đầu vào thông qua một hoặc nhiều mô-đun quan hệ, chúng ta có thể giảm ma trận xuống một vectơ bằng cách thực hiện thao tác nhóm tối đa hoặc thao tác nhóm AVG.

Đối với ma trận nút, n dấu hai chấm mũ R lũy thừa n x f, một trong hai phép toán gộp này được áp dụng trên chiều cuối sẽ tạo ra một vectơ f chiều.

Nhóm tối đa chỉ lấy giá trị tối đa dọc theo chiều cuối. Sau đó, chúng ta có thể chạy vectơ gộp này qua một hoặc nhiều lớp tuyến tính trước khi trả về kết quả cuối cùng dưới dạng giá trị q.