# Chương 3. Cải thiện tính ổn định với mạng mục tiêu Học tăng cường sâu trong thực tế, Phiên bản video

---

Phần 3.4 Cải thiện tính ổn định với mạng mục tiêu

Cho đến nay, chúng tôi đã có thể huấn luyện thành công thuật toán học tăng cường sâu để

tìm hiểu và chơi GridWorld với cả khởi tạo tĩnh xác định và khó hơn một chút

phiên bản mà người chơi được đặt ngẫu nhiên trên bảng mỗi trò chơi.

Thật không may, mặc dù thuật toán dường như học cách chơi nhưng điều đó hoàn toàn có thể xảy ra.

nó chỉ ghi nhớ tất cả các cấu hình bo mạch có thể có, vì không có nhiều cấu hình như vậy

trên bảng 4x4.

Biến thể khó nhất của trò chơi là nơi người chơi, mục tiêu, hố và tường đều được khởi tạo.

ngẫu nhiên mỗi trò chơi, khiến thuật toán khó ghi nhớ hơn nhiều.

Điều này sẽ buộc phải thực hiện một số lượng kiến thức thực tế, nhưng như bạn đã thấy, chúng ta vẫn đang gặp phải

khó khăn khi học biến thể này.

Chúng tôi đang nhận được những âm mưu mất mát rất ồn ào.

Để giúp giải quyết vấn đề này, chúng tôi sẽ thêm một thứ nguyên khác vào quy tắc cập nhật để giúp xử lý trơn tru hơn

các giá trị cập nhật.

Phần 3.4.1 Học tập không ổn định

Một vấn đề tiềm ẩn mà DeepMind đã xác định khi họ xuất bản bài báo Deep Q-Network

là nếu bạn tiếp tục cập nhật các thông số của Q-Network sau mỗi lần di chuyển, bạn có thể gây ra

những bất ổn nảy sinh.

Ý tưởng là vì phần thưởng có thể thưa thớt (chúng tôi chỉ trao phần thưởng đáng kể

khi thắng hoặc thua trò chơi), cập nhật từng bước (trong đó hầu hết các bước không

nhận được bất kỳ phần thưởng đáng kể nào) có thể khiến thuật toán bắt đầu hoạt động thất thường.

Ví dụ: Q-Network có thể dự đoán giá trị cao cho hành động "tăng" trong một số

trạng thái.

Nếu nó di chuyển lên và tình cờ rơi vào mục tiêu và giành chiến thắng, chúng tôi sẽ cập nhật Q-Network thành

phản ánh thực tế là nó đã được thưởng +10.

Tuy nhiên, ván tiếp theo nó cho rằng "lên" là một nước đi thực sự tuyệt vời và dự đoán một

giá trị Q cao, nhưng sau đó nó tăng lên và nhận được phần thưởng -10, vì vậy chúng tôi cập nhật và bây giờ nó nghĩ

Rốt cuộc "lên" không phải là tuyệt vời như vậy.

Rồi một vài ván sau đó tiến lên dẫn tới chiến thắng lần nữa.

Bạn có thể thấy điều này có thể dẫn đến một loại hành vi dao động như thế nào, trong đó dự đoán

Giá trị Q không bao giờ ổn định ở một giá trị hợp lý mà cứ bị giật.

Điều này rất giống với vấn đề quên lãng thảm khốc.

Đây không chỉ là vấn đề lý thuyết.

Đó là điều mà DeepMind đã quan sát được trong quá trình đào tạo của chính họ.

Giải pháp họ nghĩ ra là sao chép Q-Network thành hai bản sao, mỗi bản có

tham số mô hình riêng, Q-Network thông thường và một bản sao được gọi là Mạng mục tiêu, tượng trưng

ký hiệu là Mạng Q-Hat.

Mạng mục tiêu giống hệt với Mạng Q ngay từ đầu, trước bất kỳ khóa đào tạo nào, nhưng

các thông số riêng của nó tụt hậu so với Q-Network thông thường về cách chúng được cập nhật.

Hãy cùng xem lại chuỗi sự kiện với Mạng mục tiêu đang hoạt động.

Chúng tôi sẽ bỏ qua các chi tiết về việc phát lại trải nghiệm.

1.

Khởi tạo Q-Network với các tham số, trọng số, theta_q.

2.

Khởi tạo Mạng mục tiêu dưới dạng bản sao của Mạng Q, nhưng có các tham số riêng biệt

theta_t và đặt theta_t = theta_q.

3.

Sử dụng chiến lược tham lam epsilon với các giá trị Q của Mạng Q để chọn hành động A.

4.

Quan sát phần thưởng và trạng thái mới rt+1 st+1.

5.

Giá trị Q của Mạng mục tiêu sẽ được đặt thành rt+1 nếu tập vừa bị chấm dứt

(tức là trò chơi đã thắng hoặc thua) hoặc tới rt+1+gamma nhân giá trị Q tối đa từ Mục tiêu

Mạng cho trạng thái tiếp theo st+1.

Nếu không, hãy chú ý việc sử dụng Mạng mục tiêu tại đây.

6.

Truyền ngược giá trị Q của Mạng mục tiêu thông qua Mạng Q, không phải Mạng mục tiêu.

7.

Mỗi c số lần lặp, đặt theta_t = theta_q, tức là đặt Mạng mục tiêu

các tham số bằng với các tham số của Q-Network.

Lưu ý từ hình 3.15 rằng lần duy nhất chúng tôi sử dụng Mạng mục tiêu, Q-hat, là để tính toán

Giá trị Q mục tiêu để truyền ngược qua Mạng Q.

Ý tưởng là chúng tôi cập nhật các tham số chính của Q-Network trên mỗi lần lặp đào tạo, nhưng

chúng tôi giảm tác động của các bản cập nhật gần đây đối với việc lựa chọn hành động, hy vọng sẽ cải thiện

sự ổn định.

Hình 3.15.

Đây là tổng quan chung về Q-learning với Mạng mục tiêu.

Đây là phần mở rộng khá đơn giản của thuật toán Q-learning thông thường, ngoại trừ

bạn có Mạng Q thứ hai được gọi là Mạng mục tiêu, có giá trị Q dự đoán được sử dụng

để truyền ngược và huấn luyện Q-Network chính.

Các tham số của Mạng mục tiêu không được đào tạo nhưng chúng được đồng bộ hóa định kỳ

với các tham số của Q-Network.

Ý tưởng là việc sử dụng các giá trị Q của Mạng mục tiêu để huấn luyện Mạng Q sẽ cải thiện

sự ổn định của quá trình đào tạo.

Mã hiện đã hơi dài, với cả tính năng phát lại trải nghiệm và Mạng mục tiêu, vì vậy

chúng ta sẽ chỉ xem xét một phần mã đầy đủ trong cuốn sách này.

Chúng tôi sẽ để bạn kiểm tra kho lưu trữ GitHub của cuốn sách, nơi bạn sẽ tìm thấy tất cả

mã cho chương này.

Đoạn mã sau giống hệt với Liệt kê 3.5, ngoại trừ một vài dòng bổ sung vào phần

Khả năng của Mạng mục tiêu.

Liệt kê 3.7 Mạng mục tiêu.

Mạng mục tiêu chỉ đơn giản là một bản sao bị trễ của DQN chính.

Mỗi mô hình PyTorch có một phương thức state_dict trả về tất cả các tham số được sắp xếp

trong một cuốn từ điển.

Chúng tôi sử dụng mô-đun sao chép tích hợp của Python để sao chép cấu trúc dữ liệu mô hình PyTorch, sau đó

chúng tôi sử dụng phương thức Load_state_dict trên model2 để đảm bảo rằng nó đã sao chép các tham số

của DQN chính.

Tiếp theo, chúng tôi đưa vào vòng huấn luyện đầy đủ, hầu hết giống như Liệt kê 3.5, ngoại trừ

mà chúng tôi sử dụng model2 khi tính toán giá trị hàng đợi tối đa cho trạng thái tiếp theo.

Chúng tôi cũng bao gồm một vài dòng mã để sao chép các tham số từ mô hình chính

đến model2 cứ sau 50 lần lặp.

Liệt kê 3.8 DQN với Mạng mục tiêu và Phát lại trải nghiệm.

Khi chúng tôi vẽ biểu đồ tổn thất cho cách tiếp cận Mạng mục tiêu với Phát lại trải nghiệm, hình 3.16,

chúng tôi vẫn nhận được một biểu đồ mất mát ồn ào, nhưng nó ít ồn ào hơn đáng kể và rõ ràng đang có xu hướng giảm.

Bạn nên thử thử nghiệm các siêu tham số, chẳng hạn như kích thước bộ đệm Phát lại trải nghiệm,

kích thước lô, tần suất cập nhật Mạng mục tiêu và tốc độ học tập.

Hiệu suất có thể khá nhạy cảm với các siêu tham số này.

Hình 3.16, biểu đồ tổn thất DQN sau khi bao gồm Mạng mục tiêu để ổn định quá trình đào tạo.

Điều này cho thấy sự hội tụ đào tạo nhanh hơn nhiều so với khi không có Mạng mục tiêu, nhưng nó có

lỗi tăng đột biến đáng chú ý khi Mạng mục tiêu đồng bộ hóa với DQN chính.

Khi chúng tôi thử nghiệm mô hình được đào tạo trên 1000 trò chơi, chúng tôi nhận thấy tỷ lệ thắng được cải thiện khoảng 3%.

so với đào tạo không có Mạng mục tiêu.

Chúng tôi đang đạt được độ chính xác cao nhất khoảng 95%, mà chúng tôi nghĩ có lẽ là độ chính xác tối đa

do những hạn chế của môi trường này, tức là khả năng xảy ra các trạng thái không thể vượt qua được.

Chúng tôi chỉ đào tạo tối đa 5000 sử thi, trong đó mỗi sử thi là một trò chơi.

Số lượng cấu hình trò chơi có thể có, kích thước của không gian trạng thái, xấp xỉ

16 nhân 15 nhân 14 nhân 13 bằng 43.680, vì có 16 vị trí có thể

tác nhân có thể ở trên lưới 4x4 và sau đó có 15 cấu hình có thể có cho tường, vì

tác nhân và tường không thể chồng lên nhau trong không gian, v.v.

Vì vậy, chúng tôi chỉ lấy mẫu khoảng 5000 chia cho 43.680 bằng 0,11 bằng 11% tổng số

số trạng thái trò chơi có thể bắt đầu.

Nếu mô hình có thể chơi thành công các trò chơi mà nó chưa từng thấy trước đây thì chúng tôi có chút tự tin

nó được khái quát hóa.

Nếu bạn nhận được kết quả tốt với bảng 4x4, bạn nên thử đào tạo một đại lý để

chơi trên bảng 5x5 hoặc lớn hơn bằng cách thay đổi tham số kích thước khi tạo phiên bản GridWorldGame.

Xem mã này.

Mạng DeepQ của DeepMind.

Dù bạn có tin hay không, nhưng trong chương này về cơ bản chúng tôi đã xây dựng Mạng DeepQ (DQN)

DeepMind được giới thiệu vào năm 2015 và đã học cách chơi các trò chơi Atari cũ với hiệu suất siêu phàm

cấp độ.

DQN của DeepMind đã sử dụng chiến lược lựa chọn hành động tham lam, trải nghiệm lại và

một mạng mục tiêu.

Tất nhiên, chi tiết triển khai của chúng tôi là khác nhau, vì chúng tôi đang chơi một trò chơi tùy chỉnh.

GridWorldGame và DeepMind đang đào tạo về pixel thô từ các trò chơi điện tử thực.

Ví dụ: một điểm khác biệt đáng chú ý là họ thực sự nhập bốn khung hình cuối cùng

của một trò chơi vào mạng Q của họ.

Đó là bởi vì một khung hình trong trò chơi điện tử không đủ thông tin để xác định

tốc độ và hướng của các vật thể trong trò chơi, điều này rất quan trọng khi quyết định cái gì

hành động cần thực hiện.

Bạn có thể đọc thêm về các chi tiết cụ thể về DQN của DeepMind bằng cách tìm kiếm bài viết "Human Level" của họ

Kiểm soát thông qua học tập tăng cường sâu".

Một điều cần lưu ý là họ đã sử dụng kiến trúc mạng nơ-ron bao gồm hai cấu trúc tích chập

các lớp theo sau là hai lớp được kết nối đầy đủ.

Trong trường hợp của chúng tôi, chúng tôi đã sử dụng ba lớp được kết nối đầy đủ.

Sẽ là một thử nghiệm đáng giá nếu xây dựng một mô hình với lớp chập và thử

đào tạo nó với GridWorld.

Một lợi thế rất lớn của các lớp chập là chúng độc lập với kích thước của

tensor đầu vào.

Ví dụ: khi chúng tôi sử dụng một lớp được kết nối đầy đủ, chúng tôi phải tạo kích thước đầu tiên

64.

Chúng tôi đã sử dụng ma trận tham số 64 x 164 cho lớp đầu tiên.

Tuy nhiên, lớp tích chập có thể được áp dụng cho dữ liệu đầu vào có độ dài bất kỳ.

Điều này sẽ cho phép bạn huấn luyện một mô hình trên lưới 4 x 4 và xem liệu nó có đủ khái quát không

để có thể chơi trên lưới 5 x 5 hoặc lớn hơn.

Hãy tiếp tục, thử nó!

[KẾT THÚC]