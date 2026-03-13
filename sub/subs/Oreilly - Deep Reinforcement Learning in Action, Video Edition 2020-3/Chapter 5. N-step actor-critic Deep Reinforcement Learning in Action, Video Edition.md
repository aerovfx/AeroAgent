# Chương 5. Học tập tăng cường sâu trong hành động của diễn viên-nhà phê bình N-step, Phiên bản video đã dịch

---

Phần 5.4, Phê bình diễn viên N-Step

Trong phần trước, chúng ta đã triển khai bộ phê bình diễn viên lợi thế phân tán, ngoại trừ việc chúng ta đã huấn luyện

ở chế độ Monte Carlo.

Chúng tôi đã chạy một tập đầy đủ trước khi cập nhật các thông số mô hình.

Mặc dù điều đó có ý nghĩa đối với một trò chơi đơn giản như Cartpole, nhưng thông thường chúng tôi muốn có thể thực hiện

cập nhật thường xuyên hơn.

Trước đây chúng ta đã đề cập sơ qua về việc học N-Step, nhưng để nhắc lại, điều đó có nghĩa là chúng ta chỉ đơn giản tính toán

sự mất mát của chúng tôi và cập nhật các tham số sau N-Bước, trong đó N là bất cứ thứ gì chúng tôi chọn.

Nếu N bằng 1 thì đây hoàn toàn là học trực tuyến.

Nếu N rất lớn thì đó sẽ lại là Monte Carlo.

Điểm ngọt ngào nằm ở đâu đó ở giữa.

Với việc học tập đầy đủ của Monte Carlo, chúng tôi không tận dụng được khả năng khởi động vì có

không có gì để khởi động.

Chúng tôi thực hiện bootstrap trong học tập trực tuyến, như chúng tôi đã làm với DQN, nhưng với một bước học, bootstrap

có thể đưa ra nhiều thành kiến.

Sự thiên vị này có thể vô hại nếu nó đẩy các tham số của chúng ta đi đúng hướng, nhưng trong một số trường hợp

trường hợp sự thiên vị có thể quá lệch lạc đến mức chúng ta không bao giờ đi đúng hướng.

Đây là lý do tại sao học N-Step thường tốt hơn học một bước trực tuyến.

Giá trị mục tiêu cho nhà phê bình chính xác hơn nên việc đào tạo nhà phê bình sẽ ổn định hơn,

và sẽ có thể tạo ra các giá trị trạng thái ít sai lệch hơn.

Với bootstrapping, chúng ta đang đưa ra dự đoán từ một dự đoán, vì vậy các dự đoán đó sẽ

sẽ tốt hơn nếu bạn có thể thu thập thêm dữ liệu trước khi tạo chúng.

Và chúng tôi thích khởi động vì nó cải thiện hiệu quả lấy mẫu.

Bạn không cần phải xem nhiều dữ liệu, chẳng hạn như các khung hình trong trò chơi, trước khi cập nhật các thông số

đi đúng hướng.

Hãy sửa đổi mã của chúng tôi để thực hiện học tập N-Step.

Chức năng duy nhất chúng ta cần sửa đổi là chạy tập gạch dưới.

Chúng ta cần thay đổi nó để chỉ chạy trong N-Step thay vì đợi tập phim kết thúc.

Nếu tập kết thúc trước N-Steps, giá trị trả về cuối cùng sẽ được đặt thành 0, vì

không có trạng thái tiếp theo khi trò chơi kết thúc, như trong trường hợp Monte Carlo.

Tuy nhiên, nếu tập chưa kết thúc sau N-Steps, chúng tôi sẽ sử dụng giá trị trạng thái cuối cùng

như dự đoán của chúng tôi về kết quả sẽ như thế nào nếu chúng tôi tiếp tục chơi.

Đó là nơi quá trình khởi động diễn ra.

Nếu không khởi động, nhà phê bình chỉ đang cố gắng dự đoán lợi nhuận trong tương lai từ một trạng thái,

và nó nhận được kết quả thực tế dưới dạng dữ liệu huấn luyện.

Với bootstrapping, nó vẫn đang cố gắng dự đoán lợi nhuận trong tương lai, nhưng nó đang làm như vậy trong

một phần bằng cách sử dụng dự đoán của chính nó về lợi nhuận trong tương lai, vì dữ liệu huấn luyện sẽ bao gồm

dự đoán của riêng mình.

Liệt kê 5.9, Huấn luyện N-Step với thao tác kéo xe.

Điều duy nhất chúng tôi đã thay đổi là các điều kiện cho vòng lặp while, thoát bằng N-Steps và chúng tôi đã

đặt giá trị trả về là giá trị trạng thái của bước cuối cùng, nếu tập phim chưa kết thúc, do đó

cho phép khởi động.

Hàm Run gạch dưới tập mới này trả về G một cách rõ ràng, vì vậy để có được điều này

để hoạt động, chúng tôi cần thực hiện một số cập nhật nhỏ cho bản cập nhật, gạch dưới hàm Params

và chức năng của người lao động.

Đầu tiên, thêm tham số G vào định nghĩa của hàm Params gạch dưới cập nhật,

và thay đổi dấu gạch dưới ret bằng G.

Xem mã này.

Phần còn lại của hàm hoàn toàn giống nhau và bị bỏ qua ở đây.

Tất cả những gì chúng ta cần thay đổi trong hàm worker là nắm bắt mảng G mới được trả về và

chuyển nó để cập nhật thông số gạch dưới.

Xem mã này.

Bạn có thể chạy lại thuật toán huấn luyện như trước và mọi thứ sẽ hoạt động như cũ, ngoại trừ

với hiệu suất tốt hơn.

Bạn có thể ngạc nhiên về mức độ hiệu quả của việc học N-Step.

Hình 5.15 cho thấy sơ đồ độ dài của tập trong 45 giây đào tạo đầu tiên cho phần này

mô hình.

Hình 5.15, biểu đồ thực hiện dành cho nhà phê bình diễn viên lợi thế phân tán với khả năng khởi động N-Step thực sự.

So với thuật toán Monte Carlo trước đây của chúng tôi, hiệu suất mượt mà hơn nhiều do

nhà phê bình ổn định hơn.

Lưu ý trong Hình 5.15 rằng mô hình N-Step bắt đầu trở nên tốt hơn ngay lập tức và đạt đến

thời lượng tập 300 chỉ sau 45 giây so với chỉ khoảng 140 của Monte Carlo

phiên bản.

Cũng lưu ý rằng cốt truyện này mượt mà hơn nhiều so với cốt truyện Monte Carlo.

Bootstrapping làm giảm sự khác biệt trong nhà phê bình và cho phép nó học nhanh hơn nhiều

hơn Monte Carlo.

Một ví dụ cụ thể, hãy tưởng tượng trường hợp bạn nhận được phần thưởng ba bước là một, một

trừ một cho tập một, rồi một, một, một cho tập hai.

Lợi nhuận tổng thể cho tập một là 0,01, với gamma bằng 0,99 và 1,99 cho tập

hai.

Đó là hai bậc chênh lệch độ lớn chỉ dựa trên kết quả ngẫu nhiên của

tập phim sớm trong quá trình đào tạo.

Đó là rất nhiều sự khác biệt.

So sánh điều đó với trường hợp tương tự ngoại trừ với, mô phỏng, bootstrapping, để kết quả trả về

đối với mỗi tập đó cũng bao gồm lợi nhuận dự đoán đã được khởi động.

Với dự đoán lợi nhuận khởi động là 1,0 cho cả hai, giả sử các trạng thái tương tự nhau,

lợi nhuận được tính toán là 0,99 và 2,97, gần hơn nhiều so với khi không khởi động.

Bạn có thể tạo lại ví dụ này bằng đoạn mã sau.

Liệt kê 5.10 trả về có và không có bootstrapping.

Tóm lại, trong phương pháp gradient chính sách đơn giản của chương trước, chúng ta chỉ đào tạo một

hàm chính sách sẽ đưa ra phân phối xác suất cho tất cả các hành động, sao cho

hành động tốt nhất được dự đoán sẽ có xác suất cao nhất.

Không giống như học Q trong đó học giá trị mục tiêu, chức năng chính sách được củng cố trực tiếp

để tăng hoặc giảm xác suất thực hiện hành động tùy thuộc vào phần thưởng.

Trong cùng một hành động, có thể tạo ra kết quả trái ngược nhau về mặt khen thưởng, gây ra sự khác biệt lớn

trong quá trình đào tạo.

Để giảm thiểu điều này, chúng tôi đã giới thiệu một mô hình phê phán hoặc trong chương này chúng tôi đã sử dụng một mô hình hai đầu duy nhất.

mô hình, giúp giảm sự khác biệt của các cập nhật chức năng chính sách bằng cách lập mô hình trực tiếp

giá trị trạng thái.

Bằng cách này, nếu người thực hiện chính sách thực hiện hành động và nhận được phần thưởng lớn hay nhỏ bất thường,

nhà phê bình có thể tiết chế sự dao động lớn này và ngăn chặn một cú dao động lớn bất thường và có thể mang tính hủy diệt,

cập nhật tham số cho chính sách.

Điều này cũng dẫn đến khái niệm về lợi thế, thay vì đào tạo chính sách dựa trên

dựa trên lợi nhuận thô, phần thưởng tích lũy trung bình, chúng tôi đào tạo dựa trên mức độ tốt hơn hay tệ hơn,

hành động được so sánh với những gì nhà phê bình dự đoán.

Điều này rất hữu ích vì nếu cả hai hành động đều dẫn đến cùng một phần thưởng tích cực, chúng ta sẽ

ngây thơ giả định những hành động tương đương của chúng, nhưng nếu chúng ta so sánh với những gì chúng ta mong đợi sẽ xảy ra,

và một phần thưởng được thực hiện tốt hơn nhiều so với dự kiến, thì hành động đó cần được củng cố nhiều hơn.

Giống như các phương pháp học sâu còn lại, chúng ta thường phải sử dụng các lô dữ liệu để

để rèn luyện một cách hiệu quả.

Việc đào tạo với một ví dụ về thời gian sẽ tạo ra quá nhiều tiếng ồn và việc đào tạo có thể sẽ

không bao giờ hội tụ.

Để giới thiệu đào tạo hàng loạt với Q-learning, chúng tôi đã sử dụng kinh nghiệm đào tạo

có thể chọn ngẫu nhiên các đợt trải nghiệm trước đó.

Chúng ta có thể sử dụng tính năng phát lại trải nghiệm với nhà phê bình diễn viên, nhưng việc sử dụng tính năng phát lại trải nghiệm được phân bổ phổ biến hơn.

đào tạo với nhà phê bình diễn viên và rõ ràng là Q-learning cũng có thể được phân phối.

Việc đào tạo phân tán trong các mô hình phê bình diễn viên phổ biến hơn vì chúng ta thường muốn sử dụng

một mạng lưới thần kinh tái diễn, RNN, lớp, như một phần của mô hình học tăng cường của chúng tôi, trong

trường hợp việc theo dõi các trạng thái trước đó là cần thiết hoặc hữu ích để đạt được mục tiêu.

Nhưng RNN cần một chuỗi các ví dụ có liên quan về mặt thời gian và việc phát lại trải nghiệm phụ thuộc vào một đợt

của những trải nghiệm độc lập.

Chúng ta có thể lưu trữ toàn bộ quỹ đạo, chuỗi trải nghiệm trong bộ đệm phát lại, nhưng điều đó

chỉ làm tăng thêm sự phức tạp.

Thay vào đó, với việc đào tạo phân tán và mỗi quy trình chạy trực tuyến với môi trường riêng của nó,

các mô hình có thể dễ dàng kết hợp RNN.

Chúng tôi không đề cập đến vấn đề này ở đây nhưng có một cách khác để đào tạo thuật toán phê bình diễn viên trực tuyến

bên cạnh việc đào tạo phân tán.

Chỉ cần sử dụng nhiều bản sao môi trường của bạn và sau đó gộp các trạng thái từ mỗi bản sao lại với nhau.

môi trường độc lập, đưa nó vào một mô hình phê bình tác nhân duy nhất sau đó sẽ tạo ra

dự đoán độc lập cho từng môi trường.

Đây là một giải pháp thay thế khả thi cho việc đào tạo phân tán khi môi trường không tốn kém

để chạy.

Nếu môi trường của bạn là một trình mô phỏng chuyên sâu về máy tính và bộ nhớ cao phức tạp, thì đó là

có lẽ sẽ rất chậm khi chạy nhiều bản sao của nó trong một quy trình, vì vậy

trường hợp, cách tiếp cận phân tán là tốt hơn.

Bây giờ chúng tôi đã đề cập đến những gì chúng tôi coi là phần cơ bản nhất của việc gia cố

học tập ngày nay.

Bây giờ bạn đã cảm thấy thoải mái với khung toán học cơ bản của học tăng cường

như một quy trình quyết định Markov, MDP, và bạn sẽ có thể triển khai Q-learning, đơn giản

độ dốc chính sách và mô hình phê bình tác nhân.

Nếu bạn đã làm theo cho đến nay, bạn sẽ có một nền tảng tốt để giải quyết nhiều vấn đề khác.

lĩnh vực học tập củng cố.

Trong phần còn lại của cuốn sách, chúng tôi sẽ đề cập đến các phương pháp học tăng cường nâng cao hơn với

mục đích dạy cho bạn một số thuật toán RL tiên tiến nhất thời gian gần đây theo cách trực quan

cách.