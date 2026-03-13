# 03 cập nhật dữ liệu với thông tin mới

---

Xin chào và chào mừng đến với

video cuối cùng của tuần này.

Hãy giúp PrimeBuy với

tuyên bố vấn đề cuối cùng rằng

đã được đề cập tại

đầu của mô-đun này.

PrimeBuy muốn thành lập

một hệ thống liền mạch để cập nhật

dữ liệu trong trực quan hóa.

Hãy nhảy vào vấn đề.

Mỗi tháng, PrimeBuy

quản lý nhận được

một tệp Excel riêng biệt với

dữ liệu bán hàng hàng tháng từ

bộ phận bán hàng

trong một thư mục được chia sẻ.

Cấu trúc của

bảng trong tập tin

phù hợp hoàn hảo với

phiếu đặt hàng bán hàng.

PrimeBuy gặp phải một

thách thức trong việc duy trì

dựa trên trực quan hóa ngày

trên Dữ liệu mới hiện tại.

Quá trình này bao gồm

cập nhật thủ công

tờ đơn đặt hàng này với

dữ liệu bán hàng hàng tháng mới.

Tuy nhiên, quá trình thủ công này

không hiệu quả và

dễ mắc lỗi.

Đây là cách hiện tại

quá trình hoạt động.

Đầu tiên, họ sao chép tất cả các hàng

từ mới nhận được

dữ liệu bán hàng hàng tháng.

Thứ hai, họ dán thủ công

sao chép dữ liệu vào

tờ đơn đặt hàng gốc,

File excel ở cuối.

Bây giờ cuối cùng, họ

làm mới dữ liệu trong

Power BI để nắm bắt

doanh số hàng tháng mới nhất

dữ liệu từ nút này.

Bây giờ, bạn có để ý điều này không

quá trình trông rất kém hiệu quả?

Mỗi lần họ

nhận được một tập dữ liệu mới,

họ phải làm theo

bài tập này nữa.

Có cái nào tốt hơn không

cách tiếp cận

vấn đề này? Vâng, có.

Chúng ta có thể đạt được hiệu quả bằng cách

kết nối với

thư mục chứa dữ liệu

trực tiếp trong Power BI và

sử dụng bảng nâng cao

hoạt động để đảm bảo

chúng tôi nắm bắt cái mới

tập dữ liệu mỗi khi chúng tôi

nhận dữ liệu bán hàng của tháng mới

từ bộ phận bán hàng.

Với mục đích của bản demo này,

bạn có thể tạo một thư mục mới trong

máy tính của bạn và thêm

doanh số tháng 11 năm 2020

và bán hàng tháng 12

Tệp Excel 2020

vào thư mục này mà chúng tôi

nhận được từ đội ngũ bán hàng.

Hãy tạo một thư mục mới

và đặt cả dữ liệu

tập tin vào thư mục này.

Bây giờ vì mục đích

của bản demo này,

bạn có thể tạo một thư mục mới trong

máy tính của bạn và thêm

bán hàng tháng 11 năm 2020,

và bán hàng tháng 12

Tệp Excel 2020

vào thư mục này mà chúng tôi

đã nhận được từ

đội ngũ bán hàng.

Nhưng trước khi bạn làm như vậy, hãy đảm bảo

các tập tin bạn đang sao chép

được đóng như Windows

sẽ nhắc bạn điều đó

các tập tin đang mở.

Như bạn có thể thấy, bạn

đã nhận được dữ liệu bán hàng cho

Tháng 11 và tháng 12

trong hai tập tin riêng biệt.

Tương tự, bạn mong đợi

nhận tất cả các tập tin của bạn cho

những tháng sắp tới trong

thời trang tương tự

trong thư mục này

cho mỗi tháng.

Bây giờ chúng ta có

đã hiểu vấn đề,

hãy hướng tới Quyền lực

BI để kết nối với

thư mục này và tạo

quá trình tải tự động.

Bây giờ trước khi chúng ta tiếp tục,

hãy tạo một dòng

biểu đồ bằng cách đặt

số tiền bán hàng trên

trục y và thứ tự

ngày trên trục x.

Điều này sẽ cho phép chúng tôi

theo dõi những thay đổi trong

biểu đồ đường khi chúng tôi tải

dữ liệu sắp tới

tháng kể từ các tập tin mới,

đó là tháng 11 và tháng 12.

Như bạn có thể thấy từ biểu đồ,

hiện tại là mới nhất

dữ liệu đơn bán hàng

vẫn là tháng 10 năm 2020.

Bây giờ hãy kết nối với thư mục.

Để làm được điều đó, trong Trang chủ

tab từ dải băng trên cùng,

nhấp vào trình đơn thả xuống Nhận dữ liệu.

Bây giờ bấm vào Thêm và chọn

tùy chọn Thư mục và

bấm vào Kết nối.

Bây giờ trong cửa sổ tiếp theo,

hoặc dán đường dẫn thư mục

hoặc nhấp vào Duyệt để điều hướng

từ máy tính của bạn và nhấp vào

bật Được rồi để kết nối

với thư mục.

Bây giờ trong bản xem trước tiếp theo

cửa sổ Power BI sẽ cung cấp

bạn có siêu dữ liệu của tất cả

các tập tin có trong thư mục đó.

Đối với chúng tôi, hai cột đầu tiên

là quan trọng nhất như

các cột nội dung

giữ nội dung trong

tập tin của chúng tôi ở dạng nén

và tên là

tên của tập tin.

Phần còn lại chúng ta thấy các cột khác

như tiện ích mở rộng, ngày tháng,

đã được sửa đổi, v.v., đó là

không hữu ích lắm

cho mục đích của chúng tôi.

Hãy nhấp chuột vào

thả xuống bên cạnh

Kết hợp và nhấp vào Kết hợp

và chuyển đổi dữ liệu.

Trong cửa sổ mới, nó

cung cấp cho chúng tôi bản xem trước

của tập tin đầu tiên.

Chúng ta có thể thay đổi nó thành

tập tin mà chúng tôi muốn xem.

Hãy giữ nó ở

tập tin đầu tiên và

bấm vào tham số

và nhấp vào Được rồi.

Nó báo đang đánh giá các truy vấn.

Bây giờ nó đưa chúng ta đến

trình soạn thảo truy vấn nguồn.

Ở đây chúng ta thấy Power BI

đã áp dụng rồi

một vài bước cho chúng tôi và có

đã thêm một số cột

đối với chúng tôi là tốt.

Bạn không cần phải

lo lắng về điều tương tự,

chỉ cần điều hướng đến cột

gọi là Loại và chọn

bảng như chúng ta cần bao gồm

bảng từ trang tính Excel

mà chúng tôi đã nhận được.

Sau đó, chọn

cột ngày và tên và

nhấp chuột phải để truy cập

thanh công cụ nhanh từ đó,

và xóa tất cả các cột khác

vì chúng không bắt buộc.

Đảm bảo giữ quyền kiểm soát

nhấn phím trong khi bạn đang chọn

cả hai cột này.

Bây giờ bấm vào

biểu tượng mở rộng bên cạnh

cột dữ liệu và chọn

tất cả các cột và bỏ chọn.

Sử dụng tên cột ban đầu

làm tiền tố và nhấp vào Được rồi.

Cuối cùng, chúng ta có thể loại bỏ

cột tên như

cũng như nó sẽ không như vậy

cần thiết từ thời điểm này.

Với điều đó, chúng tôi đã kết hợp

doanh số hàng tháng chúng tôi

nhận được riêng biệt thông qua

một thư mục cũng có thể

xác nhận bằng cách nhìn vào

cột ngày đặt hàng,

trong đó giữ ngày từ

Tháng 11 và tháng 12.

Nhưng chờ đã, chúng ta cũng cần

để kết hợp điều này với

phiếu bán hàng gốc

chứa đựng của chúng tôi

doanh số lịch sử,

để chúng ta có

một dữ liệu nguyên khối

bao gồm tất cả các dữ liệu bán hàng.

Đừng lo lắng bây giờ

chúng tôi có một cái bàn khác

được tạo từ các tập tin mà chúng tôi

nhận được trong một thư mục chia sẻ,

chúng ta chỉ có thể nối thêm

bảng này với bản gốc của chúng tôi

phiếu đặt hàng bán hàng.

Hãy đến phần Bán hàng

Bảng đặt hàng

và nhấp vào Nối truy vấn.

Một lần nữa, nhấp vào Thêm truy vấn

vì chúng tôi không muốn

tạo thành một bảng mới.

Đúng hơn là chúng tôi muốn thêm

dữ liệu bán hàng vào

phiếu đặt hàng bán hàng có sẵn.

Bây giờ thêm bảng chúng tôi muốn

đính kèm vào phiếu đặt hàng bán hàng.

Trong trường hợp của chúng tôi, đó là

dữ liệu bán hàng mà

nắm giữ dữ liệu bán hàng từ

Tháng 11 và tháng 12.

Từ trình đơn thả xuống, hãy chọn

dữ liệu bán hàng và nhấn OK.

Lưu ý trong các bước áp dụng,

Power BI đã được thêm vào

một truy vấn được thêm vào.

Bây giờ chúng ta hãy di chuyển

bước áp dụng cuối cùng,

đó là truy vấn được thêm vào

trước tất cả

các bước tiền xử lý,

vì vậy nó đảm bảo rằng

tiền xử lý là

được áp dụng trên cái mới

cũng đã ghi lại các tập tin dữ liệu,

và không chứa

vấn đề dữ liệu như

dữ liệu bị thiếu, ngoại lệ,

và sự không nhất quán.

Với điều đó, chúng tôi đã tự động hóa

quá trình dữ liệu

tải trong báo cáo của chúng tôi.

Bây giờ bất cứ khi nào chúng tôi nhận được

một tập dữ liệu hàng tháng mới

trong thư mục chia sẻ của chúng tôi,

chúng ta chỉ cần nhấp vào

nút Làm mới trong Nguồn

BI để phản ánh những thay đổi.

Để lưu những thay đổi này,

hãy nhấn vào Đóng và áp dụng.

Như bạn có thể thấy,

biểu đồ đã được cập nhật ngay bây giờ.

Hãy đảm bảo rằng chúng ta có được

trở lại hệ thống phân cấp.

Bây giờ hãy kéo và di chuyển

bước áp dụng cuối cùng,

đó là phần đính kèm

truy vấn trước

tất cả các bước tiền xử lý

để nó đảm bảo

tiền xử lý là

được áp dụng trên cái mới

tập tin dữ liệu được ghi lại dưới dạng

tốt và không chứa dữ liệu

các vấn đề như thiếu dữ liệu,

các ngoại lệ và những thứ khác

sự không nhất quán.

Hãy nhấn Đóng và Áp dụng

để lưu các thay đổi.

Như chúng ta có thể thấy, với điều đó,

biểu đồ của chúng tôi đã cập nhật

và chúng ta có thể thấy

dữ liệu mới nhất chỉ ra nó

giữ là ngày 30 tháng 12 năm 2020.

Với điều đó, chúng tôi đã tự động hóa

quá trình dữ liệu

tải trong báo cáo của chúng tôi.

Bây giờ bất cứ khi nào chúng tôi nhận được

một tập dữ liệu hàng tháng mới

trong thư mục chia sẻ của chúng tôi,

chúng ta chỉ cần nhấp vào

nút Làm mới trong Nguồn

BI để phản ánh những thay đổi.

Great job in helping PrimeBuy

trong việc giải quyết chúng

vấn đề kinh doanh.

Trong mô-đun này,

chúng tôi đã hỗ trợ PrimeBuy

Bằng cách kiểm tra và làm sạch

dữ liệu thô của họ bằng cách tận dụng

các tùy chọn khác nhau hiện có

dưới trình soạn thảo truy vấn nguồn.

Chúng tôi giúp họ thiết lập

những kết nối còn thiếu

trong mô hình dữ liệu.

Giúp họ tìm hiểu thông tin chi tiết

bằng cách sử dụng các bảng tổng hợp và

cũng tự động hóa

quá trình tải dữ liệu

để làm cho nó liền mạch.

Trong mô-đun tiếp theo,

chúng ta sẽ tiếp tục

hành trình giúp đỡ PrimeBuy của chúng tôi

Bằng một ngôn ngữ mạnh mẽ

trong Power BI được gọi là DAX

biểu thức phân tích dữ liệu.

Hẹn gặp lại bạn vào tuần sau.