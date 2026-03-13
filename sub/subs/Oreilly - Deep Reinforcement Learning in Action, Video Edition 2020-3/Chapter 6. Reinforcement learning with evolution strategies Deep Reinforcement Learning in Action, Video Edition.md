# Chương 6. Học tăng cường với các chiến lược tiến hóa Học tăng cường sâu trong thực tế, Phiên bản video đã dịch

---

Phần 6.2, học tăng cường với các chiến lược tiến hóa.

Trong phần này, chúng ta sẽ nói về vai trò của thể lực trong các chiến lược tiến hóa,

và chúng ta sẽ đề cập ngắn gọn đến nhiệm vụ lựa chọn những tác nhân mạnh nhất.

Tiếp theo, chúng ta sẽ tìm cách kết hợp lại các tác nhân đó thành các tác nhân mới,

và cho thấy điều gì xảy ra khi chúng ta đưa vào các đột biến.

Sự tiến hóa này là một quá trình nhiều thế hệ,

vì vậy chúng ta sẽ thảo luận về vấn đề đó và tóm tắt lại toàn bộ vòng đào tạo.

Mục 6.2.1, sự tiến hóa về mặt lý thuyết.

Nếu bạn còn nhớ lớp sinh học ở trường trung học,

chọn lọc tự nhiên chọn ra những cá thể phù hợp nhất ở mỗi thế hệ.

Trong sinh học, điều này đại diện cho những cá thể có khả năng sinh sản thành công nhất,

và do đó đã truyền lại thông tin di truyền của chúng cho các thế hệ tiếp theo.

Những con chim có hình dạng mỏ giỏi hơn trong việc lấy hạt từ cây

sẽ có nhiều thức ăn hơn và do đó có nhiều khả năng sống sót hơn để truyền gen hình mỏ đó

đến con cháu của họ.

Nhưng hãy nhớ, sự phù hợp nhất phụ thuộc vào môi trường.

Gấu Bắc cực thích nghi tốt với các chỏm băng vùng cực,

nhưng sẽ rất không phù hợp ở các khu rừng nhiệt đới Amazon.

Bạn có thể coi môi trường như việc xác định một mục tiêu hoặc chức năng thích hợp

gán cho các cá nhân điểm thể lực dựa trên hiệu suất của họ trong môi trường đó.

Hiệu suất của họ chỉ được xác định bởi thông tin di truyền của họ.

Trong sinh học, mỗi đột biến đều làm thay đổi rất tinh vi các đặc tính của cơ thể,

đến mức có thể khó phân biệt thế hệ này với thế hệ khác.

Tuy nhiên, việc cho phép những đột biến và biến thể này tích lũy qua nhiều thế hệ

cho phép những thay đổi có thể cảm nhận được.

Ví dụ, trong quá trình tiến hóa của mỏ chim,

một quần thể chim ban đầu có hình dạng mỏ gần giống nhau.

Nhưng theo thời gian, những đột biến ngẫu nhiên đã được đưa vào quần thể.

Hầu hết những đột biến này có lẽ không ảnh hưởng gì đến loài chim,

hoặc thậm chí còn có tác dụng có hại.

Nhưng với dân số đủ lớn và đủ thế hệ,

đột biến ngẫu nhiên xảy ra ảnh hưởng tốt đến hình dạng mỏ.

Những con chim có mỏ phù hợp hơn sẽ có lợi thế hơn khi kiếm được thức ăn so với những con chim khác,

và do đó họ có khả năng di truyền gen cao hơn.

Vì vậy, thế hệ tiếp theo sẽ có tần suất gen mỏ có hình dạng thuận lợi tăng lên.

Trong học tăng cường tiến hóa, chúng tôi đang lựa chọn những đặc điểm mang lại cho các tác nhân của chúng tôi

phần thưởng cao nhất trong một môi trường nhất định và theo đặc điểm, chúng tôi muốn nói đến các tham số mô hình,

ví dụ như trọng số của mạng lưới thần kinh hoặc toàn bộ cấu trúc mô hình.

Mức độ phù hợp của đặc vụ RL có thể được xác định bằng phần thưởng dự kiến mà nó sẽ nhận được

nếu nó được thực hiện trong môi trường.

Giả sử Đặc vụ A đã chơi trò chơi Atari đột phá và có thể đạt được điểm trung bình là 500,

trong khi Đặc vụ B chỉ đạt được 300 điểm.

Chúng ta có thể nói rằng Đặc vụ A phù hợp hơn Đặc vụ B,

và rằng chúng tôi muốn tác nhân tối ưu của mình giống với Tác nhân A hơn B.

Hãy nhớ rằng, lý do duy nhất khiến Đặc vụ A phù hợp hơn Đặc vụ B

là do các tham số mô hình của nó đã được tối ưu hóa hơn một chút cho phù hợp với môi trường.

Mục tiêu trong học tăng cường tiến hóa hoàn toàn giống như trong đào tạo dựa trên lan truyền ngược và giảm dần độ dốc.

Sự khác biệt duy nhất là chúng ta sử dụng quá trình tiến hóa này,

thường được gọi là thuật toán di truyền,

để tối ưu hóa các tham số của mô hình như mạng nơ-ron, Hình 6.3.

Hình 6.3. Trong cách tiếp cận thuật toán tiến hóa để học tăng cường,

các tác nhân cạnh tranh trong một môi trường và các tác nhân phù hợp hơn,

những loài tạo ra nhiều phần thưởng hơn sẽ được ưu tiên sao chép để tạo ra con cái.

Sau nhiều lần lặp lại quá trình này, chỉ còn lại những tác nhân phù hợp nhất.

Quá trình này khá đơn giản nhưng chúng ta hãy xem xét các bước của thuật toán di truyền một cách chi tiết hơn.

Giả sử chúng ta có một mạng lưới thần kinh mà chúng ta muốn sử dụng làm tác nhân để chơi thế giới lưới,

và chúng tôi muốn huấn luyện nó bằng thuật toán di truyền.

Hãy nhớ rằng, huấn luyện mạng nơ-ron chỉ có nghĩa là cập nhật lặp đi lặp lại các tham số của nó,

như vậy hiệu suất của nó được cải thiện. Cũng nhớ lại rằng với kiến trúc mạng nơ-ron cố định,

các tham số hoàn toàn xác định hành vi của nó, vì vậy để sao chép mạng nơ-ron chúng ta chỉ cần sao chép các tham số của nó.

Đây là cách chúng tôi huấn luyện một mạng lưới thần kinh như vậy bằng thuật toán di truyền,

được mô tả bằng đồ họa trong Hình 6.4.

1. Chúng tôi tạo ra một quần thể ban đầu gồm các vectơ tham số ngẫu nhiên.

Chúng tôi coi mỗi vectơ tham số trong quần thể là một cá thể.

Giả sử quần thể ban đầu này có 100 cá thể.

2. Chúng tôi duyệt qua quần thể này và đánh giá mức độ phù hợp của từng cá nhân

bằng cách chạy mô hình trong thế giới lưới với vectơ tham số đó và ghi lại phần thưởng.

Mỗi cá nhân được chỉ định một điểm thể lực dựa trên phần thưởng mà họ kiếm được.

Vì quần thể ban đầu là ngẫu nhiên nên tất cả chúng đều có khả năng hoạt động rất kém,

nhưng ngẫu nhiên sẽ có một số sẽ hoạt động tốt hơn những cái khác.

3. Chúng tôi lấy mẫu ngẫu nhiên một cặp cá thể, bố mẹ, từ quần thể,

được tính theo điểm thể lực tương đối của họ,

những cá nhân có mức độ phù hợp cao hơn sẽ có xác suất được chọn cao hơn,

để tạo ra quần thể sinh sản.

Ghi chú. Có nhiều phương pháp khác nhau để lựa chọn cha mẹ cho thế hệ tiếp theo.

Một cách đơn giản là ánh xạ xác suất lựa chọn lên mỗi cá nhân

dựa trên điểm số thể lực tương đối của họ và sau đó lấy mẫu từ phân bổ này.

Bằng cách này, cái phù hợp nhất sẽ được chọn thường xuyên nhất,

nhưng vẫn có một cơ hội nhỏ để những người có thành tích kém được chọn.

Điều này có thể giúp duy trì sự đa dạng dân số.

Một cách khác là chỉ cần xếp hạng tất cả các cá nhân và chọn ra những cá nhân hàng đầu

và sử dụng chúng để giao phối để lấp đầy thế hệ tiếp theo.

Hầu như bất kỳ phương pháp nào ưu tiên lựa chọn những cá thể có thành tích tốt nhất để giao phối sẽ có hiệu quả,

nhưng một số thì tốt hơn những cái khác.

Có sự đánh đổi giữa việc lựa chọn những người hoạt động tốt nhất và giảm sự đa dạng dân số.

Điều này rất giống với sự đánh đổi giữa khám phá và khai thác trong học tập tăng cường.

Bốn. Các cá thể trong quần thể sinh sản sẽ giao phối để sinh ra con cái

sẽ hình thành một quần thể mới đầy đủ gồm 100 cá thể.

Nếu các cá thể đơn giản là các vectơ tham số của số thực,

ghép vectơ 1 với vectơ 2 liên quan đến việc lấy một tập hợp con từ vectơ 1

và kết hợp nó với tập con bổ sung của vectơ 2

để tạo ra một vectơ con mới có cùng kích thước.

Ví dụ: giả sử bạn có vectơ 1, 1, 2, 3 và vectơ 2, 4, 5, 6.

Vector 1 kết hợp với vector 2 để tạo ra 1, 5, 6 và 4, 2, 3.

Chúng tôi chỉ đơn giản ghép đôi ngẫu nhiên các cá thể từ quần thể sinh sản

và kết hợp chúng lại để tạo ra hai con mới cho đến khi chúng ta có đủ quần thể mới.

Điều này tạo ra sự đa dạng di truyền mới với những cá thể biểu hiện tốt nhất.

5. Bây giờ chúng ta có một quần thể mới với các giải pháp hàng đầu

từ thế hệ trước, cùng với các giải pháp con cháu mới.

Tại thời điểm này, chúng tôi sẽ lặp lại các giải pháp của mình

và biến đổi ngẫu nhiên một số trong số chúng để đảm bảo chúng tôi tạo ra sự đa dạng di truyền mới

vào mọi thế hệ để ngăn chặn sự hội tụ sớm ở mức tối ưu cục bộ.

Đột biến đơn giản có nghĩa là thêm một chút nhiễu ngẫu nhiên vào các vectơ tham số.

Nếu đây là các vectơ nhị phân, đột biến có nghĩa là đảo lộn ngẫu nhiên một vài bit.

Nếu không, chúng ta có thể thêm một số nhiễu Gaussian.

Tỷ lệ đột biến cần phải khá thấp, nếu không sẽ có nguy cơ phá hỏng các giải pháp tốt hiện có.

6. Bây giờ chúng ta có một quần thể con đột biến mới từ thế hệ trước.

Chúng tôi lặp lại quá trình này với quần thể mới trong N thế hệ,

hoặc cho đến khi chúng ta đạt đến sự hội tụ, đó là khi mức độ thích nghi của dân số trung bình đã ngừng cải thiện đáng kể.

6. Tối ưu hóa thuật toán di truyền của mạng lưới thần kinh để học tăng cường.

Một tập hợp các mạng lưới thần kinh ban đầu, các tác nhân RL, được thử nghiệm trong môi trường và kiếm được phần thưởng.

Mỗi đại lý riêng lẻ được gắn nhãn theo mức độ phù hợp của nó, dựa trên phần thưởng kiếm được.

Các cá nhân được lựa chọn cho thế hệ tiếp theo dựa trên thể lực của họ.

Những cá nhân khỏe mạnh hơn có nhiều khả năng được đưa vào thế hệ tiếp theo.

Các cá thể được chọn giao phối và bị đột biến để tăng tính đa dạng di truyền.

6. 2.2 Sự tiến hóa trong thực tế.

Trước khi chúng ta đi sâu vào ứng dụng học tăng cường,

chúng ta sẽ chạy một thuật toán di truyền siêu đơn giản cho một bài toán mẫu nhằm mục đích minh họa.

Chúng tôi sẽ tạo một tập hợp các chuỗi ngẫu nhiên và cố gắng phát triển chúng theo chuỗi mục tiêu mà chúng tôi đã chọn, chẳng hạn như Hello World.

Quần thể chuỗi ngẫu nhiên ban đầu của chúng tôi sẽ trông như thế nào,

gm i gs k y b x z y p, và a d l b o m x i r b h.

Chúng ta sẽ sử dụng một hàm có thể cho chúng ta biết các chuỗi này giống với chuỗi mục tiêu như thế nào để cung cấp cho chúng ta điểm số phù hợp.

Sau đó, chúng tôi sẽ lấy mẫu các cặp bố mẹ từ quần thể được đánh giá theo điểm số thể lực tương đối của họ,

sao cho những cá nhân có điểm thể lực cao hơn sẽ có nhiều khả năng được chọn làm cha mẹ hơn.

Tiếp theo, chúng ta sẽ giao phối những bố mẹ này, còn được gọi là lai hoặc kết hợp,

để tạo ra hai chuỗi con và thêm chúng vào thế hệ tiếp theo.

Chúng ta cũng sẽ biến đổi thế hệ con bằng cách đảo ngẫu nhiên một vài ký tự trong chuỗi.

Chúng tôi sẽ lặp lại quá trình này và kỳ vọng rằng dân số sẽ trở nên giàu có nhờ các chuỗi rất gần với mục tiêu của chúng tôi.

Có lẽ ít nhất một chiếc sẽ bắn trúng mục tiêu của chúng tôi một cách chính xác, lúc đó chúng tôi sẽ dừng thuật toán.

Quá trình tiến hóa này của dây được mô tả trong Hình 6.5.

Hình 6.5, sơ đồ chuỗi phác thảo các bước chính trong thuật toán di truyền để phát triển một tập hợp các chuỗi ngẫu nhiên hướng tới chuỗi mục tiêu.

Chúng tôi bắt đầu với một tập hợp các chuỗi ngẫu nhiên, so sánh từng chuỗi với chuỗi mục tiêu,

và chỉ định điểm phù hợp cho từng chuỗi dựa trên mức độ tương tự của nó với chuỗi mục tiêu.

Sau đó, chúng tôi chọn những bố mẹ có năng lực cao để giao phối hoặc kết hợp lại để sinh ra con cái,

và sau đó chúng tôi biến đổi bọn trẻ để tạo ra những biến thể di truyền mới.

Chúng ta lặp lại quá trình chọn bố mẹ và sinh con cho đến khi đủ thế hệ tiếp theo,

khi nó có cùng kích thước với quần thể ban đầu.

Đây có lẽ là một ví dụ ngớ ngẩn, nhưng nó là một trong những minh chứng đơn giản nhất về thuật toán di truyền,

và các khái niệm sẽ trực tiếp chuyển sang nhiệm vụ học tập củng cố của chúng ta.

Liệt kê 6.1 đến 6.4 hiển thị mã.

Trong Liệt kê 6.1, chúng ta bắt đầu bằng cách thiết lập các hàm sẽ khởi tạo tập hợp ban đầu của các chuỗi ngẫu nhiên,

và cũng xác định một hàm có thể tính điểm tương tự giữa hai chuỗi,

mà cuối cùng chúng ta sẽ sử dụng làm hàm thích nghi của mình.

Liệt kê 6.1, phát triển các chuỗi, thiết lập các chuỗi ngẫu nhiên.

Đoạn mã trước tạo ra một quần thể ban đầu gồm các cá thể,

là các đối tượng lớp bao gồm trường chuỗi và trường điểm thể lực.

Sau đó, nó tạo ra các chuỗi ngẫu nhiên bằng cách lấy mẫu từ danh sách các ký tự chữ cái.

Khi đã có dân số, chúng ta cần đánh giá mức độ phù hợp của từng cá thể.

Đối với chuỗi, chúng ta có thể tính toán số liệu tương tự bằng cách sử dụng mô-đun Python tích hợp được gọi là trình so khớp chuỗi.

Trong Liệt kê 6.2, chúng ta định nghĩa hai hàm, kết hợp lại và biến đổi.

Đúng như tên gọi của chúng, cái trước sẽ lấy hai chuỗi và kết hợp lại chúng để tạo ra hai chuỗi mới,

và cái sau sẽ ngẫu nhiên lật các ký tự trong một chuỗi để thay đổi chúng.

Liệt kê 6.2, phát triển các chuỗi, kết hợp lại và biến đổi.

Hàm tái hợp trước đó có hai chuỗi cha như sau:

xin chào thế giới sương mù và kết hợp lại chúng một cách ngẫu nhiên bằng cách tạo ra một số nguyên ngẫu nhiên có chiều dài bằng chuỗi,

và lấy phần đầu tiên của bố mẹ 1 và phần thứ hai của bố mẹ 2 để tạo ra con cái,

chẳng hạn như sương mù ở đó và xin chào thế giới, nếu sự chia rẽ xảy ra ở giữa.

Nếu chúng ta đã phát triển một chuỗi chứa một phần những gì chúng ta muốn, như xin chào,

và một chuỗi khác chứa một phần khác của những gì chúng ta muốn như thế giới,

thì quá trình tái hợp có thể mang lại cho chúng ta tất cả những gì chúng ta mong muốn.

Quá trình đột biến cần một chuỗi giống như, chết tiệt, nhưng, và với một xác suất nhỏ nào đó, tỷ lệ đột biến,

sẽ thay thế một ký tự trong chuỗi bằng một ký tự ngẫu nhiên.

Ví dụ: nếu tỷ lệ đột biến là 20%, 0,2, thì có khả năng ít nhất một trong năm nhân vật trong địa ngục là,

sẽ bị biến đổi thành một ký tự ngẫu nhiên.

Hy vọng rằng nó sẽ được chuyển thành lời chào nếu đó là mục tiêu.

Mục đích của đột biến là đưa thông tin, biến thể mới vào quần thể.

Nếu tất cả những gì chúng ta làm là kết hợp lại, có khả năng là tất cả các cá thể trong quần thể sẽ trở nên quá giống nhau một cách nhanh chóng,

và chúng ta sẽ không tìm ra giải pháp mong muốn, vì thông tin sẽ bị mất qua mỗi thế hệ nếu không có đột biến.

Lưu ý rằng tỷ lệ đột biến là rất quan trọng.

Nếu nó quá cao, những cá thể khỏe mạnh nhất sẽ mất đi thể lực do đột biến, còn nếu nó quá thấp, chúng ta sẽ không có đủ biến thể để tìm ra cá thể tối ưu.

Thật không may, bạn phải tìm ra tỷ lệ đột biến phù hợp theo kinh nghiệm.

Trong danh sách 6.3, chúng ta định nghĩa một hàm sẽ lặp qua từng cá thể trong một quần thể chuỗi,

tính toán điểm thể lực của nó và liên kết nó với cá nhân đó.

Chúng tôi cũng xác định một chức năng sẽ tạo ra thế hệ tiếp theo.

Liệt kê 6.3, phát triển các chuỗi, đánh giá các cá thể và tạo ra thế hệ mới.

Đây là hai chức năng cuối cùng chúng ta cần để hoàn thành quá trình tiến hóa.

Chúng tôi có một chức năng đánh giá từng cá thể trong quần thể và chỉ định điểm phù hợp,

chỉ cho biết chuỗi của cá nhân đó giống với chuỗi mục tiêu như thế nào.

Điểm thể lực sẽ khác nhau tùy thuộc vào mục tiêu của một vấn đề nhất định.

Cuối cùng, chúng ta có một hàm tạo ra một quần thể mới bằng cách lấy mẫu những cá thể phù hợp nhất trong quần thể hiện tại,

kết hợp chúng để sinh ra con cái và làm chúng biến đổi.

Trong danh sách 6.4, chúng tôi đặt mọi thứ lại với nhau và lặp lại các bước trước đó với số thế hệ tối đa.

Nghĩa là, chúng tôi bắt đầu với quần thể ban đầu, trải qua quá trình chấm điểm mức độ phù hợp của các cá thể và tạo ra quần thể con mới,

rồi lặp lại trình tự này nhiều lần.

Sau đủ số thế hệ, chúng tôi hy vọng quần thể cuối cùng sẽ được làm phong phú thêm các chuỗi rất gần với chuỗi mục tiêu của chúng tôi.

Liệt kê 6.4, phát triển các chuỗi, kết hợp tất cả lại với nhau.

Nếu bạn chạy thuật toán, sẽ mất vài phút trên CPU hiện đại.

Bạn có thể tìm thấy cá thể được xếp hạng cao nhất trong quần thể như sau.

Xem mã này.

Nó đã hoạt động. Bạn cũng có thể thấy mức độ thể lực trung bình của dân số tăng dần qua mỗi thế hệ trong Hình 6.6.

Đây thực sự là một vấn đề khó tối ưu hơn khi sử dụng thuật toán tiến hóa, vì không gian của các chuỗi không liên tục.

Thật khó để thực hiện các bước nhỏ, tăng dần theo đúng hướng, vì bước nhỏ nhất là lật một ký tự.

Do đó, nếu bạn cố gắng tạo chuỗi mục tiêu dài hơn, sẽ mất nhiều thời gian và nguồn lực hơn để phát triển.

Hình 6.6. Đây là biểu đồ về thể lực dân số trung bình qua các thế hệ.

Mức độ thích nghi trung bình của dân số tăng lên khá đơn điệu và sau đó ổn định, điều này có vẻ đầy hứa hẹn.

Nếu cốt truyện quá lởm chởm, tỷ lệ đột biến có thể quá cao hoặc quy mô quần thể quá thấp.

Nếu cốt truyện hội tụ quá nhanh, tỷ lệ đột biến có thể quá thấp.

Khi chúng tôi tối ưu hóa các tham số có giá trị thực trong một mô hình, ngay cả một sự gia tăng nhỏ về giá trị cũng có thể cải thiện mức độ phù hợp.

Và chúng ta có thể khai thác điều đó, giúp tối ưu hóa nhanh hơn.

Nhưng mặc dù các cá thể có giá trị rời rạc khó tối ưu hóa hơn trong thuật toán tiến hóa, nhưng chúng không thể tối ưu hóa bằng cách sử dụng phương pháp truyền ngược và truyền ngược độ dốc vanilla, vì chúng không khả vi.