# Chương 2. Giải quyết kẻ cướp theo ngữ cảnh Học tăng cường sâu trong thực tế, Phiên bản video

---

Phần 2.5 Giải quyết kẻ cướp theo ngữ cảnh

Chúng tôi đã xây dựng một môi trường mô phỏng cho một tên cướp theo ngữ cảnh.

Trình mô phỏng bao gồm trạng thái, số từ 0 đến 9 đại diện cho một trong 10 trang web

trong mạng, tạo phần thưởng, nhấp chuột vào quảng cáo và phương pháp chọn hành động.

trong số 10 quảng cáo để phân phát.

Danh sách sau đây hiển thị mã cho môi trường kẻ cướp theo ngữ cảnh, nhưng không chi tiêu

dành nhiều thời gian để suy nghĩ về nó vì chúng tôi muốn trình bày cách sử dụng nó chứ không phải cách viết mã

nó.

Liệt kê 2.9 Môi trường kẻ cướp theo ngữ cảnh

Đoạn mã sau đây minh họa cách sử dụng môi trường.

Phần duy nhất chúng ta cần xây dựng là tác nhân, nói chung là mấu chốt của bất kỳ vấn đề RL nào,

vì việc xây dựng một môi trường thường chỉ liên quan đến việc thiết lập đầu vào/đầu ra với một số

nguồn dữ liệu hoặc cắm vào API hiện có.

Xem mã này.

Trình mô phỏng bao gồm một lớp Python đơn giản gọi là ContextBandit có thể được khởi tạo

đến một số lượng vũ khí cụ thể.

Để đơn giản, số lượng bang bằng với số nhánh, nhưng nói chung số lượng bang

không gian thường lớn hơn nhiều so với không gian hành động.

Lớp học có hai phương pháp.

Một là get_state, được gọi không có đối số và sẽ trả về trạng thái được lấy mẫu

ngẫu nhiên từ một phân bố đều.

Trong hầu hết các bài toán, trạng thái của bạn sẽ đến từ một phân bố phức tạp hơn nhiều.

Gọi phương thức khác, choose_arm bằng dấu chấm lửng, sẽ mô phỏng việc đặt một quảng cáo,

và nó trả về phần thưởng, chẳng hạn như tỷ lệ thuận với số lần nhấp vào quảng cáo.

Chúng ta cần luôn gọi get_state và sau đó chọn_arm để liên tục nhận được

dữ liệu mới để học hỏi.

Mô-đun ContextBandit cũng bao gồm một số hàm trợ giúp, chẳng hạn như hàm softmax

và một bộ mã hóa một nóng.

Vectơ được mã hóa một nóng là vectơ trong đó tất cả trừ một phần tử được đặt thành 0.

Phần tử khác 0 duy nhất được đặt thành 1 và biểu thị trạng thái cụ thể trong trạng thái

không gian.

Thay vì sử dụng phân phối xác suất phần thưởng tĩnh duy nhất cho n hành động, giống như ban đầu của chúng tôi

Vấn đề về tên cướp, trình mô phỏng tên cướp theo ngữ cảnh sẽ thiết lập cách phân phối phần thưởng khác nhau trên

hành động của mỗi trạng thái.

Nghĩa là, chúng ta sẽ có n cách phân bổ phần thưởng softmax khác nhau cho mỗi hành động

của n trạng thái.

Do đó, chúng ta cần tìm hiểu mối quan hệ giữa các trạng thái và cách phân bổ phần thưởng tương ứng của chúng,

và sau đó tìm hiểu hành động nào có xác suất cao nhất đối với một trạng thái nhất định.

Giống như tất cả các dự án của chúng tôi trong cuốn sách này, chúng tôi sẽ sử dụng PyTorch để xây dựng mạng lưới thần kinh

mạng.

Trong trường hợp này, chúng ta sẽ xây dựng một mạng nơ ron truyền tiếp hai lớp sử dụng các tín hiệu đã được chỉnh sửa

đơn vị tuyến tính ReLU là hàm kích hoạt.

Lớp đầu tiên chấp nhận one-hot 10 phần tử, còn được gọi là one-of-k, trong đó tất cả các phần tử

nhưng một bằng 0, vectơ được mã hóa của trạng thái và lớp cuối cùng trả về vectơ 10 phần tử,

đại diện cho phần thưởng dự đoán cho mỗi hành động được đưa ra ở trạng thái.

Hình 2.6 cho thấy quá trình chuyển tiếp của thuật toán mà chúng tôi đã mô tả.

Không giống như cách tiếp cận bảng tra cứu, tác nhân mạng nơ-ron của chúng ta sẽ học cách dự đoán phần thưởng

rằng mỗi hành động sẽ dẫn đến một trạng thái nhất định.

Sau đó, chúng tôi sử dụng hàm softmax để cung cấp cho chúng tôi phân phối xác suất cho các hành động

và lấy mẫu từ bản phân phối này để chọn một nhánh, quảng cáo.

Việc chọn một cánh tay sẽ mang lại cho chúng ta một phần thưởng mà chúng ta sẽ sử dụng để huấn luyện mạng lưới thần kinh của mình.

Hình 2.6, biểu đồ tính toán cho tên cướp theo ngữ cảnh 10 nhánh đơn giản.

Hàm get_state trả về một giá trị trạng thái, được chuyển thành vectơ một điểm nóng

trở thành dữ liệu đầu vào cho mạng nơ-ron hai lớp.

Đầu ra của mạng lưới thần kinh là phần thưởng được dự đoán cho mỗi hành động có thể xảy ra, đó là

một vectơ dày đặc chạy qua softmax để lấy mẫu một hành động từ xác suất thu được

phân phối qua các hành động.

Hành động được chọn sẽ trả về phần thưởng và cập nhật trạng thái của môi trường.

Theta 1 và theta 2 đại diện cho các tham số trọng lượng cho mỗi lớp.

Các ký hiệu n, r, p biểu thị các số tự nhiên 0, 1, 2, 3, số thực, số thực

số điểm cho mục đích của chúng tôi và xác suất tương ứng.

Chỉ số trên cho biết độ dài của vectơ, vì vậy p lũy thừa 10 biểu thị

một vectơ 10 phần tử trong đó mỗi phần tử là một xác suất, sao cho tất cả các phần tử

tổng bằng 1.

Ban đầu, mạng nơ-ron của chúng ta sẽ tạo ra một vectơ ngẫu nhiên như mảng 1,4, 50,

4,3, 0,31, 0,43, 11, 121, 98,9, 1,1 khi ở trạng thái 0.

Chúng ta sẽ chạy softmax trên vectơ này và lấy mẫu một hành động, rất có thể là hành động 6, từ hành động

0 đến 9, vì đó là số lớn nhất trong vectơ ví dụ.

Chọn hành động 6 sẽ tạo ra phần thưởng là 8.

Sau đó, chúng tôi huấn luyện mạng lưới thần kinh của mình để tạo ra vectơ của mảng 1,4, 50, 4,3, 0,31,

0,43, 11, 8, 98,9, 1,1, vì đó là phần thưởng thực sự mà chúng tôi nhận được cho hành động 6, rời đi

các giá trị còn lại không thay đổi

Lần tiếp theo khi mạng lưới thần kinh nhìn thấy trạng thái 0, nó sẽ đưa ra dự đoán về phần thưởng

cho hành động 6 gần hơn với 8.

Khi chúng ta liên tục thực hiện điều này qua nhiều trạng thái và hành động, mạng lưới thần kinh cuối cùng sẽ

học cách dự đoán phần thưởng chính xác cho mỗi hành động trong một trạng thái.

Do đó, thuật toán của chúng tôi sẽ có thể chọn hành động tốt nhất mỗi lần, tối đa hóa

phần thưởng.

Đoạn mã sau nhập các thư viện cần thiết và thiết lập một số siêu tham số, tham số

để xác định cấu trúc mô hình.

Xem mã này.

Trong mã trước, n là kích thước lô, d_in là thứ nguyên đầu vào, h là ẩn

thứ nguyên và d_out là thứ nguyên đầu ra.

Bây giờ chúng ta cần thiết lập mô hình mạng lưới thần kinh của mình.

Nó là một mạng nơron tuần tự, chuyển tiếp đơn giản, có hai lớp như chúng tôi đã mô tả trước đó.

Xem mã này.

Chúng tôi sẽ sử dụng hàm mất lỗi bình phương trung bình ở đây nhưng những hàm khác cũng có thể hoạt động.

Xem mã này.

Bây giờ chúng ta thiết lập một môi trường mới bằng cách khởi tạo lớp kẻ cướp bối cảnh, cung cấp số

vũ khí cho người xây dựng nó.

Hãy nhớ rằng, chúng ta đã thiết lập môi trường sao cho số cánh tay sẽ bằng với

số lượng các tiểu bang

Xem mã này.

Vòng lặp for chính của thuật toán sẽ rất giống với vòng lặp n-armed ban đầu của chúng tôi

thuật toán, nhưng chúng tôi đã thêm bước chạy mạng nơ-ron và sử dụng đầu ra để chọn

một hành động.

Chúng ta sẽ định nghĩa một hàm gọi là train, như trong danh sách 2.10, chấp nhận môi trường

phiên bản chúng tôi đã tạo trước đó, số lượng sử thi mà chúng tôi muốn đào tạo và quá trình học tập

tỷ lệ.

Trong hàm này, chúng ta sẽ đặt biến PyTorch cho trạng thái hiện tại mà chúng ta cần phải

mã hóa one-hot bằng cách sử dụng one_hot, có dấu ba chấm, chức năng mã hóa.

Xem mã này.

Khi chúng ta bước vào vòng lặp đào tạo chính, chúng ta sẽ chạy mô hình mạng thần kinh của mình với

vectơ trạng thái hiện tại được khởi tạo ngẫu nhiên.

Nó sẽ trả về một vectơ đại diện cho dự đoán của nó về các giá trị của từng giá trị có thể

hành động.

Lúc đầu, mô hình sẽ xuất ra một loạt giá trị ngẫu nhiên do nó chưa được đào tạo.

Chúng tôi sẽ chạy hàm softmax trên đầu ra của mô hình để tạo phân phối xác suất

qua các hành động.

Sau đó, chúng tôi sẽ chọn một hành động bằng cách sử dụng choose_arm của môi trường, với chức năng dấu ba chấm,

sẽ trả lại phần thưởng được tạo khi thực hiện hành động đó.

Nó cũng sẽ cập nhật trạng thái hiện tại của môi trường.

Chúng ta sẽ biến phần thưởng, là một số nguyên không âm, thành một vectơ nóng mà chúng ta có thể

sử dụng làm dữ liệu đào tạo của chúng tôi.

Sau đó, chúng tôi sẽ chạy một bước truyền ngược với vectơ phần thưởng này, với trạng thái mà chúng tôi

đã đưa ra mô hình.

Vì chúng tôi đang sử dụng mô hình mạng nơ-ron làm hàm giá trị hành động nên chúng tôi không còn có

bất kỳ loại ký ức lưu trữ mảng giá trị hành động nào.

Mọi thứ đang được mã hóa theo tham số trọng lượng của mạng lưới thần kinh.

Toàn bộ chức năng tàu được hiển thị trong danh sách sau đây.

Liệt kê 2.10, vòng lặp đào tạo chính.

Hãy tiếp tục và chạy chức năng này.

Khi chúng tôi đào tạo mạng này trong 5000 kỷ nguyên, chúng tôi có thể vẽ đường trung bình động của phần thưởng

kiếm được trong thời gian đào tạo.

Xem hình 2.7.

Chúng tôi đã bỏ qua đoạn mã để tạo ra một biểu đồ như vậy.

Mạng lưới thần kinh của chúng ta thực sự học được sự hiểu biết khá tốt về mối quan hệ giữa

trạng thái, hành động và phần thưởng cho kẻ cướp theo ngữ cảnh này.

Khoản thanh toán phần thưởng tối đa cho bất kỳ lần chơi nào là 10 và mức trung bình của chúng tôi là khoảng

8.5, gần với mức tối ưu về mặt toán học cho tên cướp cụ thể này.

Thuật toán học tăng cường sâu đầu tiên của chúng tôi hoạt động.

Được rồi, nó không phải là một mạng lưới rất sâu, nhưng vẫn vậy.

Hình 2.7, biểu đồ huấn luyện hiển thị phần thưởng trung bình khi chơi kẻ cướp theo ngữ cảnh

trình mô phỏng sử dụng mạng thần kinh hai lớp làm hàm giá trị hành động.

Chúng ta có thể thấy phần thưởng trung bình tăng lên nhanh chóng trong thời gian đào tạo, chứng tỏ hệ thần kinh của chúng ta

mạng đang học thành công.