# 07 từ-csv-to-cloud-using-notebooks-to-ingest-avalanche-data

---

Cho đến giờ trong khóa học, bạn đã làm việc với một tệp CSV sạch có tên là Đánh giá của khách hàng.

Trong video này, bạn sẽ tải tệp đó lên Snowflake

và biến nó thành một bảng thích hợp.

Trong video tiếp theo, bạn sẽ tạo lại tập dữ liệu tương tự bằng cách kết hợp một đống tài liệu từ lộn xộn.

Nhưng bây giờ, hãy bắt đầu đơn giản và tải phiên bản sạch

để bạn có thể làm quen với quá trình này từ đầu đến cuối.

Trước tiên, hãy kiểm tra kế hoạch xây dựng MVP của bạn cho Mô-đun 1.

Bây giờ bạn đã làm việc thông qua quy trình này trong Mô-đun 1,

nhưng lần này, chúng ta sẽ bắt đầu lại với Snowflake

để bạn có thể thấy quá trình tải lên và tạo bảng đầy đủ hoạt động như thế nào trong môi trường này.

Đã đến lúc thực hiện Bước 1, đưa dữ liệu vào Snowflake.

Nếu bạn đã từng làm việc trong lĩnh vực khoa học hoặc phân tích dữ liệu, rất có thể bạn đã xử lý nhiều dữ liệu dạng bảng,

thường ở dạng CSV, tệp Excel hoặc các định dạng kiểu bảng tính khác.

Snowflake hỗ trợ tất cả các định dạng phổ biến nhất và nhiều định dạng khác,

chẳng hạn như các tệp có cấu trúc như CSV và TSV, các định dạng bảng tính cổ điển của bạn.

Đây là những điều tuyệt vời cho dữ liệu sạch sẽ, có tổ chức.

Dữ liệu bán cấu trúc như JSON, Avro, Parquet và XML.

Đây là những định dạng linh hoạt hơn, thường được sử dụng cho nhật ký, sự kiện,

hoặc thông tin lồng nhau và tài liệu văn bản, tệp PDF và Word.

Nếu bạn đến từ nền tảng khoa học dữ liệu truyền thống, điều này có thể ít quen thuộc hơn.

Nhưng nhờ có GenAI, giờ đây việc phân tích và trích xuất thông tin chuyên sâu từ loại dữ liệu này trở nên dễ dàng hơn nhiều.

Trước khi tải lên bất kỳ nội dung nào, hãy xem nhanh cách Snowflake sắp xếp dữ liệu của bạn.

Hãy nghĩ về nó giống như một tủ hồ sơ văn phòng.

Cơ sở dữ liệu giống như chính chiếc tủ, nơi chứa cấp cao nhất cho một dự án.

Các lược đồ là các thư mục bên trong tủ đó để giữ mọi thứ ngăn nắp.

Bảng, Chế độ xem và Giai đoạn.

Dữ liệu thực tế của bạn và các công cụ để quản lý nó.

Bảng là các hàng và cột của dữ liệu có cấu trúc.

Chế độ xem là các truy vấn đã lưu trông giống như bảng.

Các giai đoạn là vùng tải lên các tệp trước khi tải chúng vào bảng.

Cấu trúc này giữ cho dữ liệu của bạn sạch sẽ, theo mô-đun và dễ điều hướng.

Và bây giờ, bạn sẽ thiết lập nó cho chính mình.

Bây giờ, theo tổ chức này, bạn sẽ tạo ra ba thứ.

Cơ sở dữ liệu để lưu trữ dự án của bạn, lược đồ để sắp xếp các tệp của bạn,

và giai đoạn mà bạn sẽ tải lên tệp avalanche-customer-reviews.csv.

Thiết lập này phản ánh thiết lập dự án điển hình nhất trong Snowflake.

Đầu tiên, cơ sở dữ liệu.

Đây là vùng chứa cấp cao nhất của bạn cho mọi thứ liên quan đến ứng dụng Avalanche.

Để tạo cơ sở dữ liệu mới, trong Snowsite, hãy nhấp vào tab Dữ liệu ở thanh bên trái.

Thao tác này sẽ mở cửa sổ Cơ sở dữ liệu.

Nhấp vào biểu tượng cơ sở dữ liệu dấu cộng ở góc trên bên phải.

Trong cửa sổ Cơ sở dữ liệu, đặt tên cho cơ sở dữ liệu của bạn như avalanche gạch dưới db.

Sau đó bấm vào Tạo cơ sở dữ liệu.

Bước một, kiểm tra.

Ở đây bên trái, bây giờ bạn có cơ sở dữ liệu Avalanche mới

mà bạn sẽ sử dụng làm vùng chứa cấp cao nhất để lưu trữ tất cả các bảng và lược đồ Avalanche.

Bây giờ, hãy thêm một lược đồ để sắp xếp mọi thứ.

Đây là nơi bạn sẽ lưu trữ các tệp và bảng thô của mình.

Nhấp vào db Avalanche mới của bạn ở thanh bên trái.

Ở phía trên bên phải của cửa sổ Avalanche db mở ra, nhấp vào lược đồ dấu cộng.

Đặt tên cho lược đồ của bạn giống như lược đồ gạch dưới tuyết lở.

Sau đó nhấp vào Tạo.

Bây giờ bạn đã có một nơi để sắp xếp các tệp thô tách biệt với các tệp sạch

hoặc bất cứ điều gì khác bạn thêm vào sau.

Cuối cùng, hãy tạo một sân khấu.

Điều này đặc biệt hữu ích nếu bạn dự định sử dụng lại các tập tin trên

sổ ghi chép hoặc giữa những người dùng trong cùng một không gian làm việc.

Đây là khu vực tải lên của bạn.

Đó là nơi chứa các tệp thô trước khi chúng được tải vào bảng.

Nhấp vào lược đồ Avalanche hiện được liệt kê trong cơ sở dữ liệu Avalanche của bạn.

Ở phía trên bên phải màn hình, nhấp vào nút Tạo màu xanh lam.

Từ menu thả xuống, chọn Giai đoạn rồi chọn Snowflake Managed.

Trừ khi bạn có lý do để chọn Bộ nhớ được quản lý bên ngoài,

đây sẽ là tùy chọn dễ cấu hình nhất.

Từ cửa sổ Tạo giai đoạn, hãy đặt tên cho giai đoạn của bạn giống như giai đoạn gạch dưới tuyết lở.

Nếu lược đồ chưa trỏ tới lược đồ Avalanche db dot Avalanche, hãy cập nhật lược đồ đó ngay bây giờ.

Chọn Mã hóa phía máy chủ và bạn có thể để mọi thứ khác theo mặc định.

Sau đó nhấp vào nút Tạo màu xanh sáng ở phía dưới bên phải.

Khi giai đoạn của bạn đã sẵn sàng, đã đến lúc tải lên CustomerReviews.csv

đến giai đoạn bạn vừa tạo.

Khi giai đoạn Avalanche đã sẵn sàng, bạn sẽ được đưa tới cửa sổ Cài đặt.

Ở phía trên bên phải màn hình, nhấp vào nút Plus Files.

Kéo và thả hoặc duyệt đến vị trí nơi

bạn đã sao chép kho lưu trữ khóa học và chọn CustomerReviews.csv.

Nhấp vào nút Tải lên.

Tệp của bạn hiện được lưu trữ an toàn trong giai đoạn Avalanche

và sẵn sàng để được tham chiếu trong các truy vấn và tập lệnh.

Bây giờ dữ liệu của bạn đã có trên Snowflake, phần công việc còn lại có thể được thực hiện trong sổ ghi chép Snowflake.

Sổ ghi chép bông tuyết giống như sổ ghi chép Jupyter, nhưng được lưu trữ trong Snowflake.

Bạn có thể viết và chạy cả Python và SQL,

trực quan hóa dữ liệu và làm việc trực tiếp với môi trường Bông tuyết của bạn.

Để mở sổ ghi chép mới, trong thanh bên bên trái của trang Snow, hãy nhấp vào Dự án.

Sau đó bấm vào Sổ tay.

Ở phía trên bên phải màn hình của bạn, nhấp vào nút Plus Notebook.

Đặt tên cho sổ ghi chép của bạn giống như Avalanche CustomerReviews.

Chọn cơ sở dữ liệu Avalanche của bạn làm lược đồ.

Để lại tùy chọn thời gian chạy của bạn tại Chạy trên Kho.

Đây là lựa chọn tốt nhất của bạn để phân tích dữ liệu bằng Python

vì nó đi kèm với hầu hết các gói khoa học dữ liệu được cài đặt sẵn.

Để mọi thứ khác ở chế độ mặc định.

Sau đó bấm vào Tạo.

Khi sổ ghi chép của bạn mở ra, bạn sẽ được đưa tới cửa sổ soạn thảo chính,

đó là nơi bạn viết mã của mình.

Sổ ghi chép của bạn sẽ mở ra với một vài ô mã mẫu bằng cả Python và SQL,

được hiển thị ở đây ở phía trên bên trái của mỗi ô.

Để chạy một ô, nhấn Shift-Enter trên bàn phím của bạn

hoặc nhấn nút Run ở phía trên bên phải màn hình.

Bạn có thể thử ngay bây giờ để xem nó hoạt động như thế nào.

Ô mã đầu tiên là cách bạn kết nối với bất kỳ dữ liệu nào được lưu trữ trên Snowflake.

Vì vậy, hãy để điều đó đúng chỗ để lấy các đánh giá của khách hàng.

Nhưng bây giờ, bạn có thể tiếp tục và xóa hai khối mã ví dụ cuối cùng

bằng cách nhấp vào menu ba chấm ở trên cùng bên phải của mỗi khối và chọn Xóa.

Bây giờ bạn đã thiết lập cơ sở dữ liệu, lược đồ và giai đoạn của mình,

bạn đã sẵn sàng tải tệp customerreviews.csv của mình

vào khung dữ liệu bên trong sổ ghi chép Snowflake của bạn.

Trong Snowflake, bạn chủ yếu sẽ làm việc với hai loại khung dữ liệu,

Khung dữ liệu Pandas và khung dữ liệu Snowpark.

Chúng trông giống nhau và hỗ trợ nhiều hoạt động giống nhau,

nhưng dưới mui xe, họ cư xử rất khác nhau.

Hãy phá vỡ nó.

Khung dữ liệu Pandas chạy mọi thứ ngay lập tức trên máy cục bộ của bạn.

Điều đó thật tuyệt vời khi phân tích nhanh trên các tập dữ liệu nhỏ,

nhưng chúng có thể chạy chậm lại hoặc gặp sự cố khi dữ liệu lớn.

Khung dữ liệu Snowpark không thực thi ngay lập tức.

Thay vào đó, họ xây dựng một kế hoạch truy vấn, một loại kế hoạch chi tiết mô tả điều gì sẽ xảy ra,

như lọc, nối hoặc chuyển đổi dữ liệu,

nhưng thực tế không chạy bất cứ thứ gì cho đến khi bạn yêu cầu kết quả.

Sau đó, khi bạn đã sẵn sàng, toàn bộ kế hoạch sẽ được gửi tới cơ sở hạ tầng đám mây của Snowflake

và thực thi tất cả cùng một lúc, ngay tại nơi chứa dữ liệu.

Điều đó có nghĩa là không cần tải xuống, không bị quá tải bộ nhớ và tốc độ nhanh hơn trên quy mô lớn.

Vậy bạn nên sử dụng cái nào?

Bảng sau đây cung cấp cho bạn một cái nhìn tổng quan về sự khác biệt.

Sử dụng Pandas để kiểm tra cục bộ nhanh các tệp nhỏ.

Sử dụng khung dữ liệu Snowpark khi bạn làm việc với các tập dữ liệu lớn hơn

hoặc khi bạn muốn khai thác toàn bộ sức mạnh của công cụ tính toán của Snowflake.

Bây giờ bạn đã hiểu cách Snowflake xử lý các khung dữ liệu,

Hãy áp dụng điều đó vào thực tế bằng cách tải tệp customerreviews.csv của bạn

vào khung dữ liệu Snowpark.

Bước đầu tiên là kết nối sổ ghi chép Snowflake với môi trường dự án của bạn.

Snowflake tự động xử lý việc này cho bạn bằng cách sử dụng thứ gọi là phiên hoạt động.

Mỗi sổ ghi chép Snowflake sẽ bắt đầu được tự động điền với khối mã này.

Hãy chạy khối mã này bằng cách nhấp vào nút phát ở trên cùng bên phải.

Mã này bắt đầu bằng cách nhập các thư viện cốt lõi của bạn,

Streamlet và Pandas, giống như bạn đã làm trước đây.

Sau đó, bạn có thể gọi getActiveSession từ thư viện Snowpark.

Điều này tạo ra kết nối trực tiếp đến dự án Bông tuyết của bạn.

Sau khi phiên đó hoạt động, bạn đã hoàn toàn kết nối với phần phụ trợ của Snowflake.

Điều đó có nghĩa là bây giờ bạn có thể truy vấn các bảng hiện có, tải tệp từ một giai đoạn,

ghi dữ liệu vào các bảng mới và chạy mọi thứ bên trong đám mây của Snowflake

thay vì trên máy cục bộ của bạn.

getActiveSession là đường dây trực tiếp của bạn tới Snowflake

và động cơ cung cấp năng lượng cho mọi việc bạn sẽ làm tiếp theo.

Bây giờ bạn đã kết nối với Snowflake và có phiên sẵn sàng hoạt động,

đã đến lúc tải dữ liệu của bạn.

Hãy kéo tệp customerreviews.csv vào khung dữ liệu Snowpark

để bạn có thể bắt đầu làm việc với nó ngay trong sổ ghi chép của mình bằng dòng mã này.

Dòng này tải tệp CSV của bạn trực tiếp từ giai đoạn Bông tuyết vào khung dữ liệu Snowpark.

Vì vậy, bạn có thể xem trước và làm việc với nó bên trong mã Python của mình.

session.read cho Snowpark biết bạn sắp đọc dữ liệu vào khung dữ liệu mới.

options() suy ra lược đồ đúng.

Đây là một phím tắt hữu ích để Snowflake tự động phát hiện tên cột

và các loại dữ liệu của chúng dựa trên nội dung CSV của bạn.

Nếu không sử dụng tùy chọn này, mọi thứ sẽ được tải dưới dạng văn bản thuần túy.

csv() ở giai đoạn tuyết lở customerreviews.csv

trỏ trực tiếp đến tệp bạn đã tải lên trước đó.

Giai đoạn tuyết lở là giai đoạn được đặt tên của bạn, vùng tải lên an toàn mà bạn đã tạo.

customerreviews.csv là tệp nằm bên trong nó.

Cuối cùng, df.show cho phép bạn xem trước một số hàng trên cùng của tập dữ liệu của bạn

giống như bạn làm với df.head trong gấu trúc.

Tại thời điểm này, bạn đang đọc dữ liệu được lưu trữ trên Snowflake vào sổ ghi chép của mình,

phân tích nó bằng Python và xem trước kết quả,

tất cả mà không bao giờ rời khỏi đám mây.

Trước khi tiếp tục, bạn nên hiểu cách hoạt động của đường dẫn tệp trong Snowflake,

đặc biệt là khi bạn đang làm việc với các giai đoạn.

Khi bạn nhìn thấy đường dẫn tệp như thế này, đây là ý nghĩa của từng phần.

Biểu tượng at cho Snowflake biết bạn đang đề cập đến một sân khấu,

khu vực lưu trữ của bạn cho các tập tin.

Giai đoạn Avalanche là tên của giai đoạn bạn đã tạo trước đó.

Đó là nơi bạn tải lên tệp customerreviews.csv của mình.

customerreviews.csv là tên của tệp bạn đặt trong giai đoạn đó.

Nếu bạn đã tải tệp của mình lên thư mục con trong vùng hiển thị,

con đường có thể trông như thế này.

Bông tuyết xử lý các giai đoạn giống như các thư mục đám mây.

Bạn có thể sắp xếp các tệp bên trong chúng bằng các đường dẫn giống như thư mục,

mặc dù dung lượng lưu trữ cơ bản bằng phẳng.

Khi bạn làm việc với nhiều tệp trong các bài học sau,

hiểu cách hoạt động của các đường dẫn này sẽ giúp bạn luôn ngăn nắp và tránh sai sót.

Bây giờ bạn đã xem trước các tệp CSV của mình và xác nhận rằng mọi thứ đều ổn,

đã đến lúc làm cho dữ liệu của bạn trở nên vĩnh viễn.

Hiện tại, dữ liệu của bạn chỉ tồn tại trong bộ nhớ bên trong sổ ghi chép của bạn,

giống như một bảng ghi nhớ tạm thời.

Để làm cho nó thực sự hữu ích,

bạn muốn biến nó thành một bảng bên trong cơ sở dữ liệu Snowflake của mình.

Đây là mã để làm điều đó.

Dòng này nói với Snowpark,

customerreviews là tên của bảng bạn đang tạo trong cơ sở dữ liệu Snowflake của mình.

chế độ ghi đè bằng cho Snowflake biết,

nếu một bảng có tên này đã tồn tại, hãy thay thế nó bằng bảng này.

Khi bạn chạy lệnh này, khung dữ liệu của bạn không còn tạm thời nữa.

Nó trở thành một bảng cố định thực sự được lưu trữ trong cơ sở dữ liệu dự án của bạn

và lược đồ.

Điều này có nghĩa là bạn có thể viết các truy vấn SQL dựa trên nó.

Bạn có thể kết nối nó với các ứng dụng Streamlit.

Bạn có thể kết hợp nó với các bộ dữ liệu khác.

Và bạn có thể chia sẻ nó với nhóm của mình hoặc các công cụ khác trong môi trường Bông tuyết của bạn.

Đây là bước quan trọng để biến dữ liệu thô thành tài nguyên gốc Snowflake có cấu trúc,

sẵn sàng để được truy vấn, trực quan hóa và xây dựng dựa trên.

Đừng quên chạy ô này.

Làm tốt lắm.

Trong bài học này, bạn đã tạo cơ sở dữ liệu, lược đồ và giai đoạn mới để sắp xếp dữ liệu của mình.

Đã tải lên tệp customerreviews.csv của bạn bằng Sổ tay Snowflake.

Đã tải tệp customerreviews.csv vào khung dữ liệu Snowpark trực tiếp từ sân khấu.

Đã xem trước dữ liệu để xác minh rằng nó trông ổn.

Và lưu nó dưới dạng bảng có thể truy vấn vĩnh viễn bên trong Snowflake.

Bạn đã chính thức hoàn thành bước một trong kế hoạch xây dựng MVP của mình,

lấy dữ liệu vào Snowflake.

Trong video tiếp theo, bạn sẽ thăng cấp bằng cách lấy một đống đánh giá thô của khách hàng trên Docx

và biến chúng thành sạch sẽ,

dữ liệu có cấu trúc bằng các công cụ hỗ trợ GenAI từ Snowflake Cortex.