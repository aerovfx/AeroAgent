# 010 Các thói quen lặp đi lặp lại en

---

Giáo viên: Ở phần cuối,

chúng tôi đã tìm ra cách để đảm bảo

rằng chúng tôi chỉ nhận được một số tin nhắn

bằng với số lượng yêu cầu mà chúng tôi thực hiện.

Bây giờ tôi muốn thực hiện một thay đổi nhỏ cho chương trình của chúng tôi.

Vì vậy tôi sẽ thêm vào một yêu cầu bổ sung

hoặc một tính năng bổ sung.

Tôi muốn nói rằng chúng ta sẽ không ping

mỗi trang web này chỉ một lần,

Tôi muốn nói rằng tôi muốn liên tục ping

mỗi trang web lặp đi lặp lại nhiều lần.

Mỗi lần chúng tôi đưa ra yêu cầu,

vì vậy giả sử chúng tôi tạo một liên kết cho google.com,

bất cứ khi nào thói quen này kết thúc

Tôi muốn bắt đầu ngay lập tức

một quy trình khác cố gắng tìm nạp lại Google.

Và điều này sẽ làm cho chương trình của chúng ta

hoạt động nhiều hơn một chút

giống như một người kiểm tra trạng thái có thể sẽ làm vậy

nơi chúng tôi liên tục đưa ra yêu cầu

hết lần này đến lần khác cho đến khi cuối cùng chúng ta nói,

ồ, hình như có lỗi ở đây.

Có lẽ trang web này đã ngừng hoạt động vào thời điểm này.

Vì vậy, hãy tìm hiểu xem chúng ta sẽ thay đổi điều gì

bên trong chương trình của chúng tôi để biến điều đó thành hiện thực.

Vì vậy, về cơ bản chúng tôi muốn nói

rằng bất cứ lúc nào một yêu cầu hoàn thành,

sau đó chúng tôi sẽ ngay lập tức bắt đầu sao lưu ngay lập tức.

Và rất có thể là nó sẽ phải làm điều gì đó với

Vòng lặp For này ngay tại đây mà trước đây chúng tôi đã tập hợp lại

because this is the line of code

hoặc khối mã ở đây về cơ bản là xử lý

bất cứ khi nào một yêu cầu được hoàn thành.

Vì vậy đây là những gì chúng ta sẽ làm.

Chúng ta sẽ nói,

rằng bất cứ khi nào chức năng liên kết kiểm tra được hoàn thành,

thay vì quay trở lại,

hoặc tôi nên nói là đẩy chuỗi đơn giản này vào kênh,

hoặc chuỗi cố định này ngay tại đây,

giả sử rằng bất cứ khi nào chúng tôi hoàn thành yêu cầu,

chúng tôi lấy liên kết của chúng tôi cũng là một chuỗi,

và đẩy nó vào kênh.

Sau đó quay lại vòng For này ngay tại đây,

chúng ta có thể nhận được liên kết đó thông qua kênh,

bất cứ khi nào chúng tôi nhận được liên kết qua kênh,

điều đó có nghĩa là công việc trước đó chắc chắn vừa kết thúc

và chúng ta nên bắt đầu một thói quen đi khác

lại cố gắng gọi liên kết tìm nạp bằng một liên kết nhất định,

hoặc kiểm tra liên kết với một liên kết nhất định, xin lỗi.

Được rồi, vậy hãy thử xem.

Điều đầu tiên chúng ta sẽ làm

là tìm cả hai câu lệnh

nơi chúng tôi đẩy giá trị vào kênh của mình.

Thay vì đẩy những sợi dây cố định này vào,

Tôi sẽ nói rằng chúng ta sẽ đẩy liên kết của chúng ta

vào kênh.

Vì vậy hãy nhớ rằng, chúng ta đang nhận liên kết làm đối số

và đây là URL hoặc địa chỉ thực tế

mà chúng tôi đang đưa ra yêu cầu.

Vì vậy, chúng tôi cũng sẽ thay thế nó ở đây.

Được rồi, bây giờ khi chúng ta hoàn thành yêu cầu,

sau đó chúng tôi đăng xuất,

"Này, trang web này ngừng hoạt động hoặc nó vẫn hoạt động."

Và sau đó chúng tôi lấy liên kết đó và đẩy nó vào kênh của chúng tôi.

Vì vậy bây giờ hãy quay lại bên trong Vòng lặp For mà chúng ta vừa mới thực hiện,

chúng ta cần sửa mã này ngay tại đây

để đảm bảo rằng bất cứ khi nào chúng tôi nhận được giá trị này

sau đó chúng tôi khởi động một liên kết kiểm tra khác, tiếp tục công việc như thường lệ.

Vì vậy tôi sẽ thay thế

định dạng dòng lệnh in dấu chấm ngay tại đây,

với một cuộc gọi để kiểm tra liên kết.

Và chúng ta sẽ gọi liên kết kiểm tra

với giá trị đi ra khỏi kênh.

Và vì vậy chúng tôi đang nói

mà chúng tôi muốn nhận được một giá trị từ kênh,

điều đó có nghĩa là chúng ta sẽ đặt một mũi tên,

và sau đó là tên kênh, như vậy.

Được rồi, hãy nhớ nhận giá trị này

hoặc nhận một giá trị thông qua kênh

là một hoạt động chặn.

Và vì vậy chúng ta sẽ chỉ ngồi xung quanh và chờ đợi

cho đến khi chúng ta nhận được một giá trị ở đây

và sau đó chúng tôi sẽ gọi ngay liên kết kiểm tra với nó.

Bây giờ điều cuối cùng chúng ta phải làm,

hãy đảm bảo rằng chúng tôi gọi kiểm tra Link

và tạo thói quen đi với nó.

Và để làm được điều đó, chúng ta sẽ đảm bảo

rằng chúng tôi đặt từ khóa go ngay trước nó.

Được rồi, bây giờ chỉ còn một bước cuối cùng, một điều cuối cùng chúng ta phải làm.

Hiện tại, For Loop này chỉ mới chạy

như năm hay sáu lần,

về cơ bản là số lần chúng ta có

hoặc bao nhiêu chuỗi chúng ta có

trong lát chuỗi kiểu đó.

Nhưng tôi đang nói rằng tôi muốn chắc chắn rằng

chúng tôi chỉ liên tục tìm nạp các liên kết từ bây giờ đến vĩnh cửu.

Vì vậy, trong suốt thời gian chương trình này đang chạy,

Tôi muốn chắc chắn rằng chúng ta luôn đi

và cố gắng tìm nạp một số liên kết bổ sung.

Vì vậy để đảm bảo rằng chúng ta chỉ lặp lại mãi mãi

bên trong bốn vòng lặp này,

chúng ta có thể cô đọng cú pháp bên trong thứ này

đơn giản là for và sau đó là dấu ngoặc nhọn mở đầu.

Vậy đây là một vòng lặp vô hạn.

Nó sẽ không bao giờ thoát ra được,

nó sẽ không bao giờ thoát khỏi điều này.

Vì vậy, bất cứ khi nào chúng tôi đặt một giá trị vào kênh của mình,

sau đó chúng tôi sẽ tạo ra quy trình đi mới

với chức năng liên kết kiểm tra.

Vòng lặp For sau đó sẽ chuyển sang lần lặp tiếp theo

nó sẽ ở đâu rồi lại đợi

cho một giá trị khác thông qua kênh.

Và mặc dù đây là một vòng lặp vô hạn,

nó sẽ không được gọi

khoảng một triệu lần mỗi giây,

như thế này For Loop sẽ không được thực thi

một lần nữa, một lần nữa, và một lần nữa,

cứ như thế, hết lần này đến lần khác,

nhiều, rất nhiều lần trong một giây.

Việc nhận giá trị này thông qua kênh

vẫn là một hoạt động chặn.

Và vòng lặp For

sẽ chỉ tiến triển thông qua chính nó,

hoặc nó sẽ lặp lại bất cứ lúc nào

rằng chúng ta thực sự nhận được một giá trị thông qua kênh

có thể giống như, bạn biết đấy,

tốt nhất có thể là năm lần một giây,

giả sử rằng chúng tôi đang tìm nạp những HTT này,

hoặc chúng tôi đang hoàn thành các yêu cầu HTTP này rất nhanh.

Được rồi, hãy lưu cái này lại và bây giờ xem điều gì sẽ xảy ra.

Bây giờ khi tôi lưu tập tin,

bạn sẽ thấy có một chút sai sót ở đây.

Lỗi của tôi, tôi đã không vượt qua được kênh

như một đối số thứ hai.

Vì vậy hãy nhớ rằng, nó mong đợi chúng ta nhận được

kênh làm đối số thứ hai.

Vì vậy, chúng tôi sẽ đảm bảo rằng chúng tôi đặt dấu phẩy sau đó

rồi đặt kênh như vậy.

Vì vậy, bây giờ hãy lưu nó và nó biên dịch thành công.

Và điều này thực sự khá thú vị ở đây.

Lưu ý cách kiểm tra liên kết mong đợi

để xem một chuỗi là đối số đầu tiên.

Và do đó, go có thể nói rất thông minh,

"Ồ, cái này trông giống như một kênh

điều đó sẽ tạo ra một chuỗi.

Và vì vậy chúng tôi sẽ cho phép đây là đối số đầu tiên."

Mặc dù rõ ràng như bạn và tôi nhìn vào điều này

và trời ơi, đối với tôi nó chắc chắn không giống một sợi dây,

nhưng đi biết rằng điều này sẽ xảy ra

cuối cùng tạo ra một chuỗi.

Và vì vậy nó được phép là đối số đầu tiên

khớp với chuỗi loại mà chúng ta mong đợi thấy.

Được rồi, hãy chạy mã này và xem điều gì sẽ xảy ra.

Vì vậy, tôi sẽ quay lại thiết bị đầu cuối của mình

và tôi có một vài tin nhắn trong đó.

Vì vậy chúng ta sẽ chạy main.go,

và bây giờ chúng tôi bắt đầu tìm nạp các liên kết của mình.

Và bạn có thể thấy rất nhanh chúng tôi đang tìm nạp

tất cả những địa chỉ khác nhau này

một lần nữa, một lần nữa, và một lần nữa rất, rất nhanh.

Vì vậy vào thời điểm này,

thực sự chỉ nên có năm yêu cầu

hoạt động ở bất kỳ thời điểm nào.

Được rồi, mã này chắc chắn đang hoạt động

nhưng tôi nghĩ bạn có thể đồng ý với tôi,

mà có lẽ chúng ta không cần ping

mỗi trang web này khá nhanh chóng.

Vậy có lẽ điều cuối cùng chúng ta cần làm ở đây

là đảm bảo rằng giữa mỗi lần tìm nạp thành công,

chúng ta nên tạm dừng một chút ở đây,

để những trang web khác nhau này không nghĩ

rằng chúng tôi đang cố gắng gửi cho họ nhiều yêu cầu.

Vì vậy có lẽ chúng ta sẽ nói rằng họ sẽ chỉ đặt

một số khoảng thời gian tùy ý ở giữa mỗi yêu cầu.

Vì vậy, hãy tìm cách giải quyết vấn đề đó trong phần tiếp theo.