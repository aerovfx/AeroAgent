# 15 phần giới thiệu về aws-labs

---

Vậy là bạn đã thấy rất nhiều tài liệu

trong khóa học và cách tốt nhất để

bạn củng cố những khái niệm này trong

tâm trí của bạn là bắt tay vào thực hiện và

hãy thử một số mã cho chính mình.

Như Andrew đã đề cập,

vào đầu tuần này,

đồng nghiệp của tôi Chris Fragley đã lãnh đạo

phát triển phòng thí nghiệm cho khóa học này.

Mỗi tuần có một bài tập trong phòng thí nghiệm

cho phép bạn thử các khái niệm chính từ

các video.

Chris sẽ giúp bạn bắt đầu

bằng cách cho bạn thấy môi trường phòng thí nghiệm.

Sau đó anh ấy sẽ hướng dẫn bạn thực hiện hoạt động này

mà bạn sẽ hoàn thành trong tuần này.

Này, Chris.

>> Này, cảm ơn Mike.

Và bây giờ chúng ta hãy xem xét

môi trường phòng thí nghiệm trong phòng thí nghiệm 1.

Trước khi thực sự bước vào phòng thí nghiệm,

hãy để tôi giải thích hệ thống,

môi trường mà chúng ta sẽ trở thành

sử dụng ở đây, được gọi là Vocareum.

Và vì thế ở đây chúng ta thực sự sẽ

khởi chạy tài khoản AWS của riêng bạn

điều đó sẽ cung cấp cho bạn quyền truy cập

tới Amazon SageMaker và

do đó bạn có thể chạy những thứ này

sổ ghi chép mà không mất bất kỳ chi phí nào cho bạn.

Vì vậy một số điều cần lưu ý khi bạn nhận được

vào môi trường phòng thí nghiệm Vocareum,

bạn muốn nhấp vào Bắt đầu Lab,

đó là điều đầu tiên

Bạn sẽ thấy điều đó ở phía trên bên trái,

bạn sẽ thấy AWS bắt đầu từ

màu đỏ sang màu vàng sang màu xanh lá cây.

Vì vậy, màu xanh lá cây là tốt, màu xanh lá cây có nghĩa là chúng ta có thể

bấm vào đây và sau đó vào phòng thí nghiệm.

Vì vậy, chỉ cần một vài điều nhanh chóng ở đây.

Bạn sẽ có 2 giờ

để hoàn thành mỗi phòng thí nghiệm,

bạn không cần phải nhấp vào bất kỳ loại nào

của phòng thí nghiệm cuối khi bạn hoàn thành,

bạn chỉ cần đóng trình duyệt rồi di chuyển

sang phòng thí nghiệm hoặc video tiếp theo như bạn muốn.

Và có một số hướng dẫn ở đây, nhưng

Tôi thực sự sẽ đi bộ

thông qua điều này với bạn ngay bây giờ.

Vì vậy điều chúng tôi muốn làm là

nhấp vào AWS sẽ

thực sự khởi chạy vào bảng điều khiển AWS.

Bây giờ, nếu bạn đã đăng nhập vào AWS

bảng điều khiển, bạn sẽ cần nhấp vào đăng xuất,

và sau đó nhấp lại vào đây một lần nữa

trên cùng nút AWS màu xanh lá cây đó.

Tôi sẽ phóng to một chút ở đây,

cách nhanh nhất để thực sự đạt được

Sage Maker là gõ nó vào đây,

vào các trường tìm kiếm và

sau đó nhấp vào SageMaker.

Điều chúng tôi đang cố gắng làm là

đến studio SageMaker,

đó là một IDE dựa trên Jupyter mà chúng ta sẽ

sẽ làm tất cả sổ ghi chép của chúng ta trong ngày hôm nay.

Bấm vào Open Studio ở đằng kia,

thật nhanh, tôi đã nhấp vào Studio ở đây,

sau đó tôi nhấp vào Open Studio tại đây.

Tất cả điều này đã được cung cấp trước cho

bạn, nên bạn không phải làm gì cả.

Điều đó sẽ đưa bạn vào ngay

sổ ghi chép Jupyter, hãy để tôi phóng to.

Chế độ tối được bật theo mặc định,

bạn có thể tắt chế độ tối

vào chế độ ánh sáng nếu bạn muốn.

Bạn có thể nhấp vào Chủ đề và

sau đó chuyển sang chế độ JupyterLab Light bằng cách

mặc định đó là chế độ Tối của giao diện người dùng SageMaker

đó là một dạng màu đen mà chúng ta thấy ở đây.

Bây giờ bước đầu tiên là

để nhấp vào Mở Trình khởi chạy,

chúng tôi thực sự muốn đi tới Hệ thống

thiết bị đầu cuối vì đầu tiên

điều mà chúng tôi muốn làm là

sao chép các phòng thí nghiệm từ nhóm S3 của chúng tôi.

Vì vậy, việc lưu trữ đối tượng trên đám mây,

đây là một thùng công cộng

có chứa tất cả các sổ ghi chép và

tất cả các hình ảnh và

tất cả các tập dữ liệu cần thiết cho

phòng thí nghiệm đặc biệt này.

Vì vậy bây giờ tôi đang ở trong thiết bị đầu cuối,

Thực ra tôi đang định đi

quay lại hướng dẫn của tôi.

Vậy là chúng ta đã thực hiện xong tất cả những điều này, Bước 1, nhấp vào

Studio, Bước 2, nhấp vào Open Studio.

Có một cách khác để vào Studio,

đôi khi người học vấp phải điều này.

Nếu bạn nhìn thấy màn hình này bằng cách nào đó,

nếu bạn đang tìm tòi xung quanh,

chỉ cần biết rằng bạn có thể nhấp vào Khởi chạy và

bạn sẽ nhấp vào Studio và

nó sẽ mở Studio Notebook

theo cách tương tự.

Và rồi từ thời điểm đó,

tất cả các hướng dẫn này đều giống nhau,

nhấp vào Mở Trình khởi chạy,

nhấp vào Thiết bị đầu cuối hệ thống.

Bây giờ đây là đoạn mã tôi cần sao chép,

đảm bảo rằng bạn hoàn thành mọi việc

đến dấu gạch chéo cuối cùng ngay tại đó, được chứ?

Tôi sẽ quay lại JupyterLab và

Tôi sẽ dán cái này ngay tại đây,

được không?

Bước tiếp theo sẽ là

bấm vào thư mục và

chúng ta nên xem cuốn sổ

cái đó đã được tải xuống.

Vì tôi đã phóng to ở đây,

Tôi phải cuộn cái này qua đây,

và đây là phòng thí nghiệm đầu tiên.

Bây giờ, như tôi đã nói, tất cả việc tính toán

đã được cung cấp cho chúng tôi,

chúng ta chỉ có thể

bắt đầu chạy các phòng thí nghiệm này.

Bây giờ, nếu bạn chưa quen với Jupyter

sổ ghi chép, chỉ cần biết rằng bạn có thể làm

hoặc Shift+Enter để nhận,

từ sổ này sang sổ khác, từ ô này sang ô khác.

Hoặc nếu bạn đang cảm thấy

có lẽ bạn đang vội,

bạn có thể thực hiện Khởi động lại hạt nhân và

Chạy tất cả các ô.

Và điều đó thực sự sẽ chạy tất cả

các ô chỉ bằng một cú nhấp chuột.

Đối với những phòng thí nghiệm này, tôi khuyến khích bạn

để chạy từng bước, hãy thực hiện Shift+Enter,

Shift+Enter, Shift+Enter.

Vì vậy, tất cả chỉ là đánh dấu ở đây

nói phòng thí nghiệm này sẽ làm gì.