# Chương 4. Học cách chọn chính sách tốt nhất Các phương pháp chuyển tiếp chính sách Học tăng cường sâu trong thực tế, Phiên bản video

---

Chương 4 Học cách chọn chính sách tốt nhất - Phương pháp gradient chính sách

Chương này đề cập đến việc Thực hiện chức năng chính sách như một nơ-ron

network Giới thiệu API OpenAI GEM

Áp dụng thuật toán củng cố cho bài toán cột xe đẩy OpenAI

Trong chương trước chúng ta đã thảo luận về mạng xếp hàng sâu, một thuật toán phi chính sách

xấp xỉ hàm xếp hàng với mạng nơ-ron.

Đầu ra của mạng hàng đợi là các giá trị hàng đợi tương ứng với từng hành động trong một

trạng thái nhất định (hình 4.1).

Hãy nhớ lại rằng giá trị hàng đợi là giá trị dự kiến ​​(trung bình có trọng số) của phần thưởng.

Hình 4.1 Mạng hàng đợi nhận trạng thái và trả về

giá trị hàng đợi (giá trị hành động) cho mỗi hành động.

Chúng ta có thể sử dụng các giá trị hành động đó để quyết định hành động nào sẽ thực hiện.

Sử dụng các giá trị hàng đợi được dự đoán này từ mạng hàng đợi, chúng ta có thể sử dụng một số chiến lược để

chọn hành động để thực hiện.

Chiến lược chúng tôi sử dụng ở chương trước là cách tiếp cận epsilon-tham lam, trong đó chúng tôi

đã chọn một hành động ngẫu nhiên với xác suất epsilon và với xác suất 1 trừ epsilon,

chúng tôi đã chọn hành động liên quan đến giá trị hàng đợi cao nhất.

Hành động mà mạng xếp hàng dự đoán là tốt nhất dựa trên kinh nghiệm của nó cho đến nay.

Có bất kỳ chính sách nào khác mà chúng tôi có thể đã tuân theo, chẳng hạn như sử dụng softmax

lớp trên các giá trị hàng đợi.

Điều gì sẽ xảy ra nếu chúng ta bỏ qua việc chọn một chính sách trên DQN và thay vào đó đào tạo một mạng lưới thần kinh

để xuất ra một hành động trực tiếp?

Nếu chúng ta làm điều đó, mạng lưới thần kinh của chúng ta sẽ trở thành một chức năng chính sách hoặc mạng chính sách.

Hãy nhớ từ chương 3 rằng hàm chính sách, pi của trạng thái ánh xạ tới xác suất hành động

trạng thái nhất định, chấp nhận một trạng thái và trả về hành động tốt nhất.

Chính xác hơn, nó sẽ trả về một phân bố xác suất cho các hành động và chúng ta có thể

mẫu từ bản phân phối này để chọn hành động.

Nếu phân phối xác suất là một khái niệm xa lạ với bạn, đừng lo lắng.

Chúng ta sẽ thảo luận về nó nhiều hơn trong chương này và trong suốt cuốn sách.

Phần 4.1 Chức năng chính sách sử dụng mạng thần kinh

Trong chương này chúng tôi sẽ giới thiệu một lớp thuật toán cho phép chúng tôi tính gần đúng

hàm chính sách, pi của S, thay vì hàm giá trị, V pi hoặc Q.

Nghĩa là, thay vì huấn luyện mạng đưa ra các giá trị hành động, chúng ta sẽ huấn luyện mạng

đến đầu ra, xác suất của, hành động.

Phần 4.1.1 Mạng thần kinh là chức năng chính sách

Ngược lại với mạng hàng đợi, mạng chính sách cho chúng ta biết chính xác những gì cần làm với trạng thái

chúng tôi đang ở trong.

Không cần thêm quyết định nào nữa.

Tất cả những gì chúng ta cần làm là lấy mẫu ngẫu nhiên từ phân bố xác suất của A cho trước S,

và chúng ta nhận được một hành động cần thực hiện, hình 4.2.

Những hành động có nhiều khả năng mang lại lợi ích nhất sẽ có cơ hội được lựa chọn cao nhất

từ việc lấy mẫu ngẫu nhiên, vì chúng được ấn định xác suất cao nhất.

Hình 4.2.

Mạng chính sách là một hàm nhận trạng thái và trả về phân bố xác suất

qua các hành động có thể xảy ra.

Cho trước phân bố xác suất của A cho trước S dưới dạng một cái lọ, chứa đầy những ghi chú nhỏ có chữ

một hành động được viết trên mỗi.

Trong một trò chơi có bốn hành động có thể xảy ra, sẽ có các ghi chú có nhãn từ 1 đến 4 hoặc 0 đến

3 nếu chúng là chỉ mục trong Python.

Nếu mạng lưới chính sách của chúng tôi dự đoán rằng hành động 2 có nhiều khả năng mang lại kết quả cao nhất

phần thưởng, nó sẽ lấp đầy lọ này với rất nhiều ghi chú nhỏ được dán nhãn 2 và ít ghi chú được dán nhãn hơn

1, 3 và 4.

Để chọn một hành động, tất cả những gì chúng ta làm là nhắm mắt lại và lấy một ghi chú ngẫu nhiên

từ bình.

Rất có thể chúng ta sẽ chọn hành động 2, nhưng đôi khi chúng ta sẽ chọn hành động khác và hành động đó

cho chúng ta cơ hội khám phá.

Sử dụng sự tương tự này, mỗi khi trạng thái của môi trường thay đổi, chúng ta đưa ra trạng thái

vào mạng chính sách của chúng tôi và nó sử dụng mạng đó để lấp đầy lọ bằng một bộ ghi chú được gắn nhãn mới,

thể hiện các hành động theo các tỷ lệ khác nhau.

Sau đó, chúng tôi chọn ngẫu nhiên từ lọ.

Lớp thuật toán này được gọi là các phương pháp gradient chính sách và nó có một số tính năng quan trọng.

sự khác biệt so với thuật toán DQN.

Chúng ta sẽ khám phá những khác biệt này trong chương này.

Phương pháp gradient chính sách cung cấp một số lợi thế so với các phương pháp dự đoán giá trị như DQN.

Một là, như chúng ta đã thảo luận, chúng ta không còn phải lo lắng về việc nghĩ ra một hành động nữa.

chiến lược lựa chọn như Epsilon Greedy.

Thay vào đó, chúng tôi lấy mẫu trực tiếp các hành động từ chính sách.

Hãy nhớ rằng, chúng ta đã dành rất nhiều thời gian để tìm ra các phương pháp nhằm cải thiện tính ổn định của quá trình luyện tập.

DQN của chúng tôi.

Chúng tôi phải sử dụng mạng mục tiêu và mạng phát lại trải nghiệm, đồng thời có một số mạng khác

phương pháp trong tài liệu học thuật mà chúng ta có thể đã sử dụng.

Mạng lưới chính sách có xu hướng đơn giản hóa một số vấn đề phức tạp đó.

Phần 4.1.2 Độ dốc chính sách ngẫu nhiên

Có nhiều loại phương pháp gradient chính sách khác nhau.

Chúng ta sẽ bắt đầu với phương pháp gradient chính sách ngẫu nhiên, hình 4.3, đây là phương pháp mà chúng ta vừa

được mô tả.

Với độ dốc chính sách ngẫu nhiên, đầu ra của mạng nơ-ron của chúng ta là một vectơ hành động

đại diện cho một phân bố xác suất.

Hình 4.3.

Hàm chính sách ngẫu nhiên Hàm chính sách chấp nhận một trạng thái và trả về

một phân phối xác suất trên các hành động.

Nó mang tính ngẫu nhiên vì nó trả về một phân phối xác suất cho các hành động thay vì trả về

một hành động đơn lẻ mang tính quyết định.

Chính sách mà chúng tôi sẽ tuân theo là chọn một hành động từ phân bố xác suất này.

Điều này có nghĩa là nếu đại lý của chúng tôi ở cùng một trạng thái hai lần, chúng tôi có thể không nhận được

cùng một hành động mọi lúc.

Trong hình 4.3, chúng ta cung cấp trạng thái cho hàm của mình là 1, 2 và đầu ra là một vectơ

xác suất tương ứng với mỗi hành động.

Ví dụ: nếu đây là một tác nhân trong thế giới lưới, thì tác nhân đó sẽ có xác suất 0,50

đi lên, không có khả năng đi xuống, xác suất rẽ trái là 0,25 và xác suất 0,25

về việc đi đúng.

Nếu môi trường đứng yên, đó là lúc sự phân bố trạng thái và phần thưởng

là không đổi và chúng tôi sử dụng chiến lược xác định, chúng tôi mong đợi phân phối xác suất

cuối cùng hội tụ về một phân bố xác suất suy biến, như thể hiện trong hình 4.4.

Phân bố xác suất suy biến là phân bố trong đó tất cả xác suất

khối lượng được gán cho một kết quả tiềm năng duy nhất.

Khi xử lý phân bố xác suất rời rạc như chúng tôi làm trong cuốn sách này, tất cả các xác suất

phải có tổng bằng 1.

Vì vậy, phân phối suy biến là phân phối trong đó tất cả các kết quả đều được gán xác suất bằng 0 ngoại trừ

cho 1, được gán 1.

Hình 4.4.

Hàm chính sách xác định, thường được biểu thị bằng ký tự π của Hy Lạp, có trạng thái và

trả về một hành động cụ thể cần thực hiện, không giống như chính sách ngẫu nhiên, trả về xác suất

phân phối qua các hành động.

Trong giai đoạn đầu đào tạo, chúng tôi muốn phân bổ khá đồng đều để có thể tối đa hóa

khám phá, nhưng trong quá trình đào tạo, chúng tôi muốn phân phối hội tụ trên

hành động tối ưu, cho một trạng thái.

Nếu chỉ có một hành động tối ưu cho một trạng thái, chúng ta sẽ hội tụ về một

phân phối suy biến, nhưng nếu có hai hành động tốt như nhau thì chúng ta mong đợi

việc phân phối có hai chế độ.

Một dạng phân bố xác suất chỉ là một từ khác để chỉ đỉnh.

Tôi quên mất, phân phối xác suất là gì?

Trong thế giới lưới, chúng tôi có bốn hành động có thể thực hiện là lên, xuống, trái và phải.

Chúng ta gọi đây là tập hành động hoặc không gian hành động vì chúng ta có thể mô tả nó về mặt toán học như sau:

một bộ.

Ví dụ: A là một tập hợp chứa các phần tử lên, xuống, trái và phải, trong đó đường cong

dấu ngoặc nhọn biểu thị một bộ.

Một tập hợp trong toán học chỉ là một tập hợp trừu tượng, không có thứ tự của các sự vật với một số

các hoạt động được xác định.

Vậy việc áp dụng phân bố xác suất cho tập hợp hành động này có ý nghĩa gì?

Xác suất thực sự là một chủ đề rất phong phú và thậm chí còn gây tranh cãi.

Có nhiều quan điểm triết học khác nhau về ý nghĩa chính xác của xác suất.

Đối với một số người, xác suất có nghĩa là nếu bạn tung một đồng xu với một số lượng rất lớn

nhiều lần, lý tưởng nhất là vô số lần về mặt toán học, xác suất của

một đồng xu công bằng lật mặt ngửa bằng với tỷ lệ mặt ngửa trong chiều dài vô hạn đó

chuỗi các lần lật.

Nghĩa là, nếu chúng ta tung một đồng xu công bằng một triệu lần, chúng ta sẽ mong đợi khoảng một nửa số lần tung

là mặt ngửa và nửa còn lại là mặt sấp nên xác suất bằng tỷ lệ đó.

Đây là cách giải thích thường xuyên về xác suất, vì xác suất được hiểu là dài hạn.

tần số của một số sự kiện lặp đi lặp lại nhiều lần.

Một trường phái tư tưởng khác chỉ giải thích xác suất như một mức độ niềm tin, một đánh giá chủ quan

về mức độ ai đó có thể dự đoán một sự kiện dựa trên kiến thức mà họ hiện có.

Mức độ tin tưởng này thường được gọi là sự tin cậy.

Xác suất để một đồng xu công bằng xuất hiện mặt ngửa là 0,5 hoặc 50% bởi vì, với những gì chúng ta

biết về đồng xu, chúng ta không có lý do gì để dự đoán mặt ngửa hay mặt sấp

nhiều hơn những cái đầu.

Vì vậy, chúng tôi chia đều niềm tin của mình cho hai kết quả có thể xảy ra.

Do đó, bất cứ điều gì chúng ta không thể dự đoán một cách xác định, nghĩa là với xác suất 0 hoặc 1 và không có gì

ở giữa là kết quả của sự thiếu hiểu biết.

Bạn có thể tự do giải thích xác suất theo cách bạn muốn vì nó sẽ không ảnh hưởng đến tính toán của chúng tôi.

Nhưng trong cuốn sách này, chúng tôi có xu hướng ngầm sử dụng cách giải thích đáng tin cậy về xác suất.

Đối với mục đích của chúng tôi, việc áp dụng phân phối xác suất cho tập hợp các hành động trong thế giới lưới, A là

một tập hợp chứa các phần tử lên, xuống, trái và phải, nghĩa là chúng ta đang gán một mức độ

của niềm tin, một số thực từ 0 đến 1, cho mỗi hành động trong tập hợp sao cho tất cả

xác suất có tổng bằng 1.

Chúng tôi giải thích những xác suất này là xác suất mà một hành động là hành động tốt nhất để tối đa hóa

phần thưởng mong đợi, vì chúng ta đang ở trong một trạng thái nhất định.

Cụ thể, phân bố xác suất trên tập hành động A của chúng tôi được ký hiệu là P(A), trong đó

P(A) là hàm ánh xạ A_i tới khoảng 0,1, nghĩa là xác suất xảy ra sự kiện

A là ánh xạ từ tập A đến tập số thực từ 0 đến 1.

Cụ thể, mỗi phần tử A_i thuộc A được ánh xạ tới một số duy nhất trong khoảng từ 0 đến

1 sao cho tổng của tất cả các số này cho mỗi hành động bằng 1.

Chúng tôi có thể biểu thị bản đồ này cho tập hợp hành động trong thế giới lưới của chúng tôi dưới dạng vectơ, nơi chúng tôi xác định

mỗi vị trí trong vectơ có một phần tử trong tập hành động, ví dụ: lên, xuống,

trái, phải, được ánh xạ tới, 0,25, 0,25, 0,10, 0,4.

Bản đồ này được gọi là hàm khối lượng xác suất, PMF.

Những gì chúng ta vừa mô tả thực ra là một phân bố xác suất rời rạc, vì hành động của chúng ta

tập hợp rời rạc, có số phần tử hữu hạn.

Nếu tập hành động của chúng ta là vô hạn, đó là một biến liên tục như vận tốc, thì chúng ta sẽ

gọi đây là phân bố xác suất liên tục và thay vào đó chúng ta cần xác định xác suất

hàm mật độ, PDF.

Ví dụ phổ biến nhất của PDF là đường cong bình thường, còn được gọi là đường cong Gaussian hoặc chỉ là đường cong hình chuông,

phân phối.

Nếu chúng ta có khả năng xảy ra một hành động liên tục, chẳng hạn như một trò chơi ô tô mà chúng ta cần kiểm soát

vận tốc của ô tô từ 0 đến một giá trị cực đại nào đó, là một biến liên tục, làm thế nào

chúng ta có thể làm điều này với một mạng lưới chính sách không?

Chà, chúng ta có thể bỏ ý tưởng về phân bố xác suất và chỉ huấn luyện mạng để

tạo ra một giá trị duy nhất của vận tốc mà nó dự đoán là tốt nhất, nhưng sau đó chúng ta sẽ mạo hiểm

chưa khám phá đủ và rất khó để đào tạo một mạng lưới như vậy.

Rất nhiều sức mạnh đến từ một chút ngẫu nhiên.

Loại mạng lưới thần kinh mà chúng tôi sử dụng trong cuốn sách này chỉ tạo ra vectơ hoặc tensor.

nói chung, là đầu ra, vì vậy chúng không thể tạo ra phân bố xác suất liên tục.

Chúng ta phải khéo léo hơn.

Một tệp PDF giống như phân phối chuẩn được xác định bởi hai tham số, giá trị trung bình và phương sai.

Khi chúng tôi có những thứ đó, chúng tôi có phân phối chuẩn mà chúng tôi có thể lấy mẫu từ đó.

Vì vậy, chúng ta có thể huấn luyện một mạng lưới thần kinh để tạo ra các giá trị trung bình và độ lệch chuẩn mà chúng ta

sau đó có thể cắm vào phương trình phân phối chuẩn và lấy mẫu từ đó.

Đừng lo lắng nếu bây giờ tất cả điều này không còn ý nghĩa nữa.

Chúng ta sẽ tiếp tục nhắc đi nhắc lại vì những khái niệm này có mặt khắp nơi trong việc củng cố

học và học máy rộng hơn.

Mục 4.1.3 Thăm dò

Hãy nhớ lại chương trước rằng chúng ta cần chính sách của mình bao gồm một số tính ngẫu nhiên, điều này

sẽ cho phép chúng tôi đến thăm các tiểu bang mới trong quá trình đào tạo.

Đối với DQN, chúng tôi đã tuân theo chính sách tham lam của epsilon, nơi có khả năng chúng tôi sẽ không tuân theo

hành động dẫn đến phần thưởng được dự đoán lớn nhất.

Nếu chúng ta luôn chọn hành động dẫn đến phần thưởng dự đoán tối đa thì chúng ta sẽ không bao giờ

khám phá những hành động và trạng thái tốt hơn nữa có sẵn cho chúng ta.

Đối với phương pháp gradient chính sách ngẫu nhiên, vì đầu ra của chúng tôi là phân phối xác suất,

sẽ có một cơ hội nhỏ để chúng ta khám phá mọi không gian.

Chỉ sau khi thăm dò đầy đủ thì phân phối hành động mới hội tụ để sản xuất

hành động tốt nhất duy nhất, một phân phối suy biến.

Hoặc nếu bản thân môi trường có tính ngẫu nhiên thì phân bố xác suất sẽ giữ lại một số

khối lượng xác suất cho mỗi hành động.

Khi chúng tôi khởi tạo mô hình của mình ngay từ đầu, xác suất để tác nhân của chúng tôi chọn từng

hành động phải xấp xỉ bằng nhau hoặc đồng nhất, vì mô hình không có thông tin về

hành động nào tốt hơn.

Có một biến thể của độ dốc chính sách được gọi là độ dốc chính sách xác định, DPG, trong đó

có một đầu ra duy nhất mà tác nhân sẽ luôn tuân theo, như được minh họa trong hình 4.4.

Ví dụ, trong trường hợp của thế giới lưới, nó sẽ tạo ra một vectơ nhị phân bốn chiều

với 1 cho hành động được thực hiện và 0 cho các hành động khác.

Tác nhân sẽ không khám phá đúng cách nếu nó luôn tuân theo đầu ra, vì không có sự ngẫu nhiên

trong việc lựa chọn hành động.

Vì đầu ra của hàm chính sách xác định cho một tập hành động rời rạc sẽ là

các giá trị rời rạc, cũng khó có thể làm việc này theo cách có thể lấy đạo hàm hoàn toàn

mà chúng ta đã quen với việc học sâu.

Vì vậy, chúng tôi sẽ tập trung vào độ dốc chính sách ngẫu nhiên.

Xây dựng khái niệm về độ không đảm bảo vào các mô hình, ví dụ như sử dụng phân bố xác suất,

nói chung là một điều tốt.

[BÍP]