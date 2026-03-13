# Chương 1. Tại sao học tăng cường sâu Học tăng cường sâu trong thực tế, Phiên bản video

---

Phần 1.6 Tại sao phải học tăng cường sâu

Chúng tôi đã đề xuất học tăng cường, nhưng tại sao lại học tăng cường sâu?

RL đã tồn tại từ rất lâu trước khi học sâu phát triển phổ biến.

Trên thực tế, một số phương pháp sớm nhất mà chúng ta sẽ xem xét cho mục đích học tập,

không liên quan gì hơn là lưu trữ kinh nghiệm trong bảng tra cứu,

ví dụ: từ điển Python,

và cập nhật bảng đó sau mỗi lần lặp của thuật toán.

Ý tưởng là để tác nhân thử nghiệm xung quanh môi trường và xem điều gì đã xảy ra,

và lưu trữ những trải nghiệm của nó về những gì đã xảy ra trong một loại cơ sở dữ liệu nào đó.

Sau một thời gian, bạn có thể nhìn lại cơ sở dữ liệu kiến thức này

và quan sát điều gì hiệu quả và điều gì không.

Không có mạng lưới thần kinh hoặc các thuật toán ưa thích khác.

Đối với những môi trường rất đơn giản, điều này thực sự hoạt động khá tốt.

Ví dụ: trong Tic-Tac-Toe có 255.168 vị trí trên bảng hợp lệ.

Bảng tra cứu, còn được gọi là bảng bộ nhớ, sẽ có nhiều mục,

được ánh xạ từ mỗi trạng thái tới một hành động cụ thể, như trong Hình 1.12,

và phần thưởng được quan sát, không được mô tả.

Trong quá trình đào tạo, thuật toán có thể tìm hiểu hành động nào dẫn đến vị trí thuận lợi hơn

và cập nhật mục đó vào bảng bộ nhớ.

Hình 1.12, bảng tra cứu hành động cho Tic-Tac-Toe chỉ có ba mục,

trong đó người chơi, một thuật toán, chơi X.

Khi người chơi được trao một vị trí trên bàn cờ,

bảng tra cứu chỉ ra nước đi tiếp theo mà họ nên thực hiện.

Sẽ có một mục cho mọi trạng thái có thể có trong trò chơi.

Khi môi trường trở nên phức tạp hơn, việc sử dụng bảng bộ nhớ sẽ trở nên khó khăn.

Ví dụ: mọi cấu hình màn hình của trò chơi điện tử có thể được coi là một trạng thái khác nhau.

Hình 1.13.

Hãy tưởng tượng bạn đang cố gắng lưu trữ mọi kết hợp có thể có của các giá trị pixel hợp lệ được hiển thị trên màn hình trong trò chơi điện tử.

Thuật toán DQN của DeepMind, chơi Atari, được cung cấp 484 x 84 hình ảnh thang độ xám ở mỗi bước,

điều này sẽ dẫn đến 256 lũy thừa của 28.228 trạng thái trò chơi độc đáo,

256 sắc thái khác nhau của màu xám trên mỗi pixel và 4 x 84 x 84 tương đương 28.228 pixel.

Con số này lớn hơn nhiều so với số lượng nguyên tử trong vũ trụ quan sát được

và chắc chắn sẽ không vừa với bộ nhớ máy tính.

Và đây là sau khi hình ảnh được thu nhỏ lại để giảm kích thước

từ hình ảnh màu 210 x 160 pixel ban đầu.

Hình 1.13, một chuỗi ba khung đột phá,

vị trí của quả bóng hơi khác nhau trong mỗi khung hình.

Nếu bạn đang sử dụng bảng tra cứu, điều này tương đương với việc lưu trữ ba mục nhập duy nhất trong bảng.

Bảng tra cứu sẽ không thực tế vì có quá nhiều trạng thái trò chơi cần lưu trữ.

Việc lưu trữ mọi trạng thái có thể là không thể, nhưng chúng ta có thể cố gắng hạn chế các khả năng có thể xảy ra.

Trong quá trình đột phá trò chơi, bạn điều khiển một chiếc mái chèo ở cuối màn hình có thể di chuyển sang phải hoặc sang trái.

Mục tiêu của trò chơi là làm chệch hướng quả bóng và phá vỡ càng nhiều khối ở đầu màn hình.

Trong trường hợp đó, chúng ta có thể xác định các ràng buộc.

Chỉ nhìn vào các trạng thái khi bóng quay trở lại mái chèo,

vì hành động của chúng tôi không quan trọng trong khi chúng tôi chờ bóng ở đầu màn hình.

Hoặc, chúng tôi có thể cung cấp các tính năng của riêng mình.

Thay vì cung cấp hình ảnh thô, chỉ cần cung cấp vị trí của quả bóng, mái chèo và các khối còn lại.

Tuy nhiên, những phương pháp này yêu cầu người lập trình phải hiểu các chiến lược cơ bản của trò chơi,

và họ sẽ không khái quát hóa sang các môi trường khác.

Đó là nơi mà việc học sâu xuất hiện.

Thuật toán học sâu có thể học cách trừu tượng hóa các chi tiết về cách sắp xếp pixel cụ thể,

và có thể tìm hiểu các tính năng quan trọng của một trạng thái.

Vì thuật toán deep learning có số lượng tham số hữu hạn nên

chúng ta có thể sử dụng nó để nén mọi trạng thái có thể thành thứ gì đó mà chúng ta có thể xử lý một cách hiệu quả,

và sau đó sử dụng cách thể hiện mới đó để đưa ra quyết định.

Do sử dụng mạng nơ-ron nên Atari DQN chỉ có 1792 tham số,

mạng nơ ron tích chập với 16 bộ lọc 8x8, 32 bộ lọc 4x4 và lớp ẩn gồm 256 nút được kết nối đầy đủ,

trái ngược với 256 lũy thừa của 28 228 cặp giá trị khóa cần thiết để lưu trữ toàn bộ không gian trạng thái.

Trong trường hợp trò chơi đột phá, mạng lưới thần kinh sâu có thể tự học cách nhận ra các tính năng cấp cao tương tự

một lập trình viên sẽ phải thiết kế thủ công theo cách tiếp cận bảng tra cứu.

Nghĩa là, nó có thể học cách nhìn quả bóng, mái chèo, các khối và nhận biết hướng của quả bóng.

Điều đó khá tuyệt vời vì nó chỉ được cung cấp dữ liệu pixel thô.

Và điều thú vị hơn nữa là các tính năng cấp cao đã học có thể được chuyển sang các trò chơi hoặc môi trường khác.

Học sâu là thứ nước sốt bí mật tạo nên tất cả những thành công gần đây trong RL.

Không có loại thuật toán nào khác chứng minh được sức mạnh biểu diễn, tính hiệu quả và tính linh hoạt của mạng lưới thần kinh sâu.