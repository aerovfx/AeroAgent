# Chương 3. Dự đoán các trạng thái và hành động tốt nhất Mạng Q sâu Học tập tăng cường sâu trong hành động, Phiên bản video

---

Chương 3 - Dự đoán các trạng thái và hành động tốt nhất - Deep Q-Networks

Chương này bao gồm

Triển khai chức năng Q như một mạng lưới thần kinh

Xây dựng mạng Q sâu bằng PyTorch để chơi GridWorld

Chống lại sự lãng quên thảm khốc bằng tính năng phát lại trải nghiệm

Cải thiện sự ổn định trong học tập với mạng mục tiêu

Trong chương này, chúng ta sẽ bắt đầu cuộc cách mạng học tăng cường sâu.

Deep Q-Networks của Deep Mind, học cách chơi trò chơi Atari.

Chúng tôi sẽ chưa sử dụng trò chơi Atari làm nền tảng thử nghiệm nhưng chúng tôi sẽ xây dựng qua mạng

hệ thống tương tự mà Deep Mind đã làm.

Chúng tôi sẽ sử dụng một trò chơi dựa trên bảng điều khiển đơn giản có tên là GridWorld làm môi trường trò chơi của mình.

GridWorld thực ra là một nhóm trò chơi tương tự nhau, nhưng nhìn chung chúng đều liên quan đến một bảng lưới.

với một người chơi hoặc tác nhân, một ô mục tiêu, mục tiêu và có thể một hoặc nhiều đặc biệt

các ô có thể là rào cản hoặc có thể mang lại phần thưởng tiêu cực hoặc tích cực.

Người chơi có thể di chuyển lên, xuống, sang trái hoặc phải và mục đích của trò chơi là đưa người chơi

đến ô mục tiêu nơi người chơi sẽ nhận được phần thưởng tích cực.

Người chơi không chỉ phải đạt được ô mục tiêu mà còn phải đi theo con đường ngắn nhất,

và họ có thể cần phải vượt qua nhiều chướng ngại vật khác nhau.

Phần 3.1 - Hàm Q

Chúng tôi sẽ sử dụng một công cụ GridWorld rất đơn giản có trong kho GitHub

cho cuốn sách này.

Bạn có thể tải xuống tại liên kết này trong thư mục Chương 3.

Trò chơi GridWorld được mô tả trong Hình 3.1 hiển thị phiên bản đơn giản của GridWorld mà chúng ta sẽ

bắt đầu với.

Chúng tôi sẽ dần dần giải quyết các biến thể khó khăn hơn của trò chơi.

Mục tiêu ban đầu của chúng tôi là đào tạo một đặc vụ DRL để điều hướng bảng GridWorld đến mục tiêu,

theo con đường hiệu quả nhất mọi lúc.

Nhưng trước khi đi quá xa vào vấn đề đó, chúng ta hãy xem lại các thuật ngữ và khái niệm chính trong

chương trước mà chúng ta sẽ tiếp tục sử dụng ở đây.

Hình 3.1 - Đây là một thiết lập trò chơi GridWorld đơn giản.

Đặc vụ A phải di chuyển dọc theo con đường ngắn nhất đến ô mục tiêu, cộng thêm và tránh bị ngã

vào hố, trừ.

Trạng thái là thông tin mà đại lý của chúng tôi nhận được và sử dụng để đưa ra quyết định về

hành động gì để thực hiện.

Đó có thể là pixel thô của trò chơi điện tử, dữ liệu cảm biến từ xe tự hành hoặc,

trong trường hợp của GridWorld, một tensor biểu thị vị trí của tất cả các đối tượng trên lưới.

Chính sách, ký hiệu là pi, là chiến lược mà đại lý của chúng tôi tuân theo khi được cung cấp trạng thái.

Ví dụ: một chính sách trong Blackjack có thể là xem xét ván bài của chúng ta, trạng thái và đánh hoặc

ở lại một cách ngẫu nhiên.

Mặc dù đây có thể là một chính sách tồi tệ nhưng điểm quan trọng cần nhấn mạnh là

chính sách quy định những hành động chúng tôi thực hiện.

Một chính sách tốt hơn là luôn đánh cho đến khi chúng ta có 19.

Phần thưởng là phản hồi mà đại lý của chúng tôi nhận được sau khi thực hiện một hành động, đưa chúng tôi đến một hành động mới

trạng thái.

Đối với một ván cờ, chúng ta có thể thưởng cho tác nhân của mình cộng thêm 1 khi nó thực hiện một hành động dẫn đến

chiếu tướng của người chơi khác và trừ 1 cho một hành động khiến người đại diện của chúng ta bị

đã chiếu hết.

Mọi tiểu bang khác có thể được thưởng 0, vì chúng tôi không biết liệu đại lý sẽ thắng hay

không.

Tác nhân của chúng tôi thực hiện một loạt hành động dựa trên số pi chính sách của nó và lặp lại quy trình này

cho đến khi tập phim kết thúc, qua đó chúng ta nhận được một loạt các trạng thái, hành động và phần thưởng thu được.

Xem hình này.

Chúng tôi gọi tổng trọng số của phần thưởng trong khi tuân theo chính sách từ trạng thái bắt đầu

S1, giá trị của trạng thái đó hoặc giá trị trạng thái.

Chúng ta có thể biểu thị điều này bằng hàm giá trị V pi của S, chấp nhận trạng thái ban đầu và

trả về tổng phần thưởng dự kiến.

Xem biểu hiện này.

Các hệ số w1, w2, v.v., là trọng số chúng tôi áp dụng cho phần thưởng trước khi tính tổng chúng.

Ví dụ: chúng ta thường muốn coi trọng những phần thưởng gần đây hơn là tương lai xa.

phần thưởng.

Tổng có trọng số là một giá trị kỳ vọng, một thống kê phổ biến trong nhiều lĩnh vực định lượng và

nó thường được biểu thị chính xác như thế này.

Đọc dưới dạng phần thưởng mong đợi với chính sách pi và trạng thái bắt đầu S.

Tương tự, có một hàm giá trị hành động, Q pi của S A, chấp nhận trạng thái S và

hành động A và trả về giá trị của việc thực hiện hành động đó với trạng thái đó.

Nói cách khác, phần thưởng mong đợi được cung cấp cho chính sách pi và trạng thái bắt đầu S và lấy

hành động A. Một số thuật toán hoặc cách triển khai RL sẽ sử dụng cái này hoặc cái kia.

Điều quan trọng là, nếu chúng ta dựa trên thuật toán của mình để tìm hiểu các giá trị trạng thái, trái ngược với các giá trị hành động,

chúng ta phải nhớ rằng giá trị của một trạng thái phụ thuộc hoàn toàn vào chính sách của chúng ta, số pi.

Lấy blackjack làm ví dụ, nếu chúng ta ở trong tình trạng có tổng quân bài là 20, và

chúng ta có hai hành động có thể xảy ra, đánh hoặc giữ, giá trị của trạng thái này chỉ cao nếu chúng ta

chính sách nói hãy ở lại khi chúng ta có 20.

Nếu chính sách của chúng tôi nói là trúng khi chúng tôi có 20, chúng tôi có thể sẽ phá sản và thua trò chơi,

vì vậy giá trị của trạng thái đó sẽ thấp.

Nói cách khác, giá trị của một trạng thái tương đương với giá trị của hành động cao nhất được thực hiện trong

trạng thái đó.

[BLANK_AUDIO]