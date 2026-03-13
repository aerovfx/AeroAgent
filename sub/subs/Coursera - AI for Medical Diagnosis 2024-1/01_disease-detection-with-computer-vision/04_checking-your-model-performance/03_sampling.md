# 03 mẫu

---

Hãy che đậy thứ hai

thách thức của việc lấy mẫu tập hợp.

Giả sử chúng tôi đã lấy mẫu một bài kiểm tra

thiết lập từ tập dữ liệu.

Đôi khi, kích thước của tập kiểm tra là

một phần của tập dữ liệu đầy đủ như 10%.

Những lần khác, trong các nghiên cứu so sánh con người,

bởi vì bộ kiểm tra cần được chú thích

bởi độc giả con người, nút thắt cho

kích thước tập kiểm tra là bao nhiêu ví dụ

độc giả có thể được mong đợi để đọc?

Thông thường, bộ thử nghiệm chứa

ít nhất hàng trăm

ví dụ trong nghiên cứu AI y tế.

Thử thách với việc lấy mẫu bài kiểm tra

thiết lập là khi chúng ta

lấy mẫu ngẫu nhiên một bộ thử nghiệm gồm hàng trăm

các ví dụ từ tập dữ liệu,

chúng tôi có thể không lấy mẫu bất kỳ bệnh nhân nào

thực sự có bệnh.

Ở đây, chúng tôi có thể không lấy mẫu bất kỳ ví dụ nào

trong đó nhãn khối lượng là 1.

Vì vậy, chúng ta sẽ không có cách nào thực sự

kiểm tra hiệu suất của mô hình

về những trường hợp tích cực này.

Đây đặc biệt là một vấn đề với

dữ liệu y tế nơi chúng tôi có thể

đã có một tập dữ liệu nhỏ và

không có nhiều ví dụ về từng bệnh.

Một cách để giải quyết vấn đề này khi tạo

bộ kiểm tra là lấy mẫu một bộ kiểm tra

sao cho chúng ta có ít nhất X%

ví dụ về tầng lớp thiểu số của chúng tôi

Ở đây, tầng lớp thiểu số

đơn giản là lớp học dành cho

mà chúng tôi có một vài ví dụ như ở đây

ví dụ nơi có khối lượng.

Một lựa chọn phổ biến của X là 50%.

Vì vậy, để lấy mẫu một tập dữ liệu gồm 100 ví dụ,

chúng ta sẽ có 50 ví dụ về khối lượng và

50 không có khối lượng.

Điều này đảm bảo rằng nghiên cứu sẽ có

đủ số lượng để có được một ước tính tốt

về hiệu suất của mô hình cả

về các ví dụ không bệnh và về bệnh.

Thông thường, khi chúng tôi lấy mẫu tập kiểm tra,

bộ xác nhận là

lấy mẫu tiếp theo trước khi đào tạo.

Bởi vì chúng tôi muốn xác thực của chúng tôi được đặt thành

phản ánh sự phân bố trong tập kiểm tra,

thông thường, giống nhau

chiến lược lấy mẫu được sử dụng.

Chúng ta có thể quyết định có một lần nữa

100 ví dụ trong bộ xác thực

trong đó 50 là khối lượng và 50 là không khối lượng.

Cuối cùng, những bệnh nhân còn lại có thể

được đưa vào tập huấn luyện.

Bởi vì việc kiểm tra và

bộ xác thực đã được

lấy mẫu nhân tạo để có

một phần lớn các ví dụ đại chúng,

tập huấn luyện sẽ có nhiều

phần nhỏ hơn của các ví dụ về khối lượng.

Bạn đã thấy rằng chúng ta vẫn có thể đào tạo

một mô hình với sự hiện diện của dữ liệu mất cân bằng.

Vì vậy, điều này bao gồm thứ hai của chúng tôi

thách thức của việc lấy mẫu tập hợp.