# 02 - Giải pháp cho vấn đề độ dốc biến mất và bùng nổ

---

- [Người hướng dẫn] Như đã thảo luận ở video trước,

các vấn đề độ dốc biến mất và bùng nổ

hạn chế khả năng của mạng lưới thần kinh tái phát

để tìm hiểu sự phụ thuộc lâu dài.

May mắn thay, một số giải pháp đã được phát triển

để giải quyết hạn chế này.

Chúng ta hãy đi qua một vài trong số họ.

Một trong những cách đơn giản nhất

để giảm thiểu vấn đề độ dốc biến mất

là bằng cách thay thế các chức năng kích hoạt truyền thống,

như sigmoid và tanh,

với các lựa chọn thay thế, chẳng hạn như ReLU

hoặc ReLU bị rò rỉ hoặc ReLU tham số.

Cả hai hàm kích hoạt sigmoid và tanh

có xu hướng bão hòa ở các giá trị đầu vào cực đoan,

tạo ra các gradient rất gần bằng 0.

ReLU và các biến thể của nó tránh được vấn đề này

bởi vì chúng không bão hòa cho các giá trị đầu vào dương.

Đạo hàm hoặc là 1 cho đầu vào dương

hoặc 0 cho đầu vào âm,

cho phép độ dốc chảy tự do hơn

trong quá trình lan truyền ngược.

Trong khi độ dốc biến mất cản trở việc học,

độ dốc bùng nổ có thể làm mất ổn định hoàn toàn việc đào tạo.

Giải pháp ở đây là cắt bớt độ dốc.

Cắt gradient là một kỹ thuật

ngăn cản độ dốc tăng lên không kiểm soát được.

Bằng cách hạn chế độ dốc trong một phạm vi cố định,

cắt gradient đảm bảo cập nhật ổn định

tới trọng lượng của mô hình,

ngăn ngừa hành vi thất thường trong quá trình đào tạo.

Cách khởi tạo trọng số trong mạng nơ-ron

có thể có tác động đáng kể đến dòng gradient.

Khởi tạo kém có thể tăng hoặc giảm độ dốc,

làm trầm trọng thêm, biến mất hoặc bùng nổ các vấn đề về độ dốc.

Hai kỹ thuật khởi tạo trọng số nâng cao phổ biến

là khởi tạo Xavier, chia tỷ lệ trọng số

dựa trên số lượng nơ-ron đầu vào và đầu ra của một lớp,

và khởi tạo He,

chỉ sử dụng số lượng nơ-ron đầu vào để mở rộng quy mô

và được thiết kế cho các chức năng kích hoạt dựa trên ReLU.

Một giải pháp mạnh mẽ khác

là việc áp dụng các kỹ thuật chuẩn hóa

chẳng hạn như chuẩn hóa hàng loạt hoặc chuẩn hóa lớp.

Những phương pháp này ổn định việc đào tạo

bằng cách đảm bảo rằng đầu vào của mỗi lớp

có sự phân bố nhất quán.

Chuẩn hóa hàng loạt chuẩn hóa đầu vào cho một lớp

qua một loạt mẫu,

duy trì giá trị trung bình và phương sai ổn định,

trong khi chuẩn hóa lớp bình thường hóa đầu vào

qua các đặc điểm của một mẫu duy nhất,

làm cho nó đặc biệt hữu ích cho RNN

nơi kích thước lô có thể nhỏ

hoặc các chuỗi có độ dài khác nhau cần được xử lý.

Đối với dữ liệu tuần tự,

kiến trúc tiên tiến,

như mạng bộ nhớ ngắn hạn dài

và các đơn vị định kỳ có kiểm soát

được thiết kế đặc biệt

để giải quyết vấn đề độ dốc biến mất.

Chúng ta sẽ thảo luận chúng chi tiết hơn

qua hai video khóa học tiếp theo.

Bằng cách giải quyết các nguyên nhân gốc rễ

của độ dốc biến mất và bùng nổ,

những kỹ thuật và kiến trúc này

đã biến đổi khả năng của mạng lưới thần kinh

để xử lý dữ liệu tuần tự phức tạp.

Cùng nhau, chúng kích hoạt RNN và các biến thể của chúng

để thực hiện hiệu quả trên một loạt các ứng dụng.