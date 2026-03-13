# 06 người học

---

Chúng ta có thể đối chiếu

người học T với

một phương pháp khác cho

thực hiện ước tính này,

và đó là sử dụng một

mũ mu mẫu đơn

để ước tính cả hai

những kỳ vọng này.

Trong mô hình đơn,

việc điều trị là một chỉ số

có thể nhận không và một,

được sử dụng như một tính năng

trong mô hình tương tự như

tất cả các tính năng khác

như tuổi tác hoặc huyết áp.

Để có được sự mong đợi của

kết quả được điều trị,

chúng tôi ước tính mu

thiết lập w bằng một.

Tương tự, để có được kỳ vọng

về kết quả được kiểm soát,

chúng tôi ước tính cài đặt mu

điều trị hoặc w bằng 0.

Sau đó chúng ta có thể lấy sự khác biệt

trong hai ước tính này.

Phương pháp này được gọi là

cây đơn

phương pháp S-learner.

Chúng ta tìm hiểu mô hình sử dụng mu

dữ liệu thử nghiệm đối chứng ngẫu nhiên của

cả hai bệnh nhân đều được đưa vào

việc điều trị và

trong cánh tay điều khiển.

Một lần nữa, chúng ta có thể chia

dữ liệu vào tập huấn luyện và

một bộ xác nhận để tìm hiểu

một mô hình có tính khái quát.

Mô hình học tập bây giờ là

thay vào đó là một cây quyết định duy nhất

của hai cây quyết định.

Lưu ý rằng cây quyết định này

chứa các nhánh chứa

cả đặc điểm của bệnh nhân và

có phải là bệnh nhân hay không

đã được điều trị.

Sử dụng mô hình này, bây giờ chúng ta có thể

ước tính điều trị

hiệu quả đối với bệnh nhân mới.

Đối với bệnh nhân này ở độ tuổi

56 và huyết áp 130,

đầu tiên chúng ta có thể tìm thấy

kết quả mong đợi của họ

với việc điều trị để có được

mu mũ x dấu phẩy một.

Vì vậy trước tiên chúng ta đi xuống

nhánh huyết áp,

chúng ta thấy rằng máu của họ

áp suất nhỏ hơn

140 và tuổi của họ

nhỏ hơn 60.

Bây giờ chúng tôi đang xem xét

cánh tay điều trị,

vì vậy việc điều trị của chúng tôi được đặt thành

một và ước tính của chúng tôi là 0,4.

Sau đó chúng ta có thể tìm thấy chúng

kết quả mong đợi

không cần điều trị.

Đầu tiên chúng ta đi xuống giống nhau

nhánh huyết áp,

chúng tôi cũng đi xuống

nhánh cùng tuổi,

nhưng bây giờ việc điều trị của chúng tôi là con số không.

Vì vậy chúng ta tới đây và tìm

rủi ro dự kiến là 0,5.

Bây giờ chúng ta có thể nhận ra sự khác biệt trong

hai người này mong đợi

kết quả để có được

tác dụng điều trị

ước tính 0,4 trừ 0,5,

đó là âm 0,1.

Điểm bất lợi với

người học S là

mà chúng ta có thể học

một cái cây có thể quyết định

không sử dụng phương pháp điều trị

tính năng nào cả.

Nếu chúng ta không có

khả năng ép buộc

cây quyết định sử dụng

các tính năng điều trị,

chúng ta vẫn có thể có được một cái cây

điều đó làm cho rất

ước tính tốt về

kết quả mong đợi cho

một bệnh nhân thuộc cả hai

điều trị và kiểm soát.

Tuy nhiên, vấn đề là

rằng một mô hình như vậy sẽ

tạo ra tác dụng điều trị

ước tính con số 0 cho tất cả mọi người.

Ví dụ, với

cùng một bệnh nhân như lúc trước,

chúng tôi sẽ làm một

ước tính 0,45 dưới

điều trị và kiểm soát

để có được ước tính bằng không.

Điều này sẽ đúng

cho tất cả bệnh nhân,

do đó làm cho cây này không phải là một

tác dụng chữa bệnh rất tốt

công cụ ước tính nếu có

tồn tại tác dụng lên

từng bệnh nhân.

Người học T trên

mặt khác sử dụng

hai mô hình khác nhau và

ít có khả năng xảy ra

có vấn đề này

Tuy nhiên, lưu ý rằng

bởi vì mỗi mô hình trong

người học T là

sử dụng một nửa dữ liệu,

có ít dữ liệu hơn để

tìm hiểu các mối quan hệ

giữa các tính năng.

Người học chữ T hoặc S

phương pháp là một số

đơn giản nhất trong số nhiều

những phương pháp khả thi mà chúng tôi

có thể sử dụng để ước tính

tác dụng điều trị riêng lẻ

sử dụng đồng biến của bệnh nhân.

Những cá nhân hóa này

ước tính hiệu quả điều trị

có thể hữu ích hơn

để làm cá nhân

quyết định điều trị hơn

điều trị trung bình

tác dụng điều trị