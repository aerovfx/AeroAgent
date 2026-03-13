# 3 -Bundle-loại công cụ trong langflow dịch

---

Chắc chắn, khi xem xét Giao diện đồ họa Landflow,

bạn nhận thấy có một phần đặc biệt tên là Gói,

đó là một phần của Landflow.

Phần này dùng để làm gì?

Các công ty tốt hơn cung cấp nhiều dịch vụ

và có các điểm truy cập hoặc điểm cuối khác nhau

để thực hiện các nhiệm vụ khác nhau trong cùng một dịch vụ.

Ví dụ: bạn có thể thấy rằng Amazon cung cấp dịch vụ

chẳng hạn như Amazon Bird Rock.

Nó cũng hoạt động để tải các nhóm như một phần của dịch vụ Amazon.

Chúng tôi có các dịch vụ như 85, cho phép chúng tôi kết nối với các điểm cuối khác nhau.

Ví dụ: chúng tôi cũng thấy rằng chúng tôi có dịch vụ Nvidia,

cho phép chúng tôi truy cập các dịch vụ khác nhau trong cùng một nền tảng.

Vì vậy, đó là mục đích của những gói này.

Chúng là các dịch vụ khác nhau được nhóm thành các danh mục phụ.

Và nếu chúng tôi đưa từng dịch vụ riêng lẻ vào phần công cụ,

chúng ta sẽ có một danh sách rất dài.

Vì vậy, nhóm quyết định gói gọn và sắp xếp chúng theo các danh mục con,

thêm tên công ty như một phần của danh mục chính.

Hãy thử một trong những gói này.

Hãy thử dịch vụ có tên Firecrowley,

một công ty rất nổi tiếng trong lĩnh vực mô hình AI.

Về cơ bản, nó là một trình trích xuất cho phép chúng ta lấy thông tin từ một trang web.

Ví dụ: nó cho phép bạn nhập URL và chỉ trả về văn bản mà chúng tôi quan tâm.

Nó tương tự như những gì chúng ta đã thấy trước đây với công cụ có tên Taville.

Trong trường hợp này, Taville tiến hành tìm kiếm, nhưng với Firecrowley,

ví dụ: chúng tôi có các API cho phép chúng tôi

để trích xuất thông tin từ các trang web,

hoặc chúng ta có thể sử dụng chúng để lấy dữ liệu từ một số loại bản đồ.

Hãy thử một trong những thứ này.

Trong trường hợp của Firecrowley,

bạn cần truy cập trang web Firecrowley.deft.

Tại đây, bạn cần tạo một tài khoản,

và sau khi bạn đã đăng ký, hãy chuyển đến phần có tên Khóa API.

Bạn phải tạo một khóa mới,

và khi đã có nó, bạn sẽ sao chép nó để kết nối với dịch vụ.

Hãy theo dõi một trong các thành phần.

Ví dụ: cái này có tên là FirecrowleyScreateATI.

Chúng ta sẽ tạo biến toàn cục.

Sau khi lưu các thay đổi đối với khóa này, hãy chọn nó và khi bạn đã thực hiện xong,

thông báo có một trường bắt buộc quan trọng.

Thuộc tính này được gọi là URL,

cho phép chúng tôi nhập thông tin trước khi trích xuất của người khác.

Ví dụ: trước đó tôi đã xem lại tài liệu về langflow,

và sao chép URL này mà tôi sẽ sử dụng cho mục đích trình diễn.

Về thời gian chờ, tôi để nguyên như vậy,

và như bạn có thể thấy rằng thành phần cụ thể này cung cấp các tùy chọn bổ sung

để cấu hình trích xuất và loại bỏ.

Vì vậy, khi chúng ta hoàn thành việc này,

Tôi sẽ bắt đầu chạy thành phần này.

Chúng ta hãy chờ đợi một lát.

Và khi quá trình trích xuất dữ liệu hoàn tất,

chúng ta hãy xem lại kết quả.

Và bạn có thể thấy rằng điều này trả về nội dung trang ở định dạng Markdown,

điều này rất hữu ích cho mô hình AMAIA

vì chỉ có thông tin liên quan mới được lấy ra.

Bằng cách này, chúng ta có thể khám phá các tiêu đề,

chỉ xem lại các phần có văn bản hoặc trích xuất hình ảnh,

trong số các lựa chọn khác.

Chúng tôi có thêm thông tin thu được từ truy vấn này.

Đây là cách chúng tôi sử dụng thành phần nằm trong các gói này.

Bạn có thể định cấu hình bất kỳ thứ nào trong số này và sử dụng chúng khi cần.