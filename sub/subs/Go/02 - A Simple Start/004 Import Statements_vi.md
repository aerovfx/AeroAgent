# 004 Báo cáo nhập khẩu vi

---

Bây giờ chúng ta đã hiểu rõ hơn về những gói nào trong GO, chúng ta

Sẽ chuyển sang câu hỏi lớn thứ ba, sẽ tìm thấy câu lệnh import Fmt có nghĩa là gì.

Vì vậy, hãy quay lại bên trong trình soạn thảo mã hóa của chúng tôi.

Chúng tôi đang nói về vấn đề này ngay tại đây.

Câu lệnh được sử dụng để cung cấp gói hàng của chúng tôi.

Vì vậy, cái mà chúng tôi đang viết ngay bây giờ, truy cập vào một số mã được viết, được viết trong

một gói khác.

Vì vậy, đặc tính FMT input có nghĩa là cấp cho gói quyền truy cập chính của tôi vào tất cả mã và tất cả

các chức năng được chứa trong các gói khác có tên Fmt này.

Fmt là tên của một thư viện tiêu chuẩn gói được bao gồm trong trình cài đặt ngôn ngữ theo mặc định.

Bản thân Fmt là một dạng rút gọn của định dạng từ.

Fmt thư viện được sử dụng để in nhiều thông tin khác nhau, đặc biệt tới đầu thiết bị cuối cùng, chỉ dành cho bạn

hiểu rõ hơn về việc gỡ lỗi và các thứ tương tự.

Bây giờ, để hiểu rõ hơn về các gói và cách nhiều gói hoạt động giống nhau trong một dự án thông thường, bạn có

có thể nghĩ về một cái gì đó như thế này.

Vì vậy, ở trung tâm, tôi đã có gói chính của chúng tôi.

Xung quanh nó có một loạt các gói khác là một phần của tiêu chuẩn thư viện theo mặc định.

Gói chính của chúng tôi có quyền truy cập hoàn toàn không có mã bên trong bất kỳ mã nào trong số các gói khác này để đảm bảo rằng mã hóa

chúng tôi đang làm việc hoặc gói mà chúng tôi đang làm việc có quyền truy cập vào các thư viện khác

hoặc các gói khác.

Chúng tôi phải đặc biệt sử dụng câu lệnh nhập để tạo liên kết từ gói của chúng tôi đến các gói khác.

Vì vậy, chúng tôi sẽ nhập FMT để tạo một liên kết từ gói chính của chúng tôi đến Fmt.

Chúng tôi cũng có thể nói rằng có thể nhập toán học để có quyền truy cập vào gói toán học.

Hiện tại, chúng tôi không giới hạn các gói có trong thư viện tiêu chuẩn, chúng tôi

bạn có thể dễ dàng sử dụng lệnh nhập để yêu cầu nhập hoặc nhập vào các gói đã có kỹ năng

sư tác giả khác.

Vì vậy, ví dụ: gói chính của chúng tôi có thể nhập FMT, nhưng nó cũng có thể nhập vào, có giới hạn như gói có tên là

máy tính hoặc trình tải lên do các kỹ năng khác hoạt động và xuất bản.

Và đây sẽ là những ví dụ về các gói có thể tái sử dụng.

Bây giờ, điều cuối cùng tôi muốn nói với bạn là bản thân gói Fmt một chút.

Như tôi đã nói, gói Fmt là một thành phần của chuẩn thư viện của lá cờ.

Chúng tôi có thể tìm thấy một số tài liệu tuyệt vời xung quanh tất cả các gói thư viện tiêu chuẩn bằng cách

truy cập Golang dot org sl pcgg.

Vì vậy, tôi đã mở một trình duyệt tab mới với liên kết đó.

Này, nó ở ngay đây.

Vì vậy, bạn có thể thấy tôi đang ở gowling dot org chém pcgg.

Đây là danh sách tất cả các gói khác nhau trong thư viện chuẩn.

Vì vậy, nếu chúng tôi cuộn xuống một chút, cuối cùng bạn sẽ tìm thấy Fmt ngay tại đây, vì vậy hãy cung cấp cho bạn một chút mô tả

rút ngắn nó về.

Bạn có thể nhấp vào liên kết và sau đó đọc tài liệu chính thức.

Bây giờ tôi sẽ nói với bạn ngay bây giờ rằng tôi hy vọng bạn thích trang này.

Tôi hy vọng bạn thích trang này bởi vì tôi có thể cho bạn biết ngay bây giờ chúng ta

sẽ xem xét tài liệu tiêu chuẩn rất nhiều, rất nhiều bởi vì rất nhiều học tập chỉ là tìm hiểu về các gói tiêu chuẩn

this và cách chúng hoạt động.

Vì vậy, đây là lần đầu tiên chúng tôi nếm thử một số tài liệu chính và chúng tôi sẽ quay lại

với những tài liệu chính thức này rất nhiều lần trong suốt khóa học này để tìm hiểu về cách hoạt động

của nhiều thư viện rất chuẩn này và cách chúng tôi có thể sử dụng chúng để phát triển các tác vụ rất phổ biến

trình lập ngôn ngữ go.

Vì vậy, tôi nghĩ rằng điều đó có thể là đủ trên các báo cáo nhập khẩu ngay bây giờ.

Một lần nữa, chúng tôi sử dụng các lệnh nhập để có quyền truy cập vào một gói khác trong gói mà chúng tôi đang tạo ra.

Vì vậy, chúng tôi nghỉ ngơi nhanh chóng.

Continue in the next part.

Bạn có thể chuyển chủ đề cuối cùng của chúng tôi, đó là điều thú vị.

Vì vậy, tôi sẽ gặp bạn chỉ sau một phút.