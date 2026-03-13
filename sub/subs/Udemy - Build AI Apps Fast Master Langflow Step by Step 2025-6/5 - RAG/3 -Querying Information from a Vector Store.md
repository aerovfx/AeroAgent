# 3 -Truy vấn thông tin từ Cửa hàng Vector được dịch

---

Khi chúng tôi đã tạo luồng, điều đó cho phép chúng tôi lưu thông tin vào cơ sở dữ liệu cục bộ.

Hãy xác minh xem thông tin đã thực sự được bắt đầu chưa hoặc đã xảy ra sự cố hay chưa.

Làm thế nào chúng ta có thể đạt được điều này?

Chúng ta chỉ cần kéo lại thành phần DB cục bộ, bạn có thể tìm thấy nó trong phần bắt đầu vector

và chúng tôi có nó ở đây.

Bạn có thể thấy rằng thành phần này có cả chế độ nhập và truy xuất.

Hãy chuyển đổi chế độ để lấy.

Bạn có thể xem ở đây các bộ sưu tập mà chúng tôi hiện có.

Nếu chúng ta nhìn vào tên của bộ sưu tập mà chúng ta đã tạo trước đó được gọi là rack-demo, điều này cho phép

chúng tôi biết rằng mọi thứ đều hoạt động chính xác.

Vì vậy, chúng tôi chọn bộ sưu tập và là một phần của phần nhúng này và thành phần này, chúng tôi có thể nhập

một số loại truy vấn liên quan đến thông tin chúng tôi đã lưu trước đó.

Ví dụ, trong trường hợp của tôi, tôi đang nhập một câu hỏi có chứa một số từ liên quan đến

văn bản chúng ta đã nhập trước đây, chẳng hạn như hiến pháp, điều ước quốc tế, thượng viện, các bang thống nhất,

trong số những người khác.

Chúng ta đã chỉnh sửa xong nên chúng ta sẽ chạy thành phần để xem kết quả thu được là gì.

Trong trường hợp này, bạn có thể thấy lỗi do chúng tôi chưa nhập phần nhúng dưới dạng

một phần của thành phần.

Điều này đề cập đến điều gì?

Hãy nhớ rằng tôi đã đề cập trước đó, để lưu thông tin, bạn cần có được các đặc điểm ngữ nghĩa

của văn bản bạn muốn lưu trữ.

Khi bạn muốn truy vấn thông tin, điều tương tự cũng xảy ra, nhưng với văn bản bạn đang tìm kiếm

cho.

Cần phải có được các đặc điểm ngữ nghĩa của văn bản bạn đang tìm kiếm để

so sánh chúng với các vectơ được lưu trữ trong cơ sở dữ liệu.

Đó là lý do tại sao cần có thành phần nhúng khi truy vấn thông tin.

Bây giờ, hãy kéo và thả thành phần nhúng Open William và kết nối hai thành phần này.

Hãy sử dụng cùng một mô hình.

Hãy chạy lại và bạn có thể thấy rằng lần này chúng tôi nhận được phản hồi chính xác và không có lỗi.

Nếu chúng tôi kiểm tra khung dữ liệu, bạn có thể thấy nó hiện cung cấp cho chúng tôi thông tin về câu hỏi

chúng tôi hỏi.

Điều thực sự xảy ra là nó cung cấp cho chúng ta thông tin gần với câu hỏi hơn về mặt ngữ nghĩa

chúng tôi đã thực hiện.

Bạn có thể nhận thấy có một số từ khóa như 3T's.

Đây là một thuật ngữ giống hệt về mặt ngữ nghĩa với câu hỏi chúng tôi đặt ra.

Vì vậy, thông tin này được liên kết với câu hỏi chúng tôi đang hỏi.

Chúng tôi cũng có một văn bản khác phải được liên kết theo cách nào đó hoặc có liên quan về mặt ngữ nghĩa với

câu hỏi.

Bằng cách này, chúng tôi đã xác minh rằng thông tin được lưu và thông tin đó chính xác ở đâu từ

cơ sở dữ liệu cục bộ.

Việc triển khai Rack Flow như một phần của các luồng trong Lifeflow thực sự rất đơn giản.

Hãy tiếp tục với những chiếc xe.