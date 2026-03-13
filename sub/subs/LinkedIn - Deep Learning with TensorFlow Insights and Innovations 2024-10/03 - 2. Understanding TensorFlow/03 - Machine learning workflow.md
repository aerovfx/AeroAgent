# 03 - Quy trình học máy

---

- [Người hướng dẫn] Bây giờ chúng ta đã học xong TensorFlow

và giao diện đơn giản hóa của nó dành cho người dùng NumPy,

bây giờ là lúc đi sâu vào quy trình làm việc của máy học.

Hãy coi nó như cuốn sách công thức nấu ăn của bạn

để tạo các dự án ML thành công,

đảm bảo bạn có một cách tiếp cận có cấu trúc

để giải quyết bất kỳ nhiệm vụ nào từ món khai vị đến món chính.

Hãy bắt đầu với bức tranh lớn,

danh sách kiểm tra dự án học máy.

Đây chính là lộ trình dẫn đến thành công của bạn.

Đầu tiên, hãy xác định vấn đề và nhìn vào bức tranh toàn cảnh.

Tiếp theo, lấy dữ liệu.

Thực hiện theo bằng cách khám phá dữ liệu để hiểu rõ hơn.

Sau đó chuẩn bị dữ liệu cho các thuật toán học máy.

Sau đó khám phá các mô hình khác nhau và đưa vào danh sách rút gọn những mô hình tốt nhất.

Sau đó, tinh chỉnh mô hình của bạn

và kết hợp chúng thành một giải pháp tuyệt vời

và trình bày giải pháp của bạn.

Cuối cùng, khởi chạy, giám sát và bảo trì hệ thống của bạn.

Hãy nhớ rằng, danh sách kiểm tra này có thể được thông qua

để phù hợp với nhu cầu và tình hình cụ thể của bạn

như trao đổi nguyên liệu dựa trên những gì trong mùa.

Bước đầu tiên trong danh sách kiểm tra là xác định vấn đề.

Điều này liên quan đến việc thu thập thông tin từ các bên liên quan

và hiểu rõ mục tiêu kinh doanh.

Ví dụ: nếu chúng ta muốn dự đoán vị trí của một quận

giá nhà trung bình, chúng ta cần biết

tại sao dự đoán này lại quan trọng.

Việc xác định mục tiêu giúp xác định mục tiêu của thuật toán

các biện pháp thực hiện và nỗ lực cần thiết.

Giống như việc biết đích đến trước khi bắt đầu một cuộc hành trình,

hoặc trong trường hợp ẩn dụ của chúng ta,

biết món ăn chúng ta muốn chuẩn bị

trước khi thu thập nguyên liệu.

Tiếp theo, chúng ta cần lấy dữ liệu.

Trong ví dụ của chúng tôi, chúng tôi sẽ sử dụng

dữ liệu giá nhà ở California

dựa trên cuộc điều tra dân số California năm 1990.

Trong trường hợp cụ thể này, nó không thành vấn đề

rằng đó là một tập dữ liệu cũ hơn một chút.

Nó phục vụ mục đích một cách hoàn hảo cho chúng tôi

để học sâu với TensorFlow.

Tập dữ liệu này đã được sửa đổi một chút

cho mục đích giảng dạy.

Hãy nhớ rằng, hiểu nguồn dữ liệu của bạn là rất quan trọng

cho bất kỳ dự án học máy nào,

giống như biết nguyên liệu của bạn đến từ đâu

trước khi bạn bắt đầu nấu ăn.

Chuyển sang khám phá dữ liệu.

Sau khi có dữ liệu, chúng tôi sẽ khám phá dữ liệu đó để hiểu rõ hơn.

Sử dụng các thư viện Python như Pandas,

chúng ta có thể nhìn vào một vài hàng đầu tiên với hàm head,

và sau đó chúng ta có thể có được cái nhìn tổng quan với chức năng thông tin

và kiểm tra số liệu thống kê bằng chức năng mô tả.

Trực quan hóa dữ liệu bằng biểu đồ

và các biểu đồ phân tán giúp xác định các mô hình và sự bất thường.

Bước này giống như kiểm tra nguyên liệu trước khi nấu,

đảm bảo mọi thứ đều tươi mới và sẵn sàng hoạt động.

Bây giờ hãy chuẩn bị dữ liệu.

Làm sạch dữ liệu là điều cần thiết.

Ví dụ: xử lý các giá trị bị thiếu

với SimpleImputer của scikit-learn.

Dữ liệu phân loại cần mã hóa,

việc này có thể được thực hiện bằng OrdinalEncode hoặc OneHotEncode.

Mã hóa phân loại không gì khác hơn là một cách nói hoa mỹ

thay đổi nhãn và danh mục thành số,

thuật toán học máy nào có thể hiểu được.

Chia tỷ lệ trong tương lai đảm bảo tất cả các thuộc tính số

có cùng quy mô, sử dụng các công cụ như StandardScaler.

Vì vậy, nếu chúng ta có một số lượng tương đối lớn

và chúng tôi có một con số rất nhỏ,

những khác biệt đó không ảnh hưởng

thuật toán học máy tiêu cực.

Sự chuẩn bị này tạo tiền đề

để học máy hiệu quả, chẳng hạn như ướp thịt

hoặc cắt rau trước khi nấu.

Với dữ liệu của chúng tôi đã sẵn sàng, chúng tôi chuyển sang chọn

và đào tạo người mẫu.

Chúng tôi bắt đầu với các mô hình đơn giản như hồi quy tuyến tính

để có được một đường cơ sở.

Sau đó thử các mô hình phức tạp hơn như cây quyết định hồi quy

hoặc Công cụ hồi quy rừng ngẫu nhiên.

Sử dụng xác thực chéo với scikit-learn's

hàm cross_val_score để đánh giá mô hình.

Điều này giống như việc thử nhiều công thức nấu ăn khác nhau để tìm ra công thức tốt nhất,

đảm bảo món ăn cuối cùng của bạn ngon miệng.

Vì vậy, sau khi chọn một mô hình, việc tinh chỉnh là rất quan trọng.

Chúng tôi sử dụng GridSearchCV để khám phá các kết hợp siêu tham số

để xem sự kết hợp nào đang hoạt động tốt nhất

để có thể chọn những cái tốt nhất

hoặc chúng tôi sử dụng RandomizedSearchCV cho không gian rộng lớn.

Chúng tôi cũng sử dụng các phương pháp tổng hợp như đóng bao, tăng cường,

hoặc xếp chồng, điều này có thể cải thiện hiệu suất hơn nữa

bằng cách kết hợp các mô hình.

Hãy coi bước này như việc điều chỉnh gia vị

để hoàn thiện món ăn của bạn, đảm bảo hương vị vừa phải.

Khi mô hình của bạn đã được tinh chỉnh,

bây giờ là lúc để trình bày giải pháp của bạn.

Tóm tắt những phát hiện của bạn,

nêu bật những gì hiệu quả và những gì không,

và nêu rõ mọi giả định và hạn chế.

Sử dụng những hình ảnh trực quan rõ ràng và những câu nói dễ nhớ.

Ví dụ: thu nhập trung bình là yếu tố dự báo số một

của giá nhà ở.

Trình bày là chìa khóa để làm cho công việc của bạn dễ hiểu

và có tác động mạnh mẽ, giống như việc bày biện món ăn của bạn thật đẹp mắt

trước khi phục vụ.

Cuối cùng, chúng tôi khởi chạy, giám sát và bảo trì hệ thống.

Triển khai mô hình của chúng tôi bằng các công cụ và nền tảng phù hợp.

Liên tục theo dõi hiệu suất của nó

và đào tạo lại khi cần thiết để đảm bảo tính chính xác liên tục.

Bảo trì hệ thống

giống như giữ cho một chiếc xe chạy êm ái

với việc kiểm tra và bảo trì thường xuyên.

Vì vậy, tuân theo quy trình học máy có cấu trúc

giúp bạn quản lý các dự án phức tạp hiệu quả hơn nhiều.

Từ việc xác định vấn đề đến việc khởi động

và duy trì hệ thống, mỗi bước đều quan trọng

để xây dựng các mô hình mạnh mẽ và đáng tin cậy.

Tiếp tục tinh chỉnh quy trình của bạn và áp dụng danh sách kiểm tra

đáp ứng nhu cầu của bạn cho các dự án học máy thành công.

Hãy nhớ rằng, đây là một ví dụ

của quy trình học máy nói chung.

Khi sử dụng TensorFlow, quy trình làm việc sẽ tương tự,

nhưng với những công cụ và phương pháp cụ thể

phù hợp với khuôn khổ của TensorFlow.

Hiểu cả quy trình làm việc chung

và các chi tiết cụ thể của TensorFlow

sẽ cung cấp cho bạn một bộ công cụ toàn diện

để giải quyết một loạt các dự án học máy.

Chúc mừng mã hóa!