# 02 bảng chuyển-dữ-dữ-dùng-trục

---

Xin chào và chào mừng trở lại.

Trong video trước, chúng tôi đã sử dụng Power

Trình soạn thảo truy vấn để giúp Primebuy dọn dẹp và

chuyển đổi dữ liệu của nó để có được mức trung bình

giảm giá trên các kênh bán hàng khác nhau.

Trong video này,

chúng ta sẽ giải quyết một vấn đề khác cho

Primebuy bằng cách thao túng dữ liệu bán hàng.

Một vấn đề khác mà Primebuy muốn giải quyết

giải quyết là thao tác dữ liệu để xem xét

doanh số trung bình mỗi tháng

trên các kênh bán hàng khác nhau cho

tập dữ liệu có sẵn.

Trước khi chúng ta bắt đầu giải quyết

tuyên bố vấn đề, hãy làm việc

về các điều kiện tiên quyết và điều chỉnh

tập dữ liệu để làm cho nó sẵn sàng hiển thị.

Chúng ta cần xem dữ liệu bán hàng

trên các kênh bán hàng khác nhau,

nhưng nếu bạn nhìn vào bảng Đơn đặt hàng bán hàng,

bạn sẽ khám phá ra rằng điều này

tập dữ liệu thiếu cột

sẽ cho biết số tiền bán hàng

liên quan đến từng đơn hàng.

Để thêm một cột mới chứa thông tin

về số tiền bán hàng, hãy điều hướng đến

bảng đơn đặt hàng bán hàng và chọn mới

cột ở phần tính toán.

Khi bạn nhấp vào nó,

một cột mới ở ngoài cùng bên phải

sẽ được chèn vào bảng.

Một hộp thoại mới xuất hiện

trên đầu bảng,

và trong hộp đó bạn được yêu cầu tạo

công thức tính doanh số bán hàng.

Chúng tôi có tất cả các thông tin cần thiết

để tính số tiền bán hàng.

Chúng ta có thể nhân số lượng đặt hàng với

đơn giá để có được số tiền bán hàng cho

một đơn đặt hàng trước khi giảm giá.

Vì chiết khấu của chúng tôi là số thập phân,

chúng ta có thể nhân số tiền này với một dấu trừ

giảm giá áp dụng để có được

số tiền bán hàng cuối cùng.

Bây giờ, trong thanh công thức, trước tiên hãy thay thế

cột có tên bạn muốn.

Trong trường hợp này, hãy chọn số tiền bán hàng.

Tiếp theo, gõ một vài chữ cái đầu tiên

của cột mà bạn muốn sử dụng,

và Power Bi sẽ cung cấp cho bạn một chiếc ô tô

tùy chọn điền để chọn.

Hãy nhân lên

số lượng đặt hàng,

đơn giá và

một điểm trừ

giảm giá

áp dụng.

Bây giờ hãy đảm bảo kèm theo một điểm trừ

giảm giá được áp dụng trong ngoặc đơn vì vậy

rằng công thức hoạt động chính xác và

nhấn Enter khi bạn đã hoàn tất.

Công thức tính số tiền bán hàng

và trả về giá trị cho mỗi đơn hàng.

Bạn có thể thấy số tiền bán hàng cột mới

đã được thêm vào phần ngoài cùng bên phải.

Đã thêm thành công Số tiền bán hàng

vào bảng đơn đặt hàng bán hàng của chúng tôi,

chúng ta hãy quay lại vấn đề hiện tại.

Mục tiêu của Primebuy là phân tích mức trung bình

số liệu bán hàng qua các lần bán hàng khác nhau

kênh cho mỗi tháng.

Vì vậy chúng ta cần thêm hai cột nữa

để hoàn thành phân tích của chúng tôi.

Chúng ta cần cột kênh bán hàng và

cột một tháng.

Nhưng nếu bạn nhìn vào cột ngày đặt hàng,

bạn sẽ nhận thấy rằng dữ liệu

hiện diện ở định dạng ngày đầy đủ.

Tuy nhiên, chúng ta chỉ cần giá trị tháng

kể từ ngày hoàn thành phân tích của chúng tôi.

Hãy nhìn vào kết quả

chúng tôi muốn đạt được.

Bạn có thể thấy từ bảng mà chúng tôi

có doanh thu trung bình mỗi tháng cho

bốn kênh bán hàng khác nhau.

Vì vậy, hãy tạo một cột khác

tháng trong bảng đơn hàng bán hàng.

Hãy điều hướng đến đơn đặt hàng bán hàng

bảng và chọn cột mới.

Trong thanh công thức, nhập tên

của cột tháng có dấu bằng,

và sau đó thêm chức năng tháng.

Tiếp theo, bên trong dấu ngoặc đơn,

chuyển cột ngày đặt hàng.

Hàm tháng trích xuất tháng

thành phần từ cột ngày đặt hàng.

Công thức sẽ trông như thế này.

Nhấn Enter để áp dụng công thức.

Công thức trả về giá trị hàng tháng cho

mỗi đơn hàng bạn đã tạo bổ sung

cột cần thiết để hoàn thành việc phân tích.

Tuy nhiên, để trình bày thông tin trong

dạng mong muốn thì cần có một bảng mới.

Bảng này sẽ bao gồm thông tin

về số tiền bán hàng trung bình cho

các kênh bán hàng khác nhau

trong nhiều tháng.

Nhưng trước khi chúng ta bắt đầu phân tích,

hãy nhanh chóng hiểu cách hoạt động của Pivot.

Pivot thay đổi cấu trúc của hàng và

cột theo cách tổng hợp các giá trị

của một cột cho mỗi giá trị duy nhất

sự kết hợp từ nhiều cột.

Bảng Pivot hoạt động bằng cách

lấy một tập dữ liệu lớn và

cho phép bạn sắp xếp lại và

tóm tắt dữ liệu chỉ với một vài cú nhấp chuột.

Chúng ta hãy nhìn vào hình đã cho

hiểu biết hơn.

Như bạn có thể thấy, cột thuộc tính là

cột chúng tôi đã xoay quanh và các giá trị

được tổng hợp cho mỗi sự kết hợp của

nhiều cột có trong bảng.

Có được sự hiểu biết về

cột xoay vòng, chúng ta hãy xem lại

tờ đơn đặt hàng bán hàng và xem chúng tôi làm thế nào

có thể biến đổi nó thành như thế này.

Lưu ý tính năng bảng trụ là

sẵn có trong Power Query,

làm biến đổi dữ liệu trong khi chúng ta

đang cố gắng trả lại một đầu ra tương tự

sử dụng Matrix Visual trong

báo cáo lượt xem trong video này.

Bây giờ chúng ta hãy bắt đầu.

Điều hướng đến phần xem báo cáo và

trong một trang mới,

chọn ma trận trực quan

từ khung hiển thị.

Sau khi hoàn tất, bạn có thể thấy một ma trận trống

trực quan được thêm vào trong khu vực Canvas báo cáo.

Bây giờ hãy thêm các cột có liên quan từ

bảng đơn đặt hàng bán hàng vào ma trận trực quan.

Cột kênh bán hàng trong phần bán hàng

bảng đặt hàng chứa các giá trị

dưới dạng dữ liệu phân loại

lặp lại cho đến khi hết tập dữ liệu.

Tuy nhiên, bảng kết quả

có mỗi giá trị duy nhất từ Bán hàng

kênh làm tiêu đề cột.

Điều này cho chúng ta biết rằng chúng ta nên bỏ

cột kênh bán hàng vào trường cột.

Bây giờ, vì những tháng khác nhau

đang xuất hiện dưới dạng tiêu đề hàng,

hãy thêm cột tháng vào

trường hàng của bảng ma trận.

Trường giá trị đại diện cho dữ liệu

điều đó sẽ được tổng hợp và

hiển thị trong các cột mới được tạo.

Bạn nên chọn cột số

cung cấp thông tin có ý nghĩa

khi tổng hợp,

chẳng hạn như số tiền bán hàng trong trường hợp của chúng tôi.

Vậy hãy kéo số lượng bán hàng

cột vào trường giá trị.

Bây giờ bạn có thể thấy Power Bi đó theo mặc định

tổng hợp các giá trị thành tổng,

nhưng nếu bạn nhớ lại,

chúng tôi muốn số tiền bán hàng trung bình.

Vì vậy, hãy thay đổi tổng hợp thành trung bình

bằng cách nhấp vào tùy chọn thả xuống bên dưới

trường giá trị.

Lưu ý rằng ngay cả tổng số cũng được sửa đổi

để hiển thị các giá trị trung bình

tương ứng với tiêu đề hàng và cột.

Ví dụ: 9694 là mức bán trung bình của

tháng giêng và chúng ta đã hoàn thành.

Có rất nhiều điều thú vị

những hiểu biết hiện có trong bảng.

Ví dụ: doanh thu trung bình cao nhất là

vào các tháng 11, 12 và

Tháng Giêng qua nhiều nơi khác nhau

các kênh bán hàng.

Kênh bán buôn cũng mang lại

doanh số bán hàng cao hơn trong tháng 4,

trong khi kênh bán hàng trực tuyến là

thấp nhất vào tháng 8.

Đây là những hiểu biết khác có thể

bắt nguồn từ bảng sẽ

rất có giá trị đối với Primebuy.

Trong phần tiếp theo và

video cuối cùng của tuần này,

hãy giúp Primebuy những việc cuối cùng của họ

báo cáo vấn đề, đó là cập nhật

trực quan hóa một cách liền mạch bởi

thêm dữ liệu mới được thu thập.