# 02 thử thách tính toán của đào tạo

---

Một trong những điều nhất

những vấn đề thường gặp bạn

vẫn phản đối khi bạn cố gắng

để đào tạo các mô hình ngôn ngữ lớn

sắp hết bộ nhớ.

Nếu bạn đã từng thử

đào tạo hoặc thậm chí

chỉ cần tải của bạn

mô hình trên GPU Nvidia,

thông báo lỗi này

có thể trông quen thuộc.

CUDA, viết tắt của Điện toán

Kiến trúc thiết bị hợp nhất,

là một tập hợp các thư viện và

công cụ được phát triển cho GPU Nvidia.

Các thư viện như PyTorch và

TensorFlow sử dụng CUDA để tăng tốc

hiệu suất về số liệu

phép nhân

và các hoạt động khác

chung cho học sâu.

Bạn sẽ gặp phải những điều này

vấn đề hết bộ nhớ

bởi vì hầu hết LLM đều rất lớn,

và cần rất nhiều bộ nhớ để

lưu trữ và đào tạo tất cả

các thông số của chúng.

Hãy làm nhanh một chút

toán học phát triển

trực giác về

quy mô của vấn đề.

Một tham số duy nhất thường

được biểu thị bằng float 32 bit,

đó là cách máy tính

biểu diễn số thực.

Bạn sẽ thấy nhiều hơn

chi tiết về cách

số được lưu trữ trong

định dạng này trong thời gian ngắn.

Một float 32-bit chiếm

bốn byte bộ nhớ.

Vì vậy để lưu trữ một tỷ

thông số bạn sẽ cần

bốn byte nhân một

tỷ thông số,

hoặc bốn gigabyte RAM GPU

ở độ chính xác đầy đủ 32-bit.

Đây là rất nhiều

trí nhớ và ghi chú,

nếu chỉ tính đến

bộ nhớ để lưu trữ

trọng lượng mô hình cho đến nay.

Nếu bạn muốn đào tạo mô hình,

bạn sẽ phải lập kế hoạch cho

các thành phần bổ sung sử dụng

Bộ nhớ GPU trong quá trình đào tạo.

Chúng bao gồm hai Adam

trạng thái tối ưu hóa,

độ dốc, kích hoạt,

và các biến tạm thời

cần thiết cho chức năng của bạn.

Điều này có thể dễ dàng dẫn đến

Thêm 20 byte bộ nhớ

mỗi tham số mô hình.

Trên thực tế, để giải thích

tất cả những chi phí này

trong quá trình đào tạo,

bạn thực sự sẽ yêu cầu

khoảng 6 lần số tiền

RAM GPU mà mô hình

trọng lượng một mình chiếm.

Để đào tạo một tỷ

mô hình tham số

ở độ chính xác đầy đủ 32-bit,

bạn sẽ cần khoảng

RAM GPU 24 gigabyte.

Cái này chắc chắn là quá lớn

cho phần cứng tiêu dùng,

và thậm chí là thách thức đối với

phần cứng được sử dụng trong trung tâm dữ liệu,

nếu bạn muốn đào tạo

với một bộ xử lý duy nhất.

Bạn có những lựa chọn nào

giảm trí nhớ

cần thiết cho việc đào tạo?

Một kỹ thuật mà

bạn có thể sử dụng để

giảm bộ nhớ là

gọi là lượng tử hóa.

Ý tưởng chính ở đây là bạn

giảm bộ nhớ cần thiết

để lưu trữ trọng lượng

mô hình của bạn bằng cách giảm

độ chính xác của họ từ

Số dấu phẩy động 32 bit

đến 16-bit nổi

số điểm,

hoặc số nguyên 8 bit.

Các kiểu dữ liệu tương ứng

được sử dụng trong học sâu

khuôn khổ và

thư viện là FP32 cho

Vị trí đầy đủ 32-bit,

FP16 hoặc Bfloat16 cho

Độ chính xác một nửa 16 bit,

và số nguyên tám bit int8.

Phạm vi số

bạn có thể đại diện

với FP32 đi từ

xấp xỉ

-3*10^38 đến 3*10^38.

Theo mặc định, mô hình

trọng lượng, kích hoạt,

và các thông số mô hình khác

được lưu trữ trong FP32.

Lượng tử hóa

dự án thống kê

32-bit gốc

số dấu phẩy động

vào một không gian có độ chính xác thấp hơn,

sử dụng các hệ số tỷ lệ

tính toán dựa trên

phạm vi của bản gốc

Số dấu phẩy động 32 bit.

Hãy xem một ví dụ.

Giả sử bạn muốn

để lưu trữ PI vào

sáu chữ số thập phân trong

các vị trí khác nhau.

Điểm nổi

số được lưu trữ dưới dạng

một loạt các bit số 0 và số một.

32 bit để lưu trữ số trong

độ chính xác đầy đủ với FP32 bao gồm

một bit cho

dấu hiệu nơi số 0

chỉ ra một số dương,

và một là số âm.

Sau đó tám bit cho

số mũ của số,

và 23 bit đại diện

phân số của số đó.

Phân số là

còn được gọi là

mantissa, hoặc đáng kể.

Nó thể hiện độ chính xác

bit tắt số.

Nếu bạn chuyển đổi 32-bit

giá trị dấu phẩy động

trở lại giá trị thập phân,

bạn nhận thấy sự nhẹ nhàng

mất đi độ chính xác.

Để tham khảo, đây là

giá trị thực của

Pi đến 19 chữ số thập phân.

Bây giờ chúng ta hãy xem những gì

xảy ra nếu bạn chiếu

đại diện FP32 này

của Pi vào FP16,

Không gian có độ chính xác thấp hơn 16 bit.

16 bit bao gồm

một chút cho dấu hiệu,

như bạn đã thấy ở FP32,

nhưng bây giờ chỉ có FP16

gán năm bit cho

biểu thị số mũ và

10 bit để biểu diễn

phân số.

Vì vậy, phạm vi

số bạn có thể

đại diện cho FP16 là rất nhiều

nhỏ hơn từ âm

65.504 đến dương 65.504.

Giá trị FP32 ban đầu

được chiếu tới

3.140625 trong không gian 16 bit.

Chú ý rằng bạn mất một số

độ chính xác với phép chiếu này.

Chỉ có sáu nơi

sau dấu thập phân bây giờ.

Bạn sẽ thấy rằng sự mất mát này trong

độ chính xác được chấp nhận trong

hầu hết các trường hợp vì bạn đang cố gắng

để tối ưu hóa cho

dấu chân bộ nhớ.

Lưu trữ một giá trị trong FP32

yêu cầu bốn byte bộ nhớ.

Ngược lại, việc lưu trữ một giá trị trên

FP16 chỉ yêu cầu

hai byte bộ nhớ,

vì vậy với lượng tử hóa bạn có

giảm trí nhớ

yêu cầu giảm đi một nửa.

Nghiên cứu AI

cộng đồng đã khám phá

cách tối ưu hóa 16-bit

lượng tử hóa.

Một kiểu dữ liệu trong

cụ thể là BFLOAT16,

gần đây đã trở thành một

thay thế phổ biến cho FP16.

BFLOAT16, viết tắt của Brain

Định dạng dấu phẩy động

được phát triển tại Google Brain

đã trở nên phổ biến

sự lựa chọn trong học sâu.

Nhiều LLM, bao gồm FLAN-T5,

đã được đào tạo trước

với BFLOAT16.

BFLOAT16 hoặc BF16 là giống lai

giữa một nửa độ chính xác FP16

và độ chính xác đầy đủ FP32.

BF16 giúp ích đáng kể

sự ổn định đào tạo

và được hỗ trợ

bởi GPU mới hơn như vậy

như A100 của NVIDIA.

BFLOAT16 thường được mô tả

như một float 32-bit bị cắt ngắn,

vì nó nắm bắt

toàn dải động

của phao 32 bit đầy đủ,

chỉ sử dụng 16 bit.

BFLOAT16 sử dụng

đầy đủ tám bit

để biểu diễn số mũ,

nhưng cắt bớt phần

chỉ còn bảy bit.

Điều này không chỉ tiết kiệm bộ nhớ,

nhưng cũng tăng

hiệu suất mô hình

bằng cách tăng tốc độ tính toán.

Nhược điểm là BF16

không phù hợp lắm cho

phép tính số nguyên,

nhưng đây là những điều tương đối

hiếm gặp trong học sâu.

Để hoàn thiện

chúng ta hãy nhìn vào

điều gì xảy ra nếu bạn lượng tử hóa

Pi từ 32-bit thành

độ chính xác thậm chí còn thấp hơn

không gian tám bit.

Nếu bạn sử dụng một bit cho dấu hiệu

Giá trị INT8 được biểu diễn

bằng bảy bit còn lại.

Điều này cung cấp cho bạn một phạm vi để

biểu diễn các số từ

âm 128 đến dương

127 và không ngạc nhiên khi Pi nhận được

dự kiến hai hoặc ba

ở mức 8 bit thấp hơn

không gian chính xác.

Điều này mang lại ký ức mới

yêu cầu giảm từ

ban đầu là bốn byte

thành chỉ một byte,

nhưng rõ ràng dẫn đến

khá kịch tính

mất độ chính xác.

Hãy tóm tắt những gì

bạn đã học ở đây và

nhấn mạnh những điểm chính bạn

nên lấy đi từ

cuộc thảo luận này.

Hãy nhớ rằng

mục tiêu lượng tử hóa

là để giảm

bộ nhớ cần thiết để

lưu trữ và huấn luyện các mô hình bằng cách

giảm độ chính xác

ra khỏi trọng lượng mô hình.

Lượng tử hóa

dự án thống kê

32-bit gốc

số dấu phẩy động vào

không gian có độ chính xác thấp hơn

sử dụng các hệ số tỷ lệ

được tính toán dựa trên phạm vi

của các float 32-bit ban đầu.

Học sâu hiện đại

khuôn khổ và

hỗ trợ thư viện

đào tạo nhận thức lượng tử hóa,

học lượng tử hóa

các yếu tố tỷ lệ trong quá trình

quá trình đào tạo.

Các chi tiết của quá trình này

nằm ngoài phạm vi

của khóa học này.

Nhưng bạn đã thấy

điểm mấu chốt ở đây,

mà bạn có thể sử dụng

lượng tử hóa để giảm

dấu chân bộ nhớ tắt

mô hình trong quá trình đào tạo.

BFLOAT16 đã trở thành

sự lựa chọn phổ biến của độ chính xác

trong học sâu như nó

duy trì sự năng động

phạm vi của FP32,

nhưng làm giảm bộ nhớ

dấu chân giảm một nửa.

Nhiều LLM, bao gồm FLAN-T5,

đã được đào tạo trước

với BFOLAT16.

Hãy chú ý đề cập đến

BFLOAT16 trong phòng thí nghiệm tuần tới.

Bây giờ chúng ta hãy quay trở lại

thách thức của việc lắp các mô hình vào

Bộ nhớ GPU và hãy xem

lúc va chạm

lượng tử hóa có thể có.

Bằng cách áp dụng

lượng tử hóa, bạn có thể

giảm trí nhớ của bạn

tiêu dùng cần thiết để

lưu trữ mô hình

thông số xuống

chỉ sử dụng hai gigabyte

Độ chính xác một nửa 16 bit của

Tiết kiệm 50% còn bạn

có thể giảm thêm

dấu chân bộ nhớ bởi

50% khác bằng cách đại diện

các thông số mô hình

dưới dạng số nguyên tám bit,

chỉ yêu cầu một

gigabyte RAM GPU.

Lưu ý rằng trong tất cả

những trường hợp này bạn vẫn

có một mô hình với một

tỷ thông số.

Như bạn có thể thấy, các vòng tròn

đại diện cho các mô hình

có cùng kích thước.

Lượng tử hóa sẽ cung cấp cho bạn

mức tiết kiệm như nhau

khi nói đến đào tạo.

Tuy nhiên hiện nay có nhiều mô hình

kích thước vượt quá

50 tỷ thậm chí 100

tỷ thông số.

Có nghĩa là bạn sẽ cần tới

Bộ nhớ tăng gấp 500 lần

khả năng đào tạo họ,

hàng chục ngàn gigabyte.

Những mô hình khổng lồ lùn

tham số một tỷ

mô hình chúng tôi đang xem xét,

hiển thị ở đây để chia tỷ lệ ở bên trái.

Là quy mô phương thức vượt ra ngoài một

vài tỷ thông số,

nó trở nên không thể

huấn luyện họ trên một GPU duy nhất.

Thay vào đó, bạn sẽ cần phải chuyển sang

tính toán phân tán

kỹ thuật trong khi bạn

đào tạo mô hình của bạn

trên nhiều GPU.

Điều này có thể yêu cầu quyền truy cập

tới hàng trăm GPU,

cái này rất đắt.

Một lý do khác tại sao

bạn sẽ không tập luyện trước

mô hình của riêng bạn từ

gãi hầu hết thời gian.

Tuy nhiên, một bổ sung

quá trình đào tạo

gọi là tinh chỉnh,

mà bạn sẽ học

khoảng tuần tới.

Cũng yêu cầu lưu trữ tất cả

thông số đào tạo trong

bộ nhớ và rất có thể

bạn sẽ muốn tinh chỉnh

một mô hình tại một thời điểm nào đó.

Để giúp bạn

hiểu thêm về

các khía cạnh kỹ thuật của

đào tạo trên GPU,

chúng tôi đã chuẩn bị một

video tùy chọn cho bạn.

Nó rất chi tiết, nhưng nó sẽ

giúp bạn hiểu một số

những lựa chọn đó

tồn tại cho các nhà phát triển

giống như bạn để đào tạo những mô hình lớn hơn.

Bạn nên cảm thấy tự do

để bỏ qua video này.

Nhưng nếu bạn quan tâm

trong việc học thêm,

Tôi hy vọng bạn sẽ kiểm tra nó.