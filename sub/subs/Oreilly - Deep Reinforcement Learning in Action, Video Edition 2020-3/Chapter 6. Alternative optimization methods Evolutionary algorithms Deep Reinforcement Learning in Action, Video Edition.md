# Chương 6. Các phương pháp tối ưu hóa thay thế Thuật toán tiến hóa Học tăng cường sâu trong thực tế, Phiên bản video đã được dịch

---

Chương 6.

Phương pháp tối ưu hóa thay thế.

Thuật toán tiến hóa.

Chương này đề cập đến các thuật toán tiến hóa để giải quyết các vấn đề tối ưu hóa.

Ưu và nhược điểm của phương pháp tiến hóa so với các thuật toán trước đó.

Giải quyết trò chơi kéo xe mà không cần truyền ngược.

Tại sao các chiến lược tiến hóa có thể mở rộng quy mô tốt hơn các thuật toán khác?

Mạng lưới môi trường được lấy cảm hứng lỏng lẻo từ bộ não sinh học thực sự và cấu trúc phức tạp

mạng lưới thần kinh cũng được lấy cảm hứng từ cơ chế sinh học của thị giác.

Có truyền thống lâu đời về những tiến bộ trong công nghệ và kỹ thuật được thúc đẩy bởi sinh học

sinh vật.

Thiên nhiên qua quá trình tiến hóa bằng chọn lọc tự nhiên đã giải quyết được nhiều vấn đề

một cách trang nhã và hiệu quả.

Đương nhiên, người ta thắc mắc liệu bản thân sự tiến hóa có thể được vay mượn và thực hiện hay không?

trên máy tính để tạo ra giải pháp cho các vấn đề.

Như bạn sẽ thấy, chúng ta thực sự có thể khai thác sự tiến hóa để giải quyết vấn đề và nó có tác dụng đáng kinh ngạc.

tốt và tương đối dễ thực hiện.

Trong quá trình tiến hóa tự nhiên, các đặc điểm sinh học thay đổi và các đặc điểm mới được tạo ra đơn giản bởi

thực tế là một số đặc điểm mang lại lợi thế sinh tồn và sinh sản dẫn đến những đặc điểm đó

sinh vật có thể tạo ra nhiều bản sao gen của chúng hơn ở thế hệ tiếp theo.

Lợi thế tồn tại của gen phụ thuộc hoàn toàn vào môi trường, điều này thường không thể đoán trước được.

và năng động.

Các trường hợp sử dụng mô phỏng tiến hóa của chúng tôi đơn giản hơn nhiều vì chúng tôi thường muốn tối đa hóa

hoặc giảm thiểu một số duy nhất, chẳng hạn như tổn thất khi đào tạo mạng lưới thần kinh.

Trong chương này, bạn sẽ học cách sử dụng các thuật toán tiến hóa mô phỏng để huấn luyện các nơ-ron thần kinh.

mạng để sử dụng trong học tăng cường mà không sử dụng lan truyền ngược và giảm độ dốc.

Phần 6.1, một cách tiếp cận khác để học tăng cường.

Tại sao chúng ta lại nghĩ đến việc từ bỏ việc truyền ngược?

Chà, với cả cách tiếp cận DQN và độ dốc chính sách, chúng tôi đã tạo ra một tác nhân có chính sách phụ thuộc vào

trên mạng nơ-ron để tính gần đúng hàm Q hoặc hàm chính sách.

Như được hiển thị trong Hình 6.1, tác nhân tương tác với môi trường, thu thập kinh nghiệm,

và sau đó sử dụng phương pháp lan truyền ngược để cải thiện độ chính xác của mạng lưới thần kinh của nó, và do đó,

chính sách của nó.

Chúng tôi cần điều chỉnh cẩn thận một số siêu tham số, từ việc chọn chức năng tối ưu hóa phù hợp,

quy mô lô nhỏ và tốc độ học tập để quá trình đào tạo diễn ra ổn định và thành công.

Nếu việc đào tạo cả thuật toán DQN và độ dốc chính sách đều dựa vào độ dốc ngẫu nhiên

đi xuống, đúng như tên gọi, phụ thuộc vào độ dốc nhiễu, không có gì đảm bảo rằng

những mô hình này sẽ học thành công, nghĩa là hội tụ ở mức tối ưu cục bộ hoặc toàn cục tốt.

Hình 6.1, đối với các thuật toán trước đây mà chúng tôi đã đề cập, tác nhân của chúng tôi đã tương tác với môi trường,

tích lũy kinh nghiệm rồi rút kinh nghiệm từ những kinh nghiệm đó.

Chúng tôi lặp đi lặp lại quá trình tương tự cho mỗi sử thi cho đến khi tác nhân ngừng học hỏi.

Tùy thuộc vào môi trường và độ phức tạp của mạng, việc tạo một tác nhân có quyền

siêu tham số có thể cực kỳ khó khăn.

Hơn nữa, để sử dụng phương pháp giảm gradient và lan truyền ngược, chúng ta cần một mô hình

có thể phân biệt được.

Chắc chắn có những mô hình thú vị và hữu ích mà bạn có thể xây dựng nhưng không thể thực hiện được

để huấn luyện với độ dốc giảm dần do thiếu khả năng phân biệt.

Thay vì tạo ra một tác nhân và cải tiến nó, chúng ta có thể học hỏi từ Charles Darwin

và sử dụng sự tiến hóa bằng chọn lọc phi tự nhiên.

Chúng ta có thể sinh ra nhiều tác nhân khác nhau với các thông số, trọng lượng khác nhau, quan sát xem tác nhân nào

những người đã làm điều tốt nhất và tạo ra những tác nhân tốt nhất để con cháu có thể kế thừa

những đặc điểm mong muốn của cha mẹ, giống như trong chọn lọc tự nhiên.

Chúng ta có thể mô phỏng quá trình tiến hóa sinh học bằng thuật toán.

Chúng ta sẽ không cần phải vất vả điều chỉnh các siêu tham số và trọng số từ nhiều kỷ nguyên để xem liệu

đại lý đang học chính xác.

Chúng tôi chỉ có thể chọn các đại lý đã hoạt động tốt hơn.

Hình 6.2

Hình 6.2, các thuật toán tiến hóa khác với các kỹ thuật tối ưu hóa dựa trên độ dốc giảm dần.

Với các chiến lược tiến hóa, chúng tôi tạo ra các tác nhân và chuyển các trọng số có lợi nhất xuống

cho các đại lý tiếp theo.

Lớp thuật toán này không yêu cầu một tác nhân riêng lẻ học.

Nó không dựa vào việc giảm độ dốc và được gọi một cách khéo léo là thuật toán không có độ dốc.

Nhưng chỉ vì các tác nhân riêng lẻ không bị thúc đẩy trực tiếp tới một mục tiêu nào đó,

không có nghĩa là chúng ta đang dựa vào cơ hội thuần túy.

Nhà sinh vật học tiến hóa nổi tiếng Richard Dawkins từng nói,

chọn lọc tự nhiên không hề là ngẫu nhiên.

Tương tự, trong nỗ lực xây dựng hoặc chính xác hơn là khám phá đại lý tốt nhất, chúng tôi sẽ không

đang dựa vào cơ hội thuần túy.

Chúng tôi sẽ lựa chọn những người khỏe mạnh nhất trong một quần thể có sự khác biệt về đặc điểm.