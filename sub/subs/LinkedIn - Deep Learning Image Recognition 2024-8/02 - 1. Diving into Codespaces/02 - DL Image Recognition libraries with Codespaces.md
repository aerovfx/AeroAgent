# 02 - Thư viện nhận dạng hình ảnh DL với Codespaces

---

- Cùng điểm qua 10 thư viện quan trọng

mà chúng tôi sẽ sử dụng cho dự án này.

Vì vậy số một là thư viện hệ điều hành.

Vì vậy, nó cung cấp chức năng phụ thuộc vào hệ điều hành.

Vì vậy, bất kể hệ điều hành của bạn là gì,

chúng ta vẫn có thể hoạt động và sử dụng cấu trúc mà chúng ta có.

Nó giúp quản lý các thư mục và đường dẫn tập tin.

Nó gần như hoạt động như một cầu nối giữa mã Python

và hệ điều hành.

Vì vậy hãy coi OS như một quản gia

người có thể đi tìm kiếm mọi thứ trong nhà bạn

và có thể cho bạn biết mọi thứ ở đâu.

Bây giờ, thư viện tiếp theo mà chúng ta sẽ sử dụng là NumPy.

NumPy là một thư viện mạnh mẽ

đặc biệt là tính toán số.

Nó hỗ trợ mảng, ma trận,

và rất nhiều hàm toán học.

Nó rất cần thiết cho việc xử lý và thao tác dữ liệu.

Chà, chúng ta có thể coi NumPy như một chiếc máy tính

có thể giải quyết những vấn đề toán học phức tạp nhất

một cách dễ dàng.

Tiếp theo là Matplotlib.

Chà, đó là một trong những thư viện nổi tiếng để vẽ đồ thị.

Nó tạo ra hình ảnh tĩnh, hoạt hình và tương tác.

Nó giúp trực quan hóa dữ liệu rất hiệu quả.

Chà, chúng ta có thể coi đó là một nghệ sĩ

người có thể vẽ nên một bức tranh rõ ràng về dữ liệu của bạn,

làm cho nó dễ hiểu.

Tiếp theo là tensorflow.keras.datasets.

Vâng, điều này cung cấp các bộ dữ liệu nổi tiếng

mà chúng tôi sẽ sử dụng, chẳng hạn như tập dữ liệu CIFAR-10.

Nó đơn giản hóa việc tải và chuẩn bị bộ dữ liệu.

Chà, nó cho phép chúng ta tập trung hơn

về xây dựng và đào tạo mô hình

hơn là cố gắng tìm ra cách tải dữ liệu

và lấy nó ở đâu, vân vân.

Nó làm giảm bớt gánh nặng trên vai chúng ta.

Well, we can think of it like a recipe book

điều đó mang lại cho chúng tôi tất cả các công thức nấu ăn

và các nguyên liệu đã được đo lường trước để chúng ta có thể tập trung vào việc nấu nướng.

Tiếp theo, chúng ta có tensorflow.keras.utils.

Vâng, điều này bao gồm các chức năng tiện ích

để xử lý trước dữ liệu.

Các chức năng tiện ích là gì?

Vâng, một ví dụ là mã hóa một lần.

Điều này chuyển đổi vectơ lớp thành ma trận lớp nhị phân.

Nó đơn giản hóa các bước tiền xử lý cho chúng tôi.

Chà, chúng ta có thể coi nó giống như một đầu bếp phó

người chuẩn bị nguyên liệu cho chúng tôi,

đảm bảo mọi thứ đã sẵn sàng để chúng ta bắt đầu nấu ăn.

Tiếp theo là tensorflow.keras.models.

Vâng, đây là để xác định

và đào tạo các mô hình deep learning.

Giao diện cấp cao để xây dựng mô hình,

đơn giản hóa việc tạo các mạng lưới thần kinh phức tạp

thành dòng mã đơn giản hơn rất nhiều.

Chà, một phép ẩn dụ hay

vì đây giống như bản thiết kế của một kiến trúc sư.

Nó cho chúng ta một kế hoạch rõ ràng để xây dựng mạng lưới thần kinh của mình.

Tiếp theo là tensorflow.keras.layers.

Nó cung cấp cho chúng ta nhiều lớp mạng thần kinh khác nhau.

Một số lớp bao gồm Conv2D, MaxPooling2D,

phẳng, dày đặc và bỏ học.

Nó cung cấp các khối xây dựng để thiết kế kiến ​​trúc mô hình.

Mặc dù các lớp này giống như các khối xây dựng của bộ Lego,

nó cho phép chúng ta xây dựng các cấu trúc phức tạp.

Next is the sklearn.metrics.

Nó có chức năng đánh giá hiệu suất của mô hình.

Nó bao gồm ma trận nhầm lẫn,

mà chúng tôi sẽ sử dụng trong dự án của mình

và báo cáo phân loại.

Nó giúp hiểu được hiệu suất mô hình

và xác định các vấn đề.

Chúng ta có thể nhìn vào sklearn.metrics

giống như một thẻ báo cáo cho mô hình của chúng tôi,

cho chúng tôi thấy nó hoạt động như thế nào và nó có thể cải thiện ở đâu.

Sinh ra ở biển.

Chà, Seaborn rất tốt cho việc trực quan hóa dữ liệu thống kê.

Cái này được xây dựng dựa trên Matplotlib,

mà chúng tôi đã xem xét trước đó.

Đây là giao diện cấp cao

để vẽ đồ họa thống kê, hấp dẫn.

Chúng ta có thể coi Seaborn giống như một nhà thiết kế đồ họa

người không chỉ làm cho dữ liệu của chúng tôi rõ ràng,

nhưng nó cũng rất có tính thẩm mỹ.

Tiếp theo là TensorFlow.

Đây là một khung học máy nguồn mở của Google.

Đó là hệ sinh thái toàn diện thật tuyệt vời

để xây dựng và triển khai các mô hình.

Đó là xương sống cho các nhiệm vụ học sâu của chúng tôi.

Chà, chúng ta có thể nghĩ đến TensorFlow

như nền tảng của một ngôi nhà.

Nó hỗ trợ mọi thứ và giữ tất cả lại với nhau.

Vâng, đây là 10 thư viện quan trọng nhất

mà chúng tôi sẽ làm việc cùng.

Mỗi thư viện đều đóng góp đáng kể cho dự án của chúng tôi.

Chúng bao gồm những thứ như xử lý trước dữ liệu,

trực quan hóa, xây dựng mô hình và đánh giá.

Việc hiểu rõ những công cụ này là rất, rất cần thiết

cho các dự án khoa học dữ liệu và học máy hiệu quả.