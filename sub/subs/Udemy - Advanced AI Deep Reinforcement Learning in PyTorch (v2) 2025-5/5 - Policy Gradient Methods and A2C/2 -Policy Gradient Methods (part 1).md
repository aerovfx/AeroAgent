# 2 -Các phương thức gradient chính sách (phần 1) đã dịch

---

Được rồi, bài giảng này sẽ nói về các phương pháp gradient chính sách.

Các phương pháp gradient chính sách

Được rồi, vậy phần này nói về cái gì?

Cho đến nay trong khóa học này, chúng ta đã xác định chính sách tối ưu là chính sách chọn một hành động

tối đa hóa hàm giá trị, tức là lợi nhuận kỳ vọng.

Được rồi, vậy hãy viết nó ra.

Vì vậy, hành động tối ưu bằng arg max.

Được rồi, sau đó chúng ta có mảng q, s a, arg max.

Vì vậy, bạn sẽ nhận thấy rằng điều này ngụ ý rằng chính sách tối ưu phải mang tính quyết định.

Đúng vậy, vì ở mọi trạng thái, chúng ta luôn chọn hành động giống nhau.

Vì vậy, điều này hàm ý chính sách tối ưu phải mang tính quyết định.

Được rồi, nhưng đây là một câu hỏi cần xem xét.

Điều gì sẽ xảy ra nếu chính sách tối ưu mang tính xác suất?

Và điều gì sẽ xảy ra nếu chính sách tối ưu mang tính xác suất?

Vì vậy, hãy nghĩ về một số ví dụ về trường hợp này có thể xảy ra như thế nào.

Vì vậy, ví dụ kinh điển về thời điểm chính sách xác suất là tối ưu là trò oẳn tù tì.

Được rồi, ví dụ như trò kéo búa bao.

Tôi chắc rằng tất cả các bạn đã từng chơi oẳn tù tì trước đây và nếu chưa, hãy tra cứu nó.

Vì vậy, về cơ bản, mục tiêu của bạn là chọn một trong những chiếc oẳn tù tì hoặc kéo này và đối thủ của bạn.

Vì vậy, đây là một trò chơi hai người.

Đồng thời, đối thủ của bạn cũng chọn oẳn tù tì.

Và vì vậy khi bạn tiết lộ lựa chọn của mình cùng lúc, sẽ có người thắng hoặc thua dựa trên

mối quan hệ giữa trò chơi oẳn tù tì và kéo này.

Và như vậy kéo sẽ thắng giấy vì kéo có thể cắt được giấy.

Giấy thắng được đá vì giấy có thể đè được đá và đá thắng được kéo vì bạn

có thể dùng đá đập nát cái kéo.

Được rồi, vậy tại sao một chính sách xác định lại không phải là tối ưu?

Vì vậy, một chính sách tất định, vì không có trạng thái nên bạn sẽ luôn chọn cùng một trạng thái

hành động.

Nhưng nếu lần nào bạn cũng chọn cùng một hành động, đối thủ sẽ nhanh chóng lợi dụng bạn.

Vì vậy, ví dụ, nếu bạn luôn chọn đá thì đối thủ của bạn sẽ luôn chọn

chọn giấy.

Nhưng bạn sẽ nhận thấy rằng nếu bạn chọn một hành động ngẫu nhiên thống nhất, thì một phần ba cơ hội xảy ra

giấy hoặc kéo, bạn không bao giờ có thể bị lợi dụng.

Được rồi, vậy nếu chính sách là chọn với xác suất một phần ba thì bạn không thể bị lợi dụng.

Và đối với đối thủ của bạn, đây cũng sẽ là chính sách tối ưu.

Vì vậy bạn không thể khai thác lẫn nhau.

Một lần nữa, xin lưu ý thêm rằng đây là một chủ đề từ Lý thuyết trò chơi.

Và đây được gọi là chiến lược hỗn hợp Cân bằng Nash nếu bạn tò mò.

Vì vậy, Lý thuyết trò chơi không hữu ích cho khóa học này.

Thật thú vị khi biết.

Chiến lược hỗn hợp.

Cân bằng Nash.

Được rồi, bây giờ bạn đã tin rằng các chính sách xác suất có thể hữu ích, chúng ta sẽ triển khai như thế nào

họ?

Bởi vì rõ ràng chúng ta có thể thực hiện chính sách xác suất chỉ cần chọn argmax của Q.

Vì vậy, giải pháp cho vấn đề này là đưa ra một mô hình hoàn toàn khác, đó là chính sách

các phương pháp gradient.

Được rồi, giải pháp là các phương pháp gradient chính sách.

Được rồi, vậy điều gì làm cho các phương thức Policy gradient khác với những gì chúng ta đã làm trước đây?

Những gì chúng ta đã có trước đây, đó là những gì bây giờ chúng ta sẽ gọi là các phương pháp dựa trên giá trị.

Vì vậy, chúng tôi sẽ đặt tên hồi tố cho những gì chúng tôi đang làm là các phương pháp dựa trên giá trị.

Tại sao?

Bởi vì cái chúng ta đang cố ước tính là hàm giá trị.

Được rồi, về cơ bản bạn có thể nghĩ là chúng ta đang cố gắng ước tính điều gì đó.

Vì vậy, dựa trên giá trị.

Vì vậy, chúng ta đang cố gắng ước tính một hàm với một số tham số, chẳng hạn như w, trong đó đây là

lợi nhuận kỳ vọng.

Được rồi.

Vì vậy, đối với các phương pháp gradient chính sách, dựa trên chính sách, fw ước tính chính sách tối ưu.

Được rồi, nói cách khác, chúng ta sẽ tham số hóa chính sách tối ưu.

Được rồi, mạng nơ-ron của chúng ta hoặc bất kỳ mô hình nào khác, thay vì sử dụng mô hình đó để đưa ra ước tính của nó

của kết quả trả về, chúng ta sẽ đưa ra hành động tối ưu.

Được rồi, bây giờ hãy nghĩ xem làm thế nào chúng ta có thể biểu diễn các chính sách xác suất trong toán học hoặc

trong mã?

Vậy làm thế nào để thể hiện các chính sách xác suất?

Được rồi, bạn có thể nhớ lại rằng sự tham lam của epsilon mang tính xác suất.

Vì vậy, bạn có thể nghĩ, ồ, tại sao chúng ta không thể sử dụng epsilon tham lam?

Vì vậy, mặc dù theo một nghĩa nào đó, epsilon tham lam mang tính xác suất nhưng nó vẫn chỉ là một phiên bản giới hạn

về điều này.

Vậy tại sao vậy?

Lý do là vì khi bạn chọn một hành động ngẫu nhiên thì đây là tất cả các hành động, hành động

và thăm dò.

Vì vậy hành động tối ưu của chúng ta sẽ có một số xác suất.

Được rồi, vậy nó sẽ là một trừ epsilon cộng epsilon về số lượng hành động và sau đó là mọi thứ

nếu không thì ngoài chính sách tối ưu, chúng ta sẽ có xác suất vượt qua.

Số lượng hành động.

Được rồi, đây là một dạng hạn chế của chính sách xác suất vì tất cả các hành động không tối ưu đều có

có cùng xác suất, tức là epsilon trên kích thước của không gian tác dụng.

Được rồi, nhưng thay vào đó, chúng ta nên làm gì, giả sử chúng ta có một mạng lưới thần kinh.

Vì vậy, giả sử kích thước của không gian hành động hoặc không gian trạng thái là ba và chúng ta có bốn ẩn

đơn vị và giả sử chúng ta có hai hành động.

Thế là một, hai.

Được rồi, và đầu ra của cái này, vậy hãy nói đây là trạng thái.

Điều này sẽ là, nói đây là hành động một.

Đây sẽ là xác suất mà chúng ta nên thực hiện hành động một với trạng thái s và điều này

sẽ là xác suất để chúng ta thực hiện hành động thứ hai với trạng thái s.

Được rồi, mạng nơ-ron này xuất ra các xác suất này một cách trực tiếp thay vì xuất ra

giá trị và sau đó bạn chọn arg max.

Và vì vậy tôi cũng muốn nhấn mạnh tại sao điều này lại thú vị và đó là vì nó cũng có thể được áp dụng

đến không gian hành động liên tục.

Vì vậy, không gian hành động liên tục.

Đúng vậy, trong trường hợp trên, chúng ta giả định rằng các hành động là rời rạc.

Vì vậy, chúng ta có hành động một, hành động hai, hành động ba, v.v.

Nếu không gian hành động là liên tục thì sao?

Và vì vậy bạn có thể thắc mắc, trong kịch bản nào chúng ta muốn không gian hành động liên tục?

Và vì vậy tôi sẽ cho bạn một số ví dụ, ví dụ.

Lái xe ô tô.

Được rồi, vậy tại sao điều đó lại đòi hỏi một không gian hành động liên tục?

Vì vậy, khi bạn lái xe, nếu bạn nghĩ về điều đó, bạn không chỉ bị hỏng hoặc không bị hỏng hoặc tăng tốc

hoặc không tăng tốc, bạn có thể tưởng tượng rằng đó sẽ là một trải nghiệm lái xe rất khó chịu.

Đúng vậy, vì vậy bạn có thể dừng hẳn hoặc tăng tốc lên mức tối đa.

Đúng, lái xe sẽ khá tệ.

Và trên thực tế, điều bạn quan tâm là mức độ đột phá và mức độ tăng tốc.

Nói cách khác, bạn đang chọn một số trên quang phổ.

Và vì vậy nếu bạn nghĩ về nó, nguồn cung cấp cho robot trong thế giới thực nhất của bạn.

Vì vậy, việc đi lại và di chuyển xung quanh, cánh tay robot, v.v.

Đúng vậy, bạn phải có khả năng điều chỉnh lượng lực mà bạn áp dụng.

Được rồi, robot trong thế giới thực nói chung hơn.

Và một ví dụ khác không thuộc thế giới vật chất là giao dịch chứng khoán.

Đúng vậy, một ví dụ về điều đó là đầu ra của bạn có thể là sự phân bổ tối ưu cho danh mục đầu tư.

Vì vậy, 27% cho cổ phiếu này, 25% cho cổ phiếu này, v.v.

Được rồi, vậy là phân bổ cổng, folio.

Và vì vậy nếu chúng ta có một không gian hành động liên tục và chúng ta muốn đưa ra một phân bố,

thì phân phối của chúng ta phải vượt quá một giá trị liên tục.

Vì vậy, nếu bạn nghĩ về nó, chúng ta có rất nhiều sự lựa chọn.

Đúng, chúng ta có thể sử dụng phân phối Gaussian.

Chúng ta có thể sử dụng bản phân phối beta.

Chúng ta có thể sử dụng phân phối chi bình phương, v.v.

Đúng vậy, có rất nhiều bản phân phối liên tục ngoài kia.

Chúng ta có xu hướng chỉ sử dụng Gaussian bình thường.

Và bạn làm điều đó như thế nào nếu mạng lưới thần kinh chỉ xuất ra một giá trị duy nhất tại một thời điểm?

Và câu trả lời là bạn sẽ thừa nhận sự phân phối này trong mã của mình

và sau đó xuất ra các tham số của phân phối đó.

Được rồi, ví dụ như,

ví dụ là bình thường với giá trị trung bình, mu và phương sai, hình vuông đơn.

Nhưng giả sử chúng ta muốn giá trị trung bình này phụ thuộc vào trạng thái đầu vào S,

và phương sai cũng phụ thuộc vào trạng thái đầu vào S.

Vậy cách chúng ta có thể làm điều đó là chúng ta có một mạng lưới thần kinh.

Lần này tôi sẽ không vẽ ra các kết nối.

Nhưng bây giờ đầu ra của chúng tôi là các tham số của phân phối này.

Vậy đây là S. Bây giờ đầu ra là mu của S và sigma bình phương của S.

Được rồi, trong thực tế, chúng ta thường sử dụng phương sai log hoặc độ lệch chuẩn log.

Đúng vậy, trong thực tế, xuất ra log của sigma bình S hoặc log của sigma S.

Được rồi, bây giờ chúng ta đã biết cách trình bày chính sách bằng mô hình tham số,

câu hỏi tiếp theo là làm cách nào để đào tạo một mô hình như vậy?

Đúng rồi, vậy luyện tập như thế nào?

Làm thế nào để đào tạo?

Điều này không đơn giản nếu bạn nghĩ về nó.

Được rồi, vì với các phương pháp dựa trên giá trị, thật đơn giản vì chúng ta biết thứ mình muốn ước tính.

Đúng vậy, với các phương pháp dựa trên giá trị, điều đó thật dễ dàng vì chúng ta có thể sử dụng sai số bình phương.

Vâng, chúng tôi biết những gì chúng tôi muốn ước tính.

Nói cách khác, chúng ta biết chúng ta muốn V của S gần với cái gì.

Và khi chúng ta muốn dự đoán của mình gần với giá trị thực, chúng ta có thể sử dụng sai số bình phương

với giá trị thực.

Vì vậy, IE được gần gũi.

Và sau đó chúng ta có thể sử dụng sai số bình phương trung bình.

Đúng vậy, mục tiêu của chúng ta chỉ là

giá trị kỳ vọng của G, do đó lợi nhuận trừ V của S cho theta trên bình phương.

Hoặc một cách khác để nghĩ về điều này là ngôi sao theta.

Vậy theta sẽ là tham số của V bằng argmax của theta.

Được rồi, vì vậy chúng tôi muốn V ở gần G, đó chính là mục đích của việc này.

Nhưng bạn sẽ nhận thấy rằng nếu chúng ta cố gắng áp dụng điều này cho các mức độ chính sách hoặc mô hình chính sách,

thậm chí còn không rõ chúng ta muốn chính sách này hướng tới điều gì.

Đúng, bởi vì điều đó có nghĩa là chúng ta biết chính sách tối ưu, điều này là sai.

Đó là lý do tại sao điều này hơi khó hiểu.

Vậy chúng ta có biết mình muốn gì không?

Tôi có một chữ S nhất định để ở gần.

Không, vì khi đó chúng ta đã biết chính sách tối ưu.

Đúng vậy, bởi vì đó sẽ là chính sách tối ưu, đó là điều chúng tôi đang cố gắng tìm kiếm,

đúng, đó là những gì chúng tôi đang cố gắng tìm kiếm.

Được rồi, vậy là nó sẽ không có tác dụng.

Chúng ta không thể chỉ chọn thứ gì đó mà chúng ta muốn Pi ở gần và sau đó thực hiện hồi quy.

Được rồi, vậy chúng ta sẽ làm gì?

Vì vậy, tôi muốn cung cấp cho bạn cái nhìn tổng quan ở cấp độ cao về các bước chúng tôi sẽ thực hiện,

chỉ để nó có ý nghĩa và bạn không nghĩ rằng chúng ta đang làm nhiều phép tính mà không có lý do.

Được rồi, tổng quan cấp cao về giải pháp.

Được rồi, về cơ bản cách tiếp cận mà chúng ta sắp thực hiện có phần khác thường.

Tôi thích nghĩ về nó theo cách này.

Vì vậy, thay vì đi từ trên xuống, tối ưu hóa điển hình là tối ưu hóa từ trên xuống.

Vậy tôi phải nói gì từ trên xuống?

Bởi vì chúng tôi bắt đầu với một mục tiêu, nên đó là mục tiêu hàng đầu.

Chúng tôi chỉ có một con số duy nhất mà chúng tôi muốn tối ưu hóa và sau đó chúng tôi thực hiện một số thủ thuật toán học

và điều đó giúp chúng ta tìm ra giải pháp mà tôi coi là nhược điểm vì đó là

nơi có tất cả các chi tiết.

Được rồi, nhưng với độ dốc chính sách, nên dạng viết tắt của điều đó là PG.

Đây sẽ là từ dưới lên.

Được rồi, vậy tại sao nó lại là từ dưới lên vì chúng ta thực sự muốn biết mục tiêu của mình cho đến cuối cùng

nguồn gốc của chúng tôi.

Vì vậy, chúng ta không bắt đầu với mục tiêu, chúng ta kết thúc với mục tiêu.

Vì vậy, chúng tôi sẽ kết thúc với mục tiêu.

Được rồi, thông thường chúng ta bắt đầu với mục tiêu và tối ưu hóa nó bằng chính sách chuyển màu,

chúng ta sẽ bắt đầu với cái gì đó khác và sau đó kết thúc với mục tiêu.

Được rồi, và cụ thể hơn, điều này sẽ làm cho tên này trở thành một gradient chính sách có ý nghĩa.

Điều chúng ta sắp làm là bắt đầu bằng việc cố gắng tìm gradient của

khách quan.

Được rồi, vậy chúng ta bắt đầu bằng việc tìm độ dốc của vật kính thay vì vật kính

của mục tiêu của chúng tôi chứ không phải là mục tiêu và sau đó nói một cách đại khái, chúng tôi sẽ tích hợp

nó để quay trở lại mục tiêu hoặc sự mất mát vô hướng sẽ giảm thiểu với PyTorch hoặc TensorFlow.

Được rồi, vì vậy chúng ta bắt đầu với việc tìm gradient và sau đó chúng ta kết thúc với mục tiêu dấu gạch chéo mất mát.