# 53 - Bài tập tổng quan về sổ tay dự án Keras Tiếng Anh

---

Chào mừng mọi người quay trở lại, trong bài giảng này, chúng tôi sẽ cung cấp cho các bạn cái nhìn tổng quan về dự án này

của khóa học sử dụng API Keris 2.0 nhạy cảm để thực hiện nhiệm vụ phân loại.

Bây giờ, đây là một trong những dự án lớn nhất trong toàn bộ khóa học.

Vì vậy, hãy tiếp tục và dành thời gian để thực sự xem tổng quan về những gì có trong sổ ghi chép.

Được rồi.

Vì vậy, nếu bạn mở thư mục chứa trong sổ ghi chép và cuộn xuống, bạn sẽ thấy hai dự án

sổ ghi chép liên quan.

Phần đầu tiên là Bài tập Dự án Keris, và phần tiếp theo là Giải pháp Bài tập Dự án Keris.

Ngay bây giờ, chúng tôi sẽ cung cấp cho bạn cái nhìn tổng quan về sổ ghi chép bài tập thực tế.

Và sau đó, trong loạt bài giảng tiếp theo, chúng tôi sẽ hướng dẫn bạn các giải pháp.

Vì vậy, hãy tiếp tục và bắt đầu bài tập dự án Keris.

Và chúng tôi sẽ sử dụng một tập hợp con của bộ dữ liệu LendingClub thu được từ Kagle.

Và bạn có thể kiểm tra liên kết ở đây.

Nhưng hãy nhớ, chúng tôi khuyên bạn không nên tải xuống tệp zip đầy đủ.

Đó thực sự là từ liên kết này .

Chúng tôi cung cấp một phiên bản đặc biệt của tệp này, phiên bản này thực sự có thêm một số tính năng kỹ thuật để bạn sử dụng.

làm.

Vì vậy, chúng tôi đã thêm một số tính năng bổ sung để bạn sử dụng nhằm thực hành về kỹ thuật tính năng và cách làm việc

với dữ liệu trông thực tế.

Đây là dữ liệu thực và chúng tôi thực sự đã thêm nhiều thông tin hơn vào một tập hợp con của dữ liệu đó.

Được rồi, LendingClub, nếu bạn chưa quen với nó thì về cơ bản thì đây là một công ty cho vay ngang hàng của Hoa Kỳ.

Nó có trụ sở tại San Francisco, California.

Và những gì nó làm là cung cấp các khoản vay cho mọi người và sau đó họ phải trả khoản vay đó với một số tiền nhất định

lãi suất.

Và đôi khi người ta sẽ không trả hết khoản vay đó.

Và công ty sẽ phải ghi lại điều đó được gọi là khoản giảm giá.

Về cơ bản, họ phải xóa khoản vay vì nó không được trả lại cho họ.

Vì vậy, cột trạng thái khoản vay sẽ chứa nhãn của chúng tôi cho loại cụ thể này.

Và chúng tôi sẽ cố gắng dự đoán dựa trên dữ liệu lịch sử và đặc điểm của khách hàng tiềm năng,

người đi vay tiềm năng, cho dù họ có vỡ nợ hay không.

Vì vậy, việc vỡ nợ được gọi là khoản giảm giá, hay họ sẽ trả lại đầy đủ khoản vay đã được trả đầy đủ?

Vì vậy, hãy ghi nhớ các số liệu phân loại mà bạn sẽ đánh giá khi đánh giá hiệu suất

mô hình của bạn.

Vậy là một vài ô đầu tiên đã được điền cho bạn.

Và vì thực tế có nhiều bộ dữ liệu Câu lạc bộ cho vay trên Kaggle nên chúng tôi có thông tin về vấn đề cụ thể này.

tập dữ liệu được điền cho bạn trong một bảng ở đây trong ô này để bạn có thể tiếp tục và kiểm tra các dữ liệu khác nhau

tính năng.

Vì vậy, ví dụ, E.A. tỷ lệ gạch dưới, đây là mô tả về nó.

Đó là lãi suất của khoản vay.

Vì vậy, nếu các mô tả cho các tính năng khác nhau có trong bộ dữ liệu này thì khá

một tập dữ liệu lớn với nhiều tính năng thú vị.

Vì vậy, chúng ta sẽ dành nhiều thời gian để hình dung và thực hiện phân tích dữ liệu thăm dò cũng như thực hiện

kỹ thuật tính năng cơ bản.

Và chúng tôi đã điền một ít mã khởi đầu để bạn đọc trong tệp.

Cũng như một chút thông tin gạch dưới FTS, bạn sẽ nhận thấy rằng chúng tôi thực sự có bảng này và những gì

chúng tôi đã làm là xây dựng một chức năng nhỏ cho bạn có tên là thông tin gạch dưới FT, chức năng này sẽ in ra tính năng

thông tin dựa trên cột chuỗi bạn cung cấp.

Vì vậy, ví dụ: nếu bạn nhìn thấy trục gạch dưới của cột chuỗi Morts, thì bạn có thể chuyển nó

vào hóa đơn này 10 feet, gạch dưới thông tin và nó sẽ in lại cho bạn mô tả thực tế

là số lượng tài khoản thế chấp.

Vì vậy, hãy tiếp tục và chạy.

Một vài ô đầu tiên này sẽ đọc trong tệp cho bạn và tôi cũng sẽ tạo chức năng thông tin này

Hãy gọi và sau đó ở dưới đây chúng tôi sẽ đọc dữ liệu thực tế cho bạn.

Và sau đó nó trông giống như thế này.

Lưu ý rằng sẽ có dữ liệu bị thiếu mà bạn sẽ phải xử lý và về cơ bản chúng tôi sẽ hướng dẫn bạn

cùng với dự án này.

Vậy là chúng ta đã thực sự đến được phần nhiệm vụ của dự án.

Và Phần một là phân tích dữ liệu thăm dò.

Và chúng tôi sẽ chỉ yêu cầu bạn tạo một số hình ảnh trực quan này.

Và hãy nhớ rằng, bạn có thể thực sự cần phải tìm kiếm trên Google và chúng tôi cung cấp các liên kết hữu ích về một số tác vụ nhất định

rằng chúng tôi có thể chưa trình bày cụ thể nhưng bạn có thể thực hiện chúng dựa trên những gì chúng tôi đã trình bày

hơn và phần khóa học về sự cố trực quan hóa dữ liệu.

Vì vậy, ví dụ: chúng tôi có bản đồ nhiệt để bạn xây dựng.

Và trong trường hợp bạn cần bất kỳ trợ giúp nào về vấn đề đó, chúng tôi có các liên kết ở đây để biết thông tin về bản đồ nhiệt, trợ giúp về việc thay đổi kích thước,

v.v. Và bạn có thể tiếp tục cuộn xuống.

Tôi muốn bạn tạo một số biểu đồ phân tán, một số biểu đồ hình hộp mà chúng tôi muốn bạn thực sự làm theo hướng dẫn

để xây dựng một số lô đất ở đây phù hợp dựa trên tải trọng.

Đó là liệu nó đã được thanh toán đầy đủ hay bị tính phí.

Và có mô tả ở đây về những gì bạn có thể làm.

Và sau đó chúng tôi muốn bạn tạo một biểu đồ thanh cho mỗi danh mục, có thể bắt đầu nhận ra nó.

Vì vậy, nó trông giống như thế này.

Bạn cũng có thể thay đổi bảng màu, v.v.

Vì vậy, về cơ bản chúng tôi có nhiều cốt truyện khác nhau để bạn thử sức.

Và nếu chúng ta cuộn xuống, phần tiếp theo là tiền xử lý dữ liệu và phần này ít liên quan hơn đến

thực sự trực quan hóa dữ liệu.

Và thực sự mục tiêu của chúng tôi ở đây là loại bỏ hoặc điền vào dữ liệu còn thiếu.

Chúng tôi muốn loại bỏ các tính năng không cần thiết hoặc lặp đi lặp lại và sau đó chúng tôi muốn chuyển đổi chuỗi phân loại

đặc trưng cho các biến giả.

Vì vậy, đây là nơi chúng tôi sẽ thực hiện nhiều kỹ thuật tính năng và phân tích tính năng.

Vì vậy, trước tiên hãy giải quyết, dữ liệu còn thiếu và chúng tôi có hướng dẫn ở đây để bạn làm theo

cùng và cách xử lý dữ liệu còn thiếu đó.

Sau đó, chúng ta sẽ kiểm tra những dữ liệu còn thiếu, xem chúng ta có thể giữ lại những gì, những gì chúng ta nên điền vào

và những gì chúng ta nên bỏ đi, sau đó chúng ta cũng sẽ bắt đầu xử lý dữ liệu phân loại.

Vì vậy, nếu chúng ta bắt đầu đi xuống đây, chúng ta sẽ bắt đầu xử lý dữ liệu phân loại.

Và chúng tôi cũng có một số nhiệm vụ thử thách để bạn theo dõi trực tiếp.

Và ở dưới đây, chúng ta tiếp tục xử lý từng loại tính năng theo cơ sở tính năng, v.v.

Và cuối cùng, sau khi xử lý tất cả kỹ thuật tính năng này, bạn nên sẵn sàng cho một chuyến tàu

tách nếu bạn gặp khó khăn trong bất kỳ nhiệm vụ kỹ thuật tính năng nào mà chúng tôi cố gắng đặt ra cho bạn ở trên

chuyến tàu này sẽ phân tuyến, hãy tiếp tục và tham khảo sổ ghi chép giải pháp của chúng tôi.

Và hãy nhớ rằng, bạn thực sự có thể lấy tập dữ liệu này và cố gắng tự mình xây dựng một mô hình mà không cần

nhất thiết phải làm theo các bước chính xác mà chúng tôi đã trình bày ở đây.

Mục tiêu chính của việc này là xây dựng một mô hình nhằm dự đoán lớp nhãn thực tế.

Đây là cách phân loại nhị phân.

Vì vậy, bạn thực hiện phân chia bài kiểm tra tàu của mình và sau đó, tùy ý, bạn có thể lấy mẫu cho thời gian đào tạo.

Vì vậy, mẫu chứa khoảng ba trăm chín mươi lăm nghìn mục.

Nếu bạn đang làm một chiếc máy tính tròn nhỏ hơn hoặc thứ gì đó thì đó không phải là GPU.

Chúng tôi có một ít mã mẫu ở đây để lấy một phần dữ liệu để huấn luyện.

Được rồi, sau khi thực hiện phân tách thử nghiệm tàu, bạn muốn chuẩn hóa dữ liệu, sau đó bạn tạo

mô hình.

Chúng tôi có một số thông tin đầu vào cho bạn ở đây.

Bạn có thể tạo bất kỳ mô hình nào bạn cảm thấy cần thiết, nhưng chúng tôi khuyên bạn nên sử dụng bảy mô hình,

tám tế bào thần kinh.

Việc ba mươi chín tuổi, 19 tuổi đến một tuổi về điều này là hoàn toàn tùy chọn.

Về cơ bản bạn có các lựa chọn không giới hạn.

Bạn có thể loay hoay bằng cách thêm vào các lớp bỏ học, v.v.

Và chúng tôi cũng có các liên kết để bạn kiểm tra tại đây.

Vì vậy, tôi khuyên bạn nên thêm các lớp bỏ học ngay lập tức và trong sổ tay Giải pháp, bạn có thể kiểm tra xem

ra ngoài là tốt.

Chúng tôi có cấu trúc mạng cụ thể này với tỷ lệ rớt 0,2 hoặc 20% cho mỗi

những lớp đó để cố gắng ngăn chặn việc trang bị quá mức.

Họ muốn bạn điều chỉnh mô hình đó trong ít nhất 25 kỷ nguyên và sau đó bạn sẽ tiếp tục ở đây, hãy lưu lại

mô hình, đánh giá hiệu suất mô hình của bạn, xem các biểu đồ này, những gì chúng tôi đã và đang làm và sau đó

cuối cùng đưa ra khách hàng này dưới đây.

Bạn sẽ đề nghị người này một mình.

Được rồi, sau đó bạn có thể kiểm tra kết quả và đó là dự án.

Cảm ơn.

Và chúng ta sẽ gặp bạn ở loạt bài giảng tiếp theo cuối cùng sẽ tìm ra giải pháp này

cuốn sổ.

Nếu bạn gặp khó khăn ở bất kỳ đâu trong bài tập dự án này, hãy tiếp tục và chỉ cần tham khảo sổ tay giải pháp

điều đó đã được điền cho bạn.

Tôi sẽ gặp bạn ở đó.