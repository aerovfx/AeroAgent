# 003 Kiểm tra liên kết nối tiếp vi

---

Trong phần cuối cùng, chúng ta đã cùng thực hiện lần đầu tiên của trạng thái kiểm tra chương trình của chúng ta.

Nhưng nếu chúng ta xem thử kỹ năng đầu ra của chương trình của mình, khi chúng ta chạy nó ở thiết bị đầu cuối, chúng ta sẽ

đã tìm thấy một số hành động khá thú vị.

Vì vậy, tôi sẽ chạy chương trình và khi tôi thực hiện, bạn sẽ thấy rằng tôi có

một chút tốc độ, sau đó là bản in cho Google, sau đó là tốc độ và sau đó là tốc độ của Facebook, độ tĩnh, tĩnh, độ

trà tràn. và như thế.

Và do đó, có vẻ như có một chút chậm rãi đặc biệt giữa việc tìm kiếm từng địa chỉ này ngay lập tức

tại đây.

Vì vậy, chúng tôi hãy xem một sơ đồ và cố gắng hình dung chính xác cách mã hóa của chúng tôi đang thực hiện điều này

ngay bây giờ.

Bây giờ, đây là một loại sơ đồ điên rồ, nhưng chúng tôi sẽ xem xét nó từng bước một.

Vì vậy, ở phía bên trái ở đây, chúng tôi có một danh sách tất cả các địa chỉ khác nhau của chúng tôi hoặc tất cả

tất cả các URL khác nhau.

Vì vậy, đây là những gì thực sự xảy ra đằng sau hậu trường.

Khi tôi chạy chương trình, chúng tôi sẽ nhận được liên kết đầu tiên từ các phần của chúng tôi.

Chúng tôi yêu cầu nó.

Vì vậy, đây là một yêu cầu gửi đến Google. com và sau đó chúng tôi ngồi xung quanh và chờ phản hồi

hồi phục trở lại.

Và như vậy, dòng mã bên trong chức năng kiểm tra liên kết chức năng của chúng tôi ngay tại đây, dòng này ngay lập tức

tại đây, bất cứ khi nào chúng tôi thực hiện yêu cầu liên kết, chúng tôi đang ngồi và chờ yêu cầu hoàn thành.

Vì vậy, chúng tôi thực hiện yêu cầu.

Chúng tôi thường ngồi và xoay ngón tay của mình và chúng tôi chờ phản hồi trở lại.

Và do đó, chúng tôi sẽ không tiếp tục phần còn lại của chức năng của mình cho đến khi chúng tôi nhận được phản hồi từ chức năng

điều này ngay tại đây.

Vì vậy, điều đó có nghĩa là mỗi khi chúng tôi đưa ra yêu cầu, chúng tôi ngồi xung quanh và chờ phản hồi

hồi phục trở lại.

Sau đó, chúng tôi nhận được liên kết tiếp theo, đưa ra yêu cầu của mình, ngồi xung quanh và chờ phản hồi của chúng tôi

quay lại và sau đó lặp đi lặp lại nhiều lần.

Và vì vậy, chương trình cơ bản của chúng tôi đang chạy theo một dòng tự động hoặc dòng tiếp theo ngay bây giờ.

Giữa mỗi lần tìm, chúng tôi chỉ ngồi xung quanh và chờ đợi một khoảng thời gian.

Bây giờ tôi muốn bạn nghĩ về chương trình mà chúng tôi đang viết ngay bây giờ và mục tiêu của bạn

nó cũng như lý do tại sao điều đó có thể là một vấn đề nhỏ nếu chúng tôi kết thúc với rất nhiều liên kết khác nhau trong

phần này ngay tại đây, như , giả sử, hàng liên kết khác nhau.

Điều đó có nghĩa là chúng tôi chỉ có thể kiểm tra bất kỳ liên kết nào tốt nhất một lần mỗi giờ hoặc tương tự như vậy, bởi

bởi vì chúng tôi chỉ đưa ra một yêu cầu tại một thời điểm.

Và để kiểm tra lại một liên kết khác, chúng tôi phải chạy lại toàn bộ danh sách để quay lại

đầu trang.

Vì vậy, tôi sẽ lưu ý rằng có lẽ đây không phải là cách tiếp cận tốt nhất để kết hợp chương trình của chúng tôi

lại với nhau ngay bây giờ, đặc biệt là khi chúng ta có thể muốn kiểm tra Google. com hoặc Golang dot org nhiều lần liên tiếp

Rất nhanh chóng, vì chúng tôi đã hoàn thành thành công Amazon và lặp lại với Google rồi lướt qua

Facebook rồi đến StackOverflow và cuối cùng quay lại googling dot org một lần nữa.

Vì vậy, tôi sẽ đề xuất một cách tiếp cận khác ở đây.

Tôi sẽ gợi ý rằng chúng tôi có thể muốn thực hiện một bài hát tiếp theo cho chương trình này.

Có thể thay đổi từng yêu cầu trong Serial, có thể chúng ta nên lấy từng URL trong phần cắt của mình, đưa ra yêu cầu

Yêu cầu từng URL và sau đó bất cứ khi nào có bất kỳ phản hồi yêu cầu nào, chúng tôi sẽ tham gia

ra trạng thái.

Và vì vậy, chìa khóa của quy trình này ngay tại đây là chúng tôi sẽ cố gắng thực hiện mọi yêu cầu ngay lập tức,

như ngay sau khi chương trình của chúng tôi khởi động, thay vì yêu cầu trước khi kết thúc và nhận lại

Phản hồi và phát hiện trạng thái .

Và vì vậy đây là lúc có ý tưởng về các quy trình và kênh sẽ bắt đầu phát huy tác dụng.

Vì vậy, chúng tôi tạm dừng một chút, quay lại trong phần tiếp theo và

chúng tôi sẽ nói về cách chúng tôi sẽ sử dụng các quy trình để chạy bài hát từng yêu cầu này.

Vì vậy, hãy nhanh chóng nghỉ ngơi và tôi sẽ gặp lại bạn sau một phút.