# 03 giới thiệu về bối cảnh cột và hàng được tính toán

---

Xin chào và chào mừng trở lại.

Hãy chuyển sang Power BI để trợ giúp

PrimeBI trong việc giải quyết vấn đề của họ

vấn đề kinh doanh đầu tiên.

PrimeBI đã và đang nhận được

phản hồi của khách hàng

về thời gian giao hàng.

Một số khách hàng tỏ ra phấn khích

nhận được đơn đặt hàng của họ ngay lập tức,

nhưng những người khác, họ đang chờ đợi

quá lâu để giải quyết vấn đề này.

PrimeBI cần hiểu

phải mất bao nhiêu ngày,

trung bình cho các đơn đặt hàng

được giao trong

các trạng thái khác nhau.

Hãy cố gắng

giải quyết vấn đề này

bằng cách đầu tiên tìm ra

các cột có liên quan.

Điều hướng đến Chế độ xem dữ liệu và

chọn bảng Đơn đặt hàng bán hàng.

Khi kiểm tra kỹ hơn,

bạn có thể nhận thấy

mà chúng tôi không có

bất kỳ cột nào liên quan đến

thời gian giao hàng cho các đơn đặt hàng.

Nhưng nếu bạn đến gần

nhìn vào dữ liệu,

chúng tôi có hai cột sử dụng

chúng ta có thể rút ra được

cột thời gian giao hàng.

Như bạn đã xác định, chúng tôi có thể tạo

cột thời gian giao hàng bằng

trừ ngày đặt hàng

kể từ ngày giao hàng.

Đây, để tôi giới thiệu

bạn với khái niệm về

cột tính toán.

Các cột được tính toán là

cột mới được tạo

sử dụng phép tính trên

các cột hiện có bằng DAX.

Chức năng cột được tính toán,

giống như bất kỳ khác

cột trong một bảng,

và có thể được sử dụng

trong suốt báo cáo.

Biểu thức DAX được xác định cho

một cột được tính toán hoạt động

trong bối cảnh của

mỗi hàng trong bảng.

Nói một cách đơn giản hơn, tính toán

các cột hoạt động theo từng hàng.

Hiểu bối cảnh hàng.

Ví dụ, trong

mô-đun trước,

khi tạo

cột số tiền bán hàng,

cột tính toán được đánh giá

bối cảnh hàng bằng cách thực hiện

các phép tính cần thiết và

trả lại số liệu đã tính toán

giá trị cho mỗi hàng.

Ngoài ra, hãy nhớ rằng

cột được tính toán

mở rộng bảng và dữ liệu của bạn.

Do đó, cột tính toán

chiếm thêm bộ nhớ.

Bây giờ, được trang bị

sự hiểu biết này,

chúng tôi đã sẵn sàng để tạo ra

cột thời gian giao hàng và sử dụng

nó để so sánh thời gian giao hàng

khắp các tiểu bang khác nhau.

Trong phiếu đặt hàng bán hàng,

nhấp vào Cột mới

hiện diện dưới

phần tính toán.

Một thanh công thức sẽ

xuất hiện trên màn hình.

Trong thanh Công thức, chúng ta sẽ sử dụng

công thức tính thuế

thời gian giao hàng.

Để có được thời gian giao hàng,

chúng ta cần tính toán

thời gian trôi qua

giữa sự khởi đầu của

một đơn đặt hàng và sự xuất hiện của nó.

Để tính toán điều này

sử dụng công thức DAX,

gõ vào cột

đặt tên là thời gian giao hàng,

và chuyển vào cột ngày giao hàng

từ phiếu đặt hàng bán hàng,

và trừ nó với

cột ngày đặt hàng.

Công thức của bạn sẽ trông

một cái gì đó như thế này

Bấm vào Enter và bây giờ

bạn có thể thấy một cột mới.

Thời gian giao hàng đã được thêm vào

trong phiếu đặt hàng bán hàng.

Nhưng có điều gì đó không ổn ở đây.

Bạn có thể thấy stent đó

mang lại cột mới

ở định dạng mong muốn,

đó là số ngày

giữa hai cột.

Lý do là khi bạn trừ

hai cột ngày tháng, trong trường hợp này,

ngày đặt hàng và ngày giao hàng,

Power BI có xu hướng trả về

kết quả ở định dạng ngày giờ.

Bây giờ để thay đổi điều này,

chúng ta cần nhấp vào

cột thời gian giao hàng

mà chúng tôi vừa tạo

và sau đó thay đổi kiểu dữ liệu

từ ngày giờ đến số nguyên.

Bấm vào Có. Làm điều đó,

bạn có thể thấy

lịch trình giao hàng

đã được làm mới để hiển thị

các giá trị và ngày.

Với điều này, chúng tôi đã tạo ra

một tính toán mới

cột, thời gian giao hàng.

Bây giờ hãy sử dụng cột này để

hình dung thời gian giao hàng

khắp các tiểu bang khác nhau.

Để làm điều đó, hãy điều hướng đến

chế độ xem báo cáo

phần và chọn

bảng ma trận từ

ngăn hiển thị.

Bây giờ thêm một cột trạng thái

từ bảng vùng tới

trường hàng và

cột thời gian giao hàng từ

phiếu đặt hàng bán hàng

vào trường giá trị.

Bạn có thể thấy Sức mạnh

BI, theo mặc định,

đã tổng hợp

thời gian giao hàng cho một số,

nhưng chúng tôi sẽ yêu cầu

trung bình của

thời gian giao hàng cho hội chợ

so sánh giữa các bang.

Hãy thay đổi

tổng hợp đến mức trung bình.

Làm điều đó, bạn có thể thấy một

ma trận được tạo có chứa

một danh sách các tiểu bang và của họ

trung bình tương ứng

thời gian giao hàng.

Cuối cùng nhấn vào cột

tiêu đề để sắp xếp ma trận trong

thứ tự giảm dần của

thời gian giao hàng đến

trạng thái trả về mất

thời gian lâu nhất để

giao hàng.

Bây giờ khi chúng ta nhìn vào dữ liệu,

chúng ta có thể thấy mức phân phối trung bình

thời gian cho mỗi trạng thái.

Điều thú vị là Mississippi

đứng đầu bảng xếp hạng,

theo sau là Alabama.

Điều này ngụ ý rằng những trạng thái này

có cái dài nhất

thời gian giao hàng trung bình.

Ngoài ra, hãy nhấp chuột vào

tiêu đề cột một lần nữa để

sắp xếp nó theo thứ tự tăng dần

về thời gian giao hàng trung bình.

Ở đây chúng ta thấy Bắc Dakota và

Nam Dakota là hai trong số

trạng thái hoạt động tốt nhất.

Điều này có giá trị

thông tin cho PrimeBI.

Nó xác định chính xác

công ty ở đâu

cần phải nỗ lực cải thiện

quá trình giao hàng của nó.

Họ có thể học hỏi từ

những thực hành tốt

theo sau ở miền Bắc và

Nam Dakota và cố gắng

thực hiện chúng ở các tiểu bang khác.

Nhanh chóng và đáng tin cậy

việc giao hàng có thể

tăng cường đáng kể khách hàng

sự hài lòng và lòng trung thành.

Bây giờ một câu hỏi rằng

có thể xuất hiện là,

là mức trung bình

thời gian giao hàng nhận được

bị ảnh hưởng bởi

số lượng đơn đặt hàng?

Hãy đánh giá điều đó

trong video tiếp theo bởi

sử dụng một khái niệm mới

gọi là biện pháp thuế.