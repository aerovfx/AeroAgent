# 45 - Đánh giá mô hình cú pháp Keras tiếng Anh

---

Chào mừng mọi người trở lại, trong phần ba của Keris, Syntex, BASIX, chúng ta sẽ tập trung vào

đánh giá mô hình của chúng tôi

Hãy nhớ rằng chúng ta có bộ thử nghiệm này để có thể so sánh các dự đoán của mô hình nhằm đánh giá mức độ hiệu quả của chúng.

mô hình của chúng tôi thực sự đang hoạt động.

Hãy quay lại sổ ghi chép và tiếp tục từ nơi chúng ta đã dừng lại.

Được rồi, chúng ta đang ở nơi chúng ta đã dừng lại lần trước.

Bây giờ, với cốt truyện này, tôi có thể thấy những mất mát của mình trên tập huấn luyện.

Nhưng điều tôi thực sự muốn biết là mô hình này sẽ hoạt động tốt như thế nào trên dữ liệu mà nó chưa từng thấy trước đây?

Và dữ liệu đó là dữ liệu thử nghiệm của chúng tôi.

Có rất nhiều cách khác nhau để chúng ta có thể đánh giá.

Vì vậy, chúng ta sẽ tìm hiểu một loạt các phương pháp khác nhau và rất nhiều trong số này sẽ trả về kết quả

kết quả tương tự, một số lỗi bình phương trung bình.

Vì vậy, chúng ta sẽ tìm hiểu các phương pháp khác nhau để thực hiện việc này.

Một cách để làm điều này là gọi các đánh giá mô hình và mô hình trọng số đánh giá hoạt động khi bạn vượt qua

trong tập thử nghiệm X và Y của bạn.

Vậy điều tôi sắp nói là bài kiểm tra X.

Và tại sao lại kiểm tra, và tôi sẽ nói dài dòng bằng 0, vì vậy tôi không thấy nhiều kết quả đầu ra và nếu tôi chạy

điều này xảy ra là nó trả về phần bị mất của mô hình của bạn trên tập kiểm tra và chúng tôi kiểm tra.

Vì vậy, con số này thực sự thể hiện sự mất mát số liệu mà bạn đã quyết định.

Và nếu chúng ta nhìn lại mô hình của mình, trong trường hợp của chúng ta, đó là sai số bình phương trung bình.

Vì vậy, điều này có nghĩa là trên tập thử nghiệm, đó là dữ liệu chưa từng thấy trước đây.

Nó đang trả về sai số bình phương trung bình là 24,9 bảy.

Vì vậy, chúng ta có thể làm điều tương tự cho tập huấn luyện của mình để có thể đánh giá mô hình.

vô cùng.

So với tại sao đào tạo?

Chạy nó và chúng tôi thấy sự mất mát trên tập huấn luyện của chúng tôi.

Hãy nhớ rằng, các giá trị của bạn có thể trông hơi khác chỉ do cách hoạt động của mạng lưới thần kinh.

Nó bắt đầu khởi tạo ngẫu nhiên.

Vì vậy, bạn có thể nhận được những con số hơi khác một chút.

Tuy nhiên, sau khi đào tạo khoảng 250 kỷ nguyên, bạn sẽ lơ lửng ở khoảng giữa 24

và 26 là sai số bình phương trung bình của bạn.

Vậy điều này thực sự có ý nghĩa gì?

Chà, đây là cách chúng ta có thể diễn giải kết quả của mình để xem các dự đoán thực sự hoạt động tốt như thế nào.

Và chúng tôi sẽ chỉ cho bạn cách lấy gốc, sai số bình phương trung bình và sai số tuyệt đối trung bình.

Vì vậy, cách chúng ta có thể làm là có được những dự đoán đúng thực tế của mình.

Và chúng tôi làm điều đó bằng cách nói mô hình dự đoán.

Và chúng ta sẽ đi vào.

Bài kiểm tra của chúng tôi để có được dấu gạch dưới kiểm tra.

Dự đoán.

Vì vậy, điều này có nghĩa là chúng tôi chuyển các tính năng thử nghiệm của mình và để mô hình dự đoán chỉ dựa trên các tính năng đó,

những gì nó nghĩ giá nên được.

Vì vậy, bây giờ đây là danh sách các mức giá được dự đoán dựa trên tập thử nghiệm tiếp theo của chúng tôi và trên thực tế, hãy cùng

mang những thứ này lại với nhau cùng với các giá trị thực cho tập kiểm tra đó.

Đó là bài kiểm tra tại sao.

Và sau đó chúng ta có thể vẽ chúng ra, so sánh chúng với nhau.

Vì vậy, những gì tôi sẽ làm là như sau.

Tôi sẽ tạo một khung dữ liệu có tên PRAD gạch dưới D.F..

Vì vậy, khung dữ liệu dự đoán của tôi.

Và nó sẽ bằng và trong trường hợp này tôi sẽ nói rằng dự đoán thử nghiệm của tôi là mô hình này

dự đoán và tôi sẽ biến chúng thành một cái chảo.

Chuỗi bằng cách nói dự đoán kiểm tra bằng PD.

Chuỗi đó kiểm tra các dự đoán gạch dưới và trong trường hợp này, tôi sẽ cần phải định hình lại thành ba

trăm dấu phẩy và chỉ vậy thôi là nó phù hợp với kích thước mà tiếng gọi nghiêm túc của gấu trúc mong đợi.

Về cơ bản, sau khi chạy cái này, tôi vẫn có những dự đoán thử nghiệm tương tự, nhưng đó là một bộ truyện về gấu trúc

bây giờ thay vì một Nampara.

Điều này sẽ cho phép tôi làm như sau.

Tôi có thể nói khung dữ liệu dự đoán của tôi bằng PDE.

Khung dữ liệu đó.

Dựa trên.

Tại sao phải kiểm tra?

Tôi sẽ nói rằng các cột ở đây chỉ là sự kiểm tra đúng, tại sao?

Vì vậy, ngay bây giờ, khung dữ liệu dự đoán của tôi vừa có giá trị thực sự là tại sao.

Và điều tôi sắp làm là nói, hãy tiếp tục và nối nó lại.

Chúng ta có giá trị thực của dấu phẩy y với dự đoán thử nghiệm của mình và tôi biết có rất nhiều mã ở đây vì

cũng như rất nhiều dấu ngoặc và dấu ngoặc đơn của Brace.

Vì vậy, nếu bạn gặp lỗi ở đâu đó, hãy tiếp tục và kiểm tra sổ ghi chép của chúng tôi và chỉ cần chạy trực tiếp và

nghe.

Điều tôi sắp làm cũng là đảm bảo rằng tôi nối cái này dọc theo trục bằng một.

Vì vậy, dọc theo các cột sau khi chạy, bạn sẽ có thể thấy khung dữ liệu dự đoán của mình, khung này

về cơ bản là trông như thế này.

Chúng tôi có bài kiểm tra.

ĐÚNG VẬY.

Tại sao?

Và ở đây chúng ta nhận được số 0 vì chúng ta thực sự không có tên cho nó.

Vì vậy, hãy tiếp tục và nói rằng các cột của tôi đang kiểm tra y đúng và sau đó là dự đoán mô hình của tôi.

Vì vậy, bây giờ khi tôi xem khung dữ liệu dự đoán của mình, tôi nhận được kết quả này.

Vì vậy, ở đây tôi có thể trực tiếp xem dựa trên bộ thử nghiệm của mình giá trị giá thực sự là gì và mô hình của tôi dự đoán.

Được rồi, điều tôi có thể làm là bây giờ tôi có thể thực sự sắp xếp những thứ này với nhau.

Vì vậy, những gì tôi có thể làm là nói.

Tạo một biểu đồ phân tán.

Dựa trên dữ liệu này trong khung dữ liệu dự đoán của tôi, sau đó tôi cũng sẽ làm như sau, tôi sẽ nói X là

bằng với phép thử đúng Y.

Và tôi đã lập biểu đồ chống lại những dự đoán mô hình này, vì vậy hãy chạy nó và chúng ta sẽ thấy kết quả này.

Vậy điều này thực sự có ý nghĩa gì?

Chà, hãy tưởng tượng rằng những dự đoán của tôi hoàn toàn phù hợp với mức giá tại sao thực sự.

Điều đó có nghĩa là tôi mong đợi một đường thẳng hoàn hảo ở đây, bởi vì nếu giá của tôi là ba trăm thì

dự đoán của tôi cũng sẽ là ba trăm.

Bây giờ hãy chú ý, chúng ta thực sự đang ở khá gần một đường thẳng rất thẳng, có nghĩa là mô hình này là

biểu diễn rất tốt.

Và về cơ bản, chúng ta cũng có thể lấy các số liệu để chứng minh điều đó không chỉ về mặt định tính thông qua cốt truyện mà còn về mặt định lượng.

thông qua các phương pháp hồi quy khác nhau mà chúng ta đã nói đến.

Nhớ lại trong các bài giảng về học máy, chúng ta đã thảo luận toàn bộ về đánh giá hồi quy.

Vì vậy chúng ta đã nói về sai số tuyệt đối trung bình, sai số bình phương trung bình và sau đó là căn bậc hai, sai số bình phương trung bình.

Vì vậy, hãy chỉ cho bạn cách bạn thực sự có thể lấy được những thứ đó.

Để làm được điều đó, tôi có thể nói từ Escalon rằng việc nhập số liệu có nghĩa là có lỗi tuyệt đối và.

Không khí phun ra trung bình, và nếu tôi muốn không khí tuyệt đối trung bình, thì tôi chỉ cần làm vậy nếu tôi nhìn vào cái này,

so sánh sự thật của tôi với màu trắng dự đoán của tôi và thật may mắn là tôi đã sắp xếp việc đó cho chính mình ở tiểu bang

của khung hình nơi tôi thực hiện bài kiểm tra của mình.

Đúng, tôi.

Và tôi cũng có dự đoán mô hình của mình, vì vậy tôi chạy nó và tôi nhận được sai số tuyệt đối trung bình khoảng 4,

đó là thứ bạn nên nhận được.

Bạn sẽ nhận được khoảng bốn cho một lỗi trung bình, tuyệt đối.

Vì vậy, điều này có nghĩa là trung bình tôi giảm được khoảng 4 đô la so với mức giá của mình.

Bây giờ, câu hỏi ngu ngốc phổ biến nhất mà tôi nhận được là làm sao tôi biết điều này là tốt hay xấu?

Vâng, nó thực sự phụ thuộc vào dữ liệu ban đầu của bạn.

Nếu bạn nhìn vào bản ghi khung dữ liệu ban đầu của chúng tôi, chúng tôi có cột giá này.

Hãy tiếp tục và gọi đó là mô tả về điều này.

Và chúng ta có thể thấy rằng giá trung bình là khoảng năm trăm đô la với mức tối thiểu là hai trăm hai mươi

ba và tối đa là bảy trăm bảy mươi bốn và sai số tuyệt đối trung bình của chúng tôi, đó là mức trung bình

chúng ta cách đây bao xa.

Chúng tôi đang giảm trung bình bốn đô la.

Vậy nếu tôi nhìn vào giá trung bình, nó sẽ nhỏ hơn 1%.

Vì vậy, điều đó có nghĩa rằng đây thực sự là một lỗi tuyệt đối, khá tốt.

Có điều gì đó được chỉ ra một lần nữa bởi cốt truyện này ở đây.

Đó gần như là một đường thẳng hoàn hảo.

Vì vậy, điều này cho thấy rằng mô hình của chúng tôi đang hoạt động rất tốt trong việc dự đoán giá của

đá quý dựa trên hai đặc điểm này.

Bây giờ, một lần nữa, lỗi tuyệt đối trung bình không có ý nghĩa gì nếu không có ngữ cảnh của nhãn.

Bạn đang cố gắng dự đoán xem giá trung bình là một đô la một giờ có nghĩa là sai số tuyệt đối là bốn đô la hay không.

Điều đó có nghĩa là chúng ta đã sai bốn trăm phần trăm.

Và đó là một câu chuyện rất khác.

Vì vậy, bạn luôn phải tính đến các giá trị trung bình cũng như mức phân phối thực tế của nhãn của mình

khi so sánh nó với lỗi của bạn, chẳng hạn như lỗi tuyệt đối trung bình.

Và chúng ta cũng có thể tính sai số bình phương trung bình của mình.

Bằng cách thực hiện chính xác điều tương tự để tôi có thể nói là kẻ đáng sợ hơn, hãy tiếp tục sao chép và dán cái này và

để ý rằng đó là 24 điểm chín bảy, về cơ bản giống với số chúng ta có ở dưới cùng

ở đây khi chúng tôi nói mô hình để đánh giá trong thử nghiệm X so với thử nghiệm Y, điều này hợp lý vì ban đầu

mất mát cho mô hình có nghĩa là lỗi bình phương.

Vì vậy, về cơ bản những gì mô hình này đánh giá như thế này chính xác là những gì dòng này làm.

Nó chỉ tính toán sai số bình phương trung bình cho bất kỳ tập kiểm tra phần trăm nào hoặc tập huấn luyện của bạn.

Và nếu chúng ta muốn lấy căn bậc hai là bình phương, thì tất cả những gì tôi cần làm về cơ bản là lấy căn bậc hai

của cái này, cũng giống như lấy một cái gì đó lũy thừa 0 phẩy 5.

Bạn cũng có thể nói và nếu bạn đã nhập một số bánh và sau đó chúng tôi lấy lại lỗi bình phương trung bình gốc,

đó là bốn phẩy chín mươi chín.

Vì vậy, bạn có thể sử dụng sai số tuyệt đối trung bình, bình phương trung bình và căn bậc hai, bình phương trung bình, tuy nhiên bạn thấy phù hợp với

đánh giá hiệu suất của mô hình của bạn.

Và cuối cùng, tôi muốn chuyển sang phần cuối cùng, đó là dự đoán dựa trên dữ liệu hoàn toàn mới.

Hãy tưởng tượng rằng chúng ta đi ra cánh đồng và tôi nhặt viên đá quý này ra khỏi mặt đất và nó có.

Những đặc điểm này, giả sử tôi nhặt viên đá quý mới này và chú ý đến kích thước của mình ở đây tôi có

dấu ngoặc kép sao cho khớp với dữ liệu gốc và tính năng một bằng chín trăm

chín mươi tám và tính năng hai bằng một nghìn.

‫And these are just made up features.

Vì vậy tôi đã nhặt viên ngọc mới này ra khỏi lòng đất.

Và tôi muốn hỏi mô hình của tôi, tôi nên định giá nó ở mức nào?

Chà, một điều tôi phải nhớ là mô hình của tôi đã được đào tạo về các tính năng được chia tỷ lệ này.

Vì vậy, điều đầu tiên tôi phải làm là lấy đại lượng vô hướng ban đầu và biến đổi.

Viên ngọc mới, bây giờ tôi đã có phiên bản thu nhỏ của các tính năng này, vì vậy hãy tiếp tục và đặt một viên ngọc mới tương đương

đến phiên bản thu nhỏ của New Gem.

Và bây giờ điều tôi có thể làm chỉ đơn giản là lấy mô hình của tôi.

Và dự đoán.

Giá của viên ngọc mới đó, trong trường hợp này sẽ vào khoảng bốn trăm hai mươi đô la,

vì vậy đó là cách bạn dự đoán về một bộ dữ liệu hoàn toàn mới.

Hãy nhớ rằng, đó chính xác là quy trình bạn vừa chạy trên tập dữ liệu thử nghiệm của mình vì dữ liệu thử nghiệm của bạn

được thiết lập, theo mô hình, về cơ bản là dữ liệu hoàn toàn mới mà nó chưa từng thấy trước đây.

Vì vậy, cách bạn đánh giá tập thử nghiệm của mình về cơ bản giống hệt như cách bạn làm đối với dữ liệu hoàn toàn mới.

Và cuối cùng, nếu bạn đang chạy một mô hình rất phức tạp và mất nhiều thời gian để đào tạo, bạn muốn

đảm bảo rằng bạn lưu mô hình đó.

Và Charise làm điều đó khá dễ dàng.

Chúng tôi chỉ đơn giản nói từ luồng cảm biến mang mô hình đó nhập khẩu.

Tải mô hình và sau đó tôi lấy mô hình hiện tại của mình.

Và họ lưu nó dưới dạng tệp PDF, vì vậy tôi có thể nói.

Model Maija nào đó, H5 chạy cái đó, còn bây giờ việc mình làm được là dùng model tải, vào sau nhé

trên tôi có thể nói, được rồi, tôi đang sử dụng một cuốn sổ tay mới và tôi muốn tải mô hình này lên.

Tôi chỉ cần chạy mô hình tải lên lệnh nhập này và tôi nói các mô hình sau này bằng.

Tải mô hình và sau đó tôi đọc mô hình đó, tôi đã lưu năm mô hình phòng tập thể dục của mình và sau đó bạn thực hiện nó vào một buổi sáng nào đó,

chúng dựa trên hình dạng đầu vào.

Bạn hoàn toàn có thể bỏ qua cảnh báo đó.

Không sao đâu.

Nhưng bây giờ hãy chú ý rằng tôi có thể xử lý mô hình sau này giống như bất kỳ mô hình nào khác.

Và sau đó dự đoán về GM mới, giống như tôi đã làm trước đây và nhận thấy rằng chúng tôi nhận được kết quả giống hệt nhau.

Vì vậy, đó là cách bạn có thể vừa lưu mô hình vừa tải nó sau trong tệp mới.

Được rồi, vậy là chúng ta đã đi qua những điều cơ bản nhất.

Bây giờ, chúng tôi đã làm điều này trên một tập dữ liệu được tạo giả.

Tiếp theo, hãy tập trung vào tập dữ liệu thực tế hơn nhiều và thực sự tập trung vào toàn bộ quy trình làm việc,

bao gồm phân tích dữ liệu khám phá và kỹ thuật tính năng, điều này rất quan trọng để trở thành một chuyên gia giỏi

người thực hành học máy.

Cảm ơn.

Và tôi sẽ gặp bạn ở bài giảng tiếp theo.