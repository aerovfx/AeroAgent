# 009 Nhận tin nhắn vi

---

Trong video cuối cùng, chúng tôi đã biết rằng việc nhận tin nhắn qua kênh là một hoạt động ngăn chặn.

Bây giờ chúng ta sẽ cấu trúc lại dòng lệnh khối ở đây ngay tại đây thành một điều hợp lý

hơn một chút.

Vì vậy, trong thực tế, chúng tôi sẽ không bao giờ thực sự muốn tìm thấy một loạt cuộc gọi nhận tin nhắn xếp hàng như thế

điều này ngay tại đây.

Vì vậy, chúng tôi sẽ thay thế tất cả điều này bằng một vòng lặp cho đơn giản.

Vì vậy, tôi sẽ xóa cái này.

Và thay vào đó, chúng tôi sẽ viết một vòng lặp để gọi định dạng đó, trong hàm và

nhận được giá trị trên kênh của chúng tôi nhiều lần bằng cách sử dụng số chuỗi mà chúng tôi có trong phần của chúng tôi

ngay tại đây.

Vì vậy, chúng ta hãy bắt đầu ngay bây giờ.

Chúng tôi chưa bao giờ viết vòng lặp cho trước đó không sử dụng trợ giúp phạm vi và trong trường hợp này, tôi không muốn sử dụng

vi phạm hỗ trợ.

Tôi chỉ muốn lặp lại từ 0 đến một trừ đi số bên trong phần cắt này.

Vì vậy, để thực hiện một vòng lặp để đếm một số nguyên, chúng ta sẽ sử dụng một cú pháp

pháp rất quen thuộc mà bạn có thể đã quen với JavaScript hoặc Java hoặc C ++.

Về cơ bản, nó là một cảm hứng từ vòng lặp cho.

Vì vậy, chúng tôi sẽ nói bốn, tôi bắt đầu từ 0 và sau đó đếm đến tôi ít hơn chiều dài của các liên kết và sau đó chúng

tôi sẽ tăng cường từng liên kết một.

Vì vậy, về cơ bản bắt đầu từ 0, hãy đếm một trừ đi độ dài của các liên kết ngay tại đây.

Và sau đó, chúng tôi sẽ nói rằng đối với mỗi lần lặp qua vòng lặp này, chúng tôi sẽ định dạng các dòng trong và nhận một

giá trị từ kênh C Like của chúng tôi.

Vì vậy, ngay bây giờ trước khi chúng tôi chạy mã này, tôi muốn bạn xem những gì đang xảy ra với vòng lặp cho việc này

ngay tại đây.

Lần đầu tiên vòng lặp được thực hiện, chúng tôi sẽ thực hiện dòng lệnh này ngay tại đây.

Bây giờ, line in hoặc cụ có thể nhận một giá trị bên ngoài kênh sẽ thực sự chặn

vòng lặp để tiếp tục.

Vì vậy, ngay sau khi chúng tôi nhận được tin nhắn qua kênh, toàn bộ dòng mã ngay tại đây

cuối cùng sẽ thực hiện việc này.

Và sau đó chúng ta sẽ tiếp tục bước tiếp theo vòng lặp thông qua for.

Vì vậy, toàn bộ vòng lặp không được thực hiện ngay lập tức hoặc giống như tất cả cùng một lúc.

Chúng tôi vẫn đang chờ thông báo đến qua kênh trước khi chúng tôi tiếp tục bước tiếp theo của

vòng lặp.

Vì vậy, hãy lưu tệp này và sau đó kiểm tra điều này bằng lệnh dòng.

Được chứ.

Vì vậy, hiện tại chúng tôi chỉ đang nghe một số thông báo bằng một hoặc số phần tử bên trong lát

trừ đi một.

Và vì vậy, về cơ bản chúng tôi chờ năm thông báo được gửi đến.

Sau đó, không có mã nào khác được thực thi trong quy trình chính của chúng tôi và chương trình của chúng tôi sẽ thoát hoàn toàn.

Bây giờ, điều này có vẻ giống như một loại phương pháp hack ish ngay tại đây để chỉ xem xét độ dài của các liên kết.

Nhưng thành thật mà nói, nhiều thứ mà bạn sẽ xem và đi đôi khi cảm thấy hơi bị hack, nhưng sự thật thì

tôi không thực sự gọi đây là hack ish.

Tôi sẽ gọi điều này đơn giản và dễ hiểu.

Bạn có thể xem điều này và nó thực sự không sử dụng bất kỳ trợ giúp nào của trình hỗ trợ.

Tất cả những gì bạn thực sự cần phải hiểu đều là một giá trị từ C là một lệnh gọi và miễn phí mà bạn hiểu

điều đó, thì có lẽ bạn sẽ nhanh chóng nhận được điều đó, điều này, chúng ta chỉ đang

kết hợp điều này lại với nhau để mong đợi mọi quy trình thực hiện một thông báo và sau đó chúng tôi sẽ thoát hoàn toàn

khỏi chương trình này.

Vì vậy, vẫn còn rất nhiều cách khác để tương tác với một kênh.

Vì vậy, chúng ta hãy thoải mái nghỉ ngơi.

Chúng tôi sẽ quay lại phần tiếp theo và chúng tôi sẽ bổ sung một hoặc hai yêu cầu khác vào chương trình của

mình và chúng tôi sẽ chỉ xem cách chúng tôi có thể viết điều đó và kết hợp tất cả những thứ đó lại với nhau.

Vì vậy, hãy nhanh chóng nghỉ ngơi và chúng tôi sẽ tiếp tục khám phá các kênh trong phần tiếp theo.