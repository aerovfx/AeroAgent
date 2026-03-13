# 3 -Cải tiến chính sách và lặp lại chính sách

---

Được rồi, trong bài giảng này chúng ta sẽ xem xét các phương pháp giải pháp cho việc học tăng cường.

Vì vậy, hãy nhắc lại những gì chúng ta đã làm cho đến nay.

Vậy là có ba phần.

Những gì tôi nói ban đầu là hai phần, nhưng tôi đã làm thành ba phần.

Vậy tôi có đang viết cái này không?

Vì vậy, phần một chỉ nhằm đấu tranh với một số điều khoản.

Phần hai sử dụng những thuật ngữ đó để xác định số lượng.

Vì vậy, ví dụ như giá trị trả về, giá trị trạng thái và giá trị hành động.

Và thứ ba, đó là bài giảng này, sẽ là các phương pháp giải.

Vậy làm thế nào để chúng ta sử dụng những đại lượng đó để thực hiện các phép tính thực tế hữu ích?

Được rồi?

Vì vậy, những gì tôi muốn làm ở định dạng này hơi khác so với những gì tôi đã làm trước đây.

Vì vậy, tôi sẽ bắt đầu bằng việc giới thiệu cho bạn thuật toán học Q.

Và khi biết rằng đó là mục tiêu, chúng tôi sẽ quay ngược lại và xây dựng nó lại từ đầu.

Được rồi?

Vì vậy, thuật toán học Q trông như thế này.

Vậy là học Q.

Được rồi?

Và vì vậy chúng ta được cung cấp đối tượng môi trường.

Thực ra bài viết của tôi không lộn xộn đến mức này.

Đó là do chảo bị lag trên iPad của tôi.

Được rồi?

Vì vậy, chúng tôi được cung cấp đối tượng môi trường này.

Nó sẽ tuân theo một số API, tương tự như API của phòng tập thể dục, đó là những gì

chúng tôi sẽ sử dụng trong mã.

Đó là lý do tại sao nó sẽ trông như thế nào.

Được rồi?

Vì vậy, sau đó chúng tôi khởi tạo bảng Q của mình.

Vì vậy, đây sẽ là giá trị ngẫu nhiên.

Chúng tôi sẽ chỉ nói ngẫu nhiên.

Được rồi?

Với mọi, với mọi s trong không gian trạng thái s và mọi hành động a trong không gian hành động a.

Được rồi?

Vì vậy, đây là một thuật toán lặp.

Vậy Q của s trong bảng a hoặc Q hoặc giá trị hành động.

Nó được khởi tạo với các số ngẫu nhiên.

Và sau đó khi chúng ta thực hiện thuật toán này, nó sẽ liên tục sửa đổi các giá trị đó

để có được giá trị đúng.

Được rồi?

Vì vậy, tiếp theo chúng ta sẽ bước vào một vòng lặp.

Vì vậy, đối với tôi trong phạm vi.

Được rồi?

Được rồi, có nhiều tập.

Vì vậy, chúng tôi sẽ đi bất kỳ tập nào mà chúng tôi quyết định.

Và nếu bạn đã từng học máy trước đây thì bạn đã thực hiện các thuật toán như độ dốc

sem, về cơ bản những gì bạn đang tìm kiếm là chuyển đổi.

Được rồi?

Vì vậy, bạn muốn một cái gì đó hội tụ.

Và bạn sẽ chọn số tập sao cho bất cứ điều gì bạn muốn hội tụ

hội tụ.

Được rồi?

Thực ra ở đây, chúng ta cũng được cung cấp số tập.

Chúng ta có thể coi nó như một đầu vào.

Được rồi?

Vì vậy, bên trong vòng lặp, bây giờ bạn có thể thấy một chút về API cho môi trường.

Vì vậy chúng tôi gọi env.reset.

Và điều đó trả về một trạng thái, đây sẽ là trạng thái ban đầu cho tập này.

Chúng tôi cũng sẽ đặt cờ xong.

Vậy đây là một biến Boolean.

Chúng tôi sẽ đặt điều này thành sai.

Được rồi?

Vì vậy, bây giờ chúng tôi chỉ chơi một tập phim.

Vì vậy, trong khi chưa hoàn thành.

Vì vậy, chúng tôi lặp lại từng bước của tập phim.

Vì vậy, bên trong vòng lặp này, chúng ta sẽ chọn một hành động.

Vậy a bằng việc chọn hành động.

Vì vậy, tôi sẽ mô tả chức năng của nó nhưng tôi sẽ mô tả ngay sau đây.

Vì vậy, nó nằm trong bảng xếp hàng và nó ở trạng thái hiện tại.

Vì vậy, như đã đề cập, dựa trên trạng thái hiện tại, chúng ta có thể nhận được một hành động mới.

Được rồi?

Vì vậy, đây là pi của s hoặc pi của một s hoặc chính sách nhất định.

Được rồi?

Và tiếp theo, bây giờ chúng ta đã có hành động, chúng ta có thể thực hiện hành động đó trong môi trường.

Được rồi?

Vì vậy, nó trông như thế này.

Vì vậy, nó sẽ trả về trạng thái tiếp theo là trạng thái nguyên tố, phần thưởng r và cờ done để thông báo

chúng tôi dù tập phim này có được thực hiện hay không.

Và hàm chúng ta gọi là env.step truyền vào hành động a.

Được rồi?

Vì vậy, trong thực tế, hiện tại chúng tôi đang trả về ba giá trị từ env.step.

Sẽ có thêm một vài giá trị liên quan đến API.

Nhiều cú pháp hơn là học tăng cường cơ bản thực tế.

Vì vậy, chúng tôi không quá tập trung vào điều đó.

Nhưng trong mã, bạn sẽ thấy nhiều giá trị hơn.

Được rồi?

Vì vậy, sau đó chúng tôi đi đến hàng đợi cập nhật.

Vì vậy, bằng cách sử dụng thông tin này, chúng tôi có thể cập nhật hàng đợi.

Và một lần nữa, tôi vẫn chưa mô tả lý do tại sao điều này lại hiệu quả, nhưng chúng tôi sẽ sớm mô tả.

Vì vậy hãy cập nhật hàng đợi bằng công thức này.

Vì vậy, trước tiên, chúng ta sẽ xác định mục tiêu.

Vậy y bằng r, mà chúng ta vừa mới đưa ra ở đây, cộng với gamma, là tỷ lệ chiết khấu của chúng ta,

nhân với giá trị tối đa của tất cả các hành động, số nguyên tố của hàng đợi s nguyên tố, số nguyên tố.

Vì vậy, chúng tôi đang sử dụng bảng hàng đợi để xác định mục tiêu này mà chúng tôi gọi là y.

Vì vậy, đây là một mục tiêu.

Và sau đó chúng ta sẽ làm một cái gì đó trông khá giống với việc giảm độ dốc hoặc độ dốc

đi lên.

Vì vậy, hãy xếp hàng s a, gán giá trị, QSA hiện có, cộng với một số tốc độ học.

Được rồi?

Vì vậy, đây là một tỷ lệ học tập eta.

Và sau đó nhân số đó với y trừ hàng đợi, S a.

Được rồi?

Nhân tiện, đại lượng này, y trừ QSA, đây được gọi là sai số TD, trong đó TD là viết tắt của

đối với sự khác biệt về thời gian.

Được rồi, sự khác biệt tạm thời.

Điều này không quá quan trọng, nhưng về sau, điều này sẽ có ý nghĩa nếu xét theo ngữ cảnh.

Được rồi?

Vì vậy, bây giờ có một điều quan trọng nhưng lại dễ quên.

Vì vậy, trong vòng lặp này, chúng tôi luôn xem xét trạng thái hiện tại để xác định trạng thái tiếp theo

hành động nên có.

Vì vậy bạn không thể quên gán trạng thái tiếp theo cho trạng thái hiện tại để tác nhân có thể

quyết định phải làm gì cho trạng thái tiếp theo.

Được rồi?

Vì vậy tôi sẽ coi điều này là quan trọng.

Vì thế bạn đừng quên nó.

Chúng ta gán S nguyên tố cho S.

Tôi đoán thay vì bằng, nó có thể là một mũi tên, nhưng không sao cả.

Cách nào cũng tốt.

Được rồi?

Vậy đó là thuật toán học hàng đợi.

Chúng tôi đang ở cuối trang này.

Vì vậy chúng ta sẽ bắt đầu một trang mới.

Và bây giờ chúng ta sẽ nói về cách chúng ta học theo hàng đợi?

Được rồi.

Vì vậy, chỉ trong một số bối cảnh, trong một khóa học tăng cường đầy đủ, trong RL đầy đủ, chúng ta sẽ làm điều này

quá trình.

Vì vậy, chúng ta sẽ chuyển từ lập trình động mà tôi sẽ gọi là DP.

Tôi sẽ không viết nó ra vì chúng ta thậm chí không sử dụng nó trong khóa học này, hoặc chúng ta

thậm chí không sử dụng nó trong phần này.

Lập trình động.

Sau đó, chúng ta chuyển từ đó sang phương pháp được gọi là phương pháp Monte Carlo.

Vì vậy, MC, Monte Carlo, và sau đó chúng ta chuyển sang các phương pháp sai phân theo thời gian, TD.

Vì vậy chúng ta vừa nói về TD trước đó.

Vì vậy, bây giờ bạn thấy nó phù hợp ở đâu trong bối cảnh.

Vì vậy, thông thường chúng ta sẽ xem xét cả ba phương pháp giải này.

Và trong khóa học tăng cường đầy đủ của tôi, mỗi phần đều có phần riêng.

Vì thế chúng không hề tầm thường.

Nhưng trong bài đánh giá rất ngắn này, tôi sẽ coi chúng như thể chúng tầm thường.

Được rồi?

Hy vọng điều đó có ý nghĩa.

Và trong phần này, điều tôi sắp làm, chỉ để nói thật ngắn gọn, là tôi sẽ bỏ qua

lập trình động hoàn toàn.

Và chúng ta sẽ đi thẳng từ Monte Carlo tới việc học về sự khác biệt theo thời gian.

Được rồi.

Vì vậy, đây là một câu hỏi quan trọng cần xem xét, được đưa ra một trạng thái, một trạng thái nhất định, làm thế nào để

chúng ta chọn hành động tốt nhất?

Làm thế nào để chọn hành động tốt nhất?

Và khẳng định của tôi là hành động tối ưu ở một trạng thái, chúng ta sẽ gọi nó là Ngôi sao, bằng

arg max trên tất cả các hành động A từ bảng Q cho trạng thái S và hành động A này.

Vì vậy, nó chỉ xem qua tất cả các giá trị khác nhau của A, với trạng thái nhất định và kết quả này sẽ trả về

hành động tối ưu.

Được rồi?

Và tại sao điều đó lại có ý nghĩa?

Vì vậy hãy nhớ rằng bảng Q thực sự là một giá trị được mong đợi.

Phải?

Vì vậy, đây là lợi nhuận kỳ vọng G của T, với điều kiện là bạn đang ở trạng thái S tại thời điểm T và bạn

cải cách hành động A tại thời điểm T. Được chứ?

Vì đây là giá trị được mong đợi hoặc không được mong đợi, nhưng chúng ta có một giá trị được mong đợi xung quanh nó, nên nó

tương lai, đó là tổng số phần thưởng trong tương lai.

Vì vậy, chúng ta đang nói xem chúng ta có thể làm hành động nào để tối đa hóa giá trị kỳ vọng của tổng

về phần thưởng trong tương lai?

Được rồi?

Và hy vọng điều đó có ý nghĩa dựa trên những gì bạn đã học được cho đến nay.

Được rồi?

Nhưng đây là một sự tinh tế mà chúng ta cũng phải xem xét.

Rất tinh tế, điều này giả định rằng chúng ta biết Q của S và A, và sau đó chúng ta tìm ra chính sách tối ưu

bánh.

Được rồi?

Giả sử chúng ta đã biết, Q sẽ gọi là Q star, chính sách tối ưu, giá trị hành động tối ưu tương ứng

đến chính sách tối ưu.

Hoặc đáp ứng chính sách tối ưu bánh sao.

Được rồi?

Và khẳng định của tôi là thuật toán học Q mà chúng ta đã xem xét trước đó cuối cùng đã dẫn chúng ta đến

Q tối ưu này và chính sách tinh tế.

Được rồi?

Vậy bây giờ có điều cần xem xét, đó có phải là vấn đề không?

Chúng ta không biết Q và bây giờ chúng ta sẽ viết lại ký tự này bằng pi.

Vì vậy, với một số miếng bánh chính sách, chúng ta không biết đó là Q. Được chứ?

Vậy làm thế nào để chúng ta tìm thấy điều đó?

Và vì vậy bạn sẽ nhận thấy rằng trong trang hoặc trang trước đó, chúng ta không có chỉ số dưới trên Q vì

điều này được giả định là sau khi chúng ta hoàn thành vòng lặp này, chúng ta sẽ có sao Q, mức tối ưu

Q. Nhưng trong quá trình này, chúng ta sẽ có một số thứ ở giữa, Q hoàn toàn ngẫu nhiên

và sau đó là tối ưu Q. Được chứ?

Vì vậy, trong khi chúng tôi tìm hiểu, trong khi tác nhân đang học, Q đang cập nhật và ngày càng tiến gần hơn

đến mức tối ưu.

Được rồi?

Nhưng câu hỏi ở đây hơi khác một chút.

Nó nói rằng với một chiếc bánh chính sách cụ thể, Q là gì?

Được rồi?

Và vì vậy chúng ta không biết điều này vì đây là giá trị được mong đợi, phải không?

Và các giá trị kỳ vọng trên phân phối, pi, chính sách và xác suất chuyển đổi trạng thái.

Vậy pi, cho trước s và p của s prime đều cho s và a, đó là môi trường, phải không?

Phân bố xác suất nào mô tả môi trường?

Và như tôi đã đề cập trước đó, chúng ta thường không biết điều này.

Vậy là bạn đang chơi một trò chơi điện tử.

Bạn không biết những trạng thái tiếp theo sẽ ra sao.

Được rồi?

Vì vậy, bạn không giống như được đưa ra điều này trong một cuốn sách hướng dẫn hay gì đó.

Bạn phải tự mình tìm ra hoặc học nó khi chơi trò chơi.

Được rồi?

Vì vậy chúng ta sẽ sử dụng một thủ thuật từ số liệu thống kê.

Khi chúng ta không biết một giá trị, chúng ta có thể ước tính nó.

Chúng ta có thể ước tính giá trị kỳ vọng bằng cách sử dụng mẫu.

Được rồi?

Vì vậy, để làm ví dụ, chúng ta có x từ một phân phối xác suất nào đó và chúng ta muốn biết kết quả mong đợi

giá trị của x.

Làm thế nào để chúng ta tính toán điều đó?

Vì vậy, chúng tôi có thể thu thập các mẫu của x.

Vì vậy, các mẫu sẽ là x1, x2, cho đến xn.

Và sau đó chúng tôi sẽ lấy giá trị trung bình của những mẫu đó như thế.

Được rồi?

Vì vậy, đó là cách chúng ta ước tính e của x, giá trị kỳ vọng của x.

Bây giờ chúng ta cũng có thể có hàm x.

Vì vậy e của g của x.

Và điều này sẽ xấp xỉ bằng việc áp dụng hàm đó cho các mẫu, tính tổng chúng

tất cả cùng nhau và chia cho n.

Được rồi?

Nói cách khác, điều này có nghĩa là bạn ước chừng giá trị kỳ vọng của mẫu

trung bình hoặc bạn ước chừng giá trị trung bình thực với giá trị trung bình mẫu.

Được rồi?

Vì vậy, nếu chúng ta muốn ước tính q, chúng ta có thể phát n tập và khi đó q pi s a xấp xỉ

bằng 1 trên n và sau đó là tổng của tất cả kết quả thu được khi bạn ở trạng thái này

và bạn đã thực hiện hành động này, cái tôi của thời gian.

Vậy tôi tăng 1 lên n.

Được rồi?

Vì vậy, có rất nhiều chỉ số ở đây, nhưng hy vọng nó có ý nghĩa.

Vì vậy, về cơ bản đối với mỗi trạng thái và hành động bạn gặp phải, bạn sẽ tính toán đâu là

trở lại khi tôi ở trạng thái và hành động đó, khi tôi ở trạng thái đó và tôi thực hiện điều đó

hành động, có nghĩa là bạn phải thực hiện một chút công việc ghi sổ trong mã.

Vì vậy, hãy tưởng tượng bạn sẽ thực hiện điều đó như thế nào.

Vì vậy, bạn đã giữ nó, vì vậy bạn phải theo dõi tất cả phần thưởng bạn nhận được và sau đó tổng hợp chúng

tất cả cùng nhau, kết hợp gamma, hệ số chiết khấu, vân vân, vân vân.

Được rồi?

Lưu ý một điều khác, đó là để có q chính xác cho tất cả các trạng thái và tất cả

hành động, bạn sẽ phải thực hiện tất cả các trạng thái và tất cả các hành động nhiều lần.

Vâng, hy vọng rất nhiều lần để bạn có thể đưa ra ước tính của mình khi chơi trò chơi.

Được rồi?

Và quá trình tìm q này, với một chính sách đã cho, chúng tôi gọi đây là đánh giá chính sách.

Vì vậy, chính sách, đánh giá chính sách.

Được rồi.

Trang tiếp theo.

Được rồi, như vậy tôi vừa nói nếu muốn đo q chính xác thì chúng ta phải thử mọi hành động ở mọi trạng thái

rất nhiều lần.

Nhưng đây là một vấn đề.

Vấn đề là chúng ta không thể chọn trạng thái nào để có thể thử tất cả các

hành động từ trạng thái đó và thu thập tất cả trạng thái.

Phải?

Vì vậy, hãy tưởng tượng rằng chúng ta đang chơi một trò chơi hắc ín hoặc bất kỳ trò chơi điện tử nào, bạn không thể chọn trạng thái nào

của trò chơi bạn muốn tham gia bất kỳ lúc nào.

Phải?

Có lẽ nếu bạn tự lập trình trò chơi thì có thể.

Nhưng nếu chúng ta đang chơi một trò chơi mà bạn nói là tải xuống trên internet thì bạn không thể làm như vậy

một thứ.

Bạn chỉ cần chơi trò chơi.

Được rồi?

Và đó cũng là cách chúng tôi muốn các đặc vụ của mình học hỏi trong cuộc sống thực.

Phải?

Chúng tôi không muốn có một số hack để vào bất kỳ trạng thái nào chúng tôi muốn, điều này là không thể trong

thế giới vật chất.

Chúng tôi chỉ muốn đại lý rút kinh nghiệm.

Chúng ta phải chơi trò chơi.

Được rồi?

Vì vậy, đây là nơi chúng ta quay lại chức năng chọn hành động mà chúng ta đã nói trước đó.

Và cụ thể là chúng ta sẽ triển khai một thuật toán gọi là epsilon tham lam.

Được rồi?

Và do đó, điều này cho phép chúng tôi thử tất cả các hành động từ mọi trạng thái mà chúng tôi gặp phải để chúng tôi nhận được nhiều

dữ liệu từ việc thực hiện tất cả những hành động này.

Phải?

Vì vậy, chắc chắn, hãy chọn hành động.

Vậy chức năng này thực sự trông như thế nào?

Đưa vào bảng xếp hàng và một trạng thái cụ thể.

Và tôi sẽ nói nếu ngẫu nhiên nhỏ hơn epsilon.

Vì vậy, con số này, rất ngẫu nhiên, chúng ta trả về số 0 và một và sau đó epsilon thường là,

vì vậy đây là siêu tham số chúng ta phải chọn nó.

Nhưng nó thường là một số nhỏ như 0,1, 0,01, v.v.

Được chứ?

Về cơ bản, đó là xác suất để chúng ta chọn một hành động ngẫu nhiên.

Vì vậy, hãy trả lại hành động ngẫu nhiên.

Được rồi?

Khác.

Ngược lại, chúng tôi chọn hành động tối ưu đã đề cập hoặc bất cứ điều gì chúng tôi tin là

hành động tối ưu hiện nay.

Như đã đề cập là arg max trên bảng xếp hàng cho trạng thái này.

Vì vậy, arg max trên QS a.

Được rồi?

Vì vậy, đó là hành động lựa chọn của chúng tôi đối với sự tham lam của epsilon.

Được rồi?

Và một điều nhỏ tôi muốn đề cập đến là vì đôi khi điều này khiến mọi người bối rối.

Vậy hãy nghĩ xem, xác suất để chọn được hành động tối ưu theo hàng đợi là bao nhiêu.

Vì vậy bạn có thể nghĩ nó chỉ là một epsilon trừ.

Bởi vì epsilon là xác suất chọn một hành động ngẫu nhiên.

Vì vậy, bạn có thể nghĩ rằng một epsilon trừ sẽ là xác suất chọn được kết quả tốt nhất

hành động, hành động tối ưu.

Vậy xác suất là epsilon mà chúng ta đến đây và xác suất một trừ epsilon mà chúng ta đi

ở đây.

Khẳng định của tôi là xác suất chọn được hành động tối ưu thực sự lớn hơn một

trừ epsilon.

Phải?

Bởi vì khi chúng ta chọn một hành động ngẫu nhiên thì chúng ta cũng vẫn có thể chọn được hành động tối ưu.

Vì vậy, nó cao hơn một trừ epsilon một chút.

Nhưng câu hỏi của tôi dành cho bạn là xác suất đó là bao nhiêu?

Được rồi.

Vì vậy bây giờ chúng ta hãy chuyển sang một khái niệm gọi là cải tiến chính sách.

Vì vậy, chúng tôi đã xem xét đánh giá chính sách.

Đó là khi chúng ta có một chính sách và muốn biết giá trị hàng đợi của chính sách đó là gì.

Nhưng bây giờ đây là một định lý cải tiến chính sách câu hỏi hơi khác, trong đó hỏi, làm thế nào

chúng ta có được chính sách tốt hơn không?

Và tất nhiên, nếu chúng ta có thể tiếp tục có được một chính sách tốt hơn, cuối cùng chúng ta sẽ đạt được mục tiêu

chính sách tốt nhất.

Và về cơ bản, tôi thậm chí sẽ không viết hầu hết những điều này ra giấy.

Nhưng về cơ bản, lý thuyết cải tiến chính sách nói rằng nếu chúng ta tiếp tục đánh giá

và arg max trong một vòng lặp, cuối cùng chúng ta sẽ có được chính sách tối ưu và chúng ta gọi đây là

quá trình lặp lại chính sách.

Được rồi.

Vì vậy, về cơ bản tôi sẽ cố gắng mô tả điều đó dưới dạng một thuật toán.

Vì vậy, chúng tôi thực hiện một vòng lặp.

Và thực ra chúng ta bắt đầu với một chính sách ngẫu nhiên, tương đương với việc bắt đầu với một chính sách ngẫu nhiên

hàng đợi bằng chính sách ngẫu nhiên, ngẫu nhiên.

Và sau đó chúng tôi lặp lại.

Vì vậy, chúng tôi thực hiện đánh giá chính sách.

TỨC LÀ.

Find my pen hiện tại đang lag lắm.

Tìm, tôi thực sự không viết lộn xộn này.

Tìm hàng đợi, hàng đợi pi, SA.

Và bước thứ hai là arg max.

Được rồi.

Vậy chính sách mới

Và lưu ý rằng điều này mang tính quyết định.

Điều này thực sự khó chịu.

Tôi không biết tại sao bút của tôi bị chậm lại rất nhiều.

Bằng với arg tối đa.

Hành động tổng thể.

Q, SA.

Được rồi.

Và sau đó chúng ta có thể cắm cái này vào hàm hành động chọn để thực hiện tham lam epsilon.

Nhưng bây giờ chúng tôi sẽ giữ điều này mang tính quyết định.

Được rồi.

Vì vậy, chúng tôi gọi đây là sự lặp lại chính sách chính sách.