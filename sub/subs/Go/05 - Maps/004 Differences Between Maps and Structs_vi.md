# 004 Sự khác biệt giữa Bản đồ và Cấu trúc vi

---

Bây giờ chúng tôi đã có một ý tưởng khá tốt về một số cú pháp cơ bản xung quanh bản đồ, nhưng câu hỏi

Hiện tại vẫn còn nóng ở đầu bạn, Cái này khác với cấu trúc như thế nào?

Giống như cấu trúc thực tế giống nhau.

Chúng tôi xác định một số thuộc tính tên và sau đó chỉ định cho nó một số giá trị.

Vậy cấu trúc và bản đồ khác nhau như thế nào?

Tôi tập hợp một sơ đồ nhỏ để so sánh và đối chiếu một số điểm khác biệt giữa

hai dữ liệu cấu hình này.

Vì vậy, chúng ta hãy xem xét.

Bây giờ, có rất nhiều điểm khác biệt ở đây, nhưng chúng ta sẽ đi qua từng điểm một.

Vì vậy, trước tiên chúng ta sẽ bắt đầu với một số thuộc tính rất rõ ràng, và sau đó chúng

ta sẽ nói về một số loại khác biệt thú vị hơn giữa bản đồ và cấu trúc.

Vì vậy, trước hết, sự khác biệt rõ ràng nhất ở đây giữa bản đồ và cấu trúc với bản đồ,

Tất cả các khóa phải cùng loại và tất cả các giá trị phải cùng loại.

Một cấu trúc khác được xác định rõ ràng bởi vì trong một cấu trúc, tất cả các giá trị có thể thuộc về các kiểu hoàn toàn khác nhau.

Bây giờ, hãy lưu ý ở đây rằng chúng ta đang nói các giá trị có thể thuộc nhiều loại khác nhau bởi vì trong

struct hoặc with struct, xin lỗi, các phím không được nhập mạnh.

Chúng tôi tương tác với các khóa đó bằng cách xác định trước khóa tên hoặc thuộc tính tên trước đó

limit.

Và sau đó chúng tôi truy cập chúng bằng cú pháp dấu chấm quen thuộc.

Vì vậy, một số điểm đặc biệt cần lưu là tất cả các khóa và giá trị trên bản đồ phải

cùng loại.

Nhưng với cấu trúc, chúng ta có thể hợp nhất và kết hợp các loại giá trị khác nhau nếu chúng ta muốn.

Điều đặc biệt thứ hai là với bản đồ, tất cả các khóa khác nhau đều được lập chỉ mục.

Vì vậy, bằng cách thiết lập chỉ mục, tôi muốn nói rằng với một bản đồ, chúng tôi có thể lặp lại tất cả các cặp khóa giá trị khác nhau

trong bản đồ.

Nhưng điều này không đúng với một cấu trúc.

Vì vậy, với struct, chúng tôi không thể lặp lại tất cả các cặp giá trị khác nhau cho tất cả các thuộc tính khác

cùng nhau trong một.

Bây giờ một trong những điều khác biệt và điều này quay trở lại cuộc thảo luận của chúng ta về con trỏ và

bắt đầu là bản đồ là một tham chiếu kiểu trong khi cấu trúc là một giá trị kiểu.

Vì vậy, hãy nhớ những gì chúng tôi đã nói về các loại tham chiếu và loại giá trị khi chúng tôi thảo luận về con trỏ?

Về cơ bản, điều này có nghĩa là khi chúng ta chuyển một bản đồ cho một hàm, chúng ta đang chuyển một tham chiếu

đến cơ sở dữ liệu cấu hình.

Vì vậy, nếu chúng tôi chuyển một bản đồ cho một chức năng tương tự như chúng tôi đã làm ngay tại đây với bản đồ trong đó, bạn sẽ thấy rằng

chúng tôi không nói gì về màu sắc.

Bạn không tìm thấy bất kỳ ký hiệu nào và ở đây.

Bạn không tìm thấy bất kỳ ngôi sao nào, không có gì giống như vậy bên trong mã này.

Nhưng nếu chúng tôi thực hiện thay đổi đối với bản đồ trong hoặc nếu chúng tôi thực hiện thay đổi đối với bản đồ của mình

Bên trong bản đồ, xin lỗi, các màu của cơ sở dữ liệu cấu trúc ở đây sẽ được tìm thấy bản cập nhật or.

Vì vậy, khi chúng tôi chuyển đổi chức năng của bản đồ này, chúng tôi không sao chép bản đồ, chúng tôi đang sao chép một tham số

reference to the maps.

Bây giờ điều đó hoàn toàn khác để tương tác của chúng tôi với cấu trúc, trong đó nếu chúng tôi chuyển một cấu trúc

cho một hàm, chúng tôi đã tạo một bản sao của toàn bộ cấu trúc.

Và vì vậy, nếu chúng ta thay đổi cấu trúc, nó sẽ không sửa đổi cấu trúc cấm đầu mà chúng ta đã tạo

bên ngoài hàm.

Vì vậy, có một điều mà bạn có thể tò mò là, tôi nhận ra một số điều khác biệt, tôi hiểu chúng,

Nhưng tôi sử dụng một cấu trúc dữ liệu này thay vì cấu trúc kia ở đâu?

Nói chung, và đây là một số hướng dẫn ở cấp độ rất cao vì rất khó để cung cấp

cho bạn những quy tắc rất chắc chắn và nói, ồ, sử dụng bản đồ 100% thời gian ở đây hoặc sử dụng cấu trúc 100% thời gian

ở đây.

Chỉ có một số hướng dẫn rất chung chung là bạn sẽ muốn sử dụng bản đồ bất cứ khi nào bạn có thể thực hiện một bộ

tập hợp các thuộc tính có liên kết chặt chẽ với nhau.

Và vì vậy ví dụ mã hóa mà chúng tôi vừa tập hợp lại thực sự là một ví dụ tuyệt vời về điều đó.

Vì vậy, ngay tại đây, chúng tôi tập hợp một bộ sưu tập các cặp giá trị đại diện cho ánh xạ giữa

màu tên và biểu tượng hex mã hóa của nó.

Và như vậy, đây là một số giá trị có liên quan chặt chẽ với nhau và tất cả đều có một số ý nghĩa rất quan trọng

với nhau.

Điều này có liên quan rất chặt chẽ đến một trong những điểm khác biệt giữa bản đồ và cấu hình

trúc, và đối với bản đồ, chúng tôi không biết danh sách tất cả các khóa khác nhau hoặc tất cả các tên

các trường khác nhau tại thời điểm biên dịch.

Vì vậy, với một bản đồ, chúng tôi có thể thoải mái tạo bản đồ ngay tại đây.

Và sau đó chúng tôi có thể bổ sung và xóa các thuộc tính như đã nói, tôi không biết, màu vàng hoặc bạn có những gì theo thời gian tùy ý

chúng tôi và sau đó chúng tôi có thể xóa nó ngay sau đó.

Và đó là một ví dụ mà chúng tôi thấy được trong 2 giây.

Nhưng với một cấu trúc, chúng ta phải xác định rõ ràng tất cả các thuộc tính tên khác nhau và tất cả

các loại của chúng tại thời điểm biên dịch.

Giống như chúng tôi phải liệt kê rõ ràng tất cả các tài sản tên này.

Và vì vậy nếu bạn đang nghĩ rằng bạn đang tạo ra một số loại mối quan hệ giữa một số khóa và một số

giá trị và bạn không xác định được bộ sưu tập giá trị sẽ như thế nào hoặc bộ sưu tập khóa đó

như thế nào khi biên dịch thời gian.

Giống như khi bạn đang viết mã của mình thì rất có thể bạn đã có một trường hợp sử

rất hữu ích cho bản đồ, nhưng nếu bạn có một số khóa đã được đóng, hãy hạn chế, nếu bạn biết rằng bạn luôn chỉ

hoạt động với các phím màu đỏ, xanh lá cây và trắng, thì có thể bạn đã tìm thấy trường hợp hợp mà bạn có thể muốn xem xét

bằng cách sử dụng một cấu trúc.

Bây giờ, theo thời gian, khi chúng ta bắt đầu viết một số chương trình phức tạp hơn, chúng ta sẽ có thêm một

Trải nghiệm nhỏ với bản đồ và cấu trúc.

Và vì vậy, chúng tôi sẽ có thể chỉ ra cách sử dụng cấu trúc tuyệt vời trong một số trường hợp hợp, có thể là

cách sử dụng bản đồ tuyệt vời.

Bây giờ, tôi sẽ nói rằng trong phần lớn các loại mã hóa cấp độ chuyên nghiệp mà tôi đã viết thường xuyên sử dụng

nhiều cấu trúc hơn là bản đồ.

Nhưng một lần nữa, nó thực sự phụ thuộc vào loại ứng dụng mà bạn đang xây dựng.

Vì vậy, tôi nghĩ rằng chúng tôi đã hiểu rõ hơn bản đồ là gì trong một số điểm khác biệt giữa bản đồ

và cấu hình.

Vì vậy, tôi nghĩ rằng chúng tôi sẽ tạm nghỉ ngay bây giờ và chúng tôi có thể sẽ có một hoặc hai câu hỏi tranh luận

nhanh chóng chỉ để tìm lỗ hổng về một số khía cạnh của bản đồ và một số khía cạnh của chúng.

Vì vậy, chúng tôi nghỉ ngơi nhanh chóng.

Chúng tôi sẽ đến với bài kiểm tra đó và sau đó chúng tôi sẽ tiếp tục với các chủ đề tiếp theo của chúng tôi trong phần tiếp theo.