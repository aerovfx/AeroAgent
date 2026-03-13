# 001 Câu chuyện nhàm chán Hello World vi

---

Người hướng dẫn: Bây giờ chúng ta đã làm xong rồi

với môi trường của chúng tôi được thiết lập,

chúng ta sẽ bắt đầu làm việc đầu tiên

chương trình rất nhỏ, rất ít.

Bây giờ, chương trình đầu tiên chúng ta sẽ thực hiện

về cơ bản sẽ là một ứng dụng kiểu Hello World

nơi chúng ta sắp đăng xuất bằng bảng điều khiển

hoặc đăng xuất một số dữ liệu nhỏ.

Và tôi biết đây là một chương trình rất nhàm chán

để bắt đầu, nhưng hãy tin tôi,

chúng ta sẽ tìm hiểu thật sâu

về chính xác cách Go đang hoạt động đằng sau hậu trường,

và chúng ta sẽ học được nhiều điều

về cách chúng tôi biên soạn, xây dựng dự án,

tất cả những thứ tốt đẹp này

chỉ bằng cách nghiên cứu chương trình nhỏ bé này.

Vì vậy, mặc dù đây chỉ là một chương trình rất nhỏ,

chúng ta sẽ học được rất nhiều điều từ nó.

Vì vậy, chúng ta sẽ chuyển sang Trình soạn thảo mã của mình.

Trong phần này, chúng ta sẽ chỉ viết ra

chương trình rất đơn giản, sau đó chúng ta sẽ nghỉ giải lao,

quay lại trong video tiếp theo,

và sau đó chúng ta sẽ bắt đầu tìm hiểu sâu

về chính xác cách nó hoạt động.

Vì vậy, tôi sẽ bắt đầu bằng cách tạo một thư mục dự án mới

để thực hiện chương trình nhỏ này.

Tôi sẽ đi tới Tệp, tôi sẽ nhấp vào Mở,

và sau đó tôi sẽ tạo một thư mục mới

để thực hiện dự án mới này.

Vì vậy tôi sẽ nhấp vào Thư mục mới ở dưới đây,

và tôi sẽ gọi thư mục mới là Hello World.

Bây giờ khi tôi tạo thư mục mới đó,

Tôi sẽ thấy nó được chọn

và tôi sẽ nhấp vào Mở ở dưới cùng

để mở thư mục mới tạo đó.

Bây giờ khi tôi nhấp vào Mở,

Tôi sẽ thấy điều hướng bên trái mở ra trên tab Explorer.

Tab Explorer là thứ cho phép tôi xem

tất cả các tập tin và thư mục khác nhau

nằm trong thư mục dự án đang làm việc của tôi.

Nếu bạn không thấy tab Explorer ở đây,

bạn luôn có thể vào Xem

và sau đó nhấp vào Explorer ngay tại đây.

Bây giờ bên trong thư mục Hello World này,

chúng ta sẽ tạo một tập tin mới

bằng cách nhấp vào nút Tệp mới ngay tại đây.

Vì vậy, chúng ta sẽ tạo một tệp mới và gọi nó là main.go.

Được rồi, bên trong đây

đây là nơi chúng ta sẽ cài đặt một chương trình kiểu Hello World.

Một lần nữa, bây giờ chúng ta sẽ lướt nhanh qua mã.

Chúng ta sẽ ném tất cả lên màn hình,

chúng ta sẽ nghỉ ngơi,

và sau đó quay lại và nói chuyện rất chi tiết

về từng dòng mà chúng tôi đang viết ra.

Vậy hãy ném mã lên đây, (cười khúc khích)

và sau đó chúng ta sẽ nói về những gì đang diễn ra trong giây lát.

Vì vậy, chúng ta sẽ bắt đầu bằng cách nói package main.

Bên dưới nó chúng ta sẽ nói import fmt,

và đảm bảo rằng fmt nằm trong dấu ngoặc kép,

không phải dấu ngoặc đơn.

Chúng tôi muốn có dấu ngoặc kép ở đây.

Và bên dưới chúng ta sẽ nói func main.

Chúng ta sẽ đặt một bộ dấu ngoặc đơn,

chúng ta sẽ đặt một bộ dấu ngoặc nhọn và bên trong đó,

fmt.Println.

Đảm bảo rằng Print có chữ P viết hoa,

và chúng ta sẽ chuyển cho nó một chuỗi chữ Xin chào khác, giống như vậy.

Bây giờ, có một điều tôi muốn chỉ ra cho bạn, rất quan trọng,

đảm bảo rằng bạn có dấu ngoặc kép

cả trên báo cáo nhập khẩu ngay tại đây,

và trên chuỗi mà chúng ta đang truyền

vào chức năng dòng in, được chứ?

Được rồi, bây giờ chúng ta đã tập hợp xong

chương trình rất đơn giản, rất cơ bản này,

chúng ta sẽ nghỉ ngơi nhanh chóng, chúng ta sẽ quay lại,

chúng ta sẽ tìm ra cách chạy chương trình này,

và chúng ta sẽ nói về từng dòng

mã bên trong ở đây rất chi tiết.

Vì vậy, nghỉ ngơi nhanh chóng.

Chúng ta sẽ quay lại và thực sự đi sâu vào mã này.

Hẹn gặp bạn sau một phút nữa.