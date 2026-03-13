# 007 Chấm dứt vòng lặp bất thường Phần 1

---

Xin chào tất cả mọi người.

Chào mừng trở lại.

Trong video này, chúng ta sẽ nói về câu lệnh break.

Đôi khi cần phải thoát khỏi một vòng lặp từ giữa thân của nó.

Tức là thoát khỏi vòng lặp trước tất cả các câu lệnh trong đó.

Cơ thể thực hiện.

Điều này có nghĩa là nếu một điều kiện nhất định.

Lấy làm tiếc.

Lấy làm tiếc.

Xin chào tất cả mọi người.

Chào mừng trở lại.

Trong video này.

Chúng ta sẽ nói về việc chấm dứt vòng lặp bất thường.

Thông thường một câu lệnh hoang dã sẽ được thực thi cho đến khi điều kiện của nó trở thành sai.

Một chương trình đang chạy sẽ kiểm tra điều kiện này trước để xác định.

Liệu nó có thực thi các câu lệnh trong phần thân vòng lặp hay không.

Sau đó nó chỉ kiểm tra lại điều kiện này sau khi thực hiện tất cả các câu lệnh còn lại trong phần thân vòng lặp.

Thông thường, một vòng lặp while sẽ không thoát ra ngay phần thân của nó nếu điều kiện của nó trở thành sai trước khi hoàn thành.

tất cả các câu lệnh trong phần thân của nó.

Câu lệnh while được thiết kế theo cách này bởi vì thông thường người lập trình có ý định thực hiện tất cả các lệnh

các tuyên bố trong cơ thể như một đơn vị riêng lẻ hoặc không thể chia cắt.

Tuy nhiên, đôi khi bạn nên thoát khỏi cơ thể ngay lập tức hoặc kiểm tra lại tình trạng từ cơ thể.

thay vào đó là giữa vòng lặp.

Như đã nói ở trên, câu lệnh while chỉ kiểm tra điều kiện của nó ở đầu vòng lặp chứ không phải ở đầu vòng lặp.

giữa.

Không phải vòng lặp while kết thúc ngay lập tức khi điều kiện của nó trở thành đúng.

Hãy để chúng tôi minh họa hành vi này với sự trợ giúp của ví dụ.

Vì vậy, ở đây.

Chúng tôi có một ví dụ đơn giản thể hiện hành vi thoát ra trên cùng của vòng lặp while.

Ban đầu chúng ta đã gán giá trị cho biến X là 10.

Trong khi x bằng bằng mười.

Có nghĩa là khi x bằng mười thì điều kiện trở thành đúng.

Sau đó, chúng ta có ba câu lệnh in bên trong phần thân của vòng lặp while.

Sau đó.

Đúng vậy.

Việc gán lại giá trị sẽ tìm kiếm biến X để minh họa hành vi hàng đầu.

Hành vi thoát hàng đầu.

Của vòng lặp while.

Khi chúng tôi gán người Sikh vào X.

Chúng ta có thoát ngay lập tức không?

Vì vậy đây là điều kiện chúng ta phải kiểm tra.

Được rồi, chúng ta hãy chạy mã này và kiểm tra xem chúng ta có thoát ngay lập tức hay không.

Cho dù dòng điều khiển.

Tiếp tục kiểm tra.

Mặc dù.

Toàn bộ câu lệnh của vòng lặp while trước khi nó chuyển sang vòng lặp while.

Điều kiện hàng đầu có nghĩa là sau.

Hoàn thành tất cả các câu lệnh, luồng điều khiển sẽ chuyển sang điều kiện trên cùng.

Được rồi.

Đó là những gì chúng ta phải kiểm tra.

Hãy để chúng tôi làm điều này.

Phá vỡ tuyên bố như bình luận.

Bây giờ chúng ta hãy lưu và chạy chương trình này từ đây đến đây.

Vì vậy hãy nhìn vào đây.

Ngay cả sau khi gán giá trị sáu cho biến X, câu lệnh in thứ tư vẫn được thực thi có nghĩa là

mặc dù điều kiện cho.

Tiếp tục.

Vòng lặp thay đổi ở giữa thân vòng lặp.

Câu lệnh while không kiểm tra điều kiện cho đến khi nó hoàn thành tất cả các câu lệnh còn lại trong

cơ thể của nó.

Và việc thực thi trở lại đầu vòng lặp.

Khi X trở thành sáu, luồng điều khiển sẽ diễn ra.

Sẽ hoàn thành.

Thực hiện tất cả các câu lệnh trong cơ thể của nó.

Và sau khi hoàn thành tất cả các tuyên bố.

Trong cơ thể.

Luồng điều khiển sẽ trở về đầu vòng lặp.

Đó là x bằng mười.

Khi luồng điều khiển đạt đến đỉnh vòng lặp.

Nó sẽ gán giá trị mới.

Được gán cho biến X là sáu.

Sáu bằng mười.

Điều kiện trở thành sai.

Vòng lặp while sẽ chấm dứt.

Đôi khi sẽ thuận tiện hơn nếu thoát khỏi một vòng lặp từ giữa thân của nó.

Tức là thoát khỏi vòng lặp trước khi tất cả các câu lệnh trong phần thân của nó được thực thi.

Điều này có nghĩa là nếu một điều kiện nhất định trở thành đúng trong phần thân vòng lặp, hãy thoát ngay lập tức.

Tương tự, một câu lệnh sai thường lặp lại trên tất cả các giá trị trong phạm vi của nó hoặc trên tất cả các ký tự.

trong chuỗi của nó.

Tuy nhiên, đôi khi bạn nên thoát khỏi vòng lặp for sớm.

Python cung cấp các câu lệnh break và continue để giúp các lập trình viên linh hoạt hơn.

Thiết kế logic điều khiển vòng lặp.

Vì vậy, chúng ta có các câu lệnh break và continue do hàm cung cấp.

Trăn.

Chúng ta hãy nói về câu lệnh break ban đầu, như chúng ta đã nói trước đó.

Đôi khi cần phải thoát khỏi một vòng lặp từ giữa thân của nó.

Tức là thoát khỏi vòng lặp trước khi tất cả các câu lệnh trong phần thân của nó được thực thi.

Điều này có nghĩa là nếu một điều kiện nhất định trở thành đúng trong thân vòng lặp thì sẽ thoát ngay lập tức.

Điều kiện thoát ở giữa này có thể giống điều kiện điều khiển vòng lặp while, nhưng nó có

không cần phải như vậy.

Python cung cấp câu lệnh break để triển khai vòng lặp thoát ở giữa.

Logic điều khiển.

Câu lệnh break làm cho việc thực thi chương trình ngay lập tức thoát ra khỏi phần thân vòng lặp.

Chúng ta hãy chuyển sang công việc thực tế của mình và xem câu lệnh break hoạt động như thế nào.

Trong ví dụ trước chúng ta đã thấy.

Nếu không có câu lệnh break, luồng chương trình hoặc luồng điều khiển sẽ tiếp tục kiểm tra toàn bộ câu lệnh

trong vòng lặp while.

Hãy để chúng tôi kích hoạt câu lệnh break và xem.

Nó hoạt động như thế nào.

Không có câu lệnh break nào được chèn vào.

Ngay sau khi gán giá trị mới 6 cho biến x, chúng ta có thoát ngay lập tức không?

Vì câu lệnh break đã được kích hoạt?

Đúng.

Luồng điều khiển sẽ thoát.

Vòng lặp while ngay lập tức mà không kiểm tra các câu lệnh còn lại hoặc không thực hiện các câu lệnh còn lại

các câu lệnh của thân vòng lặp while.

Điều này là do điều kiện.

X bằng sáu.

Điều kiện này sẽ được theo sau bởi.

Sau đây là ba câu lệnh in và câu lệnh break.

Tuyên bố cuối cùng này là X bằng sáu.

Vậy khi X bằng sáu.

Phá vỡ vòng lặp.

Chúng ta hãy lưu cái này và chạy chương trình để xem nó có hoạt động hay không.

Điều khiển.

Cộng thêm vào.

Vì vậy hãy nhìn vào đây khi câu lệnh break xuất hiện bên trong vòng lặp.

Luồng điều khiển sẽ.

Dừng lại.

Thực hiện các câu lệnh còn lại.

Chúng ta hãy xem một ví dụ khác với sự trợ giúp của câu lệnh break.

Chương trình này, chương trình nhỏ, chỉ tính tổng các số dương và kết thúc bằng việc nhận số âm

những con số.

Ban đầu, mục nhập bằng 0 và tổng cũng bằng 0.

Đây là hướng dẫn cho người dùng.

Trong khi đúng.

Nhận mục nhập từ người dùng.

Nếu mục nhập nhỏ hơn 0.

Phá vỡ vòng lặp nếu mục nhập lớn hơn 0.

Nếu mục nhập lớn hơn 0.

Sau đó, tuyên bố phá vỡ này.

Sẽ không được kích hoạt vì câu lệnh break sẽ kích hoạt.

Chỉ khi điều kiện trở thành đúng.

Nếu điều kiện trở thành sai.

Câu lệnh break này sẽ không được kích hoạt vì câu lệnh break này đã được chèn vào bên trong

cơ thể của.

Tuyên bố nếu.

Chúng tôi biết điều đó.

Nếu điều kiện của câu lệnh if trở thành sai, phần thân của câu lệnh if sẽ không được thực thi.

Do đó nếu điều kiện trở thành sai.

Luồng điều khiển sẽ không thực thi phần thân của câu lệnh if bên trong phần thân.

Chúng tôi có tuyên bố phá vỡ.

Bạn có hiểu được logic bên trong cơ thể không?

Chúng tôi có tuyên bố phá vỡ.

Do đó khi điều kiện if trở thành sai.

Phần thân của câu lệnh if sẽ không được thực thi.

Đó là nghỉ ở đây.

Và bên trong vòng lặp while, chúng ta có phần thân là some bằng với một số mục cộng.

Tổng không nằm trong câu lệnh break, hãy cẩn thận quan sát ở đây có một.

Chỉ có một câu lệnh bên trong câu lệnh if phá vỡ mục nhập nào đó.

Và nếu tất cả đây là các câu lệnh của vòng lặp while thì tổng bằng tổng cộng với mục và cuối cùng in

số tiền.

Hãy để chúng tôi chạy mã này và kiểm tra xem nó hoạt động như thế nào.

Hãy để chúng tôi nhập số.

Các số dương như năm.

Năm không nhỏ hơn không.

Do đó cơ thể.

Câu lệnh vòng lặp sẽ không được đánh giá vì điều kiện trở thành sai.

Và tổng trở thành tổng bằng tổng cộng với mục nhập bằng 0 cộng với 5 vì giá trị ban đầu của

tổng không là gì ngoài số không.

Chúng ta hãy nhập số là bốn.

Bốn nhỏ hơn không.

Điều kiện trở thành sai một lần nữa.

Tuyên bố nghỉ sẽ không được đánh giá.

Tổng trở thành tổng bằng tổng cộng với mục nhập, nghĩa là.

Năm cộng bốn.

Chín.

Chúng ta hãy nhập thêm một số nữa.

Đó là để.

Vẫn còn điều kiện là sai trong câu lệnh if.

Chúng ta nhập giá trị âm để kết thúc vòng lặp.

Đó là trừ hai.

Khi số nhập trở thành âm hai, âm hai nhỏ hơn không.

Điều kiện trở thành đúng khi điều kiện if trở thành đúng.

Phần thân của câu lệnh if sẽ được đánh giá bên trong phần thân.

Chúng tôi có tuyên bố phá vỡ.

Bất cứ khi nào luồng điều khiển tìm thấy câu lệnh break.

Nó ngay lập tức bỏ qua các câu lệnh còn lại trong phần còn lại của vòng lặp.

Có nghĩa là.

Phần còn lại của câu lệnh sẽ bị luồng điều khiển bỏ qua.

Vì vậy, hãy để chúng tôi.

Nhấn vào.

Vì vậy bây giờ hãy nhìn vào đây.

Sau khi vào.

Trừ hai.

Câu lệnh if trở thành đúng vì âm hai nhỏ hơn 0.

Luồng điều khiển sẽ di chuyển đến phần thân của câu lệnh if.

Bên trong phần thân của câu lệnh if, chúng ta có dấu ngắt.

Tuyên bố.

Vì vậy, tuyên bố phá vỡ này.

Sẽ phá vỡ vòng lặp.

Chúng ta sẽ thoát ra khỏi vòng lặp.

Có nghĩa là luồng điều khiển sẽ.

Phá vỡ.

Vòng lặp và nó sẽ không.

Kiểm tra hoặc thực hiện hoặc đánh giá các câu lệnh còn lại của.

Vòng lặp.

Và cuối cùng, câu lệnh print print này nằm ngoài .

Phần thân của vòng lặp while sẽ được đánh giá.

Vậy tổng bằng tổng.

Đó là 14.

Xin lỗi, số 11.

Đây là cách hoạt động của câu lệnh break.

Khi câu lệnh break break xuất hiện, luồng điều khiển sẽ xuất hiện.

Ra.

Từ vòng lặp.

Nó sẽ không đánh giá các câu lệnh còn lại của vòng lặp.

Dù thế nào đi nữa.

Được rồi.

Điều kiện của câu lệnh while trong ví dụ này là tautology.

Vì vậy, khi chương trình chạy, nó được đảm bảo bắt đầu thực thi các câu lệnh trong khối while tại

ít nhất một lần vì điều kiện của thời điểm đó không bao giờ sai.

Câu lệnh break là cách duy nhất để làm điều đó.

Thoát khỏi vòng lặp trong ví dụ này.

Vì vậy, đây là trạng thái nghỉ.

Câu lệnh chỉ thực thi khi nó xác định số đó.

Người dùng nhập vào là số âm.

Khi chương trình gặp câu lệnh break trong quá trình thực thi, nó sẽ bỏ qua bất kỳ câu lệnh nào

theo dõi.

Thân vòng lặp và thoát khỏi vòng lặp ngay lập tức.

Từ khóa break có nghĩa là thoát ra khỏi vòng lặp.

Vị trí của câu lệnh break trong ví dụ này làm cho không thể thêm số âm vào

biến tổng.

Một số nhà thiết kế phần mềm tin rằng các lập trình viên nên sử dụng câu lệnh break.

Tiết kiệm vì nó đi chệch khỏi logic điều khiển vòng lặp thông thường.

Lý tưởng nhất là mỗi vòng lặp nên có một điểm vào và một điểm thoát duy nhất.

Ví dụ này có tệp single.

Điểm thoát.

Đó là tuyên bố phá vỡ.

Một số lập trình viên thường sử dụng câu lệnh break bên trong câu lệnh while.

Trong đó điều kiện của thời điểm đó không phải là sự lặp lại.

Việc thêm câu lệnh break vào vòng lặp như vậy sẽ thêm một điểm thoát bổ sung.

Có nghĩa là đỉnh của vòng lặp nơi điều kiện được kiểm tra là một điểm và câu lệnh break là một điểm khác.

Hầu hết các lập trình viên đều trỏ đến điểm thoát.

Hoàn toàn có thể chấp nhận được, nhưng đặc biệt hơn nhiều là phá vỡ các điểm trong một vòng lặp.

Và bạn nên tránh thực hành đó.

Câu lệnh break không hoàn toàn cần thiết để kiểm soát hoàn toàn vòng lặp while.

Nghĩa là, chúng ta có thể viết lại bất kỳ chương trình Python nào có chứa câu lệnh break trong vòng lặp while sao cho

nó hành xử theo cùng một cách.

Nhưng không sử dụng câu lệnh break.

Vì vậy, ở đây chúng ta có thể thấy.

Câu lệnh ngắt độ rộng vòng lặp while và tương tự.

Vòng lặp while không có câu lệnh break trong điều kiện if.

Chúng tôi đang sử dụng câu lệnh break.

Vì vậy, ở đây.

Điều tương tự có thể được thay thế.

Với sự giúp đỡ của.

Điều kiện tạo vòng lặp là sai, đó chính là điều kiện.

Đối với vòng lặp while.

Ban đầu làm cho vòng lặp là đúng.

Và bên trong điều kiện if, làm cho vòng lặp thành sai và sau đó sử dụng phần khác.

Phần C và phần B vẫn giữ nguyên.

Chỉ có sự khác biệt là.

Chúng tôi đang sử dụng.

Vòng lặp và điều kiện.

Như để.

Các câu lệnh trong biểu thức Boolean ghép.

Để tránh sử dụng câu lệnh break.

Vì vậy, hãy nhìn vào điều kiện while.

Trong ví dụ đầu tiên không có câu lệnh break.

Câu lệnh while chỉ có một điều kiện.

Với tuyên bố break.

Câu lệnh while có điều kiện boolean phức hợp.

Có nghĩa là có hai điều kiện phụ lặp lại và điều kiện một.

Nếu điều kiện trở thành điều kiện một trở thành đúng và vòng lặp trở thành đúng, chỉ khi đó điều kiện ghép

biểu thức boolean trở thành đúng.

Và sau đó.

Chúng tôi có câu lệnh if.

Và bên trong câu lệnh if mà chúng ta đang tạo, vòng lặp bằng false để kết thúc vòng lặp while.

Khi vòng lặp trở thành sai và khi chương trình.

Luồng là luồng điều khiển đạt đến đỉnh của vòng lặp while.

Vòng lặp sẽ được.

Ban đầu được thay thế bằng sai.

Đó là sự thật.

Sai và đúng đều trở thành sai.

Vì vậy, câu lệnh while sẽ chấm dứt.

Bởi vì biểu thức boolean phức hợp cuối cùng.

Nếu bất kỳ một trong các biểu thức con trở thành sai, thì biểu thức boolean phức hợp cuối cùng sẽ trở thành sai.

Trong khi đó trong trường hợp ví dụ đầu tiên.

Thay vì sử dụng lá.

Có nghĩa là vòng lặp.

Và phần khác, chúng ta chỉ sử dụng câu lệnh break.

Vậy kết luận cuối cùng là phiên bản không có phanh.

Giới thiệu vòng lặp biến boolean và logic điều khiển vòng lặp phức tạp hơn một chút.

Phiên bản không ngắt sử dụng nhiều bộ nhớ hơn và nhiều thời gian hơn để thực thi.

Bộ nhớ bổ sung này là không đáng kể.

Và ngoại trừ các ứng dụng chuyên dụng hiếm hoi, thời gian thực hiện sẽ tăng thêm.

Không thể nhận thấy.

Trong hầu hết các trường hợp, vấn đề quan trọng hơn là logic điều khiển càng phức tạp.

Đối với một phần mã nhất định, mã càng khó viết chính xác.

Trong một số trường hợp, mặc dù nó vi phạm nguyên tắc một điểm vào duy nhất, một điểm thoát duy nhất.

câu lệnh break đơn giản là một lựa chọn điều khiển vòng lặp mong muốn.

Vì vậy, hãy làm cho nó thật đơn giản với câu lệnh break đơn giản bên trong bất kỳ vòng lặp nào mà không làm phức tạp hơn.

Giống như một biểu thức Boolean ghép.

Chúng ta cũng có thể sử dụng câu lệnh break bên trong vòng lặp for.

Vì vậy, đây là ví dụ minh họa cách sử dụng câu lệnh break.

Thoát khỏi vòng lặp for sớm.

Chúng ta đã biết cách đếm các nguyên âm trong bất kỳ chuỗi hoặc từ nào.

Bây giờ chúng tôi đang thêm phần bổ sung ở đây.

Tham gia câu lệnh if và sử dụng dấu ngắt bên trong câu lệnh if.

Nếu chúng ta nhìn vào phần khác.

Bất cứ khi nào ký tự trở thành X hoặc x nhỏ.

Rồi họ.

Phần thân của nhóm LC bao gồm câu lệnh break.

Cái nào sẽ được kích hoạt và.

Vòng lặp for sẽ kết thúc.

Word là biến được người dùng nhập vào và là biến ban đầu.

Chúng tôi sẽ đếm là số không.

Nhưng hướng nội.

Nếu C bằng A hoặc A nhỏ viết hoa E hoặc e nhỏ.

A.

E.

tôi.

Ô.

U.

In các nguyên âm và đếm.

Số nguyên âm sử dụng số gạch dưới nguyên âm bằng với số gạch dưới bằng lời nói.

Đếm cộng một.

Giả sử nếu chuỗi bao gồm X.

Sau đó, đây là câu lệnh if khác.

Sẽ được đánh giá nếu điều kiện trở thành đúng.

nhéo.

Nếu chuỗi bao gồm x hoặc x nhỏ thì câu lệnh break sẽ được kích hoạt.

Nội dung câu lệnh ElseIf sẽ chỉ được đánh giá nếu điều kiện trở thành đúng.

Bên trong cơ thể.

Chúng tôi có tuyên bố phá vỡ.

Khi các tệp X trong chuỗi chương trình sẽ chạy.

Sẽ.

Thoát khỏi vòng lặp có nghĩa là luồng điều khiển sẽ thoát khỏi vòng lặp for.

Và nó sẽ chỉ hiển thị số nguyên âm.

Lên đến.

Cái.

Có nghĩa là nó sẽ đếm các nguyên âm.

Đó là trước chữ X trong bất kỳ chuỗi nào.

Hãy để chúng tôi chạy mã này và hiểu theo cách tốt hơn.

Chúng ta hãy nhập tên Pruthvi.

Chỗ trống ở đây không có chữ X nên không có chuyện phá vỡ câu nói.

Chúng ta có bốn nguyên âm E.

E i và a a.

Trên thực tế ba chữ A đã được lặp lại hai lần.

Hãy để chúng tôi chạy mã một lần nữa.

Và lần này hãy để chúng tôi.

Đi vào.

Từ bao gồm ký tự X.

Ví dụ.

Chúng tôi có.

Máy Xerox.

Nhìn ra đây.

Ở thế giới này.

Câu của chúng ta có E là nguyên âm, E và E Sau đó chúng ta có X.

Vì vậy anh ấy đã thắng a.

Nguyên âm thứ hai.

Và một lần nữa, e.

Lần đếm thứ ba.

Và sau đó chúng ta có X.

Bất cứ khi nào.

Cái.

Luồng chương trình hoặc luồng điều khiển tìm thấy.

Nó sẽ chấm dứt.

Vòng lặp for vì câu lệnh break.

Và các nhân vật còn lại trong.

Câu sẽ không được đánh giá.

Hãy để chúng tôi kiểm tra bằng cách nhấn enter.

Vì vậy hãy nhìn vào đây.

Vâng.

Ye và E chỉ có ba nguyên âm được tính.

Sau đó chúng ta có X trong câu lệnh khác.

Chúng ta có C nếu C bằng x hoặc C bằng x nhỏ.

Kích hoạt câu lệnh break.

Bỏ lỡ.

Phần thân của câu lệnh khác sẽ được đánh giá bên trong phần thân.

Chúng tôi có một tuyên bố nghỉ giải lao.

Vì vậy câu lệnh break này sẽ kết thúc vòng lặp for.

Cho đến nay vòng lặp là.

Thực ra làm thế nào để đếm các nguyên âm.

Toàn bộ chuỗi.

Nhưng vì tuyên bố phá vỡ.

Khi điều kiện trở thành đúng.

Có nghĩa là khi phần khó nắm bắt tìm thấy ký tự X.

Khi đó điều kiện trở thành đúng.

Khi đó câu lệnh break sẽ được kích hoạt.

Và câu lệnh break này sẽ chấm dứt.

Dòng chảy chương trình.

Vì vậy đây là cách hoạt động của câu lệnh break trong Python.

Câu lệnh break rất hữu ích khi có tình huống phát sinh đòi hỏi phải thoát khỏi vòng lặp ngay lập tức.

Vòng lặp for trong Python hoạt động khác với vòng lặp while.

Trong đó nó không có điều kiện rõ ràng để kiểm tra việc tiếp tục thực hiện.

Bởi vì trong vòng lặp for chúng ta chỉ có đối tượng có thể lặp lại được.

Rõ ràng.

Được rồi.

Không có điều kiện có nghĩa là không có điều kiện rõ ràng.

Bản thân đối tượng có thể lặp lại là chính nó hoạt động như một điều kiện rõ ràng.

Chúng ta phải sử dụng câu lệnh break nếu muốn thoát sớm vòng lặp for trước khi nó hoàn thành.

lần lặp xác định.

Vòng lặp for là một vòng lặp xác định, có nghĩa là người lập trình có thể xác định trước số lần lặp

vòng lặp sẽ thực hiện.

Tuyên bố break có khả năng phá vỡ khả năng dự đoán này.

Vì lý do này, các lập trình viên ít sử dụng câu lệnh break trong vòng lặp for hơn.

Và chúng thường đóng vai trò như một lối thoát khỏi một tình huống tồi tệ cứ lặp đi lặp lại.

Điều đó có thể làm cho tồi tệ hơn.

Vì vậy, nó được khuyến khích sử dụng.

Bất kỳ cái nào khác.

Câu lệnh ngoại trừ câu lệnh break.

Nhưng trong cả hai mã logic.

Để bỏ qua một phần của.

Mã hoặc một số.

Một phần của mã.

Nếu điều kiện trở thành đúng.

Ở giữa.

Vòng lặp.

Tuyên bố tiếp tục sẽ phục vụ điều này.

Loại ứng dụng.

Trong bài học tiếp theo, chúng ta sẽ xem cách làm việc với câu lệnh continue.