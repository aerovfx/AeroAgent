# Chương 4. Làm việc với Học tập tăng cường sâu trong phòng tập thể dục OpenAI, Phiên bản video được dịch

---

Phần 4.3, làm việc với OpenAI Gym.

Để minh họa cách hoạt động của các gradient chính sách, chúng tôi đã sử dụng GridWorld làm ví dụ kể từ đó.

nó đã quen thuộc với bạn từ chương trước.

Tuy nhiên, chúng ta nên sử dụng một vấn đề khác để thực sự triển khai thuật toán gradient chính sách,

vừa đa dạng vừa giới thiệu OpenAI Gym.

OpenAI Gym là một bộ môi trường mã nguồn mở với API phổ biến hoàn hảo

để thử nghiệm các thuật toán học tăng cường.

Nếu bạn nghĩ ra một số thuật toán DRL mới, hãy thử nghiệm nó trên một số môi trường trong

Phòng tập thể dục là một cách tuyệt vời để biết được nó hoạt động tốt như thế nào.

Phòng tập thể dục chứa nhiều môi trường từ những môi trường dễ dàng có thể được giải quyết bằng tuyến tính đơn giản

hồi quy hoàn toàn đến những vấn đề đòi hỏi một cách tiếp cận DRL phức tạp,

xem Hình 4.8.

Có các trò chơi, điều khiển robot và các loại môi trường khác.

Có lẽ có điều gì đó trong đó bạn sẽ quan tâm.

Hình 4.8.

Hai môi trường ví dụ được cung cấp bởi môi trường Gym của OpenAI.

OpenAI Gym cung cấp hàng trăm môi trường để kiểm tra các thuật toán học tăng cường của bạn

trên.

OpenAI liệt kê tất cả các môi trường hiện được hỗ trợ trên trang web của mình, liên kết này.

Tại thời điểm viết bài, chúng được chia thành bảy loại.

A Tari, Box 2D, Classic Control, Mujoko, Robotics, Toy Text.

Bạn cũng có thể xem toàn bộ danh sách môi trường từ sổ đăng ký OpenAI trong trình bao Python của mình

với đoạn mã sau.

Liệt kê 4.1, liệt kê các môi trường OpenAI Gym.

Có hàng trăm môi trường để lựa chọn, 797 trong phiên bản 0.9.6.

Thật không may, một số môi trường này yêu cầu giấy phép, Mujoko hoặc các phần phụ thuộc bên ngoài,

Box 2D, Tari và do đó sẽ cần một chút thời gian thiết lập.

Chúng ta sẽ bắt đầu với một ví dụ đơn giản, thăm dò giỏ hàng, Hình 4.9 để tránh những điều không cần thiết

sự phức tạp và giúp chúng tôi viết mã ngay lập tức.

Hình 4.9, ảnh chụp màn hình từ môi trường trò chơi thăm dò ý kiến ​​​​bằng xe đẩy trong OpenAI Gym.

Có một chiếc xe đẩy có thể lăn sang trái hoặc sang phải, phía trên là một chiếc xe đẩy trên một trục quay.

Mục đích là để cân bằng thùng phiếu thẳng đứng trên xe bằng cách cẩn thận di chuyển xe sang trái

hoặc đúng.

Mục 4.3.1, thăm dò giỏ hàng.

Môi trường thăm dò giỏ hàng nằm trong phần Kiểm soát cổ điển của OpenAI và nó có rất

mục tiêu đơn giản.

Đừng để cuộc thăm dò thất bại.

Kiểm tra trò chơi tương đương với việc cố gắng giữ thăng bằng một cây bút chì trên đầu ngón tay của bạn.

Để cân bằng cuộc thăm dò thành công, bạn phải áp dụng đúng số lượng

chuyển động nhỏ, trái và phải của xe đẩy.

Trong môi trường này, chỉ có hai hành động tương ứng với việc thực hiện một cú đẩy nhỏ,

trái hoặc phải.

Trong API OpenAI Gym, các môi trường có không gian hành động riêng biệt đều có các hành động được thể hiện

dưới dạng số nguyên từ 0 đến tổng số hành động cho môi trường cụ thể.

Vì vậy, trong cuộc thăm dò giỏ hàng, các hành động có thể thực hiện là 0 và 1, biểu thị việc đẩy sang trái

hoặc bên phải.

Trạng thái được biểu diễn dưới dạng vectơ có độ dài 4 cho biết vị trí giỏ hàng, giỏ hàng

vận tốc, góc thăm dò và vận tốc thăm dò.

Chúng tôi nhận được phần thưởng cộng thêm một cho mỗi bước mà cuộc thăm dò không kết thúc, điều này xảy ra

khi góc thăm dò lớn hơn 12 độ tính từ tâm hoặc khi vị trí xe đẩy

bên ngoài cửa sổ.

Do đó, mục tiêu của cuộc thăm dò giỏ hàng là tối đa hóa độ dài của tập phim, vì mỗi bước

trả lại phần thưởng tích cực cộng một.

Bạn có thể tìm thêm thông tin trên trang OpenAI Gym GitHub tại liên kết này.

Lưu ý rằng không phải mọi vấn đề tiếp theo đều có trang thông số kỹ thuật đẹp như thăm dò giỏ hàng

có, nhưng chúng tôi sẽ xác định trước phạm vi của vấn đề trong tất cả các chương tiếp theo.

Phần 4.3.2, API phòng tập OpenAI.

OpenAI Gym đã được xây dựng để cực kỳ dễ sử dụng và chỉ có chưa đến một nửa

hàng tá phương pháp mà bạn sẽ thường xuyên sử dụng.

Bạn đã thấy một môi trường trong danh sách 4.1 nơi chúng tôi liệt kê tất cả các môi trường có sẵn.

Một phương pháp quan trọng khác là tạo ra một môi trường.

Liệt kê 4.2, tạo môi trường trong OpenAI Gym.

Và bây giờ, chúng ta sẽ chỉ tương tác với biến NV này.

Chúng ta cần một cách để quan sát trạng thái hiện tại của môi trường và sau đó tương tác với

nó.

Chỉ có hai phương pháp bạn cần để làm điều này.

Liệt kê 4.3, thực hiện một hành động trong thăm dò giỏ hàng.

Phương thức reset khởi tạo môi trường và trả về trạng thái đầu tiên.

Trong ví dụ này, chúng tôi đã sử dụng phương thức mẫu của đối tượng không gian gạch dưới NV.action để

lấy mẫu một hành động ngẫu nhiên

Và đủ rồi, chúng tôi sẽ lấy mẫu các hành động từ một mạng lưới chính sách đã được huấn luyện để đóng vai trò củng cố cho chúng tôi

đại lý học tập.

Sau khi khởi tạo môi trường, chúng ta có thể tự do tương tác với nó thông qua phương thức step.

Phương thức bước trả về 4 biến quan trọng mà vòng đào tạo của chúng tôi cần truy cập để

để chạy.

Tham số đầu tiên, trạng thái, đại diện cho trạng thái tiếp theo sau khi chúng ta thực hiện hành động.

Tham số thứ hai, phần thưởng, là phần thưởng ở bước thời gian đó, dành cho cuộc thăm dò giỏ hàng của chúng tôi

vấn đề là 1 và ít hơn cuộc thăm dò đã thất bại.

Tham số thứ ba, done, là một Boolean cho biết trạng thái cuối có hay không

đã đạt được.

Đối với vấn đề thăm dò giỏ hàng của chúng tôi, điều này sẽ luôn trả về sai cho đến khi cuộc thăm dò ý kiến thất bại, hoặc

chiếc xe đã di chuyển ra ngoài cửa sổ.

Tham số cuối cùng, thông tin, là một từ điển có thông tin chẩn đoán có thể hữu ích

để gỡ lỗi, nhưng chúng tôi sẽ không sử dụng nó.

Đó là tất cả những gì bạn cần biết để thiết lập và vận hành hầu hết các môi trường trong OpenAI Gym.