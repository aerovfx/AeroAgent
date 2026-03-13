# Chương 1. Tôi có thể làm gì với học tăng cường Học tăng cường sâu trong thực tế, Phiên bản video

---

Phần 1.5 Tôi có thể làm gì với việc học tăng cường?

Chúng tôi bắt đầu chương này bằng cách xem xét các khái niệm cơ bản về thuật toán học máy được giám sát thông thường,

chẳng hạn như bộ phân loại hình ảnh, và mặc dù những thành công gần đây trong học tập có giám sát là quan trọng

và việc học có giám sát, hữu ích sẽ không đưa chúng ta tới trí tuệ nhân tạo tổng quát

(AGI).

Cuối cùng, chúng tôi tìm kiếm những cỗ máy học tập có mục đích chung có thể áp dụng cho nhiều vấn đề

với sự giám sát tối thiểu hoặc không có sự giám sát và kho kỹ năng của họ có thể được chuyển giao giữa các lĩnh vực.

Các công ty lớn có nhiều dữ liệu có thể được hưởng lợi từ các phương pháp tiếp cận được giám sát, nhưng các công ty nhỏ hơn

và các tổ chức có thể không có đủ nguồn lực để khai thác sức mạnh của học máy.

Các thuật toán học tập có mục đích chung sẽ tạo sân chơi bình đẳng cho mọi người và

học tăng cường hiện là cách tiếp cận hứa hẹn nhất đối với các thuật toán như vậy.

Nghiên cứu và ứng dụng RL vẫn đang hoàn thiện nhưng đã có nhiều bước phát triển thú vị

trong những năm gần đây.

Nhóm nghiên cứu DeepMind của Google đã cho thấy một số kết quả ấn tượng và thu hút được sự quan tâm quốc tế

chú ý.

Lần đầu tiên là vào năm 2013 với một thuật toán có thể chơi nhiều trò chơi Atari ở mức siêu phàm

cấp độ.

Những nỗ lực trước đây trong việc tạo ra các tác nhân để giải quyết các trò chơi này liên quan đến việc tinh chỉnh cơ bản

thuật toán để hiểu các quy tắc cụ thể của trò chơi, thường được gọi là kỹ thuật tính năng.

Những phương pháp tiếp cận kỹ thuật tính năng này có thể hoạt động tốt cho một trò chơi cụ thể, nhưng chúng không thể

để chuyển bất kỳ kiến thức hoặc kỹ năng nào sang một trò chơi hoặc miền mới.

Thuật toán Deep Q Network (DQN) của DeepMind đủ mạnh để hoạt động trên bảy trò chơi mà không cần

bất kỳ chỉnh sửa nào dành riêng cho trò chơi (xem Hình 1.11).

Nó không có gì khác ngoài các pixel thô từ màn hình làm đầu vào và chỉ được yêu cầu

tối đa hóa điểm số, tuy nhiên thuật toán đã học được cách chơi vượt xa trình độ chuyên gia của con người.

Hình 1.11.

Thuật toán DQN của DeepMind đã học thành công cách chơi bảy trò chơi Atari chỉ với

pixel thô làm đầu vào và điểm của người chơi làm mục tiêu cần tối đa hóa.

Các thuật toán trước đây, chẳng hạn như Deep Blue của IBM, cần được tinh chỉnh để chơi một trò chơi cụ thể.

trò chơi.

Gần đây hơn, thuật toán AlphaGo và AlphaZero của DeepMind đã đánh bại những người chơi giỏi nhất thế giới

tại trò chơi cờ vây của Trung Quốc cổ đại.

Các chuyên gia tin rằng trí tuệ nhân tạo sẽ không thể chơi cờ vây một cách cạnh tranh ở mức

ít nhất một thập kỷ nữa vì trò chơi có những đặc điểm mà thuật toán thường

không xử lý tốt.

Người chơi không biết nước đi tốt nhất để thực hiện ở bất kỳ lượt nào và chỉ nhận được phản hồi

cho hành động của họ khi kết thúc trò chơi.

Nhiều cao thủ tự coi mình là nghệ sĩ hơn là nhà chiến lược tính toán

và mô tả những bước đi chiến thắng là đẹp đẽ hoặc tao nhã.

Với hơn 10 đến 170 vị trí trong hội đồng pháp lý, các thuật toán mạnh mẽ mà IBM

Deep Blue từng thắng cờ vua, điều đó là không khả thi.

AlphaGo đạt được thành tích này phần lớn bằng cách chơi các trò chơi mô phỏng cờ vây hàng triệu lần và

tìm hiểu những hành động nào sẽ tối đa hóa phần thưởng khi chơi tốt trò chơi.

Tương tự như trường hợp Atari, AlphaGo chỉ có quyền truy cập vào thông tin giống như người chơi

sẽ - vị trí các quân cờ trên bàn cờ.

Mặc dù các thuật toán có thể chơi trò chơi tốt hơn con người là rất đáng chú ý nhưng lời hứa và

tiềm năng của RL vượt xa việc tạo ra các bot trò chơi tốt hơn.

DeepMind đã có thể tạo ra một mô hình để giảm 40% chi phí làm mát trung tâm dữ liệu của Google,

một cái gì đó chúng tôi đã khám phá trước đó trong chương này làm ví dụ.

Phương tiện kinh doanh sử dụng RL để tìm hiểu chuỗi hành động nào - tăng tốc, rẽ, phanh,

báo hiệu - dẫn đến hành khách đến đích đúng giờ và học cách

để tránh tai nạn.

Và các nhà nghiên cứu đang đào tạo robot để hoàn thành các nhiệm vụ, chẳng hạn như học cách chạy mà không cần

lập trình các kỹ năng vận động phức tạp.

Nhiều ví dụ trong số này dựa trên thực tế rằng RL là một cái máy.

Nó không phải là một chiếc xe hơi.

Bạn không thể chỉ để một cỗ máy học cách lái ô tô bằng cách thử và sai.

May mắn thay, ngày càng có nhiều ví dụ thành công về việc cho phép học tập

máy móc sử dụng các trình mô phỏng vô hại và khi chúng đã thành thạo trình mô phỏng, hãy để

họ thử phần cứng thực sự trong thế giới thực.

Một ví dụ mà chúng ta sẽ khám phá trong cuốn sách này là giao dịch thuật toán.

Một phần đáng kể của tất cả các giao dịch chứng khoán được thực hiện bằng máy tính với rất ít hoặc không có

đầu vào từ người vận hành con người.

Hầu hết các nhà giao dịch thuật toán này đều được quản lý bởi các quỹ phòng hộ khổng lồ quản lý hàng tỷ đô la.

Tuy nhiên, trong vài năm gần đây, chúng tôi ngày càng nhận thấy sự quan tâm của các nhà giao dịch cá nhân

trong việc xây dựng các thuật toán giao dịch.

Thật vậy, Quantopian cung cấp một nền tảng nơi người dùng cá nhân có thể viết các thuật toán giao dịch

bằng Python và kiểm tra chúng trong môi trường mô phỏng, an toàn.

Nếu các thuật toán hoạt động tốt, chúng có thể được sử dụng để giao dịch tiền thật.

Nhiều nhà giao dịch đã đạt được thành công tương đối nhờ các thuật toán phỏng đoán đơn giản và dựa trên quy tắc.

Tuy nhiên, thị trường chứng khoán rất năng động và không thể đoán trước được, vì vậy thuật toán RL học liên tục có

lợi thế là có thể thích ứng với những thay đổi của điều kiện thị trường trong thời gian thực.

Một vấn đề thực tế mà chúng tôi sẽ giải quyết sớm trong cuốn sách này là vị trí đặt quảng cáo.

Nhiều doanh nghiệp web có được doanh thu đáng kể từ quảng cáo và doanh thu từ

quảng cáo thường gắn liền với số lượng nhấp chuột mà quảng cáo đó có thể thu được.

Có động lực lớn để đặt quảng cáo ở nơi họ có thể tối đa hóa số nhấp chuột.

Tuy nhiên, cách duy nhất để làm điều này là sử dụng kiến thức về người dùng để hiển thị nhiều nhất

quảng cáo phù hợp.

Nhìn chung, chúng tôi không biết đặc điểm nào của người dùng có liên quan đến lựa chọn quảng cáo phù hợp,

nhưng chúng ta có thể sử dụng các kỹ thuật RL để đạt được một số tiến bộ.

Nếu chúng tôi cung cấp cho thuật toán RL một số thông tin có thể hữu ích về người dùng thì chúng tôi sẽ cung cấp những gì

sẽ gọi môi trường hoặc trạng thái của môi trường và yêu cầu nó tối đa hóa số lần nhấp vào quảng cáo,

nó sẽ học cách liên kết dữ liệu đầu vào với mục tiêu của nó và cuối cùng nó sẽ học

quảng cáo nào sẽ tạo ra nhiều nhấp chuột nhất từ một người dùng cụ thể.

[tĩnh]