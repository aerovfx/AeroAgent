# 08 kiến ​​trúc multi-task-loss-dataset-size-and-cnn-architecture

---

Chúng tôi sửa đổi hàm mất

như vậy mà chúng ta nhìn vào

lỗi liên quan

với từng bệnh.

Chúng ta có thể trình bày sự mất mát mới của mình như

tổng số tổn thất trên

nhiều bệnh tật.

Đây được gọi là đa nhãn

mất mát hoặc mất đa nhiệm vụ.

Trong trường hợp này, đây là

sự mất mát đó

chúng tôi nhận được tám ví dụ.

Học kỳ đầu tiên ở đây

đại diện cho sự mất mát

liên kết với

lớp đại chúng sử dụng

xác suất dự đoán này

và sử dụng nhãn này.

Tương tự, ở đây chúng ta có

sự mất mát liên quan đến

lớp viêm phổi đến với

đầu ra mô hình này và nhãn này.

Vì vậy chúng tôi cộng ba

tổn thất cho chúng tôi

bởi sự mất mát cá nhân

thành phần chức năng.

Một sự cân nhắc cuối cùng

là cách chúng ta có thể

giải quyết sự mất cân bằng lớp học

trong cài đặt đa nhiệm.

Một lần nữa, chúng ta có thể áp dụng

sự giảm cân đó

chúng tôi đã đề cập trước đó.

Lần này, chúng tôi không

chỉ có một trọng lượng

liên kết với chỉ

nhãn tích cực và tiêu cực,

nhưng nó dành cho nhãn tích cực

gắn liền với điều đó

lớp cụ thể và

nhãn tiêu cực

liên kết với

nhiệm vụ cụ thể đó

sao cho đối với khối lượng,

sẽ có một sự khác biệt

con đường đến lớp học tích cực

hơn là viêm phổi hoặc phù nề.

Điều này bao gồm giải pháp của họ để

thử thách thứ hai

của việc học tập đa nhiệm.

Chúng ta hãy nhìn vào

thử thách thứ ba mà

là thách thức kích thước tập dữ liệu.

Đối với nhiều y tế

vấn đề hình ảnh,

kiến trúc lựa chọn

là tích chập

mạng lưới thần kinh,

còn được gọi là ConvNet hoặc CNN.

Chúng được thiết kế để xử lý

Hình ảnh 2D như tia X.

Nhưng các biến thể của chúng

cũng rất phù hợp với

xử lý tín hiệu y tế

hoặc hình ảnh y tế 3D

như chụp CT,

cái mà chúng ta sẽ xem xét

vào một tuần tới.

Một số dây thần kinh tích chập

kiến trúc mạng,

chẳng hạn như Khởi đầu,

ResNet, DenseNet,

ResNeXt và Hiệu quảNets

đã được đề xuất và đang

phổ biến rộng rãi ở

phân loại hình ảnh.

Những kiến trúc này được cấu thành

của các khối xây dựng khác nhau.

Trong các vấn đề y tế,

tiêu chuẩn là dùng thử

nhiều mô hình trên

các nhiệm vụ mong muốn

và xem cái nào hoạt động tốt nhất.