# 6 -Tạo luồng đa tác nhân tuần tự trong langflow được dịch

---

Khi chúng tôi hiểu cách các đại lý làm việc và khả năng cung cấp cho họ nhiều công cụ, bạn

có thể cân nhắc việc tạo ra một siêu đặc vụ với 20 hoặc thậm chí 50 công cụ.

Thực tế là với các mẫu AA hiện tại, sau khi tích hợp một số công cụ nhất định,

các tác nhân có xu hướng nhầm lẫn và tạo ra kết quả không chính xác, khiến phản hồi của họ mất đi độ chính xác.

Đó là lý do tại sao các mẫu tác nhân khác nhau đã được phát triển để tối ưu hóa việc sử dụng các công cụ trong

đại lý.

Một trong những mẫu đơn giản và nổi tiếng nhất là mẫu tuần tự.

Word và tác nhân truy vấn tác nhân tiếp theo để thực hiện một tác vụ, v.v. cho đến khi có kết quả cuối cùng

đã đạt được.

Hãy làm một ví dụ thực tế trong Lancthlo.

Giả sử chúng ta muốn nhập một phép toán vào cuộc trò chuyện và mô hình AA không cung cấp cho chúng ta

kết quả mà thay vào đó cung cấp mô tả về những người đã tạo ra toán học

khái niệm.

Hãy làm điều đó.

Chúng ta sẽ bắt đầu bằng cách thêm thành phần tác nhân, giống như chúng ta đã làm trước đây.

Tôi sẽ chọn mô hình GPT, trừ 4O mini và tiếp theo tôi thêm một thành phần hoặc công cụ,

đó sẽ là máy tính mà chúng tôi đã sử dụng trước đó.

Thành phần này sẽ cho phép chúng ta thực hiện các phép toán cần thiết để tiến hành nghiên cứu

về người đã tạo ra công thức đó.

Vì vậy, tôi kích hoạt chế độ công cụ và kết nối công cụ với tác nhân.

Hãy kết nối một đầu vào trò chuyện ở đây.

Chúng tôi liên kết nó với đầu vào của tổng đài viên và chúng tôi cũng thêm đầu ra trò chuyện, kết nối phản hồi

đến đầu ra trò chuyện.

Đây là điều chúng ta đã thấy trước đây.

Tôi sẽ nhập một phép toán để tác nhân giải và bạn có thể thấy rằng

chức năng đã được thực thi.

Công cụ hoặc thành phần máy tính cho chúng ta thấy kết quả.

Điều này hoạt động chính xác.

Bây giờ, bước tiếp theo là khi tác nhân trả về thông tin về câu trả lời cho

vấn đề toán học, chúng tôi muốn tạo ra một tác nhân khác sẽ điều tra xem ai là người

người sáng lập ra phép toán.

Vì vậy, tôi sẽ kéo thành phần nhắc nhở vì tôi muốn gửi kết quả này đến thành phần đó.

Hãy nhớ rằng để điều này hoạt động bình thường, chúng ta phải xác định một tập hợp các biến như một phần của

thành phần này.

Tôi sẽ dán lời nhắc mà tôi đã tạo trước đó, trong đó ghi rằng bạn là một nhà toán học

nhà sử học.

Bạn cần phân tích các thông tin sau đây là kết quả của lời giải toán học.

Điều này chỉ ra rằng chúng ta phải rút ra những nguyên tắc cơ bản đằng sau các yếu tố toán học.

Ví dụ, nếu nó là tích phân hoặc nếu nó liên quan đến lượng giác thì cuối cùng, nó

là cần thiết để nghiên cứu tác giả của các nguyên tắc cơ bản toán học mà trên đó

câu trả lời là có cơ sở.

Vì vậy, chúng tôi để lại lời nhắc hoặc mẫu này.

Hãy kết nối thành phần loại tác nhân với lời nhắc này.

Điều này sẽ chuyển thông tin từ kết quả toán học sang thành phần nhắc nhở,

mà sau đó chúng ta phải rò rỉ cho một đặc vụ khác.

Bây giờ, hãy kết nối đại lý.

Đây rồi.

Hãy xác định rằng đầu vào cho thành phần hay đúng hơn là tác nhân sẽ là đầu ra từ

thành phần nhắc nhở.

Chúng tôi kết nối nó theo cách này.

Bây giờ chúng ta cần điều tra xem ai là người sáng tạo hoặc ai là người sáng lập ra những công cụ toán học này.

các khái niệm.

Đối với điều này, chúng tôi sẽ sử dụng một công cụ.

Công cụ này sẽ là Wikipedia, cũng miễn phí.

Hãy biến nó thành một công cụ và sau đó kết nối nó với tác nhân để nó có thể điều tra thêm

về các nhân vật lịch sử.

Điều quan trọng chúng ta cần làm ở đây là sửa đổi hướng dẫn của tác nhân, vì nếu không

nó có thể không tiến hành nghiên cứu thích hợp.

Trong trường hợp này, chúng tôi xác định rằng như một phần của hướng dẫn này, cần phải điều tra

tất cả sự thật về người đã phát minh ra công thức này.

Vì vậy, chúng tôi hoàn thành mọi thứ và bạn có thể thấy rằng bây giờ chúng tôi có một quy trình tuần tự.

Nó bắt đầu bằng đầu vào trò chuyện, xử lý thông tin và sau đó chuyển nó sang một giây

đại lý sẽ tiến hành một cuộc điều tra sâu hơn.

Hãy chỉ định rằng chúng tôi muốn có đầu ra trò chuyện vì trước đó chúng tôi đã xóa nó.

Hãy kết nối đầu ra của tổng đài viên này với thành phần đầu ra trò chuyện và kiểm tra luồng mới

chúng tôi đã tạo trong sân chơi.

Tôi sẽ bắt đầu một cuộc trò chuyện mới và nhập một hướng dẫn đơn giản.

321 nhân với 23 bằng bao nhiêu?

Hãy gửi hướng dẫn.

Chúng tôi thấy rằng thông tin đang được xử lý.

Tại đây, người ta đã thu được phép tính toán học phù hợp và ngay sau khi nghiên cứu

đã được hoàn thành với chức năng này đã tìm nạp nội dung, bạn có thể thấy rằng hướng dẫn

được sử dụng để hoàn thành thông tin thành phần tìm kiếm Wikipedia là lịch sử của số học.

Điều này cung cấp cho chúng ta một bản tóm tắt về phép toán này bao gồm những gì, trong đó

đã cho chúng ta một kết quả cụ thể.

Đầu tiên, chúng ta nhận được câu trả lời cho phép tính toán học và sau đó là lời giải thích ngắn gọn

của cơ sở toán học.

Hãy thử một hướng dẫn phức tạp hơn một chút.

Trong trường hợp này, đó là lệnh liên quan đến phân số.

Hãy gửi câu hỏi này đến A-Model và xem phản hồi của nó là gì nhé.

Sau vài giây, bạn có thể thấy quá trình xử lý đã hoàn tất.

Đầu tiên, chúng ta có thể ghi lại kết quả của phép tính toán và tiếp theo, chúng ta được giải thích

về bối cảnh lịch sử của công thức, cho phép chúng tôi xác minh rằng những công thức này hoạt động chính xác.

Đây là cách chúng ta có thể tạo các tác nhân tuần tự trong lagflow.