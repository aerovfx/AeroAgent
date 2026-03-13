# Phụ lục. Học tập tăng cường sâu PyTorch trong thực tế, Phiên bản video

---

A.4 PyTorch

Trong các phần trước, bạn đã học cách sử dụng phương pháp giảm độ dốc để tìm giá trị nhỏ nhất của

một chức năng.

Nhưng để làm được điều đó, chúng tôi cần độ dốc.

Với ví dụ đơn giản của chúng ta, chúng ta có thể tính toán độ dốc bằng giấy và bút chì.

Đối với các mô hình học sâu, điều đó là không thực tế.

Vì vậy, chúng tôi dựa vào các thư viện như PyTorch để cung cấp khả năng phân biệt tự động

điều đó làm cho nó dễ dàng hơn nhiều.

Ý tưởng cơ bản là trong PyTorch chúng ta tạo một biểu đồ tính toán, tương tự như các sơ đồ

chúng tôi đã sử dụng ở phần trước, trong đó mối quan hệ giữa đầu vào, đầu ra và kết nối giữa

các chức năng khác nhau được làm rõ ràng và được theo dõi để chúng ta có thể dễ dàng áp dụng chuỗi

quy tắc tự động để tính toán độ dốc.

May mắn thay, việc chuyển từ NumPy sang PyTorch rất đơn giản và hầu hết chúng ta chỉ có thể

thay thế NumPy bằng Torch.

Hãy dịch mạng lưới thần kinh của chúng ta từ trên cao sang PyTorch.

Liệt kê A.3 Mạng thần kinh PyTorch

Phiên bản này trông gần giống với phiên bản NumPy, ngoại trừ việc chúng tôi sử dụng torch.relu thay vì np.maximum,

nhưng chúng có cùng chức năng.

Chúng tôi cũng đã thêm tham số require_grad=true vào thiết lập ma trận trọng số.

Điều này cho PyTorch biết rằng đây là những tham số có thể huấn luyện mà chúng tôi muốn theo dõi độ dốc

for, trong khi x là đầu vào, không phải là tham số có thể huấn luyện được.

Chúng tôi cũng đã loại bỏ chức năng kích hoạt cuối cùng vì những lý do sẽ trở nên rõ ràng.

Trong ví dụ này, chúng tôi sẽ sử dụng bộ dữ liệu MNIST nổi tiếng có chứa hình ảnh viết tay

các chữ số từ 0 đến 9, chẳng hạn như số trong hình A.2.

Hình A.2, một hình ảnh ví dụ từ tập dữ liệu MNIST gồm các chữ số vẽ tay.

Chúng tôi muốn đào tạo mạng lưới thần kinh của mình để nhận dạng những hình ảnh này và phân loại chúng thành các chữ số 0

qua 9.

PyTorch có một thư viện liên quan cho phép chúng tôi dễ dàng tải xuống tập dữ liệu này.

Liệt kê A.4 Phân loại MNIST bằng mạng thần kinh

Bạn có thể biết rằng mạng lưới thần kinh đang được đào tạo thành công bằng cách quan sát hàm mất mát một cách khá rõ ràng.

giảm dần theo thời gian huấn luyện, hình A.3.

Đoạn mã ngắn này huấn luyện một mạng lưới thần kinh hoàn chỉnh để phân loại thành công MNIST

chữ số với độ chính xác khoảng 70%.

Chúng tôi vừa triển khai tính năng giảm độ dốc giống hệt như cách chúng tôi đã làm với hàm logarit đơn giản của mình.

hàm số f(x) bằng logarit của đại lượng x lũy thừa 4 cộng với x lập phương

cộng thêm 2, nhưng PyTorch đã xử lý độ dốc cho chúng tôi.

Vì độ dốc của các tham số của mạng nơ-ron phụ thuộc vào dữ liệu đầu vào nên mỗi

Khi chúng tôi chạy mạng nơ-ron "chuyển tiếp" với một mẫu hình ảnh ngẫu nhiên mới, độ dốc

sẽ khác.

Vì vậy, chúng tôi chạy mạng lưới thần kinh về phía trước với một mẫu dữ liệu ngẫu nhiên, PyTorch sẽ theo dõi

của các phép tính xảy ra và khi hoàn thành, chúng tôi gọi phương thức lùi ở cuối cùng

đầu ra.

Trong trường hợp này, nó thường là sự mất mát.

Phương pháp lùi sử dụng vi phân tự động để tính toán tất cả độ dốc cho tất cả các biến PyTorch

yêu cầu đặt "_grad=true".

Sau đó, chúng ta có thể cập nhật các tham số mô hình bằng cách sử dụng phương pháp giảm độ dốc.

Chúng tôi gói phần giảm độ dốc thực tế trong ngữ cảnh "torch.no_grad" vì chúng tôi

không muốn nó theo dõi những tính toán này.

Hình A.3, hàm mất mát cho mạng nơron của chúng ta được huấn luyện trên tập dữ liệu MNIST.

Chúng ta có thể dễ dàng đạt được độ chính xác lớn hơn 95% bằng cách cải thiện thuật toán huấn luyện bằng một

phiên bản phức tạp hơn của việc giảm độ dốc.

Trong danh sách A.4, chúng tôi đã triển khai phiên bản giảm độ dốc ngẫu nhiên của riêng mình, phiên bản ngẫu nhiên

một phần vì chúng tôi lấy ngẫu nhiên các tập hợp con từ tập dữ liệu và tính toán độ dốc dựa trên

trên đó, điều này mang lại cho chúng ta những ước tính ồn ào về độ dốc thực với toàn bộ dữ liệu.

PyTorch bao gồm các trình tối ưu hóa tích hợp, trong đó có độ dốc giảm dần ngẫu nhiên, SGD, là một trong số đó.

Giải pháp thay thế phổ biến nhất được gọi là Atom, đây là phiên bản phức tạp hơn của SGD.

Chúng ta chỉ cần khởi tạo trình tối ưu hóa với các tham số mô hình.

Liệt kê A.5 sử dụng trình tối ưu hóa Atom.

Bạn có thể thấy rằng hàm mất mát trong hình A.4 giờ đây mượt mà hơn nhiều với trình tối ưu hóa Atom,

và nó làm tăng đáng kể độ chính xác của bộ phân loại mạng thần kinh của chúng tôi.

Hình A.4, biểu đồ mất mát của mạng nơ-ron được đào tạo trên MNIST với PyTorch tích hợp

trình tối ưu hóa Atom.

Cảm ơn.