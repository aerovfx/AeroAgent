# 05 - Chọn mẫu phù hợp từ trung tâm Ôm Mặt

---

- [Người hướng dẫn] Để truy cập trung tâm mô hình Ôm Mặt,

hãy truy cập ôm mặt.co/models.

Nền tảng này lưu trữ một bộ sưu tập lớn các mô hình được đào tạo trước,

điều này có vẻ áp đảo lúc đầu.

Tuy nhiên, bằng cách làm theo một số bước chính,

bạn có thể tìm thấy mô hình phù hợp với nhu cầu của mình một cách hiệu quả.

Bước đầu tiên trong việc lựa chọn một mô hình

đang xác định nhiệm vụ cụ thể của bạn.

Ví dụ: nếu bạn đang làm công việc phân tích tình cảm,

thuộc phân loại văn bản,

điều hướng đến bảng điều khiển bên trái

và chọn Phân loại văn bản từ tác vụ có sẵn.

Điều này lọc các mô hình có sẵn, chỉ hiển thị những mô hình

được thiết kế để phân loại văn bản.

Trung tâm Ôm Mặt hỗ trợ nhiều

thư viện học sâu,

bao gồm PyTorch, TensorFlow và JAX.

Để giữ mọi thứ đơn giản, chúng ta sẽ giới hạn bản thân

để xây dựng các mô hình bằng cách sử dụng chức năng đường ống,

được cung cấp như một phần của thư viện Ôm Mặt.

Để áp dụng bộ lọc này,

chọn Transformers từ các thư viện có sẵn.

Tiếp theo, tinh chỉnh tìm kiếm của bạn

bằng cách chọn ngôn ngữ mà mô hình của bạn sẽ hỗ trợ.

Nếu bạn đang phân tích văn bản tiếng Anh,

chọn tiếng Anh làm ngôn ngữ ưa thích.

Bước này đảm bảo rằng chỉ những mô hình có khả năng

xử lý dữ liệu tiếng Anh vẫn còn trong danh sách.

Trước khi sử dụng mô hình, hãy xem lại giấy phép của nó

để đảm bảo nó phù hợp với mục đích sử dụng của bạn.

Một số mô hình bị hạn chế trong nghiên cứu học thuật,

trong khi những người khác cho phép các ứng dụng thương mại.

Vì đây chỉ là bản demo nên

chúng tôi sẽ không áp dụng bộ lọc giấy phép trong trường hợp này.

Sau khi áp dụng các bộ lọc tác vụ, khung và ngôn ngữ,

bạn có nhiều lựa chọn về mô hình hơn.

Bạn có thể thu hẹp lựa chọn của mình hơn nữa bằng cách lọc

theo tên mẫu máy nếu bạn nghĩ đến một mẫu máy cụ thể

và/hoặc sắp xếp các mô hình theo xu hướng, lượt thích,

lượt tải xuống, ngày tạo,

hoặc cập nhật lần cuối để tìm thông tin phù hợp nhất

và các tùy chọn được sử dụng rộng rãi.

Nhấp vào mô hình sẽ đưa bạn trực tiếp đến thẻ mô hình của nó.

Mỗi thẻ mô hình cung cấp các chi tiết cần thiết

về quá trình huấn luyện mô hình, hướng dẫn sử dụng,

những rủi ro, hạn chế, thành kiến đã biết,

và những thông tin cần thiết khác.

Ngoài ra, số lượt tải xuống của mô hình

và các cuộc thảo luận cộng đồng có sẵn trên trang.

Những hiểu biết này có thể giúp đánh giá

mức độ phổ biến và độ tin cậy của mô hình.

Sau khi bạn đã chọn được một mô hình,

bạn có thể tải nó vào môi trường mã hóa của mình

bằng cách tham khảo tên của nó.

Ví dụ: để sử dụng mô hình DistilBERT hiển thị ở đây,

chúng tôi đề cập đến tên của nó khi khởi tạo một đường dẫn.

Bằng cách làm theo bảy bước được nêu ở đây,

bạn sẽ có thể tìm thấy mô hình được đào tạo trước phù hợp

cho công việc của bạn một cách hiệu quả hơn.