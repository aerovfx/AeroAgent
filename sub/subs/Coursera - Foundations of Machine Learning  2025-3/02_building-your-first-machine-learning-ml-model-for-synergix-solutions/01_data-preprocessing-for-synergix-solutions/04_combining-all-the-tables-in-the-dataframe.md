# 04 kết hợp tất cả các bảng trong khung dữ liệu

---

Hãy chắc chắn rằng bạn chạy tất cả

các ô phía trên trước khi bạn bắt đầu.

Giống như chúng ta đã làm trước đó,

hãy bắt đầu với việc đọc

dữ liệu tìm kiếm.

Nó chứa

thông tin liên quan đến

thứ hạng tìm kiếm của

một sản phẩm trong một tuần,

và số lượng duy nhất

cụm từ tìm kiếm cho mỗi SKU_ID.

Bây giờ, hãy lấy một mô tả

của tất cả các biến.

Chúng ta có thể rút ra được

quan sát sau đây

từ khung dữ liệu tìm kiếm.

Dữ liệu tìm kiếm

chỉ ở đó cho

295 SKU_ID so với

297 SKU_ID trong dữ liệu POS.

Nhìn vào ngày

cột trong search.head,

có vẻ như dữ liệu ở

cấp tuần. Chúng tôi sẽ xác minh điều này.

Giống như dữ liệu POS,

dữ liệu tìm kiếm cũng

bắt đầu từ ngày 2 tháng 1,

năm 2021 và kéo dài cho đến

Ngày 31 tháng 12 năm 2022.

Chúng tôi có 25.711 hồ sơ

trong khung dữ liệu tìm kiếm,

đó là 5.474 hồ sơ

ít hơn dữ liệu POS.

Điều này gợi ý rằng

không phải tất cả các sản phẩm

có một kỷ lục cho mỗi tuần.

Hãy kiểm tra xem cái nào trong số

SKU_ID bị thiếu.

Để làm điều này, chúng tôi tạo ra hai bộ

SKU_ID trong cả hai khung dữ liệu,

và trừ các giá trị.

SKU780 và SKU952 là

hai SKU_ID đó

không có ở đó trong

khung dữ liệu tìm kiếm.

Điều này có thể có nghĩa là chúng ta

không có dữ liệu cho

hai sản phẩm này hoặc có

không có hoạt động liên quan đến

xếp hạng tìm kiếm cho

hai sản phẩm này.

Lý tưởng nhất là chúng ta sẽ cần

để nói chuyện với đội,

và điều tra việc này

quan trọng hơn nữa.

Bây giờ, hãy trích xuất

ngày trong tuần

cho những ngày tháng,

và xác nhận nếu ngày

hàng tuần hay không.

Dữ liệu tìm kiếm ở đây là

cũng hàng tuần,

và tất cả những ngày này trong

khung dữ liệu

thuộc về thứ bảy.

Hãy hợp nhất tìm kiếm

khung dữ liệu với dữ liệu.

Bây giờ chúng ta hãy kiểm tra

hình dạng của dữ liệu.

Chúng ta có thể thấy nó có

cùng một số lượng

quan sát như trước đó,

nhưng đã thêm hai cột nữa.

Tiếp theo, hãy đọc dữ liệu VPC

và nhận được một mô tả

của tất cả các biến của nó.

Phiếu giảm giá do VPC hoặc nhà cung cấp cung cấp,

truyền đạt chi phí

phát sinh bởi sự hiệp lực để

bán sản phẩm tại

một tỷ lệ chiết khấu

trong một khoảng thời gian cụ thể.

Điều này được sử dụng để

tăng doanh số bán hàng.

Hãy chạy ba ô bên dưới.

Sau đây khác

quan sát ban đầu

từ khung dữ liệu VPC.

Dữ liệu VPC chỉ có ở đó cho

260 SKU_ID so với

290 SKU_ID trong dữ liệu POS.

Điều này có nghĩa là có

nhiều sản phẩm làm được

không có bất kỳ phiếu giảm giá.

Nhìn vào ngày

cột trong VPC.head,

có vẻ như dữ liệu là

trải dài trong tuần.

Dữ liệu VPC có

thông tin chỉ từ

Ngày 2 tháng 1 năm 2021 tới

Ngày 27 tháng 8 năm 2022.

Điều này có nghĩa là không

tất cả các sản phẩm

có phiếu giảm giá trên khắp

tất cả các ngày.

Chúng tôi đã có rồi

tổng chi tiêu,

đó là tổng số tiền

chi cho các chương trình khuyến mãi.

Chi tiêu thay đổi cho khuyến mãi

đã là một phần rồi

tổng số tiền chi tiêu,

và do đó, nó không bắt buộc.

Đối với một ngày cụ thể,

số lượng khuyến mãi tối đa

là hai và tối thiểu là một.

Hãy bắt đầu với việc thả

chi tiêu thay đổi

trên cột khuyến mãi.

Bây giờ chúng ta hãy kiểm tra xem cái nào

SKU_ID bị thiếu.

Để làm điều này, chúng tôi tạo ra hai bộ

SKU_ID trong cả hai khung dữ liệu,

và trừ các giá trị

giống như chúng tôi đã làm trước đó.

Đây là SKU_ID

đó là một phần của

dữ liệu kết hợp nhưng không

có trong dữ liệu VPC.

Hãy trích xuất những ngày

trong tuần từ VPC.

Ở đây cũng vậy, tất cả các ngày

thuộc về thứ Bảy.

Với điều này, chúng ta có thể chuyển sang

kết hợp dữ liệu VPC

với dữ liệu chính,

và nhìn vào hình dạng của nó.

Chúng ta có thể thấy điều đó

dữ liệu kết hợp của chúng tôi có hai

nhiều cột hơn trước.

Bây giờ hãy phân tích

dữ liệu trực tuyến.

Dữ liệu trực tuyến chứa

tất cả dữ liệu

liên quan đến tiếp thị trực tuyến,

bao gồm các nhấp chuột,

ấn tượng, v.v.

Chúng ta sẽ bắt đầu với

đọc dữ liệu trực tuyến,

và tìm ra

các mô tả biến.

Chúng ta có thể quan sát sự

theo đuổi những điều

Chỉ có 249 SKU_ID có

bất kỳ hình thức trực tuyến

hoạt động tiếp thị,

phần còn lại không có.

Dữ liệu trực tuyến gợi ý một số hoặc

các hoạt động tiếp thị khác

đã xảy ra suốt

hai năm,

giống như dữ liệu POS.

Là một phần của quá trình,

chúng ta sẽ lặp lại điều tương tự

tập thể dục nơi chúng tôi tìm thấy

SKU_ID bị thiếu trong

so sánh dữ liệu trực tuyến

đến dữ liệu kết hợp.

Chúng ta có thể thấy SKU_ID

đó là một phần

của dữ liệu kết hợp nhưng

không phải dữ liệu trực tuyến.

Hãy trích xuất ngày của

tuần kể từ cột ngày.

Một lần nữa, tất cả những ngày tháng

thuộc về thứ Bảy.

Với điều này, chúng ta có thể

chuyển sang kết hợp

dữ liệu trực tuyến với

khung dữ liệu,

và quan sát hình dạng của nó.

Đến thời điểm này, tôi hy vọng bạn có

nhận ra rằng chúng tôi

chỉ tổng hợp

dữ liệu sản phẩm và không

bất kỳ bảng nào khác như

dữ liệu sản phẩm là bảng duy nhất

với dữ liệu hiện tại

ở mức độ hàng ngày.

Với điều này, chúng ta hãy

chuyển sang sáp nhập

dữ liệu trực tuyến với chúng tôi

dữ liệu tên khung dữ liệu.

Chúng ta cũng có thể kiểm tra

hình dạng của dữ liệu.

Như bạn có thể thấy, số

các quan sát đều giống nhau,

trong khi các cột có

tăng lên bốn.

Bây giờ chúng ta hãy chuyển sang

bàn cuối cùng,

tức là dữ liệu ngoại tuyến.

Điều này bao gồm các hoạt động

liên quan đến tiếp thị ngoại tuyến.

Chúng ta một lần nữa bắt đầu

với việc đọc dữ liệu,

và nhận được

các mô tả biến.

Chúng tôi quan sát những điều sau đây.

Dữ liệu ngoại tuyến

ở cấp độ thương hiệu,

chứ không phải ở cấp SKU_ID.

Bằng cách nhìn vào số ngày,

chúng ta có thể suy luận rằng

chỉ còn 38 tuần

đã có chiến dịch ngoại tuyến.

Có rất nhiều giá trị rỗng

các giá trị trong hình ảnh Nhấp chuột,

Hình ảnh chi phí, Số lần hiển thị

cột hình ảnh.

Những thứ này chỉ có mặt

trong 25 trên 38 ngày.

Biến quốc gia và thương hiệu

chỉ có một giá trị,

do đó chúng ta có thể loại bỏ chúng.

Cột, Số chiến dịch duy nhất

có cùng tên như trong

khung dữ liệu trực tuyến.

Chúng ta sẽ phải đổi tên

nó trước khi chúng ta hợp nhất chúng.

Hãy bắt đầu với việc thả

cột với

ít thông tin hơn.

Tiếp theo, hãy đổi tên Num

cột chiến dịch duy nhất để

phân biệt nó

từ cột với

cùng tên trong

khung dữ liệu kết hợp.

Trước khi tiếp tục, hãy nhanh chóng

kiểm tra lại nếu những thay đổi

đã được đưa vào.

Vâng, bây giờ chúng ta tiến hành

để kiểm tra ngày

tuần để hẹn hò.

Một lần nữa, dữ liệu

thuộc về thứ Bảy.

Bây giờ chúng tôi hợp nhất nó với

khung dữ liệu.

Lưu ý rằng, không giống như

những lần trước,

lần này chúng ta chỉ có thể hợp nhất

sử dụng cột ngày,

vì dữ liệu ngoại tuyến đang ở

cấp độ thương hiệu và không

ở cấp độ SKU_ID.

Hãy hợp nhất nó, và

kiểm tra hình dạng.

Chúng ta có cùng số

của các quan sát,

nhưng chúng tôi đã thêm

bốn cột nữa.

Với điều đó, chúng tôi

thực hiện với cái đầu tiên

nhiệm vụ cho bài học này.

Nhưng trước khi chúng ta nhảy

sang nhiệm vụ tiếp theo,

hãy thực hiện một số kiểm tra cuối cùng

trên dữ liệu kết hợp.

Những kiểm tra này sẽ đảm bảo rằng

tập dữ liệu kết hợp có

không có hồ sơ không liên quan.

Như chúng tôi đã nói trước đó, nếu

đầu vào của mô hình là rác rưởi,

đầu ra của mô hình

cũng sẽ là rác.

Hãy thực hiện những kiểm tra này

trong video sau.