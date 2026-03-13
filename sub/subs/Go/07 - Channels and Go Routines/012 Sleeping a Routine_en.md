# 012 Ngủ theo thói quen vi

---

-: Ở phần trước chúng tôi đã nói

mà chúng tôi muốn chèn một số loại

tạm dừng trước khi chúng tôi cố gắng tìm nạp lại một liên kết nhất định,

và vì vậy chỉ để đảm bảo

rằng chúng ta thực sự hiểu vòng lặp for ngay tại đây.

Vòng lặp for này có nghĩa là hãy xem kênh C

bất cứ khi nào một giá trị xuất hiện từ nó

gán giá trị đó cho l, l là viết tắt của một liên kết.

Khi giá trị đó xuất hiện và được gán cho L,

phần thân của vòng lặp for sẽ được thực thi ngay lập tức.

Vì vậy về cơ bản chúng tôi đang chờ đợi

về tuyên bố này ngay tại đây trước khi chúng ta lặn

vào phần thân thực sự của vòng lặp for và phần thân

của vòng lặp for ngay lập tức bắt đầu một liên kết kiểm tra, hãy thực hiện theo thói quen.

Vì vậy mục tiêu của chúng ta bây giờ là tìm ra

tìm ra cách nào đó để chèn một chút tạm dừng vào quá trình này.

Vì vậy chúng tôi muốn đảm bảo rằng chúng tôi tạm dừng

trước khi chúng tôi tiếp tục và cố gắng tìm lại liên kết.

Bây giờ việc tạm dừng thực sự sẽ

khá đơn giản

nhưng tìm ra chính xác nơi để đặt mã vào

việc tạm dừng sẽ khó khăn hơn một chút.

Vì vậy, hãy xem tài liệu của chúng tôi

và chúng ta sẽ tìm ra cách đặt

trong một số kiểu tạm dừng tùy ý trong mã của chúng tôi.

Vì vậy tôi sẽ chuyển sang phần tài liệu goling của chúng ta.

Vì vậy tôi đang xem tài liệu về các gói

mà chúng ta đã xem xét nhiều lần trước đây.

Bây giờ bên trong đây tôi sẽ cuộn

xuống tận cuối trang.

Tôi đang tìm một gói có tên time.

Được rồi, không phải là đáy

nhưng ít nhất là theo gói thời gian

gần như ở cuối trang.

Vì vậy chúng ta sẽ xem xét gói thời gian bên trong đây.

Chúng ta sẽ cuộn xuống phần chỉ mục và bên trong

trong đó bạn sẽ tìm thấy một chức năng gọi là ngủ ngay tại đây.

Vì vậy chúng ta hãy nhìn vào giấc ngủ.

Được rồi, giấc ngủ sẽ tạm dừng quy trình thực hiện hiện tại

trong ít nhất một khoảng thời gian D.

Vì vậy, đây là một hàm mà chúng ta có thể sử dụng ngay tại đây để đặt

trong một số tạm dừng tùy ý đối với mã của chúng tôi.

Bây giờ điều rất quan trọng cần lưu ý ở đây là thuật ngữ

mà nó sử dụng.

Nó báo thao tác này sẽ ngủ hoặc tạm dừng quy trình hoạt động hiện tại.

Và vì vậy chúng ta sẽ phải sớm tìm ra ở đây

tìm hiểu một chút về điều gì chính xác

chính xác đó là thói quen.

Chúng tôi thực sự muốn tạm dừng.

Bây giờ bạn sẽ nhận thấy rằng hàm tạm dừng có một đối số

của D, được cho là thuộc loại thời lượng.

Vì vậy, hãy nhấp vào thời lượng ngay tại đây

và tìm ra chính xác nó là gì.

Vì vậy, đây là loại thời lượng.

Nếu bạn cuộn xuống một chút

ở cuối phần này, bạn sẽ nhận thấy

rằng khoảng thời gian này cũng bao gồm hằng số thứ hai.

Và vì vậy về cơ bản chúng ta có thể gọi time.second.

Về cơ bản những gì được liệt kê ở đây.

Và đó là một loại giá trị của một giây.

Vì vậy, nếu chúng ta muốn tạm dừng mã của mình trong đúng một giây

chúng ta có thể gọi time.sleep.

Đây là chức năng ngủ

và truyền một đối số time.second

và điều đó sẽ tạm dừng mã của chúng tôi trong đúng một giây.

Được rồi, bây giờ hãy quay lại mã của chúng ta

và chúng ta sẽ suy nghĩ một chút

quyết định chính xác nơi chúng ta sẽ đến

chèn mã này để thực sự tạm dừng

trước khi chúng tôi tiếp tục và cố gắng tìm nạp lại một liên kết.

Vì vậy, trước tiên hãy thêm mã vào

điều đó sẽ làm cho việc tạm dừng thực sự xảy ra.

Để làm như vậy chúng ta sẽ nói điều gì đó như time.sleep

rồi lần thứ hai như vậy.

Bây giờ thời gian thứ hai là một loại thời lượng như chúng ta vừa thấy.

Nhưng trên thực tế, loại thời lượng đó thực sự là int 64.

Và đây là một chút

kiến thức về chính xác những gì lần này.thứ hai

thứ ở ngay đây

Tôi sẽ chỉ theo đuổi thay vì

hơn là thực hiện một cuộc thảo luận dài về các loại ở đây.

Và tôi sẽ nói với bạn rằng nếu chúng ta muốn tạm dừng

trong nhiều giây, chúng ta có thể nhân giá trị này ngay tại đây

và tạm dừng trong vài giây.

Vì vậy, ví dụ, nếu chúng ta muốn chèn một khoảng dừng

trong năm giây, chúng ta có thể nói năm lần

Time.second như vậy.

Vì vậy, dòng mã này ở đây sẽ

tạm dừng thói quen đi hiện tại đang thực thi nó

trong năm giây.

Bây giờ nếu chúng ta nhìn vào đoạn mã ở đây, tôi muốn bạn

chỉ cần suy nghĩ một chút xem có hay không

đây là một cách thích hợp để kết hợp hoạt động này với nhau.

Nếu bạn thực sự nghĩ về nó

chúng tôi đang nói điều đó mỗi lần

rằng một giá trị xuất phát từ kênh C

tạm dừng trong năm giây và sau đó ngay lập tức

bắt đầu quy trình tiếp theo để tìm nạp lại liên kết này.

Bây giờ chỉ có một vấn đề lớn ở đây.

Tôi muốn bạn thực sự suy nghĩ về điều này trong một giây.

Vì vậy, tôi sẽ vẽ một sơ đồ.

Được rồi, thế này thật tử tế

về những gì chúng ta đang xem xét, phải không?

Chúng tôi có thói quen sử dụng Google,

chúng ta có một khoảng dừng giữa mỗi phần,

chúng tôi đã gặp phải tình trạng tràn ngăn xếp và tạm dừng giữa các khoảng thời gian, v.v.

Bây giờ nếu chúng ta đặt sự tạm dừng đó vào thói quen chính của mình

đó là một cuộc gọi chặn

và điều đó có nghĩa là trong khi quy trình chính bị tạm dừng

nó không thể nhận bất kỳ tin nhắn nào khác thông qua kênh.

Bây giờ những tin nhắn đó không bị mất

họ chỉ giống như xếp hàng hoặc xếp hàng.

Nhưng vấn đề là chúng tôi đang nói rằng cùng lắm chúng tôi chỉ có thể

thực hiện một quy trình đi mới cứ năm giây một lần

bởi vì khi chúng ta đặt câu lệnh về giấc ngủ vào thời điểm này

của thói quen chính của chúng tôi, chúng tôi đang nói, ồ, được rồi

giống như quy trình truy cập google.com vừa kết thúc ngay tại đây.

Được rồi, bây giờ chúng ta sẽ tạm dừng công việc chính.

Vì vậy, quy trình chính bây giờ sẽ bị tạm dừng vào thời điểm này

và sau đó chúng ta phải đợi năm giây trước thứ đó

có thể tỉnh dậy trở lại.

Và có lẽ năm giây giống như ở đây.

Vậy có lẽ chúng ta đang nói từ đây đến đây là 5 giây.

Và trong thời gian đó quy trình tràn ngăn xếp

cũng có thể kết thúc.

Vì vậy thủ tục tràn ngăn xếp sẽ đưa ra một thông báo

vào kênh, nhưng quy trình chính sẽ không

hãy sẵn sàng đón nhận nó trong khoảng hai giây nữa.

Và vì vậy chúng tôi nhanh chóng nhận ra rằng này

thói quen chính sẽ chỉ có thể làm điều gì đó một lần

cứ năm giây một lần nếu chúng ta để mã thời gian ngủ ở đó.

Vì vậy, thật sự không thích hợp khi đặt câu lệnh tạm dừng hoặc

tuyên bố về giấc ngủ đó trực tiếp vào thói quen chính của chúng tôi.

Chúng tôi muốn đảm bảo rằng quy trình chính luôn hoạt động

và sẵn sàng nhận một số tin nhắn qua kênh.

Nếu không, chúng ta sẽ tăng ga rất nhanh

chúng tôi ở đây và nhận được rất nhiều

của các tin nhắn được sao lưu bên trong kênh.

Rõ ràng là chúng ta cần phải làm điều gì đó một chút

thông minh hơn ở đây.

Vì vậy chúng ta hãy tạm dừng nhanh chóng.

Chúng ta sẽ quay lại ở phần tiếp theo

và chúng ta sẽ tìm hiểu

chính xác nơi chúng ta nên đặt câu lệnh ngủ này.

Vì vậy, hãy nghỉ nhanh và chúng ta sẽ giải quyết vấn đề đó chỉ trong một phút.