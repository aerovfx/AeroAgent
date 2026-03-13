# 02 Hãy-hình dung-cây quyết định

---

Trong video này, chúng ta hãy sử dụng một chút

tập hợp con dữ liệu từ synergix

vấn đề phân loại để xây dựng và

hình dung mô hình cây quyết định.

Một khi chúng ta xây dựng được một thế lực vững mạnh

hiểu biết về các khái niệm,

chúng tôi sẽ sử dụng tập dữ liệu gốc

cũng như để xây dựng mô hình.

Vì video này và các video tiếp theo

sẽ được thực hành,

vui lòng tạm dừng video và

mã cùng.

Để tải xuống tập hợp con nhỏ của dữ liệu,

đi đến phần tài nguyên

được cung cấp cùng với khóa học này.

Hãy bắt đầu bằng cách nhập

các thư viện cần thiết.

Thay đổi thư mục làm việc thành

nơi bạn đã lưu trữ tập dữ liệu.

Hãy đọc dữ liệu và hiển thị nó.

Như bạn có thể thấy từ dữ liệu, chúng tôi có

chỉ giữ lại những đặc điểm phân loại đó

có ba hoặc

ít danh mục riêng biệt hơn.

Hơn nữa, chúng tôi đã xem xét

vấn đề phân loại.

Bây giờ bạn có thể thắc mắc tại sao chúng tôi

chỉ giữ các tính năng phân loại và

nhìn vào phân loại hiệp lực

vấn đề trong tập dữ liệu này?

Đó là bởi vì cây quyết định đã

ban đầu được xây dựng để chỉ xử lý

vấn đề phân loại và

điều đó cũng chỉ với dữ liệu phân loại.

Vì vậy, chỉ có các tính năng phân loại sẽ

làm cho quá trình phân tách đơn giản hơn và

dễ hiểu hơn.

Hơn nữa, như chúng ta đang xem xét

tính năng phân loại với số lượng hạn chế

có giá trị duy nhất, quyết định

cây sẽ có ít cành hơn.

Hãy tiếp tục và chia tập dữ liệu thành

các biến độc lập, đó là các đặc điểm,

và biến phụ thuộc,

đó là số đơn vị được bán lớn hơn nghìn.

Vì chúng ta chỉ đang cố gắng hiểu

cách xây dựng cây quyết định với giới hạn

dữ liệu, chúng tôi sẽ không chia tập dữ liệu

vào tập huấn luyện và tập kiểm tra.

Vì vậy, hãy trực tiếp xây dựng mô hình.

Đầu tiên, chúng ta sẽ nhập

phân loại cây quyết định.

Tiếp theo, chúng ta sẽ tạo cây quyết định

đối tượng phân loại được gọi là DT_model.

Như bạn có thể thấy, chúng tôi đã sử dụng tiêu chí

gini, mà chúng ta sẽ hiểu sau.

Chúng tôi cũng đã thiết lập

trạng thái ngẫu nhiên là 42.

Đó là vì cây quyết định có rất nhiều

về tính ngẫu nhiên được xây dựng bên trong mô hình,

và tham số này giúp trong

kiểm soát tính ngẫu nhiên.

Tuy nhiên, nó không loại bỏ nó.

Nó có nghĩa là mô hình của bạn có thể

khác với mô hình của tôi ngay cả khi chúng tôi

sử dụng cùng một trạng thái ngẫu nhiên.

Hãy tiếp tục và chạy ô này.

Bây giờ mô hình đã được xây dựng,

hãy tiếp tục và

hình dung cây quyết định bằng cách

sử dụng phương pháp cây lô.

Phương pháp cây lô này cần

những lập luận chính sau đây.

Mô hình cây quyết định

được gọi là DT_model.

Danh sách tên tính năng

được dán nhãn là các tính năng.

Một danh sách có thứ tự các tên lớp trong đó

doanh thu thấp tương ứng với 0 và

bán cao tương ứng với 1.

Tham số đã điền,

mà khi được đặt thành true sẽ lấp đầy các nút cây

với màu sắc để biểu thị lớp đa số.

Bây giờ hãy chạy mã và

trưng bày cây.

Đây là cây quyết định.

Xin lưu ý rằng cây quyết định của tôi có thể

trông khác với quyết định của bạn

cây vì tính ngẫu nhiên.

Chúng ta hãy sử dụng hình ảnh đơn giản này của

một cây quyết định để hiểu nó.

This is a simple image we will be

sử dụng cho vài video tiếp theo.

Như bạn có thể thấy, ở mỗi lần chia,

hai nút phụ được tạo ra.

Như đã thảo luận trong video trước,

đó là vì loại quyết định

triển khai cây được sử dụng trong

scikit-learn tạo ra hai

các nút phụ trên mỗi lần chia.

Việc thực hiện cụ thể này

của cây quyết định được gọi là GIỎ HÀNG,

hoặc cây phân loại và hồi quy.

Có những triển khai khác là tốt.

Một số cái phổ biến

là Phép phân đôi lặp lại 3,

đó là ID3, C4.5 và C5, v.v.

Bây giờ chúng ta hãy xem xét kỹ hơn và

hiểu cái gì là

xảy ra bên trong cây.

Cây trông như thế này.

Nó bắt đầu với nút gốc.

Nó đại diện cho toàn bộ dữ liệu và

do đó tổng số quan sát hoặc

mẫu là 30.

Trong số 30 mẫu có 15 mẫu

belong to the class low sales and

15 mẫu còn lại thuộc về

đến lớp bán hàng cao.

Vì nút gốc chứa bằng nhau

mẫu thuộc cả hai lớp,

nó là một nút rất không tinh khiết.

Ở đây chúng ta có thể thấy lớp = Doanh thu thấp,

mặc dù cả hai lớp đều có

số lượng mẫu bằng nhau.

Đó là bởi vì trong hiện tại

triển khai scikit-learn,

cây quyết định chọn số

hạng nhất trong trường hợp số lượng bằng nhau

các mẫu có mặt trong một nút cho

các lớp khác nhau.

Trong trường hợp này, lớp 0 là số

hạng nhất đại diện cho doanh thu thấp.

Bây giờ hãy chuyển trọng tâm của chúng ta sang

mục đầu tiên trong nút.

Bạn có nhận thấy tình trạng này không?

Nó xác định cách tập dữ liệu của chúng tôi

được chia thành các nút tiếp theo.

Trong cây quyết định vẽ

bởi hàm cây đồ thị,

mẫu dữ liệu thỏa mãn

điều kiện đi đến nhánh bên trái.

Mẫu dữ liệu không thỏa mãn

điều kiện đi đến nút nhánh bên phải.

Như chúng ta có thể thấy, trong số 30 mẫu,

24 mẫu thỏa mãn điều kiện và

6 mẫu thì không.

Vì vậy dữ liệu được phân chia tương ứng

trong hai nút nhánh.

Ở nút nhánh trái,

trong số 24 mẫu có 10 mẫu thuộc về

đến mức doanh thu thấp và

14 mẫu thuộc loại có doanh số cao.

Tương tự, ở nút nhánh bên phải,

trong số sáu mẫu thì có năm mẫu thuộc về

đến mức doanh thu thấp, trong khi một

mẫu thuộc về lớp bán hàng cao.

Khi nút gốc được phân chia

thành hai nút nhánh,

cái cây không dừng lại ở đó.

Mỗi nút nhánh tiếp theo

được chia thành hai hoặc

nhiều nút hơn dựa trên các điều kiện cụ thể.

Như bạn có thể thấy ở đây, nhánh bên trái

nút được chia thêm dựa trên

điều kiện là giá trị của

đoạn này nhỏ hơn hoặc bằng 0,5.

Bằng cách này, cây tiếp tục tách ra

cho đến khi tới được các nút lá.

Như một bản tóm tắt nhanh chóng,

nút lá là nút tạo ra

điểm cuối của cây quyết định.

Mặt khác,

nút nhánh bên phải xa hơn

chia dựa trên số lượng

khuyến mãi nhỏ hơn hoặc bằng 0,5.

Nếu bạn để ý, sau khi chia quyền

nút nhánh thành hai nút phụ,

quá trình phân tách bị dừng lại.

Vì vậy hai nút phụ này

cũng là các nút lá.

Nút lá bên trái có các mẫu thuộc về

cho cả hai lớp, vì vậy đó là một nút không tinh khiết.

Nút lá bên phải có mẫu

chỉ thuộc một loại, doanh thu thấp.

Vì vậy, nó là một nút thuần túy.

Nếu bạn nhìn vào bảng màu

của toàn bộ lô cây,

bạn có thể thấy rằng tất cả các nút

có doanh thu cao như dự đoán

lớp học tràn ngập màu xanh,

trong khi tất cả các nút có lớp

dự đoán doanh số thấp

được lấp đầy bởi màu cam.

Khi độ tinh khiết của các nút tăng lên,

cường độ của màu sắc cũng tăng lên.

Vậy là chúng ta hãy kết thúc video này.

Bây giờ bạn đã nắm vững

những nguyên tắc cơ bản đằng sau việc xây dựng

mô hình cây quyết định

Tuy nhiên, bạn có thể thắc mắc, điều gì

logic đằng sau mỗi sự phân chia?

Tiêu chí nào chi phối

mỗi nút sẽ được phân chia như thế nào?

Hãy cùng tìm hiểu điều đó trong video tiếp theo của chúng tôi.