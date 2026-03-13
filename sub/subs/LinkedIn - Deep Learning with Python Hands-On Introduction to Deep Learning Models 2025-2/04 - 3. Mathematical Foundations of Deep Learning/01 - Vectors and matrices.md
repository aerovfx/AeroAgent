# 01 - Vectơ và ma trận

---

- [Người hướng dẫn] Trong deep learning, mạng lưới thần kinh

phụ thuộc nhiều vào vectơ và ma trận

để biểu diễn dữ liệu và thực hiện các phép tính.

Hiểu cách chúng hoạt động là rất quan trọng

vì những cấu trúc toán học này là nền tảng của

thông tin được xử lý như thế nào

qua các lớp của mạng.

Vector là một mảng số một chiều.

Trong bối cảnh của mạng lưới thần kinh,

Các vectơ thường được sử dụng để biểu diễn dữ liệu đầu vào, trọng số

và kích hoạt, đó là kết quả đầu ra từ tế bào thần kinh.

Ví dụ: giả sử chúng ta có đầu vào sau

cho một tập dữ liệu ứng dụng cho vay.

Chúng ta có thể biểu diễn mỗi hàng dữ liệu dưới dạng một vectơ

sau khi chuyển đổi dữ liệu phân loại như lớp

và mục đích cho vay đối với các giá trị bằng số.

Mỗi phần tử trong vectơ sẽ tương ứng

đến một tính năng trong dữ liệu đầu vào.

Ma trận là một mảng số hai chiều,

hàng và cột.

Ma trận được sử dụng trong mạng lưới thần kinh

để biểu diễn trọng số giữa các lớp.

Mỗi hàng của ma trận trọng số tương ứng với các trọng số

cho một nơron ẩn.

Bây giờ chúng ta đã xác định được vectơ

và ma trận, hãy xem

cách chúng tương tác trong mạng lưới thần kinh.

Để làm điều này, trước tiên chúng ta sẽ kiểm tra

cách một nút ẩn xử lý đầu vào

sử dụng sản phẩm chấm

của vectơ đầu vào và trọng số của nút ẩn.

Tích vô hướng của hai vectơ là một phép toán

có hai vectơ có độ dài bằng nhau

và trả về một số duy nhất,

mà còn được gọi là vô hướng.

Trong mạng lưới thần kinh,

tích số chấm được sử dụng để tính tổng có trọng số

đầu vào cho một nơ-ron đơn lẻ.

Nếu chúng ta chỉ xem xét một nơron ẩn có một vectơ

của đầu vào X và trọng số W, chúng tôi tính toán kích hoạt của nó,

Z là tích vô hướng của cả hai vectơ.

Tích số chấm được tính

bằng cách nhân các phần tử tương ứng

của hai vectơ với nhau rồi tính tổng các phần.

Ví dụ, với các đầu vào sau

và trọng lượng, tích vô hướng của vectơ W

và X sẽ là 1001,4.

Mặc dù tích số chấm rất hữu ích cho việc tính toán kích hoạt

của một nơ-ron đơn lẻ,

Mạng nơ-ron thường có nhiều nơ-ron trong mỗi lớp.

Chúng ta cần một cách để tính toán kích hoạt

của nhiều nơron cùng một lúc.

Điều này dẫn chúng ta đến phép nhân ma trận.

Phép nhân ma trận hay còn gọi là tích ma trận

là một phép toán có hai ma trận A và B,

và tạo ra ma trận C mới,

trong đó mỗi phần tử là tích vô hướng của một hàng từ A

và một cột từ B.

Để nhân hai ma trận,

số cột trong ma trận đầu tiên phải

bằng số hàng của ma trận thứ hai.

Ma trận kết quả có kích thước bằng số

các hàng của ma trận đầu tiên

và số cột của ma trận thứ hai.

Ở đây chúng ta thấy ma trận 3 x 2 nhân với 2

bằng ma trận 3, dẫn đến ma trận 3 x 3.

Tương tự, cho ma trận trọng số 2 x 3 W

cho hai nút ẩn trong mạng của chúng tôi

và vectơ đầu vào 3 x 1 X,

sản phẩm sẽ là ma trận Z 2 x 1,

đại diện cho việc kích hoạt các đầu vào có trọng số

cho cả hai nút ẩn.

Cho đến nay, chúng tôi đã tóm tắt các yếu tố đầu vào có trọng số

cho mỗi nơ-ron trong lớp ẩn.

Tuy nhiên, trước khi một nút có thể được kích hoạt, chúng ta cũng cần

để thêm độ lệch trước khi truyền tín hiệu

đến chức năng kích hoạt.

Hãy cùng khám phá cách hoạt động của thao tác theo từng phần tử này.

Một hoạt động theo phần tử đề cập đến một hoạt động

được áp dụng riêng cho từng phần tử tương ứng

của hai ma trận hoặc vectơ.

Ngược lại với phép nhân ma trận

hoặc tích chấm, bao gồm việc tính tổng các phần

của nhiều phần tử,

các thao tác theo phần tử hoạt động trực tiếp trên các phần tử,

duy trì hình dạng của ma trận hoặc vectơ đầu vào.

Thực hiện các phép toán theo phần tử trên vectơ

và ma trận là đơn giản.

Tham số thiên vị

của một nút giúp dịch chuyển hàm kích hoạt lên hoặc xuống.

Ví dụ: nếu vectơ thiên vị cho các lớp ẩn là B,

thêm độ lệch vào trọng lượng của một số

của các tế bào thần kinh theo kiểu nguyên tố

cho chúng ta một vectơ khác, Z nguyên tố.

Chức năng kích hoạt giới thiệu phi tuyến tính

vào mạng và cũng được áp dụng theo kiểu từng phần tử.

Giả sử chúng ta đang sử dụng chức năng kích hoạt ReLU

trong các nút ẩn.

Áp dụng chức năng kích hoạt ReLU cho các phần tử

của vectơ Z Prime riêng lẻ đảm bảo một cách hiệu quả

các giá trị âm được đặt

về 0 trong khi các giá trị dương không thay đổi.