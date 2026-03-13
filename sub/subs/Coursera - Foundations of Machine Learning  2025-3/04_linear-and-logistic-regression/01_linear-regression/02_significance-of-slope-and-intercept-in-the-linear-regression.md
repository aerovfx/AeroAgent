# 02 ý nghĩa của độ dốc và điểm chặn trong hồi quy tuyến tính

---

Xin chào và chào mừng trở lại.

Trong video trước chúng ta đã thảo luận

các khái niệm nền tảng

của hồi quy tuyến tính.

Chúng tôi đã khám phá nó

nhiều hình thức khác nhau và

khám phá sự đa dạng của nó

ứng dụng.

Trong video này, chúng tôi sẽ

hiểu điều điên rồ

và bu lông đơn giản

hồi quy tuyến tính.

Chúng tôi sẽ xây dựng đơn giản của riêng mình

mô hình hồi quy tuyến tính

để dự đoán số lượng

đơn vị được bán với

chỉ một biến.

Bây giờ điều đó đưa chúng ta đến một

câu hỏi rất quan trọng.

Chúng ta chọn thế nào

một biến đó?

Chúng tôi muốn chọn

một biến có

hiệp hội mạnh nhất

với biến mục tiêu của chúng tôi,

đó là đơn vị đã bán.

Đây là nơi có sự tương quan

phân tích có thể giúp chúng tôi.

Phân tích tương quan

cho phép chúng ta định lượng

sức mạnh của tuyến tính

mối quan hệ giữa các biến.

Hãy chuyển sang một

Máy tính xách tay sao Mộc và

thực hiện tương quan

phân tích trên tập dữ liệu của chúng tôi.

Nhưng trước đó,

chúng ta cần nhập khẩu

các thư viện cần thiết và sau đó

nhập tập dữ liệu

vào Máy tính xách tay Sao Mộc.

Hãy thực hiện các bước này.

Hãy bắt đầu với

nhập thư viện trước.

Bây giờ thay đổi thư mục làm việc

đến nơi bạn có

đã lưu trữ tập dữ liệu.

Hãy tải tập dữ liệu và

nhìn vào vài hàng đầu tiên.

Một khi việc này được thực hiện,

ở bước tiếp theo,

hãy biểu diễn

phân tích tương quan.

Chúng tôi sẽ bỏ phân đoạn

tính năng vì nó là của

loại đối tượng và truyền thống

phân tích tương quan

không áp dụng cho nó.

Chúng tôi sẽ bỏ tính năng này trong khi

thực hiện phân tích tương quan.

Lưu ý rằng các đơn vị gạch dưới

bán được hơn 1.000

tính năng có

tương quan cao nhất

với tính năng mục tiêu.

Điều này rất rõ ràng vì chúng ta có

đã tạo tính năng này từ

một tính năng mục tiêu của chính nó.

Điều rất quan trọng là phải loại bỏ

điều này khi tập luyện

mô hình như chúng tôi

sẽ không có tính năng này trong

thế giới thực và điều này sẽ

dẫn đến những dự đoán xấu.

Hãy bỏ tính năng này đi và

thực hiện tương quan

phân tích một lần nữa.

Ở đây bạn có thể thấy lưu lượng truy cập trang

xuất hiện nhiều nhất

biến tương quan dương,

theo sau là

num_unique-chiến dịch,

mặc dù có một

khoảng cách đáng kể giữa

các giá trị tương quan của

cả hai cột này.

Dự kiến, đơn giá là

mối tương quan tiêu cực nhất

thay đổi theo đơn vị được bán.

Dựa trên thông tin này,

hãy sử dụng lưu lượng truy cập trang để xây dựng

mô hình hồi quy tuyến tính đơn giản

và hiểu

toán học đằng sau nó.

Khi chúng ta nói về toán học

hồi quy tuyến tính đơn giản,

nó khá đơn giản.

Nó giống như phương trình của

một đường thẳng, y=mx+c.

Đây y là những gì chúng ta đang có

cố gắng dự đoán,

trong trường hợp của chúng tôi là đơn vị đã bán.

M là độ dốc của đường

Nó cho chúng ta biết bao nhiêu y

thay đổi khi x thay đổi.

X là tính năng của chúng tôi

sử dụng để làm

dự đoán, và đối với chúng tôi,

đó là lưu lượng truy cập trang và cuối cùng,

C. C là giao điểm,

dòng ở đâu

đi qua trục y.

Độ dốc và điểm chặn y

là quan trọng vì họ

xác định tuyến tính và

định vị hồi quy

đường trong đồ thị.

Họ có vai trò tối quan trọng trong

hiểu bản chất của

mối quan hệ giữa

đơn vị đã bán và lưu lượng truy cập trang.

Để hiểu được

ý nghĩa thực tiễn của

độ dốc và

chặn y trong tập dữ liệu của chúng tôi,

chúng ta hãy kiểm tra trực quan

tác động của chúng lên

sự định hướng và vị trí

của đường thẳng trong đồ thị.

Chúng ta hãy hiểu

tầm quan trọng của độ dốc

và chặn bằng cách đi

qua một vài ví dụ.

Hãy tạo ra một điều hữu ích

chức năng đó sẽ

giúp chúng tôi vẽ đường thẳng

dòng trên ô phân tán

của cả hai đơn vị đã bán

và lưu lượng truy cập trang

dựa trên độ dốc và giao điểm

những giá trị mà chúng tôi cung cấp.

Hãy chạy ô bên dưới

để xem đầu ra.

Khi chúng tôi chỉ định m

là 0,2 và C là 0,

chúng tôi quan sát điều đó bởi vì

chặn hoặc C là 0,

đường thẳng đi qua gốc tọa độ.

Điều này có nghĩa là dòng

đi qua trục y tại gốc tọa độ.

Độ dốc 0,2 ở đây thể hiện

độ nhạy của đơn vị

bán cho những thay đổi

trong lưu lượng truy cập trang.

Nó định lượng điều đó cho

mỗi đơn vị tăng

trong lưu lượng truy cập trang,

đơn vị bán tăng

bằng 0,2 đơn vị.

Đường này có thể giúp chúng ta dự đoán

giá trị của y hoặc đơn vị

được bán với bất kỳ giá trị nào

của x hoặc lưu lượng truy cập trang.

Bây giờ hãy thêm một cái nữa

đường vào biểu đồ của chúng tôi.

Bằng cách sửa đổi giá trị của m thành

0,4 trong khi giữ

hằng số C tại 0,

chúng tôi quan sát thấy rằng dòng

vẫn cắt trục y

thông qua nguồn gốc,

nhưng có độ dốc lớn hơn

so với trường hợp trước.

Điều này tích cực hơn

độ dốc hàm ý

độ nhạy tăng cường của đơn vị

được bán cho biến thể

trong lưu lượng truy cập trang.

Cụ thể, nó có nghĩa là

cho mỗi đơn vị tăng

trong lưu lượng truy cập trang,

đơn vị bán bây giờ tăng

bằng 0,4 đơn vị,

đó là mức tăng gấp đôi

quan sát với độ dốc 0,2.

Bây giờ, trong trường hợp tiếp theo,

hãy hiểu

tầm quan trọng của

y-chặn bằng cách giữ

hằng số độ dốc.

Giữ độ dốc

không đổi ở mức 0,4 và

thay đổi

y-chặn C đến 500,

chúng tôi quan sát thấy một chiều dọc

thay đổi trong dòng,

chỉ ra rằng

dòng bây giờ vượt qua

trục y tại điểm 0, 500.

Bây giờ bạn có thể thấy ở đây rằng

đường màu xanh đã bị dịch chuyển.

Bây giờ vượt qua y tại y=500.

Giá trị chặn của

500 có nghĩa là thậm chí

khi lưu lượng truy cập trang bằng 0,

mô hình dự đoán

đơn vị bán được 500.

Độ dốc không đổi,

vẫn chứng minh rằng đối với

mỗi đơn vị tăng

trong lưu lượng truy cập trang,

đơn vị bán tăng 0,4 đơn vị.

Điều này cũng được quan sát thấy

từ thực tế

rằng đường màu xanh là

song song với đường màu xanh lá cây.

Cho đến nay chúng tôi đã xem xét

các tình huống có độ dốc

nhận các giá trị dương.

Trong kịch bản tiếp theo và cuối cùng,

chúng ta hãy hình dung ý nghĩa

độ dốc âm bởi

thiết lập giá trị độ dốc thành

trừ 20 và chặn tới 1500.

Bằng cách đặt m thành âm

20 và C đến 1500,

chúng ta có thể thấy rằng dòng

đã có độ dốc đi xuống,

chặn trục y

tại điểm 0, 1500.

Độ dốc 20 gợi ý

đó cho mỗi đơn vị

tăng đơn giá,

đơn vị bán giảm đi

bằng 20 đơn vị,

phản ánh sự mạnh mẽ

tương quan âm

giữa hai biến.

Điều đó đưa chúng ta đến

cuối video này.

Tìm hiểu vai trò của

độ dốc và chặn y trong

phương trình tuyến tính cung cấp một

hiểu biết nền tảng

tuyến tính đơn giản

các mô hình hồi quy.

Trong video tiếp theo, chúng tôi sẽ

sử dụng những bài học này

để hiểu

cơ sở trên đó

dòng phù hợp nhất có thể

được tìm thấy cho tuyến tính

các mô hình hồi quy.