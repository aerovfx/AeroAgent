# 01 - Chuẩn bị xây dựng mô hình deep learning trong Python

---

- [Người hướng dẫn] Trong video này,

bạn sẽ học cách nhập các thư viện cần thiết

cho việc học sâu cũng như cách nhập

và xử lý trước một tập dữ liệu mẫu

để học sâu trong Python.

Tôi sẽ chạy mã hoàn chỉnh trong tệp 04_01e.

Bạn có thể làm theo bằng cách hoàn thành các ô mã trống

trong tệp 04_01b.

Lưu ý rằng đây là lần đầu tiên trong chuỗi ba video

dạy bạn cách xây dựng mô hình deep learning

bằng Python bằng Keras.

Hãy bắt đầu.

Điều đầu tiên chúng ta làm là chọn kernel đó.

Vì vậy hãy chọn môi trường Python, Python 3.10.

Được rồi.

Và vì vậy phần đầu tiên của quá trình của chúng tôi ở đây

là nhập các thư viện cần thiết

mà chúng tôi sẽ sử dụng trong suốt hướng dẫn này.

Vì vậy, hãy tiếp tục và nhập NumPy, TensorFlow, Keras,

cũng như gói lớp.

Như vậy cảnh báo trên màn hình lúc này là được.

Gần như nó đang nói với chúng ta rằng chúng ta không thể sử dụng GPU

không được thiết lập cho môi trường này và điều đó không sao cả.

Chúng tôi sẽ không tận dụng GPU

cho bất kỳ công việc nào chúng ta sẽ làm hôm nay.

Được rồi, như tôi đã đề cập trước đó,

các thư viện chúng tôi vừa nhập là NumPy,

TensorFlow, Keras và các lớp.

Việc tiếp theo chúng ta làm là đặt một hạt giống ngẫu nhiên.

Và lý do chúng tôi làm điều này là để khi bạn chạy mã này

sau này, bạn và tôi có thể nhận được kết quả tương tự

vì công cụ khởi tạo ngẫu nhiên

đang sử dụng cùng một hạt giống trong cả hai trường hợp.

Vì vậy, tôi sẽ tiếp tục và chạy nó ngay bây giờ.

Và điều đó đã được thực hiện.

Vì vậy sau khi nhập khẩu của chúng tôi

và tập hợp hạt giống của chúng tôi, bước tiếp theo là tải dữ liệu của chúng tôi.

Vì vậy, đối với hướng dẫn này, chúng ta sẽ sử dụng

tập dữ liệu MNIST, phải không?

Đây là bộ dữ liệu cổ điển trong học máy,

và nó bao gồm 70.000 hình ảnh thang màu xám

gồm các chữ số viết tay từ 0 đến 9.

Mỗi hình ảnh hoặc chữ số trong những hình ảnh này

là 28 x 28 pixel,

và tập dữ liệu đã được chia trước thành 60.000

hình ảnh đào tạo và 10.000 hình ảnh thử nghiệm.

Vì vậy, chúng ta sẽ tiếp tục nhập các hình ảnh đào tạo,

nhãn huấn luyện, hình ảnh kiểm tra và nhãn kiểm tra.

Vì vậy, khi quá trình đó hoàn tất,

được rồi, chúng ta hãy dành một chút thời gian ở đây

để hiểu dữ liệu chúng ta đang làm việc, phải không?

Vì vậy chúng ta sẽ tiếp tục và nhìn vào hình dạng

của việc huấn luyện trên các tập kiểm tra.

Và những gì chúng ta thấy ở đây là chúng ta có 60.000 hình ảnh

cho dữ liệu huấn luyện và 10.000 hình ảnh cho dữ liệu thử nghiệm.

Và bạn cũng có thể thấy rằng kích thước là 60.000,

28, 28, đại diện cho mật độ điểm ảnh

cho chính những hình ảnh đó.

Được rồi, điều tiếp theo chúng ta muốn làm ở đây

là để hình dung một số mẫu

mà chúng ta vừa kéo xuống phải không?

Vì vậy, điều chúng ta sắp làm là sử dụng matplotlib.

Trước hết chúng ta sẽ nhập gói,

và sau đó chúng ta sẽ đi qua

và chỉ lấy mẫu năm hình ảnh từ tập dữ liệu

từ tập dữ liệu huấn luyện để chúng ta thực sự có thể thấy,

hiểu được những hình ảnh này trông như thế nào.

Và vì vậy tôi sẽ tiếp tục và chạy nó.

Và ở đây chúng ta thấy hình ảnh đầu tiên

mà chúng tôi vừa kéo xuống là hình ảnh viết tay của số 5.

Và nhãn hiệu là năm,

và đây là hình ảnh trông như thế nào.

Và số tiếp theo ở đây là số không và bốn và một.

Và số chín là số cuối cùng chúng ta có ở đây.

Vì vậy, điều tiếp theo chúng tôi muốn làm bây giờ là,

nên chúng tôi hiểu rõ về những gì chúng tôi đang kéo xuống

và những gì chúng tôi đang làm việc.

Chúng tôi muốn xử lý trước dữ liệu của mình.

Vì vậy trước khi chúng tôi đưa dữ liệu vào mô hình học sâu,

chúng ta cần điều chỉnh kích thước của dữ liệu

và làm một số việc với nó, phải không?

Và điều đầu tiên chúng ta sẽ làm là làm phẳng

chính những hình ảnh đó phải không?

Đó là những hình ảnh có kích thước 28 x 28,

và chúng ta sẽ làm phẳng chúng thành một vector có kích thước 784,

đó là 28 nhân 28.

Vì vậy chúng ta sẽ làm phẳng các hình ảnh đào tạo

và cả những hình ảnh thử nghiệm.

Vì vậy, tôi sẽ tiếp tục và chạy nó để làm phẳng chúng.

Và bây giờ chúng ta đã làm phẳng các hình ảnh.

Chúng tôi muốn xem dữ liệu của chúng tôi là gì,

hình dạng của dữ liệu đó trông như thế nào.

Vì vậy, hãy chạy lại cái này.

Và bây giờ chúng ta thấy rằng thay vì 60.000, 28 x 28,

bây giờ chúng ta có 60.000 x 784.

Và đối với các bài kiểm tra, chúng tôi có 10.000 x 784.

Đó chính xác là những gì chúng tôi mong đợi.

Vì vậy, giá trị pixel trong hình ảnh

phạm vi thường từ 0 đến 255.

Mạng lưới thần kinh hoạt động tốt hơn nhiều khi các giá trị

mà chúng tôi đưa vào chúng sẽ được thu nhỏ lại trong một phạm vi nhỏ hơn,

thường nằm trong khoảng từ 0 đến 1.

Vì vậy, để đáp ứng điều này, chúng tôi muốn tiếp tục

và bình thường hóa các giá trị pixel của chúng tôi.

Vì vậy, chúng có thể rơi vào khoảng từ 0 đến 1.

Và cách chúng ta làm điều này là chia chúng cho 255.

Vì vậy, mỗi giá trị pixel sẽ được chia cho 255.

Vì vậy bây giờ chúng tôi bình thường hóa phạm vi của các giá trị.

Vì vậy, ngay bây giờ nó rơi vào khoảng từ 0 đến 1.

Vì vậy, chúng tôi tiếp tục và làm điều đó cho các hình ảnh huấn luyện

cũng như các hình ảnh thử nghiệm.

Vì vậy, tôi sẽ tiếp tục và chạy nó.

Và điều tiếp theo chúng tôi muốn làm

sau khi chúng ta hoàn tất việc chuẩn hóa

là điều chỉnh các giá trị hoặc cấu trúc của nhãn của chúng tôi.

Vì vậy, mỗi nhãn cho mỗi hình ảnh là một số nguyên

đó đi từ 0 đến 9.

Vì vậy, để phân loại nhiều lớp,

việc chuyển đổi các nhãn này thường là tiêu chuẩn

thành các vectơ được mã hóa một nóng.

mã hóa one-hot liên quan đến việc biểu diễn các biến phân loại

dưới dạng vectơ nhị phân.

Ví dụ, nếu chúng ta có nhãn bằng 0,

bây giờ nó trở thành một vectơ trong đó giá trị đầu tiên

là một và các giá trị khác bằng 0.

Hoặc nếu nhãn là chín, nó sẽ không trở thành vectơ

trong đó mọi giá trị khác bằng 0 trong khi chữ số cuối cùng là một.

Vì vậy, ở đây chúng ta có 10 giá trị có thể từ 0 đến 9.

Vì vậy chúng ta sẽ sử dụng hàm phân loại

để sửa đổi hoặc mã hóa một lần các nhãn trong tập dữ liệu của chúng tôi.

Vì vậy, hãy tiếp tục và chạy nó.

Được rồi, sau khi chúng ta làm xong việc đó,

nhãn cho tập dữ liệu của chúng tôi hiện là ma trận

hoặc vectơ có hình dạng 60.000 và 10

và lần lượt là 10.000 và 10.

Vì vậy trong video này,

chúng tôi đã nhập thành công các thư viện

và dữ liệu chúng ta cần cho deep learning.

Chúng tôi cũng đã xử lý trước dữ liệu để chuẩn bị.

Trong video tiếp theo, chúng ta sẽ tìm hiểu quá trình này

về việc xác định mô hình mà chúng tôi dự định đào tạo.

Hẹn gặp lại bạn ở một phía khác.