# 003 Kiểm tra liên kết nối tiếp vi

---

Giáo viên: Ở phần cuối,

chúng tôi kết hợp lần lặp đầu tiên

chương trình kiểm tra trạng thái của chúng tôi.

Nhưng nếu chúng ta xem xét kỹ kết quả của chương trình

khi chúng tôi chạy nó ở thiết bị đầu cuối,

chúng ta sẽ nhận thấy một số hành vi khá thú vị.

Vì vậy tôi sẽ chạy chương trình và khi tôi làm vậy

bạn sẽ nhận thấy rằng tôi hơi chậm trễ một chút,

sau đó là bản in cho Google và sau đó là sự chậm trễ,

và sau đó là Facebook, độ trễ, tràn tĩnh, độ trễ, v.v.

Và vì vậy có vẻ như có một chút

có độ trễ rõ rệt

giữa việc tìm nạp từng địa chỉ này ngay tại đây.

Vì vậy chúng ta hãy nhìn vào một sơ đồ,

và cố gắng tạo ra một bức tranh chính xác

mã của chúng tôi hiện đang được thực thi như thế nào.

Được rồi, đây là một sơ đồ điên rồ,

nhưng chúng ta sẽ thực hiện nó từng bước một.

Vậy ở vế trái ở đây,

chúng tôi có danh sách tất cả các địa chỉ khác nhau,

hoặc tất cả các URL khác nhau.

Vì vậy, đây là những gì thực sự xảy ra đằng sau hậu trường

khi chương trình của chúng tôi chạy.

Chúng tôi lấy liên kết đầu tiên từ lát cắt của chúng tôi,

chúng tôi đưa ra yêu cầu cho nó.

Vì vậy, đây là một yêu cầu được gửi đến google.com,

và sau đó chúng tôi ngồi xung quanh và chờ đợi phản hồi.

Và dòng mã bên trong của chúng ta

chức năng checkLink ngay tại đây, dòng này ngay tại đây,

bất cứ khi nào chúng tôi yêu cầu một liên kết, chúng tôi đang ngồi xung quanh

và chờ đợi yêu cầu đó hoàn thành.

Vì vậy chúng tôi đưa ra yêu cầu,

chúng tôi kiểu như ngồi và vặn ngón tay cái của mình,

và chúng tôi chờ đợi phản hồi trở lại.

Và vì vậy chúng tôi không tiến bộ

thông qua phần còn lại của chức năng của chúng tôi

cho đến khi chúng tôi nhận được phản hồi từ chức năng này ngay tại đây.

Vậy điều đó có nghĩa là gì

mỗi lần chúng tôi đưa ra yêu cầu,

chúng tôi ngồi xung quanh và chờ phản hồi trở lại.

Sau đó chúng tôi lấy liên kết tiếp theo, đưa ra yêu cầu của mình,

ngồi xung quanh và chờ phản hồi của chúng tôi quay lại,

rồi lặp đi lặp lại nhiều lần.

Và về cơ bản chương trình của chúng tôi đang chạy

trong một dòng chảy rất tuần tự hoặc kiểu nối tiếp ngay bây giờ.

Ở giữa mỗi lần tìm nạp, chúng tôi chỉ ngồi xung quanh

và chờ đợi một khoảng thời gian.

Bây giờ tôi muốn bạn suy nghĩ

về chương trình chúng tôi đang viết bây giờ

và mục đích của nó, và tại sao điều đó có thể

có chút vấn đề.

Nếu cuối cùng chúng ta có rất nhiều liên kết khác nhau

bên trong lát cắt này ngay tại đây,

chẳng hạn như có hàng ngàn liên kết khác nhau,

điều đó có nghĩa là chúng ta chỉ có thể kiểm tra

bất kỳ liên kết cụ thể nào như một lần mỗi giờ hoặc tương tự,

bởi vì chúng tôi chỉ đưa ra một yêu cầu tại một thời điểm.

Và để kiểm tra lại một liên kết khác,

chúng ta phải xem lại toàn bộ danh sách

để trở lại đỉnh cao.

Vì vậy tôi sẽ gợi ý rằng có lẽ

đây không phải là cách tiếp cận tốt nhất

vì đã kết hợp chương trình của chúng tôi ngay bây giờ,

đặc biệt là xem xét rằng chúng tôi có thể muốn

kiểm tra google.com hoặc golang.org

nhiều lần liên tiếp rất nhanh,

thay vì đợi chúng tôi hoàn thành Amazon

và sau đó lặp lại với Google

sau đó truy cập Facebook và sau đó truy cập stackoverflow,

và cuối cùng quay lại golang.org lần nữa.

Vì vậy, tôi sẽ đề xuất một cách tiếp cận hơi khác ở đây.

Tôi sẽ gợi ý rằng có lẽ chúng ta muốn lấy

một cách tiếp cận song song với chương trình này.

Có lẽ thay vì chạy từng yêu cầu nối tiếp,

có lẽ chúng ta nên đưa từng URL vào trong lát cắt của mình,

đưa ra yêu cầu cho mỗi người,

và sau đó bất cứ khi nào có bất kỳ phản hồi yêu cầu nào quay trở lại,

sau đó chúng tôi sẽ in ra trạng thái.

Và chìa khóa trong dòng chảy này nằm ở ngay đây

là chúng tôi sẽ cố gắng thực hiện mọi yêu cầu

ngay lập tức, chẳng hạn như ngay khi chương trình của chúng tôi bắt đầu,

thay vì đợi yêu cầu trước đó kết thúc

và nhận được phản hồi và in ra trạng thái.

Và đây là nơi nảy sinh ý tưởng về Goroutines và Kênh

sắp bắt đầu phát huy tác dụng.

Vì vậy, hãy tạm dừng nhanh chóng, quay lại phần tiếp theo,

và chúng ta sẽ nói về cách chúng ta sẽ sử dụng

của Goroutine để chạy song song từng yêu cầu này.

Vì vậy, hãy nghỉ ngơi nhanh và tôi sẽ gặp bạn sau một phút.