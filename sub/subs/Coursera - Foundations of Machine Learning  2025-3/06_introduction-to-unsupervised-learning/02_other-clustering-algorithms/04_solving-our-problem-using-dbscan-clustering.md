# 04 giải quyết vấn đề của chúng tôi bằng cách sử dụng dbscan-phân cụm

---

Giải pháp Synergix có

nhận thấy rằng hoạt động tiếp thị của nó

chiến lược dựa trên các chiến lược hiện có

phân đoạn không hiệu quả lắm.

Họ muốn dùng thử gói thời đại mới

chiến lược tiếp thị trực tuyến sẽ

yêu cầu họ nhóm các sản phẩm tương tự

với nhau không phân biệt phân khúc.

>> Giống như chúng tôi đã làm cho

các thuật toán trước đó.

Cho đến quá trình mở rộng quy mô,

quy trình giống nhau, đó là tải

tập dữ liệu, chọn các tính năng và

xử lý trước dữ liệu thông qua việc chia tỷ lệ.

Vì vậy hãy thực hiện điều đầu tiên

nhanh ba bước.

Bây giờ chúng ta đã thành công

hoàn tất quá trình tiền xử lý dữ liệu,

chúng ta hãy chuyển sang bước tiếp theo,

đó là việc chọn các giá trị cho

tham số, mẫu tối thiểu và giá trị EPS.

Một giải pháp khả thi cho

tìm các mẫu tối thiểu tối ưu và

Giá trị EPS sẽ là thử các giá trị khác nhau

sự kết hợp của các tham số này và

kiểm tra điểm hình bóng cho

tất cả sự kết hợp.

Tuy nhiên, cách tiếp cận này có thể

tính toán rất tốn kém cho

các tập dữ liệu lớn.

Có những quy ước nhất định có thể

giúp chúng ta tìm được giá trị tối ưu.

Hãy cùng chúng tôi tìm hiểu về họ.

Tốt nhất, chúng ta nên chọn min

mẫu đầu tiên và sau đó là giá trị EPS.

Có một số quy ước phổ biến

để chọn các giá trị mẫu tối thiểu.

Điều đầu tiên cần ghi nhớ

là tập dữ liệu càng lớn,

giá trị của PTS tối thiểu càng lớn.

Một quy ước là tối thiểu

mẫu phải lớn hơn hoặc

bằng số lượng

các đặc tính trong tập dữ liệu.

Một quy ước khác là

để chọn giá trị cho

mẫu tối thiểu bằng

gấp đôi số lượng tính năng.

Lưu ý rằng ngay cả những giá trị lớn cũng có thể

cần thiết cho tập dữ liệu cực lớn.

Trong trường hợp của chúng tôi,

hãy chọn gấp đôi số lượng tính năng

như các quy ước của các mẫu tối thiểu.

Vì chúng ta có 13 tính năng,

hãy chọn 26 làm mẫu tối thiểu của chúng tôi.

Giá trị được chọn này cũng sẽ giúp chúng tôi

trong việc xác định giá trị EPS tối ưu.

Quy ước để tìm

giá trị EPS tối ưu tương tự

để tìm số K có nghĩa là

cụm sử dụng biểu đồ khuỷu tay.

Chúng tôi tìm thấy khoảng cách trung bình của mỗi

điểm có số mẫu tối thiểu

của hàng xóm.

Trong trường hợp của chúng tôi,

điều đó có nghĩa là chúng ta sẽ tìm giá trị trung bình

khoảng cách của mỗi mẫu với 26 hàng xóm.

Sau đó, chúng ta chỉ cần vẽ biểu đồ trung bình

khoảng cách theo thứ tự khác nhau và

tìm khoảng cách EPS tại điểm uốn hoặc

điểm khuỷu của đồ thị.

Đồ thị này được gọi là đồ thị khoảng cách K.

Vì vậy trước tiên hãy tính khoảng cách của K

mỗi mẫu có 26 số hàng xóm.

Với khoảng cách được tính toán, hãy

sắp xếp khoảng cách theo thứ tự tăng dần.

Đây là khoảng cách trung bình của mỗi

trong số các mẫu có 26 mẫu gần nhất

hàng xóm theo thứ tự tăng dần.

Bây giờ chúng ta chỉ cần vẽ đồ thị những khoảng cách này và

tìm điểm uốn hoặc khuỷu tay.

Từ biểu đồ trên, có vẻ như

điểm khuỷu tay ở đâu đó khoảng 2,3.

Vì vậy bây giờ hãy sử dụng EPS là 2,3 và

mẫu tối thiểu là 26 để xây dựng

mô hình phân cụm quét DB của chúng tôi.

Sau khi mô hình được xây dựng, chúng ta sẽ thêm

cụm nhãn vào khung dữ liệu tỷ lệ.

Có vẻ như chúng ta có hai cụm,

không và trừ một.

Hãy xác minh điều này.

Dựa trên đầu ra,

chúng ta có thể thấy rằng chỉ có một

cụm trong tập dữ liệu theo DBSCAN.

Các điểm dữ liệu được đánh dấu là trừ một

ở đây được xác định là ngoại lệ và

không thực sự là một phần của các cụm.

Có vẻ như thuật toán DBSCAN không phải

thuật toán thích hợp nhất cho

Tập dữ liệu Synergix.

Điều này chủ yếu là do

không có cụm nào cho

đội ngũ tiếp thị để làm việc cùng.

Do đó, chúng ta cũng cần

có khả năng phân tích và

giải thích các cụm dựa trên

về các tính năng khác nhau.

Hiệu suất của DBSCAN có xu hướng

xuống cấp trong những tình huống có

có nhiều tính năng và

vài hàng như trong tập dữ liệu Synergix.

DBSCAN cũng gặp khó khăn với bộ dữ liệu

có mật độ cụm khác nhau.

Nói chung có một số kỹ thuật

có thể được sử dụng để giảm số lượng

tính năng trước khi áp dụng

các thuật toán phân cụm.

Tuy nhiên, những kỹ thuật đó vượt xa

phạm vi của khóa học này.

Trong học máy không giám sát cũng vậy,

không có một kích cỡ nào phù hợp cho tất cả,

vì vậy tốt hơn nên thử nhiều

thuật toán trước khi quyết định

tiếp tục với bất kỳ một thuật toán nào.

Trong trường hợp Synergix này, K có nghĩa là

một sự phân nhóm theo cấp bậc đã mang lại cho chúng tôi điều tốt

kết quả, và một trong những thuật toán này

có thể được lựa chọn bởi đội ngũ tiếp thị

ai có sản phẩm chi tiết

thông tin được ánh xạ tới từng skyd.

Khi chúng ta kết thúc khóa học này,

Tôi chắc chắn rằng mỗi người trong số các bạn sẽ

có thể thực hiện không giám sát cũng như

thuật toán học máy có giám sát

đưa ra bất kỳ kịch bản thực tế nào trong tương lai.

Trước khi bạn đi qua

video tóm tắt khóa học,

đảm bảo bạn xem qua tài liệu đọc

với tất cả những điều thú vị khác nhau

ứng dụng kinh doanh của

phân cụm trong thế giới thực.