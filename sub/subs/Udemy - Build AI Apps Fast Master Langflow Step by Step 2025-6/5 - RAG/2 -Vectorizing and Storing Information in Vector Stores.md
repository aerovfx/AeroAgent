# 2 -Vectorizing và lưu trữ thông tin trong Vector Stores được dịch

---

Khi chúng ta đã có tập hợp các thành phần để trích xuất thông tin, bước tiếp theo là vector hóa

những dữ liệu này và sau đó lưu trữ chúng.

Tại sao không sử dụng nó để vector hóa thông tin này?

Thông thường khi làm việc với các mô hình AI, cơ sở dữ liệu hoặc thông tin vectơ sẽ được sử dụng.

Điều này là do việc tìm kiếm ngữ nghĩa được thực hiện không phải theo nghĩa đen, như thể bạn đang tìm kiếm

để có một văn bản phù hợp chính xác.

Vì vậy khi thực hiện tìm kiếm vector hoặc tìm kiếm ngữ nghĩa, bạn cần chuyển đổi từng đặc điểm

văn bản thành những mẩu thông tin nhỏ.

Ví dụ: nếu bạn đang mô tả một quả táo, bạn có thể bao gồm các tính năng hoặc thẻ nhất định

Apple với các đặc tính như nó có màu đỏ không, nó có hình tròn không, kích thước của nó là bao nhiêu

trong số những người khác.

Mỗi phần dữ liệu đó sẽ là một biểu diễn vector của quả táo đó.

Điều tương tự cũng xảy ra với thông tin.

Bạn nhận được những mẩu dữ liệu nhỏ từ mỗi văn bản bạn phân tích.

Nhưng để có được thông tin này hoặc các vectơ này, cần phải sử dụng dịch vụ nhúng

cho phép bạn có được dữ liệu cụ thể này.

Tiếp theo, đó là những gì chúng ta sẽ làm.

Chúng tôi sẽ trích xuất thông tin đó.

Làm thế nào chúng ta có thể làm điều này?

May mắn thay, langflow có các công cụ cho phép chúng ta thực hiện việc này rất dễ dàng.

Đầu tiên, chúng tôi sẽ chỉ trích xuất từ văn bản được phân tách này những thông tin mà chúng tôi quan tâm

in, đó là cột được gọi là văn bản.

Trong trường hợp cụ thể khác, chúng tôi không quan tâm đến việc lưu URL, nguồn, nội dung, loại hoặc

dữ liệu khác.

Chúng tôi chỉ quan tâm đến việc lưu văn bản.

Vì vậy, chúng ta hãy chỉ chọn cột này.

Để làm điều này, chúng tôi có một thành phần được gọi là Hoạt động khung dữ liệu, đây là những gì bạn thấy trên

màn hình.

Hãy cho biết rằng chúng tôi muốn tạo kết nối với văn bản được phân tách và khi chúng tôi có điều này

thành phần đã sẵn sàng, chúng tôi sẽ chỉ định rằng hoạt động mà Quan tâm đang chọn một số cụ thể

cột.

Trong trường hợp của chúng tôi, chúng tôi chỉ quan tâm đến một cột, cột được gọi là văn bản mà bạn có thể thấy

trên màn hình.

Sau khi thực hiện việc này, chúng tôi sẽ kiểm tra lại việc thực thi thành phần và bạn có thể thấy điều đó

bây giờ nó chỉ trả về cột dán một lần, đây là cột mà chúng tôi thực sự muốn vector hóa.

Với điều này, chúng tôi đã đạt được tiến bộ trong việc khai thác thông tin.

Bây giờ, trong phần được gọi là cửa hàng vector, bạn sẽ tìm thấy một số nhà cung cấp cho phép bạn

để lưu thông tin ngữ nghĩa từ văn bản thu được từ tài liệu hoặc URL.

Trong trường hợp cụ thể này, chúng tôi có nhiều dịch vụ mà bạn có thể dùng thử nếu muốn.

Trong trường hợp của tôi, để mọi thứ đơn giản và dễ hiểu, tôi đã sử dụng thành phần có tên localDB, vì

nó không yêu cầu đăng ký trên bất kỳ trang web bên ngoài nào và có sẵn để sử dụng cục bộ.

Tôi nghĩ đây là một thành phần thích hợp cho trường hợp sử dụng của chúng tôi, vì hiện tại chúng tôi chỉ muốn

để thực hiện các bài kiểm tra.

Nhóc, chúng ta thấy phần mô tả nói rằng đó là một cửa hàng vector địa phương có khả năng thực hiện

tìm kiếm.

Bạn có thể thấy thành phần này yêu cầu một số nút thông tin, chẳng hạn như tên của bộ sưu tập.

Tại đây, bạn có thể gán bất kỳ tên nào bạn thích, ví dụ: bản demo giá trong trường hợp của tôi.

Ngoài ra, bạn có thể nhận thấy ở trên cùng là chúng tôi có hai chế độ để sử dụng thành phần này.

Ở chế độ nhập, về cơ bản được sử dụng để thêm thông tin mới vào cơ sở dữ liệu cục bộ hoặc

Chế độ Android Vib, cho phép chúng tôi trích xuất thông tin khi cần.

Trong trường hợp của tôi, vì chúng tôi muốn lưu trữ thông tin nên chúng tôi sẽ để nó ở chế độ nhập.

Hãy giữ nguyên tên của bộ sưu tập này và bạn có thể nhận thấy rằng nó cũng yêu cầu nhúng,

là dịch vụ cho phép trích xuất thông tin ngữ nghĩa từ văn bản bạn muốn

để lưu trữ.

Vì vậy, những gì chúng ta sẽ làm là chọn nút.

Tiếp theo, hãy xác định một số dịch vụ cung cấp tập hợp các phần nhúng.

Ở đây, tôi quan tâm đến việc sử dụng cái của OpenAI, vì nó là một trong những cái phổ biến nhất.

Vì vậy, tôi kéo và thả thành phần và chọn mô hình mặc định, nhúng văn bản 3 nhỏ.

Tôi để lại khóa API OpenAI mà tôi đã nhập trước đó và sẽ kết nối thành phần này

đến thành phần DB cục bộ.

Bước tiếp theo hoặc bước cuối cùng là kết nối tập dữ liệu với thành phần cơ sở dữ liệu, do đó

chúng tôi kết nối nút khung dữ liệu với nút dữ liệu nhập vào để thiết lập kết nối.

Bằng cách này, luồng của chúng tôi sẽ sẵn sàng để lưu thông tin.

Điều cuối cùng chúng ta cần làm là kiểm tra bằng cách chạy thành phần để xác minh rằng mọi thứ đều hoạt động

một cách chính xác, và tôi có thể nói đó là một sự thực hiện khá nhanh chóng.

Tôi không có khung dữ liệu ở đây nhưng chúng tôi sẽ kiểm tra xem thông tin đã được lưu trong

video tiếp theo.