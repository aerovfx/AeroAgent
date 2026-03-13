# Chương 3. Xem lại Học tập tăng cường sâu trong thực tế, Phiên bản video đã được dịch

---

Phần 3.5, xem xét.

Chúng ta đã đề cập đến rất nhiều điều trong chương này và một lần nữa chúng ta đã đưa vào rất nhiều kiến thức cơ bản.

khái niệm học tập tăng cường.

Chúng tôi lẽ ra có thể đưa ra một loạt các định nghĩa học thuật trước mặt bạn để bắt đầu, nhưng chúng tôi đã chống lại

bị cám dỗ và quyết định bắt tay vào viết mã càng nhanh càng tốt.

Hãy xem lại những gì chúng tôi đã hoàn thành và điền vào một số lỗ hổng về mặt thuật ngữ.

Trong chương này, chúng tôi đã đề cập đến một thuật toán RL cụ thể được gọi là QLearning.

QLearning không liên quan gì đến việc học sâu hoặc mạng lưới thần kinh.

Nó là một cấu trúc toán học trừu tượng.

QLearning đề cập đến việc giải quyết một nhiệm vụ điều khiển bằng cách học một hàm gọi là hàm Q.

Bạn cung cấp cho hàm Q một trạng thái, ví dụ như trạng thái trò chơi và nó dự đoán giá trị của nó

tất cả các hành động có thể xảy ra mà bạn có thể thực hiện dựa trên trạng thái đầu vào và chúng tôi gọi những hành động này là

giá trị dự đoán giá trị Q.

Bạn quyết định phải làm gì với những giá trị Q này.

Bạn có thể quyết định thực hiện hành động tương ứng với giá trị Q cao nhất, một hành động tham lam.

hoặc bạn có thể chọn một quy trình lựa chọn phức tạp hơn.

Như bạn đã học ở chương 2, bạn phải cân bằng giữa việc khám phá, thử những điều mới và việc lợi dụng,

thực hiện hành động tốt nhất mà bạn biết.

Trong chương này, chúng tôi đã sử dụng cách tiếp cận tham lam tiêu chuẩn của Epsilon để lựa chọn các hành động trong đó

ban đầu chúng tôi thực hiện các hành động ngẫu nhiên để khám phá và sau đó dần dần chuyển đổi chiến lược của mình

để thực hiện những hành động có giá trị cao nhất.

Hàm Q phải được học từ dữ liệu.

Hàm Q phải học cách đưa ra dự đoán giá trị Q chính xác của các trạng thái.

Hàm Q thực sự có thể là bất kỳ thứ gì, từ cơ sở dữ liệu kém thông minh đến cơ sở dữ liệu phức tạp.

thuật toán học sâu.

Vì học sâu là loại thuật toán học tập tốt nhất mà chúng tôi có vào thời điểm hiện tại nên chúng tôi

sử dụng mạng lưới thần kinh làm chức năng Q của chúng tôi.

Điều này có nghĩa là việc học hàm Q cũng giống như huấn luyện mạng nơ-ron với

lan truyền ngược.

Một khái niệm quan trọng về học tập Q mà chúng tôi đã giữ lại cho đến bây giờ đó là nó nằm ngoài chính sách.

thuật toán trái ngược với thuật toán on-policy.

Bạn đã biết chính sách là gì từ chương trước.

Đó là chiến lược mà thuật toán sử dụng để tối đa hóa phần thưởng theo thời gian.

Nếu một người đang học cách chơi thế giới lưới, họ có thể áp dụng một chính sách đầu tiên là tìm kiếm

tất cả các con đường có thể hướng tới mục tiêu và sau đó chọn con đường ngắn nhất.

Một chính sách khác có thể là thực hiện các hành động ngẫu nhiên cho đến khi bạn đạt được mục tiêu.

Một thuật toán học tăng cường ngoài chính sách như học Q có nghĩa là việc lựa chọn chính sách

không ảnh hưởng đến khả năng học các giá trị Q chính xác.

Thật vậy, mạng Q của chúng tôi có thể tìm hiểu các giá trị Q chính xác nếu chúng tôi chọn các hành động một cách ngẫu nhiên.

Cuối cùng, nó sẽ trải qua một số trò chơi thắng và thua và suy ra các giá trị

của các trạng thái và hành động.

Tất nhiên điều này cực kỳ kém hiệu quả, nhưng chính sách này chỉ quan trọng ở mức độ nó giúp ích cho

chúng ta học với lượng dữ liệu ít nhất.

Ngược lại, thuật toán về chính sách sẽ phụ thuộc rõ ràng vào việc lựa chọn chính sách hoặc ý chí

trực tiếp nhằm mục đích tìm hiểu một chính sách từ dữ liệu.

Nói cách khác, để huấn luyện DQN, chúng ta cần thu thập dữ liệu, kinh nghiệm từ

môi trường và chúng tôi có thể thực hiện việc này bằng bất kỳ chính sách nào, vì vậy DQN nằm ngoài chính sách.

Ngược lại, thuật toán on-policy học một chính sách đồng thời sử dụng cùng một chính sách

có chính sách thu thập kinh nghiệm để đào tạo bản thân.

Một khái niệm quan trọng khác mà chúng tôi đã lưu giữ cho đến bây giờ là khái niệm dựa trên mô hình và không có mô hình

thuật toán.

Để hiểu được điều này, trước tiên chúng ta cần hiểu mô hình là gì.

Chúng tôi sử dụng thuật ngữ này một cách không chính thức để chỉ mạng lưới thần kinh và nó thường được dùng để chỉ

cho bất kỳ loại mô hình thống kê nào, những loại khác là mô hình tuyến tính hoặc mô hình đồ họa Bayes.

Trong một bối cảnh khác, chúng ta có thể nói một mô hình là một biểu diễn tinh thần hoặc toán học của

cách một cái gì đó hoạt động trong thế giới thực.

Nếu chúng ta hiểu chính xác cách thức hoạt động của một thứ gì đó thì đó là những gì nó được cấu tạo và cách thức hoạt động của chúng.

các thành phần tương tác với nhau, khi đó chúng ta không chỉ có thể giải thích dữ liệu chúng ta đã thấy mà còn có thể dự đoán

dữ liệu chúng tôi chưa thấy.

Ví dụ, liệu các nhà dự báo có xây dựng được những mô hình khí hậu rất tinh vi

tính đến nhiều biến số liên quan và chúng liên tục đo lường dữ liệu thế giới thực.

Họ có thể sử dụng mô hình của mình để dự đoán thời tiết ở một mức độ chính xác nào đó.

Có một câu thần chú thống kê gần như sáo rỗng rằng, tất cả các mô hình đều sai, nhưng một số thì hữu ích,

nghĩa là không thể xây dựng được mô hình giống 100% với thực tế.

Sẽ luôn có dữ liệu hoặc mối quan hệ mà chúng ta đang thiếu.

Tuy nhiên, nhiều mô hình nắm bắt đủ sự thật về một hệ thống mà chúng ta quan tâm

chúng hữu ích cho việc giải thích và dự đoán.

Nếu chúng ta có thể xây dựng một thuật toán có thể tìm ra cách thế giới lưới hoạt động, thì nó sẽ có

đã suy ra một mô hình thế giới lưới và nó có thể chơi nó một cách hoàn hảo.

Trong Q-learning, tất cả những gì chúng tôi cung cấp cho mạng Q là một tensor gọn gàng.

Nó không có mô hình tiên nghiệm về thế giới lưới, nhưng nó vẫn học cách chơi bằng cách thử và sai.

Chúng tôi không giao nhiệm vụ cho mạng Q là tìm hiểu cách hoạt động của thế giới lưới.

Công việc duy nhất của nó là dự đoán phần thưởng mong đợi.

Do đó, Q-learning là một thuật toán không có mô hình.

Với tư cách là kiến trúc sư của các thuật toán, chúng ta có thể thiết kế một số thuật toán của riêng mình

kiến thức miền về một vấn đề như một mô hình để tối ưu hóa vấn đề của chúng ta.

Sau đó, chúng tôi có thể cung cấp mô hình này cho thuật toán học tập và để nó tìm hiểu chi tiết.

Đây sẽ là một thuật toán dựa trên mô hình.

Ví dụ: hầu hết các thuật toán chơi cờ đều dựa trên mô hình.

Họ biết các quy tắc về cách thức hoạt động của cờ vua và kết quả của việc thực hiện một số nước đi nhất định sẽ như thế nào.

được.

Phần duy nhất chưa được biết và chúng tôi muốn thuật toán tìm ra là gì

chuỗi các bước di chuyển sẽ giành chiến thắng trong trò chơi.

Với một mô hình trong tay, thuật toán có thể lập kế hoạch dài hạn để đạt được mục tiêu

giống nhau.

Trong nhiều trường hợp, chúng tôi muốn sử dụng các thuật toán có thể phát triển từ không có mô hình sang

lập kế hoạch bằng mô hình.

Ví dụ: một robot đang học cách đi có thể bắt đầu học bằng cách thử và sai, không cần mô hình.

Nhưng một khi nó đã hiểu được những điều cơ bản của việc đi bộ, nó có thể bắt đầu suy ra mô hình về môi trường của nó.

rồi lập kế hoạch cho một chuỗi các bước để đi từ điểm A đến điểm B, dựa trên mô hình.

Chúng ta sẽ tiếp tục khám phá các thuật toán chính sách, phi chính sách, dựa trên mô hình và không có mô hình trong

phần còn lại của cuốn sách.

Trong chương tiếp theo, chúng ta sẽ xem xét một thuật toán giúp chúng ta xây dựng một mạng có thể xấp xỉ

chức năng chính sách