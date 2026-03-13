# 01 - Hãy tạo mô hình TensorFlow

---

- [Giảng viên] Trong buổi học này,

chúng ta sẽ thực hiện bước đầu tiên

xây dựng mô hình TensorFlow từ đầu.

Chúng tôi sẽ trải qua toàn bộ quá trình.

Chúng tôi sẽ đơn giản hóa nó.

Bằng cách đó chúng ta có thể bắt đầu

từ sự hiểu biết về vấn đề

để tạo và đào tạo mô hình

và hiểu cách chúng ta có thể đi

từ A đến Z.

Vậy chúng ta hãy tiếp tục

và mở môi trường không gian mã.

Và trước khi chúng ta đi sâu vào mã,

hãy hiểu những gì chúng ta đang làm ở đây

và mục tiêu là gì.

Vì vậy ở đây

chúng tôi đang cố gắng giải quyết

một vấn đề hồi quy đơn giản.

Mục đích ở đây là dự đoán

một biến mục tiêu liên tục

dựa trên một số tính năng đầu vào.

Đối với ví dụ này,

chúng tôi sẽ sử dụng bộ dữ liệu nhà ở California,

nơi mục tiêu là đơn giản.

Chúng tôi muốn dự đoán giá trị ngôi nhà trung bình

cho các quận của California

đưa ra một số tính năng như

thu nhập trung bình, dân số,

và tỷ lệ sử dụng nhà ở.

Vì vậy hãy tiếp tục và nhìn vào khung bên trái ở đây

và tìm thư mục SRC.

Và sau khi bạn tìm thấy nó,

phóng to nó

và nhấp vào tệp python 03_01_begin.

Trước khi bắt đầu, chúng ta hãy điểm qua các thư viện

mà chúng tôi có sẵn ở đây

mà chúng tôi đang sử dụng.

Đầu tiên chúng tôi gọi bộ dữ liệu dấu chấm học SK

và chúng tôi đang nhập khẩu nhà ở California.

Vì vậy, đây là điều chúng tôi làm cho phép chúng tôi

để tải tập dữ liệu nhà ở California

sau này trong mã,

đó là một tập dữ liệu hồi quy

mục tiêu là đến đâu

dự đoán, một lần nữa, giá nhà đất.

Tiếp theo chúng ta đi tiếp

và từ lựa chọn mô hình skLearn,

chúng tôi nhập chức năng phân chia thử nghiệm tàu,

đó là một tiện ích để phân chia tập dữ liệu

vào các tập huấn luyện, xác nhận và kiểm tra.

Tiếp theo, chúng ta tiếp tục và nhập

bộ chia tỷ lệ tiêu chuẩn từ SK Learn tiền xử lý.

Và bộ chia tỷ lệ tiêu chuẩn

không gì khác ngoài một công cụ

để chuẩn hóa các tính năng bằng cách loại bỏ giá trị trung bình

và chia tỷ lệ thành phương sai đơn vị.

Tiếp theo, chúng ta tiếp tục và nhập TensorFlow dưới dạng TF,

đó là một thư viện mã nguồn mở

cho học máy và học sâu

và là trọng tâm chính của khóa học của chúng tôi.

Bây giờ hãy tiếp tục tải dữ liệu và phân chia các tập dữ liệu.

Chúng tôi bắt đầu với

đang tải tập dữ liệu nhà ở California

vào một biến gọi là nhà ở,

bằng cách nói nhà ở tương đương với nhà ở California,

dấu ngoặc đơn mở và đóng.

Tiếp theo chúng ta tiếp tục và sử dụng

phần kiểm tra tàu ở đây

và chúng tôi nhập dữ liệu đó vào,

nhà ở mục tiêu đó,

và sau đó chúng tôi cho nó trạng thái ngẫu nhiên 42,

phân chia tập dữ liệu cho chúng tôi

thành tập huấn luyện đầy đủ và tập kiểm tra.

Tiếp theo chúng ta sử dụng phép chia thử nghiệm tàu ​​một lần nữa.

Lần này,

chúng tôi tiếp tục chia toàn bộ tập huấn luyện thành một

tập huấn luyện nhỏ hơn

và một bộ xác nhận.

Tiếp theo, chúng tôi tiếp tục và mở rộng quy mô tương lai.

Chúng tôi sử dụng một bộ chia tỷ lệ có tên StandardScaler.

Điều này khởi tạo đối tượng StandardScaler.

Sau đó, chúng ta tiếp tục và sử dụng hàm biến đổi phù hợp.

Điều này phù hợp với bộ chia tỷ lệ với dữ liệu huấn luyện

và biến đổi nó,

chia tỷ lệ các tính năng để có giá trị trung bình bằng 0 và phương sai một.

Sau đó chúng ta đi tiếp

và sử dụng phép biến đổi dấu chấm tỷ lệ trên dữ liệu xác thực X.

Chúng tôi gọi nó là dấu gạch dưới X hợp lệ.

Và sau đó chúng tôi sử dụng điều tương tự cho dữ liệu thử nghiệm X.

Chúng tôi sử dụng phép biến đổi dấu chấm tỷ lệ trong bài kiểm tra X

và chúng tôi gọi nó là bài kiểm tra gạch dưới X.

Vì vậy, điều này biến đổi việc xác nhận

và các bộ kiểm tra sử dụng cùng một bộ điều chỉnh tỷ lệ

đến dữ liệu huấn luyện.

Điều này đảm bảo rằng tất cả các tập dữ liệu được chia tỷ lệ theo cùng một cách.

Tiếp theo chúng ta sẽ bắt đầu và

xây dựng mô hình TensorFlow tại đây.

Để tạo chút không gian,

chúng ta có thể thu nhỏ cửa sổ bên trái

bằng cách nhấp vào biểu tượng thám hiểm ở đây.

Vì vậy, nó sẽ cung cấp cho chúng ta nhiều không gian theo chiều ngang hơn ở đây để làm việc.

Hãy tiếp tục và xác định mô hình

như TF

dấu chấm

máy ảnh

dấu chấm

tuần tự.

Đó là mô hình xếp chồng các lớp tuyến tính.

Sau đó, chúng ta tiếp tục và điền thông tin này như sau.

Vì vậy chúng ta sẽ tiếp tục và thêm một kết nối chặt chẽ

và lớp được kết nối đầy đủ với 30 nơ-ron

và kích hoạt relu.

Vì vậy, hãy tiếp tục và làm điều đó.

Chúng ta sẽ tận dụng keras ở đây

dấu chấm

lớp

chấm dày đặc,

và sau đó chúng tôi sẽ cho 30 ở đây

trong đó có 30 tế bào thần kinh.

Và sau đó chúng ta sẽ sử dụng

chức năng kích hoạt của relu.

Hãy tiếp tục và xác định hàm kích hoạt

và sau đó chúng ta sẽ nói hình dạng đầu vào bằng

X gạch dưới tàu,

và sau đó chúng ta sẽ tạo cho nó một hình dạng

trong đó chỉ định kích thước đầu vào.

Nói cách khác, số lượng

tính năng ở đây.

Vì vậy chúng ta sẽ tiếp tục và nói

một dấu hai chấm, đóng ngoặc.

Tiếp theo chúng ta sẽ thêm một lớp đầu ra chỉ với một nơ-ron.

Vì vậy, chúng tôi sẽ làm điều đó bằng cách nói TF dot keras dotlayers

chấm dày đặc.

Và sau đó, cho nó một cái

để chỉ ra rằng chúng tôi có một lớp đầu ra

với một nơ-ron đó là

thích hợp cho các nhiệm vụ hồi quy,

đó là dự đoán một giá trị liên tục duy nhất,

đó là giá nhà ở đây.

Vì vậy, khi chúng ta xác định được mô hình, việc tiếp theo chúng ta làm là gì,

chúng tôi tiếp tục và biên dịch nó.

Vì vậy, chúng tôi nói rằng, mô hình dấu chấm

biên dịch và chúng tôi sẽ cho nó tổn thất bằng giá trị trung bình

lỗi bình phương.

Và chúng ta sẽ tiếp tục

và chỉ định trình tối ưu hóa

là độ dốc giảm dần ngẫu nhiên, SGD.

Tiếp theo chúng ta sẽ tiếp tục

và tạo mô hình có lịch sử bằng với mô hình dot fit.

Và sau đó chúng ta sẽ đưa nó cho tàu X, tàu Y.

Chúng tôi sẽ đưa ra 20 kỷ nguyên ở đây

có 20 lần lặp.

Tiếp theo, chúng tôi sẽ cung cấp dữ liệu xác thực

được

Xác thực dấu gạch dưới X,

Xác thực gạch dưới Y.

Và tất cả chúng ta đã sẵn sàng. Chúng tôi vừa tạo ra lịch sử

theo mô hình dot fit.

Và tiếp theo chúng ta sẽ tiếp tục và đánh giá mô hình.

Chúng tôi sẽ chỉ định bài kiểm tra MSE,

kiểm tra lỗi bình phương trung bình,

mô hình chấm đánh giá,

và sau đó chúng tôi sẽ thực hiện bài kiểm tra gạch dưới X,

Kiểm tra gạch dưới Y.

Luôn luôn là một thực hành tốt để tiến về phía trước

và in những gì kết quả kiểm tra nói.

Vì vậy, có nghĩa là

bình phương

lỗi

trên tập thử nghiệm.

Và tiếp theo chúng ta sẽ tiếp tục

và gọi nó từ cung trên

mà chúng ta vừa tạo.

Vậy những gì chúng tôi đã làm ở đây,

chúng tôi đã tiếp tục và nhập các thư viện cần thiết.

Sau đó, chúng tôi lấy dữ liệu nhà ở ở California.

Chúng tôi đã thực hiện việc chia tách đoàn tàu thử nghiệm,

chúng tôi đã thực hiện tiêu chuẩn hóa,

và sau đó chúng tôi tiếp tục và chuẩn hóa dữ liệu của mình.

Chúng tôi đã chuẩn hóa chuỗi gạch dưới X,

X gạch dưới hợp lệ, X kiểm tra gạch dưới.

Sau đó, chúng tôi tiếp tục và tạo mô hình ở đây.

Mô hình có một lớp đầu vào

và một lớp đầu ra.

Tiếp theo, chúng tôi biên soạn mô hình.

Chúng tôi đã đưa ra hàm mất lỗi bình phương trung bình

cũng như

trình tối ưu hóa giảm độ dốc ngẫu nhiên.

Sau đó, chúng tôi tiếp tục và đào tạo mô hình ở đây

theo mô hình dot fit.

Tiếp theo, chúng tôi đánh giá mô hình

bằng sai số bình phương trung bình.

Cuối cùng, chúng tôi đã in nó.

Vì vậy, điều này sẽ giống như

không ba gạch dưới không một gạch dưới

và tập tin python.

Vì vậy hãy phóng to khung bên trái ở đây

và tiếp tục từ tập tin cuối tiếp theo.

Và sau đó chỉ cần chạy

bằng cách nhấp vào hình tam giác nhỏ

trên cửa sổ phía trên bên phải.

Vì vậy, nó sẽ trải qua 20 lần lặp như chúng ta đã xác định.

Vì vậy, sau đó, nó sẽ tiếp tục và

đưa cho chúng tôi bản in của

có nghĩa là lỗi bình phương

như chúng tôi đã nói với nó

trong chức năng.

Vậy sai số bình phương trung bình

cho vấn đề này là

0,36.

Vì vậy, trong video này, chúng ta thực hiện những bước đầu tiên

xây dựng mô hình TensorFlow

từ đầu.

Hãy tiếp tục.