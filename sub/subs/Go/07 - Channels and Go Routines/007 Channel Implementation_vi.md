# 007 Thực hiện kênh vi

---

Trong video cuối cùng, chúng tôi thấy rằng các thói quen quen thuộc của chúng tôi phải như thoát ra ngay khi nó tạo ra tất cả các thói quen

quen với hoạt động của nó.

Và vì vậy, chúng tôi rất nhanh chóng được biết rằng ngay sau khi quy trình chính của chúng tôi hết mã hóa để thực hiện điều này,

toàn bộ chương trình sẽ thoát ra.

Mặc dù vậy, chúng tôi vẫn có những thói quen khác đang chạy.

Sau đó, chúng tôi đã nói về cách chúng tôi có thể giải quyết vấn đề này bằng cách sử dụng một kênh để giao tiếp giữa tất cả các vấn đề đó

các hoạt động khác nhau của các quy trình này.

Vì vậy, về cơ bản, chúng tôi sẽ tạo một kênh mà chúng tôi có thể sử dụng để nói, Này, quy trình này đã hoàn thành chưa?

Quy trình này đã hoàn thành chưa?

Cái này chưa hoàn thành?

Được chứ.

Hiện tại, thói quen chính có thể thoát ra sớm hơn.

Hiện tại, việc sử dụng các kênh không còn dễ dàng như vậy.

Vì vậy, chúng tôi sẽ tìm hiểu rất nhiều quy tắc thú vị và một số điều kỳ lạ xung quanh chúng khi chúng tôi bắt

đầu tiên sử dụng chúng.

Điều quan trọng khác mà chúng tôi học về các kênh là chúng rất chặt chẽ, vì vậy rất

tài liệu hoặc thông điệp mà chúng tôi gửi qua một kênh phải luôn cùng loại tương ứng với cách chúng tôi

tạo kênh.

Vì vậy, chúng tôi hãy kiểm tra lại mã của chúng tôi.

Vì vậy, đây là chức năng chính của chúng tôi ở đây.

Chúng tôi sẽ tạo kênh đầu tiên của mình và sau đó chúng tôi sẽ sử dụng kênh đó để giao tiếp giữa các thói quen khác nhau của chúng tôi.

Vì vậy, ngay bên dưới phần của chúng tôi ngay tại đây, tôi sẽ tạo kênh mới của chúng tôi.

Tôi sẽ nói C viết tắt của kênh sẽ là Make Chan, và sau đó chúng tôi sẽ đặt loại dữ liệu mà chúng tôi muốn

truyền đạt qua kênh này.

Vì vậy, trong trường hợp này, chúng tôi sẽ nói rằng chúng tôi muốn giao tiếp thông qua kênh với chuỗi giá trị.

Vì vậy, đây là cách chúng tôi tạo một kênh hoàn toàn mới.

Chúng tôi đã tìm thấy từ khóa make before here.

Nó là một hàm hợp nhất sẽ tạo ra một giá trị bên ngoài kiểu đã chọn.

Vì vậy, chúng tôi tạo kênh này và chúng tôi chỉ định nó cho biến này hoặc bán C, không phải chuỗi.

Vì vậy, hiện tại C là kênh của chúng tôi và chúng tôi có thể tự động chuyển nó xung quanh ứng dụng của mình.

Bây giờ chúng tôi phải xử lý kênh này mặc dù chúng tôi sử dụng nó để liên lạc và tất cả những điều đặc biệt này.

Chúng tôi coi nó giống như bất kỳ giá trị nào khác trong ứng dụng của chúng tôi.

Vì vậy, nếu chúng tôi mong đợi quá trình truy cập được khởi chạy bởi dòng mã này ngay tại đây, thì cũng giống như if

chúng tôi mong đợi mã bên trong kiểm tra liên kết như chức năng thực tế này để có thể sử dụng kênh này, chúng

ta phải chuyển kênh vào chức năng đó.

Giá trị ngay tại đây là biến này.

US sử dụng tất cả các quy tắc xác định phạm vi tương tự mà chúng tôi sử dụng với các biến khác trong hoạt động.

Vì vậy, biến C này chỉ có thể truy cập được bên trong hàm chính này.

Chúng tôi không thể tham khảo một cách hữu ích trong quá trình kiểm tra liên kết.

Vì vậy, về cơ bản, họ cần đảm bảo rằng họ chuyển kênh này đến chức năng kiểm tra, sau đó liên kết kiểm tra

will beđược thực thi bên trong một quy trình hoạt động.

Chúng tôi sẽ có khả năng tiếp tục trở lại chức năng chính này.

Vì vậy, như một đối số thứ hai để kiểm tra liên kết, tôi sẽ chuyển đến kênh mà chúng tôi vừa tạo.

Vì vậy, các biến này nhìn giống nhau nên hiện tại chúng tôi chỉ chuyển thêm một đối số để kiểm tra liên kết.

Vì vậy, chúng tôi cần đảm bảo rằng chúng tôi sẽ sửa đổi danh sách đối số ở đây một cách hợp lý.

Vì vậy, giống như một đối số thứ hai, chúng ta sẽ mong đợi tìm thấy một biến mà chúng ta sẽ gọi là kênh C viết tắt.

Một lần nữa, nó thuộc loại kênh, được viết tắt là B đơn giản là Chan.

Và ngay cả ở đây, chúng tôi cũng phải khai báo loại dữ liệu mà chúng tôi muốn chia sẻ qua kênh.

Và vì vậy, giống như chúng tôi đã nói trước đây, chúng tôi mong đợi việc chia sẻ các giá trị của chuỗi kiểu.

Chúng tôi cũng phải tuyên bố điều đó ở đây.

Vì vậy, tôi sẽ nói C sẽ là một kênh.

Bạn có thể giao tiếp nó chỉ bằng ký tự chuỗi.

Vì vậy, hiện tại chúng tôi có chức năng kiểm tra quyền truy cập vào kênh và chúng tôi có thể sử dụng nó để giao dịch tiếp theo bất kỳ lúc nào

bất kỳ quy trình nào đang chạy chức năng kiểm tra liên kết và chức năng chính của chúng tôi.

Vì vậy, bây giờ câu hỏi nhanh chóng trở thành thành viên, à, chúng ta thực hiện giao tiếp tiếp theo bằng cách nào?

Làm cách nào để chúng tôi gửi tin nhắn giữa các chức năng chính của chúng tôi và các chức năng kiểm tra liên kết?

Vì vậy, đây là nơi chúng tôi sẽ giới thiệu một đoạn pháp luật mới trong GO.

Và đây thực sự là một đoạn pháp luật vui nhộn.

Tôi thích nó hơn bản thân mình.

Vì vậy, đây là những gì nó nhìn thấy như thế nào.

Đây là cách chúng tôi gửi dữ liệu qua các kênh.

Vì vậy, hãy nhớ rằng kênh của chúng tôi giống như một thiết bị nhắn tin hai chiều.

Chúng ta có thể coi nó giống như tin nhắn văn bản.

Vì vậy, sẽ luôn có một người đang gửi một tin nhắn và sau đó là một người khác hoặc một người thực sự

khác, tôi nên nói, đối với chương trình của chúng tôi, người đang nhận được thông báo đó.

Vì vậy, đối với chúng tôi, chúng tôi có thể muốn gửi dữ liệu từ chính quy trình cho tất cả hoạt động quy trình của mình hoặc chúng tôi

có thể muốn gửi dữ liệu từ quy trình chuyển hướng của chúng tôi và nhận dữ liệu trong quy trình chính.

Vì vậy, với suy nghĩ đó, chúng ta hãy xem xét các phần khác nhau của cú pháp.

Đầu tiên là cách chúng tôi gửi một số dữ liệu vào một kênh.

Vì vậy, nếu chúng tôi muốn gửi số năm vào kênh của mình, chúng tôi sẽ nói kênh và sau đó là một mũi tên nhỏ như vậy và

sau đó là giá trị mà chúng tôi muốn gửi vào đó.

Vì vậy, điều đó giống như nếu bạn rút điện thoại di động của mình ra ngay bây giờ và bạn mở ứng dụng Messenger của

mình, bạn nhập tin nhắn vào và bấm gửi.

Đó là những gì chúng tôi đang làm ngay tại đây.

Chúng tôi đang nhập một giá trị và gửi nó vào kênh.

Mặt khác, cuối cùng ai đó phải nhận giá trị đó để chúng tôi có thể nhận giá trị từ một

kênh.

Và bạn có thể nghĩ điều này giống như một người đã nhận được tin nhắn văn bản của bạn và rút điện thoại của bạn ra.

Điện thoại của họ sẽ mở khóa và đọc tin nhắn văn bản của bạn.

Điều đó được thực hiện bằng cách đặt một thông báo nhận biến vào một mũi tên và sau đó là tên của kênh.

Vì vậy, về cơ bản, chúng tôi đang nói rằng hãy mong đợi một giá trị qua kênh của chúng tôi.

Và khi nó chỉ định giá trị đó cho số lượng của tôi và sau đó là một nâng cấp nhỏ về mặt pháp lý, chúng ta không phải lúc này

ai cũng phải lấy một giá trị từ một kênh và phân bổ nó cho một biến.

Chúng tôi có thể dễ dàng nói rằng, Này, hãy xem kênh bất cứ khi nào có giá trị từ kênh đó.

Sử dụng nó làm đối số cho các dòng trong này để chúng có thể lấy các giá trị trực tiếp từ một kênh và chuyển đổi

chúng tôi cho các chức năng như thế này ngay tại đây.

Và trên thực tế, tôi nghĩ đây sẽ là cú pháp nhỏ đầu tiên mà chúng tôi thử.

Vì vậy, thay vì cố gắng nhận một thông báo vào một biến, tôi nghĩ rằng trước tiên chúng ta sẽ bắt đầu sử dụng

cách thử một thông báo trực tiếp.

Vì vậy, chúng tôi hãy thử điều này ngay bây giờ.

Giả sử rằng chúng tôi không muốn làm bất cứ điều gì với việc kiểm tra liên kết cho đến khi nó truy cập thành công một

thực thi một số URL.

Vì vậy, hãy giả sử sau khi chúng tôi đã truy cập một URL, hãy gửi một tin nhắn vào kênh của chúng tôi và sau đó chúng tôi sẽ nhận được nó qua bên trong

chức năng chính của chúng tôi ngay tại đây và chúng tôi sẽ chỉ thực hiện bất cứ điều gì chúng tôi gửi.

Vì vậy, tôi sẽ đưa kênh này gửi thông điệp đến các địa điểm cụ thể và chúng tôi sẽ nói rất ngắn về

lý do tại sao chúng ta chọn hai địa điểm cụ thể này.

Vì vậy, ngay bên dưới dòng lệnh trong chúng tôi, bên trong lệnh if ở đây, tôi sẽ nói rằng hãy

gửi một tin nhắn vào kênh của chúng tôi.

Vì vậy, chúng tôi nói vào kênh, gửi và sau đó là giá trị mà chúng tôi muốn gửi.

Vì vậy, tôi sẽ gửi một chuỗi thông báo rằng có thể không hoạt động, tôi nghĩ vậy.

Và sau đó, nếu chúng tôi nhận thấy rằng trang web đã thực sự hoạt động hoặc liên kết thực sự được nâng cấp, chúng tôi

will send a another message.

Vì vậy, ở bên dưới đây, bên dưới dòng lệnh khác, chúng tôi sẽ nói, vâng, nó cũng vậy.

Bây giờ hãy quay lại với các chức năng chính của chúng tôi, chúng tôi sẽ bổ sung một lệnh để nhận dữ liệu đó

from kênh.

Vì vậy, bên dưới câu lệnh dành cho chúng tôi, vì vậy ngay bên dưới vòng lặp để ngay tại đây, hãy vào ra.

Vì vậy, chúng tôi sẽ nói các dạng, dòng trong và sau đó chúng tôi sẽ nhận được một giá trị từ kênh.

Vì vậy, chúng tôi sẽ nói mũi tên như vậy và sau đó xem.

Vì vậy, cú pháp mà chúng tôi sử dụng trong cả hai trường hợp ở đây đều kèm theo chính xác những gì chúng tôi thấy phù hợp trong slide ngay tại đây.

Vì vậy, chúng tôi có thể đặt một giá trị, mũi tên và sau đó là kênh mà chúng tôi muốn gửi thông điệp.

Và mặt trái của điều đó cũng là một quy trình thực hiện khác, chúng ta có thể thêm vào một biến được cấp phép hoặc

một lời gọi hàm.

Vì vậy, trong trường hợp này, chúng tôi đang sử dụng một lời gọi hàm.

Chúng tôi đang nói rằng hãy nhận giá trị từ kênh này và ghi lại ngay lập tức.

Vì vậy, hãy chạy mã này và xem điều gì sẽ xảy ra.

Tôi sẽ lưu tệp.

Tôi phải đảm bảo rằng tôi không có bất kỳ hình vuông màu đỏ nào ở đây báo hiệu lỗi.

Có vẻ như tôi ổn, vì vậy tôi sẽ lại thiết bị cuối cùng của mình và tôi sẽ chạy lại chương trình

this browser.

Vì vậy, lần này chúng tôi xác thực được một lệnh cập nhật ở đây và sau đó có vẻ như chúng tôi đã thoát khỏi chương trình một

lần nữa.

Vì vậy, có vẻ như cái đó mà chúng tôi nhận được là Google. com.

Vì vậy, nó nói ở đây google. com đã lên và sau đó chúng tôi đã tìm thấy giao dịch tiếp theo của chúng tôi thông qua kênh, văn bản.

Đúng, bây giờ đã hết nếu tôi tiếp tục chạy cái này, phải không?

Có vẻ như mọi lần Google đều có vẻ hơi lạ khi chúng tôi chỉ nhận được một thông tin liên lạc

ở đây thay vì tất cả các thông tin liên lạc khác nhau.

Vì vậy, điều này thực sự cho chúng tôi tìm thấy một trong những điều thú vị thực sự lớn xung quanh các kênh.

Vì vậy, chúng tôi tạm dừng nhanh chóng.

Chúng ta sẽ quay trở lại trong phần tiếp theo và chúng ta sẽ nói về tính chính xác tại sao chúng ta

chỉ nhận được một thông báo qua kênh và sau đó thoát khỏi chương trình của mình.

Vì vậy, nhanh chóng nghỉ ngơi.

Chúng tôi sẽ quay lại chỉ sau một giây.