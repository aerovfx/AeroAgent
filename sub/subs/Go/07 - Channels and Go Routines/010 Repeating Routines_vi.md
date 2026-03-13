# 010 Các thói quen lặp đi lặp lại vi

---

Trong phần cuối cùng, chúng tôi đã tìm ra cách đảm bảo rằng chúng tôi chỉ nhận được một số lượng tin nhắn bằng cách

với số lượng yêu cầu mà chúng tôi thực hiện.

Bây giờ tôi muốn thực hiện một thay đổi nhỏ đối với chương trình của chúng tôi, vì vậy tôi sẽ bổ sung thêm một yêu cầu bổ sung

sung hoặc một tính năng bổ sung.

Tôi muốn nói rằng chúng tôi sẽ không ping từng trang web này chỉ một lần.

Tôi muốn nói rằng tôi muốn liên tục ping từng trang web nhiều lần, lặp đi lặp lại mỗi khi chúng tôi

đưa ra yêu cầu.

Vì vậy, giả sử rằng chúng tôi đã tạo một tài khoản cho Google. com.

Bất cứ khi nào quy trình này kết thúc, tôi muốn bắt đầu ngay lập tức một quy trình khác

Load lại Google.

Và vì vậy, điều này sẽ làm cho chương trình của chúng ta hoạt động giống như một trạng thái kiểm tra hơn một chút, ở đâu

chúng tôi liên tục đưa ra các vòng lặp yêu cầu đi lặp lại cho đến khi cuối cùng chúng tôi nói, Ồ, có

có vẻ như có lỗi ở đây.

Có thể trang web này đã ngừng hoạt động vào thời điểm này.

Vì vậy, hãy tìm hiểu xem chúng tôi sẽ thay đổi những gì trong chương trình của mình để biến điều đó thành hiện thực.

Vì vậy, về cơ bản, chúng tôi muốn nói rằng bất kỳ khi nào có yêu cầu hoàn thành, chúng tôi sẽ bắt

đầu lập tức sao lưu.

Và vì vậy, rất có thể nó sẽ phải làm điều gì đó với vòng lặp này ngay tại đây mà chúng ta

đã đặt trước đó giống nhau, bởi vì đây là mã dòng hoặc mã khối ngay tại đây về cơ bản được xử lý

bất cứ khi nào một yêu cầu được hoàn thành.

Vì vậy, đây là những gì tôi sẽ làm.

Chúng tôi sẽ nói rằng bất cứ khi nào việc kiểm tra liên kết chức năng đều được hoàn thành, thay vào đó sẽ trả lại, hoặc

tôi nên nói điều này đơn giản trên kênh với cố định chuỗi này ngay tại đây, giả sử rằng bất chấp

bất cứ khi nào chúng tôi hoàn thành yêu cầu, chúng tôi sẽ lấy liên kết của chúng tôi, cũng là một chuỗi và đưa nó

vào kênh.

Sau đó quay lại vòng lặp này ngay tại đây, chúng tôi có thể nhận được liên kết thông qua kênh đó.

Bất cứ khi nào chúng tôi nhận được liên kết thông qua kênh, điều đó có nghĩa là quy trình

trước đó phải kết thúc và chúng tôi nên bắt đầu một quy trình truy cập khác, cố gắng gọi liên kết tìm kiếm bằng một liên kết

xác định hoặc kiểm tra liên kết nhất với liên kết đã chọn.

Xin lỗi cho tôi hỏi.

Được rồi, vậy hãy thử xem.

Điều đầu tiên chúng tôi sẽ làm là tìm ra cả hai câu lệnh mà chúng tôi cung cấp giá trị cho kênh của

mình thay vì đưa ra cố định chuỗi này.

Tôi sẽ nói rằng chúng tôi sẽ đưa liên kết của chúng tôi vào kênh.

Vì vậy, hãy nhớ rằng, chúng tôi đang nhận các liên kết dưới dạng đối số và đây là URL hoặc địa chỉ thực tế mà chúng

tôi đã đưa ra yêu cầu.

Vì vậy, chúng tôi cũng sẽ thay thế nó ở đây.

Vì vậy, hiện tại khi chúng tôi hoàn thành yêu cầu, chúng tôi sau đó đăng xuất, Này, trang web này liên tục hoạt động hoặc nó hoạt động, sau đó

chúng tôi lấy liên kết đó và cung cấp nó cho kênh của chúng tôi.

Vì vậy, bây giờ chúng tôi quay trở lại trong vòng lặp mà chúng tôi vừa làm.

Chúng tôi cần sửa mã này ngay tại đây để đảm bảo rằng bất cứ khi nào chúng tôi nhận được giá trị này, sau đó chúng tôi sẽ

bắt đầu một kiểm tra liên kết khác, thực hiện quy trình.

Vì vậy, tôi sẽ thay thế dòng lệnh ở dạng định dạng ngay tại đây bằng một lệnh gọi để kiểm tra liên kết.

Và chúng tôi sẽ gọi liên kết Séc với giá trị mang lại cho kênh.

Vì vậy, chúng tôi đang nói rằng chúng tôi muốn nhận được một giá trị từ kênh, nghĩa là

chúng tôi sẽ đặt một mũi tên và sau đó đặt tên kênh như vậy.

Vì vậy, hãy nhớ nhận giá trị này hoặc nhận giá trị thông qua kênh là một

hoạt động chặn.

Và vì vậy, chúng tôi sẽ chỉ ngồi một chỗ và chờ đợi khi chúng tôi nhận được một giá trị ở đây và sau đó chúng tôi sẽ ngay lập tức gọi nó

is check link with it.

Bây giờ, điều cuối cùng chúng ta phải làm là đảm bảo rằng chúng ta gọi liên kết kiểm tra và tạo thói quen sử dụng

nó.

Và để làm được điều đó, chúng tôi chắc chắn rằng chúng tôi sẽ đặt từ khóa ngay trước nó.

Bây giờ, chỉ một bước cuối cùng.

Một điều cuối cùng mà chúng tôi phải thực hiện.

Vòng lặp cho vòng này sẽ chỉ chạy giống như năm hoặc sáu lần, về cơ bản là số lần mà chúng ta có hoặc

tuy nhiên có nhiều chuỗi mà chúng ta có trong lát của kiểu chuỗi đó.

Nhưng tôi đang nói rằng tôi muốn chắc chắn rằng chúng tôi chỉ liên tục tìm tải các liên kết từ bây giờ cho đến Viễn Viễn.

Vì vậy, luôn luôn, miễn là chương trình này đang chạy, tôi muốn chắc chắn rằng chúng tôi luôn truy cập và cố gắng

Load một số plugin liên kết.

Vì vậy, để đảm bảo rằng chúng ta chỉ lặp vĩnh viễn bên trong vòng lặp cho điều này, chúng ta có

có thể cô ấy trả lời cú pháp bên trong thành phần thứ hai và sau đó là dấu ngoặc mở.

Vì vậy, quyền này ở đây là một vòng lặp vô hạn.

Nó sẽ không bao giờ thoát ra.

Nó sẽ không bao giờ thoát khỏi điều này.

Vì vậy, bất kể khi nào chúng tôi đặt giá trị vào kênh của mình, chúng tôi sẽ tạo quy trình truy cập mới với các chức năng liên kết

check check.

Sau đó, vòng lặp for sẽ chuyển sang vòng lặp tiếp theo, nơi nó sẽ được mong đợi một giá trị

other information qua kênh.

Và vì vậy, mặc dù đây là một vòng lặp vô hạn, nó sẽ không được gọi như một triệu lần

mỗi giây.

Vòng lặp for like thế này sẽ không thực hiện lặp lại vòng lặp, cứ lặp đi lặp lại

lặp lại.

Nhiều, rất nhiều lần trong một giây.

Việc nhận giá trị thông qua kênh này vẫn là một hoạt động bị chặn và thực hiện vòng lặp để tiếp tục tự động

diễn trình hoặc it lặp lại chỉ mục bất kỳ lúc nào mà chúng tôi thực sự nhận được một mức giá

giá trị thông qua kênh, có thể là tốt nhất có thể là một năm một giây, giả sử rằng chúng tôi đang tìm kiếm

Load các yêu cầu này ở mức cao hoặc chúng tôi đang hoàn thành các yêu cầu HTTP này rất nhanh.

Vì vậy, chúng tôi hãy lưu điều này và bây giờ hãy xem điều gì sẽ xảy ra.

Bây giờ, khi tôi lưu tệp, bạn sẽ tìm thấy một lỗi nhỏ ở đây.

Lỗi của tôi.

Tôi đã không vượt qua kênh như một đối số thứ hai.

Vì vậy, hãy nhớ rằng chúng tôi mong đợi sẽ nhận được thứ hai.

Kênh là đối số thứ hai, vì vậy chúng tôi đảm bảo rằng chúng tôi sẽ đặt dấu coma sau đó

rồi đặt kênh như vậy.

Vì vậy, bây giờ hãy lưu nó và biên dịch thành công.

Và vì vậy điều này thực sự khá thú vị ngay tại đây.

Lưu ý cách Kiểm tra liên kết mong đợi xem một chuỗi là đối số đầu tiên và vì vậy Go có thể nói một cách rất

thông minh rằng, Ồ, điều này giống như một kênh sẽ tạo ra một chuỗi.

Và vì vậy, chúng tôi sẽ cho phép đây là đối số đầu tiên, mặc dù rõ ràng như bạn và tôi nhìn vào

điều này và gee, nó chắc chắn không giống như một chuỗi đối với tôi, nhưng Chúa biết rằng điều này cuối cùng sẽ tạo ra

một chuỗi.

Và vì vậy nó được phép là đối số đầu tiên phù hợp với loại chuỗi mà chúng ta mong đợi sẽ được tìm thấy.

Được rồi, hãy chạy mã này và bây giờ hãy xem điều gì sẽ xảy ra.

Vì vậy, tôi sẽ lại một thiết bị cuối cùng của mình và tôi có một vài tin nhắn trong đó.

Vì vậy, chúng tôi sẽ chạy xoài và bây giờ chúng tôi bắt đầu tìm kiếm các liên kết của chúng tôi và bạn có thể tìm thấy chúng tôi rất nhanh

đang tìm tất cả các địa chỉ khác nhau, vòng lặp này lặp lại rất nhanh.

Vì vậy, tại thời điểm này, chỉ nên thực hiện yêu cầu hoạt động năm ở bất kỳ thời điểm nào.

Vì vậy, mã này chắc chắn đang hoạt động.

Nhưng tôi nghĩ bạn có thể đồng ý với tôi rằng chúng tôi có thể không cần phải ping từng trang web

điều này quá nhanh.

Vì vậy, có lẽ điều cuối cùng chúng ta cần làm ở đây là chắc chắn rằng giữa mỗi lần tìm kiếm thành công,

chúng ta nên tạm dừng một chút ở đây để các trang web khác nhau điều này không nghĩ rằng chúng ta đang cố gắng

Chúng tôi sẽ làm đầy chúng theo yêu cầu.

Vì vậy, có thể chúng tôi sẽ nói rằng chúng tôi sẽ chỉ đặt một số tùy chọn khoảng thời gian vào giữa mỗi yêu cầu.

Vì vậy, hãy tìm cách giải quyết vấn đề đó trong phần tiếp theo.