# 04 hiểu-hàm-lọc-tính-và-lọc-phần 1

---

Xin chào và chào mừng trở lại.

Trong video cuối cùng,

chúng tôi đã giúp PrimeBuy

trong việc hiểu việc bán hàng của họ

sử dụng chức năng văn bản.

Bây giờ chúng ta hãy tiến về phía trước và

giải quyết vấn đề cuối cùng,

đó là phân tích doanh số bán hàng của

một sản phẩm cụ thể một cách chi tiết,

và so sánh nó với

các sản phẩm khác.

Chúng ta hãy hiểu

vấn đề trước mắt một cách chi tiết.

PrimeBuy tung ra dòng sản phẩm mới

bàn thiết kế thân thiện với môi trường

đèn vào tháng 3 năm 2018.

Sự ra mắt được đi kèm

đáng kể

nỗ lực tiếp thị.

Một vài tháng sau khi ra mắt,

PrimeBuy muốn hiểu

đèn bàn như thế nào

đã biểu diễn.

Để hoàn thành nhiệm vụ này, trước hết

PrimeBuy muốn phân tích

sự phân chia phần trăm của

bán đèn bàn khắp nơi

các trạng thái khác nhau.

Thứ hai, PrimeBuy muốn

tìm tỷ lệ phần trăm của

đơn đặt hàng đèn bàn có

tỷ suất lợi nhuận ròng

lớn hơn 50 phần trăm.

Thứ ba, PrimeBuy muốn

để phân tích cách

giá đèn bàn so với

các mặt hàng khác trong

hạng mục thiết bị chiếu sáng,

bao gồm cả sàn

đèn và nến.

Hãy giúp PrimeBuy tham gia

hoàn thành hai điều đầu tiên

vấn đề trong video này.

Dựa trên mục tiêu đầu tiên,

chúng ta sẽ cần phần trăm của

tổng doanh số bán đèn như một phần của

tổng doanh số bán hàng của một tiểu bang.

Để có được điều này, chúng ta cũng sẽ

cần tổng doanh số bán đèn.

Cả hai đều có thể

được tạo ra bằng các biện pháp

Để có được điều này, chúng tôi cũng sẽ

cần tổng doanh số bán đèn.

Cả hai đều có thể

được tạo ra bằng các biện pháp

Vấn đề ở

tay cũng yêu cầu

cô lập dữ liệu

dành riêng cho đèn bàn.

Đây là nơi khái niệm về

lọc trở nên cần thiết.

Các chức năng lọc

là một bộ mạnh mẽ của

Chức năng Power BI

điều đó cho phép bạn

lặp lại các hàng của bất kỳ bảng nào,

tạo bối cảnh hàng

cho mỗi mục và

kiểm tra xem

hàng nên là

bao gồm trong của bạn

tính toán hay không.

Hãy cùng khám phá một số

các loại quan trọng của

chức năng lọc mà chúng tôi đang có

sẽ sử dụng trong mô-đun này.

Bản thân chức năng lọc

là một loại phổ biến của

chức năng lọc.

Chức năng lọc trong

Dax cho phép bạn quay trở lại

một tập hợp con của toàn bộ bảng

dựa trên một điều kiện cụ thể.

Nó tạo ra một bảng mới từ

các hàng đáp ứng

tiêu chí bạn chỉ định.

Hàm lọc trong Dax

có hai tham số,

biểu thức bảng và bộ lọc.

Tham số của bảng chiếm

tên của bảng đó

cần phải được lọc.

Thông số này cũng có thể

chứa một biểu thức

kết quả là một bảng.

Thứ hai, biểu thức lọc

bộ lọc Dax Power BI a

điều kiện đó là phải có

đánh giá cho mỗi hàng

của bảng đã cho.

Các hàng dành cho

điều kiện đến

đúng được giữ lại trong khi

phần còn lại được loại bỏ.

Tiếp theo, hàm tính toán

là chức năng cơ bản của

thao tác và kiểm soát

bối cảnh bộ lọc trong

tính toán dữ liệu.

Nó cho phép bạn áp dụng

nhiều bộ lọc cho một công thức.

Cú pháp tính toán

chức năng được đưa ra dưới đây,

biểu thức ở đâu

là những phép tính

hoặc đo lường mà bạn

muốn tính toán và

lọc một và hai và như vậy

điều kiện lọc

bạn muốn nộp đơn vào

các tính toán.

Tiếp theo, chức năng Tất cả là

một Dax mạnh mẽ

chức năng lọc đó

xóa tất cả các bộ lọc khỏi

bảng hoặc cột được đề cập

bên trong hàm.

Nó cho phép chúng ta xem

dữ liệu mà không có bất kỳ

bộ lọc được áp dụng.

Cú pháp của tất cả

chức năng được đưa ra dưới đây,

nơi đặt tên bảng và

tên cột là

tên của bảng,

cột hoặc cột khác

biểu thức bảng

mà bạn muốn

loại bỏ các bộ lọc khỏi.

Với những bài học này,

chúng ta hãy hướng tới

một trang Power BI mới và

tạo ra một thước đo mới,

tổng doanh số bán đèn,

sử dụng hàm tính toán.

Bằng cách sử dụng chức năng này,

chúng ta có thể vượt qua một bộ lọc

để cô lập và

chỉ phân tích dữ liệu

sản phẩm ở đâu

Tên là đèn bàn.

Bây giờ, hãy tạo ra nó.

Điều hướng đến

bảng đo và

nhấp chuột phải vào nó để

tạo ra một biện pháp mới.

Tiếp theo, chuyển tên của

biện pháp này như

Tổng doanh thu đèn.

Sau đó gọi

tính toán hàm.

Nhân tiện, bạn phải có

nhận thấy điều này bật lên bây giờ.

Sự thông minh của Power BI luôn

hướng dẫn chúng tôi về những gì

một chức năng nào đó.

Đó là một công cụ tiện dụng

cung cấp hỗ trợ

trong khi viết cú pháp của

một chức năng và cách sử dụng nó.

Bây giờ trong dấu ngoặc đơn

của hàm tính toán,

gõ các biểu thức đó

bạn muốn đánh giá,

đó là biện pháp hiện có

tổng doanh số bán hàng như

lập luận đầu tiên.

Sau biểu thức,

bạn cần phải

chỉ định bộ lọc là

lập luận thứ hai của

tính toán hàm để cô lập

các dữ liệu liên quan đến

chỉ có sản phẩm đèn bàn.

Để làm điều đó, hãy nhập dấu phẩy và

loại đối số thứ hai sản phẩm

tên bằng đèn bàn.

Bộ lọc này kiểm tra

cột tên sản phẩm

trong bảng sản phẩm và

hạn chế dữ liệu

chỉ bao gồm

hàng nơi sản phẩm

Tên là Đèn bàn.

Đồng thời đảm bảo rằng

T viết hoa trong

chiếc đèn bàn vì nó

tồn tại như trong dữ liệu.

Bây giờ hãy đóng dấu ngoặc đơn lại.

Công thức dax hoàn chỉnh sẽ

trông giống như thế này

Với biện pháp này, hiện nay chúng ta

có biện pháp riêng cho

bán đèn bàn có nguồn gốc

sử dụng hàm tính toán.

Tiếp theo, hãy sử dụng biện pháp này để

hình dung bảng

doanh số bán đèn theo tiểu bang.

Để làm được điều đó trong

phần xem báo cáo,

chọn một cột được nhóm

biểu đồ và kéo trạng thái từ

bảng vị trí cửa hàng và

tổng doanh số bán đèn đo từ

bảng đo và thả

vào trục x và

trục y tương ứng.

Sau khi thực hiện xong, bạn có thể thấy một

biểu đồ cột cụm

được tạo ra hiển thị doanh số bán hàng

đèn bàn cho mỗi tiểu bang.

Tuy nhiên, sự hình dung này

không chính xác là cái gì

chúng tôi đang hướng tới.

Nó cung cấp một số

phân tích doanh số bán hàng theo tiểu bang.

Nhưng mục tiêu của chúng tôi là hiểu

phần trăm đóng góp của

bán đèn bàn cho mỗi tiểu bang.

Về cơ bản, chúng tôi muốn

xác định

tỷ lệ phần trăm cho một tiểu bang,

được tính bằng

tổng doanh số bán đèn bàn cho

trạng thái cụ thể đó chia cho

tổng doanh số bán đèn

cho tất cả các bang.

Để đạt được điều đó, chúng tôi

có thể trực tiếp

chuyển đổi cột xếp chồng này

biểu đồ thành biểu đồ hình tròn,

hoặc trước tiên chúng ta cần tạo

một biện pháp khác để lưu trữ

giá trị theo tỷ lệ phần trăm

và sau đó sử dụng nó để có được

phần trăm đóng góp của

doanh số bán đèn bàn theo tiểu bang.

Nhưng chuyển đổi trực tiếp sang

biểu đồ hình tròn không phải lúc nào cũng có thể

mang lại kết quả chính xác.

Đặc biệt khi có

bộ lọc hoặc bộ cắt khác

tích cực về báo cáo này.

Có biện pháp đảm bảo

rằng các tính toán

chính xác

và cũng đảm bảo khả năng tái sử dụng

tính toán của chúng tôi.

Với sự hiểu biết đó,

hãy tạo ra một thước đo mới,

phần trăm đóng góp

của đèn bàn.

Hãy bắt đầu sáng tạo

một biện pháp mới.

Vì nó là một tỷ lệ,

chúng ta sẽ tận dụng

một hàm chia.

Chúng ta cần chuyển tiếp ba

lý lẽ cho việc này.

Hai cái đầu tiên là

số muốn chia.

Thứ ba là

kết quả thay thế,

nếu kết quả phép chia

ở vô cực,

giống như vấn đề chia cho số không.

Trong trường hợp của chúng tôi, thứ ba

đối số sẽ được đặt thành 0.

Hãy bắt đầu với

viết mã dax.

Đối với trường hợp của chúng ta, tử số sẽ

là tổng doanh số bán đèn bàn cho

một trạng thái cụ thể và

mẫu số sẽ

tổng doanh số bán đèn bàn

khắp các tiểu bang.

Để có được tử số,

đó là tổng doanh số bán hàng của

bán đèn bàn cho

một trạng thái cụ thể,

chúng tôi sử dụng biện pháp đó

chúng tôi đã tạo rồi,

đó là tổng doanh số bán đèn.

Biện pháp này mà

chúng tôi đã tạo trước đó,

hoạt động trong vòng một

lọc bối cảnh.

Có nghĩa là nó tự động

điều chỉnh tính toán của nó

dựa trên trạng thái đã chọn

hoặc bất kỳ ứng dụng nào khác

lọc trong báo cáo,

hoặc thông qua một

trực quan hoặc một slicer.

Hãy lấy mẫu số

thành phần giúp chúng ta có được

tổng doanh số bán đèn bàn

khắp các tiểu bang.

Chúng ta cần sửa đổi bối cảnh

của biện pháp hiện có,

đó là tổng doanh thu đèn,

để lọc tất cả các

các bang và để làm được điều đó,

tính toán hàm

có ích.

Hãy xây dựng mẫu số

thành phần của công thức,

đó là bán hàng cho

tất cả các bang.

Trong hàm tính toán,

chúng tôi sẽ sử dụng chức năng tất cả.

Chức năng all sẽ giúp chúng ta

xóa mọi bộ lọc

trên cột trạng thái

để đảm bảo chúng tôi đang nhận được

tổng doanh số bán đèn bàn

khắp các tiểu bang.

Hãy viết nó ra.

Trong lập luận thứ hai

của hàm tính toán,

chúng ta sẽ truyền hàm all.

Biểu thức này đặc biệt giúp

chúng tôi sẽ loại bỏ tất cả

bộ lọc trên trạng thái.

Đừng lo lắng, chúng ta sẽ học

tất cả đều hoạt động tốt hơn

chi tiết trước thời hạn.

Bây giờ hãy đóng dấu ngoặc đơn

của hàm tính toán trong

mẫu số và vượt qua

về kết quả thay thế

cho hàm chia,

đó là số không.

Hãy đóng dấu ngoặc đơn

cho cả hàm chia nữa.

Một công thức dax sẽ trông

một cái gì đó như thế này

Bây giờ hãy nhấn Enter

để thực hiện biện pháp này.

Với lượt đó,

hãy tiếp tục sử dụng

biện pháp này để

hình dung vấn đề của chúng ta.

Để làm điều đó, hãy chọn

đã được xây dựng trước đó

biểu đồ cột cụm

và từ khung hiển thị,

thay đổi nó thành dòng và

biểu đồ cột cụm.

Bây giờ thêm cái mới

thước đo được tạo ra,

đó là phần trăm

đóng góp của đèn bàn

vào đường trục y

lĩnh vực hình ảnh này.

Làm điều đó bạn có thể thấy

hình ảnh đã được cập nhật để hiển thị

phần trăm đóng góp của

bán đèn bàn khắp nơi

các trạng thái khác nhau.

Nếu bạn để ý kỹ,

những con số đang

hiển thị ở dạng số thập phân.

Để thay đổi nó thành phần trăm,

hãy nhấp vào thước đo

và theo định dạng

tab từ dải băng trên cùng,

hãy tạm dừng biểu tượng phần trăm.

Sử dụng nguyên tố trực quan này,

Tôi đã có thể đạt được những hiểu biết sâu sắc về

phần trăm đóng góp của

tiểu bang khác nhau

cho đèn bàn.

Biểu đồ này cho thấy rằng

gần 17% của

bán đèn bàn

đang đến từ California.

Điều này cho thấy sự mạnh mẽ

sự hiện diện trên thị trường,

và nhu cầu ở trạng thái này.

Bây giờ hãy áp dụng một

lọc theo trạng thái để biết

5 bang hàng đầu

theo tỷ lệ

bán đèn bàn

vào tổng doanh số bán hàng.

Để làm điều đó, chúng ta hãy

bấm vào biểu đồ

và mở rộng bộ lọc

phần của nhà nước.

Thay đổi bộ lọc

gõ để đầu vào,

đặt năm vào mục trưng bày,

và thêm phần trăm

đèn bàn đóng góp

ở phần giá trị.

Với điều đó, hãy nhấp vào

trên bộ lọc Áp dụng.

Làm điều đó Power BI sẽ sắp xếp

trực quan hóa để hiển thị

5 bang hàng đầu với

đóng góp cao nhất

đến việc bán đèn bàn.

5 tiểu bang hàng đầu

đóng góp khoảng

hơn 50% đối với

bán đèn bàn.

Vì Hoa Kỳ có 50 tiểu bang,

chúng ta có thể nói rằng 50%

của doanh số bán hàng cho

đèn bàn có nguồn gốc từ

10% số bang.

Đây là một dấu hiệu rõ ràng

để PrimeBuy tập trung

thêm về các tiểu bang ở

giữa của đồ thị,

họ phải nghĩ ra chiến lược

điều đó có thể giúp họ

đa dạng hóa việc bán hàng

khắp các tiểu bang khác nhau.

Vì dựa dẫm nhiều

về doanh số bán hàng từ

chỉ một vài tiểu bang có thể phơi bày

Hoạt động kinh doanh của PrimeBuy

gặp nhiều rủi ro

chủ yếu là do

thiếu đa dạng hóa.

Chẳng hạn như bất kỳ sự gián đoạn nào

thông qua chuỗi cung ứng khu vực,

như thiên tai,

bất ổn chính trị,

vân vân,

có thể ảnh hưởng nghiêm trọng

khả năng của họ

giao sản phẩm tới

khu vực bán hàng chính của họ.

Ngoài ra đối với PrimeBuy thì

quan trọng để tấn công

sự cân bằng giữa

sản phẩm có lợi nhuận cao

, và nhu cầu thị trường.

Tìm hiểu tỷ trọng của

đơn đặt hàng đèn bàn có

tỷ suất lợi nhuận ròng đáng kể

là rất quan trọng đối với một

hoạch định chiến lược.

Bằng cách tập trung vào những điều này

đơn hàng có lợi nhuận cao,

công ty có thể

phân bổ nguồn lực

hiệu quả và phù hợp

nỗ lực tiếp thị

cho những sản phẩm như vậy.

Bây giờ chúng ta hãy đánh vào

vấn đề tiếp theo.

Để hình dung PrimeBuy này

muốn tìm tỉ lệ phần trăm của

đơn đặt hàng đèn bàn có

tỷ suất lợi nhuận ròng

lớn hơn 50%.

Hãy giúp PrimeBuy

trong việc hình dung

vấn đề này bằng cách sử dụng

tính toán hàm.

Điều hướng đến bảng đo

và nhấp chuột phải để

tạo ra một biện pháp mới.

Như trên tên của

biện pháp này như

đơn đặt hàng đèn bàn

tỷ suất lợi nhuận cao.

Bắt đầu bằng cách gọi

tính toán hàm,

bên trong kiểu dấu ngoặc đơn

những biểu hiện đó

bạn muốn đánh giá,

đó là cái hiện có

đo số lượng

mệnh lệnh làm đối số đầu tiên

của hàm tính toán.

Bây giờ chúng ta gặp phải một thử thách.

Thông thường, bước tiếp theo

sẽ là chỉ định

bộ lọc thứ hai

đối số của hàm tính toán.

Mục đích của chúng tôi là cô lập

những mệnh lệnh đó

dành riêng cho

sản phẩm đèn bàn,

và có lợi nhuận ròng

lớn hơn 50%.

Một cách tiếp cận điển hình có thể

liên quan đến việc kêu gọi

biện pháp khác,

tỷ suất lợi nhuận ròng, và

đặt ra một điều kiện,

lớn hơn 50%,

hãy thử điều đó.

Vì tỷ suất lợi nhuận ròng

tính bằng phần trăm,

vì vậy chúng tôi sẽ viết

nó là 0,5 cho 50%.

Công thức sẽ trông

một cái gì đó như thế này

Hãy thử nhấn "Enter".

Có một sắc thái cần hiểu

đối số thứ hai của tính toán

không thể trực tiếp sử dụng

một biện pháp như

tỷ suất lợi nhuận ròng đến

đánh giá một điều kiện

Hàm mong đợi một

cột từ một bảng,

đó là một Boolean

điều kiện và không

một thước đo như lợi nhuận ròng

biên trong trường hợp này.

Để khắc phục hạn chế này,

chúng ta sẽ tận dụng

chức năng lọc bên trong

chức năng tính toán.

Hãy thêm một bộ lọc như

lập luận thứ hai của

chức năng tính toán.

Chức năng lọc

sẽ giúp chúng ta tạo ra

một bảng mới chỉ

bao gồm các hàng trong đó

sản phẩm là đèn bàn của

phiếu đặt hàng bán hàng và

tỷ suất lợi nhuận ròng

lớn hơn 50%.

Hãy làm điều đó. Như bạn có thể thấy,

chức năng lọc yêu cầu

một bảng làm đối số đầu tiên của nó,

mà nó sẽ xử lý hàng theo

hàng để áp dụng điều kiện này.

Trong trường hợp của chúng tôi, bảng này

là phiếu đặt hàng bán hàng.

Bây giờ là đối số thứ hai

của chức năng LỌC,

chuyển tỷ suất lợi nhuận ròng

lớn hơn 0,5 đến

đảm bảo chúng tôi đang xem xét

đơn đặt hàng lợi nhuận cao và

đóng chức năng lọc.

Bây giờ là đối số thứ ba cho

chức năng TÍNH TOÁN này,

chúng ta có thể thêm một bộ lọc khác cho

tên sản phẩm đèn bàn

Vì điều kiện này là

Boolean về bản chất,

tính toán chúng ta sẽ không có

vấn đề xử lý việc này.

Hãy xóa đi

mã không cần thiết.

Hai điều kiện này đảm bảo

mà chúng tôi đang đếm

số lượng

đơn đặt hàng cho lợi nhuận ròng

biên độ lớn hơn

50% và sản phẩm

đèn bàn tên.

Công thức cuối cùng

sẽ trông như thế này

Với điều đó, chúng ta có

đã tạo thành công

một biện pháp mới sử dụng

một chức năng lọc bên trong

một hàm TÍNH TOÁN.

Bây giờ để hình dung tỷ lệ phần trăm

số đơn đặt hàng đèn bàn có

tỷ suất lợi nhuận lớn hơn

hơn 50% so với

tổng số

các đơn đặt hàng trên bàn,

chúng ta cần tạo ra

biện pháp khác đó

nắm giữ tổng số đơn đặt hàng đèn bàn.

Hãy tạo ra thước đo này.

Hãy gọi biện pháp này

như đơn đặt hàng đèn bàn.

Bạn biết bây giờ chúng tôi

sẽ tận dụng

hàm TÍNH TOÁN vì chúng ta

muốn thay đổi

lọc bối cảnh.

Ngoài ra, chúng ta sẽ tận dụng

cái đã được tạo

số biện pháp đặt hàng,

vì chúng tôi muốn

đếm số

các đơn đặt hàng đèn bàn.

Như bạn có thể thấy, đây là

sức mạnh của văn bản

biện pháp rõ ràng.

Từng lớp một, bạn có thể thêm

sự phức tạp trong các biện pháp của bạn.

Hãy thêm một cái khác

điều kiện đảm bảo

dữ liệu đã được lọc

chỉ dành cho đèn bàn.

Công thức cuối cùng

sẽ trông như thế này

Hãy nhấn Enter để

tạo ra thước đo này.

Cuối cùng, chúng ta cũng cần

tạo ra một biện pháp khác

tính toán đó

tỷ lệ cao

đơn đặt hàng đèn bàn lề

từ tổng số

đơn đặt hàng đèn bàn.

Như bạn đoán, đó là một tỷ lệ

và do đó chúng tôi sẽ thực hiện

sử dụng chức năng CHIA.

Trong tử số,

chúng tôi sẽ chuyển tiếp

đèn bàn

đặt lệnh có tỷ suất lợi nhuận cao,

và ở mẫu số,

chúng ta cần tổng số

đơn đặt hàng đèn bàn.

Như một cách thực hành tốt nhất,

in the third argument,

chúng ta sẽ vượt qua số 0 một lần nữa.

Công thức của chúng ta sẽ trông

một cái gì đó như thế này

Một lần nữa, hãy đảm bảo chuyển đổi

thước đo này thành phần trăm.

Bây giờ hãy kéo thước đo này

trong một thẻ và kiểm tra xem đó là gì

tỷ lệ lợi nhuận cao

đơn đặt hàng đèn bàn.

Với sự trợ giúp của hình ảnh này,

PrimeBuy nhận thấy rằng gần 13%

đơn đặt hàng đèn bàn đã đưa cho họ

a profit margin

lớn hơn 50%.

Điều này mang lại cho PrimeBuy sự chắc chắn về

chiếc giường họ đã chiếm

with the introduction of

table lamps as

selling products with

higher margin generate

more profit per sale,

contributing to overall

tăng trưởng tài chính

và sự ổn định của doanh nghiệp.

Cho đến nay trong video này,

chúng tôi đã sử dụng

hàm TÍNH TOÁN và

Hàm FILTER để giải quyết vấn đề

Vấn đề kinh doanh của PrimeBuy.

Hãy hiểu sự khác biệt

giữa LỌC và

hàm TÍNH TOÁN.

LỌC là lý tưởng khi tạo

bảng mới dựa trên

điều kiện cụ thể,

đặc biệt hữu ích nếu

hoạt động tiếp theo

trên các bảng này là bắt buộc.

Trong khi hàm CALCULATE

là lựa chọn để thay đổi

lọc bối cảnh

không có chi phí chung

của các bảng mới: Nó hiệu quả,

ngắn gọn và tuyệt vời để điều chỉnh

tính toán hiện có.

LỌC cũng được sử dụng

bên trong TÍNH TOÁN trong

những trường hợp chúng tôi muốn

lọc dữ liệu

dựa trên một thước đo.

Vì FILTER lặp lại

qua mỗi hàng trong bảng,

nó có thể chậm và

bộ xử lý chuyên sâu.

Không sử dụng LỌC nếu

Hàm TÍNH TOÁN sẽ

thực hiện tương tự

thứ. Bây giờ chỉ vậy thôi.

Trong video này, chúng tôi đã

đã giúp PrimeBuy hiểu

phần trăm đóng góp của

đèn bàn theo các trạng thái khác nhau.

Chúng tôi cũng phát hiện ra

bao nhiêu phần trăm của

đơn đặt hàng đèn bàn đã đưa ra một

tỷ suất lợi nhuận ròng

lớn hơn 50%.

Hãy tiến về phía trước và giải quyết

vấn đề thứ ba

trong video tiếp theo,

đó là PrimeBuy muốn

phân tích đèn bàn như thế nào

giá vé so với các mặt hàng khác

trong ánh sáng

thể loại lịch thi đấu,

bao gồm đèn sàn và

nến. Hẹn gặp bạn ở đó.