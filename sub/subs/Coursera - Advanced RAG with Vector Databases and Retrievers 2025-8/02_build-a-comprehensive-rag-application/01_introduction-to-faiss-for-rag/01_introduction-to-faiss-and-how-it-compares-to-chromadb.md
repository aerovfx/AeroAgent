# 01 phần giới thiệu về faiss và cách so sánh với chromadb

---

Chào mừng bạn đến với video này, giới thiệu về FAISS và so sánh nó với Chroma DB.

Sau khi xem video này, bạn sẽ có thể mô tả FAISS và Chroma DB, giải thích các

điểm khác biệt chính giữa FAISS và Chroma DB, mô tả các loại chỉ mục khác nhau được sử dụng

bởi FAISS, giải thích các khái niệm về băm nhạy cảm cục bộ và thế giới nhỏ có thể điều hướng theo cấp bậc,

mô tả cách mở rộng FAISS bằng Milvus và hiểu khi nào nên sử dụng FAISS hoặc Chroma DB.

FAISS, viết tắt của Tìm kiếm tương tự AI của Facebook, là một thư viện được Meta tạo ra để tìm kiếm nhanh

tìm kiếm vectơ.

Nó chạy trên một máy duy nhất, sử dụng CPU hoặc GPU.

Bạn sử dụng nó bằng cách viết mã vì không có cơ sở dữ liệu hoặc máy chủ tích hợp.

Đó là lý tưởng khi bạn muốn có toàn quyền kiểm soát và hiệu suất cao.

Chroma DB là cơ sở dữ liệu vectơ được xây dựng cho các trường hợp sử dụng AI.

Nó lưu trữ cả vectơ và siêu dữ liệu như thẻ hoặc mô tả.

Bạn có thể chạy nó cục bộ hoặc như một máy chủ.

Nó hoạt động tốt với các công cụ như LangChain, giúp dễ dàng tích hợp.

Bây giờ hãy so sánh hai công nghệ và xem chúng khác nhau như thế nào.

FAISS là một thư viện, trong khi Chroma DB là cơ sở dữ liệu đầy đủ.

FAISS được thiết kế để vận hành một nút và không cung cấp khả năng chia tỷ lệ phân tán gốc.

Ngược lại, Chroma DB hỗ trợ cả triển khai một nút và phân tán, mang lại sự rõ ràng

con đường mở rộng quy mô cho khối lượng công việc lớn hơn.

FAISS cung cấp nhiều tùy chọn lập chỉ mục, trong khi Chroma DB chỉ hỗ trợ Điều hướng phân cấp

Thế giới nhỏ, hay HNSW.

FAISS không hỗ trợ siêu dữ liệu nguyên bản, trong khi Chroma DB hỗ trợ lưu trữ và lọc siêu dữ liệu

dựa trên thẻ siêu dữ liệu.

Và cả FAISS và Chroma DB đều hoạt động với LangChain và LlamaIndex.

Chỉ mục giúp bạn tìm kiếm qua vectơ hiệu quả hơn.

FAISS cung cấp một số loại chỉ mục khác nhau và mỗi loại chỉ mục sẽ cân bằng tốc độ, bộ nhớ,

và độ chính xác khác nhau.

Chỉ số phẳng so sánh khoảng cách, sử dụng khoảng cách Euclide hoặc tích chấm,

giữa việc nhúng truy vấn và việc nhúng mọi vectơ trong kho vectơ bằng cách sử dụng

một cuộc tìm kiếm vũ lực.

Sau đó nó truy xuất "k vectơ gần nhất", được sắp xếp từ gần nhất đến xa nhất.

Đây là một cách tiếp cận rất chính xác nhưng lại rất chậm đối với các tập dữ liệu lớn.

Chỉ mục tệp đảo ngược, còn được gọi là chỉ mục IVF, tăng tốc tìm kiếm vectơ bằng cách phân cụm

vectơ sử dụng các phương pháp như k-means, tạo thành các ô Voronoi xung quanh centroid.

Mỗi ô chứa các vectơ gần tâm nhất của nó.

Khi một vectơ truy vấn được giới thiệu, việc tìm kiếm được giới hạn ở các vectơ trong các ô gần nhất,

giảm bớt tính toán.

Điều này nhanh hơn chỉ số phẳng, nhưng có thể làm giảm độ chính xác một chút do một số chỉ số gần đó

vectơ có thể ở các ô khác.

Băm nhạy cảm cục bộ, hay LSH, sử dụng các hàm băm ánh xạ các vectơ tương tự tới

cùng một thùng.

Điều này cho phép tìm kiếm nhanh và tiết kiệm bộ nhớ.

Khi một vectơ truy vấn được đưa vào, LSH sẽ tìm kiếm các vectơ trong các nhóm phù hợp nhất.

Nó đặc biệt hữu ích cho dữ liệu thưa thớt nhiều chiều như nhúng văn bản, mặc dù

nó không phải là phương pháp nhanh nhất và chính xác nhất.

Thế giới nhỏ có thể điều hướng theo thứ bậc, hay HNSW, tổ chức các vectơ thành một hệ thống phân cấp các lớp.

Các lớp trên cùng thưa thớt và chỉ chứa một vài vectơ.

Các lớp này hoạt động giống như đường cao tốc, giúp thuật toán tìm kiếm nhanh chóng tiến gần đến

vùng mục tiêu.

Biểu đồ trở nên dày đặc hơn khi tìm kiếm đi xuống các lớp thấp hơn.

Các lớp này cung cấp các kết nối cục bộ chi tiết hơn, cho phép thuật toán tinh chỉnh tìm kiếm của nó.

Việc tìm kiếm bắt đầu ở lớp trên cùng và di chuyển xuống dưới, sử dụng ứng cử viên tốt nhất từ

mỗi lớp làm điểm vào cho lớp tiếp theo.

Cách tiếp cận theo lớp này giúp HNSW vừa nhanh vừa chính xác, đặc biệt đối với các tập dữ liệu lớn.

FAISS rất mạnh cho tìm kiếm vectơ cục bộ, hiệu suất cao, nhưng nó thiếu các tính năng như

hỗ trợ siêu dữ liệu và chia tỷ lệ phân tán.

Milvus, một cơ sở dữ liệu vectơ, sử dụng FAISS làm một trong những công cụ lập chỉ mục cốt lõi của nó và bổ sung thêm những công cụ này

khả năng còn thiếu.

Nó hỗ trợ lưu trữ và lọc siêu dữ liệu cùng với các vectơ, cho phép truy vấn kết hợp

chẳng hạn như "Tìm các mặt hàng tương tự dưới $50".

Milvus cũng hỗ trợ triển khai phân tán, phù hợp cho sản xuất quy mô lớn

môi trường.

Vậy khi nào bạn nên sử dụng FAISS, Chroma DB hoặc Milvus?

Sử dụng FAISS khi bạn muốn có toàn quyền kiểm soát và hiệu suất trên một máy.

Sử dụng Chroma DB để phát triển AI nhanh chóng bằng cách sử dụng nguyên mẫu và cho các truy vấn giàu siêu dữ liệu.

Sử dụng Milvus khi bạn cần cơ sở dữ liệu vectơ có thể mở rộng, sẵn sàng sản xuất với tính năng tìm kiếm kết hợp và phân phối

khả năng.

Trong video này, bạn đã học được rằng…

FAISS và Chroma DB được xây dựng cho các mục tiêu khác nhau.

FAISS cung cấp cho bạn quyền kiểm soát việc lập chỉ mục nhưng thiếu siêu dữ liệu và phân phối theo mặc định.

Chroma DB dễ triển khai hơn và hỗ trợ siêu dữ liệu nhưng có ít tùy chọn lập chỉ mục hơn.

Bạn có thể mở rộng FAISS bằng Milvus để có khả năng mở rộng và siêu dữ liệu.

Bạn có thể mở rộng cả hai công cụ bằng LangChain hoặc LlamaIndex cho các đường dẫn RAG.

Và, bạn nên chọn công cụ phù hợp dựa trên quy mô, độ phức tạp và cơ sở hạ tầng của dự án.