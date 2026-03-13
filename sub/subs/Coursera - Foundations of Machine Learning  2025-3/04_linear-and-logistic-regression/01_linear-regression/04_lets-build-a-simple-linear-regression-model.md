# 04 cho phép xây dựng một mô hình hồi quy tuyến tính đơn giản

---

Xin chào và chào mừng trở lại.

Ở phần trước

video, chúng tôi đã hiểu

toán học đằng sau

tìm ra dòng phù hợp nhất.

Giờ là lúc phải tiếp tục

từ lý thuyết đến thực hành.

Trong video này, của chúng tôi

trọng tâm sẽ là

xây dựng đơn giản đầu tiên của chúng tôi

mô hình hồi quy tuyến tính.

Mục tiêu của chúng tôi là dự đoán

đơn vị được bán bằng cách sử dụng

lưu lượng truy cập trang như của chúng tôi

tính năng. Hãy đi sâu vào.

Hồi quy tuyến tính

mô hình có thể được xây dựng cho

hai mục đích, mô tả

và mang tính dự đoán.

Mục tiêu chính của

phương pháp mô tả

là để hiểu những gì

đã xảy ra trong quá khứ

Trong cách tiếp cận này,

chúng tôi không chia rẽ

tập dữ liệu vào huấn luyện và kiểm tra,

và cũng nhìn vào

tất cả các giả định của

hồi quy tuyến tính

mô hình một cách chi tiết.

Trong Python, mô hình thống kê là

được sử dụng rất thường xuyên để xây dựng

các mô hình mô tả.

Ngược lại, trong

phương pháp dự đoán,

trọng tâm chính của chúng tôi là

để đưa ra dự đoán

trên các tập dữ liệu trong tương lai hoặc chưa nhìn thấy.

Trong trường hợp này, chúng tôi không quan tâm

về các giả định và phân chia

tập dữ liệu để có được

hiệu suất dự kiến

trên tập dữ liệu chưa nhìn thấy.

Trong Python, học tâm linh là

thường được sử dụng để xây dựng

các mô hình dự đoán.

Để hiểu được sự thật

sạn và tác động

có nhiều tính năng khác nhau

trên một biến mục tiêu.

Chúng ta sẽ bắt đầu với

Tuy nhiên, phương pháp mô tả

đến cuối bài học,

chúng ta sẽ chuyển sang một

cách tiếp cận mang tính dự đoán.

Hãy bắt đầu bằng cách xây dựng một cách đơn giản

mô hình hồi quy tuyến tính với

phương pháp mô tả

sử dụng các mô hình thống kê

Hãy xây dựng máy ảnh SLR

làm mẫu từng bước.

Trước khi chúng ta đi sâu vào mã,

điều quan trọng là phải đảm bảo rằng

môi trường Python của chúng tôi là

sẵn sàng và cần thiết

các thư viện được cài đặt.

Chúng tôi sẽ sử dụng số liệu thống kê

thư viện mô hình.

Bây giờ bước tiếp theo là

trích xuất các biến x và y.

Ở đây, X và Y được trích xuất

từ tập dữ liệu DF,

trong đó x đại diện cho

biến độc lập

và y đại diện cho

đơn vị biến phụ thuộc được bán.

Các biến này được

then chốt cho các mô hình của chúng tôi,

vì x được dùng để dự đoán y.

Khi đã xong việc đó, tiếp theo

bước là thêm một hằng số.

Thêm một hằng số vào x

đảm bảo rằng việc đánh chặn là

khác không và

mô hình hồi quy

không bị hạn chế

đi qua gốc tọa độ.

Hãy tiếp tục và

chạy tế bào này.

Bây giờ đến bước nơi

chúng ta cần phải phù hợp với mô hình.

Chúng ta sẽ sử dụng hàm OLS

để bắt đầu mô hình bằng cách sử dụng

bình phương tối thiểu thông thường.

Sau đó chúng ta sẽ sử dụng dấu chấm

phương pháp tính toán phù hợp

các giá trị tối ưu

của các hệ số

điều đó làm giảm thiểu tổng

của số dư bình phương,

đó là hàm mất mát.

Hãy thực hiện bước này.

Với mô hình được trang bị,

bước tiếp theo là

dự đoán các giá trị của

y dựa trên

biến độc lập x.

Bây giờ cuối cùng, chúng ta hãy

hình dung mô hình với

đường phù hợp nhất bằng cách vẽ đồ thị

các điểm dữ liệu thực tế bằng cách

sử dụng chức năng Plt.Scatter và

các điểm dự đoán hoặc

đường hồi quy bằng cách sử dụng

hàm Plt.plot.

Sau khi phù hợp với hồi quy của chúng tôi

dòng vào dữ liệu.

Bước quan trọng tiếp theo là

hiểu các hệ số

đặc biệt là độ dốc

và sự đánh chặn.

Chúng ta sẽ sử dụng mô hình

chức năng

để lưu trữ các giá trị

của các hệ số.

Hàm này lấy

các hệ số

sử dụng phương pháp lập chỉ mục.

Chúng tôi đã thu được

giá trị chính xác

độ dốc và giao điểm.

Bây giờ chúng ta có thể nói rằng

đường hồi quy của chúng tôi

có thể được xác định bởi

phương trình y bằng

đến 526,2275 cộng 0,1806x.

Điều này cho chúng ta biết khi nào

lưu lượng truy cập trang bằng không,

chúng ta có thể mong đợi hàng tuần

đơn vị bán hàng là 526.

Với đơn vị tăng

trong lưu lượng truy cập trang,

chúng ta có thể mong đợi đơn vị của chúng ta

doanh số bán hàng tăng 0,18.

Ví dụ, nếu

lưu lượng truy cập trang là

1.000 đơn vị có thể bán được

được tính như sau.

Y bằng 526,2275

cộng 0,1806 vào x.

Khi mô hình của chúng tôi được xây dựng,

bước quan trọng tiếp theo trong

phương pháp mô tả là

xem xét kỹ lưỡng hiệu suất của nó và

nhìn vào chiếc chìa khóa đó

thông số thống kê.

Điều này có thể được thực hiện một cách thuận tiện

sử dụng tóm tắt mô hình

trong mô hình thống kê.

Từ bản tóm tắt được cung cấp,

chúng ta có thể thấy rằng

Giá trị bình phương R là

0,363 chỉ ra rằng

khoảng 36,3%

của các biến thể

trong số đơn vị đã bán có thể là

được giải thích bởi lưu lượng truy cập trang.

Trong khi đây không phải là một

tỷ lệ cực cao,

đó là một khởi đầu tốt đẹp

và có thể có

các biến hoặc yếu tố khác

có thể giúp cải thiện điều này.

Điều quan trọng cần lưu ý

giá trị p trong bản tóm tắt.

Đối với cả lưu lượng truy cập trang

và hằng số,

những giá trị này đang chỉ ra

cho cả hai hằng số

và lưu lượng truy cập trang.

Giá trị P nhỏ

chỉ ra rằng

những hệ số này

có ý nghĩa thống kê.

Với tư cách là một quy ước,

để có một tính năng

tác động đáng kể

biến mục tiêu,

giá trị P nên

nhỏ hơn 0,05.

Tính đến thời điểm hiện tại, chúng tôi đã bao gồm

chỉ có một tính năng trong khi

xây dựng mô hình

điều đó giải thích

giá trị bình phương R thấp

mà chúng tôi đã đạt được.

Trong video tiếp theo, chúng ta hãy

cố gắng cải thiện

Giá trị bình phương R bằng

thêm nhiều tính năng hơn và

tạo bội số

mô hình hồi quy tuyến tính.

Chúng ta cũng sẽ khám phá cái khác

thông số thống kê

từ mô hình tóm tắt dấu chấm,

điều này sẽ giúp chúng ta hiểu

giả định của

hồi quy tuyến tính.