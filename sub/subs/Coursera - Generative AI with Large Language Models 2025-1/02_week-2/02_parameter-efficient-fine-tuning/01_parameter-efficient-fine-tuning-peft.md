# 01 tham số-hiệu quả-tinh chỉnh-peft

---

Như bạn đã thấy ở phần đầu tiên

tuần của khóa học,

đào tạo LLM là

tính toán chuyên sâu.

Tinh chỉnh đầy đủ yêu cầu bộ nhớ

không chỉ để lưu trữ mô hình,

nhưng nhiều thứ khác

các thông số được

được yêu cầu trong quá trình

quá trình đào tạo.

Ngay cả khi máy tính của bạn có thể

giữ trọng lượng mô hình,

hiện đang có trên

thứ tự hàng trăm

gigabyte cho

những mô hình lớn nhất,

bạn cũng phải như vậy

có thể phân bổ

bộ nhớ cho các trạng thái tối ưu hóa,

độ dốc, kích hoạt chuyển tiếp,

và trí nhớ tạm thời xuyên suốt

quá trình đào tạo.

Các thành phần bổ sung này

có thể lớn hơn gấp nhiều lần

mô hình và có thể nhanh chóng trở thành

quá lớn để xử lý

về phần cứng của người tiêu dùng.

Ngược lại với đầy đủ

tinh chỉnh ở đâu

mỗi trọng lượng mô hình được cập nhật

trong quá trình học có giám sát,

tham số hiệu quả

các phương pháp tinh chỉnh

chỉ cập nhật một chút

tập hợp con của các tham số.

Một số kỹ thuật đường dẫn bị đóng băng

hầu hết mô hình

trọng lượng và sự tập trung

on fine tuning a subset of

các tham số mô hình hiện có,

ví dụ, cụ thể

lớp hoặc thành phần.

Các kỹ thuật khác không chạm vào

mô hình ban đầu

trọng lượng chút nào,

và thay vào đó thêm một

số lượng nhỏ

các tham số hoặc lớp mới và

chỉ tinh chỉnh

các thành phần mới.

Với PEFT, hầu hết nếu không phải tất cả

của trọng lượng LLM

được giữ đông lạnh.

Kết quả là, số lượng

thông số được đào tạo là nhiều

nhỏ hơn số lượng

các tham số trong LLM gốc.

Trong một số trường hợp, chỉ 15-20%

của trọng lượng LLM ban đầu.

Điều này làm cho

yêu cầu bộ nhớ

để đào tạo nhiều

dễ quản lý hơn.

Trên thực tế, PEFT thường có thể

được thực hiện trên một GPU duy nhất.

Và bởi vì LLM ban đầu là

chỉ sửa đổi một chút

hoặc không thay đổi,

PEFT ít bị ảnh hưởng hơn

sự lãng quên thảm khốc

các vấn đề về tinh chỉnh đầy đủ.

Kết quả tinh chỉnh đầy đủ

trong phiên bản mới của

mô hình cho mọi

nhiệm vụ bạn đào tạo.

Mỗi cái này đều giống nhau

kích thước như mô hình ban đầu,

vì vậy nó có thể tạo ra một

vấn đề lưu trữ đắt tiền

nếu bạn đang tinh chỉnh

cho nhiều nhiệm vụ.

Hãy xem cách bạn có thể sử dụng PEFT

để cải thiện tình hình.

Với tham số

tinh chỉnh hiệu quả,

bạn chỉ đào tạo một chút

số lượng trọng lượng,

dẫn đến nhiều

tổng thể dấu chân nhỏ hơn,

nhỏ như megabyte

tùy theo nhiệm vụ.

Các thông số mới

được kết hợp với

LLM gốc

trọng số để suy luận.

Trọng lượng PEFT được huấn luyện cho

từng nhiệm vụ và có thể dễ dàng

đổi chỗ cho suy luận,

cho phép thích ứng hiệu quả

mô hình ban đầu

tới nhiều nhiệm vụ.

Có một số

phương pháp bạn có thể sử dụng cho

tinh chỉnh tham số hiệu quả,

mỗi cái đều có sự đánh đổi

hiệu quả tham số,

hiệu quả bộ nhớ,

tốc độ đào tạo,

chất lượng mẫu mã và

chi phí suy luận.

Chúng ta hãy nhìn vào

ba lớp chính

của phương pháp PEFT.

Các phương pháp chọn lọc được

những thứ chỉ tinh chỉnh

một tập hợp con của bản gốc

thông số LLM.

Có một số cách tiếp cận

mà bạn có thể mang đến

xác định thông số nào

bạn muốn cập nhật.

Bạn có tùy chọn để đào tạo

chỉ một số thành phần nhất định của

mô hình hoặc các lớp cụ thể,

hoặc thậm chí là cá nhân

các loại tham số.

Các nhà nghiên cứu đã tìm thấy rằng

hiệu suất của những điều này

phương pháp được trộn lẫn và có

sự đánh đổi đáng kể giữa

hiệu quả tham số

và tính hiệu quả.

Chúng tôi sẽ không tập trung vào

chúng trong khóa học này.

Tham số lại

phương pháp cũng có tác dụng

với bản gốc

thông số LLM,

nhưng giảm số lượng

các tham số cần huấn luyện bằng cách tạo

biến đổi thứ hạng thấp mới

của trọng số mạng ban đầu.

Một kỹ thuật thường được sử dụng

thuộc loại này là LoRA,

mà chúng ta sẽ khám phá trong

chi tiết ở video tiếp theo.

Cuối cùng, các phương pháp bổ sung

tiến hành tinh chỉnh

bằng cách giữ tất cả

trọng lượng LLM ban đầu

đông lạnh và giới thiệu

các thành phần mới có thể đào tạo được.

Ở đây có hai

những cách tiếp cận chính.

Thêm phương thức bộ điều hợp

các lớp có thể huấn luyện mới

đến kiến trúc

của mô hình,

thông thường bên trong

bộ mã hóa hoặc bộ giải mã

thành phần sau khi chú ý

hoặc các lớp chuyển tiếp nguồn cấp dữ liệu.

Phương pháp nhắc nhở mềm,

mặt khác,

giữ kiến trúc mô hình

cố định và đông lạnh,

và tập trung vào việc thao túng

đầu vào để đạt được

hiệu suất tốt hơn.

Điều này có thể được thực hiện bằng cách thêm

các thông số có thể huấn luyện được

các nhúng nhắc nhở

hoặc giữ đầu vào

cố định và đào tạo lại

các trọng số nhúng.

Trong bài học này,

bạn sẽ xem xét

một lời nhắc mềm cụ thể

kỹ thuật được gọi là điều chỉnh kịp thời.

Đầu tiên, chúng ta hãy chuyển sang

video tiếp theo và

nhìn kỹ hơn vào

phương pháp LoRA và xem nó như thế nào

giảm trí nhớ

cần thiết cho đào tạo