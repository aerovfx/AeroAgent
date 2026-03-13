# 09 làm việc với một bộ đào tạo nhỏ

---

Thách thức là tất cả

những kiến trúc này là

đói dữ liệu và lợi ích

từ hàng triệu ví dụ

tìm thấy trong hình ảnh

tập dữ liệu phân loại.

Trong các vấn đề y tế,

làm thế nào chúng ta vẫn có thể nộp đơn

những kỹ thuật này khi chúng ta không

có hàng triệu ví dụ?

Một giải pháp, là

huấn luyện trước mạng.

Ở đây ý tưởng là

đầu tiên có mạng,

nhìn vào những hình ảnh tự nhiên,

và học cách xác định đồ vật

chẳng hạn như chim cánh cụt hoặc mèo,

hoặc chó thì dùng cái này

mạng làm điểm khởi đầu

để học tập ở

nhiệm vụ hình ảnh y tế

bằng cách sao chép qua

đặc điểm đã học.

Mạng sau đó có thể tiếp tục

được đào tạo để nhìn vào

chụp X-quang ngực và xác định

sự hiện diện và

sự vắng mặt của bệnh tật.

Ý tưởng của quá trình này,

đó là khi chúng ta đang học

nhiệm vụ đầu tiên của chúng tôi

xác định mèo hoặc chó,

mạng sẽ học

đặc điểm chung mà

sẽ giúp nó học tập

về nhiệm vụ y tế.

Một ví dụ về điều này,

có thể đó là những tính năng

hữu ích để

xác định các cạnh trên chim cánh cụt,

cũng hữu ích cho

xác định các cạnh trên phổi,

sau đó sẽ hữu ích cho

xác định một số bệnh.

Sau đó, khi chúng tôi chuyển những thứ này

các tính năng cho mạng mới của chúng tôi,

mạng có thể học

nhiệm vụ mới của

giải thích X-quang ngực

với điểm khởi đầu tốt hơn.

Bước đầu tiên này là

được gọi là đào tạo trước,

và bước thứ hai,

được gọi là tinh chỉnh.

Nói chung là được hiểu

rằng các lớp đầu tiên

của mạng,

nắm bắt các tính năng hình ảnh cấp thấp

có thể khái quát hóa một cách rộng rãi,

trong khi các lớp sau

nắm bắt các chi tiết được

cấp độ cao hơn hoặc hơn

cụ thể cho một nhiệm vụ.

Vì vậy, ví dụ,

lớp đầu tiên có thể học

về các cạnh của một vật thể,

và điều này có thể hữu ích cho

giải thích X-quang ngực sau này.

Nhưng các lớp sau

có thể học cách

xác định người đứng đầu

một con chim cánh cụt và có thể không

hữu ích cho ngực

Giải thích tia X.

Vì vậy khi chúng ta tinh chỉnh

mạng lưới trên X-quang ngực,

thay vì tinh chỉnh tất cả

các tính năng chúng tôi đã chuyển giao,

chúng ta có thể đóng băng

đặc điểm đã học

các lớp nông và chỉ

tinh chỉnh các lớp sâu hơn.

Trong thực tế, hai trong số

thiết kế phổ biến nhất

lựa chọn là một,

để tinh chỉnh tất cả các lớp,

và hai, chỉ

tinh chỉnh sau hoặc

lớp cuối cùng và không

tinh chỉnh các lớp trước đó.

Phương pháp đào tạo trước này

và tinh chỉnh,

còn gọi là chuyển

học tập và là

một cách hiệu quả để giải quyết

thách thức kích thước tập dữ liệu nhỏ.