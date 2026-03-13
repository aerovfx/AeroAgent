# 01 - Giải pháp Tinh chỉnh mô hình phân tích cảm tính

---

- [Giảng viên] Vậy thử thách đó thế nào?

Như bạn đã biết,

nếu bạn không thể đi đến cuối cùng thì cũng không sao cả.

Ở đây, chúng tôi sẽ trình bày một giải pháp,

nhưng điều quan trọng nhất trong tất cả

là điều này rất, rất quan trọng,

bởi vì chúng tôi sẽ bắt đầu xây dựng LLM

rằng chúng ta sẽ cắm

cuối cùng thành một giải pháp chatbot đầy đủ.

Và tôi không biết bạn, nhưng đối với tôi, điều đó cực kỳ thú vị.

Vì vậy, hãy bắt đầu. Hãy để tôi kết nối với GPU.

Nó đây rồi. Tôi đã kết nối với GPU.

Như mọi khi, chúng ta cần thực hiện cài đặt pip.

Và thế là mọi thứ đã được cài đặt.

Vì vậy, bây giờ, chúng tôi sẽ thực hiện nhập khẩu bình thường

và lưu ý rằng trong trường hợp này,

khi chúng tôi đang thực hiện phân tích tình cảm,

đó là sự phân loại trình tự,

chế độ tự động sử dụng là ForSequenceClassification.

Điều đó rất quan trọng.

Trước đây, chúng tôi sử dụng seq2seq,

bởi vì chúng tôi đang sử dụng mô hình seq2seq.

Vì vậy, chúng tôi sẽ thực hiện việc nhập khẩu và chúng tôi bắt đầu.

Đối với phân tích tình cảm của chúng tôi,

chúng tôi sẽ sử dụng bộ dữ liệu SST2

từ phòng thí nghiệm Stanford NLP, là nguồn mở.

Và chúng ta bắt đầu.

Vì vậy, như bạn đã biết, điều chúng ta cần làm bây giờ

là mã hóa tập dữ liệu

và tạo bộ dữ liệu TensorFlow.

Tokenizer sẽ đến từ distilbert

và việc mở rộng token của chúng tôi sẽ dễ dàng hơn rất nhiều,

bởi vì ở đây, chúng ta chỉ có câu

và chúng tôi cần token hóa họ để kiểm tra tình cảm của họ.

Thế thôi.

Vì vậy, chúng ta sẽ làm

ví dụ["Câu"], đệm='max_length',

cắt ngắn=Đúng, max_length=128.

Điều gì đó hay ho về mã thông báo distilbert

Tôi muốn đề cập đến là chỉ trong trường hợp này,

bạn không cần đặt return_tensors='tf',

vì nó tự động phát hiện ra nó.

Tuy nhiên, nếu bạn muốn chơi an toàn và đặt nó ở đây,

như return_tensors='tf',

nó không giống như nó sẽ bị vỡ.

Nó giống nhau.

Tôi chỉ muốn đề cập đến điều đó,

bởi vì bạn có thể thấy các giải pháp trong Stack Overflow

hoặc thậm chí có thể bằng công cụ GenAI

điều đó sẽ không thể thêm nó trong trường hợp này với distilbert

và đây là lý do.

Vì vậy, hãy thực hiện mã thông báo của chúng tôi.

Nó đây rồi. Siêu đơn giản.

Và bây giờ, chúng tôi so sánh với tập dữ liệu TensorFlow.

Và điều này cũng giống như những gì chúng tôi đã và đang làm từ trước đến nay.

Chúng tôi chuyển ["Input_ids", "Attention_mask"] dưới dạng cột.

Các cuộc gọi nhãn sẽ là "nhãn".

Chúng tôi sẽ xáo trộn.

Và kích thước lô như mọi khi,

hãy nhớ rằng, chúng tôi sẽ điều chỉnh nó tùy thuộc vào RAM GP của chúng tôi.

Trong trường hợp của tôi, tôi sẽ đặt 64, đủ tốt.

Tôi thậm chí có thể đặt nó là 128 và nó sẽ ổn thôi.

Trong trường hợp của bạn, nếu bạn không có GPU chẳng hạn,

bởi vì bạn đang ở thời điểm quan trọng,

thì bạn có thể đặt nó là số tám

và điều duy nhất bạn sẽ có

là thời gian đào tạo dài hơn,

đó không phải là ngày tận thế.

Chúng ta đây rồi.

Vì vậy, nếu chúng ta có được một phần tử,

chúng tôi muốn xem hình dạng của ID đầu vào,

mặt nạ chú ý và nhãn.

Và thực sự, mọi thứ đều tốt đẹp.

64 hàng và 128 mã thông báo.

Cả trên ID đầu vào và mặt nạ chú ý.

Và chúng tôi có 64 nhãn. Mọi thứ đã sẵn sàng cho mô hình của chúng tôi.

Vì vậy, trước tiên, chúng ta sẽ tải mô hình.

Và vì đây là cách phân loại trình tự,

chúng ta cần chỉ định số lượng nhãn.

Điều đó có nghĩa là số lượng lớp học.

Đây là phân tích tình cảm.

Vì vậy, điều này sẽ là tích cực hoặc tiêu cực.

Nhưng nếu bạn muốn làm điều này

đối với một kiểu phân loại trình tự khác, bạn có thể.

Điều này rất, rất quan trọng,

vì giả sử bạn muốn tạo một chatbot

muốn phân loại tin tức, bạn đưa cho nó bài báo

và nó phải cho bạn biết bạn có loại tin tức nào.

Bạn chỉ cần đặt một lượng tin tức khác nhau mà bạn có ở đây,

như tôi biết thể thao, kinh tế, thế giới, chính trị, v.v.,

và nó sẽ chỉ hoạt động với cùng một mã.

Thật tuyệt vời phải không?

Vì vậy, mặc dù chúng tôi đang phân tích tình cảm,

chatbot này chúng tôi sẽ tạo

có thể được điều chỉnh theo bất cứ điều gì bạn muốn.

Và đó là toàn bộ ý tưởng của tôi khi giới thiệu với bạn dự án này.

Vì vậy, bây giờ, chúng tôi có mô hình của chúng tôi.

Nếu bạn còn nhớ, lớp đầu tiên của rượu chưng cất của chúng tôi

để phân loại trình tự là distilbert.

Vì vậy, chúng ta sẽ đặt nó là có thể huấn luyện được = Sai

to do a transfer learning,

và chúng ta có thể xác minh điều đó bằng một bản tóm tắt mô hình.

Đầu tiên, chúng ta có máy chưng cất,

mà chúng tôi đặt là không thể đào tạo được,

và sau đó là các lớp dày đặc,

sẽ là bộ phân loại,

mà chúng tôi sắp đào tạo.

Vì vậy, việc này sẽ diễn ra khá nhanh.

Và sau đó, như mọi khi, chúng tôi thực hiện việc biên dịch.

Hãy nhớ rằng chúng ta sẽ sử dụng Adam,

Độ chính xác phân loại thưa thớt và phân loại thưa thớt,

bởi vì đây là một vấn đề phân loại,

chúng ta có thể sử dụng độ chính xác làm thước đo.

Vì vậy, chúng tôi biên dịch.

Và bây giờ, chúng tôi phù hợp.

Và chúng ta sẽ phù hợp với ba kỷ nguyên.

Nếu bạn muốn hiệu suất tốt hơn,

bạn có thể đặt nó thậm chí nhiều hơn như 5 hoặc 10, như bạn biết.

Nó phụ thuộc vào thời gian bạn muốn chờ đợi.

Ở đó nó đang được chuyển sang GPU.

Và như bạn biết, việc này sẽ mất một chút thời gian.

Được rồi, bây giờ chúng ta đã thấy quá trình đào tạo đã kết thúc.

Phải mất bốn phút để xem điều này.

Có thể mất nhiều thời gian hơn trong trường hợp của bạn, nhưng đừng lo lắng.

Nó là bình thường.

Điều quan trọng nhất mà chúng ta có thể thấy

đó không chỉ là sự mất mát giảm theo từng thời kỳ,

nhưng ngoài ra, chúng ta có thể kiểm tra ở mức độ chính xác và phân loại thưa thớt này

và chúng ta có thể thấy làm thế nào chúng ta đạt được 84%.

Điều này có lẽ là nhiều

như chúng ta có thể nhận được nếu chúng ta chỉ đào tạo ba kỷ nguyên

và chúng tôi không thích thấp hơn,

kỹ thuật hoạt động tiên tiến hơn,

nhưng nó là quá đủ cho chúng tôi.

Vậy chúng ta sẽ làm gì?

Được rồi, nếu bạn muốn sử dụng nó,

mô hình này sau đó để tải nó vào chatbot,

sau đó bạn chỉ cần làm model.save_pretrain

và điều này sẽ lưu mô hình.

Bạn có thể thấy nó ở đây trong các tập tin.

Bây giờ, bạn có thư mục này

trong đó có tất cả cấu hình mô hình của mọi thứ.

Và sau đó, nếu bạn thích model.load, nó sẽ tải mô hình.

Vì vậy, về cơ bản đó là cách tiết kiệm

và tải các mô hình trong

(không rõ ràng)

và TensorFlow.

Rất, rất dễ dàng như bạn đã thấy.

Để đánh giá mô hình,

chúng ta sẽ chạy model.evaluate như trước

và in mất mát và độ chính xác.

Vì vậy, hãy chạy nó.

Và chúng ta có thể thấy rằng độ chính xác xác nhận là 83,3%,

gần giống như độ chính xác khi huấn luyện,

điều đó có nghĩa là chúng tôi không chỉ có một mô hình xuất sắc,

nhưng điều này cũng có nghĩa là chúng tôi chưa đủ khỏe.

Vì vậy, chúng tôi đã thành công trong nỗ lực của mình

để học chuyển tiếp trên Distilbert,

trên tập dữ liệu SST2 để thực hiện phân tích tình cảm.

Nhưng hãy nhớ, điều này có thể được áp dụng

đối với bất kỳ nhiệm vụ phân loại nào.