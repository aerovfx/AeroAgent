# Chương 2. Xây dựng mạng lưới với Học tập tăng cường sâu PyTorch trong thực tế, Phiên bản video

---

Phần 2.4 Xây dựng mạng bằng PyTorch

Hiện nay có rất nhiều framework deep learning như TensorFlow, MXNet và PyTorch

có lẽ là phổ biến nhất.

Chúng tôi chọn sử dụng PyTorch cho cuốn sách này vì tính đơn giản của nó.

Nó cho phép bạn viết mã Python có giao diện gốc mà vẫn nhận được tất cả các ưu điểm của một ứng dụng tốt.

khuôn khổ như phân biệt tự động và tối ưu hóa tích hợp.

Chúng tôi sẽ giới thiệu nhanh cho bạn về PyTorch tại đây nhưng chúng tôi sẽ giải thích thêm khi tiếp tục.

Nếu bạn cần tìm hiểu sâu về cơ bản, hãy xem phần phụ lục nơi chúng tôi có thông tin khá chi tiết.

xem xét về học sâu và bao quát kỹ lưỡng hơn về PyTorch.

Nếu bạn cảm thấy thoải mái với mảng đa chiều NumPy, bạn có thể thay thế hầu hết mọi thứ bạn

làm với NumPy với PyTorch.

Ví dụ: ở đây chúng tôi khởi tạo ma trận 2x3 trong NumPy.

Xem mã này.

Và đây là cách bạn khởi tạo ma trận tương tự bằng PyTorch.

Xem mã này.

Mã PyTorch về cơ bản giống với phiên bản NumPy, ngoại trừ trong PyTorch chúng ta gọi là

tensor mảng đa chiều.

Không có gì đáng ngạc nhiên, đây cũng là thuật ngữ được sử dụng trong TensorFlow và các khung công tác khác, vì vậy hãy lấy

quen nhìn thấy các mảng đa chiều được gọi là tensor.

Chúng ta có thể và thực sự đề cập đến thứ tự tensor, về cơ bản là có bao nhiêu thứ nguyên chỉ mục

tensor có.

Điều này hơi khó hiểu vì đôi khi chúng ta nói về chiều của vectơ, theo

trường hợp nào chúng ta đang đề cập đến độ dài của vectơ.

Nhưng khi chúng ta nói về cấp của một tensor, chúng ta muốn nói đến việc nó có bao nhiêu chỉ số.

Một vectơ có một chỉ mục, nghĩa là mọi phần tử có thể được xử lý bằng một giá trị chỉ mục duy nhất,

vì vậy nó gọi tắt là một tensor hoặc viết tắt là một tensor.

Một ma trận có hai chỉ số, một chỉ số cho mỗi chiều nên nó là một tensor hai.

Các tensor bậc cao hơn có thể được gọi là tensor k, trong đó k là bậc, một giá trị không âm

số nguyên.

Mặt khác, một số là tensor bằng 0, còn được gọi là số vô hướng, vì nó có

không có chỉ số.

Mục 2.4.1 Tự động phân biệt

Các tính năng quan trọng nhất của PyTorch mà chúng ta cần mà NumPy không cung cấp là

tự động phân biệt và tối ưu hóa.

Giả sử chúng ta muốn thiết lập một mô hình tuyến tính đơn giản để dự đoán một số dữ liệu quan tâm.

Chúng ta có thể dễ dàng xác định mô hình bằng cách sử dụng cú pháp NumPy thông thường, giống như cú pháp.

Xem mã này.

Bạn chỉ cần cung cấp đối số require_grad bằng true cho các tensor PyTorch mà bạn

muốn tính toán độ dốc và sau đó gọi phương thức lùi trên nút cuối cùng trong

biểu đồ tính toán, sẽ truyền ngược gradient qua tất cả các nút có require_grad

bằng đúng.

Sau đó, bạn có thể thực hiện giảm độ dốc bằng độ dốc được tính toán tự động.

Mục 2.4.2 Xây dựng mô hình

Trong hầu hết cuốn sách này, chúng ta sẽ không bận tâm xử lý trực tiếp các vấn đề được tính toán tự động.

độ dốc.

Thay vào đó, chúng tôi sẽ sử dụng mô-đun nn của PyTorch để dễ dàng thiết lập mạng nơ-ron chuyển tiếp nguồn cấp dữ liệu

mô hình, sau đó sử dụng các thuật toán tối ưu hóa tích hợp để tự động huấn luyện mạng thần kinh

mạng mà không cần phải chỉ định thủ công các cơ chế lan truyền ngược và độ dốc

đi xuống.

Đây là một mạng nơ-ron hai lớp đơn giản với một trình tối ưu hóa được thiết lập.

Xem mã này.

Chúng tôi đã thiết lập mô hình hai lớp với ReLU, các đơn vị tuyến tính được chỉnh lưu, các hàm kích hoạt,

đã xác định hàm mất lỗi bình phương trung bình và thiết lập trình tối ưu hóa.

Tất cả những gì chúng ta phải làm để huấn luyện mô hình này, vì chúng ta có một số dữ liệu huấn luyện được gắn nhãn, là

bắt đầu một vòng đào tạo.

Xem mã này.

Biến x là dữ liệu đầu vào của mô hình.

Biến y_Corr là một tensor biểu thị đầu ra đúng được gắn nhãn.

Chúng tôi đưa ra dự đoán bằng cách sử dụng mô hình, tính toán tổn thất và sau đó tính toán độ dốc bằng cách sử dụng

phương pháp lùi về nút cuối cùng trong biểu đồ tính toán, hầu như luôn luôn

hàm mất mát.

Sau đó, chúng tôi chỉ chạy phương thức bước trên trình tối ưu hóa và nó sẽ chạy một bước chuyển màu

đi xuống.

Nếu chúng ta cần xây dựng các kiến trúc mạng nơ-ron phức tạp hơn mô hình tuần tự, chúng ta

có thể viết lớp Python của riêng chúng ta, kế thừa từ lớp mô-đun của PyTorch và sử dụng lớp đó thay thế.

Xem mã này.

Đó là tất cả những gì bạn cần biết hiện tại về PyTorch để sử dụng nó hiệu quả.

Chúng ta sẽ thảo luận về một số điểm thú vị khác khi đọc hết cuốn sách.