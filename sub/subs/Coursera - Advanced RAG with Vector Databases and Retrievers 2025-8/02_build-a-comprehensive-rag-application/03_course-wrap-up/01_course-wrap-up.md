# Tổng kết 01 khóa học

---

[ÂM NHẠC]

Xin chúc mừng, bạn đã kết thúc khóa học này. Chúng ta hãy dành một chút thời gian để suy ngẫm

trên hành trình của mình, nơi bạn đã đạt được một số kiến thức cần thiết về cách sử dụng cơ sở dữ liệu vectơ và các công cụ nâng cao

công cụ truy xuất trong quá trình phát triển các ứng dụng Thế hệ truy xuất tăng cường (hoặc RAG).

Hãy xem lại một số khía cạnh chính của những gì bạn đã học được trong suốt khóa học.

Trình truy xuất LangChain là giao diện trả về tài liệu dựa trên truy vấn phi cấu trúc.

Nó không nhất thiết phải lưu trữ tài liệu vì mục đích của nó là lấy chúng hoặc các đoạn của chúng.

Trình truy xuất LangChain chấp nhận truy vấn chuỗi làm đầu vào và trả về danh sách tài liệu hoặc khối làm đầu ra.

Công cụ truy xuất dựa trên cửa hàng vector lấy tài liệu từ cơ sở dữ liệu vector và có thể

được tạo trực tiếp từ đối tượng lưu trữ vectơ bằng phương thức truy xuất bằng cách sử dụng tìm kiếm tương tự

hoặc mức độ liên quan cận biên tối đa (MMR).

Loại công cụ truy tìm đơn giản nhất, công cụ truy xuất dựa trên cửa hàng vector,

lấy tài liệu từ cơ sở dữ liệu vector.

Trình truy xuất nhiều truy vấn tương tự như trình truy xuất dựa trên cửa hàng vector, ngoại trừ việc nó sử dụng LLM để

tạo các phiên bản truy vấn khác nhau, tạo ra tập hợp tài liệu được truy xuất phong phú hơn.

Trình truy xuất tự truy vấn chuyển đổi truy vấn thành hai thành phần:

một chuỗi để tra cứu về mặt ngữ nghĩa và một bộ lọc siêu dữ liệu đi kèm với nó.

Trình truy xuất tài liệu gốc có hai bộ tách văn bản: một bộ tách gốc có chức năng phân tách

văn bản thành các phần lớn cần truy xuất và một bộ chia con giúp chia tài liệu

thành các phần nhỏ để tạo ra các phần nhúng có ý nghĩa.

Trong quá trình truy xuất, trình truy xuất tài liệu gốc trước tiên sẽ tìm nạp các phần nhỏ hơn,

tra cứu ID gốc của chúng và trả về tài liệu lớn hơn trong đó có các phần nhỏ.

VectorStoreIndex trong LlamaIndex lưu trữ các phần nhúng dữ liệu vectơ cho mỗi đoạn,

phù hợp nhất cho việc truy xuất ngữ nghĩa,

và thường được sử dụng trong các quy trình liên quan đến các mô hình ngôn ngữ lớn.

DocumentSummaryIndex tạo và lưu trữ các bản tóm tắt tài liệu.

Những bản tóm tắt này được sử dụng để lọc tài liệu trước khi lấy ra toàn bộ nội dung.

Loại chỉ mục này rất hữu ích khi làm việc với các bộ tài liệu lớn và đa dạng.

KeyTableIndex trích xuất các từ khóa từ tài liệu và ánh xạ chúng tới nội dung cụ thể

các khối và rất hữu ích trong các tình huống tìm kiếm kết hợp hoặc dựa trên quy tắc.

Vector Index Retriever sử dụng các vectơ nhúng để tìm nội dung liên quan đến ngữ nghĩa,

và lý tưởng cho các đường ống RAG và tìm kiếm có mục đích chung.

BM25 Retriever là một phương pháp dựa trên từ khóa để xếp hạng tài liệu.

Nó truy xuất nội dung dựa trên kết quả khớp từ khóa chính xác thay vì sự tương đồng về ngữ nghĩa.

Trình truy xuất chỉ mục tóm tắt tài liệu sử dụng tóm tắt tài liệu thay vì tài liệu thực tế

để tìm nội dung có liên quan bằng cách sử dụng LLM hoặc sự tương đồng về ngữ nghĩa.

Auto Merge Retriever bảo toàn ngữ cảnh trong các tài liệu dài bằng cách sử dụng cấu trúc phân cấp

và sử dụng phân đoạn theo cấp bậc để chia tài liệu thành các nút cha và nút con.

Công cụ truy xuất đệ quy tuân theo các mối quan hệ giữa các nút và sử dụng các tham chiếu như

trích dẫn trong các bài báo học thuật hoặc các liên kết siêu dữ liệu.

Trình truy xuất kết hợp truy vấn kết hợp các kết quả từ các trình truy xuất khác nhau bằng cách sử dụng các chiến lược tổng hợp.

Kết hợp xếp hạng đối ứng kết hợp các danh sách được xếp hạng bằng cách gán điểm cao hơn cho các tài liệu

xuất hiện gần đầu bất kỳ danh sách nào.

Tổng hợp điểm tương đối chuẩn hóa điểm số trong mỗi bộ kết quả bằng cách chia điểm tối đa.

Fusion-Based Fusion sử dụng các kỹ thuật thống kê, chẳng hạn như chuẩn hóa điểm z hoặc

xếp hạng phần trăm, để kết hợp kết quả.

Tìm kiếm tương tự AI của Facebook (hoặc FAISS) là một thư viện do Meta tạo ra để tìm kiếm vectơ nhanh.

Đó là lý tưởng khi bạn muốn có toàn quyền kiểm soát và hiệu suất cao.

Chroma DB là cơ sở dữ liệu vectơ được xây dựng cho các trường hợp sử dụng AI.

Nó lưu trữ cả vectơ và siêu dữ liệu, chẳng hạn như thẻ hoặc mô tả.

FAISS là một thư viện, trong khi Chroma DB là cơ sở dữ liệu đầy đủ.

FAISS được thiết kế để vận hành một nút và không cung cấp khả năng chia tỷ lệ phân tán gốc.

Chroma DB hỗ trợ cả triển khai một nút và phân tán cho khối lượng công việc lớn.

FAISS cung cấp nhiều tùy chọn lập chỉ mục,

trong khi Chroma DB chỉ hỗ trợ Thế giới nhỏ có thể điều hướng theo cấp bậc (hoặc HNSW).

FAISS vốn không hỗ trợ siêu dữ liệu,

trong khi Chroma DB hỗ trợ lưu trữ siêu dữ liệu và lọc dựa trên thẻ siêu dữ liệu.

Cả FAISS và Chroma DB đều hoạt động với LangChain và LlamaIndex.

Chỉ mục giúp bạn tìm kiếm qua vectơ hiệu quả hơn.

FAISS cung cấp một số loại chỉ mục khác nhau.

Chỉ số phẳng so sánh khoảng cách, sử dụng khoảng cách Euclide hoặc tích số chấm, giữa

nhúng truy vấn và nhúng mọi vectơ trong kho vectơ bằng cách sử dụng tìm kiếm mạnh mẽ.

Sau đó nó truy xuất 'k-vectơ gần nhất', được sắp xếp từ gần nhất đến xa nhất.

Chỉ mục tệp đảo ngược (hoặc chỉ mục IVF) tăng tốc tìm kiếm vectơ bằng cách phân cụm các vectơ bằng cách sử dụng

các phương pháp như k-mean, hình thành các ô Voronoi xung quanh centroid.

Mỗi ô chứa các vectơ gần tâm nhất của nó.

Băm nhạy cảm cục bộ (hoặc LSH) sử dụng các hàm băm ánh xạ các vectơ tương tự vào cùng một nhóm.

LSH tìm kiếm các vectơ trong các nhóm phù hợp gần nhất, cho phép tìm kiếm nhanh và tiết kiệm bộ nhớ.

Nó đặc biệt hữu ích cho dữ liệu thưa thớt có chiều cao như nhúng văn bản.

Thế giới nhỏ có thể điều hướng theo cấp bậc (hoặc HNSW) tổ chức các vectơ thành một hệ thống phân cấp các lớp.

Các lớp trên cùng thưa thớt và chỉ chứa một vài vectơ.

Các lớp thấp hơn cung cấp các kết nối cục bộ chi tiết hơn, cho phép thuật toán tinh chỉnh tìm kiếm của nó.

Việc tìm kiếm bắt đầu ở lớp trên cùng và di chuyển xuống dưới,

sử dụng ứng cử viên tốt nhất từ mỗi lớp làm điểm vào cho lớp tiếp theo.

Cách tiếp cận theo lớp này giúp HNSW vừa nhanh vừa chính xác, đặc biệt đối với các tập dữ liệu lớn.

Bây giờ bạn đã xem lại một số ý tưởng cơ bản được trình bày trong khóa học này,

ghi nhớ bảng chú giải thuật ngữ và bảng ghi chú của mỗi mô-đun.

Bạn có thể sử dụng những nội dung này để tham khảo nhanh phần lớn những gì bạn đã học được.

Nếu bạn chưa đăng ký Chứng chỉ chuyên nghiệp IBM RAG và Agentic AI của chúng tôi

Chương trình mà khóa học này là một phần, chúng tôi khuyến khích bạn làm như vậy.

Tùy thuộc vào lịch trình của bạn và số lượng các khóa học trong chương trình,

chương trình này sẽ mất khoảng 1-2 tháng để hoàn thành.

Mỗi chương trình bao gồm nhiều phòng thí nghiệm thực hành và một dự án cuối cùng.

Các Chương trình Chứng chỉ Chuyên nghiệp cũng có một khóa học cơ bản để bạn tổng hợp

và giới thiệu tất cả các kỹ năng bạn đã học được trong suốt chương trình.

Chúc mừng bạn đã hoàn thành khóa học này và cảm ơn bạn đã trở thành một phần của hành trình học tập này.

Bước tiếp theo, chúng tôi khuyên bạn nên tiếp tục hành trình học tập và tiếp tục áp dụng các kỹ năng mới của mình.

Đây là lời chúc tốt đẹp nhất cho bạn!

[ÂM NHẠC]