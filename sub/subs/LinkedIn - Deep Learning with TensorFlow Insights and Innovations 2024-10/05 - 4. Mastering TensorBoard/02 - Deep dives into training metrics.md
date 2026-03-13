# 02 - Đi sâu vào các chỉ số đào tạo

---

- [Giảng viên] Trong buổi học này,

chúng ta sẽ xây dựng dựa trên những gì chúng ta đã học trước đây

về TensorBoard và đào tạo mô hình.

Vậy nên hãy gặp tôi ở không gian mật mã của bạn,

tìm thư mục src từ bảng điều khiển bên trái của bạn

và tìm tệp 04_02_begin.py.

Vì vậy, hãy bắt đầu với mã bắt đầu,

và sau đó tìm cách khớp với mã kết thúc ngay tại đây,

đó là tệp 04_02_end.py.

Vì vậy, thiết lập này tương tự như những gì chúng ta đã thấy trước đây,

nhưng nó bỏ đi một số thành phần quan trọng

rằng chúng ta sẽ cùng nhau hoàn thành và kết hợp

đến cuối tệp Python.

Vì vậy, phần này nên quen thuộc.

Chúng tôi đang tải tập dữ liệu california_housing,

chia nó thành các tập huấn luyện, xác nhận và kiểm tra,

và sau đó chuẩn hóa dữ liệu

sao cho mỗi tính năng đóng góp như nhau

đến quá trình học tập.

Tiếp theo, chúng tôi đang xây dựng mô hình.

Chúng tôi xây dựng một mô hình mạng lưới thần kinh đơn giản

với hai lớp ẩn

và biên dịch nó bằng lỗi bình phương trung bình,

MSE là hàm mất mát,

và giảm độ dốc ngẫu nhiên, SGD là trình tối ưu hóa.

Đây là một mạng nơron truyền thẳng cơ bản

với hai lớp, mỗi lớp 30 nơ-ron,

tiếp theo là lớp đầu ra dự đoán giá nhà đất.

Vì vậy, chúng tôi có phần giữ chỗ ở đây

để thiết lập ghi nhật ký TensorBoard và đào tạo mô hình.

Những phần giữ chỗ này cho biết

nơi chúng tôi sẽ chèn chức năng ghi nhật ký TensorBoard

và quá trình đào tạo.

Vì vậy chúng ta có một phần giữ chỗ ở đây

nơi chúng tôi xác định log_dir,

sau đó chúng ta có tensorboard_callback,

thì chúng ta có phần giữ chỗ đào tạo.

Vậy hãy cuộn lên

và thêm một số thư viện

bị thiếu trong mã bắt đầu này

để kết hợp TensorBoard.

Vì vậy, từ tensorflow.keras.callbacks

nhập TensorBoard.

Vì vậy, từ tensorflow.keras.callbacks hãy nhập TensorBoard.

Và điều khác mà chúng tôi muốn nhập vào đây là chúng tôi muốn

để nhập hệ điều hành, nhập os,

bởi vì chúng tôi muốn xác định một thư mục nhất định

thay vì ngày giờ để ghi lại mô hình của chúng tôi

vào thư mục nhật ký.

Vì vậy sau khi tải hai thư viện bổ sung này,

chúng ta có thể tiếp tục và đi tiếp

với thiết lập ghi nhật ký TensorBoard.

Vì vậy, hãy cuộn xuống phần giữ chỗ của chúng tôi ở đây.

Bây giờ chúng ta sẽ hoàn thành mã này.

Chúng tôi sẽ xóa cái không

và sau đó chúng tôi sẽ cung cấp hệ điều hành,

hệ điều hành, path.join.

Vì vậy, đây là nơi chúng tôi xác định thư mục

để lưu trữ nhật ký của chúng tôi.

Hãy tưởng tượng rằng bạn muốn

để đặt tên cho một thư mục cụ thể ở đây.

Đây là cách bạn làm điều đó.

Vì vậy chúng tôi nói os.path.join.

Tiếp theo, chúng tôi sẽ cung cấp thư mục.

Được rồi, chúng tôi muốn ghi vào nhật ký,

chúng ta muốn có thân hình cân đối, và sau đó chúng ta muốn trở thành,

hãy đặt tên chương ở đây, 04_02.

Tiếp theo, hãy tiếp tục và điền tensorboard_callback.

Vì vậy, ở đây, chúng tôi sẽ thiết lập dữ liệu nhật ký,

bao gồm biểu đồ về trọng số và độ lệch,

điều này có thể rất hữu ích

khi chúng ta hình dung quá trình đào tạo sau này trong TensorBoard.

Vì vậy, hãy tiếp tục và nói TensorBoard,

log_dir bằng

vào thư mục nhật ký mà chúng tôi vừa xác định ở trên.

Sau đó chúng ta nói histogram_freq=1,

và sau đó chúng ta nói histogram_freq=1.

Tiếp theo, chúng ta có phần giữ chỗ đào tạo.

Vì vậy, hãy tiếp tục và đào tạo mô hình.

Vì vậy, điều này lại quen thuộc,

tuy nhiên, chúng tôi sẽ làm điều này một lần nữa chỉ để nhắc nhở bản thân

rằng chúng tôi sẽ xác định phần gọi lại

trong khóa đào tạo này.

Vậy model.fit, dấu ngoặc đơn, X_train, y_train,

kỷ nguyên = 20,

validation_data=(X_valid, y_valid),

callbacks=tensorboard_callback, dấu ngoặc đơn.

Vì vậy, ở đây, chúng tôi đào tạo mô hình

để bao gồm tensorboard_callback

trong tham số gọi lại.

Hãy đảm bảo rằng chúng ta có dấu ngoặc đơn chính xác.

Chúng tôi không, chúng tôi có thể nói bằng dấu ngoặc đơn màu đỏ ở đây

rằng nó phàn nàn rằng nó không có cặp đóng.

Vì vậy bây giờ hãy làm cho nó bằng dấu ngoặc đơn đóng.

Vì vậy chúng tôi đào tạo mô hình ở đây

để bao gồm tensorboard_callback

trong tham số gọi lại.

Điều này sẽ đảm bảo rằng tất cả dữ liệu liên quan được ghi lại

và sẵn sàng để chúng tôi phân tích trong TensorBoard.

Vì vậy, chúng tôi sẽ tiếp tục và đánh giá mô hình tiếp theo.

Vì vậy, hãy làm điều đó tiếp theo.

Đánh giá mô hình

trên tập thử nghiệm.

Vì vậy, điều này quen thuộc với chúng ta,

msc_test, lỗi bình phương trung bình,

model.evaluate(X_test, y_test).

Sau đó chúng ta sẽ tiếp tục và in kết quả,

f"Lỗi bình phương trung bình

trong Bộ kiểm tra: {mse_test}".

Sau đó chúng ta tiếp tục và nói rằng hãy lên kế hoạch đào tạo

và mất xác nhận, plt.plot.

Chúng ta bắt đầu với lịch sử mất mát.history,

rồi tiếp tục chèn phần mất mát vào,

dấu phẩy, chúng tôi sẽ gắn nhãn là Mất.

Được rồi, tiếp theo chúng ta sẽ đưa ra thông tin xác thực.

Chúng ta có thể sao chép nó. Bằng cách đó, nó nhanh hơn.

Tất cả những gì chúng ta làm là thay đổi loss thành val_loss

và tên là Mất xác thực.

Sau đó, chúng ta tiếp tục cung cấp xlabel và ylabel,

plt.xlabel('Kỷ nguyên'),

và sau đó plt.ylabel('Mất'),

sau đó plt.legend().

Và hãy tiếp tục và lưu nó vào thư mục đầu ra,

plt.savefig, và sau đó chúng ta sẽ lưu lại cái này

vào thư mục đầu ra.

Đặt tên chương chính xác,

tên phiên, loss_plot.png.

Vì vậy chúng ta hãy tiếp tục và cho nó một cái nhìn khác.

Hãy chắc chắn rằng mọi thứ được gõ chính xác.

Vì vậy điều chúng tôi đã làm là chúng tôi tiếp tục

và thêm hai lần nhập khẩu nữa ở đây.

Một là nhập TensorBoard,

cái còn lại là nhập hệ điều hành.

Sau đó, chúng tôi đã tải và chuẩn bị điền vào,

điền tiêu chuẩn hóa, xây dựng mô hình đã điền.

Chúng tôi biên soạn mô hình,

sau đó chúng tôi thiết lập ghi nhật ký TensorBoard.

Vì vậy, ở đây, chúng tôi cung cấp thư mục mà chúng tôi muốn lưu,

nhật ký sẽ được lưu,

sau đó chúng ta tiếp tục và xác định tensorboard_callback ở đây,

nơi chứa log_dir

và nó lấy histogram_freq ở đây.

Tiếp theo, chúng tôi đào tạo mô hình ở đây,

và sự khác biệt ở đây là chúng tôi cung cấp lệnh gọi lại

trở thành tensorboard_callback.

Sau đó, chúng tôi tiếp tục và đánh giá mô hình bằng MSE.

Tiếp theo, chúng tôi vẽ biểu đồ mất mát đào tạo và xác nhận ở đây.

Vì vậy trong phiên này,

chúng tôi đã chuyển từ một kịch bản đã hoàn thành một phần

đến một thiết bị có đầy đủ chức năng ghi dữ liệu vào TensorBoard,

đào tạo một mạng lưới thần kinh,

và đánh giá hiệu quả của mô hình.

TensorBoard là một công cụ rất mạnh cho phép chúng ta

để theo dõi và tinh chỉnh các mô hình của chúng tôi trong thời gian thực.

Điều này làm cho nó trở thành một phần thiết yếu

của bất kỳ quy trình học sâu nào.

Vì vậy hãy tiếp tục và mở tệp 04_02_end.py.

Vì vậy, điều này phải phù hợp với những gì chúng tôi đã làm.

Chỉ cần cho nó một cái nhìn khác

và cố gắng tóm tắt cho chính mình những gì chúng ta đã làm ở đây.

Điều đáng chú ý ở đây là gì?

Điều đáng rút ra một lần nữa là chúng tôi đã tạo một thư mục mới ở đây

và sau đó chúng ta thiết lập tính năng ghi nhật ký TensorBoard trong phần này.

Chúng tôi đã xác định nơi chúng tôi muốn thư mục nhật ký này

để được cứu.

Chúng tôi đã đưa ra các cài đặt mà chúng tôi muốn.

Và cuối cùng, chúng ta có thể tiếp tục và chạy thử ở đây.

Vậy nên hãy dành vài phút,

và kết quả là 0,33, Lỗi bình phương trung bình trong bài kiểm tra.

Chúng ta có thể tiếp tục và mở TensorBoard ở đây một lần nữa.

Nhưng trước đó, hãy tóm tắt.

Phần này đã giới thiệu một cách có tổ chức hơn

và cách tiếp cận có cấu trúc

để thiết lập TensorBoard bằng os.path.join.

Vì vậy, đây là cách chúng ta có thể nối và xác định các thư mục.

Chúng tôi đã tiếp tục và điền vào tất cả các phần giữ chỗ

từ tệp bắt đầu và chúng tôi đã đến tệp cuối cùng.

Phần này nhấn mạnh sự sạch sẽ

và quản lý tập tin nhất quán,

đặc biệt là khi chúng ta đang giải quyết

với nhiều thí nghiệm tương tự

để mọi thứ được tổ chức.

Bằng cách đó, chúng ta có thể tìm thấy từ bảng điều khiển bên trái

rằng chúng tôi có nhật ký ở đây.

Và như bạn thấy, nó hiển thị màu xanh lá cây,

nghĩa là chúng tôi vừa cập nhật thư mục 04_02,

đó là một cách rất có tổ chức để lưu nhật ký của chúng tôi.

Vì vậy, chúng tôi có đào tạo, chúng tôi có xác nhận,

thay vì chỉ lưu nó theo ngày và giờ,

điều đó cũng có lợi ích của nó.

Bạn có thể đưa ra phán quyết về mục đích của bạn là gì

và tại sao bạn lại lưu nhật ký.

Tuy nhiên, bây giờ chúng ta phải thấy hai cách khác nhau

về cách chúng tôi có thể ghi lại hiệu suất mô hình của mình tại đây.

Bây giờ là bước tiếp theo,

chúng ta có thể gọi lại TensorBoard từ thiết bị đầu cuối,

và mở một trang web để hiển thị hiệu suất của chúng tôi

của người mẫu ở đây.

Vì vậy hãy tiếp tục và bắt đầu gõ vào cửa sổ terminal,

tenorboard, dấu gạch ngang, dấu gạch ngang,

và chúng tôi phải cung cấp một thư mục nhật ký,

đó là nhật ký/phù hợp.

Đó là nơi chúng tôi lưu tất cả dữ liệu của mình ở đây.

Vì vậy chúng ta tiếp tục và nhấn Enter,

và nó cung cấp cho chúng tôi một trang web ở đây.

Vì vậy, chúng tôi Control + nhấp vào đây để mở nó ra,

và chúng tôi có nó, tất cả dữ liệu của chúng tôi.

Vì vậy, hãy bắt đầu từ khung bên trái ở đây.

Chúng tôi có thanh bên trái.

Điều này hiển thị danh sách tất cả các khóa đào tạo khác nhau

và các lần chạy xác thực được đăng nhập vào TensorBoard.

Vì vậy chúng ta chỉ cần chọn chương bốn, phần hai ở đây.

Mã màu còn giúp chúng ta phân biệt

giữa các lần chạy và các giai đoạn khác nhau.

Ví dụ: nếu đó là đào tạo hoặc nếu đó là xác nhận.

Vì vậy, chúng ta có thể tiếp tục và chỉ kiểm tra thư mục này,

04_02/train và xác nhận ngay bây giờ.

Sau đó, chúng ta có thể tiếp tục và xem xét độ lệch/biểu đồ trước.

Vì vậy, độ lệch/biểu đồ cho thấy sự phân bố của các giá trị độ lệch

trong các lớp của mạng lưới thần kinh trong giai đoạn huấn luyện.

Trục x ở đây biểu thị phạm vi giá trị sai lệch,

và trục y hiển thị tần số của các giá trị đó.

Sự tăng đột biến hoặc các đỉnh trong biểu đồ có thể chỉ ra

những thành kiến đang được điều chỉnh như thế nào trong quá trình đào tạo.

Vì vậy, sự thiên vị là quan trọng.

Giám sát sự phân bổ các thành kiến có thể cho chúng ta những hiểu biết sâu sắc

vào việc mô hình đang học như thế nào.

Nếu các thành kiến luôn ở mức cao hay thấp,

nó có thể chỉ ra vấn đề với tốc độ học tập

hoặc phân phối dữ liệu.

Chuyển sang epoch_learning_rate.

Biểu đồ này cho thấy tốc độ học tập được sử dụng

trong mỗi thời kỳ đào tạo.

Trong ví dụ cụ thể này,

tỷ lệ học tập hiển thị 0,01 trên tất cả các kỷ nguyên

như được chỉ ra bởi đường phẳng.

Trục X biểu thị số kỷ nguyên

và trục y hiển thị giá trị tốc độ học tập.

Vậy tại sao điều này lại quan trọng?

Hiểu cách thức hoạt động của tốc độ học tập

trong quá trình đào tạo là rất quan trọng vì nó ảnh hưởng đến tốc độ

và sự ổn định của việc học.

Một tốc độ học tập liên tục có thể là đủ,

nhưng trong một số trường hợp, chúng ta có thể muốn điều chỉnh nó một cách linh hoạt.

Chuyển sang epoch_loss. Vì vậy, hãy tiếp tục và phóng to cái này.

Vì vậy, âm mưu này cho thấy sự mất mát qua các kỷ nguyên

cho cả hai giai đoạn đào tạo và xác nhận.

Vậy trục x ở đây biểu thị số kỷ nguyên,

là 20 và sau đó trục y hiển thị giá trị tổn thất ở đây.

Vì vậy, bạn có thể làm cho nó lớn hơn hoặc nhỏ hơn

bằng Alt + cuộn. như vậy.

Vì vậy, đường cong màu xanh thể hiện sự mất mát trong quá trình đào tạo ở đây,

trong khi đường cong màu hồng biểu thị sự mất xác thực.

Vậy tại sao điều này lại quan trọng?

Điều này rất quan trọng vì nó là biểu đồ chính

để hiểu mô hình của chúng tôi đang học tốt như thế nào.

Lý tưởng nhất là cả việc đào tạo

và tổn thất xác nhận sẽ giảm và hội tụ.

Nếu tổn thất xác thực cao hơn nhiều hoặc ngừng giảm,

nó có thể cho thấy trang bị quá mức.

Vì vậy, trong trường hợp của chúng tôi, chúng đều giảm và hội tụ.

Tiếp theo, chuyển sang phần đánh giá_loss_vs_iterations.

Hãy tiếp tục và nhấp vào nó để phóng to và xem biểu đồ.

Vì vậy, biểu đồ này cho thấy sự mất mát trong quá trình đánh giá.

Nói cách khác, xác nhận qua các lần lặp khác nhau.

Vì vậy trục x biểu thị số lần lặp

và trục y hiển thị giá trị tổn thất.

Đường cong giúp chúng ta thấy hiệu suất của mô hình thay đổi như thế nào

khi nó tiếp tục đánh giá trên bộ xác nhận.

Điều này quan trọng vì nó giúp chúng ta chẩn đoán

mô hình ổn định như thế nào trong quá trình đánh giá.

Nếu tổn thất tiếp tục giảm,

nó có nghĩa là mô hình đang được cải thiện.

Tuy nhiên, nếu nó dao động hoặc bắt đầu tăng,

chúng ta có thể thấy dấu hiệu cho ăn quá nhiều.

Cuối cùng, hãy tiếp tục và nhấp vào kernel,

trong đó hiển thị kernel/biểu đồ.

Biểu đồ này hiển thị sự phân bố của kernel.

Nói cách khác, trọng lượng.

Điều này đang hiển thị trọng lượng trong giai đoạn đào tạo.

Tương tự như độ lệch/biểu đồ,

trục x biểu thị phạm vi giá trị hạt nhân,

và trục y ở đây đang hiển thị tần số.

Các đỉnh và hình dạng của biểu đồ có thể chỉ ra

trọng lượng được điều chỉnh như thế nào trong suốt quá trình tập luyện.

Tại sao điều này lại quan trọng?

Giám sát trọng lượng hạt nhân là rất quan trọng để hiểu

các tham số của mô hình thay đổi như thế nào theo thời gian.

Những thay đổi hoặc mô hình đáng kể có thể chỉ ra vấn đề

như độ dốc biến mất hoặc khởi tạo không đúng cách.

Vậy để tóm tắt điều quan trọng ở đây,

bảng điều khiển Chạy ở bên trái,

nó giúp so sánh các buổi đào tạo và xác nhận khác nhau,

và chúng ta có thể chạy và chúng ta có thể chọn chúng

bằng cách nhấp vào các ô này

hoặc bỏ chọn chúng bằng cách nhấp lại.

Sau đó, chúng tôi xem xét độ lệch/biểu đồ,

giám sát sự phân bố của các sai lệch trong mô hình.

Chúng ta đã nói về epoch_learning_rate,

trong đó cho thấy tốc độ học tập qua các kỷ nguyên.

Sau đó chúng tôi ôn lại epoch_loss,

theo dõi sự mất mát trong quá trình đào tạo và xác nhận qua các kỷ nguyên.

Sau đó, chúng tôi xem xét đánh giá_loss_vs_iterations.

Điều này đánh giá tính ổn định của mô hình trong quá trình xác nhận.

Cuối cùng, chúng tôi xem xét kernel/biểu đồ,

trong đó quan sát việc đánh giá trọng lượng trong quá trình đào tạo.

Vì vậy, bằng cách nhìn vào những biểu đồ này,

chúng tôi hiểu cách TensorBoard cung cấp thông tin chuyên sâu

vào quá trình đào tạo,

điều này giúp chẩn đoán dễ dàng

và cải thiện hiệu suất của mô hình.

Vì vậy trong phiên này,

chúng tôi đã biết cách sắp xếp nhật ký của mình vào một thư mục cụ thể,

và sau đó làm cách nào chúng ta có thể xem kết quả từ TensorBoard

và làm thế nào chúng ta có thể đánh giá chúng.