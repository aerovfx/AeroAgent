# 14 -CodeChallenge Tinh chỉnh codeGen cho phép tính

---

Thử thách viết mã này bám sát video trước, vì vậy hãy đảm bảo bạn đã xem

video trước đó trước khi xem qua video này.

Trên thực tế, thực sự chỉ có một bài tập trong thử thách viết mã này.

Bắt đầu từ tệp sổ ghi chép từ video trước.

Bạn có thể tạo một bản sao mới của nó hoặc theo nghĩa đen chỉ cần thêm nhiều mã hơn vào tệp đó.

Mục tiêu ở đây là tinh chỉnh mô hình bằng cách sử dụng mã Python tính toán và sau đó đánh giá

đầu ra được tạo ra sau đào tạo.

Bây giờ tôi cho bạn toàn quyền tự do về cách bạn muốn tinh chỉnh mô hình, học những gì

tốc độ và số lượng giai đoạn đào tạo sẽ sử dụng cũng như bất kỳ thông số nào khác mà bạn chọn.

Bạn cũng có thể chọn cách bạn muốn định lượng hiệu suất.

Bạn có thể làm điều gì đó rất đơn giản, dễ hiểu và chất lượng.

Bạn có thể thử viết mã thứ gì đó phức tạp và định lượng hơn.

Điều đó hoàn toàn phụ thuộc vào bạn.

Tôi muốn bạn có nhiều tự do trong bài tập này.

Bây giờ tôi sẽ chuyển sang mã và chỉ cho bạn giải pháp của tôi.

Nhưng miễn là bạn không mắc phải bất kỳ lỗi nào thì bất cứ điều gì bạn nghĩ ra đều tuyệt vời.

Bạn không nhất thiết phải làm những gì tôi đã làm.

nhập một vài mô-đun hoặc thư viện, chúng tôi có thể nhập mã thông báo

và bản thân mô hình. Được rồi và tất nhiên là đẩy nó vào GPU ở đây. bây giờ

điều tôi muốn đề cập ngắn gọn mà tôi chưa thảo luận ở phần trước

video là nếu bạn đang tương tác với LLM với hy vọng nó ghi

mã dành cho bạn, chẳng hạn như trò chuyện GPT hoặc Claude hoặc Gemini, bạn sẽ viết một lời nhắc có thể trông giống như vậy

như thế này.

Nhập lại và xác định biểu thức chính quy khớp với địa chỉ email.

Tất nhiên bây giờ bạn có thể sử dụng điều này làm lời nhắc cho mô hình này, model.generate, và bạn sẽ

nhận được một cái gì đó

Nó có thể không chính xác, nhưng nó có thể sẽ phù hợp với bối cảnh nào đó.

Được rồi, trong trường hợp này, điều này thực sự không có gì liên quan.

Hãy thử lại lần nữa.

Vấn đề là để nhận được văn bản từ một lời nhắc như thế này, một lời nhắc bằng ngôn ngữ tự nhiên như

điều này, thành mã, đòi hỏi một loạt chương trình đào tạo chuyên dụng khác.

Và đó được gọi là điều chỉnh lệnh.

Và đó là trọng tâm của phần tiếp theo của khóa học.

Vậy là chúng ta chưa huấn luyện mô hình này, và mô hình này cũng chưa huấn luyện để biến đổi

ngôn ngữ tự nhiên như thế này thành mã không tự động xảy ra trong ngôn ngữ

các mô hình.

Người mẫu cần được đào tạo để hiểu bạn đang cố gắng làm gì, bạn muốn tương tác như thế nào

với mô hình.

Vì vậy, một lần nữa, đó là chủ đề cho phần tiếp theo về điều chỉnh lệnh.

Và tôi chỉ muốn đề cập đến điều đó.

Vì vậy, bạn sẽ nhận được một số nội dung có liên quan ở đây.

Nhưng dù sao, hãy để tôi nhận xét điều đó

và chạy lại dòng này ở đây.

Được rồi, và một lần nữa, như chúng ta đã thấy ở video trước,

vâng, tôi không mong đợi nhận được thứ gì đó

siêu lừa đảo hợp lý ở đây.

Được rồi, mã này được sao chép theo đúng nghĩa đen

từ ô mã trước đó,

nên tôi sẽ không đi, hoặc tập tin trước đó,

vì vậy tôi sẽ không thảo luận về điều đó.

Đây là nơi tôi bắt đầu đào tạo.

Vì vậy tôi sử dụng AtomWOptimizer.

Tất nhiên, chúng tôi luôn sử dụng trình tối ưu hóa này trong LLM.

Tôi có một tỷ lệ học tập khá nhỏ.

Tôi đã không thực sự chơi đùa với tốc độ học tập nhiều.

Tôi đã thử một vài giá trị khác nhau, nhưng không nhiều lắm.

Và sau đó tôi sẽ huấn luyện 200 mẫu

với kích thước lô là 64 và độ dài chuỗi là 128.

Bây giờ, vì, bạn biết đấy,

chỉ là cách mã đó được viết,

128 token thực sự là rất nhiều cho token

so với ngôn ngữ của con người, giống như một bài viết trên Wikipedia

trong đó 128 mã thông báo sẽ không có nhiều văn bản như vậy.

Được rồi, đây là vòng lặp đào tạo.

Hãy xem, tất cả điều này sẽ quen thuộc với bạn.

Không có gì thực sự đặc biệt ở đây.

Những gì tôi tìm thấy khi tôi đang chơi đùa với cái này

và khám phá các thông số khác nhau

là nó thực sự không cần phải đào tạo nhiều

để mô hình này tạo ra mã

trông rất giống cuốn sách tính toán mã Python.

Vì vậy thời gian huấn luyện ở đây dài hơn GPT-2 nhỏ một chút.

Không có gì ngạc nhiên khi mô hình này lớn hơn gấp đôi

như mẫu nhỏ GPT-2.

Được rồi, để đánh giá, tôi chỉ muốn giữ nó

rất đơn giản và dễ hiểu.

Đây là một đánh giá hoàn toàn chất lượng.

Vì vậy, tôi chỉ chạy lại cái này.

Và sau đó chúng tôi thấy rằng chúng tôi nhận được,

vì vậy trong một số hàm chúng ta đang tạo một biểu thức tượng trưng

sử dụng thư viện simpy.

Vậy 10 lần sin của X bình phương.

Và ở đây chúng ta chỉ sao chép nó sang hàm hai.

Hãy xem, không phải tất cả những điều này,

thực sự điều này có vẻ khá hợp lý.

Và vâng, được rồi, nó không hợp lý lắm,

nhưng điều này chắc chắn trông rất giống mã Python tính toán.

Mã Python có vẻ khác

hơn là những tin nhắn tiếng Anh viết cho bạn,

nhưng đối với mô hình ngôn ngữ thì thực sự không có sự khác biệt.

Nó chỉ là một chuỗi các token

mà mô hình đã học được.

Mặt khác, điều đặc biệt ở mã

là có xu hướng có tương đối ít token

được sử dụng liên quan đến ngôn ngữ của con người

như tiếng Anh hoặc tiếng Tây Ban Nha.

Và các mã thông báo cũng có xu hướng có ít ký tự hơn,

điều đó có nghĩa là nó thực sự khó hơn một chút

để người mẫu học cách viết mã.

Các công ty như OpenAI, Salesforce, Google, Anthropic,

họ đã dành rất nhiều thời gian và sức lực

tối ưu hóa mô hình của họ

để có thể hiểu và tạo mã.

Đó không phải là điều gì đó, vì vậy hãy trở thành một lập trình viên giỏi

hoặc có thể viết mã,

không phải là thứ gì đó xuất hiện một cách tự nhiên

ngoài mô hình ngôn ngữ.

Đó là thứ mà họ đã được đào tạo đặc biệt

để giỏi.

Và điều đó cũng thật tuyệt vì khi họ làm

mô hình của họ có sẵn, bạn có thể hưởng lợi bằng cách tải xuống,

tinh chỉnh và sau đó sử dụng các mô hình nền tảng đó.

Bạn