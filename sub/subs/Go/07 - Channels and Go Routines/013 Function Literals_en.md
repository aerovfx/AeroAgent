# 013 Hàm chữ vi

---

Giáo viên: Ở phần cuối,

chúng tôi đã thêm vào trong tuyên bố về Giấc ngủ

theo thói quen chính của chúng tôi, nhưng sau đó rất nhanh chóng nhận ra

rằng nó sẽ khiến tất cả các tin nhắn đang đến

thông qua kênh của chúng tôi để được điều tiết.

Vì vậy, chúng tôi sẽ chỉ nhận được một tin nhắn

tốt nhất cứ năm giây một lần hoặc lâu hơn.

Vì vậy chúng ta cần tìm ra một nơi thông minh hơn

để đưa ra tuyên bố về Giấc ngủ nhỏ này.

Bây giờ, giải pháp rất rõ ràng ở đây,

có thể bạn đang nghĩ, được thôi,

tốt, chúng ta hãy lấy câu lệnh Ngủ.

Vì thế tôi sẽ cắt nó ngay từ đó,

và thay vào đó chúng ta sẽ đặt nó vào hàm của mình.

Vì vậy bây giờ chúng ta đang nói rằng khi chương trình của chúng ta khởi động lần đầu tiên,

nó sẽ khởi động tất cả các goroutine checkLink ban đầu

và sau đó chúng ta sẽ đợi năm giây

và sau đó bắt đầu bắt đầu quá trình tìm nạp.

Sau đó mỗi lần chúng tôi nhận được một sự kiện hoặc một tin nhắn

thông qua kênh của chúng tôi, chúng tôi sẽ bắt đầu một goroutine khác.

Cái đó sẽ tạm dừng năm giây và sau đó thực hiện tìm nạp.

Vì vậy, về cơ bản chúng ta đang xem xét điều gì đó như,

chúng ta hãy dọn dẹp một chút từ phần cuối cùng ở đây.

Chúng tôi đại loại đang nói, được thôi, quy trình chính luôn có thể chạy,

nhưng rồi tất cả những đứa trẻ này sẽ phải chờ đợi

trong năm giây trước khi thực sự tìm nạp.

Vì vậy tôi sẽ đề nghị

rằng có lẽ đó cũng không phải là cách tiếp cận tốt nhất trên thế giới.

Và lý do cho điều đó là khi chúng ta nhìn

tại chức năng này checkLink ngay tại đây, tôi không biết về bạn,

nhưng trong tâm trí tôi, tôi đang tưởng tượng rằng mục đích

của chức năng checkLink là kiểm tra một liên kết ngay bây giờ.

Giống như đừng tạm dừng.

Nếu tôi gọi checkLink, tôi hy vọng nó sẽ hoạt động ngay lập tức

và cố gắng tìm nạp liên kết này.

Vì vậy tôi nghĩ rằng mặc dù điều này chắc chắn sẽ có hiệu quả,

mặc dù điều này sẽ giữ thói quen chính của chúng tôi

do bị điều tiết, tôi nghĩ rằng đó cũng là

việc sử dụng chức năng checkLink không thực sự phù hợp.

Vì vậy, rõ ràng, giữa thói quen chính

và chức năng checkLink này,

chúng ta phải đặt câu lệnh time.Sleep này ở đâu đó.

Vì vậy đây là những gì chúng ta sẽ làm.

Quay lại bên trong vòng lặp for,

chúng ta sẽ xóa chức năng checkLink ở đây,

và thay vào đó, chúng ta sẽ đặt một hàm theo nghĩa đen,

một chức năng theo nghĩa đen.

Bây giờ, nếu bạn đến từ bất kỳ ngôn ngữ nào khác,

có lẽ bạn đã biết rồi

nghĩa đen của hàm là gì.

Có lẽ bạn chỉ có một cái tên khác cho nó.

Vì vậy, nếu bạn đến từ thế giới JavaScript,

một hàm chữ trong Go tương đương 100%

tới một hàm ẩn danh hoặc Ruby, Python, C Sharp, PHP,

à, không phải PHP.

PHP là một hàm ẩn danh,

nhưng tất cả những người khác, bạn có thể biết điều này

dưới dạng hàm Lambda hoặc biểu thức Lambda.

Vì vậy, trong Go, chữ hàm là một hàm không tên

mà chúng tôi sử dụng để bọc một đoạn mã nhỏ,

để chúng tôi có thể thực hiện nó vào một thời điểm nào đó trong tương lai.

Vì vậy tôi sẽ đề xuất điều đó khi chúng ta khởi động goroutine này

ngay tại đây, thay vì chỉ nói, Này,

goroutine, hãy đi và khởi động ngay

chức năng checkLink này,

Tôi nghĩ thay vào đó chúng ta nên đặt một hàm theo nghĩa đen ở đây.

Và bên trong hàm đó, chúng ta có thể tạm dừng mã của mình,

để chúng ta có thể thực hiện câu lệnh Ngủ trong 5 giây,

rồi gọi hàm checkLink.

Vậy hãy xem thực tế nó sẽ trông như thế nào.

Chúng ta sẽ nói vui, chúng ta sẽ đặt xuống

dấu ngoặc đơn của chúng tôi cho danh sách đối số.

Chúng ta sẽ đặt dấu ngoặc nhọn xuống,

giống như chúng ta làm với chức năng bình thường.

Và bên trong thân hàm ngay tại đây,

chúng ta sẽ đặt mã

mà chúng tôi thực sự muốn thực hiện.

Vì vậy, trước tiên chúng ta sẽ bắt đầu bằng cách nói thời gian. Ngủ

năm lần. Thứ hai,

và sau đó chúng ta cũng sẽ nói checkLink với l và c.

Và bây giờ điều cuối cùng chúng ta phải thêm vào đây.

Chúng tôi phải thêm vào một bộ dấu ngoặc đơn

sau hàm chữ.

Vậy để cho rõ ràng, đây là một hàm số.

Điều này định nghĩa một hàm theo nghĩa đen,

nhưng chúng ta phải đặt thêm bộ này

dấu ngoặc đơn để gọi nó hoặc thực sự gọi nó.

Bây giờ, điều đó có vẻ hơi đáng ngạc nhiên,

nhưng hãy nhớ, hàm checkLink

mà chúng ta vừa có trước đây là một cái gì đó

như đi checkLink l và c.

Và vì vậy khi chúng ta muốn bắt đầu một goroutine mới,

chúng tôi thực hiện một cuộc gọi chức năng

hoặc một lệnh gọi hàm ngay sau từ khóa go.

Vậy trong trường hợp này chúng ta đang nói, được rồi,

đây là chức năng và gọi nó như vậy.

Được rồi, tại thời điểm này, hãy lưu mã của chúng tôi ở đây.

Và bây giờ khi tôi làm vậy,

bạn có thể nhận thấy một chút nguệch ngoạc màu xanh lá cây ở đây

trên màn hình.

Vì vậy, màu xanh lá cây có nét nguệch ngoạc, và một lần nữa,

bạn chỉ có thể thấy điều này nếu bạn đang sử dụng Mã VS.

Vì vậy, nếu bạn đang sử dụng một trình soạn thảo khác,

bạn có thể thấy hoặc không thấy điều này.

Nếu tôi di chuột qua nó, bạn sẽ thấy thông báo cảnh báo ở đây,

và nó nói biến phạm vi l được bắt bởi func theo nghĩa đen

hoặc chức năng theo nghĩa đen.

Hmm, điều đó thật thú vị.

Vì vậy, đây thực sự sẽ là một cú hích lớn

kết thúc một cuộc thảo luận rất thú vị khác

về goroutine nói chung.

Vì vậy chúng ta hãy tạm dừng nhanh chóng.

Chúng tôi sẽ quay lại

trong phần tiếp theo và chúng ta sẽ tìm hiểu

chính xác ý nghĩa của thông báo cảnh báo nhỏ này.

Vậy nên hãy nghỉ ngơi nhanh và tôi sẽ gặp bạn sau một phút nữa.