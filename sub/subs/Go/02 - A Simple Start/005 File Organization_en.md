# 005 Tổ chức tập tin vi

---

Giảng viên: Được rồi, chỉ còn hai câu hỏi nhanh nữa thôi

và chúng ta sẽ giải quyết cả hai vấn đề này trong phần này.

Vì vậy điều đầu tiên tôi muốn nói đến là điều thú vị đó

bên trong tệp main.go của chúng tôi.

Vì vậy, cụ thể là func main ngay tại đây.

Vâng, như bạn có thể tưởng tượng

func là viết tắt của hàm.

Các hàm bên trong hàm Go giống như các hàm

trong các ngôn ngữ lập trình khác.

Vì vậy, nếu bạn đã quen với các hàm trong Ruby, Python,

JavaScript, rất giống nhau về chức năng.

Chúng ta khai báo một hàm bằng cách đặt từ khóa func,

sau đó là tên của hàm và sau đó là danh sách đối số.

Nếu tôi đặt cái này ở dạng sơ đồ

nó có thể trông giống như thế này,

hãy xem liệu tôi có thể tìm thấy nó ở đây không.

Bắt đầu nào.

Vì vậy trước hết chúng tôi tuyên bố

rằng chúng ta sẽ tạo ra một hàm mới

với từ khóa func.

Sau đó chúng ta đặt tên của hàm,

một bộ dấu ngoặc đơn

mà chúng tôi sẽ chỉ định danh sách các đối số

mà chúng ta muốn chuyển đến hàm này.

Sau đó chúng tôi đặt dấu ngoặc nhọn của mình,

và bên trong các dấu ngoặc nhọn đó là nội dung hàm của chúng ta.

Bây giờ đây là lần đầu tiên chúng ta nếm thử một số cú pháp xung quanh Go.

Và hãy tin tôi, chúng ta sẽ có rất nhiều thời gian

và thực hành rất nhiều với một số cú pháp cơ bản

cho những thứ như chức năng và những thứ tương tự.

Vì thế tôi nghĩ hiện tại,

có lẽ thế là đủ để bạn bình tĩnh và nói,

"Ừ, gần như chúng ta vừa khai báo một hàm."

Bây giờ điều cuối cùng tôi muốn nói tới,

hoặc câu hỏi lớn cuối cùng mà chúng ta có,

là cách tổ chức tệp main.go đó.

Vì vậy, bây giờ chúng ta đã hiểu rõ hơn về gói là gì,

báo cáo nhập khẩu là gì,

và chức năng đó ở phía dưới,

làm thế nào để chúng ta tổ chức tất cả những khía cạnh khác nhau này

cùng nhau bên trong một tập tin?

Vâng, trong thực tế, nó luôn luôn kết thúc

là cùng một mô hình.

Hãy để tôi tìm sơ đồ của tôi ở đây thật nhanh.

Bắt đầu nào.

Vì vậy, nó sẽ luôn có cùng một khuôn mẫu

bên trong mỗi tập tin mà chúng tôi từng tạo.

Ở trên cùng

chúng tôi sẽ luôn khai báo gói hàng của mình.

Vì vậy hãy nhớ rằng chúng ta nói, ồ, tập tin này là một phần của gói,

bla, bla, bla.

Trong trường hợp này gói main.

Sau đó, ngay bên dưới đó,

chúng tôi sẽ liệt kê tất cả các gói khác

mà chúng tôi có thể cần phải nhập vào tệp này.

Vì vậy, câu lệnh nhập cho FMT và sau đó có thể cho IO

hoặc HĐH hoặc bất kỳ gói nào khác mà chúng tôi muốn có quyền truy cập.

Hoặc từ danh sách các gói thư viện tiêu chuẩn,

hãy nhớ rằng chúng ta vừa xem xét hai giây trước.

Hoặc chúng ta cũng có thể chỉ định các câu lệnh nhập

đối với các gói tùy chỉnh, như các gói có thể tái sử dụng

mà bạn và tôi đã tự mình viết ra.

Sau các câu lệnh đóng gói và nhập khẩu,

sau đó chúng ta đi vào phần nội dung của tập tin,

đó là nơi chúng tôi thêm vào một loạt logic

điều đó thực sự có tác dụng gì đó.

Vì vậy, nó sẽ là tập hợp các chức năng khác nhau,

khai báo biến

và tất cả những thứ tốt đẹp khác nữa.

Nói chung, chúng ta sẽ quen dần với điều này

mẫu mã rất giống nhau

trong mọi tập tin cuối cùng mà chúng tôi tập hợp lại với nhau.

Được rồi, tôi nghĩ điều đó sẽ kết thúc

cho năm câu hỏi lớn về tệp main.go của chúng tôi.

Vậy là chúng ta đã nói về mô hình,

chúng ta đã nói về các gói hàng, hàng nhập khẩu,

chúng ta đã đề cập một chút đến các chức năng,

và chúng ta có ý tưởng hay hơn

về những gì gói FMT này đang làm cụ thể.

Vì vậy tôi nghĩ rằng điều đó gần như đã kết thúc

để có cái nhìn tổng quan rất cơ bản về chương trình rất cơ bản này.

Hy vọng bây giờ bạn đồng ý với tôi

mặc dù đó là một chương trình Hello World nhàm chán

chúng tôi vẫn kiếm được một khoản khá lớn từ nó.

Tuy nhiên, vâng, điều này rất đơn giản,

chương trình đơn giản.

Vậy hãy tiếp tục phần tiếp theo

nơi chúng ta sẽ bắt đầu nói về

một dự án phức tạp hơn rất nhiều

mà chúng ta sẽ bắt đầu làm việc.

Vì vậy, hãy nghỉ ngơi nhanh chóng và sau đó chúng ta sẽ đi sâu vào dự án tiếp theo

trong phần tiếp theo.