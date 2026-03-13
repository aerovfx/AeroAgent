# 03 - Kỹ thuật nhanh chóng với FLAN-T5

---

- [Giảng viên] Hãy nói về

cách sử dụng mô hình đa năng này

để tóm tắt văn bản, dịch thuật

và trả lời câu hỏi

sử dụng thư viện máy biến áp Ôm Mặt và TensorFlow.

Video này được thiết kế

để giúp bạn tận dụng tối đa tiềm năng của một

trong những công cụ mạnh mẽ nhất trong xử lý ngôn ngữ tự nhiên.

Ôm Mặt là một nền tảng lưu trữ một bộ sưu tập lớn

của các mô hình được đào tạo trước, bao gồm FLAN-T5,

có thể thích ứng với một mảng rộng

các nhiệm vụ dựa trên văn bản.

FLAN-T5 là phiên bản nâng cao

của mẫu T5 nguyên bản.

Đó là lý do tại sao họ gọi nó là FLAN

vì nó ngon,

cố gắng hiểu

và tạo văn bản dựa trên lời nhắc theo ngữ cảnh tăng trưởng.

Đầu tiên, chúng ta cần thiết lập môi trường của mình.

Điều này bao gồm việc lắp đặt máy biến áp

và thư viện TensorFlow, cung cấp cơ sở hạ tầng

và các mô hình cần thiết cho nhiệm vụ của chúng tôi.

Sau khi cài đặt, việc chúng ta sẽ làm là tải FLAN-T5 bằng cách sử dụng

thư viện Transformers đó, được chứ?

Để làm điều đó, chúng ta sẽ sử dụng AutoTokenizer,

sẽ xử lý văn bản

sang định dạng mà mô hình mà chúng tôi sử dụng có thể hoạt động được.

Chúng tôi sẽ chuyển đổi các câu thành một chuỗi mã thông báo

hoặc biểu diễn số.

Mặt khác,

TFAutoModelForSeq2SeqLM là mô hình

điều đó sẽ giải thích các mã thông báo này

và tạo văn bản dựa trên chúng.

Chúng ta sẽ nói nhiều hơn về TFAutoModels trong các bản demo,

vì vậy đừng lo lắng

nếu lớp học đó nghe như thế này,

"Tôi không biết nó đến từ đâu."

Vì vậy, hãy bắt đầu với việc tóm tắt văn bản.

Chúng tôi sẽ cung cấp cho FLAN-T5 một đoạn văn bản

và yêu cầu một bản tóm tắt ngắn gọn.

Ở đây, điều chúng ta cần làm trước tiên là đặt lời nhắc,

đó là lời nhắc tóm tắt nói về cà rốt.

Sau đó chúng ta sẽ vượt qua nó

thông qua mã thông báo.

return_tensors="tf" rất quan trọng,

sao cho mã thông báo sẽ xuất ra các thang đo TensorFlow

bởi vì thư viện máy biến áp Ôm Mặt có thể hoạt động

với TensorFlow và PyTorch.

Vì vậy, nếu chúng ta không cẩn thận,

chúng ta có thể có được tensor PyTorch,

điều đó sẽ phá vỡ mọi thứ.

Ngoài ra, độ dài tối đa sẽ giới hạn số lượng mã thông báo trong một

được hỗ trợ bởi FLAN-T5.

Trong trường hợp này là 512.

Bạn có thể hỏi tôi, làm sao bạn biết điều đó?

À, bởi vì trong Ôm Mặt,

chúng ta sẽ thấy trong bản demo sẽ có một thẻ mô hình

nơi nó sẽ giải thích cách gọi mô hình.

Sau đó chúng ta sẽ sử dụng model.generate,

đó là thứ được sử dụng để tạo ra đầu ra.

Các tham số chúng ta sẽ vượt qua,

đó là số lượng dầm,

Early_stopping và độ dài tối đa,

sẽ kiểm soát độ dài và chất lượng của phản hồi.

Tôi rất khuyến khích bạn sau này chơi xung quanh

và thay đổi các tham số và xem đầu ra thay đổi như thế nào.

Và cuối cùng, chúng tôi sử dụng tokenizer

để giải mã các con số thành văn bản.

Tiếp theo, chúng ta sẽ sử dụng FLAN-T5

để dịch văn bản từ tiếng Anh sang tiếng Pháp.

Trong trường hợp này,

lời nhắc dịch sẽ là dịch ngôn ngữ

sang ngôn ngữ, trong trường hợp này là tiếng Anh sang tiếng Pháp.

Và chúng ta đang nói phô mai rất ngon.

Đúng là như vậy.

Vì vậy, một lần nữa, chúng ta chuyển qua mã thông báo, model.generate,

và sau đó chúng tôi in tokenizer.decode.

Tôi khuyến khích bạn chạy cái này trên máy của bạn ngay bây giờ

và tự mình xem nó hoạt động như thế nào.

Tất nhiên, chúng tôi sẽ làm điều đó trong bản demo,

nhưng tốt nhất bạn nên dừng video ngay bây giờ và bắt đầu cảm nhận.

Cuối cùng, hãy khám phá cách trả lời câu hỏi.

Chúng tôi sẽ cung cấp bối cảnh và câu hỏi,

rồi hỏi FLAN-T5

cho câu trả lời.

Ở đây câu hỏi ngữ cảnh sẽ là

một câu nêu bối cảnh,

“Vạn Lý Trường Thành của Trung Quốc dài hơn 13.000 dặm.”

Và sau đó đến điểm đánh dấu nhỏ này

mà tôi đã nói với bạn, trong trường hợp này,

"câu hỏi: Vạn Lý Trường Thành của Trung Quốc dài bao nhiêu?"

Một lần nữa, tokenizer, một lần nữa, model.generate,

và một lần nữa, với mã.

Khi trả lời câu hỏi, số

của các chùm tia sẽ điều khiển một thuật toán gọi là tìm kiếm chùm tia,

được sử dụng để khám phá nhiều đường dẫn dự đoán.

Và điều đó nâng cao tính chính xác của phản hồi.

dừng_sớm, điều này rất quan trọng

trong việc trả lời câu hỏi, ngừng tạo ra

khi một câu trả lời thỏa đáng được hình thành.

Một lần nữa tôi khuyến khích các bạn dừng video ngay bây giờ

và thử mã này cho chính mình.

Chúng tôi đã thấy cách áp dụng FLAN-T5

tới ba nhiệm vụ khác nhau,

thể hiện tính linh hoạt và sức mạnh của mô hình.

Bằng cách hiểu cách tạo ra những lời nhắc hiệu quả

và cấu hình các tham số mô hình,

bạn có thể nâng cao khả năng của các ứng dụng của mình,

làm cho chúng thông minh hơn và phản ứng nhanh hơn.