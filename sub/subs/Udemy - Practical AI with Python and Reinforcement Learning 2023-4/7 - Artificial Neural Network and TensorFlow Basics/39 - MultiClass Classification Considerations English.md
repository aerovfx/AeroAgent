# 39 - Cân nhắc phân loại nhiều lớp

---

Chào mừng mọi người trở lại với bài giảng này về hàm kích hoạt đa lớp, vì vậy trước đây chúng ta chỉ

đã thấy rằng tất cả các chức năng kích hoạt trong bài giảng trước, điều đó có ý nghĩa đối với một điều gì đó

đầu ra duy nhất.

Hoặc bạn đang cố gắng dự đoán nhãn liên tục hoặc bạn đang cố gắng dự đoán thứ gì đó bằng phân loại nhị phân

vấn đề.

Điều đó có nghĩa là bạn muốn số 0 hoặc số 1 hoặc số nào đó nằm trong khoảng từ 0 đến 1 và chỉ định xác suất.

Nhưng chúng ta phải làm gì nếu thực sự rơi vào tình trạng đa giai cấp và tình trạng đa giai cấp?

Lớp đầu ra thực sự sẽ có nhiều nơ-ron.

Vì vậy, hãy nhớ rằng có hai loại tình huống đa lớp chính, đó là tình huống lớp không độc quyền

và về cơ bản không độc quyền có nghĩa là một điểm dữ liệu thực sự có thể có nhiều lớp hoặc danh mục

được giao cho nó.

Một tình huống lớp loại trừ lẫn nhau, thường là khi bạn học về học máy,

loại phổ biến hơn là loại bạn chỉ có thể có một lớp cho mỗi điểm dữ liệu.

Vì vậy, hãy tiếp tục xem xét các hàm kích hoạt cho hai trường hợp sử dụng này.

Vì vậy, trước hết, đối với những thứ như các lớp không độc quyền, một lần nữa, đó là nơi một điểm dữ liệu có thể có nhiều

các lớp hoặc danh mục được gán cho nó.

Vì vậy, ví dụ: hãy tưởng tượng dữ liệu của bạn là một bức ảnh.

Một bức ảnh có thể có nhiều thẻ.

Nó có thể được gắn thẻ kỳ nghỉ gia đình ở bãi biển, v.v.

Vì vậy, có thể có nhiều lớp hoặc danh mục sau đó được gán cho một bức ảnh duy nhất.

Lớp rất loại trừ lẫn nhau, điểm dữ liệu chỉ có thể được gán một lớp hoặc danh mục cho nó.

Vì vậy, ví dụ: ảnh có thể được Katara phân loại thành thang độ xám, đen trắng hoặc toàn bộ

màu sắc.

Một bức ảnh thực sự không thể có cả hai cùng một lúc.

Nó có màu xám, đen trắng hoặc đủ màu.

Bạn không thể chỉ định cả hai lớp đó cho một điểm dữ liệu duy nhất có ý nghĩa.

Vì vậy, đó là loại trừ lẫn nhau.

Vì vậy, điều tôi muốn làm trước tiên là tìm ra cách chúng ta thực sự sắp xếp dữ liệu chứa nhiều lớp

và cách dễ nhất để tổ chức nhiều lớp là chỉ cần có một nút đầu ra cho mỗi lớp.

Vì vậy, trước đây, nếu nhìn lại mạng lưới thần kinh mà chúng ta đã vẽ ra và minh họa, chúng ta

coi lớp đầu ra bị mất đó là một nút duy nhất.

Ghi chú đó có thể tạo ra một giá trị hồi quy liên tục hoặc phân loại nhị phân hoặc một hoặc có thể

một số giá trị giữa 0 hoặc một.

Tuy nhiên, bây giờ chúng ta hãy mở rộng lớp này lên để giải quyết trường hợp phân loại đa dạng.

Vì vậy, kết quả cuối cùng là chúng ta có lớp đầu vào ngay từ đầu, sau đó chúng ta có một số

lớp ẩn và sau đó chúng ta có lớp đầu ra cuối cùng.

Lớp đầu ra cuối cùng của chúng tôi về cơ bản là một nơ-ron cho mỗi lớp, vì vậy sẽ có một năm cho lớp một,

lớp hai, cho đến hết lớp.

Vì vậy, điều này có nghĩa là chúng ta cần sắp xếp các danh mục cho lớp đầu ra này.

Chúng tôi sẽ không thể cung cấp một danh mục mạng lưới thần kinh.

Nó giống như một sợi dây màu đỏ, xanh dương hoặc xanh lục.

Hãy nhớ lại rằng mạng lưới thần kinh sẽ nhận các giá trị X và những giá trị đó phải là số.

Sau đó, nó có thể áp dụng trọng số cho chúng và thêm độ lệch.

Bạn thực sự không thể nhân các từ màu đỏ, xanh lam hoặc xanh lục và thường là các điểm dữ liệu thực.

Khi chúng ta có các lớp học, chúng sẽ là những thứ như sắp xếp mã chuỗi để tìm ra cách chúng ta thực sự thực hiện

biến đổi dữ liệu của chúng tôi một cách chính xác để có thể sử dụng mạng thần kinh cho các tình huống nhiều lớp.

Vì vậy, điều chúng tôi có thể làm là thay vào đó chúng tôi có thể sử dụng thứ được gọi là mã hóa nóng, bạn có thể cũng đã nghe nói

cái này gọi là biến giả.

Vì vậy, chúng ta hãy xem điều này trông như thế nào đối với các lớp loại trừ lẫn nhau.

Đối với các lớp loại trừ lẫn nhau, bạn có thể có thứ gì đó trông như thế này, bạn có dữ liệu

điểm và sau đó là một lớp thuộc về mỗi điểm dữ liệu.

Ở đây bạn có thể thấy điểm dữ liệu một là màu đỏ, sau đó hai là màu xanh lá cây, ba là màu xanh lam cho đến khi điểm dữ liệu

và có màu đỏ.

Bây giờ, chúng ta sẽ không thể đưa các chuỗi mã màu đỏ, xanh lá cây và xanh lam này vào hệ thống thần kinh của chúng ta.

mạng.

Vậy làm thế nào để chúng ta thực sự tổ chức việc này, đặc biệt là xem xét lớp đầu ra cuối cùng?

Chà, thực ra chúng ta có thể làm chỉ là sử dụng phân loại nhị phân cho mỗi lớp, và những gì chúng ta làm là kết thúc

đang xây dựng một ma trận để chúng ta có thể thấy ở đây chúng ta thấy điểm dữ liệu một là một cho màu đỏ và sau đó là 0 cho phần còn lại

của các lớp đó.

Khi đó, điểm dữ liệu thứ hai bằng 0 cho màu đỏ, một cho màu xanh lá cây và 0 cho màu xanh lam.

Và bạn có thể thấy về cơ bản chúng tôi có thể mở rộng ý tưởng này như thế nào.

Vì vậy, một lần nữa, đây được gọi là một mã hóa và những người khác gọi đây là việc tạo ra các biến giả.

Bây giờ, đối với các lớp không độc quyền, nó sẽ hơi khác một chút, hãy nhớ lại ở các lớp không độc quyền

có nghĩa là mỗi điểm dữ liệu thực sự có thể có nhiều lớp được gán cho nó, chẳng hạn như một bức ảnh có nhiều

thẻ hoặc danh mục được gán cho nó.

Vì vậy, chúng ta có thể thấy ở đây điểm dữ liệu có các lớp và được gán cho nó.

Điểm dữ liệu tới là điểm dữ liệu thứ ba có CMB, v.v. Vì vậy, chúng tôi thực sự đã thực hiện cùng một ý tưởng, ngoại trừ

bây giờ điểm dữ liệu có thể có giá trị là một cho nhiều danh mục.

Vì vậy, ý tưởng tương tự ở đây.

Về cơ bản, bạn đang ở nơi điểm dữ liệu đó khớp với một lớp hoặc danh mục.

Bạn chỉ định một giá trị bằng 1 ở mọi nơi khác mà bạn chỉ định giá trị bằng 0, về cơ bản là chuyển đổi hoặc mã hóa

thông tin chuỗi đó là nóng, về cơ bản cho thấy rằng một có nghĩa là bật và số 0 là tắt.

Vì vậy, bây giờ chúng ta đã sắp xếp dữ liệu một cách chính xác và một mặt chúng ta sẽ sắp xếp dữ liệu, bao gồm

dữ liệu của chúng tôi sau và chúng tôi thực sự đang mã hóa, tôi muốn bạn làm là chọn kích hoạt phân loại chính xác

chức năng mà lớp đầu ra cuối cùng nên có.

Vì vậy, nếu bạn đang xử lý không độc quyền, thì bạn chỉ có thể sử dụng hàm sigmoid vì mỗi nơ-ron

sẽ xuất ra một giá trị từ 0 đến 1 cho biết xác suất có lớp đó được gán cho

nó.

Vì vậy, điều này trông giống như về cơ bản là chúng ta sẽ có một nơ-ron cho mỗi lớp.

Một lần nữa, điều này không độc quyền, do đó các điểm dữ liệu có thể được gán nhiều lớp cho chúng, khi đó bạn

cuối cùng chỉ cần đặt một hàm sigmoid.

Hãy nhớ lại hàm sigmoid, còn được gọi là hàm logistic.

Nó có thể luôn luôn bằng không và một.

Và sau đó tất cả đầu ra của các nơ-ron đó sẽ sáng lên ở khoảng từ 0 đến 1.

Và điều cuối cùng bạn làm là nói, được rồi, trong trường hợp cụ thể này, điểm dữ liệu này có 80

phần trăm khả năng thuộc về Lớp một, cũng như có 20 phần trăm khả năng thuộc Lớp

hai người được giao cho nó và sau đó có thể có 30% khả năng được tham gia lớp học.

Và vì vậy chúng ta có thể chỉ nói, được rồi, hãy tiếp tục và gán lớp một cho điểm dữ liệu này.

Tuy nhiên, hãy nhớ rằng khi chúng ta xử lý các lớp không độc quyền, bạn có thể thấy ở đây chúng ta hãy

nói RAM một điểm dữ liệu khác.

Và tôi tình cờ nói rằng lớp một là sau khi trải qua một hàm sigmoid, lớp 0,8 đến

0 điểm 6 đối với trường hợp không loại trừ, nếu điểm giới hạn của tôi ở 0 điểm 5 thì thực tế tôi sẽ

chỉ định ở đây cho các lớp hoặc hai loại.

Điểm dữ liệu này, tôi muốn nói rằng cả Lớp một và Lớp hai sẽ được gán cho điểm dữ liệu này

vì tôi đang làm việc với các lớp không độc quyền.

Một lần nữa, các lớp không độc quyền nên các điểm dữ liệu có thể được chỉ định nhiều danh mục hoặc nhiều lớp.

Vì vậy, trong trường hợp này, vì Loại một và loại hai vi phạm ở nửa điểm 0,5, chúng tôi

gán cả một và hai cho điểm dữ liệu cụ thể này.

Vì vậy, như tôi vừa đề cập, đối với các lớp không độc quyền mà chúng ta đang sử dụng hàm sigmoid đó, hãy luôn giữ

hãy nhớ rằng điều đó cho phép mỗi nơ-ron xuất ra độc lập với các lớp khác.

Vì vậy, nó cho phép một điểm dữ liệu duy nhất được đưa vào hàm có thể được gán nhiều lớp cho nó.

Bây giờ, chúng ta phải làm gì khi mỗi điểm dữ liệu thực sự chỉ có thể được gán một lớp duy nhất cho nó?

Chà, để làm được điều này, có một chức năng kích hoạt softmax thực sự thông minh.

Vì vậy, hàm softmax trông giống như thế này và về cơ bản điều cuối cùng bạn làm là gọi lại

ở đây chúng ta có Z là đầu vào thực tế của lớp đầu ra cuối cùng.

Và những gì chúng ta sắp có thể làm là với hàm softmax cụ thể này, hãy lưu ý rằng nó thực sự

có AI bằng 1 thì đến K và K ở đây tượng trưng cho số lượng danh mục.

Và về cơ bản điều này làm là chức năng của nghi phạm tính toán xác suất, phân bố

của sự kiện qua k sự kiện khác nhau.

Và trong trường hợp này, chúng tôi chỉ có các lớp khác nhau.

Vì vậy, hàm này tính toán xác suất của từng lớp mục tiêu trên tất cả các lớp mục tiêu có thể có.

Vì vậy, phạm vi sẽ từ 0 đến 1 và điều thực sự quan trọng ở đây là khi bạn sử dụng softmax

hàm kích hoạt, tổng tất cả các xác suất sẽ bằng một.

Vì vậy, điều đó có nghĩa là trong lớp đầu ra đó, khi bạn chuyển qua hàm softmax, tổng của

tất cả các xác suất ở đầu ra đều bằng một.

Vì vậy, khi mô hình trả về, bạn sẽ làm được xác suất của mỗi lớp.

Lớp mục tiêu được chọn bởi nơ-ron có xác suất cao nhất.

Vậy thực chất điều này trông như thế nào?

Chà, điều chính cần ghi nhớ là, một lần nữa, chúng ta đang xử lý các lớp loại trừ lẫn nhau.

Vì vậy, đối với loại vấn đề đó, sau khi bạn áp dụng softmax, bạn sẽ nhận được kết quả đầu ra trông giống như

cái này.

Bạn có một số vị trí chỉ mục phù hợp với các nơ-ron đó trong lớp đầu ra và sau đó là Softmax

cung cấp xác suất cho mỗi lớp.

Vì vậy, chúng ta có thể thấy ở đây đối với điểm dữ liệu cụ thể này, chúng ta có 0 điểm một cho màu đỏ, 0 điểm sáu cho

màu xanh lá cây và điểm 0 cho màu xanh lam.

Bạn sẽ nhận thấy rằng tổng của tất cả các xác suất đó bằng một, điều này hợp lý vì

tổng trên toàn bộ không gian xác suất phải bằng một, vì về cơ bản điều đó trả lời câu hỏi

rằng có 100% khả năng điểm dữ liệu này thuộc về một trong những lớp này.

Nhưng nếu chúng ta tìm hiểu sâu hơn về điều này, về cơ bản điều này nói lên rằng có 10% khả năng nó thuộc về việc đọc

60% khả năng nó thuộc về màu xanh lá cây và 30% khả năng nó thuộc về màu xanh lam.

Vì vậy, đối với trường hợp cụ thể này, chúng tôi sẽ chọn Màu xanh lá cây làm phân loại cho trường hợp loại trừ lẫn nhau này.

lớp và nói rằng mạng này tin rằng điểm dữ liệu cụ thể này có màu xanh lá cây và nó cho điểm 60

phần trăm cơ hội có màu xanh lá cây.

Và như tôi đã lưu ý, xác suất của mỗi lớp đều bằng một, đó là xác suất cao nhất

như nhiệm vụ của chúng tôi.

Vì vậy, để xem lại lý thuyết mà chúng ta đã trình bày cho đến nay, chúng ta hiểu Perceptron cơ bản về cách chúng có thể mở rộng

đến mô hình mạng nơ-ron.

Chúng tôi hiểu trọng số và độ lệch cũng như cách chúng được chuyển vào bằng chức năng kích hoạt.

Và chúng ta cũng tìm hiểu về các hàm kích hoạt cụ thể cho các tình huống nhiều lớp.

Tuy nhiên, chúng ta chưa thực sự thảo luận về cách mạng thực sự học.

Làm cách nào để chúng tôi cập nhật các trọng số và thành kiến ​​này nhằm cải thiện hiệu suất của mình?

Ban đầu, tất cả đều bắt đầu chỉ với các trọng số ngẫu nhiên và chạy các giá trị sai lệch.

Cuối cùng, chúng ta sẽ tìm ra cách mạng này thực sự học cách chọn trọng số chính xác.

Và để làm được điều đó, trước tiên chúng ta đã tìm hiểu về các hàm chi phí và sau đó chúng ta có thể tìm hiểu về những thứ như độ dốc

truyền xuống và lan truyền ngược.

Vì vậy, chúng ta hãy tiếp tục tìm hiểu các hàm chi phí trong bài giảng tiếp theo.

Tôi sẽ gặp bạn ở đó.