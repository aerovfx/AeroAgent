# 02 loại cơ sở dữ liệu vector

---

Chào mừng đến với video về

các loại cơ sở dữ liệu vector

Sau khi xem video này,

bạn sẽ có thể

phân loại phổ biến

cơ sở dữ liệu vector dựa

về loại của chúng,

năng lực và nhà cung cấp.

Tương phản các chức năng

và đặc điểm của

cơ sở dữ liệu vector chuyên dụng với

cơ sở dữ liệu hỗ trợ

tìm kiếm vectơ,

và xác định các nhà cung cấp phổ biến của

cơ sở dữ liệu vector chuyên dụng và

cơ sở dữ liệu hỗ trợ

tìm kiếm vectơ.

Đúng như tên gọi,

cơ sở dữ liệu vector trong bộ nhớ

lưu trữ vectơ

ngay trong bộ nhớ.

Cách tiếp cận này cho phép nhanh chóng

hoạt động đọc và ghi,

làm cho những cơ sở dữ liệu này trở nên lý tưởng cho

các ứng dụng yêu cầu

truy cập dữ liệu nhanh chóng,

bao gồm cả phân tích thời gian thực

và các hệ thống khuyến nghị.

Cơ sở dữ liệu trong bộ nhớ

cơ sở dữ liệu vector

bao gồm RedisAI và Torchserve.

Ví dụ: RedisAI là

một vectơ trong bộ nhớ

cơ sở dữ liệu hỗ trợ

lưu trữ và truy vấn

vectơ cho các nhiệm vụ như

tìm kiếm tương tự,

phân loại, phân cụm.

Tiếp theo, dựa trên đĩa

cơ sở dữ liệu vector

lưu trữ các vectơ trên đĩa.

Phương pháp này phù hợp với tập dữ liệu lớn

vượt quá dung lượng bộ nhớ.

Những cơ sở dữ liệu này sử dụng

lập chỉ mục phức tạp và

nén

kỹ thuật để nâng cao

lưu trữ và truy xuất

hiệu quả.

Vectơ dựa trên đĩa

cơ sở dữ liệu bao gồm

Làm phiền, Milvus và ScaNN.

Ví dụ như Làm phiền,

viết tắt của xấp xỉ

hàng xóm gần nhất ồ vâng,

là một cơ sở dữ liệu

trong thể loại này.

Làm phiền lưu trữ vectơ trên đĩa và

xây dựng các chỉ mục cho nhanh chóng

các ứng dụng truy xuất.

Làm phiền báo cáo rằng

nó được xây dựng cho

nhanh gần đúng gần nhất

tìm kiếm hàng xóm

và sẵn sàng cho

hệ thống khuyến nghị

và thông tin

các ứng dụng truy xuất.

Vectơ phân phối

cơ sở dữ liệu lan rộng

dữ liệu vectơ trên

nhiều nút hoặc máy chủ.

Vectơ phân phối

cơ sở dữ liệu cung cấp

khả năng mở rộng theo chiều ngang

và khả năng chịu lỗi,

làm cho những cơ sở dữ liệu này

thích hợp để quản lý

tập dữ liệu khổng lồ và

nhiệm vụ thông lượng cao.

Cơ sở dữ liệu phân tán

các nhà cung cấp bao gồm FAISS,

Elaticsearch với Vector

Plugin và Dask-ML.

Một ví dụ đáng chú ý là

Điểm tương đồng AI của Facebook

tìm kiếm hoặc FAISS,

đó là một phân phối

và cơ sở dữ liệu được tối ưu hóa

được thiết kế cho

tìm kiếm tương tự trong

không gian nhiều chiều

và phân vùng dữ liệu

qua các nút để đạt được

tìm kiếm có thể mở rộng và nhanh chóng.

Cơ sở dữ liệu vectơ dựa trên đồ thị

dữ liệu mô hình dưới dạng đồ thị

với các nút và

các cạnh đại diện

thuộc tính vector hoặc nhúng.

Những cơ sở dữ liệu này

xuất sắc trong việc nắm bắt

những mối quan hệ phức tạp và

tạo điều kiện thuận lợi cho việc phân tích biểu đồ.

Cơ sở dữ liệu vectơ dựa trên đồ thị

các nhà cung cấp bao gồm Neo4j,

Amazon Neptune và TigerGraph.

Ví dụ: Neo4j là

cơ sở dữ liệu dựa trên đồ thị

hỗ trợ

lưu trữ vectơ dưới dạng nút

thuộc tính hoặc thuộc tính.

Neo4j cho phép truy vấn và

phân tích dữ liệu vector trong

bối cảnh của một biểu đồ.

Hỗ trợ khả năng Neo4j

phân tích mạng xã hội,

hệ thống khuyến nghị,

và đồ thị kiến thức.

Tiếp theo chúng ta cùng tìm hiểu về

cơ sở dữ liệu vector chuỗi thời gian.

Cơ sở dữ liệu vector chuỗi thời gian

quản lý dữ liệu được thu thập

theo các khoảng thời gian và

biểu diễn dữ liệu này dưới dạng vectơ.

Các cơ sở dữ liệu này phục vụ

như những công cụ mạnh mẽ

để phân tích thời gian

mô hình và sự bất thường.

Một số cơ sở dữ liệu đáng chú ý trong này

danh mục bao gồm InfluxDB,

TimescaleDB và Prometheus.

InfluxDB, một nhà cung cấp trong lĩnh vực này

cho phép lưu trữ vector

cùng với dữ liệu được đóng dấu thời gian.

Khả năng này

cho phép truy vấn và

phân tích chuỗi thời gian

vectơ để phát hiện các mẫu,

dự báo xu hướng và theo dõi

số liệu hệ thống trong IoT,

giám sát và sự bất thường

các ứng dụng phát hiện

Tiếp theo, hãy đối chiếu

cơ sở dữ liệu vector chuyên dụng

với cơ sở dữ liệu

hỗ trợ tìm kiếm vector.

Họ khác nhau từ mỗi

khác. Hãy tìm hiểu thêm.

Đúng như tên gọi,

cơ sở dữ liệu vector chuyên dụng

là những hệ thống sử dụng

đặc biệt của riêng họ

đặc điểm

và tối ưu hóa để lưu trữ,

lập chỉ mục, truy vấn và phân tích

lượng lớn dữ liệu vectơ

một cách nhanh chóng và chính xác.

Tìm kiếm tương tự, phân cụm,

và phân loại công việc nhiều hơn

sử dụng hiệu quả

cơ sở dữ liệu vectơ.

Tiếp theo, khám phá

đặc điểm thiết yếu

cơ sở dữ liệu vector chuyên dụng.

Đầu tiên, để lưu trữ và

truy xuất vectơ nhanh chóng,

vectơ chuyên dụng

cơ sở dữ liệu thường sử dụng

cấu trúc dữ liệu độc đáo

như các chỉ mục đảo ngược,

lượng tử hóa sản phẩm, và

địa phương nhạy cảm

băm hoặc LSH.

Các cơ sở dữ liệu này hỗ trợ

phép toán vectơ

như tìm kiếm hàng xóm gần nhất,

tìm kiếm tương tự và

tính toán khoảng cách,

cho phép người dùng thực hiện các thao tác phức tạp

tìm kiếm trên dữ liệu vector.

Vectơ chuyên dụng

cơ sở dữ liệu được thực hiện để

có khả năng mở rộng để

người dùng có thể lưu trữ

và truy vấn các tập dữ liệu vector lớn

nhanh chóng trên các cụm

hoặc các hệ thống phân tán.

Những cơ sở dữ liệu này đặt tốc độ lên hàng đầu,

sử dụng các thuật toán tối ưu hóa và

cấu trúc dữ liệu để có được

câu trả lời nhanh cho các truy vấn,

ngay cả đối với dữ liệu vectơ với

rất nhiều kích thước,

và người dùng có thể thay đổi

các tham số để lập chỉ mục và

đang tìm kiếm để có được

kết quả tốt nhất cho

trường hợp sử dụng nhất định

hoặc các loại dữ liệu.

Một số hiện đang phổ biến

cơ sở dữ liệu vector chuyên dụng

bao gồm Faiss, (Facebook

Tìm kiếm tương tự AI),

Làm phiền (Gần nhất gần nhất

Hàng xóm Oh Yeah) và Milvus.

Tiếp theo, ngược lại, hãy xem xét

các công nghệ cơ sở dữ liệu khác như thế nào

hỗ trợ tìm kiếm vector.

Cơ sở dữ liệu đó

hỗ trợ tìm kiếm vector

đều đặn

hệ thống cơ sở dữ liệu

hoặc khung xử lý dữ liệu

cho phép bạn lưu trữ và

truy vấn dữ liệu vectơ.

Mặc dù những cơ sở dữ liệu này có thể

không được thực hiện cho

hoạt động vectơ,

họ có các công cụ hoặc tiện ích bổ sung

điều đó cho phép người dùng

thực hiện tìm kiếm vector cùng

với các loại truy vấn khác.

Vậy có những đặc điểm gì

quan trọng đối với các cơ sở dữ liệu này?

Những cơ sở dữ liệu này cho phép

người dùng lưu trữ dữ liệu vectơ

như một phần của mô hình dữ liệu của họ.

Dữ liệu này có thể được

được lưu trữ dưới dạng các đốm màu,

mảng hoặc người dùng-

các loại được xác định hoặc UDT.

Một số cơ sở dữ liệu cho phép bạn tổ chức

dữ liệu vector sử dụng tiêu chuẩn

hoặc cấu trúc chỉ mục tùy chỉnh.

Điều này làm cho nó dễ dàng

lấy vectơ dựa trên

các số liệu như độ tương tự

hoặc khoảng cách.

Nhiều cơ sở dữ liệu có tiện ích bổ sung

hoặc tích hợp

cho phép người dùng lấy

hành động trên dữ liệu vector

sử dụng đặc biệt

thư viện hoặc plug-in.

Ví dụ, khi thực hiện

tìm kiếm tương tự hoặc

các nhiệm vụ khác liên quan đến vector,

người dùng có thể sử dụng các công cụ bên ngoài.

Mặc dù những cơ sở dữ liệu này

cho phép tìm kiếm vector,

họ có thể không

nhanh hay là tốt

được tối ưu hóa chuyên dụng

cơ sở dữ liệu vectơ.

Người dùng phải cân nhắc

chức năng,

hiệu suất và khả năng mở rộng

phù hợp với nhu cầu của họ.

Dưới đây là một số nhà cung cấp cơ sở dữ liệu

hỗ trợ tìm kiếm vector.

Đầu tiên, SingleStore với

xử lý cơ sở dữ liệu vector

hoạt động với IBM watsonx.ai.

Tiếp theo, Elaticsearch

có phần bổ sung vector của nó.

PostgreSQL bao gồm

Thêm PostGIS của nó

bật cho các vectơ trong không gian.

MySQL có chỉ mục riêng

để tìm kiếm vectơ.

RedisAI thực hiện vector

chức năng trong bộ nhớ,

và Apache MongoDB và

Vectơ hỗ trợ Apache Cassandra

tìm kiếm với các lược đồ linh hoạt.

Trong video này, bạn đã học được rằng

cơ sở dữ liệu dựa trên vector

các loại bao gồm trong bộ nhớ,

dựa trên đĩa, phân tán,

dựa trên đồ thị,

và cơ sở dữ liệu dựa trên thời gian.

Cơ sở dữ liệu dựa trên vector,

hiệu suất tốc độ

cho các hệ thống khuyến nghị,

phân tích mạng xã hội,

đồ thị kiến thức

(phân tích biểu đồ) và

các công việc phức tạp khác.

Cơ sở dữ liệu vector chuyên dụng

sử dụng cấu trúc dữ liệu,

chỉ số đảo ngược,

lượng tử hóa sản phẩm,

và băm nhạy cảm với địa phương

LSH cung cấp khả năng mở rộng,

mang lại tốc độ và

tùy biến nâng cao.

Vectơ cơ sở dữ liệu phổ biến

các nhà cung cấp cơ sở dữ liệu bao gồm FAISS,

Làm phiền và Milvus.

Cơ sở dữ liệu hỗ trợ

tìm kiếm vector là

hệ thống cơ sở dữ liệu thông thường hoặc

khung xử lý dữ liệu

cho phép bạn lưu trữ dữ liệu dưới dạng BLOB,

mảng hoặc kiểu do người dùng xác định.

Các nhà cung cấp đáng chú ý hỗ trợ

tìm kiếm vector bao gồm

SingleStore với

hỗ trợ cho IBM watsonx.ai,

Elaticsearch,

PostgreSQL, MySQL,

RedisAI, Apache MongoDB,

và Apache Cassandra.