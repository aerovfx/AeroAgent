# 01 - Các yếu tố cần thiết của TensorFlow

---

- [Giảng viên] Trong bài này chúng ta sẽ tìm hiểu

làm thế nào bạn có thể trở thành một đầu bếp bậc thầy trên thế giới

mạng lưới thần kinh sử dụng TensorFlow.

Hãy coi Keras như đầu bếp nước sốt của bạn, giúp mọi việc trở nên dễ dàng hơn.

Nhưng chúng ta cũng sẽ tự mình đi sâu vào bếp

và bắt tay vào sử dụng API cấp thấp hơn của TensorFlow

để kiểm soát và tùy chỉnh nhiều hơn.

Tại sao nên sử dụng API cấp thấp hơn của TensorFlow?

Hãy coi Keras như đầu bếp nước sốt của bạn,

xử lý những điều cơ bản để bạn có thể tập trung

về việc tạo ra những công thức nấu ăn tuyệt vời hoặc các mô hình học sâu.

Keras đơn giản hóa việc xây dựng mô hình,

nhưng đôi khi bạn cần kiểm soát nhiều hơn,

giống như thêm một thành phần bí mật

hoặc điều chỉnh thời gian nấu.

API này cho phép bạn viết các hàm, số liệu mất mát tùy chỉnh,

công cụ khởi tạo và hơn thế nữa.

Vì vậy hãy nghĩ về nó giống như có được sự tự do

để điều chỉnh mọi khía cạnh của món ăn của bạn đến mức hoàn hảo.

Vì vậy, chúng ta hãy đi qua và thực hiện một chuyến tham quan nhanh về TensorFlow.

Vì vậy hãy nghĩ đến TensorFlow

giống như một thiết bị nhà bếp có công suất cao,

linh hoạt và hiệu quả cho tính toán số

và các nhiệm vụ học máy.

Nó được phát triển bởi Brain Team của Google.

Đó là bí quyết đằng sau nhiều dịch vụ của Google,

như Google Photos và tìm kiếm.

Vì vậy TensorFlow đã trở thành một yếu tố chủ yếu

trong cộng đồng học sâu,

giống như một cuốn sách nấu ăn thường dùng trong nhà bếp của một đầu bếp.

Vậy một số tương lai của TensorFlow là gì?

Trước hết, sự tương đồng với NumPy.

Nếu bạn đã sử dụng thư viện Python NumPy,

TensorFlow sẽ có cảm giác quen thuộc,

nhưng có thêm sức mạnh hỗ trợ GPU.

Vì vậy, hãy ghi nhớ tại thời điểm ghi âm này,

không gian mã không hỗ trợ GPU.

Vì vậy, vì lợi ích của lớp học này, chúng ta sẽ không sử dụng GPU,

nhưng chỉ cần biết rằng nếu bạn đang sử dụng TensorFlow

trong môi trường địa phương của bạn,

và nếu bạn có quyền truy cập vào phần hỗ trợ GPU,

TensorFlow rất giống với NumPy nhưng có thêm hỗ trợ GPU.

Vì vậy, hãy tưởng tượng NumPy là công cụ nhà bếp cơ bản của bạn

và TensorFlow giống như những công cụ tương tự có tính năng tăng tốc turbo.

Hãy nói về tính toán phân tán.

Giống như có nhiều đầu bếp trong bếp,

mỗi người xử lý các nhiệm vụ khác nhau cùng một lúc

trên nhiều thiết bị.

Điều này đảm bảo bữa ăn phức tạp của bạn

hoặc mô hình học sâu của bạn được thực hiện nhanh hơn

và hiệu quả hơn.

Vì vậy, tiếp theo chúng ta hãy xem xét trình biên dịch đúng lúc.

Tính năng này tối ưu hóa tính toán của bạn

cho tốc độ và hiệu quả như một máy xay tăng áp

chuẩn bị mọi thứ ngay lập tức.

Vì vậy, tiếp theo, chúng ta hãy nhìn vào biểu đồ tính toán.

Những biểu đồ này cho phép bạn xuất

và chạy tính toán của bạn trong các môi trường khác nhau

từ Python sang Java trên Android.

Giống như có một công thức hoạt động hoàn hảo,

cho dù bạn đang nấu ăn ở nhà

hoặc trong một nhà bếp chuyên nghiệp.

Tiếp theo, phân biệt chế độ đảo ngược.

Đó là một từ hoa mỹ,

nhưng điều này giúp tối ưu hóa công thức nấu ăn của bạn,

nói cách khác, mô hình hóa bằng cách tính toán độ dốc một cách hiệu quả.

Hãy nghĩ về nó giống như có một GPS ẩm thực hướng dẫn bạn

thông qua các bước chính xác cần thiết để có được món ăn hoàn hảo.

Vì vậy, hãy xem API TensorFlow Python.

Trước hết, nó bao gồm các API học sâu cấp cao.

Tf.keras xây dựng mô hình

rất đơn giản và trực quan.

Nó giống như một hỗn hợp làm sẵn, bạn chỉ cần thêm nước vào.

Thế là xong, bạn đã có một chiếc bánh.

Tiếp theo là API học sâu cấp thấp.

Tf.nn và tf.GradientType cung cấp cho bạn khả năng kiểm soát tốt cần thiết

cho các hoạt động tùy chỉnh.

Nó giống như được tiếp cận với từng loại gia vị

và các loại thảo mộc để tạo ra sự pha trộn độc đáo của riêng bạn.

Tiếp theo, chúng ta hãy xem xét các phép toán.

Các thư viện như tf.math, tf.linalgebra,

đó là linalg,

và tf.signal là những công cụ rất cần thiết

cho nhu cầu toán học của bạn.

Vì vậy, hãy nghĩ về chúng giống như thìa đo lường, máy trộn,

và máy đánh trứng để nấu ăn chính xác.

Tiếp theo là trực quan hóa.

Tf.summary tích hợp với TensorBoard

để trực quan hóa các mô hình của bạn và hiệu suất của chúng.

Điều này giống như việc bày món ăn của bạn lên một chiếc đĩa đẹp mắt

để gây ấn tượng với khách hàng của bạn.

Tiếp theo là kiến ​​trúc TensorFlow.

Về cốt lõi, công cụ thực thi của TensorFlow

đảm bảo hoạt động hiệu quả trên nhiều thiết bị

giống như một nhân viên nhà bếp được phối hợp ăn ý.

Nó có thể xử lý các tác vụ trên CPU, GPU,

và thậm chí cả TPU để có hiệu suất nhanh hơn.

Nó hỗ trợ nhiều ngôn ngữ khác nhau,

bao gồm Python, C++, Java và Swift,

làm cho nó trở thành một công cụ linh hoạt trong bộ công cụ của bạn.

Điều này giống như có một cuốn sách dạy nấu ăn đa ngôn ngữ

hoạt động ở mọi nơi và mọi nơi.

Tiếp theo, TensorFlow Lite cho phép bạn

để chạy mô hình trên thiết bị di động,

mang theo những sáng tạo ẩm thực của bạn khi đang di chuyển,

giống như một chiếc xe tải chở đồ ăn mang đến những bữa ăn ngon cho bạn

đến đường phố.

Vì vậy, để kết luận, API cấp cao của TensorFlow, Keras,

giống như đầu bếp nước sốt đáng tin cậy của bạn.

Thật tuyệt vời cho những bữa ăn nhanh chóng và dễ dàng,

nhưng khi bạn cần chuẩn bị một bữa tiệc thịnh soạn,

API cấp thấp hơn của TensorFlow cung cấp cho bạn quyền kiểm soát

để tùy chỉnh mọi khía cạnh của mô hình của bạn.

Điều này cho phép bạn tinh chỉnh sáng tạo của mình

và tối ưu hóa chúng cho các nhiệm vụ cụ thể.

Tính năng tính toán phân tán giống như có

một đội đầu bếp làm nước sốt trong bếp,

mỗi người làm những phần khác nhau của bữa ăn

để đảm bảo mọi thứ đều được hẹn giờ và nấu chín hoàn hảo.

Trình biên dịch đúng lúc sẽ tối ưu hóa các tính toán của bạn,

đảm bảo mô hình của bạn chạy hiệu quả và nhanh chóng.

Vì vậy, với kiến trúc linh hoạt của TensorFlow,

bạn có thể xuất và chạy biểu đồ tính toán của mình

trong các môi trường khác nhau,

đảm bảo tính nhất quán và hiệu suất

bất kể bạn ở đâu.

Điều này làm cho TensorFlow trở nên mạnh mẽ

và công cụ linh hoạt trong thế giới máy học.