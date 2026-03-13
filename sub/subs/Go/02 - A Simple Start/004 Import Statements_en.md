# 004 Báo cáo nhập khẩu vi

---

Người hướng dẫn: Bây giờ chúng ta đã hiểu rõ hơn rồi

về những gói bên trong Go,

chúng ta sẽ chuyển sang câu hỏi lớn thứ ba,

đang tìm ra

câu lệnh import fmt đó có nghĩa là gì.

Vì vậy, hãy quay lại bên trong trình soạn thảo Mã của chúng tôi,

vâng, chúng ta đang nói về điều này ngay tại đây.

Câu lệnh nhập được sử dụng để cung cấp gói của chúng tôi,

vì vậy bài viết mà chúng tôi đang viết bây giờ,

truy cập vào một số mã được viết

bên trong một gói khác.

Vì vậy, nói cụ thể, import fmt có nghĩa là

cấp cho gói của tôi, gói chính, quyền truy cập vào tất cả mã

và tất cả các chức năng

được chứa bên trong gói khác này có tên là fmt.

Fmt là tên của gói thư viện chuẩn

cái đó được bao gồm

với ngôn ngữ lập trình Go theo mặc định.

Bản thân Fmt là một dạng rút gọn

của định dạng từ.

Thư viện fmt được sử dụng để in ra

rất nhiều thông tin khác nhau, đặc biệt là về thiết bị đầu cuối

chỉ để giúp bạn có cảm giác gỡ lỗi tốt hơn

và những thứ như thế.

Bây giờ, để hiểu rõ hơn về các gói

và cách nhiều gói hoạt động cùng nhau trong một dự án bình thường,

bạn có thể nghĩ ra điều gì đó như thế này.

Vì vậy, ở chính giữa, tôi đã có gói chính của mình.

Xung quanh nó là một loạt các gói khác

đó là một phần của thư viện tiêu chuẩn của Go.

Theo mặc định, gói chính của chúng tôi có quyền truy cập

hoàn toàn không có mã bên trong bất kỳ mã nào khác.

Để đảm bảo rằng đoạn mã mà chúng tôi đang xử lý,

hoặc gói mà chúng tôi đang thực hiện,

có quyền truy cập vào các thư viện khác

hoặc những gói khác,

chúng ta phải sử dụng cụ thể câu lệnh nhập khẩu

để tạo liên kết từ gói của chúng tôi tới những gói khác.

Vì vậy, chúng tôi sẽ nói nhập fmt để tạo liên kết

từ gói chính của chúng tôi tới fmt.

Chúng tôi cũng có thể nói, bạn biết đấy, có thể nhập toán học

để có được quyền truy cập vào gói toán học.

Bây giờ chúng tôi không chỉ giới hạn ở các gói

được bao gồm trong thư viện tiêu chuẩn,

chúng ta có thể dễ dàng sử dụng một câu lệnh nhập

để yêu cầu hoặc nhập vào,

các gói đã được tác giả bởi các kỹ sư khác.

Vì vậy, ví dụ: gói chính của chúng tôi có thể nhập fmt,

nhưng nó cũng có thể nhập khẩu chẳng hạn,

một gói có tên là máy tính hoặc trình tải lên,

được tác giả và xuất bản bởi các kỹ sư khác.

Và đây sẽ là ví dụ về các gói có thể tái sử dụng.

Bây giờ điều cuối cùng tôi muốn nói với bạn,

bản thân gói fmt là một chút.

Như tôi đã nói, gói fmt

là một phần của thư viện chuẩn của Go.

Chúng ta có thể tìm thấy một số tài liệu tuyệt vời

xung quanh tất cả các gói thư viện tiêu chuẩn

bằng cách truy cập golang.org/pkg.

Vậy là tôi đã mở rồi

một tab trình duyệt mới có liên kết đó.

Đây là ngay đây,

để bạn có thể thấy tôi đang ở golang.org/pkg.

Đây là danh sách tất cả các gói khác nhau

được bao gồm trong thư viện tiêu chuẩn.

Vì vậy, nếu chúng ta cuộn xuống một chút,

cuối cùng bạn sẽ thấy fmt ngay tại đây.

Vì vậy, để cung cấp cho bạn một mô tả ngắn gọn về nó,

bạn có thể nhấp vào liên kết,

và sau đó đọc tài liệu chính thức.

Bây giờ tôi sẽ kể cho bạn nghe ngay bây giờ

rằng tôi hy vọng bạn thích trang này. (cười khúc khích)

Tôi hy vọng bạn thích trang này,

bởi vì tôi sẽ nói với bạn ngay bây giờ,

chúng ta sẽ xem xét

rất nhiều tài liệu tiêu chuẩn,

bởi vì học rất nhiều Đi

tất cả là về việc tìm hiểu về các gói tiêu chuẩn này

và cách chúng hoạt động.

Vì vậy, đây là hương vị nhỏ đầu tiên của chúng tôi

của một số tài liệu chính thức,

và chúng ta sẽ quay lại với những tài liệu chính thức này

rất nhiều lần trong suốt khóa học này

để tìm hiểu về cách

rất nhiều thư viện tiêu chuẩn này hoạt động,

và cách chúng ta có thể sử dụng chúng để thực hiện các nhiệm vụ rất phổ biến

với ngôn ngữ lập trình Go.

Được rồi, tôi nghĩ thế là đủ

trên báo cáo nhập khẩu ngay bây giờ.

Một lần nữa, chúng tôi sử dụng câu lệnh nhập

để có quyền truy cập vào gói khác

bên trong cái mà chúng tôi đang soạn thảo.

Vậy chúng ta hãy nghỉ ngơi nhanh thôi,

tiếp tục ở phần tiếp theo,

và đi vào chủ đề cuối cùng của chúng ta,

đó là điều thú vị

Vậy tôi sẽ gặp bạn sau một phút nữa.