# Chương 9. Học tập củng cố sâu Q-learning trong thực tế, Phiên bản video đã được dịch

---

Phần 9.2, Học Tập Q Khu Phố.

Bạn có thể tự hỏi liệu có cách nào hiệu quả và nhỏ gọn hơn để thể hiện hành động

và các hành động chung có thể giải quyết vấn đề này về một hành động chung lớn không thực tế

không gian.

Nhưng thật không may, không có cách nào rõ ràng để biểu diễn một hành động bằng cách sử dụng một cách ngắn gọn hơn.

mã hóa.

Hãy thử nghĩ cách bạn có thể giao tiếp một cách rõ ràng, những hành động mà một nhóm đặc vụ đã sử dụng

một con số duy nhất và bạn sẽ nhận ra rằng bạn không thể làm điều đó tốt hơn với một số mũ

số lượng ngày càng tăng.

Tại thời điểm này, Marl có vẻ không thực tế, nhưng chúng ta có thể thay đổi điều đó bằng cách thực hiện một số phép tính gần đúng

đối với chức năng Q hành động chung được lý tưởng hóa này.

Một lựa chọn là nhận ra rằng trong hầu hết các môi trường, chỉ các tác nhân ở gần nhau

sẽ có ảnh hưởng đáng kể lẫn nhau.

Chúng ta không nhất thiết phải lập mô hình hành động chung của tất cả các tác nhân trong môi trường.

Chúng ta có thể ước tính điều này bằng cách chỉ mô hình hóa hành động chung của các tác nhân trong cùng một vùng lân cận.

Theo một nghĩa nào đó, chúng ta chia toàn bộ không gian hành động chung thành một tập hợp các không gian con chồng lên nhau và

chỉ tính giá trị Q cho các không gian con nhỏ hơn nhiều này.

Chúng ta có thể gọi phương pháp này là lân cận Q Learning hoặc không gian con Q Learning, Hình 9.6.

Hình 9.6.

Trong vùng lân cận Marl, mỗi tác nhân có một trường quan sát, FOV hoặc vùng lân cận và nó có thể

chỉ nhìn thấy hành động của các đặc vụ khác trong vùng lân cận này.

Tuy nhiên, nó vẫn có thể nhận được thông tin trạng thái đầy đủ về môi trường.

Bằng cách hạn chế kích thước của vùng lân cận, chúng tôi ngăn chặn sự tăng trưởng theo cấp số nhân của khớp

không gian hành động theo kích thước cố định mà chúng tôi đặt cho vùng lân cận.

Nếu chúng ta có một thế giới lưới đa tác nhân với bốn hành động cho mỗi tác nhân và tổng cộng 100 tác nhân,

không gian hành động chung đầy đủ là 4 được nâng lên lũy thừa 100, đây là một kích thước không thể điều chỉnh được.

Không có máy tính nào có thể tính toán hoặc thậm chí lưu trữ một vectơ lớn như vậy.

Tuy nhiên, nếu chúng ta sử dụng không gian con của không gian tác động chung và đặt kích thước của từng không gian con,

chúng ta tìm lân cận của 3, vậy kích thước của mỗi không gian con là 4 lập phương bằng 64.

Đây là một vectơ lớn hơn nhiều so với một tác nhân duy nhất, nhưng đó chắc chắn là điều chúng tôi

có thể tính toán với.

Trong trường hợp này, nếu chúng tôi tính giá trị Q cho Tác nhân 1, chúng tôi sẽ tìm thấy ba tác nhân gần nhất

trong khoảng cách tới Đặc vụ 1 và xây dựng một hành động chung một vectơ nóng có độ dài 64 cho ba người này

đại lý.

Đó là những gì chúng ta đưa ra cho hàm Q, Hình 9.7.

Vì vậy, đối với mỗi tác nhân trong số 100 tác nhân, chúng tôi sẽ xây dựng các vectơ hành động chung trong không gian con này và sử dụng

chúng để tính giá trị Q cho mỗi tác nhân.

Sau đó, chúng tôi sẽ sử dụng các giá trị Q đó để thực hiện các hành động như bình thường.

Hình 9.7.

Hàm Q lân cận cho Tác nhân J chấp nhận trạng thái hiện tại và vectơ hành động chung

đối với các tác nhân khác trong vùng lân cận hoặc trường nhìn của nó, được ký hiệu là A chứ không phải J. Nó tạo ra

Giá trị Q được chuyển đến hàm chính sách để chọn hành động cần thực hiện.

Hãy viết một số mã giả để biết cách thức hoạt động của nó.

Liệt kê 9.1.

mã giả cho việc học Q lân cận phần 1.

Mã giả trong danh sách 9.1 cho thấy rằng chúng ta cần một hàm nhận tác nhân hiện tại

J và tìm ba hàng xóm gần nhất của nó.

Và sau đó chúng ta cần một chức năng khác sẽ xây dựng hành động chung bằng cách sử dụng ba chức năng gần nhất này.

hàng xóm.

Tại thời điểm này, chúng tôi có một vấn đề khác.

Làm thế nào để chúng ta xây dựng hành động chung khi chưa biết hành động của các tác nhân khác?

Để tính toán các giá trị Q cho Đặc vụ J và từ đó thực hiện hành động, chúng ta cần biết

những hành động mà đặc vụ không phải J đang thực hiện.

Chúng tôi không sử dụng J để biểu thị các đặc vụ không phải là Đặc vụ J, nhưng trong trường hợp này chỉ là đặc vụ gần nhất

hàng xóm.

Tuy nhiên, để tìm ra hành động của các tác nhân không phải J, chúng ta cần tính toán tất cả

giá trị Q của chúng và sau đó có vẻ như chúng ta rơi vào một vòng lặp vô hạn và không bao giờ có được

bất cứ nơi nào.

Để tránh vấn đề này, chúng tôi bắt đầu bằng cách khởi tạo tất cả các hành động cho các tác nhân một cách ngẫu nhiên và

thì chúng ta có thể tính toán các tác động chung bằng cách sử dụng các tác động ngẫu nhiên này.

Nhưng nếu đó là tất cả những gì chúng tôi đã làm, việc sử dụng các hành động chung sẽ không giúp ích được gì nhiều vì chúng mang tính chất ngẫu nhiên.

Trong mã giả trong danh sách 9.2, chúng ta giải quyết vấn đề bằng cách chạy lại quá trình này một vài lần.

lần.

Đó là phạm vi 4M của phần M, trong đó M là một số nhỏ như 5.

Lần đầu tiên chúng tôi chạy cái này, hành động chung sẽ là ngẫu nhiên.

Nhưng sau đó tất cả các tác nhân sẽ thực hiện hành động dựa trên chức năng Q của họ, vì vậy điều thứ hai

thời gian nó sẽ ít ngẫu nhiên hơn một chút.

Và nếu chúng ta tiếp tục làm điều này thêm vài lần nữa thì độ ngẫu nhiên ban đầu sẽ đủ

được pha loãng và chúng ta có thể thực hiện các hành động ở cuối vòng lặp này trong môi trường thực.

Liệt kê 9.2, mã giả cho việc học Q lân cận phần 2.

Danh sách 9.1 và 9.2 cho thấy cấu trúc cơ bản về cách chúng ta sẽ triển khai việc học tập Q lân cận.

Nhưng một chi tiết chúng tôi đã bỏ qua chính xác là làm thế nào để xây dựng không gian hành động chung cho

đại lý lân cận.

Chúng tôi xây dựng một hành động chung từ một tập hợp các hành động riêng lẻ bằng cách sử dụng thao tác sản phẩm bên ngoài

từ đại số tuyến tính.

Cách đơn giản nhất để diễn đạt điều này là thăng cấp một vectơ thông thường thành ma trận.

Ví dụ: chúng ta có một vectơ có độ dài 4 và chúng ta có thể thăng cấp nó thành ma trận 4x1.

Trong PyTorch và NumPy, chúng ta có thể thực hiện việc này bằng phương pháp định hình lại trên tensor.

Ví dụ: tạo một tensor PyTorch với các giá trị 1, 0, 0, 0 và định hình lại nó thành 1x4

ma trận.

Kết quả ta nhận được khi nhân 2 ma trận phụ thuộc vào chiều và thứ tự của chúng

trong đó chúng tôi nhân chúng.

Nếu chúng ta lấy một ma trận dấu hai chấm 1x4 và nhân nó với một ma trận b dấu hai chấm 4x1 khác, thì chúng ta nhận được

kết quả 1x1, là một số vô hướng, một số.

Đây sẽ là tích bên trong của 2 vectơ, được thăng cấp thành ma trận, vì lớn nhất

kích thước được kẹp ở giữa 2 kích thước đơn.

Sản phẩm bên ngoài chỉ là mặt trái của sản phẩm này, trong đó có 2 kích thước lớn ở bên ngoài,

và 2 kích thước đơn nằm ở bên trong, tạo ra tích tensor 4x1, 1x4 bằng

ma trận 4x4.

Nếu chúng ta có 2 đặc vụ trong thế giới lưới với các hành động riêng lẻ, 0, 0, 0, 1, phải và 0, 0, 1, 0,

bên trái, hành động chung của chúng có thể được tính bằng cách lấy tích bên ngoài của các vectơ này.

Đây là cách chúng tôi làm điều đó trong numpy.

Xem mã này.

Kết quả là một ma trận 4x4, với tổng số 16 phần tử như chúng ta mong đợi từ cuộc thảo luận của mình

ở phần trước.

Thứ nguyên của kết quả tích ngoài giữa 2 ma trận là thứ nguyên của a, lần

chiều của b, trong đó a và b là vectơ và dim đề cập đến kích thước, chiều của

vectơ.

Sản phẩm bên ngoài chính là lý do khiến không gian hoạt động chung tăng lên theo cấp số nhân.

Nói chung, chúng ta cần hàm Q của mạng nơ-ron để hoạt động trên các đầu vào là vectơ, vì vậy

vì tích bên ngoài cho chúng ta một kết quả ma trận nên chúng ta chỉ cần làm phẳng nó thành một vectơ.

Xem mã này.

Hy vọng rằng bạn có thể đánh giá cao rằng phương pháp học Q lân cận không phức tạp hơn nhiều

hơn là học Q thông thường.

Chúng ta chỉ cần cung cấp cho nó một đầu vào bổ sung, đó là vectơ hành động chung của mỗi

hàng xóm gần nhất của đại lý.

Hãy tìm hiểu chi tiết bằng cách giải quyết một vấn đề thực sự.