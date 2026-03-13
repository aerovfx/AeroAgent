# Chương 3. Tóm tắt Học tập tăng cường sâu trong thực tế, Phiên bản video

---

Bản tóm tắt. Không gian trạng thái là tập hợp tất cả các trạng thái có thể có của môi trường.

Thông thường các trạng thái được mã hóa dưới dạng tensor, do đó không gian trạng thái có thể là vectơ loại R^n hoặc ma trận R^n/m.

Không gian hành động là tập hợp tất cả các hành động có thể xảy ra với một trạng thái.

Ví dụ, không gian hành động của trò chơi cờ vua sẽ là tập hợp tất cả các nước đi hợp lệ trong một trạng thái nào đó của trò chơi.

Giá trị trạng thái là tổng số phần thưởng chiết khấu dự kiến ​​cho một trạng thái nếu chúng tôi tuân theo một số chính sách.

Nếu một trạng thái có giá trị trạng thái cao, điều đó có nghĩa là việc bắt đầu từ trạng thái này có thể sẽ dẫn đến phần thưởng cao.

Giá trị hành động là phần thưởng mong đợi khi thực hiện một hành động ở một trạng thái cụ thể.

Đó là giá trị của một cặp trạng thái-hành động.

Nếu bạn biết các giá trị hành động cho tất cả các hành động có thể xảy ra đối với một trạng thái,

bạn có thể quyết định thực hiện hành động có giá trị hành động cao nhất,

và kết quả là bạn sẽ nhận được phần thưởng cao nhất.

Chức năng chính sách là chức năng ánh xạ trạng thái tới hành động.

Đây là chức năng quyết định hành động nào sẽ được thực hiện với một số trạng thái đầu vào.

Hàm Q là hàm nhận một cặp hành động trạng thái và trả về giá trị hành động.

Q-learning là một hình thức học tăng cường trong đó chúng tôi cố gắng mô hình hóa hàm Q.

Nói cách khác, chúng tôi cố gắng học cách dự đoán phần thưởng mong đợi cho mỗi hành động trong một trạng thái.

Mạng Q sâu, DQN, chỉ đơn giản là nơi chúng tôi sử dụng thuật toán học sâu làm mô hình trong Q-learning.

Học ngoài chính sách là khi chúng ta tìm hiểu một chính sách trong khi thu thập dữ liệu bằng một chính sách khác.

Học theo chính sách là khi chúng ta tìm hiểu một chính sách đồng thời sử dụng chính sách đó để thu thập dữ liệu cho việc học.

Sự quên lãng nghiêm trọng là một vấn đề lớn mà các thuật toán học máy gặp phải khi đào tạo với các lô dữ liệu nhỏ tại một thời điểm.

trong đó dữ liệu mới được học sẽ xóa hoặc làm hỏng thông tin cũ đã được học.

Phát lại kinh nghiệm là một cơ chế cho phép đào tạo hàng loạt các thuật toán học tăng cường

để giảm thiểu sự quên lãng thảm khốc và cho phép đào tạo ổn định.

Mạng mục tiêu là bản sao của DQN chính mà chúng tôi sử dụng để ổn định quy tắc cập nhật cho việc đào tạo DQN chính.