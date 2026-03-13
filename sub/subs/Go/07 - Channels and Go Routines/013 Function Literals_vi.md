# 013 Hàm số vi

---

Trong phần trước, chúng tôi đã thêm thông báo về chế độ ngủ vào quy trình chính của mình, nhưng sau đó rất nhanh

nhận ra rằng điều đó sẽ khiến tất cả các thông báo đến qua kênh của chúng tôi bị chặn.

Vì vậy, chúng tôi sẽ chỉ nhận được một tin nhắn tốt nhất là 5 giây một lần hoặc lâu hơn.

Vì vậy, chúng tôi cần tìm một nơi thông minh hơn để đặt lệnh ngủ ít này.

Bây giờ, giải pháp rất rõ ràng ở đây, bạn có thể đang nghĩ, đã xong, hãy thực hiện lệnh sleep

này.

Vì vậy, tôi sẽ cắt nó ngay từ đó và thay vào đó chúng tôi sẽ đưa nó vào các chức năng của chúng tôi.

Vì vậy, hiện tại chúng tôi đang nói rằng khi chương trình của chúng tôi khởi động lần đầu tiên, nó sẽ khởi động

tất cả các liên kết kiểm tra ban đầu, thực hiện các quy trình, sau đó chúng tôi sẽ đợi 5 giây và sau đó bắt đầu bắt đầu quá

quá trình tìm kiếm.

Sau đó, mỗi khi chúng tôi nhận được một sự kiện hoặc một tin nhắn qua kênh của mình thì chúng tôi sẽ bắt đầu một

một quy trình khác.

Quá trình này sẽ tạm dừng 5 giây và sau đó thực hiện tải.

Vì vậy, về cơ bản chúng tôi đang xem xét một cái gì đó như thế nào, chúng tôi hãy làm một chút dọn dẹp từ phần

cuối cùng ở đây.

Chúng ta thường nói rằng, đã được rồi, mọi thứ luôn có thể chạy, nhưng sau đó là tất cả các quy trình

conf này sẽ phải được chờ đợi trong 5 giây trước khi thực hiện tải.

Vì vậy, tôi sẽ lưu ý rằng có thể đó cũng không phải là cách tiếp cận tốt nhất trên thế giới.

Và lý do lựa chọn điều đó là khi họ nhìn vào chức năng kiểm tra liên kết này

Ngay tại đây, tôi không biết bạn thế nào, nhưng trong đầu tôi nhận thấy rằng mục tiêu của chức năng kiểm tra là để kiểm tra một liên kết

kết nối ngay bây giờ. .

Như vậy, đừng cho tôi tạm dừng.

Nếu tôi gọi kiểm tra liên kết, tôi hy vọng nó sẽ đi ngay lập tức và cố gắng lấy liên kết này.

Vì vậy, tôi nghĩ rằng mặc dù điều này chắc chắn sẽ hiệu quả, mặc dù điều này sẽ giữ cho thói quen chính thống

Chúng tôi không bị hạn chế chế độ, tôi nghĩ rằng nó cũng không thực sự là cách sử dụng chức năng kiểm tra hợp lý.

Vì vậy, hãy xác định rõ ràng giữa chế độ chính và chức năng kiểm tra này, chúng tôi phải đặt lệnh thời gian chờ ngủ ở đây

ở đâu đó.

Vì vậy, đây là những gì chúng tôi sẽ làm lại trong vòng lặp.

Chúng tôi sẽ xóa các kiểm tra liên kết chức năng ở đây và thay vào đó chúng tôi sẽ đặt một hàm chữ,

a function signature.

Bây giờ, nếu bạn đến từ bất kỳ ngôn ngữ nào khác, bạn có thể biết ý nghĩa đen của

function is what.

Bạn có thể chỉ định một tên khác cho nó.

Vì vậy, nếu bạn đến từ thế giới JavaScript, một hàm đen và tương thích 100% với một

hàm ẩn danh hoặc an php ruby python c-sharp php không phải php.

PHP là một chức năng ẩn danh, nhưng có tất cả những chức năng khác.

Bạn có thể biết đây là một hàm lambda hoặc một biểu thức lambda.

Vì vậy, trong thực tế, một hàm nghĩa đen là một hàm không có tên mà chúng ta sử dụng để bọc một số đoạn mã nhỏ để chúng ta có thể thực thi

thi nó vào một thời điểm nào đó trong tương lai.

Vì vậy, tôi sẽ đề nghị rằng khi chúng ta bắt đầu thói quen đi này ngay tại đây, thay vì

chỉ nói, this, đi, thói quen, đi và ngay lập tức khởi động chức năng kiểm tra này, tôi nghĩ chúng ta nên đặt một

chức năng đen ở đây.

Và bên trong hàm đen đó, chúng ta có thể tạm dừng mã hóa của mình để chúng có thể thực hiện lệnh ngủ trong 5

giây và sau đó gọi hàm kiểm tra liên kết.

Vì vậy, hãy xem điều này thực sự sẽ như thế nào.

Chúng ta sẽ nói funk.

Chúng tôi sẽ đặt dấu ngoặc đơn cho danh sách đối số.

Chúng ta sẽ đặt dấu ngoặc xuống tương tự như chúng ta làm việc với một hàm bình thường.

Và bên trong hàm ngay tại đây, chúng ta sẽ đặt đoạn mã mà chúng ta muốn

thực thi.

Vì vậy, trước tiên chúng ta sẽ bắt đầu bằng cách nói thời gian ngủ năm lần, lần thứ hai, và sau đó chúng ta cũng sẽ

nói kiểm tra liên kết với L và C.

Và bây giờ là một điều cuối cùng chúng ta phải bổ sung ở đây.

Chúng ta phải thêm vào một tập hợp các dấu ngoặc đơn sau nghĩa đen của hàm.

Vì vậy, chỉ để rõ ràng, điều này ngay ở đây là một nghĩa đen của hàm.

Điều này xác định nghĩa đen của hàm.

Nhưng chúng ta phải đặt thêm dấu ngoặc đơn này để gọi nó hoặc thực sự gọi nó.

Bây giờ, điều đó có vẻ như hơi ngạc nhiên ngay tại đó.

Nhưng hãy nhớ rằng, chức năng cười khúc khích mà chúng ta vừa có trước đó là một cái gì đó giống như Go Check Link L

và C.

Và vì vậy, khi chúng tôi muốn bắt đầu một quy trình mới, chúng tôi đặt một hàm gọi lệnh hoặc một lệnh gọi hàm

ngay sau từ khóa go.

Vì vậy, trong trường hợp này, chúng tôi đang nói, đã được rồi, đây là hàm và gọi nó như vậy.

Được chứ.

Vì vậy, tại thời điểm này, hãy lưu mã của chúng tôi ở đây và bây giờ.

Khi tôi làm như vậy, bạn có thể tìm thấy một chút chữ nguệch ngoạc màu xanh lục ở đây trên màn hình.

Vì vậy, các chữ nguệch ngoạc màu xanh lá cây.

Và một lần nữa, bạn có thể chỉ tìm thấy điều này nếu bạn đang sử dụng VTS mã hóa.

Vì vậy, nếu bạn đang sử dụng một trình soạn thảo khác, bạn có thể tìm thấy hoặc không tìm thấy điều này.

Nếu tôi di chuột qua nó, bạn sẽ thấy một thông báo cảnh báo ở đây và nó cho biết biến phạm vi có thể

nắm bắt bởi đen hoặc hàm func.

Ủa!

Điều đó thực sự thú vị.

Vì vậy, điều này thực sự sẽ bắt đầu một cuộc thảo luận rất thú vị khác về thói quen đi lại

nói chung.

Vì vậy, chúng tôi tạm dừng nhanh chóng.

Chúng tôi sẽ quay lại phần tiếp theo và chúng tôi sẽ tìm hiểu chính xác cảnh thông báo

báo nhỏ ngay tại đây có nghĩa là gì.

Vì vậy, hãy nhanh chóng nghỉ ngơi và tôi sẽ gặp lại bạn chỉ sau một phút.