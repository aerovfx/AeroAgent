# 03 bản đồ nhiệt

---

Một thay đổi cuối cùng chúng tôi thực hiện trong

tính toán này là như vậy

chúng tôi chỉ quan tâm

trong các tính năng có

có ảnh hưởng tích cực đến

điểm cho bệnh tim to.

Vì vậy ở đây chỉ cần mở rộng ra

bản đồ bản địa hóa nên chúng tôi

có thể nhìn thấy tất cả các con số

Chúng ta sẽ đặt giá trị âm

số đây,

trong bản đồ định vị tới

số không và số dương

số chúng tôi giữ nguyên.

Điều này đang được áp dụng

hàm ReLu,

tất cả những gì nó đang làm là

quyết định cái nào lớn hơn,

phần tử hoặc số không,

và thiết lập nó thành

mức tối đa của điều đó.

Vì vậy chúng tôi thực hiện sửa đổi đó

đến việc tính toán

bản địa hóa

bản đồ L. Bây giờ, thay vào đó

hơn là nhìn vào bản địa hóa

bản đồ dưới dạng số trên bảng,

chúng ta có thể hình dung nó

sử dụng bản đồ nhiệt.

Một bản đồ nhiệt được tạo ra bằng cách sử dụng

một bản đồ màu dịch

số thành màu sắc.

Trong trường hợp này,

số dương hơn

sắp xuất hiện

tươi sáng và những con số

gần bằng 0 xuất hiện màu đen.

Bản đồ nhiệt được tạo ra tại

độ phân giải thấp vì nó

cùng kích thước với bản đồ không gian

mà chúng ta đã thấy trước đó

là 10 x 10.

Chúng ta thường phải thay đổi kích thước của nó và

thường có một số loại

của nội suy để

điền vào chỗ trống khi

chúng tôi thay đổi kích thước để mang nó

lên đến kích thước của

hình ảnh tia X.

Cuối cùng, bây giờ chúng ta có thể phủ lên

bản đồ nhiệt đã thay đổi kích thước

trên ảnh gốc.

Đôi khi sự minh bạch là

đã thêm vào bản đồ nhiệt,

đôi khi tỷ lệ thuận

đến điểm số

cho lớp học như vậy

bản đồ nhiệt sáng hơn

khi điểm số là

cao hơn và ít hơn nếu không.

Khi chúng ta kết hợp cả hai,

bản đồ nhiệt và hình ảnh tia X,

chúng tôi có lớp phủ này

cho chúng ta thấy nơi

người mẫu đang tìm kiếm

để đưa ra một quyết định cụ thể

cho bệnh tim to trong trường hợp này.

Như vậy chúng ta có thể tính toán

GradCAM cho

tim to bằng cách sử dụng cái này

thủ tục trên ngay cả những hình ảnh mới.

Là phần mở rộng cuối cùng,

nếu mô hình có nhiều

các lớp đầu ra có thể

làm hình mẫu cho ngực của bạn

phân loại tia X,

có một bản đồ nhiệt khác

bạn muốn cho mỗi căn bệnh.

Điều này là do khác nhau

các phần của hình ảnh được

sẽ là dấu hiệu của

bệnh lý khác nhau.

Do đó, GradCAM có thể được mở rộng

đến bất kỳ lớp C nào bằng cách sử dụng

điểm số cụ thể đó cho

lớp yC đó để lấy

trọng lượng cho điều đó

lớp aC cụ thể,

từ đó tạo ra

bản đồ nhiệt cụ thể cuối cùng.

Ở đây chúng tôi có bản đồ nhiệt

được chỉ định cho chứng tim to và phù nề,

cả hai đều là

có mặt trong hình ảnh này.

Vì vậy điều này bao gồm

Phương pháp GradCam cho

hình dung mạng lưới sâu sắc của chúng tôi.

Chúc mừng bạn đã hoàn thành

khóa học thứ ba và cuối cùng

cho chuyên ngành này.

Bây giờ bạn đã bảo hiểm

chi nhánh thứ ba

về y học, điều trị.

Bạn đã tìm hiểu về các công cụ

cho suy luận nhân quả,

nơi chúng tôi chỉ quan sát

chuyện gì xảy ra với

một bệnh nhân nếu họ có

điều trị hay không,

nhưng điều chúng tôi thực sự quan tâm

về sự khác biệt trong

kết quả khi bệnh nhân

được điều trị

so với khi họ không làm như vậy.

Bạn cũng đã tìm hiểu về các công cụ dành cho

trích xuất thông tin

từ văn bản với

các ứng dụng của

trả lời câu hỏi y khoa

và trích xuất nhãn từ văn bản.

Trong Khóa 1, bạn đã học

công cụ học sâu từ

giải thích hình ảnh y tế

và trong Khóa 2,

bạn đã học về máy học

công cụ để làm việc

với dữ liệu có cấu trúc,

bao gồm cả mô hình sinh tồn.

Ở Khóa 3, cuối cùng bạn

đã học về các phương pháp

giải thích những mô hình này

bạn đã xây dựng trong các khóa học đó.

Xin chúc mừng một lần nữa

khi hoàn thành khóa học này.