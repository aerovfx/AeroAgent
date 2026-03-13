# 03 sự kết hợp-tầm quan trọng

---

Hãy tưởng tượng bộ tính năng đang được

hình thành một tính năng tại một thời điểm.

Đầu tiên, bộ tính năng của chúng tôi trống.

Sau đó, nó có một tính năng,

hãy nói rằng đó là tuổi.

Sau đó, nó có một tính năng khác, đó là dBP.

Và cuối cùng, nó nhận được sBP.

Bây giờ chúng ta có thể tìm ra sự đóng góp

của sBP khi nó tham gia vào bộ tính năng

bằng cách tính toán dự đoán của mô hình

với ba tính năng trừ đi dự đoán

của một người chỉ có tuổi và dBP, mà

xuất hiện trước sBP trong bộ tính năng.

Một cách khác có thể

các tính năng có thể được hình thành

đó là tuổi tác đến trước

tiếp theo là sBP và tiếp theo là dBP.

Ở đây chúng ta có thể tìm thấy sự đóng góp của sBP

khi nó tham gia vào tính năng được thiết lập bởi máy tính

sự khác biệt của một mô hình sử dụng độ tuổi và

sBP trừ đi một chỉ sử dụng tuổi, đó là

tính năng đã đến

trước sBP để có 0,53.

Chúng ta có thể tưởng tượng tất cả các cách có thể

bộ tính năng có thể được hình thành.

Vì có ba đặc điểm

có ba giai thừa hoặc

sáu cách có thể hình thành bộ tính năng này.

Đối với mỗi điều này, chúng ta có thể

tính toán tầm quan trọng của sBP

chống lại các tính năng

xuất hiện trước nó.

Ví dụ ở hàng thứ ba

cột thứ hai ở đây,

sBP xuất hiện trước cả tuổi và dBP.

Vì vậy chúng tôi tính toán đầu ra

của mô hình chỉ có sBP

trừ mô hình với phần trống

thiết lập và lấy sự khác biệt.

Cuối cùng, chúng tôi tính trung bình tất cả

những tính năng quan trọng này

như một số trong sáu số này

chia cho 6 để có được giá trị trung bình

điều này cho chúng ta thấy tầm quan trọng của sBP đối với

Bệnh nhân A xuất hiện khoảng 0,38.

Chúng tôi gọi tầm quan trọng này là

Giá trị Shapley được biểu diễn

bằng chữ I viết hoa cho

sBP cho bệnh nhân A.

Chúng ta có thể tính toán tương tự Shapley

giá trị cho tuổi và cho dBP.

Lưu ý rằng sự đóng góp của sBP và

dBP có vẻ cao hơn nhiều so với tuổi và

trước đây và điều này đang thu hút

rằng hai giá trị cao này đang thúc đẩy

nguy cơ cho bệnh nhân này.

Một tính chất thú vị khác của giá trị Shapley

đó là các giá trị Shapley tổng hợp

dự đoán rủi ro với mô hình đầy đủ

trừ đi rủi ro cơ bản trong dân số.

Nói cách khác, giá trị Shapley

đang cho chúng ta biết mỗi tính năng có bao nhiêu

góp phần làm tăng thêm rủi ro

rủi ro cơ bản của dân số.

Vậy đây là một bệnh nhân khác

trong một tập dữ liệu mới và

sự phổ biến ở đây

tập dữ liệu mới là 0,001.

Chúng ta có ba giá trị Shapley cho

ba đặc điểm của bệnh nhân này,

tất cả cộng lại để tạo thành đầu ra

với tất cả các tính năng,

bằng 0,26 trừ đầu ra

không có tính năng,

điều đó sẽ trở nên phổ biến,

nhận được đầu ra là 0,26.

Vì vậy chúng ta có thể hình dung các giá trị Shapley và

tổng số của họ bằng cách sử dụng một âm mưu lực lượng.

Trên biểu đồ lực, chúng ta có

giá trị đầu ra là 0,26 và

giá trị cơ bản là 0,00.

Và khoảng cách này sẽ được bao phủ

bằng tổng của ba giá trị Shapley này.

Vì vậy chúng ta có thể thấy điều đó

sự đóng góp của dBP là 0,01,

được biểu thị bằng độ dài

của phân đoạn này ở đây.

Đóng góp lớn nhất,

tất nhiên là bởi sBP

đó là sự đóng góp

0,3 theo chiều dương,

và sự đóng góp của tuổi tác là -0,05.

Bây giờ tuổi tác đang buộc sản lượng phải

hướng thấp hơn nên nó có màu xanh lam.

Trong khi sBP và dBP đang buộc nó vào

chiều dương nên chúng có màu đỏ.