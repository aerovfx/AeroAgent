# 01 sklearn-to-build-optimal-process-to-build-an-ml-model

---

Các thư viện trong Python là

một công cụ hữu ích

khi chúng giảm

nỗ lực viết

mã dài để thực thi

các thuật toán phức tạp.

Trong video này, chúng tôi

sẽ giới thiệu cho bạn

một thư viện như vậy đã được

hoành tráng trong việc tạo ra Python

sự lựa chọn mặc định

cho việc học máy.

Thư viện này cũng giúp

thực hiện nhiều bước

của quy trình làm việc ML.

Chúng tôi bắt đầu với sự hiểu biết

vấn đề kinh doanh,

sau đó chúng tôi thu thập dữ liệu,

đã chuẩn bị dữ liệu

bằng cách kết hợp dữ liệu,

và xử lý các giá trị còn thiếu.

Chúng tôi cũng đã thực hiện EDA cơ bản để

hiểu và logic

chuẩn bị dữ liệu.

Bây giờ hai bước tiếp theo là

mô hình hóa và đánh giá mô hình.

Đây là nơi nổi tiếng

thư viện scikit-learn

sẽ đến giúp chúng tôi.

Scikit-learn, hoặc sklearn,

là một thư viện rất quan trọng trong

dữ liệu Python

hệ sinh thái khoa học.

Nó cung cấp các công cụ đa năng

cho việc học máy.

Nó chủ yếu được sử dụng cho

các nhiệm vụ sau:

chuẩn bị dữ liệu,

xây dựng mô hình,

và đánh giá mô hình.

Chúng ta hãy hiểu chúng từng cái một

một bắt đầu bằng

xử lý trước dữ liệu.

Xử lý trước dữ liệu

trong scikit-learn giúp

với những điều sau đây

công việc: phân chia dữ liệu,

nhân rộng dữ liệu và

mã hóa biến đổi.

Chúng ta hãy đi sâu hơn vào từng

từng nhiệm vụ này một.

Để phân chia dữ liệu, chúng tôi đã sử dụng

mô-đun lựa chọn mô hình từ

thư viện scikit-learn.

Hãy nhìn vào

mã. Phương pháp cho

phân chia dữ liệu như vậy

như train_test_split,

xác nhận chéo, v.v.

tất cả đều có sẵn trong

mô-đun lựa chọn mô hình

Tiếp theo, hãy nói về

việc mở rộng quy mô dữ liệu.

Việc chia tỷ lệ dữ liệu được sử dụng để

mang lại những tính năng

về một phạm vi chung.

Các phương pháp chia tỷ lệ khác nhau

mà chúng ta đã thảo luận là

có sẵn trước

mô-đun xử lý

của thư viện scikit-learn.

Cuối cùng, hãy nói về

mã hóa biến đổi.

Điều này phần lớn liên quan

chuyển đổi các tính năng văn bản và

biến mục tiêu để

số thích hợp

các đại diện.

Để thực hiện các thao tác này,

có những công cụ có sẵn trong

cả gấu trúc và

thư viện scikit-learn.

Hãy nhìn vào mã dưới đây.

Tiếp theo, chúng ta hãy xem

khi xây dựng một mô hình.

vở kịch Scikit-học

một vai trò rất quan trọng

trong việc đơn giản hóa việc xây dựng

của một mô hình học máy.

Thư viện có các module dành cho

hầu hết máy

mô hình học tập,

và cứu bạn khỏi

rắc rối của

viết tỉ mỉ

mã cho từng mẫu.

Đây là một mẫu trên

mã hoạt động như thế nào.

Trong trường hợp chúng tôi muốn

xây dựng mô hình KNN,

chúng tôi sẽ chỉ nhập

k-hàng xóm gần nhất

phân loại từ

mô-đun hàng xóm của

thư viện scikit-learn.

Sau khi nhập, chúng tôi

sẽ sử dụng.fit

phương pháp hỗ trợ mô hình

tìm hiểu các quy tắc từ

dữ liệu huấn luyện.

Sau đó chúng ta sẽ đơn giản sử dụng

phương thức the.predict trên

cả tàu và

dữ liệu thử nghiệm để có được

dự đoán của mô hình.

Hãy chuyển đến phần cuối cùng

nhiệm vụ quan trọng được thực hiện bởi

thư viện scikit-learn,

đánh giá mô hình.

Để đánh giá mô hình, chúng tôi

có mô-đun số liệu.

Với điều này, chúng ta có thể đánh giá

tất cả các chỉ số đánh giá

phù hợp để phân loại,

và các mô hình hồi quy như

như có nghĩa là lỗi tuyệt đối,

R^2, độ chính xác, v.v.

Đây là một mã mẫu.

Giờ đã đến.

Cuối cùng, chúng tôi sẽ mở

sổ ghi chép Jupyter của chúng tôi

trong video tiếp theo,

và tạo ra sản phẩm đầu tiên của chúng tôi

mô hình học máy

sử dụng thuật toán KNN.

Hẹn gặp bạn ở đó.