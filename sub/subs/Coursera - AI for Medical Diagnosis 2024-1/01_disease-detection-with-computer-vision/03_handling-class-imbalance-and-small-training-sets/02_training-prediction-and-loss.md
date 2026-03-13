# 02 tập-dự đoán-thua

---

Trong quá trình huấn luyện, một thuật toán

được hiển thị hình ảnh chụp X-quang ngực

được dán nhãn liệu họ

có chứa khối lượng hay không.

Thuật toán học bằng cách sử dụng

những hình ảnh và nhãn này.

Thuật toán cuối cùng sẽ học

đi từ đầu vào X-quang ngực

để tạo ra đầu ra của việc liệu

tia X chứa khối lượng.

Và thuật toán này có thể

đi theo tên khác nhau.

Bạn có thể đã nghe nói về các điều khoản

thuật toán học sâu

hoặc mô hình hoặc mạng lưới thần kinh hoặc

mạng lưới thần kinh tích chập.

Thuật toán tạo ra một đầu ra

dưới dạng điểm số,

đó là những xác suất mà

hình ảnh chứa một khối lượng.

Vậy xác suất để hình ảnh này

chứa khối lượng được xuất ra là 0,48,

và xác suất cho

hình ảnh này được xuất ra là 0,51.

Khi quá trình đào tạo chưa bắt đầu,

những điểm số này,

những kết quả đầu ra xác suất này không

sẽ phù hợp với nhãn mong muốn.

Giả sử nhãn mong muốn cho

khối lượng là 1 và bình thường là 0.

Và bạn có thể thấy rằng 0,48

khác xa với 1 và

0,51 còn rất xa

nhãn mong muốn là 0.

Và chúng ta có thể đo được lỗi này

bằng cách tính hàm mất mát.

Hàm mất mát đo lỗi

giữa xác suất đầu ra của chúng tôi

và nhãn mong muốn.

Chúng ta sẽ xem sự mất mát này như thế nào

được tính toán đủ sớm.

Sau đó, một bộ ảnh mới và mong muốn

nhãn được trình bày cho thuật toán

khi nó học cách tạo ra điểm số

gần hơn với các nhãn mong muốn theo thời gian.

Lưu ý xác suất đầu ra này như thế nào

đang tiến gần đến 1, và

xác suất đầu ra này

đang tiến gần tới 0.