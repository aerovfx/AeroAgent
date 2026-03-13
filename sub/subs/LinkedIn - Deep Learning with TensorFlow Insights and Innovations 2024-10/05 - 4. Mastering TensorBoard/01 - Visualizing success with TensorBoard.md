# 01 - Hình dung thành công với TensorBoard

---

- [Người hướng dẫn] Vì vậy, trước khi chúng ta đi sâu vào phần mã,

hãy nói về TensorBoard.

Hãy truy cập www.tensorflow.org/tensorboard.

Vậy TensorBoard là gì?

TensorBoard là một công cụ trực quan mạnh mẽ

đi kèm với TensorFlow.

Nó cho phép chúng tôi theo dõi và trực quan hóa các số liệu khác nhau

trong quá trình đào tạo.

Đó là những gì?

Đó là sự mất mát, độ chính xác,

và thậm chí cả trọng số và thành kiến trong mô hình của chúng tôi.

Điều này giúp chúng tôi hiểu mô hình của chúng tôi đang học tập tốt như thế nào

và nơi chúng tôi có thể cần điều chỉnh

để làm cho nó thậm chí còn tốt hơn.

Bạn có thể hỏi, điều này thật tuyệt, nhưng tại sao chúng ta lại sử dụng nó?

Vâng, bởi vì nó cung cấp thông tin chi tiết theo thời gian thực

vào quá trình huấn luyện mô hình.

Nó giúp chúng ta chẩn đoán vấn đề

như trang bị quá mức hoặc thiếu trang bị

bằng cách trực quan hóa các số liệu,

và nó cũng tạo điều kiện cho việc điều chỉnh siêu tham số

bằng cách so sánh các đợt tập luyện khác nhau.

Vì vậy, hãy quay lại mã của chúng tôi

và kết hợp TensorBoard vào dự án của chúng tôi.

Vì vậy hãy tiếp tục và gặp tôi tại Codespaces của bạn.

Tìm thư mục SRC từ khung bên trái

và tìm tệp Python 04_01_begin.

Vì vậy, hãy bắt đầu với thiết lập ban đầu

cho mô hình TensorFlow của chúng tôi

nơi chúng tôi sẽ sử dụng

lại tập hợp dữ liệu nhà ở California.

Chúng tôi sẽ chia nhỏ từng bước

để xem TensorBoard phù hợp với quy trình làm việc của chúng tôi như thế nào tại đây.

Để bắt đầu, chúng ta sẽ bắt đầu từ tập tin bắt đầu

và sau đó chúng ta sẽ kết thúc bằng tệp Python 04_01_end

từ khung bên trái trong thư mục SRC.

Vì vậy, hãy bắt đầu từ tập tin bắt đầu

và đi đến tập tin cuối cùng.

Trước hết, chúng tôi bắt đầu với việc kết hợp các thư viện.

Lưu ý rằng chúng tôi có một bổ sung ở đây,

đó là từ tensorflow.keras.callbacks nhập TensorBoard.

Đó là nơi chúng tôi mời TensorBoard tham gia dự án của mình.

Trong khối mã ban đầu mà tôi đang nhấn mạnh ở đây,

chúng tôi đang nhập tất cả các thư viện cần thiết

từ TensorFlow.keras.callbacks nhập TensorBoard

là phiên bản mới.

Đó là chìa khóa để kích hoạt tính năng giám sát thời gian thực của chúng tôi ở đây.

Tiếp theo, chúng ta chuyển sang tải và chuẩn bị dữ liệu.

Đầu tiên, chúng ta cần tải và chuẩn bị tập dữ liệu của mình.

Một lần nữa, chúng tôi đang sử dụng bộ dữ liệu nhà ở California

cho bài tập này.

Chúng tôi tải dữ liệu, sau đó thực hiện phân chia,

và chúng tôi tạo thêm xác thực X bằng cách xác thực đào tạo và Y.

Xin nhắc lại, bộ xác thực sẽ giúp chúng tôi theo dõi

mô hình của chúng tôi khái quát tốt như thế nào

đến dữ liệu chưa được nhìn thấy trong quá trình đào tạo.

Vì vậy, sau đó, chúng tôi tiếp tục tiêu chuẩn hóa.

Chúng tôi sử dụng bộ chia tỷ lệ tiêu chuẩn, chúng tôi biến đổi tàu X,

và chúng tôi chuyển đổi các tập dữ liệu kiểm tra X và xác thực X.

Bước tiếp theo là xác định mô hình.

Hãy tiếp tục và thu nhỏ khung bên trái này.

Vì vậy, chúng tôi thấy nhiều mã hơn ở đây.

Chúng ta sẽ xây dựng một mạng lưới thần kinh đơn giản ở đây,

giống như chúng tôi đã làm lần trước.

Một lần nữa, chúng ta có hai lớp ẩn

với chức năng kích hoạt của relu và 30 tế bào thần kinh

cũng như một lớp đầu ra ở đây.

Bạn có thể hỏi tại sao chúng ta chỉ sử dụng một nơ-ron

trong lớp đầu ra?

Bởi vì chúng tôi đang dự đoán giá trị duy nhất này

giá nhà ở đây.

Tiếp theo chúng ta sẽ biên dịch mô hình.

Điều này liên quan đến việc xác định trình tối ưu hóa và hàm mất mát.

Chúng tôi sẽ sử dụng trình tối ưu hóa adam

và chúng tôi đang sử dụng sai số bình phương trung bình làm hàm mất mát.

Đây là tiêu chuẩn cho các nhiệm vụ hồi quy.

Bây giờ hãy tiếp tục và thiết lập TensorBoard.

Đây là lúc TensorBoard phát huy tác dụng.

Chúng ta sẽ thiết lập một callback ghi lại dữ liệu cho TensorBoard

trong quá trình đào tạo.

Vậy chúng ta làm điều đó như thế nào?

Chúng tôi tạo một log_dir, đây là thư mục nhật ký.

Điều đó bao gồm ngày và giờ hiện tại.

Điều này giúp chúng tôi theo dõi các đợt đào tạo khác nhau

và cuộc gọi lại TensorBoard sẽ ghi dữ liệu vào thư mục này

và chúng ta có thể hình dung nó sau bằng cách sử dụng TensorBoard.

Tiếp theo, chúng ta có một phần giữ chỗ cho việc đào tạo.

Vì vậy, chúng ta sẽ tiếp tục và tiếp tục từ đây.

Vì vậy, hãy tiếp tục và đào tạo mô hình ở đây.

Vì vậy, chúng ta sẽ nói lịch sử tương đương với model.fit

và chúng ta đã khá quen thuộc với bước này.

Chúng tôi đã làm điều này một vài lần.

x_train, y_train, cho nó 20 kỷ nguyên,

dữ liệu xác thực là xác thực X, xác thực Y,

và điều mới ở đây là các lệnh gọi lại.

Vì vậy, chúng ta sẽ gọi các cuộc gọi lại bằng với cuộc gọi lại bảng tenorboard.

Vì vậy ở bước này,

chúng tôi đang đào tạo mô hình trong 20 kỷ nguyên.

Dữ liệu xác thực giúp chúng tôi theo dõi hiệu suất

và cuộc gọi lại TensorBoard ghi lại mọi thứ.

Sau khi chạy cái này,

chúng ta có thể khởi động TensorBoard để trực quan hóa quá trình đào tạo.

Tiếp theo, chúng ta chuyển sang đánh giá mô hình.

Vì vậy, sau khi đào tạo xong,

bây giờ là lúc chúng ta đánh giá mô hình trên dữ liệu thử nghiệm

để xem nó hoạt động tốt như thế nào trên dữ liệu không nhìn thấy được.

Vì vậy, chúng ta sẽ lại sử dụng sai số bình phương trung bình.

Chúng ta có thể thực hiện đánh giá sms_test bằng model.evaluate,

và sau đó chúng ta sẽ có x_test và y_test.

Tiếp theo, như mọi khi, chúng ta sẽ tiếp tục in cái này,

Lỗi bình phương trung bình trên tập kiểm tra, mse_test.

Vì vậy chúng ta đang đánh giá mô hình trên tập kiểm tra

và sai số bình phương trung bình

cung cấp cho chúng tôi một thước đo tốt về hiệu suất của nó ở đây.

Tiếp theo chúng ta sẽ tiếp tục

và hình dung sự mất mát trong quá trình đào tạo và xác thực.

Vì vậy, hãy tiếp tục và làm điều đó.

Chúng ta sẽ tạo ra một chức năng mới.

Trước hết hãy bình luận tiêu đề của việc chúng ta đang làm.

Vì vậy, đây là một chức năng để vẽ sơ đồ mất mát đào tạo và xác nhận.

Vì vậy, chúng ta sẽ tiếp tục và tạo một hàm ở đây.

Vì vậy nó sẽ được gọi là lô_loss,

và nó sẽ mang lịch sử đến đây.

Tiếp theo chúng ta sẽ tiếp tục và plt.plot

và chúng ta sẽ kết hợp sự mất mát trước tiên,

vậy history.history,

dấu ngoặc đơn mở và mất, dấu phẩy, nhãn,

và chúng tôi sẽ gắn nhãn nó là Mất mát.

Chúng ta đừng quên trích dẫn kết thúc ở đây.

Dấu ngoặc luôn cho chúng ta biết bằng cách thay đổi màu sắc.

Vậy hãy chuyển sang dòng khác, plt.plot.

Lần này, chúng ta sẽ xử lý việc mất xác thực.

Vì vậy, history.history,

và sau đó chúng tôi sẽ gọi mất xác nhận ở đây.

Hãy chắc chắn rằng chúng ta có dấu gạch dưới.

Nhãn tiếp theo là mất xác nhận.

Khi đó chúng ta có nhãn X, plt.xlabel,

và nó sẽ có các kỷ nguyên.

Nhãn Y sẽ bị mất, plt.ylabel.

Đó sẽ là Mất mát, và sau đó hãy tiếp tục.

Chúng ta sẽ có plt.legend.

Tiếp theo chúng ta sẽ có plt.grid, True,

sau đó chúng ta sẽ tiếp tục,

và lưu nó vào thư mục đầu ra, vậy hãy thực hiện điều đó.

đầu ra plt.savefigure,

và sau đó hãy đặt tên cho chương

và tên phiên loss_plot.png.

Được rồi, đây là âm mưu mất mát của chúng ta.

Đây là chức năng và bây giờ chúng ta sẽ tiếp tục

và gọi âm mưu này và cứu lấy sự mất mát.

Chúng ta hãy chú ý đến chữ thường và chữ hoa ở đây,

và sau đó chúng ta sẽ gọi hàm story_loss history.

Vì vậy, hãy tiếp tục và xem lại những gì chúng tôi đã làm.

Tôi đã nhận thấy lỗi đánh máy ở đây,

vì vậy chúng ta hãy tiếp tục và sửa nó thành nhãn.

Vì vậy, chúng tôi đã xác định hàm mất đồ thị,

xử lý sự mất mát và mất mát xác thực,

và chúng tôi gắn nhãn trục X là kỷ nguyên, trục Y là mất mát.

Chúng tôi làm truyền thuyết, chúng tôi chăm sóc lưới điện,

và chúng tôi lưu hình vào thư mục đầu ra.

Sau đó chúng tôi gọi chức năng này

để chạy chức năng trên lịch sử ở đây.

Được rồi, tuyệt, và khi chúng ta cuộn lên, hãy luôn đảm bảo

rằng chúng tôi đã viết mọi thứ một cách chính xác.

Vì vậy tôi nhận thấy rằng chúng ta nên có model.fit ở đây.

Hoàn hảo.

Luôn kiểm tra lại mọi thứ.

Vì vậy, những gì chúng tôi đã làm ở đây là chúng tôi đã đào tạo mô hình ở đây.

Lịch sử tương đương với model.fit, x_train, Y_train,

kỷ nguyên bằng 20.

Chúng tôi đã cung cấp dữ liệu xác thực và chúng tôi đã cung cấp các lệnh gọi lại.

Tiếp theo, chúng tôi đánh giá mô hình

và sau đó chúng tôi sẽ in ra

sai số bình phương trung bình trên tập kiểm tra.

Tiếp theo, chúng ta xác định hàm

để vẽ sơ đồ mất mát đào tạo và xác nhận.

Cuối cùng, chúng ta gọi hàm đó để lưu số liệu tổn thất.

Tuyệt vời.

Vì vậy, hãy tiếp tục và mở tệp Python 04_01_end

để so sánh công việc của chúng tôi.

Hãy chắc chắn rằng nó phù hợp

với những cập nhật mà chúng tôi đã thực hiện đối với tệp bắt đầu,

và sau khi bạn xác minh rằng nó phù hợp,

chúng ta hãy tiếp tục và chạy cái này.

Được rồi, kịch bản của chúng ta đã kết thúc

với sai số bình phương trung bình là 0,32 khi được kiểm tra.

Tiếp theo, chúng ta sẽ kết hợp TensorBoard.

Vì vậy trước tiên chúng ta sẽ điều hướng đến thư mục

nơi nhật ký của chúng tôi được lưu,

và chúng ta sẽ chạy lệnh trong terminal để mở nó lên.

Vì vậy, hãy tiếp tục và làm điều đó.

Trước hết, chúng ta hãy đi tìm nơi lưu nhật ký của chúng ta.

Chúng tôi đã cung cấp điều này trong mã.

Chúng được lưu trong thư mục logs/fit,

nên chúng được lưu ngay tại đây.

Vì vậy đây là một thông tin tuyệt vời cần ghi nhớ

bởi vì đó là những gì chúng tôi sẽ cung cấp ngay bây giờ.

Đây là điểm mấu chốt của phiên này.

Vì vậy chúng ta sẽ tiếp tục và kết hợp TensorBoard

bằng cách gõ tensorboard trên thiết bị đầu cuối

và sau đó là thư mục --logged.

Đây là nơi chúng tôi cung cấp nơi lưu trữ nhật ký của chúng tôi.

Vì vậy, chúng tôi đã cho nó là log/fit từ mã của chúng tôi ngay tại đây,

vì vậy đó là những gì chúng tôi đang cung cấp ở đây.

Vì vậy, hãy tiếp tục và nhấp vào chạy để thực hiện việc này.

Vì vậy, những gì nó sẽ làm là cung cấp cho chúng ta một URL,

và chúng ta sẽ tiếp tục và mở cái này

bằng cách nhấp vào điều khiển và nhấp chuột.

Vì vậy, nó sẽ mở ra một trang web mới cho chúng ta,

và đây là cách chúng tôi theo dõi và hình dung

đào tạo của người mẫu.

Điều đó rất quan trọng cho các dự án học máy thành công.

Đây là một công cụ rất, rất quan trọng

để theo dõi và phân tích kết quả của chúng tôi.

Vậy chúng ta đang thấy gì ở đây?

Vâng, ở bảng bên trái,

chúng tôi có một số hoạt động đào tạo được liệt kê,

mỗi cái được xác định bằng dấu thời gian và nhãn,

chẳng hạn như đào tạo và xác nhận.

Những màu sắc khác nhau mà chúng ta thấy

đại diện cho các lần chạy hoặc tập dữ liệu khác nhau,

ví dụ, đào tạo và xác nhận.

Các hoạt động này được tổ chức theo ngày và giờ,

cho phép chúng tôi so sánh các buổi đào tạo khác nhau.

Và một thư mục ở đây được thể hiện bằng tên thư mục.

Để thể hiện điều đó, chúng ta có thể cấu trúc nó theo ngày

hoặc chúng ta có thể cấu trúc nó theo tên chương hoặc tên thư mục,

bất cứ điều gì phù hợp với nhu cầu dự án của bạn trong tương lai.

Sau đó, chúng tôi thấy một số tab ở trên.

Vì vậy chúng ta thấy chuỗi thời gian, thước đo tỷ lệ,

đồ thị, phân phối và biểu đồ.

Chuỗi thời gian là nơi chúng tôi hiện đang tập trung,

hiển thị cách số liệu phát triển theo thời gian,

và khi chúng ta nhấp vào bộ chia tỷ lệ,

điều này theo dõi các số liệu như mất mát và độ chính xác.

Khi chúng ta nhấp vào biểu đồ,

chúng ta có thể hình dung kiến trúc mô hình ở đây

và tìm hiểu thêm về các mô hình.

Và khi chúng ta nhấp vào phân phối và biểu đồ,

những điều này cho thấy sự phân bố trọng số và độ lệch

qua các lớp trong mô hình theo thời gian.

Bây giờ chúng ta hãy quay lại chuỗi thời gian

và nói về thẻ biểu đồ thiên vị.

Vì vậy bảng điều khiển chính hiển thị biểu đồ

về những thành kiến trong các lớp của mô hình của chúng tôi.

Những biểu đồ này cho thấy độ lệch được phân bổ như thế nào

sau mỗi bước hoặc giai đoạn huấn luyện,

cung cấp cái nhìn sâu sắc về

các tham số của mô hình đang phát triển như thế nào trong quá trình đào tạo.

Chúng ta cũng thấy các màu sắc khác nhau như tím, cam.

Chúng tương ứng với các hoạt động đào tạo khác nhau.

Điều này cho phép chúng ta so sánh

cách phân phối thay đổi qua các lần chạy.

Sau đó chúng ta có bảng cài đặt.

Trong bảng cài đặt, chúng ta thực sự có thể mở rộng hoặc ẩn nó.

Vì vậy, trong bảng cài đặt,

chúng ta có thể xem và điều chỉnh hình ảnh.

Vì vậy chúng ta có thể thay đổi trục ngang

hoặc kích hoạt lựa chọn bước ở đây

và điều chỉnh độ mịn của các ô chia tỷ lệ.

Vì vậy, chúng ta có thể thực hiện các điều chỉnh cài đặt khác nhau ở đây.

Vì vậy, tất cả những điều này có nghĩa là gì, chúng ta có thể so sánh nhiều lần chạy.

Bảng điều khiển cho phép chúng tôi

để so sánh nhiều đợt huấn luyện cạnh nhau,

điều này rất hữu ích cho việc điều chỉnh siêu tham số

hoặc đánh giá tác động của những thay đổi

trong kiến trúc mô hình của chúng tôi.

Mặc dù chúng tôi có thể theo dõi tình trạng của mô hình

bằng cách hình dung sự phân bố của độ lệch hoặc trọng số,

chúng tôi có thể theo dõi tình trạng của mô hình trong quá trình đào tạo.

Ví dụ: nếu biểu đồ rất hẹp hoặc bị lệch,

nó có thể chỉ ra vấn đề

như độ dốc biến mất hoặc bùng nổ.

Và khi nói đến việc tinh chỉnh trực quan,

cài đặt cho phép chúng tôi tùy chỉnh cách hiển thị dữ liệu.

Nó làm cho việc giải thích kết quả dễ dàng hơn

và đưa ra quyết định về quá trình đào tạo của chúng tôi.

Nhìn chung, những gì chúng ta thấy trong bảng điều khiển TensorBoard này

là bước rất mạnh mẽ để theo dõi và so sánh

đào tạo các mô hình khác nhau

hoặc rus khác nhau của cùng một mô hình.

Điều này giúp chúng tôi đưa ra quyết định dựa trên dữ liệu

về điều chỉnh và cải tiến mô hình.