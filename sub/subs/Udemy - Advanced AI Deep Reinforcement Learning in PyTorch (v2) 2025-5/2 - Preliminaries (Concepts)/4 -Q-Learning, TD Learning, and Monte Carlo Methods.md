# 4 -Q-Learning, TD Learning và Monte Carlo Methods đã được dịch

---

Được rồi, trước đây chúng ta đã xem xét định lý cải tiến chính sách và sự lặp lại chính sách, điều mà tôi nên làm

lưu ý, mặc dù chúng tôi sẽ không triển khai chính xác điều này trong mã, nhưng thực sự là đủ để bạn thực hiện

thực hiện một tác nhân làm việc.

Được rồi, mặc dù chúng tôi đang hướng tới QLearning, nhưng chỉ riêng điều này thôi, vậy nên bạn đã biết đủ vào thời điểm này

để xây dựng một thuật toán học tăng cường tự nhiên.

Được rồi, vậy cách hoạt động của thuật toán là bạn bắt đầu bằng việc khởi tạo số pi chỉ là các giá trị ngẫu nhiên,

tương đương với việc khởi tạo Q với các giá trị ngẫu nhiên, bởi vì bạn sắp

làm số pi theo Q phải không?

Hành động được chọn bằng cách sử dụng Q, sau đó bạn thực hiện vòng lặp trong đó bạn luân phiên giữa việc đánh giá

và argmax mà chúng tôi gọi là cải tiến chính sách.

Và lý do tại sao chúng tôi không thực hiện điều này là do có vấn đề với thuật toán này.

Và vấn đề là nó mất quá nhiều thời gian.

Vì vậy, nếu bạn nghĩ xem việc này phải được thực hiện bao nhiêu lần, chúng ta phải chơi bao nhiêu lần

các tập trong trò chơi của chúng tôi, bạn sẽ nhận thấy rằng thực tế có hai vòng lặp ở đây, mặc dù nó chỉ

hình như có một cái.

Được rồi, vậy là chúng ta có một vòng lặp, rõ ràng là một vòng lặp vì tôi đã viết loop.

Và vòng lặp này, nhiệm vụ của nó là lặp lại từng phiên bản của Q. Vì vậy, chúng ta bắt đầu với

Q ngẫu nhiên, sau đó chúng tôi đánh giá nó, sau đó chúng tôi sử dụng argmax để cải thiện nó một chút, sau đó chúng tôi

đánh giá lại Q, sau đó chúng tôi sử dụng lại argmax, sau đó chúng tôi đánh giá lại Q, v.v.

Nhưng bạn sẽ nhận thấy rằng bản thân việc đánh giá là một vòng lặp vì chúng ta phải chơi trò chơi nhiều lần.

lần.

Trên thực tế, đã rất nhiều lần thu thập các mẫu trả lại để chúng tôi có thể tìm thấy Q, tức là

giá trị trung bình mẫu của những lợi nhuận đó.

Được rồi, đây thực ra cũng là một vòng lặp.

Được rồi, vậy giải pháp cho vấn đề này là gì?

Giải pháp cho vấn đề này được gọi là lặp lại chính sách tổng quát hoặc GPI.

Vì vậy, đó là sự lặp lại chính sách tổng quát hoặc GPI.

Được rồi, cách thức hoạt động về cơ bản là chúng tôi cắt bớt bước đánh giá để thu thập

chỉ có một mẫu.

Đây là một thay vì đánh giá Q bằng cách thu thập nhiều mẫu, chúng tôi chỉ chơi trò chơi một lần

và điều đó cung cấp cho chúng tôi một mẫu mới cho Q bằng cách sử dụng bất kỳ trạng thái và hành động nào mà chúng tôi gặp phải

trong vòng đó, trong tập đó.

Và điều này sẽ làm mọi việc nhanh hơn nhiều vì bây giờ chỉ có một vòng lặp thay vì hai

các vòng lặp lồng nhau.

Được rồi, chúng ta sẽ bắt đầu một trang mới và điều này dẫn chúng ta đến thuật toán điều khiển đầu tiên

nơi chúng ta bắt đầu với Q ngẫu nhiên và sau đó với Q tối ưu. Và đây được gọi là Monte Carlo

Kiểm soát.

Vì vậy, Kiểm soát Monte Carlo.

Được rồi, cách thức hoạt động của nó là chúng ta được cấp một đối tượng ENV như trước.

Bạn đã thấy điều này khi chúng tôi giới thiệu thuật toán học Q và sau đó chúng tôi khởi tạo QSA,

bằng một giá trị ngẫu nhiên cho mọi S và không gian trạng thái S và mọi hành động trong

không gian hành động A.

Được rồi, từ đây chúng ta sẽ phát tập phim này vài lần.

Vì vậy, đối với tôi trong phạm vi, số tập, tôi đoán đây có thể là đầu vào nhưng hãy bỏ nó đi.

Được rồi, vậy là bạn đã thấy hầu hết những điều này trước đây.

Vì vậy, chúng tôi thiết lập lại môi trường.

Điều này cung cấp cho chúng tôi trạng thái ban đầu, thiết lập lại dấu chấm ENV và sau đó chúng tôi chơi cho đến khi hoàn tất.

Vì vậy chúng ta sẽ khởi tạo done thành false.

Vì vậy, điều này rõ ràng cũng sẽ khác với những gì bạn đã thấy trước đây vì nó không phải là Q

học tập.

Và chúng ta sẽ lưu lại tất cả các trạng thái, hành động và phần thưởng mà chúng ta gặp phải.

Vì vậy, trạng thái, hành động, phần thưởng.

Vì vậy, chúng tôi sẽ bắt đầu chúng dưới dạng danh sách trống và chúng tôi sẽ điền chúng khi chúng tôi phát trong tập.

Được rồi, vậy chúng ta sẽ nói trong khi chưa xong.

Được rồi.

Và do đó, điều này sẽ sử dụng Q hiện tại để phát một tập.

Vì vậy, bạn có thể coi đây là bước cải tiến vì đây là lúc chúng tôi lấy arg max

đôi khi hơn Q.

Vì vậy, chúng ta sẽ chọn hành động bằng cách sử dụng chiến lược tham lam epsilon của mình.

Vì vậy hãy chọn hành động.

Vì vậy đôi khi chúng ta sẽ chọn hành động tối ưu theo Q.

Vì vậy hãy chọn hành động.

Chúng ta sẽ đậu ở Q. Chúng ta sẽ đậu ở bang S. Được rồi.

Và tiếp theo chúng ta thực hiện bước đó, thực hiện hành động đó trong môi trường.

Chúng tôi nhận lại phần thưởng trạng thái tiếp theo và cờ hoàn thành.

Vì vậy, bước chấm ENV.

Truyền vào hành động A. Được rồi.

Và bây giờ chúng tôi có tất cả dữ liệu này mà chúng tôi có thể sử dụng.

Vì vậy, chúng ta sẽ thêm trạng thái này vào danh sách các trạng thái của mình.

Thêm hành động vào danh sách hành động của chúng tôi và thêm phần thưởng vào danh sách phần thưởng của chúng tôi.

Và đây là một bước quan trọng mà mọi người luôn quên đó là thay đổi trạng thái hiện tại

là trạng thái tiếp theo cho vòng tiếp theo của vòng lặp này.

Được rồi.

Và hãy chú ý rằng vòng lặp này chúng tôi không cập nhật Q. Nó chỉ phát tập theo

Q. Được rồi.

Và sau khi thoát khỏi vòng lặp này, chúng ta đã phát xong tập phim.

Bây giờ chúng tôi có thể cập nhật Q. Vì vậy, bạn có thể coi đây là bước đánh giá.

Và chúng ta sẽ làm điều này như thế nào?

Vì vậy, hãy chú ý cách tôi đã nói với Monte Carlo, chúng tôi muốn sử dụng lợi nhuận trung bình đó, đó là chúng tôi

sử dụng chữ G. Nhưng tất cả những gì chúng tôi có cho đến nay là phần thưởng cá nhân.

Vì vậy, điều chúng ta cần làm là bằng cách nào đó tính G bằng cách tính tổng R một cách thích hợp.

Và cách chúng tôi làm điều đó là với vòng lặp này.

Vì vậy, chúng ta sẽ nói về trạng thái S. Ồ, và chúng ta sẽ khởi tạo G bằng 0.

Bạn sẽ thấy lý do tại sao rất sớm.

Vì vậy, SAR tham gia và vì vậy chúng tôi sẽ đảo ngược các hành động và phần thưởng của tiểu bang.

Vì vậy, chúng ta sẽ lặp lại chúng theo chiều ngược lại.

Vì vậy, trạng thái, hành động và phần thưởng.

Và vì vậy trong vòng lặp này, trước tiên chúng ta sẽ tính G sẽ bằng bao nhiêu.

Được rồi.

Vậy là G. Và chúng ta lại thấy cùng một khuôn mẫu, khuôn mẫu đệ quy đó.

Vậy G bằng R cộng gamma nhân G. Được rồi.

Bởi vì trên thực tế chúng ta nên đặt một lỗi ở đó vì chúng ta đang gán.

Bây giờ nó là một chữ G xấu xí. Được rồi.

Vậy chữ G bên phải là G cũ. Và chữ G bên trái là G mới. Được rồi.

Và rõ ràng là bạn phải suy nghĩ về điều này một chút.

Hãy suy nghĩ về lý do tại sao nó hoạt động.

Bởi vì nó không thực sự rõ ràng.

Trên thực tế, bước tiếp theo này là bước không rõ ràng nhất.

Và đó chỉ là do tôi bỏ qua rất nhiều cho mục đích đánh giá này.

Nhưng chúng tôi cập nhật Q bằng công thức này.

Vậy là QSA.

Vì vậy, một lần nữa, đây là giá trị mới.

Nó xuất phát từ giá trị cũ của QSA.

Và sau đó cộng với tốc độ học tập nhân với giá trị G hiện tại bằng trừ QSA.

Được rồi.

Và vì vậy bạn có thể hỏi, à, đây không phải là ý nghĩa mẫu sao?

Và câu trả lời là có.

Và câu trả lời cũng là như vậy.

Và vì vậy nếu bạn muốn biết cách thức hoạt động của nó, bạn sẽ phải xem toàn bộ bài đánh giá

hoặc khóa học tăng cường đầy đủ, là điều kiện tiên quyết cho khóa học này, để

hiểu lý do tại sao điều này thực hiện ý nghĩa mẫu.

Được rồi.

Vì vậy, tôi sẽ đưa ra một bình luận ở đây.

Điều này tương đương với khoảng.

Chúng ta thực sự cần phải phân rã tốc độ học để có được giá trị trung bình mẫu chính xác.

Nhưng điều này thực sự có tác dụng tốt hơn vì chính sách cũng đang thay đổi.

Chính sách này không cố định khi chúng tôi lặp qua phần này, khi chúng tôi lặp qua các tập.

Được rồi.

Vì vậy, đây gần như là mẫu trung bình.

Trên thực tế, đây là đường trung bình động có trọng số theo cấp số nhân của những khoản lợi nhuận đó nếu bạn tò mò.

Đó là đủ chi tiết cho đánh giá này.

Tất cả những gì bạn phải biết là đây giống như ý nghĩa mẫu.

Và một số ý kiến ​​khác về điều này.

Vì vậy, trước tiên, tôi phải thừa nhận, vì tôi chưa thực sự chạy mã này nên đây chỉ là mã giả,

có thể có một số sai sót ở đây.

Vì vậy, nếu bạn muốn biết điều này thực sự hoạt động như thế nào trong thực tế, bạn luôn có thể truy cập trang khác của tôi

Khóa học tăng cường điều kiện tiên quyết của tôi là nơi chúng tôi thực sự triển khai điều này, phải không?

Đây chỉ là để cung cấp cho bạn một số trực giác về cách nó hoạt động.

Vì vậy, bạn muốn nghĩ về bức tranh lớn.

Giống như tại sao chúng ta đảo ngược các phần trạng thái và phần thưởng?

Tại sao lại có hai vòng lặp riêng biệt này, v.v.?

Được rồi.

Vì vậy, với mục đích của bài đánh giá này, hãy nghĩ đến những nét khái quát hơn là những chi tiết nhỏ này.

Được rồi.

Vì vậy, thứ hai, hãy quay lại phép tính trung bình mẫu này hoặc những gì tôi cho là mẫu

nghĩa là.

Và hãy nghĩ xem liệu bạn có thực sự tính toán giá trị trung bình mẫu ở đây hay không.

Vì vậy, thay vào đó, nếu bạn làm điều gì đó như thế này, thì QSA sẽ bằng 1 trên n, một số i từ 1

đến N.

Và sau đó là một số chữ G mà bạn đã gặp cho đến nay đối với trạng thái và hành động này.

Lưu ý rằng bạn cũng sẽ phải theo dõi các phần cuối, chẳng hạn như số lượng.

Vì vậy, những thứ này cũng sẽ được SNA lập chỉ mục.

Phải.

Vì vậy, bạn đã được SNA lập chỉ mục.

Được rồi.

Vì vậy, đó là một chi tiết kế toán khác mà bạn cần quan tâm.

Nhưng cũng khôn ngoan, điều này không hiệu quả để thực hiện với một số thứ n, đó là chữ O của

n hoạt động.

Vì vậy, bạn sẽ thực hiện một thao tác O trên n S bên trong một vòng lặp khác, việc này có khả năng sẽ mất

một thời gian dài.

Phải.

Nó làm cho vòng lặp này trở thành bậc hai về độ phức tạp thời gian thay vì hằng số.

Được rồi.

Vì vậy, một chi tiết khác cần suy nghĩ là nếu trước đây bạn đã học về máy học, thì

Tôi cho rằng hầu hết các bạn đều có và đó là điều tôi khuyên bạn trước khi bắt đầu tăng cường

học được rằng điều này trông giống như sự giảm dần độ dốc một cách đáng ngờ.

Trên thực tế, đây là dấu gạch chéo độ dốc đi lên.

Được rồi.

Vì vậy, đây là sự đi lên theo độ dốc.

Được rồi.

Và sai số bình phương với tổn thất sẽ là g trừ q dưới dạng bình phương.

Được rồi.

Vì vậy, tổn thất sai số bình phương điển hình cho hồi quy.

Được rồi.

Vì vậy, về cơ bản đó là toàn bộ thuật toán và sau đó một vài nhận xét sẽ cắt bớt những hiểu biết sâu sắc về cách nó

hoạt động.

Nhưng bạn sẽ nhận thấy rằng cũng có vấn đề với điều này.

Vì vậy, hãy để tôi nhấn mạnh những vấn đề này.

Hãy xem xét hạn chế này là chúng ta phải phát toàn bộ tập trước khi có thể thực hiện bất kỳ

thay đổi thành q và do đó cập nhật chính sách.

Phải.

Vì vậy, thực sự ở đây, tôi đã nói rằng đây giống bước đánh giá hơn, nhưng trên thực tế, đây là

giống bước cải tiến hơn vì chúng tôi đang cập nhật q, điều này sẽ thay đổi chính sách.

Vì vậy, có một chút chúng được trộn lẫn với nhau, nhưng nó không thực sự quan trọng về mặt tổng thể.

kế hoạch của sự vật.

Và dù sao đi nữa, điều quan trọng cần chú ý bây giờ là chúng ta phải làm toàn bộ việc này

trước khi chúng tôi có thể cập nhật q.

Và điều gì sẽ xảy ra nếu tập phim thực sự dài hoặc thậm chí là vô tận?

Nếu là tập vô hạn, chúng tôi sẽ không bao giờ cập nhật q, điều này không tốt.

Điều đó có nghĩa là mô hình của chúng tôi sẽ không bao giờ học hoặc các tác nhân sẽ không bao giờ học.

Nếu nó quá dài thì điều đó thực sự không hiệu quả vì điều đó có nghĩa là bạn phải

phát một tập phim thực sự dài trước khi bạn có thể thực hiện bất kỳ thay đổi nào đối với q.

Và điều đó không tốt.

Được rồi, trong phần còn lại của bài giảng này, chúng ta sẽ tập trung chủ yếu vào phần này

chúng tôi sửa đổi điều này để hiệu quả hơn một chút.

Chúng tôi sẽ tập trung vào bản cập nhật cụ thể này của q.

Được rồi, vậy chúng ta sẽ bắt đầu một trang mới.

Và vì vậy tôi sẽ lưu ý rằng thuật toán của chúng tôi thực sự đã hoàn thành được 90%.

Chúng ta đã tiến rất gần đến việc học q vào thời điểm này.

Chúng ta chỉ cần thực hiện một vài thay đổi so với thuật toán điều khiển Monte Carlo mà chúng ta vừa xem xét.

tại.

Vì vậy, hiện tại chúng ta có thể nghĩ về nó ở mức độ cao hơn.

Vì vậy, hiện tại chúng ta có thay vì G, hãy nghĩ về nó như là chúng ta có một mục tiêu nào đó.

Vì vậy, q, SA là QSA cũ cộng với tốc độ học nhân với mục tiêu trừ đi QSA cũ.

Vì vậy, việc q học được điều này sẽ làm thay đổi mục tiêu là gì.

Và vì vậy đối với MC, Monte Carlo, mục tiêu là G, hay nghĩ về nó là G của T, tức là R của T

cộng một cộng R của T cộng hai.

Và vân vân và vân vân.

Trò chơi là hai R của T cộng ba.

Được rồi.

Bây giờ điều gì sẽ xảy ra nếu chúng ta chỉ thay thế phần còn lại bằng giá trị kỳ vọng của nó hoặc ước tính giá trị kỳ vọng của nó?

giá trị.

Nếu chúng ta làm điều đó, đó chính là điều mang lại cho chúng ta sự học hỏi.

Chà, theo cách cụ thể này, thực tế có nhiều cách bạn có thể làm điều này.

Nhưng một lần nữa, đó lại là chủ đề của khóa học tăng cường đầy đủ.

Được rồi.

Vì vậy, đối với TD, cụ thể là học Q, mục tiêu là R của T cộng một cộng gamma nhân với

ước tính phần còn lại, như bạn biết là hàm giá trị.

Và thay vì chỉ có hàm giá trị, thực ra hàm giá trị sẽ là Sarsa.

Nhưng đó không phải là vấn đề.

Một lần nữa, hãy xem lại toàn bộ khóa học tăng cường nếu bạn muốn tìm hiểu về điều đó.

Đối với việc học Q, những gì chúng tôi làm là đạt mức tối đa.

Vì vậy, chúng tôi nói giá trị tối đa trên tất cả các hành động A. Chúng tôi gọi nó là số nguyên tố.

Số nguyên tố của Q. Và sau đó tôi sẽ trộn các ký hiệu của mình ở đây, nhưng chúng ta sẽ nói trạng thái tiếp theo tại

thời gian T cộng một.

Và sau đó là một số nguyên tố.

Nhưng tôi hy vọng bạn có được ý tưởng.

Vì vậy, bạn cũng có thể đặt số nguyên tố này vào đó.

Vì vậy, đây là trạng thái tiếp theo trạng thái tiếp theo.

Và hành động tiếp theo.

Vì vậy, nó đạt mức tối đa cho tất cả các hành động tiếp theo.

Vậy điều này có nghĩa là gì?

Đó là loại tinh tế.

Nó có nghĩa là chúng ta đặt mục tiêu theo hành động mà lẽ ra chúng ta sẽ làm nếu tuân theo

chính sách tham lam.

Không phải chính sách tham lam của epsilon, chính sách tham lam.

Nói cách khác, nếu chúng ta làm theo những gì chúng ta tin là hành động tốt nhất.

Được rồi.

Và phần thưởng chỉ là phần thưởng không thay đổi.

Được rồi.

Vì vậy, hãy chú ý rằng khi bạn làm điều này, bạn không thực sự tính Q theo

chính sách bạn đang theo dõi.

Bạn đang tính Q theo chính sách mà bạn sẽ tuân theo nếu bạn làm điều tối ưu

hoặc những gì bạn tin là điều tối ưu hiện tại.

Và vì lý do đó, chúng tôi gọi đây là thuật toán tắt chính sách.

Vì vậy, tắt chính sách.

Đây không phải là một sự khác biệt quá quan trọng đối với khóa học này.

Vì vậy, tôi sẽ không lo lắng quá nhiều nếu bây giờ bạn thấy nó khó hiểu.

Nhưng hãy ghi nhớ điều đó cho việc học tập sau này của bạn.

Được rồi.

Vì vậy, một cách dễ dàng hơn để viết điều này, tất nhiên, chỉ là mục tiêu là R cộng gamma lần tối đa hoặc

Một số nguyên tố Q của S số nguyên tố A.

Được rồi.

Đó là cách điển hình hơn bạn sẽ thấy điều này.

Được rồi.

Và tôi cũng muốn lưu ý rằng có một việc khác chúng ta có thể làm, đó là một việc ở giữa

hai thứ này được gọi là phương pháp N bước.

Được rồi.

Vì vậy, trong trường hợp này, chúng ta có thể có mục tiêu bằng R của T cộng một cộng gamma nhân R của T cộng

hai và sau đó cộng gamma bình phương và sau đó đạt cực đại, chúng ta sẽ gọi nó là A của T cộng hai.

Và sau đó là Q của S của T cộng, nó sẽ là bao nhiêu?

Hai, vâng.

Hai.

A của T cộng hai.

Được rồi.

Và trong trường hợp này, bạn đang thu thập hai phần thưởng và sau đó ước tính phần còn lại.

Trong khi ở phần trước, bạn đang lấy mẫu một phần thưởng và sau đó ước tính phần còn lại.

Và về cơ bản N cho phương pháp N bước là số phần thưởng thực tế bạn sử dụng.

Nhưng bạn có thể sử dụng bất kỳ số lượng phần thưởng nào bạn chọn.

Và điều này liên quan đến một khái niệm trong học máy được gọi là sự đánh đổi phương sai sai lệch.

Được rồi.

Vì vậy, phương sai thiên vị phải đánh đổi.

Và một lần nữa, điều này không quá quan trọng nếu bạn chưa từng nghe đến điều này trước đây.

Nhưng nếu có, bạn sẽ thấy nó hữu ích.

Được rồi.

Vì vậy, nếu bạn đã nghe về điều này, những gì tôi sắp nói sẽ có lý.

Vì vậy, về cơ bản Monte Carlo chính xác hơn vì nó sử dụng số tiền lãi thực tế bạn nhận được.

Vì vậy, nó có độ lệch thấp, nhưng có độ lệch cao bởi vì mỗi khi bạn chơi trò chơi, bạn

sẽ nhận được một sự trở lại khác nhau.

Mặt khác, thái cực còn lại là học TD khi bạn chỉ sử dụng một phần thưởng thực tế.

Và sau đó bạn ước tính phần còn lại.

Vì vậy, vì bạn đang sử dụng ước tính cho phần lớn lợi nhuận, nên chúng tôi nói rằng con số đó có tỷ lệ cao

sai lệch, nhưng nó có phương sai thấp vì nếu bạn làm điều này, chẳng hạn 100 lần, bạn sẽ

sử dụng cùng một giá trị mọi lúc để ước tính phần lợi nhuận còn lại.

Được rồi.

Vì vậy, đó là một khái niệm hữu ích và thú vị cần ghi nhớ.

Vì vậy, trong mọi trường hợp, điều quan trọng cần biết ở đây, thông điệp mang về nhà là thay vào đó

vì phải phát toàn bộ tập phim, bạn chỉ cần cập nhật Q bằng một bước.

Và đó dường như là chủ đề của tất cả các thuật toán này, phải không?

Chúng tôi bắt đầu với một điều đầy đủ ở Monte Carlo, nơi chúng tôi phải ước tính bằng cách sử dụng rất nhiều mẫu

và chúng tôi rút ngắn điều đó bằng cách nói, này, điều gì sẽ xảy ra nếu chúng tôi chỉ giữ một mẫu và sau đó sử dụng mẫu đó

để cập nhật ước tính của chúng tôi.

Và hóa ra nó hoạt động khá tốt.

Được rồi.

Vậy TD, trong trường hợp tôi chưa viết điều này, TD là viết tắt của việc học khác biệt theo thời gian.

Khác biệt.

Và trong trường hợp bạn chưa từng nghe thuật ngữ này trước đây, chúng tôi đang khởi động lại ước tính của mình về

Q sử dụng ước tính hiện có của Q. Được rồi.

Vì vậy, khởi động.

Đây chỉ là thuật ngữ phổ biến và học tập tăng cường.

Q sử dụng Q hiện tại. Được rồi.

Vì vậy chúng ta sẽ bắt đầu một trang mới.

Và vì vậy, chủ đề cuối cùng của bài giảng này là xem xét câu hỏi, điều gì sẽ xảy ra nếu

các trạng thái không rời rạc và không hữu hạn, điều này sẽ xảy ra với tất cả các ví dụ

trong khóa học này?

Hiện tại chúng ta đang xem Q của S và một dạng bảng.

Vì vậy, trên thực tế, chúng tôi gọi nó là bảng Q.

Và tại sao chúng tôi lại nói như vậy?

Và câu trả lời là nó có hàng và cột, phải không?

Vì vậy, bạn có thể coi Q như một bảng trong đó chúng ta có tất cả các giá trị khác nhau của S. Vậy S bằng

một bằng hai.

Cho đến S bằng kích thước của không gian trạng thái.

Và sau đó bạn có tất cả các hành động ở đây, phải không?

Vậy một bằng một bằng hai.

Và khi đó a bằng bất kể kích thước của không gian hành động là bao nhiêu.

Và sau đó mỗi giá trị trong bảng này là lợi nhuận ước tính cho trạng thái và hành động đó.

Vậy điều gì sẽ xảy ra nếu bạn có vô số trạng thái hoặc vô số hành động và

bạn không thể làm điều này nữa?

Vì vậy, những gì chúng tôi làm trong trường hợp này là sử dụng hàm gần đúng.

Vì vậy, để làm ví dụ, giả sử chúng ta tạo một vectơ đặc trưng.

Vì vậy, vectơ đặc trưng X.

Và cái này bằng 5 của S và a.

Vì vậy, phép tính gần đúng của hàm tuyến tính sẽ là Q, S, A bằng W chuyển vị.

Vì vậy, một số vectơ trọng số nhân với X, sẽ là W hoán vị 5 của S, được chứ?

Và đây là lý do tại sao tôi luôn khuyên mọi người nên học machine learning thường xuyên trước

họ nghiên cứu học tăng cường vì như bạn có thể thấy, học máy thông thường chỉ là

một phần của việc học tăng cường.

Được rồi, và có một cách khác để mô tả đầu vào, cách này phổ biến hơn trong các phương thức

chúng tôi sẽ xem xét.

Vì vậy, thay vì làm những gì chúng ta đã làm ở trên, chúng ta sẽ làm Q của S A.

Vậy tôi sẽ biến nó.

Điều này tương đương với một chuyển vị W lớn và sau đó là năm S.

Và đây là gì?

Thực ra nói A ở đây cũng không đúng lắm.

Điều này giống như một sự dành cho tất cả hơn, rất tiếc.

Với mọi giá trị của A.

Và cách nghĩ về điều này là giả sử số năm của bạn có rất nhiều giá trị.

Và sau đó là cơ sở hành động của bạn, giả sử đó chỉ là hai giá trị.

Vì vậy, có hai hành động có thể xảy ra.

Được rồi, đây sẽ là năm của bạn và đây sẽ là kết quả đầu ra của bạn.

Và W ở đây, đây là ma trận trọng số.

Và sau đó bạn có một đầu ra cho mọi hành động có thể.

Vậy đây sẽ là Q của S A bằng một và Q của S A bằng hai.

Và rõ ràng là đối với khóa học này, được gọi là học tăng cường sâu,

sử dụng mạng lưới thần kinh sâu, phép tính gần đúng của hàm này sẽ không tuyến tính.

Nó sẽ là một mạng lưới thần kinh và chúng ta sẽ xem xét nhiều loại mạng lưới thần kinh khác nhau để thực hiện

nhiều nhiệm vụ khác nhau.

Và điều này làm thay đổi bản cập nhật như thế nào?

Vì vậy, giả sử rằng chúng ta có một mạng lưới thần kinh và nó được sử dụng để thực hiện phép tính gần đúng hàm

cho Q

Và thế là chúng ta sẽ gọi thông số, bút của mình lại bị lag.

Đó là ngẫu nhiên làm điều này.

Chúng ta sẽ gọi các tham số là theta.

Vì vậy, thay vì thực hiện cập nhật mà chúng tôi đã làm trước đây, tức là chúng tôi cập nhật Q trực tiếp, bây giờ điều gì sẽ xảy ra?

nó có nghĩa là cập nhật Q?

Trên thực tế, thứ chúng tôi thực sự đang cập nhật là theta, các thông số của mạng lưới thần kinh.

Vì vậy, bản cập nhật trở thành.

Và theta, theta mới được gán theta cũ cộng với số lần tốc độ chạy bất kể mục tiêu là gì

là trừ Q S A theta nhân với gradient của Q đối với theta.

Vậy là S A hết chỗ trống theta.

Và tôi nên đề cập rằng, tôi nghĩ rằng tôi đã mắc một sai lầm nhỏ trước đó, khi tôi nói rằng chúng tôi đang giảm thiểu

sự mất mát lỗi bình phương.

Nhưng trên thực tế vì có dấu cộng ở đây nên điều này giống việc tối đa hóa số âm hơn

mất mát lỗi bình phương.

Vì vậy, đó cũng là một điều quan trọng cần ghi nhớ đối với việc học tăng cường là mặc dù

tất cả các thuật toán đều được trình bày như thế này trong máy tính khi bạn học sâu

với các thư viện như PyTorch hoặc TensorFlow, chúng hoạt động bằng cách giảm thiểu mục tiêu.

Vì vậy, bạn luôn phải thể hiện mục tiêu của mình như một điều gì đó cần giảm thiểu.

Như vậy trong thực tế muốn có điểm cộng ở đây bạn có điểm trừ thì mục tiêu sẽ

được điều chỉnh cho phù hợp.

Và một lưu ý cuối cùng cho việc này.

Vì vậy, mặc dù điều này được trình bày dưới dạng giảm độ dốc thông thường, bạn luôn có thể hoán đổi các

trình tối ưu hóa, hiệu quả hơn so với giảm độ dốc.

Vì vậy, ví dụ: thêm ừm, OK, RMS prop, v.v.