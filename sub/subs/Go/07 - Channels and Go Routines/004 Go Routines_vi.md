# 004 Đi thường lệ vi

---

Trong phần trước, chúng tôi đã nói về cách chương trình của chúng tôi hiện đang tìm kiếm từng URL, được mong đợi

yêu cầu hoàn thành và sau đó chuyển sang URL tiếp theo.

Tác động của điều này là nếu chúng tôi có nhiều URL mà chúng tôi muốn tìm thấy trong chương trình

của mình, sẽ mất nhiều thời gian để tìm từng URL một vì chúng tôi đang làm từng cái một.

Vì vậy, giải pháp rất nhanh chóng nên chúng tôi đưa ra quyết định rằng chúng tôi có thể muốn tìm ra

một số cách để tìm nhiều yêu cầu cùng một lúc.

Vì vậy, chúng tôi muốn gửi yêu cầu tới Google. com, Facebook, StackOverflow, v.v. cùng một lúc, sau đó để tất cả

cả hai đều giải quyết và cuối cùng đưa ra trạng thái của từng vấn đề.

Vì vậy, bây giờ tùy thuộc vào chúng tôi để tìm ra cách bắt đầu thực hiện các yêu cầu này cùng một lúc.

Vì vậy, trong video này, chúng ta sẽ bắt đầu nói về thói quen đi lại.

Bây giờ, có rất nhiều điều để nói về thói quen đi lại.

Vì vậy, trong video này, chúng tôi sẽ nói một chút về lý thuyết đằng sau chúng và cách chúng hoạt động trên máy tính

local của bạn hoặc tương tự như trên hệ điều hành địa phương của bạn ngay bây giờ.

Sau đó chúng ta sẽ nghỉ ngơi.

Chúng tôi sẽ quay lại video tiếp theo và chúng tôi sẽ bắt đầu thực sự phát triển các hoạt động quy trình trong chương trình của chúng tôi.

Vì vậy, video này là tất cả về một số lý thuyết và sau đó chúng tôi sẽ thực hiện phát triển khai thực tế

một khoảnh khắc.

Vì vậy, với suy nghĩ đó, hãy bắt đầu.

Bây giờ, điều đầu tiên tôi muốn bạn hiểu là khi chúng tôi khởi chạy một chương trình, giống như

Khi chúng tôi biên dịch và thực thi nó, chúng tôi sẽ tự động tạo một quy trình một lần.

Bạn có thể nghĩ rằng một thói quen đi như là một cái gì đó tồn tại bên trong chương trình đang chạy của tôi hoặc quy trình của chúng tôi.

Quy trình này sẽ lấy từng dòng mã trong chương trình của chúng tôi và thực thi từng dòng một.

Bây giờ, khi tôi nói dòng mã trong chương trình của chúng ta và thực thi từng dòng một, hãy nhớ rằng tất cả mã

mà chúng tôi đang viết đều được biên dịch.

Và vì vậy, chúng tôi không thể nhìn vào từng dòng theo nghĩa đen và nói, được rồi, dòng này, dòng này, dòng này.

Bởi vì hình thức biên dịch thực tế của mã hóa của chúng ta có thể nhìn thấy một chút khác, nhưng

để thảo luận, chúng tôi có thể tưởng tượng rằng một quy trình chỉ thực thi từng dòng mã của chúng ta.

Bây giờ tôi muốn đi sâu vào chương trình hiện có của chúng tôi và nghĩ về cách quy trình chính này được tạo ra

thực thi mã bên trong chương trình của chúng tôi.

Vì vậy, chúng tôi bắt đầu chương trình của mình.

Chúng tôi dòng này hoặc tất cả mã hóa bên trong đây, đây là tất cả mã hóa trong chương trình mà chúng tôi có được

thực thi tự động từng dòng theo quy trình này.

Vì vậy, quy trình bắt đầu và nó tạo ra các lát này hoặc các lát cắt, lát chuỗi, xin

lỗi và sau đó khởi động nó vào vòng lặp cho điều này, nơi nó bắt đầu lặp lại mỗi lần liên kết

bên trong lát cắt đó rồi gọi chức năng kiểm tra liên kết ngay tại đây.

Sau đó, chúng tôi nhập vào chức năng kiểm tra và sau đó chúng tôi nhận được yêu cầu HTTP thực tế này ngay tại đây.

Bây giờ, lệnh gọi hàm này được chúng ta gọi là lệnh gọi chặn vì đoạn mã bên trong ở đây bị mất

một khoảng thời gian để thực hiện việc này.

Khi chức năng này được thực thi, quy trình chính sẽ không thể làm gì khác.

Vì vậy, cơ sở dữ liệu của nó đã được đóng băng trên dòng mã này ngay tại đây và nó không có khả năng tiếp tục hoặc thực hiện bất kỳ lúc nào

điều gì khác trong chương trình của chúng tôi.

Vì vậy, chúng tôi sẽ giải quyết vấn đề này.

Chúng tôi sẽ tìm cách giảm thiểu vấn đề đó ngay tại đó bằng cách giới thiệu ý tưởng khởi chạy các quy trình

plugin bổ sung.

Vì vậy, họ thử xem một sơ đồ ở đây và tìm cách thức hoạt động của nó.

Được chứ.

Vì vậy, tôi biết cấu hình thực sự nhỏ, nhưng hy vọng nó vẫn dễ đọc.

Bây giờ tôi cũng sẽ đưa một chút yếu tố vào màn hình.

Vì vậy, đó là lý do tại sao tôi thu nhỏ ngay bây giờ.

Vì vậy, đây là những thay đổi mà chúng tôi sẽ thực hiện cho chương trình của mình.

Khi chúng ta gọi hàm kiểm tra liên kết, chúng ta sẽ đặt một từ khóa mới trước nó và

từ khóa mới nhất chỉ là từ đi.

Khi họ sử dụng từ khóa go, điều đó có nghĩa là hãy chạy chức năng này trong một quy trình hoàn toàn mới.

Và vì vậy, chúng ta hãy bắt đầu suy nghĩ về những gì sẽ xảy ra khi chúng ta bắt đầu khởi chạy quy trình truy cập mới để

run code of we ta.

Vì vậy, chúng tôi vẫn bắt đầu công việc chính của mình.

Chúng tôi vẫn đang tạo các lát cắt chuỗi này, chúng tôi bắt đầu lặp qua vòng lặp cho.

Sau đó, chúng tôi tìm thấy từ khóa go ngay tại đây và thời gian chạy Go tự động tạo một quy trình go new để chạy

cụ thể mã hóa trong quá trình kiểm tra liên kết chức năng.

Và vì vậy ngay khi họ nhấn từ khóa đi này ngay tại đây, họ có thể tưởng tượng rằng một quy trình hoàn tất

toàn bộ mới được tạo và thực thi trên máy tính của chúng ta.

Vì vậy, chúng tôi có thói quen đi theo thứ hai này hoặc loại công cụ thứ hai này chạy mã hóa trong chương trình của chúng tôi.

Nó khởi động và bắt đầu chạy tất cả các mã bên trong hàm kiểm tra từng dòng một.

Bây giờ, dòng mã đầu tiên được thực thi bởi quy trình mới này vẫn là lệnh chặn tương tự mà chúng

ta đã có trước khi nhận được yêu cầu thực sự.

Vì vậy, quy trình này sẽ mới, quy trình thứ hai được tạo vừa phải để chạy, chỉ cần chức năng này ngay tại

đây ngay lập tức chúng ta có thể tưởng tượng sẽ chuyển sang chế độ ngủ hoặc dừng thực thi mã hóa khi nó chờ hàm JIT này thực thi

đã được hoàn thành.

Bây giờ khi thứ này nói, cái này, loại thông tin thường này được phát hiện một sự kiện và nó nói với phần còn lại

của thế giới và nói, Này, có vẻ như tôi vừa phải một lệnh gọi hàm chặn ở đây.

Nếu có bất kỳ quy trình truy cập nào khác trong chương trình mà chúng tôi muốn chạy thì bây giờ sẽ là thời điểm tuyệt vời

để làm điều đó.

Và tại thời điểm đó, quy trình kiểm soát sau đó được chuyển trở lại quy trình hoạt động chính của chúng ta.

Sau đó, quy trình này được biết, đã được rồi, có vẻ như tôi vừa khởi động chức năng đó.

Có vẻ như thói quen đi không thể làm được gì khác.

Vì vậy, tôi sẽ thực hiện bước tiếp theo theo vòng lặp thông qua for.

Vì vậy, nó sẽ chuyển đến phần tử tiếp theo bên trong lát cắt.

Sau đó, nó chạy lại dòng mã này, nơi nó tạo ra một chức năng chạy thứ hai mới của quy trình

check tra.

Và vì vậy, họ có thể tưởng tượng rằng quy trình này sẽ được xoay vòng.

Quy trình thực hiện thứ hai sau đó chạy mã đầu tiên tại đây và không có yêu cầu thực hiện theo hướng dẫn nào

đến URL này và sau đó điều chính xác sẽ xảy ra như quy trình trước đó.

Vì vậy, quy trình đi này sẽ nói, Ồ, có vẻ như đây là một lệnh gọi hàm chặn.

Tôi không thể làm gì khác khi công việc này hoàn thành.

Và do đó, kiểm soát những gì chương trình sẽ quay trở lại quy trình chính một lần nữa và nó

sẽ tiếp tục tạo ra các quy trình mới cho đến khi có một số chuỗi hoặc địa chỉ mà chúng tôi đang cố gắng

Load ở đây.

Vì vậy, điều quan trọng cần ghi nhớ ở đây là mỗi lần chúng tôi sử dụng từ khóa này để khởi động

khởi chạy một chức năng mới, chúng tôi đang khởi chạy một quy trình mới.

Và chúng ta có thể nghĩ về những thói quen này giống như một công cụ nhỏ bắt đầu xử lý mã hóa

bên trong một hàm duy nhất.

Vì vậy, cú pháp xung quanh các quy trình này khá đơn giản.

Chúng tôi sẽ thực hiện bất kỳ lệnh gọi hàm nào mà chúng tôi muốn thực hiện bên trong cá nhân của chính

it, tiến trình quy trình và chỉ cần thêm từ khóa ngay trước đó.

Được chứ.

Vì vậy, điều đó có vẻ như, thế này, không tệ lắm, đơn giản là vậy, nhưng vẫn rất

nhiều quy tắc và tác dụng phụ rất thú vị và loại lý thuyết đằng sau những thứ thực sự quan

Điều quan trọng cần hiểu.

Vì vậy, chúng tôi sẽ tạm thời nghỉ ngay bây giờ và chúng tôi sẽ quay lại phần tiếp theo

và bắt đầu nói về một số trường hợp thực tế hoặc một số điều mà bạn có thể biết và hiểu về

những thói quen này .

Vì vậy, hãy bình tĩnh nhanh chóng và chúng tôi sẽ bắt đầu nói về những sản phẩm bổ sung này chỉ sau một phút.