# 05 - Giải pháp kỹ thuật phân loại ảnh hiệu quả

---

(nhạc sôi động)

- Chà, tôi hy vọng bạn vui vẻ khi thực hiện thử thách này.

Bây giờ chúng ta hãy tiếp tục và xem xét giải pháp.

Chà, trong giải pháp này, chúng tôi sẽ lấy mã thử thách

từ phần trước

và thực hiện các sửa đổi cần thiết.

Cụ thể, chúng tôi sẽ thêm một lớp chập bổ sung

sang mô hình CNN nâng cao của chúng tôi.

Điều này sẽ giúp chúng ta thấy việc tăng độ sâu của mạng như thế nào

có thể cải thiện khả năng học hỏi của nó

và khái quát hóa từ dữ liệu.

Việc thêm các lớp vào mạng nơ-ron cũng tương tự

để bổ sung thêm nhiều tế bào thần kinh vào não người,

nên sẽ thông minh hơn nếu bạn nghĩ theo cách đó.

Chúng ta càng có nhiều tế bào thần kinh,

những mô hình phức tạp hơn mà chúng ta có thể nhận ra.

Tương tự, bằng cách thêm nhiều lớp hơn vào CNN của chúng tôi,

chúng tôi tăng công suất của nó

để nắm bắt các mẫu phức tạp trong hình ảnh.

Vì vậy, chúng ta hãy đi qua các giải pháp từng bước một.

Hãy tiếp tục và tìm tệp python 02_05_solution.

Và trước tiên chúng ta lại bắt đầu với việc nhập

các thư viện cần thiết.

Như thường lệ, chúng ta có hệ điều hành numpy, matplotlib,

Thư viện TensorFlow, sau đó chúng ta tiếp tục

để tải tập dữ liệu, đó là tập dữ liệu CIFAR-10.

Một lần nữa, chúng tôi đang làm việc với 60.000 hình ảnh.

Tiếp theo, chúng tôi xác định mô hình CNN cộng nâng cao,

đó là bài tập, thử thách của chúng tôi.

Vì vậy hãy tiếp tục và tìm nó vì phần còn lại của mã

đại loại là đang xem xét các chức năng tương tự mà chúng ta đã xem qua

trước đó, chẳng hạn như hiển thị hình ảnh để xem hình ảnh nào

chúng tôi đã làm việc với

và sau đó lưu nó cũng như tiếp tục

và hiển thị một mẫu hình ảnh đào tạo.

Vì vậy, bài tập cốt lõi của chúng tôi ở đây là xác định

một mô hình CNN nâng cao

với một lớp chập bổ sung,

mà chúng tôi gọi là mô hình cộng nâng cao.

Vì vậy chúng ta sẽ tiếp tục

và tạo một lớp chập mới ở đây,

mà tôi đã thực hiện trong giải pháp.

Như bạn thấy ở đây, chúng tôi đã thêm lớp Conv2D

với 256, hai nhân hai, tức là 256 bộ lọc

và mỗi lớp chập được theo sau

bởi một lớp chuẩn hóa hàng loạt

để ổn định quá trình học tập và thêm một lớp bỏ học

để ngăn chặn việc lắp quá mức.

Vì vậy, đây là mô hình CNN nâng cao của chúng tôi.

Tiếp theo, chúng ta biên dịch và huấn luyện mô hình như bình thường.

Chúng tôi thực sự sử dụng lại trình tối ưu hóa Adam

và hàm mất entropy chéo phân loại ở đây.

Sau đó, chúng tôi huấn luyện mô hình trên bộ dữ liệu CIFAR-10

trong 20 kỷ nguyên.

Vì vậy, sau khi xác định trình tối ưu hóa và phần mất mát,

chúng tôi tiếp tục và in bản tóm tắt mô hình,

và sau đó chúng tôi huấn luyện mô hình trên dữ liệu huấn luyện.

Chúng ta tiếp tục và lưu mô hình xe lửa

vào thư mục đầu ra, sau đó chúng ta tiếp tục

và lưu báo cáo hiệu suất,

đó là mô hình cộng nâng cao, biểu đồ số chính xác.

Chúng tôi tiếp tục và theo dõi biểu đồ này,

và sau đó chúng tôi đánh giá mô hình trên dữ liệu thử nghiệm

để có được số mất mát và độ chính xác.

Bây giờ chúng ta có thể tiếp tục và chạy cái này vì chúng ta đã có

mô hình cộng nâng cao được lưu trong thư mục đầu ra.

Nó sẽ tiếp tục và kiểm tra xem mô hình này có tồn tại hay không.

Nó đã tồn tại nên nó sẽ không tiếp tục nữa

và đào tạo lại mô hình này vì nó biết rằng nó ở đó.

Nó sẽ chỉ in ra báo cáo kiểm tra độ chính xác cho chúng tôi,

đó là con số chính xác của bài kiểm tra.

Nếu bạn thực sự muốn trước đó, hãy đi đến cốt truyện

và xem mô hình cộng nâng cao 02_05.

Đây là độ chính xác so với các kỷ nguyên mà chúng tôi có thể theo dõi ở đây.

Một lần nữa, nếu bạn muốn đào tạo lại điều này,

tất cả những gì bạn phải làm là vào các mô hình và tìm mô hình,

đó là mô hình CIFAR10_enhanced_plus.

Hãy tiếp tục và xóa cái này.

Đừng lo lắng về việc xóa vì chúng tôi không cam kết

và đẩy mã của chúng tôi vào kho lưu trữ,

vì vậy nó sẽ không gây hại gì cho repo.

Vì vậy chúng ta sẽ quay lại và tìm giải pháp.

Và nếu bạn muốn tạo lại cái này, hãy tiếp tục và chạy nó

bởi vì nó sẽ tìm kiếm mô hình cộng nâng cao đó

và nó sẽ không tìm thấy nó.

Nó sẽ tiếp tục và tạo mô hình

và sử dụng 20 kỷ nguyên như chúng tôi đã xác định.

Và sau khi hoàn thành 20 kỷ nguyên đó, nó sẽ tiếp tục

và cho chúng tôi hiệu suất của mô hình,

cũng như lưu các ô vào thư mục ô đầu ra.

Vì vậy, sẽ mất vài phút để chạy qua các kỷ nguyên

từ một đến 20 nên bạn có thể đợi nhé

và sau khi hoàn tất, bạn sẽ thấy con số chính xác

và sau đó bạn có thể tiếp tục và kiểm tra.

Mô hình được lưu trong thư mục đầu ra,

và cốt truyện được lưu trong thư mục lô đầu ra.

Vì vậy, sau khi chờ đợi một vài phút, chúng ta sẽ thấy

rằng tất cả 20 kỷ nguyên hiện đã hoàn thành và nó sẽ tiếp tục

và cung cấp cho chúng tôi kết quả chính xác của tất cả,

và nó sẽ lưu mô hình

và cốt truyện vào thư mục đầu ra.

Vì vậy, đây là thư mục đầu ra.

Nó đã lưu cốt truyện dưới cốt truyện 02_05_end_enhanced_plus_model.

Vì vậy, chúng ta có thể thấy biểu đồ độ chính xác ở đây,

và chúng ta có thể thấy mô hình cộng nâng cao hiện cũng đã được lưu

vào thư mục đầu ra.

Vì vậy, điều này kết thúc giải pháp thách thức của chúng tôi.