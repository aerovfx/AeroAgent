# 011 Cú pháp vòng lặp thay thế vi

---

Cuối cùng, trong video, chúng tôi đã thực hiện một chút thay đổi đối với mã của mình để đảm bảo rằng chúng tôi

cố gắng tải lại một liên kết sau khi nó được tìm thấy thành công hoặc bị lỗi.

Bây giờ, tại thời điểm này, chúng tôi vẫn lặp lại vòng lặp cho this ngay tại đây và chỉ chạy mãi mãi.

Bây giờ, bạn và tôi đều biết rằng vòng lặp for sẽ không quay các bánh xe của nó như một tỷ lệ lần

mỗi giây.

Nó vẫn sẽ chạy rất nhanh.

Nhưng mỗi khi chúng tôi mong đợi nhận được tin nhắn ngay tại đây, chúng tôi sẽ nhận được một chút tạm dừng

nhỏ đó cho đến khi yêu cầu tiếp theo được thực hiện thành công.

Vì vậy, mặc dù có vẻ giống như vòng lặp cho việc này sẽ chạy qua một mã duy nhất

tốc độ thấp nhất mỗi giây, nhưng nó không thực sự nhanh như vậy.

Tuy nhiên, có một vấn đề nhỏ với vòng lặp này và tôi muốn nói rằng đây hoàn toàn là một

liên hệ quan tâm về phong cách.

Vì vậy, chúng tôi sẽ thực hiện một chút thay đổi đối với thứ này và đó chỉ là loại mã mà chúng tôi

đang xem xét ngay tại đây.

Vì vậy, bạn có thể tưởng tượng rất dễ dàng rằng nếu chúng ta có nhiều logic khác trong vòng lặp cho điều này

ngay tại đây, sẽ có nhiều kỹ năng khác đến xem mã này và hiểu rõ ràng về điều này

có thể thực thi một công thức. đang thực hiện vòng lặp.

Và do đó, tôi muốn nói rằng sẽ là một thử thách đối với một kỹ sư khác khi tìm kiếm một đoạn mã

nhỏ duy nhất ngay tại đây có nội dung là, chúng tôi sẽ mong đợi một giá trị nhận được trên

kênh này.

Vì vậy, bởi vì nó là một công thức hoàn thiện so với một kỹ sư khác khi đi trên trường hiện tại ở đây, hãy xem

loop for this và tìm kiếm lệnh chặn này ngay tại đây.

Go cung cấp một cú pháp thay thế để viết một vòng lặp rất giống nhau.

Vì vậy, chúng tôi sẽ viết cú pháp thay thế và chúng tôi sẽ nói về chính xác những gì đang xảy ra.

Vì vậy, bên trong khai báo vòng lặp ngay trên đây, chúng tôi sẽ thay đổi điều này để nói rằng L dấu hai chấm bằng phạm tội

vi C và sau đó thay thế mũi tên mũi tên này bên trong đây, chúng tôi sẽ thay thế nó bằng cách sử dụng

l l viết tắt của liên kết.

Bây giờ, đó là toàn bộ cấu trúc lại ngay lúc đó.

Đoạn mã mà chúng tôi đang xem ngay bây giờ hoàn toàn tương thích với những gì chúng tôi có trên

màn hình 2 giây trước.

Vì vậy, chúng tôi đã nhiều lần tìm thấy cú pháp phạm pháp này và chúng tôi luôn thấy phạm vi được

sử dụng để lặp lại như một lát cắt, một phần tử.

Chúng tôi đã nói rằng khi chúng tôi sử dụng các từ khóa có phạm vi trên một lát cắt, chúng tôi sẽ lấy tất cả các phần tử ra khỏi phần cắt này, chỉ định nó cho một

một số biến và sau đó chúng tôi có quyền truy cập vào phần tử đó trong vòng lặp.

Và do đó, việc sử dụng một phạm vi với một kênh hoạt động rất giống với mã này ngay tại đây, chúng tôi đang

Nói rằng hãy đợi kênh trả về một số giá trị sau khi kênh đã trả về một số giá trị, hãy chỉ định nó cho biến này.

Trong trường hợp này, L l là một liên kết tắt, sau đó chạy phần thân của vòng lặp cho và bên trong vòng lặp, chúng tôi ngay lập tức

thiết lập tạo ra một liên kết kiểm tra quy trình gọi mới chuyển đến liên kết mà chúng tôi vừa nhận được

trong kênh và sau đó chuyển vào kênh như đối số thứ hai.

Vì vậy, điều này một lần nữa hoàn toàn tương đương với cú pháp mà chúng ta vừa có, nhưng rõ ràng hơn rất nhiều

đối với những người khác đang đi dạo hoặc xem qua mã của bạn.

Họ dễ dàng hơn nhiều để tìm ra mục tiêu chính xác của vòng lặp cho việc này là gì, vì vậy họ sẽ dễ dàng

hơn rất nhiều khi nhìn vào điều này và nói, đã được rồi, tôi hiểu rằng chúng ta sẽ vượt qua vòng lặp for.

Chúng tôi sẽ chạy vòng lặp cho mỗi kênh phát ra giá trị nào?

Vì vậy, hãy lưu tệp này và chạy lại chỉ để đảm bảo rằng mã chúng hiện có đã hoàn toàn tương thích.

Vì vậy, chúng tôi sẽ quay lại thiết bị đầu cuối của mình để chạy, chạy, chạy lại.

Và chúng tôi vẫn nhận được thư rác lớn này trong số tất cả các thư khác nhau.

Bây giờ, như tôi đã nói ở video cuối trước, có thể không hoàn toàn hợp lý nếu bạn gửi đi gửi

lại các trang web khác nhau một cách nhanh nhất có thể.

Vì vậy, tôi vẫn muốn bổ sung thêm một tính năng bổ sung ở đây và tôi muốn nói rằng chúng

nên có một đoạn tạm dừng ngắn giữa mỗi lần tải.

Vì vậy, chúng ta hãy nghỉ ngơi nhanh chóng, quay lại và chúng ta sẽ tìm ra

cách chúng tôi sẽ sửa đổi mã của mình để hợp lý các khoảng dừng giữa mỗi lệnh kiểm tra liên kết cuộc gọi.

Vì vậy, hãy nhanh chóng nghỉ ngơi và tôi sẽ gặp lại bạn chỉ sau một phút.