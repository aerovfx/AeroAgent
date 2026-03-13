# 13 -SuperGLUE và các sự kết hợp khác được dịch

---

Có lẽ trong mọi video trong phần này, tôi đã đề cập rằng mỗi phương pháp mà bạn

đã học có sai sót hoặc hạn chế, hoặc ít nhất có thể khó diễn giải một cách khách quan

bởi vì việc lựa chọn tham số, văn bản, độ dài chuỗi, v.v. có thể ảnh hưởng đến việc định lượng.

Điều đó không phải vì những người phát triển các biện pháp đó cẩu thả.

Hoàn toàn ngược lại.

Thay vào đó, đó là vì LLM rất lớn và rất phức tạp, còn ngôn ngữ của con người thì phức tạp.

và cẩu thả và không hoàn hảo.

Vì vậy, thật khó để có được một biện pháp thực sự hiệu quả.

Vậy theo bạn đâu là giải pháp cho vấn đề đó?

Tôi có thể tưởng tượng rằng bạn đoán rằng chúng tôi có thể, một cách tiếp cận mà chúng tôi có thể thực hiện là tập hợp

nhiều định lượng riêng lẻ và tổng hợp chúng lại với nhau để tạo ra một điểm trung bình.

Đó là ý tưởng của superglue và cũng có một số cách tiếp cận tổng hợp khác

cũng vậy.

Động cơ là những ưu điểm của một số phương pháp cân bằng được những nhược điểm của

các phương pháp đánh giá khác, và vì vậy chúng ta chỉ nên tính trung bình của nhiều phương pháp đó cùng nhau.

Đây là một cách tiếp cận rất phổ biến khi nghiên cứu các hệ thống phức tạp.

Ví dụ, bạn luôn thấy điều đó trong nghiên cứu tâm lý học.

Nếu bạn muốn đánh giá tính cách, bạn không chỉ có một câu hỏi mà bạn

hỏi ai đó.

Thay vào đó, bạn yêu cầu mọi người tự báo cáo về hàng chục hoặc có thể hàng trăm tuyên bố về bản thân họ.

Và sau đó giả định rằng bất kỳ tuyên bố riêng lẻ nào cũng không nhất thiết mang tính biểu thị,

vì vậy bạn lấy rất nhiều trong số chúng và tính trung bình chúng lại với nhau.

Và đó là ý tưởng về một phương pháp tiếp cận cầu thận giống như keo siêu dính.

Đây là một tiêu chuẩn có mục đích chung kết hợp nhiều nhiệm vụ khác nhau để mô hình thực hiện

làm được và điểm cuối cùng phản ánh mức trung bình của nhiều nhiệm vụ riêng lẻ.

Nó thực sự dựa trên một phiên bản cũ hơn của cùng một phương pháp được gọi là keo,

và sau đó họ cho ra đời keo siêu dính về cơ bản chỉ là một cách để làm cho các bài kiểm tra trở nên khó khăn hơn

bởi vì các mô hình ngôn ngữ đã trở nên tốt hơn nhiều.

Tôi thích cái tên superglue, nhưng chắc chắn đó không phải là cách tiếp cận dựa trên tổng hợp duy nhất.

Đây là một cái khác thường được viết tắt là Helm hoặc H-E-L-M.

Cái này cũng được sử dụng khá phổ biến và bạn có thể thấy ngay trong bản tóm tắt rằng

pin nhiệm vụ này bao gồm 57 nhiệm vụ được nhắm mục tiêu để mô hình thực hiện, từ toán học

lịch sử, pháp luật và nhiều chủ đề khác.

Bây giờ đây chỉ là ba trong số nhiều phương pháp đánh giá dựa trên mức trung bình và tôi không nhấn mạnh

ba cái này bởi vì chúng là những cái duy nhất hoặc nhất thiết phải là những cái tốt nhất.

Đây chỉ là để cung cấp cho bạn cảm giác về một số tùy chọn.

Đó thực sự là tất cả những gì tôi muốn nói trong video này.

Tôi sẽ không thảo luận về việc triển khai, mặc dù về cơ bản mọi đánh giá này đều

các phương thức có một số thư viện hoặc API Python mà bạn có thể truy cập.

Tuy nhiên, tôi muốn đưa ra hai điểm cuối cùng.

Trước hết, đó là khi bạn có dữ liệu nhiễu hoặc tín hiệu có tỷ lệ nhiễu thấp, tính trung bình

qua các phép đo khác nhau hoặc các loại phép đo khác nhau là một quy trình được thiết lập tốt

trong phân tích thống kê.

Thứ hai, bạn cũng nên lưu ý rằng tất cả các sắc thái trong từng nhiệm vụ riêng lẻ vẫn còn

phải được xem xét trong các biện pháp tổng hợp.

Vào cuối ngày, LLM rất phức tạp và ngôn ngữ cũng phức tạp đến mức nó chỉ

rất khó để gắn một số duy nhất vào khả năng LLM, giống như rất khó

để gắn một con số có ý nghĩa vào khả năng của con người.