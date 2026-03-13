# 012 Ngủ theo thói quen vi

---

Trong phần trước, chúng tôi đã nói rằng chúng tôi muốn chèn một số kiểu tạm dừng trước khi cố gắng tìm lại một

định nghĩa liên kết tối đa.

Và vì vậy, chỉ để đảm bảo rằng họ thực sự hiểu được vòng lặp cho điều này ngay tại đây, vòng lặp

vì điều này nói rằng hãy xem kênh, xem bất cứ nơi nào khi có giá trị nào xuất hiện từ kênh đó, hãy chỉ định giá trị đó cho l là viết tắt của một

link.

Khi giá trị đó xuất hiện và được chỉ định cho l, phần thân của vòng lặp sau đó sẽ được thực hiện ngay lập tức.

Vì vậy, về cơ bản, chúng tôi đang mong đợi lệnh này ngay tại đây trước khi chúng tôi đi sâu vào phần

nội dung thực tế của vòng lặp cho và các phần nội dung của vòng lặp để cài đặt ngay lập tức bắt đầu quá trình kiểm tra liên kết.

Vì vậy, mục tiêu của chúng tôi hiện đang tìm ra một số cách để chèn một điểm dừng tạm thời trong quá trình này.

Vì vậy, chúng tôi muốn đảm bảo rằng chúng tôi sẽ tạm dừng trước khi bắt đầu và cố gắng tìm lại một liên kết.

Bây giờ thực hiện tạm dừng thực hiện sẽ khá đơn giản, nhưng việc tìm kiếm chính xác

vị trí đặt mã để tạm dừng sẽ khó khăn hơn một chút.

Vì vậy, hãy xem tài liệu của chúng tôi và chúng tôi sẽ tìm ra cách chúng tôi đưa ra một số loại tạm dừng

tùy chọn mã hóa của chúng tôi.

Vì vậy, tôi sẽ lại tài liệu về liên kết Go của chúng tôi.

Vì vậy, tôi đang xem gói tài liệu mà chúng tôi đã xem xét vài lần trước đây.

Bây giờ bên trong đây, tôi sẽ cuộn xuống cuối trang.

Tôi đang tìm một gói có tên là Thời gian.

Được chứ?

Vì vậy, không phải là rất, rất cuối cùng, nhưng ít nhất là xuống gói thời gian,

gần cuối trang.

Vì vậy, chúng tôi sẽ xem xét gói thời gian bên trong đây.

Chúng tôi sẽ cuộn xuống mục chỉ mục.

Và bên trong đó, bạn sẽ tìm thấy một chức năng gọi là sleep ngay tại đây.

Vì vậy, họ nhìn vào giấc ngủ.

Vì vậy, giấc ngủ sẽ tạm thời dừng thói quen đi lại hiện tại trong ít nhất một khoảng thời gian.

DX Vì vậy, đây là một chức năng mà chúng ta có thể sử dụng ngay tại đây để đặt một số tùy chọn tạm dừng cho mã của chúng ta.

Bây giờ điều rất quan trọng cần lưu ý ở đây là thuật ngữ mà nó sử dụng.

Nó cho biết điều này sẽ ngủ hoặc tạm dừng thói quen đi hiện tại.

Và vì vậy, chúng ta sẽ phải rất sớm ở đây tìm ra một chút về cái nào chính xác cái nào đi

theo thói quen.

Chúng tôi thực sự muốn tạm dừng ngay lúc này.

Bạn sẽ thấy rằng chức năng tạm dừng đã nhận được đối số là D, được cho là có loại thời gian.

Vì vậy, hãy nhấp vào thời lượng ngay tại đây và tìm hiểu chính xác nó là gì.

Vì vậy, đây là loại thời gian.

Nếu bạn cuộn xuống cuối phần này một chút, bạn sẽ nhận thấy rằng lượng

bao này cũng bao gồm một số thứ hai không đổi.

Và vì vậy về cơ bản chúng ta có thể gọi là thời gian.

Thứ hai về cơ bản là những gì được liệt kê ngay tại đây, và đó là loại giá trị 1/2.

Vì vậy, nếu chúng tôi muốn tạm dừng mã của mình trong chính xác 1/2, chúng tôi có thể gọi thời gian ngủ.

Vì vậy, đây là chức năng ngủ và truyền đối số là dấu chấm thời gian giây và điều đó sẽ tạm thời dừng mã hóa

của chúng ta chính xác là 1/2.

Được chứ.

Vì vậy, chúng tôi hãy sử dụng lại mã của chúng tôi bây giờ và chúng tôi sẽ suy nghĩ một chút về việc quyết định

xác định chính xác nơi chúng tôi sẽ chèn đoạn mã này để thực hiện tạm dừng trước khi chúng tôi đi và cố gắng tìm lại một

link.

Vì vậy, trước tiên hãy thêm mã sẽ làm cho công việc tạm dừng thực hiện sự việc xảy ra.

Để làm như vậy, chúng ta sẽ nói một cái gì đó như thời gian, giấc ngủ và sau đó là thời gian chấm giây như vậy bây giờ thời gian

Giây là một loại thời gian như chúng ta thấy.

Nhưng trên thực tế, loại thời gian thực sự là int 64.

Và đây là một kiến thức nhỏ về chính xác thời gian này.

Điều thứ hai đang ở ngay đây, tôi sẽ chỉ đi sâu vào cuộc rượt đuổi hơn là thảo luận dài dòng

về các loại ở đây.

Và tôi sẽ nói với bạn rằng nếu chúng tôi muốn tạm dừng trong nhiều giây, chúng tôi có thể nhân

giá trị này ngay tại đây và tạm dừng trong vài giây.

Vì vậy, ví dụ, nếu chúng tôi muốn chèn khoảng dừng 5 giây, chúng tôi có thể tiết kiệm thời gian gấp năm lần.

Thứ hai, như vậy.

Vì vậy, dòng mã này ngay tại đây sẽ tạm thời dừng quá trình chạy thực thi nó trong 5 giây.

Bây giờ, nếu chúng tôi xem mã ngay tại đây, tôi muốn bạn chỉ cần suy nghĩ trong giây lát xem

Đây phải là cách thích hợp để kết hợp các thao tác này với nhau hay không.

Nếu bạn thực sự nghĩ về điều đó, chúng tôi sẽ nói rằng mỗi khi có một sản phẩm có giá trị

khỏi kênh, hãy xem tạm dừng trong 5 giây và sau đó bắt đầu quá trình tiếp theo ngay lập tức để tìm lại liên kết này.

Bây giờ chỉ có một vấn đề lớn ở đây.

Tôi muốn bạn thực sự nghĩ về điều này trong một giây, vì vậy tôi sẽ vẽ một sơ đồ.

Được chứ.

Vì vậy, đây là loại những gì chúng ta đang xem ngay bây giờ, phải không?

Chúng tôi đã có quy trình Google của mình.

Chúng tôi có một khoảng dừng giữa mỗi cái.

Chúng tôi có Stack Overflow của chúng tôi và một khoảng dừng giữa, v.v.

Bây giờ, nếu chúng tôi đưa việc tạm dừng đó vào thói quen chính của mình, thì đó là một cuộc gọi chặn.

Và nó có nghĩa là khi quá trình chính bị tạm dừng, nó không thể nhận bất kỳ tin nhắn nào khác

qua kênh.

Bây giờ những tin nhắn đó không bị mất.

Họ được chỉ định nhận loại vào hàng hoặc xếp hàng.

Nhưng vấn đề là chúng tôi đang nói rằng tối đa chúng tôi chỉ có thể thực hiện một quy trình mới sau 5 giây

một lần.

Bởi vì khi chúng tôi đưa tuyên bố thời gian này vào trong thói quen chính của mình, chúng tôi đang nói, Ồ, được rồi,

Tương tự như truy cập google. com quy trình hoàn thành ngay tại đây.

Được chứ.

Chà, bây giờ chúng tôi sẽ tạm dừng công việc chính.

Vì vậy, quy trình chính đã bị tạm dừng tại thời điểm này.

Và sau đó chúng ta phải đợi 5 giây trước khi thức dậy trở lại.

Và vì vậy có thể có 5 giây giống như ngay tại đây.

Vì vậy, chúng tôi có thể nói từ đây đến đây trong 5 giây.

Và trong thời gian đó, quy trình Stack Overflow cũng có thể kết thúc.

Vì vậy, quy trình Stack Overflow sẽ đưa ra một thông báo vào kênh, nhưng quy trình chính sẽ không có sẵn

sẵn sàng nhận nó trong 2 giây nữa.

Và vì vậy chúng tôi rất nhanh chóng nhận ra ở đây rằng, thói quen chính sẽ chỉ có thể làm được

điều gì cứ sau 5 giây một lần nếu chúng tôi mã hóa thời gian chờ ngủ ở đó.

Vì vậy, thực sự không hợp lý nếu đặt lệnh tạm dừng hoặc lệnh ngủ trực tiếp vào thói quen

chính của chúng ta.

Chúng tôi muốn đảm bảo rằng quy trình chính thức luôn sẵn sàng và sẵn sàng nhận một số thông báo cho

kênh.

Nếu không, chúng tôi sẽ nhanh chóng điều chỉnh chính mình ở đây và nhận được rất nhiều thông báo

sao lưu bên trong kênh.

Vì vậy, rõ ràng chúng ta cần làm điều gì đó khéo léo hơn một chút ở đây.

Vì vậy, chúng tôi tạm dừng nhanh chóng.

Chúng ta sẽ quay trở lại trong phần tiếp theo và chúng ta sẽ tìm ra chính xác nơi chúng ta nên

set câu lệnh sleep này.

Vì vậy, hãy nhanh chóng nghỉ ngơi và chúng tôi sẽ giải quyết vấn đề đó chỉ sau một phút.