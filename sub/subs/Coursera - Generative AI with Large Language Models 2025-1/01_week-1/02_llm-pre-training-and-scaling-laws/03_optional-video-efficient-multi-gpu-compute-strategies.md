# 03 chiến lược điện toán-đa-gpu-tùy chọn-video-hiệu quả

---

Rất có thể là tại

một lúc nào đó bạn sẽ cần phải

mở rộng quy mô đào tạo mô hình của bạn

những nỗ lực vượt xa một GPU duy nhất.

Mình đã nhấn mạnh ở video trước

mà bạn sẽ cần

sử dụng nhiều GPU

chiến lược tính toán

khi mô hình của bạn

trở nên quá lớn để

phù hợp với một GPU duy nhất.

Nhưng ngay cả khi mô hình của bạn làm được

phù hợp với một GPU duy nhất,

có những lợi ích khi sử dụng

nhiều GPU để tăng tốc

tăng cường đào tạo của bạn.

Sẽ rất hữu ích nếu biết

cách phân phối máy tính

trên các GPU ngay cả khi bạn

làm việc với một mô hình nhỏ

Hãy thảo luận về cách bạn có thể

thực hiện việc chia tỷ lệ này

trên nhiều GPU

một cách hiệu quả.

Bạn sẽ bắt đầu bằng

xem xét vụ việc

mô hình của bạn vẫn ở đâu

phù hợp trên một GPU duy nhất.

Bước đầu tiên trong việc mở rộng quy mô

đào tạo mô hình là để

phân phối các tập dữ liệu lớn

trên nhiều GPU và

xử lý các lô này

của dữ liệu song song.

Một cách triển khai phổ biến của

nhân rộng mô hình này

kỹ thuật là

Ngọn đuốc Pi được phân phát

dữ liệu song song,

hoặc viết tắt là DDP.

DDP sao chép của bạn

mô hình trên mỗi GPU

và gửi các lô dữ liệu tới

từng GPU song song.

Mỗi tập dữ liệu được xử lý

song song và sau đó

một bước đồng bộ hóa kết hợp

kết quả của từng GPU,

từ đó cập nhật

mô hình trên mỗi GPU,

luôn luôn như vậy

giống hệt nhau trên các chip.

Việc triển khai này cho phép

tính toán song song

trên tất cả các GPU

mang lại kết quả đào tạo nhanh hơn.

Lưu ý rằng DDP yêu cầu điều đó

trọng lượng mô hình của bạn và tất cả

các tham số bổ sung,

độ dốc và trạng thái tối ưu hóa

cần thiết cho việc đào tạo,

phù hợp với một GPU duy nhất.

Nếu mô hình của bạn là

quá lớn cho việc này,

bạn nên nhìn vào

kỹ thuật khác

được gọi là sharding phương thức.

Một cách triển khai phổ biến của

phương thức sharding là Pi Torch

được phân chia hoàn toàn dữ liệu song song,

hoặc viết tắt là FSDP.

FSDP được thúc đẩy bởi một bài báo

được công bố bởi các nhà nghiên cứu tại

Microsoft năm 2019 đã đề xuất

một kỹ thuật gọi là ZeRO.

Zero là viết tắt của số không

trình tối ưu hóa dự phòng

và mục tiêu của

Zero là để tối ưu hóa

bộ nhớ bằng cách phân phối

hoặc phân mảnh

trạng thái mô hình trên các GPU

với sự chồng chéo dữ liệu ZeRO.

Điều này cho phép bạn mở rộng quy mô

đào tạo mô hình xuyên suốt

GPU khi mô hình của bạn

không phù hợp với

bộ nhớ của một chip đơn.

Hãy nhanh chóng

hãy nhìn xem ZeRO thế nào

hoạt động trước khi đến

Trở lại FSDP.

Đầu tuần này,

bạn đã xem tất cả

thành phần bộ nhớ

cần thiết để đào tạo LLM,

yêu cầu bộ nhớ lớn nhất

dành cho các trạng thái tối ưu hóa,

chiếm gấp đôi

nhiều không gian như trọng lượng,

theo sau là trọng lượng

bản thân chúng và các gradient.

Hãy đại diện cho

thông số như ô màu xanh này

độ dốc và màu vàng

và trình tối ưu hóa

các tiểu bang có màu xanh lá cây.

Tắt một giới hạn

sự sao chép mô hình

chiến lược mà tôi đã chỉ ra

trước đó là bạn cần giữ

một bản sao mô hình đầy đủ trên mỗi GPU,

dẫn đến dư thừa

tiêu thụ bộ nhớ.

Bạn đang lưu trữ tương tự

số trên mỗi GPU.

Mặt khác, Zero,

loại bỏ sự dư thừa này bằng cách

phân phối còn được gọi là

phân chia các tham số mô hình,

độ dốc và trạng thái tối ưu hóa

thay vào đó trên các GPU

về việc sao chép chúng.

Đồng thời,

chi phí liên lạc

đối với trạng thái mô hình chìm

ở gần với cái đó

ADP đã được thảo luận trước đó.

ZeRO cung cấp ba

các giai đoạn tối ưu hóa

Zero Giai đoạn 1,

trình tối ưu hóa chỉ ảnh

trạng thái trên GPU,

điều này có thể làm giảm

dấu chân bộ nhớ

lên tới hệ số bốn.

ZeRO Giai đoạn 2 cũng bắn

độ dốc trên các chip.

Khi áp dụng cùng nhau

với Giai đoạn 1,

điều này có thể làm giảm

dấu chân bộ nhớ

tới tám lần.

Cuối cùng là ảnh chụp ZeRO Giai đoạn 3

tất cả các thành phần bao gồm

các thông số mô hình

trên các GPU.

Khi áp dụng cùng nhau

với Giai đoạn 1 và 2,

giảm bộ nhớ là tuyến tính

với một số GPU.

Ví dụ: phân chia trên

64 GPU có thể làm giảm

bộ nhớ theo hệ số 64.

Hãy áp dụng khái niệm này vào

trực quan hóa GDP và

thay thế LLM bằng

biểu diễn bộ nhớ

của các tham số mô hình,

độ dốc và trạng thái tối ưu hóa.

Khi bạn sử dụng FSDP,

bạn phân phối dữ liệu trên

nhiều GPU như bạn

đã thấy xảy ra trong GDP.

Nhưng với FSDP,

bạn cũng đã phân phối hoặc

chia nhỏ mô hình

các thông số, độ dốc,

và tối ưu hóa các trạng thái

trên các nút GPU

sử dụng một trong những chiến lược

được chỉ định trong bài báo ZeRO.

Với chiến lược này,

bây giờ bạn có thể làm việc với

những mô hình quá lớn

để phù hợp trên một con chip duy nhất.

Ngược lại với GDP,

nơi mỗi GPU có tất cả

của các trạng thái mô hình

cần thiết cho

xử lý từng đợt

dữ liệu có sẵn tại địa phương,

FSDP yêu cầu bạn thu thập

dữ liệu này từ tất cả

GPU trước

chuyền tiến và lùi.

Mỗi CPU yêu cầu dữ liệu từ

các GPU khác theo yêu cầu

hiện thực hóa

dữ liệu được phân chia thành

dữ liệu chưa được khám phá cho

thời gian của hoạt động.

Sau khi thao tác, bạn thả ra

dữ liệu phi địa phương chưa được khám phá

quay lại các GPU khác như

dữ liệu được phân chia gốc

Bạn cũng có thể chọn

giữ nó cho các hoạt động trong tương lai

trong quá trình lùi lại

vượt qua chẳng hạn.

Lưu ý, điều này đòi hỏi

lại có thêm RAM GPU,

đây là một màn trình diễn điển hình

so với trí nhớ

quyết định đánh đổi.

Ở bước cuối cùng sau

đường chuyền ngược,

FSDP được đồng bộ hóa

độ dốc trên

các GPU giống nhau

cách họ đã làm cho DDP.

Phân mảnh mô hình S

được mô tả bằng FSDP

cho phép bạn giảm bớt

sử dụng bộ nhớ GPU tổng thể.

Tùy chọn, bạn có thể chỉ định

FSDP giảm tải một phần

việc đào tạo

tính toán cho GPU để

giảm thêm GPU của bạn

việc sử dụng bộ nhớ.

Để quản lý sự đánh đổi giữa

hiệu suất và

sử dụng bộ nhớ,

bạn có thể cấu hình

mức độ phân mảnh

sử dụng FSDP là yếu tố biểu đồ.

Một yếu tố sharding của

về cơ bản là loại bỏ

sharding và nhân rộng

mô hình đầy đủ tương tự như DDP.

Nếu bạn đặt

yếu tố sharding để

số lượng tối đa

số GPU có sẵn,

bạn bật sharding đầy đủ.

Cái này có nhiều nhất

tiết kiệm bộ nhớ,

nhưng tăng cường giao tiếp

âm lượng giữa các GPU.

Bất kỳ yếu tố sharding nào ở giữa

cho phép siêu phân mảnh.

Chúng ta hãy xem làm thế nào

FSDP thực hiện so sánh

đến DDP được đo bằng

teraflop trên mỗi GPU.

Những thử nghiệm này đã được thực hiện

sử dụng tối đa

512 GPU NVIDIA V100,

mỗi cái có 80

gigabyte bộ nhớ.

Lưu ý, một teraflop

tương ứng với

một nghìn tỷ dấu phẩy động

hoạt động mỗi giây.

Hình đầu tiên cho thấy

Hiệu suất FSDP cho

mô hình T5 kích thước khác nhau.

Bạn có thể thấy sự khác biệt

số hiệu suất cho FSDP,

toàn bộ mảnh màu xanh lam,

siêu mảnh màu cam và

bản sao đầy đủ màu xanh lá cây.

Để tham khảo, DDP

hiệu suất được hiển thị bằng màu đỏ.

Đối với 25 mẫu đầu tiên có

611 triệu thông số và

2,28 tỷ thông số,

hiệu suất của FSDP

và DDP là tương tự.

Bây giờ, nếu bạn chọn một mô hình

quy mô vượt quá 2,28 tỷ,

chẳng hạn như 25 với 11,3

tỷ thông số,

DDP chạy vào

lỗi hết bộ nhớ.

Mặt khác, FSDP có thể

dễ dàng xử lý các mô hình

kích thước này và

đạt được cao hơn nhiều

teraflop khi

hạ thấp mô hình

độ chính xác đến 16-bit.

Hình thứ hai cho thấy

giảm 7% trên mỗi

GPU teraflop khi

tăng

số lượng GPU từ

8-512 cho ngày 11

mô hình tỷ T5,

vẽ ở đây bằng cách sử dụng một

cỡ lô 16 và

cam và một lô

kích thước tám màu xanh lam.

Khi mô hình phát triển

về kích thước và là

phân phối trên

ngày càng có nhiều GPU,

sự gia tăng trong

khối lượng liên lạc giữa

chip bắt đầu tác động

hiệu suất,

làm chậm quá trình tính toán.

Tóm lại, điều này cho thấy

mà bạn có thể sử dụng FSDP cho

cả mô hình nhỏ và lớn và

quy mô liền mạch

đào tạo người mẫu của bạn

trên nhiều GPU.

Tôi biết cuộc thảo luận này có

có tính kỹ thuật cao và tôi

muốn nhấn mạnh rằng bạn không

cần phải nhớ tất cả

của các chi tiết ở đây.

Điều quan trọng nhất

là có ý thức

về cách các tham số mô hình dữ liệu

và đào tạo

tính toán được chia sẻ

xuyên suốt các quy trình

khi đào tạo LLM.

Với chi phí và

độ phức tạp kỹ thuật của

mô hình đào tạo trên GPU,

một số nhà nghiên cứu có

đang khám phá những cách để

đạt được hiệu suất tốt hơn

với các mô hình nhỏ hơn.

Trong video tiếp theo,

bạn sẽ tìm hiểu thêm về

nghiên cứu này vào

tính toán mô hình tối ưu.

Chúng ta hãy tiếp tục và xem xét.