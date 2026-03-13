# 1 -Thuật ngữ học tăng cường được dịch

---

Được rồi, trong video này chúng ta sẽ ôn lại cách học tăng cường từ đầu

cho đến QLearning.

Vì vậy tôi muốn nhấn mạnh một vài điều.

Vì vậy, trước hết, đây là một đánh giá rất, rất nhanh.

Vì vậy, bạn sẽ thấy rằng trong khóa học này, chúng tôi có phần nền tảng, đây cũng là phần ôn tập

về các khái niệm giống nhau, ngoại trừ việc nó đi sâu vào chi tiết hơn một chút.

Và điều đó dành cho những bạn thực sự không có điều kiện tiên quyết cho khóa học này, và

bạn muốn thử bắt đầu lại hoàn toàn từ đầu.

Vì vậy, phần này chủ yếu dành cho những người đã biết về việc ôn tập học tăng cường

về học tập tăng cường và xây dựng động lực cho các chủ đề của khóa học này.

Vì vậy, nếu bạn muốn xem xét thêm một chút, hãy chuyển đến phần nền và thực hiện một chút

nhiều hơn một chút.

Nhưng bạn cũng sẽ lưu ý rằng tôi có một bài giảng ở cuối phần đó, trong đó đề cập đến

thậm chí điều đó vẫn chưa đủ để thực sự hiểu được việc học tăng cường.

Vì vậy, nếu bạn thực sự muốn hiểu về học tập tăng cường, hãy thực sự có cả một khóa học về

đó.

Được rồi, tôi muốn cung cấp cho bạn cái nhìn toàn cảnh về cách xem ba cách này

học tập củng cố.

Vì vậy, chúng tôi có toàn bộ khóa học, hiện tại nó dài khoảng 20 giờ.

Vậy là 20 giờ.

Và chúng ta có phần nền tảng của khóa học này.

Vì vậy, nền, bút bị lag, nền, và thế là dài hai giờ.

Được rồi.

Và sau đó chúng ta có bộ bài giảng này.

Vì vậy, bài đánh giá này, tôi đoán vậy, vì tôi đang thực hiện nó ngay bây giờ.

Tôi không biết nó sẽ kéo dài bao lâu, nhưng tôi đoán nó sẽ kéo dài dưới một giờ, dưới

một giờ.

Được rồi.

Bạn thấy đấy, bây giờ chúng ta đang áp dụng tất cả các khái niệm này từ 20 giờ và làm ít hơn thế gấp 10 lần.

Vì vậy, hai giờ và sau đó làm ít hơn 50%, tức là chưa đến một giờ.

Được rồi, điều đó sẽ giúp bạn hiểu được mức độ chi tiết mà chúng tôi sắp đề cập.

Được rồi, rõ ràng là nếu giảm từ 20 giờ xuống còn chưa đầy một giờ, bạn sẽ không

có được càng nhiều chi tiết và hiểu biết càng tốt nếu bạn đã trải qua

toàn bộ quá trình 20 giờ.

Được rồi.

Được rồi, vì vậy hãy giữ những mong đợi của bạn thực tế và ghi nhớ rằng bạn có thể cần nhiều hơn thế.

xem xét sau khi đi qua phần này.

Được rồi.

Và theo cách tôi đã lên kế hoạch cho đến nay, tôi nghĩ chúng ta sẽ làm gì.

Bài giảng này sẽ được chia thành hai phần.

Vì vậy, phần một sẽ xác định các thuật ngữ và số lượng.

Vì vậy, hãy xác định các điều khoản và số lượng.

Và sau đó phần hai sẽ là các phương pháp giải.

Được rồi.

Được rồi, như đã nói, tôi muốn tuyên bố từ chối trách nhiệm về việc học tăng cường.

Vì vậy, mặc dù học tăng cường được coi là học máy nhưng nó không giống như học truyền thống

học máy nơi chúng tôi có đầu vào và mục tiêu giống như trường hợp được giám sát, cũng như không chỉ

đầu vào cho trường hợp không được giám sát mà chúng tôi đưa vào mô hình tham số.

Được rồi.

Không giống như ML truyền thống, nơi chúng tôi có đầu vào và mục tiêu, được giám sát hoặc chỉ là đầu vào

bởi chính họ, không được giám sát.

Được rồi.

Vì vậy, chúng tôi không thực sự cố gắng tìm hiểu một số mô hình tham số.

Được rồi, người phụ trách công việc đó.

Nơi chúng tôi có đầu vào ở đây.

Và sau đó chúng ta có kết quả đầu ra ở đây.

Và sau đó chúng ta gặp một sự mất mát khi đó là khoảng cách nào đó giữa đầu ra và mục tiêu.

Vì vậy, chúng tôi không làm điều này.

Vì vậy, trên thực tế, điều này sẽ trở thành một phần của việc học tăng cường.

Nhưng bản thân điều này, mô hình này nơi chúng tôi đang đào tạo một số tham số hoặc trọng số đã cho

một số dữ liệu đầu vào, cố gắng khớp với một số mẫu, đó là học máy truyền thống.

Học tăng cường không giống như vậy.

Được rồi.

Vì vậy, hãy loại bỏ ý tưởng này ra khỏi đầu bạn nếu đây là cách bạn đang nghĩ rằng học tăng cường

có thể là vậy.

Vì vậy, nó rất khác với việc học có giám sát và không giám sát.

Vì vậy, thay vào đó, bạn nên nghĩ như thế nào thì RL chỉ là một mô hình xác suất, xác suất

mô hình.

Và ngôn ngữ của việc học tăng cường là xác suất.

Vì vậy, hy vọng bạn giỏi xác suất.

Được rồi.

Chúng ta cần bắt đầu một trang mới.

Được rồi.

Được rồi.

Vì vậy, bây giờ chúng ta hãy chuyển sang một số điều khoản.

Được rồi.

Vì vậy, thuật ngữ đầu tiên chúng ta sẽ nói đến là tác nhân và môi trường.

Được rồi.

Và vì vậy tôi nghĩ cách tốt nhất để hiểu tác nhân và môi trường là thông qua các ví dụ.

Vì vậy, ví dụ, một bot đang cố gắng giải quyết mê cung.

Được rồi.

Vì vậy, trong trường hợp này, đây là tác nhân và đây là môi trường.

Được rồi.

Ví dụ, một chương trình chơi trò chơi điện tử.

Được rồi.

Vậy đây là tác nhân và đây là môi trường.

Robot vật lý học cách đi bộ.

Được rồi.

Trong trường hợp này, robot hoặc chương trình điều khiển robot là tác nhân và thế giới.

Là môi trường.

Vì vậy, môi trường thực tế xung quanh robot hoặc bạn có thể nghĩ về chính robot, nó nằm ở vị trí

bên ngoài chương trình máy tính đang chạy robot.

Đó cũng là một phần của môi trường.

Vâng, môi trường chỉ là những thứ xung quanh tác nhân mà bạn mã hóa.

Thế giới.

Được rồi.

Được rồi, đây là hai phần đầu tiên chúng ta tìm hiểu về tác nhân và môi trường.

Bây giờ chúng ta có một thuật ngữ khác, tập phim.

Vậy một tập phim là gì?

Vì vậy, tôi sẽ xem xét đây là một vòng tương tác giữa các tác nhân và môi trường.

Được rồi, một lần nữa, tốt hơn là bạn chỉ nên nghĩ ra một số ví dụ.

Vậy hãy mô tả điều này.

Vì vậy, ví dụ: nếu bạn đang chơi trò chơi điện tử, đó có thể là một cấp độ của trò chơi điện tử.

Một cấp độ của trò chơi điện tử.

Và tập phim diễn ra từ khi bạn bắt đầu cấp độ cho đến khi bạn hoàn thành cấp độ đó,

bạn hoàn thành cấp độ hoặc bạn sẽ thua.

Được rồi, nhân vật của bạn chết.

Một ví dụ khác là một trận đấu cờ vua.

Thế là một trận cờ vua.

Vậy hoặc là bạn thua hoặc bạn thắng, nhưng từ đầu trận đấu đến cuối trận đấu đó,

đó là một tập phim.

Được rồi, trên thực tế, bạn có thể xác định tập phim theo ý muốn.

Vì vậy, ví dụ, nếu bạn đang nhìn vào thị trường chứng khoán, bạn có thể xem xét một năm, một

tập hoặc một tuần, một tập.

Và một số khái niệm chính ở đây.

Khái niệm chính là bạn có thể sẽ thu thập nhiều tập dữ liệu để huấn luyện

trong các đại lý của chúng tôi.

Được rồi, hãy thu thập nhiều tập dữ liệu để huấn luyện.

đại lý RL.

Và một điểm quan trọng khác là một số môi trường không mang tính sử thi.

Được rồi, vậy là chúng ta thực sự không có các tập phim một cách tự nhiên.

Vì vậy, chìa khóa.

Một số môi trường.

Một số không mang tính sử thi.

Được rồi, tức là

Họ tiếp tục mãi mãi.

Được rồi, ví dụ về thị trường chứng khoán đó.

Điều đó sẽ không kết thúc.

Được rồi.

Và một điều quan trọng nữa là bạn có thể làm cho nó thành nhiều tập, nhưng bạn có thể làm cho nó thành nhiều tập bằng cách xác định đơn giản

những gì bạn muốn dưới dạng một tập phim, như đã đề cập trước đó.

Vì vậy, bạn có thể lặp đi lặp lại dữ liệu chứng khoán trong cùng một năm để đại lý tìm hiểu

cách cư xử tối ưu trong suốt năm đó.

Và sau đó rõ ràng là bạn muốn kiểm tra đại lý đó vào năm tới để xem liệu nó có hoạt động không

dẫn đến hiệu suất tương tự.

Được rồi, ở cuối trang này, chúng ta hãy chuyển sang trang tiếp theo.

Vì vậy, một số thuật ngữ tiếp theo mà chúng tôi muốn nói đến là trạng thái, hành động và phần thưởng.

Được rồi, vậy đây là gì?

Vì vậy, trạng thái là bất cứ điều gì tác nhân quan sát được trong môi trường.

Được rồi, đó là điểm mấu chốt.

Vì vậy, bạn có thể nghĩ về các đại lý.

Đặc vụ có mắt.

Và nó có thể nhìn thấy những gì trong môi trường.

Được rồi, và đó là những gì nó sẽ sử dụng để xác định xem nó nên làm gì.

Trên thực tế, tác nhân còn có những giác quan khác.

Vì vậy, trên thực tế, nó không chỉ là những gì nó nhìn thấy.

Đó là những gì nó có thể nghe và chạm vào, v.v.

Vì vậy, bất cứ điều gì nó có thể cảm nhận được.

Vì vậy, bạn sẽ cho con người, phải không?

Chúng ta có năm giác quan, đó là vị trí, âm thanh, vân vân, vân vân.

Vì vậy, những tác nhân này sẽ có giác quan riêng và bất cứ thứ gì chúng cảm nhận được trong môi trường,

bất cứ điều gì họ đo lường hoặc quan sát, điều đó sẽ trở thành trạng thái.

Được rồi.

Và nó sẽ quan sát các trạng thái này ở mọi thời điểm trong môi trường.

Được rồi.

Vì vậy, trạng thái là bất cứ điều gì mà tác nhân quan sát được trong môi trường ở mỗi trạng thái.

Bước thời gian.

Được rồi, vậy có một giả định ngầm ở đây, đó là khi chúng ta nói các bước thời gian,

điều này ngụ ý rằng chúng ta đang xem xét một vấn đề thời gian rời rạc.

Được rồi.

Và trong RL, trường hợp này thường xảy ra.

Được rồi, trong RL, thời gian thường là rời rạc.

Được rồi, vậy chúng ta sẽ có, ví dụ, thời gian bằng một, thời gian bằng hai, thời gian bằng ba, v.v.

Vậy chúng ta không có thời gian bằng 1,5.

Và vì vậy tôi đoán hệ quả tất yếu của điều đó là có ít việc phải làm phép tính hơn.

Được rồi.

Mặc dù bạn sẽ thấy vẫn còn có phép tính, nhưng sẽ không nhiều như vậy nếu chúng ta làm việc trong thời gian liên tục.

Và hãy lưu ý rằng có những lĩnh vực khác thực hiện công việc tương tự như học tăng cường, nhưng trong thời gian liên tục.

Được rồi, một lần nữa, việc nghĩ ra các ví dụ sẽ dễ dàng nhất.

Vậy ví dụ về một trạng thái là gì?

Được rồi, ví dụ vậy.

Bảng tích tắc.

Giống như trạng thái sẽ là trạng thái của bảng, bất kể bạn quan sát thấy điều gì.

Đúng, đây là chữ X.

Đây là chữ X.

Vì vậy, đó là một trạng thái.

Và bạn sẽ nhận thấy rằng đây cũng là thời gian rời rạc bởi vì, giả sử bạn chuyển sang bước thời gian tiếp theo,

và ở bước tiếp theo, hãy nói nó trông như thế này.

Được rồi.

Vì vậy, một điều thú vị mà bạn nên nghĩ đến là đây là một bức tranh.

Đúng rồi, tôi đã vẽ một bức tranh về bảng đánh dấu thuế.

Nhưng làm thế nào bạn có thể biểu diễn trạng thái này trong máy tính?

Và trong trường hợp này, những trạng thái này là rời rạc.

Vì vậy, bạn có thể gọi trạng thái này là một trạng thái, 500, v.v., v.v.

Vì vậy, việc xác định các trạng thái này như thế nào và cách triển khai các thuật toán này là tùy thuộc vào bạn

trong một máy tính.

Vì vậy, chúng ta sẽ không nói nhiều về điều đó trong suốt các bài giảng này, hay cụ thể là bài giảng này.

Bài giảng tiếp theo sẽ xem xét chi tiết hơn một chút về cách bạn có thể thực hiện những điều này.

Nhưng đối với bài giảng này, chỉ cần suy nghĩ trong đầu, bạn sẽ biểu diễn trạng thái này trên máy tính như thế nào?

Đúng rồi, hiện tại bạn đang nhìn thấy một hình ảnh ở đây.

Nhưng hãy nghĩ xem, liệu hình ảnh có phải là cách tốt nhất để thể hiện dữ liệu này nếu bạn đang viết mã bên trong

một chiếc máy tính?

Và câu trả lời là, đối với trường hợp này là không.

Nhưng ví dụ tiếp theo thực sự là trường hợp hình ảnh phù hợp.

Ví dụ tiếp theo là ảnh chụp màn hình của trò chơi điện tử.

Được rồi, trong trường hợp này, nếu bạn đang chơi trò chơi điện tử, bạn muốn nhân viên hỗ trợ chơi trò chơi

trò chơi điện tử giống như cách chúng ta chơi trò chơi điện tử.

Chúng tôi nhìn vào màn hình.

Được rồi, điều này cũng mang đến cho bạn một số điều thú vị để suy nghĩ.

Vì vậy, để sử dụng hình ảnh, chúng ta có thể muốn áp dụng CNN, một kiến trúc deep learning

chuyên về hình ảnh làm việc.

Và một điều thú vị khác để nói đến là ảnh chụp màn hình.

Vì vậy, chúng ta có thể nói trạng thái hiện tại là ảnh chụp màn hình tại thời điểm cụ thể này.

Nhưng như bạn sẽ thấy trong khóa học này, chúng tôi không định nghĩa mọi thứ theo cách đó.

Vì vậy, trong khóa học này, hoặc tôi đoán trong DeepRL nói chung, trạng thái thực sự là bốn ảnh chụp màn hình cuối cùng.

Rất tiếc, tôi đánh vần sai ảnh chụp màn hình.

Và do đó, làm mọi thứ theo cách này sẽ mang lại cho bạn cảm giác mọi thứ đang chuyển động trên màn hình như thế nào.

Phải?

Vì vậy, nếu bạn chỉ nhìn vào một ảnh chụp màn hình, thật khó để biết mọi thứ đang chuyển động theo hướng nào.

Nhưng nếu bạn có bốn ảnh chụp màn hình, bạn sẽ dễ dàng nhìn thấy chuyển động của mọi thứ hơn.

Và một lần nữa, đây chỉ là một ví dụ về việc mặc dù trạng thái là những gì bạn quan sát được nhưng nó

cũng có trường hợp trạng thái có thể là sự tổng hợp của những thứ mà bạn quan sát và đã quan sát thấy trong

quá khứ.

Được rồi, vậy một thuật ngữ khác mà chúng ta muốn tìm hiểu là không gian trạng thái.

Vì vậy không gian trạng thái là tập hợp tất cả các trạng thái có thể có.

Và điều tôi muốn bạn suy nghĩ là phải làm gì nếu không gian trạng thái không rời rạc

hoặc có kích thước vô hạn.

Vậy phải làm gì?

Đây là một kích thước rời rạc hoặc vô hạn.

OK, vậy tại thời điểm này chúng ta cần tạo một trang mới.

Vậy là một trang mới và bây giờ chúng ta sẽ nói về các hành động.

Vì vậy, tôi đã đề cập trước đó, chúng tôi muốn nói về trạng thái, hành động và phần thưởng.

Vì vậy, bây giờ chúng tôi đang hành động.

ĐƯỢC RỒI.

Vậy hành động là gì?

Một hành động là những gì tác nhân thực hiện trong môi trường của nó.

ĐƯỢC RỒI.

Và nhân tiện, tôi sẽ sử dụng ENV như một từ viết tắt cho môi trường.

ĐƯỢC RỒI.

Vì vậy, không gian hành động, như bạn có thể đoán, là tập hợp tất cả các hành động, các hành động có thể xảy ra trong một môi trường.

ĐƯỢC RỒI.

Vì vậy, một lần nữa, để làm ví dụ, tốt nhất bạn nên nghĩ ra các ví dụ để xác định các thuật ngữ này.

Để giải mê cung, chúng ta sẽ gọi nó là A, có thể lên, xuống, trái và phải.

Một ví dụ khác là Tick-Tack-Toe.

Hành động sẽ như thế này, vì vậy bây giờ tôi đang sử dụng một chút A. Đây không phải là không gian hành động, mà là

một số hành động có thể là hai.

Đặt X ở góc trên, bên trái.

Và một điều thú vị khác cần suy nghĩ là không phải mọi hành động đều được phép.

Vì vậy, nếu bạn là người chơi X chẳng hạn, bạn không thể đặt chữ O xuống hoặc nếu góc trên bên trái

bị chiếm giữ bởi một X hoặc O khác, thế thì bạn không thể đặt bất cứ thứ gì vào đó.

Vì vậy, đôi khi một số hành động không được phép.

ĐƯỢC RỒI.

Một ví dụ khác, đây là ví dụ về nơi hành động không rời rạc.

Vì vậy, giả sử bạn đang lái một chiếc ô tô.

Và hành động có thể tăng tốc bao nhiêu.

Phải.

Vì vậy, bạn có thể có, chẳng hạn, 0,2 km một giờ bình phương.

ĐƯỢC RỒI.

Vì vậy, trong trường hợp này, không gian hành động sẽ nằm trên các số thực dương.

Tôi đoán bạn có thể có gia tốc âm đối với bạn.

Đó chỉ là phá vỡ.

Vì vậy bạn có thể nói không gian hành động đều là số thực.

Và trên thực tế, bạn có thể có một vectơ các hành động có giá trị thực.

Vì vậy, một hành động khác mà bạn có thể thực hiện, một ví dụ khác, là góc quay.

Và đây có thể là từ, đây là gì?

Vậy đây là 0.

Đây là pi trên 2.

Đây là trừ pi trên 2.

Tôi không thể.

Vâng.

Phải.

Vì vậy, bây giờ bạn có thể có một vectơ hành động.

Vì vậy, một hành động mẫu, một hành động mẫu, có thể được tăng tốc 0,2 km một giờ bình phương.

Và sau đó quay lại, nói một góc của pi trên 4.

Được rồi.

Vì vậy, bạn có thể có một vectơ giá trị thực.

ĐƯỢC RỒI.

Vậy bây giờ hãy nói về phần thưởng.

Nó chỉ mới bắt đầu ném bóng.

Vì vậy, nó thưởng một giá trị vô hướng cho tác nhân sau mỗi bước.

Vì vậy, giá trị vô hướng được trao cho tác nhân sau mỗi bước.

Vì vậy, bạn có thể nghĩ về điều này.

Và đây là cách đại lý biết nó hoạt động tốt như thế nào.

Và nó cũng cho bạn biết tại sao lĩnh vực này được gọi là học tăng cường.

Vì vậy, bạn có thể nghĩ nó giống như việc huấn luyện một con vật.

Bạn có thể nghĩ đến việc học tăng cường dưới dạng huấn luyện động vật.

Vì vậy, khi một con vật làm điều gì đó mà bạn muốn làm, bạn thưởng cho nó một món quà để củng cố nó.

hành vi.

Ví dụ: bạn đang huấn luyện một con chó, bạn muốn nó ngồi.

Nếu nó ngồi thành công thì bạn sẽ thưởng cho nó.

Nếu nó không ngồi thành công thì bạn sẽ không thưởng cho nó.

Vì vậy, bạn đang củng cố hành vi bằng cách thưởng cho nó.

Bây giờ hãy nhận ra rằng đồ ăn vặt là một điều tốt.

Vì vậy, trong thế giới thực, bạn luôn nghĩ phần thưởng là một điều tích cực.

Nhưng quan trọng là, trong học tăng cường, phần thưởng không nhất thiết phải là điều tích cực.

Nó chỉ là một con số.

ĐƯỢC RỒI.

Vì vậy chúng ta vẫn gọi nó là phần thưởng nhưng nó cũng có thể rất tệ.

Vì vậy, nếu bạn nhận được phần thưởng tiêu cực thì đó thường không phải là điều tốt.

Nhưng điều quan trọng là đại lý vẫn có thể sử dụng phần thưởng, cho dù chúng là tích cực hay tích cực.

tiêu cực để sửa đổi hành động của mình.

Và điều này đưa chúng ta đến một điểm quan trọng, đó là mục tiêu của một tác nhân.

Thế là mục tiêu, bút của tôi lại bị lag.

Mục tiêu của đặc vụ là tối đa hóa hoặc đạt được phần thưởng tối đa qua mỗi tập.