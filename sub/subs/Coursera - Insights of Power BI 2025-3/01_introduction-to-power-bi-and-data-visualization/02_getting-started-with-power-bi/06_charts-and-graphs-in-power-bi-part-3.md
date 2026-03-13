# 06 biểu đồ-đồ thị-in-power-bi-part-3

---

Power Bi cho phép bạn tạo biểu đồ

bằng cách sử dụng ngôn ngữ hàng ngày.

Điều này có thể thực hiện được bằng cách sử dụng

tính năng hỏi đáp của power bi.

Hãy đến một trang mới và khám phá điều này

tính năng thú vị bằng cách tạo trước đó

bản đồ cây cho

loại khách hàng sử dụng ngôn ngữ hàng ngày.

Để làm như vậy, hãy nhấp vào tab chèn

có sẵn trong phần Ribbon.

Trong tab Chèn, nhấp vào Hỏi đáp

tùy chọn có trong phần AI Visual.

Sau khi thực hiện xong sẽ xuất hiện hộp thoại

màn hình yêu cầu lời nhắc.

Nhập lời nhắc hàng ngày

Tiếng Anh để có được biểu đồ mà chúng tôi muốn.

Hãy gõ sự đóng góp của khách hàng

nhập vào doanh thu thực tế trong bản đồ cây.

Bạn có thể thấy Power Bi đã phản hồi

với biểu đồ bản đồ cây hiển thị

sự đóng góp của mỗi người

loại khách hàng đối với doanh thu.

Thật tuyệt vời phải không?

Sự linh hoạt và đơn giản này

sử dụng truy vấn ngôn ngữ tự nhiên

biến Power Bi thành một công cụ tuyệt vời dành cho

phân tích dữ liệu.

Vì vậy, hãy tiếp tục và sửa đổi lời nhắc của bạn,

thêm nhiều bối cảnh hơn và

tiếp tục làm những biểu đồ thú vị

sử dụng tính năng Hỏi & Đáp của Power BI.

Cho đến nay chúng ta đã đề cập đến các yếu tố

như doanh thu ID đặt phòng và

đã tạo ra các biểu đồ và đồ thị xung quanh chúng.

Nhưng trong nhiệm vụ tiếp theo,

khu nghỉ dưỡng nâng cao muốn chúng tôi đi sâu vào

vào yếu tố mới đó là sự hủy bỏ.

Khu nghỉ dưỡng nâng cao muốn hiểu

các mẫu hủy bỏ với

tôn trọng thời gian dẫn đầu và

phương thức thanh toán của đặt phòng.

Hãy bắt đầu bằng cách giúp đỡ họ

giải quyết vấn đề đầu tiên của họ

Đồ thị phân tán được sử dụng rộng rãi để

hình dung mối quan hệ giữa hai

cột số.

Đôi khi nó còn được gọi là mối tương quan

cốt truyện vì nó cho thấy hai

các biến có mối tương quan với nhau.

Vì chúng ta phải học

mối quan hệ giữa thời gian thực hiện và

số lượng hủy bỏ,

biểu đồ này sẽ có thể giúp chúng tôi.

Trên một trang mới từ ngăn trực quan hóa,

chọn một biểu đồ phân tán.

Trong phần trường, đặt phần dẫn đầu

biến thời gian trên trục x và

là biến hủy trên trục y.

Sau khi bạn thêm các cột vào các trường,

bạn sẽ chỉ có thể

thấy một điểm trên đồ thị.

Đó là vì theo mặc định, Power Bi

áp dụng một số tổng hợp cho các giá trị.

Tuy nhiên, đối với phân tích này,

chúng ta cần thay đổi tổng hợp thành

Đừng tóm tắt trong thời gian dẫn đầu,

như chúng ta muốn thấy số lượng

hủy bỏ cho thời gian thực hiện khác nhau.

Lưu ý rằng việc đếm trong bị hủy

cột sẽ không giúp ích gì vì nó chứa

các giá trị bằng 0 và một trong đó một

thể hiện rằng việc đặt chỗ đã bị hủy.

Tổng hợp cột sẽ cho chúng ta

số lượng đặt phòng bị hủy.

Sự điều chỉnh này đảm bảo rằng mỗi

điểm dữ liệu được thể hiện chính xác

trên đồ thị phân tán.

Chúng ta có thể quan sát thấy có một tiêu cực

mối tương quan giữa thời gian thực hiện và

việc hủy đặt phòng.

Có nhiều sự hủy bỏ hơn khi

thời gian thực hiện sẽ ít hơn và ngược lại.

Bằng cách sử dụng biểu đồ phân tán, Elevate Resort

đã có thể xác định được lượt đặt chỗ đó

thực hiện một vài ngày trước khi đến

ngày bị hủy thường xuyên hơn,

trong khi các đặt phòng được thực hiện trong một năm

trước hiếm khi bị hủy bỏ.

Tiếp tục, nhiệm vụ tiếp theo của chúng ta là học

việc hủy đặt phòng đối với

từng loại tiền gửi.

Khu nghỉ dưỡng Elevate cho phép khách hàng của mình

để đặt chỗ dựa trên

sở thích của họ như không cần đặt cọc,

không hoàn lại và hoàn lại.

Họ muốn đi sâu vào để hiểu

số lần hủy

đối với các đặt phòng cho từng loại tiền gửi.

Vì chúng ta cần hiển thị cả phần bị hủy

đặt phòng cũng như tổng số

đặt phòng dựa trên loại tiền gửi,

biểu đồ cột được nhóm lại sẽ

là lựa chọn tốt nhất cho chúng tôi.

Biểu đồ cột nhóm là

hữu ích khi chúng ta muốn nhìn thấy hai hoặc

nhiều giá trị số hơn với

tôn trọng một thể loại.

Để tạo biểu đồ cột nhóm,

hãy chuyển sang một trang mới,

và từ khung hiển thị,

chọn biểu đồ cột cụm.

Trong lĩnh vực này,

thêm loại tiền gửi trên trục x và

bị hủy và ID đặt chỗ trên trục y.

Khi đã xong, một biểu đồ cột được nhóm

đại diện cho số lượng đặt phòng và

tổng số lần hủy bởi

loại tiền gửi được tạo.

Sử dụng biểu đồ,

chúng ta có thể rút ra kết luận rằng

tỷ lệ hủy trên đặt phòng cho

loại tiền gửi không có tiền gửi cao hơn

hơn là loại tiền gửi không hoàn lại.

Ngoài ra, hầu như không có bất kỳ đặt phòng nào cho

loại hoàn lại.

Với điều này,

Elevate Resort đã đạt được những hiểu biết sâu sắc và

đã đưa ra những quyết định kinh doanh sáng suốt.

Nhưng ban quản lý muốn có một hình dung

thông qua đó họ có thể dễ dàng có

nhìn vào những con số kinh doanh chính

chẳng hạn như tổng số lượng đặt phòng,

đặt phòng bị hủy, tổng doanh thu

được tạo ra và doanh thu bị mất.

Đây là những thước đo quan trọng để

Nâng cao khu nghỉ dưỡng.

Hãy giúp đỡ họ bằng cách cung cấp

những con số đó trong Power Bi.

Để giới thiệu thẻ số liệu chính

trực quan hóa có ích.

Hình dung thẻ cung cấp ngay lập tức,

Tóm tắt dễ đọc

của những nhân vật chủ chốt.

Khả năng nhấn mạnh đơn

số cần thiết mà không có

sự phức tạp của đồ thị hoặc

biểu đồ làm cho nó trở thành một công cụ có giá trị.

Hãy làm theo các bước để tạo ra nó.

Hãy chuyển sang trang mới và

từ khung hiển thị,

bấm vào nút thẻ.

Với thẻ mới được chọn,

đi tới khung trường và

kéo Mã đặt chỗ vào phần trường của

ngăn trực quan hóa, thế là xong.

Bạn sẽ thấy số lượng

Mã đặt chỗ trên thẻ.

Bạn luôn có thể thay đổi tổng hợp

đo từ phần hiện trường như bình thường bằng cách

bấm vào thả xuống.

Sẽ thật tuyệt nếu thêm tất cả những thứ khác

thẻ để cung cấp ý nghĩa quan trọng

số doanh nghiệp bằng

theo các bước tương tự.

Hãy lặp lại quá trình tương tự cho

ba cột khác là

Doanh thu thực bị hủy và doanh thu bị mất.

Chỉ cần nhớ, đối với Đặt chỗ đã bị hủy,

bạn nên sử dụng số tiền để có được tổng số

số lượng đặt phòng bị hủy,

sắp xếp này từ dữ liệu.

Mặc dù nếu chúng ta nhớ lại

từ danh sách nhiệm vụ,

có thêm một cái nhìn sâu sắc hơn

mà Elevate Resorts mong muốn.

Elevate Resorts muốn tạo ra

một bảng thông tin tương tác có thể kết hợp

nhiều thông tin chi tiết và số liệu chính

mà chúng ta đã phát triển trong bài học này.

Hãy giúp họ trong việc tạo ra

bảng điều khiển trong bài học tiếp theo.

>> Người phát biểu 1: Chúng tôi đã đến

đến cuối video này.

Công việc tuyệt vời trong việc giúp Elevate

khu nghỉ dưỡng trong việc trích xuất những hiểu biết sâu sắc

họ đã tìm kiếm từ dữ liệu.

Mặc dù nếu chúng ta nhớ lại từ

danh sách các nhiệm vụ,

có thêm một cái nhìn sâu sắc hơn

mà Elevate Resorts mong muốn.

Elevate Resorts muốn tạo ra

một bảng thông tin tương tác có thể kết hợp

nhiều thông tin chi tiết và số liệu chính

mà chúng tôi đã phát triển trong video này.

Hãy giúp họ trong việc tạo ra

trang tổng quan trong video tiếp theo.