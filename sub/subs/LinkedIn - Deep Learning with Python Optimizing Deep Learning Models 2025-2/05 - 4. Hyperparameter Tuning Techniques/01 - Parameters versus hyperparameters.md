# 01 - Tham số so với siêu tham số

---

- [Người hướng dẫn] Trong học máy và học sâu,

tham số và siêu tham số là những khái niệm cơ bản

đóng vai trò riêng biệt trong thiết kế mô hình,

đào tạo và tối ưu hóa.

Tham số là các biến nội bộ của mô hình

được học từ dữ liệu huấn luyện

trong quá trình đào tạo.

Đây là những giá trị mà mô hình điều chỉnh để phù hợp với dữ liệu

và đưa ra những dự đoán chính xác.

Các thông số không được thiết lập bằng tay.

Thay vào đó, chúng được tối ưu hóa bằng thuật toán học tập

để giảm thiểu hàm mất mát,

đo lường sự khác biệt

giữa dự đoán của mô hình và dữ liệu thực tế.

Ví dụ, hãy xem xét một mô hình hồi quy tuyến tính đơn giản

dự đoán giá nhà dựa trên mét vuông.

Mô hình có thể được biểu diễn bằng phương trình hiển thị ở đây,

trong đó Y là giá nhà dự đoán,

X là tính năng đầu vào theo thước vuông,

W là trọng lượng hoặc độ dốc của đường,

và B, là độ lệch, còn được gọi là điểm chặn Y.

Trong phương trình này, W và B là các tham số.

Trong quá trình huấn luyện, mô hình điều chỉnh W và B

nhằm giảm thiểu tổn thất,

đại diện cho sự khác biệt

giữa giá dự đoán và giá thực tế

trong tập dữ liệu huấn luyện.

Bây giờ hãy xem một ví dụ phức tạp hơn một chút

liên quan đến mạng lưới thần kinh.

Giả sử chúng ta đang xây dựng một mạng lưới thần kinh

để nhận biết chữ số viết tay.

Tập dữ liệu huấn luyện chứa 70.000 hình ảnh

gồm các chữ số viết tay có giá trị từ 0 đến 9.

Mỗi hình ảnh có kích thước 28 x 28 pixel,

dẫn đến 784 tính năng đầu vào cho mỗi hình ảnh.

Mạng lưới thần kinh của chúng ta có thể có kiến trúc

tương tự như cái được hiển thị ở đây,

một lớp đầu vào có 784 nơ-ron, mỗi nơ-ron cho mỗi pixel,

hai lớp ẩn với 512 nơ-ron và 128 nơ-ron,

và một lớp đầu ra có 10 nơ-ron,

một cho mỗi lớp chữ số từ 0 đến 9.

Trong mạng này, các tham số bao gồm

của trọng số và độ lệch.

Mỗi kết nối giữa các tế bào thần kinh có một trọng số liên quan.

Giữa lớp đầu vào và lớp ẩn đầu tiên,

có 784 nhân 512 quả cân.

Giữa lớp ẩn thứ nhất và lớp ẩn thứ hai,

có 512 nhân 128 quả cân.

Cuối cùng, giữa lớp ẩn và lớp đầu ra,

có 128 nhân 10 quả cân.

Mỗi nơ-ron ở lớp ẩn và lớp đầu ra

cũng có một thuật ngữ thiên vị,

vậy có 512 độ lệch trong lớp ẩn đầu tiên,

128 thành kiến trong lớp ẩn thứ hai,

và 10 độ lệch trong lớp đầu ra.

Những trọng số và độ lệch này được điều chỉnh trong quá trình đào tạo

sử dụng thuật toán tối ưu hóa

giống như sự giảm dần độ dốc ngẫu nhiên.

Mục đích là tìm giá trị tối ưu cho các tham số này

làm giảm thiểu hàm mất mát.

Bây giờ chúng ta đã biết tham số là gì,

hãy thảo luận về siêu tham số.

Siêu tham số là cấu hình bên ngoài

thiết lập trước khi quá trình huấn luyện bắt đầu.

Không giống như các thông số mô hình được điều chỉnh

và học trực tiếp từ dữ liệu huấn luyện

trong quá trình đào tạo mô hình,

siêu tham số chi phối hành vi

của thuật toán huấn luyện

và kiến trúc mô hình tổng thể,

nhưng bản thân chúng không được học từ dữ liệu.

Họ thường yêu cầu thử nghiệm và điều chỉnh

để đạt được hiệu suất tối ưu.

Chúng ta cũng có thể nghĩ đến sự khác biệt

giữa các tham số và siêu tham số

trong bối cảnh xây dựng một ngôi nhà.

Các thông số giống như vật liệu dùng trong xây dựng,

gạch, xi măng, gỗ.

Chất lượng và sự sắp xếp của các vật liệu này

quyết định sức mạnh và sự ổn định của ngôi nhà.

Siêu tham số giống như bản thiết kế kiến trúc,

các quyết định thiết kế như số lượng phòng,

cách bố trí, loại móng.

Những quyết định này hướng dẫn cách xây dựng ngôi nhà,

những gì được xác định trước khi bắt đầu xây dựng.

Ví dụ về siêu tham số trong deep learning

bao gồm tốc độ học tập,

xác định kích thước bước trong quá trình cập nhật trọng số.

Cỡ lô, xác định số lượng mẫu được sử dụng

để tính toán độ dốc trong mỗi lần lặp.

Và số lượng kỷ nguyên quyết định

mô hình lặp lại bao nhiêu lần

trên toàn bộ tập dữ liệu trong quá trình đào tạo.

Trong video tiếp theo, chúng ta sẽ khám phá một số tính năng khác

các siêu tham số chính được sử dụng trong học sâu.