# 01 - Cơ bản về xử lý ảnh

---

- [Giảng viên] Vậy ở phần này,

chúng ta sẽ tìm hiểu những điều cơ bản về xử lý hình ảnh,

nhưng trước hết hãy quyết định xem hình ảnh nào

chúng tôi thậm chí sẽ làm việc cùng.

Chà, chúng tôi sẽ làm việc với tập dữ liệu CIFAR-10.

Và hãy tiếp tục và liệt kê tất cả các lý do

tại sao chúng tôi chọn tập dữ liệu này.

Vâng, nó là viết tắt của

Bộ dữ liệu 10 của Viện nghiên cứu nâng cao Canada.

Đây là bộ dữ liệu được sử dụng rất rộng rãi để phân loại hình ảnh.

Nó bao gồm 60.000 hình ảnh màu 32x32

ở 10 lớp khác nhau.

Và ứng dụng của nó rất đa dạng,

chẳng hạn như điểm chuẩn, thuật toán học máy,

và đặc biệt là nhận dạng hình ảnh.

Vâng, tập dữ liệu này bao gồm hình ảnh của 10 lớp,

bao gồm máy bay, ô tô,

chim, mèo, hươu, chó,

ếch, ngựa, tàu và xe tải.

Chúng tôi có khá nhiều loại ở đây.

Nào, chúng ta hãy cùng điểm qua phần đào tạo và kiểm tra.

Nó có 50.000 hình ảnh đào tạo,

và nó có 10.000 hình ảnh thử nghiệm.

Định dạng dữ liệu.

Hình ảnh có kích thước 32x32 pixel, hình ảnh định dạng RGB.

Chà, tải và khám phá CIFAR-10 thì sao?

CIFAR-10 có thể được tải dễ dàng,

mà chúng ta sẽ thấy bằng cách sử dụng thư viện máy học

chỉ trong một hoặc hai dòng.

Và hình ảnh có thể được hình dung

để hiểu sự phân bố dữ liệu.

Khám phá dữ liệu giúp chuẩn bị dữ liệu

để đào tạo người mẫu.

Bây giờ chúng ta đã xem qua tập dữ liệu CIFAR-10,

bây giờ chúng ta hãy tìm hiểu những điều cơ bản về xử lý hình ảnh.

Vâng, chúng ta sẽ nói về việc xử lý hình ảnh.

Khi làm việc với dữ liệu hình ảnh,

tiền xử lý là một bước quan trọng.

Nó giúp bình thường hóa dữ liệu,

và nó giúp chuyển đổi nó

ở định dạng có thể được nạp một cách hiệu quả

vào các thuật toán học máy.

Hãy nhảy vào mã để xem chúng ta có thể xử lý việc này như thế nào.

Vì vậy, trước hết, hãy mở môi trường không gian mã của bạn.

Và tôi đang nhìn vào phía dưới bên trái

để đảm bảo rằng tôi đang ở trong không gian mã của mình.

Bây giờ, hãy tìm tệp 02_01_begin.python.

Hãy bắt đầu với việc nhập thư viện

mà chúng tôi sẽ làm việc cùng.

Vì vậy, trước tiên, chúng ta sẽ nhập thư viện hệ điều hành.

Tiếp theo, chúng tôi sẽ nhập NumPy.

Again, the OS was the operating system library.

Tiếp theo, chúng tôi sẽ nhập NumPy dưới dạng np.

Tiếp theo, chúng ta sẽ nhập

matplotlib.pyplot dưới dạng plt.

Và đây là để vẽ hình ảnh.

Và thư viện tiếp theo mà chúng ta sẽ làm việc cùng

sẽ là TensorFlow.

Vì vậy, hãy nhập tensorflow.keras.

Và đây là nơi tập dữ liệu của chúng tôi xuất hiện.

Vì vậy, hãy tiếp tục và nói về tập dữ liệu.

Và từ số nhiều, bạn có thể biết có rất nhiều,

nhiều bộ dữ liệu mà bạn có thể chơi ở đây.

Và chúng ta sẽ chọn tập dữ liệu CIFAR-10

cho khóa học đặc biệt này.

Vì vậy, từ tensorflow.keras.utils,

nhập vào_categorical.

Đây là một phần của bước tiền xử lý của chúng tôi.

Tiếp theo, chúng ta sẽ thực sự tiếp tục

và vô hiệu hóa các thiết bị GPU khỏi nền tảng của chúng tôi,

bởi vì chúng tôi đang chạy cái này trong không gian mã.

Và không gian mã, tại thời điểm ghi âm này,

không hỗ trợ GPU.

Vì vậy, chúng ta sẽ tiếp tục và làm

vô hiệu hóa các hoạt động tùy chỉnh oneDNN.

Và sau đó để làm điều đó, chúng ta sẽ gọi OS.environment.

Và sau đó nó sẽ tự động hoàn thành cho chúng tôi,

và chúng tôi sẽ nói TF_ENABLE_ONEDNN_OPTS.

Và điều này bằng không.

Vì vậy, chúng tôi đã tiếp tục và vô hiệu hóa nó.

Chúng tôi sẽ tiếp tục và đảm bảo

rằng TensorFlow chỉ sử dụng CPU.

Vì vậy, chúng tôi sẽ làm điều đó bằng cách nói

đảm bảo TensorFlow chỉ sử dụng CPU.

Và chúng ta sẽ tiếp tục với OS.environment.

Và chúng tôi sẽ nói CUDA_VISIBLE_DEVICES

bằng chuỗi rỗng.

Và sau đó chúng ta sẽ tiếp tục nhập TensorFlow.

Dòng chảy căng như tf.

Và sau đó chúng ta sẽ nói tf.config.set_visible_devices,

mở và đóng dấu ngoặc đơn và chúng ta sẽ nói GPU.

Được rồi, chúng ta đã vô hiệu hóa GPU thành công

và làm việc với CPU.

Bây giờ là thời điểm tốt để tải tập dữ liệu.

Vì vậy, hãy tiếp tục và thực hiện việc tải đó ở đây.

Vì vậy, hãy nhớ rằng chúng ta đang sử dụng tập dữ liệu CIFAR-10,

trong đó bao gồm 60.000 hình ảnh.

Vì vậy, chúng ta sẽ tiếp tục nói x_train và y_train,

dấu ngoặc đơn đóng,

sau đó hãy tiếp tục và nhập bài kiểm tra.

Đầu tiên là X_test và sau đó là y_test.

Sau đó chúng ta sẽ tiếp tục và nói dữ liệu cifar10.load.

Thế thôi.

Khi chúng ta nói dữ liệu tải, nó thực sự sẽ tiếp tục

và tải nó cho chúng tôi.

Hãy tiếp tục và hoàn thành nó,

Load_data, mở và đóng dấu ngoặc đơn.

Thế là xong.

That's as simple as that.

Vì vậy, chúng ta sẽ có 60.000 bộ dữ liệu chỉ với một dòng.

Tiếp theo, chúng ta sẽ thực hiện một số thao tác chuẩn hóa.

Vì vậy, vì lợi ích của tốc độ,

các ý kiến ​​có thể được viết tắt một chút.

Để biết thêm chi tiết, vui lòng tham khảo tệp Python cuối

cho cùng một phần.

Được rồi, để bình thường hóa,

chúng tôi sẽ thực hiện X_train bằng

X_train dưới dạng float32 chia cho 255.

Được rồi, vì vậy chúng tôi đang bình thường hóa các giá trị này ngay bây giờ.

Vì vậy, khi chúng tôi chia tỷ lệ các giá trị pixel thành 0 và 1,

giống như chúng tôi làm, chúng tôi sẽ chuẩn hóa tập dữ liệu này,

đó là một bước tiền xử lý phổ biến.

Bằng cách đó, nó đảm bảo rằng dữ liệu ở quy mô tương tự.

Vì vậy điều này cũng giúp cho mô hình

hội tụ nhanh hơn trong quá trình huấn luyện.

Bây giờ hãy làm điều tương tự cho X_test.

X_test.astype, sau đó tiếp tục và nói float32.

Sau đó chúng ta sẽ tiếp tục nói chia cho 255.

Được rồi, tuyệt vời.

Chúng tôi cũng cần chuyển đổi các lớp học của chúng tôi

đến các vectơ được mã hóa một nóng.

Vì vậy, mã hóa one-hot một lần nữa là

rất cần thiết cho nhiệm vụ phân loại phân loại,

bởi vì nó biến đổi nhãn lớp

thành biểu diễn ma trận nhị phân.

Bây giờ hãy tiếp tục và chuyển đổi nhãn lớp

tới các vectơ được mã hóa một nóng tiếp theo.

Vì vậy, tôi sẽ nói chuyển đổi nhãn lớp

đến các vectơ được mã hóa một nóng.

Được rồi, một lần nữa, điều này là cần thiết cho việc phân loại theo phân loại.

Vì vậy, những gì chúng tôi làm là Y_train bằng to_categorical,

đơn giản như vậy.

Chỉ một dòng thôi cũng có tác dụng với chúng ta,

Y_train, sau đó chúng ta sẽ tiếp tục và nói 10.

Được rồi, tiếp theo chúng ta sẽ tiếp tục và làm điều tương tự

cho X_test bằng,

hãy sửa lại các khoảng trống cho phù hợp.

Được rồi, nó sẽ được phân loại,

và tiếp theo chúng ta sẽ nói Y_test, 10.

Được rồi, bây giờ là thế này.

Chúng tôi có 10 lớp, vì vậy chúng tôi định nghĩa nó là 10.

Bây giờ hãy xác định nhãn của tập dữ liệu.

Vì vậy, hãy làm điều đó tiếp theo.

Vì vậy, các nhãn, thực ra, hãy bình luận nó.

Labels would be.

Nhãn bằng, bắt đầu danh sách,

và nó sẽ bao gồm, một lần nữa, máy bay, ô tô,

tiếp theo chúng ta có con chim, tiếp theo chúng ta có con mèo,

và sau đó chúng ta có con nai,

và sau đó chúng ta có con chó,

tiếp theo chúng ta có con ếch,

và chúng tôi có những nhãn nào khác?

Vâng, chúng ta có ngựa, tàu, và sau đó là xe tải.

Vì vậy, hãy tiếp tục và thêm chúng,

ngựa, tàu, rồi xe tải.

Hoàn hảo.

Vậy là bây giờ chúng ta đã có danh sách nhãn,

trong đó bao gồm 10 nhãn.

Hoàn hảo.

Vậy chúng ta phải làm gì tiếp theo?

Thôi, chúng ta hãy tiếp tục và dành một chút thời gian

cũng để xác minh sự biến đổi của chúng tôi

bằng cách in các hình dạng của tập dữ liệu của chúng tôi tiếp theo.

Điều này giúp đảm bảo rằng các bước xử lý trước dữ liệu của chúng tôi

đã được thực hiện chính xác.

Vì vậy, đối với điều này, chúng ta sẽ tiếp tục

và thêm một số chức năng in ngay tại đây,

sẽ in hình X_train,

in hình dạng X_test,

in hình dạng Y_train,

và in hình dạng Y_test.

Được rồi.

Tiếp theo, chúng ta sẽ xác định thư viện đầu ra cho mô hình của mình.

Một lần nữa, thư viện đầu ra này cũng sẽ đề cập đến

vào thư viện đầu ra trong thư mục của chúng tôi ngay tại đây.

Vì vậy, chúng ta hãy tiếp tục và làm điều đó.

Thư viện đầu ra.

Và thư viện đầu ra của chúng tôi sẽ là thư mục đầu ra bằng,

và sau đó chúng tôi sẽ đưa ra toàn bộ con đường.

Tiếp theo, chúng tôi sẽ cung cấp thư mục cốt truyện

nơi chúng tôi muốn lưu những lô này.

Một lần nữa, hãy nhớ rằng, vì trong không gian mã,

Rất tiếc, cốt truyện.show sẽ không mở ra

một cửa sổ mới giống như trong Visual Studio Code cục bộ.

Vì vậy, như một giải pháp thay thế, chúng tôi thực sự đang lưu lại từng ô

vào thư mục lô đầu ra.

Vì vậy, chúng ta sẽ tiếp tục và nói thư mục cốt truyện,

và sau đó chúng ta sẽ nói story_path = OS.path.join,

thư mục đầu ra, và sau đó vẽ sơ đồ.

Được rồi, đây là thư mục cốt truyện của chúng tôi.

Bây giờ, nếu đường dẫn cốt truyện của chúng ta không tồn tại thì sao?

Vì vậy, hãy tạo đường dẫn cốt truyện nếu nó không tồn tại.

Vì vậy, chúng ta hãy tiếp tục và làm điều đó ở đây.

Tiếp theo, thực ra chúng ta muốn xem tập dữ liệu này, phải không?

Chúng ta đã nói về tập dữ liệu này được một thời gian rồi,

nhưng chúng tôi vẫn chưa nhìn thấy một hình ảnh nào.

Vì vậy, hãy tiếp tục và viết một hàm

để hiển thị hình ảnh, phải không?

Vì vậy, hãy viết một hàm để hiển thị hình ảnh.

Được rồi.

Vì vậy, chức năng hiển thị hình ảnh này sẽ thực sự hoạt động

và hiển thị một số hình ảnh mẫu trong tập dữ liệu

mà chúng tôi đã tải ở đây,

và nó sẽ lưu nó vào thư mục đầu ra cho chúng ta.

Được rồi, và chúng ta muốn đặt tên cái này là gì?

Thực ra chúng ta muốn đặt tên nó như định nghĩa tên.

Vì vậy, chúng tôi muốn nói tệp cốt truyện bằng

có lẽ hình ảnh hiển thị sẽ là một cái tên thích hợp.

Và sau đó chúng tôi muốn hiển thị một mẫu hình ảnh đào tạo

với nhãn của họ.

Và sau đó chúng ta sẽ thực sự tiếp tục và chạy hàm

chúng ta vừa tạo và lưu nó vào thư mục đầu ra/lô.

Được rồi, đó là rất nhiều.

Vì vậy, hãy mở thư mục cuối

và xem lại những gì chúng tôi đã làm.

Chúng tôi đã nhập các thư viện cần thiết,

chúng tôi đã tắt GPU và chỉ bật CPU,

chúng tôi đã tải dữ liệu CIFAR-10,

chúng tôi đã chuẩn hóa nó giữa 0 và 1 bằng cách chia cho 255.

Sau đó, chúng tôi chuyển đổi nhãn lớp thành vectơ được mã hóa một lần.

Sau đó, chúng tôi đưa ra danh sách nhãn, bao gồm 10 lớp.

Và sau đó chúng tôi muốn mã in ra các hình dạng

of X_train, Y_train, and X_test, Y_test.

Tiếp theo, chúng tôi xác định một thư mục đầu ra.

Và tiếp theo, chúng tôi tiếp tục và tạo

một chức năng hiển thị hình ảnh để tìm và hiển thị

các hình ảnh từ thư mục CIFAR-10.

Bây giờ chúng ta hãy tiếp tục và chạy cái này.

Vì vậy, những cảnh báo này là bình thường và không có gì phải lo lắng.

Và như bạn thấy, cốt truyện đã được lưu

để các ô đầu ra hiển thị hình ảnh.

Vì vậy, chúng ta sẽ đi đến đầu ra, vẽ đồ thị, hiển thị hình ảnh.

Và ở đây chúng ta có một ví dụ về hình ảnh ở đây.

Hãy làm cho nó lớn hơn.

Và như bạn thấy, chúng ta có một số ví dụ về con tàu,

ngựa, chó, mèo, hươu, máy bay, ếch, mèo, ngựa.

Một lần nữa, đây là những điều ngẫu nhiên.

Vì vậy, chúng ta sẽ làm việc với tất cả những hình ảnh vui nhộn này.

Vì vậy, hãy tiếp tục.