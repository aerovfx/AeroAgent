# Chương 9. Mô hình 1D Ising Học tăng cường sâu trong thực tế, Phiên bản video được dịch

---

Phần 9.3, Mô hình Ising 1D.

Trong phần này, chúng ta sẽ áp dụng đạo đức để giải một bài toán vật lý thực tế

được mô tả lần đầu tiên vào đầu những năm 1920 bởi nhà vật lý Wilhelm Lenz và học trò của ông là Ernst Eising.

Nhưng trước tiên, một bài học vật lý ngắn gọn.

Các nhà vật lý đang cố gắng tìm hiểu hành vi của các vật liệu từ tính như sắt bằng toán học

các mô hình.

Một miếng sắt mà bạn có thể cầm trên tay là tập hợp các nguyên tử sắt

nhóm lại với nhau bằng liên kết kim loại.

Nguyên tử gồm có hạt nhân proton tích điện dương, nơtron không mang điện,

và lớp electron bên ngoài mang điện tích âm.

Electron giống như các hạt cơ bản khác có một tính chất gọi là spin, được lượng tử hóa

sao cho electron chỉ có thể có spin lên hoặc spin xuống bất cứ lúc nào.

Hình 9.8

Hình 9.8.

Electron là các hạt cơ bản tích điện âm bao quanh hạt nhân của mọi

nguyên tử.

Chúng có một đặc tính gọi là quay và nó có thể quay lên hoặc quay xuống.

Vì chúng là các hạt tích điện nên chúng tạo ra từ trường và hướng quay của chúng

xác định hướng của các cực, bắc hoặc nam, của từ trường.

Tính chất spin có thể được coi là electron quay theo chiều kim đồng hồ hoặc ngược chiều kim đồng hồ.

Điều này không đúng theo nghĩa đen, nhưng nó đủ cho mục đích của chúng tôi.

Khi một vật nhiễm điện quay sẽ tạo ra một từ trường.

Vì vậy, nếu bạn lấy một quả bóng cao su, tạo cho nó một điện tích tĩnh điện bằng cách cọ xát nó trên thảm,

và sau đó xoay nó xung quanh.

Bạn sẽ có cho mình một nam châm bóng bay, mặc dù nam châm cực kỳ yếu.

Các electron cũng tạo ra từ trường nhờ spin và điện tích của chúng,

vì vậy các electron thực sự là những nam châm rất nhỏ.

Và vì tất cả các nguyên tử sắt đều có electron nên toàn bộ miếng sắt có thể trở thành một nam châm lớn

nếu tất cả các electron của nó được sắp xếp theo cùng một hướng.

Tức là tất cả đều quay lên hoặc tất cả đều quay xuống.

Các electron đang cố gắng nghiên cứu cách các electron quyết định tự sắp xếp,

và nhiệt độ của bàn ủi ảnh hưởng như thế nào đến quá trình này.

Nếu bạn làm nóng một nam châm, đến một lúc nào đó các electron thẳng hàng sẽ bắt đầu xen kẽ nhau một cách ngẫu nhiên.

spin của chúng, làm cho vật liệu mất đi từ trường ròng của nó.

Các nhà vật lý biết rằng mỗi electron tạo ra một từ trường,

và một từ trường cực nhỏ sẽ ảnh hưởng đến một electron ở gần.

Bạn đã từng chơi với hai thanh nam châm.

Bạn nhận thấy rằng chúng sẽ tự nhiên xếp hàng theo một hướng hoặc đẩy lùi theo hướng ngược lại.

Các electron làm điều tương tự.

Điều hợp lý là các electron cũng sẽ cố gắng sắp xếp chúng theo cùng một spin,

hình 9.9.

Hình 9.9.

Khi các electron tập trung lại với nhau, chúng thích có các spin sắp xếp theo cùng một hướng,

bởi vì nó có cấu hình năng lượng thấp hơn so với khi spin của chúng chống thẳng hàng,

và tất cả các hệ thống vật lý đều có xu hướng hướng tới năng lượng thấp hơn, tất cả các yếu tố khác đều như nhau.

Tuy nhiên, có một sự phức tạp được thêm vào.

Mặc dù các electron riêng lẻ có xu hướng tự sắp xếp, nhưng một nhóm đủ lớn

của các electron liên kết thực sự trở nên không ổn định.

Điều này là do khi số lượng electron liên kết tăng lên thì từ trường tăng lên

và tạo ra một số sức căng bên trong vật liệu.

Vì vậy điều thực sự xảy ra là các electron sẽ hình thành các cụm, gọi là các miền, trong đó

tất cả các electron được sắp xếp thẳng hàng, quay lên hoặc quay xuống, nhưng các miền khác cũng được hình thành.

Ví dụ, có thể có một miền gồm 100 electron sắp xếp quay tròn cạnh một miền khác

miền 100 electron đều sắp xếp quay xuống.

Vì vậy, ở cấp độ cục bộ, các electron giảm thiểu năng lượng của chúng bằng cách sắp xếp thẳng hàng.

Nhưng khi có quá nhiều thứ được căn chỉnh và từ trường trở nên quá mạnh, năng lượng tổng thể

của hệ thống tăng lên, khiến cho các electron chỉ sắp xếp thành các miền tương đối nhỏ.

Có lẽ sự tương tác giữa hàng nghìn tỷ electron trong vật liệu khối dẫn đến

sự tổ chức phức tạp của các electron thành các miền.

Nhưng rất khó để mô hình hóa nhiều tương tác như vậy.

Vì vậy, các nhà vật lý đã đưa ra một giả định đơn giản hóa rằng một electron nhất định chỉ bị ảnh hưởng bởi

những người hàng xóm gần nhất, đó chính xác là giả định tương tự mà chúng tôi đã đưa ra với những người hàng xóm

Học Q, hình 9.10.

Hình 9.10.

Đây là mô hình ising có độ phân giải cao, trong đó mỗi pixel đại diện cho một electron.

Các pixel nhẹ hơn sẽ được quay lên và màu đen sẽ được quay xuống.

Bạn có thể thấy rằng các electron tổ chức thành các miền trong đó tất cả các electron trong một

miền được căn chỉnh, nhưng các electron gần đó trong miền liền kề được chống liên kết với

tôn trọng miền đầu tiên.

Tổ chức này làm giảm năng lượng của hệ thống.

Đáng chú ý là chúng ta có thể mô hình hóa hành vi của nhiều electron và quan sát quy mô lớn

tổ chức mới nổi với việc học tăng cường đa tác nhân.

Tất cả những gì chúng ta cần làm là hiểu năng lượng của một electron là phần thưởng của nó.

Nếu một electron thay đổi spin của nó để thẳng hàng với hàng xóm của nó, chúng ta sẽ cho nó một giá trị dương

phần thưởng.

Nếu nó quyết định chống liên kết, chúng tôi sẽ trao cho nó một phần thưởng tiêu cực.

Khi tất cả các electron đang cố gắng tối đa hóa phần thưởng của chúng, điều này cũng giống như việc cố gắng

giảm thiểu năng lượng của chúng và chúng ta sẽ nhận được kết quả tương tự như các nhà vật lý nhận được khi họ sử dụng

các mô hình dựa trên năng lượng

Bạn có thể thắc mắc tại sao các electron được mô hình hóa này không sắp xếp theo cùng một hướng,

thay vì hình thành các miền như một nam châm thực sự nếu các electron nhận được phần thưởng tích cực khi tồn tại

căn chỉnh.

Mô hình của chúng tôi không hoàn toàn thực tế, nhưng cuối cùng nó cũng tạo thành các miền vì với

một số lượng electron đủ lớn thì điều đó ngày càng trở nên khó xảy ra đối với tất cả mọi người.

trong số chúng sắp xếp theo cùng một hướng, vì có một số tính ngẫu nhiên trong quá trình này,

hình 9.11.

Hình 9.11.

Đây là sự mô tả mô hình 2D của các spin electron trong đó dấu cộng được quay lên và

điểm trừ là quay xuống.

Có một miền các electron đều quay xuống, nổi bật bằng màu đen, và những miền này

được bao quanh bởi một lớp vỏ electron có spin up.

Như bạn sẽ thấy, chúng ta cũng có thể lập mô hình nhiệt độ của hệ thống bằng cách thay đổi lượng thăm dò

và bóc lột.

Hãy nhớ rằng, việc khám phá bao gồm việc lựa chọn ngẫu nhiên các hành động và nhiệt độ cao bao gồm

cũng có những thay đổi ngẫu nhiên.

Chúng khá giống nhau.

Mô hình hóa hành vi của spin electron có vẻ không quan trọng, nhưng mô hình cơ bản tương tự

kỹ thuật sử dụng cho điện tử có thể được sử dụng để giải quyết các vấn đề về di truyền, tài chính, kinh tế,

thực vật học và xã hội học, cùng nhiều lĩnh vực khác.

Đó cũng là một trong những cách đơn giản nhất để kiểm tra đạo đức, vì vậy đó là động lực chính của chúng tôi.

ở đây.

Điều duy nhất chúng ta cần làm để tạo mô hình ising là tạo một lưới các chữ số nhị phân

trong đó số 0 tượng trưng cho độ xoáy xuống và một tượng trưng cho độ xoáy lên.

Lưới này có thể có kích thước bất kỳ.

Chúng ta có thể có lưới một chiều, vectơ, lưới hai chiều, ma trận hoặc một số

tensor bậc cao.

Trong một số danh sách mã tiếp theo, trước tiên chúng ta sẽ giải quyết một mô hình D-Icing, vì nó là

dễ dàng đến mức chúng ta không cần sử dụng bất kỳ cơ chế phức tạp nào như phát lại hoặc phân phối trải nghiệm

thuật toán.

Chúng tôi thậm chí sẽ không sử dụng trình tối ưu hóa tích hợp sẵn của PyTorch.

Chúng tôi sẽ viết phần giảm dần độ dốc theo cách thủ công chỉ bằng một vài dòng mã.

Trong danh sách 9.3, chúng ta sẽ định nghĩa một số hàm để tạo ra lưới điện tử.

Bắt đầu từ phiên bản 9.3, một mô hình D-Icing, tạo lưới và tạo ra phần thưởng.

Chúng ta có hai hàm trong danh sách 9.3.

Cái đầu tiên tạo một lưới D được khởi tạo ngẫu nhiên, một vectơ, bằng cách trước tiên tạo một lưới

của các số rút ra từ phân phối chuẩn chuẩn.

Sau đó, chúng ta đặt tất cả các số âm bằng 0 và tất cả các số dương là một,

và chúng ta sẽ nhận được số lượng số 1 và số 0 trong lưới xấp xỉ nhau.

Chúng ta có thể hình dung lưới bằng Matplotlib.

Xem mã này.

Như bạn có thể thấy trong Hình 9.12, các số 1 được tô đậm và các số 0 có màu tối.

Chúng ta phải sử dụng các kích thước mở rộng gọn gàng với hàm dấu ba chấm để tạo vectơ

vào ma trận bằng cách thêm thứ nguyên đơn, vì plt.imShow chỉ hoạt động trên ma trận hoặc

ba tensor.

Hình 9.12.

Đây là mô hình một D-Icing biểu diễn spin của các electron được sắp xếp

trong một hàng duy nhất.

Hàm thứ hai trong danh sách 9.3 là hàm phần thưởng của chúng tôi.

Nó chấp nhận một danh sách, s, gồm các chữ số nhị phân và một chữ số nhị phân duy nhất, a, rồi so sánh

có bao nhiêu giá trị trong s khớp với a.

Nếu tất cả các giá trị khớp nhau thì phần thưởng là tối đa và nếu không có giá trị nào khớp thì phần thưởng sẽ âm.

Đầu vào s sẽ là danh sách những người hàng xóm.

Trong trường hợp này, chúng ta sẽ sử dụng hai hàng xóm gần nhất, vì vậy đối với một tác nhân nhất định, các hàng xóm của nó

sẽ là các đại lý ở bên trái và bên phải của nó trên lưới.

Nếu một tác nhân ở cuối lưới, hàng xóm bên phải của nó sẽ là thành phần đầu tiên trong

lưới, vì vậy chúng tôi sẽ bắt đầu lại từ đầu.

Điều này làm cho lưới thành một lưới tròn.

Mỗi phần tử trong lưới, một hoặc không, đại diện cho một electron đang quay lên hoặc quay

xuống.

Trong thuật ngữ học tăng cường, các electron là các tác nhân riêng lẻ trong môi trường.

Các tác nhân cần phải có các hàm và chính sách giá trị, vì vậy chúng không thể chỉ là một số nhị phân.

Số nhị phân trên lưới thể hiện hành động của tác nhân, chọn là

quay lên hoặc quay xuống.

Do đó, chúng ta cần lập mô hình các tác nhân của mình bằng cách sử dụng mạng lưới thần kinh.

Chúng tôi sẽ sử dụng phương pháp học Q thay vì phương pháp gradient chính sách.

Trong danh sách 9.4, chúng ta định nghĩa một hàm sẽ tạo ra các vectơ tham số được sử dụng trong

một mạng lưới thần kinh.

Liệt kê 9.4, một mô hình D-Icing, tạo ra các tham số mạng thần kinh.

Vì chúng ta sẽ sử dụng mạng nơ-ron để mô hình hóa hàm Q, nên chúng ta cần tạo

các thông số cho nó.

Trong trường hợp của chúng tôi, chúng tôi sẽ sử dụng một mạng lưới thần kinh riêng cho từng tác nhân, mặc dù điều này là không cần thiết.

Mỗi tác nhân có cùng một chính sách, vì vậy chúng ta có thể sử dụng lại cùng một mạng lưới thần kinh.

Chúng tôi sẽ làm điều này chỉ để cho thấy nó hoạt động như thế nào.

Đối với các ví dụ sau, chúng tôi sẽ sử dụng hàm Q dùng chung cho các tổng đài viên có chính sách giống hệt nhau.

Vì mô hình D-Icing rất đơn giản nên chúng ta sẽ viết mạng nơron theo cách thủ công bằng cách chỉ định

tất cả các phép nhân ma trận thay vì sử dụng các lớp tích hợp của PyTorch.

Chúng ta cần tạo một hàm Q chấp nhận vectơ trạng thái và vectơ tham số, và

trong thân hàm, chúng ta giải nén vectơ tham số thành nhiều ma trận tạo thành mỗi ma trận

lớp của mạng.

Liệt kê 9.5, một mô hình D-Icing, xác định hàm Q.

Đây là hàm Q được triển khai dưới dạng mạng nơ-ron hai lớp đơn giản, hình 9.13.

Nó mong đợi một vectơ trạng thái, s, đó là vectơ nhị phân của các trạng thái lân cận và một tham số

vectơ, theta.

Nó cũng cần tham số từ khóa, các lớp, là danh sách dạng chứa các cặp

chẳng hạn như s1, s2, s3, s4, v.v., cho biết hình dạng của ma trận tham số cho từng

lớp.

Tất cả các hàm Q đều trả về giá trị Q cho mỗi hành động có thể xảy ra, trong trường hợp này chúng dành cho xuống hoặc

lên, hai hành động.

Ví dụ: nó có thể trả về vectơ trừ 1, 1, biểu thị phần thưởng mong đợi cho

thay đổi vòng quay thành xuống là 1 và phần thưởng mong đợi cho việc thay đổi vòng quay thành lên là cộng

1.

Hình 9.13, hàm Q cho Tác nhân J chấp nhận vectơ tham số và mã hóa một nóng

vectơ hành động chung cho hàng xóm của Đặc vụ J.

Ưu điểm của việc sử dụng một vectơ tham số là dễ dàng lưu trữ tất cả các

các tham số cho nhiều mạng thần kinh dưới dạng danh sách các vectơ.

Chúng tôi chỉ để mạng lưới thần kinh giải nén vectơ thành các ma trận lớp.

Chúng ta sử dụng hàm kích hoạt tan vì đầu ra của nó nằm trong khoảng trừ 1, 1,

và phần thưởng của chúng tôi nằm trong khoảng trừ 2, 2, vì vậy phần thưởng cộng 2 sẽ thúc đẩy mạnh mẽ

đầu ra giá trị Q hướng tới cộng 1.

Tuy nhiên, chúng tôi muốn có thể sử dụng lại hàm Q này cho các dự án sau này của mình, vì vậy chúng tôi cung cấp

hàm kích hoạt dưới dạng tham số từ khóa tùy chọn, AFN.

Trong danh sách 9.6, chúng ta định nghĩa một số hàm trợ giúp để tạo ra thông tin trạng thái từ môi trường,

đó là lưới điện.

Liệt kê 9.6, mô hình 1D-Icing, lấy trạng thái của môi trường.

Các hàm trong danh sách 9.6 là hai hàm phụ trợ chúng ta cần chuẩn bị thông tin trạng thái

đối với hàm Q.

Để có được hàm trạng thái phụ gạch dưới cần một số nhị phân duy nhất, 0 cho spin down và

1 để quay lên và biến nó thành vectơ hành động được mã hóa một lần, trong đó 0 trở thành 1,0,

và 1 trở thành 0, 1 cho không gian hành động lên, xuống.

Lưới chỉ chứa một dãy số nhị phân biểu thị spin của mỗi tác nhân, nhưng

chúng ta cần biến những chữ số nhị phân đó thành vectơ hành động, rồi lấy tích bên ngoài

để có được một vectơ hành động chung cho hàm Q.

Trong danh sách 9.7, chúng tôi ghép một số phần chúng tôi đã tạo lại với nhau để tạo ra một lưới mới và

một tập hợp các vectơ tham số trên thực tế bao gồm tập hợp các tác nhân trên lưới.

Liệt kê 9.7, mô hình 1D-Icing, khởi tạo lưới.

Nếu bạn chạy mã danh sách 9.7, bạn sẽ nhận được kết quả giống như hình 9.14, nhưng mã của bạn sẽ

trông khác vì nó được khởi tạo ngẫu nhiên.

Xem mã này.

Hình 9.14, mô hình 1D của các electron được sắp xếp thành một hàng.

Bạn sẽ nhận thấy rằng các vòng quay được phân bổ khá ngẫu nhiên giữa lên, 1 và xuống,

0.

Khi huấn luyện hàm Q, chúng tôi hy vọng các spin sẽ tự sắp xếp theo cùng một hướng.

hướng.

Tất cả chúng có thể không sắp xếp theo cùng một hướng, nhưng ít nhất chúng phải tập hợp thành các miền

tất cả đều được căn chỉnh.

Bây giờ chúng ta hãy đi vào vòng đào tạo chính khi chúng ta đã xác định tất cả các chức năng cần thiết.

Liệt kê 9.8, mô hình 1D-Icing, vòng huấn luyện.

Trong vòng đào tạo chính, chúng tôi lặp lại tất cả 20 tác nhân đại diện cho các điện tử,

và với mỗi cái chúng ta tìm các láng giềng bên trái và bên phải của nó, lấy vectơ hành động chung của chúng,

và sử dụng giá trị đó để tính giá trị Q cho hai hành động có thể xảy ra là quay xuống và quay lên.

Mô hình 1D-Icing, như chúng tôi đã thiết lập, không chỉ là một dòng ô lưới mà là một hình tròn

chuỗi các ô lưới sao cho tất cả các tác nhân đều có hàng xóm bên trái và bên phải, hình 9.15.

Hình 9.15, chúng ta đang biểu diễn mô hình 1D-Icing bằng một vectơ nhị phân, nhưng nó

thực chất là một lưới tròn vì chúng ta coi electron ngoài cùng bên trái là electron ngay bên cạnh

tới electron ngoài cùng bên phải.

Mỗi tác nhân có vectơ tham số liên kết riêng mà chúng tôi sử dụng để tham số hóa hàm Q,

do đó mỗi tác nhân được điều khiển bởi một mạng Q sâu riêng biệt, mặc dù nó chỉ là mạng hai lớp

mạng lưới thần kinh nên chưa thực sự sâu sắc.

Một lần nữa, vì mỗi tác nhân có cùng một chính sách tối ưu, đó là sắp xếp theo cùng một cách với nó.

hàng xóm, chúng ta có thể sử dụng một DQN duy nhất để kiểm soát tất cả.

Chúng tôi sẽ sử dụng phương pháp này trong các dự án tiếp theo của mình, nhưng chúng tôi nghĩ rằng nó rất hữu ích khi trình bày

việc mô hình hóa từng tác nhân riêng biệt đơn giản như thế nào.

Trong các môi trường khác, nơi các tổng đài viên có thể có các chính sách tối ưu khác nhau, bạn sẽ cần

để sử dụng DQN riêng biệt cho từng cái.

Chúng tôi đã đơn giản hóa chức năng đào tạo chính này một chút để tránh bị phân tâm, hình 9.16.

Đầu tiên, hãy lưu ý rằng chính sách chúng tôi sử dụng là chính sách tham lam.

Tác nhân thực hiện hành động có giá trị Q cao nhất mọi lúc.

Không có chính sách tham lam epsilon nào mà đôi khi chúng ta thực hiện một hành động ngẫu nhiên.

Nói chung, một số loại chiến lược thăm dò là cần thiết, nhưng đây là một vấn đề đơn giản.

rằng nó vẫn hoạt động.

Trong phần tiếp theo, chúng ta sẽ giải mô hình Đóng băng 2D trên lưới vuông và trong trường hợp đó,

chúng tôi sẽ sử dụng chính sách softmax trong đó tham số nhiệt độ sẽ mô hình hóa vật lý thực tế

nhiệt độ của hệ electron mà chúng ta đang cố gắng lập mô hình.

Hình 9.16.

Đây là sơ đồ chuỗi cho vòng đào tạo chính.

Đối với mỗi tác nhân J, hàm Q tương ứng chấp nhận một vectơ tham số và khớp

vectơ hành động của đặc vụ J được ký hiệu là không phải J.

Hàm Q xuất ra một vectơ giá trị Q gồm 2 phần tử làm đầu vào cho hàm chính sách,

và nó chọn một hành động, một chữ số nhị phân, sau đó được lưu trữ trong một bản sao, bản sao của

môi trường lưới.

Sau khi tất cả các tổng đài viên đã chọn hành động, lưới được phản chiếu sẽ đồng bộ hóa với lưới chính.

Phần thưởng được tạo cho mỗi tác nhân và được chuyển đến hàm mất, tính toán

mất mát và truyền ngược lại mất mát vào hàm Q và cuối cùng vào tham số

vectơ để cập nhật.

Sự đơn giản hóa khác mà chúng tôi đã thực hiện là giá trị Q mục tiêu được đặt là RT cộng 1,

thưởng sau khi thực hiện hành động.

Thông thường nó sẽ là RT cộng 1 cộng gamma nhân V của ST viết hoa cộng 1, trong đó số cuối cùng

số hạng là hệ số chiết khấu gamma nhân với giá trị của trạng thái sau khi thực hiện hành động.

V của ST vốn cộng 1 được tính bằng cách chỉ lấy giá trị Q tối đa của số tiếp theo

vốn nhà nước ST cộng 1.

Đây là thuật ngữ khởi động mà chúng ta đã học trong chương DQN.

Chúng tôi sẽ đưa thuật ngữ này vào mô hình hình ảnh 2D ở phần sau của chương này.

Nếu bạn chạy vòng huấn luyện và vẽ lại lưới, bạn sẽ thấy nội dung như thế này.

Xem mã này.

Biểu đồ đầu tiên trong Hình 9.17 là biểu đồ phân tán về tổn thất qua mỗi sử thi đối với mỗi tác nhân.

Mỗi màu là một tác nhân khác nhau.

Bạn có thể thấy rằng tổn thất đều giảm và ổn định trong khoảng 30 kỷ nguyên.

Tất nhiên, cốt truyện phía dưới là lưới mô hình ising của chúng tôi và bạn có thể thấy rằng nó được tổ chức

thành hai miền hoàn toàn liên kết với nhau.

Phần nhẹ hơn ở giữa là nhóm tác nhân được sắp xếp theo hướng lên, một,

hướng, và phần còn lại được căn chỉnh theo hướng xuống, hướng 0.

Điều này tốt hơn nhiều so với phân phối ngẫu nhiên mà chúng tôi đã bắt đầu, vì vậy thuật toán đạo đức của chúng tôi

chắc chắn đã có tác dụng trong việc giải quyết mô hình D này.

Hình 9.17 Trên cùng Tổn thất của mỗi tác nhân trong quá trình đào tạo

thời đại.

Bạn có thể thấy rằng tất cả chúng đều giảm và ở mức tối thiểu là khoảng 30 kỷ nguyên hoặc lâu hơn.

Dưới cùng Mô hình một D sau khi tối đa hóa phần thưởng, giảm thiểu năng lượng.

Bạn có thể thấy rằng tất cả các electron được tập hợp lại với nhau thành các miền mà chúng đều được định hướng

cùng một cách.

Chúng ta đã giải thành công mô hình một D.

Hãy phức tạp hơn một chút bằng cách chuyển sang mô hình định vị 2D.

Ngoài việc giải quyết một số đơn giản hóa mà chúng tôi đã thực hiện, chúng tôi sẽ giới thiệu một cách tiếp cận mới để

Học Q lân cận được gọi là học Q trường trung bình.