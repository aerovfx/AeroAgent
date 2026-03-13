# Phụ lục. Học tập tăng cường sâu PyTorch trong thực tế, Phiên bản video.vi

---

A.4 PyTorch Trong các phần trước, bạn đã học

có thể sử dụng phương pháp giảm dần theo

gradient để tìm giá trị cực tiểu của một hàm.

Nhưng để làm được điều đó,

chúng ta cần đạo hàm theo độ dốc.

Với các ví dụ đơn giản, chúng ta có thể tính toán

đạo theo hàm độ dốc bằng giấy và bút chì.

Tuy nhiên, điều đó lại không

khả năng này với các mô hình học sâu.

Vì vậy, chúng tôi dựa vào thư viện như PyTorch để cung cấp khả năng

năng tính đạo hàm tự động, giúp mọi công việc dễ dàng hơn rất nhiều.

Về cơ bản, trong PyTorch, chúng tôi sẽ tạo ra một sơ đồ tính toán tương tự

như sơ đồ chúng ta đã sử dụng trong phần trước, trong đó các mối quan hệ giữa

đầu vào, đầu ra và kết nối giữa các hàm khác nhau có thể được xác định rõ ràng và

theo dõi để chúng ta có thể dễ dàng áp dụng quy tắc tự động chuỗi để tính toán đạo hàm.

May mắn thay, chuyển đổi từ NumPy sang PyTorch rất đơn giản

giản và phần lớn thời gian chúng ta chỉ cần thay thế NumPy bằng Torch.

Chúng ta hãy chuyển đổi mạng

nơ-ron ở trên sang PyTorch.

Liệt kê A.3 Mạng nơ-ron PyTorch Mạng nơ-ron này gần đây

giống như NumPy phiên bản gốc,

ngoại trừ việc chúng ta sử dụng torch.

relu thay vì np.maximum,

Nhưng chúng là một hàm giống nhau.

Chúng tôi cũng đã thêm các tham số require_grad=true

vào ma trận thiết lập.

Điều này cho PyTorch biết đây là những tham số có thể đào tạo mà chúng tôi

muốn theo dõi độ dốc, trong khi x lại là đầu vào, không cần phải có tham số có thể tạo.

Chúng tôi cũng đã loại bỏ chức năng kích hoạt

gần nhất vì những lý do đó sẽ trở nên rõ ràng.

Đối với ví dụ này, chúng tôi sẽ sử dụng bộ dữ liệu nổi MNIST

tiếng bao gồm các hình ảnh về chữ số viết tay từ 0 đến 9, như hình A.2.

Hình A.2, một ví dụ hình ảnh từ

bộ dữ liệu MNIST về chữ viết tay.

Chúng tôi muốn đào tạo mạng nơ-ron của mình để nhận dạng

Những hình ảnh này và phân loại chúng thành các chữ số từ 0 đến 9.

PyTorch có một thư viện trợ giúp liên kết

chúng tôi dễ dàng tải xuống bộ dữ liệu này.

Liệt kê A.4 Phân loại MNIST bằng cách sử dụng mạng nơ-ron Chúng ta

có thể thấy rằng mạng nơ-ron đang được đào tạo thành công bằng cách

quan sát hàm mất giảm khá đều trong suốt thời gian đào tạo, hình A.3.

Đoạn mã ngắn này đào tạo toàn bộ mạng nơ-ron để phân tích

loại thành công MNIST chữ số với khoảng chính xác 70%.

Chúng tôi mới phát triển các bước xuống dốc chính xác theo cùng cách chúng tôi

đã làm hàm lôgarit đơn giản của mình f(x) bằng lôgarit của lượng x mũ

Bốn cộng x lập phương cộng 2, nhưng PyTorch đã xử lý các độ dốc cho chúng tôi.

Thực hiện độ dốc của các tham số phụ thuộc của mạng nơ-ron phụ thuộc vào

đầu vào, mỗi lần chúng tôi chạy "chuyển mạng"

next" with a new image ngẫu nhiên mẫu, độ dốc sẽ khác nhau.

Vì vậy, chúng tôi tiến hành chuyển tiếp mạng với một dữ liệu mẫu

ngẫu nhiên, PyTorch theo dõi các tính năng được phép xảy ra và khi chúng tôi

hoàn tất, chúng tôi gọi phương thức ngược lên đầu ra cuối cùng.

Trong trường hợp này, thường bị mất mát.

Phương pháp ngược lại sử dụng tính năng tự động phân tích được phép để tính toán tất cả

các gradient cho tất cả các PyTorch biến có yêu cầu phải thiết lập "_grad=true".

Sau đó, chúng tôi có thể cập nhật các tham số

số mô hình bằng cách sử dụng bước xuống dốc.

Chúng tôi cung cấp gói thực tế hạ cấp trong bối cảnh

"torch.no_grad" vì chúng tôi không muốn theo dõi các tính năng được phép này.

Hình A.3, chức năng mất mát cho mạng nơ-ron

chúng tôi được đào tạo trên bộ dữ liệu MNIST.

Chúng tôi có thể dễ dàng đạt được độ chính xác cao hơn 95% bằng cách cải tiến kỹ thuật huấn luyện

with version phức tạp hơn của gradient tuyến tính tiếp theo.

Trong danh sách A.4, chúng tôi đã phát triển phiên bản tiếp theo ngẫu nhiên, phần ngẫu nhiên

bởi vì chúng tôi đang ngẫu nhiên lấy các tập tin từ tập dữ liệu và tính toán tuyến tính dựa trên dữ liệu

dữ liệu đó, cung cấp cho chúng tôi tính năng nhiễu của tuyến tiếp theo, thực hiện cung cấp đầy đủ dữ liệu.

PyTorch bao gồm các bộ hợp hóa ưu tiên tối ưu,

trong đó có tuyến ngẫu nhiên tiếp theo, SGD.

Lựa chọn thay thế phổ biến nhất được gọi là

Adam, một phiên bản phức tạp hơn của SGD.

Chúng tôi chỉ cần khởi động tối đa

ưu tiên cho các mô hình tham số.

Danh sách A.5 sử dụng Adam tối ưu hóa.

Bạn có thể tìm thấy các hàm bị mất mát trong cấu hình A.4 hiện nhanh hơn nhiều với bộ tối ưu hóa Adam

và nó làm tăng độ chính xác đáng kinh ngạc của các loại mạng nơ-ron phân tích của chúng tôi.

Hình A.4, chúng tôi đã nhận được biểu đồ mất mát của mạng nơ-ron

đào tạo trên MNIST với bộ tích hợp tối ưu hóa Adam của PyTorch.

Cảm ơn.