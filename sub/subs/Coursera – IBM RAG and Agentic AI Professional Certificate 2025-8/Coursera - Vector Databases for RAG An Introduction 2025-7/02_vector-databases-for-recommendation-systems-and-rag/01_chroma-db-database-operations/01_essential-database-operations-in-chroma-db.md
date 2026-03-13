# 01 cơ sở dữ liệu cần thiết-hoạt động-in-chroma-db

---

Chào mừng bạn đến với video này, Các thao tác cơ sở dữ liệu thiết yếu trong Chroma DB.

Sau khi xem video này, bạn sẽ có thể

Tạo bộ sưu tập trong Chroma DB Sửa đổi bộ sưu tập trong Chroma DB

Thêm, cập nhật và xóa tài liệu khỏi bộ sưu tập trong Chroma DB

Trong video này, bạn sẽ tìm hiểu cách tạo và sửa đổi các bộ sưu tập cũng như cách

thêm, cập nhật và xóa tài liệu.

Những hoạt động này tạo thành nền tảng cho việc xây dựng các ứng dụng thông minh, dựa trên vector

tận dụng khả năng mạnh mẽ của Chroma DB.

Trước tiên, hãy xem cách tạo bộ sưu tập trong Chroma DB.

Bộ sưu tập là một cách để sắp xếp dữ liệu của bạn.

Để bắt đầu, bạn nhập chromadb và embedding_functions, cho phép bạn xác định

một mô hình nhúng

Sau đó, bạn xác định mô hình nhúng.

Trong trường hợp này, chúng tôi đang sử dụng mô hình từ SentenceTransformers.

Và chúng tôi xác định nó bằng hàm SentenceTransformerEmbeddingFunction.

Sau đó, bạn xác định ứng dụng khách chromadb của mình và sử dụng create_collection của ứng dụng khách

phương pháp tạo ra một bộ sưu tập.

Ở đây, chúng tôi đang tạo một bộ sưu tập có tên my_collection kèm theo mô tả

trong siêu dữ liệu của nó.

Siêu dữ liệu có thể giúp bạn theo dõi mục đích và nội dung bộ sưu tập của mình.

Dòng cuối cùng tạo đầu ra, trong trường hợp này chỉ là tên bộ sưu tập mà chúng tôi

được chỉ định trước đó.

Nếu bạn đã có bộ sưu tập muốn kết nối, bạn có thể thiết lập kết nối

vào nó bằng phương thức get_collection.

Trong trường hợp cụ thể này, chúng tôi đang kết nối với bộ sưu tập my_collection,

bộ sưu tập mà chúng tôi đã xác định trước đó.

Chúng tôi có thể xác minh điều này bằng cách in siêu dữ liệu của bộ sưu tập, trong trường hợp này là mô tả

chúng tôi đã xác định cho my_collection.

Bạn có thể thay đổi bộ sưu tập bằng cách sử dụng phương thức sửa đổi.

Trong trường hợp cụ thể này, chúng tôi đang thay đổi tên và siêu dữ liệu của bộ sưu tập hiện có của mình.

Lưu ý rằng siêu dữ liệu bộ sưu tập trong Chroma DB có thể chấp nhận bất kỳ cặp khóa-giá trị nào hữu ích

để mô tả bộ sưu tập của bạn.

Trong trường hợp này, với mục đích trình diễn, chúng tôi chỉ đơn giản sử dụng phím 'key' và gán

nó thành giá trị 'giá trị'.

Và một lần nữa, dòng cuối cùng tạo đầu ra, trong trường hợp này là siêu dữ liệu đã sửa đổi

chỉ đơn giản bao gồm cặp khóa-giá trị của chúng tôi.

Xin lưu ý rằng một số thay đổi nhất định, chẳng hạn như sửa đổi mô hình nhúng hoặc khoảng cách

số liệu, không thể được thực hiện với bộ sưu tập hiện có.

Để áp dụng những thay đổi này, bạn cần sao chép một bộ sưu tập, đây có thể là một thao tác tốn kém

về mặt tính toán nếu bạn có một lượng dữ liệu đáng kể được lưu trữ trong bộ sưu tập của mình.

Thêm dữ liệu vào bộ sưu tập của bạn rất đơn giản.

Sử dụng phương thức thêm để chèn tài liệu bằng danh sách.

Bạn cũng có thể cung cấp siêu dữ liệu tùy chọn bằng cách chuyển danh sách từ điển tới siêu dữ liệu

tham số.

Không có giới hạn về nội dung của siêu dữ liệu.

Trong trường hợp này, chúng tôi đang chuyển thông tin nguồn và phiên bản của tài liệu.

Đảm bảo bao gồm ID cho từng tài liệu trong danh sách được chuyển đến tham số ids.

Bạn có thể lấy dữ liệu, chẳng hạn như tài liệu, từ một bộ sưu tập bằng phương thức get.

Lưu ý rằng phương thức get trả về một từ điển Python.

Khi bạn chạy phương thức Collection.get, kết quả đầu ra sẽ trả về tất cả tài liệu trong bộ sưu tập.

Lưu ý rằng đầu ra không trả về các phần nhúng.

Tuy nhiên, các phần nhúng thực sự được lưu trữ trong bộ sưu tập nhưng chúng không được hiển thị

theo mặc định để giữ cho đầu ra sạch sẽ.

Để xem các phần nhúng, chúng ta cần chuyển include=['embeddings'] vào phương thức get.

Hơn nữa, ngoài việc lấy ra tất cả các tài liệu trong một bộ sưu tập, bạn có thể truy xuất

các tài liệu riêng lẻ bằng cách chuyển ID của chúng tới phương thức get.

Để cập nhật dữ liệu hiện có trong bộ sưu tập của bạn, hãy sử dụng phương thức cập nhật.

Điều này cho phép bạn sửa đổi một hoặc nhiều bản ghi dựa trên ID của chúng.

Trong ví dụ về mã này, chúng tôi đang cập nhật tài liệu về LangChain bằng cách chỉ định ID của nó, 'id1'.

Và chúng tôi đang thay đổi cả thông tin siêu dữ liệu và văn bản của tài liệu.

Lưu ý rằng Chroma DB xử lý việc nhúng lại ở chế độ nền, tính toán lại các phần nhúng

cho tài liệu ngay khi bản cập nhật được gửi.

Cuối cùng, bạn có thể chuyển vào danh sách ID cần xóa hoặc sử dụng bộ lọc Where để

lọc siêu dữ liệu của tài liệu.

Lưu ý rằng bạn cũng có thể sử dụng kết hợp ID và bộ lọc.

Trong ví dụ này, chỉ tài liệu liên quan đến LlamaIndex sẽ bị xóa vì điều đó

là tài liệu duy nhất mà câu lệnh Where có giá trị đúng.

Chroma DB sử dụng thuật toán có tên Hierarchical Navigable Small World (hoặc HNSW) để thực hiện

tìm kiếm hàng xóm gần nhất gần đúng.

Tham số không gian trong HNSW xác định hàm khoảng cách được sử dụng trong không gian nhúng.

Theo mặc định, giá trị này được đặt thành l2, viết tắt của định mức L2 bình phương.

Các tùy chọn được hỗ trợ khác bao gồm cosine cho khoảng cách cosine và ip cho sản phẩm bên trong

hoặc dấu chấm khoảng cách sản phẩm.

Để chỉ định hàm khoảng cách, hãy chuyển giá trị bạn đã chọn vào phím cách khi định cấu hình

bộ sưu tập Chroma DB tại thời điểm tạo.

Trong ví dụ về mã này, khi chúng ta tạo một bộ sưu tập có tên my_collection, trong cấu hình

từ điển, chúng ta chuyển cosine làm giá trị của phím cách khi định cấu hình HNSW.

Trong video này, bạn đã học được rằng

Các hoạt động của Chroma DB tạo thành nền tảng để xây dựng các ứng dụng dựa trên vector thông minh.

Bộ sưu tập là một cách để sắp xếp dữ liệu của bạn trong Chroma DB.

Bạn xác định mô hình nhúng của mình bằng các hàm nhúng của Chroma DB.

Bạn tạo một bộ sưu tập bằng phương thức create_collection.

Siêu dữ liệu giúp bạn theo dõi mục đích và nội dung bộ sưu tập của mình.

Bạn kết nối với bộ sưu tập hiện có bằng cách sử dụng phương thức get_collection.

Bạn thay đổi bộ sưu tập hiện có bằng cách sử dụng phương thức sửa đổi.

Bạn sử dụng phương thức add để chèn tài liệu vào bộ sưu tập.

Bạn lấy dữ liệu từ một bộ sưu tập bằng phương thức get.

Bạn cập nhật dữ liệu hiện có trong bộ sưu tập bằng cách sử dụng phương thức cập nhật.

Bạn xóa dữ liệu khỏi bộ sưu tập bằng phương pháp xóa.

Bạn sử dụng tham số cấu hình không gian HNSW để xác định hàm khoảng cách khi thực hiện

các tìm kiếm lân cận gần nhất trong Chroma DB.