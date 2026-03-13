# 05 hiểu-lọc-hàm-tất-cả-phần-3

---

Xin chào và chào mừng trở lại.

Trong video cuối cùng,

chúng tôi đã giúp Primeby hiểu rõ về nó trên toàn tiểu bang

sự đóng góp của doanh số bán đèn bàn và

tỷ lệ doanh số bán đèn bàn với

the net profit margin greater than 50%.

Trong video này,

hãy giúp Primeby hiểu

việc bán đèn bàn tốt hơn.

Primeby muốn phân tích cách bảng

giá đèn so với các mặt hàng khác trong

danh mục thiết bị chiếu sáng,

chẳng hạn như đèn sàn và nến.

Hiểu được sự khác biệt giữa

các thiết bị chiếu sáng về mặt

giá trị đơn hàng trung bình có thể cung cấp

cái nhìn sâu sắc có giá trị cho Primeby và

trợ việc ra quyết định theo nhiều cách.

Ví dụ,

điều này sẽ giúp ích cho chiến lược sản phẩm.

Biết sản phẩm nào có giá cao hơn

giá trị đơn hàng trung bình sẽ cho phép

Primeby tập trung vào việc quảng bá và

tiếp thị những mặt hàng đó một cách tích cực,

dẫn đến tăng doanh thu và

khả năng sinh lời.

Một lĩnh vực khác là tối ưu hóa kết hợp sản phẩm.

Sự hiểu biết về giá trị đơn hàng trung bình có thể

hỗ trợ tối ưu hóa việc kết hợp sản phẩm.

Nó sẽ giúp Primeby xác định

những khoảng trống tiềm ẩn trong chủng loại và

giới thiệu những sản phẩm mới sẽ

phù hợp với sở thích của khách hàng.

Với sự hiểu biết này,

hãy tiếp tục và giải quyết vấn đề này.

Nhưng trước tiên chúng ta cần tìm giá trị trung bình

giá trị đơn hàng của sản phẩm.

Hãy chuyển sang trang mới trong Power Bi và

tạo ra một biện pháp mới.

Trong thanh công thức hãy nhập tên của

thước đo là Giá trị đặt hàng trung bình.

Vì chúng ta cần tính toán

tổng số tiền bán hàng

để trung bình vượt qua Tên

của cột Số tiền bán hàng

từ Phiếu đặt hàng bán hàng

bên trong hàm trung bình.

Công thức cuối cùng sẽ như thế này

hãy nhấn Enter để tạo thước đo

với điều đó.

Đầu tiên, hãy hình dung điều này

vấn đề bằng cách sử dụng một ma trận trực quan.

Trong phần Xem báo cáo, chúng tôi chọn

the matrix visual and add the product name

trường vào các hàng và Giá trị đơn hàng trung bình

đo vào trường giá trị.

Vì muốn so sánh

Giá trị đặt hàng trung bình chỉ dành cho

các sản phẩm rơi vào

danh mục thiết bị chiếu sáng,

hãy áp dụng mức độ trực quan

lọc trên hình ảnh ma trận này.

Để làm điều đó, hãy đi tới Bộ lọc

và chọn các sản phẩm từ

danh sách bằng cách mở rộng Tên sản phẩm

có trong phần Bộ lọc.

Hình ảnh ma trận hiển thị sản phẩm

tên cùng với tên tương ứng của họ

giá trị đơn hàng trung bình.

Mặc dù hình ảnh này hiển thị mức trung bình

giá trị đơn hàng cho từng sản phẩm, chúng tôi

cũng cần tính trung bình tổng thể

xem xét tất cả các sản phẩm bất kể

của bất kỳ bối cảnh bộ lọc nào được cung cấp bởi các bộ lọc,

slicer hoặc thậm chí các hàng của bất kỳ hình ảnh trực quan nào.

Đây là nơi TẤT CẢ

chức năng phát huy tác dụng.

Trong Power Bi, các biện pháp luôn bị ảnh hưởng

bởi các bộ lọc thông qua hình ảnh,

nghĩa là bối cảnh bộ lọc.

Ví dụ, khi chúng ta tính toán

Giá trị đặt hàng trung bình cho

từng sản phẩm, kết quả

bị ảnh hưởng bởi bối cảnh bộ lọc

áp dụng cho tên sản phẩm

trường trong ma trận trực quan.

Chức năng ALL là một công cụ mạnh mẽ

trong DAX cho phép chúng tôi sửa đổi

bối cảnh bộ lọc.

Bằng cách sử dụng hàm ALL, chúng ta có thể

xóa mọi bộ lọc được áp dụng cho cụ thể

các cột như tên sản phẩm và

đảm bảo rằng tính toán xem xét

tất cả các sản phẩm trong tập dữ liệu, do đó

cung cấp giá trị đặt hàng trung bình tổng thể.

Để tính tổng thể

giá trị đơn hàng trung bình,

hãy bắt đầu tạo ra một thước đo mới.

Chúng ta sẽ sử dụng hàm CALCULATE

cùng với hàm ALL bên trong nó.

Hãy gọi hàm CALCULATE và

như một đối số đầu tiên,

hãy vượt qua Giá trị đơn hàng trung bình

đo lường như chúng ta muốn đánh giá nó.

Bây giờ trong đối số thứ hai, chúng ta cần phải

gọi hàm TẤT CẢ và chuyển sản phẩm

tên từ bảng sản phẩm ở phần thứ hai

đối số của hàm CALCULATE, vì chúng ta

muốn xóa rõ ràng mọi bộ lọc

áp dụng cho cột tên sản phẩm.

Bước tiếp theo, đóng dấu ngoặc đơn

cho hàm TÍNH TOÁN.

Công thức cuối cùng sẽ trông

như thế này nhấn Enter để tạo

Tổng giá trị đơn hàng trung bình.

Công thức sẽ được đánh giá và

biện pháp sẽ được thêm vào

vào bảng biện pháp.

Hãy thêm thước đo mới này vào

trực quan bằng cách chọn hình ảnh trực quan và

thêm nó vào phần Giá trị.

Làm như vậy, bạn có thể thấy giá trị tương tự

đang được lặp lại trên các hàng,

vì biện pháp của chúng tôi dường như bị bỏ qua

ngữ cảnh được cung cấp bởi các hàng tên sản phẩm

trong hình ảnh của chúng tôi.

Bây giờ chúng ta hãy nhớ lại vấn đề

mà chúng tôi đang giải quyết.

Primeby muốn so sánh những mức trung bình này với

xác định những khoảng trống tiềm ẩn trong chủng loại

và giới thiệu các sản phẩm hoặc biến thể mới

phù hợp với sở thích của khách hàng.

Để hình dung rõ hơn điều này,

hãy thay đổi biểu đồ ma trận này

sang biểu đồ cột nhóm.

Đầu tiên chúng ta hãy nhấp chuột vào hình ảnh ma trận và

sau đó từ ngăn Trực quan hóa,

bấm vào biểu đồ cột cụm.

Làm như vậy bạn có thể dễ dàng so sánh

Tổng giá trị đơn hàng trung bình

với Giá trị đơn hàng trung bình tương ứng

cho từng sản phẩm.

Với sự trợ giúp của biểu đồ này, Primeby đã

có thể quan sát điều đó trong số ba

thiết bị chiếu sáng chính, nghĩa là,

đèn bàn, đèn sàn và nến.

Sản phẩm của chúng tôi được quan tâm,

chiếc đèn bàn, là chiếc đèn duy nhất

có giá trị đơn hàng trung bình cao hơn

so với mức trung bình chung.

Những ngọn đèn bàn đang tỏa sáng rực rỡ

về mặt giá trị đơn hàng.

Nhưng tại sao?

Primeby đã quyết tâm

hiểu những lý do cơ bản.

Họ thu hẹp giả thuyết của mình

tới ba yếu tố tiềm năng.

Đầu tiên, số lượng cao hơn cho mỗi đơn hàng.

Phải chăng khách hàng đang mua bàn

đèn với số lượng lớn hơn cho mỗi đơn hàng?

Xu hướng mua số lượng lớn có thể là

nâng cao giá trị đơn hàng trung bình.

Thứ hai, đơn giá cao hơn.

Có lẽ, những chiếc đèn bàn đã có giá

cao hơn các thiết bị chiếu sáng khác,

đơn giá cao hơn đương nhiên sẽ

dẫn đến giá trị đơn hàng trung bình cao hơn.

Thứ ba, giảm giá ít hơn.

Đèn bàn có chịu ít hơn không

giảm giá so với các sản phẩm khác?

Nếu vậy, mức chiết khấu ít hơn có thể

được bảo toàn giá trị đơn hàng.

Bước tiếp theo cho

Primeby là đi sâu vào dữ liệu và

kiểm tra các yếu tố này để

đi đến bất kỳ kết luận nào.

Vì vậy, hãy giúp họ đưa ra kết luận

bằng cách tạo ra một ma trận thô và

kéo cột tên sản phẩm vào đó.

Như bạn có thể thấy trong ma trận,

tất cả các sản phẩm được liệt kê.

Có lẽ chúng ta có thể có

đã sử dụng các bộ lọc trên này

toàn bộ trang khi chúng tôi lọc

ra trên các thiết bị chiếu sáng.

Nhưng bây giờ hãy thêm bộ lọc vào ánh sáng

đồ đạc để ma trận cũng

kết quả là ba tên sản phẩm

đèn bàn, đèn sàn và nến.

Bây giờ chúng ta cần kéo vào các cột như

đơn giá, số lượng đặt hàng và

áp dụng giảm giá.

Bây giờ hãy đảm bảo thay đổi tổng hợp

tính trung bình cho tất cả các cột.

Sau khi phân tích xong,

Primeby đã có thể làm sáng tỏ bí ẩn

đằng sau mức trung bình cao hơn

giá trị đơn hàng của đèn bàn.

Họ đã kiểm tra đơn vị trung bình đó

giá cả là lý do chính tại sao bảng

đèn có giá trị đặt hàng trung bình cao hơn.

Điều này là do xung quanh

thiết bị chiếu sáng khác,

đèn bàn có cao nhất

đơn giá trung bình.

Mức giảm giá được cung cấp cho đèn bàn và

số lượng đặt hàng trung bình là

tương tự hoặc

thấp hơn so với các thiết bị chiếu sáng khác.

Primeby có thể sử dụng thông tin có giá trị này

lập kế hoạch chiến lược tiếp thị và

đưa ra các quyết định về giá.

Với điều này, chúng tôi đã đi đến cuối cùng

của video và mô-đun này.

Trong suốt cuộc hành trình này,

chúng tôi đã hỗ trợ Primeby trong

giải quyết vấn đề bằng cách sử dụng nhiều DAX khác nhau

các toán tử như hàm tổng hợp,

chức năng logic, chức năng văn bản,

và chức năng lọc.

Tiến lên phía trước trong phần tiếp theo này và

mô-đun cuối cùng của khóa học này,

chúng ta sẽ đi qua nhiều khái niệm

mà chúng tôi đã đề cập trong Power Bi bằng cách sử dụng

tập dữ liệu toàn cầu của chuyên ngành này.

Chúng tôi sẽ cố gắng hiểu

mô hình bán hàng hiện tại và

cố gắng tìm biện pháp cải thiện

doanh thu cho các giải pháp tổng hợp.

Hẹn gặp bạn ở đó.