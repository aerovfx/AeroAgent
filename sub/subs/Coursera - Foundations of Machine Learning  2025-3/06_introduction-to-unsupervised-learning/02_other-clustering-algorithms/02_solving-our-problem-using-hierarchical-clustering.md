# 02 giải quyết-vấn đề-của-chúng-ta-sử dụng-phân cấp-phân cụm

---

Giải pháp tổng hợp,

đã phát hiện ra rằng các chiến lược tiếp thị của mình,

dựa trên các phân khúc hiện có,

không hiệu quả lắm.

Họ muốn thử sức, thời đại mới, gói gọn

chiến lược tiếp thị trực tuyến, sẽ

yêu cầu họ nhóm các sản phẩm tương tự

cùng nhau, không phân biệt, của phân khúc.

>> Giống như chúng tôi đã làm trước đó.

Ở đây cũng vậy,

3 bước đầu tiên sẽ giống nhau.

Đầu tiên chúng ta sẽ tải tập dữ liệu và

sau đó chọn các tính năng có liên quan cho

xử lý.

Sau đó, chúng tôi sử dụng quy trình xử lý sơ bộ thích hợp

biện pháp phát biểu vấn đề.

Sau khi chúng tôi hoàn thành thành công

quá trình xử lý trước, tất cả những gì chúng ta phải làm,

là áp dụng HCA,

để tạo chương trình dendrogram, và

sau đó tiến hành chọn số

của các cụm sử dụng một ngưỡng.

Cuối cùng, chúng tôi đánh giá và

giải thích các cụm bằng cách vẽ đồ thị

các tính năng khác nhau với nhãn cụm.

Vì vậy, hãy tiếp tục và chạy các ô này.

Bây giờ chúng ta đã hoàn thành thành công

tiền xử lý và chia tỷ lệ tập dữ liệu,

bước tiếp theo là áp dụng

phân tích cụm phân cấp cho nó.

HCA hoạt động theo hai cách khác nhau.

Đầu tiên là cách tiếp cận từ trên xuống,

bắt đầu với tất cả các điểm dữ liệu chỉ trong

một cụm và sau đó dữ liệu được chia

vào cụm nhỏ hơn một mẫu tại một thời điểm.

Mặt khác, cách tiếp cận thứ hai,

đó là cách tiếp cận phổ biến,

là cách tiếp cận từ dưới lên.

Bắt đầu với tất cả dữ liệu

điểm dưới dạng các cụm riêng biệt và

sau đó các điểm dữ liệu được hợp nhất

mỗi lần một mẫu,

cho đến khi chỉ có một cụm chính với

tất cả các điểm dữ liệu được hình thành.

Cách tiếp cận thứ hai là những gì chúng tôi đã sử dụng trong

ví dụ về sách của chúng tôi trước đó trong video.

Đây cũng là cách tiếp cận mà

có sẵn ở hầu hết các thư viện.

Lý do là vì, cách tiếp cận này

về mặt tính toán ít tốn kém hơn và

ít khó khăn hơn để thực hiện.

Đối với thủ tục này, chúng ta sẽ có

để nhập thư viện có tên SciPy.

SciPy hoặc

Thư viện Python khoa học.

Được sử dụng ở đây là nguồn mở và miễn phí

Thư viện Python dành cho khoa học và

tính toán kỹ thuật.

Nó là một bộ sưu tập của

các thuật toán toán học và

chức năng tiện lợi được xây dựng

trên thư viện NumpY phổ biến.

Vậy chúng ta hãy tiếp tục và

nhập thư viện và

tiến hành áp dụng phân cụm theo cấp bậc

trên khung dữ liệu quy mô dữ liệu này.

Hàm liên kết lấy đầu vào,

áp dụng phân cụm từ dưới lên và

trả về thứ bậc

phân cụm được mã hóa dưới dạng ma trận.

Có nhiều cách tiếp cận khác nhau

để tìm các cụm,

ở gần nhau,

chẳng hạn như duy nhất, đầy đủ và như vậy.

Chúng tôi đã sử dụng một phương pháp phổ biến gọi là Ward,

trong trường hợp nghiên cứu của chúng tôi.

Hãy thoải mái xem qua các tài liệu

để hiểu các phương pháp khác nhau.

Như bạn có thể quan sát,

rất khó để giải thích ma trận.

Vì vậy, hãy sử dụng chương trình dendrogram

để trực quan hóa ma trận,

sử dụng thư viện SciPy và NumPy.

Chương trình dendro này khá hấp dẫn,

phải không?

Chúng tôi đã thành công

đã tạo dendrogram của chúng tôi cho

bộ dữ liệu Synergy trên

thang đo dữ liệu khung dữ liệu.

Lưu ý rằng ở đây, khoảng cách của

các đường thẳng đứng trong chương trình dendro,

khoảng cách giữa các cụm nhiều hơn.

Sau khi dendrogram được tạo, bước tiếp theo

bước là đặt khoảng cách ngưỡng,

và vẽ một đường ngang

lấy số cụm.

Một quy ước phổ biến để có được cụm là

vẽ một đường ngang ngang qua cao nhất

đường thẳng đứng, ở một khoảng cách cho phép

cho chúng tôi số lượng cụm mong muốn.

Ngoài ra, hãy đảm bảo rằng số lượng

của các cụm được chọn,

nên có một lượng đáng kể

số lượng quan sát trong đó.

Đối với dendrogram của chúng tôi ở đây,

đường thẳng đứng cao nhất là

rõ ràng là đường màu xanh ở đây.

Trước tiên hãy đặt khoảng cách ngưỡng

là 23 và vẽ một đường ngang.

Chúng tôi đang đặt Y thành 23.

Hãy chạy ô này ở đây,

đường ngang

cắt ba đường thẳng đứng khác nhau,

và do đó nó sẽ tạo thành ba cụm.

Ở đây, tất cả các cụm rõ ràng

có số lượng quan sát đáng kể.

Một khả năng khác từ dendrogram này,

là sử dụng ngưỡng 30.

Hãy tiếp tục và

thay đổi giá trị của Y thành 30.

Với ngưỡng này ta được 2 cluster.

Nếu bạn nhớ,

khi chúng tôi áp dụng thuật toán K Mean,

2 cụm cũng được đề xuất

bởi điểm số hình bóng.

Ngoài ra, hãy chú ý rằng chúng ta không cần phải

chỉ định số lượng cụm trong khi

tạo ra các cụm phân cấp.

Lựa chọn đi 2 hoặc 3 cụm,

sẽ phụ thuộc vào nhu cầu kinh doanh,

và phân tích cấp độ sản phẩm

được tiến hành cho từng cụm.

Điều này sẽ tương tự như cách

chúng tôi đã thực hiện phân tích trực quan, vì

một vài tính năng sau khi chúng tôi áp dụng phương tiện K.

Đây là mã có thể giúp

bạn nhận được nhãn cụm,

dựa trên ngưỡng khoảng cách.

Khi bạn nhận được khung dữ liệu với

nhãn cụm, tôi khuyến khích bạn,

để thực hiện phân tích trực quan,

giống như chúng tôi đã làm trước đó.

Trong mã này, t là viết tắt của

ngưỡng khoảng cách chúng tôi đã chọn trước đó.

Hãy thoải mái thay đổi giá trị này và

quan sát số lượng cụm thay đổi như thế nào.

[ÂM THANH].

>> Hiện tại chúng tôi đã thử 2 cách phổ biến

các thuật toán phân cụm và

dường như có sự đồng thuận

tiếp tục với hai cụm.

Nhưng trước khi chúng ta kết luận rằng 2 là

thực sự là số cụm lý tưởng,

chúng ta hãy thử một cái

thuật toán phân cụm hơn.

Quét cơ sở dữ liệu.