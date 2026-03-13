# 004 Đi thường lệ vi

---

Giảng viên: Ở phần trước chúng ta đã nói chuyện

về cách chương trình của chúng tôi hiện đang tìm nạp một URL

tại một thời điểm, chờ đợi yêu cầu đó hoàn thành,

và sau đó chuyển sang URL tiếp theo.

Tác động của việc này là nếu chúng ta có nhiều URL

mà chúng tôi có thể muốn tìm nạp trong chương trình của mình,

sẽ mất nhiều thời gian để lấy từng cái một

bởi vì chúng tôi đang làm từng việc một.

Vì vậy, giải pháp rất nhanh chóng mà chúng tôi nghĩ ra là

để quyết định rằng chúng ta có thể muốn tìm ra cách nào đó

để lấy nhiều yêu cầu cùng một lúc.

Vì vậy, chúng tôi muốn gửi yêu cầu tới google.com,

Facebook, Stack Overflow, v.v. cùng một lúc

và sau đó để tất cả họ giải quyết

và cuối cùng in ra trạng thái của từng cái.

Vì vậy bây giờ việc của chúng ta là tìm ra cách

để Go thực sự thực hiện những yêu cầu này

cùng một lúc.

Vì vậy trong video này chúng ta sẽ bắt đầu nói chuyện

về Go Routines.

Bây giờ có rất nhiều điều để nói với Go Routines.

Vì vậy trong video này chúng ta sẽ nói một chút

về lý thuyết đằng sau chúng

và cách chúng hoạt động trên máy tính cục bộ của bạn

hoặc giống như trên hệ điều hành cục bộ của bạn ngay bây giờ.

Sau đó chúng ta sẽ nghỉ ngơi và quay lại

trong video tiếp theo và chúng ta sẽ bắt đầu

để thực sự triển khai Go Routines trong chương trình của chúng tôi.

Vì vậy, video này chủ yếu nói về một số lý thuyết

và sau đó chúng ta sẽ triển khai thực tế sau một lát nữa.

Vì vậy, với ý nghĩ đó, chúng ta hãy bắt đầu.

Bây giờ, điều đầu tiên tôi muốn bạn hiểu là

rằng khi chúng tôi khởi chạy một chương trình Go, giống như khi chúng tôi biên dịch nó

và thực thi nó, chúng tôi sẽ tự động tạo một Quy trình đi.

Bạn có thể nghĩ về một thói quen đi

như là một cái gì đó tồn tại bên trong

của chương trình đang chạy hoặc quy trình của chúng tôi.

Quy trình Go này sử dụng mọi dòng mã

bên trong chương trình của chúng tôi và thực hiện từng cái một.

Bây giờ, khi tôi nói dòng mã

trong chương trình của chúng ta và thực hiện từng cái một, hãy nhớ

rằng tất cả mã chúng ta đang viết đều được biên dịch.

Và vì thế chúng ta không thể nhìn theo nghĩa đen

ở mỗi dòng và nói,

"Được rồi, dòng này, dòng này, dòng này,"

bởi vì hình thức biên soạn thực tế

mã của chúng tôi có thể trông hơi khác một chút.

Nhưng để thảo luận, chúng ta có thể tưởng tượng

rằng Go Routine chỉ thực thi từng dòng mã của chúng tôi.

Bây giờ tôi muốn đi sâu vào chương trình hiện có của chúng tôi

và suy nghĩ về cách tạo ra Quy trình đi chính này

đang thực thi mã bên trong chương trình của chúng tôi.

Vì vậy, chúng tôi bắt đầu chương trình của mình,

dòng này hoặc tất cả mã bên trong đây,

đây là tất cả mã trong chương trình của chúng tôi,

được tự động thực thi từng dòng theo Quy trình Go này.

Vì vậy, Quy trình đi bắt đầu và nó tạo ra chuỗi này

lát hoặc lát dây này, xin lỗi.

Sau đó nó bắt đầu vào vòng lặp for và bắt đầu lặp lại

qua mỗi liên kết bên trong lát cắt đó.

Sau đó nó gọi hàm checkLink ngay tại đây.

Sau đó chúng ta nhập vào hàm checkLink và sau đó chúng ta nhận được

tới yêu cầu HTTP thực tế này ngay tại đây.

Bây giờ lệnh gọi hàm này là những gì chúng tôi đề cập đến

như một cuộc gọi chặn

bởi vì mã bên trong ở đây cần một số tiền

thời gian để thực hiện.

Trong khi chức năng này đang được thực thi,

Quy trình đi chính không thể làm gì khác.

Vì vậy, về cơ bản nó đã bị đóng băng trên dòng mã này ngay tại đây

và nó không có khả năng tiếp tục hay làm bất cứ điều gì khác

bên trong chương trình của chúng tôi.

Vì vậy, chúng tôi sẽ khắc phục vấn đề này.

Chúng ta sẽ bằng cách nào đó giảm thiểu vấn đề đó ngay tại đó

bằng cách giới thiệu ý tưởng triển khai các Quy trình đi bổ sung.

Vì vậy chúng ta hãy nhìn vào một sơ đồ ở đây

và tìm hiểu xem nó sẽ hoạt động như thế nào.

Được rồi, tôi biết văn bản ở đây rất nhỏ

nhưng hy vọng nó vẫn đọc được.

Bây giờ tôi sẽ lấy một vài yếu tố

cũng lên màn hình,

vì vậy đó là lý do tại sao tôi đang thu nhỏ nó ra ngay bây giờ.

Vì vậy đây là sự thay đổi mà chúng ta sẽ thực hiện

đến chương trình của chúng tôi.

Khi chúng ta gọi hàm checkLink đó,

chúng ta sẽ đặt một từ khóa mới trước nó.

Và từ khóa mới đó chỉ là từ đi.

Khi chúng tôi sử dụng từ khóa Go,

điều đó có nghĩa là hãy chạy chức năng này bên trong Go Routine hoàn toàn mới.

Và vì vậy hãy bắt đầu suy nghĩ kỹ xem điều gì sẽ xảy ra

khi chúng tôi bắt đầu khởi chạy các Quy trình Go mới để chạy mã của mình.

Vì vậy, chúng tôi vẫn bắt đầu công việc chính của mình.

Chúng ta vẫn tạo chuỗi các lát cắt.

Chúng ta bắt đầu lặp qua vòng lặp for.

Sau đó chúng ta thấy từ khóa go ngay tại đây

và thời gian chạy Go sẽ tự động tạo một Quy trình Go mới

để chạy mã cụ thể bên trong

của hàm checkLink.

Và ngay khi chúng ta nhấn vào từ khóa go này ngay tại đây,

chúng ta có thể tưởng tượng

rằng một Quy trình Go hoàn toàn mới đã được tạo

và thực hiện trên máy tính của chúng tôi.

Vì vậy, chúng tôi có Quy trình đi thứ hai hoặc loại thứ hai này

của công cụ chạy mã bên trong chương trình của chúng tôi.

Nó khởi động và bắt đầu chạy tất cả

mã bên trong hàm checkLink theo từng dòng.

Bây giờ, dòng mã đầu tiên được thực thi

bởi Quy trình Go mới này vẫn là cuộc gọi chặn tương tự

mà chúng tôi đã có trước đây, yêu cầu nhận thực tế.

Vì vậy, Quy trình đi mới này, quy trình thứ hai

vừa được tạo để chạy chức năng này ngay tại đây,

ngay lập tức chúng ta có thể tưởng tượng đi ngủ

hoặc dừng thực thi mã khi chờ hàm get này

thực sự được hoàn thành.

Bây giờ khi thứ này nói, "Ồ này," kiểu Go Routine này

of phát ra một sự kiện và nó cho biết phần còn lại

của thế giới và nói,

"Này, hình như tôi vừa chạy

vào một cuộc gọi chức năng chặn ở đây.

Nếu có bất kỳ Quy trình đi nào khác trong chương trình của chúng tôi

muốn chạy, bây giờ sẽ là thời điểm tuyệt vời để làm điều đó."

Và tại thời điểm đó, luồng điều khiển sẽ được truyền trở lại

vào Quy trình đi chính của chúng tôi.

Sau đó, Quy trình đi này sẽ nói: "Được rồi, có vẻ như

giống như tôi vừa khởi chạy chức năng đó.

Có vẻ như Go Routine không thể làm gì khác được.

Vì vậy tôi sẽ thực hiện bước lặp tiếp theo

thông qua vòng lặp for."

Và do đó nó đi tới phần tử tiếp theo bên trong lát cắt

và sau đó nó chạy lại dòng mã này

nơi nó tạo ra Quy trình đi mới thứ hai

chạy chức năng checkLink.

Và chúng ta có thể tưởng tượng rằng Go Routine thứ hai này

sau đó được quay lên.

Quy trình đi thứ hai sau đó chạy ngay dòng đầu tiên

mã ở đây và cố gắng thực hiện yêu cầu nhận

tới URL này.

Và điều tương tự sẽ xảy ra

như lần trước.

Vì vậy, Quy trình đi này sẽ nói,

"Ồ, có vẻ như đây là lệnh gọi chức năng chặn.

Tôi không thể làm gì khác cho đến khi chuyện này hoàn tất.”

Và vì vậy việc kiểm soát chương trình sẽ quay trở lại

quay lại quy trình đi chính một lần nữa

và nó sẽ tiếp tục sinh ra các Thói quen đi mới

cho đến khi có số bằng số đó

chuỗi hoặc địa chỉ mà chúng tôi đang cố gắng tìm nạp ở đây.

Vì vậy điều quan trọng cần ghi nhớ ở đây là

rằng mỗi lần chúng ta sử dụng từ khóa go này

Để khởi chạy một chức năng mới, chúng tôi sẽ khởi chạy Quy trình đi mới.

Và chúng ta có thể nghĩ về những thói quen đi này

giống như một động cơ nhỏ khởi động

để duyệt qua mã bên trong một hàm duy nhất.

Vậy cú pháp xung quanh các Quy trình đi này

khá đơn giản.

Chúng ta sẽ thực hiện bất kỳ lệnh gọi hàm nào

mà chúng tôi muốn bị hành quyết bên trong

của riêng nó Go Routine

và chỉ cần thêm từ khóa Go ngay trước nó.

Được rồi, điều đó có vẻ giống như, này,

không tệ lắm, khá đơn giản.

Nhưng vẫn còn rất nhiều quy định rất thú vị

và tác dụng phụ và loại lý thuyết

đằng sau những điều thực sự quan trọng cần hiểu.

Vì vậy bây giờ chúng ta sẽ nghỉ ngơi nhanh chóng

và chúng ta sẽ quay lại trong phần tiếp theo

và bắt đầu nói về một số trường hợp thực tế

hoặc một số điều mà có lẽ bạn nên biết

và hiểu về các Quy trình đi này.

Vì vậy, hãy nghỉ ngơi nhanh chóng và chúng ta sẽ bắt đầu nói chuyện

về những mục bổ sung này chỉ trong một phút.