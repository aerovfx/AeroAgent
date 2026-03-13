# Chương 2. Giải quyết kẻ cướp theo ngữ cảnh Học tăng cường sâu trong hành động, Video Edition.vi

---

Phần 2.5 quyết định Bandit theo bối cảnh Chúng tôi

tôi đã xây dựng một môi trường mô phỏng cho bối cảnh Bandit.

Trình mô phỏng bao gồm trạng thái, số từ 0 đến 9 biểu tượng một trong

10 trang web trong mạng, tạo phần thưởng, nhấp quảng cáo và một

phương pháp lựa chọn hành động, trong số 10 quảng cáo nào sẽ được hiển thị.

Danh sách sau đây cho thấy mã cho môi trường Bandit theo bối cảnh

cảnh báo, nhưng đừng để mất nhiều thời gian để nghĩ về nó vì chúng

tôi muốn chứng minh cách sử dụng chứ không phải mã hóa.

Danh sách 2.9 Môi trường Bandit theo bối cảnh

Đoạn mã sau đây minh họa cách sử dụng môi trường.

Phần duy nhất chúng tôi cần xây dựng là một tác nhân, thường là tâm điểm của

bất kỳ vấn đề nào về RL, vì việc xây dựng môi trường chỉ liên quan đến công việc

thiết lập đầu vào/đầu ra với một số nguồn dữ liệu hoặc kết nối với API hiện có.

Xem mã này.

Trình mô phỏng bao gồm một lớp Python đơn giản gọi là

ContextBandit có thể được khởi tạo thành một số nhánh cụ thể.

Vì đơn giản nên trạng thái

với số nhánh, nhưng nói chung trạng thái

không có trạng thái lớn

hơn nhiều so với không có tác động.

Lớp này có hai phương thức.

Một là get_state, hàm này sẽ được gọi mà không có đối số nào và

will return a state get ngẫu nhiên theo bố cục đều đặn.

Trong quá trình xử lý các vấn đề, trạng thái của bạn sẽ

lấy nguồn từ một bộ phân phối được phép phức tạp hơn nhiều.

Gọi phương thức kia là choose_arm với dấu ba chấm, hàm này sẽ mô phỏng hành động đặt quảng

báo cáo và sẽ trả về phần thưởng, có giới hạn như phần thưởng thuận lợi với số lần quảng cáo nhấp chuột.

Chúng ta luôn cần gọi get_state rồi mới gọi choose_arm

theo thứ tự đó để liên tục nhận dữ liệu mới để học.

Mô-đun ContextBandit cũng bao gồm một số hàm hỗ trợ

giúp đỡ, giới hạn như hàm softmax và bộ mã hóa một giá trị.

Một vectơ được mã hóa một giá trị là vectơ mà chỉ trừ một

toàn bộ các phần tử khác sẽ được cài đặt thành 0.

Phần tử không phải là 0 duy nhất được đặt thành 1 và

cho biết trạng thái cụ thể nào trong trạng thái không.

Thay vì sử dụng một phân tích xác thực phần thưởng tĩnh nhất trên n

tác động, như vấn đề Bandit ban đầu, mô phỏng Bandit có ngữ cảnh thiết kế

thiết lập một phần thưởng khác nhau trên các hành động cho mỗi trạng thái.

Tức là, chúng tôi sẽ có nhiều phần thưởng softmax khác nhau được phân phối trên nhiều hoạt động đối với mỗi người

n trạng thái.

Do đó, chúng ta cần tìm hiểu mối quan hệ giữa các trạng thái và phân phối phần thưởng tương thích

ứng dụng của chúng, sau đó tìm hiểu bất kỳ hành động nào có hiệu suất cao nhất đối với một trạng thái nhất định.

Tương tự như tất cả các dự án của chúng trong cuốn sách

này, chúng tôi sẽ sử dụng PyTorch để xây dựng mạng lưới nơ-ron.

Trong tình huống này, chúng tôi sẽ xây dựng một mạng lưới truyền dẫn nơ-ron

Tiếp tục liên kết hai lớp bằng cách sử dụng các tuyến tính toán điều chỉnh ReLU đơn vị để kích hoạt chức năng.

Lớp đầu tiên chấp nhận véc tơ mã hóa một đơn vị nóng bao gồm 10 phần tử, hay còn gọi là một-trong-k,

trong đó tất cả các phần tử đều là số không, trừ một phần tử, biểu thị trạng thái và lớp cuối cùng trả về

véc tơ 10 phần tử, biểu thị phần thưởng dự kiến cho từng hành động đối với trạng thái được cung cấp.

Hình 2.6 cho thấy phần tiếp theo của luồng truyền phát

theo thuật toán mà chúng tôi đã mô tả.

Không giống như cách tiếp cận nghiên cứu bảng tiếp theo, các hoạt động mạng nơ-ron của chúng ta sẽ

học cách mong đợi phần thưởng mà mỗi hành động sẽ cung cấp lại cho một trạng thái nhất định.

Sau đó, chúng tôi sử dụng hàm softmax để cung cấp

cho chúng tôi phân phối hiệu suất trên các hoạt động

và lấy mẫu từ phân phối này để

chọn một nhánh và quảng cáo.

Việc chọn một nhánh sẽ cung cấp cho chúng ta một phần thưởng,

mà chúng tôi sẽ sử dụng để huấn luyện mạng nơ-ron của mình.

Hình 2.6, một biểu đồ tính toán

máy đánh lừa cảnh 10 nhánh đơn giản.

Hàm get_state trả về một trạng thái giá trị, được chuyển đổi thành công

vector nóng, trở thành đầu vào dữ liệu cho lớp mạng nơ-ron hai lớp.

Đầu ra của mạng lưới nơ-ron là phần thưởng được mong đợi cho từng hành động

có thể, đó là một vectơ dày, chạy qua softmax để

lấy hành động mẫu từ phân phối kết quả xác thực cho các hành động.

Lựa chọn hành động sẽ trả lại phần thưởng

và cập nhật trạng thái của môi trường.

Theta 1 và theta 2 biểu tượng

các tham số quan trọng cho từng lớp.

Các ký hiệu n, r và p chỉ các số tự nhiên, 0, 1, 2, 3, các số

thực tế, số dấu chấm cho mục tiêu của chúng ta và một hiệu suất.

Mũ bảo hiểm có độ dài chỉ định của vectơ, nên p mũ 10 biểu thị một vectơ 10

phần tử, trong đó mỗi phần tử là một xác thực, trong đó tất cả các phần tử

cộng với 1.

Ban đầu, mạng nơ-ron của họ

ta sẽ tạo ra một ngẫu nhiên ngẫu nhiên như

một mảng 1,4, 50, 4,3, 0,31, 0,43,

11, 121, 98,9, 1,1 khi ở trạng thái 0.

Chúng ta sẽ chạy softmax trên

điều này và lấy một hành động mẫu, nhiều khả năng

năng là hành động 6, từ hành động 0

đến 9, vì đó là số lớn nhất trong ví dụ.

Choose action 6 will

tạo phần thưởng, giả sử là 8.

Sau đó, họ huấn luyện mạng

nơ-ron của mình để tạo ra sự phấn khích của một

mảng 1,4, 50, 4,3, 0,31, 0,43, 11,

8, 98,9, 1,1, vì đó là phần thưởng

kinh tế mà chúng tôi đã nhận được sự lựa chọn hành động

động 6, để nguyên phần còn lại của giá trị.

Next next on network

nơ-ron được tìm thấy trạng thái 0, it will

tạo phần thưởng dự kiến

cho action 6 near than 8.

Khi chúng tôi liên tục thực hiện điều này ở

nhiều trạng thái và hành động, cuối cùng, mạng

nơ-ron sẽ học cách mong đợi phần thưởng chính

xác định từng hành động cho một trạng thái nhất định.

Làm điều đó, thuật toán của họ

ta sẽ có thể chọn hành động

tốt nhất mỗi lần, tối đa hóa

phần thưởng của chúng ta.

Đoạn mã sau khi nhập các thư viện cần thiết

and setting a hyper number, number

để chỉ định cấu hình cấu hình.

Xem đoạn mã này.

Trong mã trước, n là kích thước lô, d_in là chiều

đầu vào, h là chiều ẩn và d_out là chiều đầu ra.

Bây giờ chúng ta cần thiết lập

mô hình mạng lưới của mình.

Đây là một tiến trình mạng nơ-ron, hướng tiếp theo,

đơn giản với hai lớp như đã mô tả ở trên.

Xem mã này.

Chúng tôi sẽ sử dụng phương pháp trung bình lỗi mất

bình ở đây nhưng những chức năng khác cũng có thể hoạt động.

Xem mã này.

Bây giờ, chúng tôi thiết lập một môi trường mới bằng

cách khởi động lớp bandit theo bối cảnh, cung cấp số

vũ khí cho nhà tạo.

Hãy nhớ rằng chúng tôi đã thiết lập trường môi trường

for vũ khí số lượng bằng số lượng trạng thái.

Xem mã này.

Vòng lặp chính của thuật toán sẽ rất giống với máy tính toán

Chúng ta có thể kiếm được tiền bằng cách cấm chúng ta đánh đầu, nhưng chúng ta đã có

thêm bước chạy mạng và sử dụng đầu ra để chọn hành động.

Chúng ta sẽ xác định một hàm có tên

là train, được hiển thị trong danh sách 2.

10, hàm này chấp nhận trường

môi trường hợp lý mà chúng ta

đã tạo trước đó, số lượng sử dụng này chúng tôi mong muốn đào tạo và tốc độ học.

Trong hàm, chúng ta sẽ đặt một biến PyTorch cho trạng thái hiện tại, biến này chúng ta sẽ

cần mã hóa một cách nhanh chóng bằng hàm mã hóa một cách nóng bỏng, với dấu ba chấm, dấu ba chấm.

Xem mã này.

Khi chúng ta vào vòng đào tạo chính, chúng ta sẽ chạy hình

Mạng nơ ron của mình với trạng thái hiện tại được khởi tạo ngẫu nhiên.

Nó sẽ trả về một kết quả có thể được mong đợi

it for value of each action can may ra.

Lúc đầu, mô hình sẽ chọn ra một loạt các

giá trị ngẫu nhiên vì nó chưa được đào tạo.

Chúng ta sẽ chạy hàm softmax trên đầu ra của mô hình để tạo ra phân tích xác thực trên

các hành động.

Sau đó, chúng tôi sẽ chọn một hành động bằng cách sử dụng choose_arm của môi trường, với

hàm ba dấu chấm, hàm này sẽ trả về phần thưởng do thực hiện hành động tạo ra.

Hàm này cũng sẽ cập nhật

hiện trạng thái của môi trường.

Chúng ta sẽ biến các phần thưởng, là một số nguyên không âm, thành công

Một giá trị mà chúng tôi có thể sử dụng làm huấn luyện viên dữ liệu.

Sau đó chúng ta sẽ chạy một bước ngược dòng với phần

thưởng này, do trạng thái mà chúng tôi đã cung cấp cho mô hình.

Vì chúng tôi đang sử dụng mô hình mạng nơ-ron làm chức năng giá trị hành động,

do đó, chúng tôi không còn bất kỳ mảng giá trị hành động nào được lưu trữ trong bộ nhớ.

Tất cả mọi thứ đều được mã hóa trong

các tham số quan trọng của nơ-ron mạng.

Toàn bộ chức năng huấn luyện được

show in the after list.

Danh sách 2.10, huấn luyện chính vòng lặp.

Continue and run this function.

Khi chúng tôi huấn luyện mạng này trong 5000 kỷ nguyên, chúng tôi có thể vẽ

biểu đồ trung bình của phần thưởng được đào tạo trong thời gian huấn luyện.

Xem hình 2.7.

Chúng tôi đã bỏ mã hóa để

tạo ra một biểu đồ như vậy.

Mạng nơ-ron của chúng tôi thực sự

học khá tốt hiểu biết về mối

quan hệ giữa trạng thái, hành động và

phần thưởng cho bối cảnh tên này.

Khoản thanh toán tối đa tiền thưởng cho bất kỳ lượt chơi nào

cái nào là 10 và mức độ trung bình của chúng tôi

đạt được giá trị ở khoảng 8,5, gần đạt kết quả tối ưu

ưu tiên về mặt toán học cho cụ thể tên này.

Thuật toán học theo cố gắng củng cố

độ sâu đầu tiên của chúng tôi hoạt động.

Đã rồi, đó không phải là một

mạng lưới rất sâu nhưng vẫn còn.

Hình 2.7, sơ đồ đào tạo có thể hiện phần

trả lương trung bình khi chơi mô phỏng

bối cảnh đặt tên khi sử dụng mạng

nơ-ron hai lớp làm chức năng giá trị hành động.

Chúng ta có thể tìm thấy phần thưởng

trung bình tăng tốc trong thời gian

gian đào tạo, chứng minh rằng mạng

nơ-ron của chúng tôi đã học thành công.