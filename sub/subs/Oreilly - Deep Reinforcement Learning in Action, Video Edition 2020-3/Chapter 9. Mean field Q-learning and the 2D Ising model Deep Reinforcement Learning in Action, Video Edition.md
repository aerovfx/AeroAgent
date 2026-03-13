# Chương 9. Q-learning trường trung bình và mô hình 2D Ising Học tăng cường sâu trong hành động, Phiên bản video được dịch

---

Phần 9.4, Học Q trường trung bình và Mô hình Ising 2D.

Bạn vừa thấy cách tiếp cận Q Learning lân cận có thể giải quyết mô hình Ising 1D

khá nhanh chóng.

Điều này là do, thay vì sử dụng toàn bộ không gian hành động chung sẽ là một

2 lũy thừa 20, bằng 1.048.576 vectơ hành động chung của phần tử, không thể điều chỉnh được, chúng tôi

chỉ cần sử dụng hàng xóm bên trái và bên phải của mỗi đại lý.

Điều đó làm giảm kích thước xuống còn 2 bình phương bằng 4 vectơ tác dụng chung, tức là

rất dễ quản lý.

Trong lưới 2D, nếu chúng ta muốn thực hiện điều tương tự và chỉ cần lấy không gian tác động chung của một

hàng xóm ngay lập tức của tác nhân, có 8 người hàng xóm, vì vậy không gian hành động chung là 2 mũ

lũy thừa của 8 bằng 256 vectơ phần tử.

Việc tính toán với vectơ 256 phần tử chắc chắn là có thể thực hiện được, nhưng thực hiện điều đó chẳng hạn,

400 đại lý trong mạng lưới 20 x 20 sẽ bắt đầu tốn kém.

Nếu chúng ta muốn sử dụng mô hình Ising 3D, số lượng hàng xóm ngay lập tức sẽ là 26 và

không gian tác dụng chung là 2 mũ 26, bằng 67,108,864.

Bây giờ chúng ta lại rơi vào lãnh thổ khó chữa.

Như bạn có thể thấy, cách tiếp cận lân cận tốt hơn nhiều so với việc sử dụng toàn bộ hành động chung.

không gian, nhưng với những môi trường phức tạp hơn, ngay cả không gian hành động chung của ngay lập tức

hàng xóm quá lớn khi số lượng hàng xóm lớn.

Chúng ta cần thực hiện một phép tính gần đúng đơn giản hóa lớn hơn nữa.

Hãy nhớ rằng lý do tại sao cách tiếp cận vùng lân cận có tác dụng trong mô hình Ising là vì

spin của electron bị ảnh hưởng nhiều nhất bởi từ trường của các electron lân cận gần nhất.

Cường độ từ trường giảm tỉ lệ với bình phương khoảng cách từ trường

nguồn, vì vậy việc bỏ qua các electron ở xa là hợp lý.

Chúng ta có thể thực hiện một phép tính gần đúng khác bằng cách lưu ý rằng khi hai nam châm được đưa lại gần nhau,

trường kết quả là tổng của hai nam châm này, hình 9.18.

Chúng ta có thể thay thế kiến thức về việc có hai nam châm riêng biệt bằng một giá trị gần đúng

việc có một nam châm có từ trường, đó là tổng của hai thành phần.

Vấn đề quan trọng không phải là từ trường riêng lẻ của các electron gần nhất

dưới dạng tổng của chúng, thay vì cung cấp cho hàm Q thông tin spin về mỗi lân cận

electron, thay vào đó chúng ta có thể cho nó tổng số spin của chúng.

Ví dụ: trong lưới 1D, nếu hàng xóm bên trái có vectơ hành động là 1, 0, xuống và

hàng xóm bên phải có vectơ hành động là 1, 0, lên, tổng sẽ là 1, 0 cộng 0, 1 bằng

1, 1.

Sau ngày 18/9, bên trái, một thanh nam châm và các đường sức từ của nó.

Hãy nhớ lại rằng một nam châm có hai cực từ, thường được gọi là cực bắc, n và cực nam, s.

Đúng rồi, đặt hai thanh nam châm lại gần nhau thì từ trường tổng hợp của chúng hơi

phức tạp hơn.

Khi chúng ta mô hình hóa cách các spin electron hoạt động trong lưới 2D hoặc 3D, chúng ta quan tâm đến

từ trường tổng thể được tạo ra bởi sự đóng góp của tất cả các electron trong một

khu phố.

Chúng ta không cần biết từ trường của từng electron riêng lẻ là bao nhiêu.

Thuật toán học máy hoạt động tốt hơn khi dữ liệu được chuẩn hóa trong một phạm vi cố định

như 0, 1, một phần là do hàm kích hoạt chỉ xuất dữ liệu trong

phạm vi đầu ra hạn chế, tên miền mã hóa và chúng có thể bị bão hòa bởi các đầu vào quá

lớn hoặc quá nhỏ.

Ví dụ: hàm tan có một tên miền, phạm vi giá trị mà nó có thể xuất ra,

và khoảng, trừ 1, cộng 1.

Vì vậy, nếu bạn cho nó hai số thực sự lớn nhưng không bằng nhau, nó sẽ xuất ra các số rất gần nhau

đến 1.

Vì máy tính có độ chính xác hạn chế nên cả hai giá trị đầu ra đều có thể làm tròn

đến 1 mặc dù dựa trên các đầu vào khác nhau.

Ví dụ: nếu chúng ta chuẩn hóa các đầu vào này trong khoảng âm 1, 1, thì tan có thể trả về

0,5 cho một đầu vào và 0,6 cho đầu vào kia, một sự khác biệt có ý nghĩa.

Vì vậy, thay vì chỉ tính tổng các vectơ hành động riêng lẻ cho hàm Q của chúng ta,

chúng tôi sẽ cung cấp cho nó tổng chia cho tổng giá trị của tất cả các phần tử, điều này sẽ chuẩn hóa

các phần tử trong vectơ kết quả nằm trong khoảng 0, 1.

Ví dụ: ta sẽ tính 1, 0, cộng 0, 1 bằng 1, 1, chia cho 2 bằng 0,50.

Vectơ chuẩn hóa này sẽ có tổng bằng 1 và mỗi phần tử sẽ nằm trong khoảng từ 0, 1.

Vậy điều đó nhắc nhở bạn điều gì?

Một phân phối xác suất.

Về bản chất, chúng ta sẽ tính toán phân bố xác suất theo các hành động gần nhất

hàng xóm và đưa vectơ đó cho hàm Q của chúng tôi.

Tính toán vectơ hành động trường trung bình.

Nói chung, chúng tôi tính toán vectơ hành động trường trung bình bằng công thức này.

Xem công thức này.

Trường hợp không j chỉ là ký hiệu cho trường trung bình của các tác nhân lân cận xung quanh tác nhân

j và ai đề cập đến vectơ hành động của tác nhân i, là một trong những hàng xóm của tác nhân j.

Vì vậy, chúng ta tính tổng tất cả các vectơ hành động trong vùng lân cận có kích thước n cho tác nhân j và sau đó chúng ta chia cho

kích thước của vùng lân cận để bình thường hóa kết quả.

Nếu phép toán không phù hợp với bạn, bạn sẽ sớm thấy cách thức hoạt động của nó trong Python.

Cách tiếp cận này được gọi là xấp xỉ trường trung bình, hoặc trong trường hợp của chúng tôi, học Q trường trung bình, MfQ.

Ý tưởng là chúng ta tính toán một loại từ trường trung bình xung quanh mỗi electron, thay vì

hơn là cung cấp từ trường riêng lẻ của mỗi người hàng xóm, hình 9.19.

Điều tuyệt vời của phương pháp này là vectơ trường trung bình chỉ dài bằng một

vectơ hành động riêng lẻ, bất kể quy mô vùng lân cận của chúng ta lớn đến mức nào hay tổng cộng có bao nhiêu

đại lý chúng tôi có.

Hình 9.19.

Tác dụng chung của một cặp spin electron là sản phẩm bên ngoài giữa từng spin của chúng

vectơ hành động, là bốn phần tử, một vectơ nóng.

Thay vì sử dụng hành động chung chính xác này, chúng ta có thể ước chừng nó bằng cách lấy giá trị trung bình

của hai vectơ hành động này, dẫn đến cái gọi là xấp xỉ trường trung bình.

Đối với hai electron cùng nhau, với một electron quay lên và một electron quay xuống, xấp xỉ trường trung bình

dẫn đến việc giảm hệ thống hai electron này thành một electron ảo duy nhất có điện tích không xác định

quay 0,50,5.

Điều này có nghĩa là vectơ trường trung bình của chúng tôi cho mỗi tác nhân sẽ chỉ là vectơ hai phần tử

cho một mô hình D-I-Zing và cả cho hai mô hình I-Zing chiều D và cao hơn.

Môi trường của chúng ta có thể phức tạp và có chiều cao tùy ý, và nó vẫn sẽ được tính toán

dễ dàng.

Chúng ta hãy xem cách học Q trường trung bình, MfQ, hoạt động như thế nào trên hai mô hình D-I-Zing.

Mẫu hai D-I-Zing giống hệt mẫu một D, chỉ khác là bây giờ là hai

Lưới D, tức là một ma trận.

Đại lý ở góc trên bên trái sẽ có hàng xóm bên trái là đại lý ở trên cùng bên phải

góc và hàng xóm của nó ở trên sẽ là tác nhân ở góc dưới bên trái, do đó lưới

thực sự được bao quanh bề mặt của một quả cầu.

Hình 9.20.

Hình 9.20.

Chúng tôi biểu diễn hai mô hình D-I-Zing dưới dạng lưới vuông hai D, nghĩa là một ma trận.

Nhưng chúng tôi thiết kế nó sao cho không có ranh giới và các tác nhân dường như nằm trên ranh giới

thực sự nằm ngay cạnh các tác nhân ở phía đối diện của lưới.

Như vậy, lưới hai D thực sự là một lưới hai D bao quanh bề mặt của một hình cầu.

Liệt kê 9.9, học tập MfQ, chức năng chính sách.

Chức năng mới đầu tiên chúng ta sẽ sử dụng cho hai mô hình D-I-Zing là softmax

chức năng.

Bạn đã thấy điều này ở chương 2 khi chúng tôi giới thiệu ý tưởng về hàm chính sách.

Hàm chính sách là một hàm, pi ánh xạ từ S đến A, từ không gian trạng thái đến không gian

của các hành động.

Nói cách khác, bạn cung cấp cho nó một vectơ trạng thái và nó sẽ trả về một hành động cần thực hiện.

Trong chương 4, chúng tôi đã sử dụng mạng lưới thần kinh làm chức năng chính sách và trực tiếp đào tạo nó

để đưa ra những hành động tốt nhất.

Trong học Q, chúng ta có bước trung gian là tính toán các giá trị hành động đầu tiên, giá trị Q,

cho một trạng thái nhất định, sau đó chúng tôi sử dụng các giá trị hành động đó để quyết định nên thực hiện hành động nào.

Vì vậy, trong quá trình học Q, hàm chính sách nhận các giá trị Q và trả về một hành động.

Sự định nghĩa.

Hàm softmax được định nghĩa về mặt toán học là...

Biểu hiện này.

Trong đó Pt của A là phân bố xác suất trên các hành động, Qt của A là vectơ giá trị Q,

và tau là thông số nhiệt độ.

Xin nhắc lại, hàm softmax nhận vào một vectơ với các số tùy ý, sau đó

chuẩn hóa vectơ này thành phân bố xác suất, sao cho tất cả các phần tử đều

dương và có tổng bằng 1, và mỗi phần tử sau phép biến đổi tỷ lệ thuận với

phần tử trước khi chuyển đổi.

Nghĩa là, nếu một phần tử lớn nhất trong vectơ thì nó sẽ được gán giá trị lớn nhất

xác suất.

Hàm softmax có thêm một đầu vào, tham số nhiệt độ, ký hiệu là

biểu tượng tau của Hy Lạp.

Nếu tham số nhiệt độ lớn sẽ giảm thiểu sự khác biệt về xác suất

giữa các phần tử và nếu nhiệt độ nhỏ, sự khác biệt ở đầu vào sẽ

phóng đại.

Ví dụ: vectơ softmax, nhiệt độ 10, 5, 90 bằng 100, bằng 0,2394, 0,2277,

0,5,328 và softmax, 10, 5, 90, nhiệt độ bằng 0,1, bằng 0,0616, 0,0521, 0,8863.

Ở nhiệt độ cao, mặc dù phần tử cuối cùng, 90, lớn hơn 9 lần so với phần tử

phần tử lớn thứ hai, 10, phân bố xác suất thu được sẽ gán cho nó một xác suất

là 0,53, chỉ lớn gấp đôi xác suất lớn thứ hai.

Khi nhiệt độ tiến tới vô cùng, phân bố xác suất sẽ đồng đều,

nghĩa là mọi xác suất đều bằng nhau.

Khi nhiệt độ tiến tới 0, phân bố xác suất sẽ trở thành phân bố suy biến,

trong đó tất cả khối lượng xác suất tập trung tại một điểm duy nhất.

Bằng cách sử dụng chức năng này như một hàm chính sách, khi tau tiến tới vô cùng, các hành động sẽ là

được chọn hoàn toàn ngẫu nhiên và khi tau tiến tới 0, chính sách sẽ trở thành argmax

mà chúng ta đã sử dụng ở phần trước với mô hình định vị 1D.

Sở dĩ tham số này được gọi là nhiệt độ là vì hàm softmax cũng được sử dụng

trong vật lý để mô hình hóa các hệ vật lý như spin của hệ electron, trong đó

nhiệt độ làm thay đổi hoạt động của hệ thống.

Có rất nhiều sự giao thoa giữa vật lý và học máy.

Trong vật lý, nó được gọi là phân bố Boltzmann, trong đó nó cho biết xác suất mà một hệ

sẽ ở một trạng thái nhất định, là một hàm số của năng lượng và nhiệt độ của trạng thái đó

của hệ thống, Wikipedia.

Trong một số tài liệu học thuật về học tăng cường, bạn có thể thấy chính sách softmax được đề cập

như chính sách của Boltzmann, nhưng bây giờ bạn biết nó cũng giống như vậy.

Chúng tôi đang sử dụng thuật toán học tăng cường để giải một bài toán vật lý, vì vậy nhiệt độ

tham số của hàm softmax thực sự tương ứng với nhiệt độ của electron

hệ thống chúng tôi đang mô hình hóa.

Nếu chúng ta đặt nhiệt độ của hệ lên rất cao, các electron sẽ quay ngẫu nhiên,

và xu hướng hòa hợp với hàng xóm của chúng sẽ bị khắc phục bởi nhiệt độ cao.

Nếu chúng ta đặt nhiệt độ quá thấp, các electron sẽ bị kẹt và không thể thay đổi nhiều.

Trong danh sách 9.10, chúng tôi giới thiệu một hàm để tìm tọa độ của các tác nhân và một hàm khác

chức năng tạo phần thưởng trong môi trường 2D mới.

Liệt kê 9.10, trường trung bình Q, các hàm học tập, phối hợp và khen thưởng.

Thật bất tiện khi làm việc với tọa độ xy để tham chiếu đến các tác nhân trong lưới 2D.

Chúng tôi thường đề cập đến các tác nhân sử dụng một giá trị chỉ mục duy nhất dựa trên việc làm phẳng lưới 2D

thành một vectơ, nhưng chúng ta cần có khả năng chuyển đổi chỉ số phẳng này thành tọa độ xy,

và đó chính là chức năng của chức năng lấy hợp âm gạch dưới.

Chức năng nhận phần thưởng gạch dưới 2D là chức năng phần thưởng mới của chúng tôi dành cho lưới 2D.

Nó tính toán sự khác biệt giữa vectơ hành động và vectơ trường trung bình.

Ví dụ: nếu vectơ trường trung bình là 0,25, 0,75 và vectơ hành động là 1,0 thì

phần thưởng phải thấp hơn nếu vectơ hành động là 0,1.

Xem mã này.

Bây giờ chúng ta cần tạo một hàm để tìm những người hàng xóm gần nhất của một tác nhân và sau đó

tính toán vectơ trường trung bình cho những người hàng xóm này.

Liệt kê 9.11, học Q trường trung bình, tính vectơ hành động trung bình.

Hàm này chấp nhận một chỉ mục tác nhân, j, một số nguyên duy nhất, chỉ mục dựa trên mặt phẳng

lưới và trả về 8 hành động có ý nghĩa gần nhất, xung quanh, lân cận của tác nhân đó trên lưới.

Chúng tôi tìm thấy 8 người hàng xóm gần nhất bằng cách lấy tọa độ của tác nhân, chẳng hạn như 5,5 và

thì chúng ta chỉ cần cộng mọi tổ hợp của xy, trong đó x và y thuộc tập 0,1.

Vì vậy, chúng ta sẽ tính 5,5 cộng 1,0 bằng 6,5 và 5,5 cộng trừ 1,1 bằng 4,6, v.v.

Đây là tất cả các chức năng bổ sung mà chúng tôi cần cho vỏ 2D.

Chúng ta sẽ sử dụng lại hàm lưới gạch dưới init và các hàm tham số gạch dưới gen từ trước đó.

Hãy khởi tạo lưới trong các tham số.

Xem mã này.

Chúng tôi đang bắt đầu với lưới 10 x 10 để giúp nó chạy nhanh hơn, nhưng bạn nên thử chơi

với kích thước lưới lớn hơn.

Bạn có thể thấy trong hình 9.21 rằng các spin được phân phối ngẫu nhiên trên lưới ban đầu,

vì vậy chúng tôi hy vọng rằng sau khi chạy thuật toán đạo đức, nó sẽ trông có tổ chức hơn rất nhiều.

Chúng tôi hy vọng sẽ thấy các cụm electron thẳng hàng.

Chúng tôi đã giảm kích thước lớp ẩn xuống còn 10 để giảm thêm chi phí tính toán.

Lưu ý rằng chúng tôi chỉ tạo một vectơ tham số duy nhất.

Chúng ta sẽ sử dụng một dqn duy nhất để kiểm soát tất cả 100 đặc vụ, vì họ có

chính sách tối ưu tương tự.

Chúng tôi đang tạo hai bản sao của lưới chính vì những lý do sẽ rõ ràng khi chúng tôi nhận được

vào vòng đào tạo.

Hình 9.21.

Đây là mô hình định dạng 2D được khởi tạo ngẫu nhiên.

Mỗi ô vuông đại diện cho một electron.

Các ô vuông có lưới màu sáng tượng trưng cho các electron được định hướng với spin hướng lên và các ô vuông màu tối

đang quay xuống.

Trong ví dụ này, chúng tôi sẽ thêm một số điểm phức tạp mà chúng tôi đã bỏ qua trong trường hợp 1D,

vì đây là một vấn đề khó hơn.

Chúng tôi sẽ sử dụng cơ chế phát lại trải nghiệm để lưu trữ kinh nghiệm và đào tạo theo nhiều đợt

của những trải nghiệm này.

Điều này làm giảm phương sai và độ dốc và ổn định quá trình đào tạo.

Chúng tôi cũng sẽ sử dụng các giá trị Q mục tiêu thích hợp, RT cộng 1, cộng gamma nhân V vốn

ST cộng 1.

Vì vậy, chúng ta cần tính giá trị Q hai lần cho mỗi lần lặp, một lần để quyết định hành động cần thực hiện,

và sau đó lại lấy V của ST viết hoa cộng 1.

Trong danh sách 9.12, chúng ta chuyển sang vòng huấn luyện chính của mô hình định dạng 2D.

Trong danh sách 9.12, học tập Q trường trung bình, vòng đào tạo chính.

Đó là rất nhiều mã, nhưng nó chỉ phức tạp hơn một chút so với những gì chúng tôi đã có cho

Mô hình định vị 1D.

Điều đầu tiên cần chỉ ra là vì trường trung bình của mỗi tác nhân phụ thuộc vào

hàng xóm và các vòng quay của hàng xóm được khởi tạo ngẫu nhiên, tất cả các trường trung bình sẽ

ngẫu nhiên để bắt đầu quá.

Để giúp hội tụ, trước tiên chúng tôi cho phép mỗi tác nhân chọn một hành động dựa trên các

các trường trung bình và chúng tôi lưu trữ hành động trong bản sao lưới tạm thời, gạch dưới lưới,

để lưới chính không thay đổi cho đến khi tất cả các đại lý đưa ra quyết định cuối cùng về

hành động nào để thực hiện.

Sau khi mỗi tác nhân thực hiện một hành động dự kiến trong phần gạch dưới của lưới, chúng tôi sẽ cập nhật

bản sao lưới tạm thời thứ hai, gạch dưới lưới, đây là những gì chúng tôi đang sử dụng để tính toán

trường nghĩa.

Trong lần lặp tiếp theo, các trường trung bình sẽ thay đổi và chúng tôi cho phép các tổng đài viên cập nhật

những hành động mang tính thăm dò.

Chúng tôi thực hiện việc này một vài lần, được điều khiển bởi tham số mục num gạch dưới, để cho phép

hành động để ổn định xung quanh giá trị gần tối ưu dựa trên phiên bản hiện tại của

hàm Q.

Sau đó, chúng tôi cập nhật lưới chính và thu thập tất cả các hành động, phần thưởng, trường trung bình và dấu gạch dưới Q

các giá trị tiếp theo, v của ST viết hoa cộng 1 và thêm chúng vào bộ đệm phát lại trải nghiệm.

Khi bộ đệm phát lại có nhiều trải nghiệm hơn tham số kích thước lô, chúng ta có thể bắt đầu

được đào tạo nhiều kinh nghiệm.

Chúng tôi tạo danh sách các giá trị chỉ mục ngẫu nhiên và sử dụng các giá trị này để tập hợp một số trải nghiệm ngẫu nhiên

trong bộ đệm phát lại.

Sau đó, chúng tôi chạy một bước giảm độ dốc như bình thường.

Hãy chạy vòng lặp đào tạo và xem những gì chúng ta nhận được.

Xem mã này.

Nó đã hoạt động.

Bạn có thể thấy trong hình 9.22 rằng tất cả trừ ba electron, các tác nhân, đều có spin của chúng

được sắp xếp theo cùng một hướng, giúp giảm thiểu năng lượng của hệ thống và tối đa hóa

phần thưởng.

Biểu đồ mất mát có vẻ hỗn loạn một phần vì chúng tôi đang sử dụng một DQN duy nhất để lập mô hình cho từng tác nhân,

vì vậy DQN giống như đang trong một cuộc chiến chống lại chính nó, khi một đặc vụ đang cố gắng liên kết với

hàng xóm của nó, nhưng hàng xóm của nó đang cố gắng liên kết với một tác nhân khác.

Một số bất ổn có thể xảy ra.

Hình 9.22.

Biểu đồ trên cùng là biểu đồ tổn thất của DQN.

Sự mất mát có vẻ như không hội tụ, nhưng chúng ta có thể thấy rằng nó thực sự học cách

giảm thiểu năng lượng của hệ thống, tối đa hóa phần thưởng, nói chung ở bảng dưới cùng.

Trong phần tiếp theo, chúng tôi sẽ nâng cao kỹ năng học tập tăng cường đa tác nhân của mình lên cấp độ tiếp theo

cấp độ bằng cách giải quyết một vấn đề khó khăn hơn với hai đội đặc vụ chiến đấu với nhau

trong một trò chơi.