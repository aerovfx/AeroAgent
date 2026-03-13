# 3 -Policy gradient Methods (phần 2) đã dịch

---

Được rồi, trong video này chúng ta sẽ xem xét nguồn gốc của phương pháp gradient chính sách.

Vì vậy, về cơ bản chúng ta sẽ áp dụng những gì chúng ta đã mô tả trong bài giảng trước và chúng ta sẽ

áp dụng nhiều phép toán để tìm ra câu trả lời.

Vì vậy, đạo hàm gradient chính sách.

Được rồi, vì vậy nó có liên quan một chút.

Nó không quá khó, nhưng nếu bạn muốn, bạn sẽ không muốn trải qua bài toán này,

Tôi sẽ trình bày kết quả.

Và điều bạn có thể làm là bỏ qua tất cả trọng lượng ở phần cuối, hoặc có thể là bài giảng tiếp theo,

Tôi không biết việc này sẽ mất bao lâu nữa.

Nhưng hãy bỏ qua phần đó để xem điều này thực sự được triển khai như thế nào trong mã.

Nếu bạn không quan tâm đến việc điều này có nguồn gốc như thế nào.

Được rồi, chúng ta sẽ bắt đầu với định lý gradient chính sách, trong đó nói lên điều này.

Định lý gradient chính sách.

Được rồi, nó nói rằng nếu chúng ta có một chính sách thì nó sẽ được tham số hóa bởi theta.

Vì vậy, hãy giả vờ đó là tất cả trọng số của mạng lưới thần kinh.

Độ dốc của chính sách này sẽ tối ưu hóa chính sách này được đưa ra bởi biểu thức này.

Được rồi, vậy j là hàm của theta.

Đó là giá trị mong đợi của thứ mà chúng ta gọi là lợi thế.

Và sau đó chúng tôi lấy độ dốc của nhật ký của chính sách này.

Được rồi, và một số ghi chú.

Vì vậy, trong khóa học này, cũng như nhiều khóa học khác và các cuốn sách khác mà bạn thấy trực tuyến, bằng nhật ký, chúng tôi

nhật ký thực sự có ý nghĩa.

Vì vậy, nhật ký tự nhiên.

Cũng log cơ số E. Vậy ở đây có một đại lượng mà chúng ta chưa thảo luận.

Đây là lợi thế.

Vì vậy chúng ta sẽ nói về vấn đề này nhiều hơn ở phần sau của loạt bài giảng.

Nhưng bây giờ, tôi sẽ chỉ nói rằng thuật ngữ lợi thế này thực ra có thể có nhiều thứ.

Vì vậy, độ dốc chính sách không cho bạn biết nên sử dụng cái nào phù hợp.

Nó chỉ nói rằng có những lựa chọn khả thi để bạn thử.

Được rồi, vậy một số ví dụ có thể là, tôi sẽ không viết dấu bằng, nhưng bạn có thể quyết định

loại dấu hiệu nào là thích hợp nhất.

Tôi sẽ chỉ nói rằng nó có thể là sự trở lại bắt đầu từ trạng thái này trong phần này.

Vậy đây chỉ là tổng số phần thưởng thôi phải không?

Vậy R cộng gamma R nguyên tố cộng gamma bình phương, v.v.

Được rồi, vậy nó có thể chỉ là kết quả thực tế từ cặp trạng thái và hành động đó.

Một số lựa chọn khác là thay vì GE, chúng ta có thể sử dụng giá trị kỳ vọng của G.

Vì vậy, chúng ta có thể sử dụng Q.

Được rồi.

Và cách khác, chúng ta cũng có thể sử dụng QSA trừ V của S. Nói cách khác, thay vì trả về

bản thân nó là lợi nhuận kỳ vọng khi thực hiện hành động này trừ đi lợi nhuận kỳ vọng trung bình

trên tất cả các hành động, phải không?

Đó là V. Vậy thực hiện hành động này tốt hơn mức trung bình bao nhiêu?

Và vì vậy một số khác chúng ta có là R cộng gamma V của S prime trừ V của S.

Vì vậy thay vì Q, chúng ta sử dụng cái này.

Và chúng tôi cũng có cái gọi là phương pháp N bước.

Vì vậy N bước, thay vì chỉ sử dụng một phần thưởng, chúng tôi sử dụng nhiều phần thưởng.

Phải?

Vì vậy, ví dụ, R cộng gamma R nguyên tố cộng gamma R số nguyên tố kép cộng gamma bình phương, gamma lập phương.

V của S, có cái này sẽ là hai.

Không, nó sẽ bằng 3 trừ V của S.

Được rồi, nhưng chúng ta sẽ nói về điều đó nhiều hơn sau.

Được rồi?

Được rồi, bây giờ chúng ta hãy tìm hiểu làm thế nào để chúng ta thực sự lấy được gradient chính sách?

Được rồi.

Vì vậy chúng ta sẽ bắt đầu với điều gì đó rất rõ ràng.

Chúng tôi muốn làm gì khi phát một tập về môi trường học tập tăng cường

là chúng tôi muốn tối đa hóa tổng số phần thưởng trong một tập.

Được rồi?

Chúng tôi gần như đã biết điều này từ các phương pháp giải pháp trước đây mà chúng tôi đã xem xét.

Bây giờ có một số vấn đề với cách tiếp cận này, phải không?

Vì vậy, chúng tôi có thể nói điều chúng tôi muốn là mục tiêu của chúng tôi chỉ là giá trị mong đợi của những phần thưởng này

mà chúng tôi thu thập.

Tôi không viết ra gamma, chỉ viết bây giờ để đơn giản hơn.

Được rồi?

Vì vậy, đây là điểm khởi đầu cho những gì chúng tôi muốn tối ưu hóa.

Vấn đề với điều này là không thực sự rõ ràng điều này phụ thuộc vào chính sách như thế nào

thông số theta.

Nói cách khác, chúng ta không biết công thức của J này là gì. Vì vậy, vì chúng ta không biết

công thức của J theo theta, chúng ta không thể vi phân và viết mã rồi thực hiện phép tính thần kinh

tối ưu hóa độ dốc mạng.

Được rồi?

Vì vậy, nếu chúng ta không thể lấy đạo hàm, chúng ta không thể cập nhật trọng số.

Vì vậy mục tiêu của chúng ta là tìm ra gradient của cái này là gì.

Được rồi?

Và để làm được điều này, trước tiên chúng ta sẽ xác định một biểu tượng mới.

Vì vậy, chúng ta sẽ nói hãy để omega, đây sẽ là một chuỗi các cặp hành động trạng thái mà chúng ta gặp phải

trong một tập phim.

Lên đến STAT của bạn.

Và bằng cách sử dụng điều này, tôi sẽ nói sự trở lại.

Vì vậy, chúng ta đang làm quá tải hàm G này mọi lúc, nhưng không sao cả.

Vậy G của omega, đây sẽ là kết quả bạn nhận được khi thực hiện chuỗi này,

trải qua chuỗi trạng thái và hành động này.

Vì vậy, nó chỉ là một số, nó là một trong những chữ T, R lớn của STAT.

Được rồi?

Chỉ là tổng số phần thưởng trong suốt tập phim.

Được rồi?

Vì vậy, bây giờ bằng cách sử dụng điều này, chúng ta có thể xác định mục tiêu của mình rõ ràng hơn một chút.

Vì vậy hãy xác định mục tiêu.

Được rồi?

Vậy J của theta, đây sẽ là giá trị mong đợi, bởi vì đây là ngẫu nhiên, bởi vì chuỗi

hành động và trạng thái mà chúng ta sẽ thấy là ngẫu nhiên.

Vì vậy, G của omega đã đưa ra chính sách, pi theta.

Được rồi?

Vì vậy, không có gì thực sự đã thay đổi.

Chúng tôi chỉ đang sử dụng một số biểu tượng mới.

Vậy bây giờ chúng ta hãy nghĩ xem giá trị kỳ vọng là gì?

Giá trị kỳ vọng là tổng có trọng số, trong đó chúng ta tính trọng số của vật bên trong bằng xác suất

của thứ đó.

Phải?

Vì vậy, đây là một cách khác để viết ra mục tiêu này.

Chúng ta có thể nói tổng trên tất cả các quỹ đạo có thể.

Vì vậy chúng ta sẽ gọi nó là omega, nếu trước đây tôi gọi nó là sigma thì đó là một sai lầm.

Đây là omega.

Vì vậy, tất cả các quỹ đạo khác nhau có thể có, chúng tôi tính trọng số theo xác suất của quỹ đạo đó.

Và điều này cũng có thể phụ thuộc vào theta, vì điều đó sẽ quyết định hành động chúng ta thực hiện.

Và sau đó là G của omega.

Được rồi?

Vậy bây giờ câu hỏi cho bài giảng này về cơ bản sẽ là, xác suất này là bao nhiêu?

Được rồi.

Vậy hãy thử nghĩ xem, tôi muốn đưa điều này trở lại thế giới thực một chút.

Một số ví dụ về điều này, phải không?

Bởi vì nó có thể hơi trừu tượng một chút.

Vì vậy, nếu bạn tưởng tượng chúng ta có một thế giới lưới, giả sử, đây là thế giới lưới cổ điển từ

khóa học tiên quyết của chúng tôi.

Vậy đây là bức tường, bạn không thể vào đó được.

Đây là điểm khởi đầu của các đại lý của bạn.

Và cuối cùng, bạn nhận được phần thưởng cộng một ở đây và phần thưởng trừ một ở đây.

Và đó là những trạng thái cuối cùng.

Được rồi?

Vì vậy, một số ví dụ về quỹ đạo là, lên, lên, phải, phải, phải.

Vì vậy, nó sẽ lên, lên, phải, phải, phải, phải, và sau đó bạn nhận được một cộng.

Vì vậy, đó là một quỹ đạo có thể.

Và bạn có thể viết ra chuỗi các trạng thái và hành động nếu muốn, nhưng hơi mất thời gian.

phức tạp.

Tôi đã làm điều này trong các phiên bản trước của các khóa học này, nhưng bây giờ tôi sẽ không bận tâm làm điều đó nữa.

Vì vậy, ví dụ, đúng, bạn có thể gọi cái này là một, hai, ba cho các hàng, một, hai,

ba, bốn cho các cột.

Và sau đó, bạn biết đấy, trạng thái một sẽ là một, một, trạng thái hai sẽ là một, hai, hoặc vâng,

một, hai, v.v.

Vì vậy, bạn có thể làm điều đó.

Tôi sẽ không bận tâm vì tôi nghĩ bạn hiểu điều đó.

Được rồi?

Vì vậy, một quỹ đạo khả dĩ khác sẽ là, chẳng hạn, phải, phải, lên, lên, phải.

Và bạn cũng sẽ nhận được một điểm cộng, phải không?

Vậy phải, phải, lên, lên, phải, và bạn cũng được cộng một, phải, phải, lên, phải,

và bạn cũng có thể viết ra các trạng thái nếu muốn.

Được rồi?

Vậy một quỹ đạo khả dĩ khác là phải, phải, phải, lên, và trong trường hợp đó, bạn sẽ

thua trò chơi mà bạn nhận được một điểm trừ.

Vậy phải, phải, phải, lên, bạn được trừ một.

Vì vậy, đây là tất cả các giá trị có thể có hoặc các trường hợp của omega.

Vì vậy, các trường hợp có thể có của omega.

Và vì vậy điều chúng ta đang nói ở đây, số tiền này, là chúng ta phải cộng tất cả những thứ có thể có này

omega khác nhau.

Và điều đó sẽ cho chúng ta câu trả lời.

Được rồi?

Được rồi.

Và vì vậy mục tiêu của chúng ta là nghĩ xem làm cách nào để tìm được xác suất này?

Được rồi.

Vì vậy, đây là nơi tất cả các phép toán bắt đầu.

Vì vậy, ngay dưới đây, toán học bắt đầu.

Vậy là chúng ta đã hoàn thành xong tất cả các khái niệm.

Bây giờ chúng ta sẽ làm việc với phương trình này thêm một chút.

Vì vậy, chúng tôi sẽ lấy những gì chúng tôi có.

Vậy j là tổng trọng số của g.

Và điều chúng ta sắp làm là lấy độ dốc của cả hai cạnh.

Được rồi?

Vậy gradient của j, chúng ta chỉ lấy gradient của cạnh bên kia.

Một phép toán đơn giản cho đến nay.

Vậy p omega theta g omega.

Được rồi?

Vì vậy, một điều chúng ta có thể làm là di chuyển gradient bên trong tổng.

Được rồi, điều đó luôn được cho phép.

Tôi nghĩ vậy.

Được rồi.

Và nhân tiện, một điều cần lưu ý là g không phụ thuộc trực tiếp vào theta.

Được rồi?

Nó chỉ phụ thuộc vào những trạng thái và hành động mà chúng ta thực hiện.

Hoặc trạng thái chúng ta đang ở và những hành động chúng ta làm.

Và vì phần thưởng, chúng ta chỉ đảm nhận các hàm S và A. Trong mọi trường hợp,

không quá quan trọng.

Vì vậy, bước tiếp theo ở đây trong đạo hàm này là chúng ta sẽ nhân phần trên và

phía dưới cùng một điều.

Cụ thể, chúng ta sẽ nhân với p của omega theta p của omega theta.

Được rồi?

Vì vậy, điều đó mang lại cho chúng tôi điều này.

Vì vậy, chúng tôi chỉ có điều tương tự nhiều lần.

Nhưng bây giờ chúng ta sẽ sử dụng một thủ thuật.

Vì vậy chúng ta sẽ di chuyển một trong những người này.

Đưa cái đó cho anh chàng đó.

Được rồi?

Vì vậy, nó sẽ là một số omega.

Vì vậy, bây giờ chúng tôi chỉ có một trong những thứ này ở trên cùng.

Và sau đó chúng ta có hai thứ này cùng nhau.

Trên cùng một điều.

G của omega.

Được rồi.

Và bây giờ điều chúng ta sắp làm là áp dụng ngược lại quy tắc dây chuyền.

Vì vậy, bạn nhớ lại từ nghiên cứu tính toán của bạn.

Vì vậy, từ Calc.

Độ dốc của log của hàm giống như độ dốc của hàm chia

theo chức năng.

Được rồi?

Và vì vậy nếu bạn không nhớ nó đến từ đâu, chúng tôi sẽ thực hiện nó rất nhanh.

Vì vậy, chúng ta sẽ thực hiện nó ở dạng vô hướng để làm cho nó đơn giản hơn nữa.

Vì vậy, giả sử chúng ta có y bằng ln f.

Được rồi?

Và sau đó chúng ta lấy số mũ của cả hai vế.

Vậy e mũ y bằng f.

Được rồi?

Và bây giờ chúng ta muốn lấy đạo hàm của cả hai vế.

Vậy e của y nhân đạo hàm của y.

Vậy y nguyên tố.

Và đây là đạo hàm của f, là f nguyên tố.

Vì vậy, bạn nghĩ y nguyên tố là dy by dx.

Và khi đó f nguyên tố sẽ bằng df by dx.

Được rồi?

Và từ đây chúng ta có thể chuyển cái này sang phía bên kia.

Vậy y phẩy bằng f phẩy trên e mũ y.

Nhưng e mũ y chỉ là f.

Phải?

Vì vậy, nó là f nguyên tố chia cho f.

Và y nguyên tố là ln f, vâng y là ln f.

Vì vậy, nó thực sự là đạo hàm của ln f.

ln f đạo hàm bằng đạo hàm của f chia cho f.

Tôi sẽ đợi anh chàng này đi qua chúng ta.

Được rồi, quay trở lại đây, chúng ta có thể thấy điều này,

thực ra chúng ta hãy thực hiện bước tiếp theo này trước.

Vậy bằng cách sử dụng danh tính này, những gì chúng ta có thể làm

là chúng ta có thể thay thế nó bằng log của gradient.

Vậy nó là omega, p omega theta, gradient log,

của p của omega theta, g omega.

Được rồi?

Và bạn nhận thấy rằng nó vẫn ở dạng

của một giá trị mong đợi, phải không?

Bởi vì điều này được cân nhắc bởi những xác suất này.

Được rồi, đây là giá trị mong đợi của gradient,

p omega theta, g omega.

Được rồi, hãy viết ra những gì chúng ta có bây giờ.

Vì vậy, độ dốc của mục tiêu của chúng tôi là giá trị mong đợi,

của độ dốc của log của xác suất quỹ đạo này

lần lợi nhuận của quỹ đạo đó.

Được rồi?

Trong thực tế, tất nhiên chúng ta không thể tính được

giá trị mong đợi này vì chúng tôi không thể tìm thấy,

cho hầu hết các môi trường thế giới thực,

vô số quỹ đạo có thể xảy ra,

khi chúng ta không thể vượt qua tất cả những điều đó.

Chúng ta không thể trải qua vô số khả năng.

Vì vậy, điều chúng tôi làm trong thực tế là ước tính điều này bằng cách sử dụng các mẫu

chúng tôi thu thập từ việc thực sự chơi trong môi trường.

Vậy cái này xấp xỉ bằng,

vì vậy chúng ta sẽ sử dụng chữ M.

Vậy nếu chúng ta thực hiện M chơi trong môi trường,

thì chúng ta chỉ có thể lấy mức trung bình.

Vì vậy, nó sẽ là gradient của log p của quỹ đạo thứ i,

bạn biết đấy, theta, g của omega, i, và khung số.

Được rồi, tại thời điểm này tôi nghĩ đây là thời điểm tốt để dừng lại

và tiếp tục ở bài giảng tiếp theo.

Nhưng mục tiêu của chúng ta bây giờ về cơ bản là loại bỏ omega này.

Đi, loại bỏ omega.

Và thực sự để đặt điều này trong điều kiện của một cái gì đó

điều đó phụ thuộc vào theta.

Đúng, vậy điều này phụ thuộc vào pi hay theta như thế nào?

Được rồi, và nhân tiện, chỉ là một số thuật ngữ thôi.

Chúng tôi gọi đây là những mẫu chúng tôi thu thập bằng cách phát các tập phim,

chúng tôi gọi chúng là triển khai.

Được rồi, vậy tôi, e, chúng tôi triển khai M.

Được rồi, không quá quan trọng,

nó chỉ cho bạn biết một số thuật ngữ

mà chúng tôi sử dụng trong lĩnh vực này.