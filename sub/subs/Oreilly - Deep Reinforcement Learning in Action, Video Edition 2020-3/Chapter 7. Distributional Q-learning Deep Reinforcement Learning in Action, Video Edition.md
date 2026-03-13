# Chương 7. Học tập củng cố sâu Q-learning phân phối trong hành động, Phiên bản video được dịch

---

Phần 7.4, Học tập Q phân phối.

Hiện chúng tôi đã đề cập đến tất cả các bước sơ bộ cần thiết để triển khai mạng Q sâu phân phối,

QUẬN-DQN.

Nếu bạn chưa hiểu hết tất cả nội dung ở các phần trước,

đừng lo lắng, nó sẽ trở nên rõ ràng hơn khi chúng ta bắt đầu viết mã.

Trong chương này, chúng ta sẽ sử dụng một trong những trò chơi Atari đơn giản nhất trong AI Gym mở,

Freeway, Hình 7.7, để chúng ta có thể huấn luyện thuật toán trên CPU máy tính xách tay.

Không giống như các chương khác, chúng tôi cũng sẽ sử dụng phiên bản RAM của trò chơi.

Nếu bạn nhìn vào môi trường trò chơi có sẵn tại liên kết này,

bạn sẽ thấy mỗi trò chơi có hai phiên bản, trong đó một phiên bản được gắn nhãn RAM.

Hình 7.7, Ảnh chụp màn hình từ Đường cao tốc trò chơi Atari.

Mục tiêu là di chuyển gà qua đường cao tốc, tránh các phương tiện giao thông đang chạy tới.

Freeway là trò chơi trong đó bạn điều khiển một con gà bằng các hành động lên, xuống hoặc không lên, không thao tác hoặc không làm gì cả.

Mục tiêu là di chuyển con gà băng qua đường cao tốc, tránh xe cộ đang chạy tới, sang phía bên kia,

nơi bạn nhận được phần thưởng cộng thêm một.

Nếu bạn không đưa được cả ba con gà qua đường trong một khoảng thời gian giới hạn,

bạn thua trò chơi và nhận được phần thưởng âm.

Trong hầu hết các trường hợp trong cuốn sách này, chúng tôi đào tạo các đặc vụ DRL của mình bằng cách sử dụng biểu diễn pixel thô của trò chơi,

và do đó sử dụng các lớp tích chập trong mạng lưới thần kinh của chúng tôi.

Tuy nhiên, trong trường hợp này, chúng tôi đang giới thiệu độ phức tạp mới bằng cách tạo DQN phân phối,

vì vậy, chúng tôi sẽ tránh các lớp tích chập để tập trung vào chủ đề trước mắt và duy trì hiệu quả đào tạo.

Phiên bản RAM của mỗi trò chơi về cơ bản là một bản trình bày nén của trò chơi dưới dạng vectơ 1,2,8 phần tử,

vị trí và vận tốc của từng nhân vật trong trò chơi, v.v.

Một vectơ phần tử 1,2,8 đủ nhỏ để xử lý thông qua một vài lớp dày đặc, được kết nối đầy đủ.

Khi bạn cảm thấy thoải mái với cách triển khai đơn giản mà chúng tôi sẽ sử dụng ở đây,

bạn có thể sử dụng phiên bản pixel của trò chơi và nâng cấp DQN để sử dụng các lớp chập.

Phần 7.4.1, trình bày phân phối xác suất trong Python.

Nếu bạn chưa đọc phần tùy chọn 7.3, điều quan trọng duy nhất bạn đã bỏ lỡ là thay vì sử dụng mạng nơ-ron

để biểu diễn hàm Q, Q pi của S, A, trả về một giá trị Q duy nhất,

thay vào đó, chúng ta có thể biểu thị một phân bố giá trị, Z pi của S, A, đại diện cho một biến ngẫu nhiên gồm các giá trị Q cho một cặp hành động trạng thái.

Chủ nghĩa hình thức xác suất này bao gồm các thuật toán xác định mà chúng ta đã sử dụng trong các chương trước,

vì một kết quả xác định luôn có thể được biểu diễn bằng phân bố xác suất suy biến, hình 7.8,

trong đó tất cả xác suất được gán cho một kết quả duy nhất.

Hình 7.8, đây là một phân bố suy biến, vì tất cả các giá trị có thể được gán xác suất bằng 0 ngoại trừ 1 giá trị.

Các giá trị kết quả không được gán xác suất 0 được gọi là hỗ trợ phân phối xác suất.

Phân phối suy biến có độ hỗ trợ là 1 phần tử, trong trường hợp này là giá trị 0.

Trước tiên hãy bắt đầu với cách chúng ta biểu diễn và làm việc với phân phối giá trị.

Như chúng tôi đã làm trong phần lý thuyết xác suất, chúng tôi sẽ biểu thị phân bố xác suất rời rạc trên phần thưởng bằng cách sử dụng mảng 2 số pi.

Mảng 1 num pi sẽ là kết quả có thể xảy ra, tức là sự hỗ trợ của việc phân phối,

và mảng còn lại sẽ là một mảng có kích thước bằng nhau lưu trữ các xác suất cho từng kết quả liên quan.

Hãy nhớ lại, nếu chúng ta lấy tích bên trong giữa mảng hỗ trợ và mảng xác suất, chúng ta sẽ nhận được phần thưởng mong đợi của phân phối.

Một vấn đề với cách chúng ta biểu diễn phân bố giá trị, z của s, a, là vì mảng của chúng ta có kích thước hữu hạn nên chúng ta chỉ có thể biểu thị một số kết quả hữu hạn.

Trong một số trường hợp, phần thưởng thường bị giới hạn trong một phạm vi hữu hạn cố định nào đó, nhưng trên thị trường chứng khoán chẳng hạn,

số tiền bạn có thể kiếm được hoặc mất về mặt lý thuyết là không giới hạn.

Với phương pháp của chúng tôi, chúng tôi phải chọn giá trị tối thiểu và tối đa mà chúng tôi có thể biểu thị.

Hạn chế này đã được giải quyết trong bài báo tiếp theo của Dabney, học tăng cường phân phối với hồi quy Quantile, 2017.

Chúng ta sẽ thảo luận ngắn gọn về cách tiếp cận của họ ở cuối chương.

Đối với đường cao tốc, chúng tôi giới hạn mức hỗ trợ trong khoảng từ âm 10 đến cộng 10.

Tất cả các bước thời gian không phải là điểm cuối, tức là những bước không dẫn đến trạng thái thắng hoặc thua, sẽ thưởng trừ 1 để phạt việc mất quá nhiều thời gian băng qua đường.

Chúng tôi thưởng cộng 10 nếu gà qua đường thành công và trừ 10 nếu thua trò chơi nếu gà không qua đường trước khi hết giờ.

Khi con gà bị ô tô tông, trò chơi chưa chắc đã thua. Con gà vừa bị đẩy ra xa khung thành.

DqN dist của chúng tôi sẽ có một trạng thái, là vectơ từ 1 đến 8 phần tử và sẽ trả về ba tensor riêng biệt nhưng có kích thước bằng nhau biểu thị phân bố xác suất trên mức hỗ trợ cho từng hành động trong số ba hành động có thể xảy ra.

Lên, xuống, không op, tùy theo trạng thái đầu vào.

Chúng ta sẽ sử dụng hỗ trợ 51 phần tử, vì vậy các tensor hỗ trợ và xác suất sẽ là 51 phần tử.

Nếu đặc vụ của chúng tôi bắt đầu trò chơi với DqN dist được khởi tạo ngẫu nhiên, thực hiện hành động và nhận phần thưởng trừ 1, thì làm cách nào để cập nhật DqN dist của chúng tôi?

Phân phối mục tiêu là gì và làm cách nào để tính hàm mất mát giữa hai phân phối?

Chà, chúng tôi sử dụng bất kỳ phân phối nào mà DqN dist trả về cho trạng thái tiếp theo, ST cộng 1, làm phân phối trước đó và chúng tôi cập nhật phân phối trước đó với phần thưởng được quan sát duy nhất, RT, sao cho một ít phân phối được phân phối lại xung quanh RT được quan sát.

Nếu chúng ta bắt đầu với một phân bố đều và quan sát RT bằng âm 1, thì phân bố sau sẽ không còn đồng đều nữa, nhưng nó vẫn khá gần nhau, hình 7.9.

Chỉ khi chúng ta quan sát nhiều lần RT bằng âm 1 cho cùng một trạng thái thì phân phối mới bắt đầu đạt cực đại mạnh quanh âm 1.

Trong quá trình học Q thông thường, tỷ lệ chiết khấu, gamma, kiểm soát mức độ đóng góp của phần thưởng dự kiến trong tương lai vào giá trị của trạng thái hiện tại.

Trong học tập Q phân phối, tham số gamma kiểm soát mức độ chúng tôi cập nhật trước đó đối với phần thưởng được quan sát, đạt được chức năng tương tự, hình 7.10.

Hình 7.9. Chúng tôi đã tạo một hàm thực hiện phân phối riêng biệt và cập nhật nó dựa trên phần thưởng được quan sát.

Hàm này đang thực hiện một loại suy luận Bayes gần đúng bằng cách cập nhật phân phối trước thành phân phối sau.

Bắt đầu từ phân phối đồng đều, trên cùng, chúng tôi quan sát thấy một số phần thưởng và chúng tôi nhận được phân phối cao nhất ở mức 0, hiển thị ở giữa, sau đó chúng tôi quan sát thấy nhiều phần thưởng hơn, tất cả đều bằng 0 và phân phối trở thành một phân phối hẹp, giống như bình thường, như được hiển thị ở phía dưới.

Hình 7.10. Hình này cho thấy sự phân bố đồng đều thay đổi như thế nào với các giá trị gamma, hệ số chiết khấu thấp hơn hoặc cao hơn.

Nếu chúng ta giảm giá tương lai nhiều thì phần sau sẽ tập trung nhiều vào phần thưởng được quan sát gần đây. Nếu chúng tôi chiết khấu hàng tuần trong tương lai, phần thưởng được quan sát sẽ chỉ cập nhật nhẹ mức phân phối trước đó,

vốn Z của ST cộng 1, vốn A T cộng 1. Vì đường cao tốc có ít phần thưởng tích cực lúc ban đầu, vì chúng tôi cần thực hiện nhiều hành động trước khi quan sát chiến thắng đầu tiên của mình, nên chúng tôi sẽ đặt gamma nên chỉ thực hiện các cập nhật nhỏ cho phân phối trước đó.

Trong danh sách 7.1, chúng tôi thiết lập một phân bố xác suất rời rạc thống nhất ban đầu và chỉ ra cách vẽ đồ thị đó.

Liệt kê 7.1, thiết lập phân bố xác suất rời rạc trong NumPy.

Chúng tôi đã xác định một phân phối xác suất thống nhất. Bây giờ hãy xem cách chúng tôi cập nhật bản phân phối. Chúng tôi muốn một hàm, cập nhật dấu gạch dưới, Dist of Z, phần thưởng có phân phối trước và phần thưởng được quan sát và trả về phân phối sau.

Chúng ta biểu diễn độ hỗ trợ của phân phối dưới dạng vectơ từ âm 10 đến 10.

Xem mã này.

Chúng ta cần có khả năng tìm thấy phần tử hỗ trợ gần nhất trong vectơ hỗ trợ với phần thưởng được quan sát. Ví dụ: nếu chúng tôi quan sát RT bằng âm 1, chúng tôi sẽ muốn ánh xạ giá trị đó thành âm 1,2 hoặc âm 0,8 vì đó là các phần tử hỗ trợ gần nhất, gần bằng nhau.

Quan trọng hơn, chúng ta muốn chỉ số của các phần tử hỗ trợ này để có thể nhận được xác suất tương ứng của chúng trong vectơ xác suất.

Vector hỗ trợ là tĩnh. Chúng tôi không bao giờ cập nhật nó. Chúng tôi chỉ cập nhật các xác suất tương ứng.

Bạn có thể thấy rằng mỗi phần tử hỗ trợ cách các phần tử lân cận gần nhất 0,4.

Hàm NumPy Linspace tạo một chuỗi các phần tử có khoảng cách đều nhau và khoảng cách được tính bằng V max trừ V min chia cho N trừ 1, trong đó N là số phần tử hỗ trợ.

Nếu bạn thay 10 trừ 10 và N bằng 51 vào công thức đó, bạn sẽ nhận được 0,4. Chúng tôi gọi giá trị này là DZ cho delta Z và chúng tôi sử dụng nó để tìm giá trị chỉ số phần tử hỗ trợ gần nhất theo phương trình BJ bằng R trừ V min chia cho DZ.

Vì BJ có thể là một số phân số và các chỉ số cần phải là số nguyên không âm nên chúng tôi chỉ cần làm tròn giá trị đến số nguyên gần nhất bằng vòng NumPy với các đối số bên trong dấu ngoặc đơn.

Chúng tôi cũng cần cắt bỏ mọi giá trị nằm ngoài phạm vi hỗ trợ tối thiểu và tối đa. Ví dụ: nếu RT quan sát được bằng trừ 2 thì BJ bằng trừ 2 trừ trừ 10 chia cho 0,4 bằng trừ 2.

Bạn có thể thấy rằng phần tử hỗ trợ có chỉ số 20 là âm 2, trong trường hợp này tương ứng chính xác với phần thưởng quan sát được, không cần làm tròn.

Sau đó chúng ta có thể tìm xác suất tương ứng cho phần tử hỗ trợ âm 2 bằng cách sử dụng chỉ mục.

Khi chúng tôi tìm thấy giá trị chỉ mục của phần tử hỗ trợ tương ứng với phần thưởng được quan sát, chúng tôi muốn phân phối lại một số khối lượng xác suất cho phần tử hỗ trợ đó và các phần tử hỗ trợ gần đó.

Chúng ta phải lưu ý rằng phân bố xác suất cuối cùng là phân bố thực và có tổng bằng 1.

Chúng ta sẽ chỉ cần lấy một số khối lượng xác suất từ các lân cận ở bên trái và bên phải và thêm nó vào phần tử tương ứng với phần thưởng quan sát được.

Sau đó, những người hàng xóm gần nhất sẽ đánh cắp một số khối lượng xác suất từ ​​người hàng xóm gần nhất của họ, v.v., như được hiển thị trong Hình 7.11.

Khối lượng xác suất bị đánh cắp sẽ nhỏ hơn theo cấp số nhân khi chúng ta càng đi xa khỏi phần thưởng quan sát được.

Hình 7.11. Hàm DIST cập nhật gạch dưới phân phối lại xác suất từ ​​các lân cận đối với giá trị phần thưởng được quan sát.

Trong Liệt kê 7.2, chúng ta triển khai hàm lấy một tập hợp các hỗ trợ, các xác suất liên quan và một quan sát, rồi trả về một phân bố xác suất được cập nhật bằng cách phân phối lại khối lượng xác suất cho giá trị được quan sát.

Liệt kê 7.2, cập nhật phân bố xác suất.

Chúng ta hãy tìm hiểu cơ chế hoạt động của nó để xem nó hoạt động như thế nào. Chúng tôi bắt đầu với sự phân phối trước thống nhất.

Xem mã này.

Bạn có thể thấy rằng mỗi hỗ trợ có xác suất khoảng 0,02. Chúng tôi quan sát RT bằng âm 1 và chúng tôi tính toán BJ xấp xỉ bằng 22.

Sau đó chúng ta tìm các hàng xóm bên trái và bên phải gần nhất, ký hiệu là ML và MR, lần lượt là chỉ số 21 và 23.

Chúng tôi nhân ML với gamma với lũy thừa của J, trong đó J là giá trị mà chúng tôi tăng thêm 1 bắt đầu từ 1, do đó chúng tôi nhận được một chuỗi gamma giảm theo cấp số nhân.

Gamma lũy thừa 1, gamma bình phương, gamma lũy thừa J.

Hãy nhớ rằng, gamma phải có giá trị từ 0 đến 1, vì vậy chuỗi gamma sẽ là 0,5, 0,25, 0,125, 0,0625,

nếu gamma bằng 0,5.

Vì vậy, lúc đầu, chúng ta lấy 0,5 nhân 0,02 bằng 0,01 từ các hàng xóm bên trái và bên phải, rồi cộng nó vào xác suất hiện có tại BJ bằng 22, cũng là 0,02.

Vậy xác suất tại BJ bằng 22 sẽ trở thành 0,01 cộng 0,01 cộng 0,02 bằng 0,04.

Bây giờ hàng xóm bên trái, ML, lấy khối lượng xác suất từ ​​hàng xóm bên trái của chính nó ở chỉ số 20, nhưng nó đánh cắp ít hơn vì chúng ta nhân với bình phương gamma.

Người hàng xóm bên phải, MR, cũng làm điều tương tự bằng cách ăn trộm của người hàng xóm bên phải.

Lần lượt từng phần tử lấy trộm từ phần tử bên trái hoặc bên phải của nó cho đến khi chúng ta đi đến cuối mảng.

Nếu gamma gần bằng 1, chẳng hạn như 0,99, rất nhiều khối lượng xác suất sẽ được phân phối lại cho vùng hỗ trợ gần với RT.

Hãy kiểm tra chức năng cập nhật phân phối của chúng tôi. Chúng tôi sẽ trao cho nó phần thưởng quan sát được là âm 1 bắt đầu từ việc phân phối đồng đều.

Liệt kê 7.3, phân phối lại khối lượng xác suất sau một lần quan sát.

Bạn có thể thấy trong hình 7.12 rằng sự phân bố vẫn khá đồng đều, nhưng bây giờ có một điểm lồi lên rõ rệt ở giữa điểm âm 1.

Chúng ta có thể kiểm soát mức độ lớn của vết sưng này bằng gamma hệ số chiết khấu. Tự mình thử thay đổi gamma để xem nó thay đổi bản cập nhật như thế nào.

Hình 7.12. Đây là kết quả của việc cập nhật phân bố xác suất thống nhất ban đầu sau khi quan sát một phần thưởng duy nhất.

Một số khối lượng xác suất được phân phối lại cho phần tử hỗ trợ tương ứng với phần thưởng được quan sát.

Bây giờ hãy xem sự phân bổ thay đổi như thế nào khi chúng ta quan sát một chuỗi các phần thưởng khác nhau.

Chúng tôi vừa tạo ra chuỗi phần thưởng này. Họ không đến từ trò chơi đường cao tốc. Chúng ta sẽ có thể quan sát đa phương thức.

Liệt kê 7.4, phân phối lại khối lượng xác suất với một chuỗi các quan sát.

Bạn có thể thấy trong hình 7.13 hiện nay có bốn đỉnh có độ cao khác nhau tương ứng với bốn loại phần thưởng khác nhau được quan sát, đó là 10, 0, 1 và trừ 10.

Đỉnh cao nhất, phương thức phân phối, tương ứng với 10, vì đó là phần thưởng được quan sát thường xuyên nhất.

Hình 7.13. Đây là kết quả của việc cập nhật phân bố xác suất thống nhất ban đầu sau khi quan sát một chuỗi các phần thưởng khác nhau. Mỗi đỉnh trong phân phối tương ứng với một phần thưởng được quan sát.

Bây giờ hãy xem phương sai giảm như thế nào nếu chúng ta quan sát cùng một phần thưởng nhiều lần, bắt đầu từ bộ đồng phục trước đó.

Liệt kê 7.5, phương sai giảm với chuỗi phần thưởng giống nhau.

Bạn có thể thấy trong hình 7.14 rằng phân bố đồng đều chuyển thành phân bố giống như chuẩn tắc có tâm ở 5 với phương sai thấp hơn nhiều.

Chúng tôi sẽ sử dụng hàm này để tạo phân phối mục tiêu mà chúng tôi muốn dqn dist tìm hiểu để ước chừng. Hãy xây dựng dist dqn ngay bây giờ.

Hình 7.14. Kết quả của việc cập nhật phân bố xác suất thống nhất ban đầu sau khi quan sát cùng một phần thưởng nhiều lần. Phân phối đều hội tụ về phía phân phối chuẩn.

Mục 7.4.2. Triển khai dist dqn. Như chúng ta đã thảo luận ngắn gọn trước đó, dist dqn sẽ lấy vectơ trạng thái 1, 2, 8 phần tử, chuyển nó qua một vài lớp chuyển tiếp dữ liệu dày đặc,

và sau đó nó sẽ sử dụng vòng lặp for để nhân lớp cuối cùng với 3 ma trận riêng biệt để được 3 vectơ phân phối riêng biệt.

Cuối cùng chúng ta sẽ áp dụng hàm softmax để đảm bảo đây là phân bố xác suất hợp lệ. Kết quả là một mạng lưới thần kinh có 3 đầu ra khác nhau.

Chúng tôi thu thập 3 phân phối đầu ra này thành một ma trận 3 nhân 51 và trả về đó là đầu ra cuối cùng của dqn dist.

Do đó, chúng ta có thể nhận được các phân phối giá trị hành động riêng lẻ cho một hành động cụ thể bằng cách lập chỉ mục cho một hàng cụ thể của ma trận đầu ra.

Hình 7.15. Hiển thị kiến ​​trúc tổng thể và các phép biến đổi tensor. Trong danh sách 7.6, chúng ta định nghĩa hàm thực hiện dist dqn.

Hình 7.15. Dist dqn chấp nhận vectơ trạng thái 1, 2, 8 phần tử và tạo ra 3 vectơ phân phối xác suất 51 phần tử riêng biệt, sau đó được xếp chồng thành một ma trận 3 nhân 51.

Liệt kê 7.6, dist dqn.

Trong chương này, chúng ta sẽ thực hiện giảm độ dốc theo cách thủ công và để thực hiện việc này dễ dàng hơn, chúng ta có dist dqn chấp nhận một vectơ tham số duy nhất gọi là theta, chúng ta sẽ giải nén và định hình lại thành nhiều ma trận lớp riêng biệt có kích thước phù hợp.

Điều này dễ dàng hơn vì chúng ta chỉ có thể thực hiện giảm độ dốc trên một vectơ duy nhất, thay vì trên nhiều thực thể riêng biệt.

Chúng ta cũng sẽ sử dụng một mạng đích riêng biệt như đã làm trong chương 3, vì vậy tất cả những gì chúng ta cần làm là giữ một bản sao của theta và chuyển nó vào cùng một hàm dqn gạch dưới dist.

Điểm mới lạ khác ở đây là nhiều đầu ra. Chúng ta đã quen với việc mạng thần kinh trả về một vectơ đầu ra duy nhất, nhưng trong trường hợp này, chúng ta muốn nó trả về một ma trận.

Để làm điều đó, chúng tôi thiết lập một vòng lặp trong đó chúng tôi nhân L2 với mỗi ma trận trong số ba ma trận lớp riêng biệt, tạo ra ba vectơ đầu ra khác nhau mà chúng tôi xếp chồng thành một ma trận.

Ngoài ra, nó là một mạng lưới thần kinh rất đơn giản với tổng cộng năm lớp dày đặc.

Bây giờ chúng ta cần một hàm sẽ lấy đầu ra của dist dqn, phần thưởng và hành động, đồng thời tạo ra mức phân phối mục tiêu mà chúng ta muốn mạng thần kinh của mình tiến gần hơn.

Hàm này sẽ sử dụng hàm dist gạch dưới cập nhật mà chúng ta đã sử dụng trước đó, nhưng nó chỉ muốn cập nhật phân phối liên quan đến hành động đã thực sự được thực hiện.

Ngoài ra, như bạn đã học ở chương 3, chúng ta cũng cần một mục tiêu khác khi đạt đến trạng thái cuối.

Ở trạng thái cuối, phần thưởng mong đợi là phần thưởng được quan sát, vì theo định nghĩa không có phần thưởng trong tương lai.

Điều đó có nghĩa là bản cập nhật Bellman rút gọn về Z của S, T, A, T, gán R của chữ S, T, chữ A, T viết hoa.

Vì chúng tôi chỉ quan sát một phần thưởng duy nhất và không có phân phối trước đó để cập nhật nên mục tiêu trở thành thứ được gọi là phân phối suy biến.

Đó chỉ là một thuật ngữ ưa thích cho một phân bố trong đó tất cả khối lượng xác suất tập trung ở một giá trị duy nhất.

Liệt kê 7.7, tính toán phân phối mục tiêu.

Hàm Get gạch dưới mục tiêu gạch dưới dist lấy một lô dữ liệu có hình B x 3 x 51, trong đó B là thứ nguyên lô và nó trả về một tenxơ có kích thước bằng nhau.

Ví dụ: nếu chúng tôi chỉ có một ví dụ trong lô của mình, 1 x 3 x 51 và tác nhân thực hiện hành động 1 và nhận thấy phần thưởng là âm 1, thì hàm này sẽ trả về tenxơ 1 x 3 x 51,

ngoại trừ việc phân phối 1 x 51 được liên kết với chỉ số 1 của thứ nguyên 1 sẽ được thay đổi theo hàm dist gạch dưới cập nhật bằng cách sử dụng phần thưởng được quan sát là âm 1.

Thay vào đó, nếu phần thưởng được quan sát là 10 thì phân phối 1 x 51 liên quan đến hành động 1 sẽ được cập nhật thành phân phối suy biến trong đó tất cả các phần tử có xác suất bằng 0, ngoại trừ phân phối 1 liên quan đến phần thưởng 10, chỉ số 50.