# 004 Sự khác biệt giữa Bản đồ và Cấu trúc vi

---

Người hướng dẫn: Bây giờ chúng ta đã có một ý tưởng khá hay

một số cú pháp cơ bản về bản đồ,

nhưng câu hỏi cháy bỏng

điều đó có lẽ vẫn còn đọng lại trong đầu bạn,

này, cái này khác với cấu trúc như thế nào?

Cấu trúc trông thực sự giống nhau.

Chúng tôi đã xác định một số tên thuộc tính

và sau đó gán cho nó một giá trị nào đó.

Vậy struct và maps khác nhau như thế nào?

Tôi tập hợp một sơ đồ nhỏ

đó sẽ là sự so sánh và đối chiếu

một số khác biệt giữa hai cấu trúc dữ liệu này.

Vì vậy chúng ta hãy xem xét.

Bây giờ, có rất nhiều sự khác biệt ở đây,

nhưng chúng ta sẽ đi qua từng cái một.

Vì vậy trước tiên chúng ta sẽ bắt đầu

với một số đặc tính rất rõ ràng,

và sau đó chúng ta sẽ nói về

một số khác biệt thú vị hơn

giữa bản đồ và cấu trúc.

Trước hết, sự khác biệt rõ ràng nhất ở đây

giữa bản đồ và cấu trúc

là với bản đồ, tất cả các khóa phải cùng loại

và tất cả các giá trị phải cùng loại.

Một cấu trúc có sự khác biệt rõ ràng, bởi vì trong một cấu trúc,

tất cả các giá trị có thể thuộc các loại hoàn toàn khác nhau.

Bây giờ, hãy chú ý ở đây rằng chúng ta đang nói về giá trị

có thể có nhiều loại khác nhau,

bởi vì trong struct, hoặc với struct, xin lỗi,

các phím được gõ không mạnh.

Chúng ta tương tác với những phím đó

bằng cách xác định trước tên khóa

hoặc tên thuộc tính trước thời hạn,

và sau đó chúng tôi truy cập chúng bằng cú pháp dấu chấm quen thuộc đó.

Vì vậy, sự khác biệt số một cần phải nhận thức rõ ràng

đó là tất cả các khóa và giá trị có bản đồ

phải cùng loại,

nhưng với cấu trúc,

chúng ta có thể trộn và kết hợp các loại giá trị khác nhau nếu muốn.

Sự khác biệt lớn thứ hai là với bản đồ,

tất cả các khóa khác nhau đều được lập chỉ mục.

Vì vậy, bằng cách lập chỉ mục, tôi muốn nói rằng với một bản đồ,

chúng ta có thể lặp lại tất cả các cặp giá trị khóa khác nhau

bên trong bản đồ,

nhưng điều này không đúng với cấu trúc.

Vì vậy, với một cấu trúc, chúng ta không thể lặp lại

trên tất cả các cặp giá trị khóa khác nhau

hoặc tất cả các thuộc tính khác nhau bên trong một.

Bây giờ, một trong những khác biệt lớn nhất,

và điều này quay lại cuộc thảo luận của chúng ta về con trỏ trong Go,

đó là bản đồ là một loại tài liệu tham khảo,

trong khi struct là một loại giá trị.

Vì vậy hãy nhớ những gì chúng ta đã nói

về các loại tham chiếu và các loại giá trị

khi chúng ta đang thảo luận về con trỏ?

Về cơ bản điều này có nghĩa

rằng khi chúng ta chuyển bản đồ tới một hàm,

chúng tôi đang chuyển đi một tài liệu tham khảo

vào cấu trúc dữ liệu cơ bản.

Vì vậy, nếu chúng ta chuyển bản đồ cho một hàm,

giống như chúng ta đã làm ở đây với printMap,

bạn sẽ thấy rằng chúng tôi không nói gì về màu sắc.

Bạn không thấy bất kỳ ký hiệu nào ở đây, bạn không thấy bất kỳ ngôi sao nào,

không có gì giống như vậy bên trong mã này.

Nhưng nếu chúng ta thực hiện thay đổi đối với printMap

hoặc nếu chúng tôi thực hiện thay đổi đối với bản đồ của mình

bên trong printMap, xin lỗi,

thì màu cấu trúc dữ liệu cơ bản ở đây

sẽ thấy bản cập nhật đó.

Vì vậy, khi chúng ta chuyển bản đồ này cho hàm,

chúng tôi không sao chép bản đồ,

chúng tôi đang sao chép một tham chiếu đến bản đồ.

Bây giờ, điều đó thật khác biệt

hơn là sự tương tác của chúng ta với các cấu trúc,

trong đó nếu chúng ta chuyển một cấu trúc cho một hàm,

chúng tôi đã tạo một bản sao của toàn bộ cấu trúc,

và vì vậy nếu chúng ta thay đổi cấu trúc,

nó không sửa đổi bản gốc

mà chúng tôi đã tạo bên ngoài hàm.

Vì vậy, một điều mà bạn có thể tò mò là,

được rồi, tôi hiểu một số khác biệt này,

Tôi hiểu họ,

nhưng tôi phải sử dụng một cấu trúc dữ liệu ở đâu

trái ngược với cái kia?

Vâng, nói chung, và đây là một số hướng dẫn cấp cao

bởi vì thật khó để đưa ra cho bạn những quy tắc thật chắc chắn

và nói, ồ, sử dụng bản đồ 100% ở đây

hoặc sử dụng cấu trúc 100% thời gian ở đây.

Chỉ là một số hướng dẫn rất chung chung

là bạn sẽ muốn sử dụng bản đồ

bất cứ khi nào bạn đại diện cho một bộ sưu tập

có những đặc tính có liên quan rất chặt chẽ.

Và ví dụ về mã mà chúng tôi vừa tổng hợp lại

thực sự là một ví dụ tuyệt vời về điều đó.

Vì vậy, ngay tại đây, chúng tôi tập hợp một bộ sưu tập

của các cặp giá trị khóa đại diện cho ánh xạ

giữa tên màu và biểu diễn mã hex của nó.

Và đây là một số giá trị có liên quan rất chặt chẽ

rằng tất cả đều có ý nghĩa rất quan trọng đối với nhau.

Điều này có liên quan rất chặt chẽ

đến một trong những khác biệt lớn khác

giữa bản đồ và cấu trúc,

và đó là với một bản đồ,

chúng ta không cần biết danh sách tất cả các khóa khác nhau

hoặc tất cả các tên trường khác nhau tại thời điểm biên dịch.

Vì vậy, với một bản đồ,

chúng tôi có thể tự do tạo bản đồ ngay tại đây,

và sau đó chúng ta có thể thêm và xóa các thuộc tính,

như nói, tôi không biết, màu vàng hay bạn có gì,

theo thời gian tùy ý chúng tôi,

và sau đó chúng ta có thể xóa nó ngay sau đó.

Và đó là ví dụ mà chúng ta vừa thấy hai giây trước.

Nhưng với một struct, chúng ta phải xác định rất rõ ràng

tất cả các tên thuộc tính khác nhau

và tất cả các loại của chúng tại thời điểm biên dịch.

Chúng ta phải liệt kê rất rõ ràng tất cả các tên tài sản này.

Và vì vậy nếu bạn đang nghĩ

rằng bạn đang tạo ra một số loại mối quan hệ

giữa một số khóa và một số giá trị,

và bạn không thực sự biết tập hợp các giá trị đó là gì

sẽ như vậy,

hoặc bộ sưu tập chìa khóa đó sẽ là gì

tại thời điểm biên dịch, giống như khi bạn đang viết mã,

tốt, vậy thì rất có thể

bạn có một trường hợp sử dụng tuyệt vời cho bản đồ.

Nhưng nếu bạn có một số chìa khóa đã đóng,

ví dụ như,

nếu bạn biết rằng bạn sẽ luôn làm việc

chỉ với các phím màu đỏ, xanh lá cây và trắng,

ồ, vậy thì có lẽ bạn có một trường hợp

nơi bạn có thể muốn xem xét việc sử dụng một cấu trúc.

Giờ đây, theo thời gian,

khi chúng tôi bắt đầu viết một số chương trình phức tạp hơn,

chúng ta sẽ có thêm một chút kinh nghiệm

với bản đồ và cấu trúc,

và vì vậy chúng ta sẽ có thể chỉ ra

trong một số trường hợp, đó là một công dụng tuyệt vời của cấu trúc,

và trong một số trường hợp có thể đó là một công dụng tuyệt vời của bản đồ.

Bây giờ tôi sẽ nói rằng phần lớn

loại mã Go cấp độ chuyên nghiệp mà tôi đã viết,

thường kết thúc bằng việc sử dụng cấu trúc nhiều hơn bản đồ,

nhưng một lần nữa, nó thực sự chỉ liên quan đến

loại ứng dụng bạn đang xây dựng.

Được rồi, tôi nghĩ chúng ta hiểu rõ hơn

bản đồ là gì

và một số khác biệt giữa bản đồ và cấu trúc,

vì vậy tôi nghĩ bây giờ chúng ta sẽ nghỉ ngơi nhanh chóng

và chúng ta có thể sẽ có một hoặc hai câu đố nhanh

chỉ để tìm hiểu sâu về một số khía cạnh của bản đồ

và một số khía cạnh quan trọng của chúng.

Vì vậy, hãy nghỉ ngơi nhanh chóng, chúng ta sẽ đi đến bài kiểm tra đó,

và sau đó chúng ta sẽ tiếp tục

với chủ đề lớn tiếp theo của chúng tôi trong phần tiếp theo.