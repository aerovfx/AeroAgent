# 13 lab-1-tuyết-vận chuyển-phân tích

---

Chào mừng đến với Phòng thí nghiệm vận chuyển Avalanche.

Trong một số video gần đây nhất, bạn đã tải từng tệp riêng lẻ lên

và dữ liệu hàng loạt được dàn dựng trong Snowflake.

Bây giờ là lúc kết hợp tất cả những kỹ năng đó lại với nhau

trong một kịch bản thế giới thực.

Lần này, bạn sẽ làm việc với Nhật ký vận chuyển Avalanche

bởi vì trong khi đánh giá của khách hàng giúp bạn hiểu

điều mọi người đang nói về những mặt hàng bạn bán,

dữ liệu vận chuyển giúp bạn hiểu

việc giao hàng ảnh hưởng đến cảm xúc của họ như thế nào.

Khi bạn kết hợp cả hai,

bạn có được cái nhìn sâu sắc đa chức năng mạnh mẽ

giúp nhóm của bạn đưa ra quyết định thông minh hơn.

Trong phòng thí nghiệm này, bạn sẽ làm việc với tệp CSV có cấu trúc

có chứa nhật ký về hoạt động vận chuyển của Avalanche.

Mỗi hàng đại diện cho một lô hàng

và một số có thể có vấn đề về giao hàng

tương quan với những đánh giá kém của khách hàng.

Hãy đi sâu vào.

Vậy là bạn đã được trao một tệp CSV có tên Shippinglogs.csv

chứa nhật ký hoạt động vận chuyển của Avalanche.

Công việc của bạn là tải tệp lên giai đoạn Avalanche,

làm sạch và xác thực nội dung,

tải nó vào bảng Snowflake,

và chuẩn bị dữ liệu sạch để kết hợp

với các đánh giá của khách hàng trong phòng thí nghiệm tiếp theo.

Bạn có thể tìm thấy mọi thứ bạn cần cho phòng thí nghiệm này

trong khóa học repo GitHub.

Lab này giả định rằng bạn đã tạo

Avalanche DB, Lược đồ Avalanche, Giai đoạn Avalanche.

Nếu bạn chưa tạo những thứ này,

quay lại các video trước

và đi qua các bước đó

trước khi tiếp tục.

Quay lại trang chủ Snowsite,

bắt đầu bằng cách tải lên tệp Shippinglogs.csv

từ máy cục bộ của bạn vào tài khoản Snowflake của bạn

giống như cách bạn đã làm

với tệp CSV đánh giá của khách hàng.

Lần này sẽ dễ dàng hơn một chút

vì bạn đã tạo rồi

lược đồ và giai đoạn cơ sở dữ liệu.

Từ màn hình chính của Snowsite,

nhấp vào nút dấu cộng trên menu điều hướng bên trái

và chọn tùy chọn cuối cùng, thêm dữ liệu.

Trong cửa sổ bật lên,

bạn sẽ thấy tùy chọn tải tệp vào một giai đoạn

bởi vì bạn sẽ cần phải dọn sạch tập dữ liệu

trước khi biến nó thành một cái bàn.

Tiếp theo kéo thả hoặc duyệt tới vị trí

trên máy tính nơi bạn đã tải xuống Shippinglogs.csv.

Chọn cơ sở dữ liệu, lược đồ và giai đoạn của Avalanche,

sau đó bấm tải lên.

Khi tập tin đã được tải lên,

xác nhận nó ở đó bằng cách chạy một câu lệnh SQL nhanh.

Bấm vào dự án, sau đó vào sổ ghi chép.

Ở góc trên bên phải, nhấp vào dấu cộng sổ tay

để mở một cuốn sổ tay Snowflake mới.

Đặt tên cho sổ ghi chép, chọn cơ sở dữ liệu và lược đồ Avalanche.

Để các tùy chọn khác ở chế độ mặc định như bạn đã làm trước đây.

Đặt cho nó một cái tên giống như thử nghiệm.

Sau đó bấm vào dấu cộng SQL để thêm một ô SQL mới.

Sao chép và chạy lệnh sau.

Điều này sẽ liệt kê tất cả các tập tin hiện được lưu trữ trong giai đoạn của bạn.

Nếu bạn thấy Shippinglogs.csv thì bạn đã sẵn sàng.

Tiếp theo, trong sổ tay Snowflake của bạn,

thêm một ô Python và dán đoạn mã sau.

Khối mã này đọc tệp nhật ký vận chuyển của bạn

từ giai đoạn Avalanche vào khung dữ liệu Snowpark.

Nhận phiên hoạt động kết nối máy tính xách tay của bạn

đến phiên tính toán Snowflake.

Session.read.options suy ra lược đồ đúng

yêu cầu Snowpark tự động phát hiện tên cột

và các kiểu dữ liệu.

Tiêu đề đúng cho Snowpark biết rằng hàng đầu tiên của tệp

chứa tên cột, không phải dữ liệu.

.csv đọc trong CSV của bạn từ giai đoạn Bông tuyết.

.show cung cấp cho bạn bản xem trước dữ liệu

giống như hàm df.head trong gấu trúc.

Bấm vào chạy.

Làm tốt.

Bây giờ bạn có dữ liệu vận chuyển trong khung dữ liệu Snowpark.

Bạn có thể sử dụng Python và Snowpark để dọn dẹp và khám phá dữ liệu.

Trong bản xem trước khung dữ liệu,

bạn có thể thấy tên cột có dấu ngoặc kép xung quanh chúng.

Bạn có thể khắc phục điều đó khá dễ dàng bằng cách cập nhật chúng

với bí danh để đổi các cột như thế này.

Snowpark tải tên cột chính xác

khi chúng xuất hiện trong tập tin,

bao gồm dấu ngoặc kép, chữ in hoa và dấu cách.

Bằng cách sử dụng mã và bí danh,

bạn đang sử dụng phương ngữ SQL Snowflake

để chỉnh sửa trực tiếp tên cột.

Sau khi tên cột của bạn được dọn sạch,

bạn có thể làm những việc như đếm xem có bao nhiêu lô hàng

mỗi nhà mạng thực hiện và chuyển sang gấu trúc

để tạo mẫu nhanh.

Nói chung, nên sử dụng gấu trúc

khi làm việc cục bộ với các tập dữ liệu nhỏ hơn,

như Snowpark khi bạn muốn phân tích trong nền tảng có thể mở rộng.

Riêng bạn, hãy dành thời gian này để dọn dẹp dữ liệu

bằng cách kiểm tra null,

đảm bảo các đơn vị đo có ý nghĩa,

và bất cứ điều gì khác bạn thường làm để chuẩn bị một tập dữ liệu.

Nếu bạn cần trợ giúp, hãy làm việc với ứng dụng JNI yêu thích của bạn.

Khi khung dữ liệu của bạn trông ổn,

lưu nó vào một bảng mới bằng hàm df.write.saveAsTable.

Điều này sẽ đăng ký vĩnh viễn

khung dữ liệu nhật ký vận chuyển đã được làm sạch của bạn

dưới dạng bảng bên trong cơ sở dữ liệu Avalanche của bạn.

Vì vậy, nó có thể được truy vấn bằng SQL,

tham gia với các bảng khác,

được truyền vào ứng dụng,

hoặc gửi đến Cortex để phân tích JNI.

Xin chúc mừng, bây giờ bạn đã có thể

để đọc và ghi dữ liệu vào Snowflake.

Phòng thí nghiệm này sẽ giúp bạn sẵn sàng cho bước tiếp theo

trong kế hoạch xây dựng MVP,

thực hiện việc chuẩn bị dữ liệu cuối cùng và phân tích tình cảm.

Nếu bạn gặp khó khăn,

giải pháp nằm trong khóa học GitHub repo tại m2lab1.

Chúc may mắn và hẹn gặp lại các bạn ở video tiếp theo.