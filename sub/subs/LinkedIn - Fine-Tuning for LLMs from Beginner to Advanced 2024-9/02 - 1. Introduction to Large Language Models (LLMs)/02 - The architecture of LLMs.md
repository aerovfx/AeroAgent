# 02 - Kiến trúc của LLM

---

- [Người hướng dẫn] Bây giờ chúng ta hãy giải nén cấu trúc

và hoạt động bên trong của các mô hình ngôn ngữ lớn, hay LLM,

tập trung vào kiến trúc máy biến áp mang tính cách mạng.

Hãy tưởng tượng sự hiểu biết về thiết kế phức tạp

của một nhà bếp hiện đại có hiệu quả cao.

Đó là những gì chúng tôi đang làm với LLM ngày nay.

Transformers được các nhà nghiên cứu tại Google giới thiệu vào năm 2017

là xương sống của hầu hết các LLM hiện đại.

Họ đã thay đổi hoàn toàn cách máy móc xử lý ngôn ngữ.

Về cốt lõi, máy biến áp bao gồm

của các lớp mã hóa và giải mã.

Bộ mã hóa đọc và xử lý văn bản đầu vào

trong khi bộ giải mã tạo ra đầu ra

dựa trên thông tin đó.

Hãy coi bộ mã hóa như nhân viên nhà bếp

người chuẩn bị tất cả nguyên liệu cho bạn,

và những người giải mã như những đầu bếp

người đã kết hợp những thành phần đó lại với nhau

để tạo ra một món ăn.

Nó cực kỳ quan trọng

để không tập trung vào từng ô và nó có ý nghĩa gì.

Chúng ta sẽ đạt được điều đó.

Bây giờ hãy có được bức tranh toàn cảnh về bộ mã hóa và bộ giải mã.

Một trong những cải tiến quan trọng của máy biến áp

là cơ chế tự chú ý.

Điều này cho phép mô hình đánh giá được tầm quan trọng

của những từ khác nhau so với những từ khác trong câu.

Ví dụ, trong câu,

"Đầu bếp đã đào tạo tôi nấu ăn rất ngon"

người mẫu sẽ nhận ra rằng đầu bếp và các đầu bếp

được liên kết rất quan trọng mặc dù khoảng cách giữa chúng.

Sự hiểu biết này cải thiện khả năng của mô hình

để xử lý các sắc thái trong ngôn ngữ.

Không giống như các mô hình cũ hơn như RNN hoặc LSTM

xử lý dữ liệu một cách tuần tự,

máy biến áp xử lý tất cả các phần của dữ liệu cùng một lúc.

Quá trình xử lý song song này giống như

đến nhiều trạm bếp làm việc cùng một lúc

tăng tốc đáng kể các nhiệm vụ.

Bây giờ hãy kiểm tra sự hiểu biết của bạn.

Cơ chế tự chú ý như thế nào

nâng cao khả năng của máy biến áp

để hiểu ngữ cảnh trong câu?

Hãy suy nghĩ về nó trong 30 giây.

(nhạc sôi động)

LLM sử dụng các kiến trúc máy biến áp này

để xuất sắc trong các công việc như dịch thuật,

tạo nội dung và hơn thế nữa

bằng sự hiểu biết một cách hiệu quả

và tạo ra văn bản giống con người,

Khả năng xử lý nhanh chóng lượng dữ liệu khổng lồ

và nắm bắt các mẫu phức tạp

làm cho chúng trở nên vô giá trên các lĩnh vực khác nhau.

Để lặn sâu hơn một chút,

mỗi lớp của máy biến áp có thể được coi như một bộ não nhỏ,

mỗi người tự đưa ra quyết định về phần nào

của văn bản là quan trọng.

Các lớp này xếp chồng lên nhau tạo thành một mạng lưới mạnh mẽ

điều chỉnh ngôn ngữ và thế hệ.