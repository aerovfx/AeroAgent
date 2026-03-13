# Chương 2. Xây dựng mạng lưới với Học tập tăng cường sâu PyTorch trong thực tế, Video Edition.vi

---

Phần 2.4 Xây dựng mạng với PyTorch Hiện nay

nhiều framework học sâu, TensorFlow, MXNet và

PyTorch có lẽ là framework phổ biến nhất.

Chúng tôi chọn sử dụng PyTorch cho

cuốn sách này vì tính đơn giản của nó.

Framework này cho phép bạn viết mã Python trông giống như bản gốc mã và vẫn có tất cả những tính năng này

năng lượng tốt nhất của một framework như tính vi phân tự động và chức năng tối ưu hóa tích hợp.

Chúng tôi sẽ giới thiệu ngắn gọn về PyTorch tại đây, nhưng

chúng tôi sẽ giải quyết các kỹ năng tốt hơn khi chúng tôi tiến hành.

Nếu bạn cần xem lại bài học cơ bản sâu, hãy xem phần phụ lục, nơi chúng tôi

có đánh giá khá chi tiết về học sâu và phạm vi bao quát hơn về PyTorch.

Nếu bạn khai thác NumPy mảng đa chiều, bạn có thể

thay thế hầu hết mọi thứ bạn làm với NumPy bằng PyTorch.

Ví dụ, tại đây chúng tôi khởi động

tạo một ma trận 2x3 trong NumPy.

Xem đoạn mã này.

Và đây là cách bạn khởi tạo

cùng một ma trận với PyTorch.

Xem đoạn mã này.

Mã PyTorch về cơ bản cũng giống như phiên bản NumPy,

Ngoại trừ ở PyTorch, chúng tôi gọi mảng đa chiều là tenxơ.

Không có gì đáng ngạc nhiên, đây cũng là thuật ngữ được sử dụng trong TensorFlow và các khung

khác, vậy nên hãy làm quen với cách gọi mảng đa chiều là tenxơ.

Chúng ta có thể và sẽ tham chiếu đến tenxơ thứ tự

cơ sở là có bao nhiêu chỉ mục chiều mà tenxơ có.

Điều này gây khó chịu vì đôi khi chúng ta nói đến chiều của

Một điều thú vị, trong trường hợp đó, chúng tôi đang nói đến độ dài của.

Nhưng khi chúng ta nói đến thứ tự của một tenxơ,

chúng tôi muốn nói đến một số chỉ mục mà nó có.

Một niềm vui có một mục tiêu, nghĩa là mọi phần tử đều có thể được giải quyết bằng cách

do đó, một mục duy nhất có giá trị nên nó là tenxơ bậc một hoặc tenxơ một để tắt.

Một ma trận có hai chỉ mục, một

cho mỗi chiều nên nó là mười cơ hai.

Tenxơ cấp cao hơn có thể được gọi là

k-tenxơ, trong đó k là bậc, là số nguyên không âm.

Mặt khác, số duy nhất là tenxơ không, còn

được gọi là vô hướng vì nó không có chỉ mục.

Phần 2.4.1 Phân tách tự động Các tính năng quan trọng

Quan trọng nhất của PyTorch mà chúng ta cần và NumPy

không cung cấp tự động phân biệt và ưu tiên tối ưu.

Giả sử chúng tôi muốn thiết lập một tuyến hình

tính toán đơn giản để dự đoán một số dữ liệu quan tâm.

Chúng ta có thể dễ dàng xác định mô-đun

Cấu hình bằng cú pháp NumPy bình thường.

Xem đoạn mã này.

Bạn chỉ cần cung cấp đối số require_grad bằng true cho các tenxơ

PyTorch mà bạn muốn tính toán độ dốc, sau đó gọi phương thức lui

lại ở nút cuối cùng trong biểu đồ tính toán của bạn, điều này sẽ

truyền ngang độ dốc qua tất cả các nút có require_grad bằng true.

Sau đó, bạn có thể thực hiện hạ dốc

gradient với các gradient được tính toán tự động.

Phần 2.4.2 Xây dựng các mô hình trong phần lớn

của cuốn sách này, chúng tôi sẽ không bận tâm đến

xử lý trực tiếp các độ dốc được tự động tính toán.

Thay vào đó, chúng ta sẽ sử dụng mm nn của PyTorch để dễ dàng

thiết lập mô hình mạng nơ-ron cấp trên, sau đó sử dụng các thuật toán

hợp lý hóa tối ưu hóa để tự động huấn luyện mạng nơ-ron mà

không cần phải xác định chỉ định cách thức truyền ngược và độ dốc dốc của thức thức.

Dưới đây là một mạng lưới hai lớp đơn

normal with the setting maxization.

Xem đoạn mã này.

Chúng tôi đã thiết lập một mô hình hai lớp với ReLU,

tính toán tuyến tính các đơn vị, các chức năng kích hoạt,

định nghĩa một phương pháp lỗi sai

trung bình và tối ưu hóa trình thiết lập.

Tất cả những gì chúng tôi phải làm để huấn luyện mô hình này, với điều kiện

Chúng tôi có một số dữ liệu huấn luyện được gắn nhãn, bắt đầu huấn luyện vòng lặp.

Xem mã này.

Biến x là dữ liệu đầu vào của mô hình.

Biến y_ Correct là tenxơ đại diện

cho đầu ra chính xác đã gắn nhãn.

Chúng tôi tạo ra dự đoán bằng cách sử dụng mô hình, tính toán tổng quát

thất bại và sau đó tính toán độ dốc bằng phương pháp ngược lại

nút cuối cùng trong biểu đồ tính toán, gần như luôn luôn có hàm mất.

Sau đó, chúng tôi chỉ cần chạy các bước phương pháp trên tối ưu

ưu tiên hóa và nó sẽ chạy một bước duy nhất của độ dốc tăng dần.

Nếu chúng ta cần xây dựng các mô hình mạng phức tạp hơn các cấu trúc tuần tự, chúng ta có

có thể viết lớp Python của riêng mình, kế thừa từ lớp mô-đun của PyTorch và sử dụng lớp đó để thay thế.

Xem mã này.

Chỉ cần biết về PyTorch như vậy là

bạn đã có thể làm việc hiệu quả với nó rồi.

Chúng tôi sẽ thảo luận về một

nhiều lợi ích khác khi bạn đọc sách.