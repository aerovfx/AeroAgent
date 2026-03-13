# 03 - Kiến trúc CNN nâng cao

---

- Bây giờ tiếp theo, trước khi chúng ta tiếp tục

đến các mạng lưới thần kinh tích chập tiên tiến,

hãy tóm tắt nhanh những gì chúng ta đã làm cho đến nay.

Vâng, chúng ta đã thảo luận về CNN cơ bản

và hiệu quả của chúng trong các nhiệm vụ nhận dạng hình ảnh.

Phiên này tập trung vào mô hình CNN nâng cao

kết hợp các kỹ thuật tiên tiến như chuẩn hóa hàng loạt

và bỏ học để cải thiện độ chính xác,

và quan trọng hơn là sự khái quát hóa.

Nào, hãy tiếp tục và tóm tắt những gì chúng ta đã làm trước.

Vì vậy, chúng tôi đã chuẩn bị trước dữ liệu.

Hãy nhớ rằng lần đầu tiên chúng tôi nhập thư viện,

sau đó chúng tôi tải tập dữ liệu CIFAR-10 chỉ bằng một dòng,

đã tải 60.000 hình ảnh, là hình ảnh màu 32x32

trong 10 lớp như máy bay,

ngựa, hươu, v.v.

Sau đó, điều chúng tôi đã làm là bình thường hóa các giá trị pixel

nằm giữa số không và một,

để mô hình của chúng tôi hiểu nó tốt hơn.

Tiếp theo, chúng tôi thực hiện mã hóa một lần,

đó là sự chuyển đổi của nhãn lớp

đến các vectơ được mã hóa một nóng.

Vâng, chúng tôi luôn hiển thị hình ảnh để chúng tôi thấy

những gì chúng tôi đang làm việc với.

Vì vậy, chúng tôi đã đi và hiểu rõ hơn về tập dữ liệu.

Chúng tôi đã hiển thị một mẫu hình ảnh đào tạo

với nhãn tương ứng của chúng.

Hãy bổ sung thêm mô hình CNN mà chúng ta đã xây dựng,

vì vậy nó sẽ bao gồm Conv2D, chuẩn hóa hàng loạt,

và các lớp bỏ học để cải thiện hiệu suất

và ngăn chặn việc trang bị quá mức.

Vì vậy, tiếp theo, chúng ta sẽ tiếp tục chia nhỏ các lớp này,

một lần nữa, Conv2D,

áp dụng các bộ lọc để phát hiện các tính năng.

Sau đó, tiếp theo chúng ta sẽ chuẩn hóa hàng loạt,

bình thường hóa đầu ra để tăng tốc độ đào tạo

và ổn định việc học tập.

Tiếp theo chúng ta sẽ có MaxPooling.

Một lần nữa, MaxPooling2D, giúp giảm kích thước không gian.

Chúng ta sẽ có một lớp bỏ học, giúp ngăn chặn việc trang bị quá mức

bằng cách loại bỏ các tế bào thần kinh trong quá trình huấn luyện.

Sau đó chúng ta sẽ có sự làm phẳng,

giúp chuyển đổi bản đồ đặc trưng 2D thành vectơ 1D.

Tiếp theo, chúng ta sẽ có các lớp được kết nối đầy đủ,

thực hiện việc phân loại.

Sau đó chúng ta sẽ tiếp tục và huấn luyện mô hình này

như chúng tôi vẫn thường làm, đó là biên soạn mô hình

sử dụng trình tối ưu hóa Adam

và hàm mất entropy chéo phân loại.

Sau đó chúng ta sẽ huấn luyện mô hình trong 20 kỷ nguyên

and we will validate using test data.

Tiếp theo, chúng ta sẽ đánh giá mô hình này trên dữ liệu thử nghiệm

để có được giá trị mất mát và độ chính xác.

Vâng, để kết luận, mô hình CNN nâng cao

với các lớp chuẩn hóa và bỏ học hàng loạt

cải thiện hiệu suất và giảm việc lắp quá mức.

Sự kết hợp của những kỹ thuật mà chúng ta đã nói đến

mang lại kết quả mạnh mẽ và chính xác hơn

mô hình phân loại hình ảnh,

và việc ghi nhớ sẽ ít hơn, nếu điều đó hợp lý.

Điều này kết thúc phần tóm tắt về những gì chúng ta sẽ làm,

và bây giờ chúng ta hãy tiếp tục và tập trung vào việc viết mã.

Bây giờ, trước khi chúng ta bắt đầu viết mã, tôi muốn

để nhấn mạnh tầm quan trọng của không gian mã một lần nữa.

Vì vậy, chúng tôi đi đến trang kho lưu trữ

và sau đó chúng tôi tìm thấy mã ở nút màu xanh lá cây,

và chúng tôi làm việc với mũi tên xuống ngay tại đây.

Vì vậy, với một số mục đích đơn giản,

bạn thực sự có thể mở ra nhiều không gian mã,

và sau đó trong mỗi không gian mã bạn có thể chọn

để làm việc trên một khía cạnh khác của chương trình này.

Một là CNN đơn giản,

cái còn lại sẽ là CNN tiên tiến, v.v.

Vì vậy, để chứng minh rằng tôi thực sự đã tạo ra một không gian mã mới

với một cái tên khác, sau đó tôi sẽ tiếp tục

đến ba dấu chấm rồi mở trong Visual Studio Code.

Vì vậy, bạn có thể làm tương tự và bạn thực sự có thể tiếp tục

và thậm chí xóa các khoảng trống mã bằng cách nhấp vào xóa,

và bạn có thể chọn làm việc

với nhiều không gian mã nếu bạn muốn.

Vì vậy, bây giờ chúng ta hãy nhập mã.

Bây giờ hãy mở mã của chúng tôi

và tìm tệp 02_03_begin.py.

Vì vậy chúng ta sẽ bắt đầu với tập tin bắt đầu này

và sau đó đi tiếp như mọi khi

vào tệp 02_03_end.python,

đó là mã cuối cùng

Vì thế bạn có thể chọn đi theo tôi,

hoặc bạn có thể chỉ cần đi đến cuối tệp python

và chỉ chạy tệp python cuối.

So let's go back to the begin file

và hãy cải thiện mô hình CNN đơn giản của chúng ta

thành một mô hình CNN nâng cao.

Vì vậy, mô hình này bao gồm các lớp 2D tích chập bổ sung,

các lớp chuẩn hóa hàng loạt,

và các lớp bỏ học để cải thiện hiệu suất

và ngăn chặn việc trang bị quá mức.

Vì vậy, hãy tiếp tục và bắt đầu thêm các lớp bổ sung đó

mà chúng ta đã nói đến để nâng cao mô hình của mình.

Vậy chúng ta hãy đến đây

và tạo một chức năng mới ở đây,

được gọi là tạo mô hình CNN nâng cao.

Vậy là chúng ta đã tạo được mô hình CNN đơn giản.

Chúng tôi thực sự sẽ tiếp tục

và tạo ra một thứ gọi là

tạo mô hình nâng cao.

Vì vậy, điều này tạo ra mô hình nâng cao, tương tự như mô hình đơn giản,

sẽ thực sự bắt đầu với một mô hình tương đương với tuần tự,

và nó thực sự sẽ bắt đầu liệt kê các lớp

bên trong tuần tự này.

Vì vậy, hãy tiếp tục và bắt đầu với điều đó.

Vì vậy, tôi sẽ bắt đầu lại với lớp Conv2D của chúng ta,

rồi tôi sẽ tiếp tục điền thông tin vào đây.

Vì vậy, các lớp này sẽ thực sự được áp dụng cho 32.

Tiếp theo chúng ta sẽ có Conv2D 64,

và khi đó chúng ta sẽ có 128 bộ lọc tương ứng.

Vì vậy, chúng ta đang bắt đầu với cái đầu tiên ngay bây giờ,

và sau đó mỗi kích thước của chúng sẽ là ba x ba.

Đây là ý nghĩa của nó và sau đó chúng ta sẽ tiếp tục

và cung cấp cho nó chức năng kích hoạt dưới dạng relu một lần nữa.

Tiếp theo chúng ta sẽ tiếp tục và thêm việc chuẩn hóa hàng loạt,

nhưng trước đó, hãy thực sự nhắc nhở bản thân

Relu đang làm gì.

Vì vậy, điều này một lần nữa giới thiệu tính phi tuyến tính vào mô hình

và giúp học các mẫu phức tạp.

Các lớp này giúp phát hiện các đặc điểm như cạnh, kết cấu,

và hình dạng trong các hình ảnh đầu vào mà chúng ta đang làm việc.

Bây giờ sau lời giải thích này, chúng ta hãy tiếp tục

và tạo chuẩn hóa hàng loạt ở đây.

Vì vậy, tôi sẽ tạo chuẩn hóa hàng loạt

rồi đóng và mở, tiếp theo là mở và đóng dấu ngoặc đơn.

Vì vậy, chuẩn hóa hàng loạt sẽ chuẩn hóa đầu ra

của lớp trước đó.

Nó giúp đẩy nhanh quá trình đào tạo cho chúng tôi,

và nó ổn định việc học tập.

Bằng cách giảm sự dịch chuyển hiệp phương sai bên trong,

nó thực sự cho phép sử dụng tỷ lệ học tập cao hơn

và nó làm giảm độ nhạy để khởi tạo.

Bây giờ, sau đó chúng ta sẽ tiếp tục

và tạo lớp MaxPooling2D.

Và một lần nữa, lớp MaxPooling này

giảm kích thước không gian,

đó là chiều cao và chiều rộng của bản đồ đặc điểm.

Nó giúp giảm đặc biệt là chi phí tính toán,

mà chúng tôi quan tâm và kiểm soát việc trang bị quá mức

bằng cách cung cấp một hình thức biểu diễn trừu tượng.

Vâng, trong trường hợp này, chúng tôi thực sự sẽ chọn kích thước tổng hợp

của hai nhân hai.

Vì vậy, hãy tiếp tục và làm điều đó.

Tiếp theo chúng ta sẽ đi và có một lớp bỏ học.

Và bỏ học là một kỹ thuật chính quy hóa

ngẫu nhiên làm rơi một phần tế bào thần kinh

trong quá trình đào tạo.

Vì vậy, điều này cũng ngăn mạng trở nên quá phụ thuộc

trên các tế bào thần kinh cụ thể.

Vì vậy, kết quả là nó làm giảm tình trạng trang bị quá mức cho chúng ta.

Trong mô hình này, chúng tôi thực sự tăng dần

tỷ lệ bỏ học từ 0,2 đến 0,5,

vì vậy chúng ta sẽ có nhiều hơn một lớp bỏ học,

và mỗi lần chúng tôi sẽ tăng nó từ 0,2

cho đến tận 0,5.

Sau đó, tiếp theo chúng ta sẽ chuyển sang phần làm phẳng.

Lớp này chuyển đổi bản đồ đặc trưng 2D thành vectơ 1D,

có thể được đưa vào các lớp được kết nối đầy đủ.

Khi đó chúng ta sẽ có các lớp được kết nối đầy đủ,

đó là nơi dày đặc,

và lớp dày đặc có 128 nơ-ron được kích hoạt bằng relu,

và lớp dày đặc cuối cùng có 10 nơ-ron,

một cho mỗi lớp trên tập dữ liệu Cifar10

chúng tôi đang làm việc với

với chức năng kích hoạt softmax

để xuất ra xác suất của lớp.

Bây giờ, tôi đã đi và lấp đầy tất cả các lớp này

bên trong mô hình CNN nâng cao

trong tệp Python 02_03_end.

Vậy chúng ta hãy tiếp tục và mở nó ra

và hãy tóm tắt lại những gì chúng ta đã làm.

Vậy mô hình CNN nâng cao này

bao gồm ba lớp chập

mỗi lớp theo sau là một lớp chuẩn hóa hàng loạt, như chúng ta thấy,

lớp MaxPooling 2D và lớp bỏ học.

The dropout layers have increasing rates

để dần dần ngăn chặn việc trang bị quá mức.

Bạn thấy nó bắt đầu bằng 0,2 và tiến tới 0,3, 0,4,

và sau đó là 0,5.

Sau khi làm phẳng các bản đồ đặc trưng, chúng ta có hai lớp dày đặc

với lớp cuối cùng sử dụng chức năng kích hoạt softmax

để xuất ra xác suất của lớp.

Bằng cách sử dụng chuẩn hóa hàng loạt,

chúng tôi đẩy nhanh quá trình đào tạo và ổn định việc học,

trong khi bỏ học giúp điều chỉnh mô hình

để tránh trang bị quá mức, điều này rất quan trọng.

Sự kết hợp các kỹ thuật này mang lại kết quả mạnh mẽ hơn

và mô hình phân loại hình ảnh chính xác.

Thôi chúng ta tiếp tục nhé

và đảm bảo thư mục đầu ra tồn tại

vì đây là nơi chúng ta sẽ đặt mô hình.

Tiếp theo, chúng ta sẽ xác định đường dẫn mô hình,

và nó sẽ được đặt tên là mẫu nâng cao Cifar10,

và nó sẽ nằm trong thư mục đầu ra ngay tại đây.

Như bạn thấy, tôi đã chạy những mô hình đó trước đây,

và đây là Cifar10_enhanced_model.h5.

Bây giờ chúng ta hãy tiếp tục.

Chúng tôi thực sự xem xét đầu tiên nếu mô hình đã tồn tại.

Chà, nếu mô hình đã tồn tại,

mã được tải từ mô hình hiện có.

Nếu không, nó sẽ tạo ra mô hình CNN nâng cao cho chúng ta khi đang di chuyển.

Sau đó, chúng tôi biên dịch mô hình bằng trình tối ưu hóa Adam

và hàm mất entropy chéo phân loại.

Tiếp theo, chúng tôi in bản tóm tắt mô hình

để hiểu kiến ​​trúc của nó.

Chúng tôi đào tạo mô hình bằng model.fit X_train Y_train.

Chúng tôi cung cấp cho nó các kỷ nguyên bằng 20, kích thước lô bằng 64,

sau đó chúng tôi cung cấp dữ liệu xác thực dưới dạng X_test và Y_test.

Sau đó chúng ta lưu mô hình đào tạo vào thư mục đầu ra.

Tiếp theo, chúng ta tiếp tục và lập một âm mưu

về việc mô hình này hoạt động tốt như thế nào, đó là biểu đồ độ chính xác,

mà chúng tôi gọi là 02_03_end_enhanced_model.png.

Tiếp theo, chúng tôi tiến hành in kết quả kiểm tra độ chính xác.

Vì vậy, khi chúng ta tiếp tục và chạy cái này,

chúng ta sẽ thấy rằng nó thực sự tìm thấy mô hình,

vì nó đã được lưu rồi,

bởi vì chúng tôi đã chạy cái này trước đây.

Nó sẽ tiếp tục và thực hiện các quy trình sau cho chúng tôi.

Những cảnh báo này chúng tôi thấy là bình thường và được mong đợi.

Vì vậy, tất cả đều tốt.

Trước hết, nó sẽ tiếp tục

và tải xuống dữ liệu từ tài nguyên.

Tiếp theo, nó sẽ tạo ra các hình dạng

và nó sẽ tải mô hình hiện có từ thư mục đầu ra,

và nó sẽ cho chúng ta điểm chính xác của bài kiểm tra.

Bây giờ, bạn thực sự có thể tiếp tục và mở phần cốt truyện

rồi tìm biểu đồ 02_03_end_enhance_model.png.

Tuyệt vời, nhưng nếu bạn thực sự muốn

tạo lại mô hình?

Chà, trong trường hợp này, điều bạn phải làm là tiếp tục

và xóa mô hình nâng cao ở đây, không phải dấu cộng nâng cao,

nhưng mô hình nâng cao và nhấp vào có.

Sau đó, bạn tiếp tục và chạy lại 02_03.

Điều này thực sự sẽ làm là nó sẽ đào tạo lại mô hình

từ đầu và nó sẽ lưu nó vào thư mục đầu ra,

và nó cũng sẽ tiếp tục ghi đè

biểu đồ cốt truyện 02_03_end_enhanced_model.png

để chứng minh sự thực hiện của giá trị.

Như chúng ta thấy, nó không tìm thấy nó trong thư mục đầu ra

bởi vì chúng tôi cố tình đi

và xóa mô hình để nó đào tạo lại mô hình

từ đầu.

Và nó sẽ trải qua 20 kỷ nguyên ở đây,

và sau đó, nó sẽ lưu mô hình,

và sau đó nó sẽ tiếp tục và lưu cốt truyện

để chúng tôi theo dõi xem mô hình đã hoạt động như thế nào.

Vậy đây là một mô hình kiến ​​trúc CNN nâng cao.