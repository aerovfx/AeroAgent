# 10 phân tích sinh-ai-cho-dữ liệu

---

Xin chào và chào mừng đến với

video cuối cùng của bài học này.

Chúng tôi đã hoàn thành

xử lý trước dữ liệu.

Chúng tôi cũng đã thực hiện EDA cơ bản

để giúp chúng tôi hiểu

điểm dữ liệu cụ thể và

xử lý trước dữ liệu một cách logic.

Nhưng tất cả điều này đã mất

chúng tôi rất nhiều thời gian,

đó là một chút

có tác dụng răn đe trong

thế giới hiện tại

kết quả ở đâu

dự kiến trong

thời gian nhanh nhất có thể.

Một cách để tăng tốc độ của bạn

hiểu biết và tìm tòi

dữ liệu là bằng cách sử dụng

công cụ AI sáng tạo dành cho

nhiệm vụ khoa học dữ liệu của bạn.

Trong video này, chúng ta hãy

hiểu làm thế nào chúng ta có thể

tận dụng một công cụ phổ biến,

ChatGPT, để thực hiện

phân tích dữ liệu thăm dò

trên dữ liệu POS.

Hãy truy cập chat.openai.com và

đăng nhập với của bạn

tài khoản có liên quan.

Theo mặc định, chúng tôi sẽ đạt được

phiên bản miễn phí của

công cụ có sẵn công khai,

đó là ChatGPT 3.5.

Bây giờ là cách ChatGPT

công việc rất đơn giản.

Dù bạn có thắc mắc gì

có liên quan đến EDA của bạn,

chỉ cần gõ nó ra trong khu vực này

càng nhiều chi tiết càng tốt.

Tin nhắn này bạn gửi tới

ChatGPT được gọi là lời nhắc.

Chúng ta hãy bắt đầu bằng cách hỏi một số

câu hỏi thống kê.

Cùng với

câu hỏi, chúng ta phải

cũng thiết lập bối cảnh công việc của chúng tôi.

Giả sử chúng ta muốn tìm cái nào

SKU_ID có giá trị cao nhất

có nghĩa là đơn giá.

Chúng ta có thể viết một câu nói nhắc nhở,

Tôi có khung dữ liệu có tên là 'pos'.

Tôi muốn tìm SKU_ID

giá trị trung bình cao nhất

cho đơn giá.

Viết mã cho

nó. Khi tôi nhấp vào

"Nhập" chúng tôi nhận được

tham chiếu mã Python tới

nhận được câu trả lời cho truy vấn của chúng tôi

chỉ trong vài giây.

Bạn có thể sao chép và thực thi

mã cần thiết trong

Sổ tay Jupyter của bạn.

Mã có thể không

có thể sử dụng trực tiếp và bạn

có thể phải chỉnh sửa một vài

tên cột hoặc tên biến.

Bạn có thể xem ở đây

mã đó in

SKU_ID có giá trị cao nhất

giá trị đơn giá trung bình.

Nhưng bạn cũng muốn in

đơn giá trung bình

của SKU_ID này.

Hãy sử dụng lời nhắc này.

Như bạn có thể quan sát, chúng tôi

đã không phải đưa

bối cảnh một lần nữa,

và chúng tôi tiếp tục

trò chuyện với ChatGPT.

Tương tự, bạn có thể

viết lời nhắc tới

lấy mã để

hình dung các tính năng của bạn.

Giả sử bạn muốn

trực quan hóa lưu lượng truy cập trang

và các đơn vị đã bán.

Sau đó bạn phải thử

lời nhắc sau đây.

Vì nó hiển thị ChatGPT

đã tạo ra một mã

chúng ta có thể sử dụng lại trong

Notebook Jupyter của

thay đổi mã này như

theo tên cột.

Nếu tất cả điều này cảm thấy

công việc nặng nhọc còn bạn

muốn toàn bộ khuôn khổ

cho EDA chỉ trong một lần,

tại sao bạn không thử

lời nhắc sau đây.

Bạn đã được ban phước

với mã để

sử dụng lúc đầu

điểm cho EDA của bạn.

Sự kỳ diệu của thế hệ này

Công cụ AI không dừng lại ở đây.

Phiên bản trả phí của ChatGPT,

đó là GPT 4,

cho phép bạn tải lên

Tệp Excel và CSV,

thực hiện EDA và giới thiệu

kết quả đúng

trong cửa sổ trò chuyện.

Tôi sẽ thu thập cuộc trò chuyện mới

ở bên trái và chọn

GPT 4 ở dạng trả phí

phiên bản ChatGPT.

Sau đó tôi có thể chỉ cần tải lên

một tệp CSV hoặc Excel.

Hãy sử dụng lời nhắc, đó là

năm màn trình diễn hàng đầu

SKU_ID dựa trên đơn vị đã bán.

Xây dựng biểu đồ với đơn vị được bán

mỗi SKU_ID trên y

trục và hiển thị nó.

Như bạn có thể thấy, GPT 4 có

tự động hiển thị một

đồ họa đẹp cho bạn.

Hãy thử xây dựng

một hình ảnh khác.

Chúng ta hãy thử lời nhắc sau đây.

Vẽ đồ thị trục kép

với doanh thu trên đơn vị

được bán trên trục y và

ngày hàng tháng trên trục x.

Tổng hợp số liệu hàng tháng

và thêm lưới hàng quý.

Ngoài ra, hãy để doanh thu được thể hiện

theo đường màu đỏ và

đơn vị được bán màu xanh lam.

Vâng, khả năng đọc

của trục này

kém và lưới điện

dòng là đột ngột.

Hãy để chúng tôi cải thiện nó với

lời nhắc sau đây.

Loại bỏ tất cả các đường lưới và

hiển thị ngày trên trục x

cho mỗi quý.

Bây giờ biểu đồ này trông

giống như có chút trống rỗng.

Hãy để chúng tôi hỏi ChatGPT

để thêm dòng lớp

mỗi quý bất cứ ngày nào

có thể nhìn thấy trên trục x.

Bạn thấy phần hay nhất

của GPT 4 là nó

làm mọi thứ như bạn yêu cầu

và cũng cung cấp mã.

Bạn cũng có thể xem

mã và sao chép chúng vào

sổ ghi chép tương ứng của bạn bằng cách

chỉ cần nhấp vào

danh sách thả xuống của Hiển thị công việc.

Một lời nhắc đơn giản như, hãy cho tôi

năm hiểu biết hàng đầu từ

dữ liệu POS sẽ làm nên điều kỳ diệu

dành cho bạn. Chúng ta hãy thử điều này.

Khi đã xong, bạn có thể

xem nó mang lại như thế nào

góc độ khác nhau

để bạn suy nghĩ và thực hiện

toàn bộ idiac

đàm thoại cho bạn.

Đây là cách đơn giản hiện đại

khoa học dữ liệu ngày

nhiệm vụ đã trở thành.

Các công cụ AI sáng tạo như ChatGPT

đã thực sự trở thành một

trụ cột để nâng cao

học tập giữa

người mới học và

nâng cao hiệu quả giữa

các chuyên gia đang làm việc.

Nhưng hãy cẩn thận, hoàn toàn dựa vào

về AI sáng tạo

công cụ mã hóa,

và những đề xuất có thể nguy hiểm,

đặc biệt là cho người mới bắt đầu.

Những công cụ này có xu hướng tạo ra

sai lầm và đưa ra sai lầm

mã và đề xuất.

Sử dụng những công cụ này

yêu cầu một cách hiệu quả

những người đã học và có kinh nghiệm

con mắt của các nhà khoa học dữ liệu,

để họ có thể phán xét

liệu các giải pháp

được trình bày bởi các công cụ như vậy

có đúng hay không.

Điều đó đưa chúng ta đến

kết thúc video này

và bài học này Xem

bạn trong phần tiếp theo.