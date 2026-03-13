# 05 mô hình thực hành xây dựng cây quyết định

---

Xin chào người học. Trong video này,

hãy bắt đầu bằng việc xây dựng

mô hình cây quyết định giúp

Giải pháp tổng hợp để xác định

sản phẩm nào sẽ bán

hơn 1.000 đơn vị.

Đầu tiên, hãy nhập

các thư viện cần thiết.

Hãy thay đổi

thư mục làm việc

đến nơi chúng tôi có

đã lưu trữ tập dữ liệu của chúng tôi.

Tiếp theo, hãy đọc dữ liệu

và hiển thị năm hàng đầu tiên.

Bây giờ chúng ta có

đã tải tập dữ liệu,

chúng ta hãy tập trung vào

cột một sao,

hai sao, ba sao,

bốn sao và

xếp hạng năm sao.

Trong mô-đun trước

bao gồm tuyến tính và

hồi quy logistic,

bạn đã quan sát thấy điều đó

những cột này là

có tính chất tích lũy.

Nó tạo ra một khuôn mẫu trong

dữ liệu đào tạo và cản trở

hiệu suất của mô hình.

Để xử lý vấn đề này,

chúng ta sẽ tạo một cột

gọi là tốt bằng xấu,

đó sẽ là tỷ lệ

xếp hạng tốt và xấu.

Vì nó là một tỷ lệ nên

nó sẽ không có vấn đề gì đối với

ML tích lũy

xếp hạng mang lại.

Để tạo cột này trước tiên,

chúng ta sẽ tính tổng

số lượng xếp hạng tốt,

đó là bốn sao và

xếp hạng năm sao,

và sau đó chúng tôi sẽ tính toán

the sum of numbers

về những đánh giá xấu.

Đó là đánh giá một sao

và xếp hạng hai sao.

Vì giá trị của

xếp hạng cột 3 sao

cho biết đánh giá trung lập,

chúng tôi không xem xét

những giá trị này hoặc trong

hạng mục xếp hạng tốt hoặc

trong danh mục đánh giá xấu.

Sau đó chúng ta có thể tính toán

tỷ lệ của

xếp hạng tốt và xấu trong

một cột mới được gọi là

tốt bởi đánh giá xấu.

Trong khi tính toán điều này

tỉ số, nếu là mẫu số,

đó là tổng các giá trị của

cột đánh giá một sao

và xếp hạng hai sao,

hóa ra là số không,

thì nó sẽ dẫn đến

một lỗi chia số không.

Để xử lý

mối quan tâm này, đầu tiên,

Hãy tìm hiểu xem liệu

những cột này có

bất kỳ giá trị 0 nào.

Ở đây chúng tôi có một lượng đáng kể

số lượng hàng

chứa giá trị 0 trong

cả một sao và

đánh giá hai sao.

Trong bước tiếp theo, chúng ta có thể

xử lý các cạnh này

trường hợp bằng cách tạo

một danh sách trống và thêm giá trị

trong danh sách dựa trên

ba kịch bản này.

Kịch bản 1. Đối với kịch bản này,

chúng tôi sẽ kiểm tra xem tổng của

giá trị của một sao

xếp hạng và xếp hạng hai sao,

cũng như tổng các giá trị của

xếp hạng bốn sao và

xếp hạng năm sao bằng không.

Trong trường hợp này, chúng ta có thể giữ

các giá trị tương ứng

bằng 0 trong danh sách mới

như chúng ta có thể giả định

mặt hàng đó có

không có đánh giá cho đến nay. Kịch bản 2.

Tổng số chỉ là xấu

xếp hạng là bằng không.

Đối với kịch bản này, chúng tôi sẽ

kiểm tra xem chỉ có tổng các giá trị,

đánh giá một sao và

xếp hạng hai sao, bằng không.

Nếu vậy, trong trường hợp đó,

mẫu số của

tỷ lệ kết quả sẽ bằng không.

Để tránh lỗi chia bằng 0,

chúng ta có thể giữ tương ứng

giá trị tạm thời

trừ 99.999 vào danh sách mới.

Sau này chúng ta sẽ thay thế

giá trị này tối đa

giá trị của tỷ lệ

để biểu thị tỷ lệ cao của

sự tích cực

xếp hạng. Kịch bản 3.

Tổng hợp những điều xấu

xếp hạng là khác không.

Đối với kịch bản này,

chúng ta có thể trực tiếp

tính tỉ số và

thêm chúng vào danh sách mới.

Hãy chạy ô bên dưới.

Tiếp theo, chúng ta có thể thay thế

giá trị tạm thời của âm

99.999 với mức tối đa

các giá trị của tỷ số.

Tiếp theo, hãy thêm

giá trị của danh sách trong

khung dữ liệu với cột

đặt tên tốt theo đánh giá xấu.

Chúng ta hãy nhìn vào

người đứng đầu dữ liệu.

Bây giờ chúng ta có một cột được gọi là

tốt bởi đánh giá xấu ở cuối.

Hãy thả tất cả các cột

liên quan đến xếp hạng.

Tiếp theo, chúng ta hãy nhìn vào

đoạn cột đó

chứa các giá trị phân loại.

Hãy xem có gì khác biệt

các danh mục có trong đó.

Từ kết quả,

rõ ràng là

cột phân đoạn có ba

phân khúc riêng biệt: Trang điểm,

dưỡng da, chăm sóc tóc.

Nhưng đối với quyết định

mô hình cây để làm việc,

chúng ta phải chuyển đổi những thứ này

giá trị phân loại

thành các giá trị số.

Để làm như vậy, chúng tôi sẽ sử dụng

mã hóa nhãn.

Mã hóa nhãn gán một

nhãn số độc đáo

theo từng loại riêng biệt,

chuyển đổi

giá trị phân loại

thành các giá trị số.

Chăm sóc tóc trở thành số không,

trang điểm trở thành một, và

chăm sóc da trở thành hai.

Một điều quan trọng về

mã hóa nhãn là nó

giới thiệu một thứ tự tùy ý

đến các giá trị phân loại.

Nhưng đối với tập dữ liệu của chúng tôi,

điều này không được áp dụng vì

không có trật tự

trong các phân đoạn.

Hơn nữa, cây quyết định

mạnh mẽ trong việc xử lý

dữ liệu phân loại và

đừng để bị ảnh hưởng

bởi những mệnh lệnh tùy tiện như vậy,

không giống như các mô hình tuyến tính.

Trong khi mã hóa một nóng là

thường được ưa thích

cho các mô hình tuyến tính,

chúng ta có thể sử dụng mã hóa nhãn

cho các mô hình cây quyết định.

Hãy áp dụng nhãn

mã hóa như được hiển thị ở đây.

Hãy kiểm tra tập dữ liệu ngay bây giờ.

Ở đây, các giá trị của

phân khúc đã thay thế

với các giá trị số.

Bây giờ lưu ý rằng dữ liệu

tập hợp có cột,

đơn vị đã bán và đơn vị đã bán

cả hai đều lớn hơn 1.000,

đơn vị được bán ở đâu

một biến mục tiêu liên tục

và đơn vị bán được nhiều hơn

hơn 1.000 là

mục tiêu phân loại

biến chứa

giá trị nhị phân 0 và 1

tương ứng với doanh thu thấp,

máy bán ở đâu

nhỏ hơn 1.000,

doanh thu cao, nơi đơn vị

bán được nhiều hơn

1.000 tương ứng.

Vì vấn đề chúng ta đang giải quyết

là một vấn đề phân loại,

chúng ta phải bỏ

đơn vị cột đã bán.

Bây giờ chúng ta có một cách khá

tập dữ liệu đã xử lý

tách biệt các

biến đặc trưng

và biến mục tiêu.

Bây giờ chúng ta có tính năng

và các biến mục tiêu đã sẵn sàng,

đã đến lúc thực hiện chuyến tàu và

kiểm tra phân chia trên tập dữ liệu.

Hãy kiểm tra

kích thước của mỗi lần chia.

Bây giờ là lúc để xây dựng

mô hình cây quyết định đầu tiên

Để làm như vậy, hãy nhập

phân loại cây quyết định.

Tiếp theo, chúng ta có thể tạo

phân loại cây quyết định

đối tượng được gọi là DT_model.

Bây giờ hãy xây dựng mô hình

sử dụng dữ liệu huấn luyện.

Bây giờ một mô hình đã được xây dựng,

hãy thực hiện dự đoán trên

cả việc đào tạo và

dữ liệu thử nghiệm.

Điều này sẽ giúp chúng ta so sánh

hiệu suất mô hình của chúng tôi trên cả hai

dữ liệu huấn luyện và kiểm tra.

Bây giờ chúng ta hãy nhìn vào

hiệu suất của mô hình.

Để làm như vậy, hãy nhập

báo cáo phân loại

từ sklearn.metrics.

Bây giờ trước tiên hãy in

báo cáo phân loại

trên tập dữ liệu huấn luyện.

Như bạn có thể thấy,

hiệu suất mô hình

trên dữ liệu tàu là đặc biệt.

Chúng tôi đã đạt được hiệu suất 100%

cho điểm f1 cho Lớp 1,

cùng với tất cả các

các số liệu khác.

Theo quy ước,

tầm quan trọng cao hơn

được trao cho Lớp 1,

vậy điểm f1 cũng vậy

được xét vào lớp 1

Bây giờ hãy hiển thị

báo cáo phân loại

của mô hình trên dữ liệu thử nghiệm.

Từ báo cáo phân loại,

chúng ta có thể suy luận rằng

hiệu suất mô hình

thấp hơn trên dữ liệu thử nghiệm.

Ngoài ra, sự khác biệt

trong điểm f1 cho

Lớp 1 giữa

dữ liệu đào tạo và kiểm tra là rất lớn.

Do đó, chúng ta có thể nói rằng

mô hình quá phù hợp.

Điều này là do

thuật toán cây quyết định

là một thuật toán tham lam.

Tại mỗi bước của

quá trình xây dựng cây,

cách chia tốt nhất là

được thực hiện cho bước đó.

Nó không chiếu

chuyển tiếp để chọn

sự chia rẽ sẽ nhiều hơn

tối ưu cho toàn bộ cây.

Như chúng ta đã thảo luận ở

các video trước đó,

cây quyết định có xu hướng

trở nên rất cụ thể đối với

huấn luyện dữ liệu và có thể thực hiện

kém trên tập dữ liệu chưa nhìn thấy.

Đừng lo lắng, chúng tôi sẽ

học cách giảm

vấn đề trang bị quá mức

trong một video sau.

Cây quyết định có tính chất duy nhất

tài sản mà nó có thể cho chúng ta biết

tầm quan trọng tương đối của

các tính năng khác nhau

được sử dụng để xây dựng mô hình.

Việc này được thực hiện dựa trên cách

một tính năng cụ thể là

được sử dụng trong việc chia tách

tập dữ liệu.

Tổng của

tầm quan trọng của tính năng

của tất cả các tính năng thêm vào một.

Tài sản này cũng có thể

được sử dụng để thoát khỏi

dựa trên các tính năng không liên quan

về điểm quan trọng tích lũy.

Các quy ước phổ biến để

bỏ các tính năng dựa trên

điểm tích lũy là

0,99, 0,95 và 0,90.

Hãy hiểu tầm quan trọng của tính năng

và bỏ các cột không liên quan.

Đầu tiên chúng ta hãy truy xuất

điểm số quan trọng

từ quyết định sửa đổi.

Tiếp theo, hãy sắp xếp các tính năng theo

quan trọng trong quyết định

thứ tự trong DataFrame.

Như bạn có thể thấy,

lưu lượng truy cập trang tính năng

nắm giữ cao nhất

điểm số quan trọng,

biểu thị mức độ tối đa của nó

ý nghĩa trong mô hình.

tính năng

Good_By_Bad_Rating bật

tỷ lệ đánh giá cũng giữ nguyên

ý nghĩa đáng kể.

Bây giờ hãy tạo một cột mới

được gọi là tầm quan trọng tích lũy trong

DataFrame vậy

mà nó có thể chứa

điểm tích lũy của

cột tầm quan trọng

Bây giờ hãy xác định một cách hiệu quả

những đặc điểm ít quan trọng nhất.

Để làm được điều đó chúng ta phải xác định

những cột có tích lũy

tầm quan trọng vượt quá 0,90.

Tất cả các cột này đều

được lưu trữ trong một danh sách mới

được gọi là drop_col.

Bây giờ chúng ta đã xác định được

những đặc điểm ít quan trọng hơn,

hãy thả chúng ra khỏi

tập dữ liệu x_train và x_test.

Bây giờ hãy xây dựng mô hình

một lần nữa bằng cách sử dụng x_train đã sửa đổi.

Bây giờ hãy đưa ra dự đoán

sử dụng x_test đã sửa đổi.

Hãy kiểm tra mô hình

hiệu suất bằng cách kiểm tra

báo cáo phân loại

của mô hình trên dữ liệu tàu.

Như bạn có thể thấy,

hiệu suất mô hình

trên dữ liệu tàu là

một lần nữa đặc biệt.

Chúng tôi đã đạt được hiệu suất 100% cho

Lớp 1 và dành cho

tất cả các số liệu khác.

Bây giờ hãy hiển thị

báo cáo phân loại

của mô hình trên dữ liệu thử nghiệm.

Như bạn có thể thấy,

hiệu suất mô hình

đã không thay đổi nhiều.

Chúng ta có thể cố gắng cải thiện

hiệu suất mô hình của

mô hình bằng cách cắt tỉa.

Điều này có thể được thực hiện bằng cách sử dụng

siêu tham số của

cây quyết định.

Để làm điều đó, chúng ta hãy

đầu tiên tìm hiểu về

các siêu tham số khác nhau được sử dụng

trong các mô hình cây quyết định.

Đó là chuyện tiếp theo

video, vì vậy hãy theo dõi.