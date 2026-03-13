# 02 từ xử lý nhiều nghĩa

---

Một trong những thách thức chính

của cách biểu diễn từ

là cách xử lý lời nói

có nhiều ý nghĩa.

Ví dụ,

đây là hai câu trong đó

lực lượng từ có ý nghĩa khác nhau.

Cách biểu diễn từ không theo ngữ cảnh

sử dụng một từ đại diện duy nhất cho

một từ.

Vậy từ lực trong cả hai câu

có cùng một cách biểu diễn từ ở đây.

Từ không có ngữ cảnh như vậy

kỹ thuật biểu diễn bao gồm

Word2Vec và Găng tay.

Những từ gần đây hơn được đưa ra

dựa trên sự đại diện

vào ngữ cảnh xung quanh một từ.

Vậy từ lực lượng sẽ có nghĩa khác

biểu đạt theo cả hai nghĩa.

Và thậm chí nhiều cách thể hiện khác nhau hơn

nếu bất kỳ từ nào khác của câu

thay đổi,

như mạnh thành yếu chẳng hạn.

Từ được ngữ cảnh hóa như vậy

đại diện bao gồm ELMo và BERT.

Hãy xem BERT học những điều này như thế nào

biểu diễn từ theo ngữ cảnh.

Các từ trong một đoạn văn bản

được đưa vào mô hình BERT.

Sau đó, một trong những thẻ trong đoạn văn

được che bằng mã thông báo MASK đặc biệt.

Mô hình được đào tạo để

dự đoán mặt nạ là gì.

Một lớp bổ sung được thêm vào nơi

đầu ra là xác suất

từ còn thiếu là mọi

từ duy nhất trong từ vựng.

Ở đây chúng ta có thể thấy rằng sự thiếu sót thực sự

tranh luận từ có xác suất

đầu ra của mô hình 0,7.

Trong quá trình học tập để

dự đoán chính xác từ bị che giấu,

người mẫu học chữ

đại diện ở đây có màu xanh lam.

Đã có phần mở rộng cho BERT

mô hình y học như BioBERT,

sử dụng các đoạn văn từ các bài báo y khoa

để tìm hiểu những cách biểu diễn từ này.

Ưu điểm của việc này là những từ

do đó BioBERT có thể học được,

là những từ được sử dụng trong bối cảnh y học.

Bây giờ chúng ta biết BERT đại diện như thế nào

từ có cách biểu thị bằng từ.

Hãy quay lại cách chúng ta có thể sử dụng BERT cho

nhiệm vụ trả lời câu hỏi