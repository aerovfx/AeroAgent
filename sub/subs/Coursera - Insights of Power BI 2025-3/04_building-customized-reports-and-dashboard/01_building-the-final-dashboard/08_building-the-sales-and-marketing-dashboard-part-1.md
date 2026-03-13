# 08-xây dựng-bán-và-tiếp thị-bảng điều khiển-phần 1

---

Xin chào và chào mừng trở lại.

Synergix đã hoạt động khá tốt

cuộc hành trình phải không?

Bạn đã hiểu sâu sắc

số của họ

hiểu biết sâu sắc và có một

nắm bắt khá tốt

về số liệu tiếp thị của họ,

nhưng giờ là lúc quyết định,

nhóm phân tích tại Synergix

đã có những hiểu biết sâu sắc.

Họ có động lực,

nhưng cái họ cần là

một cái nhìn tổng hợp

để trình bày tất cả của họ

những phát hiện rõ ràng,

và cách sắc nét

tới các nhà điều hành.

Trong video này, chúng tôi sẽ tạo

bán hàng và tiếp thị

đó là bảng điều khiển

được thiết kế riêng cho Synergix,

những nhà điều hành hàng đầu.

Đây sẽ là một điều rất

bảng điều khiển mô tả,

phân tích các chỉ số tiếp thị,

doanh thu, số lượng hàng bán v.v. tại

mức độ hạt khác nhau,

như phân đoạn nghiêng, v.v.

Hãy chuyển sang một trang mới và

đổi tên nó thành

Bảng điều khiển của Synergix.

Chúng tôi sẽ bắt đầu với các bộ lọc

cho ngày và ID nghiêng.

Những bộ lọc này sẽ cho phép

các giám đốc điều hành để khoan

xuống thời gian cụ thể

thời kỳ hoặc sản phẩm.

Bây giờ chúng ta hãy bắt tay vào làm việc.

Chúng ta sẽ bắt đầu bằng việc tạo một ngày

bộ lọc và bộ lọc ID nghiêng.

Hãy kéo ngày từ

Bảng lịch và chọn

hình ảnh như máy cắt.

Đảm bảo rằng chúng tôi không

chọn hệ thống phân cấp ngày.

Từ định dạng tab trực quan của bạn.

Chọn cài đặt bộ cắt và

dưới đó chọn giữa.

Bây giờ với bộ cắt ID nghiêng này,

có một thách thức.

Chọn ID nghiêng nào.

Nếu chúng ta chọn từ

bảng trực tuyến,

thì các biện pháp phụ thuộc

trên bàn POS sẽ không

được lọc dưới dạng bảng trực tuyến

và POS không được kết nối,

vì vậy các bộ lọc sẽ không chảy giữa

hai bảng này và ngược lại.

Điều này có thể được xác nhận từ

chế độ xem mô hình là tốt.

Không có trực tiếp

mối quan hệ giữa dữ liệu POS,

và bảng dữ liệu trực tuyến.

Chúng ta cần tạo ra

một bảng bổ sung

trong Power BI đó

giữ tất cả các ID lệch duy nhất từ ​​

cả bảng trực tuyến và POS.

Chúng tôi sẽ tạo ra một

mối quan hệ từ

bảng mới được tạo để

cả hai bảng sự kiện này.

Điều này sẽ cho phép chúng tôi

bộ lọc ID nghiêng

đi qua cả hai

của những bảng này,

làm cho nó trở thành một phân tích có liên quan.

Theo một cách nào đó, độ lệch mới của chúng tôi

bảng mã sẽ hoạt động như thế nào

một bảng kích thước đó

sẽ vượt qua các bộ lọc

tới cả POS và

bảng thực tế trực tuyến.

Hãy nhanh chóng tạo một

bàn mới. Mã lệch.

Chúng tôi sẽ sử dụng

chức năng công đoàn trong

Power BI và kết hợp

mã riêng biệt của

ID lệch từ trực tuyến

có mã riêng biệt

ID lệch từ POS

cái bàn. Hãy mã hóa nó ra.

Chức năng riêng biệt

ở đây giúp chúng tôi quay trở lại

danh sách giá trị duy nhất hoặc

cột giữ như một bảng.

Trong khi chức năng công đoàn

kết hợp cả hai kết quả

biểu thức bảng,

chúng tôi nhận được bằng cách sử dụng chức năng riêng biệt.

Bây giờ như chúng ta đã biết, chúng ta sẽ

chắc chắn có ID sai lệch

lặp lại trong cả hai trực tuyến

cũng như dữ liệu POS.

Một lần nữa, chúng tôi sẽ gói DAX

với sự khác biệt để trở lại

chỉ có tập hợp riêng biệt của

ID lệch. Hãy làm điều đó.

Công thức DAX cuối cùng

sẽ trông như thế này

Hãy nhấn Enter để

tạo bảng này.

Hãy kiểm tra cái mới này

bảng trong chế độ xem dữ liệu.

Như bạn có thể thấy, độ lệch

bảng mã chứa

297 mã khác biệt từ

cả hai bảng này.

Sau khi phát triển bảng này,

Hãy tạo ra một mối quan hệ

giữa cái bàn này

với bảng POS và VPC trực tuyến.

Bây giờ, khi đã xong việc đó,

hãy thêm một slicer

ID Skew đã được lấy

từ bảng mã Skew

liền kề với bộ lọc ngày.

Đảm bảo thay đổi

cài đặt máy thái

phong cách để thả xuống.

Bạn thấy đấy, trong khi máy thái của chúng tôi

có thể cho chúng tôi một cái nhìn chi tiết,

các giám đốc điều hành tại Synergix

thường sẽ cần một

tổng quan cấp cao.

Các nhà điều hành không phải lúc nào cũng

có sự xa xỉ về thời gian.

Họ cần phải xem làm thế nào

doanh nghiệp đang làm tại

một cái nhìn dựa trên nơi

họ đã và đang

họ đang ở đâu.

Xem xét tất cả điều này,

hãy kết hợp

những KPI đó mà chúng tôi

được tạo trước đó vào

trang tổng quan của chúng tôi để đảm bảo rằng

Ban lãnh đạo Synergix có

tiếp thị quan trọng

những con số liên quan họ

cần ngay trong tầm tay của họ.

Khi đã làm xong việc đó, chúng tôi

đã bao gồm một trong

các khía cạnh chính của

tạo ra doanh số bán hàng và

bảng điều khiển tiếp thị.

Bây giờ hãy tiếp tục và thêm

điều quan trọng khác

trực quan hóa rằng

chúng tôi đã tạo ra trong

những video trước đó.

Khi đã xong, chúng tôi đã thêm

tất cả những điều quan trọng

trực quan hóa để

bảng điều khiển sẽ giúp ích

các nhà điều hành đưa ra thông tin

các quyết định tiếp thị.

Bây giờ đây là nơi nó

trở nên thú vị.

Synergix có kế hoạch bơm

trong một ngân sách đáng kể

vào việc quảng bá của họ

phạm vi chăm sóc da

trong những tháng mùa đông,

khi da khô

một mối quan tâm chung.

Hoặc có lẽ, họ sẽ tăng cường

chương trình khuyến mãi chăm sóc tóc của họ

trong suốt mùa hè,

tận dụng vốn

nhu cầu về sản phẩm tóc

cung cấp sự bảo vệ chống lại

nắng nóng gay gắt.

Bây giờ các giám đốc điều hành giám sát

những chiến dịch này muốn

nhanh chóng đánh giá hiệu quả

của các phân khúc này

khuyến mại cụ thể.

Hãy đảm bảo của chúng tôi

trang bị bảng điều khiển

Lãnh đạo Synergix với

khả năng quan trọng này

và thêm bộ cắt phân đoạn của chúng tôi.

Nhưng ở đây chúng ta có

gặp phải một vấn đề.

Như chúng ta có thể thấy, máy cắt lát

có thể không tương tác với

một số biểu đồ hoặc KPI như CTR,

CPC và chi tiết chi tiêu.

Những con số vẫn

vẫn như cũ.

Trước khi chúng tôi khắc phục vấn đề này,

trước tiên chúng ta hãy cố gắng hiểu

tại sao điều này lại xảy ra

Như chúng ta đã biết, cột phân đoạn

độc quyền cho bảng POS.

Biểu đồ được xây dựng bằng bảng POS,

như thẻ KPI lưu lượng truy cập web và

biểu đồ khu vực phân chia doanh thu,

sẽ phản hồi với slicer.

Nhưng các biểu đồ tùy thuộc vào

bảng trực tuyến hoặc bảng VPC,

nói biểu đồ KPI CPC hoặc

biểu đồ phân tích chi tiêu

sẽ không nhận ra bộ lọc này.

Để hiểu điều này tốt hơn,

Hãy nhìn vào khung nhìn mô hình của chúng tôi.

Khi kiểm tra chặt chẽ,

chúng tôi thấy điều đó

cột phân đoạn

không trực tiếp

được kết nối với VPC hoặc dữ liệu trực tuyến.

Nếu bạn cố gắng tạo

một mối quan hệ trực tiếp

sử dụng cột ID SKU,

Power BI giơ cờ.

Nó nói nó sẽ tạo ra

sự mơ hồ giữa

mã SKew và POS.

Đây là điều

Bàn trực tuyến là trực tiếp

liên quan đến bảng mã SKew,

và gián tiếp liên quan đến

SKew mã vào bảng POS.

Kết nối kép này tạo ra

sự nhầm lẫn đối với Power BI,

nghĩ về nó như là có

hai ông chủ và không biết

tuân theo mệnh lệnh của ai.

Hãy dừng lại ở đây. Chúng tôi đã học được

nhiều điều mới mẻ trong video này.

Hãy sửa lại những khái niệm này

trước khi chúng ta tiếp tục

trong phần tiếp theo.