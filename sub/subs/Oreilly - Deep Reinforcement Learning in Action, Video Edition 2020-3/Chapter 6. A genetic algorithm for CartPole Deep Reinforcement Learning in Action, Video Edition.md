# Chương 6. Thuật toán di truyền cho hoạt động Học tăng cường sâu của CartPole, Phiên bản video được dịch

---

Phần 6.3, một thuật toán di truyền cho thăm dò giỏ hàng.

Hãy xem chiến lược tiến hóa này hoạt động như thế nào trong một ví dụ học tăng cường đơn giản.

Chúng tôi sẽ sử dụng một quy trình tiến hóa để tối ưu hóa một nhân viên hỗ trợ chơi cuộc thăm dò giỏ hàng.

Môi trường mà chúng tôi đã giới thiệu trong Chương 4, nơi người đại diện được khen thưởng vì đã giữ cho cuộc thăm dò diễn ra suôn sẻ, Hình 6.7.

Hình 6.7, chúng ta sẽ sử dụng môi trường thăm dò giỏ hàng để kiểm tra tác nhân của mình.

Người đại diện được khen thưởng bằng cách giữ cho cuộc thăm dò ở tư thế thẳng đứng và có thể di chuyển giỏ hàng sang trái hoặc phải.

Chúng ta có thể biểu diễn một tác nhân như một mạng lưới thần kinh gần đúng với chức năng chính sách.

Nó chấp nhận một trạng thái và đưa ra một hành động, hay điển hình hơn là phân phối xác suất cho các hành động.

Danh sách sau đây cho thấy một ví dụ về mạng ba lớp.

Liệt kê 6.5, định nghĩa một tác nhân.

Hàm trong danh sách 6.5 xác định mạng nơ-ron ba lớp.

Hai lớp đầu tiên sử dụng các hàm kích hoạt đơn vị tuyến tính đã được chỉnh lưu và lớp cuối cùng sử dụng hàm kích hoạt log softmax,

để chúng tôi lấy xác suất nhật ký của các hành động làm đầu ra cuối cùng.

Lưu ý rằng hàm này yêu cầu trạng thái đầu vào, x và các tham số gạch dưới chưa được đóng gói, là một bộ gồm các ma trận tham số riêng lẻ được sử dụng trong mỗi lớp.

Để làm cho quá trình tái tổ hợp và đột biến trở nên dễ dàng hơn, chúng ta sẽ tạo một tập hợp các vectơ tham số, một tensor, sau đó chúng ta phải giải nén hoặc phân tách thành các ma trận tham số riêng lẻ để sử dụng trong mỗi lớp của mạng lưới thần kinh.

Liệt kê 6.6, giải nén một vectơ tham số.

Hàm trước lấy vectơ tham số phẳng làm đầu vào tham số và đặc tả của các lớp mà nó chứa làm đầu vào lớp, đây là danh sách các bộ dữ liệu.

Nó giải nén vectơ tham số thành một tập hợp các ma trận lớp riêng lẻ và các vectơ thiên vị được lưu trong danh sách.

Bộ mặc định cho các lớp chỉ định mạng thần kinh ba lớp, do đó bao gồm ba ma trận trọng số, với các kích thước 25 lần 4, 10 lần 25 và 2 lần 10 và ba vectơ thiên vị có kích thước, 1 lần 25, 1 lần 10 và 1 lần 2, tổng cộng là 4 lần 25,

cộng 25, cộng 10 nhân 25, cộng 10, cộng 2 nhân 10, cộng 2, bằng 407 tham số trong vectơ tham số phẳng.

Lý do duy nhất khiến chúng tôi thêm sự phức tạp này bằng cách sử dụng vectơ tham số phẳng và giải nén chúng để sử dụng là vì chúng tôi muốn có thể biến đổi và kết hợp lại toàn bộ tập hợp tham số, kết quả là về tổng thể sẽ đơn giản hơn và khớp với những gì chúng tôi đã làm với chuỗi.

Một cách tiếp cận khác là coi mạng lưới thần kinh của mỗi lớp như một nhiễm sắc thể riêng lẻ, nếu bạn nhớ về mặt sinh học.

Chỉ những nhiễm sắc thể phù hợp mới kết hợp lại.

Sử dụng phương pháp này, bạn sẽ chỉ kết hợp lại các tham số từ cùng một lớp.

Điều này sẽ ngăn thông tin từ các lớp sau làm hỏng các lớp trước đó.

Chúng tôi khuyến khích bạn thử triển khai nó bằng cách sử dụng phương pháp tiếp cận nhiễm sắc thể này như một thử thách khi bạn cảm thấy thoải mái với cách chúng tôi thực hiện ở đây.

Bạn sẽ cần lặp lại từng lớp, kết hợp lại và biến đổi chúng một cách riêng biệt.

Tiếp theo, hãy thêm một hàm để tạo một tập hợp các tác nhân.

Liệt kê 6.7, sinh ra một quần thể.

Mỗi tác nhân sẽ là một từ điển Python đơn giản lưu trữ vectơ tham số cho tác nhân đó và điểm phù hợp cho tác nhân đó.

Tiếp theo, chúng ta triển khai hàm sẽ kết hợp lại hai tác nhân mẹ để tạo ra hai tác nhân con mới.

Liệt kê 6.8, tái tổ hợp di truyền.

Hàm này có hai tác nhân đóng vai trò là cha mẹ và sinh ra hai đứa con hoặc con cái.

Nó thực hiện điều này bằng cách lấy một điểm phân chia hoặc điểm giao nhau ngẫu nhiên, sau đó lấy phần đầu tiên của phần cha mẹ và kết hợp nó với phần thứ hai của phần cha mẹ hai, và tương tự như vậy, kết hợp phần thứ hai của phần cha mẹ một và phần đầu tiên của phần cha mẹ hai.

Đây chính xác là cơ chế tương tự mà chúng ta đã sử dụng để kết hợp lại các chuỗi trước đây.

Đó là giai đoạn đầu tiên để tạo ra thế hệ tiếp theo.

Giai đoạn thứ hai là biến đổi các cá thể với xác suất khá thấp.

Đột biến là nguồn thông tin di truyền mới duy nhất ở mỗi thế hệ.

Sự kết hợp lại chỉ xáo trộn xung quanh thông tin đã tồn tại.

Liệt kê 6.9, làm thay đổi các vectơ tham số.

Về cơ bản, chúng tôi tuân theo quy trình tương tự như chúng tôi đã làm với chuỗi.

Chúng tôi thay đổi ngẫu nhiên một vài phần tử của vectơ tham số.

Tham số tốc độ đột biến kiểm soát số lượng phần tử mà chúng ta thay đổi.

Chúng ta cần kiểm soát tỷ lệ đột biến một cách cẩn thận để cân bằng giữa việc tạo ra thông tin mới có thể được sử dụng để cải thiện các giải pháp hiện có và việc hủy bỏ thông tin cũ.

Tiếp theo, chúng ta cần đánh giá mức độ phù hợp của từng tác nhân bằng cách thực sự thử nghiệm chúng trên môi trường, thăm dò giỏ hàng trong trường hợp của chúng ta.

Liệt kê 6.10, kiểm tra từng tác nhân trong môi trường.

Hàm mô hình gạch dưới kiểm tra lấy một tác nhân, một từ điển của vectơ tham số và giá trị phù hợp của nó rồi chạy nó trong môi trường thăm dò giỏ hàng cho đến khi nó thua trò chơi và trả về số bước thời gian mà nó kéo dài làm điểm số.

Chúng tôi muốn tạo ra những đại lý có thể tồn tại ngày càng lâu hơn trong cuộc thăm dò giỏ hàng, từ đó đạt được điểm cao.

Chúng ta cần làm điều này cho tất cả các tác nhân trong quần thể.

Liệt kê 6.11, đánh giá tất cả các tác nhân trong tổng thể.

Hàm đánh giá tổng thể gạch dưới sẽ lặp lại qua từng tác nhân trong quần thể và chạy thử nghiệm mô hình gạch dưới trên chúng để đánh giá mức độ phù hợp của chúng.

Hàm chính cuối cùng mà chúng ta cần là hàm tạo dấu gạch dưới tiếp theo trong danh sách 6.12.

Không giống như thuật toán di truyền chuỗi của chúng tôi trước đó, nơi chúng tôi lựa chọn cha mẹ theo xác suất dựa trên điểm số thể lực của họ, ở đây chúng tôi sử dụng một cơ chế lựa chọn khác.

Cơ chế lựa chọn xác suất tương tự như cách chúng ta chọn hành động trong phương pháp gradient chính sách và nó hoạt động tốt ở đó.

Nhưng việc chọn bố mẹ trong thuật toán di truyền thường dẫn đến sự hội tụ nhanh chóng của cả hai.

Các thuật toán di truyền đòi hỏi nhiều sự khám phá hơn so với các phương pháp dựa trên độ dốc.

Trong trường hợp này, chúng tôi sẽ sử dụng cơ chế lựa chọn có tên là Lựa chọn phong cách giải đấu, Hình 6.8.

Hình 6.8. Trong Lựa chọn giải đấu, chúng tôi đánh giá mức độ phù hợp của tất cả các cá thể trong quần thể như thường lệ và sau đó chúng tôi chọn một tập hợp con ngẫu nhiên của toàn bộ quần thể.

Trong hình này, chỉ hai trong số bốn, sau đó chọn những cá thể hàng đầu, thường là hai, trong tập hợp con này, khiến chúng sinh ra con cái và biến đổi chúng.

Chúng tôi lặp lại quá trình lựa chọn này cho đến khi có đủ thế hệ tiếp theo.

Trong Lựa chọn phong cách giải đấu, chúng tôi chọn một tập hợp con ngẫu nhiên từ toàn bộ quần thể, sau đó chọn hai cá thể hàng đầu trong tập hợp con này làm bố mẹ.

Điều này đảm bảo rằng chúng tôi không phải lúc nào cũng chọn cùng hai đại diện cha mẹ hàng đầu, nhưng cuối cùng chúng tôi lại chọn những đại lý hoạt động tốt hơn thường xuyên hơn.

Chúng ta có thể thay đổi Quy mô Giải đấu, quy mô của tập hợp con ngẫu nhiên, để kiểm soát mức độ mà chúng ta ưu tiên lựa chọn những tác nhân tốt nhất trong thế hệ hiện tại, trước nguy cơ mất đi sự đa dạng di truyền.

Trong trường hợp cực đoan, chúng tôi có thể đặt Kích thước giải đấu bằng với quy mô của quần thể, trong trường hợp đó chúng tôi sẽ chỉ chọn hai cá thể đứng đầu trong quần thể.

Ở một thái cực khác, chúng tôi có thể tạo ra Quy mô Giải đấu 2 để chúng tôi chọn ngẫu nhiên phụ huynh.

Trong ví dụ này, chúng tôi đặt Quy mô giải đấu theo phần trăm quy mô dân số.

Theo kinh nghiệm, Quy mô giải đấu khoảng 20% ​​dường như hoạt động khá tốt.

Liệt kê 6.12, tạo ra thế hệ tiếp theo.

Hàm tạo dấu gạch dưới tiếp theo sẽ tạo một danh sách các chỉ số ngẫu nhiên để lập chỉ mục cho danh sách tổng thể và tạo một tập hợp con cho Lô giải đấu.

Chúng tôi sử dụng hàm liệt kê để theo dõi vị trí chỉ mục của từng tác nhân trong tập hợp con, nhờ đó chúng tôi có thể tham khảo lại chúng trong tập hợp chính.

Sau đó, chúng tôi sắp xếp lô điểm thể lực theo thứ tự tăng dần và lấy hai thành phần cuối cùng trong danh sách làm hai cá nhân đứng đầu trong lô đó.

Chúng tôi tra cứu chỉ số của họ và chọn toàn bộ tác nhân từ danh sách quần thể ban đầu.

Tổng hợp tất cả lại, chúng ta có thể đào tạo một nhóm đặc vụ chơi trò kéo xe chỉ sau một vài thế hệ.

Bạn nên thử nghiệm các siêu tham số về tỷ lệ đột biến, quy mô dân số và số lượng thế hệ.

Liệt kê 6.13, huấn luyện các mô hình.

Thế hệ đầu tiên bắt đầu với một quần thể các vectơ tham số ngẫu nhiên, nhưng tình cờ là một số vectơ tham số này sẽ tốt hơn các vectơ tham số khác.

Và chúng ta ưu tiên lựa chọn những con này để giao phối và sinh ra con cái cho thế hệ tiếp theo.

Để duy trì sự đa dạng di truyền, chúng tôi cho phép mỗi cá thể bị đột biến một chút.

Quá trình này lặp đi lặp lại cho đến khi chúng ta có được những cá nhân đặc biệt giỏi chơi trò kéo xe.

Bạn có thể thấy trong Hình 6.9 rằng điểm số tăng dần theo từng thế hệ tiến hóa.

Hình 6.9, điểm trung bình của quần thể qua các thế hệ trong một thuật toán di truyền được sử dụng để huấn luyện các tác nhân chơi trò kéo xe.