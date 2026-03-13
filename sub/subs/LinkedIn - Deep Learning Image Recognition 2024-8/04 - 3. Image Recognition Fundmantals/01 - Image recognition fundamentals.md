# 01 - Nguyên tắc cơ bản về nhận dạng hình ảnh

---

- Bây giờ chúng ta quay lại vấn đề cơ bản.

Trong phần này, chúng ta sẽ đề cập đến

Nguyên tắc cơ bản về nhận dạng hình ảnh.

Chúng ta sẽ khám phá các nguyên tắc cơ bản của xử lý hình ảnh

sử dụng CNN và chia nhỏ từng phần của quy trình

với những ví dụ rất thực tế.

Vì vậy, đầu tiên, như thường lệ,

chúng ta sẽ tiếp tục và thiết lập môi trường

bằng cách nhập các thư viện cần thiết

như OS, như NumPy, như Matplotlib.

Và sau đó chúng ta sẽ tiếp tục

và tải tập dữ liệu CIFAR-10 nổi tiếng,

trong đó bao gồm 60.000 hình ảnh.

Mỗi hình ảnh là 32 x 32 hình ảnh màu,

trong đó có 10 lớp.

Vì vậy đây là một ví dụ

về cách một số hình ảnh trông như thế nào trong tập dữ liệu của chúng tôi.

Tiếp theo chúng ta sẽ tiếp tục

và hiểu hoạt động tích chập.

Vì vậy, tích chập về cơ bản là áp dụng bộ lọc hoặc hạt nhân

thành đầu vào để tạo bản đồ tương lai.

Điều này giúp phát hiện các đặc điểm khác nhau trong hình ảnh đầu vào

chẳng hạn như các cạnh, kết cấu, v.v.

Chúng ta sẽ tiếp tục và minh họa

hoạt động tích chập trong mã của chúng tôi.

Tiếp theo, chúng ta sẽ đi qua hoạt động gộp.

Hoạt động gộp được sử dụng để giảm

kích thước không gian của đầu vào,

giúp giảm chi phí tính toán

và kiểm soát việc lắp quá mức.

Nói cách khác, chúng tôi không để mô hình ghi nhớ.

Chúng ta sẽ xem qua một ví dụ

cho hoạt động gộp tối đa trong mã.

Vâng, chúng ta sẽ hình dung một kiến trúc CNN đơn giản

để củng cố sự hiểu biết của chúng ta.

Trong phần này, để tóm tắt, chúng ta sẽ đề cập đến những vấn đề cơ bản về CNN,

bao gồm các hoạt động tích chập và gộp,

và chúng ta sẽ minh họa một kiến trúc CNN đơn giản.

Nền tảng này sẽ rất cần thiết

khi chúng ta tiến về phía trước và xây dựng những mô hình phức tạp.

Hãy đi vào mã.

Vì vậy, hãy tiếp tục và mở tệp python 03_01_begin.

Vì vậy, trong tệp Python này, chúng ta sẽ bắt đầu trống

và chúng tôi sẽ dần dần xây dựng nó trong các tập tin tiếp theo.

Vì vậy, như thường lệ, chúng tôi sẽ thực sự tiếp tục

và nhập các thư viện cần thiết.

Chúng tôi sẽ tải tập dữ liệu CIFAR-10 và sau đó chúng tôi sẽ tiếp tục

và vô hiệu hóa GPU cho mục đích của chúng tôi.

Như bạn thấy, chúng tôi đã nhập các thư viện cần thiết.

Chúng tôi đã vô hiệu hóa GPU.

Tiếp theo chúng ta sẽ tiến hành tải dữ liệu

và thực hiện tất cả quá trình xử lý trước như chúng tôi đã làm trước đây.

Được rồi, bây giờ chúng ta đã làm xong việc đó,

chúng tôi đã tải dữ liệu, chúng tôi đã chuẩn hóa nó,

chúng tôi đã chuyển đổi nhãn lớp thành vectơ được mã hóa one_hot,

chúng tôi đã xác định nhãn của tập dữ liệu,

và chỉ để đảm bảo rằng chúng tôi đang in

hình dạng của tập dữ liệu để xác minh

rằng chúng ta đã thực hiện các phép biến đổi chính xác.

Tiếp theo chúng ta sẽ tiếp tục

và bao gồm mã xác định thư mục đầu ra,

xác định thư mục cốt truyện nơi chúng tôi muốn lưu các ô.

Hãy chắc chắn rằng chúng tôi có thư mục đầu ra

và thư mục cốt truyện tồn tại.

Nếu không, hãy tiếp tục và tạo một cái.

Chúng tôi sẽ tiếp tục và hiển thị hình ảnh một lần nữa.

Và sau đó chúng ta sẽ xác định lại tên của hình ảnh,

đó là display_images.

Tiếp theo chúng ta sẽ tiếp tục

và hiển thị một mẫu hình ảnh đào tạo.

Sau khi hiển thị hình ảnh,

chúng ta sẽ tiếp tục và định nghĩa một hàm

để minh họa một kiến trúc CNN đơn giản.

Một lần nữa, chúng ta đã xem xét lại những điều này trước đây,

vì vậy chúng tôi đang sao chép mã

mà chúng ta đã tạo ở các phần trước

và đây là nơi bắt đầu thông tin chính trong phiên này.

Vì vậy chúng ta sẽ tiếp tục và định nghĩa một hàm

để giải thích phép toán tích chập là gì.

Đây thực sự là một trong những khối xây dựng cơ bản của CNN.

Vì vậy tích chập về cơ bản là áp dụng một bộ lọc

hoặc hạt nhân vào đầu vào để tạo bản đồ trong tương lai.

Điều này giúp phát hiện các đặc điểm khác nhau trong hình ảnh đầu vào

chẳng hạn như các cạnh, kết cấu, v.v.

Và đây là hàm tích chập mà chúng tôi đã tạo.

Vì vậy, tiếp theo chúng ta sẽ thảo luận về các hoạt động gộp, được sử dụng

để giảm kích thước đặc biệt của đầu vào,

giúp giảm chi phí tính toán,

điều này rất quan trọng,

và kiểm soát việc lắp quá mức,

điều đó ngăn cản việc ghi nhớ.

Và ở đây chúng ta có ví dụ về hàm gộp.

Chúng tôi tạo một hình ảnh bốn x bốn đơn giản với một kênh duy nhất,

và sau đó chúng tôi áp dụng thao tác gộp tối đa cho việc này,

tạo pool_layer và pull_output.

And then we go ahead and print out the Input Image

và sau đó là Đầu ra gộp tối đa.

Vì vậy, điều này tóm tắt các nguyên tắc cơ bản của chúng tôi về nhận dạng hình ảnh.

Chúng ta hãy tiếp tục và chạy thử.

Bây giờ chúng ta hãy tiếp tục và tìm file python 03_01_end

và hãy thử xem.

Chúng ta sẽ nhận thấy rằng nó sẽ thực hiện thao tác tích chập

và hoạt động tổng hợp,

và nó sẽ đưa ra kết quả cho chúng ta.

Vì vậy, trước tiên chúng ta hãy nhìn vào bộ lọc hình ảnh đầu vào

và đầu ra tích chập,

và sau đó hãy chụp lại điều này trong tâm trí chúng ta

rồi đi giải thích chuyện gì đang thực sự xảy ra ở đây.

Vậy điều đang diễn ra ở đây là phép tích chập

áp dụng bộ lọc cho hình ảnh đầu vào để tạo bản đồ trong tương lai

nêu bật những đặc điểm quan trọng

chẳng hạn như các cạnh, kết cấu, v.v.

Vì vậy, chúng ta hãy tiếp tục và đi qua từng cái một.

Vậy là chúng ta đã có hình ảnh đầu vào.

Đây là một hình ảnh nhỏ 3 x 3 có chứa các giá trị.

Hãy nghĩ về nó như một hình ảnh tỷ lệ xám nhỏ

trong đó mỗi số đại diện cho độ sáng của pixel.

Tiếp theo, chúng ta có bộ lọc.

Đây là một lưới số 2 x 2

rằng chúng ta sẽ lướt qua hình ảnh, nếu điều đó hợp lý.

Vì vậy, bộ lọc giúp xác định các tính năng

giống như các cạnh trong hình ảnh.

Và tất cả hoạt động như thế nào để tạo ra kết quả tích chập này

là bộ lọc di chuyển qua hình ảnh, nhân các giá trị của nó

với các giá trị tương ứng trong hình ảnh

và cộng chúng lại.

Và đây là cách toán học diễn ra

để tạo ra kết quả tích chập,

bao gồm trừ 2, 1, 2 và 1.

Bây giờ chúng ta hãy quay trở lại mã.

Hãy cuộn xuống và tìm thao tác gộp.

Vì vậy, sau đầu ra tích chập,

chúng ta thấy hình ảnh đầu vào và đầu ra tổng hợp tối đa.

Bây giờ chúng ta hãy đi qua và giải thích chi tiết

những gì đang xảy ra trong hoạt động tổng hợp.

Bây giờ chúng ta hãy đi qua hoạt động tổng hợp

và ghé thăm những gì vừa xảy ra ở đây.

Vâng, chúng ta có một hình ảnh đầu vào,

đó là hình ảnh 4 x 4 với một kênh duy nhất.

Và sau đó chúng tôi có một quá trình tổng hợp,

đó là tổng hợp tối đa với cửa sổ 2 x 2,

và bước 2 được áp dụng để giảm kích thước đặc biệt.

Vì vậy, chúng tôi thực sự tìm kiếm hàng trên cùng.

Và ở hàng trên cùng, chúng ta có 1, 2, 1 và 0,

và chúng tôi xem xét giá trị tối đa của điều đó.

Và chúng ta tiếp tục chèn nó vào trên cùng bên trái.

Tiếp theo chúng ta đi và tính toán phía trên bên phải.

Vì vậy, chúng ta nhìn vào 1, 0, 3 và 1,

và sau đó chúng tôi chèn cái này vào phía trên bên phải phía dưới bên trái.

Vậy chúng ta xét 2, 2, 1, 0,

và chúng tôi chèn nó vào phía dưới bên trái.

Và ở phía dưới bên phải,

chúng ta tiếp tục và nhìn vào 0, 0, 1, 3, bằng 3,

và sau đó chúng tôi chèn nó vào phía dưới bên phải.

Vì vậy, đây là kết quả đầu ra.

Hoạt động gộp là quan trọng và tại sao?

Bởi vì nó làm giảm kích thước đặc biệt của đầu vào

giúp giảm chi phí tính toán

và giảm bớt sự phù hợp quá mức.

Đây là bản tóm tắt của phép toán tích chập

và hoạt động tổng hợp giúp máy học của chúng tôi

và các mô hình học sâu.