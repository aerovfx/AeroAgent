# 07 Thực hành xây dựng cây quyết định-phân loại-mô hình-phần 2

---

Xin chào và chào mừng trở lại.

Trong video trước, chúng ta đã khám phá

siêu tham số khác nhau

có thể được sử dụng

để cải thiện hiệu suất

của mô hình cây quyết định.

Trong video này chúng ta hãy thực hiện

kiến thức để nâng cao

hiệu suất mô hình của chúng tôi.

Chúng tôi sẽ tiếp tục

với cùng một cuốn sổ

mà chúng tôi đã làm việc trên

trong video trước đó.

Nếu bạn không lưu

sổ ghi chép trước đó, đừng lo lắng.

Bạn có thể tải sổ ghi chép xuống

liên kết với video này

từ phần tài nguyên.

Vui lòng đảm bảo chạy

tất cả các ô phía trên này

điểm trước khi tiếp tục.

Chúng tôi sẽ chủ yếu

đang thử nghiệm

với việc cắt tỉa

độ sâu tối đa siêu tham số.

Nhưng hãy thoải mái thử nghiệm với

các siêu tham số khác mà bạn

đã học ở

video trước đó.

Như chúng ta đã biết, độ sâu tối đa giúp chúng ta

tỉa cây bằng cách

giảm độ sâu

cây quyết định.

Theo mặc định, không có giới hạn

độ sâu tối đa trong cây.

Thay vì thử nghiệm

đầu tiên với số ngẫu nhiên,

chúng ta hãy tìm hiểu độ sâu của

mô hình hiện tại của chúng tôi sử dụng

phương pháp tìm độ sâu.

Như bạn có thể thấy độ sâu

của mô hình là 26.

Tiếp theo, chúng ta sẽ tạo một danh sách

có giá trị bắt đầu từ

độ sâu cây mặc định và

giảm đi ba cho đến khi

đạt đến độ sâu của một.

Danh sách này sẽ giúp chúng tôi thực hiện

cắt tỉa bằng cách sử dụng khác nhau

giá trị của độ sâu tiếp theo.

Tiếp theo chúng ta sẽ luyện tập

mô hình cây quyết định

với mức tối đa khác nhau

giá trị độ sâu và sau đó

tính toán và hiển thị cả

luyện tập và kiểm tra điểm f1

lên đến ba chữ số thập phân

điểm cho từng mô hình.

Để làm như vậy, chúng ta hãy

bắt đầu bằng cách nhập

điểm f1 từ

sklearn.metrics.

Đoạn mã dưới đây tính toán

điểm f1 cho mỗi mô hình.

Hãy mã hóa nó và chạy nó.

Quan sát kết quả, nó

rõ ràng là khác nhau

tham số độ sâu tối đa

dẫn đến khác nhau

điểm số đào tạo và f1.

Điều thú vị là khi tối đa

độ sâu được đặt thành tám,

sự chênh lệch giữa

luyện tập và kiểm tra điểm f1 là

giảm thiểu trong khi vẫn giữ

quá trình kiểm tra đạt khoảng 84%.

Để cải thiện điểm số hơn nữa,

cứ thoải mái thử cái khác

siêu tham số.

Để giúp bạn tất cả dưới đây là

mã mà bạn

có thể sử dụng để điều chỉnh

lá mẫu tối thiểu bằng cách thêm

số nguyên trong phút

danh sách lá mẫu.

Ngoài ra, đừng quên chỉ định

giá trị độ sâu tối đa

mà bạn đã đạt được trong

bước trước đó để

biến đã cho dưới đây.

Xin lưu ý rằng đây là

thực hiện đơn giản

điều chỉnh siêu tham số.

Trong khóa học tiếp theo,

bạn sẽ học

về một số kỹ thuật tiên tiến

để điều chỉnh siêu tham số.

Tôi hy vọng bạn thích

quá trình tinh chỉnh

các siêu tham số của

quyết định sửa sang lại của chúng tôi.

Với điều này, chúng tôi kết luận

phân loại của chúng tôi

phát triển mô hình.

Trong video tiếp theo, chúng ta sẽ

chuyển trọng tâm của chúng tôi sang

giải pháp tổng hợp

vấn đề hồi quy.

Hẹn gặp lại bạn ở lần tiếp theo.