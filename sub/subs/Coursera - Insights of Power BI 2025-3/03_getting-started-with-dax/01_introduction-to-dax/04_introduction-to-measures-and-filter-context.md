# 04 giới thiệu bối cảnh đo lường và lọc

---

Trong video trước,

chúng tôi đã giúp Primeby tìm thấy

thời gian giao hàng trung bình của họ và

khám phá sức mạnh của

cột tính toán.

Sau khi kiểm tra

các biến thể thời gian dẫn

trên khắp các tiểu bang,

một câu hỏi cấp bách được đặt ra.

Is the sheer volume of

yếu tố chính là giao hàng

ảnh hưởng đến sự biến đổi của

thời gian dẫn qua

các trạng thái khác nhau?

Hãy cùng khám phá điều này

trong video này.

Primeby muốn hiểu

nếu số lượng cao hơn

đơn đặt hàng ở một tiểu bang

dẫn đến sự gia tăng

thời gian giao hàng trung bình.

Hãy thiết lập điều đó và

đi đến trang mới.

Theo truyền thống, chúng tôi

có thể hình dung

điều này chỉ đơn giản là

kéo và thả

nhà nước và trật tự

cột số trên

bảng ma trận và

sử dụng số đếm khác biệt

như một sự tổng hợp.

Một cách tiếp cận khác

sẽ là tạo ra

một biện pháp có tên

số lượng đơn đặt hàng.

Hãy dành khoảnh khắc này để

hiểu biện pháp

và tại sao chúng tôi sử dụng chúng.

Các biện pháp Power BI là một cách

xác định phép tính

trong mô hình DAX.

Biện pháp chuyên cho chúng ta

tổng hợp các giá trị từ

nhiều hàng của một bảng.

hàm tổng hợp

là những chức năng

ngưng tụ nhiều giá trị

đến một giá trị duy nhất.

Một số tổng hợp thông dụng

chức năng là tối thiểu,

tối đa, đếm hàng,

trung bình, tổng, v.v.

Không giống như các cột được tính toán,

các biện pháp thực hiện tính toán trên

con ruồi như chúng vốn có

dựa trên người dùng

tương tác trong một báo cáo,

họ lấy dòng điện

bối cảnh có tính đến,

có nghĩa là đầu ra của họ

có thể thay đổi linh hoạt

dựa trên các bộ lọc hoặc

slicer được áp dụng cho báo cáo.

Hãy so sánh các biện pháp

với cách tiếp cận truyền thống của chúng tôi.

Trong cách tiếp cận truyền thống,

khi bạn kéo

trường số vào

ngăn hiển thị

của sức mạnh thị giác BI,

áp dụng một số tổng hợp để

làm cho nó có ý nghĩa

cho người xem.

Đây là một trường hợp

biện pháp ngầm.

Mặt khác, chúng tôi

cũng có thể rõ ràng

ghi các hàm DAX vào

xác định các cột là

các biện pháp trong Power BI.

Trong cái này và cái

các video sau,

chúng tôi sẽ viết

biện pháp rõ ràng

để có được các giá trị tổng hợp.

Bây giờ chắc hẳn bạn đang nghĩ,

tại sao chúng ta cần phải viết

biện pháp rõ ràng từ

điểm này trên từ?

Vấn đề với các biện pháp ngầm

là họ sống

trong thị giác

trong đó họ

được tạo ra và không thể

được tham chiếu ở bất cứ đâu

khác ở bên ngoài.

Trong khi đó, khi chúng ta tạo

biện pháp rõ ràng,

chúng có thể được tái sử dụng ở bất cứ đâu

trong báo cáo và giúp đỡ

tạo ra các lớp phức tạp

bằng các biện pháp tham khảo,

các biện pháp hiểu biết sâu sắc.

Vậy hãy thử các biện pháp

để giải quyết vấn đề của chúng tôi.

Để bắt đầu, hãy điều hướng

vào tab Trang chủ,

tìm phần tính toán,

và chọn "Biện pháp mới".

Bây giờ chúng ta cần đưa ra

đo một tên duy nhất.

Hãy gọi nó là Num_of_orders.

Một dấu bằng của trình phân tích cú pháp,

giống như chúng ta đã làm trong cột,

và sử dụng hàm đếm

trong đó đếm số hàng.

Trong tập dữ liệu của chúng tôi, mỗi hàng

đại diện cho một trật tự duy nhất.

Vì vậy việc đếm số lượng

hàng sẽ cung cấp cho chúng tôi

số lượng đơn đặt hàng.

Vì chi tiết đặt hàng là

trình bày trong đơn đặt hàng một tờ giấy,

chúng ta cần phải vượt qua

tên trang tính cho

chức năng đếm hàng.

Hãy đóng dấu ngoặc đơn lại.

Bây giờ một khi chúng ta nhấp vào

''Vào'' một cái mới

thước đo được gọi là Num_of_orders,

sẽ xuất hiện trong dữ liệu

chùm tia. Nhưng nó ở đâu?

Từ dải băng trên cùng,

bạn có thể xem bảng nhà để biết

đo mới được tạo

là tờ thông tin khách hàng.

Mặc dù chúng ta có thể thay đổi

bàn nhà

từ đầu đến phiếu đặt hàng bán hàng.

Và bây giờ biện pháp của chúng tôi đã được

chuyển sang bảng đặt hàng bán hàng.

Một cách giải quyết trực tiếp

làm điều này là để tạo ra

biện pháp bằng cách nhấp chuột phải vào

tên bảng từ

chùm dữ liệu.

Để đảm bảo rằng biện pháp đó được

được đặt ở vị trí mong muốn

bàn trong một lần.

Bây giờ làm điều đó, bạn có thể thấy,

và thước đo được đánh dấu

bằng ký hiệu máy tính.

Ký hiệu máy tính này biểu thị

rằng nó thực sự là một biện pháp.

Ngoài ra, hãy chú ý rằng các biện pháp

không thể nhìn thấy được về mặt vật lý

trong chế độ xem dữ liệu,

không giống như các cột được tính toán.

Chỉ là một lời nhắc nhở nhanh chóng,

một cột được tính toán trả về

đầu ra cho mỗi hàng trong khi

biện pháp tạo ra

các giá trị tổng hợp

có thể được lọc thêm

dựa trên đầu ra mong muốn.

Bây giờ hãy tham khảo của chúng tôi

phát biểu vấn đề.

PrimeBuy muốn hiểu

nếu số lượng đơn đặt hàng cao hơn trong

một trạng thái dẫn đến sự gia tăng

giao hàng trung bình

thời gian ở trạng thái đó.

Để làm điều đó, hãy điều hướng đến

tab xem báo cáo và

chọn một hình ảnh ma trận.

Tiếp theo, hãy kéo

cột trạng thái

từ bảng khu vực và

thả nó vào trường hàng.

Sau đó kéo thước đo

Num_of_đơn đặt hàng và số lượng được tính toán

thời gian phân phối cột và thả

nó vào trường giá trị

của bảng ma trận.

Bây giờ, hãy đảm bảo rằng việc tổng hợp

áp dụng khi giao hàng

thời gian là trung bình.

Bằng cách đó, bạn có thể thấy

một hình ảnh ma trận mới được thêm vào

đến khu vực Canvas báo cáo,

cung cấp thông tin

về tổng số đơn đặt hàng

và thời gian giao hàng của từng bang.

Bây giờ hãy sắp xếp

thời gian giao hàng trung bình

theo thứ tự giảm dần bởi

bấm vào tiêu đề.

Để nhìn vào mối quan hệ

giữa hai

các biến liên tục.

Trong trường hợp này, số lượng đơn đặt hàng

thời gian giao hàng trung bình,

một biểu đồ phân tán là

một sự lựa chọn tuyệt vời

Hãy chuyển đổi ma trận của chúng tôi

bảng thành biểu đồ phân tán.

Liệu chúng ta có thể quan sát được

từ biểu đồ phân tán,

rằng không có khuôn mẫu nào giữa

thời gian giao hàng trung bình

và Số_đơn_hàng.

Giả thuyết của chúng tôi nêu rõ với

thời gian giao hàng trung bình,

sẽ có đơn hàng cao hơn

có vẻ sai rồi

đừng nản lòng.

Là một chuyên gia về dữ liệu,

bạn sẽ làm

nhiều giả thuyết

cái đó sẽ không quay lại

hóa ra là sự thật,

nhưng việc kiểm tra chúng là

một phần thiết yếu của một

hành trình chuyên nghiệp dữ liệu.

Vì vậy, tóm tắt video,

chúng tôi đã sử dụng các biện pháp để tạo ra

số lượng đơn đặt hàng và phát hiện ra

rằng số lượng đơn đặt hàng có

không có tác dụng tăng

thời gian giao hàng trung bình của đơn hàng.

Với điều đó, chúng tôi đã giúp Primeby

trong việc giải quyết hai

về các vấn đề của họ.

Hiểu biết về

thời gian giao hàng trung bình

xuyên suốt khác nhau

nêu và phân tích

tác động của tổng số

đơn đặt hàng cho mỗi tiểu bang

về thời gian giao hàng trung bình.

Tiếp theo, bạn sẽ trải qua

một tài liệu đọc mà

mang đến cho bạn sự rõ ràng hơn

trên thích hợp

kịch bản trong đó

cột tính toán và

nên sử dụng các biện pháp