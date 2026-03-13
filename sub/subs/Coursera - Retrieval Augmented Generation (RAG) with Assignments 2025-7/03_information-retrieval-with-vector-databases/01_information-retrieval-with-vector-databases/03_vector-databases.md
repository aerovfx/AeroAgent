# 03 cơ sở dữ liệu vector

---

Trong hệ thống RAG sản xuất, thông thường bạn sẽ lưu trữ và truy xuất các vectơ từ một

cơ sở dữ liệu được gọi là cơ sở dữ liệu vector.

Hãy cùng khám phá một số thao tác phổ biến với cơ sở dữ liệu vectơ và cách chúng đặt nền móng

để thực hiện truy xuất bên trong ứng dụng RAG.

Cơ sở dữ liệu vectơ là cơ sở dữ liệu được thiết kế từ đầu để lưu trữ dữ liệu nhiều chiều

dữ liệu vectơ và triển khai các thuật toán hướng vectơ như Hàng xóm gần nhất gần đúng

thuật toán bạn vừa thấy.

Chúng trở nên phổ biến vào đầu những năm 2020 để đáp ứng sự sẵn có rộng rãi

của các mô hình ngôn ngữ lớn và sự bùng nổ của các kỹ thuật dựa trên nhúng vector như

Tìm kiếm ngữ nghĩa.

Cơ sở dữ liệu quan hệ tiêu chuẩn hoạt động kém ở Tìm kiếm ngữ nghĩa, trong đó hiệu suất của chúng

gần hơn với thuật toán K-Nearest Neighbors kém hiệu quả cao.

Cơ sở dữ liệu vectơ được tối ưu hóa cho các tác vụ như xây dựng biểu đồ lân cận hỗ trợ HNSW

hoặc tính toán khoảng cách vectơ, từ đó mở rộng quy mô tốt và hoạt động nhanh hơn đáng kể trong hầu hết

các ứng dụng dựa trên vector, đặc biệt là xây dựng hệ thống RAG.

Cơ sở dữ liệu vectơ bạn sẽ sử dụng trong khóa học này có tên là Weaviate.

Đó là cơ sở dữ liệu vectơ nguồn mở phổ biến mà bạn có thể chạy cục bộ hoặc trên đám mây.

Ngoài ra còn có rất nhiều cơ sở dữ liệu vector khác có sẵn trên thị trường.

Nếu bạn chọn một cơ sở dữ liệu vectơ khác cho các dự án trong tương lai, gần như chắc chắn chúng sẽ

cung cấp chức năng rất giống với những gì tôi sẽ giới thiệu với Weaviate.

Mục tiêu ở đây là thực hành một số quy trình công việc phổ biến đối với bất kỳ dự án RAG nào.

Có một số bước liên quan đến việc chuẩn bị sẵn sàng cơ sở dữ liệu vectơ để xử lý tìm kiếm,

một số trong đó được xử lý tự động cho bạn.

Bạn sẽ cần thiết lập cơ sở dữ liệu, tải tài liệu của mình, tạo các vectơ thưa thớt

sẽ hỗ trợ Tìm kiếm từ khóa, tạo các vectơ nhúng dày đặc hỗ trợ Tìm kiếm ngữ nghĩa và cuối cùng

tạo chỉ mục hỗ trợ thuật toán tìm kiếm ANN của bạn, giống như chỉ mục HNSW mà bạn

vừa nhìn thấy.

Tại thời điểm đó, bạn đã sẵn sàng thực hiện tìm kiếm thực tế.

Trong phòng thí nghiệm chưa được phân loại sau đây, bạn sẽ thấy tất cả các bước này một cách chi tiết, nhưng chúng ta hãy

xem qua một số ví dụ để biết cách xử lý các bước này trong Weaviate.

Bước đầu tiên để làm việc với Weaviate là tạo một phiên bản cơ sở dữ liệu hoặc kết nối

đến một cái hiện có.

Bạn sẽ thấy các ví dụ về cách thực hiện điều này trong phòng thí nghiệm chưa được phân loại.

Tiếp theo, bạn sẽ cần tạo một bộ sưu tập để lưu giữ dữ liệu của mình.

Bộ sưu tập tôi đã tạo ở đây được gọi là bài viết và sẽ chứa tiêu đề cũng như nội dung của các bài báo.

Mã này cũng chỉ định rằng mỗi loại dữ liệu sẽ là văn bản.

Quan trọng hơn, lệnh gọi này cho biết nên sử dụng mô hình nhúng hoặc bộ vector hóa nào

để tạo vectơ ngữ nghĩa cho mỗi bài viết được thêm vào.

Bây giờ bạn đã định cấu hình bộ sưu tập của mình, bạn đã sẵn sàng thêm dữ liệu vào đó.

Mã này đang thêm dữ liệu vào bộ sưu tập bằng phương pháp bó của bộ sưu tập.

Batch.addObject thực sự thêm đối tượng vào bộ sưu tập, nhưng nó cũng tính và theo dõi

các lỗi có thể sửa lại sau đó hoặc ngắt vòng lặp nếu có quá nhiều lỗi

đang gặp phải.

Sau khi dữ liệu được chèn vào, bạn đã sẵn sàng thực hiện tìm kiếm vectơ.

Trong truy vấn đầu tiên này, tôi đang chỉ định bộ sưu tập tôi vừa tạo và sau đó bạn có thể chuyển vào

truy vấn văn bản.

Cũng được chuyển vào đây là một yêu cầu siêu dữ liệu cụ thể, giúp bạn rút ngắn khoảng cách.

Đó sẽ là khoảng cách giữa vectơ truy vấn và vectơ đối tượng cho từng đối tượng.

Bạn cũng có thể thực hiện tìm kiếm từ khóa.

Weaviate tự động tạo một chỉ mục đảo ngược cho bạn, cho phép bạn ánh xạ

các từ được sử dụng và tần suất sử dụng trong mỗi tài liệu.

Tại đây bạn có thể thực hiện một truy vấn BM25 đơn giản mà bạn đã học ở mô-đun trước.

Và chúng tôi đã yêu cầu ba tài liệu xếp hạng hàng đầu dựa trên truy vấn này.

Bạn cũng có thể tiếp tục và kết hợp tìm kiếm vectơ với tìm kiếm từ khóa ở dạng kết hợp

tìm kiếm.

Với tìm kiếm kết hợp, điều xảy ra là cả tìm kiếm từ khóa và tìm kiếm vectơ sẽ được thực hiện trong

nền song song.

Và sau đó sử dụng tham số alpha này, hiện được đặt thành 0,25, bạn cân nhắc điểm số

từ tìm kiếm vector và tìm kiếm từ khóa tương ứng.

Vì vậy, với alpha ở mức 0,25, tìm kiếm vectơ có trọng số là 25% và 75% còn lại

để tìm kiếm từ khóa.

Những thứ đó sẽ được xếp hạng lại cho phù hợp và sau đó chúng tôi lấy lại được ba vị trí hàng đầu.

Trong sản xuất và thực tế, đây là phương pháp được đa số các công ty sử dụng vì nó cho phép

bạn cân bằng sự tương tự về mặt ngữ nghĩa của tìm kiếm vectơ và sự tương đồng đối sánh chặt chẽ

của từ khóa tìm kiếm.

Sau đó, bạn cũng có thể tiếp tục và áp dụng các bộ lọc trên này.

Ví dụ: ở đây bạn có thể có bộ lọc được áp dụng cho một thuộc tính cụ thể và

kiểm tra giá trị tại thuộc tính đó.

Nếu nó khớp, đối tượng sẽ vượt qua bộ lọc của chúng tôi và có thể được trả về.

Nếu nó không khớp, nó sẽ không được trả lại.

Vì vậy, toàn bộ vòng lặp từ đầu đến cuối trông giống như thế này.

Bạn định cấu hình cơ sở dữ liệu, sau đó tải và lập chỉ mục dữ liệu của mình và cuối cùng bạn viết một tệp cụ thể

truy vấn bao gồm các bộ lọc tìm kiếm kết hợp.

Đó là thông tin tổng quan hay về cách sử dụng cơ sở dữ liệu vectơ.

Hãy xem Phòng thí nghiệm chưa được phân loại để thực hành tất cả các bước này.