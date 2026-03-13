# 2 -Trả về, hàm giá trị và phương trình Bellman được dịch

---

Được rồi, trước đây tôi đã nói chúng ta sẽ chia bài giảng này thành hai phần.

Phần đầu tiên sẽ tập trung vào các thuật ngữ và phần thứ hai, các thuật ngữ và số lượng, và

phần thứ hai sẽ tập trung vào các phương pháp giải hoặc thuật toán mà chúng tôi sử dụng có liên quan đến

những đại lượng đó trong học tập tăng cường.

Thay vào đó, những gì tôi coi là phần một, thực ra tôi sẽ chia thành hai phần

trong chính nó.

Vì vậy, phần đầu tiên có nhiều thuật ngữ hơn và phần thứ hai có nhiều số lượng hơn.

Được rồi, trong bài giảng này chúng ta sẽ sử dụng tất cả các thuật ngữ mà chúng ta đã định nghĩa ở phần trước.

giảng và xây dựng dựa trên chúng để xác định các đại lượng mới và hữu ích.

Được rồi, chúng tôi đã xem xét phần thưởng và mục tiêu của chúng tôi là đạt được mức tối đa

thưởng qua từng tập.

Được rồi, và chúng tôi sẽ sớm làm rõ chính xác điều đó có nghĩa là gì.

Vì vậy, đầu tiên chúng ta sẽ nói về một đại lượng mới đó là chính sách.

Vì vậy, chính sách là những gì mô tả hành vi của tác nhân.

Được rồi, mô tả các đặc vụ, và cách tôi viết trong dấu nháy đơn ở đó, mô tả hành vi của các đặc vụ.

Được rồi, cụ thể đó là một chức năng.

Vì vậy, đây là một hàm nhận trạng thái s và trả về hành động a.

Được rồi, điều này khá minh họa vì nó cho chúng ta biết rằng hành động được thực hiện bởi

một tác nhân chỉ phụ thuộc vào trạng thái hiện tại.

Nó không phụ thuộc vào bất kỳ trạng thái nào trước đó.

Được rồi, đó chỉ là một phần trong khuôn khổ học tập tăng cường mà chúng tôi tuân theo.

Chúng tôi không cần phải tuân theo khuôn khổ này, nhưng đó là khuôn khổ chúng tôi làm.

Được rồi, và trên thực tế có hai cách để thể hiện một chính sách.

Vậy có hai cách, hai cách để thể hiện chính sách.

Số một là xác định.

Vì vậy thuật ngữ này là huyền bí.

Được rồi, và chúng ta nói chính sách này là hành động là pi(s).

Vậy pi là hàm, s là đầu vào của hàm đó.

Vì vậy, như tôi đã đề cập trước đây, thật tuyệt khi nghĩ về cách bạn triển khai những điều này

những thứ trong mã.

Được rồi, điều đó sẽ ngày càng hữu ích hơn khi chúng ta cùng thảo luận về tất cả những điều này.

lượng và thuật toán.

Vì vậy, một cách để thực hiện điều này sẽ là, ví dụ, việc triển khai sẽ là một Python

từ điển.

Được rồi, ví dụ, giả sử không gian trạng thái của bạn, không gian trạng thái của bạn bằng một, hai,

ba.

Được rồi, có những trạng thái riêng biệt.

Bạn chỉ có ba trạng thái trong môi trường của bạn.

Và sau đó chính sách của bạn hoặc từ điển Python thể hiện chính sách đó có thể là một điểm

đến.

Cứ cho là đi lên đi xuống rồi ba nói cháy hay gì đó.

Được rồi, vậy đó có thể là một loại trò chơi điện tử mà bạn chỉ có thể thực hiện ba hành động đó

và sau đó chỉ ở ba trạng thái đó.

Đây không phải là một trò chơi thú vị lắm, nhưng bạn hiểu ý đấy.

Được rồi.

Vì vậy, một cách khác để trình bày các chính sách là xác suất.

Vì vậy, có xác suất.

Và trong trường hợp này, chúng tôi sẽ định lượng chính sách bằng phân phối xác suất.

Vậy pi của A cho trước s là phân bố xác suất.

Được rồi.

Và vì vậy đối với hầu hết các ví dụ trong khóa học này, đây sẽ là một phân bố phân loại.

Vì vậy, một cái gì đó trông như thế này, phải không?

Vì vậy, đây là hành động của bạn trong các trạng thái nhất định.

Đây có thể là hành động một, hành động hai, hành động ba, hành động bốn.

Và đó chỉ là một số xác suất để thực hiện hành động đó từ trạng thái đó.

Được rồi.

Vậy đó là lúc bạn có những trạng thái hay hành động rời rạc.

Nhưng cũng có trường hợp bạn có thể phải thực hiện các hành động liên tục.

Phải?

Vì vậy, trong trường hợp đó, bạn có thể có một cái gì đó như thế này.

Vậy pi của A cho trước s bằng một trên căn bậc hai của ba pi, bình phương bằng nhau.

Vì vậy, điều này sẽ là bình thường.

E nhân trừ một nửa và nói, tôi không biết, chúng ta đang nói bình phương và sau đó là s trừ mu bình phương.

Phải?

Vì vậy, với một số trạng thái s, chúng tôi xác định xác suất của một số hành động trên đường thực là phân phối này.

Được rồi.

Vì vậy, điều tiếp theo chúng tôi muốn xác định là xác suất chuyển trạng thái.

Chúng tôi cũng gọi môi trường là động lực.

Vì vậy, động lực môi trường.

Nó được đại diện bởi một quá trình quyết định Markov.

Vì vậy, quá trình ra quyết định Markov, mà chúng tôi viết tắt bằng các chữ cái mdp.

Được rồi.

Và số lượng, số lượng cụ thể mà chúng tôi quan tâm ở đây để mô tả môi trường

động lực học là xác suất chuyển trạng thái.

Vì vậy, xác suất chuyển trạng thái.

Và chúng ta sẽ sớm kết hợp những thứ này lại với nhau.

Vì thế đừng lo lắng.

Vào một loại hình ảnh lớn của quan điểm.

Bây giờ tôi chỉ đang xác định tất cả các phần.

Vì vậy, xác suất chuyển trạng thái.

Đó là xác suất để chúng ta đến một trạng thái nào đó, một trạng thái tiếp theo nào đó, s(t+1).

Chúng ta nhận được phần thưởng r(t+1).

Và điều này được cho là chúng ta đang ở một trạng thái s nào đó của t.

Và chúng ta đã thực hiện một số hành động trong trạng thái đó, a of t.

Được rồi.

Và thường thì chúng ta không viết thời gian trên biển.

Chúng ta chỉ nói p của s nguyên tố và r cho s và a, viết ra sẽ ngắn hơn nhiều.

Được rồi.

Vậy điều này cho chúng ta biết điều gì khi chỉ nhìn vào nó?

Chúng ta có thể thấy gì?

Chỉ từ những gì chúng tôi có trên trang cho đến nay.

Vì vậy, trước tiên chúng ta có thể thấy rằng trạng thái tiếp theo và phần thưởng chúng ta nhận được ở trạng thái đó phụ thuộc

duy nhất ở trạng thái trước đó và hành động mà chúng ta đã thực hiện ở trạng thái đó.

Được rồi.

Vì vậy, điều đó có thể gây ngạc nhiên nếu bạn nghĩ về nó.

Vì vậy, nơi bạn đến và phần thưởng bạn nhận được không phụ thuộc vào mọi thứ bạn đã từng làm

xong.

Nó chỉ phụ thuộc vào vị trí của bạn trong bước thời gian cuối cùng.

Và những gì bạn đã làm ở đó.

Được rồi.

Nó giải thích thuật ngữ đánh dấu xuất phát từ đâu.

Vì vậy, đánh dấu.

Vì vậy, nếu bạn quen thuộc với các mô hình đánh dấu, điều này có thể phức tạp hơn một chút

hơn những gì bạn thường thấy.

Nhưng một quá trình đánh dấu.

Vì vậy, nếu chúng tôi không có hành động và phần thưởng, chúng tôi chỉ xem xét một số hệ thống có trạng thái

và chúng tôi muốn biết các bang đã phát triển quá trình đánh dấu đó như thế nào.

Vì vậy, chúng tôi muốn nói một quy trình đánh dấu không có đầu vào kiểm soát.

Vì vậy, quy trình đánh dấu ví dụ không có đầu vào điều khiển sẽ được biểu thị bằng.

Vậy nó chỉ là P(s) T cộng với 1 s đã cho của T. Được rồi.

Vì vậy, chúng tôi loại bỏ tất cả phần thưởng và hành động.

Và chúng ta nói trạng thái mà chúng ta đạt tới tiếp theo chỉ phụ thuộc vào trạng thái mà chúng ta đã ở trước đó.

Được rồi.

Và một số ví dụ về điều này là gì?

Vì vậy, chúng tôi làm điều này trong rất nhiều khóa học của tôi.

Nhưng trong trường hợp bạn chưa từng thấy điều này trước đây, một số ví dụ là biến động giá cổ phiếu.

Được rồi.

Đó là một ví dụ và một NLP.

Chúng tôi có các mô hình ngôn ngữ.

Vì vậy, bạn có thể xây dựng mô hình ngôn ngữ từ bản phân phối như thế này trong quá trình đánh dấu.

Và rõ ràng đây là một điểm hay để đề cập rằng khi bạn nghĩ về một mô hình ngôn ngữ,

điều đó cho thấy rõ rằng đây chỉ là một mô hình.

Chúng ta biết rằng khi chúng ta viết ra các từ, khi chúng ta nói các từ, từ tiếp theo sẽ không

chỉ phụ thuộc vào từ trước đó.

Điều đó không thực tế khi chúng ta nghĩ về ngôn ngữ.

Như bạn đã biết từ trạng thái gần đây nhất của máy biến áp lớn và mô hình ngôn ngữ lớn,

đúng.

Chúng chỉ có tác dụng vì chúng ta không đưa ra giả định này.

Trên thực tế, đây chính là thứ mà họ gọi là cửa sổ ngữ cảnh.

Vì vậy, cửa sổ ngữ cảnh là kích thước của tất cả đầu vào mà chúng ta có thể có để dự đoán từ tiếp theo

hoặc mã thông báo trong một chuỗi các từ và mã thông báo.

Được rồi.

Nhưng mặc dù đây là một mô hình nhưng nó vẫn hoạt động khá tốt.

Được rồi.

Và sau đó là thuật ngữ khác ở đây, quá trình quyết định đánh dấu.

Vì vậy, chúng tôi biết quá trình đánh dấu là gì.

Và phần quyết định về cơ bản đề cập đến việc có đầu vào điều khiển.

Có một hành động liên quan đến quá trình này trong xác suất chuyển trạng thái.

Được rồi.

Vì vậy, trong trường hợp bạn tò mò, mọi người sẽ hỏi tôi những ví dụ.

Vì vậy, hãy nghĩ về một số ví dụ về MDP.

Vì vậy, ví dụ là một mê cung hoặc một thế giới lưới.

Được rồi.

Vì vậy, hãy nghĩ về một cái gì đó như thế này.

Và mỗi tiểu bang là một vị trí trên bảng.

Vậy là robot của bạn đã ở đây.

Và các hành động là nói đi lên hoặc đi sang phải, v.v.

Và phần thưởng là con số bạn nhận được khi đến một trạng thái cụ thể.

Vì vậy, giả sử bạn được cộng một nếu bạn đến đây trừ một nếu bạn đến đây.

Được rồi.

Vì vậy, như ví dụ.

Và vì vậy bạn có thể thắc mắc, tại sao điều này lại mang tính xác suất?

Và câu trả lời là, đối với trường hợp đơn giản này, nó rõ ràng không mang tính xác suất như tôi đã làm.

mô tả nó cho đến nay.

Nhưng trong thế giới thực, mọi thứ cũng có thể mang tính xác suất vì bạn chưa đo lường được thứ gì đó

một cách chính xác hoặc vì môi trường thực sự mang tính xác suất.

Vì vậy, kết quả của một điều gì đó thực sự phụ thuộc vào việc tung đồng xu.

Được rồi.

Vì vậy, một ví dụ về cách chúng tôi có thể làm cho thế giới lưới này có xác suất là giả sử đại diện của bạn quyết định

để di chuyển sang trái, nhưng thay vào đó, trên thực tế, nó lại di chuyển lên hoặc xuống.

Chúng ta thường gọi đó là thế giới lưới gió, phải không?

Trời có gió.

Vì vậy, hướng bạn cố gắng đi không phải là hướng bạn thực sự sẽ đi.

Thế giới lưới gió lộng gió.

Được rồi.

Nó có thể mang tính xác suất, nhưng hãy lưu ý rằng phần thưởng vẫn mang tính quyết định, phải không?

Vì vậy, khi bạn đến trạng thái này, bạn luôn nhận được điểm cộng.

Vì vậy, trong trường hợp này, mô hình sẽ giảm xuống P của S prime với S và A.

Đúng không?

Vì vậy, đó là một sự phân bổ cho chúng ta biết chúng ta sẽ đi đến đâu, biết chúng ta đã ở đâu và hành động gì

chúng tôi đã làm.

Và sau đó chúng tôi sẽ thưởng một chức năng khen thưởng.

Chúng ta có thể gọi nó là R của S prime.

Và vì vậy điều này mang tính quyết định vì khi chúng ta hạ cánh ở trạng thái S prime, phần thưởng sẽ được xác định.

Được rồi.

Vì vậy tôi sẽ chỉ nói rằng đây là một mô hình đơn giản hơn mà chúng ta có thể sử dụng.

Được rồi.

Nhưng mô hình đầy đủ và cách thực hiện tất cả các công thức này là chuyển đổi trạng thái đầy đủ

xác suất trong đó R cũng có xác suất.

Được rồi.

Vì vậy, một ví dụ khác mà chúng tôi thực sự sẽ làm việc là bạn có một bản nhạc và

một chiếc xe đẩy và trên hết, bạn có một cái cột gắn vào xe đẩy có thể nghiêng sang trái hoặc

đúng.

Và mục tiêu của bạn là điều chỉnh vị trí của chiếc xe đẩy này sang trái hoặc phải sao cho cây cột vẫn ở nguyên vị trí

lên.

Được rồi.

Đó là môi trường cột xe đẩy.

Giống như M-nist của học tăng cường.

Vì vậy, nếu trước đây bạn đã từng học máy thường xuyên thì bạn đã quen làm việc với M-nist.

Đó là một tập dữ liệu khá đơn giản dành cho máy học mà mọi người sử dụng để kiểm tra xem liệu

mô hình của họ có hoạt động hay không.

Và cột xe đẩy cũng tương tự như vậy đối với việc học tăng cường.

Được rồi.

Và trong trường hợp này, các trạng thái là gì?

Vì vậy, các bang có một số lựa chọn, phải không?

Bạn có thể nói, đây là điểm 0 và sau đó bạn có khoảng cách từ điểm 0

chỉ vào chiếc xe đẩy cũng có góc của cột phải không?

Vì vậy, theta.

Và do đó, trạng thái của điều này là D. Tôi sẽ đánh giá nó rõ ràng hơn.

Sắp hết chỗ rồi.

Dấu chấm D và D này.

Vì vậy, đó sẽ là đạo hàm theo thời gian hoặc tốc độ của xe và sau đó là theta và sau đó là theta

dấu chấm, đó sẽ là tốc độ góc của xe hoặc cột.

Được rồi.

Vì vậy, đó sẽ là trạng thái trong trường hợp này.

Và như đã đề cập, hành động là rời rạc.

Vì vậy, nó là trái hoặc phải.

Và vì vậy hãy lưu ý rằng đối với cái này, trạng thái là liên tục.

Đó là một vectơ trong R4.

Được rồi.

Được rồi.

Nói cách khác, đây là một không gian trạng thái có kích thước vô hạn.

Được rồi, chúng ta hãy chuyển sang trang tiếp theo.

Hãy làm một ví dụ khác.

Vì vậy, một ví dụ khác về MDP có thể là tích, tích, toe.

Được rồi.

Vì vậy, trong trường hợp này, chúng ta có thể thấy xác suất phát huy tác dụng ở đâu.

Vì vậy trạng thái là trạng thái của bảng, trong đó x và o là hành động ở đó

bạn có thể đặt x hoặc o.

Phần thưởng là, hầu hết thời gian của trò chơi, nó chẳng là gì cả.

Và sau đó bạn nói rằng bạn được cộng một khi bạn thắng thua hoặc được cộng một khi bạn thắng và nói

trừ một nếu bạn thua hoặc bằng 0 nếu bạn thua.

Nhưng lưu ý rằng đó là xác suất vì bạn không biết đối thủ của mình sẽ làm gì

để làm.

Bạn chỉ có thể kiểm soát những gì bạn làm.

Vì vậy, lần tới đã đến lúc bạn phải đưa ra quyết định mà chúng tôi cho là quyết định tiếp theo

trạng thái, bạn phải đoán xem đối thủ của bạn có thể làm gì.

Được rồi.

Vì thế nó chỉ mang tính xác suất.

Không có gì đảm bảo rằng đối thủ của bạn sẽ thực hiện một động thái cụ thể.

Được rồi.

Vậy là xong các ví dụ.

Nhưng tôi muốn kết thúc bằng một số điểm chính ở đây.

Vì vậy, điểm mấu chốt.

Đây chỉ là một mô hình như đã đề cập về môi trường.

Và như tôi đã đưa ra một số ví dụ trước đó, giả định Markov, giả định rằng những gì

bạn thấy tiếp theo chỉ phụ thuộc vào những gì bạn thấy bây giờ. Không nhất thiết phải thực tế nhưng nó hoạt động.

Và cũng là điểm mấu chốt.

Chúng ta thường không biết xác suất chuyển trạng thái.

Vì vậy, điều này tôi chưa từng đề cập trước đây.

Nhưng đó là một điều quan trọng cần biết.

Tôi luôn vẽ quá nhiều dấu phẩy.

Và một.

Được rồi.

Vì vậy, chúng tôi không biết xác suất này.

Và điều đó có ý nghĩa, phải không?

Vì vậy, nếu bạn đang chơi trên thị trường chứng khoán, làm sao bạn biết được trạng thái tiếp theo sẽ diễn ra như thế nào?

được không?

Và như bạn sẽ thấy, giải pháp cho vấn đề đó là ước tính.

Được rồi.

Vì vậy, bây giờ chúng ta đã xác định được hai đại lượng này, chính sách và xác suất chuyển đổi trạng thái.

Chúng có vẻ ngẫu nhiên nhưng bây giờ chúng ta sẽ ghép chúng lại với nhau.

Vì vậy, chúng ta sẽ có sơ đồ hệ thống RL, sơ đồ này mô tả ở mức độ cao cách thức

hoạt động học tập củng cố.

Vì vậy, chúng tôi có đại lý.

Và sau đó chúng ta có môi trường.

Và nó giống như một ngọn núi trên cây, một loại môi trường nào đó.

Được rồi.

Và đại lý được đặc trưng bởi chính sách này, phải không?

Vì vậy, nó nhìn thấy một số trạng thái.

Và từ đó tôi đã viết sai.

Và từ trạng thái đó nó quyết định hành động cần làm.

Được rồi.

Trong khi đó môi trường được đặc trưng bởi xác suất chuyển trạng thái.

Vì vậy bạn thực hiện hành động này.

Và bạn đã ở trong một trạng thái nào đó.

Và điều này đưa bạn đến trạng thái tiếp theo.

Và nó phun ra một số phần thưởng.

Được rồi.

Vậy thế nào là cơ quan, cơ quan, nhà nước nào đó.

Và nó cũng là một phần thưởng.

Được rồi.

Nhưng ngoài ra, chúng ta phải tách trạng thái tiếp theo khỏi trạng thái hiện tại.

Vậy cơ quan, thực trạng hiện nay.

Và những điều này đi cùng nhau, phải không?

Vì vậy, nó nhìn thấy trạng thái hiện tại giống như hành động a.

Và sau đó môi trường sẽ đưa ra trạng thái tiếp theo là trạng thái nguyên tố và phần thưởng r.

Được rồi.

Và do đó, nó chỉ tạo ra kẽ hở này cho đến khi bạn đạt đến trạng thái cuối, tức là

sự kết thúc của một tập phim.

Nhân tiện, đó là một thuật ngữ khác dành cho bạn, trạng thái cuối.

Tôi sẽ không viết nó ra mà chỉ ghi nhớ nó.

Được rồi.

Vì vậy bây giờ chúng ta sẽ nói về lợi nhuận.

Vì vậy lợi nhuận giúp chúng ta mô tả chính xác hơn mục tiêu của đại lý.

Được rồi.

Vì vậy, để chính xác hơn, chính xác hơn.

Đại lý muốn tối đa hóa phần thưởng trong tương lai.

Được rồi.

Tất cả các phần thưởng trong tương lai, bởi vì phần thưởng hiện tại và trước đó, chúng ta không thể làm được gì

làm để thay đổi những điều đó.

Chúng tôi vừa có được chúng.

Vì vậy, đó là những gì nó được.

Và trong tương lai, chúng tôi muốn thực hiện những hành động tốt nhất để tối đa hóa phần thưởng mà

chúng tôi nhận được.

Và vì vậy chúng tôi gọi số tiền hoàn trả là tổng số phần thưởng trong tương lai.

Được rồi.

Vậy return là g(t).

Và số tiền này bằng với phần thưởng ở bước thời gian tiếp theo, r của t cộng một cộng r của t cộng

hai.

Và nói đến r của t.

Vậy bước thời gian t, t lớn là lúc ta đạt đến trạng thái cuối.

Bây giờ bạn có thể hỏi, điều gì sẽ xảy ra nếu tập phim tiếp tục kéo dài mãi mãi?

Nó không kết thúc.

Và trong trường hợp đó, phần thưởng sẽ là vô hạn.

Vậy làm thế nào để chúng ta mô tả được ý nghĩa của việc tối đa hóa phần thưởng trong tương lai nếu mỗi lần

chúng ta có được vô cùng?

Và do đó có khái niệm về lợi tức chiết khấu.

Được rồi.

Và đó là g(t) bằng r(t+1+lambda).

Vì vậy, đây là gamma của chúng tôi.

Và đây là siêu tham số mà chúng ta có thể chọn.

Nó thường gần bằng một.

Vì vậy, giống như 0,99, 0,98, r(t+2+gamma bình phương, r(t+3).

Vì vậy, bạn có được mô hình, phải không?

Vì vậy chỉ số thời gian tăng lên.

Và khi đó sức mạnh của gamma cũng tăng lên.

Và khi chúng ta đến bước thời gian cuối cùng, t lớn, gamma sẽ là t lớn trừ t nhỏ trừ

một.

Bạn có thể tự mình kiểm tra điều đó, r của t.

Được rồi.

Vì vậy, bạn có thể nghĩ về chiết khấu giống như những gì bạn thấy trong tài chính, phải không?

Vì vậy, có khái niệm về giá trị hiện tại ròng mà bạn muốn biết giá trị là gì

của điều gì đó ngày hôm nay, vì chúng ta sẽ nhận được 100 đô la mỗi tháng kể từ bây giờ cho đến

10 năm sau.

Vì vậy, nó không chỉ là 100 lần 10 năm.

Đó là tỷ lệ chiết khấu gấp 100 lần tùy thuộc vào khoảng cách trong tương lai.

Được rồi.

Chúng ta hãy giải quyết hai khái niệm như lạm phát và lãi suất, v.v.

Được rồi.

Vì vậy, điều đó làm cho tiền ít có giá trị hơn trong tương lai.

Được rồi.

Vì vậy chúng ta hãy chuyển sang trang tiếp theo.

Được rồi.

Vì vậy bây giờ chúng ta sẽ nói về các hàm giá trị và phương trình Bellman.

Vì vậy, các hàm giá trị và phương trình Bellman.

Nó thực sự không quá quan trọng đối với cách tôi sẽ phát triển các phương pháp giải pháp

cho khóa học này

Nhưng ý tôi là cụ thể là phương trình Bellman, nhưng bạn cần phải biết về giá trị

chức năng.

Nhưng nhìn vào phương trình Bellman, mặc dù chúng ta sẽ không sử dụng nó, chắc chắn sẽ có ích

chúng ta thấy đi nhìn lại những khuôn mẫu giống nhau trong các phương trình.

Được rồi.

Thế bạn nghe thấy gì thế này?

Vì vậy, sự trở lại thực sự là xác suất.

Vì vậy, tôi đã nói rằng chúng tôi muốn tối đa hóa phần thưởng trong tương lai, tiền lãi, nhưng đó chỉ là xác suất.

Vậy làm thế nào để chúng ta tối đa hóa một thứ mà chúng ta không thực sự biết giá trị của nó sẽ là bao nhiêu?

Chúng tôi không thể tính toán nó.

Và câu trả lời là chúng ta sử dụng thay vì chính return, chúng ta sử dụng giá trị mong đợi

của sự trở lại.

Được rồi.

Vì vậy, với một số chính sách, nếu chúng ta tuân theo chính sách này, chúng ta muốn biết.

Đó là lý do tại sao chúng ta có nó được ký hiệu là pi.

Chúng ta muốn biết số tiền lãi mà tôi sẽ nhận được khi tham gia là bao nhiêu.

Bang ít hơn một chút vào thời điểm này.

Vì vậy, đó là hàm giá trị.

Cụ thể hơn, đây là hàm giá trị trạng thái.

Được rồi.

Và gần đây có người hỏi tôi rằng tại sao điều này lại có xác suất?

Nếu phần thưởng được xác định bởi trạng thái bạn kết thúc.

Và câu trả lời là cả sự chuyển đổi trạng thái và hành động đều là ngẫu nhiên.

Vì vậy, xác suất để tôi kết thúc ở trạng thái nguyên tố nào đó là xác suất tuân theo

về trạng thái s trước đó và hành động a mà tôi đã thực hiện.

Vì vậy, chúng ta không biết trước quỹ đạo của các quốc gia.

Vì vậy, chúng tôi không biết quỹ đạo của phần thưởng theo thời gian.

Vì vậy, chúng ta chỉ cần nhìn vào mức trung bình, đó là giá trị mong đợi.

Được rồi.

Và vì vậy tôi sẽ bỏ qua phần lớn phần toán ở đây, nhưng bạn có thể xem các tài nguyên khác

nếu bạn muốn tìm hiểu thêm.

Nhưng việc mở rộng biểu thức này, nếu chúng ta làm như vậy, sẽ cho chúng ta cái mà chúng ta gọi là phương trình Bellman.

Vậy phương trình Bellman là thế này.

Vì vậy, nó cũng giống như vậy ở bên trái.

Nhưng ở bên phải, đó là giá trị mong đợi của phần thưởng tiếp theo.

Cộng gamma nhân V của s của t cộng 1.

Được rồi.

Vì vậy hàm giá trị ở trạng thái tiếp theo, với điều kiện s(t) bằng s.

Được rồi.

Vậy tại sao điều này lại có ý nghĩa?

Tại sao điều này lại tốt đẹp?

Và lý do tại sao nó tốt là vì nó làm cho phương trình có tính đệ quy.

Vậy chúng ta có V ở bên trái và chúng ta có V ở bên phải.

Nói cách khác, V phụ thuộc vào chính nó, điều này cho chúng ta một phương trình mà chúng ta cũng có thể giải được.

Được rồi.

Vì vậy, nó là đệ quy.

V phụ thuộc vào V.

Và do đó, dựa trên trực giác đằng sau điều này, bạn sẽ nhận thấy rằng cách chúng ta xác định lợi nhuận,

đó là r của t cộng 1 cộng gamma r của t cộng 2.

Rất tiếc, dấu ngoặc phụ cộng với gamma r của t cộng 2 và gamma bình phương, v.v.

Được rồi.

Bạn sẽ nhận thấy rằng kết quả trả về thực sự là đệ quy.

Vậy g(t) bằng r(t+1).

Và bạn có thể tự mình kiểm tra điều này nếu bạn không tin tôi.

G của t cộng 1.

Được rồi.

Vì vậy, tôi cảm thấy việc chú ý đến mô hình này sẽ giúp phương trình Bellman trở nên có ý nghĩa.

Sự trở lại là đệ quy.

Do đó, giá trị kỳ vọng của kết quả trả về cũng có tính đệ quy.

Vậy đó là phương trình Bellman.

Và chúng ta có thể không cần điều này, nhưng một lần nữa, việc xem xét các khuôn mẫu xuất hiện sẽ rất hữu ích.

Chúng ta có thể mở rộng giá trị kỳ vọng này.

Vậy làm thế nào để bạn thực sự tính toán được giá trị kỳ vọng?

Về cơ bản, nó là thứ nằm trong giá trị kỳ vọng được tính theo xác suất của chúng.

Vậy V của s, giá trị này bằng tổng của tất cả các hành động, một số trạng thái tổng thể, trạng thái tiếp theo, một số

phần thưởng tổng thể.

Và bên trong nó sẽ là pi của s cho trước, p của s nguyên tố và r cho trước s và a.

Và khi đó số lượng thực tế sẽ là r cộng gamma V của s nguyên tố.

Được rồi.

Vậy đó là phương trình Bellman.

Và bây giờ tôi muốn nói về một đại lượng khác, tương tự.

Nó được gọi là giá trị hành động.

Và một lần nữa, đây chỉ là những con số mà chúng tôi thực sự đang cho bạn biết nhiều về lý do tại sao chúng tôi

giới thiệu họ bây giờ

Nhưng bạn sẽ thấy trong các bài giảng tiếp theo, khi chúng ta xem xét các phương pháp giải, những điều này diễn ra như thế nào

được sử dụng.

Vì vậy giá trị hành động, chúng ta sử dụng chữ q.

Đôi khi chúng tôi gọi đây là bảng q.

Vậy q pi của s và a.

Giá trị này bằng với giá trị mong đợi của một lần nữa, lợi nhuận.

Nhưng bây giờ bạn đang ở trạng thái s và bạn đã thực hiện hành động a ở trạng thái đó.

Được rồi.

Và một lần nữa, chúng ta có số tiền tương tự như trên, nhưng lần này chúng ta không tính tổng trên a bởi vì

a được đưa ra.

Vậy bây giờ nó chỉ là s nguyên tố r và pi của s cho trước, p của s nguyên tố, số nguyên tố r đã cho này

s và a.

Và một lần nữa, chúng ta có r cộng gamma, p pi s.

Được rồi.

Và vì vậy bạn có thể thắc mắc, tại sao lại có q ở một bên và v ở bên kia?

Đây là điều mà bạn sẽ tìm hiểu thêm về cách xử lý nếu bạn nhận được sự gia cố đầy đủ.

khóa học.

Nhưng về cơ bản, v sẽ là tổng của tất cả.

Vâng, chúng tôi không cần điều này ở đây.

Đây không phải ở đây.

Đi vào đây.

Vì vậy, tổng hợp của tất cả các hành động.

Một số nguyên tố, hành động tiếp theo, một số nguyên tố.

Vì vậy, hành động tiếp theo ở trạng thái tiếp theo.

Và q của s nguyên tố, một số nguyên tố.

Được rồi.

Vậy đây sẽ là v pi của s nguyên tố.

Được rồi.

Chúng tôi chỉ lấy giá trị mong đợi.

Nhìn chung, những hành động chúng ta có thể đã làm được.