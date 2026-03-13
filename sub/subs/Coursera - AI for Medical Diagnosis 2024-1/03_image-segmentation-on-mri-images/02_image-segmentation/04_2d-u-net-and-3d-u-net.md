# 04 2d-u-net-và-3d-u-net

---

Bây giờ chúng ta đã đề cập đến 2D và

Phương pháp tiếp cận 3D để phân đoạn,

chúng ta hãy đi sâu vào

các kiến trúc phân đoạn.

Chúng ta sẽ bắt đầu với

kiến trúc phân đoạn.

Chúng tôi sẽ sử dụng tác vụ 2D để xây dựng

đến sự phân đoạn

kiến trúc cho nhiệm vụ 3D.

Một trong những điều nhất

kiến trúc phổ biến

để phân đoạn

đã là U-Net.

U-Net lần đầu tiên được thiết kế cho

phân đoạn hình ảnh y sinh và

đã chứng minh được kết quả tuyệt vời trên

nhiệm vụ theo dõi tế bào.

Điều thú vị về U-Net,

là nó có thể đạt được

kết quả tương đối tốt,

thậm chí với hàng trăm ví dụ.

Kiến trúc U-Net nợ

tên của nó có hình chữ U.

U-Net bao gồm hai

đường dẫn: một đường dẫn hợp đồng,

và một con đường mở rộng.

Con đường hợp đồng là

một mạng tích chập điển hình

như được sử dụng trong hình ảnh

phân loại.

Nó bao gồm lặp đi lặp lại

ứng dụng của

tích chập và

hoạt động tổng hợp.

Hoạt động tích chập ở đây

được gọi là tích chập xuống.

Chìa khóa ở đây là ở chỗ

con đường hợp đồng,

bản đồ đặc trưng của chúng tôi có được

nhỏ hơn về mặt không gian,

đó là lý do tại sao nó

gọi là sự co lại.

Sau đó, có

con đường mở rộng.

Con đường mở rộng trong

một số cách đang làm

điều ngược lại của

đường hợp đồng.

Nó đang lấy đi của chúng tôi

bản đồ tính năng nhỏ

thông qua một loạt các lần lấy mẫu

và các bước tích chập lên để

quay lại bản gốc

kích thước của hình ảnh.

Nó cũng nối các

biểu diễn mẫu tại

mỗi bước với

bản đồ đặc trưng tương ứng

ở con đường co bóp.

Cuối cùng, ở bước cuối cùng,

kiến trúc

xuất ra xác suất

khối u cho mỗi

pixel trong ảnh.

Kiến trúc U-Net

có thể được đào tạo về

cặp đầu vào đầu ra của 2D

các lát cắt theo cách tiếp cận 2D.

Chúng tôi đã bảo hiểm U-Net

cho cách tiếp cận 2D.

Hãy xem chúng ta có gì

có thể làm khi chúng ta có

Các tập con 3D theo cách tiếp cận 3D.

Chúng tôi có thể cung cấp bất kỳ subvolume 3D nào

vào một kiến trúc phân đoạn,

nếu chúng ta có thể thay thế tất cả

các hoạt động 2D với

đối tác 3D của họ.

Đây chính xác là những gì

một phần mở rộng để

U-Net được gọi là

3D U-Net có.

Sự tích chập 2D

trở thành tích chập 3D,

và các lớp tổng hợp 2D

trở thành các lớp tổng hợp 3D.

Sẽ không sao nếu bạn chưa

đã thấy các kết cấu 3D trước đây.

Tất cả những gì quan trọng

hiểu ở đây là

rằng 3D U-Net

cho phép chúng tôi đi vào

tập con 3D và

có được một đầu ra cho

mỗi voxel trong tập

chỉ định

xác suất của một khối u.

3D U-Net có thể được huấn luyện trên

đầu vào và đầu ra âm lượng nhỏ

như một phần của phương pháp 3D.