# 04 snowsight-phát triển-môi trường

---

Được rồi, bây giờ bạn đã xây dựng và khởi chạy ứng dụng Streamlit trên máy cục bộ của mình,

bạn sẽ mang trải nghiệm đó vào Snowflake và đưa mọi thứ lên một tầm cao mới.

Trong video này, bạn sẽ có được chuyến tham quan chuyên sâu đầu tiên về SnowSite,

đó là giao diện dựa trên web của Snowflake.

Đây là nơi bạn sẽ truy cập dữ liệu của mình, viết mã Python,

xây dựng các ứng dụng Streamlit và về cơ bản là hoạt động trong phần còn lại của khóa học.

Trước khi đi sâu vào, hãy nói về Snowflake là gì và bạn sẽ sử dụng nó như thế nào.

Snowflake là trung tâm chỉ huy dữ liệu tất cả trong một của bạn trên đám mây.

Nó lưu trữ dữ liệu của bạn, chạy các truy vấn của bạn và xử lý các công việc nặng nhọc,

tự động tăng hoặc giảm tỷ lệ, tùy thuộc vào những gì bạn cần.

Không cần phần cứng, không cần phải đau đầu khi thiết lập.

Đằng sau hậu trường, Snowflake sử dụng kho ảo.

Đây là những công cụ tính toán độc lập xử lý công việc của bạn song song,

điều đó có nghĩa là nhiều tác vụ có thể chạy cùng lúc mà không làm chậm tác vụ khác.

Bản thân dữ liệu của bạn nằm trong bộ lưu trữ đám mây như AWS S3 hoặc Google Cloud Storage.

Nhưng trên Snowflake, dữ liệu của bạn được lưu trữ ở chế độ tối ưu,

định dạng nén giúp tìm kiếm nhanh và dễ dàng mở rộng quy mô.

Phần Snowflake mà bạn sẽ tương tác chủ yếu trong khóa học này được gọi là SnowSite.

Đó là không gian làm việc dựa trên web và sẽ là trung tâm chính để bạn khám phá dữ liệu,

viết mã và xây dựng các ứng dụng hỗ trợ Gen AI.

Trong SnowSite, bạn sẽ dành phần lớn thời gian làm việc trong cơ sở dữ liệu nơi dữ liệu của bạn được lưu trữ,

sổ ghi chép nơi bạn sẽ phân tích dữ liệu bằng mã, cho dù đó là SQL hay Python,

Streamlet nơi bạn sẽ xây dựng và xem trước giao diện ứng dụng của mình.

Trong SnowSite, bạn có các công cụ mạnh mẽ để lựa chọn.

SQL là ngôn ngữ tiêu chuẩn để truy vấn dữ liệu.

Bạn sử dụng nó để khám phá và tóm tắt các tập dữ liệu của mình.

Snowpark là một khung dành cho nhà phát triển để sử dụng Python, Java hoặc Scala trực tiếp bên trong Snowflake.

Nó hoạt động giống như gấu trúc và chạy mã nơi dữ liệu của bạn tồn tại, an toàn và có quy mô lớn.

Cortex là bộ công cụ Gen AI được quản lý hoàn toàn được tích hợp trong Snowflake.

Bạn có thể gọi các mô hình ngôn ngữ lớn, chạy phân tích cảm xúc, tạo văn bản,

và xây dựng hệ thống giá đỡ bằng cách sử dụng các hàm SQL hoặc Python tích hợp sẵn.

Và Snowflake Copilot là trợ lý mã hóa AI cho các truy vấn SQL.

Bạn bắt đầu bằng cách khám phá dữ liệu của mình trong SnowSite,

sau đó sử dụng SQL hoặc Python với Snowpark để phân tích vào sổ ghi chép.

Khi bạn sẵn sàng chia sẻ thông tin chi tiết của mình, chẳng hạn như với trang tổng quan tương tác,

bạn sẽ sử dụng Streamlet để xây dựng và triển khai nguyên mẫu của mình bên trong Snowflake hoặc trên Đám mây cộng đồng Streamlet.

Cortex hỗ trợ ứng dụng của bạn với các tính năng Gen AI như phân tích cảm xúc và tạo văn bản.

Vì sự hỗ trợ của Copilot dành cho Python vẫn đang được phát triển,

chúng tôi khuyên bạn nên sử dụng các công cụ như Cloud hoặc ChatGBT để trợ giúp bạn khi làm việc bằng Python.

Để đăng nhập vào SnowSite, hãy mở trình duyệt của bạn và truy cập...

Nhập số nhận dạng tài khoản của bạn, trông giống như thế này,

và có thể được tìm thấy trong email xác nhận mà bạn nhận được trong lần đăng ký đầu tiên.

Sau đó đăng nhập bằng thông tin đăng nhập Snowflake của bạn.

Chào mừng đến với SnowSite!

Đây là trung tâm chỉ huy tất cả trong một của bạn để khám phá dữ liệu, xây dựng sổ ghi chép và tạo ứng dụng.

Nhìn vào thanh bên trái để tìm các công cụ điều hướng chính của bạn.

Hãy bắt đầu bằng cách nhấp vào Dữ liệu để xem tất cả cơ sở dữ liệu, bảng và lược đồ của bạn sẽ nằm ở đâu.

Khi mở tab Dữ liệu, bạn sẽ thấy danh sách mọi cơ sở dữ liệu đã được tạo,

chẳng hạn như các cơ sở dữ liệu Bông tuyết mẫu này mà bạn có thể sử dụng để thực hành.

Sau khi tạo cơ sở dữ liệu Avalanche, bạn sẽ thấy nó được liệt kê ở đây.

Bây giờ, chúng ta sẽ khám phá cái mà tôi đã thiết lập.

Mỗi cơ sở dữ liệu giống như một thư mục dự án chính,

chỉ cần nhấp vào cơ sở dữ liệu để xem tất cả các lược đồ chứa trong đó.

Bên trong cơ sở dữ liệu Avalanche, bạn sẽ thấy cùng dữ liệu mà bạn đã sử dụng trong Mô-đun 1,

nhưng bây giờ được lưu trữ theo cách được tối ưu hóa cho hiệu suất.

Dữ liệu đó đến từ hơn 100 tệp Word docx riêng biệt,

và được làm sạch, hợp nhất và nạp vào Snowflake.

Bạn sẽ học cách làm điều đó sớm thôi.

Đây là cách Snowflake tổ chức dữ liệu.

Cơ sở dữ liệu là vùng chứa cấp cao nhất,

lược đồ giống như các thư mục con nhóm các loại dữ liệu khác nhau,

và bảng là nơi dữ liệu thực sự tồn tại.

Tiếp theo, nhấp vào lược đồ Avalanche để mở trang chi tiết của nó.

Tại đây, bạn có thể xem thông tin về người có quyền truy cập vào lược đồ đó và các cài đặt quản trị viên liên quan.

Từ đây, nhấp vào tab Bảng.

Điều này sẽ hiển thị cho bạn tất cả các bảng trong lược đồ đó,

như đánh giá của khách hàng và dữ liệu vận chuyển.

Bạn có thể nhấp vào bất kỳ bảng nào để mở nó,

sau đó bạn sẽ được hiển thị các tab này.

Tab Chi tiết bảng,

bao gồm cài đặt quản trị viên và quyền cho bảng.

Tab Cột, liệt kê từng tên cột, kiểu dữ liệu và mô tả.

Và tab Xem trước dữ liệu, hiển thị mẫu dữ liệu của bạn

và thông tin về kho điện toán mà nó sử dụng để chạy truy vấn.

Chế độ xem này cung cấp cho bạn mọi thứ bạn cần để hiểu cấu trúc dữ liệu của mình,

không cần mã.

Bây giờ, chúng ta hãy xem nhanh một số phần khác của Snowflake mà bạn sẽ sử dụng.

Trên thanh bên điều hướng bên trái, nhấp vào menu Dự án.

Menu này là menu bạn sẽ muốn sử dụng

khi tạo bất kỳ loại quy trình công việc mới nào trong Snowflake,

chẳng hạn như viết truy vấn và mã.

Chúng tôi sẽ làm việc rất nhiều với Bảng tính bông tuyết,

nơi bạn có thể viết và chạy mã SQL và Python

trực tiếp bên trong môi trường Bông tuyết của bạn.

Đó là một nơi tuyệt vời để kiểm tra các truy vấn hoặc phân tích nhanh.

Để mở Bảng tính SQL Bông tuyết,

nhấp vào Bảng tính trong thanh bên điều hướng,

sau đó nhấp vào Bảng tính Plus ở trên cùng bên phải để tạo một bảng tính mới.

Tiếp theo, từ menu điều hướng bên trái, hãy đi tới Notebooks.

Đây là nơi bạn sẽ thực hiện hầu hết các phân tích nhiều bước của mình.

Không giống như Bảng tính, Sổ ghi chép cho phép bạn kết hợp văn bản, SQL và Python

tất cả ở cùng một nơi, giống như Sổ tay Jupyter gốc của Snowflake.

Để mở Notebook Bông tuyết mới,

nhấp vào Sổ tay trong thanh bên điều hướng,

sau đó nhấp vào Plus Notebook ở trên cùng bên phải.

Cuối cùng, nhấp vào Ứng dụng trong thanh bên điều hướng.

Đây là nơi các ứng dụng Streamlit đã triển khai của bạn sẽ nằm trong Snowflake.

Khi bạn xuất bản ứng dụng Streamlit từ Notebook,

đây là nơi bạn có thể tìm thấy nó.

Bạn sẽ sử dụng hầu hết các công cụ này trong một số video tiếp theo,

vì vậy hãy thoải mái dành một phút để khám phá chúng ngay bây giờ.

Trước khi tiếp tục, hãy dành một chút thời gian để ăn mừng bạn đã tiến được bao xa.

Bạn đã đăng nhập vào Snowsite, khám phá cơ sở dữ liệu Avalanche,

được điều hướng qua các lược đồ và bảng,

đã xem trộm bên trong bảng Đánh giá của Khách hàng,

và kiểm tra các công cụ chính như Bảng tính, Sổ tay và Ứng dụng.

Có rất nhiều tính năng trong Snowsite mà chúng tôi sẽ không sử dụng trong khóa học này,

nhưng bạn có thể xem video demo được liên kết trong mục đọc tiếp theo

nếu bạn muốn tìm hiểu cách tận dụng tối đa tất cả các chức năng.

Bây giờ bạn đã biết cách sử dụng không gian làm việc của Snowflake,

nền tảng đó sẽ làm cho phần còn lại của khóa học này dễ theo dõi hơn nhiều.

Tiếp theo, bạn sẽ bắt đầu tải dữ liệu Avalanche của mình

và khám phá nó bằng Python.

Hãy tiếp tục duy trì đà phát triển.