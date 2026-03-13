# 07 trình tạo văn bản trước khi chuyển đổi

---

Điều quan trọng cần lưu ý là

thuật toán tổng quát

không phải là mới.

Các thế hệ trước của

mô hình ngôn ngữ được sử dụng

một kiến trúc được gọi là tái diễn

mạng lưới thần kinh hoặc RNN.

RNN mạnh mẽ

cho thời gian của họ,

bị giới hạn bởi

lượng tính toán và

bộ nhớ cần thiết để thực hiện

giỏi trong các nhiệm vụ sáng tạo.

Hãy xem một ví dụ

của một RNN đang thực hiện

một từ tiếp theo đơn giản

nhiệm vụ tạo dự đoán.

Chỉ với một lần trước

những từ mà người mẫu nhìn thấy,

dự đoán

không thể tốt lắm

Khi bạn mở rộng quy mô RNN

triển khai để có thể

để xem thêm phần trước

các từ trong văn bản,

bạn phải đáng kể

mở rộng quy mô tài nguyên

mà mô hình sử dụng.

Về phần dự đoán,

tốt, mô hình đã thất bại ở đây.

Ngay cả khi bạn mở rộng mô hình,

nó vẫn chưa thấy đủ

đầu vào để thực hiện

một dự đoán tốt.

Để thành công

dự đoán từ tiếp theo,

người mẫu cần xem nhiều hơn

chỉ là vài từ trước đó.

Người mẫu cần có

một sự hiểu biết về

cả câu hoặc

thậm chí toàn bộ tài liệu.

Vấn đề ở đây là

ngôn ngữ rất phức tạp.

Trong nhiều ngôn ngữ, một từ

có thể có nhiều ý nghĩa.

Đây là những từ đồng âm.

Trong trường hợp này, nó chỉ

với bối cảnh của

câu mà chúng ta có thể thấy

nghĩa là loại ngân hàng nào.

Các từ trong câu

các cấu trúc có thể

mơ hồ hoặc có những gì chúng ta có thể

gọi sự mơ hồ về mặt cú pháp.

Ví dụ như câu này,

“Thầy đã dạy

học sinh với cuốn sách."

Có phải giáo viên đã dạy sử dụng

cuốn sách hoặc đã làm

sinh viên có cuốn sách,

hay là cả hai?

Làm thế nào một thuật toán có thể

có ý nghĩa

ngôn ngữ của con người nếu

đôi khi chúng ta không thể?

Vâng vào năm 2017, sau

việc xuất bản bài báo này,

Sự chú ý là tất cả những gì bạn cần,

từ Google và

Đại học Toronto,

mọi thứ đã thay đổi.

Máy biến áp

kiến trúc đã đến.

Cách tiếp cận mới lạ này đã mở khóa

sự tiến bộ trong sáng tạo

AI mà chúng ta thấy ngày nay.

Nó có thể được thu nhỏ một cách hiệu quả

để sử dụng GPU đa lõi,

nó có thể song song

xử lý dữ liệu đầu vào,

sử dụng lớn hơn nhiều

tập dữ liệu huấn luyện,

và điều quan trọng là,

nó có thể học

chú ý

đến ý nghĩa của

những từ nó đang xử lý.

Và sự chú ý là tất cả bạn

cần. Nó ở trong tiêu đề.