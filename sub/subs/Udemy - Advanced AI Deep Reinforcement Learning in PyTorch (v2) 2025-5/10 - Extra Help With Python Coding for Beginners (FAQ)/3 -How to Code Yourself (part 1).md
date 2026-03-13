# 3 -How to Code Yourself (phần 1) đã dịch

---

Xin chào mọi người và chào mừng trở lại lớp học này.

Bài giảng này nói về cách viết mã một cách độc lập khi bạn đang học máy.

Bạn luôn nghe tôi nói rằng điều đầu tiên bạn nên cố gắng làm khi học một thuật toán

là tự mình viết mã trước khi xem mã của người khác.

Đối với một số sinh viên mới làm quen với học máy, họ chưa rõ cách thực hiện điều đó.

Vì vậy, bài giảng này sẽ giải thích quá trình suy nghĩ mà bạn nên trải qua với hy vọng rằng

nó khuyến khích nhiều người cố gắng tự viết mã hơn.

Tôi muốn gói gọn điều này trong câu khi đến lúc viết mã bạn phải viết mã.

Vì vậy, hãy nhớ điều này bất cứ khi nào bạn thấy một số mã thể hiện các khái niệm chúng ta học trong phần này.

tất nhiên.

Ngay cả khi bạn không hiểu đầy đủ những gì đang diễn ra, việc viết mã và sao chép các ví dụ từ người khác

giúp bạn xây dựng trí nhớ cơ bắp.

Đôi khi mọi người hành động như thể họ đang học quần vợt bằng cách đọc một cuốn sách về quần vợt.

Điều này tất nhiên là không thể.

Bạn cần tìm hiểu một số điều về quần vợt, đó là sự thật thuần túy trong việc khiến bộ não của bạn hoạt động một cách có ý thức.

sự thật, nhưng sau đó bạn phải ra ngoài và thực hành những khái niệm đó trên sân tennis.

Khi bạn đã kiệt sức và nắm vững mọi thứ bạn biết cho đến nay, bạn có thể học các kỹ thuật mới.

Vì vậy, bạn có chu kỳ liên tục học các kỹ thuật mới và sau đó thực hành chúng.

Tại sao lại thế này?

Bởi vì học kỹ thuật này như một sự thật thuần túy không có nghĩa là bạn thực sự hiểu nó.

Thực hành kỹ thuật này giúp bạn suy nghĩ về kỹ thuật đó từ một góc nhìn khác.

Luyện tập nhiều lần dẫn đến sự hiểu biết mới về việc học trong tiềm thức, đó là cơ bắp

trí nhớ.

Bạn phải trải qua chu kỳ này.

Nhưng một số sinh viên ngây thơ nghĩ rằng họ sẽ đọc cả một cuốn sách về quần vợt và sau đó

trở thành bậc thầy quần vợt trong lần đầu tiên họ thử chơi.

Điều này rất phổ biến, đặc biệt khi tất cả những gì bạn thực sự cần làm là ngồi đó và xem video

và không ai có thể buộc bạn phải gõ.

Rất nhiều người thậm chí không nghĩ đến việc thử.

Vì vậy, chỉ cần nhớ điều này bất cứ khi nào bạn nhìn thấy mã.

Khi đến lúc viết mã, bạn phải viết mã.

Chúng ta sẽ nói một chút về lý do tại sao bạn muốn tự mình viết mã.

Nhiều khi thuật toán thực hiện hoặc cách thức hoạt động của nó không được rõ ràng ngay lần đầu tiên

bạn tìm hiểu về nó.

Mỗi cá nhân sẽ có nền tảng riêng của mình nên họ có thể quen thuộc với

mẫu và biết chính xác phải làm gì trong khi một số cá nhân có thể có những câu hỏi mà không

một người khác có.

Đôi khi bạn che đậy các chi tiết bởi vì bạn cho rằng bạn biết chuyện gì đang xảy ra trong khi thực sự

có những điều quan trọng mà bạn chưa xem xét.

Vì vậy, việc cố gắng tự viết mã có thể giúp ích cho bạn như thế nào.

Việc tự mình viết mã buộc bạn phải suy nghĩ về từng chi tiết.

Nó buộc bạn phải suy nghĩ từng dòng một.

Bạn phải làm quen với các kiểu dữ liệu và hình dạng của tất cả các biến của bạn và chúng

tất cả phải khớp với nhau một cách hợp lý, giống như những khối hợp pháp.

Ví dụ, bạn biết rằng để thực hiện phép cộng ma trận phần tử, cả hai ma trận

phải có hình dạng giống hệt nhau.

Vì vậy, nếu bạn thấy rằng chúng không có hình dạng giống nhau thì một trong những giả định trước đây của bạn là

không đúng.

Vì vậy bạn nên quay lại và sửa nó.

Các khối pháp lý phải tuân theo một bộ quy tắc cụ thể để khớp với nhau một cách hợp lý.

Nếu bạn đưa ra những giả định không chính xác về cách các khối pháp lý khớp với nhau và bạn cố gắng tham gia

với họ nó sẽ không hoạt động.

Nếu không cố gắng tự mình xây dựng mọi thứ, bạn sẽ không bao giờ khám phá được những chi tiết này.

Bây giờ chúng ta hãy nói về cách tự viết mã.

Hãy xem xét kịch bản học máy có giám sát.

Chúng tôi biết rằng chúng tôi sẽ có một số đầu vào và một số mục tiêu và chúng tôi muốn cố gắng thực hiện

dự đoán từ các đầu vào rất gần với mục tiêu.

Chúng tôi thường gọi đầu vào là x và mục tiêu là y.

Đôi khi chúng ta gọi các mục tiêu là t nhưng vì mục đích của bài giảng này chúng ta sẽ gọi các mục tiêu là

y.

Bây giờ điểm tiếp theo này là điểm mấu chốt.

Thực ra x là gì và y là gì không quan trọng.

Sẽ không thành vấn đề nếu bạn đang xem tập dữ liệu thương mại điện tử và các cột của x có thể

là thời gian trên trang web, thời gian trong ngày, số lượng trang mà người dùng đã xem, v.v.

Bạn cũng có thể xem một tập dữ liệu gồm các hình ảnh X-quang trong đó mỗi cột là pixel

cường độ của một hình ảnh.

Đây là điểm mấu chốt.

Chúng tôi nói rằng tất cả dữ liệu đều giống nhau.

Khi chúng tôi thực hiện hồi quy tuyến tính, chúng tôi không có các loại hồi quy tuyến tính khác nhau cho thương mại điện tử

và hình ảnh X quang.

Hồi quy tuyến tính là cùng một thuật toán cho dù tập dữ liệu của bạn là gì.

Vì vậy, chúng tôi nói tất cả dữ liệu đều giống nhau.

Về mặt lý thuyết, tôi có thể cung cấp cho bạn một tập dữ liệu gồm x và y và bạn có thể huấn luyện cách phân loại

thuật toán trên đó mà không cần tôi nói cho bạn biết ý nghĩa của x và y.

Bạn sẽ cảm thấy rất thoải mái với ý tưởng này.

Đôi khi, mọi người nói, điều này không thực tế vì tôi muốn làm những ví dụ cụ thể, nhưng

đó là vì họ không suy nghĩ thông minh.

Trên thực tế, đây là điều thiết thực nhất chúng ta có thể làm vì nó có nghĩa là tất cả những gì chúng ta học được.

chúng ta có thể áp dụng nó cho bất kỳ tập dữ liệu nào tồn tại.

Điều đó có nghĩa là tôi có thể huấn luyện một mô hình trên tập dữ liệu thương mại điện tử, nhưng tôi cũng có thể huấn luyện một mô hình

trên bộ dữ liệu quảng cáo trực tuyến mà không cần tìm hiểu thêm điều gì mới.

Đó thực sự là hình thức lập trình lười biếng tuyệt vời nhất.

Hãy học một điều gì đó một lần và áp dụng nó vào mọi ngành nghề.

Một hệ quả lớn của tất cả dữ liệu là giống nhau là có một lượng dữ liệu không giới hạn.

cơ hội thực tập dành cho bạn.

Bạn có thể tải xuống các bộ dữ liệu từ Kaggle, từ Google, từ Wikipedia, từ Amazon hoặc từ

bất cứ nơi nào khác và thử các thuật toán bạn đã học.

Điều này có nghĩa là, giả sử bạn có một tập dữ liệu, bạn quan tâm đến nhiều thứ hơn

chúng tôi làm trong lớp

Nhìn vào lớp học, chúng ta phải sử dụng những tập dữ liệu mà mọi người đều có thể hiểu được.

Ví dụ: văn bản và hình ảnh.

Mọi người nên biết văn bản và hình ảnh là gì.

Văn bản và hình ảnh chỉ là các loại dữ liệu cơ bản trên web.

Bạn có thể thậm chí không nghĩ đến thực tế rằng văn bản và hình ảnh là dữ liệu bởi vì nó

thật tầm thường.

Trong mọi trường hợp, chúng tôi làm việc rất nhiều với văn bản và hình ảnh vì mọi người đều hiểu chúng.

Nhưng giả sử bạn là nhà sinh vật học và bạn biết về DNA.

Bạn thấy DNA và bộ gen thực sự thú vị.

Vì vậy, bạn muốn sử dụng các thuật toán mà chúng tôi tìm hiểu về điều đó.

Chà, điều đó thật tuyệt và bạn hoàn toàn nên làm điều đó.

Hãy nhớ rằng, tất cả dữ liệu đều giống nhau, vì vậy tất cả những gì bạn cần làm là chuyển đổi dữ liệu của mình thành dạng thích hợp.

x và y để đưa vào các thuật toán học máy của chúng tôi.

Nhược điểm là chúng ta sẽ không nói về DNA trong lớp trừ khi nó rất đơn giản.

ví dụ vì hầu hết các nhà khoa học máy tính cũng không phải là nhà sinh học.

Vì thế họ không biết DNA là gì.

Họ không hiểu chi tiết cụ thể.

Vì vậy, một ví dụ sẽ không có nhiều ý nghĩa đối với họ.

Điều này trái ngược với văn bản và hình ảnh có ý nghĩa đối với mọi người.

Tương tự với bất kỳ lĩnh vực chuyên môn nào khác như tài chính, mạng máy tính, vũ trụ học

và vân vân.

Vì vậy, bây giờ chúng ta có thể bắt đầu từ đúng nơi để nói về học tập có giám sát.

Chúng ta có x và chúng ta có y.

Chúng ta phải làm gì với chúng?

Trong học tập có giám sát, chúng tôi biết rằng có hai điều chính chúng tôi muốn làm.

Chúng tôi muốn đào tạo và chúng tôi muốn dự đoán.

Trong scikit-learn, tất cả các mô hình đều có cùng một API.

Sẽ không thành vấn đề nếu bạn đang thực hiện hồi quy logistic hoặc cây quyết định hoặc rừng ngẫu nhiên.

Tất cả các mô hình được giám sát trong scikit-learn đều có hai chức năng giống nhau.

Phù hợp và dự đoán.

Lắp một mô hình chỉ là một từ đồng nghĩa với việc đào tạo một mô hình.

Nếu bạn không tin tôi, bạn có thể tự mình xem tài liệu về scikit.

Khi bạn tìm hiểu về học máy có giám sát, điều bạn thực sự học là,

những gì diễn ra bên trong hai chức năng này.

Các thông số là gì và các thông số đó được học như thế nào?

Đó thực sự là tất cả những gì học máy có giám sát, thực hiện hai chức năng này.

Thực hiện theo quan điểm này sẽ mang lại cấu trúc mã của bạn và nó sẽ tạo ra mọi thứ

dễ dàng hơn nhiều để hình dung trong đầu bạn.

Bây giờ hãy làm một ví dụ đơn giản để củng cố ý tưởng này.

Trong ví dụ này, tôi sẽ cung cấp cho bạn một thuật toán và bạn sẽ triển khai nó bằng mã.

Có hai điểm chính tôi muốn nêu rõ trước khi đưa ra thuật toán cho bạn.

Đầu tiên, tôi sẽ không cung cấp cho bạn nhiều trực giác về cách thức hoạt động của nó.

Thứ hai, tôi sẽ không rút ra lý thuyết đằng sau lý do tại sao nó hoạt động.

Lý do tôi muốn đề cập đến hai điểm chính này là bạn nên nhận ra rằng bạn không

cần hai thông tin này để dịch mã giả thành mã.

Rất nhiều thời gian, ba khái niệm, trực giác, lý thuyết và cách thực hiện này có tác dụng củng cố

lẫn nhau.

Lý do tôi đang tập trung vào việc thực hiện ngay bây giờ là vì đó là điều mà mọi người

thường bỏ lỡ hoặc nghĩ rằng họ không cần tất cả trong khi thực sự đó là một phần cực kỳ quan trọng

của quá trình học tập.

OK, mã giả như sau.

Trong chức năng dự đoán của tôi, như bạn đã biết, tôi sẽ lấy một số dữ liệu đầu vào X. Của tôi

dự đoán sẽ là Y mũ bằng X nhân W. Bạn có thể đã nhận ra đây là tuyến tính

hồi quy.

Tuy nhiên, hãy quên những gì bạn biết về hồi quy tuyến tính và giả vờ rằng đây chỉ là

một số công thức tôi đã đưa cho bạn.

Điều tôi có thể nói với bạn là chúng tôi đang tạo ra một loại mô hình hồi quy nào đó.

Từ phương trình này có thể thấy rõ rằng các tham số của mô hình được chứa

trong vectơ có trọng số W. Có lẽ tôi cũng sẽ nói với bạn rằng W là một vectơ

cùng kích thước với số lượng vectơ đặc trưng trong X. Tất nhiên, điều này phải đúng theo thứ tự

để ma trận nhân có giá trị.

Trục này giống như một loại kiểm tra độ tỉnh táo để bạn có thể đảm bảo mọi thứ đều có ý nghĩa.

Trong hàm fit của tôi, tôi muốn thực hiện vòng lặp này một số lần.

Như chúng ta đã biết từ slide trước rằng các tham số của mô hình được chứa trong

W, thì rõ ràng là bên trong hàm fit, điều chúng ta muốn làm là cập nhật

W. Không có gì đáng ngạc nhiên, đó là những gì đang xảy ra ở đây, một sự kiểm tra tỉnh táo tốt khác.

Bây giờ vì bạn đã quen với hồi quy tuyến tính nên có thể bạn đã nhận ra

đây là sự giảm dần độ dốc.

Một lần nữa, tôi muốn bạn giả vờ như bạn không biết điều đó.

Nhưng bạn biết gì không?

Bạn biết rằng các thuật toán lặp lại rất phổ biến trong học máy và việc giảm độ dốc

là một trong những phổ biến nhất.

Bạn có thể suy luận rằng đây là một dạng giảm độ dốc, nhưng bạn không cần

để biết nó là gì để viết nó thành mã.

Chúng ta còn biết gì nữa?

Bạn biết vòng lặp for là gì và bạn biết cách viết when bằng Python.

Bạn biết rằng X là ma trận N x D chứa dữ liệu đầu vào và Y là vectơ kích thước N

chứa các mục tiêu.

Bạn biết rằng mũ Y là một vectơ cỡ N chứa các dự đoán.

Bạn biết rằng W là vectơ kích thước D chứa các tham số mô hình và bạn biết cách thêm,

trừ và nhân các đối tượng này.

Vì vậy, chúng ta có thể viết thuật toán này mà không cần biết nó hoạt động như thế nào.

Tất nhiên có thể suy ra rất nhiều điều về cách thức hoạt động của nó từ công thức này.

Đây là những gì bạn không biết.

Bạn không biết T, số lần vòng lặp được cho là sẽ chạy.

Bạn không biết Ada, tỷ lệ học tập.

Điều này hoàn toàn ổn.

Bạn không thể để sự thiếu hiểu biết này cản trở bước đi của bạn.

Sự thật của vấn đề là sẽ có những tình huống mà bạn không được thông báo

con số chính xác để cắm vào.

Trong nhiều trường hợp, câu trả lời sẽ là tùy thuộc vào vấn đề.

Điều quan trọng là bạn phải làm quen với ý tưởng thử và sai và bạn có

để đưa ra những phỏng đoán có cơ sở dựa trên những gì bạn đã biết.

Vậy bạn có thể làm gì?

Khi bạn biết rằng tốc độ học được cho là một con số nhỏ, nó nhỏ đến mức nào tùy thuộc vào

vấn đề.

Thông thường đó là một số nhỏ hơn 1 như 0,1.

Nếu điều đó không hiệu quả, bạn có thể thử hạ thấp nó.

Thông thường chúng tôi hạ thấp nó theo hệ số 10.

Vì vậy, ví dụ, tốc độ học tiếp theo chúng tôi sẽ thử là 10 mũ trừ 2, 10 mũ trừ

3 và vân vân.

Thông thường trong học máy, cho dù bạn đang xem thuật toán được giám sát hay không được giám sát,

có một chi phí liên quan hoặc hàm mục tiêu mà bạn đang cố gắng giảm thiểu.

Giả sử tôi nói với bạn rằng đó là sai số bình phương, đây thường là sai số mà chúng tôi thường sử dụng để hồi quy.

Bây giờ bạn có cách chọn số lần lặp của vòng lặp và cách học

tỷ lệ.

Chúng ta làm điều này như thế nào?

Vì vậy, bên trong hàm fit, bạn sẽ vẽ biểu đồ chi phí dưới dạng hàm lặp.

Tôi luôn khuyên bạn nên làm điều này bất kể bạn đang xem thuật toán nào.

Nói chung bạn luôn muốn chi phí hội tụ.

Mô hình bạn thường thấy là lúc đầu có sự sụt giảm mạnh và dần dần

phẳng ra khi số lần lặp tăng lên.

Để chọn số lần lặp bạn muốn dừng khi đường cong đủ phẳng.

Bạn có thể nhận ra đây là một kịch bản lợi nhuận giảm dần.

Lợi nhuận giảm dần vì lúc đầu, chúng tôi giảm chi phí rất nhiều chỉ sau một vài lần lặp.

Cuối cùng, chúng tôi có thể thực hiện nhiều lần lặp lại nhưng chúng tôi hầu như không giảm được chi phí.

Một cách khác là bạn có thể sử dụng một bộ xác thực riêng và dừng khi xác thực

chi phí tăng lên nhưng đó không phải là trọng tâm của bài giảng này.

Không giống như chi phí đào tạo, chi phí xác nhận không được đảm bảo giảm ở mỗi vòng

bởi vì đó không phải là điều chúng tôi đang giảm thiểu.

Bạn cũng có thể sử dụng cốt truyện tương tự này để giúp cải thiện tốc độ học tập của mình.

Nếu chi phí tăng vọt hoặc không còn là một con số, tỷ lệ học tập của bạn có thể quá cao.

Nếu chi phí của bạn hội tụ quá chậm, bạn có thể thử tăng tốc độ học tập của mình.

Vậy mã cuối cùng của bạn trông như thế nào?

Chà, chúng tôi biết rằng chúng tôi muốn tạo một lớp có ít nhất các hàm dự đoán và phù hợp.

Bạn không cần phải sử dụng một lớp nhưng tôi thấy rằng nó gói gọn mã một cách độc đáo và cung cấp

cấu trúc hữu ích

Lưu ý rằng một khi bạn đã có thuật toán trong toán học thì bạn không cần phải làm nhiều việc để chuyển nó thành

mã numpy.

Bạn biết cách nhân ma trận, bạn biết cách cộng, bạn biết cách trừ.

Đây là những phép tính số học cơ bản mà tôi chắc chắn bạn đã biết.

Nếu bạn không biết cách thực hiện những điều này trong numpy thì tôi có một khóa học hoàn toàn miễn phí về numpy

trên ngăn xếp gọn gàng mà bạn có thể lấy.

Đây là phần thứ hai của mã nơi chúng ta thực sự tạo một thể hiện của lớp và

sau đó sử dụng nó.

Tôi cũng đã đưa vào hàm chi phí lỗi bình phương chỉ nhằm mục đích hoàn thành.

Điều thú vị về mẫu này là nó không thực sự thay đổi từ một thuật toán

tiếp theo.

Cấu trúc về cơ bản sẽ luôn như vậy, ít nhất là đối với việc học có giám sát

và học tập không giám sát.

Vì vậy, như chúng ta đã thảo luận trước đó, việc bạn đang triển khai thuật toán nào không quan trọng, cho dù

nó là hồi quy tuyến tính, hồi quy logistic, mạng lưới thần kinh, v.v.

Chúng luôn có chức năng dự đoán và chức năng phù hợp.

Và việc tìm hiểu những gì diễn ra bên trong các hàm này cũng tương đương với việc học thuật toán.

Vì vậy, trên thực tế, một cách để bắt đầu viết mã là bắt đầu chỉ với mã soạn sẵn này và sau đó

điền vào chỗ trống.