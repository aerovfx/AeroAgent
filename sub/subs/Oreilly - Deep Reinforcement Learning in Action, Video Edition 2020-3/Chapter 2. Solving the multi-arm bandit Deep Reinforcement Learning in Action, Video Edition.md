# Chương 2. Giải quyết tên cướp nhiều tay Học tăng cường sâu trong thực tế, Phiên bản video

---

Mục 2.2 Giải quyết tên cướp nhiều tay

Bây giờ chúng ta đã sẵn sàng để bắt đầu với một bài toán học tăng cường thực sự và xem xét

các khái niệm và kỹ năng liên quan cần thiết để giải quyết vấn đề này khi chúng ta tiếp tục.

Nhưng trước khi chúng ta quá mơ mộng về việc xây dựng thứ gì đó như AlphaGo, trước tiên chúng ta hãy xem xét một cách đơn giản

vấn đề.

Giả sử bạn đang ở một sòng bạc và trước mặt bạn là 10 máy đánh bạc có hình dáng hào nhoáng.

ký hiệu có nội dung "Chơi miễn phí, khoản thanh toán tối đa là 10 đô la".

Ồ, không tệ.

Tò mò, bạn hỏi một nhân viên chuyện gì đang xảy ra, vì nó có vẻ quá tốt để có thể

đúng, và cô ấy nói "Điều đó thực sự đúng, chơi bao nhiêu tùy thích, hoàn toàn miễn phí.

Mỗi máy đánh bạc được đảm bảo mang lại cho bạn phần thưởng từ $0 đến $10.

Ồ, nhân tiện, hãy giữ điều này cho riêng bạn, nhưng 10 máy đánh bạc đó đều có một cách khác nhau.

khoản thanh toán trung bình, vì vậy hãy cố gắng tìm ra cái nào mang lại nhiều phần thưởng trung bình nhất và

bạn sẽ kiếm được rất nhiều tiền".

Đây là loại sòng bạc gì?

Ai quan tâm, hãy cùng tìm ra cách kiếm được nhiều tiền nhất.

Ồ, nhân tiện, đây là một trò đùa.

Tên gọi khác của máy đánh bạc là gì?

Một tên cướp một tay, hiểu không?

Nó có một cánh tay, một đòn bẩy và thường ăn cắp tiền của bạn.

Chúng ta có thể gọi tình huống của mình là vấn đề tên cướp 10 vũ trang hoặc vấn đề tên cướp vũ trang N hơn

nói chung, trong đó N là số lượng máy đánh bạc.

Mặc dù vấn đề này cho đến nay nghe có vẻ khá viển vông, nhưng sau này bạn sẽ thấy rằng những chiếc vũ khí N này

vấn đề tên cướp, hay tên cướp nhiều tay, có một số ứng dụng rất thực tế.

Hãy trình bày lại vấn đề của chúng ta một cách chính thức hơn.

Chúng ta có N hành động có thể xảy ra, ở đây N=10, trong đó một hành động có nghĩa là kéo cánh tay hoặc đòn bẩy của

một máy đánh bạc cụ thể và tại mỗi lần chơi, K, của trò chơi này, chúng ta có thể chọn một đòn bẩy duy nhất

để kéo.

Sau khi thực hiện hành động A, chúng ta sẽ nhận được phần thưởng là RK, phần thưởng ở lượt chơi K.

Mỗi đòn bẩy có một khả năng phân bổ xác suất duy nhất về các khoản thanh toán, phần thưởng.

Ví dụ: nếu chúng ta có 10 máy đánh bạc và chơi nhiều trò chơi thì máy đánh bạc số 3 có thể

đưa ra phần thưởng trung bình là 9 đô la, trong khi máy đánh bạc số 1 chỉ đưa ra phần thưởng trung bình

phần thưởng 4$.

Tất nhiên, vì phần thưởng ở mỗi lần chơi mang tính xác suất nên có thể số đòn bẩy

1 sẽ tình cờ mang lại cho chúng tôi phần thưởng trị giá 9 đô la cho một lần chơi.

Nhưng nếu chơi nhiều trò chơi, chúng ta kỳ vọng trung bình rằng máy đánh bạc số 1 sẽ được liên kết.

với phần thưởng thấp hơn số 3.

Chiến lược của chúng ta là chơi một vài lần, chọn các đòn bẩy khác nhau và quan sát

phần thưởng cho mỗi hành động.

Sau đó, chúng tôi muốn chỉ chọn đòn bẩy có phần thưởng trung bình lớn nhất được quan sát.

Vì vậy, chúng ta cần một khái niệm về phần thưởng mong đợi khi thực hiện hành động A, dựa trên hành động trước đó của chúng ta.

vở kịch.

Chúng ta sẽ gọi phần thưởng mong đợi này là QK của A về mặt toán học.

Bạn đưa ra cho hàm một hành động, vì chúng ta đang chơi K và nó trả về phần thưởng mong đợi

vì đã thực hiện hành động đó.

Điều này được thể hiện chính thức ở đây.

Bảng 2.2, cách tính phần thưởng mong đợi trong toán học và mã giả.

Xem hình bảng.

Nghĩa là, phần thưởng mong đợi ở trò chơi K cho hành động A là trung bình số học của tất cả

phần thưởng trước đó chúng tôi đã nhận được khi thực hiện hành động A.

Do đó, những hành động và quan sát trước đây của chúng ta sẽ ảnh hưởng đến những hành động trong tương lai của chúng ta.

Chúng ta thậm chí có thể nói rằng một số hành động trước đây sẽ củng cố các hành động hiện tại và tương lai của chúng ta.

Nhưng chúng ta sẽ quay lại vấn đề này sau.

Hàm QK của A được gọi là hàm giá trị vì nó cho chúng ta biết giá trị của một thứ gì đó.

Đặc biệt, nó là hàm giá trị hành động vì nó cho chúng ta biết giá trị của việc lấy một

hành động cụ thể.

Vì chúng ta thường biểu thị hàm này bằng ký hiệu Q nên nó cũng thường được gọi là Q.

chức năng.

Chúng ta sẽ quay lại đánh giá các hàm sau và đưa ra một định nghĩa phức tạp hơn,

nhưng điều này sẽ đủ cho bây giờ.

Mục 2.2.1 Thăm dò khai thác.

Khi mới bắt đầu chơi, chúng ta cần chơi trò chơi và quan sát phần thưởng chúng ta nhận được

các máy móc khác nhau.

Chúng ta có thể gọi đây là chiến lược khám phá vì về cơ bản chúng ta khám phá ngẫu nhiên

kết quả hành động của chúng ta.

Điều này trái ngược với một chiến lược khác mà chúng ta có thể sử dụng được gọi là khai thác, chiến lược này

có nghĩa là chúng tôi sử dụng kiến thức hiện tại của mình về chiếc máy nào dường như tạo ra nhiều phần thưởng nhất

và tiếp tục chơi cái máy đó.

Chiến lược tổng thể của chúng tôi cần bao gồm một số mức độ khai thác, lựa chọn phương án tốt nhất

đòn bẩy dựa trên những gì chúng tôi biết cho đến nay và một số khám phá, chọn đòn bẩy ngẫu nhiên

để chúng ta có thể tìm hiểu thêm.

Sự cân bằng hợp lý giữa khai thác và thăm dò sẽ rất quan trọng để tối đa hóa phần thưởng của chúng tôi.

Làm thế nào chúng ta có thể đưa ra một thuật toán để tìm ra máy đánh bạc nào có điểm trung bình lớn nhất

thanh toán?

Chà, thuật toán đơn giản nhất là chỉ chọn hành động liên quan đến mức cao nhất

giá trị Q.

Ví dụ 2.3, Tính toán hành động tốt nhất với phần thưởng mong đợi (Xem bảng hình).

Danh sách sau đây cho thấy nó là mã Python 3 hợp pháp.

Liệt kê 2.1, Tìm các hành động tốt nhất với phần thưởng mong đợi trong Python 3.

Chúng ta sử dụng hàm Qk(A) trên cho tất cả các hành động có thể và chọn hành động mà

trả về phần thưởng trung bình tối đa.

Vì Qk(A) phụ thuộc vào bản ghi các hành động trước đó của chúng ta và phần thưởng liên quan của chúng, điều này

phương thức sẽ không đánh giá các hành động mà chúng ta chưa khám phá.

Vì vậy, trước đây chúng ta có thể đã thử sử dụng đòn bẩy số 1 và số 3 và nhận thấy rằng đòn bẩy

số 3 mang lại cho chúng tôi phần thưởng cao hơn.

Nhưng với phương pháp này, chúng ta sẽ không bao giờ nghĩ đến việc thử một đòn bẩy khác, chẳng hạn như số 6, mà không biết

đối với chúng tôi, thực sự mang lại phần thưởng trung bình cao nhất.

Phương pháp đơn giản là chọn đòn bẩy tốt nhất mà chúng ta biết cho đến nay được gọi là đòn bẩy tham lam.

hoặc phương pháp khai thác.

Phần 2.2.2, Chiến lược tham lam của Epsilon.

Chúng ta cần khám phá những đòn bẩy khác, những máy đánh bạc khác để khám phá ra sự thật

hành động tốt nhất.

Một sửa đổi đơn giản đối với thuật toán trước đây của chúng tôi là thay đổi nó thành thuật toán tham lam epsilon,

sao cho với xác suất epsilon, chúng ta sẽ chọn ngẫu nhiên một hành động A và

thời gian còn lại, xác suất, 1 trừ epsilon, chúng ta sẽ chọn đòn bẩy tốt nhất dựa trên những gì

chúng ta hiện đã biết từ những vở kịch trước đây.

Hầu hết chúng ta sẽ chơi tham lam, nhưng đôi khi chúng ta sẽ mạo hiểm và chọn một con đường.

đòn bẩy ngẫu nhiên để xem điều gì sẽ xảy ra.

Tất nhiên, kết quả sẽ ảnh hưởng đến những hành động tham lam trong tương lai của chúng ta.

Hãy xem liệu chúng ta có thể giải quyết vấn đề này bằng mã bằng Python hay không.

Phần 2.2, Chiến lược tham lam của Epsilon để lựa chọn hành động.

Trong ví dụ về sòng bạc này, chúng ta sẽ giải bài toán tên cướp 10 tay, do đó n bằng 10.

Chúng tôi cũng đã xác định một mảng có độ dài n chứa đầy các số float ngẫu nhiên có thể hiểu được

như xác suất.

Mỗi vị trí trong mảng probs tương ứng với một nhánh, đây là một hành động có thể thực hiện được.

Ví dụ: phần tử đầu tiên có vị trí chỉ mục 0, vì vậy hành động 0 là nhánh 0.

Mỗi nhánh có một xác suất liên quan để xác định số tiền thưởng mà nó trả.

Cách chúng tôi đã chọn để triển khai phân phối xác suất phần thưởng cho mỗi nhánh là

cái này.

Mỗi nhánh sẽ có xác suất, ví dụ: 0,7 và phần thưởng tối đa là 10 đô la.

Chúng ta sẽ thiết lập một vòng lặp for lên tới 10 và ở mỗi bước nó sẽ thêm 1 vào phần thưởng nếu

một lần thả nổi ngẫu nhiên nhỏ hơn xác suất của cánh tay.

Do đó, ở vòng lặp đầu tiên, nó tạo thành một số float ngẫu nhiên, ví dụ: 0,4.

0,4 nhỏ hơn 0,7 nên phần thưởng cộng bằng 1.

Ở lần lặp tiếp theo, nó tạo thành một số float ngẫu nhiên khác, ví dụ 0,6, cũng là

nhỏ hơn 0,7 nên phần thưởng cộng bằng 1.

Điều này tiếp tục cho đến khi chúng tôi hoàn thành 10 lần lặp và sau đó chúng tôi trả lại tổng phần thưởng cuối cùng,

có thể là bất cứ thứ gì từ 0 đến 10.

Với xác suất nhánh là 0,7, phần thưởng trung bình khi thực hiện điều này đến vô cùng sẽ là

7, nhưng trong bất kỳ lần chơi nào, nó có thể nhiều hơn hoặc ít hơn.

Liệt kê 2.3, xác định hàm phần thưởng.

Bạn có thể kiểm tra điều này bằng cách chạy nó.

Xem mã này.

Đầu ra này cho thấy rằng việc chạy mã này 2000 lần với xác suất 0,7 thực sự mang lại

cho chúng tôi phần thưởng trung bình là gần 7.

Xem biểu đồ trong hình 2.2.

Hình 2.2.

Việc phân phối phần thưởng cho một tên cướp không có vũ khí được mô phỏng với xác suất xuất chi là 0,7.

Chức năng tiếp theo mà chúng ta sẽ xác định là chiến lược tham lam của chúng ta trong việc chọn nhánh tốt nhất cho đến nay.

Chúng ta cần một cách để theo dõi cánh tay nào đã được kéo và phần thưởng thu được là gì

là.

Ngây thơ, chúng ta có thể chỉ cần có một danh sách và thêm các quan sát như "phần thưởng cánh tay", cho

ví dụ 2, 9, cho biết chúng tôi đã chọn nhánh 2 và nhận được phần thưởng 9.

Danh sách này sẽ dài hơn khi chúng tôi chơi trò chơi.

Tuy nhiên, có một cách tiếp cận đơn giản hơn nhiều vì chúng ta thực sự chỉ cần theo dõi

phần thưởng trung bình cho mỗi cánh tay.

Chúng ta không cần phải lưu trữ từng quan sát.

Hãy nhớ lại rằng để tính giá trị trung bình của một danh sách các số x_i, được lập chỉ mục bởi i, chúng ta chỉ cần

tổng hợp tất cả các giá trị x_i rồi chia cho số x_i, chúng ta sẽ biểu thị

k.

Giá trị trung bình thường được biểu thị bằng chữ cái Hy Lạp, mu.

Xem biểu hiện này.

Ký hiệu chữ hoa của Hy Lạp, sigma, được sử dụng để biểu thị phép tính tổng.

Ký hiệu i bên dưới có nghĩa là chúng ta tính tổng từng phần tử, x_i.

Về cơ bản, nó tương đương với toán học của một vòng lặp for.

Xem mã này.

Nếu chúng tôi đã có phần thưởng trung bình, mu, cho một nhánh cụ thể, chúng tôi có thể cập nhật mức trung bình này

khi chúng ta nhận được phần thưởng mới bằng cách tính lại mức trung bình.

Về cơ bản, chúng ta cần hoàn tác mức trung bình và sau đó tính toán lại nó.

Để hoàn tác nó, chúng ta nhân mu với tổng số giá trị k.

Tất nhiên, điều này chỉ cho chúng ta tổng chứ không phải tập hợp giá trị ban đầu.

Bạn không thể hoàn tác một khoản tiền.

Nhưng tổng số là những gì chúng ta cần để tính lại giá trị trung bình với một giá trị mới.

Chúng ta chỉ cần cộng tổng này vào giá trị mới rồi chia cho k cộng 1, tổng số mới của

các giá trị.

Xem biểu hiện này.

Chúng ta có thể sử dụng phương trình này để liên tục cập nhật phần thưởng trung bình quan sát được cho mỗi nhánh như

chúng tôi thu thập dữ liệu mới.

Và theo cách này chúng ta chỉ cần theo dõi hai số cho mỗi nhánh k, số

giá trị quan sát được và mu, giá trị trung bình hiện tại.

Chúng ta có thể dễ dàng lưu trữ cái này trong một mảng có kích thước 10 x 2, giả sử chúng ta có 10 cánh tay.

Chúng ta sẽ gọi mảng này là bản ghi.

Xem mã này.

Cột đầu tiên của mảng này sẽ lưu trữ số lần mỗi cánh tay được kéo,

và cột thứ hai sẽ lưu trữ phần thưởng trung bình đang chạy.

Hãy viết một hàm cập nhật bản ghi, đưa ra một hành động và phần thưởng mới.

Liệt kê 2.4, cập nhật bản ghi khen thưởng.

Hàm này lấy mảng bản ghi, một hành động, là giá trị chỉ mục của nhánh và một

quan sát phần thưởng mới.

Để cập nhật phần thưởng trung bình, nó chỉ cần thực hiện chức năng toán học mà chúng tôi đã mô tả trước đây,

và sau đó tăng bộ đếm ghi lại số lần cánh tay đó được kéo.

Tiếp theo, chúng ta cần một hàm sẽ chọn cánh tay nào để kéo.

Chúng tôi muốn nó chọn nhánh có liên quan đến phần thưởng trung bình cao nhất, vì vậy tất cả những gì chúng tôi cần

việc cần làm là tìm hàng trong mảng bản ghi có giá trị lớn nhất trong cột 1.

Chúng ta có thể dễ dàng thực hiện việc này bằng cách sử dụng hàm argmax tích hợp sẵn của Numpy, hàm này chứa một mảng,

tìm giá trị lớn nhất trong mảng và trả về vị trí chỉ mục của nó.

Liệt kê 2.5, tính toán hành động tốt nhất.

Bây giờ chúng ta có thể vào vòng lặp chính để chơi trò chơi tên cướp có vũ trang N.

Nếu một số ngẫu nhiên lớn hơn tham số epsilon, chúng tôi chỉ tính toán hành động tốt nhất

sử dụng hàm get_best_arm và thực hiện hành động đó.

Nếu không, chúng tôi thực hiện một hành động ngẫu nhiên để đảm bảo một số lượng khám phá.

Sau khi chọn nhánh, chúng ta sử dụng hàm get_reward và quan sát giá trị phần thưởng.

Sau đó chúng tôi cập nhật mảng bản ghi với quan sát mới này.

Chúng tôi lặp lại quá trình này nhiều lần và nó sẽ liên tục cập nhật mảng bản ghi.

Cánh tay có xác suất nhận thưởng cao nhất cuối cùng sẽ được chọn thường xuyên nhất, vì

nó sẽ đưa ra phần thưởng trung bình cao nhất.

Chúng tôi đã đặt nó phát 500 lần trong danh sách sau và hiển thị biểu đồ phân tán matplotlib

về phần thưởng trung bình cho các vở kịch.

Hy vọng rằng chúng ta sẽ thấy rằng phần thưởng trung bình sẽ tăng lên khi chúng ta chơi nhiều lần hơn.

Liệt kê 2.6, giải quyết tên cướp có vũ trang N.

Như bạn có thể thấy trong hình 2.3, phần thưởng trung bình thực sự được cải thiện sau nhiều lần chơi.

Thuật toán của chúng tôi đang học hỏi, nó đang được củng cố bởi những lần chơi hay trước đó, tuy nhiên nó vẫn như vậy

một thuật toán đơn giản.

Hình 2.3.

Biểu đồ này cho thấy phần thưởng trung bình cho mỗi lần chơi máy đánh bạc tăng theo thời gian,

cho thấy chúng tôi đang học thành công cách giải quyết vấn đề tên cướp có vũ trang N.

Vấn đề chúng ta đang xem xét ở đây là một vấn đề dừng, bởi vì xác suất phần thưởng cơ bản

phân phối cho vũ khí không thay đổi theo thời gian.

Chúng ta chắc chắn có thể xem xét một biến thể của bài toán này khi điều này không đúng, một bài toán không cố định.

vấn đề.

Trong trường hợp này, một sửa đổi đơn giản sẽ là cho phép cập nhật các quan sát phần thưởng mới

giá trị phần thưởng trung bình được lưu trữ trong bản ghi một cách sai lệch, do đó nó sẽ là giá trị có trọng số

trung bình, có trọng số đối với quan sát mới nhất.

Bằng cách này, nếu mọi thứ thay đổi theo thời gian, chúng ta có thể theo dõi chúng ở một mức độ nào đó.

Chúng tôi sẽ không triển khai biến thể phức tạp hơn một chút này ở đây, nhưng chúng tôi sẽ gặp phải biến thể không cố định

những vấn đề sau này trong cuốn sách.

Mục 2.2.3.

Chính sách lựa chọn của Softmax Hãy tưởng tượng một loại vấn đề khác về tên cướp.

Một bác sĩ mới được đào tạo chuyên điều trị các bệnh nhân bị đau tim.

Cô có 10 phương án điều trị, trong đó cô chỉ được chọn một phương án để điều trị cho mỗi bệnh nhân.

cô ấy nhìn thấy.

Vì lý do nào đó, tất cả những gì cô ấy biết là 10 phương pháp điều trị này có hiệu quả và cách điều trị khác nhau.

hồ sơ rủi ro để điều trị các cơn đau tim.

Cô vẫn chưa biết cái nào là tốt nhất.

Chúng ta có thể sử dụng thuật toán tên cướp N-armed từ giải pháp trước đó, nhưng chúng ta có thể muốn

để xem xét lại chính sách tham lam epsilon của chúng ta về việc thỉnh thoảng chọn ngẫu nhiên một phương pháp điều trị.

Trong vấn đề mới này, việc lựa chọn ngẫu nhiên một phương pháp điều trị có thể khiến bệnh nhân tử vong chứ không chỉ mất đi

một số tiền.

Chúng tôi thực sự muốn đảm bảo rằng chúng tôi không chọn cách điều trị tồi tệ nhất, nhưng chúng tôi vẫn muốn một số

khả năng khám phá các lựa chọn của chúng tôi để tìm ra lựa chọn tốt nhất.

Đây là nơi lựa chọn softmax có thể phù hợp nhất.

Thay vì chỉ chọn một hành động ngẫu nhiên trong quá trình khám phá, softmax cho chúng ta xác suất

phân phối trên các lựa chọn của chúng tôi.

Tùy chọn có xác suất lớn nhất sẽ tương đương với hành động cánh tay tốt nhất trong

giải pháp trước đó, nhưng nó cũng sẽ cho chúng ta một số ý tưởng về giải pháp thứ hai và thứ ba

hành động tốt nhất chẳng hạn.

Bằng cách này, chúng ta có thể chọn ngẫu nhiên để khám phá các lựa chọn khác trong khi tránh được điều tồi tệ nhất

các tùy chọn vì chúng sẽ được ấn định xác suất rất nhỏ hoặc thậm chí bằng không.

Đây là phương trình softmax.

Bảng 2.4 Phương trình Softmax (Xem hình bảng)

Pr(A) là hàm chấp nhận vectơ, mảng giá trị hành động và trả về xác suất

phân phối trên các hành động, sao cho các hành động có giá trị cao hơn có xác suất cao hơn.

Ví dụ: nếu mảng giá trị hành động của bạn có bốn hành động có thể thực hiện được và tất cả chúng đều hiện đang

có cùng giá trị, giả sử khi A bằng mảng 10, 10, 10, 10 thì Pr(A) sẽ

bằng mảng 0,25, 0,25, 0,25, 0,25.

Nói cách khác, tất cả các xác suất đều như nhau và phải có tổng bằng 1.

Tử số của phân số lũy thừa mảng giá trị hành động chia cho một tham số,

tau, tạo ra một vectơ có cùng kích thước, tức là độ dài, làm đầu vào.

Mẫu số tính tổng theo lũy thừa của từng giá trị hành động riêng lẻ chia cho

tau, mang lại một số duy nhất.

Tau là một tham số được gọi là nhiệt độ để chia tỷ lệ phân bố xác suất của các hành động.

Nhiệt độ cao sẽ khiến xác suất rất giống nhau, trong khi nhiệt độ thấp

sẽ phóng đại sự khác biệt về xác suất giữa các hành động.

Việc chọn một giá trị cho tham số này đòi hỏi phải có sự phỏng đoán có căn cứ và một số lần thử và sai.

Hàm mũ toán học e lũy thừa của x là một hàm được gọi tới np.exp với dấu ba chấm

trong sự khó chịu.

Nó sẽ áp dụng hàm theo từng phần tử trên vectơ đầu vào.

Đây là cách chúng tôi thực sự viết hàm softmax trong Python.

Liệt kê 2.7, hàm softmax.

Khi chúng tôi triển khai vấn đề tên cướp 10 nhánh trước đó bằng softmax, chúng tôi không cần get_best_arm

hoạt động nữa.

Vì softmax tạo ra phân bố xác suất có trọng số cho các hành động có thể xảy ra của chúng ta,

chúng ta có thể chọn ngẫu nhiên các hành động theo xác suất tương đối của chúng.

Nghĩa là, hành động tốt nhất của chúng ta sẽ được chọn thường xuyên hơn vì nó sẽ có softmax cao nhất

xác suất, nhưng các hành động khác sẽ được chọn ở tần số thấp hơn.

Để thực hiện điều này, tất cả những gì chúng ta cần làm là áp dụng hàm softmax trên cột thứ hai,

chỉ số cột 1 của mảng bản ghi, vì đó là cột lưu trữ giá trị hiện tại

phần thưởng trung bình, giá trị hành động cho mỗi hành động.

Nó sẽ chuyển đổi các giá trị hành động này thành xác suất.

Sau đó, chúng ta sử dụng hàm np.random.choice, hàm này chấp nhận một mảng đầu vào tùy ý, x,

và một tham số p, đó là một mảng các xác suất tương ứng với mỗi phần tử trong x.

Vì bản ghi của chúng tôi được khởi tạo bằng tất cả các số 0, nên lúc đầu softmax sẽ trả về một phân bố đồng đều

trên tất cả các nhánh, nhưng sự phân bổ này sẽ nhanh chóng nghiêng về bất kỳ hành động nào có liên quan

với phần thưởng cao nhất.

Đây là một ví dụ về việc sử dụng softmax và hàm lựa chọn ngẫu nhiên.

Xem mã này.

Chúng ta sử dụng hàm numpy.arrange để tạo một mảng từ 0 đến 9, tương ứng với

chỉ số của mỗi nhánh, do đó hàm lựa chọn ngẫu nhiên sẽ trả về chỉ số nhánh theo

với vectơ xác suất được cung cấp.

Chúng ta có thể sử dụng vòng lặp đào tạo tương tự như chúng ta đã làm trước đây.

Chúng ta chỉ cần thay đổi phần chọn arm để nó sử dụng softmax thay vì get_best_arm là được

và chúng ta cần loại bỏ lựa chọn hành động ngẫu nhiên vốn là một phần của thói tham lam epsilon

chiến lược.

Liệt kê 2.8.

Lựa chọn hành động Softmax cho tên cướp không có vũ khí.

Lựa chọn hành động Softmax dường như hoạt động tốt hơn phương pháp tham lam epsilon cho vấn đề này,

như bạn có thể thấy từ hình 2.4.

Có vẻ như nó hội tụ một chính sách tối ưu nhanh hơn.

Nhược điểm của softmax là phải chọn tham số tau theo cách thủ công.

Softmax ở đây khá nhạy cảm với tau và phải mất một thời gian chơi với nó

tìm thấy một giá trị tốt.

Rõ ràng, với epsilon-greedy chúng ta phải đặt tham số epsilon, nhưng việc chọn tham số đó

trực quan hơn nhiều.

Hình 2.4.

Với chính sách softmax, thuật toán kẻ cướp không vũ trang có xu hướng hội tụ nhanh hơn trên

phần thưởng trung bình tối đa.