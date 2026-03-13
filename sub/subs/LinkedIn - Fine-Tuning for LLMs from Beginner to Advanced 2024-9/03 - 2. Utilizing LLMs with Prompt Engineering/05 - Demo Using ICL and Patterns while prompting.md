# 05 - Demo Sử dụng ICL và Mẫu trong khi nhắc

---

- [Người hướng dẫn] Trong bản demo này,

chúng tôi sẽ cải thiện lời nhắc mà chúng tôi đã thực hiện với Flan-T5

với việc học theo ngữ cảnh và mô hình vài lần bắn.

Tôi đã tham gia Colab, sổ ghi chép đã được tải lên,

and now again I will click connect to connect to our GPU.

Hoàn hảo, tôi đã kết nối với GPU.

Hãy nhớ rằng, điều đầu tiên chúng ta cần phải cài đặt

máy biến áp và dòng tensor.

Và nó đây rồi.

Và bây giờ chúng ta cần tải xuống tokenizer và mô hình.

Gợi ý, điều tương tự như trước đây.

Hoàn hảo.

Bây giờ mô hình của chúng tôi đã được tải xuống,

chúng tôi sẽ cải thiện tính năng nhắc nhở của mình.

Vì vậy, hãy bắt đầu với việc tóm tắt.

Kỹ thuật mà chúng ta sắp thấy là học vài lần.

Điều đó có nghĩa là chúng tôi sẽ cung cấp

một vài ví dụ hiển thị nhiệm vụ

và bản tóm tắt hoặc kết quả thực tế mà chúng ta mong muốn.

Sau khi đưa ra một vài ví dụ,

LLM sẽ hiểu rõ hơn những gì chúng tôi muốn làm,

loại, trong trường hợp này là tóm tắt mà chúng tôi muốn,

chẳng hạn như chúng ta muốn nó trong bao lâu, chẳng hạn

và nó cũng sẽ hiểu định dạng của đầu ra,

trong trường hợp chúng tôi có một định dạng cụ thể.

Vì vậy, một vài ví dụ ngắn gọn của chúng tôi,

và bạn có thể thêm bao nhiêu tùy thích,

Tôi vừa thêm hai cái cho đơn giản,

sẽ là "Con cáo nâu nhanh nhẹn nhảy qua con chó lười.

Con chó không thích thú với những trò hề của con cáo”.

Lưu ý một lần nữa, tôi đặt tóm tắt ở đầu.

Và lưu ý rằng tôi đã thêm phần tóm tắt,

"Con cáo nhảy qua con chó không vui."

Sau đó tôi thêm một ví dụ khác,

đó là về mưa ở Tây Ban Nha, cùng một dạng.

Sau đó tôi có lời nhắc thực tế,

cái đó cũng giống như cái trước,

câu chuyện về cà rốt, nhớ không?

Tất nhiên, chúng tôi đã tóm tắt.

Chúng tôi có nhiệm vụ.

Nhưng lưu ý rằng nó không có câu trả lời thực sự.

Vì vậy, chúng ta sẽ kết hợp tất cả những lời nhắc này lại với nhau.

Một vài ví dụ về cảnh quay và lời nhắc thực tế

được phân tách bằng hai dòng mới.

Bằng cách này, người mẫu sẽ hiểu một cách hoàn hảo

mô hình vài lần bắn.

Sau đó, chúng tôi chuyển qua mô hình mã thông báo.generate

và sau đó chúng tôi giải mã giống như cách chúng tôi đã làm trong bản demo trước đó.

Hãy chạy cái này.

Hoàn hảo.

Và bây giờ hãy để ý rằng cùng một mô hình,

thay vì chỉ nói ăn cà rốt,

nó cho chúng ta biết "Cà rốt là nguồn cung cấp vitamin A dồi dào,

điều này rất quan trọng để duy trì thị lực khỏe mạnh."

Không chỉ đúng mà còn là một bản tóm tắt rất hay.

Đây chính là sức mạnh của mô hình vài cú đánh.

Chúng ta hãy xem điều tương tự trong bản dịch.

Vì vậy, bạn có thể thấy rằng thực tế kỹ thuật này

là bất khả tri đối với nhiệm vụ.

Bạn có thể làm điều đó trên bất cứ điều gì bạn muốn:

phân tích tình cảm, trả lời câu hỏi.

Bạn muốn làm điều đó với chuỗi hành động suy nghĩ?

Đừng lo lắng, bạn có thể làm được.

Vì vậy bây giờ tôi sẽ đưa ra hai ví dụ,

một lần nữa, dịch tiếng Anh sang tiếng Tây Ban Nha,

và sau đó là lời nhắc dịch thuật của chúng tôi,

trong trường hợp này vẫn là "Phô mai rất ngon"

nhưng chúng ta có thể làm nó khó hơn nữa.

Không có gì.

Chúng tôi làm kỹ thuật tương tự.

Chúng tôi chạy nó

và lưu ý rằng chúng tôi nhận được bản dịch ngược,

"El queso rất ngon"

đó là bản dịch chính xác.

Một lần nữa, nếu chúng ta muốn,

chúng ta có thể làm cho nó khó khăn hơn, lời nhắc dịch thuật

và nó vẫn hoạt động vì có ít ví dụ về ảnh.

Cuối cùng, hãy thực hiện một số câu hỏi và đáp.

Trong trường hợp Q và A...

Vì vậy chúng tôi nói vài lần

và trong việc học theo ngữ cảnh, chúng gần như giống nhau,

nên chúng tôi gọi nó là học theo ngữ cảnh

khi chúng tôi đang cung cấp như một số loại

sơ đồ trả lời câu hỏi.

Đó là một thuật ngữ lịch sử hơn

sự khác biệt về mặt kỹ thuật.

Ý tưởng là như nhau.

Chúng tôi cung cấp một bối cảnh,

như "Vạn Lý Trường Thành của Trung Quốc dài hơn 13.000 dặm",

một câu hỏi và câu trả lời.

Sau đó, một bối cảnh khác, một câu hỏi khác, một câu trả lời khác.

Cuối cùng, chúng tôi sẽ cung cấp một bối cảnh mới

như "Đỉnh Everest là ngọn núi cao nhất thế giới"

và chúng tôi hỏi ngọn núi cao nhất thế giới là gì?

Chúng tôi kết hợp, mã hóa, tạo, giải mã,

và thứ chúng tôi nhận được là đỉnh Everest.

Vì vậy chúng ta có thể thấy rằng mô hình vài lần bắn này

cung cấp ví dụ là một ý tưởng cực kỳ hay

để cải thiện lời nhắc của bạn đối với LLM

không được thiết kế đặc biệt cho

bất kỳ loại đầu vào nào, chẳng hạn như GPT4,

nhưng nhỏ và có thể được sử dụng cho các nhiệm vụ cụ thể

cho các ứng dụng, bot trò chuyện,

hoặc thậm chí để tăng năng suất.