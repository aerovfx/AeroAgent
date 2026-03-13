# 5 -Dịch chính xác dự đoán từ được che giấu

---

Liên quan đến sự bối rối là việc xem xét độ chính xác của việc dự đoán từ bị che giấu.

Ý tưởng rất đơn giản.

Bạn bắt đầu bằng một câu hoặc một chuỗi dấu hiệu nào đó, sau đó che giấu một từ trong câu và

xem liệu LLM có dự đoán được từ còn thiếu hay không.

Cách tiếp cận này chủ yếu hữu ích với mô hình kiểu BERT vì nó không sử dụng mô hình nhân quả.

mặt nạ chú ý, điều đó có nghĩa là các mô hình này có thể sử dụng các từ sau trong chuỗi để dự đoán

một từ còn thiếu trước đó trong chuỗi.

Mặt khác, khi tôi cho bạn xem ví dụ ở slide tiếp theo, nó sẽ khá rõ ràng.

rằng ngay cả khi mô hình không chính xác về mặt kỹ thuật, theo nghĩa là nó không dự đoán được

từ mục tiêu thực tế, những từ mà mô hình dự đoán có thể liên quan chặt chẽ đến

từ mục tiêu thực tế.

Vì vậy, con người chúng ta có lẽ sẽ không thực sự coi nó là hoàn toàn sai và để đo lường

sự liên quan về mặt ngữ nghĩa đó, chúng ta sẽ sử dụng độ tương tự cosine.

Hiện tại, không có nhiều lý thuyết hay toán học mà bạn cần phải hiểu.

Bản demo mã này mà bạn chưa biết, vì vậy hãy để tôi cung cấp cho bạn cái nhìn tổng quan về

Bản demo Python và sau đó chúng ta sẽ bắt đầu.

Sử dụng mã thông báo và mô hình BERT, tôi sẽ mã hóa câu này.

Chủ nghĩa lập thể là một phong trào nghệ thuật khơi dậy sự đổi mới trong âm nhạc và kiến ​​trúc.

Bây giờ nếu chúng ta chỉ tập trung vào nghệ thuật chữ, chúng ta có thể tách riêng nhật ký cho mã thông báo đó và xem

những gì mô hình dự đoán sẽ là từ này dựa trên ngữ cảnh của nó.

Và hóa ra trong trường hợp này, người mẫu đã dự đoán chính xác từ nghệ thuật.

Đây là nhật ký cho toàn bộ từ vựng và nhật ký lớn nhất là mã thông báo

tương ứng với nghệ thuật.

Vì vậy, trong trường hợp này, mô hình đã sử dụng chính xác ngữ cảnh để dự đoán từ còn thiếu.

Mặt khác, bạn có thể thấy rằng có một số token khác cũng có giá khá cao.

giá trị logit.

Và nếu chúng ta xem những mã thông báo đó là gì, bạn có thể thấy mã thông báo đó trong số 10 nhật ký hoặc mã thông báo hàng đầu

cũng có thể phù hợp với câu này, chúng đều có ý nghĩa về mặt ngữ nghĩa và chúng có thể

phù hợp với câu này thay cho từ nghệ thuật.

Vì vậy, điều này có nghĩa là, ví dụ, nếu mô hình thực sự có logit cao nhất cho từ

nghệ thuật, thì về mặt kỹ thuật, phân loại, điều đó không đúng vì nghệ thuật và nghệ thuật có những điểm khác nhau.

mã thông báo.

Nhưng rõ ràng ý nghĩa sẽ giống nhau.

Vì vậy, điều đó không thực sự tương đương với, ví dụ, nếu mô hình đã dự đoán từ cannelope

hoặc một cái gì đó.

Vì vậy, một cách chúng ta có thể đánh giá mức độ liên quan là tính toán độ tương tự cosin giữa

mã thông báo mà mô hình dự đoán và mã thông báo thực tế trong câu.

Và đó là những gì bạn thấy ở đây.

Vì vậy, điều tôi đã làm là lặp lại tất cả các từ trong câu, che đi từng từ riêng lẻ

mã thông báo.

Và ở giữa là dấu hiệu mà mô hình sinh dự đoán sẽ ở đó.

Và ở đây, bạn thấy sự tương đồng cosine với mã thông báo mục tiêu.

Và tất nhiên, đây là độ tương tự cosine của các vectơ nhúng chứ không phải mã thông báo

chính họ.

Đó chỉ là số nguyên.

Và điều đó có nghĩa là sự giống nhau về cách thể hiện trong nội bộ sau này trong

mô hình có thể cao hơn đáng kể vì việc nhúng mã thông báo không phản ánh ảnh hưởng

của bối cảnh xung quanh.

Dù sao đi nữa, hãy chuyển sang Python và xem xét.

Vì vậy, một số thư viện ở đây.

Tôi đang nhập mô hình được đào tạo trước của Bert và đây cũng là mô hình.

Và đây là tokenizer của nó.

Một lần nữa, bạn sẽ thấy rất nhiều điều này trong suốt phần còn lại của khóa học này.

Chúng tôi không tập luyện nữa.

Vì vậy, bạn luôn muốn chuyển mô hình sang chế độ eval.

Được rồi.

Thế nên tôi có câu này đây.

Đây là từ trang wiki này về chủ nghĩa lập thể.

Được rồi.

Và bây giờ tôi chỉ đang mã hóa nó.

Hầu hết các từ trong câu này được biểu thị bằng các ký hiệu riêng lẻ ngoại trừ chủ nghĩa lập thể, vốn

đã chia thành cub và hash ism.

Điều đó thực sự sẽ phù hợp với một số token mà mô hình có thể dự đoán

sẽ ở đây.

Được rồi.

Vì vậy, bây giờ tôi cũng thực hiện chuyển tiếp với torch.nograd.

Và ở đây tôi đang xử lý tất cả các mã thông báo.

Bây giờ tôi chưa che giấu bất kỳ mã thông báo nào.

Vì vậy, trong trường hợp này, trong ví dụ này ở đây, mô hình đang nhận được tất cả các mã thông báo hợp lệ và

tất cả những gì tôi đang tìm kiếm là xem dự đoán logic tối đa cho mã thông báo năm là bao nhiêu.

Và tất nhiên, điều này đề cập đến chỉ số năm ở đây, thực tế là mã thông báo thứ sáu.

Được rồi.

Vì vậy, ở đây tôi nhận được tất cả các bản ghi.

Và ở đây tôi chỉ tìm thấy đâu là token có logic lớn nhất.

Và đó là những gì tôi đánh dấu bằng màu xanh lá cây ở đây.

Vì vậy, ở đây bạn thấy tất cả nhật ký của tất cả 30.000 mã thông báo trong từ vựng của Bert.

Và vòng tròn màu xanh lá cây này làm nổi bật vòng tròn lớn nhất, tương ứng với từ nghệ thuật.

Và vâng, đó cũng là điều đúng đắn.

Vì vậy, hãy quay lại và xem chuỗi mã thông báo này ở đây.

Vì vậy, ở đây chúng ta có mã số 0, một, hai, ba, bốn, năm.

Vì vậy, nó thực sự là nghệ thuật chữ.

Và giá trị mã thông báo lớn nhất cho giá trị đó hoặc giá trị logic lớn nhất cho vị trí thứ tự đó

tương ứng với từ nghệ thuật.

Bây giờ có thể bạn nghĩ rằng điều đó không thú vị lắm bởi vì đó thực sự là từ mà

đọc mô hình.

Được rồi.

Vì vậy, bây giờ những gì chúng ta sẽ làm là sử dụng mặt nạ.

Vì vậy, thay vì sử dụng nghệ thuật chữ thực sự, tôi sẽ đặt mặt nạ chữ viết hoa toàn bộ và bao quanh

bằng dấu ngoặc vuông.

Vì vậy, chúng ta hãy xem xét mã thông báo của điều này.

Bây giờ bạn thấy rằng Bert thực sự nhận ra chìa khóa này, nhân vật đặc biệt này với tư cách là một cá nhân

mã thông báo.

Đó là một trong ba mã thông báo thực sự xuất hiện ngay sau mã thông báo CLS và một SCF dành cho

một mã thông báo phân cách.

Vậy là chúng ta có mã thông báo mặt nạ.

Đây là mã thông báo dành riêng đặc biệt được sử dụng trong Bert mà mô hình sẽ bỏ qua nhưng vẫn cố gắng

dự đoán.

Được rồi.

Vì vậy, từ nghệ thuật không thực sự xuất hiện ở bất cứ đâu trong câu này.

Vì vậy, người mẫu không bao giờ thực sự nhìn thấy chữ nghệ thuật.

Thay vào đó nó nhìn thấy từ mặt nạ.

Và bây giờ chúng ta có thể lặp lại chính xác phân tích mà chúng ta đã làm ở trên.

Và bây giờ chúng ta có thể thấy mã thông báo mà mô hình dự đoán sẽ thay thế cho mặt nạ là gì.

Vì vậy, một lần nữa, tất cả chỉ là mã lặp lại.

Vì vậy, hãy che dấu mã thông báo IDX, nó ở ngay đây.

Vì vậy, ở đây tôi đang tìm nơi mã thông báo bằng ID mã thông báo mặt nạ.

Đó là mã thông báo đặc biệt trong mã thông báo giảm giá cho chính xác mã thông báo này cho mặt nạ từ.

Được rồi.

Vậy thì vâng, bạn thấy mô hình vẫn thực sự dự đoán được từ nghệ thuật.

Dù không thực sự nhìn thấy chữ nghệ thuật nhưng người mẫu chỉ nhìn vào ngữ cảnh

và quyết định rằng thứ phù hợp nhất ở đây sẽ là nghệ thuật chữ hoặc biểu tượng cho

từ nghệ thuật.

Được rồi.

Và bây giờ, vâng, đây là những gì tôi đã trình bày trước khi chúng ta có thể xem xét 10 giá trị logic hàng đầu

và in ra lời nói của họ.

Vì vậy, mô hình dự đoán rằng từ còn thiếu sẽ là nghệ thuật, nhưng nó cũng dự đoán rằng

nó có thể là nghệ thuật, thẩm mỹ, Mỹ, và vân vân, trí tuệ, công nghiệp.

Và nếu bạn quay lại câu ban đầu, bạn có thể thêm bất kỳ từ nào trong số này và

câu nói cũng có nhiều ý nghĩa.

Vì vậy, hãy thử điều này với kiến ​​trúc.

Chủ nghĩa lập thể là một phong trào kiến ​​trúc khơi dậy sự đổi mới trong âm nhạc và kiến ​​trúc.

Được rồi.

Vì vậy, từ kiến ​​trúc tồn tại ở đó.

Nhưng bạn biết đấy, chúng ta có thể thực hiện phong trào trí tuệ ở đây và điều đó vẫn có hiệu quả.

Được rồi.

Vì vậy, đó là dự đoán mã thông báo bị che giấu.

Và đó là cho một mã thông báo.

Và bây giờ những gì tôi đang làm trong vòng lặp for ở đây về cơ bản là lặp lại điều này cho tất cả

của từng từ riêng lẻ trong câu đó.

Vì vậy, từ văn bản mã thông báo hoặc mã thông báo đó, tôi sẽ thay thế từng mã thông báo riêng lẻ

bằng mã thông báo mặt nạ và sau đó chạy lại phân tích.

Chỉ cần lấy nhật ký ra, đó là dự đoán của mô hình về mã thông báo đó.

Bạn thấy đấy, đây chỉ là để hiển thị cho bạn tất cả các chuỗi mã thông báo.

Vì vậy, 103, bạn có thể thấy đi xuống theo đường chéo, đó là mã thông báo mặt nạ.

Và đó chỉ là minh họa những gì chúng ta đang làm ở đây, những gì tôi đang triển khai trong vòng lặp for này.

Vì vậy, lặp lại toàn bộ văn bản và thay thế từng từ riêng lẻ bằng mặt nạ.

Được rồi.

Và sau đó chúng ta có thể kiểm tra kết quả.

Đây là nhìn qua.

Vì vậy, đây là văn bản gốc.

Chủ nghĩa lập thể là một phong trào nghệ thuật khơi dậy sự đổi mới trong âm nhạc và kiến ​​trúc.

Và chúng tôi thay thế từng từ riêng lẻ bằng một mặt nạ và yêu cầu, chịu đựng để điền vào dựa trên

ngữ cảnh, nó nghĩ từ đó nên như thế nào.

Chúng tôi hiểu chủ nghĩa tối giản là một loại hình nghệ thuật bao gồm sự quan tâm đến nghệ thuật và thời kỳ.

Vì vậy, nó không hoàn toàn giống nhau, nhưng bạn có thể thấy nó đang hoạt động khá tốt.

Nó chắc chắn có liên quan chặt chẽ về mặt ngữ nghĩa với văn bản gốc.

Được rồi.

Và đây chỉ là mã để in ra bảng mà tôi đã trình bày trước đây.

Một lần nữa, vấn đề ở đây là ngay cả khi xu hướng giảm là không chính xác về mặt kỹ thuật, thì nó vẫn

vẫn nhận được một từ khá gần.

Vì vậy, chuyển động và hình thức đã khơi dậy và bao gồm những đổi mới và sự quan tâm, v.v.

Một trong những điểm mà tôi muốn truyền tải trong video này, đó là một chủ đề xuyên suốt

toàn bộ phần này là rất khó để đánh giá hiệu suất và

khả năng của mô hình ngôn ngữ

Đánh giá định lượng rất tuyệt vời vì chúng là những con số mà chúng ta có thể sử dụng và so sánh.

Nhưng những con số đó hiếm khi phản ánh thực sự khả năng, hiệu suất và ứng dụng của mô hình.

Vì vậy, trong trường hợp này, trong video này, bạn đã thấy rằng ngay cả khi mô hình không chính xác về mặt kỹ thuật

khi đánh giá định lượng, bạn cần tìm hiểu sâu hơn một chút và xem liệu

mô hình vẫn đang truyền tải thông tin phù hợp nhưng chỉ sử dụng các từ khác nhau.