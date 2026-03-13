# Chương 10. Học tăng cường có thể giải thích được Các mô hình chú ý và quan hệ Học tăng cường sâu trong hành động, Phiên bản video được dịch

---

Chương 10. Các mô hình học tập củng cố, chú ý và quan hệ có thể giải thích được.

Chương này bao gồm. Triển khai thuật toán củng cố quan hệ bằng mô hình tự chú ý phổ biến.

Trực quan hóa bản đồ chú ý để diễn giải tốt hơn lý do của tác nhân RL.

Lý luận về tính bất biến và đẳng thức của mô hình.

Kết hợp học tập double-q để cải thiện tính ổn định của quá trình đào tạo.

Hy vọng đến thời điểm này, bạn đã đánh giá cao sự kết hợp giữa học sâu và học tăng cường mạnh mẽ như thế nào,

để giải quyết các nhiệm vụ trước đây được cho là lĩnh vực độc quyền của con người.

Học sâu là một lớp các thuật toán học tập mạnh mẽ có thể hiểu và suy luận thông qua các mẫu và dữ liệu phức tạp,

và học tăng cường là khuôn khổ chúng tôi sử dụng để giải quyết các vấn đề điều khiển.

Xuyên suốt cuốn sách này, chúng tôi đã sử dụng trò chơi làm phòng thí nghiệm để thử nghiệm các thuật toán học tăng cường,

vì chúng cho phép chúng tôi đánh giá khả năng của các thuật toán này trong môi trường được kiểm soát chặt chẽ.

Khi chúng tôi xây dựng một tác nhân RL học cách chơi tốt một trò chơi, chúng tôi thường hài lòng rằng thuật toán của chúng tôi đang hoạt động.

Tất nhiên, học tăng cường có nhiều ứng dụng hơn ngoài việc chơi game.

Trong một số miền khác, hiệu suất thô của thuật toán sử dụng một số số liệu, ví dụ: phần trăm độ chính xác trên một số tác vụ,

sẽ không hữu ích nếu không biết thuật toán đưa ra quyết định như thế nào.

Ví dụ: các thuật toán học máy được sử dụng trong các quyết định chăm sóc sức khỏe cần phải dễ giải thích,

vì bệnh nhân có quyền biết tại sao họ được chẩn đoán mắc một căn bệnh cụ thể,

hoặc tại sao họ lại được khuyến nghị một phương pháp điều trị cụ thể.

Mặc dù mạng lưới thần kinh sâu thông thường có thể được đào tạo để đạt được những thành tựu đáng chú ý,

thường không rõ quy trình nào đang thúc đẩy việc ra quyết định của họ.

Trong chương này, chúng tôi sẽ giới thiệu một kiến ​​trúc deep learning mới giúp giải quyết vấn đề này.

Hơn nữa, nó không chỉ mang lại lợi ích về khả năng diễn giải mà còn tăng hiệu suất trong nhiều trường hợp.

Lớp mô hình mới này được gọi là mô hình chú ý, bởi vì chúng học cách chú ý hoặc tập trung vào,

chỉ những khía cạnh nổi bật của một đầu vào.

Cụ thể hơn cho trường hợp của chúng tôi, chúng tôi sẽ phát triển một mô hình tự chú ý,

đây là mô hình cho phép mỗi tính năng trong một đầu vào học cách chú ý đến nhiều tính năng khác trong đầu vào.

Hình thức chú ý này có liên quan chặt chẽ đến lớp mạng lưới thần kinh được gọi là mạng lưới thần kinh đồ thị,

là các mạng thần kinh được thiết kế rõ ràng để hoạt động trên dữ liệu có cấu trúc biểu đồ.

Phần 10.1, khả năng diễn giải của máy học với sự chú ý và các thành kiến ​​quan hệ.

Biểu đồ, còn được gọi là mạng, là cấu trúc dữ liệu bao gồm một tập hợp các nút và cạnh,

kết nối giữa các nút, hình 10.1.

Các nút có thể đại diện cho bất cứ thứ gì, mọi người trong mạng xã hội, các ấn phẩm trong mạng trích dẫn xuất bản,

các thành phố được kết nối bằng đường cao tốc hoặc thậm chí là hình ảnh trong đó mỗi pixel là một nút và các pixel liền kề được kết nối bằng các cạnh.

Biểu đồ là một cấu trúc rất chung để biểu diễn dữ liệu bằng cấu trúc quan hệ, gần như là tất cả dữ liệu chúng ta thấy trong thực tế.

Trong khi mạng nơ-ron tích chập được thiết kế để xử lý dữ liệu dạng lưới, chẳng hạn như hình ảnh và mạng nơ-ron hồi quy sẵn sàng cho dữ liệu tuần tự,

Mạng thần kinh đồ thị tổng quát hơn ở chỗ chúng có thể xử lý bất kỳ dữ liệu nào có thể được biểu diễn dưới dạng biểu đồ.

Mạng nơ-ron đồ thị đã mở ra một loạt khả năng mới cho học máy và chúng là một lĩnh vực nghiên cứu tích cực, hình 10.2.

Hình 10.1, một đồ thị đơn giản. Đồ thị bao gồm các nút, các vòng tròn được gắn nhãn số và các cạnh, các đường, giữa các nút biểu thị mối quan hệ giữa các nút.

Một số dữ liệu được biểu diễn tự nhiên bằng loại cấu trúc biểu đồ này và kiến ​​trúc mạng thần kinh truyền thống không thể xử lý loại dữ liệu này.

Mặt khác, mạng thần kinh đồ thị, GNN, có thể hoạt động trực tiếp trên dữ liệu có cấu trúc đồ thị.

Hình 10.2, mạng nơ-ron đồ thị có thể hoạt động trực tiếp trên đồ thị, tính toán trên các nút và cạnh và trả về một đồ thị được cập nhật.

Trong ví dụ này, mạng nơ-ron đồ thị quyết định loại bỏ cạnh nối hai nút dưới cùng.

Đây là một ví dụ trừu tượng, nhưng các nút có thể biểu thị các biến trong thế giới thực và các mũi tên biểu thị hướng nhân quả, do đó thuật toán sẽ học cách suy ra đường dẫn nhân quả giữa các biến.

Các mô hình tự chú ý, SAM, có thể được sử dụng để xây dựng mạng lưới thần kinh đồ thị, nhưng mục tiêu của chúng tôi không phải là hoạt động trên dữ liệu có cấu trúc đồ thị rõ ràng.

Thay vào đó, chúng tôi sẽ làm việc với dữ liệu hình ảnh như bình thường nhưng chúng tôi sẽ sử dụng mô hình tự chú ý để tìm hiểu cách biểu thị bằng biểu đồ các đặc điểm trong hình ảnh.

Theo một nghĩa nào đó, chúng tôi hy vọng SAM sẽ chuyển đổi hình ảnh thô thành cấu trúc biểu đồ và cấu trúc biểu đồ mà nó xây dựng sẽ có thể hiểu được phần nào.

Ví dụ: nếu chúng ta huấn luyện SAM trên một loạt hình ảnh những người đang chơi bóng rổ, chúng ta có thể hy vọng nó học cách liên kết mọi người với quả bóng và quả bóng với rổ.

Nghĩa là, chúng tôi muốn biết rằng quả bóng là một nút, rổ là một nút và các cầu thủ là các nút và tìm hiểu các cạnh thích hợp giữa các nút.

Việc biểu diễn như vậy sẽ giúp chúng ta hiểu rõ hơn về cơ chế của mô hình học máy so với mạng nơ ron tích chập thông thường hoặc tương tự.

Các kiến ​​trúc mạng thần kinh khác nhau như tích chập, hồi quy hoặc chú ý có các thành kiến ​​quy nạp khác nhau có thể cải thiện việc học khi những thành kiến ​​đó chính xác.

Lý luận quy nạp là khi bạn quan sát một số dữ liệu và suy ra một mẫu hoặc quy tắc tổng quát hơn từ nó.

Lập luận suy diễn là những gì chúng ta làm trong toán học khi bắt đầu với một số tiền đề và bằng cách tuân theo các quy tắc logic được cho là đúng, chúng ta có thể đưa ra kết luận một cách chắc chắn.

Ví dụ, tam đoạn luận, tất cả các hành tinh xung quanh, Trái đất là một hành tinh, do đó Trái đất tròn như một dạng suy luận suy diễn.

Không có gì không chắc chắn về kết luận nếu chúng ta giả định các tiền đề là đúng.

Mặt khác, lý luận quy nạp chỉ có thể dẫn đến kết luận xác suất.

Lập luận quy nạp là điều bạn làm khi chơi một trò chơi như cờ vua.

Bạn không thể suy đoán người chơi khác sẽ làm gì. Bạn phải dựa vào những bằng chứng sẵn có và đưa ra suy luận.

Về cơ bản, Bosis là những mong đợi của bạn trước khi bạn nhìn thấy bất kỳ dữ liệu nào.

Nếu bạn luôn mong đợi đối thủ cờ vua của mình, bất kể đó là ai, sẽ thực hiện một nước đi mở đầu cụ thể, thì đó sẽ là một sự thiên vị mạnh mẽ, quy nạp.

Sự thiên vị thường được nói đến theo nghĩa miệt thị, nhưng trong học máy, những thành kiến ​​về kiến ​​trúc là điều cần thiết.

Chính xu hướng quy nạp của tính thành phần, tức là dữ liệu phức tạp có thể được phân tách thành các thành phần ngày càng đơn giản hơn theo kiểu phân cấp khiến cho việc học sâu trở nên mạnh mẽ ngay từ đầu.

Nếu chúng ta biết dữ liệu là hình ảnh có cấu trúc dạng lưới, chúng ta có thể làm cho các mô hình của mình thiên về việc tìm hiểu các tính năng cục bộ giống như mạng nơ ron tích chập đã làm.

Nếu chúng ta biết dữ liệu của mình là quan hệ, thì mạng nơ-ron có khuynh hướng quy nạp quan hệ sẽ cải thiện hiệu suất.

Mục 10.1.1, Tính không chắc chắn và tính tương đương.

Bosis là kiến ​​thức chúng ta có trước về cấu trúc dữ liệu mà chúng ta muốn tìm hiểu và chúng giúp việc học nhanh hơn nhiều.

Nhưng có nhiều điều hơn là chỉ có những thành kiến.

Với mạng nơ-ron tích chập, CNN, xu hướng thiên về việc tìm hiểu các đặc điểm cục bộ, nhưng CNN cũng có đặc tính bất biến dịch thuật.

Một hàm được cho là bất biến đối với một phép biến đổi cụ thể của đầu vào của nó, khi phép biến đổi đó không làm thay đổi đầu ra.

Ví dụ: hàm cộng không thay đổi theo thứ tự đầu vào của nó. Phép cộng của x và y bằng phép cộng của y và x, trong khi toán tử trừ không có tính bất biến thứ tự này.

Tính chất bất biến đặc biệt này có tên đặc biệt là tính giao hoán.

Nói chung, hàm f của x là bất biến đối với một số phép biến đổi, g của x, với đầu vào của nó, x, khi f của g của x bằng f của x.

CNN là các chức năng trong đó việc dịch, di chuyển lên, xuống, sang trái hoặc sang phải của một đối tượng trong ảnh sẽ không ảnh hưởng đến hoạt động của bộ phân loại CNN.

Nó bất biến đối với phép tịnh tiến, bảng trên cùng của hình 10.3.

Hình 10.3. Bất biến. Bất biến quay là một thuộc tính của hàm sao cho phép biến đổi xoay của đầu vào không làm thay đổi đầu ra của hàm.

Phương sai tương đương. Sự tương đương tịnh tiến cho một hàm là khi áp dụng bản dịch cho kết quả đầu vào cho cùng một đầu ra, giống như khi bạn áp dụng bản dịch sau khi hàm đã được thực hiện trên đầu vào không thay đổi.

Nếu chúng ta sử dụng CNN để phát hiện vị trí của một đối tượng trong ảnh, thì nó không còn bất biến đối với bản dịch mà là tương đương, bảng dưới cùng của hình 10.3.

Phương sai tương đương là khi f(g)x bằng g(f)x đối với một hàm biến đổi g nào đó.

Phương trình này cho biết rằng nếu chúng ta chụp một hình ảnh có khuôn mặt ở giữa, áp dụng bản dịch để khuôn mặt hiện ở góc trên cùng bên trái, sau đó chạy nó qua trình dò ​​tìm khuôn mặt CNN, thì kết quả sẽ giống như khi chúng ta vừa chạy hình ảnh ở giữa ban đầu thông qua trình dò ​​tìm khuôn mặt, sau đó dịch kết quả đầu ra sang góc trên cùng bên trái.

Sự khác biệt rất khó nhận thấy và thường bất biến và tương đương được sử dụng thay thế cho nhau vì chúng có liên quan với nhau.

Lý tưởng nhất là chúng ta muốn kiến ​​trúc mạng thần kinh của mình bất biến trước nhiều loại biến đổi mà dữ liệu đầu vào của chúng ta có thể phải chịu.

Trong trường hợp của hình ảnh, chúng ta thường muốn mô hình học máy của mình bất biến đối với các phép dịch, phép quay, biến dạng trơn tru, chẳng hạn như kéo dài hoặc nén và nhiễu.

CNN chỉ bất biến hoặc tương đương với các bản dịch, nhưng không nhất thiết phải mạnh mẽ chống lại các phép quay hoặc biến dạng trơn tru.

Để có được loại bất biến mà chúng ta mong muốn, chúng ta cần một mô hình quan hệ, một mô hình có khả năng xác định các đối tượng và liên hệ chúng với nhau.

Nếu chúng ta có hình ảnh một chiếc cốc ở trên bàn và huấn luyện CNN để xác định chiếc cốc thì nó sẽ hoạt động tốt.

Nhưng nếu chúng ta xoay hình ảnh 90 độ, nó có thể sẽ thất bại vì nó không bất biến về góc quay và dữ liệu huấn luyện của chúng ta không bao gồm các hình ảnh được xoay.

Tuy nhiên, về nguyên tắc, các mô hình quan hệ thuần túy sẽ không gặp vấn đề gì với điều này vì nó có thể học cách lập luận quan hệ.

Nó có thể biết rằng những chiếc cốc nằm trên bàn và mô tả quan hệ này không phụ thuộc vào một góc nhìn cụ thể.

Do đó, các mô hình học máy với khả năng suy luận quan hệ có thể mô hình hóa các mối quan hệ chung và mạnh mẽ giữa các đối tượng.

Các mô hình chú ý là một cách để đạt được điều này và là chủ đề của chương này.