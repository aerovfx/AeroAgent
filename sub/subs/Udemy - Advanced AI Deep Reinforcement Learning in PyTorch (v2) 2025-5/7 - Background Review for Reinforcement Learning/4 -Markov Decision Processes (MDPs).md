# 4 -Quy trình Quyết định Markov (MDP) được dịch

---

Trước đây, chúng ta đã học về thuật ngữ, những từ khác nhau mà chúng ta sử dụng để mô tả sự củng cố

vấn đề học tập, cho phép chúng ta giải quyết các vấn đề học tập tăng cường.

Bây giờ bạn đã hiểu các khái niệm như tác nhân, môi trường, chính sách, trạng thái, hành động,

và phần thưởng, chúng ta có thể xây dựng dựa trên điều này.

Mục tiêu là có một khuôn khổ mà sau đó chúng ta có thể sử dụng để tìm giải pháp.

Vì vậy, ở giai đoạn này, chúng tôi vẫn đang làm việc một cách chính xác hơn và trong phạm vi hẹp hơn để tìm ra vấn đề.

Khi chúng ta đã xác định chính xác vấn đề, chúng ta có thể làm việc trong khuôn khổ này và bất cứ điều gì.

giả định mà nó liên quan đến để tìm ra giải pháp.

Giả định chính mà chúng tôi đưa ra trong học tăng cường là giả định Markov.

Đây là điều chúng ta thường thảo luận dưới dạng mô hình Markov và mô hình trình tự, nhưng

Dù sao thì hãy xem lại nó ở đây.

Giả định Markov diễn ra như thế này.

Giả sử chúng ta muốn dự đoán ngày mai sẽ mưa, nắng hay mây.

Có lẽ ý tưởng của bạn có thể dựa trên việc trời mưa, nắng hay mây trong quá khứ

bảy ngày.

Vâng, giả định của Markov là thời tiết ngày mai không phụ thuộc vào tất cả thời tiết trong quá khứ

bảy ngày, chỉ ngày hôm trước.

Đây là một ví dụ khác về giả định Markov.

Giả sử tôi muốn dự đoán từ tiếp theo của câu.

Tôi nói với bạn rằng từ trước trong câu là lười biếng.

Giả định Markov là từ tiếp theo chỉ phụ thuộc vào từ trước đó.

Do đó, nếu giả định Markov là đúng thì bạn có thể dự đoán điều tiếp theo.

từ trong câu của tôi.

Tất nhiên, mọi chuyện không dễ dàng như vậy.

Bạn có thể nghĩ rằng, vì bạn đang tham gia một khóa học của người lập trình viên lười biếng, nên lần tiếp theo

từ trong câu là lập trình viên.

Nhưng thực ra đó không phải là điều tôi nghĩ đến.

Bây giờ giả sử tôi kể cho bạn nghe, câu đầy đủ cho đến giờ là, con cáo nâu nhanh nhẹn nhảy qua

kẻ lười biếng.

Tất nhiên, chúng ta biết rằng, vì chúng ta đã thấy ví dụ này nhiều lần, nên từ tiếp theo

là con chó.

Vì vậy, bạn có thể nghĩ rằng giả định Markov này thực sự không phải là một ý tưởng hay.

Trên thực tế, đã có một số công việc trong học tăng cường, trong đó họ không sử dụng

Giả định Markov, mặc dù điều đó nằm ngoài phạm vi của khóa học này.

Giả định Markov thực sự đã khá thành công cho đến nay.

Nói chung, giả định Markov phát biểu rằng, xác suất của trạng thái tại thời điểm t phụ thuộc

chỉ ở trạng thái tại thời điểm t trừ 1, và không ở bất kỳ trạng thái nào trước đó.

Bản thân giả định Markov là yếu.

Nhưng như bạn nhớ lại, tôi đã nói trước đó rằng chúng ta có thể tạo ra trạng thái bất cứ điều gì chúng ta muốn.

Vì vậy, nếu chúng ta muốn làm cho trạng thái dài 3 hoặc 4 từ cũng được.

Các từ chỉ đơn thuần là những quan sát, nhưng trạng thái được tạo thành từ một chuỗi các quan sát.

Bằng cách này, giả định Markov không tệ như bạn nghĩ ban đầu.

Vậy tại sao chúng ta cần biết về giả định Markov?

Điều này là do các vấn đề học tăng cường thường được mô tả như một quyết định Markov.

quy trình hoặc MDP.

Trước đây, chúng ta chỉ thảo luận về giả định Markov về mặt trạng thái.

Nhưng như bạn đã biết, các bài toán học tăng cường còn liên quan đến các đối tượng khác, đó là các hành động.

và phần thưởng.

Vì vậy, cách chúng tôi mô tả MDP là sử dụng xác suất chuyển trạng thái.

Đó là xác suất đến trạng thái tại thời điểm t cộng 1 và nhận được phần thưởng tại thời điểm

thời điểm t cộng 1 với trạng thái tại thời điểm t và thực hiện hành động tại thời điểm t.

Một cách đơn giản khác để viết cái này mà không cần chỉ số thời gian là viết p của s nguyên tố

n r đã cho s trong a.

Lưu ý rằng vì phần thưởng r không có ký hiệu nguyên tố nên ký hiệu nguyên tố không

chỉ ra thời gian t cộng 1.

Bạn nhận được phần thưởng tại thời điểm t cộng 1 khi đến trạng thái nguyên tố, nhưng chúng tôi không đặt số nguyên tố

biểu tượng trên r.

Như vậy tôi vừa hướng dẫn các bạn cách tổng quát nhất để viết xác suất chuyển trạng thái,

nhưng thường thì chúng ta có thể làm cho nó ít tổng quát hơn.

Ví dụ: nếu chúng ta đang giải một mê cung thì rất có thể chúng ta sẽ nhận được phần thưởng

mang tính quyết định.

Nói cách khác, không cần phải biểu diễn nó dưới dạng phân bố xác suất.

Trong trường hợp này, chúng ta có thể sử dụng ký hiệu p của s nguyên tố cho s trong a và phần thưởng có thể là

một biểu tượng tự nó, thường được ký hiệu là r của s a s prime.

Điều này mã hóa ý tưởng rằng chúng ta đang ở trạng thái s, chúng ta đã thực hiện hành động a và chúng ta đã đến

trạng thái tiếp theo là trạng thái nguyên tố.

Chúng ta thậm chí có thể chỉ cần nói r của s hoặc r của s nguyên tố trong trường hợp phần thưởng chỉ phụ thuộc vào

trạng thái nơi bạn đến, điều này thực sự khá phổ biến.

Một điểm quan trọng cần xem xét là, xác suất chuyển trạng thái có ích gì?

Bạn có thể tưởng tượng rằng nếu chúng ta đang chơi một trò chơi nào đó như Breakout trên Atari thì điều đó rất khó xảy ra

chúng ta sẽ có thể tính được những xác suất này, vì không gian trạng thái sẽ không khả thi

để liệt kê.

Và trên thực tế đối với việc học Q, thuật toán chính mà chúng ta sẽ thảo luận trong phần này, thuật toán này

xác suất hoàn toàn không được sử dụng.

Tôi muốn bạn coi mdp và xác suất chuyển đổi trạng thái như những bước đệm.

Chúng chỉ đơn giản là những công cụ mang tính khái niệm mà chúng ta sẽ sử dụng để nâng cao hơn nữa kiến thức và

đưa chúng ta đến điểm mà chúng ta thực sự có thể nghĩ ra một thuật toán thực tế để tăng cường

học tập.

Nói cách khác, mặc dù chúng ta sẽ không trực tiếp sử dụng xác suất chuyển trạng thái

trong học tập Q, chúng giúp chúng tôi xây dựng dựa trên những gì chúng tôi đã làm cho đến nay để chúng tôi thực sự có thể

đến việc học Q một cách hợp lý.

Tại sao xác suất chuyển trạng thái lại hữu ích?

Hãy tưởng tượng một trò chơi như Tic Tac Toe.

Bạn có thể nghĩ rằng không có gì mang tính xác suất về trò chơi này.

Khi tôi viết x hoặc n0, đó là nơi x hoặc o xuất hiện.

Tại sao có một xác suất liên quan đến điều đó?

Tại sao hành động của tôi không mang tính quyết định?

Và trên thực tế, hành động của bạn hoàn toàn có thể đưa bạn đến

ngày hôm sau.

Ví dụ, hãy tưởng tượng một nhiệm vụ cổ điển được gọi là con lắc ngược.

Trong nhiệm vụ học tăng cường này, công việc của bạn là điều khiển một con lắc lộn ngược sao cho

để nó không rơi xuống khi di chuyển xe sang trái hoặc sang phải khi cần thiết.

Bây giờ bạn có thể tự nghĩ, chúng ta mô tả một hệ thống như vậy như thế nào?

Vâng, chúng tôi sử dụng các định luật vật lý.

Và bây giờ hãy tự nghĩ, phải chăng các định luật vật lý không mang tính quyết định.

Ví dụ, khi chúng ta học ba định luật chuyển động của Newton, các định luật chuyển động đó bao gồm

xác suất, câu trả lời là không.

Vậy thì chúng ta cần xác suất để làm gì?

Câu trả lời là trạng thái của bạn có thể không nắm bắt được đầy đủ tất cả thông tin có thể có về

môi trường.

Hãy xem xét lại Tic Tac Toe.

Trong Tic Tac Toe, có một người chơi khác.

Đặc vụ Tic Tac Toe không thể đoán trước được bước di chuyển của người chơi đó.

Do đó, có nhiều động thái có thể xảy ra giữa hành động trước đó của đại lý.

di chuyển và động thái tiếp theo của đại lý.

Nếu nói về các hệ vật lý, chúng ta cũng phải tính đến lý thuyết hỗn loạn.

Nghĩa là, ngay cả khi bạn biết chính xác các định luật chuyển động, điều này không có nghĩa là bạn có thể

dự đoán tương lai.

Trên thực tế, bạn càng cố gắng dự đoán về tương lai thì những dự đoán của bạn càng không đáng tin cậy.

trở thành.

Đôi khi chúng tôi gọi xác suất chuyển tiếp là động lực của môi trường, điều này làm cho

có ý nghĩa khi bạn nghĩ về nó trong bối cảnh của các hệ thống vật lý.

Một hệ giống như con lắc ngược trên thực tế là một hệ động lực.

Điều cuối cùng tôi muốn đề cập trong bài giảng này là đưa điều này trở lại với bức tranh

bạn có thể đã nhìn thấy nhiều lần vào thời điểm này.

Một MDP hoặc một vấn đề maloning tăng cường bao gồm hai đối tượng này, tác nhân và

môi trường qua lại.

Tác nhân đọc trạng thái từ môi trường và quyết định hành động cần thực hiện.

Nó thực hiện hành động đó trong môi trường.

Môi trường được cập nhật dựa trên hành động đó và đưa tác nhân sang trạng thái tiếp theo trong khi

cũng trả lại một phần thưởng liên quan.

Sau đó, tác nhân có thể đọc trạng thái tiếp theo này, thực hiện hành động tiếp theo, v.v.

Vì thế họ chỉ đi tới đi lui theo hình tròn.

Những gì chúng ta đã làm cho đến nay là biểu diễn cả hai đối tượng này bằng xác suất.

Môi trường được biểu diễn bằng xác suất chuyển trạng thái, P của S prime và

R cho trước S và A. Tác nhân được biểu thị bằng xác suất pi của A cho trước S.

Điều này hữu ích hơn những gì bạn có thể nhận ra vào thời điểm này.

Bằng cách biểu diễn cả tác nhân và môi trường dưới dạng xác suất, nó cho phép chúng ta mô tả

củng cố các vấn đề học tập về mặt toán học.

Đặc biệt, khi có phương trình thì chúng ta có thể giải được phương trình đó.

Không có phương trình thì thực sự không có gì để giải.

Đó là một cái nhìn sâu sắc khá sâu sắc.

Để tìm ra giải pháp, chúng ta phải xác định rõ vấn đề.

Sử dụng toán học, cụ thể là xác suất, cho phép chúng ta tạo ra vấn đề được xác định rõ ràng này

và đó là bước đầu tiên để tìm ra giải pháp.