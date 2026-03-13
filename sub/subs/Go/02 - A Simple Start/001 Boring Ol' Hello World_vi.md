# 001 Boring Ol' Hello World vi

---

Bây giờ chúng tôi đã hoàn tất công việc thiết lập môi trường của mình, chúng tôi sẽ bắt đầu làm việc với

chương trình rất nhỏ, rất nhỏ đầu tiên của chúng ta.

Bây giờ, chương trình đầu tiên mà chúng tôi sẽ làm về cơ bản sẽ là một loại ứng dụng hello

world, nơi chúng tôi sẽ hủy đăng nhập hoặc đăng xuất một số dữ liệu nhỏ.

Và vì vậy tôi biết rằng đây là một chương trình cực kỳ nhàm chán khi bắt đầu, nhưng hãy tin tôi, chúng tôi sẽ

đi sâu về độ chính xác của hoạt động của Go ở hậu trường và chúng tôi sẽ tìm hiểu rất nhiều

về cách chúng tôi biên dịch, xây dựng các dự án, tất cả những thứ này chỉ bằng cách nghiên cứu chương trình nhỏ này.

Vì vậy, mặc dù nó sẽ là một chương trình rất nhỏ, nhưng chúng tôi sẽ học hỏi được nhiều điều từ nó.

Vì vậy, chúng tôi sẽ chuyển mã soạn thảo của chúng tôi sang phần này.

Chúng ta sẽ chỉ viết một chương trình rất đơn giản và sau đó chúng ta sẽ tạm nghỉ, quay lại trong video

tiếp theo và sau đó chúng ta sẽ bắt đầu tìm hiểu sâu về cách hoạt động của nó.

Vì vậy, tôi sẽ bắt đầu bằng cách tạo một dự án thư mục mới để chứa chương trình nhỏ này.

Tôi sẽ truy cập tệp, tôi sẽ nhấp vào Mở và sau đó tôi sẽ tạo một thư mục mới để chứa dự án

dự án mới này.

Vì vậy, tôi sẽ nhấp vào thư mục mới ở đây và tôi sẽ gọi thư mục mới là Hello World.

Bây giờ khi tôi tạo thư mục mới đó, tôi sẽ thấy nó được chọn và tôi sẽ nhấp vào mở

ở đây ở dưới cùng để mở thư mục mới được tạo.

Bây giờ khi tôi nhấp vào Mở, tôi sẽ thấy điều chỉnh hướng dẫn bên trái mở trên tab Explorer.

Tab Explorer là tab cho phép tôi xem tất cả các tệp và thư mục khác nhau trong dự án thư mục

công việc của tôi đang làm.

Nếu bạn không tìm thấy tab Explorer ở đây, bạn có thể vào xem và sau đó nhấp vào Explorer ngay tại

đây.

Bây giờ, bên trong thư mục Helloworld này, chúng tôi sẽ tạo một tệp mới bằng cách nhấp vào nút

tệp mới ngay tại đây.

Vì vậy, chúng tôi sẽ tạo một tệp mới và gọi nó là dấu chấm chính.

Đi.

Được chứ.

Vì vậy, bên trong đây, đây là nơi chúng tôi sẽ đưa ra một chương trình chào thế giới quay trở lại.

Chúng tôi sẽ chỉ tăng tốc độ thông qua mã hóa ngay bây giờ.

Chúng tôi sẽ đưa ra tất cả màn hình.

Chúng ta sẽ nghỉ ngơi một chút và sau đó quay lại và nói rất chi tiết về từng dòng mà chúng

ta đang viết ra.

Vì vậy, chúng tôi sử dụng mã hóa ở đây và sau đó chúng tôi sẽ nói về những gì đang xảy ra trong giây lát.

Vì vậy, chúng tôi sẽ bắt đầu bằng cách nói Gói chính.

Bên dưới nó sẽ nhập FMT và đảm bảo rằng Fmt nằm trong dấu ngoặc kép, không phải dấu nháy đơn.

Chúng tôi muốn dấu ngoặc kép ở đây.

Và bên dưới chúng ta sẽ nói func main.

Chúng ta sẽ đặt một tập hợp các dấu ngoặc đơn, chúng ta sẽ đặt một tập hợp các dấu ngoặc và bên trong đó Fmt dot println.

Đảm bảo rằng bản in đó có chữ P viết hoa và chúng tôi sẽ chuyển cho nó một chữ Hi khác như thế.

Vì vậy, hiện tại một điều tôi muốn chỉ ra cho bạn, rất quan trọng.

Đảm bảo rằng bạn có cả dấu ngoặc kép trên lệnh nhập ngay tại đây và trên chuỗi

chúng tôi đang chuyển tới các dòng hàm in.

Được rồi.

Vì vậy, hiện tại chúng tôi đã tổng hợp lại các chương trình rất đơn giản, rất cơ bản này, chúng tôi sẽ giải quyết

lao nhanh.

Chúng tôi sẽ quay trở lại.

Chúng tôi sẽ tìm cách chạy chương trình này.

Và chúng tôi sẽ nói về từng dòng mã bên trong đây một cách chi tiết, tuyệt vời.

Vì vậy, một cơn bình tĩnh nhanh chóng.

Chúng tôi sẽ quay lại và thực sự đi sâu vào mã này, hãy xem sau một phút.