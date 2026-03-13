# 04-giải quyết-vấn đề-sử dụng-k-nghĩa-phần 2

---

Hãy nhanh chóng chạy tất cả

mã ở trên cho đến thời điểm này.

Tiếp tục, hãy áp dụng

Thuật toán Kmeans

tập dữ liệu quy mô của chúng tôi.

Để làm như vậy, hãy đảm bảo bạn nhập

thư viện cần thiết,

đó là Kmean

thư viện từ sklearn.

Bây giờ hãy xem mã này.

Mã này thực hiện Kmeans

phân cụm trên data_scaled.

Lưu ý rằng chúng tôi đã chỉ định

trạng thái ngẫu nhiên là 42.

Gán trạng thái ngẫu nhiên

đảm bảo rằng chúng tôi nhận được

nhãn cụm giống nhau

khi chúng tôi chạy cái này

mã lại ngơ ngác nữa.

Như bạn đã biết ở Kmeans,

tập trung tâm đầu tiên

được chọn ngẫu nhiên.

Trạng thái ngẫu nhiên này giúp

kiểm soát tính ngẫu nhiên.

Sau đó chúng ta tiến hành sử dụng

chức năng phù hợp để áp dụng

thuật toán Kmeans

trên quy mô dữ liệu,

sau đó chúng tôi sử dụng the.predict

chức năng phân công từng

điểm dữ liệu đến các cụm của chúng tôi.

Khi chúng tôi nhận được nhãn cụm,

chúng tôi đang tạo một bản sao của

data_scaled và gọi nó

data_visual tới cái nào

một cụm cột mới

nhãn được thêm vào.

Lưu ý rằng chúng tôi sẽ

sử dụng dữ liệu trực quan để vẽ đồ thị

đặc điểm chống lại nhau

trong các video sắp tới.

Từ kết quả,

rõ ràng là

Thuật toán Kmeans đã phân cụm

dữ liệu của chúng tôi thành tám cụm.

Cụm 0, cụm 1,

2, lên đến 7.

Đó là bởi vì nếu chúng ta làm

không chỉ định

số cụm,

thì theo mặc định Kmeans

phân cụm dữ liệu với K=8.

Chúng tôi đã phân cụm thành công

dữ liệu của chúng tôi thành tám cụm.

Hãy nhanh chóng thực hiện một sự phân tán

đồ thị giữa đơn giá và

doanh thu và tìm kiếm

bất kỳ thông tin chi tiết thú vị nào mà chúng tôi

có thể tập hợp từ các cụm này.

Chúng tôi đang chọn những tính năng này

như họ có vẻ như vậy

các tính năng quan trọng.

Sau này chúng ta sẽ thử cách khác

sự kết hợp là tốt.

Hãy tiếp tục và nhập khẩu

các thư viện cần thiết,

và sau đó chạy mã bên dưới

để vẽ các đặc điểm

trên một biểu đồ phân tán.

Từ kết quả đồ thị,

không có nhiều điều hiển nhiên.

Chúng tôi thực sự không thể có được

tìm kiếm cụm xác định

từ hình ảnh trên.

Hãy cố gắng giảm

số lượng cụm

và chạy lại mã và xem

nếu chúng ta có được kết quả tốt hơn.

Chúng tôi vẫn không thể

nói rõ cái nào

cốt truyện thì tốt hơn

sự biểu diễn của các cụm.

Có lẽ, hình dung

các cụm dựa trên

chỉ có hai tính năng là không

cách tiếp cận tốt nhất để

đánh giá các cụm.

Hơn nữa, số

của các cụm chúng tôi đã sử dụng,

đó là năm, là

được chọn ngẫu nhiên.

Nhưng việc lựa chọn

số lượng cụm

cho một tập dữ liệu nhất định

không thể ngẫu nhiên được.

Hãy cùng tìm hiểu về một số

các phương pháp tìm tối ưu

số cụm,

không dựa vào

trên các ô phân tán.