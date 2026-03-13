# 08 xây dựng mô hình hồi quy cây quyết định

---

Xin chào người học.

Trong video này, hãy cùng giúp đỡ Synergic

Giải pháp xác định các yếu tố

dự đoán đơn vị bán cho sản phẩm.

Như bạn có thể đã đoán được,

đây là một vấn đề hồi quy.

Vì vậy chúng ta sẽ giải quyết nó bằng cách xây dựng

mô hình hồi quy cây quyết định.

Hãy đi sâu vào ngay.

Đầu tiên, hãy nhập

các thư viện cần thiết.

Bạn thay đổi thư mục làm việc thành

nơi bạn đã lưu trữ tập dữ liệu.

Hãy đọc dữ liệu và

hiển thị năm hàng đầu tiên.

Như bạn có thể thấy, đây là dữ liệu tương tự

chúng tôi đã sử dụng trong các video trước đó

giải quyết vấn đề phân loại.

Vì toàn bộ

quá trình tiền xử lý là như nhau,

hãy nhanh chóng thực hiện quá trình tiền xử lý

và chuyển sang phần về hồi quy.

Quá trình tiền xử lý chủ yếu liên quan đến

tạo một cột mới có tên Good by

Đánh giá Xấu và thực hiện mã hóa nhãn.

Hãy chạy nhanh các ô này và

chuyển sang phần hồi quy.

Vì dữ liệu cũng chứa

đơn vị biến phân loại được bán nhiều hơn

hơn ngàn, chúng ta phải bỏ nó trước

tách biến tính năng và

biến mục tiêu.

Bây giờ là lúc phải chia tay

biến đặc trưng và

biến mục tiêu như chúng ta có thể thấy ở đây.

Bây giờ chúng ta có tính năng và

biến mục tiêu đã sẵn sàng,

hãy thực hiện đào tạo và

kiểm tra sprite trên dữ liệu này.

Cuối cùng, đã đến lúc xây dựng

mô hình hồi quy cây quyết định.

Lần này, chúng ta phải nhập quyết định

công cụ hồi quy cây từ SKlearn.tree.

Chúng ta có thể tạo một bộ hồi quy cây quyết định

đối tượng được gọi là mô hình gạch dưới DT.

Bây giờ hãy xây dựng mô hình

sử dụng dữ liệu huấn luyện.

Bây giờ mô hình đã được xây dựng, hãy thực hiện

dự đoán về cả việc đào tạo và

kiểm tra dữ liệu để so sánh

hiệu suất mô hình của chúng tôi.

Chúng ta hãy nhìn vào

hiệu suất của mô hình.

Để làm như vậy, hãy nhập R2

điểm từ SKlearn.Metrics.

Tương tự, hãy tính điểm R2 cho

việc đào tạo và

kiểm tra dữ liệu để kiểm tra hiệu suất và

đo nếu mô hình được trang bị quá mức.

Giá trị của R bình phương là đặc biệt

tốt cho tập huấn luyện, nhưng

mô hình không thể hoạt động tốt trên

dữ liệu thử nghiệm, do đó mô hình bị quá khớp.

Giống như chúng tôi đã làm cho

Mô hình phân loại cây quyết định

Hãy tìm hiểu tầm quan trọng của tính năng và

bỏ tính năng không liên quan.

Bây giờ hãy xác định những cột có

tầm quan trọng tích lũy vượt quá 0,99 và

lưu trữ chúng trong một danh sách mới

được gọi là Bỏ dấu gạch dưới Cuộc gọi.

Bây giờ chúng ta đã xác định được

những đặc điểm ít quan trọng hơn này,

hãy loại bỏ chúng khỏi dữ liệu

đặt X đào tạo và kiểm tra X.

Bây giờ chúng ta có thể xây dựng mô hình

một lần nữa sử dụng tàu X đã được sửa đổi.

Hãy đưa ra dự đoán

sử dụng thử nghiệm X đã sửa đổi.

Bây giờ, hãy kiểm tra hiệu suất của mô hình

bằng cách kiểm tra giá trị bình phương R của mô hình

trên dữ liệu tàu.

Như bạn có thể thấy, hiệu suất của mô hình

trên dữ liệu tàu một lần nữa

đặc biệt trong khi nó tiếp tục

hoạt động kém trên dữ liệu thử nghiệm.

Vì vậy chúng ta có thể kết luận rằng mô hình

hiệu suất đã được cải thiện,

nhưng nó vẫn được trang bị quá mức.

Hãy cải thiện hiệu suất mô hình

bằng cách điều chỉnh các siêu tham số.

Giống như mô hình quyết định phân loại,

chúng ta sẽ thử nghiệm một cái

độ sâu tối đa của siêu tham số chính.

Hãy xem nếu thay đổi độ sâu tối đa

giá trị có cho chúng ta một mô hình tốt hơn hay không.

Độ sâu của mô hình hiện tại là 35.

Quan sát kết quả,

rõ ràng là khác nhau

tham số độ sâu tối đa dẫn đến

điểm R vuông đào tạo và kiểm tra khác nhau.

Điều thú vị là khi độ sâu tối đa được đặt thành 8,

sự khác biệt giữa tàu hỏa và

điểm kiểm tra được giảm thiểu và cả hai đều đạt được

giá trị bình phương R tối ưu tương ứng của chúng.

Giống như bạn đã làm trong trường hợp

mô hình phân loại,

khám phá các giá trị khác nhau của mẫu Min

lá cùng với giá trị thu được

độ sâu tối đa ở bước trước.

Tôi hy vọng bạn thích quá trình

tinh chỉnh các siêu tham số của chúng tôi

mô hình hồi quy cây quyết định.

Với điều này, chúng tôi kết luận quyết định của chúng tôi

phát triển mô hình cây từ đầu đến cuối.

Trong video sắp tới, chúng tôi sẽ

xem lại vấn đề phân loại của chúng tôi và

thử một kỹ thuật quan trọng để

có khả năng cải thiện hiệu suất.

Vì vậy hãy tiếp tục theo dõi.