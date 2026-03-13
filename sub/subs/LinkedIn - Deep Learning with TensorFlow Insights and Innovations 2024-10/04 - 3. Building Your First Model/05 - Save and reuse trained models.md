# 05 - Lưu và sử dụng lại các mô hình đã đào tạo

---

- [Người hướng dẫn] Trong video này,

chúng ta sẽ khám phá

cách lưu và sử dụng lại các mô hình đào tạo trong TensorFlow.

Có thể lưu mô hình sau khi đào tạo

và tải nó sau là một bước rất quan trọng

trong bất kỳ dự án học máy nào.

Điều này cho phép chúng tôi chia sẻ mô hình của mình,

triển khai chúng vào môi trường sản xuất,

hoặc tiếp tục đào tạo họ sau này.

Hãy tiếp tục và mở thư mục SRC

từ môi trường Codespaces của chúng tôi.

Tìm tệp Python 03_05_begin.

Vì vậy, tệp Python này bao gồm

nơi chúng ta đã dừng lại trong phiên trước

và sau đó chúng ta sẽ tiếp tục và tiếp tục.

Ở đây chúng tôi đã xây dựng và đào tạo

một mạng lưới thần kinh Feedforward đơn giản

sử dụng bộ dữ liệu nhà ở California.

Mô hình bao gồm hai lớp dày đặc

và chúng tôi đã huấn luyện nó trong 20 kỷ nguyên,

nói cách khác, sự lặp lại.

Bây giờ chúng ta sẽ chuyển sang lưu mô hình đã được đào tạo này.

Hãy tiếp tục và làm điều đó.

Vì vậy, chúng ta sẽ có thể lưu mô hình

chỉ với một dòng đơn giản.

Vì vậy, hãy tiếp tục và đặt tiêu đề cho nhận xét này,

Lưu mô hình được đào tạo,

và chúng ta sẽ lưu mô hình này vào thư mục đầu ra

mà chúng tôi đã và đang làm việc cùng.

Vì vậy model.save và chúng ta sẽ lưu nó vào thư mục đầu ra,

03_05_train_model.h5.

Vì vậy, chúng ta tiếp tục và lưu mô hình đã được đào tạo.

Tiếp theo chúng ta sẽ tiếp tục và tải lại mô hình

và lần này chúng ta sẽ gọi nó là loading_model,

đã tải_model bằng Tensorflow .keras.models

và sau đó chúng ta sẽ gọi Load_model

và sau đó chúng ta sẽ tiếp tục và đi theo con đường tương tự

rằng chúng tôi đã chỉ định mô hình này sẽ được lưu.

Vì vậy, chúng tôi đang tải nó trở lại từ vị trí của nó.

Tiếp theo chúng ta sẽ tiếp tục và đánh giá mô hình đã tải

để xác nhận nó được tải chính xác.

Vì vậy, đánh giá mô hình được tải

để xác nhận nó được tải chính xác.

Vì vậy, chúng ta sẽ tiếp tục

và nói kết quả posted_test bằng loading_model.evaluate

và chúng ta sẽ nói x_test, dấu phẩy, y_test

và sau đó trả về từ điển là True.

Hãy tiếp tục và in cái này.

Vì vậy chúng ta sẽ nói

print f "Kết quả kiểm tra mô hình đã tải"

được Load_test_results, test_results.

Được rồi, vậy là nó sẽ in kết quả kiểm tra

cho mô hình được tải ở đây.

Tiếp theo chúng ta sẽ so sánh các dự đoán từ mô hình ban đầu

và mô hình được tải để đảm bảo rằng chúng giống hệt nhau.

Vì vậy hãy tiếp tục và làm điều đó tiếp theo.

So sánh các dự đoán từ mô hình ban đầu và mô hình được tải.

Chúng tôi sẽ tiếp tục và đưa ra những dự đoán ban đầu

bằng model.predict x_test

và sau đó là những dự đoán được tải mà chúng tôi sẽ so sánh

sẽ bằng với model.predict x_test đã tải.

Ở đây trước tiên chúng tôi tải mô hình đã lưu từ tệp .h5

sử dụng tf.keras.models.load_model,

sau đó chúng tôi đưa ra dự đoán trên tập dữ liệu thử nghiệm

với cả mô hình ban đầu và mô hình được tải.

Tiếp theo, chúng tôi sẽ xác minh rằng các dự đoán có giống nhau.

Vì vậy chúng ta sẽ khẳng định để xác minh

rằng các dự đoán đều giống nhau.

Vì vậy chúng ta sẽ sử dụng khẳng định tf.reduce_all

và sau đó chúng ta sẽ sử dụng tf.abs.

Sau đó chúng ta sẽ lấy

sự khác biệt của những dự đoán ban đầu,

đến từ những dự đoán

mà chúng tôi đang thực hiện ở đây, trừ đi những dự đoán đã tải,

đang đến từ mô hình được tải.

Những số này có nhỏ hơn một lũy thừa của âm năm không?

Vì vậy chúng ta đang so sánh sự khác biệt

giữa dự đoán ban đầu và dự đoán được tải

và kiểm tra xem sự khác biệt

nhỏ hơn 10 lũy thừa âm 5,

đó là một con số rất nhỏ, gần bằng không.

Và sau đó chúng ta có thể tiếp tục

và thêm dòng dự đoán này khác nhau

giữa mô hình ban đầu và mô hình đã tải nếu không phải như vậy,

vì vậy chúng tôi đưa ra điều này ở giữa dấu ngoặc kép.

Vì vậy, hãy tóm tắt lại những gì chúng tôi đã làm ở đây.

Chúng tôi khẳng định để xác minh rằng các dự đoán là giống nhau

giữa các dự đoán ban đầu và các dự đoán được tải.

Vì vậy, thao tác mà chúng tôi giới thiệu ở đây, tf.abs,

tính toán sự khác biệt tuyệt đối giữa các dự đoán

được thực hiện bởi mô hình ban đầu

và mô hình được tải cho từng phiên bản trong tập dữ liệu.

Kết quả là một giọng nam cao trong đó mỗi phần tử đại diện cho

sự khác biệt tuyệt đối

giữa các dự đoán tương ứng của hai mô hình.

Sau đó chúng ta tiếp tục và kiểm tra xem sự khác biệt đó có

nhỏ hơn 10 lũy thừa âm 5.

Nếu điều kiện được đánh giá là True,

chương trình tiếp tục thực hiện bình thường.

Nếu điều kiện là Sai,

sau đó chương trình sẽ đưa ra lỗi xác nhận

và thông báo lỗi sẽ là

dự đoán khác nhau giữa các mô hình ban đầu và được tải.

Cuối cùng, chúng ta sẽ làm gì với tf.reduce_all

được sử dụng để giảm kỳ hạn này

của các giá trị boolean từ so sánh này

thành một giá trị boolean duy nhất.

Nó trả về Đúng

nếu tất cả các phần tử trong tensor đều thỏa mãn điều kiện,

nói cách khác, nếu sự khác biệt nhỏ hơn

hơn 10 lũy thừa của âm 5

và sau đó rơi vào tình trạng khác với thông báo lỗi này.

Tuyệt vời.

Bây giờ chúng ta có thể chuyển sang phần hình dung tiếp theo.

Vì vậy chúng ta sẽ hình dung

dự đoán mô hình ban đầu và được tải tiếp theo,

để trực quan hóa các dự đoán mô hình ban đầu và được tải.

Vì vậy hãy tiếp tục và khởi tạo hình này,

vẽ hình đó,

và sau đó chúng ta sẽ cho kích thước hình là 14, 7

và sau đó chúng ta sẽ tiếp tục nói plt.plot.

Bắt đầu với những dự đoán ban đầu,

dán nhãn dự đoán mô hình ban đầu.

Hãy sửa lỗi đánh máy ở đây.

Những dự đoán ban đầu và chúng tôi gắn nhãn nó như vậy.

Sau đó chúng ta sẽ tiếp tục và nói plt.plot

đã nạp_predictions lần này

và sau đó chúng ta sẽ dán nhãn cho nó

dưới dạng nhãn tương đương với Dự đoán mô hình đã tải,

và sau đó để phân biệt giữa hai điều này,

hãy tiếp tục và sử dụng kiểu đường kẻ,

và sau đó hãy sử dụng kiểu đường nét đứt ở đây.

Được rồi, tiếp theo chúng ta sẽ đặt tiêu đề cho cốt truyện này là plt.title,

dự đoán mô hình ban đầu so với tải,

Sự phân loại mô hình gốc so với mô hình đã tải.

Tiếp theo chúng ta sẽ nói plt.xlabel

để đặt cho nó nhãn XX, là chỉ mục mẫu.

Sau đó bạn sẽ làm tương tự với nhãn Y

và nó sẽ có giá trị dự đoán.

Sau đó là huyền thoại plt.legend.

Sau đó, hãy tiếp tục và như mọi khi, hãy lưu hình ảnh trực quan này,

plt.savefigure

và cung cấp cho nó vị trí đầu ra

mà chúng tôi luôn sử dụng ở đây

cho bất kỳ nhân vật nào mà chúng tôi đang xây dựng.

Vì vậy, điều tương tự ở đây, 03, lần này là 05,

và hãy gọi nó là model_comparison.png.

Vì vậy, tuyệt vời.

Trong phần cụ thể này, chúng tôi đã lưu mô hình được đào tạo.

Chúng tôi đã tải lại mô hình.

Chúng tôi đã đánh giá mô hình được tải

để xác nhận nó được tải chính xác.

Chúng tôi so sánh các dự đoán từ các mô hình ban đầu và được tải.

Tiếp theo chúng tôi khẳng định để xác minh rằng các dự đoán là giống nhau.

Chúng ta tiếp tục và hình dung

dự đoán mô hình ban đầu và được tải.

Sau đó, cuối cùng chúng tôi lưu hình ảnh trực quan.

Nếu bạn đã cùng nhau viết mã thì thật tuyệt.

Nếu không thì cũng tuyệt vời.

Bạn có thể lấy lại ở file Python 03_04_end

và chạy thật nhanh.

Sau đó chúng ta sẽ mở hình mà chúng ta đã tạo

và nhìn vào kết quả đầu ra của mã của chúng tôi

và bắt đầu phân tích kết quả của chúng tôi.

Cho nó một vài phút

và sau đó chúng ta sẽ có thể xem kết quả của nó.

Vì thế sau vài phút,

chúng ta sẽ thấy kết quả kiểm tra loading_model

được in ngay tại đây.

Chúng tôi đặt tên cho chúng như vậy trong bản in của mã,

và sau đó khi bạn cuộn lên trên,

bạn sẽ thấy rằng chúng tôi đã đặt tên cho kết quả mô hình ban đầu

như kết quả kiểm tra,

vì vậy chúng ta sẽ có thể nhìn thấy nó ngay tại đây.

Vậy là chúng ta đã có kết quả thử nghiệm từ mô hình mà chúng ta đã tạo ở đây,

và tiếp theo chúng ta có kết quả kiểm tra mô hình đã tải

nơi chúng tôi đang tải lại mô hình

và in kết quả của nó ở đây.

Bạn sẽ nhận thấy rằng kết quả thử nghiệm từ mô hình ban đầu

và mô hình được tải giống hệt nhau, đó là những gì chúng tôi mong đợi.

Điều đó có nghĩa là mô hình đã được lưu thành công

và được tải mà không bị mất thông tin.

Điều này rất quan trọng vì nó khẳng định

rằng hiệu suất của mô hình vẫn nhất quán

trên các trường hợp khác nhau.

Vậy thực tế là các dự đoán hoàn toàn giống nhau

ngụ ý rằng quá trình lưu và tải mô hình

đã hoạt động hoàn hảo ở đây.

Nó bảo toàn trọng lượng, kiến trúc của mô hình,

và chức năng tổng thể.

Vì vậy, khi chúng tôi phóng to thiết bị đầu cuối, bạn có thể thấy kết quả,

cả hai, kết quả kiểm tra

và tải kết quả thử nghiệm mô hình cùng nhau tại đây,

và một lần nữa, xác nhận rằng chúng giống hệt nhau.

Tiếp theo, chúng ta sẽ mở thư mục đầu ra

và sau đó tìm hình mà chúng tôi đã tạo ở đây,

đó là 03_05_model_comparison.

Hãy thu nhỏ cửa sổ terminal

để chúng ta có thể thấy mô hình so sánh

và vẽ đồ thị lớn hơn một chút.

Vì vậy, màu xanh lam chúng ta thấy các dự đoán của mô hình ban đầu,

và màu cam chúng ta thấy các dự đoán mô hình đã tải.

Vì vậy, biểu đồ này chứng minh một cách hiệu quả rằng mô hình được tải

thực hiện giống hệt với mô hình ban đầu,

đảm bảo rằng các dự đoán của mô hình

đáng tin cậy và nhất quán

ngay cả sau khi được lưu và khôi phục.

Làm thế nào chúng ta có thể đưa ra kết luận đó?

Bởi vì trong cốt truyện này,

dự đoán của mô hình ban đầu và mô hình được tải

chồng lên nhau gần như hoàn hảo.

Thực tế là những dự đoán

cả hai mẫu đều không thể phân biệt được

xác nhận rằng quá trình lưu tải hoạt động chính xác,

duy trì tính toàn vẹn của mô hình ở đây.

Cốt truyện xác nhận một cách trực quan việc kiểm tra xác nhận mà chúng tôi đã thực hiện,

đảm bảo rằng bất kỳ sự khác biệt nhỏ về số lượng

giữa dự đoán của mô hình ban đầu và mô hình được tải

là không đáng kể và nằm trong giới hạn có thể chấp nhận được.

Tóm lại, cốt truyện này chứng minh một cách hiệu quả

rằng mô hình đã tải

thực hiện giống hệt với mô hình ban đầu.

Điều này đảm bảo rằng các dự đoán của mô hình

đáng tin cậy và nhất quán

ngay cả sau khi được lưu và khôi phục.

Ngoài ra, hãy chú ý trong cùng thư mục đầu ra,

chúng tôi đã lưu mô hình của mình ở đây dưới 03_05_train_model.h5.

Vì vậy, phần này tóm tắt cách lưu và tải lại mô hình.