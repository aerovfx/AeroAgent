# 02 tại sao chúng ta cần làm sạch dữ liệu

---

Xin chào và chào mừng trở lại.

Trong mô-đun trước,

chúng tôi đã có một cuộc hành trình thú vị

giúp nâng tầm khu nghỉ dưỡng

giải quyết vấn đề kinh doanh của họ

bằng cách hình dung chúng,

với sự giúp đỡ của

biểu đồ và đồ thị.

Trong mô-đun này, chúng tôi

sẽ hỗ trợ PrimeBuy.

PrimeBuy là nhà sản xuất

hoạt động ở nhiều vùng,

cung cấp hàng hóa từ nhỏ đến lớn

cửa hàng bán lẻ gia dụng quy mô vừa.

Công ty cung cấp một

nhiều sản phẩm

chẳng hạn như dụng cụ nấu ăn, nhà

trang trí, nội thất.

Đội ngũ vận hành tại

PrimeBuy đã được thu thập

dữ liệu về đơn đặt hàng bán hàng cho

ba năm qua.

Nhưng họ chưa

bắt đầu phân tích

dữ liệu để làm

quyết định kinh doanh chưa.

Việc quản lý bây giờ

muốn bắt đầu

phân tích dữ liệu bằng

tạo ra sự trực quan hóa,

điều đó sẽ giúp họ trong

hiểu biết về bán hàng

hiệu suất theo khu vực,

sản phẩm và các thông số khác.

Tuy nhiên, khi họ bắt đầu

tạo ra sự trực quan hóa,

họ nhận thấy

có điều gì đó đã bị bỏ lỡ.

Tập dữ liệu họ đang làm việc

chứa rất nhiều

những mâu thuẫn, sai sót.

Một số cột có lỗi,

những người khác đã vô giá trị

giá trị và đã có

thậm chí mâu thuẫn

và các ngoại lệ

điều đó đã cản trở

sự phân tích.

Để thêm vào những thách thức này,

PrimeBuy đã phải điều hướng qua

nhiều bảng để chạy

vào những vấn đề này,

điều này đã trở thành một nhiệm vụ khổng lồ

không có định hướng cụ thể.

Nhóm đã xác định được một

vài nhiệm vụ cần thực hiện

trên tập dữ liệu trước trận chung kết

hình ảnh trực quan được xây dựng,

và chia sẻ với diễn đàn.

Những nhiệm vụ này là nhiệm vụ chung mà

chuyên gia dữ liệu khám phá

trong một tập dữ liệu bán hàng.

Đầu tiên, thực hiện sơ bộ

điều tra trên tập dữ liệu.

Điều này là cần thiết để có được một

tổng quan nhanh về tập dữ liệu,

sự không nhất quán và

các lĩnh vực cải tiến.

Thứ hai, xác định và thiết lập

mối quan hệ trong dữ liệu

hiện ở nhiều bảng khác nhau.

Đây là một yêu cầu,

bất cứ khi nào có dữ liệu

trong nhiều bảng và

có nhiều mối liên hệ chung

giữa nhiều bảng.

Thứ ba, làm sạch và chuyển hóa

dữ liệu để hiểu rõ ràng

chiết khấu trung bình

cung cấp cho

từng kênh bán hàng

trong kinh doanh của họ.

Phân tích mức giảm giá được đưa ra

tới các kênh bán hàng khác nhau

giúp hiểu biết

hiệu quả của họ

trong việc phát triển các kênh bán hàng này.

Thứ tư, thao tác dữ liệu

để xem doanh thu trung bình của

mỗi tháng trên

các kênh bán hàng khác nhau

từ tập dữ liệu có sẵn.

Điều này sẽ mang lại cho PrimeBuy

một cái nhìn toàn cảnh về cách

doanh số hàng tháng được chia nhỏ

kênh bán hàng khác nhau.

Cuối cùng, khám phá để thiết lập

một hệ thống để cập nhật dữ liệu trong

trực quan hóa một cách liền mạch.

Điều này sẽ giúp họ cập nhật

kinh doanh trực quan

vấn đề tự động,

không cần thủ công

cập nhật dữ liệu mới.

May mắn thay, Power BI có

một môi trường mạnh mẽ

để biến đổi và làm sạch

dữ liệu được gọi là

Trình soạn thảo Power Query.

Trong mô-đun này, bạn sẽ sử dụng

Trình soạn thảo Power Query

để giúp PrimeBuy,

và bạn sẽ giải quyết

sự không nhất quán,

thay thế sai

và giá trị null,

và còn nâng cao chất lượng

dữ liệu cho PrimeBuy.

Bạn cũng sẽ học cách

thay đổi kiểu dữ liệu

của các cột,

kiểm tra chúng để tìm lỗi,

và biến đổi chúng thành

rút ra những hiểu biết nâng cao.

Bây giờ chúng ta có một

sự hiểu biết rõ ràng

của các vấn đề

phải đối mặt với PrimeBuy,

chúng ta hãy nhìn vào dữ liệu của họ

trước khi chúng tôi nhập khẩu

nó vào Power BI.

Bộ dữ liệu PrimeBuy

được cấu trúc

thành nhiều tờ

trong một tệp Excel.

Chúng ta hãy nhìn vào từng tờ,

từng cái một. Phiếu đặt hàng bán hàng.

Bảng này ghi lại

chi tiết từng đơn bán hàng,

bao gồm số thứ tự,

kênh bán hàng,

ngày đặt hàng, ngày giao hàng,

và nhiều cột khác.

Bảng khách hàng, bảng này

chứa thông tin về

Khách hàng của PrimeBuy.

Nó bao gồm ID khách hàng và

tên tương ứng của chúng.

Bảng vị trí cửa hàng.

Bảng này cung cấp cái nhìn sâu sắc

vào mạng lưới cửa hàng của PrimeBuy.

Nó bao gồm ID cửa hàng,

tên thành phố, quốc gia,

các loại cửa hàng, và nhiều hơn nữa.

Bảng sản phẩm, bảng này chứa

thông tin về sản phẩm

có sẵn tại PrimeBuy.

Nó bao gồm sản phẩm

ID và tên sản phẩm.

Bảng khu vực, cái này

bảng cung cấp chi tiết

về các vùng khác nhau

PrimeBuy có hoạt động không.

Nó bao gồm mã tiểu bang,

tên tiểu bang và khu vực.

Bảng nhóm bán hàng, bảng này

chứa thông tin về

Đội ngũ bán hàng PrimeBuy,

nó bao gồm ID nhóm bán hàng,

tên nhóm bán hàng và khu vực.

Nhân khẩu học của đội ngũ bán hàng,

bảng này chứa thông tin

về nhân khẩu học của đội ngũ bán hàng.

Nó bao gồm đội ngũ bán hàng

ID, giới tính và độ tuổi.

Từ điển dữ liệu, cái này

chứa mô tả của

các cột khác nhau hiện diện

trên tất cả các tờ giấy

trong tập dữ liệu.

Xin vui lòng đi qua

những chi tiết này để

hiểu sự khác biệt

cột trong trang tính tốt hơn.

Làm ơn lấy ra một ít

đã đến lúc xem xét dữ liệu

có mặt ở nhiều nơi khác nhau

trang dữ liệu PrimeBuy,

trước khi bạn chuyển đến

bài học tiếp theo.

Trong video tiếp theo,

chúng tôi sẽ biểu diễn

một số sơ bộ

cuộc điều tra về

tập dữ liệu bằng cách sử dụng

Trình soạn thảo Power Query