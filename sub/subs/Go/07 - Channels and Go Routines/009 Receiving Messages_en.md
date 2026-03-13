# 009 Nhận tin nhắn vi

---

Người hướng dẫn: Trong video cuối cùng,

chúng tôi biết được rằng việc nhận tin nhắn qua một kênh

là một hoạt động chặn.

Bây giờ chúng ta sẽ cấu trúc lại khối này

của dòng lệnh in ngay tại đây

vào một cái gì đó hợp lý hơn một chút.

Vì vậy, trên thực tế, chúng ta sẽ không bao giờ thực sự muốn

để thấy một loạt người xếp hàng nhận cuộc gọi tin nhắn

như thế này ngay tại đây, vì vậy chúng ta sẽ thay thế tất cả những thứ này

thay vào đó bằng một vòng lặp for đơn giản.

Vì vậy tôi sẽ xóa cái này,

và thay vào đó chúng ta sẽ viết một vòng lặp for

cái đó sẽ gọi định dạng đó là hàm in dấu chấm

và nhận được giá trị qua kênh của chúng tôi

một số lần bằng số chuỗi

mà chúng ta có trong phần này ngay tại đây.

Vì vậy, hãy bắt đầu với nó.

Bây giờ, chúng ta chưa bao giờ viết vòng lặp for trước đây

không sử dụng trình trợ giúp phạm vi,

và trong trường hợp này, tôi không muốn sử dụng trợ giúp phạm vi,

Tôi muốn lặp lại từ số 0

lên tới một trừ đi số chuỗi

đó là bên trong lát cắt.

Vì vậy, để thực hiện một vòng lặp for đếm lên thông qua một số số nguyên,

chúng ta sẽ sử dụng một cú pháp rất quen thuộc

mà bạn có thể đã quen nhìn thấy, chẳng hạn như,

JavaScript hoặc Java hoặc C++.

Về cơ bản, đó là vòng lặp for lấy cảm hứng từ C.

Vì vậy chúng ta sẽ nói rằng tôi bắt đầu từ con số 0,

và sau đó đếm đến I nhỏ hơn độ dài của các liên kết,

và sau đó chúng tôi sẽ tăng thêm một đơn vị mỗi lần.

Được rồi, về cơ bản hãy bắt đầu từ con số 0,

đếm đến một trừ đi độ dài của các liên kết ở đây,

và sau đó chúng ta sẽ nói điều đó,

cho mỗi lần lặp qua vòng lặp này,

chúng tôi sẽ định dạng dòng in dấu chấm

và nhận được giá trị từ kênh C của chúng tôi, như vậy.

Bây giờ, trước khi chúng ta chạy đoạn mã này,

Tôi muốn bạn hình dung điều gì đang xảy ra

với vòng lặp for ngay tại đây.

Lần đầu tiên vòng lặp for được thực thi,

chúng ta sẽ bắt đầu dòng lệnh in này ngay tại đây.

Bây giờ, dòng in, hay cụ thể là,

nhận được một giá trị từ kênh,

thực sự sẽ chặn vòng lặp for tiếp tục.

Vì vậy ngay khi chúng tôi nhận được tin nhắn qua kênh,

toàn bộ dòng mã này ở đây

thực sự cuối cùng sẽ thực thi,

và sau đó chúng ta sẽ tiếp tục đến lần lặp tiếp theo

thông qua vòng lặp for.

Vì vậy toàn bộ vòng lặp không được thực hiện ngay lập tức

hoặc tất cả cùng một lúc.

Chúng tôi vẫn đang chờ tin nhắn

đi qua kênh trước khi chúng ta tiếp tục

tới lần lặp tiếp theo của vòng lặp.

Vì vậy hãy lưu tập tin này

và sau đó kiểm tra điều này bằng dòng lệnh.

Được rồi, bây giờ chúng ta chỉ đang lắng nghe

cho số lượng tin nhắn bằng một

hoặc số phần tử bên trong lát trừ đi một.

Và vì vậy về cơ bản chúng tôi đợi năm tin nhắn

đi qua thì không còn mã nào khác để thực thi

bên trong quy trình chính của chúng tôi và chương trình của chúng tôi sẽ thoát hoàn toàn.

Bây giờ, điều này có vẻ giống như một cách tiếp cận hackish

ngay tại đây để xem độ dài của các liên kết,

nhưng thành thật mà nói, có rất nhiều thứ bạn sẽ thấy trong Go

đôi khi có vẻ hơi hackish một chút,

nhưng thực ra, tôi sẽ không gọi điều này là hackish,

Tôi sẽ gọi điều này là đơn giản

và dễ hiểu.

Bạn có thể nhìn vào cái này,

và nó không thực sự sử dụng bất kỳ trợ giúp ưa thích nào.

Tất cả những gì bạn thực sự phải hiểu

đó là giá trị đi qua C là lệnh gọi chặn,

và miễn là bạn hiểu điều đó,

thì bạn có thể sẽ nhanh chóng nhận ra điều đó,

này, chúng ta chỉ đang kết hợp những thứ này lại với nhau thôi

để đợi mọi quy trình Go phát ra một tin nhắn,

và sau đó chúng ta sẽ thoát hoàn toàn khỏi chương trình này.

Được rồi, vậy vẫn còn rất nhiều cách khác

tương tác với một kênh, vì vậy chúng ta hãy tạm nghỉ.

Chúng ta sẽ quay lại ở phần tiếp theo

và chúng ta sẽ thêm vào

một hoặc hai yêu cầu khác đối với chương trình của chúng tôi,

và chúng ta sẽ xem làm thế nào chúng ta có thể viết nó

và đặt tất cả những thứ đó lại với nhau.

Vì vậy, hãy nghỉ ngơi nhanh chóng và chúng ta sẽ tiếp tục khám phá các kênh

trong phần tiếp theo.