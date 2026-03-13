# Chương 7. Dist-DQN trên dữ liệu mô phỏng Học tăng cường sâu trong thực tế, Phiên bản video được dịch

---

Mục 7.6, DIST-DQN trên dữ liệu mô phỏng.

Hãy kiểm tra tất cả các phần cho đến nay bằng phân phối mục tiêu mô phỏng để xem liệu DIST-DQN của chúng tôi có thể học thành công để khớp với phân phối mục tiêu hay không.

Trong Liệt kê 7.9, chúng ta lấy một phân phối thống nhất ban đầu, chạy nó qua DIST-DQN và cập nhật nó bằng cách sử dụng một vectơ tổng hợp gồm hai quan sát phần thưởng.

Liệt kê 7.9, thử nghiệm với dữ liệu mô phỏng.

Mục đích của đoạn mã trước là kiểm tra khả năng của DIST-DQN trong việc tìm hiểu phân bố cho hai mẫu dữ liệu tổng hợp.

Trong dữ liệu tổng hợp của chúng tôi, Hành động 0 được liên kết với phần thưởng là 0 và Hành động 2 được liên kết với phần thưởng là 10.

Chúng tôi hy vọng DIST-DQN biết rằng Trạng thái 1 được liên kết với Hành động 1 và Trạng thái 2 với Hành động 2 và tìm hiểu các phân phối.

Bạn có thể thấy trong Hình 7.17 với vectơ tham số được khởi tạo ngẫu nhiên phân phối dự đoán cho cả ba hành động.

Hãy nhớ rằng chúng tôi đã làm phẳng nó dọc theo chiều Hành động gần như là một phân phối đồng đều, trong khi phân phối mục tiêu đạt mức cao nhất trong Hành động 0, vì chúng tôi chỉ vẽ đồ thị mẫu đầu tiên.

Sau khi đào tạo, dự đoán và phân phối mục tiêu sẽ khá khớp nhau.

Hình 7.17, hình này hiển thị phân phối giá trị Hành động được dự đoán do DIST-DQN chưa qua đào tạo tạo ra và phân phối mục tiêu sau khi quan sát phần thưởng.

Có ba cách phân bổ giá trị Hành động riêng biệt có độ dài 51 phần tử, nhưng ở đây chúng được nối thành một vectơ dài để minh họa sự phù hợp tổng thể giữa dự đoán và mục tiêu.

51 phần tử đầu tiên tương ứng với phân phối giá trị Hành động của hoạt động NOOP, 51 phần tử thứ hai tương ứng với phân phối giá trị Hành động của hành động UP và 51 phần tử cuối cùng tương ứng với phân phối xuống.

Bạn có thể thấy dự đoán là một phân phối hoàn toàn bằng phẳng, đồng nhất cho cả ba hành động, trong khi phân phối mục tiêu có một chế độ, một đỉnh dành cho Hành động 0 và một số đỉnh nhiễu cho hai hành động còn lại.

Mục tiêu là để có được dự đoán phù hợp với phân phối mục tiêu.

Lý do tại sao mạng mục tiêu lại quan trọng như vậy là rất rõ ràng với DIST-DQN.

Hãy nhớ rằng mạng mục tiêu chỉ là bản sao của mô hình chính mà chúng tôi cập nhật sau một thời gian trễ.

Chúng tôi sử dụng dự đoán của mạng mục tiêu để tạo mục tiêu cho việc học, nhưng chúng tôi chỉ sử dụng các tham số mô hình chính để thực hiện giảm độ dốc.

Điều này giúp ổn định quá trình đào tạo vì không có mạng mục tiêu, phân phối mục tiêu sẽ thay đổi sau mỗi lần cập nhật tham số từ độ dốc giảm dần.

Tuy nhiên, việc giảm độ dốc đang cố gắng di chuyển các tham số theo hướng phù hợp hơn với phân phối mục tiêu, do đó, có tính tuần hoàn, do đó không ổn định, có thể dẫn đến phân phối mục tiêu thay đổi đáng kể do sự thay đổi giữa dự đoán của DIST-DQN và phân phối mục tiêu.

Bằng cách sử dụng bản sao có độ trễ của dự đoán DIST-DQN thông qua bản sao có độ trễ của các tham số, đó là mạng mục tiêu.

Phân phối mục tiêu không thay đổi sau mỗi lần lặp và không bị ảnh hưởng ngay lập tức bởi các cập nhật liên tục từ mô hình DIST-DQN chính.

Điều này ổn định đáng kể việc đào tạo.

Nếu bạn giảm tỷ lệ gạch dưới cập nhật xuống 1 và thử huấn luyện, bạn sẽ thấy mục tiêu phát triển thành một thứ hoàn toàn sai.

Bây giờ chúng ta hãy xem cách huấn luyện DIST-DQN.

Liệt kê 7.10, đào tạo DIST-DQN về dữ liệu tổng hợp.

Đồ họa trên cùng trong Hình 7.18 cho thấy mục tiêu và dự đoán từ DIST-DQN hiện khớp gần như chính xác sau khi huấn luyện.

Bạn thậm chí có thể không còn thấy rằng có hai bản phân phối chồng chéo nữa. Nó hoạt động.

Biểu đồ tổn thất ở cuối Hình 7.18 có các mức tăng đột biến mỗi khi mạng mục tiêu được đồng bộ hóa với mô hình chính và phân bổ mục tiêu thay đổi đột ngột, dẫn đến tổn thất cao hơn bình thường tại bước thời gian đó.

Chúng ta cũng có thể xem xét các phân phối đã học cho từng hành động đối với từng mẫu trong lô. Danh sách sau đây cho thấy cách thực hiện việc này.

Hình 7.18, trên cùng các phân phối giá trị hành động được nối cho cả ba hành động sau khi huấn luyện.

Dưới cùng, biểu đồ mất mát theo thời gian đào tạo. Tổn thất cơ bản đang giảm nhưng chúng tôi thấy mức tăng đột biến ngày càng tăng.

Liệt kê 7.11, trực quan hóa sự phân bố giá trị của hành động đã học.

Trong Hình 7.19, bạn có thể thấy rằng trong mẫu đầu tiên, phân bố ở bên trái liên quan đến hành động 0 đã sụp đổ thành phân bố suy biến tại 0, giống như dữ liệu mô phỏng.

Tuy nhiên, hai hành động còn lại vẫn khá đồng đều và không có đỉnh rõ ràng.

Tương tự, trong mẫu thứ hai trong lô, hành động 2, giảm xuống, phân phối là phân phối suy biến ở mức 10, vì dữ liệu cũng suy biến, một chuỗi các mẫu giống hệt nhau và hai hành động còn lại vẫn khá đồng nhất.

Hình 7.19, mỗi hàng chứa các phân bố giá trị hành động cho một trạng thái riêng lẻ và mỗi cột trong một hàng lần lượt là phân bố cho hành động 0, 1 và 2.

Bài kiểm tra DIST-DQN này có hầu hết mọi thứ chúng tôi sẽ sử dụng trong thử nghiệm thực tế với Xa lộ Atari. Chỉ có hai chức năng chúng ta cần trước khi chơi Freeway.

Người ta sẽ xử lý trước các trạng thái được trả về từ môi trường OpenAI Gym. Chúng ta sẽ có một mảng gọn gàng gồm 128 phần tử với các phần tử nằm trong khoảng từ 0 đến 255 và chúng ta sẽ cần chuyển đổi nó thành một tenxơ PyTorch và chuẩn hóa các giá trị nằm trong khoảng từ 0 đến 1 để điều tiết kích thước của độ dốc.

Chúng ta cũng cần một hàm chính sách để quyết định hành động nào sẽ thực hiện dựa trên phân bổ giá trị hành động được dự đoán.

Với quyền truy cập vào phân phối xác suất đầy đủ trên các giá trị hành động, chúng tôi có thể sử dụng các chính sách nhạy cảm với rủi ro phức tạp hơn.

Trong chương này, chúng ta sẽ sử dụng một chính sách đơn giản để chọn các hành động dựa trên giá trị kỳ vọng của chúng, nhằm giữ độ phức tạp ở mức tối thiểu.

Mặc dù chúng ta đang học phân phối xác suất đầy đủ, nhưng chúng ta sẽ chọn các hành động dựa trên giá trị kỳ vọng của chúng, giống như Q-learning thông thường.

Liệt kê 7.12, các trạng thái tiền xử lý và các hành động lựa chọn.

Hãy nhớ lại rằng chúng ta có thể tính giá trị kỳ vọng hoặc giá trị kỳ vọng của một phân bố rời rạc bằng cách đơn giản lấy tích bên trong của tensor hỗ trợ với tensor xác suất.

Chúng tôi thực hiện việc này cho cả ba hành động và chọn hành động có giá trị mong đợi cao nhất.

Sau khi cảm thấy thoải mái với mã ở đây, bạn có thể thử đưa ra một chính sách phức tạp hơn, có thể là chính sách có tính đến phương sai, tức là độ tin cậy của từng phân bổ giá trị hành động.