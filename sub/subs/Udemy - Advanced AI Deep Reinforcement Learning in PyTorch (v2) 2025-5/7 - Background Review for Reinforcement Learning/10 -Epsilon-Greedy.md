# 10 -Epsilon-Tham lam dịch

---

Ở phần đầu của phần này, tôi đã nói với bạn về giá trị của việc coi chính sách như một xác suất

phân phối.

Đầu tiên, nó cho phép chúng ta mô tả toàn bộ MDP như một tập hợp gồm hai xác suất, một đại diện cho

động lực môi trường và một đại diện cho tác nhân.

Điều này cho phép chúng ta suy luận về MDP về mặt toán học và tìm ra giải pháp cho cả dự đoán

và kiểm soát vấn đề như chúng ta vừa làm.

Lý do quan trọng khác mà tôi đã đề cập ngắn gọn trước đó là để tìm ra

hành động tốt nhất thì trước tiên chúng ta phải biết kết quả của việc thực hiện các hành động khác nhau.

Nói cách khác, chúng ta phải thu thập những mẫu đó.

Đây là vấn đề.

Khi chúng tôi thực hiện các hành động tổng thể argmax, Q của SA, giá trị Q ở đây không thay đổi điều đó

nhiều từ tập này sang tập khác.

Giả sử chúng ta có ba hành động, vì vậy chúng ta muốn chọn từ Q của SA1, Q của SA2 và Q của SA1.

SA3.

Chà, có lẽ chúng ta đã khởi tạo Q của SA1 và Q của SA2 về 0, trong khi chúng ta đã khởi tạo Q của SA3 thành

1.

Cũng giả định rằng tất cả các phần thưởng đều tích cực.

Trong quá trình chơi game, có thể Q của SA3 được cập nhật lên giá trị là 2.

Bây giờ chúng ta sẽ luôn chọn hành động 3 vì điều đó mang lại cho chúng ta giá trị Q tốt nhất trong số ba hành động đó.

những hành động có thể.

Vấn đề là chúng ta không biết giá trị thực của Q của SA1 và Q của SA2 vì chúng ta chưa bao giờ thu thập được

dữ liệu từ việc thực hiện những hành động đó.

Làm sao chúng ta biết giá trị của các hành động khác nếu chúng ta chưa bao giờ thực sự thực hiện những hành động đó?

Trên thực tế, chúng ta hoàn toàn không biết những giá trị đó.

Chúng tôi chỉ tình cờ khởi tạo chúng về 0.

Vì lẽ đó, chúng ta không cách nào có thể tự tin lựa chọn hành động đúng đắn.

Đây là một vấn đề tổng quát hơn được gọi là Thế lưỡng nan khám phá.

Giả sử bạn đến một sòng bạc và đang chơi một phiên bản đơn giản của máy đánh bạc.

Bạn có nhiều máy đánh bạc để lựa chọn và bạn không biết nên chọn máy nào

chơi.

Tuy nhiên, bạn có biết rằng không phải tất cả các máy đánh bạc này đều mang lại phần thưởng như nhau.

Như tôi đã nói, những máy đánh bạc này được đơn giản hóa nên chỉ có hai kết quả có thể xảy ra.

Bạn có thể thắng hoặc bạn thua.

Nếu bạn thắng, bạn nhận được 1 đô la và nếu bạn thua, bạn nhận được 0 đô la.

Rõ ràng là bạn muốn chơi máy đánh bạc mà cơ hội chiến thắng của bạn là cao nhất.

Được rồi, vậy làm thế nào bạn có thể tìm ra máy đánh bạc nào sẽ cho bạn cơ hội chơi tốt nhất?

Sự khác biệt của chiến thắng là gì?

Chà, bạn không thể hỏi người quản lý sòng bạc vì anh ta muốn kiếm tiền.

Anh ấy sẽ không chia sẻ thông tin đó với bạn.

Vậy bạn làm gì?

Phương pháp duy nhất của bạn để tìm ra máy đánh bạc nào tốt nhất là thu thập một số dữ liệu.

Vì vậy, giả sử bạn chơi mỗi máy đánh bạc 1.000 lần.

Tỷ lệ thắng của máy đánh bạc chỉ đơn giản bằng số lần bạn thắng chia cho

tổng số lần bạn đã chơi.

Nhưng có vấn đề gì với việc chúng ta vừa làm vậy?

Giả sử bạn phải chọn giữa năm máy đánh bạc.

Nếu bạn chơi mỗi máy đánh bạc 1.000 lần, điều đó có nghĩa là bạn đã chơi 5.000 trò chơi.

Bây giờ hãy để tôi nhắc bạn rằng chơi máy đánh bạc ở sòng bạc không miễn phí.

Nói chung, việc thu thập dữ liệu không miễn phí.

Nó thường đòi hỏi thời gian, nguồn lực hoặc cả hai.

Giả sử mỗi lần bạn chơi máy đánh bạc, bạn tiêu 25 xu.

Bạn cần phải thắng ít nhất một trong bốn lần để hòa vốn.

Hãy tưởng tượng rằng đối với một số máy đánh bạc này, bạn thắng không lần nào.

Bây giờ rõ ràng là chơi những máy đánh bạc đó 1.000 lần sẽ là một sự lãng phí rất lớn

cả về thời gian và tiền bạc.

Đây là một câu hỏi khác để xem xét.

Tại sao chúng ta nên thu thập 1.000 mẫu trên mỗi máy đánh bạc?

Tại sao không phải là 100? Tại sao không phải là 10?

Như bạn đã biết, bạn thu thập càng nhiều mẫu thì ước tính của bạn càng chính xác và chính xác hơn.

Thật không may, điều này cũng đồng nghĩa với việc phải chi nhiều thời gian và tiền bạc hơn.

Đó là lý do tại sao chúng tôi gọi đây là một vấn đề nan giải.

Vấn đề nan giải về khai thác Explorer có nghĩa là chúng tôi đang cố gắng cân bằng cả việc thăm dò và khai thác.

Chúng tôi muốn khám phá để có thể thu thập thêm dữ liệu nhằm tìm ra máy đánh bạc nào thực sự tốt nhất.

Mặt khác, chúng tôi muốn khai thác vì chúng tôi muốn chơi thứ mà chúng tôi tin là máy đánh bạc tốt nhất

để giành chiến thắng thường xuyên hơn và kiếm được nhiều tiền hơn.

Hai lực lượng này luôn đối lập nhau.

Câu trả lời điển hình cho vấn đề này trong học tăng cường được gọi là Epsilon Gritty.

Điều này cho phép chúng ta tham lam và khai thác những gì chúng ta nghĩ sẽ mang lại tổng phần thưởng cao nhất trong tương lai.

Nhưng chúng ta có một xác suất nhỏ để Epsilon chọn một giá trị ngẫu nhiên để có thể khám phá

và thu thập các mẫu cho bảng hàng đợi của chúng tôi để ước tính hàng đợi của chúng tôi chính xác hơn.

Và hãy nhớ rằng, chúng cần phải chính xác ở mức độ nào đó để chúng ta có thể tự tin lựa chọn hành động tốt nhất.

Đây là cách chúng tôi sẽ làm điều này trong mã.

Thay vì luôn thực hiện hành động được chính sách chỉ định, chúng tôi sẽ tạo một số ngẫu nhiên trong khoảng từ 0 đến 1.

Nếu số ngẫu nhiên này nhỏ hơn Epsilon thì chúng ta sẽ chọn một hành động ngẫu nhiên.

Ngược lại, chúng ta sẽ thực hiện hành động được chỉ định bởi chính sách tham lam, chính sách tham lam đối với hàng đợi có trạng thái s.