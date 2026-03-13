# 011 Cú pháp vòng lặp thay thế vi

---

Người hướng dẫn: Trong video cuối cùng,

chúng tôi đã thực hiện một chút thay đổi đối với mã của mình

để đảm bảo rằng chúng tôi cố gắng tìm nạp lại một liên kết

sau khi nó được lấy về,

thành công hoặc có lỗi.

Bây giờ vào thời điểm này,

chúng ta chỉ còn lại vòng lặp for ở đây

điều đó dường như cứ tiếp diễn mãi mãi.

Bây giờ bạn và tôi đều biết rằng vòng lặp for

sẽ không quay bánh xe của nó

như một tỷ lần mỗi giây.

Nó vẫn sẽ chạy rất nhanh

nhưng mỗi lần chúng ta chờ đợi một tin nhắn

được nhận ngay tại đây,

chúng ta sẽ có chút tạm dừng nhỏ đó

cho đến khi yêu cầu tiếp theo thực sự được hoàn thành.

Vì vậy, mặc dù nó trông giống như vòng lặp for ngay tại đây

sẽ chạy qua một dòng mã này

một tỷ lần mỗi giây,

nó không thực sự nhanh như vậy.

Tuy nhiên, có một vấn đề nhỏ với vòng lặp for này,

và tôi có thể nói rằng đây hoàn toàn là vấn đề về phong cách.

Vì vậy chúng ta sẽ thực hiện một chút thay đổi cho điều này

và đó chỉ là do phong cách mã

mà chúng ta đang xem xét ở đây.

Vì vậy, bạn có thể tưởng tượng rất dễ dàng

rằng nếu chúng ta có nhiều logic khác

bên trong vòng lặp for ngay tại đây,

nó có thể thực sự là một thử thách

cho một số kỹ sư khác

đến và xem mã này

và có sự hiểu biết rõ ràng

chính xác vòng lặp for này đang làm gì.

Và ý tôi là nó sẽ khá khó khăn

để một kỹ sư khác săn lùng

đoạn mã nhỏ duy nhất ở đây có nội dung là,

này, chúng ta sẽ đợi một giá trị

được nhận trên kênh này.

Vì nó khá là thử thách

để một kỹ sư khác đến hiện trường ở đây,

xem cái này cho vòng lặp,

và tìm kiếm tuyên bố chặn này ngay tại đây,

Go cung cấp một cú pháp thay thế một chút

để viết một vòng lặp rất giống nhau.

Vì vậy chúng ta sẽ viết ra cú pháp thay thế

và chúng ta sẽ nói về chính xác những gì đang xảy ra.

Vì vậy, bên trong phần khai báo vòng lặp for, ngay ở đây,

chúng ta sẽ thay đổi điều này thành l := range c.

Và sau đó thay vì đặt mũi tên C vào bên trong đây,

chúng ta sẽ thay thế nó bằng l, l là viết tắt của link.

Bây giờ đó là toàn bộ công cụ tái cấu trúc ngay tại đó.

Mã này mà chúng tôi đang xem xét ngay bây giờ

hoàn toàn tương đương với những gì chúng ta vừa thấy trên màn hình

hai giây trước.

Vì vậy, chúng ta đã thấy cú pháp phạm vi nhiều lần

và chúng tôi luôn thấy phạm vi được sử dụng để lặp lại

hơn như một lát cắt, một lát cắt các phần tử.

Chúng tôi đã nói rằng khi chúng tôi sử dụng từ khóa phạm vi trên một lát cắt,

chúng tôi lấy mọi phần tử ra khỏi lát cắt,

gán nó cho một số biến,

và sau đó chúng ta có quyền truy cập vào bên trong vòng lặp for.

Và do đó, việc sử dụng một phạm vi với một kênh hoạt động rất giống nhau.

Với mã này ngay tại đây,

chúng tôi đang nói hãy đợi kênh trả về một số giá trị.

Sau khi kênh đã trả về một số giá trị,

gán nó cho biến này l,

l trong trường hợp này là viết tắt của link,

sau đó chạy phần thân của vòng lặp for.

Và bên trong vòng lặp for, chúng tôi ngay lập tức sinh ra

một liên kết kiểm tra cuộc gọi định kỳ Go mới,

chuyển qua liên kết mà chúng tôi vừa nhận được trong kênh,

và sau đó chuyển vào kênh làm đối số thứ hai.

Vì vậy, điều này một lần nữa hoàn toàn tương đương với cú pháp

chúng ta vừa có, nhưng nó rõ ràng hơn nhiều

cho những người khác những người

những người đang đi bộ trên hiện trường

hoặc xem qua mã của bạn,

dễ dàng hơn nhiều để họ tìm ra

chính xác mục đích của vòng lặp này là gì.

Vì thế sẽ dễ dàng hơn rất nhiều cho họ khi nhìn vào điều này và nói,

được rồi, tôi hiểu chúng ta sẽ bước qua vòng lặp for.

Chúng ta sẽ chạy qua vòng lặp for

mỗi lần kênh phát ra một giá trị nào đó?

Vì vậy, hãy lưu tập tin này và chạy lại

chỉ để đảm bảo rằng mã chúng ta có bây giờ

là hoàn toàn tương đương.

Vì vậy, quay lại thiết bị đầu cuối của chúng ta, chúng ta sẽ chạy, chạy chính, chạy lại,

và chúng tôi vẫn nhận được thư rác cũ lớn này

của tất cả những thông điệp khác nhau này.

Bây giờ, như tôi đã nói ở cuối video trước,

nó có lẽ không hoàn toàn phù hợp

liên tục gửi spam các trang web khác nhau này

càng nhanh càng tốt.

Vì vậy tôi vẫn muốn thêm vào một tính năng bổ sung ở đây

và tôi muốn nói rằng chúng ta nên tạm dừng một chút

giữa mỗi lần tìm nạp.

Vậy chúng ta hãy nghỉ ngơi nhanh thôi,

quay lại và chúng ta sẽ tìm ra

chúng ta sẽ sửa đổi mã của mình như thế nào

để tích hợp khoảng dừng nhỏ đó giữa mỗi lệnh gọi liên kết kiểm tra.

Được rồi, vậy hãy nghỉ nhanh và tôi sẽ gặp bạn sau một phút nữa.