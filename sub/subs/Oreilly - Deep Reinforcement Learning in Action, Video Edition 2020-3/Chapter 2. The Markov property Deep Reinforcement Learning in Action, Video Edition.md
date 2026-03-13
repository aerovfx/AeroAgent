# Chương 2. Học tập tăng cường sâu trong thực tế thuộc tính Markov, Phiên bản video

---

Phần 2.6 Tài sản Markov

Trong bài toán kẻ cướp theo ngữ cảnh, mạng lưới thần kinh của chúng tôi đã khiến chúng tôi chọn hành động tốt nhất cho một trạng thái mà không cần tham chiếu đến bất kỳ trạng thái nào khác trước đó.

Chúng tôi chỉ cung cấp cho nó trạng thái hiện tại và nó tạo ra phần thưởng mong đợi cho mỗi hành động có thể thực hiện được.

Đây là một thuộc tính quan trọng trong học tăng cường được gọi là thuộc tính Markov.

Một trò chơi hoặc bất kỳ nhiệm vụ điều khiển nào khác thể hiện tính chất Markov được gọi là quá trình ra quyết định Markov, MDP.

Với MDP, chỉ riêng trạng thái hiện tại đã chứa đủ thông tin để lựa chọn các hành động tối ưu nhằm tối đa hóa phần thưởng trong tương lai.

Mô hình hóa nhiệm vụ điều khiển dưới dạng MDP là một khái niệm chính trong học tăng cường.

Mô hình MDP đơn giản hóa đáng kể vấn đề RL vì chúng ta không cần phải tính đến tất cả các trạng thái hoặc hành động trước đó.

Chúng ta không cần có trí nhớ, chúng ta chỉ cần phân tích tình hình hiện tại.

Do đó, chúng ta luôn cố gắng mô hình hóa một vấn đề, ít nhất là gần giống như một quá trình quyết định Markov.

Trò chơi bài Blackjack, còn được gọi là 21, là một MDP vì chúng ta có thể chơi trò chơi thành công chỉ cần biết trạng thái hiện tại của mình,

chúng ta có những quân bài nào và một quân bài ngửa của người chia bài.

Để kiểm tra sự hiểu biết của bạn về tính chất Markov, hãy xem xét từng vấn đề điều khiển hoặc nhiệm vụ quyết định trong danh sách dưới đây và xem liệu nó có tính chất Markov hay không.

Lái xe ô tô.

Quyết định có nên đầu tư vào cổ phiếu hay không.

Lựa chọn phương pháp điều trị y tế cho bệnh nhân.

Chẩn đoán bệnh của bệnh nhân.

Dự đoán đội nào sẽ thắng trong một trận bóng đá.

Chọn con đường ngắn nhất, theo khoảng cách, tới một điểm đến nào đó.

Hướng súng bắn mục tiêu ở xa.

Được rồi, hãy xem bạn đã làm như thế nào. Dưới đây là câu trả lời và giải thích ngắn gọn của chúng tôi.

Lái xe ô tô nói chung có thể được coi là có thuộc tính Markov vì bạn không cần biết chuyện gì đã xảy ra 10 phút trước để có thể lái ô tô của mình một cách tối ưu.

Bạn chỉ cần biết mọi thứ hiện tại đang ở đâu và bạn muốn đi đâu.

Quyết định có nên đầu tư vào một cổ phiếu hay không không đáp ứng các tiêu chí của đặc tính Markov vì bạn muốn biết tình hình hoạt động trong quá khứ của cổ phiếu để đưa ra quyết định.

Việc lựa chọn một phương pháp điều trị y tế dường như có đặc tính Markov vì bạn không cần biết tiểu sử của một người để chọn phương pháp điều trị tốt cho tình trạng bệnh tật của họ lúc này.

Ngược lại, việc chẩn đoán hơn là điều trị chắc chắn sẽ đòi hỏi kiến ​​thức về các trạng thái trong quá khứ.

Việc biết diễn biến lịch sử các triệu chứng của bệnh nhân thường rất quan trọng để đưa ra chẩn đoán.

Dự đoán đội bóng nào sẽ thắng không có thuộc tính Markov vì giống như ví dụ chứng khoán, bạn cần biết thành tích trong quá khứ của các đội bóng để đưa ra dự đoán chính xác.

Việc chọn con đường ngắn nhất tới đích có thuộc tính Markov vì bạn chỉ cần biết khoảng cách đến đích đối với nhiều tuyến đường khác nhau, điều này không phụ thuộc vào những gì đã xảy ra ngày hôm qua.

Nhắm súng để bắn mục tiêu ở xa cũng có thuộc tính Markov vì tất cả những gì bạn cần biết là mục tiêu ở đâu và có lẽ cả các điều kiện hiện tại như tốc độ gió và thông số kỹ thuật của súng.

Bạn không cần biết tốc độ gió của ngày hôm qua.

Chúng tôi hy vọng bạn có thể đánh giá cao rằng đối với một số ví dụ đó, bạn có thể lập luận ủng hộ hoặc phản đối việc nó có tính chất Markov.

Ví dụ: khi chẩn đoán một bệnh nhân, bạn có thể cần biết lịch sử gần đây về các triệu chứng của họ, nhưng nếu điều đó được ghi lại trong hồ sơ bệnh án của họ và chúng tôi coi hồ sơ bệnh án đầy đủ là trạng thái hiện tại của mình thì chúng tôi đã tạo ra thuộc tính Markov một cách hiệu quả.

Đây là một điều quan trọng cần ghi nhớ. Nhiều vấn đề có thể không tự nhiên có tính chất Markov, nhưng chúng ta thường có thể tạo ra nó bằng cách đưa thêm thông tin vào trạng thái.

Deep Q Learning của Deep Mind hay Deep Q Network, thuật toán học cách chơi trò chơi Atari chỉ từ dữ liệu pixel thô và điểm số hiện tại.

Trò chơi Atari có thuộc tính Markov không? Không chính xác.

Trong trò chơi Pac-Man, nếu trạng thái của chúng ta là dữ liệu pixel thô từ khung hình hiện tại, chúng ta sẽ không biết kẻ thù cách đó vài ô đang tiếp cận chúng ta hay di chuyển ra khỏi chúng ta và điều đó sẽ ảnh hưởng mạnh mẽ đến lựa chọn hành động của chúng ta.

Đây là lý do tại sao việc triển khai Deep Mind thực sự có tác dụng trong bốn khung hình cuối cùng của trò chơi, biến một người không phải MDP thành MDP một cách hiệu quả. Với bốn khung hình cuối cùng, đặc vụ có quyền truy cập vào hướng và tốc độ của tất cả người chơi.

Hình 2.8 đưa ra một ví dụ thú vị về quá trình ra quyết định Markov sử dụng tất cả các khái niệm mà chúng ta đã thảo luận cho đến nay. Bạn có thể thấy có một không gian trạng thái ba yếu tố, em bé đang khóc, em bé đang ngủ và em bé đang cười, và một không gian hành động gồm hai yếu tố là nạp và không bú.

Ngoài ra, chúng tôi còn ghi nhận các xác suất chuyển tiếp, là các bản đồ từ một hành động đến xác suất của trạng thái kết quả. Chúng ta sẽ xem xét lại điều này trong phần tiếp theo.

Tất nhiên, trong cuộc sống thực, bạn với tư cách là người đại diện không biết xác suất chuyển đổi là bao nhiêu. Nếu bạn làm vậy, bạn sẽ có một mô hình về môi trường.

Như bạn sẽ tìm hiểu sau, đôi khi một tác nhân có quyền truy cập vào mô hình môi trường, đôi khi thì không.

Trong trường hợp tác nhân không có quyền truy cập vào mô hình, chúng tôi có thể muốn tác nhân của mình tìm hiểu một mô hình môi trường, mô hình này có thể gần đúng với mô hình cơ bản thực sự.

Hình 2.8, sơ đồ MDP đơn giản với ba trạng thái và hai hành động. Ở đây chúng tôi mô hình hóa quá trình ra quyết định nuôi dạy con cái để chăm sóc trẻ sơ sinh.

Nếu trẻ khóc, chúng ta có thể cho ăn hoặc không cho ăn, và có khả năng nào đó trẻ sẽ chuyển sang trạng thái mới và sẽ nhận được phần thưởng -1, +1 hoặc +2 tùy theo mức độ hài lòng của trẻ.