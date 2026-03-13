# 03 - Phát triển hệ thống nhận dạng hình ảnh

---

- Bây giờ chúng ta đi tiếp nhé

và nói về khía cạnh quan trọng nhất,

đó là hệ thống nhận dạng hình ảnh.

Vâng, trong phần này, chúng ta sẽ tìm hiểu sâu hơn

xây dựng một hệ thống nhận dạng hình ảnh mạnh mẽ

sử dụng mạng nơ ron tích chập.

Chúng ta sẽ tiếp tục những cuộc thảo luận trước đó

và giới thiệu một mô hình CNN có hệ thống hơn

để giải quyết bộ dữ liệu CIFAR-10.

Hãy đi sâu vào và liệt kê các thành phần trong hệ thống của chúng tôi.

Thứ nhất, chúng tôi tải và xử lý trước dữ liệu.

Thứ hai, chúng ta hình dung các hình ảnh mẫu.

Thứ ba, chúng tôi xác định mô hình CNN.

Thứ tư, chúng tôi biên dịch và huấn luyện mô hình.

Số năm, lưu mô hình.

Thứ sáu, trực quan hóa độ chính xác của quá trình đào tạo và xác nhận.

Và điều thứ bảy, cuối cùng, chúng tôi đánh giá mô hình.

Hãy tiếp tục và nói về hệ thống

chi tiết hơn một chút.

Đầu tiên, như mọi khi,

chúng tôi bắt đầu bằng cách tải và xử lý trước tập dữ liệu CIFAR-10 của mình.

Điều này liên quan đến việc bình thường hóa các giá trị pixel

và chuyển đổi nhãn lớp thành các vectơ được mã hóa một lần.

Tiếp theo, chúng ta hình dung các hình ảnh mẫu.

Sau khi xử lý trước dữ liệu,

chúng tôi hình dung một số hình ảnh mẫu

để hiểu tập dữ liệu tốt hơn.

Bây giờ, xác định mô hình CNN.

Bây giờ chúng ta hãy nói về một mô hình CNN phức tạp.

Chúng ta sẽ xây dựng một mô hình có nhiều lớp chập,

các lớp tổng hợp tối đa và các lớp bỏ học

để tránh trang bị quá mức.

Đây là lời giải thích chi tiết của từng lớp.

Lớp chập đầu tiên.

Áp dụng 32 bộ lọc có kích thước 3x3 cho hình ảnh đầu vào.

Nó phát hiện các tính năng cơ bản như các cạnh và kết cấu.

Sau đó, chúng ta có lớp tổng hợp tối đa,

làm giảm kích thước, giữ lại các tính năng quan trọng.

Tiếp theo, chúng ta có lớp bỏ học,

ngăn chặn việc trang bị quá mức bằng cách không cho phép mạng

trở nên quá phụ thuộc vào bất kỳ nút nào.

Tiếp theo, chúng ta có lớp chập thứ hai

áp dụng 64 bộ lọc kích thước 3x3 cho bản đồ đặc điểm

từ lớp trước đó.

Nó phát hiện các tính năng phức tạp hơn

bằng cách kết hợp những cái đơn giản hơn được phát hiện ở lớp trước.

Tiếp theo, chúng ta có một lớp tổng hợp tối đa khác.

Nó tiếp tục làm giảm tính chiều.

Sau đó chúng ta có lớp bỏ học,

tiếp tục ngăn ngừa việc trang bị quá mức.

Tiếp theo, chúng ta có lớp dày đặc được kết nối đầy đủ

làm phẳng các bản đồ đặc trưng 2D thành vectơ 1D,

và sau đó áp dụng một lớp dày đặc với 128 nơ-ron.

Kết hợp tất cả các tính năng được phát hiện

để đưa ra quyết định phân loại cuối cùng.

Sau đó chúng ta có một lớp bỏ học khác

điều này tiếp tục ngăn ngừa việc trang bị quá mức.

Cuối cùng, chúng ta có lớp đầu ra,

có 10 nơ-ron, mỗi lớp một nơ-ron,

và sử dụng chức năng kích hoạt softmax

để đưa ra xác suất đầu ra cho mỗi lớp.

Sau khi có mô hình CNN, chúng ta tiến hành lưu mô hình.

Nếu nó đã được lưu rồi,

chúng ta tiếp tục và tải mô hình trước đó.

Cuối cùng, chúng tôi biên dịch và huấn luyện mô hình.

Nếu mô hình không tồn tại, chúng tôi biên dịch và huấn luyện mô hình.

Chúng tôi sử dụng trình tối ưu hóa Adam

và hàm mất entropy chéo phân loại,

và sau đó chúng tôi huấn luyện nó trong 20 kỷ nguyên.

Trong quá trình đào tạo, chúng tôi xác nhận mô hình

sử dụng dữ liệu thử nghiệm để theo dõi hiệu suất của nó.

Sau đó chúng ta tiếp tục và hình dung quá trình đào tạo

và biểu đồ độ chính xác xác nhận,

điều này cho chúng tôi thấy mô hình của chúng tôi đã hoạt động như thế nào.

Vâng, để tóm tắt, chúng ta có thể nói

rằng đây là những bước học sâu khá điển hình của chúng tôi.

Chúng tôi có thể gọi nó là hệ thống của chúng tôi.

Bằng cách làm theo các bước này,

chúng tôi đã tạo ra hệ thống nhận thức hình ảnh mạnh mẽ

sử dụng CNN.

Mô hình này có khả năng nhận dạng đối tượng

trong bộ dữ liệu CIFAR-10 với độ chính xác cao.

Chúng tôi cũng hình dung độ chính xác trong quá trình đào tạo và xác nhận

để đảm bảo mô hình của chúng tôi đang học tập hiệu quả.

Hãy nhớ rằng, chúng ta đang làm tất cả những điều đó mà không cần sức mạnh GPU

bởi vì chúng tôi đang làm việc với các không gian mã

với sức mạnh của CPU,

và thậm chí sau đó chúng tôi đã có mức độ chính xác khá hợp lý.

Bây giờ để tóm tắt các kỹ thuật của chúng tôi,

phần này thể hiện sức mạnh của các lớp tích chập,

lớp gộp và lớp bỏ học

trong việc xây dựng một hệ thống nhận dạng hình ảnh phức tạp.

Chà, điều gì sẽ xảy ra khi chúng ta kết hợp những kỹ thuật này?

Chúng tôi có thể nâng cao đáng kể hiệu suất

và độ tin cậy của các mô hình của chúng tôi.

Tiếp theo, hãy tiếp tục và đi sâu vào mã.

Bây giờ, hãy tiếp tục và mở tệp 03_03_begin.py.

Vì vậy đây là nơi chúng ta bắt đầu phần này,

và sau đó chúng ta sẽ đi tiếp như mọi khi

vào tệp 03_03_and.py.

Một lần nữa, chúng tôi luôn bắt đầu bằng các thư viện quan trọng

và chúng tôi vô hiệu hóa GPU do môi trường không gian mã.

Sau đó, chúng tôi tải tập dữ liệu CIFAR-10.

Chúng tôi bình thường hóa và chuẩn bị dữ liệu.

Chúng tôi chuyển đổi nhãn lớp thành các vectơ được mã hóa một lần.

Sau đó chúng tôi hiển thị hình ảnh.

Chúng tôi tiếp tục và xác định nhãn,

và đây là nơi chúng ta dừng lại trong tệp bắt đầu.

Tôi sẽ tiếp tục và xem qua hồ sơ,

điều này khá giống với các quy trình

mà chúng tôi đã và đang khám phá.

Sự khác biệt duy nhất mà chúng tôi sẽ tiếp quản

từ các phần khác là như sau.

Vì vậy, chúng tôi tạo ra một mô hình CNN đơn giản với các giải thích chi tiết

để hệ thống này được ghim chặt vào não chúng ta

ở mức độ sâu sắc hơn.

Vì vậy, đầu tiên chúng ta tạo một mô hình CNN.

Một lần nữa, chúng ta bắt đầu với một chuỗi.

Chúng tôi cung cấp lớp Conv2D trước tiên

với relu kích hoạt

và hình dạng đầu vào như chúng ta đã thảo luận.

Sau đó, chúng tôi tiếp tục và cung cấp lớp tổng hợp tối đa.

Chúng tôi cung cấp lớp bỏ học.

Chúng tôi cung cấp một lớp Conv2D khác,

theo sau là lớp tổng hợp tối đa.

Chúng tôi cung cấp cho nó một lớp bỏ học. Sau đó chúng tôi làm phẳng.

Chúng tôi tạo một lớp dày đặc, chúng tôi lại tạo một lớp bỏ đi,

và cuối cùng, chúng tôi tạo một lớp dày đặc khác.

Vì vậy, để tóm tắt, những gì chúng tôi đã làm ở đây là như sau.

Bằng cách thêm các bước này và các lớp bổ sung,

chúng tôi đã tạo ra một hệ thống nhận dạng hình ảnh mạnh mẽ bằng cách sử dụng CNN.

Mô hình này có khả năng nhận dạng đối tượng

trong bộ dữ liệu CIFAR-10 với độ chính xác cao,

và sau đó chúng tôi lại theo dõi tiếp

và xác định thư mục đầu ra, đảm bảo nó tồn tại.

Nếu không, chúng tôi tiếp tục và tạo ra nó.

Chúng tôi cung cấp đường dẫn mô hình ở đâu

và sau đó đảm bảo rằng chúng tôi đang kiểm tra

nếu mô hình đã được lưu.

Nếu không, chúng ta sẽ tiếp tục tạo và huấn luyện mô hình.

Cuối cùng, một lần nữa, như mọi khi,

chúng ta tiếp tục và lên kế hoạch đào tạo

và độ chính xác xác nhận qua các kỷ nguyên.

Chúng ta tiếp tục và cứu nó,

và điều đó kết thúc phiên hệ thống của chúng tôi.

Vì vậy, chúng ta hãy tiếp tục và chạy nó ngay bây giờ.

Vì vậy, để làm được điều đó, hãy tìm hình tam giác của bạn

và tiếp tục và chạy thử.

Nó sẽ tiếp tục và nhìn

nếu chúng ta đã lưu mô hình này trong thư mục đầu ra,

mà chúng tôi thực hiện theo mô hình hệ thống CIFAR-10,

và sau đó nó sẽ báo đã tải mô hình hiện có.

Hoàn hảo.

Vì vậy, nếu chúng ta muốn có mã này

xây dựng mô hình từ đầu,

một lần nữa, hãy tiếp tục và xóa mô hình hệ thống,

quay lại mã của bạn, đó là tệp 03_03_and.py,

và cứ thử đi

và yêu cầu nó xây dựng một mô hình hệ thống hoàn toàn mới

bắt đầu từ kỷ nguyên thứ nhất cho đến kỷ nguyên thứ 20.

Và sau đó nó sẽ tiếp tục tạo hình ảnh PNG

cho thấy độ chính xác của mô hình đã hoạt động như thế nào.

Và sau đó chúng ta cũng có thể lưu mô hình mới của mình ở đây

trong thư mục đầu ra có tên cifar10_system_model_h5.

Vì thế bây giờ có thể đi uống cà phê hoặc ăn trưa,

quay lại và xem liệu kỷ nguyên đã hoàn thành tới 20 chưa,

và sau đó nó sẽ in kết quả

và lưu mô hình vào thư mục đầu ra

trong cifar10_system_model.h5.

Được rồi, cả ba kỷ nguyên đã hoàn thành,

và chúng ta có thể kiểm tra xem nó có in các giá trị chính xác không

cũng như lưu mô hình vào thư mục đầu ra của chúng tôi,

cũng như lưu cốt truyện hiệu suất

vào thư mục đầu ra và lô.

Vì vậy, chúng ta có thể tiếp tục và xem các âm mưu

và thấy rằng cốt truyện này vừa được tạo

và chúng ta có thể thấy độ chính xác ở đây.

Đó là một cải tiến tốt so với các mô hình khác

mà chúng tôi đã và đang xây dựng,

ít liên quan hơn một chút, ít lớp hơn.

Và sau đó điều này cũng tạo ra

tệp mô hình cifar10_system_model.h5.

Vì vậy, điều này kết thúc phiên hệ thống của chúng tôi.